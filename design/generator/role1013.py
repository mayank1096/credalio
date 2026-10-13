# role1013: designer 2026-10-13 — the role picked on ONB-001 (Main) carries over to ONB-002: same scene, same role
# highlighted (other groups faded + floor glow) and the same mobile pan, but WITHOUT the route/dot animation.
# Main stores the pick in sessionStorage 'crRole' (reset to 'create' on load); ONB-002 reads it (default create).
# usage: python3 role1013.py <dir>
import os, re, sys
D = sys.argv[1]
ROLES = ['learn', 'create', 'validate', 'institution']
PAN002 = {'learn': 106, 'create': 60, 'validate': -27, 'institution': -88}   # Main pans x 60/83 (002 mobile scene is narrower)
m = open(os.path.join(D, 'Main.dc.html'), encoding='utf-8').read()
assert 'crRole' not in m
ill = m[m.find('class="cd-illus"'):]
fades = {}
for r in ROLES:
    a = ill.find('<sc-if value="{{is.%s}}"' % r); b = ill.find('</sc-if>', a)
    fades[r] = ''.join(re.findall(r'<svg class="cd-fade".*?</svg>', ill[a:b], flags=re.S)); assert fades[r].count('<svg') == 2, r
a = "pick: () => this.setState({ sel: id }),"
assert m.count(a) == 1
m = m.replace(a, "pick: () => { try { sessionStorage.setItem('crRole', id); } catch (e) {} this.setState({ sel: id }); },")
a = "constructor(props) { super(props); this.state = { sel: 'create' }; }"
assert m.count(a) == 1
m = m.replace(a, "constructor(props) { super(props); this.state = { sel: 'create' }; try { sessionStorage.setItem('crRole', 'create'); } catch (e) {} }")
open(os.path.join(D, 'Main.dc.html'), 'w', encoding='utf-8').write(m)

p = os.path.join(D, 'CR-ONB-002.dc.html'); s = open(p, encoding='utf-8').read()
assert 'crRole' not in s
i = s.find('<div class="ob-illus" aria-hidden="true"'); j = s.find('</div>', i)
blk = s[i:j]
k = blk.find('<svg class="cd-fade"'); assert k > 0
new = blk[:k] + ''.join('<sc-if value="{{rl.%s}}" hint-placeholder-val="{{%s}}">%s</sc-if>' % (r, 'true' if r == 'create' else 'false', fades[r]) for r in ROLES) + '\n'
new = new.replace('--pan: 60px;', '--pan: {{rolePan}}px;'); assert '{{rolePan}}' in new
s = s[:i] + new + s[j:]
a = "constructor(props) { super(props); this.state = { sel: 'ind' }; }"
assert s.count(a) == 1
s = s.replace(a, "constructor(props) { super(props); let role = 'create'; try { role = sessionStorage.getItem('crRole') || 'create'; } catch (e) {} this.state = { sel: 'ind', role }; }")
a = "return { o, note: notes[sel],"
assert s.count(a) == 1
s = s.replace(a, "const role = %s.includes(this.state.role) ? this.state.role : 'create';\n    const rl = {}; %s.forEach((r) => { rl[r] = r === role; });\n    return { rl, rolePan: %s[role], o, note: notes[sel]," % (ROLES, ROLES, PAN002))
open(p, 'w', encoding='utf-8').write(s); print('ok')
