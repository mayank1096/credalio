# deliv1014: delivery cleanup. Logos referenced as blobs instead of base64 copies in 62 files; orientation check/scenario
# sources moved to the shared-sources page with titles; every shared source gets a board title. usage: python3 deliv1014.py
import re, os, json, base64
LOGO = {'canvas/project': ('/_blob/f2bdb0288176649cd148845b2c46e3ab', '/_blob/9e485e715f9869055157634fa82d3fa5'),
        'canvas2/project': ('/_blob/4b16f774b3091fed36b87721ea42cd94', '/_blob/c988a8a0ac19714cd1286a040d58e5f7')}
W = open('illustrations/credalio-wordmark.png', 'rb').read(); M = open('illustrations/credalio-mark.png', 'rb').read()
for D, (wb, mb) in LOGO.items():
    n = 0
    for f in sorted(os.listdir(D)):
        if not f.endswith('.dc.html'): continue
        p = os.path.join(D, f); s = open(p, encoding='utf-8').read()
        def rep(m):
            d = base64.b64decode(m.group(1))
            assert d in (W, M), f
            return wb if d == W else mb
        s2 = re.sub(r'data:image/png;base64,([A-Za-z0-9+/=]+)', rep, s)
        if s2 != s: open(p, 'w', encoding='utf-8').write(s2); n += 1
    print(D, 'logo files', n)
    c = json.load(open(D + '/canvas.json', encoding='utf-8'))
    for b, v in c['boards'].items():
        if not v.get('title'):
            t = re.search(r'<title>([^<]*)</title>', open(os.path.join(D, b), encoding='utf-8').read()).group(1)
            v['title'] = t.replace('&amp;', '&')
    if D == 'canvas/project':
        src = ['CR-ORI-M%d-K.dc.html' % i for i in range(1, 8)] + ['CR-ORI-M7-S.dc.html']
        for i, b in enumerate(src):
            v = c['boards'][b]; v['page'] = 'p2'; v['x'] = (i % 4) * 1520; v['y'] = 5200 + (i // 4) * 1000
        c['notes']['p2-ksrc'] = {'page': 'p2', 'x': 0, 'y': 5000, 'w': 5920, 'fill': 'gray',
            'text': 'Orientation check + scenario sources: not screens in the flow. The K1–K3 / S1–S3 boards on Link 1 show them with a variant (none / right / wrong).'}
    open(D + '/canvas.json', 'w', encoding='utf-8').write(json.dumps(c, indent=2, ensure_ascii=False))
