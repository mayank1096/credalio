import sys, json, os, subprocess
# batch.py OUT SPEC_JSON -> writes calls kb_N.js (slim jobs using stored builder), grouped under ~45k chars
OUT, spec = sys.argv[1], json.load(open(sys.argv[2]))
pre = "const AF=Object.getPrototypeOf(async function(){}).constructor;const build=new AF('PG','NAME','KEY','POS','FONTS','SV','IM','JOB',figma.root.getSharedPluginData('crd','builder'));\nconst R=[];\n"
blocks = []
for s in spec:
    k, pg, x, name, old = s['key'], s['page'], s['x'], s['name'], s.get('old', '')
    d = os.path.join(OUT, k)
    subprocess.run(['python3', 'post.py', d], check=True, capture_output=True)
    for f in os.listdir(d):
        if f.startswith('job_'): os.remove(os.path.join(d, f))
    r = subprocess.run(['python3', 'gen.py', d, pg, str(x), '0', name], check=True, capture_output=True, text=True)
    js = sorted((f for f in os.listdir(d) if f.startswith('job_')), key=lambda f: int(f[4:-3]))
    for i, j in enumerate(js):
        head = open(os.path.join(d, j)).read().split('\nconst page=')[0]
        rm = ''
        if i == 0:
            names = [n for n in {name, old} if n]
            rm = "{const _p=await figma.getNodeByIdAsync(%s);_p.children.filter(c=>%s.includes(c.name)).forEach(c=>c.remove());}\n" % (json.dumps(pg), json.dumps(names))
        blocks.append((k, i, rm + "{\n" + head + "\nR.push(await build(PG,NAME,KEY,POS,FONTS,SV,IM,JOB));\n}\n"))
calls = []; cur = ''; ks = []
for k, i, b in blocks:
    if cur and len(pre + cur + b) > 45000 and i == 0:
        calls.append((ks, cur)); cur = ''; ks = []
    cur += b; ks.append(f'{k}#{i}')
if cur: calls.append((ks, cur))
for n, (ks, c) in enumerate(calls):
    open(f'kb_{n}.js', 'w').write(pre + c + "return R;")
    print(f'kb_{n}.js', len(pre + c), ks)
