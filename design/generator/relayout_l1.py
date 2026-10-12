# relayout_l1: re-place canvas boards in the client's Link 1 (D3Y) section/row order (desktop + mobile side by side),
# "Not done yet" notes for missing screens, then everything else below a divider (rows repacked, titles kept).
# usage: python3 relayout_l1.py <our canvas.json> <link1 canvas.json>
import json, sys, collections
ours_p, l1_p = sys.argv[1], sys.argv[2]
c = json.load(open(ours_p)); B = c['boards']; N = c['notes']
L1 = json.load(open(l1_p))
MOVED_Y = min(v['y'] for v in L1['notes'].values() if str(v.get('text', '')).startswith('MOVED'))
SKIP = {'Main', 'INVENTORY', 'CR-000', 'CreatorSetup', 'CreatorHome'}
ALIAS = {'CR-ONB-001': ('Main.dc.html', 'CR-ONB-001-Mobile.dc.html')}
SAME = {'CR-DASH-S01': 'CR-DASH-NEW'}
PW, GAP_T = 2070, 320
def mob(d): return d[:-8] + '-Mobile.dc.html'
# sticky suggestion notes follow their board
def owner(n):
    best = None
    for k, v in B.items():
        if v['x'] <= n['x'] < v['x'] + v['w'] and v['y'] < n['y'] and (best is None or v['y'] > B[best]['y']): best = k
    return best
stick = {k: (owner(v), v['x'] - B[owner(v)]['x'], v['y'] - B[owner(v)]['y']) for k, v in N.items() if v.get('kind') is None and 'text' in v and owner(v)}
titles = {k: v for k, v in N.items() if v.get('kind') == 'title1'}
rows_old = sorted({v['y'] for v in B.values()})
title_row = {}
for k, v in titles.items():
    nxt = [y for y in rows_old if y > v['y']]
    if nxt and k not in ('div-l1', 'div-l2'): title_row[k] = nxt[0]
newN = {}; placed = set(); y = 0; missing = []
def put(k, x, yy): B[k]['x'], B[k]['y'] = x, yy; placed.add(k)
# ---- Part A: Link 1 ----
secs = sorted([(v['y'], v['text'].split('\n')[0]) for v in L1['notes'].values() if v.get('x', 0) == 0 and v.get('text') and v['y'] < MOVED_Y])
lb = sorted([(v['y'], v['x'], k[:-8], v.get('title', '')) for k, v in L1['boards'].items() if v['y'] < MOVED_Y and k[:-8] not in SKIP])
for i, (sy, st) in enumerate(secs):
    ny = secs[i + 1][0] if i + 1 < len(secs) else MOVED_Y
    items = [r for r in lb if sy <= r[0] < ny]
    if not items: continue
    newN[f'l1s{i}'] = {'kind': 'title1', 'maxW': 8000, 'text': 'Link 1 · ' + st, 'w': 240, 'x': 0, 'y': y}
    y += GAP_T
    for ry in sorted({r[0] for r in items}):
        row = sorted([r for r in items if r[0] == ry], key=lambda r: r[1]); h = 820
        for j, (_, _, n, t) in enumerate(row):
            x = j * PW
            d, m = ALIAS.get(n, (n + '.dc.html', n + '-Mobile.dc.html'))
            if d in B:
                put(d, x, y); h = max(h, B[d]['h'])
                if m in B: put(m, x + 1520, y); h = max(h, B[m]['h'])
            else:
                txt = (f'Same screen as {SAME[n]}' if n in SAME else 'Not done yet') + f'\n{n} · {t}'
                newN[f'l1m-{n}'] = {'text': txt, 'x': x, 'y': y, 'w': 1440}
                if n not in SAME: missing.append(n)
        y += h + 520
# extra previews of ONB-001
ext = [k for k in ('CR-ONB-005b.dc.html', 'CR-ONB-005b-Mobile.dc.html', 'CR-ONB-001-Laptop.dc.html', 'CR-ONB-001-Tablet.dc.html', 'CR-ONB-002-9qo9.dc.html') if k in B]
if ext:
    newN['l1x'] = {'kind': 'title1', 'maxW': 8000, 'text': 'Not in Link 1: ONB-005b topics (ours) · extra previews (ONB-001 small laptop / narrow window, ONB-002 copy)', 'w': 240, 'x': 0, 'y': y}
    y += GAP_T; x = 0; h = 0
    for k in ext: put(k, x, y); x += B[k]['w'] + 80; h = max(h, B[k]['h'])
    y += h + 520
# ---- divider ----
newN['div-l1'] = {'kind': 'title1', 'maxW': 8000, 'text': '▲ End of Link 1 (client D3Y)', 'w': 240, 'x': 0, 'y': y}
newN['div-line'] = {'kind': 'title1', 'maxW': 40000, 'text': '━' * 400, 'w': 240, 'x': 0, 'y': y + 120}
newN['div-l2'] = {'kind': 'title1', 'maxW': 8000, 'text': '▼ Other screens (Studio · Link 2)', 'w': 240, 'x': 0, 'y': y + 260}
y += 260 + GAP_T + 200
SRC = sorted([k for k, v in B.items() if 'title' not in v], key=lambda k: B[k]['x'])
placed.update(SRC)
# ---- Part B: everything else, old row order ----
row_title = collections.defaultdict(list)
for k, ry in title_row.items(): row_title[ry].append(k)
for ry in rows_old:
    rest = sorted([k for k, v in B.items() if v['y'] == ry and k not in placed and not k.endswith('-Mobile.dc.html')], key=lambda k: B[k]['x'])
    rest += sorted([k for k, v in B.items() if v['y'] == ry and k not in placed and k.endswith('-Mobile.dc.html') and mob(k.replace('-Mobile', '')) and k.replace('-Mobile', '') not in B], key=lambda k: B[k]['x'])
    if not rest: continue
    for tk in row_title.get(ry, []):
        newN[tk] = dict(titles[tk], y=y)
    if row_title.get(ry): y += GAP_T
    h = 820
    for j, d in enumerate(rest):
        x = j * PW; m = mob(d)
        put(d, x, y); h = max(h, B[d]['h'])
        if m in B and m not in placed: put(m, x + 1520, y); h = max(h, B[m]['h'])
    y += h + 520
if SRC:
    newN['srcs'] = {'kind': 'title1', 'maxW': 8000, 'text': 'Component sources (not screens)', 'w': 240, 'x': 0, 'y': y}
    y += GAP_T; x = 0
    for k in SRC: B[k]['x'], B[k]['y'] = x, y; x += B[k]['w'] + 80
for k, (o, dx, dy) in stick.items():
    newN[k] = dict(N[k], x=B[o]['x'] + dx, y=B[o]['y'] + dy)
left = [k for k in B if k not in placed]
assert not left, left
c['notes'] = newN
json.dump(c, open(ours_p, 'w'), indent=2, ensure_ascii=False)
print('missing', len(missing)); print(' '.join(missing))
