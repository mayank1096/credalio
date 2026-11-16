"""Landing batch 5: certificate state boards (eligibility result, enrolled, certified) in a new row below the lowest row.
Usage: python3 cd5boards.py <canvas3/project> [heights.json]"""
import json, sys, os
D = sys.argv[1]; H = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else {}
c = json.load(open(os.path.join(D, 'canvas.json')))
B = [('CertDetail-Meets', 'CertDetail', ' elig="meets"', 'CERT-002 Certification Detail · Eligibility: meets the requirements'),
     ('CertDetail-Needs', 'CertDetail', ' elig="needs"', 'CERT-002 Certification Detail · Eligibility: evidence needed'),
     ('CertDetail-Not', 'CertDetail', ' elig="not"', 'CERT-002 Certification Detail · Eligibility: not yet eligible'),
     ('CertDetail-Enrolled', 'CertDetail', ' elig="enrolled"', 'CERT-002 Certification Detail · Enrolled, in progress'),
     ('CertDetail-Done', 'CertDetail', ' elig="done"', 'CERT-002 Certification Detail · Certified'),
     ('Certifications-Compare', 'Certifications', ' view="compare"', 'CERT-001 Certifications · Comparing two certifications')]
NEWK = tuple(n for n, _, _, _ in B)
row = c['notes'].get('row-b31')
Y = row['y'] + 300 if row else max(v['y'] + v['h'] for k, v in c['boards'].items() if not k.startswith(NEWK) and v['x'] < 39000) + 700
c['notes']['row-b31'] = {'x': 0, 'y': Y - 300, 'text': 'Batch 31 · Professional certificates: eligibility results, enrolled, certified, and comparing', 'kind': 'title1', 'maxW': 10000, 'page': 'main'}
W = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>%s</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
     '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">\n<style>body{margin:0}</style>\n</helmet>\n'
     '<div style="width: %s; height: %dpx; overflow: hidden; background: #FFFFFF">\n<dc-import name="%s"%s hint-size="%s,%dpx"></dc-import>\n</div>\n</x-dc>\n'
     '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":%d,"height":%d}}\'>\nclass Component extends DCLogic {\n  renderVals() { return {}; }\n}\n</script>\n</body>\n</html>\n')
x = 0
for name, src, props, title in B:
    for suf, w, ws in [('', 1440, '100%'), ('-Mobile', 390, '390px')]:
        k = name + suf + '.dc.html'; h = H.get(k, 3000); t = title + (' · Mobile' if suf else ' · Desktop')
        open(os.path.join(D, k), 'w').write(W % (t, ws, h, src, props, ws, h, w, h))
        c['boards'][k] = {'x': x + (1520 if suf else 0), 'y': Y, 'w': w, 'h': h, 'title': t, 'page': 'main', 'expand': 'fill', 'is_interactive': True}
        if k not in c['order']: c['order'].append(k)
    x += 2150
if 'row-b31' not in c.get('noteOrder', []): c.setdefault('noteOrder', []).append('row-b31')
open(os.path.join(D, 'canvas.json'), 'w').write(json.dumps(c, indent=2, ensure_ascii=False)); print('ok', Y)
