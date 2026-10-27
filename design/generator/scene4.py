# scene3: swap the main "One Line, Four Futures" scene (v2) for the designer's new four-roles scene (v3, 2026-10-12)
# in Main (ONB-001, per-role selection) and ONB-002 / 003b / 004 (Creator lit). Overlays redrawn for the new layout:
# other groups fade (white, blurred), soft cobalt floor glow under the selected group. No drawn path (the art has its own line).
# v4 (2026-10-12, designer): central walker + four roles on branching lines; walker never fades.
# usage: python3 scene4.py <dir> <new_blob_url>  (run on files that carry the v3 scene)
import re, sys, os
P, BLOB = sys.argv[1], sys.argv[2]
OLD = '/_blob/cd614cd8bd65153391f42811624f1c50'
VB = 'viewBox="0 0 2172 724" preserveAspectRatio="none" aria-hidden="true" style="position: absolute; left: 0; top: 0; width: 100%; height: 100%;'
G = {'learn': (70, 375), 'create': (462, 755), 'validate': (1298, 1505), 'institution': (1526, 2165)}
def overlay(sel):
    rects = ''.join(f'<rect x="{x0 - 10}" y="110" width="{x1 - x0 + 20}" height="560" rx="60" fill="#FFFFFF" fill-opacity="0.62"></rect>' for k, (x0, x1) in G.items() if k != sel)
    x0, x1 = G[sel]; cx = (x0 + x1) // 2; rx = int((x1 - x0) * 0.45)
    return (f'<svg class="cd-fade" {VB} filter: blur(26px)">{rects}</svg>'
            f'<svg class="cd-fade" {VB} filter: blur(18px); mix-blend-mode: multiply"><ellipse cx="{cx}" cy="624" rx="{rx}" ry="28" fill="#1652F0" fill-opacity="0.32"></ellipse></svg>')
def region(s):
    i = s.index(OLD); a = s.index('>', i) + 1; b = s.index('</div>', a)
    return a, b
out = []
s = open(os.path.join(P, 'Main.dc.html')).read()
a, b = region(s)
blk = '\n' + ''.join(f'<sc-if value="{{{{is.{k}}}}}" hint-placeholder-val="{{{{false}}}}">{overlay(k)}</sc-if>\n' for k in G)
s = s[:a] + blk + s[b:]
s = s.replace(OLD, BLOB)
s = s.replace('alt="Four scenes joined by one line: learners studying, creators recording a course, a validator checking it, and an organization planning with its team"',
              'alt="A young person walks forward on a line that branches to four people: a learner, a creator, a validator and an organization team"')
p = re.search(r'pans = \{[^}]*\}', s).group(0)
s = s.replace(p, 'pans = {"learn": 147, "create": 83, "validate": -48, "institution": -122}')
open(os.path.join(P, 'Main.dc.html'), 'w').write(s); out.append('Main.dc.html')
for f in ['CR-ONB-002.dc.html', 'CR-ONB-003b.dc.html', 'CR-ONB-004.dc.html']:
    s = open(os.path.join(P, f)).read()
    a, b = region(s)
    s = s[:a] + '\n' + overlay('create') + '\n' + s[b:]
    s = s.replace(OLD, BLOB).replace('--pan: 19px', '--pan: 60px')
    open(os.path.join(P, f), 'w').write(s); out.append(f)
print(' '.join(out))
