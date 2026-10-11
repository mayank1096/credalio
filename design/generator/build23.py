# build23: wallet outcomes on the ONE standard outcome layout (LIVE CR-KYC-003 ko-*: emblem → pill → H1 → sub → card(s) → cta → links).
# CR-WAL-OUT one source, variants processing / failed / funded (= CR-WAL-005 / 005f / 006). Replaces the older panel-style
# processing/failed (build21) and the POL-based WAL-006 (build22). Only writes its own files. usage: python3 build23.py <canvas project dir>
import re, sys, os
P = sys.argv[1]
rd = lambda f: open(os.path.join(P, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(P, f), 'w', encoding='utf-8').write(s)
def ic(paths, w=20, sw=1.9):
    return f'<svg width="{w}" height="{w}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>'
ARR = ic('<path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path>', 18, 2.4)
CHK = ic('<path d="m5 12.5 4.5 4.5L19 7.5"></path>', 12, 3)
CARD = '<rect x="3" y="6" width="18" height="14" rx="3"></rect><path d="M3 10h18M16 15h2"></path>'
BANK = '<path d="M3 10h18L12 4z"></path><path d="M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 20h18"></path>'
COIN = '<circle cx="12" cy="12" r="9"></circle><path d="M14.8 9.2A4 4 0 1 0 14.8 14.8"></path>'
VAL = '<path d="M12 3v18M5 21h14M6 7h12"></path><path d="m6 7-3 7a3 3 0 0 0 6 0zM18 7l-3 7a3 3 0 0 0 6 0z"></path>'
CHEV = ic('<path d="m9 6 6 6-6 6"></path>', 16, 2.2)

k = rd('CR-KYC-003.dc.html')
# header: wallet, no Sumsub pill
k = k.replace('<a href="CR-RDY-001.dc.html" class="lp-x" aria-label="Close and go back to readiness">', '<a href="CR-WAL-001.dc.html" class="lp-x" aria-label="Close and go back to your wallet">', 1)
k = re.sub(r'<div class="lp-title">.*?</div>', '<div class="lp-title"><span class="lp-t1" style="display: block">Credit Wallet</span></div>', k, count=1, flags=re.S)
k = re.sub(r'<span class="tk-sec tk-sum">.*?</span></span>\n', '', k, count=1, flags=re.S)
# emblem "a" icon: card instead of camera
k = re.sub(r'(<sc-if value="\{\{a\}\}" hint-placeholder-val="\{\{false\}\}">)<svg.*?</svg>(</sc-if>)', lambda m: m.group(1) + ic(CARD, 28, 2) + m.group(2), k, count=1, flags=re.S)
a = k.index('\n<sc-if value="{{r}}" hint-placeholder-val="{{true}}">\n<div class="ko-row">')
b = k.index('<div class="ko-links ob-in4">')
body = (
 '\n<sc-if value="{{r}}" hint-placeholder-val="{{true}}">\n'
 '<section class="ko-card wo-one ob-in3" aria-label="What happens next"><span class="sec-h">What happens next</span><ol class="ko-path">'
 '<li class="ko-done"><span class="ko-dot">' + CHK + '</span><span><b>Payment sent</b><span>$253.75 by Visa •••• 4417</span></span></li>'
 '<li class="ko-now"><span class="ko-dot"></span><span><b>Your bank confirms</b><span>Usually under a minute</span></span></li>'
 '<li><span class="ko-dot"></span><span><b>2,500 Credits land in your wallet</b><span>This page updates on its own</span></span></li></ol></section>\n'
 '<div class="ko-cta ob-in4"><span class="ko-cn">You won’t be charged twice. Paying again is paused until this finishes.</span></div>\n</sc-if>\n'
 '<sc-if value="{{a}}" hint-placeholder-val="{{false}}">\n'
 '<section class="ko-card wo-one ob-in3" aria-label="Other ways to pay"><span class="sec-h">Other ways to pay</span><div class="ko-opts">'
 '<a href="CR-WAL-003.dc.html" class="ko-opt"><span class="ko-oi">' + ic(BANK, 18) + '</span><span><b>Bank transfer</b><span>No fee. Usually confirmed in minutes.</span></span>' + CHEV + '</a>'
 '<a href="CR-WAL-003.dc.html" class="ko-opt"><span class="ko-oi">' + ic(CARD, 18) + '</span><span><b>A different card</b><span>Or a local payment provider.</span></span>' + CHEV + '</a></div></section>\n'
 '<div class="ko-cta ob-in4"><a href="CR-WAL-004.dc.html" class="ds-btn"><span>Try this card again</span><span class="ob-arrow">' + ARR + '</span></a><span class="ko-cn">Nothing was taken. Your balance is still 1,150 Credits.</span></div>\n</sc-if>\n'
 '<sc-if value="{{v}}" hint-placeholder-val="{{false}}">\n<div class="ko-row">\n'
 '<section class="ko-card ko-idc ob-in3" aria-label="New balance"><span class="ko-ii wo-coin">' + ic(COIN, 22, 2.2) + '</span>'
 '<span class="ko-it"><b>3,650 Credits</b><span>New balance</span></span><span class="ko-vb wo-add">+2,500</span>'
 '<div class="ko-rd wo-rd"><span class="ko-rl">$253.75 · Visa •••• 4417 · TX-88531</span><a href="#" class="ds-link">Download receipt</a></div></section>\n'
 '<section class="ko-next ob-in4" aria-label="Next for you"><span class="ko-ni">' + ic(VAL, 20) + '</span>'
 '<span class="ko-nt"><span class="ko-nl">Next for you</span><b>Pay for validation</b><span>Data Analysis with SQL needs 1,260 Credits. You have enough now.</span></span>'
 '<a href="CR-PAY-002b.dc.html" class="ds-btn sm ko-go"><span>Continue</span><span class="ob-arrow">' + ARR + '</span></a></section>\n</div>\n</sc-if>\n\n')
k = k[:a] + body + k[b:]
k = re.sub(r'<div class="ko-links ob-in4">.*?</div>', '<div class="ko-links ob-in4"><a href="CR-WAL-001.dc.html">Back to wallet</a><span aria-hidden="true">·</span><a href="CR-WAL-007.dc.html">Transactions</a></div>', k, count=1, flags=re.S)
k = k.replace('</style>', '''
/* build23 wallet outcomes */
.wo-one{max-width:560px}
.wo-coin{background:#1652F0 !important}
.wo-add{background:#E7F5EE;color:#0F6B45}
.wo-rd{justify-content:space-between}
.ko-row .ko-idc:has(.wo-rd){align-content:space-between}
.wo-rd .ds-link{font-size:13.5px;font-weight:600;white-space:nowrap}
.ko-cta:not(:has(.ds-btn)){margin-top:14px}
</style>''', 1)
s0 = k.index('<script type="text/x-dc"'); s1 = k.index('</script>', s0) + 9
k = k[:s0] + '''<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":820}}'>
class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.v = (props || {}).variant || 'processing';
  }
  renderVals() {
    const v = this.v;
    const T = {
      processing: ['ko-r', 'Processing', 'Processing your payment', 'We’re waiting for your bank to confirm. You can leave this page; we’ll let you know.'],
      failed: ['ko-a', 'Not charged', 'Your payment didn’t go through', 'Your bank declined $253.75 by Visa •••• 4417.'],
      funded: ['ko-v', 'Funded', '2,500 Credits added', 'They’re in your wallet and ready to use.']
    }[v];
    return { koCls: T[0], pill: T[1], h1: T[2], sub: T[3], r: v === 'processing', v: v === 'funded', a: v === 'failed', f: false };
  }
}
</script>''' + k[s1:]
k = re.sub(r'<title>.*?</title>', '<title>Credalio · Credit Wallet</title>', k)
wr('CR-WAL-OUT.dc.html', k)

wd, wm = rd('CR-DASH-S03.dc.html'), rd('CR-CRED-002c-Mobile.dc.html')
for n, var in [('CR-WAL-005', 'processing'), ('CR-WAL-005f', 'failed'), ('CR-WAL-006', 'funded')]:
    imp = f'<dc-import name="CR-WAL-OUT" variant="{var}"'
    t = wd.replace('<dc-import name="CR-DASH-ST" variant="s03"', imp)
    wr(n + '.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} preview</title>', t))
    t = wm.replace('<dc-import name="CR-CRED-002" variant="badge"', imp)
    wr(n + '-Mobile.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} mobile preview</title>', t))
print('build23 ok')
