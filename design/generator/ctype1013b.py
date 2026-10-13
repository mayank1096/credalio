# ctype1013b: designer 2026-10-13 — ONB-002's role scenes get the SAME route animation as Main (dev-build markup:
# blurred trail + crisp line drawing in, white comet, pulse + end dot, breathing orb under the centre person), from the
# centre person to the selected option's node: left = Create independently (ind), right = With an organization (inst).
# Paths traced from the drawn line in each ctype-*.webp (image px; ×1.086 into the 2172×724 box, y offset for
# the bottom-anchored cover crop: learner 689 px tall → −24, others −1). usage: python3 ctype1013b.py <dir>
import os, sys
K = 1.086
P = {
 'learn': {'off': -24, 'orb': (975, 591),
   'ind': [(975,591),(940,594),(920,591),(900,585),(880,576),(860,569),(840,564),(820,559),(800,556),(780,554),(740,553),(700,551),(680,548),(660,543),(640,536),(620,526),(607,519)],
   'inst': [(975,591),(1000,588),(1040,589),(1060,588),(1080,578),(1100,571),(1120,565),(1140,560),(1160,557),(1200,555),(1240,558),(1280,560),(1320,555),(1340,550),(1360,543),(1380,532),(1390,524)]},
 'create': {'off': -1, 'orb': (975, 587),
   'ind': [(975,587),(940,588),(900,587),(880,580),(860,568),(840,561),(820,557),(800,554),(780,552),(740,551),(700,547),(680,543),(660,536),(640,526),(625,515),(613,505)],
   'inst': [(975,587),(1020,588),(1060,586),(1080,575),(1100,570),(1120,567),(1140,566),(1160,568),(1180,572),(1200,576),(1220,580),(1260,582),(1300,582),(1340,580),(1380,570),(1400,564),(1420,556),(1440,543),(1455,530),(1462,520)]},
 'validate': {'off': -1, 'orb': (1000, 591),
   'ind': [(1000,591),(980,591),(940,592),(900,590),(880,582),(860,575),(840,569),(820,564),(800,561),(780,560),(740,560),(720,560),(700,558),(680,555),(660,550),(640,543),(620,534),(607,524)],
   'inst': [(1000,591),(1040,593),(1060,592),(1080,582),(1100,574),(1120,567),(1140,561),(1180,557),(1220,559),(1260,564),(1300,564),(1320,561),(1340,556),(1360,547),(1378,535),(1387,528)]},
}
def vb(p, off): return [(round(x * K), round(y * K + off)) for x, y in p]
SVG = 'viewBox="0 0 2172 724" preserveAspectRatio="none" aria-hidden="true" style="position: absolute; left: 0; top: 0; width: 100%%; height: 100%%; pointer-events: none%s"'
def route(pts):
    d = 'M' + ' L'.join('%d %d' % q for q in pts); ex, ey = pts[-1]
    return ('<svg ' + (SVG % '; filter: blur(7px); opacity: 0.85') + '><path class="cd-draw" d="' + d + '" pathLength="1" fill="none" stroke="#1652F0" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"></path></svg>'
            '<svg ' + (SVG % '') + '><path class="cd-draw" d="' + d + '" pathLength="1" fill="none" stroke="#1652F0" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"></path>'
            '<path class="cd-comet" d="' + d + '" pathLength="1" fill="none" stroke="#FFFFFF" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"></path>'
            + ('<circle class="cd-pulse" cx="%d" cy="%d" r="12" fill="none" stroke="#1652F0" stroke-width="3"></circle>'
            '<circle cx="%d" cy="%d" r="9" fill="#1652F0" stroke="#FFFFFF" stroke-width="3"></circle></svg>') % (ex, ey, ex, ey))
blocks = ''
for r, v in P.items():
    for side in ('ind', 'inst'):
        blocks += '<sc-if value="{{rt.%s_%s}}" hint-placeholder-val="{{%s}}">%s</sc-if>' % (r, side, 'true' if (r, side) == ('create', 'ind') else 'false', route(vb(v[side], v['off'])))
    ox, oy = vb([v['orb']], v['off'])[0]
    blocks += ('<sc-if value="{{rt.%s}}" hint-placeholder-val="{{%s}}"><svg ' % (r, 'true' if r == 'create' else 'false') + (SVG % '') +
               ('><circle class="cd-orb" cx="%d" cy="%d" r="7" fill="#1652F0" stroke="#FFFFFF" stroke-width="2.5"></circle></svg></sc-if>' % (ox, oy)))
p = os.path.join(sys.argv[1], 'CR-ONB-002.dc.html'); s = open(p, encoding='utf-8').read()
assert 'ctype1013b' not in s and 'rt.create_ind' not in s
i = s.find('<div class="ob-illus" aria-hidden="true"'); j = s.find('</div>', i)
s = s[:i] + s[i:j].rstrip('\n') + '\n' + blocks + '\n' + s[j:]
a = "return { roleImg: imgs[role] || imgs.create,"
assert s.count(a) == 1
s = s.replace(a, "/* ctype1013b: route animation per role + selected option */\n    const rt = {}; ['learn', 'create', 'validate'].forEach((r) => { rt[r] = r === role; rt[r + '_ind'] = r === role && sel === 'ind'; rt[r + '_inst'] = r === role && sel === 'inst'; });\n    return { rt, roleImg: imgs[role] || imgs.create,")
open(p, 'w', encoding='utf-8').write(s); print('ok')
