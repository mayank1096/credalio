# cl1012e: cleanup 5 on the last 10 orientation screens (M3-L3, M3-K, M3-DONE, M4-L1, M4-L3, M4-K, M4-DONE). usage: python3 cl1012e.py <dir>
# ori_m.trim() + two side notes moved into tooltips (M3-L3 lead sentence 2 -> "No evidence yet" chip; M4-L3 Good-to-know -> Revalidation node).
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ori_m as O, tipx
P = sys.argv[1]
def rd(f): return open(os.path.join(P, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(P, f), 'w', encoding='utf-8').write(s)
TIPCSS = '\n/* cl1012e tooltip */' + tipx.TIP_CSS + '.ln-c .tip,.vc2-n .tip{margin-left:4px;color:inherit;opacity:.75}\n.ln-c .tip-b{left:auto;right:-14px}\n'
for f in ['CR-ORI-M3-L3', 'CR-ORI-M4-L1', 'CR-ORI-M4-L3', 'CR-ORI-M3-K', 'CR-ORI-M4-K']:
    wr(f + '.dc.html', O.trim(rd(f + '.dc.html')))
s = rd('CR-ORI-M3-L3.dc.html')
assert 'cl1012e' not in s
s = s.replace(' Your Studio and Nova flag any outcome with nothing linked.', '', 1)
s = re.sub(r'(<span class="ln-c"><svg[^>]*>.*?</svg>No evidence yet)</span>', lambda m: m.group(1) + tipx.tip('Your Studio and Nova flag any outcome with nothing linked.', 'r dn') + '</span>', s, count=1, flags=re.S)
assert 'tip-b' in s and 'nothing linked.</p>' not in s
wr('CR-ORI-M3-L3.dc.html', O.with_css(s, TIPCSS))
s = rd('CR-ORI-M4-L3.dc.html')
s, n = re.subn(r'<aside class="ls-gk ob-in3">.*?</aside>', '', s, count=1, flags=re.S); assert n
s = s.replace('<b>Revalidation</b>', '<b>Revalidation' + tipx.tip('Learners keep access to the version they enrolled in.', 'r') + '</b>', 1)
assert 'tip-b' in s
wr('CR-ORI-M4-L3.dc.html', O.with_css(s, TIPCSS))
print('cl1012e ok')
