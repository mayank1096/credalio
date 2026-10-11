# build22: CR-WAL-006 (wallet funded, standard success layout from LIVE CR-POL-002), CR-WAL-007 (transactions, Studio page),
# validation payment CR-PAY one source, variants quote / short / enough / covered (= PAY-001 / 002 / 002b / 002f) on the COL focus shell.
# Credits are cobalt, never gold. Imports build17 for page(). Only writes its own files. usage: python3 build22.py <canvas project dir>
import re, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build17 as B
P, rd, wr, ic, I, ARR = B.P, B.rd, B.wr, B.ic, B.I, B.ARR
CHK = ic('<path d="m5 12.5 4.5 4.5L19 7.5"></path>', 13, 2.8)
COIN = ic('<circle cx="12" cy="12" r="9"></circle><path d="M14.8 9.2A4 4 0 1 0 14.8 14.8"></path>', 16, 2.2)
CRED = '<span class="cr-ic" aria-hidden="true">' + COIN + '</span>'
wd, wm = rd('CR-DASH-S03.dc.html'), rd('CR-CRED-002c-Mobile.dc.html')
def mob(t, h):
    t = re.sub(r'hint-size="[^"]*"', f'hint-size="390px,{h}px"', t)
    t = re.sub(r'width: \d+px; height: \d+px;', f'width: 390px; height: {h}px;', t, count=1)
    return re.sub(r'"\$preview":\{"width":\d+,"height":\d+\}', f'"$preview":{{"width":390,"height":{h}}}', t)

# ======================= CR-WAL-006 · wallet funded =======================
p2 = rd('CR-POL-002.dc.html')
p2 = p2.replace('<a href="CR-RDY-001.dc.html" class="lp-x" aria-label="Close and go back to readiness">', '<a href="CR-WAL-001.dc.html" class="lp-x" aria-label="Close and go back to your wallet">', 1)
p2 = re.sub(r'<div class="lp-title">.*?</div>', '<div class="lp-title"><span class="lp-t1" style="display: block">Credit Wallet</span></div>', p2, count=1, flags=re.S)
a = p2.index('<div class="ko-row">'); b = p2.index('</div>\n</sc-if>', a) + 6
card = ('<div class="ko-row">\n<section class="ko-card wd-card ob-in3" aria-label="Receipt"><dl class="wd-dl">'
        '<div><dt>New balance</dt><dd class="wd-big">' + CRED + '3,650 Credits</dd></div>'
        '<div><dt>Paid</dt><dd>$253.75 · Visa •••• 4417</dd></div><div><dt>Transaction</dt><dd>TX-88531</dd></div></dl></section>\n'
        '<section class="ko-next ob-in4" aria-label="Next for you"><span class="ko-ni">' + ic(I['val'], 20) + '</span>'
        '<span class="ko-nt"><span class="ko-nl">Next for you</span><b>Pay for validation</b><span>Data Analysis with SQL needs 1,260 Credits. You have enough now.</span></span>'
        '<a href="CR-PAY-002b.dc.html" class="ds-btn sm ko-go"><span>Continue</span><span class="ob-arrow">' + ARR + '</span></a></section>\n</div>')
p2 = p2[:a] + card + p2[b:]
p2 = re.sub(r'<div class="ko-links ob-in4">.*?</div>', '<div class="ko-links ob-in4"><a href="#">Download receipt</a><span aria-hidden="true">·</span><a href="CR-WAL-001.dc.html">Back to wallet</a></div>', p2, count=1, flags=re.S)
p2 = p2.replace("const T = ['ko-v', 'Complete', 'All policies accepted', 'You can read them again any time in Creator Centre.'];",
                "const T = ['ko-v', 'Funded', '2,500 Credits added', 'They’re in your wallet and ready to use.'];")
assert '2,500 Credits added' in p2
p2 = p2.replace('</style>', '''
/* build22 WAL-006 */
.cr-ic{display:inline-flex;width:32px;height:32px;border-radius:50%;background:#EAF0FF;color:#1652F0;align-items:center;justify-content:center;flex-shrink:0}
.wd-card{padding:6px 22px}
.wd-dl{margin:0}
.wd-dl > div{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:12px 0;border-top:1.5px solid #F0F2F8}
.wd-dl > div:first-child{border-top:0}
.wd-dl dt{font-size:14px;color:#5B6582}
.wd-dl dd{margin:0;display:flex;align-items:center;gap:10px;font-size:15px;font-weight:600;text-align:right}
.wd-big{font-size:20px !important}
</style>''', 1)
p2 = re.sub(r'<title>.*?</title>', '<title>Credalio · Wallet funded</title>', p2)
wr('CR-WAL-006.dc.html', p2)
t = wm.replace('<dc-import name="CR-CRED-002" variant="badge"', '<dc-import name="CR-WAL-006"')
wr('CR-WAL-006-Mobile.dc.html', re.sub(r'<title>.*?</title>', '<title>CR-WAL-006 mobile preview</title>', t))

# ======================= CR-WAL-007 · transactions =======================
# (month, date, type key, title, sub, credits, status, ref)
TX = [('October', '1 Oct', 'fund', 'Wallet funded', 'Card · Visa •••• 4417', '+2,500', 'Completed', 'TX-88531'),
      ('September', '30 Sep', 'fund', 'Wallet funded', 'Bank transfer', '+2,500', 'Completed', 'TX-88412'),
      ('September', '14 Sep', 'val', 'Validation', 'Data Analyst Career Path · VAL-01102', '−588', 'Completed', 'VAL-01102'),
      ('September', '2 Sep', 'fund', 'Wallet funded', 'Card · Visa •••• 4417', '+1,000', 'Completed', 'TX-87120'),
      ('September', '2 Sep', 'creio', 'Creio purchase', '100,000 Creio for Nova', '−80', 'Completed', 'AIT-0112'),
      ('August', '20 Aug', 'reval', 'Revalidation', 'Advanced SQL · minor revalidation', '−180', 'Completed', 'RVL-00211'),
      ('August', '12 Aug', 'creio', 'Creio purchase', '25,000 Creio for Nova', '−25', 'Completed', 'AIT-0098'),
      ('August', '3 Aug', 'fund', 'Wallet funding', 'Card · declined, not charged', '+500', 'Failed', 'TX-85002')]
IC = {'fund': I['card'], 'val': I['val'], 'reval': I['val'], 'creio': I['ai']}
groups, cur = '', None
for m, d, k, t, sub, cr, st, ref in TX:
    if m != cur:
        if cur: groups += '</ul></section>'
        groups += f'<section class="tx-g" aria-label="{m}"><span class="hp-lab">{m}</span><ul class="ds-card tx-l">'
        cur = m
    fail = st == 'Failed'
    groups += (f'<li class="tx-r" data-f="{k}"><span class="hp-ic {"am" if fail else ("gr" if k == "fund" else "")}">{ic(IC[k], 18)}</span>'
               f'<span class="tx-t"><b>{t}</b><span>{sub}</span></span><span class="tx-d">{d}</span><span class="tx-ref">{ref}</span>'
               f'<span class="tx-st">{"<span class=vp-am>Failed</span>" if fail else ""}</span><b class="tx-a {"in" if cr.startswith("+") and not fail else ("off" if fail else "")}">{cr}</b></li>')
groups += '</ul></section>'
TABS = [('All', 8), ('Funding', 4), ('Validation', 2), ('Creio', 2)]
main_tx = ('<main class="ds-main hp">\n<div class="hp-head ob-in"><div><h1 class="ds-h1">Transactions</h1><p class="hp-sub">Every Credit in and out of your wallet.</p></div>'
           '<a href="#" class="hp-rb">Export CSV</a></div>'
           '<div class="hp-tabs ob-in2" role="tablist" aria-label="Filter"><sc-for list="{{tabs}}" as="c" hint-placeholder-count="4"><button type="button" role="tab" aria-selected="{{c.sel}}" class="hp-tab {{c.cls}}" onClick="{{c.pick}}">{{c.t}} <em>{{c.n}}</em></button></sc-for></div>'
           '<div class="ob-in3 {{fCls}}">' + groups + '</div>\n</main>')
js_tx = '''    const T = ''' + json.dumps([list(x) for x in TABS]) + ''';
    const key = { 'All': '', 'Funding': 'f-fund', 'Validation': 'f-val', 'Creio': 'f-creio' };
    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }), fCls: key[S.tab],
      tabs: T.map((x) => ({ t: x[0], n: x[1], cls: S.tab === x[0] ? 'on' : '', sel: S.tab === x[0] ? 'true' : 'false', pick: () => this.setState({ tab: x[0] }) })) };'''
css_tx = '''
.tx-g{margin-top:22px}
.tx-l{list-style:none;margin:10px 0 0 0;padding:4px 22px}
.tx-r{display:grid;grid-template-columns:40px minmax(0,1fr) 80px 110px 80px 110px;align-items:center;column-gap:16px;padding:13px 0;border-top:1.5px solid #F0F2F8}
.tx-r:first-child{border-top:0}
.tx-t{display:flex;flex-direction:column;gap:2px;min-width:0}
.tx-t b{font-size:15px;font-weight:600}.tx-t span{font-size:13px;color:#5B6582;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tx-d{font-size:13.5px;color:#3A4566}
.tx-ref{font-size:13px;color:#8A93AD;font-variant-numeric:tabular-nums}
.vp-am{display:inline-flex;align-items:center;height:26px;padding:0 10px;border-radius:999px;background:#FFF3DC;color:#8A5300;font-size:12.5px;font-weight:500}
.tx-a{justify-self:end;font-size:15.5px;font-weight:600;white-space:nowrap}
.tx-a::after{content:' Cr';font-size:12.5px;font-weight:500;color:#8A93AD}
.tx-a.in{color:#0F6B45}.tx-a.off{color:#8A93AD;text-decoration:line-through}
.f-fund .tx-r:not([data-f="fund"]),.f-val .tx-r:not([data-f="val"]):not([data-f="reval"]),.f-creio .tx-r:not([data-f="creio"]){display:none}
.f-fund .tx-g:not(:has([data-f="fund"])),.f-val .tx-g:not(:has([data-f="val"])):not(:has([data-f="reval"])),.f-creio .tx-g:not(:has([data-f="creio"])){display:none}
@media (max-width: 960px){
.hp-head .hp-rb{display:none}
.tx-g{margin-top:20px}
.tx-l{padding:2px 14px}
.tx-r{grid-template-columns:36px minmax(0,1fr) auto;row-gap:2px;column-gap:12px}
.tx-r .hp-ic{width:36px;height:36px;border-radius:11px;grid-column:1;grid-row:1 / 3}
.tx-t{grid-column:2;grid-row:1}.tx-t span{display:none}
.tx-d{grid-column:2;grid-row:2;font-size:12.5px;color:#5B6582}
.tx-ref{display:none}
.tx-st{grid-column:3;grid-row:2;justify-self:end}
.tx-st:empty{display:none}
.vp-am{height:22px;font-size:11.5px;padding:0 8px}
.tx-a{grid-column:3;grid-row:1}
}
'''
B.page('CR-WAL-007', 'Credit Wallet', main_tx, js_tx, css_tx, 'Credalio · Transactions', "{ nav: false, tab: 'All' }")
t = wm.replace('<dc-import name="CR-CRED-002" variant="badge"', '<dc-import name="CR-WAL-007"')
wr('CR-WAL-007-Mobile.dc.html', re.sub(r'<title>.*?</title>', '<title>CR-WAL-007 mobile preview</title>', mob(t, 1000)))

# ======================= CR-PAY · validation payment (focus shell) =======================
col = rd('CR-COL-002.dc.html')
head = col[:col.index('<div class="tk-root')]
X = col[col.index('class="lp-x"'):]
X = X[X.index('<svg'):X.index('</a>')]
STEPS = '<ol class="cl-steps" aria-label="Steps"><li class="{{s0}}"><i></i><span>Quote</span></li><li class="{{s1}}"><i></i><span>Credits</span></li><li class="{{s2}}"><i></i><span>Confirm</span></li></ol>'
side = ('<aside class="cl-side ob-in"><h1 class="cl-h1 py-h">Data Analysis with SQL</h1>'
        '<p class="cl-sub">Course validation · 6 chapters, 31 items and 3 assessments. Validators review it together.</p>'
        '<div class="cl-meta"><span>Course</span><span>All declarations signed</span></div>' + STEPS + '</aside>')
LINES = [('Educational validator', '400'), ('Subject matter validator · case lead', '500'), ('Assessment validator', '300'), ('Credalio service fee (5%)', '60')]
quote = ('<sc-if value="{{vQuote}}" hint-placeholder-val="{{true}}"><section class="cl-panel ob-in2" aria-labelledby="py-h1"><h2 id="py-h1" class="cl-ph">Your validation quote</h2>'
         '<dl class="py-dl">' + ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in LINES) + '<div class="py-tot"><dt>Total</dt><dd>' + CRED + '1,260 Credits</dd></div></dl>'
         '<div class="py-bal"><span>Your wallet</span><b>1,150 Credits</b></div>'
         '<div class="cl-foot"><a href="CR-PAY-002.dc.html" class="ds-btn cl-go py-go"><span>Pay with Credits</span><span class="ob-arrow">' + ARR + '</span></a></div></section></sc-if>')
def check(ok, rows, note, cta, href):
    return ('<div class="py-chk ' + ('ok' if ok else 'short') + '">' + ''.join(f'<div class="{c}"><span>{k}</span><b>{v}</b></div>' for k, v, c in rows) + '</div>'
            + (f'<p class="py-note">{note}</p>' if note else '')
            + f'<div class="cl-foot"><a href="CR-PAY-001.dc.html" class="ds-ghost cl-bk" aria-label="Back">' + ic('<path d="M19 12H5"></path><path d="m11 6-6 6 6 6"></path>', 18, 2.2) + '<span>Back</span></a>'
            + f'<a href="{href}" class="ds-btn cl-go py-go"><span>{cta}</span><span class="ob-arrow">{ARR}</span></a></div>')
short = ('<sc-if value="{{vShort}}" hint-placeholder-val="{{false}}"><section class="cl-panel ob-in2" aria-labelledby="py-h2"><span class="py-ic am">' + ic('<path d="M12 7v6M12 16.5v.01"></path>', 22, 2.6) + '</span>'
         '<h2 id="py-h2" class="cl-ph">You need 110 more Credits</h2><p class="cl-pp">Add them now and you’ll come straight back here to finish.</p>'
         + check(False, [('Your wallet', '1,150', ''), ('This validation', '1,260', ''), ('Still needed', '110', 'need')], '', 'Add Credits', 'CR-WAL-002.dc.html') + '</section></sc-if>')
enough = ('<sc-if value="{{vEnough}}" hint-placeholder-val="{{false}}"><section class="cl-panel ob-in2" aria-labelledby="py-h3"><span class="py-ic gr">' + ic('<path d="m5 12.5 4.5 4.5L19 7.5"></path>', 22, 2.6) + '</span>'
          '<h2 id="py-h3" class="cl-ph">{{enoughH}}</h2><p class="cl-pp">{{enoughP}}</p>'
          + check(True, [('Your wallet', '{{walTxt}}', ''), ('This validation', '1,260', ''), ('Left after paying', '{{leftTxt}}', 'left')], '', 'Confirm and pay 1,260 Credits', '#') + '</section></sc-if>')
body = ('<div class="tk-root cl-root {{rootCls}}">\n<div class="tk-scene" aria-hidden="true"></div><div class="cl-glow" aria-hidden="true"></div>\n'
        '<header class="tk-top">\n<a href="CR-DEC-004.dc.html" class="lp-x" aria-label="Close">' + X + '</a>\n'
        '<div class="lp-title"><span class="lp-t1" style="display: block">Submit for validation</span></div>\n<span style="flex-grow: 1"></span>\n</header>\n'
        '<main class="cl">\n' + side + '\n<div class="cl-main">' + quote + short + enough + '</div>\n</main>\n</div>\n</x-dc>\n')
CSS = '''
/* build22 validation payment */
.cr-ic{display:inline-flex;width:28px;height:28px;border-radius:50%;background:#EAF0FF;color:#1652F0;align-items:center;justify-content:center;flex-shrink:0}
.py-h{margin-top:0}
.py-dl{margin:16px 0 0 0;border:1.5px solid #E6EAF3;border-radius:18px;padding:4px 20px}
.py-dl > div{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:12px 0;border-top:1.5px solid #F0F2F8}
.py-dl > div:first-child{border-top:0}
.py-dl dt{font-size:14.5px;color:#3A4566}
.py-dl dd{margin:0;display:flex;align-items:center;gap:8px;font-size:15px;font-weight:600;font-variant-numeric:tabular-nums}
.py-dl > div:not(.py-tot) dd::after{content:' Cr';font-size:12.5px;font-weight:500;color:#8A93AD}
.py-tot{border-top:2px solid #0B1433 !important}
.py-tot dt{font-size:16px;font-weight:600;color:#0B1433}.py-tot dd{font-size:21px}
.py-bal{margin-top:12px;display:flex;align-items:center;justify-content:space-between;padding:12px 18px;border-radius:14px;background:#F5F8FF;font-size:14px;color:#3A4566}
.py-bal b{font-size:15px;color:#0B1433}
.py-go{margin-left:auto}
.py-ic{width:48px;height:48px;border-radius:50%;color:#FFFFFF;display:flex;align-items:center;justify-content:center;margin-bottom:16px}
.py-ic.am{background:#B26A00;box-shadow:0 0 0 7px #FFF3DC}.py-ic.gr{background:#0F6B45;box-shadow:0 0 0 7px #E7F5EE}
.py-chk{margin-top:18px;display:grid;grid-template-columns:repeat(3,1fr);border:1.5px solid #E6EAF3;border-radius:18px;overflow:hidden}
.py-chk > div{display:flex;flex-direction:column;gap:4px;padding:16px 18px;border-left:1.5px solid #F0F2F8}
.py-chk > div:first-child{border-left:0}
.py-chk > div > span{font-size:13px;color:#5B6582}
.py-chk b{font-size:20px;font-weight:600}
.py-chk b::after{content:' Cr';font-size:12.5px;font-weight:500;color:#8A93AD}
.py-chk .need{background:#FFF8EC}.py-chk .need b{color:#8A5300}
.py-chk .left{background:#F1FAF5}.py-chk .left b{color:#0F6B45}
.is-wait .cl-glow{background:radial-gradient(60% 100% at 50% 0,rgba(214,140,20,.10),transparent 70%)}
.is-ok .cl-glow{background:radial-gradient(60% 100% at 50% 0,rgba(15,107,69,.10),transparent 70%)}
@media (max-width: 960px){
.py-dl{padding:2px 16px}
.py-dl dt{font-size:14px}
.py-chk > div{padding:14px 12px}
.py-chk b{font-size:17px}
.py-chk > div > span{font-size:12px}
}
'''
SCRIPT = '''<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":820}}'>
class Component extends DCLogic {
  constructor(props) { super(props); this.state = { v: (props && props.variant) || 'quote' }; }
  renderVals() {
    const v = this.state.v, cov = v === 'covered';
    return {
      vQuote: v === 'quote', vShort: v === 'short', vEnough: v === 'enough' || cov,
      s0: v === 'quote' ? 'on' : 'dn', s1: v === 'quote' ? '' : 'on', s2: '',
      rootCls: v === 'short' ? 'is-wait' : (v === 'quote' ? '' : 'is-ok'),
      enoughH: cov ? 'Credits added. You’re covered' : 'You have enough Credits', enoughP: cov ? 'You’re back where you left off. Confirm to pay and open the case.' : 'Confirm to pay and open the validation case.',
      walTxt: cov ? '3,650' : '3,650', leftTxt: '2,390'
    };
  }
}
</script>
</body>
</html>
'''
s = head.replace('</style>', CSS + '</style>', 1)
s = re.sub(r'<title>.*?</title>', '<title>Credalio · Validation payment</title>', s)
wr('CR-PAY.dc.html', s + body + SCRIPT)
for n, var, hm in [('CR-PAY-001', 'quote', 900), ('CR-PAY-002', 'short', 844), ('CR-PAY-002b', 'enough', 844), ('CR-PAY-002f', 'covered', 844)]:
    imp = f'<dc-import name="CR-PAY" variant="{var}"'
    t = wd.replace('<dc-import name="CR-DASH-ST" variant="s03"', imp)
    wr(n + '.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} preview</title>', t))
    t = mob(wm.replace('<dc-import name="CR-CRED-002" variant="badge"', imp), hm)
    wr(n + '-Mobile.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} mobile preview</title>', t))
print('build22 ok')
