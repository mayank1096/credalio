# ctype1014c: designer 2026-10-14 — ONB-002 Creator scene v4 = v3 with the far-left plant removed and the content shifted
# 154px left so it is centred (ctype-creator-v4.webp); same route as v3 minus 154px. usage: python3 ctype1014c.py <file>
import re, sys
sys.argv, f = sys.argv[:1], sys.argv[1]
K = 1.086; OFF = -1
NEW = '/_blob/658ad152ad44cf112bd78a2beaa31aae'
SH = 154
IND = [(985,578),(960,578),(940,577),(920,575),(900,573),(880,570),(860,565),(840,558),(820,550),(800,544),(780,540),(760,536),(740,530),(720,522),(705,511),(695,500)]
INST = [(985,578),(1020,578),(1050,577),(1080,575),(1100,576),(1120,578),(1140,580),(1160,582),(1180,585),(1200,586),(1240,587),(1260,586),(1280,584),(1300,580),(1320,576),(1340,570),(1360,560),(1380,547),(1394,532)]
def vb(p): return [(round((x - SH) * K), round(y * K + OFF)) for x, y in p]
SVG = 'viewBox="0 0 2172 724" preserveAspectRatio="none" aria-hidden="true" style="position: absolute; left: 0; top: 0; width: 100%%; height: 100%%; pointer-events: none%s"'
def route(pts):
    d = 'M' + ' L'.join('%d %d' % q for q in pts); ex, ey = pts[-1]
    return ('<svg ' + (SVG % '; filter: blur(7px); opacity: 0.85') + '><path class="cd-draw" d="' + d + '" pathLength="1" fill="none" stroke="#1652F0" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"></path></svg>'
            '<svg ' + (SVG % '') + '><path class="cd-draw" d="' + d + '" pathLength="1" fill="none" stroke="#1652F0" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"></path>'
            '<path class="cd-comet" d="' + d + '" pathLength="1" fill="none" stroke="#FFFFFF" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"></path>'
            + ('<circle class="cd-pulse" cx="%d" cy="%d" r="12" fill="none" stroke="#1652F0" stroke-width="3"></circle>'
            '<circle cx="%d" cy="%d" r="9" fill="#1652F0" stroke="#FFFFFF" stroke-width="3"></circle></svg>') % (ex, ey, ex, ey))
s = open(f, encoding='utf-8').read()
old = '/_blob/729c615a1d1ad082a0b4b35d7c8b36b7'
assert s.count(old) == 1; s = s.replace(old, NEW)
for side, pts in (('ind', IND), ('inst', INST)):
    m = re.search(r'(<sc-if value="\{\{rt\.create_%s\}\}"[^>]*>)(.*?)(</sc-if>)' % side, s, re.S)
    assert m; s = s[:m.start(2)] + route(vb(pts)) + s[m.end(2):]
ox, oy = vb(IND[:1])[0]
s, n = re.subn(r'(<circle class="cd-orb" )cx="\d+" cy="\d+"', r'\1cx="%d" cy="%d"' % (ox, oy), s)
assert n >= 1
open(f, 'w', encoding='utf-8').write(s); print('ok', n)
