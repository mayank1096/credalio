# book.py <dir with shots/> : builds shots/book.html (A4 landscape screen book) for the Landing handoff.
# Very tall pages are split into parts so every part stays readable.
import json, html, os, sys, math
from PIL import Image
S = sys.argv[1]; NAME = 'credalio-link4'; LABEL = 'Credalio · Link 4 · Course Studio · Screen book'
L = json.load(open(S + '/shots/shots.json'))
SH = S + '/shots/%s-screenshots/' % NAME; PART = S + '/shots/parts/'; os.makedirs(PART, exist_ok=True)
pairs = []; cur = None
for x in L:
    if x['lab'] == 'Desktop': cur = {'d': x, 'm': None, 'sec': x['sec'], 'title': x['title']}; pairs.append(cur)
    else: cur['m'] = x
MW, MH, MMW = 176, 150, 72  # mm: desktop box, row height, mobile box
def parts(name, n, maxw):
    """Split a screenshot into n equal horizontal parts, scaled to print size; return the relative paths."""
    im = Image.open(SH + name).convert('RGB'); w, h = im.size
    if w > maxw: im = im.resize((maxw, round(h * maxw / w)), Image.LANCZOS); w, h = im.size
    step = math.ceil(h / n); out = []
    for i in range(n):
        p = '%s.p%d.jpg' % (name[:-4], i + 1); im.crop((0, i * step, w, min(h, (i + 1) * step))).save(PART + p, quality=64, optimize=True, progressive=True); out.append('parts/' + p)
    return out
def fit(path, maxw, maxh):
    w, h = Image.open(S + '/shots/' + path).size; s = min(maxw / w, maxh / h); return w * s, h * s
pages = []
for p in pairs:
    dw, dh = Image.open(SH + p['d']['name']).size
    n = max(1, math.ceil((dh / dw) / (MH / MW * 1.25)))  # allow up to 25% shrink before splitting
    dp = parts(p['d']['name'], n, 1100); mp = parts(p['m']['name'], n, 440) if p['m'] else [None] * n
    for i in range(n): pages.append((p['sec'], p['title'] + ('' if n == 1 else '  ·  part %d of %d' % (i + 1, n)), dp[i], mp[i]))
secs = []
for i, pg in enumerate(pages):
    if not secs or secs[-1][0] != pg[0]: secs.append([pg[0], i + 3])
CSS = '''@font-face{font-family:'GS';src:url(GoogleSans-latin.woff2) format('woff2');font-weight:400 700}
@page{size:A4 landscape;margin:0}*{box-sizing:border-box}body{margin:0;font-family:'GS',system-ui;color:#0B1433}
.pg{width:297mm;height:209.8mm;position:relative;overflow:hidden;page-break-after:always;padding:16mm 16mm 14mm}
.cov{background:linear-gradient(180deg,#F5F8FF,#FFFFFF 60%);display:flex;flex-direction:column;justify-content:center;padding-left:24mm}
.cov img{width:52mm}.cov h1{font-size:30pt;font-weight:600;letter-spacing:-.02em;margin:10mm 0 4mm}.cov p{font-size:10.5pt;color:#4A5578;line-height:1.6;max-width:160mm;margin:0}
h2{font-size:15pt;font-weight:600;margin:0 0 6mm}.toc{columns:2;column-gap:14mm;font-size:9.5pt}.toc div{display:flex;justify-content:space-between;padding:2.2mm 0;border-bottom:.3mm solid #EEF1F7;break-inside:avoid}.toc span:last-child{color:#8A93AD}
.lab{font-size:8pt;color:#1652F0;font-weight:500}.ttl{font-size:13pt;font-weight:600;margin:1mm 0 5mm}
.row{display:flex;gap:8mm;align-items:flex-start;height:150mm}.dk,.mb{border:.35mm solid #E6EAF3;border-radius:3mm;overflow:hidden;background:#fff;box-shadow:0 2mm 6mm rgba(11,20,51,.06)}
.dk img,.mb img{display:block;width:100%;height:auto}.cap{font-size:7.5pt;color:#8A93AD;margin-top:2mm}
.ft{position:absolute;left:16mm;right:16mm;bottom:8mm;display:flex;justify-content:space-between;font-size:7.5pt;color:#8A93AD}'''
out = ['<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body>' % CSS]
out.append('<div class="pg cov"><img src="credalio-wordmark.png"><h1>Landing, learners &amp; pricing · Screen book</h1><p>The landing page, discovery and course, path, certificate and program pages, the journey builder, learner onboarding, the learner dashboard, checkout and pricing, and the pages for creators, institutions and validation.<br>%d screens, each shown on desktop (1440) and mobile (390), in flow order. Long pages are split into parts. Design handoff · November 2026.</p></div>' % len(pairs))
toc = ''.join('<div><span>%s</span><span>%d</span></div>' % (html.escape(s), p) for s, p in secs)
out.append('<div class="pg"><h2>Contents</h2><div class="toc">%s</div><div class="ft"><span>%s</span><span>2</span></div></div>' % (toc, LABEL))
for i, (sec, title, d, m) in enumerate(pages):
    dw, dh = fit(d, MW, MH); mob = ''
    if m:
        mw, mh = fit(m, MMW, MH)
        mob = '<div><div class="mb" style="width:%.1fmm"><img src="%s"></div><div class="cap">Mobile · 390</div></div>' % (mw, html.escape(m))
    out.append('<div class="pg"><div class="lab">%s</div><div class="ttl">%s</div><div class="row"><div><div class="dk" style="width:%.1fmm"><img src="%s"></div><div class="cap">Desktop · 1440</div></div>%s</div><div class="ft"><span>%s</span><span>%d</span></div></div>'
               % (html.escape(sec), html.escape(title), dw, html.escape(d), mob, LABEL, i + 3))
out.append('</body></html>')
open(S + '/shots/book.html', 'w').write(''.join(out)); print(len(pairs), 'screens', len(pages), 'pages', len(secs), 'sections')
