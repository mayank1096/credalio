# rm1014: designer 2026-10-14 — remove the Learner / Validator versions of "How will you create?" (boards CR-ONB-002L / 002V)
# now that ONB-001 Learner/Validator are inert; strip their dead code from ONB-002 + Main; close the 1000px canvas gap
# under ONB-002 (reverse of role1013d). usage: python3 rm1014.py <canvas project dir>
import os, re, sys, json
D = sys.argv[1]
p = os.path.join(D, 'CR-ONB-002.dc.html'); s = open(p, encoding='utf-8').read()
for r in ('learn', 'validate'):
    for k in (r + '_ind', r + '_inst', r):
        m = re.search(r'<sc-if value="\{\{rt\.%s\}\}"[^>]*>.*?</sc-if>' % k, s, re.S); assert m, k
        s = s[:m.start()] + s[m.end():]
a = s[s.find("    const role = ['learn'"):s.find("    return { rt,")]
assert 'imgs' in a and 'rl' in a
s = s.replace(a, "    const rt = { create: true, create_ind: sel === 'ind', create_inst: sel === 'inst' };\n")
s = s.replace("return { rt, roleImg: imgs[role] || imgs.create, rl, rolePan: 0,", "return { rt, roleImg: '/_blob/25b801c589477ae80d7b4950b057928d', rolePan: 0,")
assert 'imgs' not in s and "rl," not in s and 'rt.learn' not in s and 'rt.validate' not in s
open(p, 'w', encoding='utf-8').write(s)
p = os.path.join(D, 'Main.dc.html'); s = open(p, encoding='utf-8').read()
a = "ctaHref: { learn: 'CR-ONB-002L.dc.html', create: 'CR-ONB-002.dc.html', validate: 'CR-ONB-002V.dc.html', institution: 'CR-ONB-002S.dc.html' }[sel]"
assert s.count(a) == 1
s = s.replace(a, "ctaHref: sel === 'institution' ? 'CR-ONB-002S.dc.html' : 'CR-ONB-002.dc.html'")
open(p, 'w', encoding='utf-8').write(s)
cj = os.path.join(D, 'canvas.json'); c = json.load(open(cj))
for f in ('CR-ONB-002L.dc.html', 'CR-ONB-002V.dc.html'):
    del c['boards'][f]; os.remove(os.path.join(D, f))
for coll in (c['boards'], c['notes']):
    for k, v in coll.items():
        if v.get('page') == 'p1' and v['y'] >= 2000: v['y'] -= 1000
open(cj, 'w').write(json.dumps(c, indent=2, ensure_ascii=False)); print('ok')
