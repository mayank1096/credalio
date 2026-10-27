# scene3: swap the main "One Line, Four Futures" scene (v2) for the designer's new four-roles scene (v3, 2026-10-12)
# in Main (ONB-001, per-role selection) and ONB-002 / 003b / 004 (Creator lit). Overlays redrawn for the new layout:
# other groups fade (white, blurred), soft cobalt floor glow under the selected group. No drawn path (the art has its own line).
# usage: python3 scene3.py <dir> <new_blob_url>
import re, sys, os
P, BLOB = sys.argv[1], sys.argv[2]
OLD = '/_blob/877e6d93c070677634b4956192180989'
VB = 'viewBox="0 0 2172 724" preserveAspectRatio="none" aria-hidden="true" style="position: absolute; left: 0; top: 0; width: 100%; height: 100%;'
G = {'learn': (27, 538), 'create': (586, 1135), 'validate': (1195, 1575), 'institution': (1651, 2156)}
def overlay(sel):
    rects = ''.join(f'<rect x="{x0 - 10}" y="170" width="{x1 - x0 + 20}" height="480" rx="60" fill="#FFFFFF" fill-opacity="0.62"></rect>' for k, (x0, x1) in G.items() if k != sel)
    x0, x1 = G[sel]; cx = (x0 + x1) // 2; rx = int((x1 - x0) * 0.42)
    return (f'<svg class="cd-fade" {VB} filter: blur(26px)">{rects}</svg>'
            f'<svg class="cd-fade" {VB} filter: blur(18px); mix-blend-mode: multiply"><ellipse cx="{cx}" cy="606" rx="{rx}" ry="30" fill="#1652F0" fill-opacity="0.32"></ellipse></svg>')
def region(s):
    i = s.index(OLD); a = s.index('>', i) + 1; b = s.index('</div>', a)
    return a, b
out = []
s = open(os.path.join(P, 'Main.dc.html')).read()
a, b = region(s)
blk = '\n' + ''.join(f'<sc-if value="{{{{is.{k}}}}}" hint-placeholder-val="{{{{false}}}}">{overlay(k)}</sc-if>\n' for k in G)
s = s[:a] + blk + s[b:]
s = s.replace(OLD, BLOB)
s = s.replace('alt="A young person steps forward on a glowing line that branches toward four people: a learner, a creator, a validator and a mentor with a group"',
              'alt="Four scenes joined by one line: learners studying, creators recording a course, a validator checking it, and an organization planning with its team"')
p = re.search(r'pans = \{[^}]*\}', s).group(0)
s = s.replace(p, 'pans = {"learn": 137, "create": 42, "validate": -45, "institution": -131}')
open(os.path.join(P, 'Main.dc.html'), 'w').write(s); out.append('Main.dc.html')
for f in ['CR-ONB-002.dc.html', 'CR-ONB-003b.dc.html', 'CR-ONB-004.dc.html']:
    s = open(os.path.join(P, f)).read()
    a, b = region(s)
    s = s[:a] + '\n' + overlay('create') + '\n' + s[b:]
    s = s.replace(OLD, BLOB).replace('--pan: 55px', '--pan: 19px')
    open(os.path.join(P, f), 'w').write(s); out.append(f)
print(' '.join(out))
