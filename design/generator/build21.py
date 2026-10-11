# build21: Credit Wallet (CR-WAL-001, Studio page) + Add Credits flow CR-WAL-FUND one source,
# variants amount / method / summary / processing (= WAL-002 / 003 / 004 / 005), focus shell on the LIVE CR-COL-002 head (cl-*).
# Credits are NOT Creio: navy/cobalt, never gold. Imports build17 for page(). Only writes its own files.
# usage: python3 build21.py <canvas project dir>
import re, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build17 as B
P, rd, wr, ic, I, ARR = B.P, B.rd, B.wr, B.ic, B.I, B.ARR
CHK = ic('<path d="m5 12.5 4.5 4.5L19 7.5"></path>', 13, 2.8)
PLUS = ic('<path d="M12 5v14M5 12h14"></path>', 18, 2.4)
BANK = '<path d="M3 10h18L12 4z"></path><path d="M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 20h18"></path>'
PHONE = '<rect x="7" y="2.5" width="10" height="19" rx="2.5"></rect><path d="M11 18h2"></path>'
GEM = '<path d="M6 3h12l3 6-9 12L3 9z"></path><path d="M3 9h18"></path>'
CRED = ('<span class="cr-ic" aria-hidden="true">' + ic('<circle cx="12" cy="12" r="9"></circle><path d="M14.8 9.2A4 4 0 1 0 14.8 14.8"></path>', 16, 2.2) + '</span>')

# ======================= CR-WAL-001 · Credit Wallet =======================
TX = [('30 Sep', 'Wallet funded', 'Bank transfer', '+2,500', 'Completed', 'gr', 'in'),
      ('14 Sep', 'Validation', 'Data Analyst Career Path · VAL-01102', '−588', 'Completed', 'gr', 'out'),
      ('2 Sep', 'Wallet funded', 'Card · Visa •••• 4417', '+1,000', 'Completed', 'gr', 'in'),
      ('2 Sep', 'Creio purchase', '100,000 Creio for Nova', '−80', 'Completed', 'gr', 'out'),
      ('20 Aug', 'Revalidation', 'Advanced SQL · minor revalidation', '−180', 'Completed', 'gr', 'out')]
txr = ''.join(f'<li class="wl-r"><span class="wl-d">{d}</span><span class="hp-ic {"gr" if k == "in" else "gy"}">{ic(PLUS if False else (I["card"] if k == "in" else I["doc"]), 18)}</span>'
              f'<span class="wl-t"><b>{t}</b><span>{s}</span></span><b class="wl-a {k}">{a}</b></li>' for d, t, s, a, st, tone, k in TX)
main_wl = ('<main class="ds-main hp">\n<div class="hp-head ob-in"><div><h1 class="ds-h1">Credit Wallet</h1><p class="hp-sub">Credits pay for validation and other Credalio services. They’re separate from your earnings.</p></div></div>'
           '<section class="ds-card wl-bal ob-in2" aria-label="Balance"><div class="wl-b"><span class="hp-lab">Available</span><b>' + CRED + '1,150 <em>Credits</em></b><span>≈ $115.00 · 1 Credit = $0.10</span></div>'
           '<div class="wl-k"><span class="hp-lab">Pending</span><b>0</b><span>Nothing waiting to clear</span></div>'
           '<div class="wl-k"><span class="hp-lab">Next validation</span><b>~1,250</b><span>Data Analysis with SQL</span></div>'
           '<a href="CR-WAL-002.dc.html" class="ds-btn hp-btn wl-go"><span>Add Credits</span><span class="ob-arrow">' + PLUS + '</span></a></section>'
           '<section class="ds-card wl-tx ob-in3" aria-labelledby="wl-h"><div class="wl-th"><h2 id="wl-h">Recent activity</h2><a href="#" class="ds-link">View all</a></div><ul class="wl-l">' + txr + '</ul></section>'
           '<div class="wl-pm ob-in3"><span class="hp-lab">Payment methods</span><span class="wl-m">' + ic(I['card'], 18) + 'Visa •••• 4417<em>Default</em></span><span class="wl-m">' + ic(BANK, 18) + 'Bank transfer</span><a href="#" class="ds-link">Manage</a></div>\n</main>')
css_wl = '''
.cr-ic{display:inline-flex;width:30px;height:30px;border-radius:50%;background:#EAF0FF;color:#1652F0;align-items:center;justify-content:center;flex-shrink:0}
.wl-bal{display:grid;grid-template-columns:repeat(3,minmax(0,1fr)) auto;align-items:stretch;gap:0;padding:24px 28px}
.wl-b,.wl-k{justify-content:flex-start;padding:0 28px;border-left:1.5px solid #F0F2F8}
.wl-b{padding-left:0;border-left:0}
.wl-go{align-self:center;margin-left:28px}
.wl-b,.wl-k{display:flex;flex-direction:column;gap:6px}
.wl-b b{display:flex;align-items:center;gap:10px;font-size:34px;font-weight:600;letter-spacing:-0.02em;line-height:1.1}
.wl-b b em{font-style:normal;font-size:16px;font-weight:500;color:#5B6582;letter-spacing:0}
.wl-b > span:last-child,.wl-k > span:last-child{font-size:13px;color:#5B6582}
.wl-k b{font-size:22px;font-weight:600;line-height:1.1;min-height:38px;display:flex;align-items:center}
.wl-go .ob-arrow svg{width:16px;height:16px}
.wl-tx{margin-top:16px;padding:8px 24px 6px 24px}
.wl-th{display:flex;align-items:center;justify-content:space-between;padding:12px 0 8px 0}
.wl-th h2{margin:0;font-size:17px;font-weight:600}
.wl-l{list-style:none;margin:0;padding:0}
.wl-r{display:grid;grid-template-columns:64px 40px minmax(0,1fr) auto;align-items:center;column-gap:14px;padding:13px 0;border-top:1.5px solid #F0F2F8}
.wl-d{font-size:13.5px;color:#5B6582}
.wl-t{display:flex;flex-direction:column;gap:2px;min-width:0}
.wl-t b{font-size:15px;font-weight:600}.wl-t span{font-size:13px;color:#5B6582;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.wl-a{font-size:15.5px;font-weight:600;white-space:nowrap}.wl-a.in{color:#0F6B45}.wl-a.out{color:#0B1433}
.wl-a::after{content:' Cr';font-size:12.5px;font-weight:500;color:#8A93AD}
.wl-pm{margin-top:18px;display:flex;align-items:center;gap:20px;padding:0 4px;flex-wrap:wrap}
.wl-m{display:inline-flex;align-items:center;gap:8px;font-size:14px;color:#0B1433}
.wl-m svg{color:#5B6582}
.wl-m em{font-style:normal;font-size:12px;font-weight:500;color:#0E3BB8;background:#EAF0FF;border-radius:999px;padding:2px 8px;margin-left:2px}
.wl-pm .ds-link{margin-left:auto;font-size:14px}
@media (max-width: 1180px){.wl-bal{grid-template-columns:repeat(2,minmax(0,1fr)) auto}.wl-bal .wl-k:nth-of-type(3){display:none}}
@media (max-width: 960px){
.wl-bal{grid-template-columns:1fr 1fr;gap:18px 16px;padding:20px 18px}
.wl-b{grid-column:1 / -1}
.wl-b b{font-size:30px}
.wl-k{padding:0;border-left:0}
.wl-go{margin-left:0}
.wl-bal .wl-k:nth-of-type(3){display:flex}
.wl-k b{font-size:19px;min-height:0}
.wl-go{grid-column:1 / -1;width:100%;justify-content:space-between}
.wl-tx{padding:4px 16px}
.wl-r{grid-template-columns:36px minmax(0,1fr) auto;row-gap:2px;column-gap:12px}
.wl-r .hp-ic{width:36px;height:36px;border-radius:11px;grid-column:1;grid-row:1 / 3}
.wl-t{grid-column:2;grid-row:1}
.wl-t span{display:none}
.wl-d{grid-column:2;grid-row:2;font-size:12.5px}
.wl-a{grid-column:3;grid-row:1 / 3}
.wl-pm{gap:12px 16px}
.wl-pm .hp-lab{flex-basis:100%}
}
'''
B.page('CR-WAL-001', 'Credit Wallet', main_wl, B.js_new, css_wl, 'Credalio · Credit Wallet')

# ======================= CR-WAL-FUND · Add Credits flow =======================
col = rd('CR-COL-002.dc.html')
head = col[:col.index('<div class="tk-root')]
X = col[col.index('class="lp-x"'):]
X = X[X.index('<svg'):X.index('</a>')]
AMTS = [(500, '$50'), (1000, '$100'), (2500, '$250'), (5000, '$500')]
PM = [('card', I['card'], 'Card', 'Visa •••• 4417, or a new card', '1.5% fee'), ('bank', BANK, 'Bank transfer', 'To a dedicated account · usually confirmed in minutes', 'No fee'),
      ('local', PHONE, 'Local payment', 'USSD, mobile money and local cards', '1.5% fee'), ('mforge', GEM, 'MFORGE', 'Ecosystem payment', 'Network fee')]
amt_opts = ''.join(f'<button type="button" role="radio" aria-checked="{{{{a{n}.on}}}}" class="wf-o {{{{a{n}.cls}}}}" onClick="{{{{a{n}.pick}}}}"><b>{n:,}</b><span>Credits · {usd}</span><i class="xb-ck">{CHK}</i></button>' for n, usd in AMTS)
amt_opts += '<button type="button" role="radio" aria-checked="{{aC.on}}" class="wf-o {{aC.cls}}" onClick="{{aC.pick}}"><b>Custom</b><span>From 100 Credits</span><i class="xb-ck">' + CHK + '</i></button>'
pm_opts = ''.join(f'<button type="button" role="radio" aria-checked="{{{{m_{k}.on}}}}" class="wf-m {{{{m_{k}.cls}}}}" onClick="{{{{m_{k}.pick}}}}"><span class="wf-mi">{ic(p, 20)}</span><span class="wf-mt"><b>{t}</b><span>{d}<em class="wf-fm"> · {f}</em></span></span><span class="wf-fee">{f}</span><i class="xb-ck">{CHK}</i></button>' for k, p, t, d, f in PM)
STEPS = '<ol class="cl-steps" aria-label="Steps"><li class="{{s0}}"><i></i><span>Amount</span></li><li class="{{s1}}"><i></i><span>Payment</span></li><li class="{{s2}}"><i></i><span>Review</span></li></ol>'
side = ('<aside class="cl-side ob-in"><h1 class="cl-h1 wf-h">Add Credits</h1>'
        '<p class="cl-sub">Credits pay for validation, revalidation and other Credalio services.</p>'
        '<div class="wf-bal">' + CRED + '<span><span class="hp-lab">Current balance</span><b>1,150 Credits</b></span></div>' + STEPS + '</aside>')
foot = lambda back, nxt, label, off='': (f'<div class="cl-foot">' + (f'<a href="{back}" class="ds-ghost cl-bk" aria-label="Back">' + ic('<path d="M19 12H5"></path><path d="m11 6-6 6 6 6"></path>', 18, 2.2) + '<span>Back</span></a>' if back else '')
                                         + f'<a href="{nxt}" class="ds-btn cl-go wf-go {off}"><span>{label}</span><span class="ob-arrow">{ARR}</span></a></div>')
p_amount = ('<sc-if value="{{vAmount}}" hint-placeholder-val="{{true}}"><section class="cl-panel ob-in2" aria-labelledby="wf-h1"><h2 id="wf-h1" class="cl-ph">How many Credits?</h2>'
            '<div class="wf-g" role="radiogroup" aria-label="Amount">' + amt_opts + '</div>'
            '<sc-if value="{{isCustom}}" hint-placeholder-val="{{false}}"><label class="wf-cu"><span class="sr-only">Custom amount</span><input value="{{custom}}" onChange="{{onCustom}}" placeholder="e.g. 1,800"><em>Credits</em></label></sc-if>'
            '<div class="wf-tot"><span>You’ll add</span><b>{{amtTxt}}</b><span class="wf-usd">{{usdTxt}}</span></div>'
            + foot('', 'CR-WAL-003.dc.html', 'Continue') + '</section></sc-if>')
p_method = ('<sc-if value="{{vMethod}}" hint-placeholder-val="{{false}}"><section class="cl-panel ob-in2" aria-labelledby="wf-h2"><h2 id="wf-h2" class="cl-ph">How would you like to pay?</h2>'
            '<div class="wf-ml" role="radiogroup" aria-label="Payment method">' + pm_opts + '</div>'
            + foot('CR-WAL-002.dc.html', 'CR-WAL-004.dc.html', 'Continue') + '</section></sc-if>')
p_sum = ('<sc-if value="{{vSummary}}" hint-placeholder-val="{{false}}"><section class="cl-panel ob-in2" aria-labelledby="wf-h3"><h2 id="wf-h3" class="cl-ph">Review and pay</h2>'
         '<dl class="wf-dl"><div><dt>Credits</dt><dd>2,500</dd></div><div><dt>Price</dt><dd>$250.00</dd></div><div><dt>Card fee (1.5%)</dt><dd>$3.75</dd></div>'
         '<div><dt>Pay with</dt><dd>Visa •••• 4417 <a href="CR-WAL-003.dc.html" class="ds-link">Change</a></dd></div><div class="wf-total"><dt>Total</dt><dd>$253.75</dd></div></dl>'
         '<p class="wf-fine">You’re charged once. Credits arrive as soon as the payment is confirmed.</p>'
         + foot('CR-WAL-003.dc.html', 'CR-WAL-005.dc.html', 'Pay $253.75') + '</section></sc-if>')
p_proc = ('<sc-if value="{{vProc}}" hint-placeholder-val="{{false}}"><section class="cl-panel wf-proc ob-in2" aria-live="polite"><span class="wf-spin" aria-hidden="true"></span>'
          '<h2 class="cl-ph">Processing your payment</h2><p class="cl-pp">$253.75 by Visa •••• 4417. We’re waiting for your bank to confirm. This page updates on its own.</p>'
          '<div class="wf-safe">' + CHK + '<span>You won’t be charged twice. Paying again is paused until this finishes.</span></div></section></sc-if>')
body = ('<div class="tk-root cl-root">\n<div class="tk-scene" aria-hidden="true"></div><div class="cl-glow" aria-hidden="true"></div>\n'
        '<header class="tk-top">\n<a href="CR-WAL-001.dc.html" class="lp-x" aria-label="Close and go back to your wallet">' + X + '</a>\n'
        '<div class="lp-title"><span class="lp-t1" style="display: block">Credit Wallet</span></div>\n<span style="flex-grow: 1"></span>\n</header>\n'
        '<main class="cl">\n' + side + '\n<div class="cl-main">' + p_amount + p_method + p_sum + p_proc + '</div>\n</main>\n</div>\n</x-dc>\n')
CSS = '''
/* build21 add credits */
.cr-ic{display:inline-flex;width:36px;height:36px;border-radius:50%;background:#EAF0FF;color:#1652F0;align-items:center;justify-content:center;flex-shrink:0}
.hp-lab{display:block;font-size:12.5px;font-weight:500;color:#8A93AD}
.wf-h{margin-top:0}
.wf-bal{margin-top:22px;display:flex;align-items:center;gap:12px}
.wf-bal b{display:block;margin-top:2px;font-size:17px;font-weight:600}
.wf-g{margin-top:18px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}
.wf-g .wf-o:last-child{grid-column:1 / -1;flex-direction:row;align-items:baseline;gap:10px;padding:14px 16px}
.wf-g .wf-o:last-child b{font-size:16px}
.wf-o,.wf-m{position:relative;font-family:inherit;text-align:left;cursor:pointer;color:#0B1433;background:#FFFFFF;border:1.5px solid #E6EAF3;border-radius:16px;transition:border-color .2s ease,background .2s ease}
.wf-o:hover,.wf-m:hover{border-color:#AFC1F5}
.wf-o{display:flex;flex-direction:column;gap:2px;padding:16px}
.wf-o b{font-size:20px;font-weight:600}.wf-o span{font-size:13px;color:#5B6582}
.xb-ck{display:none;position:absolute;top:12px;right:12px;width:20px;height:20px;border-radius:50%;background:#1652F0;color:#FFFFFF;align-items:center;justify-content:center}
.xb-on{border-color:#1652F0;background:#F5F8FF;box-shadow:0 0 0 4px rgba(22,82,240,.10)}
.xb-on .xb-ck{display:inline-flex}
.wf-cu{margin-top:12px;display:flex;align-items:center;gap:10px;height:52px;padding:0 16px;border-radius:14px;border:1.5px solid #1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.wf-cu input{flex-grow:1;border:0;outline:none;font-family:inherit;font-size:17px;color:#0B1433;background:none}
.wf-cu em{font-style:normal;color:#5B6582;font-size:14px}
.wf-tot{margin-top:18px;display:flex;align-items:baseline;gap:10px;padding:14px 18px;border-radius:16px;background:#F5F8FF}
.wf-tot > span:first-child{font-size:14px;color:#3A4566}
.wf-tot b{font-size:20px;font-weight:600}
.wf-usd{margin-left:auto;font-size:16px;font-weight:600;color:#0B1433}
.wf-go{margin-left:auto}
.wf-ml{margin-top:18px;display:flex;flex-direction:column;gap:8px}
.wf-m{display:flex;align-items:center;gap:14px;padding:14px 48px 14px 14px}
.wf-mi{width:40px;height:40px;flex-shrink:0;border-radius:12px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.wf-mt{flex-grow:1;display:flex;flex-direction:column;gap:2px}
.wf-mt b{font-size:15px;font-weight:600}.wf-mt span{font-size:13px;color:#5B6582}
.wf-fee{font-size:13px;font-weight:500;color:#5B6582;white-space:nowrap}
.wf-fm{display:none;font-style:normal}
.wf-m .xb-ck{top:50%;margin-top:-10px;right:16px}
.wf-dl{margin:16px 0 0 0;border:1.5px solid #E6EAF3;border-radius:18px;padding:4px 20px}
.wf-dl > div{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:13px 0;border-top:1.5px solid #F0F2F8}
.wf-dl > div:first-child{border-top:0}
.wf-dl dt{font-size:14.5px;color:#5B6582}
.wf-dl dd{margin:0;font-size:15px;font-weight:600;display:flex;align-items:center;gap:12px}
.wf-dl .ds-link{font-size:13.5px;font-weight:600}
.wf-total{border-top:2px solid #0B1433 !important}
.wf-total dt{font-size:16px;font-weight:600;color:#0B1433}.wf-total dd{font-size:22px}
.wf-fine{margin:12px 0 0 0;font-size:13px;color:#5B6582}
.wf-proc{align-items:center;text-align:center;padding:44px 32px 36px 32px}
.wf-spin{width:56px;height:56px;border-radius:50%;border:4px solid #EAF0FF;border-top-color:#1652F0;animation:koSpin 1s linear infinite;margin-bottom:22px}
@keyframes koSpin{to{transform:rotate(360deg)}}
.wf-proc .cl-pp{max-width:420px}
.wf-safe{margin-top:22px;display:inline-flex;align-items:center;gap:8px;padding:10px 14px;border-radius:12px;background:#F5F8FF;font-size:13.5px;font-weight:500;color:#0E3BB8;text-align:left}
@media (max-width: 960px){
.wf-bal{margin-top:16px}
.wf-g{grid-template-columns:1fr 1fr}
.wf-m{padding:12px 44px 12px 12px}
.wf-fee{display:none}
.wf-fm{display:inline}
.wf-dl{padding:2px 16px}
.wf-proc{padding:40px 8px}
}
'''
SCRIPT = '''<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":820}}'>
class Component extends DCLogic {
  constructor(props) { super(props); this.state = { v: (props && props.variant) || 'amount', amt: 2500, custom: '', pm: 'card' }; }
  renderVals() {
    const S = this.state, v = S.v, out = {};
    [500, 1000, 2500, 5000].forEach((n) => { const on = S.amt === n; out['a' + n] = { on: on ? 'true' : 'false', cls: on ? 'xb-on' : '', pick: () => this.setState({ amt: n }) }; });
    out.aC = { on: S.amt === 'c' ? 'true' : 'false', cls: S.amt === 'c' ? 'xb-on' : '', pick: () => this.setState({ amt: 'c' }) };
    ['card', 'bank', 'local', 'mforge'].forEach((k) => { const on = S.pm === k; out['m_' + k] = { on: on ? 'true' : 'false', cls: on ? 'xb-on' : '', pick: () => this.setState({ pm: k }) }; });
    const n = S.amt === 'c' ? (parseInt(String(S.custom).replace(/\\D/g, ''), 10) || 0) : S.amt;
    const step = { amount: 0, method: 1, summary: 2, processing: 3 }[v];
    return Object.assign(out, {
      vAmount: v === 'amount', vMethod: v === 'method', vSummary: v === 'summary', vProc: v === 'processing',
      s0: step > 0 ? 'dn' : 'on', s1: step > 1 ? 'dn' : (step === 1 ? 'on' : ''), s2: step > 2 ? 'dn' : (step === 2 ? 'on' : ''),
      isCustom: S.amt === 'c', custom: S.custom, onCustom: (e) => this.setState({ custom: e.target.value }),
      amtTxt: n.toLocaleString('en-US') + ' Credits', usdTxt: '$' + (n / 10).toLocaleString('en-US', { minimumFractionDigits: 2 })
    });
  }
}
</script>
</body>
</html>
'''
s = head.replace('</style>', CSS + '</style>', 1)
s = re.sub(r'<title>.*?</title>', '<title>Credalio · Add Credits</title>', s)
wr('CR-WAL-FUND.dc.html', s + body + SCRIPT)

wd, wm = rd('CR-DASH-S03.dc.html'), rd('CR-CRED-002c-Mobile.dc.html')
def mob(t, h):
    t = re.sub(r'hint-size="[^"]*"', f'hint-size="390px,{h}px"', t)
    t = re.sub(r'width: \d+px; height: \d+px;', f'width: 390px; height: {h}px;', t, count=1)
    return re.sub(r'"\$preview":\{"width":\d+,"height":\d+\}', f'"$preview":{{"width":390,"height":{h}}}', t)
for n, var, hm in [('CR-WAL-002', 'amount', 844), ('CR-WAL-003', 'method', 900), ('CR-WAL-004', 'summary', 900), ('CR-WAL-005', 'processing', 844)]:
    imp = f'<dc-import name="CR-WAL-FUND" variant="{var}"'
    t = wd.replace('<dc-import name="CR-DASH-ST" variant="s03"', imp)
    wr(n + '.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} preview</title>', t))
    t = mob(wm.replace('<dc-import name="CR-CRED-002" variant="badge"', imp), hm)
    wr(n + '-Mobile.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} mobile preview</title>', t))
t = wm.replace('<dc-import name="CR-CRED-002" variant="badge"', '<dc-import name="CR-WAL-001"')
wr('CR-WAL-001-Mobile.dc.html', re.sub(r'<title>.*?</title>', '<title>CR-WAL-001 mobile preview</title>', mob(t, 960)))
print('build21 ok')
