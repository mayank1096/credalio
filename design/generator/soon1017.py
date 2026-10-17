"""Coming soon pages for the Learner and Validator paths (client WTusAd9o3fJn711spDqBsJ, 2026-10-17).
CR-ONB-002S becomes one source with variants: (default) organization / learn / validate.
New boards CR-ONB-001L / 001V (+ Mobile) import it; ONB-001 Continue now leads Learner -> 001L, Validator -> 001V.
Usage: python3 soon1017.py <canvas/project dir>"""
import json, os, re, sys
P = sys.argv[1]
rd = lambda f: open(os.path.join(P, f)).read()
def wr(f, s): open(os.path.join(P, f), 'w').write(s)

s = rd('CR-ONB-002S.dc.html')
assert '{{h1}}' not in s
for old, new in [('>Organizations are coming soon.</h1>', '>{{h1}}</h1>'),
                 ('>You can start creating on your own today.</p>', '>{{sub}}</p>'),
                 ('<img src="/_blob/dd59631e21fe0b4aa5b410aa522bc1b7"', '<img src="{{img}}"')]:
    assert s.count(old) == 1, old; s = s.replace(old, new)
s = s.replace('  renderVals() { return {}; }', r'''  renderVals() {
    const v = { learn: ['Learning is coming soon.', 'Pick another path to get started today.', '/_blob/8cf042f136c8ee1dfa3a3cb348ed6234'],
                validate: ['Validation is coming soon.', 'Pick another path to get started today.', '/_blob/ffd6552769fa87f54686dc11ffc01420'] }[(this.props || {}).variant]
      || ['Organizations are coming soon.', 'You can start creating on your own today.', '/_blob/dd59631e21fe0b4aa5b410aa522bc1b7'];
    return { h1: v[0], sub: v[1], img: v[2] };
  }''')
assert '{{img}}' in s and "learn: [" in s
wr('CR-ONB-002S.dc.html', s)

m = rd('Main.dc.html')
old = "ctaHref: sel === 'institution' ? 'CR-ONB-002S.dc.html' : 'CR-ONB-002.dc.html', ctaGo: sel === 'create' || sel === 'institution', ctaStay: sel === 'learn' || sel === 'validate' };"
new = "ctaHref: { institution: 'CR-ONB-002S.dc.html', learn: 'CR-ONB-001L.dc.html', validate: 'CR-ONB-001V.dc.html' }[sel] || 'CR-ONB-002.dc.html' };"
assert m.count(old) == 1; m = m.replace(old, new)
m, n = re.subn(r'<sc-if value="\{\{ctaGo\}\}" hint-placeholder-val="\{\{true\}\}">(<a href="\{\{ctaHref\}\}".*?</a>)</sc-if><sc-if value="\{\{ctaStay\}\}".*?</button></sc-if>', r'\1', m, flags=re.S)
assert n == 1; wr('Main.dc.html', m)

def wrap(title, variant, hint):
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>%s</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n'
            '<dc-import name="CR-ONB-002S" variant="%s" hint-size="%s"></dc-import>\n</x-dc>\n</body>\n</html>\n') % (title, variant, hint)
for b, v, t in [('CR-ONB-001L', 'learn', 'Learning is coming soon'), ('CR-ONB-001V', 'validate', 'Validation is coming soon')]:
    wr(b + '.dc.html', wrap('%s · %s' % (b, t), v, '1440px,820px'))
    wr(b + '-Mobile.dc.html', wrap('%s · %s · Mobile' % (b, t), v, '390px,980px'))

cj = os.path.join(P, 'canvas.json'); d = json.load(open(cj)); B = d['boards']
assert 'CR-ONB-001L.dc.html' not in B
s2 = B['CR-ONB-002S.dc.html']; Y, X0 = s2['y'], s2['x'] + 2070
for k, v in B.items():
    if v.get('page', 'p1') == 'p1' and v['y'] == Y and v['x'] >= X0: v['x'] += 2 * 2070
for n in d['notes'].values():
    if n.get('page') == 'p1' and Y < n['y'] < Y + 1300 and n['x'] >= X0: n['x'] += 2 * 2070
new = []
for i, (b, t) in enumerate([('CR-ONB-001L', 'Learning is coming soon'), ('CR-ONB-001V', 'Validation is coming soon')]):
    x = X0 + i * 2070
    B[b + '.dc.html'] = {'x': x, 'y': Y, 'w': 1440, 'h': 820, 'is_interactive': True, 'page': 'p1', 'title': '%s · %s · Desktop' % (b, t)}
    B[b + '-Mobile.dc.html'] = {'x': x + 1520, 'y': Y, 'w': 390, 'h': 980, 'is_interactive': True, 'page': 'p1', 'title': '%s · Mobile' % b}
    d['notes']['new-' + b] = {'text': 'NEW · just made · ' + b, 'x': x, 'y': Y + 1010, 'w': 1910, 'fill': 'red', 'page': 'p1'}
    new += [b + '.dc.html', b + '-Mobile.dc.html']
o = d['order']; i = o.index('CR-ONB-002S-Mobile.dc.html') + 1
d['order'] = o[:i] + new + o[i:]
row = sorted((v['x'], v['x'] + v['w'], k) for k, v in B.items() if v.get('page', 'p1') == 'p1' and v['y'] == Y)
for a, b in zip(row, row[1:]): assert a[1] <= b[0], (a, b)
json.dump(d, open(cj, 'w'), ensure_ascii=False, indent=2, sort_keys=True)
print('done')
