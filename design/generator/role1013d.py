# role1013d: canvas Play keeps each artboard's state separate (no shared storage), so the role picked on Main reaches
# ONB-002 through the LINK: Main's Continue goes to a per-role board — learn → CR-ONB-002L, validate → CR-ONB-002V,
# create → CR-ONB-002, organization → CR-ONB-002S. 002L/002V = wrappers `dc-import CR-ONB-002 role=…`; ONB-002 reads
# this.props.role (default create). New boards sit under ONB-002 (p1 items below y 1900 move down 1000).
# usage: python3 role1013d.py <dir>
import os, sys, json
D = sys.argv[1]
p = os.path.join(D, 'CR-ONB-002.dc.html'); s = open(p, encoding='utf-8').read()
a = "constructor(props) { super(props); let role = 'create'; try { role = sessionStorage.getItem('crRole') || 'create'; } catch (e) {} this.state = { sel: 'ind', role }; }"
assert s.count(a) == 1
s = s.replace(a, "constructor(props) { super(props); this.state = { sel: 'ind' }; }")
a = "const role = ['learn', 'create', 'validate', 'institution'].includes(this.state.role) ? this.state.role : 'create';"
assert s.count(a) == 1
s = s.replace(a, "const role = ['learn', 'create', 'validate'].includes(this.props.role) ? this.props.role : 'create';")
a = """data-props='{"$preview":{"width":1440,"height":820}}'"""
assert s.count(a) == 1
s = s.replace(a, """data-props='{"role":{"editor":"enum","options":["learn","create","validate"],"default":"create"},"$preview":{"width":1440,"height":820}}'""")
open(p, 'w', encoding='utf-8').write(s)
m = os.path.join(D, 'Main.dc.html'); t = open(m, encoding='utf-8').read()
a = "ctaHref: sel === 'institution' ? 'CR-ONB-002S.dc.html' : 'CR-ONB-002.dc.html' };"
assert t.count(a) == 1
t = t.replace(a, "ctaHref: { learn: 'CR-ONB-002L.dc.html', create: 'CR-ONB-002.dc.html', validate: 'CR-ONB-002V.dc.html', institution: 'CR-ONB-002S.dc.html' }[sel] };")
open(m, 'w', encoding='utf-8').write(t)
WRAP = open(os.path.join(D, 'CR-KYC-002b.dc.html'), encoding='utf-8').read()
for sfx, role, label in (('L', 'learn', 'Learner'), ('V', 'validate', 'Validator')):
    w = WRAP.replace('<title>Credalio · Verify your identity: photos</title>', '<title>Credalio onboarding: how will you create (%s)</title>' % label)
    w = w.replace('<dc-import name="CR-KYC-002" variant="photos"', '<dc-import name="CR-ONB-002" role="%s"' % role)
    assert 'CR-ONB-002" role=' in w
    open(os.path.join(D, 'CR-ONB-002%s.dc.html' % sfx), 'w', encoding='utf-8').write(w)
cj = os.path.join(D, 'canvas.json'); c = json.load(open(cj, encoding='utf-8'))
assert 'CR-ONB-002L.dc.html' not in c['boards']
for coll in (c['boards'], c['notes']):
    for k, v in coll.items():
        if v.get('page') == 'p1' and v.get('y', 0) >= 1900: v['y'] += 1000
for i, (sfx, label) in enumerate((('L', 'Learner'), ('V', 'Validator'))):
    c['boards']['CR-ONB-002%s.dc.html' % sfx] = {'expand': 'fill', 'h': 820, 'is_interactive': True, 'page': 'p1',
        'title': 'CR-ONB-002%s · How will you create? · %s picked · Desktop' % (sfx, label), 'w': 1440, 'x': 2070 + i * 2070, 'y': 1240}
    i0 = c['order'].index('CR-ONB-002-Mobile.dc.html') + 1 + i
    c['order'].insert(i0, 'CR-ONB-002%s.dc.html' % sfx)
json.dump(c, open(cj, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('ok')
