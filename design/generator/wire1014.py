# wire1014: Link 1 links matched to the client's prototype (designer 2026-10-14). Sidebar + bell, dashboard/readiness/
# notification actions, orientation module rows, lesson rails and module step lists. Link 2 targets stay '#'.
# usage: python3 wire1014.py  (run in design/; edits canvas/project in place)
import re, os, glob
D = 'canvas/project'
def rd(f): return open(os.path.join(D, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(D, f), 'w', encoding='utf-8').write(s)
H = r'<a href="#"([^>]*)>(.*?)</a>'
def hashes(f, m):
    s = rd(f); ms = list(re.finditer(H, s, re.S))
    for i in sorted(m, reverse=True):
        x = ms[i]; assert x.group(0).startswith('<a href="#"'), (f, i)
        s = s[:x.start()] + '<a href="%s"' % m[i] + s[x.start() + len('<a href="#"'):]
    wr(f, s)
def rep(f, a, b, n=1):
    s = rd(f); assert s.count(a) == n, (f, a, s.count(a)); wr(f, s.replace(a, b))
# 2. page actions ('#' anchors by order, see ctx listing)
O = lambda n: 'CR-ORI-%s.dc.html' % n
hashes('CR-DASH-NEW.dc.html', {17: 'CR-KYC-001.dc.html', 18: 'CR-CRED-001.dc.html', 19: O('001'), 20: 'CR-POL-000.dc.html'})
hashes('CR-NOT-bell.dc.html', {17: 'CR-KYC-001.dc.html', 18: 'CR-CRED-001.dc.html', 19: O('001'), 20: 'CR-POL-000.dc.html'})
hashes('CR-DASH-ST.dc.html', {19: 'CR-NOT-001.dc.html', 20: 'CR-COL-002.dc.html', 21: 'CR-DEC-001.dc.html', 22: 'CR-ASG-001.dc.html',
    26: 'CR-VAL-WS-lead.dc.html', 27: 'CR-VAL-WS-lead.dc.html', 28: 'CR-VAL-MC-002.dc.html', 29: 'CR-VAL-WS-lead.dc.html'})
hashes('CR-ASG-001.dc.html', {16: 'CR-VAL-WS-lead.dc.html', 18: 'CR-DEC-001.dc.html'})
hashes('CR-HOME-EXP.dc.html', {18: 'CR-VAL-MC-002.dc.html'})
hashes('CR-HOME-SOON.dc.html', {14: 'CR-VAL-WS-lead.dc.html', 15: 'CR-VAL-MC-002.dc.html', 16: 'CR-CTR-001.dc.html'})
hashes('CR-VAL-MC-001.dc.html', {14: 'CR-VAL-WS-lead.dc.html'})
hashes('CR-RDY-001.dc.html', {17: 'CR-CRED-001r.dc.html', 18: 'CR-CRED-001r.dc.html', 20: 'CR-CRED-001.dc.html', 21: 'CR-POL-000.dc.html'})
hashes('CR-KYC-003.dc.html', {0: 'CR-CRED-001r.dc.html', 1: 'CR-CRED-001r.dc.html'})
hashes('CR-CRED-003.dc.html', {0: O('M4-L2'), 1: O('M4-L2')})
hashes('CR-ORI-007.dc.html', {0: 'CR-CRED-001r.dc.html'})
hashes('CR-DEC-001.dc.html', {2: 'CR-DEC-003.dc.html'})
hashes('CR-ORI-001.dc.html', {17: O('M1-00'), 18: O('M2-00'), 19: O('M3-00'), 20: O('M1-00'), 21: O('M2-00'), 22: O('M3-00'),
    23: O('002'), 24: O('M5-00'), 25: O('M6-00'), 26: O('M7-00')})
rep('CR-ORI-001.dc.html', 'href="CR-ORI-003.dc.html"', 'href="CR-ORI-M4-L2.dc.html"')
rep('CR-CRED-002.dc.html', '<a href="#" class="ds-btn"><span>{{goL}}', '<a href="{{goHref}}" class="ds-btn"><span>{{goL}}')
rep('CR-CRED-002.dc.html', "goL: t === 'fix' ? 'Resubmit' : 'Submit',", "goL: t === 'fix' ? 'Resubmit' : 'Submit', goHref: (t === 'aws' || t === 'badge') ? 'CR-CRED-003.dc.html' : 'CR-CRED-003b.dc.html',")
rep('CR-NOT-001.dc.html', '<a href="#" class="hp-rb" onClick="{{r.open}}">', '<a href="{{r.href}}" class="hp-rb" onClick="{{r.open}}">')
rep('CR-NOT-001.dc.html', 'cta: r[8],', "cta: r[8], href: ({ n1: 'CR-VAL-MC-002.dc.html', n2: 'CR-COL-002.dc.html', n7: 'CR-DEC-003.dc.html', n8: 'CR-ORI-001c.dc.html' })[r[0]] || '#',")
s = rd('CR-NOT-bell.dc.html')
for t, h in (('Clarification requested for Data Analysis with SQL', 'CR-VAL-MC-002.dc.html'), ('Dr. Bola Ade invited you to co-create', 'CR-COL-002.dc.html')):
    i = s.index('<b>' + t); j = s.rindex('<a href="CR-NOT-001.dc.html">', 0, i); s = s[:j] + '<a href="%s">' % h + s[j + len('<a href="CR-NOT-001.dc.html">'):]
wr('CR-NOT-bell.dc.html', s)
# 1. sidebar + bell on every dashboard-shell page
SIDE = {'My learning experiences': 'CR-HOME-EXP.dc.html', 'Assigned to me': 'CR-ASG-001.dc.html',
        'Validation Centre': 'CR-VAL-MC-001.dc.html', 'Settings': 'CR-HOME-SET.dc.html'}
for f in sorted(os.listdir(D)):
    if not f.endswith('.dc.html'): continue
    s = rd(f); o = s
    def side(m):
        lab = re.sub(r'<[^>]+>', '', m.group(2)).strip()
        return '<a href="%s" class="ds-item%s>%s</a>' % (SIDE[lab], m.group(1), m.group(2)) if lab in SIDE else m.group(0)
    s = re.sub(r'<a href="#" class="ds-item([^>]*)>(.*?)</a>', side, s, flags=re.S)
    if f != 'CR-NOT-bell.dc.html':
        s = s.replace('<a href="#" class="ds-icon-btn" aria-label="Notifications', '<a href="CR-NOT-bell.dc.html" class="ds-icon-btn" aria-label="Notifications')
    if s != o: wr(f, s)
# 3. orientation: module rows (titles) + current-module steps on the home, lesson rails, module step lists
STEPS = {1: ['M1-L1', 'M1-L2', 'M1-K1'], 2: ['M2-L1', 'M2-L2', 'M2-K1'], 3: ['M3-L1', 'M3-L2', 'M3-L3', 'M3-K1'],
         4: ['M4-L1', 'M4-L2', 'M4-L3', 'M4-K1'], 5: ['M5-L1', 'M5-L2', 'M5-K1', 'M5-S1'], 6: ['M6-L1', 'M6-L2', 'M6-K1'],
         7: ['M7-L1', 'M7-L2', 'M7-K1', 'M7-S1']}
OV = {1: 'M1-00', 2: 'M2-00', 3: 'M3-00', 4: '002', 5: 'M5-00', 6: 'M6-00', 7: 'M7-00'}
s = rd('CR-ORI-001.dc.html')
def mrow(m):
    li = m.group(0); n = int(re.search(r'Module (\d) · ', li).group(1))
    li = re.sub(r'<b><span class="or-mn">(.*?)</b>', lambda b: '<b><a href="%s" class="or-ml"><span class="or-mn">%s</a></b>' % (O(OV[n]), b.group(1)), li, count=1, flags=re.S)
    k = [0]
    def st(x):
        r = '<li class="or-s %s"><span class="or-sd"></span><a href="%s" class="or-sl">%s</a>' % (x.group(1), O(STEPS[n][k[0]]), x.group(2)); k[0] += 1; return r
    def st2(x):
        r = '<li class="or-s %s"><span class="or-sd">%s</span><a href="%s" class="or-sl">%s</a>' % (x.group(1), x.group(2), O(STEPS[n][k[0]]), x.group(3)); k[0] += 1; return r
    return re.sub(r'<li class="or-s ([^"]*)"><span class="or-sd">(.*?)</span><span>(.*?)</span>', st2, li, flags=re.S)
s = re.sub(r'<li class="or-m[^"]*">.*?</li>(?=<li class="or-m|</ol>)', mrow, s, flags=re.S)
s = s.replace('</style>', '.or-ml,.or-sl{color:inherit;text-decoration:none}.or-ml:hover,.or-sl:hover{color:#1652F0}\n</style>', 1)
wr('CR-ORI-001.dc.html', s)
def mod_of(f):
    m = re.match(r'CR-ORI-M(\d)-', f)
    return int(m.group(1)) if m else {'CR-ORI-002.dc.html': 4, 'CR-ORI-005.dc.html': 5}.get(f)
for f in sorted(glob.glob(D + '/CR-ORI-*.dc.html')):
    f = os.path.basename(f); n = mod_of(f)
    if not n: continue
    s = rd(f); o = s
    for cls, wrapcls in (('lp-o', 'lp-oa'), ('mo-r', 'mo-a')):
        k = [0]
        def it(m):
            i = k[0]; k[0] += 1
            if 'cur' in m.group(1) or i >= len(STEPS[n]): return m.group(0)
            return '<li class="%s%s"><a href="%s" class="%s">%s</a></li>' % (cls, m.group(1), O(STEPS[n][i]), wrapcls, m.group(2))
        s = re.sub(r'<li class="%s([^"]*)">(.*?)</li>' % cls, it, s, flags=re.S)
    if s != o:
        css = []
        if 'lp-oa' in s: css.append('.lp-oa{flex:1 1 auto;align-self:stretch;display:flex;align-items:center;gap:12px;color:inherit;text-decoration:none}.lp-oa:hover b{color:#1652F0}')
        if 'mo-a' in s: css.append('.mo-a{flex:1 1 auto;align-self:stretch;display:flex;align-items:center;gap:14px;color:inherit;text-decoration:none}.mo-a:hover b{color:#1652F0}')
        s = s.replace('</style>', '\n'.join(css) + '\n</style>', 1); wr(f, s)
print('ok')
