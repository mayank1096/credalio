# relayout_l3: re-place the Studio canvas boards in the client's Link 3 (Mg8o) section/row order
# (desktop + mobile side by side). Missing screens get a "Not done yet" note in their slot.
# Skips the client's do-not-design areas: everything below "DO NOT DESIGN ANYTHING BELOW THIS NOTE"
# and the retired manual payout row. Component sources go last.
# usage: python3 relayout_l3.py <our canvas.json> <link3 canvas.json>
import json, sys
ours_p, l3_p = sys.argv[1], sys.argv[2]
c = json.load(open(ours_p)); B = c['boards']
L3 = json.load(open(l3_p)); LN = L3['notes']
STOP_Y = min(v['y'] for v in LN.values() if 'DO NOT DESIGN ANYTHING BELOW' in str(v.get('text', '')))
SKIP = {'Main', 'INVENTORY', 'CreatorHome', 'CR-PAYO-002', 'CR-PAYO-003', 'CR-PAYO-004'}
SKIP_NOTES = {'inv', 'comps', 'row_payret'}
# client id -> our board id
MAP = {'AI-001': 'CR-NOVA-001', 'AI-002': 'CR-CREIO-002', 'AI-003': 'CR-CREIO-003', 'AI-003c': 'CR-CREIO-003c',
       'AI-004': 'CR-CREIO-004', 'AI-005': 'CR-CREIO-005', 'AI-006': 'CR-CREIO-006', 'AI-006b': 'CR-CREIO-006b',
       'AI-006c': 'CR-CREIO-006c', 'AI-006d': 'CR-CREIO-006d', 'AI-007': 'CR-CREIO-USE', 'AI-010': 'CR-CREIO-010',
       'AI-010b': 'CR-CREIO-010b', 'AI-011': 'CR-CREIO-011', 'AI-011b': 'CR-CREIO-011b', 'AI-TOP': 'CR-CREIO-TOP'}
ELSEWHERE = {'CR-SET-007': 'In the Link 1 canvas (CR-HOME-SET) · to copy here',
             'AI-012': 'In the Link 1 canvas (CR-HOME-SET) · to copy here'}
PW, GAP_T, PAGE = 2070, 320, 'p2'
def mob(d): return d[:-8] + '-Mobile.dc.html'
newN = {}; placed = set(); y = 0; missing = []; done = 0
def put(k, x, yy): B[k]['x'], B[k]['y'] = x, yy; placed.add(k)
def note(k, **kw): newN[k] = dict(kw, page=PAGE)

secs = sorted([(v['y'], v['text']) for k, v in LN.items()
               if v.get('kind') == 'title1' and v.get('x', 0) == 0 and v['y'] < STOP_Y and k not in SKIP_NOTES and v.get('text')])
lb = sorted([(v['y'], v['x'], k[:-8], v.get('title', '')) for k, v in L3['boards'].items()
             if v['y'] < STOP_Y and k[:-8] not in SKIP])
note('l3-head', kind='title1', maxW=8000, w=240, x=0, y=y,
     text='Link 3 · client order (Mg8o). "Not done yet" marks a screen still to design.')
y += GAP_T
for i, (sy, st) in enumerate(secs):
    ny = secs[i + 1][0] if i + 1 < len(secs) else STOP_Y
    items = [r for r in lb if sy <= r[0] < ny]
    if not items: continue
    note(f'l3s{i}', kind='title1', maxW=8000, w=240, x=0, y=y, text=st)
    y += GAP_T
    for ry in sorted({r[0] for r in items}):
        row = sorted([r for r in items if r[0] == ry], key=lambda r: r[1]); h = 820
        for j, (_, _, n, t) in enumerate(row):
            x = j * PW
            d = MAP.get(n, n) + '.dc.html'
            if d in B:
                put(d, x, y); h = max(h, B[d]['h']); done += 1
                if mob(d) in B: put(mob(d), x + 1520, y); h = max(h, B[mob(d)]['h'])
            else:
                head = ELSEWHERE.get(n, 'Not done yet')
                note(f'l3m-{n}', text=f'{head}\n{n} · {t}', x=x, y=y, w=1440)
                if n not in ELSEWHERE: missing.append(n)
        y += h + 520
# anything of ours the client doesn't list (should only be sources)
SRC = sorted([k for k, v in B.items() if k not in placed and 'shared source' in v.get('title', '')], key=lambda k: k)
extra = sorted([k for k in B if k not in placed and k not in SRC and not k.endswith('-Mobile.dc.html')])
if extra:
    note('l3x', kind='title1', maxW=8000, w=240, x=0, y=y, text='Ours, not in the client Link 3 list')
    y += GAP_T; h = 820
    for j, d in enumerate(extra):
        put(d, j * PW, y); h = max(h, B[d]['h'])
        if mob(d) in B: put(mob(d), j * PW + 1520, y); h = max(h, B[mob(d)]['h'])
    y += h + 520
note('srcs', kind='title1', maxW=8000, w=240, x=0, y=y, text='Component sources (not screens)')
y += GAP_T; x = 0
for k in SRC: put(k, x, y); x += B[k]['w'] + 80
left = [k for k in B if k not in placed]
assert not left, left
c['notes'] = newN
json.dump(c, open(ours_p, 'w'), indent=2, ensure_ascii=False)
print('done', done, '· missing', len(missing), '· extra', len(extra)); print(' '.join(missing))
