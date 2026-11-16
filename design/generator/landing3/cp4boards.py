"""Landing batch 4: CareerPaths-Compare (+Mobile) board (comparison open) in a new row, placed below the lowest row.
Usage: python3 cp4boards.py <canvas3/project> [heights.json]"""
import json, sys, os
D = sys.argv[1]; H = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else {}
c = json.load(open(os.path.join(D, 'canvas.json')))
src = open(os.path.join(D, 'CareerPaths-Mobile.dc.html')).read()
NEW = ('CareerPaths-Compare', 'CareerPaths-Compare-Mobile')
Y = max(v['y'] + v['h'] for k, v in c['boards'].items() if not k.startswith(NEW) and v['x'] < 39000) + 700
c['notes']['row-b30'] = {'x': 0, 'y': Y - 300, 'text': 'Batch 30 · Career paths: comparing two paths', 'kind': 'title1', 'maxW': 2000, 'page': 'main'}
for k, w, x, title in [('CareerPaths-Compare', 1440, 0, 'PATH-001 Career Paths · Comparing two paths'), ('CareerPaths-Compare-Mobile', 390, 1520, 'PATH-001 Career Paths · Comparing two paths · Mobile')]:
    f = k + '.dc.html'; h = H.get(f, 3000); ws = '100%' if w > 600 else '390px'
    t = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>%s</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">\n<style>body{margin:0}</style>\n</helmet>\n'
         '<div style="width: %s; height: %dpx; overflow: hidden; background: #FFFFFF">\n<dc-import name="CareerPaths" view="compare" hint-size="%s,%dpx"></dc-import>\n</div>\n</x-dc>\n'
         '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":%d,"height":%d}}\'>\nclass Component extends DCLogic {\n  renderVals() { return {}; }\n}\n</script>\n</body>\n</html>\n') % (title, ws, h, ws, h, w, h)
    open(os.path.join(D, f), 'w').write(t)
    c['boards'][f] = {'x': x, 'y': Y, 'w': w, 'h': h, 'title': title, 'page': 'main', 'expand': 'fill', 'is_interactive': True}
    if f not in c['order']: c['order'].append(f)
if 'row-b30' not in c.get('noteOrder', []): c.setdefault('noteOrder', []).append('row-b30')
open(os.path.join(D, 'canvas.json'), 'w').write(json.dumps(c, indent=2, ensure_ascii=False)); print('ok', Y)
