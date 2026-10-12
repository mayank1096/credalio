# build37: not-enough-Credits loop for Creio + usage. PATCHES live CR-CREIO-BUY (variants short / covered = AI-006 / AI-006d),
# live CR-WAL-FUND (variant "ai" = AI-006b: amount step opened from Nova, returns to the purchase), live CR-WAL-OUT (variant "airet" = AI-006c),
# writes CR-CREIO-USE (= AI-007/008 usage + detail, Studio page). Asserts if already patched.
# usage: python3 build37.py <dir>  (scratch copy: build17 re-runs on import; copy back only the files printed at the end)
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build17 as B
from tipx import tip, TIP_CSS
P, rd, wr, ic, I, ARR = B.P, B.rd, B.wr, B.ic, B.I, B.ARR
OUT = []
BK18 = ic('<path d="M19 12H5"></path><path d="m11 6-6 6 6 6"></path>', 18, 2.2)
BACK = ic('<path d="M19 12H5"></path><path d="m11 6-6 6 6 6"></path>', 16, 2.2)
RET = ic('<path d="M9 14 4 9l5-5"></path><path d="M4 9h11a5 5 0 0 1 0 10h-3"></path>', 15, 2.2)
BANG = ic('<path d="M12 7v6M12 16.5v.01"></path>', 22, 2.6)
TICK = ic('<path d="m5 12.5 4.5 4.5L19 7.5"></path>', 22, 2.6)
CHEV = ic('<path d="m6 9 6 6 6-6"></path>', 15, 2.2)
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
def add_css(s, css):
    i = s.rfind('</style>', 0, s.find('</helmet>')); return s[:i] + css + s[i:]

# ======================= CR-CREIO-BUY · short / covered =======================
s = rd('CR-CREIO-BUY.dc.html')
assert 'vShort' not in s, 'CR-CREIO-BUY already patched'
s = s.replace('<div class="tk-root cl-root">', '<div class="tk-root cl-root {{rootCls}}">', 1)
s = s.replace('<b>1,150 Credits</b>', '<b>{{walTxt}}</b>', 1)
short = ('<sc-if value="{{vShort}}" hint-placeholder-val="{{false}}"><section class="cl-panel ob-in2" aria-labelledby="cb-h3"><span class="py-ic am">' + BANG + '</span>'
         '<h2 id="cb-h3" class="cl-ph">You need 20 more Credits</h2><p class="cl-pp">250,000 Creio costs 175 Credits and your wallet has 155. Add the difference and you’ll come straight back here.</p>'
         f'<div class="cl-foot"><a href="CR-CREIO-003.dc.html" class="ds-ghost cl-bk" aria-label="Back">{BK18}<span>Back</span></a><a href="CR-CREIO-006b.dc.html" class="ds-btn cl-go wf-go"><span>Add Credits</span><span class="ob-arrow">{ARR}</span></a></div></section></sc-if>')
cov = ('<sc-if value="{{vCov}}" hint-placeholder-val="{{false}}"><section class="cl-panel ob-in2" aria-labelledby="cb-h4"><span class="py-ic gr">' + TICK + '</span>'
       '<h2 id="cb-h4" class="cl-ph">Credits added. You’re covered</h2><p class="cl-pp">You’re back where you left off. 175 Credits come from your wallet, leaving 480.</p>'
       f'<div class="cl-foot"><a href="CR-CREIO-003.dc.html" class="ds-ghost cl-bk" aria-label="Back">{BK18}<span>Back</span></a><a href="CR-CREIO-005.dc.html" class="ds-btn cl-go wf-go"><span>Buy 250,000 Creio</span><span class="ob-arrow">{ARR}</span></a></div></section></sc-if>')
assert s.count('</div>\n</main>') == 1
s = s.replace('</div>\n</main>', short + cov + '</div>\n</main>', 1)
a = "const rev = v === 'confirm';"
assert a in s
s = s.replace(a, "const rev = v === 'confirm', sh = v === 'short', cv = v === 'covered', stp = rev || sh || cv;", 1)
a = "return Object.assign(out, { vAmt: !rev, vRev: rev, s0: rev ? 'dn' : 'on', s1: rev ? 'on' : '',"
assert a in s
s = s.replace(a, "return Object.assign(out, { vAmt: !stp, vRev: rev, vShort: sh, vCov: cv, s0: stp ? 'dn' : 'on', s1: stp ? 'on' : '',\n      rootCls: sh ? 'is-wait' : (cv ? 'is-ok' : ''), walTxt: sh ? '155 Credits' : (cv ? '655 Credits' : '1,150 Credits'),", 1)
s = add_css(s, """
/* AI-006 / 006d */
.py-ic{width:48px;height:48px;border-radius:50%;color:#FFFFFF;display:flex;align-items:center;justify-content:center;margin-bottom:16px}
.py-ic.am{background:#B26A00;box-shadow:0 0 0 7px #FFF3DC}
.py-ic.gr{background:#0F6B45;box-shadow:0 0 0 7px #E7F5EE}
.cl-pp{margin:8px 0 0 0;font-size:14.5px;line-height:1.55;color:#3A4566}
.is-ok .cl-glow{background:radial-gradient(60% 100% at 50% 0,rgba(15,107,69,.10),transparent 70%)}
""")
wr('CR-CREIO-BUY.dc.html', s); OUT.append('CR-CREIO-BUY.dc.html')
wrap('CR-CREIO-BUY', 'CR-CREIO-006', 'short', 844)
wrap('CR-CREIO-BUY', 'CR-CREIO-006d', 'covered', 844)

# ======================= CR-WAL-FUND · variant ai (AI-006b) =======================
s = rd('CR-WAL-FUND.dc.html')
assert 'isAi' not in s, 'CR-WAL-FUND already patched'
a = '<div class="lp-title"><span class="lp-t1" style="display: block">Credit Wallet</span></div>'
assert s.count(a) == 1
s = s.replace(a, '<div class="lp-title"><span class="lp-t1" style="display: block">{{barT}}</span></div>', 1)
a = '<a href="CR-WAL-001.dc.html" class="lp-x"'
assert s.count(a) == 1
s = s.replace(a, '<a href="{{closeHref}}" class="lp-x"', 1)
a = '<p class="cl-sub">Credits pay for validation, revalidation and other Credalio services.</p>'
assert s.count(a) == 1
s = s.replace(a, a + '<sc-if value="{{isAi}}" hint-placeholder-val="{{false}}"><span class="wf-ret">' + RET + 'Then back to your Creio purchase</span></sc-if>', 1)
s = s.replace('<b>1,150 Credits</b>', '<b>{{balT}}</b>', 1)
a = "constructor(props) { super(props); this.state = { v: (props && props.variant) || 'amount', amt: 2500, custom: '', pm: 'card' }; }"
assert a in s
s = s.replace(a, "constructor(props) { super(props); const v0 = (props && props.variant) || 'amount'; this.ai = v0 === 'ai'; this.state = { v: this.ai ? 'amount' : v0, amt: this.ai ? 500 : 2500, custom: '', pm: 'card' }; }", 1)
a = "return Object.assign(out, {"
assert s.count(a) == 1
s = s.replace(a, "return Object.assign(out, { isAi: this.ai, barT: this.ai ? 'Nova, your Copilot' : 'Credit Wallet', closeHref: this.ai ? 'CR-CREIO-006.dc.html' : 'CR-WAL-001.dc.html', balT: this.ai ? '155 Credits' : '1,150 Credits',", 1)
s = s.replace('<a href="CR-WAL-003.dc.html" class="ds-btn cl-go wf-go ">', '<a href="{{nextHref}}" class="ds-btn cl-go wf-go ">', 1)
s = s.replace("barT: this.ai ?", "nextHref: this.ai ? 'CR-CREIO-006c.dc.html' : 'CR-WAL-003.dc.html', barT: this.ai ?", 1)
s = add_css(s, """
.wf-ret{margin-top:14px;display:inline-flex;align-items:center;gap:8px;height:32px;padding:0 13px;border-radius:999px;background:#F5F8FF;border:1.5px solid #E1E9FF;color:#0E3BB8;font-size:13px;font-weight:500}
""")
wr('CR-WAL-FUND.dc.html', s); OUT.append('CR-WAL-FUND.dc.html')
wrap('CR-WAL-FUND', 'CR-CREIO-006b', 'ai', 844)

# ======================= CR-WAL-OUT · variant airet (AI-006c) =======================
s = rd('CR-WAL-OUT.dc.html')
assert 'airet' not in s, 'CR-WAL-OUT already patched'
a = "      paid: ['ko-v', 'Paid',"
assert a in s
s = s.replace(a, "      airet: ['ko-v', 'Funded', '500 Credits added', 'They’re in your wallet and ready to use.'],\n" + a, 1)
a = "const pay = v === 'paid', ret = v === 'ret';"
assert a in s
s = s.replace(a, "const pay = v === 'paid', ai = v === 'airet', ret = v === 'ret' || ai;", 1)
reps = [("nxH: pay ? 'Follow the case' : (ret ? 'Back to your validation payment' : 'Pay for validation'),",
         "nxH: pay ? 'Follow the case' : (ai ? 'Back to your Creio purchase' : (ret ? 'Back to your validation payment' : 'Pay for validation')),"),
        ("nxP: pay ? 'Requests and decisions show up in the Validation Centre.' : (ret ? '1,260 Credits for Data Analysis with SQL. You’re covered now.' : 'Data Analysis with SQL needs 1,260 Credits. You have enough now.'),",
         "nxP: pay ? 'Requests and decisions show up in the Validation Centre.' : (ai ? '250,000 Creio for 175 Credits. You’re covered now.' : (ret ? '1,260 Credits for Data Analysis with SQL. You’re covered now.' : 'Data Analysis with SQL needs 1,260 Credits. You have enough now.')),"),
        ("nxHref: pay ? 'CR-VAL-MC-001.dc.html' : (ret ? 'CR-PAY-002f.dc.html' : 'CR-PAY-002b.dc.html'),",
         "nxHref: pay ? 'CR-VAL-MC-001.dc.html' : (ai ? 'CR-CREIO-006d.dc.html' : (ret ? 'CR-PAY-002f.dc.html' : 'CR-PAY-002b.dc.html')),"),
        ("bar: pay ? 'Submit for validation' : 'Credit Wallet',", "bar: pay ? 'Submit for validation' : (ai ? 'Nova, your Copilot' : 'Credit Wallet'),")]
for x, y in reps:
    assert x in s, x[:40]
    s = s.replace(x, y, 1)
VALI = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v18M5 21h14M6 7h12"></path><path d="m6 7-3 7a3 3 0 0 0 6 0zM18 7l-3 7a3 3 0 0 0 6 0z"></path></svg>'
x = '<span class="ko-ni">' + VALI + '</span>'
assert s.count(x) == 1
s = s.replace(x, '<span class="ko-ni"><sc-if value="{{notAi}}" hint-placeholder-val="{{true}}">' + VALI + '</sc-if><sc-if value="{{isAi}}" hint-placeholder-val="{{false}}"><span class="cb-coin" aria-hidden="true"></span></sc-if></span>', 1)
for x, y in [('<b>3,650 Credits</b>', '<b>{{fdBal}}</b>'), ('$253.75 · Visa •••• 4417</span>', '{{fdPay}}</span>'),
             ("nxCta: pay ? 'Open Validation Centre' : (ret ? 'Return to payment' : 'Continue'),", "nxCta: pay ? 'Open Validation Centre' : (ai ? 'Return to purchase' : (ret ? 'Return to payment' : 'Continue')), isAi: ai, notAi: !ai, fdBal: ai ? '655 Credits' : '3,650 Credits', fdPay: ai ? '$50.00 · Visa •••• 4417' : '$253.75 · Visa •••• 4417',"),
             ("l1: pay ? 'Back to my Studio' : 'Back to wallet', l1h: pay ? 'CR-DASH-NEW.dc.html' : 'CR-WAL-001.dc.html',", "l1: pay ? 'Back to my Studio' : (ai ? 'Back to Nova' : 'Back to wallet'), l1h: pay ? 'CR-DASH-NEW.dc.html' : (ai ? 'CR-NOVA-001.dc.html' : 'CR-WAL-001.dc.html'),")]:
    assert s.count(x) == 1, x[:40]
    s = s.replace(x, y, 1)
s = s.replace('</style>', '\n.cb-coin{display:inline-block;width:22px;height:22px;border-radius:50%;background:linear-gradient(135deg,#FFE9A3,#F6C343 45%,#D08A12);box-shadow:inset 0 0 0 3px rgba(255,241,194,.6)}\n</style>', 1)
wr('CR-WAL-OUT.dc.html', s); OUT.append('CR-WAL-OUT.dc.html')
t = rd('CR-WAL-006-Mobile.dc.html')
for n, suf in [('CR-CREIO-006c', '-Mobile')]:
    t2 = t.replace('variant="funded"', 'variant="airet"').replace('CR-WAL-006', n)
    assert 'variant="airet"' in t2
    wr(n + suf + '.dc.html', t2); OUT.append(n + suf + '.dc.html')
wd2 = rd('CR-WAL-006.dc.html')
t2 = wd2.replace('variant="funded"', 'variant="airet"').replace('CR-WAL-006', 'CR-CREIO-006c')
assert 'variant="airet"' in t2
wr('CR-CREIO-006c.dc.html', t2); OUT.append('CR-CREIO-006c.dc.html')

# ======================= CR-CREIO-USE · usage + detail (AI-007 / 008) =======================
USE = [('Learning outcomes', 'Data Analysis with SQL', 'Today · 10:42', 850, 'Outcomes for Chapter 4'),
       ('Assessment help', 'Data Analysis with SQL', 'Today · 11:26', 1240, 'Suggestions for Quiz 3'),
       ('Chat with Nova', 'Dashboard', 'Yesterday · 16:15', 310, '“What should I work on next?”'),
       ('Course planning', 'Data Analysis with SQL', 'Yesterday · 14:02', 620, 'Course structure'),
       ('Content review', 'Applied AI Program', '29 Sep · 09:10', 9800, 'Whole programme review'),
       ('Content drafting', 'Data Analysis with SQL', '25 Sep · 11:00', 2100, 'Lesson 4.2 explanation')]
rows = ''.join(f'<li><a href="#" class="cu-r{" on" if i == 1 else ""}"><span class="cu-t"><b>{f}</b><span>{d} · {c}</span></span><span class="cu-w">{w}</span><span class="cu-n">−{n:,}</span></a></li>' for i, (f, c, w, n, d) in enumerate(USE))
TABS = ['All', 'Course building', 'Assessment help', 'Content review', 'Chat']
tabs = ''.join(f'<button type="button" class="sr-tb{" on" if t == "All" else ""}">{t}</button>' for t in TABS)
DET = [('Action', 'Suggestions for Quiz 3'), ('Learning experience', 'Data Analysis with SQL'), ('Applied to', 'Quiz 3 · Aggregation'), ('When', 'Today · 11:26'), ('Requested by', 'You')]
det = ('<aside class="ds-card cu-d" aria-label="Usage detail"><span class="hp-lab">Assessment help</span><span class="cu-big">' + COIN + '1,240<em>Creio</em>'
       + tip('Measured in Creio, so it never changes if our AI providers change.', 'l') + '</span><dl>' + ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in DET) + '</dl></aside>')
main = ('<main class="ds-main hp">\n<a href="CR-NOVA-001.dc.html" class="pg-back ob-in">' + BACK + 'Nova, your Copilot</a>'
        '<div class="hp-head ob-in"><div><h1 class="ds-h1">Creio usage</h1></div><button type="button" class="hp-rb cu-rng">This month' + CHEV + '</button></div>'
        '<div class="sr-tabs ob-in2" role="tablist" aria-label="Filter">' + tabs + '</div>'
        '<div class="cu-g ob-in3"><section class="ds-card cu-l" aria-label="Usage"><ul>' + rows + '</ul></section>' + det + '</div>\n</main>')
css = TIP_CSS + """
.cb-coin{display:inline-block;flex-shrink:0;width:22px;height:22px;border-radius:50%;background:linear-gradient(135deg,#FFE9A3,#F6C343 45%,#D08A12);box-shadow:inset 0 0 0 3px rgba(255,241,194,.6)}
.pg-back{display:inline-flex;align-items:center;gap:8px;margin-top:22px;font-size:14px;font-weight:500;color:#4A5578;text-decoration:none}.pg-back:hover{color:#0B1433}
.pg-back + .hp-head{padding-top:10px}
.cu-rng{align-self:center;gap:8px}.cu-rng svg{color:#5B6582}
.sr-tabs{display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;padding-bottom:2px}.sr-tabs::-webkit-scrollbar{display:none}
.sr-tb{flex-shrink:0;display:inline-flex;align-items:center;height:40px;padding:0 16px;border-radius:999px;border:1.5px solid #E6EAF3;background:#FFFFFF;font-family:inherit;font-size:14px;font-weight:500;color:#3A4566;cursor:pointer}
.sr-tb.on{background:#EAF0FF;border-color:#1652F0;color:#0E3BB8}
.cu-g{margin-top:18px;display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:24px;align-items:start}
.cu-l{padding:8px 12px}
.cu-l ul{list-style:none;margin:0;padding:0}
.cu-l li + li .cu-r{border-top:1.5px solid #F0F2F8}
.cu-r{display:grid;grid-template-columns:minmax(0,1fr) 140px 90px;align-items:center;gap:16px;padding:15px 14px;border-radius:14px;color:#0B1433;text-decoration:none}
.cu-r:hover{background:#F7F9FD}
.cu-r.on{background:#F5F8FF;box-shadow:inset 0 0 0 1.5px #D6E2FF}
.cu-l li + li .cu-r.on,.cu-l li:has(+ li .cu-r.on) .cu-r{border-color:transparent}
.cu-t{display:flex;flex-direction:column;gap:3px;min-width:0}.cu-t b{font-size:15px;font-weight:600}.cu-t > span{font-size:13.5px;color:#5B6582;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cu-w{font-size:13.5px;color:#5B6582}
.cu-n{text-align:right;font-size:15px;font-weight:600;color:#6B4E16;font-variant-numeric:tabular-nums}
.cu-d{position:sticky;top:96px;padding:24px}
.cu-big{margin-top:12px;display:flex;align-items:center;gap:10px;font-size:32px;font-weight:600;letter-spacing:-0.02em;color:#4A3300}
.cu-big .cb-coin{width:30px;height:30px}
.cu-big em{font-style:normal;font-size:15px;font-weight:500;color:#6B4E16;margin-left:-2px}
.cu-d dl{margin:22px 0 0 0;display:flex;flex-direction:column;gap:14px;padding-top:18px;border-top:1.5px solid #F0F2F8}
.cu-d dt{font-size:12.5px;font-weight:500;color:#8A93AD}.cu-d dd{margin:3px 0 0 0;font-size:14.5px;font-weight:500}
@media (max-width: 1080px){.cu-g{grid-template-columns:minmax(0,1fr)}.cu-d{position:static}}
@media (max-width: 960px){
.pg-back{margin-top:12px}
.cu-rng{align-self:flex-start}
.sr-tabs{margin:0 -16px;padding:0 16px 2px 16px}
.sr-tb{height:38px;padding:0 14px;font-size:13.5px}
.cu-g{margin-top:14px}
.cu-l{padding:4px 6px}
.cu-r{grid-template-columns:minmax(0,1fr) auto;gap:2px 12px;padding:13px 10px}
.cu-w{grid-column:1;grid-row:2;font-size:13px}
.cu-n{grid-column:2;grid-row:1 / span 2}
.cu-t > span{display:none}
.cu-d{display:none}
}
"""
B.page('CR-CREIO-USE', 'Nova · your Copilot', main, "    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }) };", css, 'Credalio · Creio usage')
OUT.append('CR-CREIO-USE.dc.html')
t = rd('CR-AI-001-Mobile.dc.html').replace('<dc-import name="CR-AI-001"', '<dc-import name="CR-CREIO-USE"').replace('CR-AI-001 mobile', 'CR-CREIO-USE mobile')
wr('CR-CREIO-USE-Mobile.dc.html', t); OUT.append('CR-CREIO-USE-Mobile.dc.html')
print('build37 ok'); print(' '.join(OUT))
