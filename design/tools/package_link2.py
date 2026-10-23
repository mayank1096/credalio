# package_link2.py: builds the Link 2 (Creator Studio) developer package zip from canvas2.
# usage: python3 tools/package_link2.py <support.js> <vendor-dir> <fonts-dir with google-sans.css + woff2>   (run in design/)
import os, re, sys, json, shutil, zipfile, csv, html, hashlib
SUP, VEN, FNT = sys.argv[1:4]
D = 'canvas2/project'; H = 'handoff/link2'; NAME = 'credalio-link2'
OUT = 'handoff/build/%s-developer-package' % NAME; ZIP = '%s/%s-developer-package.zip' % (H, NAME)
TITLE = 'Credalio · Link 2 · Creator Studio'
SECTIONS = ['Credit Wallet', 'Payments & revalidation', 'Earnings & payouts', 'Course overview & discussions',
            'Calendar & availability', 'Learner support, learners & analytics', 'Creator profile & organizations', 'Settings',
            'Nova panel, search & help', 'Nova & Creio', 'Creio · topping up', 'Creio · usage & alerts', 'Account menu', 'Message pop-ups']
shutil.rmtree('handoff/build', ignore_errors=True)
for d in ('screens/vendor', 'assets', 'fonts'): os.makedirs(os.path.join(OUT, d), exist_ok=True)
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
c = json.load(open(D + '/canvas.json', encoding='utf-8')); B = c['boards']; N = c['notes']
files = sorted(f for f in os.listdir(D) if f.endswith('.dc.html'))
amap = json.load(open(sys.argv[4])) if len(sys.argv) > 4 else {}
blobs = {}
for f in files:
    for i in re.findall(r'/_blob/([0-9a-f]{32})', open(os.path.join(D, f), encoding='utf-8').read()):
        blobs[i] = os.path.basename(amap[i])
for n in set(blobs.values()): shutil.copy(os.path.join(H, 'assets', n), os.path.join(OUT, 'assets', n))
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
# order: section notes (l3s0..l3s13) by y, boards by row then x; shared sources last
secs = sorted((v['y'], int(k[3:])) for k, v in N.items() if re.fullmatch(r'l3s\d+', k))
def section(y):
    t = None
    for sy, i in secs:
        if sy <= y: t = SECTIONS[i]
    return t
src = lambda b: 'shared source' in B[b].get('title', '')
order = sorted((b for b in B if not b.endswith('-Mobile.dc.html')), key=lambda b: (src(b), B[b]['y'], B[b]['x']))
rows = []
for b in order:
    s = open(os.path.join(D, b), encoding='utf-8').read()
    m = re.search(r'<dc-import name="([^"]+)"(?: variant="([^"]+)")?', s)
    mob = b.replace('.dc.html', '-Mobile.dc.html')
    srcf = (m.group(1) + '.dc.html') if m else b
    links = sorted(set(re.findall(r'href="(CR-[^"#{]+\.dc\.html)"', open(os.path.join(D, srcf), encoding='utf-8').read())))
    t = re.sub(r' · Desktop$', '', B[b].get('title', b))
    rows.append(dict(title=t, desk=b, mob=mob if mob in B else '', src=srcf, var=(m.group(2) or '') if m else '',
                     kind='shared source' if src(b) else 'screen', sec='Shared sources' if src(b) else section(B[b]['y']), links=' '.join(links)))
json.dump(rows, open('handoff/build/rows.json', 'w'), indent=1)
with open(os.path.join(OUT, 'screens.csv'), 'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh); w.writerow(['section', 'title', 'desktop board', 'mobile board', 'source file', 'variant', 'kind', 'links to'])
    for r in rows: w.writerow([r['sec'], r['title'], r['desk'], r['mob'], r['src'], r['var'], r['kind'], r['links']])
tr = []; last = None
for r in rows:
    if r['sec'] != last:
        tr.append('<tr><th colspan="3">%s</th></tr>' % html.escape(r['sec'] + (' (imported by the boards above with a variant)' if r['kind'] != 'screen' else ''))); last = r['sec']
    tr.append('<tr><td>%s</td><td><a href="screens/%s">Desktop</a></td><td>%s</td></tr>' % (html.escape(r['title']), r['desk'], ('<a href="screens/%s">Mobile</a>' % r['mob']) if r['mob'] else ''))
n = sum(1 for r in rows if r['kind'] == 'screen')
open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write('''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>%s</title>
<link rel="stylesheet" href="fonts/google-sans.css"><style>body{margin:0;padding:32px 24px;font-family:'Google Sans',system-ui,sans-serif;color:#0B1433;background:#F7F9FD}main{max-width:980px;margin:0 auto}
h1{font-weight:600;letter-spacing:-.02em}p{color:#4A5578;line-height:1.6}table{width:100%%;border-collapse:collapse;background:#fff;border:1.5px solid #E6EAF3;border-radius:16px;overflow:hidden}
th{text-align:left;padding:18px 16px 8px;font-size:13px;color:#8A93AD;font-weight:600;background:#fff}td{padding:9px 16px;border-top:1px solid #EEF1F7;font-size:14.5px}a{color:#1652F0;text-decoration:none;font-weight:500}</style></head>
<body><main><h1>%s</h1><p>%d screens, each with a desktop (1440) and mobile (390) board, in flow order, plus %d shared sources. Serve this folder over http to open them (see README).</p><table>%s</table></main></body></html>''' % (TITLE, TITLE, n, len(rows) - n, ''.join(tr)))
shutil.copy(H + '/README.md', os.path.join(OUT, 'README.md'))
shutil.copytree(H + '/tokens', os.path.join(OUT, 'tokens'))
with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, _, fs in os.walk(OUT):
        for f in sorted(fs):
            p = os.path.join(root, f); z.write(p, os.path.relpath(p, 'handoff/build'))
print(n, 'screens', len(rows) - n, 'sources', len(set(blobs.values())), 'images', os.path.getsize(ZIP) // 1024, 'KB')
