# conf1013: confetti on every success screen (standard outcome ko-* success state {{v}}, module complete dn-badge, RDY-001d rdd-em).
# usage: python3 conf1013.py <dir>   (patches in place; skips files already patched)
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from confetti import CONF, add_css
P = sys.argv[1]; done = []
KO = ['CR-KYC-003', 'CR-CRED-003', 'CR-POL-002', 'CR-COL-004', 'CR-WAL-OUT', 'CR-PAYO-OUT', 'CR-HELP-004', 'CR-CREIO-005']
DN = ['CR-ORI-006', 'CR-ORI-M1-DONE', 'CR-ORI-M2-DONE', 'CR-ORI-M3-DONE', 'CR-ORI-M4-DONE', 'CR-ORI-M6-DONE']
def patch(f, old, new, css=''):
    p = os.path.join(P, f + '.dc.html'); s = open(p, encoding='utf-8').read()
    if 'class="cf"' in s: return
    assert s.count(old) == 1, (f, s.count(old)); s = add_css(s.replace(old, new, 1))
    if css:
        i = s.rfind('</style>', 0, s.find('</helmet>')); s = s[:i] + css + s[i:]
    open(p, 'w', encoding='utf-8').write(s); done.append(f + '.dc.html')
for f in KO:
    patch(f, '<div class="ko-emb ob-in" aria-hidden="true"><span class="ko-halo"></span>',
          '<div class="ko-emb ob-in" aria-hidden="true"><sc-if value="{{v}}" hint-placeholder-val="{{false}}">' + CONF + '</sc-if><span class="ko-halo"></span>',
          '\n.ko-halo,.ko-disc{z-index:1}\n')
for f in DN:
    patch(f, '<div class="dn-badge ob-in" aria-hidden="true">', '<div class="dn-badge ob-in" aria-hidden="true">' + CONF,
          '\n.dn-badge > span:not(.cf){z-index:1}\n')
patch('CR-RDY-001', '<span class="rdd-em">', '<span class="rdd-em">' + CONF, '\n.rdd-em{position:relative}.rdd-em > svg{position:relative;z-index:1}\n')
print('conf1013 ok'); print(' '.join(done))
