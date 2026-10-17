# package.py: builds the Link 1 developer handoff zip (screens runnable offline, images, fonts, index, guide).
# usage: python3 tools/package.py <support.js> <vendor-dir> <fonts-dir with gs.css + map.txt> <blob-dir> [<board prefix> <package name> <readme> <index title>]   (run in design/)
# The optional args build a package for a subset of boards only (e.g. CR-LOG- credalio-link1-login handoff/login/README.md).
import os, re, sys, json, shutil, hashlib, zipfile, csv, html
SUP, VEN, FNT, BLOB = sys.argv[1:5]
PRE, NAME, README, TITLE = sys.argv[5:9] if len(sys.argv) > 5 else ('', 'credalio-link1', 'handoff/README.md', 'Credalio · Link 1 screens')
D = 'canvas/project'; OUT = 'handoff/build/%s-developer-package' % NAME; ZIP = os.path.join(os.path.dirname(README), '%s-developer-package.zip' % NAME)
shutil.rmtree('handoff/build', ignore_errors=True)
for d in ('screens', 'assets', 'fonts', 'screens/vendor'): os.makedirs(os.path.join(OUT, d), exist_ok=True)
md5 = lambda p: hashlib.md5(open(p, 'rb').read()).hexdigest()
ill = {md5('handoff/assets/' + f): f for f in os.listdir('handoff/assets')}
c = json.load(open(D + '/canvas.json', encoding='utf-8'))
files = [f for f in sorted(os.listdir(D)) if f.endswith('.dc.html') and f.startswith(PRE)]
# images: /_blob/<id> -> ../assets/<name>
blobs = {}
for f in files:
    for i in re.findall(r'/_blob/([0-9a-f]{32})', open(os.path.join(D, f), encoding='utf-8').read()):
        if i not in blobs:
            name = ill.get(md5(os.path.join(BLOB, i)))
            assert name, ('unknown image', i, f)
            blobs[i] = name
for name in set(blobs.values()): shutil.copy('handoff/assets/' + name, os.path.join(OUT, 'assets', name))
# fonts: Google Sans (variable, latin + latin-ext), local copy + css
fm = dict(l.split(' ') for l in open(os.path.join(FNT, 'map.txt')).read().split('\n') if l.strip())
blocks = re.findall(r'/\* (latin(?:-ext)?) \*/\s*(@font-face \{.*?\})', open(os.path.join(FNT, 'gs.css')).read(), re.S)
fcss = []
for sub, b in blocks:
    url = re.search(r'url\((https://[^)]+)\)', b).group(1); fn = 'GoogleSans-%s.woff2' % sub
    shutil.copy(os.path.join(FNT, fm[url]), os.path.join(OUT, 'fonts', fn))
    fcss.append('/* %s */\n' % sub + b.replace(url, fn))
open(os.path.join(OUT, 'fonts', 'google-sans.css'), 'w').write('\n'.join(fcss) + '\n')
# screens: offline-runnable copies
shutil.copy(SUP, os.path.join(OUT, 'screens', 'support.js'))
for v in os.listdir(VEN): shutil.copy(os.path.join(VEN, v), os.path.join(OUT, 'screens', 'vendor', v))
FONTLINK = re.compile(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com/css2\?family=Google\+Sans[^"]*">')
for f in files:
    s = open(os.path.join(D, f), encoding='utf-8').read()
    s = re.sub(r'/_blob/([0-9a-f]{32})', lambda m: '../assets/' + blobs[m.group(1)], s)
    s = FONTLINK.sub('<link rel="stylesheet" href="../fonts/google-sans.css">', s)
    s = s.replace('<script src="./support.js"></script>', '<script src="./vendor/react.js"></script><script src="./vendor/react-dom.js"></script><script src="./support.js"></script>')
    open(os.path.join(OUT, 'screens', f), 'w', encoding='utf-8').write(s)
# index: boards in canvas order (page 1 by row, then shared sources)
B = c['boards']; notes = c['notes']
def key(b): v = B[b]; return (0 if v.get('page') == 'p1' else 1, v['y'], v['x'])
rows = []
for b in sorted(B, key=key):
    if b.endswith('-Mobile.dc.html') or b not in files: continue
    s = open(os.path.join(D, b), encoding='utf-8').read()
    m = re.search(r'<dc-import name="([^"]+)"(?: variant="([^"]+)")?', s)
    mob = b.replace('.dc.html', '-Mobile.dc.html')
    links = sorted(set(re.findall(r'href="(CR-[^"#{]+\.dc\.html|Main\.dc\.html)"', open(os.path.join(D, (m.group(1) + '.dc.html') if m else b), encoding='utf-8').read())))
    rows.append([B[b].get('title', b), b, mob if mob in B else '', (m.group(1) + '.dc.html') if m else b, (m.group(2) or '') if m else '',
                 'shared source' if B[b].get('page') == 'p2' else 'screen', ' '.join(links)])
with open(os.path.join(OUT, 'screens.csv'), 'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh); w.writerow(['title', 'desktop board', 'mobile board', 'source file', 'variant', 'kind', 'links to']); w.writerows(rows)
sec = sorted([(v['y'], v.get('text', '')) for v in notes.values() if v.get('page') == 'p1' and v.get('text', '').startswith('Link 1 ·')])
def section(y):
    t = ''
    for sy, st in sec:
        if sy <= y: t = st
    return t
tr = []; last = None
for r in rows:
    if r[5] == 'screen':
        s = section(B[r[1]]['y'])
        if s != last: tr.append('<tr><th colspan="3">%s</th></tr>' % html.escape(s.replace('Link 1 · ', ''))); last = s
    elif last != 'src':
        tr.append('<tr><th colspan="3">Shared sources (imported by the boards above with a variant)</th></tr>'); last = 'src'
    tr.append('<tr><td>%s</td><td><a href="screens/%s">Desktop</a></td><td>%s</td></tr>' % (html.escape(r[0]), r[1], ('<a href="screens/%s">Mobile</a>' % r[2]) if r[2] else ''))
open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write('''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>%s</title>
<link rel="stylesheet" href="fonts/google-sans.css"><style>body{margin:0;padding:32px 24px;font-family:'Google Sans',system-ui,sans-serif;color:#0B1433;background:#F7F9FD}main{max-width:980px;margin:0 auto}
h1{font-weight:600;letter-spacing:-.02em}p{color:#4A5578;line-height:1.6}table{width:100%%;border-collapse:collapse;background:#fff;border:1.5px solid #E6EAF3;border-radius:16px;overflow:hidden}
th{text-align:left;padding:18px 16px 8px;font-size:13px;color:#8A93AD;font-weight:600;background:#fff}td{padding:9px 16px;border-top:1px solid #EEF1F7;font-size:14.5px}a{color:#1652F0;text-decoration:none;font-weight:500}</style></head>
<body><main><h1>%s</h1><p>%d boards. Open each screen in a browser served over http (see README). Desktop boards are 1440 wide, mobile boards 390; each screen is one responsive file.</p><table>%s</table></main></body></html>''' % (TITLE, TITLE, len(rows), ''.join(tr)))
shutil.copy(README, os.path.join(OUT, 'README.md'))
shutil.copytree('handoff/tokens', os.path.join(OUT, 'tokens'))
with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, _, fs in os.walk(OUT):
        for f in fs:
            p = os.path.join(root, f); z.write(p, os.path.relpath(p, 'handoff/build'))
print(len(files), 'screens', len(set(blobs.values())), 'images', len(blocks), 'font files', os.path.getsize(ZIP) // 1024, 'KB')
