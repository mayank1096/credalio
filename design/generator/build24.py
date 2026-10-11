# build24: Earnings (CR-EARN one Studio-page source, variants paid / below = EARN-001 / 001b) and payout method setup
# (CR-PAYO one source on the COL focus shell, variants choose / paypal / handoff = PAYO-001 / 001a / 001b).
# Minimal by design: one hero, three quiet stats, one list; payout = one choice at a time. Imports build17 for page().
# usage: python3 build24.py <canvas project dir>
import re, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build17 as B
P, rd, wr, ic, I, ARR = B.P, B.rd, B.wr, B.ic, B.I, B.ARR
CHK = ic('<path d="m5 12.5 4.5 4.5L19 7.5"></path>', 13, 2.8)
LOCK = ic('<rect x="5" y="11" width="14" height="10" rx="2.5"></rect><path d="M8 11V8a4 4 0 0 1 8 0v3"></path>', 15)
wd, wm = rd('CR-DASH-S03.dc.html'), rd('CR-CRED-002c-Mobile.dc.html')
def mob(t, h):
    t = re.sub(r'hint-size="[^"]*"', f'hint-size="390px,{h}px"', t)
    t = re.sub(r'width: \d+px; height: \d+px;', f'width: 390px; height: {h}px;', t, count=1)
    return re.sub(r'"\$preview":\{"width":\d+,"height":\d+\}', f'"$preview":{{"width":390,"height":{h}}}', t)

# ======================= CR-EARN · Earnings =======================
PPL = '/_blob/27435c5526a86beb998393f8bb53a00c'
main = ('<main class="ds-main hp">\n<div class="hp-head ob-in"><div><h1 class="ds-h1">Earnings</h1><p class="hp-sub">What you’ve earned from your learning experiences.</p></div>'
        '<a href="#" class="hp-rb">Payout history</a></div>'
        '<div class="er-g">'
        '<section class="ds-card er-hero ob-in2" aria-label="Next payout"><span class="hp-lab">Next payout</span>'
        '<sc-if value="{{paid}}" hint-placeholder-val="{{true}}"><b class="er-big">$2,850.00</b><p class="er-p">Arrives in early November, automatically.</p>'
        '<div class="er-src"><span class="hp-lab">Where it comes from</span><span class="er-seg"><i style="flex:1410"></i><i style="flex:780"></i><i style="flex:430"></i><i style="flex:230"></i></span></div></sc-if>'
        '<sc-if value="{{below}}" hint-placeholder-val="{{false}}"><b class="er-big">$18.40 <em>of $25</em></b><p class="er-p">Payouts start at $25. Until then, earnings carry over to next month.</p>'
        '<div class="er-src"><span class="hp-lab">$6.60 to go</span><span class="er-bar"><i></i></span></div></sc-if>'
        '<ul class="er-l2"><sc-for list="{{rows}}" as="r" hint-placeholder-count="4"><li><i class="er-dot {{r.c}}"></i><span>{{r.t}}</span><b>{{r.v}}</b></li></sc-for></ul></section>'
        '<section class="ds-card er-to ob-in3" aria-label="Paid to"><span class="hp-lab">Paid to</span><div class="er-pm"><img src="' + PPL + '" alt="" width="40" height="40"><span><b>PayPal</b><span>ada.ononuju@example.com</span></span></div>'
        '<a href="CR-PAYO-001.dc.html" class="ds-link">Change method</a></section>'
        '<section class="ds-card er-k ob-in3" aria-label="Totals"><div><span>Pending</span><b>{{pend}}</b></div><div><span>Last payout</span><b>{{last}}</b></div><div><span>Lifetime</span><b>{{life}}</b></div></section>'
        '</div>\n</main>')
js = '''    const below = props && props.variant === 'below';
    const R = below ? [['Data Analysis with SQL', '$18.40']] : [['Data Analysis with SQL', '$1,410.00'], ['Certified Data Analyst', '$780.00'], ['Advanced SQL for Analysts', '$430.00'], ['Applied AI Program', '$230.00']];
    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }), paid: !below, below,
      pend: below ? '$6.20' : '$1,120.00', last: below ? 'None yet' : '$3,400.00 · 1 Oct', life: below ? '$18.40' : '$18,400.00',
      rows: R.map((r, i) => ({ t: r[0], v: r[1], c: 'c' + i })) };'''
css = '''
.er-g{display:grid;grid-template-columns:minmax(0,1fr) 340px;grid-template-rows:auto 1fr;gap:20px;align-items:start}
.er-hero{grid-row:span 2;align-self:stretch;padding:32px 36px 20px 36px}
.er-big{display:block;margin-top:10px;font-size:48px;font-weight:600;letter-spacing:-0.03em;line-height:1.05}
.er-big em{font-style:normal;font-size:20px;font-weight:500;color:#8A93AD;letter-spacing:0}
.er-p{margin:12px 0 0 0;font-size:15px;line-height:1.55;color:#4A5578}
.er-src{margin-top:32px;padding-top:28px;border-top:1.5px solid #F0F2F8}
.er-seg{margin-top:12px;display:flex;gap:4px;height:10px}
.er-seg i{border-radius:6px;background:#1652F0}
.er-seg i:nth-child(2){background:#5B85F5}.er-seg i:nth-child(3){background:#9DB6F8}.er-seg i:nth-child(4){background:#CFDBFB}
.er-bar{display:block;margin-top:12px;height:10px;border-radius:8px;background:#E6EAF3;overflow:hidden}
.er-bar i{display:block;width:74%;height:100%;border-radius:8px;background:#1652F0}
.er-l2{list-style:none;margin:14px 0 0 0;padding:0}
.er-l2 li{display:flex;align-items:center;gap:12px;padding:14px 0;border-top:1.5px solid #F0F2F8;font-size:15px}
.er-l2 li:first-child{border-top:0}
.er-l2 li > span{flex:1;min-width:0}
.er-l2 b{font-weight:600;font-variant-numeric:tabular-nums}
.er-dot{width:10px;height:10px;border-radius:3px;flex-shrink:0;background:#1652F0}
.er-dot.c1{background:#5B85F5}.er-dot.c2{background:#9DB6F8}.er-dot.c3{background:#CFDBFB}
.er-to{padding:24px 26px}
.er-pm{margin-top:14px;display:flex;align-items:center;gap:14px}
.er-pm img{width:40px;height:40px;padding:7px;box-sizing:border-box;border-radius:12px;border:1.5px solid #E6EAF3;background:#FFFFFF}
.er-pm > span{display:flex;flex-direction:column;gap:2px;min-width:0}
.er-pm b{font-size:16px;font-weight:600}.er-pm > span > span{font-size:14px;color:#5B6582;overflow:hidden;text-overflow:ellipsis}
.er-to .ds-link{display:inline-block;margin-top:18px;font-size:14px;font-weight:600}
.er-k{padding:10px 26px}
.er-k > div{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:16px 0;border-top:1.5px solid #F0F2F8}
.er-k > div:first-child{border-top:0}
.er-k span{font-size:14px;color:#5B6582}
.er-k b{font-size:16px;font-weight:600;font-variant-numeric:tabular-nums}
@media (max-width: 1080px){
.er-g{grid-template-columns:minmax(0,1fr)}
.er-hero{grid-row:auto}
}
@media (max-width: 960px){
.hp-head .hp-rb{display:none}
.er-g{gap:14px}
.er-hero{padding:22px 20px 10px 20px}
.er-big{font-size:36px}
.er-p{font-size:14.5px}
.er-src{margin-top:22px;padding-top:20px}
.er-l2 li{font-size:14.5px;padding:13px 0}
.er-to{padding:20px}
.er-k{padding:4px 20px}
.er-k > div{padding:14px 0}
}
'''
B.page('CR-EARN', 'Earnings & payouts', main, js, css, 'Credalio · Earnings', "{ nav: false }")
s = rd('CR-EARN.dc.html').replace('constructor(props) { super(props);', 'constructor(props) { super(props); this.props0 = props;', 1).replace('const below = props &&', 'const props = this.props0; const below = props &&', 1)
wr('CR-EARN.dc.html', s)
for n, var, hm in [('CR-EARN-001', 'paid', 940), ('CR-EARN-001b', 'below', 844)]:
    imp = f'<dc-import name="CR-EARN" variant="{var}"'
    t = wd.replace('<dc-import name="CR-DASH-ST" variant="s03"', imp)
    wr(n + '.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} preview</title>', t))
    t = mob(wm.replace('<dc-import name="CR-CRED-002" variant="badge"', imp), hm)
    wr(n + '-Mobile.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} mobile preview</title>', t))

# ======================= CR-PAYO · payout method (focus shell) =======================
col = rd('CR-COL-002.dc.html')
head = col[:col.index('<div class="tk-root')]
X = col[col.index('class="lp-x"'):]
X = X[X.index('<svg'):X.index('</a>')]
LG = {'paypal': '<img src="/_blob/27435c5526a86beb998393f8bb53a00c" alt="">', 'payoneer': '<img src="/_blob/e702b7f8a951c23451145db9309e7234" alt="">', 'tipalti': '<img class="wide" src="/_blob/467c32935cc2aeacc365afecc1891e58" alt="">',
      'ach': ic('<path d="M12 3v18"></path><path d="M16.5 7.5c-.8-1.3-2.5-2-4.5-2-2.5 0-4.2 1.3-4.2 3.2 0 4.6 9 2.4 9 7 0 1.9-1.9 3.3-4.6 3.3-2.2 0-4-.9-4.8-2.4"></path>', 20, 2)}
PM = [('paypal', 'PP', 'PayPal', 'Straight to your PayPal account, worldwide.'),
      ('payoneer', 'Po', 'Payoneer', 'To a local bank account or a prepaid Mastercard.'),
      ('tipalti', 'Ti', 'Tipalti', 'Local bank deposits, lower FX fees in some regions.'),
      ('ach', 'US', 'Direct deposit', 'U.S. bank accounts only.')]
opts = ''.join(f'<button type="button" role="radio" aria-checked="{{{{o_{k}.on}}}}" class="po-o {{{{o_{k}.cls}}}}" onClick="{{{{o_{k}.pick}}}}"><span class="po-lg">{LG[k]}</span><span class="po-t"><b>{t}</b><span>{d}</span></span><i class="xb-ck">{CHK}</i></button>' for k, lg, t, d in PM)
side = ('<aside class="cl-side ob-in"><h1 class="cl-h1 po-h">How you get paid</h1>'
        '<p class="cl-sub">Choose one method. Your earnings are sent there automatically each month.</p>'
        '<div class="po-c"><span class="hp-lab">Country</span><b>Nigeria</b><a href="#" class="ds-link">Change</a></div>'
        '<ol class="cl-steps" aria-label="Steps"><li class="{{s0}}"><i></i><span>Choose</span></li><li class="{{s1}}"><i></i><span>Connect</span></li><li class="{{s2}}"><i></i><span>Done</span></li></ol></aside>')
choose = ('<sc-if value="{{vChoose}}" hint-placeholder-val="{{true}}"><section class="cl-panel ob-in2" aria-labelledby="po-h1"><h2 id="po-h1" class="cl-ph">Choose a payout method</h2>'
          '<div class="po-l" role="radiogroup" aria-label="Payout method">' + opts + '</div>'
          '<sc-if value="{{isPaypal}}" hint-placeholder-val="{{false}}"><div class="po-x"><ol><li>Log in to PayPal</li><li>Approve Credalio to send you payouts</li><li>Come back here, connected</li></ol>'
          '<p>' + LOCK + 'We only receive your PayPal email and account status.</p></div></sc-if>'
          '<div class="cl-foot"><a href="CR-PAYO-001b.dc.html" class="ds-btn cl-go po-go {{goOff}}"><span>{{goTxt}}</span><span class="ob-arrow">' + ARR + '</span></a></div></section></sc-if>')
handoff = ('<sc-if value="{{vHand}}" hint-placeholder-val="{{false}}"><section class="po-ext ob-in2" aria-label="PayPal window"><div class="po-eh"><span class="po-lg sm">' + LG['paypal'] + '</span><b>PayPal</b><span class="po-sec">' + LOCK + 'Secure window</span></div>'
           '<div class="po-eb"><h2 class="cl-ph">Allow Credalio to pay you</h2><p class="cl-pp">Logged in as ada.ononuju@example.com</p>'
           '<ul class="po-perm"><li>' + CHK + 'Send payouts to this PayPal account</li><li>' + CHK + 'See your account name and status</li></ul>'
           '<div class="po-ef"><a href="CR-PAYO-001a.dc.html" class="ds-ghost">Cancel</a><a href="#" class="ds-btn cl-go"><span>Agree and connect</span><span class="ob-arrow">' + ARR + '</span></a></div></div>'
           '<p class="po-note">This step happens on PayPal. You’ll come straight back to Credalio.</p></section></sc-if>')
body = ('<div class="tk-root cl-root">\n<div class="tk-scene" aria-hidden="true"></div><div class="cl-glow" aria-hidden="true"></div>\n'
        '<header class="tk-top">\n<a href="CR-EARN-001.dc.html" class="lp-x" aria-label="Close">' + X + '</a>\n'
        '<div class="lp-title"><span class="lp-t1" style="display: block">Payout method</span></div>\n<span style="flex-grow: 1"></span>\n</header>\n'
        '<main class="cl">\n' + side + '\n<div class="cl-main">' + choose + handoff + '</div>\n</main>\n</div>\n</x-dc>\n')
CSS = '''
/* build24 payout method */
.hp-lab{display:block;font-size:12.5px;font-weight:500;color:#8A93AD}
.po-h{margin-top:0}
.po-c{margin-top:20px;display:flex;align-items:baseline;gap:10px}
.po-c b{font-size:15px;font-weight:600}.po-c .ds-link{font-size:13.5px;font-weight:600}
.po-l{margin-top:20px;display:flex;flex-direction:column;gap:10px}
.po-o{position:relative;display:flex;align-items:center;gap:16px;padding:16px 52px 16px 16px;border-radius:16px;border:1.5px solid #E6EAF3;background:#FFFFFF;font-family:inherit;text-align:left;color:#0B1433;cursor:pointer;transition:border-color .2s ease,background .2s ease}
.po-o:hover{border-color:#AFC1F5}
.po-lg{width:44px;height:44px;flex-shrink:0;border-radius:12px;background:#FFFFFF;border:1.5px solid #E6EAF3;box-sizing:border-box;color:#3A4566;display:flex;align-items:center;justify-content:center;font-size:13.5px;font-weight:600;letter-spacing:.02em}
.po-lg img{width:26px;height:26px;object-fit:contain}.po-lg img.wide{width:34px}.po-lg.sm img{width:20px;height:20px}
.po-lg.sm{width:32px;height:32px;border-radius:10px;font-size:11.5px}
.po-t{display:flex;flex-direction:column;gap:3px}
.po-t b{font-size:15.5px;font-weight:600}.po-t span{font-size:13.5px;color:#5B6582}
.xb-ck{display:none;position:absolute;top:50%;right:18px;margin-top:-10px;width:20px;height:20px;border-radius:50%;background:#1652F0;color:#FFFFFF;align-items:center;justify-content:center}
.xb-on{border-color:#1652F0;background:#F5F8FF;box-shadow:0 0 0 4px rgba(22,82,240,.10)}
.xb-on .xb-ck{display:inline-flex}
.xb-on .po-lg{background:#FFFFFF}
.po-o.dis{opacity:.5;pointer-events:none}
.po-x{margin-top:18px;padding:18px 20px;border-radius:16px;background:#F7F9FD}
.po-x ol{margin:0;padding:0 0 0 18px;display:flex;flex-direction:column;gap:8px;font-size:14.5px;color:#0B1433}
.po-x p{margin:14px 0 0 0;display:flex;align-items:center;gap:8px;font-size:13.5px;color:#5B6582}
.po-go{margin-left:auto}
.po-go.lp-off{background:#C9D3EC;box-shadow:none;pointer-events:none}.po-go.lp-off .ob-arrow{color:#9AA8CC}
.po-ext{border-radius:24px;border:1.5px solid #D6DDEE;background:#FFFFFF;box-shadow:0 24px 60px rgba(11,20,51,.12);overflow:hidden}
.po-eh{display:flex;align-items:center;gap:10px;padding:14px 20px;background:#F7F9FD;border-bottom:1.5px solid #E6EAF3;font-size:15px}
.po-eh b{font-weight:600}
.po-sec{margin-left:auto;display:inline-flex;align-items:center;gap:6px;font-size:13px;color:#5B6582}
.po-eb{padding:28px 28px 24px 28px}
.po-perm{list-style:none;margin:20px 0 0 0;padding:0;display:flex;flex-direction:column;gap:12px}
.po-perm li{display:flex;align-items:center;gap:10px;font-size:15px}
.po-perm svg{color:#0F6B45}
.po-ef{margin-top:28px;display:flex;justify-content:flex-end;gap:10px}
.po-note{margin:0;padding:14px 28px;border-top:1.5px solid #F0F2F8;font-size:13px;color:#5B6582}
@media (max-width: 960px){
.po-c{margin-top:16px}
.po-o{padding:14px 48px 14px 14px;gap:14px}
.po-lg{width:40px;height:40px}
.po-ext{margin:0 -4px}
.po-eb{padding:22px 18px 20px 18px}
.po-ef{flex-direction:column-reverse}.po-ef .cl-go{justify-content:space-between}
.po-note{padding:12px 18px}
}
'''
SCRIPT = '''<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":820}}'>
class Component extends DCLogic {
  constructor(props) { super(props); const v = (props && props.variant) || 'choose'; this.state = { v, sel: v === 'choose' ? '' : 'paypal' }; }
  renderVals() {
    const S = this.state, v = S.v, out = {};
    ['paypal', 'payoneer', 'tipalti', 'ach'].forEach((k) => { const on = S.sel === k; out['o_' + k] = { on: on ? 'true' : 'false', cls: (on ? 'xb-on' : '') + (k === 'ach' ? ' dis' : ''), pick: () => this.setState({ sel: k }) }; });
    const names = { paypal: 'Connect PayPal', payoneer: 'Connect Payoneer', tipalti: 'Open Tipalti setup' };
    return Object.assign(out, {
      vChoose: v !== 'handoff', vHand: v === 'handoff', isPaypal: S.sel === 'paypal' && v !== 'handoff',
      s0: v === 'choose' && !S.sel ? 'on' : 'dn', s1: (v === 'choose' && !S.sel) ? '' : 'on', s2: '',
      goTxt: names[S.sel] || 'Continue', goOff: S.sel ? '' : 'lp-off'
    });
  }
}
</script>
</body>
</html>
'''
s = head.replace('</style>', CSS + '</style>', 1)
s = re.sub(r'<title>.*?</title>', '<title>Credalio · Payout method</title>', s)
wr('CR-PAYO.dc.html', s + body + SCRIPT)
for n, var, hm in [('CR-PAYO-001', 'choose', 900), ('CR-PAYO-001a', 'paypal', 1000), ('CR-PAYO-001b', 'handoff', 844)]:
    imp = f'<dc-import name="CR-PAYO" variant="{var}"'
    t = wd.replace('<dc-import name="CR-DASH-ST" variant="s03"', imp)
    wr(n + '.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} preview</title>', t))
    t = mob(wm.replace('<dc-import name="CR-CRED-002" variant="badge"', imp), hm)
    wr(n + '-Mobile.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} mobile preview</title>', t))
print('build24 ok')
