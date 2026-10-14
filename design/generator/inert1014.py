# inert1014: designer 2026-10-14 — on ONB-001 (Main) clicking Learner or Validator does nothing:
# no selection, no route animation, no hover lift, default cursor. usage: python3 inert1014.py <Main.dc.html>
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
for r in ('learn', 'validate'):
    a = '<button type="button" class="cd-card" onClick="{{c.%s.pick}}"' % r
    assert s.count(a) == 1, r
    s = s.replace(a, '<button type="button" class="cd-card cd-off" onClick="{{c.%s.pick}}"' % r)
    i = s.find('class="cd-card cd-off" onClick="{{c.%s.pick}}"' % r); j = s.find('>', i)
    tag = s[i:j]; assert tag.count('cursor: pointer') == 1
    s = s[:i] + tag.replace('cursor: pointer', 'cursor: default') + s[j:]
a = '.cd-card:active{transform:translateY(0) scale(.985)}'
assert s.count(a) == 1
s = s.replace(a, a + '\n.cd-off:hover,.cd-off:active{transform:none;border-color:#E6EAF3 !important}')
a = "pick: () => { this.setState({ sel: id }); },"
assert s.count(a) == 1
s = s.replace(a, "pick: () => { if (id === 'learn' || id === 'validate') return; this.setState({ sel: id }); },")
open(p, 'w', encoding='utf-8').write(s); print('ok')
