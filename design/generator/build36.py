# build36: Creio purchase flow. CR-CREIO-002 history (Studio page) · CR-CREIO-BUY (LIVE CR-WAL-FUND focus shell) variants pkg / custom / confirm
# (= AI-003 / AI-003c / AI-004 → boards CR-CREIO-003 / 003c / 004) · CR-CREIO-005 success (standard outcome, LIVE CR-WAL-OUT).
# usage: python3 build36.py <dir>  (scratch copy: build17 re-runs on import; copy back only the files printed at the end)
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build17 as B
from tipx import tip, TIP_CSS
P, rd, wr, ic, I, ARR = B.P, B.rd, B.wr, B.ic, B.I, B.ARR
OUT = []
BACK = ic('<path d="M19 12H5"></path><path d="m11 6-6 6 6 6"></path>', 16, 2.2)
BK18 = ic('<path d="M19 12H5"></path><path d="m11 6-6 6 6 6"></path>', 18, 2.2)
CHK = ic('<path d="m5 12.5 4.5 4.5L19 7.5"></path>', 12, 3.2)
COIN = '<span class="cb-coin" aria-hidden="true"></span>'
wd, wm = rd('CR-SET-001.dc.html'), rd('CR-SET-001-Mobile.dc.html')
def wrap(src, n, var, hm):
    for tpl, suf in [(wd, ''), (wm, '-Mobile')]:
        t = tpl.replace('<dc-import name="CR-SET" variant="account"', f'<dc-import name="{src}"' + (f' variant="{var}"' if var else '')).replace('CR-SET-001', n)
        if suf:
            t = re.sub(r'hint-size="390px,\d+px"', f'hint-size="390px,{hm}px"', t)
            t = re.sub(r'width: 390px; height: \d+px;', f'width: 390px; height: {hm}px;', t, count=1)
            t = re.sub(r'"\$preview":\{"width":390,"height":\d+\}', f'"$preview":{{"width":390,"height":{hm}}}', t)
        wr(n + suf + '.dc.html', t); OUT.append(n + suf + '.dc.html')
COINCSS = ".cb-coin{display:inline-block;flex-shrink:0;width:22px;height:22px;border-radius:50%;background:linear-gradient(135deg,#FFE9A3,#F6C343 45%,#D08A12);box-shadow:inset 0 0 0 3px rgba(255,241,194,.6)}\n"

# ======================= CR-CREIO-BUY · pkg / custom / confirm =======================
s = rd('CR-WAL-FUND.dc.html')
a0 = s.index('<header class="tk-top">'); a1 = s.index('</main>') + 7
PK = [('25,000', 25, 'For occasional help'), ('100,000', 80, 'For active course creation'), ('250,000', 175, 'For programmes and big projects')]
tiles = ''.join(f'<button type="button" role="radio" aria-checked="{{{{p{i}.on}}}}" class="wf-o cb-o {{{{p{i}.cls}}}}" onClick="{{{{p{i}.pick}}}}">'
                + ('<em class="cb-pop">Most chosen</em>' if i == 1 else '') + f'<b>{t}</b><span>Creio · {c} Credits</span><span class="cb-d">{d}</span><i class="xb-ck">{CHK}</i></button>' for i, (t, c, d) in enumerate(PK))
side = ('<aside class="cl-side ob-in"><h1 class="cl-h1 wf-h">Get more Creio</h1><p class="cl-sub">Paid with Credits from your Credit Wallet.</p>'
        '<div class="cb-bals"><div class="wf-bal cb-bal">' + COIN + '<span><span class="hp-lab">Creio</span><b>20,000</b></span></div>'
        '<div class="wf-bal"><span class="cr-ic cb-cr" aria-hidden="true">C</span><span><span class="hp-lab">Credit Wallet</span><b>1,150 Credits</b></span></div></div>'
        '<ol class="cl-steps cb-steps" aria-label="Steps"><li class="{{s0}}"><i></i><span>Amount</span></li><li class="{{s1}}"><i></i><span>Review</span></li></ol></aside>')
amount = ('<sc-if value="{{vAmt}}" hint-placeholder-val="{{true}}"><section class="cl-panel ob-in2" aria-labelledby="cb-h1"><h2 id="cb-h1" class="cl-ph">How much Creio?</h2>'
          '<div class="cb-g" role="radiogroup" aria-label="Amount">' + tiles + '</div>'
          f'<button type="button" role="radio" aria-checked="{{{{pc.on}}}}" class="wf-o cb-cu {{{{pc.cls}}}}" onClick="{{{{pc.pick}}}}"><b>Custom amount</b><span>From 10,000 Creio</span><i class="xb-ck">{CHK}</i></button>'
          '<sc-if value="{{isCustom}}" hint-placeholder-val="{{false}}"><div class="cb-in"><label class="wf-cu"><span class="sr-only">Custom amount</span><input value="{{custom}}" onChange="{{onCustom}}" placeholder="e.g. 60,000"><em>Creio</em></label>'
          '<span class="cb-rate">0.8 Credits per 1,000' + tip('Minimum 10,000 Creio, in steps of 1,000.', 'l') + '</span></div></sc-if>'
          '<div class="wf-tot"><span>You’ll get</span><b>{{getTxt}}</b><span class="wf-usd">{{costTxt}}</span></div>'
          f'<div class="cl-foot"><a href="CR-CREIO-004.dc.html" class="ds-btn cl-go wf-go"><span>Continue</span><span class="ob-arrow">{ARR}</span></a></div></section></sc-if>')
review = ('<sc-if value="{{vRev}}" hint-placeholder-val="{{false}}"><section class="cl-panel ob-in2" aria-labelledby="cb-h2"><h2 id="cb-h2" class="cl-ph">Review</h2>'
          '<dl class="wf-dl"><div><dt>Creio</dt><dd class="cb-gold">+100,000</dd></div><div><dt>Paid from Credit Wallet</dt><dd>80 Credits</dd></div>'
          '<div class="wf-total"><dt>Wallet after</dt><dd>1,070 Credits</dd></div></dl><p class="wf-fine">Creio is added right away.</p>'
          f'<div class="cl-foot"><a href="CR-CREIO-003.dc.html" class="ds-ghost cl-bk" aria-label="Back">{BK18}<span>Back</span></a><a href="CR-CREIO-005.dc.html" class="ds-btn cl-go wf-go"><span>Buy 100,000 Creio</span><span class="ob-arrow">{ARR}</span></a></div></section></sc-if>')
body = ('<header class="tk-top">\n<a href="CR-NOVA-001.dc.html" class="lp-x" aria-label="Close">' + ic('<path d="M7 7l10 10M17 7 7 17"></path>', 18, 2.2) + '</a>\n'
        '<div class="lp-title"><span class="lp-t1" style="display: block">Nova, your Copilot</span></div>\n<span style="flex-grow: 1"></span>\n</header>\n'
        '<main class="cl">' + side + '<div class="cl-main">' + amount + review + '</div>\n</main>')
s = s[:a0] + body + s[a1:]
s = s.replace('<div class="tk-root cl-root {{rootCls}}">', '<div class="tk-root cl-root">', 1)
k = s.index('class Component')
s = s[:k] + """class Component extends DCLogic {
  constructor(props) { super(props); const v = (props && props.variant) || 'pkg'; this.state = { v, pk: v === 'custom' ? 'c' : 1, custom: '60,000' }; }
  renderVals() {
    const S = this.state, v = S.v, out = {};
    const PK = [[25000, 25], [100000, 80], [250000, 175]];
    [0, 1, 2].forEach((i) => { const on = S.pk === i; out['p' + i] = { on: on ? 'true' : 'false', cls: on ? 'xb-on' : '', pick: () => this.setState({ pk: i }) }; });
    out.pc = { on: S.pk === 'c' ? 'true' : 'false', cls: S.pk === 'c' ? 'xb-on' : '', pick: () => this.setState({ pk: 'c' }) };
    const n = S.pk === 'c' ? (parseInt(String(S.custom).replace(/\\D/g, ''), 10) || 0) : PK[S.pk][0];
    const cr = S.pk === 'c' ? Math.ceil(n / 1000 * 0.8) : PK[S.pk][1];
    const rev = v === 'confirm';
    return Object.assign(out, { vAmt: !rev, vRev: rev, s0: rev ? 'dn' : 'on', s1: rev ? 'on' : '',
      isCustom: S.pk === 'c', custom: S.custom, onCustom: (e) => this.setState({ custom: e.target.value }),
      getTxt: n.toLocaleString('en-US') + ' Creio', costTxt: cr.toLocaleString('en-US') + ' Credits' });
  }
}
</script>
</body>
</html>
"""
CSS = COINCSS + TIP_CSS + """
/* CR-CREIO-BUY */
.cb-bals{margin-top:22px;display:flex;flex-direction:column;gap:14px}
.cb-bals .wf-bal{margin-top:0}
.cb-bal .cb-coin{width:36px;height:36px}
.cb-bal b{color:#4A3300}
.cb-cr{font-style:normal;font-weight:700;font-size:15px}
.cb-steps{grid-template-columns:repeat(2,minmax(0,1fr)) !important}
.cb-g{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.cb-o{position:relative;align-items:flex-start;text-align:left;padding-top:18px}
.cb-o b{font-size:22px}
.cb-d{margin-top:8px;font-size:12.5px !important;color:#5B6582 !important;line-height:1.4}
.cb-pop{position:absolute;top:-11px;left:14px;height:22px;padding:0 10px;border-radius:999px;background:#FFF1CF;border:1.5px solid #F4D98E;color:#6B4E16;font-size:11.5px;font-weight:500;font-style:normal;display:inline-flex;align-items:center}
.cb-cu{margin-top:10px;width:100%;flex-direction:row;align-items:center;gap:10px}
.cb-in{margin-top:12px;display:flex;align-items:center;gap:16px;flex-wrap:wrap}
.cb-in .wf-cu{margin-top:0;flex:1 1 220px}
.cb-rate{display:inline-flex;align-items:center;gap:6px;font-size:13px;color:#5B6582}
.cb-gold{color:#8A5A00 !important}
@media (max-width: 960px){
.cb-g{grid-template-columns:minmax(0,1fr);gap:12px}
.cb-o{flex-direction:row;align-items:baseline;gap:10px;padding:16px 16px 14px 16px}
.cb-o b{font-size:19px}
.cb-d{display:none}
.cb-bals{flex-direction:row;gap:18px}
}
"""
i = s.rfind('</style>', 0, s.find('</helmet>')); s = s[:i] + CSS + s[i:]
s = re.sub(r'<title>.*?</title>', '<title>Credalio · Get more Creio</title>', s, count=1)
wr('CR-CREIO-BUY.dc.html', s); OUT.append('CR-CREIO-BUY.dc.html')
wrap('CR-CREIO-BUY', 'CR-CREIO-003', 'pkg', 844)
wrap('CR-CREIO-BUY', 'CR-CREIO-003c', 'custom', 900)
wrap('CR-CREIO-BUY', 'CR-CREIO-004', 'confirm', 844)

# ======================= CR-CREIO-005 · success (standard outcome) =======================
s = rd('CR-WAL-OUT.dc.html')
a0, a1 = s.index('<span class="ko-pill ob-in2">'), s.index('</main>')
body = ('<span class="ko-pill ob-in2">Added</span><h1 class="lp-h1 ko-h ob-in2">100,000 Creio added</h1>'
        '<p class="ko-sub ob-in2">Nova is ready to keep helping.</p>'
        '<section class="ko-card ko-idc ob-in3 cs-c" aria-label="New balance">' + COIN + '<span class="ko-it"><b>120,000 Creio</b><span>New balance · 80 Credits from your wallet</span></span></section>'
        '<div class="ko-cta ob-in4"><a href="CR-AI-001.dc.html" class="ds-btn"><span>Back to Nova</span><span class="ob-arrow">' + ARR + '</span></a></div>'
        '<div class="ko-links ob-in4"><a href="CR-CREIO-002.dc.html">Creio history</a><span aria-hidden="true">·</span><a href="CR-DASH-NEW.dc.html">Back to my Studio</a></div>\n')
s = s[:a0] + body + s[a1:]
k = s.index('class Component')
s = s[:k] + """class Component extends DCLogic {
  renderVals() {
    return { koCls: 'ko-v', r: false, v: true, a: false, f: false, bar: 'Nova, your Copilot', closeHref: 'CR-NOVA-001.dc.html' };
  }
}
</script>
</body>
</html>
"""
s = s.replace('</style>', '\n' + COINCSS + '.cs-c{max-width:440px;width:100%;box-sizing:border-box;justify-content:flex-start;gap:14px}.cs-c .cb-coin{width:40px;height:40px}.cs-c b{color:#4A3300}\n</style>', 1)
s = re.sub(r'<title>.*?</title>', '<title>Credalio · Creio added</title>', s, count=1)
wr('CR-CREIO-005.dc.html', s); OUT.append('CR-CREIO-005.dc.html')
t = rd('CR-WAL-006-Mobile.dc.html')
t = re.sub(r'<dc-import name="CR-WAL-OUT"[^>]*?(hint-size="[^"]*")', r'<dc-import name="CR-CREIO-005" \1', t)
assert 'name="CR-CREIO-005"' in t
wr('CR-CREIO-005-Mobile.dc.html', re.sub(r'<title>.*?</title>', '<title>CR-CREIO-005 mobile preview</title>', t)); OUT.append('CR-CREIO-005-Mobile.dc.html')

# ======================= CR-CREIO-002 · history =======================
H = [('October 2026', [('20,000 Creio', 'Starter allowance', 'Free', '1 Oct', None)]),
     ('September 2026', [('100,000 Creio', 'AIT-0112', '80 Credits', '2 Sep', None)]),
     ('August 2026', [('25,000 Creio', 'AIT-0098', '25 Credits', '12 Aug', None), ('100,000 Creio', 'AIT-0097', '80 Credits', '10 Aug', 'Didn’t go through')])]
def hrow(t, i, c, d, bad):
    return (f'<li class="ch2-r{" bad" if bad else ""}">{COIN}<span class="ch2-t"><b>{t}</b><span>{i} · {c}</span></span>'
            + (f'<span class="st am">{bad}{tip("No Credits were taken.", "r")}</span>' if bad else '') + f'<span class="ch2-d">{d}</span></li>')
groups = ''.join(f'<section class="ch2-g"><span class="hp-lab">{m}</span><ul>' + ''.join(hrow(*r) for r in rows) + '</ul></section>' for m, rows in H)
main_h = ('<main class="ds-main hp">\n<a href="CR-NOVA-001.dc.html" class="pg-back ob-in">' + BACK + 'Nova, your Copilot</a>'
          '<div class="hp-head ob-in"><div><h1 class="ds-h1">Creio history</h1></div>'
          f'<a href="CR-CREIO-003.dc.html" class="ds-btn hp-btn ch2-go"><span>Get more Creio</span><span class="ob-arrow">{ARR}</span></a></div>'
          '<div class="ds-card ch2 ob-in2">' + groups + '</div>\n</main>')
css_h = COINCSS + TIP_CSS + """
.pg-back{display:inline-flex;align-items:center;gap:8px;margin-top:22px;font-size:14px;font-weight:500;color:#4A5578;text-decoration:none}.pg-back:hover{color:#0B1433}
.pg-back + .hp-head{padding-top:10px}
.ch2-go{align-self:center}
.st{display:inline-flex;align-items:center;gap:4px;height:28px;padding:0 10px 0 12px;border-radius:999px;font-size:13px;font-weight:500;white-space:nowrap}
.st.am{background:#FFF3E0;color:#9A5B00}
.ch2{padding:6px 28px 14px 28px}
.ch2-g{padding:18px 0 4px 0}.ch2-g + .ch2-g{border-top:1.5px solid #F0F2F8}
.ch2-g ul{list-style:none;margin:6px 0 0 0;padding:0}
.ch2-r{display:flex;align-items:center;gap:16px;padding:12px 0}
.ch2-r .cb-coin{width:32px;height:32px}
.ch2-r.bad .cb-coin{filter:grayscale(1);opacity:.45}
.ch2-t{flex-grow:1;min-width:0;display:flex;flex-direction:column;gap:2px}.ch2-t b{font-size:15px;font-weight:600}.ch2-t > span{font-size:13.5px;color:#5B6582}
.ch2-d{width:64px;text-align:right;font-size:13.5px;color:#5B6582}
@media (max-width: 960px){
.pg-back{margin-top:12px}
.hp-head{flex-direction:column;align-items:stretch;gap:16px}
.ch2-go{width:100%;justify-content:space-between}
.ch2{padding:2px 16px 10px 16px}
.ch2-r{gap:12px;flex-wrap:wrap}
.ch2-r .st{order:5;margin-left:44px}
}
"""
B.page('CR-CREIO-002', 'Nova · your Copilot', main_h, "    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }) };", css_h, 'Credalio · Creio history')
OUT.append('CR-CREIO-002.dc.html')
t = rd('CR-AI-001-Mobile.dc.html').replace('<dc-import name="CR-AI-001"', '<dc-import name="CR-CREIO-002"').replace('CR-AI-001 mobile', 'CR-CREIO-002 mobile')
wr('CR-CREIO-002-Mobile.dc.html', t); OUT.append('CR-CREIO-002-Mobile.dc.html')
print('build36 ok'); print(' '.join(OUT))
