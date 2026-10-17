"""Place the CR-LOG boards at the top of Link 1 page p1 (two rows) and wire every onboarding "Log in" button.
Usage: python3 log1016_canvas.py <canvas/project dir>"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from log1016 import BOARDS
P = sys.argv[1]
cj = os.path.join(P, 'canvas.json'); d = json.load(open(cj))
assert 'CR-LOG-001.dc.html' not in d['boards'], 'already placed'
SHIFT = 2600
for b in d['boards'].values():
    if b.get('page', 'p1') == 'p1': b['y'] += SHIFT
for n in d['notes'].values():
    if n.get('page', 'p1') == 'p1': n['y'] += SHIFT
rows = {'CR-LOG-001': 0, 'CR-LOG-002': 1, 'CR-LOG-003': 1}
col = {0: 0, 1: 0}; new = []
for b, src, var, t in BOARDS:
    r = rows[src]; x = col[r] * 2070; y = 320 + r * 1300; col[r] += 1
    desk = {'x': x, 'y': y, 'w': 1440, 'h': 820, 'is_interactive': True, 'page': 'p1', 'title': '%s · %s · Desktop' % (b, t)}
    if b == src: desk['expand'] = 'fill'
    d['boards'][b + '.dc.html'] = desk
    d['boards'][b + '-Mobile.dc.html'] = {'x': x + 1520, 'y': y, 'w': 390, 'h': 844, 'is_interactive': True, 'page': 'p1', 'title': '%s · Mobile' % b}
    new += [b + '.dc.html', b + '-Mobile.dc.html']
d['order'] = new + [o for o in d['order'] if o not in new]
d['notes']['l1s0'] = {'kind': 'title1', 'maxW': 8000, 'page': 'p1', 'w': 240, 'x': 0, 'y': 0, 'text': 'Link 1 · Log in: errors (check details · wrong email or password · email not confirmed · too many attempts)'}
d['notes']['l1s0b'] = {'kind': 'title1', 'maxW': 8000, 'page': 'p1', 'w': 240, 'x': 0, 'y': 1300, 'text': 'Link 1 · Forgot password: reset link sent → choose a new password → updated · or link expired'}
json.dump(d, open(cj, 'w'), ensure_ascii=False, indent=2, sort_keys=True)
n = 0
for f in ['Main.dc.html', 'CR-ONB-002.dc.html', 'CR-ONB-002S.dc.html', 'CR-ONB-003.dc.html']:
    p = os.path.join(P, f); s = open(p).read()
    s2, k = re.subn(r'<a href="#" (class="(?:ob|cd)-ghost"[^>]*>Log in</a>)', r'<a href="CR-LOG-001.dc.html" \1', s)
    assert k == 1, f; n += k; open(p, 'w').write(s2)
print('placed', len(new), 'boards; wired', n, 'Log in buttons')
