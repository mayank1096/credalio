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
CHS = ('<div class="st-tr"><ol class="st-chs" aria-label="Chapters">' + ''.join(
    f'<li class="{c}"><span class="st-seg"></span><span class="st-cl"><b>{n} · {t}</b><span>{st}</span></span></li>'
    for n, t, st, c in [(1, 'Why SQL', 'Done', 'ok'), (2, 'Selecting data', 'Done', 'ok'), (3, 'Filtering and sorting', 'Done', 'ok'),
                        (4, 'Joins', 'Needs an assessment', 'amb'), (5, 'Aggregation', 'Drafting', 'now'), (6, 'Window functions', 'Not started', '')])
    + '</ol></div>')
NBAND = (f'<div class="st-nb">{NOVA36}<span class="st-nt"><span class="st-lab">Nova suggests</span><b>{{{{nT}}}}</b><span>{{{{nD}}}}</span></span>'
         '<div class="st-chips"><sc-for list="{{nChips}}" as="c" hint-placeholder-count="2"><a href="CR-CREATE-002A.dc.html" class="ds-chip st-chip">{{c}}</a></sc-for></div></div>')
def cont_body(primary):
    act = (btn('CR-CREATE-002B.dc.html', 'Continue building') if primary else ghost('CR-CREATE-002B.dc.html', 'Resume'))
    return (f'<section class="ds-card st-cont {"st-hero" if primary else "st-mini"} ob-in2" aria-labelledby="st-c"><div class="st-ct">{COVER}<div class="st-cx">'
            '<span class="st-lab">Continue your work</span><h2 id="st-c">Data Analysis with SQL</h2><span class="st-meta">Course · Build phase · edited yesterday'
            + ('' if primary else '<span class="st-mnx"> · next: add an assessment to Chapter 4</span>') + '</span></div>'
            '<span class="st-pct"><b>68%</b><span>built</span></span>' + act + '</div>'
            + (CHS + NBAND if primary else '<div class="st-bar" aria-hidden="true"><span style="width: 68%"></span></div>') + '</section>')
ATT_INV = (f'<section class="ds-card st-att st-hero ob-in2" aria-labelledby="st-a"><div class="st-sh"><span class="st-lab" id="st-a">Needs your attention</span><a href="#" class="ds-link">Notifications</a></div>'
           '<div class="st-ar"><span class="st-av" aria-hidden="true">BA</span><span class="st-at"><b>Dr. Bola Ade invited you to co-create “Financial Modelling Basics”</b>'
           '<span>Co-Creator · ABC Institute · 20% revenue share · expires in 6 days</span></span>'
           + btn('#', 'Review invitation') + '</div>' + NBAND + '</section>')
ATT_DEC = ('<section class="ds-card st-att st-amb ob-in2" aria-label="Needs your attention"><div class="st-ar"><span class="st-ai" aria-hidden="true">' + ic(I_DOC, 20) + '</span>'
           '<span class="st-at"><b>Your contributor declaration is needed</b><span>Financial Modelling Basics can’t be submitted for validation until you declare your contribution.</span></span>'
           + ghost('#', 'Review') + '</div></section>')
ASG = (f'<section class="ds-card st-asg st-hero ob-in2" aria-labelledby="st-g"><div class="st-sh"><div><span class="st-lab">My assigned work</span><h2 id="st-g">Financial Modelling Basics</h2>'
       '<span class="st-meta">Co-Creator · Chapter 3, Revenue models<span class="st-mnx"> · Lead: Dr. Bola Ade</span></span></div><a href="#" class="ds-link">Assigned to me</a></div>'
       '<ul class="st-tl">'
       '<li class="hl"><span class="st-ring now" aria-hidden="true"></span><span class="st-tt"><b>Lesson 3.2 · Building a revenue model</b>'
       '<span class="st-tm"><span class="st-bar sm" aria-hidden="true"><span style="width: 40%"></span></span><span>40% drafted<i> · due Friday</i></span></span></span>'
       '<span class="st-due">Due Friday</span>' + btn('#', 'Resume') + '</li>'
       '<li><span class="st-ring" aria-hidden="true"></span><span class="st-tt"><b>Lesson 3.3 · Scenario analysis</b><span class="st-tm"><span>Video lesson<i> · due next Wednesday</i></span></span></span>'
       '<span class="st-due">Due next Wednesday</span><a href="#" class="st-rb">Start</a></li>'
       '<li><span class="st-ring" aria-hidden="true"></span><span class="st-tt"><b>Quiz 3 · Revenue models</b><span class="st-tm"><span>Assessment<i> · due in 2 weeks</i></span></span></span>'
       '<span class="st-due">Due in 2 weeks</span><a href="#" class="st-rb">Start</a></li></ul>'
       + NBAND + '</section>')
PATHW = ('<div class="st-pw ob-in2"><a href="CR-RDY-001.dc.html" class="st-pt"><span class="st-lab">Path to publishing</span><b>1 of 5 done</b></a>'
         '<span class="st-segs" aria-hidden="true"><i class="on"></i><i></i><i></i><i></i><i></i></span>'
         '<span class="st-pnx"><span class="st-lab">Next</span><b>Verify your identity</b></span><a href="CR-KYC-001.dc.html" class="st-rb">Start</a></div>')
I_READ = '<path d="M2 5h7a3 3 0 0 1 3 3v12a2 2 0 0 0-2-2H2z"></path><path d="M22 5h-7a3 3 0 0 0-3 3v12a2 2 0 0 1 2-2h8z"></path>'
GUIDES = lambda items: ('<section class="st-gd ob-in3" aria-labelledby="st-gh"><div class="st-sh"><span class="st-lab" id="st-gh">Helpful right now</span><a href="CR-CTR-001.dc.html" class="ds-link">Creator Centre</a></div><div class="st-gl">'
    + ''.join(f'<a href="CR-CTR-001.dc.html" class="st-gc"><span class="st-gi">{ic(I_READ, 18)}</span><span><b>{t}</b><span>{d}</span></span></a>' for t, d in items) + '</div></section>')
G2 = GUIDES([('Writing good assessment questions', 'Guide · 6 min read'), ('What validators look for', 'Guide · 5 min read'), ('Using real datasets in lessons', 'Guide · 4 min read')])
G3 = GUIDES([('Co-creating on Credalio', 'Guide · 5 min read'), ('How revenue shares work', 'Guide · 4 min read'), ('Contributor declarations', 'Guide · 3 min read')])
MAIN_D = ('<main class="ds-main st">\n<div class="st-head"><div class="ob-in"><p class="st-wel">{{wel}}</p><h1 class="ds-h1">{{h1}}</h1></div>' + PATHW + '</div>\n'
          '<div class="st-col">' + sif('s3', ATT_INV) + sif('s4', ATT_DEC) + sif('s4', ASG) + sif('s2', cont_body(True), 'true') + sif('s3', cont_body(False)) + sif('s4', cont_body(False)) + sif('s2', G2, 'true') + sif('s3', G3) +
          '</div>\n</main>')
CSS3 = """
/* build16 dashboard states v2: full-width focus card, Nova band inside, path strip in the header */
.st{max-width:1240px}
.st-head{display:flex;align-items:flex-end;justify-content:space-between;gap:24px;padding:22px 0 20px 0}
.st-wel{margin:0 0 4px 0;font-size:15px;color:#3A4566}
.st-col{display:flex;flex-direction:column;gap:16px;min-width:0}
.st h2{margin:0;font-size:17px;font-weight:600;letter-spacing:-0.01em;color:#0B1433}
.st-lab{display:block;font-size:12.5px;font-weight:500;color:#8A93AD}
.st-meta{font-size:13.5px;color:#5B6582}
.st-sh{display:flex;align-items:flex-start;justify-content:space-between;gap:12px}
.st-btn{height:48px;font-size:15px;padding:0 5px 0 20px;flex-shrink:0}
.st-btn .ob-arrow{width:38px;height:38px}
.st-gh{height:44px;padding:0 20px;font-size:14.5px;flex-shrink:0}
.st-rb{display:inline-flex;align-items:center;height:40px;padding:0 16px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;font-size:14px;font-weight:600;text-decoration:none;flex-shrink:0}
/* path strip */
.st-pw{display:flex;align-items:center;gap:18px;padding:12px 12px 12px 18px;border-radius:18px;background:#FFFFFF;border:1.5px solid #E6EAF3;flex-shrink:0}
.st-pt{display:flex;flex-direction:column;gap:2px;text-decoration:none;color:#0B1433}
.st-pt b,.st-pnx b{font-size:14.5px;font-weight:600;white-space:nowrap}
.st-segs{display:grid;grid-template-columns:repeat(5,22px);gap:4px}
.st-segs i{height:6px;border-radius:6px;background:#E6EAF3}.st-segs i.on{background:#0F6B45}
.st-pnx{display:flex;flex-direction:column;gap:2px;padding-left:18px;border-left:1.5px solid #EEF1F7}
/* focus cards */
.st-hero{padding:24px 26px 0 26px;border-color:#CBD7F5;box-shadow:0 18px 44px rgba(22,82,240,.08);overflow:hidden}
.st-mini{padding:18px 22px}
.st-ct{display:flex;align-items:center;gap:16px}
.st-cov{width:60px;height:60px;flex-shrink:0;border-radius:16px;background:linear-gradient(135deg,#1652F0,#6E96FF);color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 24px rgba(22,82,240,.22)}
.st-mini .st-cov{width:46px;height:46px;border-radius:13px;box-shadow:none}
.st-cx{flex-grow:1;min-width:0;display:flex;flex-direction:column;gap:3px}
.st-hero h2{font-size:24px;letter-spacing:-0.02em}
.st-pct{display:flex;flex-direction:column;align-items:flex-end;margin-right:8px}
.st-pct b{font-size:26px;font-weight:600;letter-spacing:-0.02em;color:#1652F0}
.st-pct span{font-size:12.5px;color:#5B6582}
.st-mini .st-pct b{font-size:19px}
.st-bar{display:block;margin-top:18px;height:8px;border-radius:8px;background:#E6EAF3;overflow:hidden}
.st-mini .st-bar{margin-top:14px;height:6px}
.st-bar span{display:block;height:100%;border-radius:8px;background:linear-gradient(90deg,#1652F0,#6E96FF)}
.st-bar.sm{margin:10px 0 6px 0;height:6px;width:100%;max-width:320px}
.st-chs .ok .st-cl b{font-size:13.5px;font-weight:600;line-height:1.3;color:#0B1433}
.st-cl span{font-size:12.5px;color:#5B6582;line-height:1.3}
.st-chs .amb .st-cl span{color:#8A5300}
/* Nova band at the foot of the focus card */
.st-nb{margin:22px -26px 0 -26px;padding:16px 26px;display:flex;align-items:center;gap:14px;background:#F5F8FF url(/_blob/d268046654a4206d2a726e62005bcc59) center / cover no-repeat;border-top:1.5px solid #E1E9FF}
.st-nt{flex-grow:1;min-width:0;display:flex;flex-direction:column;gap:2px}
.st-nt b{font-size:15px;font-weight:600}
.st-nt > span:last-child{font-size:13.5px;color:#3A4566;line-height:1.45}
.st-chips{display:flex;gap:8px;flex-shrink:0}
.st-chip{text-decoration:none;white-space:nowrap;background:#FFFFFF}
/* attention */
.st-att.st-hero{padding-top:18px}
.st-ar{display:flex;align-items:center;gap:14px;margin-top:12px}
.st-amb{padding:16px 20px}
.st-amb .st-ar{margin-top:0}
.st-att.st-amb{background:#FFFBF2;border-color:#F4D98E}
.st-av{width:48px;height:48px;flex-shrink:0;border-radius:50%;background:#0F6B45;color:#FFFFFF;font-size:15px;font-weight:600;display:flex;align-items:center;justify-content:center}
.st-ai{width:44px;height:44px;flex-shrink:0;border-radius:14px;background:#FFF1CF;color:#8A5300;display:flex;align-items:center;justify-content:center}
.st-at{flex-grow:1;min-width:0;display:flex;flex-direction:column;gap:3px}
.st-at b{font-size:17px;font-weight:600;line-height:1.35}
.st-amb .st-at b{font-size:15.5px}
.st-at > span{font-size:13.5px;color:#5B6582;line-height:1.45}
.st-amb .st-at > span{color:#8A5300}
/* assigned work */
.st-asg h2{margin-top:2px}
.st-ab{margin-top:18px;display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:24px;align-items:start}
.st-up{display:flex;flex-direction:column;align-items:flex-start;padding:18px 20px;border-radius:16px;background:#F5F8FF;border:1.5px solid #E1E9FF}
.st-up b{font-size:17px;font-weight:600;margin-top:3px}
.st-up .st-btn{margin-top:14px}
.st-ul{font-size:12.5px;font-weight:500;color:#8A93AD}
.st-rows{list-style:none;margin:0;padding:0}
.st-rows li{display:flex;align-items:center;gap:12px;padding:14px 0;border-top:1.5px solid #F0F2F8}
.st-rows li:first-child{border-top:0;padding-top:6px}
.st-dot{width:10px;height:10px;flex-shrink:0;border-radius:50%;border:2px solid #CBD3E6}
.st-rt{flex-grow:1;min-width:0;display:flex;flex-direction:column;gap:2px}
.st-rt b{font-size:15px;font-weight:600}
.st-rt span{font-size:13.5px;color:#5B6582}
/* guides row */
.st-gd{margin-top:8px}
.st-gl{margin-top:10px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.st-gc{display:flex;align-items:center;gap:12px;padding:14px 16px;border-radius:16px;background:#FFFFFF;border:1.5px solid #E6EAF3;text-decoration:none;color:#0B1433;transition:border-color .2s ease}
.st-gc:hover{border-color:#CBD7F5}
.st-gi{width:38px;height:38px;flex-shrink:0;border-radius:12px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.st-gc > span:last-child{display:flex;flex-direction:column;gap:2px;min-width:0}
.st-gc b{font-size:14.5px;font-weight:600}
.st-gc > span:last-child > span{font-size:12.5px;color:#5B6582}
@media (max-width: 960px){.st-gl{display:flex;overflow-x:auto;margin:10px -16px 0 -16px;padding:0 16px;scrollbar-width:none}.st-gc{flex:0 0 240px}}
/* chapter track v2: the progress bar IS the chapter list */
.st-tr{margin-top:20px}
.st-chs{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:6px}
.st-chs li{display:flex;flex-direction:column;gap:10px;min-width:0;padding:0;background:none;border:0;border-radius:0}
.st-seg{display:block;height:8px;border-radius:8px;background:#E6EAF3}
.st-chs .ok .st-seg{background:#1652F0}
.st-chs .now .st-seg{background:linear-gradient(90deg,#1652F0 0 45%,#C9D8FF 45% 100%)}
.st-chs .amb .st-seg{background:#F6C343}
.st-cl{display:flex;flex-direction:column;gap:2px;min-width:0;padding-right:6px}
.st-cl b{font-size:13.5px;font-weight:600;line-height:1.3;color:#0B1433;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.st-cl span{font-size:12.5px;line-height:1.3;color:#5B6582}
.st-chs .amb .st-cl span{color:#8A5300;font-weight:500}
.st-chs .now .st-cl span{color:#1652F0}
.st-chs li:not(.ok):not(.amb):not(.now) .st-cl b{color:#5B6582;font-weight:500}
.st-trm{display:none;margin:10px 0 0 0;font-size:13.5px;color:#5B6582}
.st-trm b{color:#0B1433;font-weight:600}.st-trm span{color:#8A5300;font-weight:500}

@media (max-width: 960px){
.st-head{flex-direction:column;align-items:stretch;gap:14px;padding:20px 0 14px 0}
.st-pw{gap:12px;padding:12px 12px 12px 14px}
.st-pt{display:none}
.st-segs{position:absolute;opacity:0}
.st-pnx{flex-grow:1;padding-left:0;border-left:0}
.st-hero{padding:18px 16px 0 16px}
.st-mini{padding:16px}
.st-ct{flex-wrap:wrap;gap:12px}
.st-cov{width:48px;height:48px;border-radius:14px}
.st-cx{flex-basis:calc(100% - 140px)}
.st-hero h2{font-size:19px}
.st-pct b{font-size:20px}
.st-ct .st-btn,.st-ct .st-gh{order:9;width:100%;justify-content:space-between}
.st-ct .st-gh{justify-content:center}
.st-nb{margin:18px -16px 0 -16px;padding:14px 16px;flex-wrap:wrap}
.st-chips{width:100%;overflow-x:auto;margin:2px -16px 0 -16px;padding:0 16px;scrollbar-width:none}
.st-ar{flex-wrap:wrap}
.st-ar .st-btn,.st-ar .st-gh{width:100%}
.st-ar .st-btn{justify-content:space-between}
.st-at b{font-size:15.5px}
.st-ab{grid-template-columns:minmax(0,1fr);gap:8px;margin-top:14px}
.st-up{background:none;border:0;padding:0 0 6px 0}
.st-up .st-btn{width:100%;justify-content:space-between}
.st-rows li:first-child{border-top:1.5px solid #F0F2F8;padding-top:14px}
.st-sh .ds-link{display:none}
}
/* assigned work list v2 */
.st-tl{list-style:none;margin:18px 0 0 0;padding:0;display:flex;flex-direction:column}
.st-tl li{display:grid;grid-template-columns:22px minmax(0,1fr) 170px auto;align-items:center;column-gap:16px;padding:14px 16px;border-top:1.5px solid #F0F2F8}
.st-tl li.hl{border:1.5px solid #E1E9FF;border-radius:16px;background:#F5F8FF;padding:16px}
.st-tl li.hl + li{border-top:0}
.st-ring{width:18px;height:18px;border-radius:50%;border:2px solid #CBD3E6;box-sizing:border-box}
.st-ring.now{border-color:#1652F0;background:conic-gradient(#1652F0 0 40%,#FFFFFF 40% 100%)}
.st-tt{display:flex;flex-direction:column;gap:4px;min-width:0}
.st-tt b{font-size:15.5px;font-weight:600}
.hl .st-tt b{font-size:16.5px}
.st-tm{display:flex;align-items:center;gap:10px;font-size:13.5px;color:#5B6582}
.st-tm i{font-style:normal;display:none}
.st-tm .st-bar.sm{margin:0;width:140px;flex-shrink:0}
.st-due{font-size:13.5px;color:#5B6582}
.hl .st-due{color:#0E3BB8;font-weight:500}
.st-tl .st-rb{justify-self:end}
@media (max-width: 960px){
.st-tl{margin-top:14px}
.st-tl li{grid-template-columns:18px minmax(0,1fr) auto;column-gap:12px;padding:14px 0}
.st-tl li.hl{padding:14px 0;margin:0;row-gap:14px;background:none;border:0;border-radius:0}
.hl .st-tt b{font-size:15.5px}
.st-asg .st-mnx{display:none}
.st-due{display:none}
.st-tm i{display:inline}
.st-tm{flex-direction:column;align-items:flex-start;gap:6px}
.st-tm .st-bar.sm{width:100%;max-width:none}
.st-tl li.hl .st-btn{grid-column:1 / -1;width:100%;justify-content:space-between}
.st-tl .st-rb{height:36px;padding:0 14px;font-size:13.5px}
}
/* mobile: same chapter track as desktop, swipeable; roomier card */
@media (max-width: 960px){
.st-ct{row-gap:16px}
.st-ct .st-btn{margin-top:4px}
.st-tr{margin:22px -16px 0 -16px}
.st-chs{display:flex;gap:6px;overflow-x:auto;padding:0 16px 4px 16px;scroll-snap-type:x proximity;scroll-padding:0 16px;scrollbar-width:none}
.st-chs li{flex:0 0 136px;scroll-snap-align:start;gap:10px}
.st-nb{margin:22px -16px 0 -16px;padding:18px 16px 16px 16px;display:grid;grid-template-columns:40px minmax(0,1fr);column-gap:12px;row-gap:14px;align-items:start}
.st-chips{grid-column:1 / -1;width:auto;margin:0 -16px;padding:0 16px}
.st-att.st-hero .st-sh{display:none}
.st-att.st-hero .st-ar{margin-top:0}
.st-mini{padding:16px}
.st-mini .st-ct{flex-wrap:nowrap;gap:12px}
.st-mini .st-cov,.st-mini .st-pct,.st-mini .st-mnx{display:none}
.st-mini .st-cx{flex-basis:auto}
.st-mini h2{font-size:16px}
.st-mini .st-ct .st-gh{order:0;width:auto;height:40px;padding:0 18px}
.st-mini .st-bar{margin-top:14px}
.st-att.st-hero .st-ar{flex-direction:column;align-items:center;text-align:center;gap:12px}
}
"""
# ---------- states S05–S09 (2026-10-10) ----------
I_VAL2 = '<path d="M12 3v18M5 21h14M6 7h12"></path><path d="m6 7-3 7a3 3 0 0 0 6 0zM18 7l-3 7a3 3 0 0 0 6 0z"></path>'
I_CHAT = '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"></path>'
I_CARD = '<rect x="3" y="6" width="18" height="14" rx="3"></rect><path d="M3 10h18M16 15h2"></path>'
I_CAL = '<rect x="3" y="5" width="18" height="16" rx="2"></rect><path d="M3 10h18M8 3v4M16 3v4"></path>'
I_Q = '<circle cx="12" cy="12" r="9"></circle><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6v.6M12 17h.01"></path>'
def TRACK(items):
    return ('<div class="st-tr"><ol class="st-chs">' + ''.join(
        f'<li class="{c}"><span class="st-seg"></span><span class="st-cl"><b>{t}</b><span>{st}</span></span></li>' for t, st, c in items) + '</ol></div>')
def PILL(t, c): return f'<span class="st-pill {c}">{t}</span>'
def STRIP(lab, val, segs_on, nlab, nval, act):
    segs = ''.join('<i class="on"></i>' if i < segs_on else '<i></i>' for i in range(5)) if segs_on is not None else ''
    return ('<div class="st-pw ob-in2' + (' st-keep' if segs_on is None else '') + '"><a href="CR-RDY-001.dc.html" class="st-pt"><span class="st-lab">' + lab + '</span><b>' + val + '</b></a>'
            + (f'<span class="st-segs" aria-hidden="true">{segs}</span>' if segs else '')
            + f'<span class="st-pnx"><span class="st-lab">{nlab}</span><b>{nval}</b></span>' + act + '</div>')
PATH5 = STRIP('Path to publishing', '4 of 5 done', 4, 'Next', 'Verify your identity', '<a href="CR-KYC-001.dc.html" class="st-rb">Start</a>')
READY = ('<div class="st-pw st-ok ob-in2"><span class="st-okc" aria-hidden="true">' + CHK + '</span><span class="st-pnx" style="border:0;padding:0"><span class="st-lab">Path to publishing</span><b>All 5 checks complete</b></span>'
         '<a href="CR-RDY-001.dc.html" class="st-rb">View</a></div>')
EARN = STRIP('Earnings', '$84 available', None, 'Pending', '$212', '<a href="#" class="st-rb">View</a>')
TODAY = STRIP('Today', '4 events', None, 'Next · 10:00', 'Validation meeting', '<a href="#" class="st-rb">Join</a>')

VSTEPS6 = [('Submitted', '14 Sep', 'ok'), ('Assigned', '3 validators', 'ok'), ('Review', 'In progress', 'now'), ('Decision', 'Usually 7 to 10 days', ''), ('Publish', 'After a pass', '')]
VSTEPS7 = [('Submitted', '14 Sep', 'ok'), ('Assigned', '3 validators', 'ok'), ('Review', 'Waiting on you', 'amb'), ('Decision', 'After your reply', ''), ('Publish', 'After a pass', '')]
def VALCARD(focus, steps, pill, note, act):
    return (f'<section class="ds-card st-cont {"st-hero" if focus else "st-mini st-vm"} ob-in2" aria-label="Validation"><div class="st-ct"><span class="st-cov" aria-hidden="true">{ic(I_VAL2, 26, 1.8)}</span><div class="st-cx">'
            '<span class="st-lab">In validation · case VAL-00928</span><h2>Data Analysis with SQL</h2><span class="st-meta">' + note + '</span></div>' + pill + act + '</div>'
            + TRACK(steps) + (NBAND if focus else '') + '</section>')
S6_FOCUS = VALCARD(True, VSTEPS6, PILL('Review in progress', 'cb'), 'Educational, Subject Matter and Assessment validators are reviewing.', btn('#', 'Open workspace'))
S6_ATT = ('<section class="ds-card st-att st-mini ob-in2" aria-label="Needs your attention"><div class="st-ar" style="margin-top:0"><span class="st-ai cb" aria-hidden="true">' + ic(I_CAL, 20) + '</span>'
          '<span class="st-at"><b>Validation meeting proposed: Thu 10:00</b><span>Subject Matter Validator · 30 minutes</span></span>' + ghost('#', 'Accept or propose') + '</div></section>')
S7_FOCUS = ('<section class="ds-card st-att st-hero st-ambh ob-in2" aria-label="Needs your attention"><div class="st-ar" style="margin-top:0"><span class="st-ai" aria-hidden="true">' + ic(I_VAL2, 22) + '</span>'
            '<span class="st-at"><span class="st-lab amb">Validator request · due in 3 days</span><b>Clarification required: Chapter 3 → Lesson 4</b><span>Data Analysis with SQL · case VAL-00928 · Subject Matter Validator</span></span>'
            + btn('#', 'Respond to the validator') + '</div>' + NBAND + '</section>')
S7_VAL = VALCARD(False, VSTEPS7, PILL('Your response needed', 'am'), 'One open request is assigned to you. The case continues once you respond.', ghost('#', 'Open workspace'))
S5_FOCUS = ('<section class="ds-card st-att st-hero st-ambh ob-in2" aria-label="Needs your attention"><div class="st-ar" style="margin-top:0"><span class="st-ai" aria-hidden="true">' + ic(I_ID, 22) + '</span>'
            '<span class="st-at"><span class="st-lab amb">Required to submit</span><b>Verify your identity to submit Data Analysis with SQL</b><span>Your course is ready for validation. This is the only thing left. Usually a few minutes.</span></span>'
            + btn('CR-KYC-001.dc.html', 'Verify my identity') + '</div>' + NBAND + '</section>')
S5_COURSE = ('<section class="ds-card st-cont st-mini ob-in2" aria-label="Your course"><div class="st-ct">' + COVER + '<div class="st-cx"><span class="st-lab">Ready for validation</span><h2>Data Analysis with SQL</h2>'
             '<span class="st-meta">Course · 6 of 6 chapters built<span class="st-mnx"> · submit once your identity is verified</span></span></div><span class="st-pct"><b>100%</b><span>built</span></span>' + ghost('CR-CREATE-002B.dc.html', 'Open') + '</div>'
             '<div class="st-bar" aria-hidden="true"><span style="width: 100%"></span></div></section>')
STAT = lambda v, k, sub='': f'<div class="st-st"><b>{v}</b><span>{k}</span>' + (f'<em>{sub}</em>' if sub else '') + '</div>'
S8_FOCUS = ('<section class="ds-card st-cont st-hero ob-in2" aria-label="Your published course"><div class="st-ct">' + COVER + '<div class="st-cx"><span class="st-lab">Live for learners</span><h2>Data Analysis with SQL</h2>'
            '<span class="st-meta">Course · published 2 Oct</span></div>' + PILL('Gold validated', 'gr') + '</div>'
            '<div class="st-stats">' + STAT('46', 'Learners', '+46 this week') + STAT('3', 'Verified completions') + STAT('4.8', 'Average rating') + STAT('3', 'Open questions') + '</div>'
            '<div class="st-ar st-in"><span class="st-ai cb" aria-hidden="true">' + ic(I_CHAT, 20) + '</span><span class="st-at"><b>3 learner questions are waiting</b><span>Chapter 4 has the most. Fast answers in the first weeks lift completion.</span></span>'
            + btn('#', 'Open discussions') + '</div>' + NBAND + '</section>')
S8_TODAY = ('<section class="ds-card st-att st-mini ob-in2" aria-label="Today"><div class="st-ar" style="margin-top:0"><span class="st-ai cb" aria-hidden="true">' + ic(I_CAL, 20) + '</span>'
            '<span class="st-at"><b>16:00 · Office hours</b><span>Data Analysis with SQL · 3 questions queued</span></span>' + ghost('#', 'Open calendar') + '</div></section>')
NEXT8 = ('<section class="ds-card st-att st-mini ob-in2" aria-label="Create next"><div class="st-ar" style="margin-top:0"><span class="st-ai cb" aria-hidden="true">' + ic(I_AI, 20) + '</span>'
         '<span class="st-at"><b>Ready for your next one?</b><span>Learners keep asking about window functions. That could be a follow-on course.</span></span>' + ghost('CR-CREATE-001.dc.html', 'Start something new') + '</div></section>')
def ALROW(icn, tone, t, m, act): return f'<li><span class="st-ai {tone}" aria-hidden="true">{ic(icn, 20)}</span><span class="st-at"><b>{t}</b><span>{m}</span></span>{act}</li>'
S9_FOCUS = ('<section class="ds-card st-att st-hero ob-in2" aria-label="Needs you today"><div class="st-sh"><span class="st-lab">Needs you today</span><a href="#" class="ds-link">Notifications</a></div><ul class="st-al">'
            + ALROW(I_VAL2, '', 'Evidence requested: Data Analyst Career Path', 'Career/Industry Validator · due Friday', btn('#', 'Respond'))
            + ALROW(I_CARD, '', 'Your payout method needs attention', 'Re-verify your bank details before the next payout.', '<a href="#" class="st-rb">Fix now</a>')
            + ALROW(I_CHAT, 'cb', '7 learner questions are waiting', 'Data Analysis with SQL · Chapter 4 has the most', '<a href="#" class="st-rb">Review</a>')
            + ALROW(I_CAL, 'gy', 'Cohort A capstone deadline in 5 days', 'Applied AI Program · 12 of 30 teams have submitted', '<a href="#" class="st-rb">Review</a>')
            + '</ul>' + NBAND + '</section>')
PERF = [('Data Analysis with SQL', 'Course · Gold', '1,240', '71%', '4.8', 'Up 12%', 'up'), ('Advanced SQL for Analysts', 'Course · Silver', '512', '58%', '4.6', 'Drop-off in Ch. 4', 'dn'),
        ('Certified Data Analyst', 'Professional Certification', '138', '64% pass', '4.7', 'Up 5%', 'up'), ('Applied AI Program', 'Learning Program', '30', 'Week 9 of 12', '4.9', 'On track', 'up')]
S9_PERF = ('<section class="ds-card st-att st-mini st-pf ob-in3" aria-label="Performance"><div class="st-sh"><span class="st-lab">Performance · last 30 days</span><a href="#" class="ds-link">Analytics</a></div>'
           '<div class="st-ph"><span>Learning experience</span><span>Learners</span><span>Completion</span><span>Rating</span><span>Trend</span></div><ul class="st-pt2">'
           + ''.join(f'<li><span class="st-pn2"><b>{t}</b><span>{k}</span></span><span data-l="Learners">{l}</span><span data-l="Completion">{c}</span><span data-l="Rating">{r}</span><span class="st-tr2 {cl}">{tr}</span></li>' for t, k, l, c, r, tr, cl in PERF)
           + '</ul></section>')
G6 = GUIDES([('What validators look for', 'Guide · 5 min read'), ('Validation tiers explained', 'Guide · 4 min read'), ('Responding to a validator request', 'Guide · 3 min read')])
G7 = GUIDES([('Responding to a validator request', 'Guide · 3 min read'), ('Validation tiers explained', 'Guide · 4 min read'), ('When revalidation is needed', 'Guide · 3 min read')])
G5 = GUIDES([('How identity checks work', 'Guide · 3 min read'), ('What validators look for', 'Guide · 5 min read'), ('Validation tiers explained', 'Guide · 4 min read')])
MAIN_D = ('<main class="ds-main st">\n<div class="st-head"><div class="ob-in"><p class="st-wel">{{wel}}</p><h1 class="ds-h1">{{h1}}</h1></div>'
          + sif('pw', PATHW, 'true') + sif('s5', PATH5) + sif('rdy', READY) + sif('s8', EARN) + sif('s9', TODAY) + '</div>\n'
          '<div class="st-col">' + sif('s3', ATT_INV) + sif('s4', ATT_DEC) + sif('s4', ASG) + sif('s2', cont_body(True), 'true') + sif('s3', cont_body(False)) + sif('s4', cont_body(False))
          + sif('s5', S5_FOCUS) + sif('s5', S5_COURSE) + sif('s6', S6_FOCUS) + sif('s6', S6_ATT) + sif('s7', S7_FOCUS) + sif('s7', S7_VAL)
          + sif('s8', S8_FOCUS) + sif('s8', S8_TODAY) + sif('s8', NEXT8) + sif('s9', S9_FOCUS) + sif('s9', S9_PERF)
          + sif('s2', G2, 'true') + sif('s3', G3) + sif('s5', G5) + sif('s6', G6) + sif('s7', G7) + '</div>\n</main>')
CSS_X = """
/* states S05-S09 */
.st-pill{display:inline-flex;align-items:center;height:30px;padding:0 12px;border-radius:999px;font-size:13px;font-weight:500;white-space:nowrap;flex-shrink:0;margin-right:6px}
.st-pill.cb{background:#EAF0FF;color:#0E3BB8}.st-pill.am{background:#FFF1CF;color:#8A5300}.st-pill.gr{background:#E7F5EE;color:#0F6B45}
.st-lab.amb{color:#8A5300}
.st-ambh{border-color:#F4D98E;box-shadow:0 18px 44px rgba(214,150,30,.10)}
.st-ambh .st-ai{width:52px;height:52px;border-radius:16px}
.st-ai.cb{background:#EAF0FF;color:#1652F0}.st-ai.gy{background:#F1F3F8;color:#5B6582}
.st-ok .st-okc{width:30px;height:30px;border-radius:50%;background:#0F6B45;color:#FFFFFF;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.st-vm .st-tr{margin-top:14px}
.st-chs{grid-template-columns:none;grid-auto-flow:column;grid-auto-columns:minmax(0,1fr)}
.st-stats{margin-top:20px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.st-st{display:flex;flex-direction:column;gap:2px;padding:14px 16px;border-radius:14px;background:#F7F9FD;border:1.5px solid #EEF1F7}
.st-st b{font-size:24px;font-weight:600;letter-spacing:-0.02em}
.st-st span{font-size:13px;color:#5B6582}
.st-st em{font-style:normal;font-size:12.5px;font-weight:500;color:#0F6B45}
.st-in{margin-top:16px;padding:14px 16px;border-radius:16px;background:#F5F8FF;border:1.5px solid #E1E9FF}
.st-al{list-style:none;margin:10px 0 0 0;padding:0}
.st-al li{display:flex;align-items:center;gap:14px;padding:14px 0;border-top:1.5px solid #F0F2F8}
.st-al li:first-child{border-top:0;padding-top:6px}
.st-al li:first-child .st-ai{background:#FFF1CF;color:#8A5300}
.st-al li:nth-child(2) .st-ai{background:#FFF1CF;color:#8A5300}
.st-pf{padding:18px 22px}
.st-ph{margin-top:14px;display:grid;grid-template-columns:minmax(0,2.2fr) repeat(3,minmax(0,1fr)) minmax(0,1.3fr);gap:12px;padding:0 0 8px 0;font-size:12.5px;color:#8A93AD;border-bottom:1.5px solid #F0F2F8}
.st-pt2{list-style:none;margin:0;padding:0}
.st-pt2 li{display:grid;grid-template-columns:minmax(0,2.2fr) repeat(3,minmax(0,1fr)) minmax(0,1.3fr);gap:12px;align-items:center;padding:12px 0;border-top:1.5px solid #F0F2F8;font-size:14.5px}
.st-pt2 li:first-child{border-top:0}
.st-pn2{display:flex;flex-direction:column;gap:2px;min-width:0}.st-pn2 b{font-weight:600}.st-pn2 span{font-size:12.5px;color:#5B6582}
.st-tr2{font-size:13.5px;font-weight:500}.st-tr2.up{color:#0F6B45}.st-tr2.dn{color:#8A5300}
@media (max-width: 960px){
.st-stats{grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;margin-top:16px}
.st-st{padding:12px}
.st-st b{font-size:20px}
.st-pill{order:2}
.st-ph{display:none}
.st-pt2 li{grid-template-columns:repeat(3,minmax(0,1fr));row-gap:6px;padding:14px 0}
.st-pn2{grid-column:1 / -1}
.st-pt2 li > span[data-l]::before{content:attr(data-l);display:block;font-size:12px;color:#8A93AD}
.st-tr2{grid-column:1 / -1}
.st-al li{flex-wrap:wrap}
.st-al li .st-at{flex:1 1 calc(100% - 60px)}
.st-al li .st-btn{width:100%;justify-content:space-between}
.st-al li .st-rb{margin-left:58px}
.st-in{flex-wrap:wrap}
.st-in .st-btn{width:100%;justify-content:space-between}
.st-ok .st-pnx{flex-grow:1}
.st-keep .st-pt{display:flex}
.st-keep .st-pnx{flex-grow:1;padding-left:14px;border-left:1.5px solid #EEF1F7}
.st-mini.st-vm .st-ct{flex-wrap:wrap}
.st-mini.st-vm .st-cx{flex-basis:100%}
.st-mini.st-vm .st-ct .st-gh{order:4;width:auto;margin-left:auto}
.st-mini.st-vm .st-pill{order:3;margin:0}
.st-al li:not(:first-child){flex-wrap:nowrap}
.st-al li:not(:first-child) .st-at{flex:1 1 auto}
.st-al li:not(:first-child) .st-rb{margin-left:0;height:36px;padding:0 14px;font-size:13.5px}
}
"""
CSS3 = CSS3.replace('/* mobile: same chapter track as desktop', CSS_X + '/* mobile: same chapter track as desktop', 1)
SCRIPT3 = '''<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":820}}'>
class Component extends DCLogic {
  constructor(props) { super(props); this.state = { nav: false }; this.v = (props || {}).variant || 's02'; }
  renderVals() {
    const v = this.v;
    const T = {
      s02: ['Welcome back, Ada.', 'Pick up where you left off.', 'Chapter 4 has no assessment yet', 'I can draft five questions from your lessons for you to review and edit.', ['Draft the questions', 'Suggest a project instead']],
      s03: ['Welcome back, Ada.', 'You have an invitation waiting.', 'Want a quick read of the invitation?', 'I can summarise the role, the chapter and the revenue share before you decide.', ['Summarise the invitation', 'What does a Co-Creator do?']],
      s04: ['Good to see you, Ada.', 'Your chapter is taking shape.', 'Lesson 3.2 needs one worked example', 'I can turn your revenue table into a step-by-step example learners can follow.', ['Draft the example', 'Check my lesson']],
      s05: ['Almost there, Ada.', 'One step from validation.', 'While you verify, I can run a pre-check', 'I’ll check outcomes, assessments and sources so validators see a ready course.', ['Run a pre-check', 'What happens in validation?']],
      s06: ['Welcome back, Ada.', 'Your course is with validators.', 'Get ready for Thursday’s meeting', 'I can pull together the questions validators usually ask about SQL courses.', ['Prepare for the meeting', 'How validation works']],
      s07: ['Welcome back, Ada.', 'A validator needs your answer.', 'I can draft a reply from Lesson 3.4', 'You stay in control: review it, edit it, then send it from the workspace.', ['Draft a reply', 'Show the full request']],
      s08: ['Congratulations, Ada.', 'Your course is live.', 'Your first 46 learners are in', 'Most are early-career analysts, as you designed for. I can draft answers to the open questions.', ['Draft answers', 'See who joined']],
      s09: ['Good morning, Ada.', 'Four things need you today.', 'Learners drop off at Lesson 4.3', '38% stop at window functions in Advanced SQL. A short practice task before it may help.', ['Review the chapter', 'Draft a practice task']]
    }[v];
    return { navCls: this.state.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !this.state.nav }),
      s2: v === 's02', s3: v === 's03', s4: v === 's04', s5: v === 's05', s6: v === 's06', s7: v === 's07', s8: v === 's08', s9: v === 's09', pw: ['s02','s03','s04'].includes(v), rdy: v === 's06' || v === 's07', wel: T[0], h1: T[1], nT: T[2], nD: T[3], nChips: T[4] };
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
for n, v in [('S02', 's02'), ('S03', 's03'), ('S04', 's04'), ('S05', 's05'), ('S06', 's06'), ('S07', 's07'), ('S08', 's08'), ('S09', 's09')]:
    wrap('CR-DASH-' + n, 'CR-DASH-ST', v, 'Credalio · Studio state ' + n, 1440, 1100 if n == 'S09' else 820, False)
    wrap('CR-DASH-' + n + '-Mobile', 'CR-DASH-ST', v, 'CR-DASH-' + n + ' mobile preview', 390, 980, True)
print('ok')
