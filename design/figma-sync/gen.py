#!/usr/bin/env python3
"""gen.py <screen_dir> <page_id> <x> <y> <frame name> -> writes <screen_dir>/job_N.js"""
import json, sys, os, glob
D, PG, X, Y, NAME = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
KEY = os.path.basename(D.rstrip('/'))
B = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'builder.js')).read()
tree = json.load(open(os.path.join(D, 'c.json')))
BUDGET = int(os.environ.get('BUDGET', 40000))
WS = {300: 'Light', 400: 'Regular', 500: 'Medium', 600: 'SemiBold', 700: 'Bold', 800: 'ExtraBold'}
def sty(w, i):
    s = WS.get(w) or ('Bold' if w >= 650 else 'SemiBold' if w >= 550 else 'Medium' if w >= 450 else 'Regular')
    return ('Italic' if s == 'Regular' else s + ' Italic') if i else s
J = lambda o: json.dumps(o, separators=(',', ':'), ensure_ascii=False)
size = lambda n: len(J(n))
jobs = []
def kids(n): return n[7] if n[0] == 'F' and len(n) > 7 else []
def off(n): return 1 if n[6].get('si') else 0
def pack(path, parent, children, root_shell=None):
    cur = []; sz = 0; start = off(parent); deferred = []
    first = True
    def flush(final=False):
        nonlocal cur, sz, start, first
        if root_shell is not None and first:
            jobs.append({'root': root_shell[:7] + [cur]})
        else:
            jobs.append({'path': path, 'start': start, 'nodes': cur})
        start += len(cur); cur = []; sz = 0; first = False
    for i, c in enumerate(children):
        s = size(c)
        if s > BUDGET and c[0] == 'F':
            shell = c[:7] + [[]]
            s = size(shell)
            if sz + s > BUDGET and cur: flush()
            idx = start + len(cur)
            cur.append(shell); sz += s
            deferred.append((path + [idx], c))
            continue
        if sz + s > BUDGET and cur: flush()
        cur.append(c); sz += s
    if cur or first: flush()
    for p2, c in deferred:
        pack(p2, c, kids(c))
pack([], tree, kids(tree), root_shell=tree)
for f in glob.glob(os.path.join(D, 'job_*.js')): os.remove(f)
out = []
for i, jb in enumerate(jobs):
    js = J(jb)
    # svg dedupe
    svs = []
    def walk(n):
        if n[0] == 'S' and isinstance(n[6].get('v'), str):
            v = n[6]['v']
            if v not in svs: svs.append(v)
            n[6]['v'] = svs.index(v)
        for c in kids(n): walk(c)
    for n in ([jb['root']] if 'root' in jb else jb['nodes']): walk(n)
    ws = {int(w) for w in __import__('re').findall(r'"w":(\d+)', J(jb))} | {400}
    fonts = sorted({sty(w, 0) for w in ws} | ({sty(w, 1) for w in ws} if '"i":1' in J(jb) else set()))
    head = f"const PG={J(PG)},NAME={J(NAME)},KEY={J(KEY)},POS={J([X,Y])},FONTS={J(fonts)};\nconst SV={J(svs)};\nconst JOB={J(jb)};\n"
    code = head + B
    p = os.path.join(D, f'job_{i}.js'); open(p, 'w').write(code); out.append((p, len(code)))
for p, l in out: print(p, l)
