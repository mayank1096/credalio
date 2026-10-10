# build16: CR-POL-001 (read & accept policies), CR-POL-002 (all accepted → next task),
# CR-DASH-ST one source for dashboard states s02 / s03 / s04 (+ wrappers CR-DASH-S02/S03/S04).
# Built from the LIVE canvas files (CR-CRED-001 task shell, CR-CRED-003 outcome, CR-DASH-NEW shell) so
# client copy, logo, Creio and scene fixes carry over. Only writes its own files.
# usage: python3 build16.py <canvas project dir>
import re, sys, os
P = sys.argv[1]
rd = lambda f: open(os.path.join(P, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(P, f), 'w', encoding='utf-8').write(s)

def ic(paths, w=20, sw=1.9):
    return f'<svg width="{w}" height="{w}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>'
ARR = ic('<path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path>', 18, 2.4)
BACK = ic('<path d="M19 12H5"></path><path d="m11 18-6-6 6-6"></path>', 16, 2.2)
CHK = ic('<path d="m5 12.5 4.5 4.5L19 7.5"></path>', 13, 3)
CHEV = ic('<path d="m6 9 6 6 6-6"></path>', 18, 2.2)
EXT = ic('<path d="M14 4h6v6"></path><path d="M20 4 10 14"></path><path d="M19 13v5a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2h5"></path>', 15, 2)
I_DOC = '<rect x="5" y="3" width="14" height="18" rx="2.5"></rect><path d="M9 8h6M9 12h6M9 16h3"></path>'
I_IP = '<circle cx="12" cy="12" r="9"></circle><path d="M14.5 9.5a3.5 3.5 0 1 0 0 5"></path>'
I_AI = '<path d="M12 3l1.9 5.6L19.5 10.5l-5.6 1.9L12 18l-1.9-5.6L4.5 10.5l5.6-1.9z"></path>'
I_VAL = '<path d="M12 3v18M5 21h14M6 7h12"></path><path d="m6 7-3 7a3 3 0 0 0 6 0zM18 7l-3 7a3 3 0 0 0 6 0z"></path>'
I_LRN = '<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"></path><path d="m9 12 2 2 4-4"></path>'
I_PAY = '<circle cx="12" cy="12" r="9"></circle><path d="M15 9.5c-.5-1-1.6-1.5-3-1.5-1.7 0-3 .9-3 2s1.3 1.7 3 2 3 .9 3 2-1.3 2-3 2c-1.4 0-2.5-.5-3-1.5M12 6v2M12 16v2"></path>'
I_ID = '<rect x="3" y="5" width="18" height="14" rx="2.5"></rect><circle cx="9" cy="11" r="2.2"></circle><path d="M5.8 16a3.4 3.4 0 0 1 6.4 0M14.5 10h4M14.5 13.5h3"></path>'
I_BOOK = '<path d="M4 19.5V5a2 2 0 0 1 2-2h14v18H6.5A2.5 2.5 0 0 1 4 18.5"></path><path d="M8 7h8"></path>'

# client content (CreatorHome reference, POLS)
POLS = [
 ('terms', I_DOC, 'Creator Terms of Service', 'v3.1', 'Your agreement with Credalio as a creator',
  ['You keep ownership of what you create; you grant Credalio a licence to host, deliver and promote it.',
   'Your account, earnings and listings can be suspended for serious or repeated policy breaches.',
   'Changes to these terms are notified 30 days in advance.']),
 ('ip', I_IP, 'Content & Intellectual Property', 'v2.0', 'What you may upload and how rights are handled',
  ['Only upload content you own, created, or have the right to use.',
   'Third-party material must be licensed, attributed and recorded in the Resource Library.',
   'Credalio responds to valid infringement notices and may remove affected content.']),
 ('ai', I_AI, 'Responsible AI Use', 'v1.2', 'How you may use AI, including your Copilot',
  ['You are responsible for anything AI helps you create; review it before adding it.',
   'Disclose substantial AI-generated content where the learner would reasonably expect to know.',
   'Never present AI output as verified fact or as another person’s work.']),
 ('val', I_VAL, 'Validation Integrity', 'v1.4', 'Honesty in validation',
  ['Declarations you make must be true and about your own contribution.',
   'Don’t contact or influence validators outside the Validation Workspace.',
   'Misrepresentation can void a validation decision and lead to account action.']),
 ('learn', I_LRN, 'Learner Protection & Conduct', 'v2.2', 'How you treat learners',
  ['Respond to learners respectfully and only through Credalio channels.',
   'Protect learner data; use it only to deliver and improve your learning experience.',
   'No harassment, discrimination or misleading claims about outcomes.']),
 ('pay', I_PAY, 'Payments, Earnings & Tax', 'v1.1', 'Getting paid',
  ['Earnings are paid to a payout account in your own verified name.',
   'You are responsible for tax on your earnings where you live.',
   'Refunds and chargebacks may be deducted from pending earnings.']),
]

# ======================= POL-001 =======================
base = rd('CR-CRED-001.dc.html')
top_old = re.search(r'<div class="lp-title">.*?</header>', base, re.S).group(0)
top_new = '<div class="lp-title"><span class="lp-t1">Creator policies</span><span class="lp-t2">Readiness · task 4 of 5</span></div>\n<span style="flex-grow: 1"></span>\n</header>'
m0, m1 = base.index('<main'), base.index('</main>') + 7
items = ''.join(
    f'<div class="pl-it {{{{p{i}.cls}}}}"><button type="button" class="pl-hd" onClick="{{{{p{i}.toggle}}}}" aria-expanded="{{{{p{i}.exp}}}}">'
    f'<span class="pl-ic">{ic(icn)}</span><span class="pl-tx"><b>{t}</b><span>{v} · {sub}</span></span>'
    f'<sc-if value="{{{{p{i}.acc}}}}" hint-placeholder-val="{{{{false}}}}"><span class="pl-ok">{CHK}<span>Accepted</span></span></sc-if>'
    f'<sc-if value="{{{{p{i}.todo}}}}" hint-placeholder-val="{{{{true}}}}"><span class="pl-chev">{CHEV}</span></sc-if></button>'
    f'<sc-if value="{{{{p{i}.open}}}}" hint-placeholder-val="{{{{false}}}}"><div class="pl-bd"><span class="pl-kl">Key points</span><ul class="pl-kp">'
    + ''.join(f'<li>{x}</li>' for x in pts) +
    f'</ul><div class="pl-ft"><a href="#" class="pl-full">Read the full policy{EXT}</a>'
    f'<button type="button" class="ds-btn pl-go" onClick="{{{{p{i}.accept}}}}"><span>I have read and accept</span><span class="ob-arrow">{ARR}</span></button></div></div></sc-if></div>'
    for i, (k, icn, t, v, sub, pts) in enumerate(POLS))
main = f'''<main class="pl">
<aside class="pl-side ob-in">
<a href="CR-RDY-001.dc.html" class="pl-back">{BACK}<span>Back to readiness</span></a>
<h1 class="pl-h1">Creator policies</h1>
<p class="pl-sub">Open each policy, read the key points, and accept it. You can read the full text at any time from Creator Centre.</p>
<div class="pl-prog" aria-label="{{{{nAcc}}}} of 6 accepted"><span class="pl-segs"><sc-for list="{{{{segs}}}}" as="g" hint-placeholder-count="6"><i class="{{{{g.c}}}}"></i></sc-for></span><span class="pl-pn"><b>{{{{nAcc}}}} of 6</b> accepted</span></div>
</aside>
<section class="pl-list ob-in2" aria-label="Policies">
{items}
</section>
</main>'''
CSS1 = '''
/* build16 POL-001 */
.pl{flex-grow:1;width:100%;max-width:1120px;margin:0 auto;box-sizing:border-box;padding:44px 32px 56px 32px;display:grid;grid-template-columns:minmax(0,380px) minmax(0,1fr);gap:56px;align-items:start}
.pl-side{position:sticky;top:104px;display:flex;flex-direction:column;align-items:flex-start}
.pl-back{display:inline-flex;align-items:center;gap:6px;font-size:14px;font-weight:600;color:#3A4566;text-decoration:none;margin-bottom:22px}
.pl-h1{margin:0;font-size:clamp(32px,3vw,40px);line-height:1.1;font-weight:600;letter-spacing:-0.03em;color:#0B1433}
.pl-sub{margin:12px 0 0 0;font-size:16px;line-height:1.6;color:#3A4566}
.pl-prog{margin-top:26px;width:100%;display:flex;flex-direction:column;gap:10px}
.pl-segs{display:grid;grid-template-columns:repeat(6,1fr);gap:6px}
.pl-segs i{height:6px;border-radius:6px;background:#E6EAF3}
.pl-segs i.on{background:#1652F0}
.pl-pn{font-size:14px;color:#5B6582}.pl-pn b{color:#0B1433;font-weight:600}
.pl-list{display:flex;flex-direction:column;gap:10px}
.pl-it{border:1.5px solid #E6EAF3;border-radius:18px;background:#FFFFFF;transition:border-color .2s ease,box-shadow .2s ease}
.pl-it.is-open{border-color:#CBD7F5;box-shadow:0 18px 44px rgba(22,82,240,.08)}
.pl-hd{width:100%;display:flex;align-items:center;gap:14px;padding:14px 18px 14px 14px;border:0;background:none;font-family:inherit;text-align:left;cursor:pointer;color:#0B1433}
.pl-ic{width:42px;height:42px;flex-shrink:0;border-radius:13px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.is-acc .pl-ic{background:#E7F5EE;color:#0F6B45}
.pl-tx{flex-grow:1;min-width:0;display:flex;flex-direction:column;gap:3px}
.pl-tx b{font-size:15.5px;font-weight:600}
.pl-tx span{font-size:13.5px;color:#5B6582;line-height:1.4}
.pl-ok{display:inline-flex;align-items:center;gap:5px;height:28px;padding:0 11px 0 9px;border-radius:999px;background:#E7F5EE;color:#0F6B45;font-size:12.5px;font-weight:500;white-space:nowrap}
.pl-chev{color:#8A93AD;display:flex;transition:transform .2s ease}
.is-open .pl-chev{transform:rotate(180deg);color:#1652F0}
.pl-bd{padding:4px 22px 20px 70px}
.pl-kl{font-size:12.5px;font-weight:500;color:#8A93AD}
.pl-kp{margin:8px 0 0 0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px}
.pl-kp li{position:relative;padding-left:18px;font-size:15px;line-height:1.55;color:#0B1433}
.pl-kp li::before{content:'';position:absolute;left:2px;top:9px;width:6px;height:6px;border-radius:50%;background:#1652F0}
.pl-ft{margin-top:18px;padding-top:16px;border-top:1.5px solid #F0F2F8;display:flex;align-items:center;justify-content:space-between;gap:16px}
.pl-full{display:inline-flex;align-items:center;gap:6px;font-size:14.5px;font-weight:600;color:#1652F0;text-decoration:none}
@media (max-width: 960px){
.pl{grid-template-columns:minmax(0,1fr);gap:22px;padding:32px 16px 40px 16px}
.pl-side{position:static}
.pl-back{margin-bottom:16px}
.pl-h1{font-size:26px}
.pl-sub{font-size:14.5px;margin-top:8px}
.pl-prog{margin-top:18px}
.pl-hd{padding:12px 14px 12px 12px;gap:12px}
.pl-ic{width:38px;height:38px;border-radius:12px}
.pl-tx b{font-size:15px}.pl-tx span{font-size:13px}
.pl-ok span{display:none}.pl-ok{width:28px;padding:0;justify-content:center}
.pl-bd{padding:2px 16px 16px 16px}
.pl-kp li{font-size:14.5px}
.pl-ft{flex-direction:column-reverse;align-items:stretch;gap:14px}
.pl-go{justify-content:space-between}
.pl-full{justify-content:center}
}
'''
SCRIPT1 = '''<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":820}}'>
class Component extends DCLogic {
  constructor(props) { super(props); this.state = { acc: { terms: true, ip: true }, open: 'ai' }; }
  renderVals() {
    const K = ['terms', 'ip', 'ai', 'val', 'learn', 'pay'];
    const S = this.state, out = {};
    K.forEach((k, i) => {
      const acc = !!S.acc[k], open = S.open === k;
      out['p' + i] = {
        acc, todo: !acc, open, exp: open ? 'true' : 'false',
        cls: (acc ? 'is-acc ' : '') + (open ? 'is-open' : ''),
        toggle: () => this.setState({ open: open ? '' : k }),
        accept: () => { const a = Object.assign({}, S.acc, { [k]: true }); const nx = K.find((q) => !a[q]); if (!nx) { window.location.href = 'CR-POL-002.dc.html'; return; } this.setState({ acc: a, open: nx }); }
      };
    });
    const n = K.filter((k) => S.acc[k]).length;
    out.nAcc = n; out.segs = K.map((k, i) => ({ c: i < n ? 'on' : '' }));
    return out;
  }
}
</script>'''
s = base.replace(top_old, top_new)
m0, m1 = s.index('<main'), s.index('</main>') + 7
s = s[:m0] + main + s[m1:]
s = s[:s.index('<script type="text/x-dc"')] + SCRIPT1 + '\n</body>\n</html>\n'
s = s.replace('@media (min-width: 961px){.tk-scene{display:none}}\n', '')
s = s.replace('</style>', CSS1 + '</style>', 1)
s = re.sub(r'<title>.*?</title>', '<title>Credalio · Creator policies</title>', s)
assert 'Secure · encrypted</span>' not in s and '{{p2.open}}' in s
wr('CR-POL-001.dc.html', s)

# ======================= POL-002 =======================
k = rd('CR-CRED-003.dc.html')
k = re.sub(r'<div class="lp-title">.*?</header>', top_new, k, count=1, flags=re.S)
r0 = k.index('<sc-if value="{{r}}" hint-placeholder-val="{{true}}">\n<div class="ko-row">'); r1 = k.index('</sc-if>', k.index('ko-go', r0)) + 8
k = k[:r0] + k[r1:]
k = k.replace('<sc-if value="{{r}}" hint-placeholder-val="{{true}}">', '<sc-if value="{{r}}" hint-placeholder-val="{{false}}">')
pol_list = '<ul class="pa-l">' + ''.join(f'<li><span class="pa-c">{CHK}</span>{t}</li>' for (_, _, t, _, _, _) in POLS) + '</ul>'
v0 = k.index('<section class="ko-card ko-idc ob-in3"'); v1 = k.index('</section>', v0) + 10
card = (f'<section class="ko-card ko-idc pa-card ob-in3" aria-label="Accepted policies"><span class="pa-h"><b>6 of 6 accepted</b><span>Today · versions saved to your account</span></span>{pol_list}'
        '<div class="ko-rd"><span class="ko-rl">Readiness</span><span class="ko-bar"><span class="ko-was"></span><span class="ko-up"></span></span><span class="ko-rv"><b>40%</b><em>+20%</em></span></div></section>')
k = k[:v0] + card + k[v1:]
k = re.sub(r'<span class="ko-ni"><svg.*?</svg></span>', '<span class="ko-ni">' + ic(I_ID, 22) + '</span>', k, flags=re.S)
k = k.replace('<b>Creator Orientation</b><span>3 of 7 modules done. Pick up at The validation case.</span>',
              '<b>Verify your identity</b><span>A government ID and a quick selfie check, through Sumsub.</span>')
k = k.replace('<a href="#" class="ds-btn sm ko-go"><span>Resume Orientation</span>', '<a href="CR-KYC-001.dc.html" class="ds-btn sm ko-go"><span>Verify my identity</span>')
k = k.replace('<a href="CR-CRED-001.dc.html">Your credentials</a>', '<a href="CR-RDY-001.dc.html">View readiness</a>')
k = re.sub(r"const T = \{.*?\}\[v\];", "const T = ['ko-v', 'Complete', 'All policies accepted', 'Thank you. You can read the full text of each policy any time in Creator Centre.'];", k, flags=re.S)
k = k.replace("this.v = (props || {}).variant || 'verified';", "this.v = 'verified';")
k = re.sub(r'<title>.*?</title>', '<title>Credalio · Creator policies accepted</title>', k)
CSS2 = '''
/* build16 POL-002 */
.pa-card{grid-template-columns:minmax(0,1fr)}
.pa-h{display:flex;align-items:baseline;justify-content:space-between;gap:12px;flex-wrap:wrap}
.pa-h b{font-size:17px;font-weight:600}.pa-h span{font-size:13px;color:#5B6582}
.pa-l{list-style:none;margin:2px 0 0 0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:9px 18px}
.pa-l li{display:flex;align-items:center;gap:9px;font-size:14px;color:#0B1433;min-width:0}
.pa-c{width:20px;height:20px;flex-shrink:0;border-radius:50%;background:#0F6B45;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.pa-c svg{width:11px;height:11px}
@media (max-width: 760px){.pa-l{grid-template-columns:1fr}}
'''
k = k.replace('</style>', CSS2 + '</style>', 1)
for bad in ['AWS', 'Resume Orientation', 'Credalio team', 'Secure · encrypted</span>']:
    assert bad not in k, bad
wr('CR-POL-002.dc.html', k)

# ======================= Dashboard states =======================
dsh = rd('CR-DASH-NEW.dc.html')
NOVA = re.search(r'<span aria-hidden="true" style="[^"]*"><img src="/_blob/b8f0756720795e1bd3b02e9c2655cb25" alt="" style="[^"]*"></span>', dsh).group(0)
NOVA36 = NOVA.replace('width: 26px; height: 26px;', 'width: 40px; height: 40px;')
sif = lambda v, body, d='false': f'<sc-if value="{{{{{v}}}}}" hint-placeholder-val="{{{{{d}}}}}">{body}</sc-if>'
btn = lambda href, label, cls='': f'<a href="{href}" class="ds-btn st-btn {cls}"><span>{label}</span><span class="ob-arrow">{ARR}</span></a>'
ghost = lambda href, label: f'<a href="{href}" class="ds-ghost st-gh">{label}</a>'
COVER = f'<span class="st-cov" aria-hidden="true">{ic(I_BOOK, 26, 1.8)}</span>'
CHS = ('<ol class="st-chs" aria-label="Chapters">' + ''.join(
    f'<li class="{c}"><span class="st-cn">{n}</span><span class="st-cl"><b>{t}</b><span>{st}</span></span></li>'
    for n, t, st, c in [(1, 'Why SQL', 'Done', 'ok'), (2, 'Selecting data', 'Done', 'ok'), (3, 'Filtering and sorting', 'Done', 'ok'),
                        (4, 'Joins', 'Needs an assessment', 'amb'), (5, 'Aggregation', 'Drafting', 'now'), (6, 'Window functions', 'Not started', '')]) + '</ol>')
cont_body = lambda primary: (
    f'<section class="ds-card st-cont {"st-hero" if primary else ""} ob-in2" aria-labelledby="st-c"><div class="st-ct">{COVER}<div class="st-cx">'
    '<span class="st-lab">Continue your work</span><h2 id="st-c">Data Analysis with SQL</h2><span class="st-meta">Course · Build phase · edited yesterday</span></div>'
    '<span class="st-pct"><b>68%</b><span>built</span></span></div>'
    '<div class="st-bar" aria-hidden="true"><span style="width: 68%"></span></div>'
    + (CHS if primary else '') +
    f'<div class="st-cf"><span class="st-next">{NOVA}<span><b>Next:</b> add an assessment to Chapter 4</span></span>'
    + (btn('CR-CREATE-002B.dc.html', 'Continue building') if primary else ghost('CR-CREATE-002B.dc.html', 'Resume')) + '</div></section>')
ATT_INV = (f'<section class="ds-card st-att ob-in2" aria-labelledby="st-a"><div class="st-sh"><h2 id="st-a">Needs your attention</h2><a href="#" class="ds-link">Notifications</a></div>'
           '<div class="st-ar"><span class="st-av" aria-hidden="true">BA</span><span class="st-at"><b>Dr. Bola Ade invited you to co-create “Financial Modelling Basics”</b>'
           '<span>Co-Creator · ABC Institute · 20% revenue share · expires in 6 days</span></span>'
           + btn('#', 'Review invitation') + '</div></section>')
ATT_DEC = ('<section class="ds-card st-att st-amb ob-in2" aria-labelledby="st-a"><div class="st-ar"><span class="st-ai" aria-hidden="true">' + ic(I_DOC, 20) + '</span>'
           '<span class="st-at"><b>Your contributor declaration is needed</b><span>Financial Modelling Basics can’t be submitted for validation until you declare your contribution.</span></span>'
           + ghost('#', 'Review') + '</div></section>')
ASG = (f'<section class="ds-card st-asg st-hero ob-in2" aria-labelledby="st-g"><div class="st-sh"><div><span class="st-lab">My assigned work</span><h2 id="st-g">Financial Modelling Basics</h2>'
       '<span class="st-meta">Co-Creator · Chapter 3, Revenue models · Lead: Dr. Bola Ade</span></div><a href="#" class="ds-link">Assigned to me</a></div>'
       '<div class="st-up"><span class="st-ui" aria-hidden="true">' + ic(I_BOOK, 22) + '</span><span class="st-ut"><span class="st-ul">Up next · due Friday</span>'
       '<b>Lesson 3.2 · Building a revenue model</b><span class="st-bar sm" aria-hidden="true"><span style="width: 40%"></span></span><span class="st-meta">In progress · 40% drafted</span></span>'
       + btn('#', 'Resume') + '</div>'
       '<ul class="st-rows"><li><span class="st-dot"></span><span class="st-rt"><b>Lesson 3.3 · Scenario analysis</b><span>Video lesson · due next Wednesday</span></span><a href="#" class="st-rb">Start</a></li>'
       '<li><span class="st-dot"></span><span class="st-rt"><b>Quiz 3 · Revenue models</b><span>Assessment · due in 2 weeks</span></span><a href="#" class="st-rb">Start</a></li></ul></section>')
NOVA_CARD = (f'<section class="st-nova nova-card ob-in3" aria-label="Nova suggests"><div class="st-nh">{NOVA36}<span><span class="st-lab">Nova suggests</span><b>{{{{nT}}}}</b></span></div>'
             '<p>{{nD}}</p><div class="st-chips"><sc-for list="{{nChips}}" as="c" hint-placeholder-count="2"><a href="CR-CREATE-002A.dc.html" class="ds-chip st-chip">{{c}}</a></sc-for></div></section>')
PATH = ('<section class="ds-card st-path ob-in3" aria-labelledby="st-p"><div class="st-sh"><h2 id="st-p">Your path to publishing</h2><span class="st-cnt">1 of 5 done</span></div>'
        '<span class="st-segs" aria-hidden="true"><i class="on"></i><i></i><i></i><i></i><i></i></span>'
        '<div class="st-pn"><span><span class="st-ul">Next</span><b>Verify your identity</b></span><a href="CR-KYC-001.dc.html" class="st-rb">Start</a></div>'
        '<a href="CR-RDY-001.dc.html" class="ds-link st-all">View readiness</a></section>')
MAIN_D = ('<main class="ds-main st">\n<div class="st-head ob-in"><p class="st-wel">{{wel}}</p><h1 class="ds-h1">{{h1}}</h1></div>\n'
          '<div class="st-grid"><div class="st-col">'
          + sif('s3', ATT_INV) + sif('s4', ATT_DEC) + sif('s4', ASG) + sif('s2', cont_body(True), 'true') + sif('s3', cont_body(False)) + sif('s4', cont_body(False)) +
          '</div><aside class="st-col st-aside">' + NOVA_CARD + PATH + '</aside></div>\n</main>')
CSS3 = '''
/* build16 dashboard states */
.st{max-width:1240px}
.st-head{padding:22px 0 18px 0}
.st-wel{margin:0 0 4px 0;font-size:15px;color:#3A4566}
.st-grid{display:grid;grid-template-columns:minmax(0,1fr) 352px;gap:20px;align-items:start}
.st-col{display:flex;flex-direction:column;gap:16px;min-width:0}
.st h2{margin:0;font-size:17px;font-weight:600;letter-spacing:-0.01em;color:#0B1433}
.st-lab{display:block;font-size:12.5px;font-weight:500;color:#8A93AD}
.st-meta{font-size:13.5px;color:#5B6582}
.st-sh{display:flex;align-items:flex-start;justify-content:space-between;gap:12px}
.st-btn{height:48px;font-size:15px;padding:0 5px 0 20px;flex-shrink:0}
.st-btn .ob-arrow{width:38px;height:38px}
.st-gh{height:44px;padding:0 20px;font-size:14.5px;flex-shrink:0}
.st-cont{padding:22px 24px}
.st-hero{border-color:#CBD7F5;box-shadow:0 18px 44px rgba(22,82,240,.08)}
.st-ct{display:flex;align-items:center;gap:16px}
.st-cov{width:60px;height:60px;flex-shrink:0;border-radius:16px;background:linear-gradient(135deg,#1652F0,#6E96FF);color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 24px rgba(22,82,240,.22)}
.st-cx{flex-grow:1;min-width:0;display:flex;flex-direction:column;gap:3px}
.st-cont h2{font-size:22px;letter-spacing:-0.02em}
.st-cont:not(.st-hero) h2{font-size:17px}
.st-cont:not(.st-hero) .st-cov{width:46px;height:46px;border-radius:13px}
.st-pct{display:flex;flex-direction:column;align-items:flex-end}
.st-pct b{font-size:26px;font-weight:600;letter-spacing:-0.02em;color:#1652F0}
.st-pct span{font-size:12.5px;color:#5B6582}
.st-cont:not(.st-hero) .st-pct b{font-size:19px}
.st-bar{display:block;margin-top:16px;height:8px;border-radius:8px;background:#E6EAF3;overflow:hidden}
.st-bar span{display:block;height:100%;border-radius:8px;background:linear-gradient(90deg,#1652F0,#6E96FF)}
.st-bar.sm{margin:8px 0 6px 0;height:6px;max-width:260px}
.st-cf{margin-top:16px;display:flex;align-items:center;justify-content:space-between;gap:16px}
.st-next{display:flex;align-items:center;gap:10px;font-size:14.5px;color:#0B1433}
.st-next b{font-weight:600}
.st-att{padding:18px 22px}
.st-ar{display:flex;align-items:center;gap:14px;margin-top:14px}
.st-amb .st-ar{margin-top:0}
.st-att.st-amb{background:#FFFBF2;border-color:#F4D98E}
.st-av{width:44px;height:44px;flex-shrink:0;border-radius:50%;background:#0F6B45;color:#FFFFFF;font-size:14.5px;font-weight:600;display:flex;align-items:center;justify-content:center}
.st-ai{width:44px;height:44px;flex-shrink:0;border-radius:14px;background:#FFF1CF;color:#8A5300;display:flex;align-items:center;justify-content:center}
.st-at{flex-grow:1;min-width:0;display:flex;flex-direction:column;gap:3px}
.st-at b{font-size:15.5px;font-weight:600;line-height:1.35}
.st-at > span{font-size:13.5px;color:#5B6582;line-height:1.45}
.st-amb .st-at > span{color:#8A5300}
.st-asg{padding:22px 24px}
.st-asg h2{font-size:22px;letter-spacing:-0.02em;margin-top:2px}
.st-up{margin-top:18px;display:flex;align-items:center;gap:16px;padding:16px 16px 16px 18px;border-radius:16px;background:#F5F8FF;border:1.5px solid #E1E9FF}
.st-ui{width:48px;height:48px;flex-shrink:0;border-radius:14px;background:#FFFFFF;color:#1652F0;display:flex;align-items:center;justify-content:center;border:1.5px solid #E1E9FF}
.st-ut{flex-grow:1;min-width:0;display:flex;flex-direction:column}
.st-ut b{font-size:16px;font-weight:600;margin-top:2px}
.st-ul{font-size:12.5px;font-weight:500;color:#8A93AD}
.st-rows{list-style:none;margin:6px 0 0 0;padding:0}
.st-rows li{display:flex;align-items:center;gap:14px;padding:14px 4px 14px 6px;border-top:1.5px solid #F0F2F8}
.st-rows li:first-child{border-top:0}
.st-dot{width:10px;height:10px;flex-shrink:0;border-radius:50%;border:2px solid #CBD3E6;margin:0 14px 0 13px}
.st-rt{flex-grow:1;min-width:0;display:flex;flex-direction:column;gap:2px}
.st-rt b{font-size:15px;font-weight:600}
.st-rt span{font-size:13.5px;color:#5B6582}
.st-rb{display:inline-flex;align-items:center;height:40px;padding:0 16px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;font-size:14px;font-weight:600;text-decoration:none;flex-shrink:0}
.st-nova{padding:20px 20px 18px 20px;border-radius:20px;border:1.5px solid #E1E9FF;background:#F5F8FF url(/_blob/d268046654a4206d2a726e62005bcc59) center / cover no-repeat}
.st-nh{display:flex;align-items:center;gap:12px}
.st-nh > span:last-child{display:flex;flex-direction:column;gap:2px}
.st-nh b{font-size:15.5px;font-weight:600;line-height:1.35}
.st-nova p{margin:10px 0 0 0;font-size:14px;line-height:1.55;color:#3A4566}
.st-chips{margin-top:14px;display:flex;flex-wrap:wrap;gap:8px}
.st-chip{text-decoration:none}
.st-path{padding:18px 20px}
.st-cnt{display:inline-flex;align-items:center;height:26px;padding:0 10px;border-radius:999px;background:#EAF0FF;color:#0E3BB8;font-size:12.5px;font-weight:500;white-space:nowrap}
.st-segs{margin-top:14px;display:grid;grid-template-columns:repeat(5,1fr);gap:5px}
.st-segs i{height:6px;border-radius:6px;background:#E6EAF3}.st-segs i.on{background:#0F6B45}
.st-pn{margin-top:14px;display:flex;align-items:center;justify-content:space-between;gap:12px}
.st-pn > span{display:flex;flex-direction:column;gap:2px}.st-pn b{font-size:15px;font-weight:600}
.st-all{margin-top:12px;font-size:14px}
.st-chs{list-style:none;margin:18px 0 0 0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
.st-chs li{display:flex;align-items:flex-start;gap:8px;padding:10px;border-radius:12px;background:#F7F9FD;border:1.5px solid #EEF1F7;min-width:0}
.st-cn{width:22px;height:22px;flex-shrink:0;border-radius:50%;background:#E6EAF3;color:#5B6582;font-size:12px;font-weight:600;display:flex;align-items:center;justify-content:center}
.st-chs .ok .st-cn{background:#0F6B45;color:#FFFFFF}
.st-chs .amb{background:#FFFBF2;border-color:#F4D98E}.st-chs .amb .st-cn{background:#F6C343;color:#4A3300}
.st-chs .now .st-cn{background:#1652F0;color:#FFFFFF}
.st-cl{display:flex;flex-direction:column;gap:1px;min-width:0}
.st-cl b{font-size:13px;font-weight:600;line-height:1.3;color:#0B1433}
.st-cl span{font-size:12px;color:#5B6582;line-height:1.3}
.st-chs .amb .st-cl span{color:#8A5300}
@media (max-width: 960px){
.st-chs{display:flex;overflow-x:auto;margin:16px -16px 0 -16px;padding:0 16px 2px 16px;scrollbar-width:none}
.st-chs li{flex:0 0 150px}
.st-chips{flex-wrap:nowrap;overflow-x:auto;margin:14px -20px 0 -20px;padding:0 20px;scrollbar-width:none}
.st-chip{flex-shrink:0}
.st-up{background:none;border:0;border-top:1.5px solid #F0F2F8;border-radius:0;padding:16px 0 4px 0}
.st-ui{display:none}
}
@media (max-width: 1100px){.st-grid{grid-template-columns:minmax(0,1fr) 300px}}
@media (max-width: 960px){
.st-head{padding:20px 0 14px 0}
.st-grid{grid-template-columns:minmax(0,1fr);gap:14px}
.st-col{gap:14px}
.st-cont,.st-asg{padding:18px 16px}
.st-att{padding:16px}
.st-cont h2,.st-asg h2{font-size:19px}
.st-cov{width:48px;height:48px;border-radius:14px}
.st-pct b{font-size:20px}
.st-cf{flex-direction:column;align-items:stretch;gap:14px}
.st-btn{width:100%;justify-content:space-between}
.st-ar{flex-wrap:wrap}
.st-ar .st-btn,.st-ar .st-gh{width:100%}
.st-up{flex-wrap:wrap;padding:14px}
.st-up .st-btn{width:100%}
.st-rows li{padding:12px 0}
.st-dot{margin:0 6px 0 6px}
.st-sh .ds-link{display:none}
}
'''
SCRIPT3 = '''<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":820}}'>
class Component extends DCLogic {
  constructor(props) { super(props); this.state = { nav: false }; this.v = (props || {}).variant || 's02'; }
  renderVals() {
    const v = this.v;
    const T = {
      s02: ['Welcome back, Ada.', 'Pick up where you left off.', 'Chapter 4 has no assessment yet', 'I can draft five questions from your lessons for you to review and edit.', ['Draft the questions', 'Suggest a project instead']],
      s03: ['Welcome back, Ada.', 'You have an invitation waiting.', 'Want a quick read of the invitation?', 'I can summarise the role, the chapter and the revenue share before you decide.', ['Summarise the invitation', 'What does a Co-Creator do?']],
      s04: ['Good to see you, Ada.', 'Your chapter is taking shape.', 'Lesson 3.2 needs one worked example', 'I can turn your revenue table into a step-by-step example learners can follow.', ['Draft the example', 'Check my lesson']]
    }[v];
    return { navCls: this.state.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !this.state.nav }),
      s2: v === 's02', s3: v === 's03', s4: v === 's04', wel: T[0], h1: T[1], nT: T[2], nD: T[3], nChips: T[4] };
  }
}
</script>'''
s = dsh
a0, a1 = s.index('<main class="ds-main">'), s.index('</main>') + 7
s = s[:a0] + MAIN_D + s[a1:]
s = s[:s.index('<script type="text/x-dc"')] + SCRIPT3 + '\n</body>\n</html>\n'
s = s.replace('</style>', CSS3 + '</style>', 1)
s = re.sub(r'<title>.*?</title>', '<title>Credalio · Creator Studio</title>', s)
wr('CR-DASH-ST.dc.html', s)

# ---------- wrappers ----------
wd = rd('CR-CRED-002c.dc.html'); wm = rd('CR-CRED-002c-Mobile.dc.html')
def wrap(name, src, var, title, w, h, mob):
    t = (wm if mob else wd)
    t = t.replace('<dc-import name="CR-CRED-002" variant="badge"', f'<dc-import name="{src}"' + (f' variant="{var}"' if var else ''))
    t = re.sub(r'hint-size="[^"]*"', f'hint-size="{w}px,{h}px"', t)
    t = re.sub(r'width: \d+px; height: \d+px;', f'width: {w}px; height: {h}px;', t, count=1)
    t = re.sub(r'"\$preview":\{"width":\d+,"height":\d+\}', f'"$preview":{{"width":{w},"height":{h}}}', t)
    t = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', t)
    wr(name + '.dc.html', t)
wrap('CR-POL-001-Mobile', 'CR-POL-001', '', 'CR-POL-001 mobile preview', 390, 844, True)
wrap('CR-POL-002-Mobile', 'CR-POL-002', '', 'CR-POL-002 mobile preview', 390, 844, True)
for n, v in [('S02', 's02'), ('S03', 's03'), ('S04', 's04')]:
    wrap('CR-DASH-' + n, 'CR-DASH-ST', v, 'Credalio · Studio state ' + n, 1440, 820, False)
    wrap('CR-DASH-' + n + '-Mobile', 'CR-DASH-ST', v, 'CR-DASH-' + n + ' mobile preview', 390, 980, True)
print('ok')
