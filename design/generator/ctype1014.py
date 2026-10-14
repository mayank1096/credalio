# ctype1014: designer 2026-10-14 — new Creator scene on ONB-002 (ctype-creator-v2.webp) with the route re-traced to its
# line, and the two option cards wider (max 680 -> 920) so each description fits on one line. usage: python3 ctype1014.py <file>
import re, sys
K = 1.086; OFF = -1
NEW = '/_blob/25b801c589477ae80d7b4950b057928d'
IND = [(975,587),(960,587),(940,587),(920,584),(900,582),(880,574),(860,567),(840,561),(820,556),(800,553),(780,551),(760,550),(740,550),(720,549),(700,547),(680,543),(660,535),(640,525),(625,514),(613,506)]
INST = [(975,587),(1000,586),(1040,588),(1060,580),(1080,574),(1100,569),(1120,566),(1140,565),(1160,567),(1180,572),(1200,576),(1220,579),(1260,581),(1300,581),(1320,580),(1340,577),(1360,573),(1380,568),(1400,564),(1410,560),(1430,550),(1445,539),(1452,530),(1459,523)]
def vb(p): return [(round(x * K), round(y * K + OFF)) for x, y in p]
SVG = 'viewBox="0 0 2172 724" preserveAspectRatio="none" aria-hidden="true" style="position: absolute; left: 0; top: 0; width: 100%%; height: 100%%; pointer-events: none%s"'
def route(pts):
    d = 'M' + ' L'.join('%d %d' % q for q in pts); ex, ey = pts[-1]
    return ('<svg ' + (SVG % '; filter: blur(7px); opacity: 0.85') + '><path class="cd-draw" d="' + d + '" pathLength="1" fill="none" stroke="#1652F0" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"></path></svg>'
            '<svg ' + (SVG % '') + '><path class="cd-draw" d="' + d + '" pathLength="1" fill="none" stroke="#1652F0" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"></path>'
            '<path class="cd-comet" d="' + d + '" pathLength="1" fill="none" stroke="#FFFFFF" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"></path>'
            + ('<circle class="cd-pulse" cx="%d" cy="%d" r="12" fill="none" stroke="#1652F0" stroke-width="3"></circle>'
            '<circle cx="%d" cy="%d" r="9" fill="#1652F0" stroke="#FFFFFF" stroke-width="3"></circle></svg>') % (ex, ey, ex, ey))
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
old = "'create': '/_blob/303efabd2ddabb7edfb4cda677ac03d8'"
assert s.count(old) == 1; s = s.replace(old, "'create': '%s'" % NEW)
for side, pts in (('ind', IND), ('inst', INST)):
    m = re.search(r'(<sc-if value="\{\{rt\.create_%s\}\}"[^>]*>)(.*?)(</sc-if>)' % side, s, re.S)
    assert m; s = s[:m.start(2)] + route(vb(pts)) + s[m.end(2):]
a = 'grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px; max-width: 680px'
assert s.count(a) == 1; s = s.replace(a, 'grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px; max-width: 920px')
assert s.count('min-height: 84px') == 2; s = s.replace('min-height: 84px', 'min-height: 76px')
open(p, 'w', encoding='utf-8').write(s); print('ok')
