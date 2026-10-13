# scene6: designer 2026-10-13 — main scene v6 (same layout as v5, plants added) + bring back the client's
# "moving dot": on Main, the selected role's branch of the line lights up and a cobalt dot travels from the walker's
# feet along the line to that role, with a soft pulse at the end node (loops; Play mode only).
# Paths are traced from the v6 line (image px 2000x668) and drawn in the 2172x724 viewBox via scale(1.086).
# usage: python3 scene6.py <dir>
import os, sys
P = sys.argv[1]
OLD, NEW = '/_blob/c6a3cfeead45b159745cbe37bd22bc3f', '/_blob/bdde3da6ce3a32978892f36dc5cc6685'
PTS = {
 'learn': [(960,578),(900,579),(860,571),(820,568),(780,569),(740,573),(700,578),(660,580),(620,582),(560,582),(500,580),(460,577),(420,573),(400,569),(380,564),(360,557),(342,546),(330,535),(322,524)],
 'create': [(960,578),(900,579),(862,569),(840,558),(820,551),(800,545),(780,540),(760,536),(740,531),(720,523),(705,512),(693,501)],
 'validate': [(960,578),(1020,579),(1060,578),(1082,572),(1100,561),(1118,549),(1131,536),(1140,522)],
 'institution': [(960,578),(1020,579),(1070,579),(1120,580),(1160,583),(1200,587),(1240,587),(1280,584),(1320,576),(1342,569),(1362,560),(1380,547),(1394,533)],
}
def smooth(p):
    d = 'M%d %d' % p[0]
    for i in range(len(p) - 1):
        p0 = p[i - 1] if i else p[i]; p1, p2 = p[i], p[i + 1]; p3 = p[i + 2] if i + 2 < len(p) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += ' C%.1f %.1f %.1f %.1f %d %d' % (c1 + c2 + p2)
    return d
def overlay(role):
    d = smooth(PTS[role]); ex, ey = PTS[role][-1]
    return ('<svg class="cd-route" viewBox="0 0 2172 724" preserveAspectRatio="none" aria-hidden="true" style="position: absolute; left: 0; top: 0; width: 100%%; height: 100%%; pointer-events: none; overflow: visible">'
            '<g transform="scale(1.086)">'
            '<path class="cd-lit" d="%s" pathLength="1" fill="none" stroke="#1652F0" stroke-width="5" stroke-linecap="round" stroke-opacity=".55"></path>'
            '<path class="cd-dotg" d="%s" pathLength="1" fill="none" stroke="#1652F0" stroke-width="30" stroke-linecap="round" stroke-opacity=".28" style="filter: blur(6px)"></path>'
            '<path class="cd-dotw" d="%s" pathLength="1" fill="none" stroke="#FFFFFF" stroke-width="19" stroke-linecap="round"></path>'
            '<path class="cd-dot" d="%s" pathLength="1" fill="none" stroke="#1652F0" stroke-width="12" stroke-linecap="round"></path>'
            '<circle class="cd-ping" cx="%d" cy="%d" r="11" fill="none" stroke="#1652F0" stroke-width="3"></circle>'
            '</g></svg>') % (d, d, d, d, ex, ey)
CSS = """
/* scene6: moving dot along the selected role's line */
.cd-lit{stroke-dasharray:1;stroke-dashoffset:1;animation:cdDraw 1.1s cubic-bezier(.4,0,.2,1) .15s forwards}
.cd-dot,.cd-dotw,.cd-dotg{stroke-dasharray:0.0001 2;stroke-dashoffset:0;opacity:0;animation:cdTravel 2.8s cubic-bezier(.45,.05,.35,1) .3s infinite}
@keyframes cdTravel{0%{stroke-dashoffset:0;opacity:0}8%{opacity:1}78%{stroke-dashoffset:-1;opacity:1}92%,100%{stroke-dashoffset:-1;opacity:0}}
.cd-ping{transform-box:fill-box;transform-origin:center;opacity:0;animation:cdPing 2.8s ease-out .3s infinite}
@keyframes cdPing{0%,74%{transform:scale(.6);opacity:0}78%{transform:scale(.8);opacity:.9}100%{transform:scale(2.6);opacity:0}}
@media (prefers-reduced-motion: reduce){.cd-dot,.cd-dotw,.cd-dotg,.cd-ping{animation:none;opacity:0}.cd-lit{animation:none;stroke-dashoffset:0}}
"""
out = []
for f in sorted(os.listdir(P)):
    if not f.endswith('.dc.html'): continue
    p = os.path.join(P, f); s = open(p, encoding='utf-8').read()
    if OLD not in s: continue
    s = s.replace(OLD, NEW)
    if f == 'Main.dc.html':
        assert 'scene6' not in s
        for r in PTS:
            a = '<sc-if value="{{is.%s}}" hint-placeholder-val="{{false}}">' % r
            i = s.find(a, s.find('class="cd-illus"')); assert i > 0, r
            j = s.find('</sc-if>', i); s = s[:j] + overlay(r) + s[j:]
        i = s.rfind('</style>', 0, s.find('</helmet>')); s = s[:i] + CSS + s[i:]
    open(p, 'w', encoding='utf-8').write(s); out.append(f)
print('scene6', len(out))
