# build25: payout-method outcomes on the ONE standard outcome layout (LIVE CR-KYC-003 ko-*), like build23.
# CR-PAYO-OUT one source, variants verified / pending (= CR-PAYO-001g PayPal connected / CR-PAYO-001p Payoneer verification pending).
# Only writes its own files. usage: python3 build25.py <canvas project dir>
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tipx import tip, TIP_CSS
P = sys.argv[1]
rd = lambda f: open(os.path.join(P, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(P, f), 'w', encoding='utf-8').write(s)
def ic(paths, w=20, sw=1.9):
    return f'<svg width="{w}" height="{w}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>'
ARR = ic('<path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path>', 18, 2.4)
CHK = ic('<path d="m5 12.5 4.5 4.5L19 7.5"></path>', 12, 3)
EARN = '<circle cx="12" cy="12" r="9"></circle><path d="M14.8 9.2c-.6-.9-1.6-1.4-2.8-1.4-1.6 0-2.7.8-2.7 2 0 2.9 5.7 1.5 5.7 4.4 0 1.2-1.2 2.1-2.9 2.1-1.4 0-2.5-.6-3-1.5M12 6v1.8M12 16.2V18"></path>'
PP, PO = '/_blob/27435c5526a86beb998393f8bb53a00c', '/_blob/e702b7f8a951c23451145db9309e7234'

k = rd('CR-KYC-003.dc.html')
k = k.replace('<a href="CR-RDY-001.dc.html" class="lp-x" aria-label="Close and go back to readiness">', '<a href="CR-EARN-001.dc.html" class="lp-x" aria-label="Close">', 1)
k = re.sub(r'<div class="lp-title">.*?</div>', '<div class="lp-title"><span class="lp-t1" style="display: block">Payout method</span></div>', k, count=1, flags=re.S)
k = re.sub(r'<span class="tk-sec tk-sum">.*?</span></span>\n', '', k, count=1, flags=re.S)
a = k.index('\n<sc-if value="{{r}}" hint-placeholder-val="{{true}}">\n<div class="ko-row">')
b = k.index('<div class="ko-links ob-in4">')
body = (
 '\n<sc-if value="{{r}}" hint-placeholder-val="{{false}}">\n'
 '<section class="ko-card po-one ob-in3" aria-label="What happens next"><div class="po-who"><img src="' + PO + '" alt=""><span><b>Payoneer</b><span>Local bank account · NGN •••• 2219</span></span></div><ol class="ko-path">'
 '<li class="ko-done"><span class="ko-dot">' + CHK + '</span><span><b>Account linked</b><span>Just now</span></span></li>'
 '<li class="ko-now"><span class="ko-dot"></span><span><b>Payoneer verifies it</b><span>Usually 1–3 business days</span></span></li>'
 '<li><span class="ko-dot"></span><span><b>Payouts start</b><span>Your November payout goes here</span></span></li></ol></section>\n</sc-if>\n'
 '<sc-if value="{{v}}" hint-placeholder-val="{{true}}">\n<div class="ko-row">\n'
 '<section class="ko-card ko-idc ob-in3" aria-label="Payout method"><span class="ko-ii po-lgi"><img src="' + PP + '" alt=""></span>'
 '<span class="ko-it"><b>PayPal</b><span>ada.ononuju@example.com</span></span>'
 '<div class="ko-rd po-rd"><span class="ko-rl">Verified in your name' + tip('Payouts only go to an account in your own verified name.') + '</span><a href="CR-PAYO-001.dc.html" class="ds-link">Change</a></div></section>\n'
 '<section class="ko-next ob-in4" aria-label="Next for you"><span class="ko-ni">' + ic(EARN, 20) + '</span>'
 '<span class="ko-nt"><span class="ko-nl">Next for you</span><b>$2,850.00 on its way</b><span>Your next payout arrives in early November.</span></span>'
 '<a href="CR-EARN-001.dc.html" class="ds-btn sm ko-go"><span>View earnings</span><span class="ob-arrow">' + ARR + '</span></a></section>\n</div>\n</sc-if>\n\n')
k = k[:a] + body + k[b:]
k = re.sub(r'<div class="ko-links ob-in4">.*?</div>', '<div class="ko-links ob-in4"><a href="{{lh}}">{{lt}}</a></div>', k, count=1, flags=re.S)
k = k.replace('</style>', TIP_CSS + '''
/* build25 payout outcomes */
.po-one{max-width:520px}
.po-who{display:flex;align-items:center;gap:12px;padding-bottom:16px;margin-bottom:6px;border-bottom:1.5px solid #F0F2F8}
.po-who img{width:40px;height:40px;padding:7px;box-sizing:border-box;border-radius:12px;border:1.5px solid #E6EAF3;background:#FFFFFF}
.po-who > span{display:flex;flex-direction:column;gap:2px;text-align:left}.po-who b{font-size:15px;font-weight:600}.po-who > span > span{font-size:13.5px;color:#5B6582}
.po-lgi{background:#FFFFFF !important;border:1.5px solid #E6EAF3}
.po-lgi img{width:24px;height:24px;object-fit:contain}
.po-rd{justify-content:space-between}
.ko-row .ko-idc:has(.po-rd){align-content:space-between}
.po-rd .ko-rl{display:inline-flex;align-items:center}
.po-rd .ds-link{font-size:13.5px;font-weight:600}
</style>''', 1)
s0 = k.index('<script type="text/x-dc"'); s1 = k.index('</script>', s0) + 9
k = k[:s0] + '''<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":820}}'>
class Component extends DCLogic {
  constructor(props) { super(props); this.v = (props || {}).variant || 'verified'; }
  renderVals() {
    const p = this.v === 'pending';
    return { koCls: p ? 'ko-r' : 'ko-v', pill: p ? 'Verification pending' : 'Connected', h1: p ? 'Payoneer is linked' : 'PayPal is connected',
      sub: p ? 'Payoneer is checking your account. We’ll let you know when it’s done.' : 'Your earnings go here automatically each month.',
      r: p, v: !p, a: false, f: false, lt: p ? 'Back to earnings' : 'Back to my Studio', lh: p ? 'CR-EARN-001.dc.html' : 'CR-DASH-NEW.dc.html' };
  }
}
</script>''' + k[s1:]
k = re.sub(r'<title>.*?</title>', '<title>Credalio · Payout method</title>', k)
wr('CR-PAYO-OUT.dc.html', k)
wd, wm = rd('CR-DASH-S03.dc.html'), rd('CR-CRED-002c-Mobile.dc.html')
for n, var in [('CR-PAYO-001g', 'verified'), ('CR-PAYO-001p', 'pending')]:
    imp = f'<dc-import name="CR-PAYO-OUT" variant="{var}"'
    t = wd.replace('<dc-import name="CR-DASH-ST" variant="s03"', imp)
    wr(n + '.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} preview</title>', t))
    t = wm.replace('<dc-import name="CR-CRED-002" variant="badge"', imp)
    wr(n + '-Mobile.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} mobile preview</title>', t))
print('build25 ok')
