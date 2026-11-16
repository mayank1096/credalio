"""Add a row of state boards (desktop + mobile wrappers that dc-import a source with props) below the lowest row.
Usage: python3 rowboards.py <canvas3/project> <spec.json> [heights.json]
spec = {"row": "row-b32", "title": "...", "boards": [[name, source, props, title], ...]}"""
import json, sys, os
D = sys.argv[1]; SP = json.load(open(sys.argv[2])); H = json.load(open(sys.argv[3])) if len(sys.argv) > 3 else {}
c = json.load(open(os.path.join(D, 'canvas.json')))
NEWK = tuple(b[0] for b in SP['boards'])
row = c['notes'].get(SP['row'])
Y = row['y'] + 300 if row else max(v['y'] + v['h'] for k, v in c['boards'].items() if not k.startswith(NEWK) and v['x'] < 39000) + 700
c['notes'][SP['row']] = {'x': 0, 'y': Y - 300, 'text': SP['title'], 'kind': 'title1', 'maxW': max(2000, len(SP['boards']) * 2150), 'page': 'main'}
W = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>%s</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
     '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">\n<style>body{margin:0}</style>\n</helmet>\n'
     '<div style="width: %s; height: %dpx; overflow: hidden; background: #FFFFFF">\n<dc-import name="%s"%s hint-size="%s,%dpx"></dc-import>\n</div>\n</x-dc>\n'
     '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":%d,"height":%d}}\'>\nclass Component extends DCLogic {\n  renderVals() { return {}; }\n}\n</script>\n</body>\n</html>\n')
x = 0
for name, src, props, title in SP['boards']:
    for suf, w, ws in [('', 1440, '100%'), ('-Mobile', 390, '390px')]:
        k = name + suf + '.dc.html'; h = H.get(k, 3000); t = title + (' · Mobile' if suf else ' · Desktop')
        open(os.path.join(D, k), 'w').write(W % (t, ws, h, src, props, ws, h, w, h))
        c['boards'][k] = {'x': x + (1520 if suf else 0), 'y': Y, 'w': w, 'h': h, 'title': t, 'page': 'main', 'expand': 'fill', 'is_interactive': True}
        if k not in c['order']: c['order'].append(k)
    x += 2150
if SP['row'] not in c.get('noteOrder', []): c.setdefault('noteOrder', []).append(SP['row'])
open(os.path.join(D, 'canvas.json'), 'w').write(json.dumps(c, indent=2, ensure_ascii=False)); print('ok', Y)
