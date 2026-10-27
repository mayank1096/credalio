# sel1014: designer 2026-10-14 — (1) ONB-001 Learner/Validator ARE selectable again (selection + route animation)
# but Continue does nothing for them (CTA is a plain button, no link); reverts inert1014.
# (2) ONB-002 illustration bigger: height min(60vh, 32vw, 95vh - 300px) (was min(50vh, 33.33vw, 100vh - 400px)), sized so the
# scene's top (≈25% of its height) always stays ~20px+ below the Continue button. usage: python3 sel1014.py <project dir>
import os, sys
D = sys.argv[1]
p = os.path.join(D, 'Main.dc.html'); s = open(p, encoding='utf-8').read()
s = s.replace('class="cd-card cd-off"', 'class="cd-card"')
s = s.replace('\n.cd-off:hover,.cd-off:active{transform:none;border-color:#E6EAF3 !important}', '')
s = s.replace("pick: () => { if (id === 'learn' || id === 'validate') return; this.setState({ sel: id }); },", "pick: () => { this.setState({ sel: id }); },")
for r in ('learn', 'validate'):
    i = s.find('onClick="{{c.%s.pick}}"' % r); j = s.find('>', i)
    s = s[:i] + s[i:j].replace('cursor: default', 'cursor: pointer') + s[j:]
assert 'cd-off' not in s and 'cursor: default' not in s
i = s.find('<a href="{{ctaHref}}" class="cd-cta"'); j = s.find('</a>', i) + 4
link = s[i:j]
btn = link.replace('<a href="{{ctaHref}}" class="cd-cta" style="', '<button type="button" class="cd-cta" style="border: 0; cursor: pointer; font-family: inherit; ').replace('</a>', '</button>')
s = s[:i] + '<sc-if value="{{ctaGo}}" hint-placeholder-val="{{true}}">' + link + '</sc-if><sc-if value="{{ctaStay}}" hint-placeholder-val="{{false}}">' + btn + '</sc-if>' + s[j:]
a = "ctaHref: sel === 'institution' ? 'CR-ONB-002S.dc.html' : 'CR-ONB-002.dc.html'"
assert s.count(a) == 1
s = s.replace(a, a + ", ctaGo: sel === 'create' || sel === 'institution', ctaStay: sel === 'learn' || sel === 'validate'")
open(p, 'w', encoding='utf-8').write(s)
p = os.path.join(D, 'CR-ONB-002.dc.html'); s = open(p, encoding='utf-8').read()
a = 'height: min(50vh, 33.33vw, calc(100vh - 400px)); aspect-ratio: 2172 / 724'
assert s.count(a) == 1
s = s.replace(a, 'height: min(60vh, 32vw, calc(95vh - 300px)); aspect-ratio: 2172 / 724')
open(p, 'w', encoding='utf-8').write(s); print('ok')
