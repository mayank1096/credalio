"""Build project/canvas.json for the Link 4 canvas from the batch board lists and measured heights.

Usage: python3 layout.py heights.json   (heights.json: {code: [desktop_h, mobile_h]})
Each row: title note, then desktop + mobile pairs left to right. Shared sources sit in the last row.
"""
import json, os, sys
from l4kit import OUT
import stu1

PAIR, GAP, ROWGAP = 1440 + 80 + 390, 160, 420
H = json.load(open(sys.argv[1]))
T = {c: t for c, _, _, t in stu1.BOARDS}

ROWS = [
    ('b1-setup', 'Batch 1 · Course setup: format, delivery, review, how you’ll create it, Studio welcome', ['STU-001', 'STU-002', 'STU-003', 'STU-004', 'STU-008']),
    ('b1-design-a', 'Batch 1 · Course design: Studio home, basics, audience, career & skills', ['STU-009', 'STU-010', 'STU-011', 'STU-012', 'STU-012b', 'STU-013']),
    ('b1-design-b', 'Batch 1 · Course design: outcomes, skills map, evidence, assessment & award, effort, summary', ['STU-014', 'STU-015', 'STU-016', 'STU-017', 'STU-018', 'STU-019']),
]
SOURCES = [('Setup.dc.html', 'Course setup · shared source'), ('Studio.dc.html', 'Course Studio · shared source')]

boards, order, notes = {}, [], {}
y = 300
for nid, text, codes in ROWS:
    notes[nid] = {'x': 0, 'y': y - 300, 'text': text, 'kind': 'title1', 'maxW': len(codes) * (PAIR + GAP) - GAP}
    notes[nid + '-new'] = {'x': 0, 'y': y - 150, 'text': 'NEW · batch 1', 'w': 260, 'fill': 'pink'}
    x, mh = 0, 0
    for c in codes:
        hd, hm = H[c]
        for name, w, h, sx in [(c + '.dc.html', 1440, hd, x), (c + '-Mobile.dc.html', 390, hm, x + 1520)]:
            boards[name] = {'x': sx, 'y': y, 'w': w, 'h': h, 'title': T[c] + (' · Desktop' if w > 600 else ' · Mobile'),
                            'page': 'main', 'is_interactive': True, 'expand': 'fill'}
            order.append(name)
        mh = max(mh, hd, hm)
        x += PAIR + GAP
    y += mh + ROWGAP
notes['sources'] = {'x': 0, 'y': y - 300, 'text': 'Shared sources (code the boards above import, not screens)', 'kind': 'title1', 'maxW': 3200}
x = 0
for name, title in SOURCES:
    boards[name] = {'x': x, 'y': y, 'w': 1440, 'h': 900, 'title': title, 'page': 'main', 'is_interactive': True, 'expand': 'fill'}
    order.append(name); x += 1440 + GAP

p = os.path.join(OUT, 'canvas.json')
old = json.load(open(p)) if os.path.exists(p) else {}
c = {'v': 3, 'createdOnFiles': old.get('createdOnFiles', {'v': 1, 'at': '2026-11-08T06:00:00Z'}), 'title': 'Credalio · Link 4 · Course Studio',
     'launch': {'view': 'canvas'}, 'pages': [{'id': 'main', 'name': 'Course Studio'}], 'boards': boards, 'order': order,
     'notes': notes, 'noteOrder': list(notes), 'designSystems': []}
json.dump(c, open(p, 'w'), ensure_ascii=False, indent=2)
print(len(boards), 'boards')
