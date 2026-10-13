# scene6b: designer 2026-10-13 "not matching the actual animation you did before" (ref = dev build, ONB step 0).
# Replaces scene6's dot overlay on Main with the ORIGINAL markup/classes from the dev build, retraced on the v6 line:
#   blurred 16px cobalt trail (cd-draw, filter blur 7px, .85) + crisp 4.5px cobalt line (cd-draw) + white streak running
#   along it (cd-comet, loops) + pulse ring (cd-pulse) + solid end dot (r9, white ring) at the role's node,
#   + breathing orb under the walker (cd-orb). Keyframes/classes cdDraw/cdComet/cdPulse/cdOrb already live in Main.
# usage: python3 scene6b.py <dir>
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from scene6 import PTS
K = 1.086
def vb(p): return [(round(x * K), round(y * K)) for x, y in p]
def poly(p): return 'M' + ' L'.join('%d %d' % q for q in p)
def overlay(role):
    p = vb(PTS[role]); d = poly(p); ex, ey = p[-1]
    S = 'viewBox="0 0 2172 724" preserveAspectRatio="none" aria-hidden="true" style="position: absolute; left: 0; top: 0; width: 100%%%%; height: 100%%%%; pointer-events: none%s"'
    return ('<svg ' + (S % '; filter: blur(7px); opacity: 0.85') + '><path class="cd-draw" d="%s" pathLength="1" fill="none" stroke="#1652F0" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"></path></svg>'
            '<svg ' + (S % '') + '><path class="cd-draw" d="%s" pathLength="1" fill="none" stroke="#1652F0" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"></path>'
            '<path class="cd-comet" d="%s" pathLength="1" fill="none" stroke="#FFFFFF" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"></path>'
            '<circle class="cd-pulse" cx="%d" cy="%d" r="12" fill="none" stroke="#1652F0" stroke-width="3"></circle>'
            '<circle cx="%d" cy="%d" r="9" fill="#1652F0" stroke="#FFFFFF" stroke-width="3"></circle></svg>') % (d, d, d, ex, ey, ex, ey)
p = os.path.join(sys.argv[1], 'Main.dc.html'); s = open(p, encoding='utf-8').read()
assert 'scene6b' not in s and 'cd-route' in s
s, n = re.subn(r'<svg class="cd-route".*?</svg>', '', s, flags=re.S); assert n == 4, n
for r in PTS:
    a = '<sc-if value="{{is.%s}}" hint-placeholder-val="{{false}}">' % r
    i = s.find(a, s.find('class="cd-illus"')); j = s.find('</sc-if>', i); s = s[:j] + overlay(r) + s[j:]
# walker orb (always on), after the last role overlay
wx, wy = vb([PTS['create'][0]])[0]
orb = '<svg viewBox="0 0 2172 724" preserveAspectRatio="none" aria-hidden="true" style="position: absolute; left: 0; top: 0; width: 100%%; height: 100%%; pointer-events: none"><circle class="cd-orb" cx="%d" cy="%d" r="7" fill="#1652F0" stroke="#FFFFFF" stroke-width="2.5"></circle></svg>' % (wx, wy)
i = s.find('<sc-if value="{{is.institution}}"', s.find('class="cd-illus"')); j = s.find('</sc-if>', i) + len('</sc-if>')
s = s[:j] + orb + s[j:]
# drop scene6 CSS block (the original classes are already in the page)
a = s.find('\n/* scene6: moving dot'); b = s.find('}}\n', s.find('@media (prefers-reduced-motion: reduce){.cd-dot', a)) + 3
assert a > 0 and b > a; s = s[:a] + '\n/* scene6b: original dev-build route animation (cd-draw / cd-comet / cd-pulse / cd-orb) */\n' + s[b:]
open(p, 'w', encoding='utf-8').write(s); print('ok')
