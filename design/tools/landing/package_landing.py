# package_landing.py: builds the Landing (learner-facing site) developer package zip from canvas3.
# usage (run in design/): python3 tools/landing/package_landing.py <support.js> <vendor-dir> <fonts-dir> <blobmap.json>
# blobmap.json maps each canvas image id to a file path (matched by sha256 against the canvas asset listing).
import os, re, sys, json, shutil, zipfile, csv, html
SUP, VEN, FNT, MAP = sys.argv[1:5]
D = 'canvas3/project'; H = 'handoff/landing'; NAME = 'credalio-landing'
OUT = 'handoff/build/%s-developer-package' % NAME; ZIP = '%s/%s-developer-package.zip' % (H, NAME)
TITLE = 'Credalio · Landing, learners & pricing'
shutil.rmtree('handoff/build', ignore_errors=True)
for d in ('screens/vendor', 'assets', 'fonts'): os.makedirs(os.path.join(OUT, d), exist_ok=True)
os.makedirs(H + '/assets', exist_ok=True)
c = json.load(open(D + '/canvas.json', encoding='utf-8')); B = c['boards']; N = c['notes']
files = sorted(f for f in os.listdir(D) if f.endswith('.dc.html'))
amap = json.load(open(MAP)); blobs = {}
for f in files:
    for i in re.findall(r'/_blob/([0-9a-f]{32})', open(os.path.join(D, f), encoding='utf-8').read()):
        blobs[i] = os.path.basename(amap[i])
for i, n in blobs.items():
    shutil.copy(amap[i], os.path.join(OUT, 'assets', n)); shutil.copy(amap[i], os.path.join(H, 'assets', n))
for f in os.listdir(FNT): shutil.copy(os.path.join(FNT, f), os.path.join(OUT, 'fonts', f))
shutil.copy(SUP, os.path.join(OUT, 'screens', 'support.js'))
for v in os.listdir(VEN): shutil.copy(os.path.join(VEN, v), os.path.join(OUT, 'screens', 'vendor', v))
FONTLINK = re.compile(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com/css2\?family=Google\+Sans[^"]*">')
for f in files:
    s = open(os.path.join(D, f), encoding='utf-8').read()
    s = re.sub(r'/_blob/([0-9a-f]{32})', lambda m: '../assets/' + blobs[m.group(1)], s)
    s = FONTLINK.sub('<link rel="stylesheet" href="../fonts/google-sans.css">', s)
    s = s.replace('<script src="./support.js"></script>', '<script src="./vendor/react.js"></script><script src="./vendor/react-dom.js"></script><script src="./support.js"></script>')
    open(os.path.join(OUT, 'screens', f), 'w', encoding='utf-8').write(s)
# sections = the 5 canvas columns; groups = the rows under them (row notes), in canvas order
cols = sorted((v['x'], re.sub(r'^\d+ · ', '', v['text'])) for k, v in N.items() if k.startswith('col-'))
colof = lambda x: max(i for i, (cx, _) in enumerate(cols) if cx <= x)
rown = [(k, v) for k, v in N.items() if k.startswith('row-')]
WIDE = {'row-b29', 'row-b30', 'row-b31', 'row-b32', 'row-b33'}  # bottom rows run across all columns
def rowof(b):
    best = None
    for k, v in rown:
        ok = colof(v['x']) == colof(b['x']) or k in WIDE
        if ok and v['y'] <= b['y'] and (best is None or v['y'] > best[1]['y']): best = (k, v)
    return best[1]
clean = lambda t: re.sub(r'\s*\([^)]*\)?', '', re.sub(r'^Batch \d+ · ', '', t)).replace(' · complete', '').strip()
def key(b):
    r = rowof(B[b]); return (colof(r['x']), r['y'], B[b]['y'], B[b]['x'])
order = sorted((b for b in B if not b.endswith('-Mobile.dc.html')), key=key)
rows = []
for b in order:
    s = open(os.path.join(D, b), encoding='utf-8').read()
    m = re.search(r'<dc-import name="([^"]+)"([^>]*)>', s)
    mob = b.replace('.dc.html', '-Mobile.dc.html')
    srcf = (m.group(1) + '.dc.html') if m else b
    props = ' '.join(p for p in re.findall(r'(\w[\w-]*="[^"]*")', m.group(2)) if not p.startswith('hint-size')) if m else ''
    links = sorted(set(re.findall(r'href="([A-Za-z][^"#{:]*\.dc\.html)"', open(os.path.join(D, srcf), encoding='utf-8').read())))
    r = rowof(B[b])
    t = re.sub(r' · Desktop$', '', B[b].get('title', b))
    rows.append(dict(title=t, desk=b, mob=mob if mob in B else '', src=srcf, var=props, kind='screen',
                     sec=cols[colof(r['x'])][1], grp=clean(r['text']), links=' '.join(l for l in links if l != srcf)))
for f in files:
    if f not in B: rows.append(dict(title=f[:-8] + ' (shared source)', desk=f, mob='', src=f, var='', kind='shared source', sec='Shared sources', grp='', links=''))
json.dump(rows, open('handoff/build/rows.json', 'w'), indent=1)
with open(os.path.join(OUT, 'screens.csv'), 'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh); w.writerow(['section', 'group', 'title', 'desktop board', 'mobile board', 'source file', 'props', 'kind', 'links to'])
    for r in rows: w.writerow([r['sec'], r['grp'], r['title'], r['desk'], r['mob'], r['src'], r['var'], r['kind'], r['links']])
tr = []; last = lastg = None
for r in rows:
    if r['sec'] != last:
        tr.append('<tr><th colspan="3" class="s">%s</th></tr>' % html.escape(r['sec'] + (' (imported by the boards above with props)' if r['kind'] != 'screen' else ''))); last = r['sec']; lastg = None
    if r['grp'] and r['grp'] != lastg:
        tr.append('<tr><th colspan="3" class="g">%s</th></tr>' % html.escape(r['grp'])); lastg = r['grp']
    tr.append('<tr><td>%s</td><td><a href="screens/%s">Desktop</a></td><td>%s</td></tr>' % (html.escape(r['title']), r['desk'], ('<a href="screens/%s">Mobile</a>' % r['mob']) if r['mob'] else ''))
n = sum(1 for r in rows if r['kind'] == 'screen')
open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write('''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>%s</title>
<link rel="stylesheet" href="fonts/google-sans.css"><style>body{margin:0;padding:32px 24px;font-family:'Google Sans',system-ui,sans-serif;color:#0B1433;background:#F7F9FD}main{max-width:980px;margin:0 auto}
h1{font-weight:600;letter-spacing:-.02em}p{color:#4A5578;line-height:1.6}table{width:100%%;border-collapse:collapse;background:#fff;border:1.5px solid #E6EAF3;border-radius:16px;overflow:hidden}
th{text-align:left;background:#fff}th.s{padding:22px 16px 6px;font-size:17px;color:#0B1433;font-weight:600}th.g{padding:12px 16px 4px;font-size:12.5px;color:#8A93AD;font-weight:600}
td{padding:9px 16px;border-top:1px solid #EEF1F7;font-size:14.5px}a{color:#1652F0;text-decoration:none;font-weight:500}</style></head>
<body><main><h1>%s</h1><p>%d screens, each with a desktop (1440) and mobile (390) board, in flow order, plus %d shared sources. Serve this folder over http to open them (see README).</p><table>%s</table></main></body></html>''' % (TITLE, TITLE, n, len(rows) - n, ''.join(tr)))
shutil.copy(H + '/README.md', os.path.join(OUT, 'README.md'))
shutil.copytree(H + '/tokens', os.path.join(OUT, 'tokens'))
with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, _, fs in os.walk(OUT):
        for f in sorted(fs):
            p = os.path.join(root, f); z.write(p, os.path.relpath(p, 'handoff/build'))
print(n, 'screens', len(rows) - n, 'sources', len(set(blobs.values())), 'images', os.path.getsize(ZIP) // 1024, 'KB')
