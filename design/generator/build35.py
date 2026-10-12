# build35: CR-HELPT (support requests, Studio page) variants contact / list / conv (= HELP-003 / 005 / 006),
# CR-HELP-004 request sent (standard outcome layout, built from LIVE CR-WAL-OUT), CR-NOVA-001 Nova overview (Creio balance + usage).
# usage: python3 build35.py <dir>  (scratch copy: build17 re-runs on import; copy back only the files printed at the end)
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build17 as B
from tipx import tip, TIP_CSS
P, rd, wr, ic, I, ARR = B.P, B.rd, B.wr, B.ic, B.I, B.ARR
OUT = []
BACK = ic('<path d="M19 12H5"></path><path d="m11 6-6 6 6 6"></path>', 16, 2.2)
CHEV = ic('<path d="m6 9 6 6 6-6"></path>', 16, 2.2)
CHEVR = ic('<path d="m9 6 6 6-6 6"></path>', 16, 2.2)
CLIP = ic('<path d="m21 11-8.5 8.5a5 5 0 0 1-7-7L14 4a3.3 3.3 0 0 1 4.7 4.7l-8.5 8.5a1.7 1.7 0 0 1-2.4-2.4L15.5 7"></path>', 18, 2)
SEND = ic('<path d="M12 19V5"></path><path d="m5 12 7-7 7 7"></path>', 18, 2.4)
PLUS = ic('<path d="M12 5v14M5 12h14"></path>', 16, 2.4)
wd, wm = rd('CR-SET-001.dc.html'), rd('CR-SET-001-Mobile.dc.html')
def wrap(src, n, var, hm):
    for tpl, suf in [(wd, ''), (wm, '-Mobile')]:
        t = tpl.replace('<dc-import name="CR-SET" variant="account"', f'<dc-import name="{src}"' + (f' variant="{var}"' if var else '')).replace('CR-SET-001', n)
        if suf:
            t = re.sub(r'hint-size="390px,\d+px"', f'hint-size="390px,{hm}px"', t)
            t = re.sub(r'width: 390px; height: \d+px;', f'width: 390px; height: {hm}px;', t, count=1)
            t = re.sub(r'"\$preview":\{"width":390,"height":\d+\}', f'"$preview":{{"width":390,"height":{hm}}}', t)
        wr(n + suf + '.dc.html', t); OUT.append(n + suf + '.dc.html')
def props(name):
    s = rd(name + '.dc.html').replace('constructor(props) { super(props);', 'constructor(props) { super(props); this.props0 = props;', 1)
    wr(name + '.dc.html', s.replace('    const S = this.state;\n', '    const S = this.state, props = this.props0 || {};\n', 1))
NAVJS = "navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav })"

# ======================= CR-HELPT · contact / list / conv =======================
TOPICS = ['Technical issue', 'Creator account', 'Validation', 'Payment', 'Credit Wallet', 'Payout', 'Learning experience', 'Collaboration', 'Something else']
contact = ('<a href="CR-HELP-001.dc.html" class="pg-back ob-in">' + BACK + 'Help</a>'
           '<div class="hp-head ob-in"><div><h1 class="ds-h1">Contact support</h1><p class="hp-sub">Tell us what happened. Our team usually replies within a day.</p></div></div>'
           '<section class="ds-card ht-f ob-in2" aria-label="Your request">'
           '<label class="ht-l"><span class="ob-lab">Topic</span><div class="ob-sel ht-sel"><select class="ob-f">' + ''.join(f'<option{" selected" if t == "Technical issue" else ""}>{t}</option>' for t in TOPICS) + '</select>' + CHEV + '</div></label>'
           '<label class="ht-l"><span class="ob-lab">Subject</span><input class="ht-in" value="Video upload stops at 99%"></label>'
           '<label class="ht-l"><span class="ob-lab">What happened?</span><textarea class="ht-in ht-ta" rows="5">I’m uploading the Chapter 4 video (1.8 GB, MP4). It reaches 99% and then shows “Upload failed”. I tried twice in Chrome.</textarea></label>'
           '<div class="ht-att"><button type="button" class="ht-ab">' + CLIP + 'Add screenshots or files</button><span class="ht-an">Up to 5 files, 20 MB each</span></div>'
           '<div class="ht-ft"><span class="ht-ctx">We add some details for you' + tip('The page you came from, your browser and device, and any linked case or payment. Never passwords, card or bank details.', 'l') + '</span>'
           f'<a href="CR-HELP-004.dc.html" class="ds-btn hp-btn"><span>Send request</span><span class="ob-arrow">{ARR}</span></a></div></section>')
REQ = [('Payment declined but wallet not funded?', 'SUP-00428', 'Payment', 'Updated yesterday', 'Waiting for you', 'am', 'CR-HELP-006.dc.html'),
       ('Can’t upload a 2 GB video', 'SUP-00411', 'Technical issue', 'Resolved 22 Sep', 'Resolved', 'gr', '#'),
       ('Change my affiliation role', 'SUP-00387', 'Creator account', 'Closed 5 Sep', 'Closed', 'gy', '#')]
rows = ''.join(f'<li><a href="{h}" class="ht-r"><span class="ht-t"><b>{t}</b><span>{i} · {c} · {u}</span></span><span class="st {k}">{p}</span>{CHEVR}</a></li>' for t, i, c, u, p, k, h in REQ)
lst = ('<div class="hp-head ht-hd ob-in"><div><h1 class="ds-h1">My support requests</h1></div>'
       f'<a href="CR-HELP-003.dc.html" class="ds-btn hp-btn ht-new"><span>New request</span><span class="ob-arrow">{ARR}</span></a></div>'
       '<section class="ds-card ht-lc ob-in2" aria-label="Requests"><ul class="ht-ul">' + rows + '</ul></section>')
MSG = [('me', 'Ada Ononuju', '28 Sep', 'My card was charged for 2,500 Credits but my wallet still shows the old balance.', 'bank-sms.png'),
       ('them', 'Ifeoma · Credalio Support', 'Yesterday', 'Thanks, Ada. Our payment provider shows it as reversed, not charged. Could you share the date and the last 4 digits of the card?', '')]
msgs = ''.join(f'<div class="tm {w}"><span class="tm-w">{who} · {d}</span><div class="tm-b"><p>{t}</p>' + (f'<span class="tm-at">{CLIP}{a}</span>' if a else '') + '</div></div>' for w, who, d, t, a in MSG)
META = [('Request', 'SUP-00428'), ('Topic', 'Payment'), ('Opened', '28 Sep 2026'), ('Linked', 'Wallet top-up · 2,500 Credits')]
conv = ('<a href="CR-HELP-005.dc.html" class="pg-back ob-in">' + BACK + 'My support requests</a>'
        '<div class="hp-head ob-in"><div><h1 class="ds-h1 ht-h1">Payment declined but wallet not funded?<span class="st am">Waiting for you</span></h1></div></div>'
        '<div class="ht-g ob-in2"><section class="ds-card ht-c" aria-label="Conversation"><div class="ht-ms">' + msgs + '</div>'
        '<label class="ht-cmp"><span class="sr-only">Reply</span><button type="button" class="ht-ic" aria-label="Attach a file">' + CLIP + '</button><input placeholder="Reply to Ifeoma…"><button type="button" class="cp-go" aria-label="Send">' + SEND + '</button></label></section>'
        '<aside class="ds-card ht-m" aria-label="Request details"><dl>' + ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in META) + '</dl>'
        '<button type="button" class="hp-rb ht-res">Mark as resolved</button></aside></div>')
main = ('<main class="ds-main hp">\n<sc-if value="{{isC}}" hint-placeholder-val="{{true}}">' + contact + '</sc-if>'
        '<sc-if value="{{isL}}" hint-placeholder-val="{{false}}">' + lst + '</sc-if>'
        '<sc-if value="{{isV}}" hint-placeholder-val="{{false}}">' + conv + '</sc-if>\n</main>')
js = f"""    const v = props.variant || 'contact';
    return {{ {NAVJS}, isC: v === 'contact', isL: v === 'list', isV: v === 'conv' }};"""
css = TIP_CSS + """
.pg-back{display:inline-flex;align-items:center;gap:8px;margin-top:22px;font-size:14px;font-weight:500;color:#4A5578;text-decoration:none}.pg-back:hover{color:#0B1433}
.pg-back + .hp-head{padding-top:10px}
.st{display:inline-flex;align-items:center;height:28px;padding:0 12px;border-radius:999px;font-size:13px;font-weight:500;white-space:nowrap}
.st.am{background:#FFF3E0;color:#9A5B00}.st.gr{background:#E7F5EE;color:#0F6B45}.st.gy{background:#F1F3F8;color:#5B6582}
.ht-f{max-width:720px;padding:28px 30px 24px 30px;display:flex;flex-direction:column;gap:20px}
.ht-l{display:flex;flex-direction:column;gap:8px}
.ob-lab{font-size:14px;font-weight:600;color:#0B1433}
.ht-in,.ht-sel select{width:100%;box-sizing:border-box;height:48px;padding:0 14px;border-radius:12px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:inherit;font-size:15px;color:#0B1433;outline:none}
.ht-in:focus,.ht-sel select:focus{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.ht-sel{max-width:320px}.ht-sel select{appearance:none;-webkit-appearance:none;padding-right:40px}
.ob-sel{position:relative}.ob-sel svg{position:absolute;right:14px;top:50%;transform:translateY(-50%);pointer-events:none;color:#5B6582}
.ht-ta{height:auto;padding:12px 14px;line-height:1.55;resize:vertical}
.ht-att{display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.ht-ab{display:inline-flex;align-items:center;gap:8px;height:42px;padding:0 16px;border-radius:999px;border:1.5px dashed #CBD3E6;background:#FFFFFF;font-family:inherit;font-size:14px;font-weight:500;color:#1652F0;cursor:pointer}
.ht-an{font-size:13px;color:#8A93AD}
.ht-ft{display:flex;align-items:center;justify-content:space-between;gap:16px;padding-top:18px;border-top:1.5px solid #F0F2F8}
.ht-ctx{display:inline-flex;align-items:center;gap:6px;font-size:13.5px;color:#5B6582}
.ht-new{align-self:center}
.ht-lc{padding:6px 24px}
.ht-ul{list-style:none;margin:0;padding:0}
.ht-ul li + li{border-top:1.5px solid #F0F2F8}
.ht-r{display:flex;align-items:center;gap:16px;padding:18px 0;color:#0B1433;text-decoration:none}
.ht-r > svg{color:#CBD3E6;flex-shrink:0}
.ht-r:hover .ht-t b{color:#1652F0}
.ht-t{flex-grow:1;min-width:0;display:flex;flex-direction:column;gap:4px}.ht-t b{font-size:15.5px;font-weight:600}.ht-t > span{font-size:13.5px;color:#5B6582}
.ht-h1{display:flex;align-items:center;flex-wrap:wrap;gap:8px 14px}.ht-h1 .st{letter-spacing:0}
.ht-g{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:24px;align-items:start}
.ht-c{display:flex;flex-direction:column;min-height:440px;padding:22px 24px 20px 24px}
.ht-ms{flex-grow:1;display:flex;flex-direction:column;justify-content:flex-end;gap:18px;padding-bottom:20px}
.tm{display:flex;flex-direction:column;gap:6px;max-width:78%}
.tm.me{align-self:flex-end;align-items:flex-end}
.tm-w{font-size:12.5px;font-weight:500;color:#8A93AD}
.tm-b{padding:12px 16px;border-radius:18px 18px 18px 6px;background:#F5F7FC}
.tm.me .tm-b{border-radius:18px 18px 6px 18px;background:#EAF0FF}
.tm-b p{margin:0;font-size:14.5px;line-height:1.55}
.tm-at{margin-top:10px;display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 12px;border-radius:999px;background:#FFFFFF;font-size:13px;font-weight:500;color:#1652F0}
.tm-at svg{width:15px;height:15px}
.ht-cmp{display:flex;align-items:center;gap:8px;height:52px;padding:0 6px 0 6px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF}
.ht-cmp:focus-within{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.ht-cmp input{flex-grow:1;min-width:0;border:0;outline:none;font-family:inherit;font-size:15px;color:#0B1433;background:transparent}
.ht-ic{width:40px;height:40px;flex-shrink:0;border-radius:50%;border:0;background:transparent;color:#5B6582;display:flex;align-items:center;justify-content:center;cursor:pointer}
.cp-go{width:40px;height:40px;flex-shrink:0;border-radius:50%;border:0;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center;cursor:pointer}
.ht-m{padding:22px}
.ht-m dl{margin:0;display:flex;flex-direction:column;gap:14px}
.ht-m dt{font-size:12.5px;font-weight:500;color:#8A93AD}.ht-m dd{margin:3px 0 0 0;font-size:14.5px;font-weight:500}
.ht-res{margin-top:22px;width:100%;justify-content:center}
@media (max-width: 1080px){.ht-g{grid-template-columns:minmax(0,1fr)}}
@media (max-width: 960px){
.pg-back{margin-top:12px}
.ht-f{padding:20px 18px;gap:18px}
.ht-sel{max-width:none}
.ht-ft{flex-direction:column;align-items:stretch}
.ht-ft .hp-btn{justify-content:space-between}
.ht-ctx{justify-content:center}
.ht-hd{flex-direction:column;align-items:stretch;gap:16px}
.ht-new{width:100%;justify-content:space-between}
.ht-lc{padding:2px 16px}
.ht-r{gap:12px;padding:16px 0;flex-wrap:wrap}
.ht-r > svg{display:none}
.ht-t{flex-basis:100%}
.ht-c{min-height:0;padding:18px 16px 16px 16px}
.tm{max-width:90%}
.ht-m{padding:18px}
.ht-m dl{display:grid;grid-template-columns:1fr 1fr;gap:14px}
}
"""
B.page('CR-HELPT', '', main, js, css, 'Credalio · Support requests', "{ nav: false }")
props('CR-HELPT'); OUT.append('CR-HELPT.dc.html')
wrap('CR-HELPT', 'CR-HELP-003', 'contact', 830)
wrap('CR-HELPT', 'CR-HELP-005', 'list', 620)
wrap('CR-HELPT', 'CR-HELP-006', 'conv', 900)

# ======================= CR-HELP-004 · request sent (standard outcome layout) =======================
s = rd('CR-WAL-OUT.dc.html')
a0, a1 = s.index('<span class="ko-pill ob-in2">'), s.index('</main>')
body = ('<span class="ko-pill ob-in2">Sent</span><h1 class="lp-h1 ko-h ob-in2">Your request is with our team</h1>'
        '<p class="ko-sub ob-in2">We usually reply within a day, by email and here in Credalio.</p>'
        '<section class="ko-card ko-idc ob-in3 hs-c" aria-label="Your request"><span class="ko-it"><b>Video upload stops at 99%</b><span>SUP-00431 · Technical issue</span></span></section>'
        '<div class="ko-cta ob-in4"><a href="CR-HELP-006.dc.html" class="ds-btn"><span>View request</span><span class="ob-arrow">' + ARR + '</span></a></div>'
        '<div class="ko-links ob-in4"><a href="CR-HELP-001.dc.html">Back to Help</a><span aria-hidden="true">·</span><a href="CR-DASH-NEW.dc.html">Back to my Studio</a></div>\n')
s = s[:a0] + body + s[a1:]
k = s.index('class Component')
s = s[:k] + """class Component extends DCLogic {
  renderVals() {
    return { koCls: 'ko-v', r: false, v: true, a: false, f: false, bar: 'Contact support', closeHref: 'CR-HELP-001.dc.html' };
  }
}
</script>
</body>
</html>
"""
s = s.replace('</style>', '\n.hs-c{max-width:440px;width:100%;box-sizing:border-box;justify-content:flex-start}\n</style>', 1)
s = re.sub(r'<title>.*?</title>', '<title>Credalio · Request sent</title>', s, count=1)
wr('CR-HELP-004.dc.html', s); OUT.append('CR-HELP-004.dc.html')
t = rd('CR-WAL-006-Mobile.dc.html') if os.path.exists(os.path.join(P, 'CR-WAL-006-Mobile.dc.html')) else None
t = re.sub(r'<dc-import name="CR-WAL-OUT"[^>]*?(hint-size="[^"]*")', r'<dc-import name="CR-HELP-004" \1', t)
assert 'name="CR-HELP-004"' in t
wr('CR-HELP-004-Mobile.dc.html', re.sub(r'<title>.*?</title>', '<title>CR-HELP-004 mobile preview</title>', t)); OUT.append('CR-HELP-004-Mobile.dc.html')

# ======================= CR-NOVA-001 · Nova overview (Creio) =======================
CATS = [('Course building', 14200), ('Assessment help', 5800), ('Content review', 4100), ('Chat with Nova', 2450), ('Other', 1000)]
mx = CATS[0][1]
bars = ''.join(f'<li><span class="nv-k">{k}</span><span class="nv-bar"><i style="width: {round(v / mx * 100)}%"></i></span><b>{v:,}</b></li>' for k, v in CATS)
used = sum(v for _, v in CATS)
main_n = ('<main class="ds-main hp">\n<div class="hp-head ob-in"><div><h1 class="ds-h1">Nova, your Copilot</h1></div></div>'
          '<div class="nv-g ob-in2"><section class="ds-card nv-bal" aria-label="Creio balance"><span class="hp-lab nv-lab">Creio available' + tip('Creio only powers AI help. If you run out, you can still create everything by hand.') + '</span>'
          '<span class="nv-big"><span class="nv-coin" aria-hidden="true"></span>20,000</span><span class="nv-sub">About 130 replies from Nova' + tip('Big actions, like a full course review, always show an estimate before they use Creio.') + '</span>'
          f'<a href="#" class="ds-btn hp-btn nv-go"><span>Get more Creio</span><span class="ob-arrow">{ARR}</span></a></section>'
          f'<section class="ds-card nv-use" aria-labelledby="nv-u"><div class="nv-uh"><h2 id="nv-u">This month</h2><span class="nv-tot"><b>{used:,}</b> Creio used</span></div>'
          '<ul class="nv-l">' + bars + '</ul><a href="#" class="ds-link nv-all">See all activity</a></section></div>\n</main>')
css_n = TIP_CSS + """
.nv-g{display:grid;grid-template-columns:360px minmax(0,1fr);gap:24px;align-items:stretch}
.nv-bal{padding:28px;display:flex;flex-direction:column;align-items:flex-start;background:linear-gradient(160deg,#FFFAEB 0%,#FFFFFF 60%);border-color:#F4D98E}
.nv-lab{display:flex;align-items:center;gap:6px}
.nv-big{margin-top:14px;display:flex;align-items:center;gap:12px;font-size:44px;font-weight:600;letter-spacing:-0.03em;color:#4A3300}
.nv-coin{width:38px;height:38px;border-radius:50%;background:linear-gradient(135deg,#FFE9A3,#F6C343 45%,#D08A12);box-shadow:inset 0 0 0 4px rgba(255,241,194,.6)}
.nv-sub{margin-top:8px;display:flex;align-items:center;gap:6px;font-size:14px;color:#6B4E16}
.nv-go{margin-top:auto}
.nv-bal .nv-go{margin-top:28px}
.nv-use{padding:26px 28px 22px 28px}
.nv-uh{display:flex;align-items:baseline;justify-content:space-between;gap:16px}
.nv-uh h2{margin:0;font-size:17px;font-weight:600}
.nv-tot{font-size:14px;color:#5B6582}.nv-tot b{font-size:16px;color:#0B1433;font-weight:600}
.nv-l{list-style:none;margin:22px 0 0 0;padding:0;display:flex;flex-direction:column;gap:16px}
.nv-l li{display:grid;grid-template-columns:150px minmax(0,1fr) 70px;align-items:center;gap:16px}
.nv-k{font-size:14px;color:#3A4566}
.nv-bar{height:10px;border-radius:999px;background:#F1F3F8;overflow:hidden}.nv-bar i{display:block;height:100%;border-radius:999px;background:#1652F0}
.nv-l b{text-align:right;font-size:14px;font-weight:600;font-variant-numeric:tabular-nums}
.nv-all{display:inline-block;margin-top:22px;font-size:14px}
@media (max-width: 1080px){.nv-g{grid-template-columns:minmax(0,1fr)}}
@media (max-width: 960px){
.nv-bal{padding:22px 18px;border-radius:20px}
.nv-big{font-size:36px}.nv-coin{width:32px;height:32px}
.nv-go{width:100%;justify-content:space-between}
.nv-use{padding:20px 18px}
.nv-l li{grid-template-columns:minmax(0,1fr) 64px;gap:6px 12px}
.nv-bar{grid-column:1 / -1;grid-row:2}
}
"""
B.page('CR-NOVA-001', 'Nova · your Copilot', main_n, f"    return {{ {NAVJS} }};", css_n, 'Credalio · Nova, your Copilot')
OUT.append('CR-NOVA-001.dc.html')
t = rd('CR-AI-001-Mobile.dc.html').replace('<dc-import name="CR-AI-001"', '<dc-import name="CR-NOVA-001"').replace('CR-AI-001 mobile', 'CR-NOVA-001 mobile')
wr('CR-NOVA-001-Mobile.dc.html', t); OUT.append('CR-NOVA-001-Mobile.dc.html')
print('build35 ok'); print(' '.join(OUT))
