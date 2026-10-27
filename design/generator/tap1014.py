# tap1014: mobile tap areas. Small text links (16-28px tall) get an invisible 44px hit area via ::after on <=960px;
# nothing moves visually. ONB-002 scene image src made static (avoids a request for the raw "{{roleImg}}" template).
# usage: python3 tap1014.py  (run in design/)
import os, re
D = 'canvas/project'
SEL = ['.ds-mlogo a', '.ko-links a', '.oc-links a', '.cr-fx', '.cr-back', '.ct-all', '.ds-link', '.ob-link', '.ob-x',
       '.dn-back', '.pl-back', '.pl-full', '.rq-back', '.xb-alt', '.rv-whyh']
def used(s, sel):
    c = sel.split()[0][1:]
    return re.search(r'class="[^"]*\b%s\b' % re.escape(c), s) is not None
n = 0
for f in sorted(os.listdir(D)):
    if not f.endswith('.dc.html'): continue
    p = os.path.join(D, f); s = open(p, encoding='utf-8').read()
    if '::after{content:\'\';position:absolute;left:-8px;right:-8px;top:50%;height:44px' in s or '</style>' not in s: continue
    sels = [x for x in SEL if used(s, x)]
    if not sels: continue
    a = ','.join(sels); b = ','.join(x + '::after' for x in sels)
    css = ('@media (max-width: 960px){%s{position:relative}%s{content:\'\';position:absolute;left:-8px;right:-8px;top:50%%;height:44px;transform:translateY(-50%%)}}\n' % (a, b))
    s = s.replace('</style>', css + '</style>', 1); open(p, 'w', encoding='utf-8').write(s); n += 1
p = os.path.join(D, 'CR-ORI-001.dc.html'); s = open(p, encoding='utf-8').read()
if '.or-ml::after' not in s:
    s = s.replace('</style>', ".or-ml::after{content:'';position:absolute;inset:0}.or-m a:not(.or-ml){position:relative;z-index:1}\n</style>", 1)
    open(p, 'w', encoding='utf-8').write(s)
p = os.path.join(D, 'CR-ONB-002.dc.html'); s = open(p, encoding='utf-8').read()
s = s.replace('src="{{roleImg}}"', 'src="/_blob/658ad152ad44cf112bd78a2beaa31aae"')
open(p, 'w', encoding='utf-8').write(s)
print('files', n)
