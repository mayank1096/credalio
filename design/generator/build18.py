# build18: collaboration invitation flow — CR-COL-002 one source, variants review / consent / joined (= COL-002 / 003 / 004).
# Focus-mode TASK shell taken from the LIVE CR-POL-001 (head + styles), own markup + CSS. COL-001 = CR-NOT-001 variant "col" (build17).
# Only writes its own files. usage: python3 build18.py <canvas project dir>
import re, sys, os
P = sys.argv[1]
rd = lambda f: open(os.path.join(P, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(P, f), 'w', encoding='utf-8').write(s)
def ic(paths, w=20, sw=1.9):
    return f'<svg width="{w}" height="{w}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>'
ARR = ic('<path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path>', 18, 2.4)
CHK = ic('<path d="m5 12.5 4.5 4.5L19 7.5"></path>', 14, 2.6)
NO = ic('<path d="M6 6l12 12M18 6 6 18"></path>', 13, 2.4)
BACK = ic('<path d="M19 12H5"></path><path d="m11 6-6 6 6 6"></path>', 18, 2.2)
BOOK = ic('<path d="M4 19.5V5a2 2 0 0 1 2-2h14v18H6.5A2.5 2.5 0 0 1 4 18.5"></path><path d="M8 7h8"></path>', 20)
CHAT = ic('<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"></path>', 18)

pol = rd('CR-POL-001.dc.html')
head = pol[:pol.index('<div class="tk-root">')]
X = pol[pol.index('<a href="CR-RDY-001.dc.html" class="lp-x"'):]
X = X[X.index('<svg'):X.index('</a>')]  # close icon

CONS = [('I agree to take part as Co-Creator on Financial Modelling Basics', 'You can leave later; your contributions stay attributed to you.'),
        ('I understand my role, responsibilities and permissions', 'Co-Creator: build your assigned chapter; no publishing or pricing rights.'),
        ('I accept the applicable Credalio creator terms', ''),
        ('I accept the IP and contribution terms for this course', 'Content you contribute is licensed to the course as set out in the terms.'),
        ('I accept the proposed revenue arrangement (20%)', 'Final shares are confirmed in the revenue agreement before publishing.'),
        ('I’ll follow the platform collaboration rules', 'Work communication stays in Team chat, comments and assignments.')]

side = ('<aside class="cl-side ob-in">'
        '<div class="cl-from"><span class="cl-av">BA</span><span><b>Dr. Bola Ade</b><span>Lead Creator · ABC Institute</span></span></div>'
        '<span class="cl-eb">Invited you to co-create</span>'
        '<h1 class="cl-h1">Financial Modelling Basics</h1>'
        '<p class="cl-sub">Build, test and present financial models in spreadsheets: revenue models, scenarios and sensitivity analysis, for early-career finance professionals.</p>'
        '<div class="cl-meta"><span>Course</span><span>Draft · build phase</span><span>ABC Institute</span></div>'
        '<div class="cl-team"><span class="cl-avs"><span class="cl-av sm">BA</span><span class="cl-av sm t2">TB</span><span class="cl-av sm t3">AO</span></span><span>Dr. Bola Ade, Tunde Bello and you</span></div>'
        '<ol class="cl-steps" aria-label="Steps"><li class="{{s0}}"><i></i><span>Review</span></li><li class="{{s1}}"><i></i><span>Consent</span></li><li class="{{s2}}"><i></i><span>Joined</span></li></ol>'
        '</aside>')

review = ('<sc-if value="{{vReview}}" hint-placeholder-val="{{true}}"><section class="cl-panel ob-in2" aria-labelledby="cl-ph">'
          '<h2 id="cl-ph" class="cl-ph">Your part</h2>'
          '<div class="cl-sum"><span class="cl-sc"><span class="cl-chi">' + BOOK + '</span><span><b>Chapter 3 · Revenue models</b><span>3 lessons and Quiz 3</span></span></span>'
          '<span class="cl-sv"><em>Role</em><b>Co-Creator</b></span><span class="cl-sv"><em>Revenue share</em><b>20%</b></span><span class="cl-sv"><em>Reply by</em><b>in 6 days</b></span></div>'
          '<span class="cl-lab">What you’ll do</span><ul class="cl-do">'
          + ''.join(f'<li>{CHK}<span>{t}</span></li>' for t in ['Build your chapter and respond to comments and validator requests on it', 'Declare your own contribution before validation'])
          + '</ul><div class="cl-perm"><div class="cl-pb ok"><span class="cl-pl">You can</span>'
          + ''.join(f'<span class="cl-p ok">{CHK}{t}</span>' for t in ['Edit your chapter', 'Comment anywhere', 'Use Team chat'])
          + '</div><div class="cl-pb"><span class="cl-pl">Lead Creator keeps</span>'
          + ''.join(f'<span class="cl-p">{NO}{t}</span>' for t in ['Publishing', 'Pricing', 'Other chapters'])
          + '</div></div>'
          '<sc-if value="{{asking}}" hint-placeholder-val="{{false}}"><div class="cl-box"><label for="cl-q" class="cl-lab">Your question to Dr. Bola Ade</label><textarea id="cl-q" rows="3" placeholder="For example: can I add a case study to Chapter 3?"></textarea><div class="cl-bf"><span>The reply appears with this invitation.</span><button type="button" class="ds-ghost cl-sm" onClick="{{send}}">Send question</button></div></div></sc-if>'
          '<sc-if value="{{sent}}" hint-placeholder-val="{{false}}"><div class="cl-note" role="status">' + CHAT + '<span>Question sent. Dr. Bola Ade’s reply will appear here.</span></div></sc-if>'
          '<sc-if value="{{declining}}" hint-placeholder-val="{{false}}"><div class="cl-box"><label for="cl-d" class="cl-lab">Reason (optional, shared with Dr. Bola Ade)</label><textarea id="cl-d" rows="2"></textarea><div class="cl-bf"><span>You can’t undo this.</span><button type="button" class="ds-ghost cl-sm cl-red" onClick="{{confirmDecline}}">Decline invitation</button></div></div></sc-if>'
          '<sc-if value="{{declined}}" hint-placeholder-val="{{false}}"><div class="cl-note gy" role="status"><span>You declined. Dr. Bola Ade has been told.</span></div></sc-if>'
          '<div class="cl-foot"><button type="button" class="cl-tx" onClick="{{decline}}">Decline</button><button type="button" class="ds-ghost cl-ask" onClick="{{ask}}">' + CHAT + '<span>Ask a question</span></button>'
          '<a href="CR-COL-003.dc.html" class="ds-btn cl-go {{goOff}}" onClick="{{accept}}"><span>Accept</span><span class="ob-arrow">' + ARR + '</span></a></div>'
          '</section></sc-if>')

checks = ''.join(f'<button type="button" role="checkbox" aria-checked="{{{{c{i}.on}}}}" class="cl-ck {{{{c{i}.cls}}}}" onClick="{{{{c{i}.pick}}}}"><span class="tk-box">{CHK}</span><span><b>{t}</b>' + (f'<span>{d}</span>' if d else '') + '</span></button>' for i, (t, d) in enumerate(CONS))
consent = ('<sc-if value="{{vConsent}}" hint-placeholder-val="{{false}}"><section class="cl-panel ob-in2" aria-labelledby="cl-ch2">'
           '<h2 id="cl-ch2" class="cl-ph">Before you join</h2><p class="cl-pp">Confirm how you’re taking part. This isn’t the validation declaration; that comes later, for your own work.</p>'
           '<div class="cl-ckw"><div class="cl-ckh"><span>Tick each statement to join</span><b>{{nOn}} of 6 ticked</b></div><div class="cl-cks">' + checks + '</div></div>'
           '<div class="cl-foot"><a href="CR-COL-002.dc.html" class="ds-ghost cl-bk" aria-label="Back to the invitation">' + BACK + '<span>Back</span></a>'
           '<a href="CR-COL-004.dc.html" class="ds-btn cl-go {{joinOff}}"><span>Accept and join</span><span class="ob-arrow">' + ARR + '</span></a></div>'
           '</section></sc-if>')

joined = ('<sc-if value="{{vJoined}}" hint-placeholder-val="{{false}}"><section class="cl-panel cl-done ob-in2" aria-labelledby="cl-ch3">'
          '<span class="cl-ok">' + ic('<path d="m5 12.5 4.5 4.5L19 7.5"></path>', 30, 2.6) + '</span>'
          '<h2 id="cl-ch3" class="cl-ph cl-big">You’re now a collaborator</h2><p class="cl-pp">Chapter 3 is waiting in Assigned to me, and the team knows you’ve joined.</p>'
          '<div class="cl-stats"><span><em>Role</em><b>Co-Creator</b></span><span><em>Your chapter</em><b>Chapter 3 · Revenue models</b></span></div>'
          '<div class="cl-foot"><a href="#" class="ds-ghost cl-ask">Assigned to me</a><a href="#" class="ds-btn cl-go"><span>Open Course Studio</span><span class="ob-arrow">' + ARR + '</span></a></div>'
          '</section></sc-if>')

body = ('<div class="tk-root cl-root {{rootCls}}">\n<div class="tk-scene" aria-hidden="true"></div><div class="cl-glow" aria-hidden="true"></div>\n'
        '<header class="tk-top">\n<a href="CR-NOT-001.dc.html" class="lp-x" aria-label="Close and go back to notifications">' + X + '</a>\n'
        '<div class="lp-title"><span class="lp-t1" style="display: block">Collaboration invitation</span></div>\n<span style="flex-grow: 1"></span>\n</header>\n'
        '<main class="cl">\n' + side + '\n<div class="cl-main">' + review + consent + '</div>\n</main>\n</div>\n</x-dc>\n')

CSS = '''
/* build18 collaboration */
.cl{flex-grow:1;width:min(1280px,100%);box-sizing:border-box;margin:0 auto;padding:clamp(24px,5vh,52px) 32px 64px 32px;display:grid;grid-template-columns:minmax(0,1fr) 640px;gap:64px;align-items:start;align-content:start}
.cl-side{position:sticky;top:104px;display:flex;flex-direction:column;align-items:flex-start}
.cl-from{display:flex;align-items:center;gap:12px}
.cl-from > span:last-child{display:flex;flex-direction:column;gap:1px}
.cl-from b{font-size:15px;font-weight:600}.cl-from > span:last-child span{font-size:13.5px;color:#5B6582}
.cl-av{width:44px;height:44px;flex-shrink:0;border-radius:50%;background:#0B1433;color:#FFFFFF;font-size:14px;font-weight:600;display:flex;align-items:center;justify-content:center}
.cl-av.sm{width:30px;height:30px;font-size:11px;border:2px solid #FFFFFF;box-sizing:content-box}
.cl-av.t2{background:#1652F0}.cl-av.t3{background:#5B6582}
.cl-eb{margin-top:40px;font-size:13px;font-weight:500;color:#8A93AD}
.cl-h1{margin:10px 0 0 0;font-size:clamp(30px,4.4vh,38px);line-height:1.12;font-weight:600;letter-spacing:-0.03em}
.cl-sub{margin:18px 0 0 0;font-size:15.5px;line-height:1.65;color:#3A4566;max-width:460px}
.cl-meta{margin-top:24px;display:flex;flex-wrap:wrap;gap:8px}
.cl-meta span{display:inline-flex;align-items:center;height:28px;padding:0 11px;border-radius:999px;background:#F1F3F8;color:#3A4566;font-size:12.5px;font-weight:500}
.cl-team{margin-top:26px;display:flex;align-items:center;gap:10px;font-size:13.5px;color:#5B6582}
.cl-avs{display:flex}.cl-avs .cl-av + .cl-av{margin-left:-6px}
.cl-steps{list-style:none;margin:44px 0 0 0;padding:0;display:flex;gap:6px;width:100%;max-width:420px}
.cl-steps li{flex:1 1 0;display:flex;flex-direction:column;gap:8px;font-size:13px;font-weight:500;color:#8A93AD}
.cl-steps i{display:block;height:4px;border-radius:4px;background:#E6EAF3}
.cl-steps .on i{background:#1652F0}.cl-steps .on{color:#0B1433}
.cl-steps .dn i{background:#0F6B45}.cl-steps .dn{color:#0F6B45}
.cl-panel{border-radius:24px;background:#FFFFFF;border:1.5px solid #E6EAF3;box-shadow:0 18px 44px rgba(22,82,240,.08);padding:24px 26px 18px 26px;display:flex;flex-direction:column}
.cl-ph{margin:0;font-size:20px;font-weight:600;letter-spacing:-0.01em}
.cl-pp{margin:8px 0 0 0;font-size:14.5px;line-height:1.55;color:#3A4566}
.cl-stats{margin-top:16px;display:grid;grid-template-columns:repeat(3,minmax(0,auto));justify-content:start;gap:12px 40px;padding:14px 18px;border-radius:16px;background:#F5F8FF}
.cl-stats > span{display:flex;flex-direction:column;gap:2px;min-width:0}
.cl-stats em{font-style:normal;font-size:12.5px;color:#8A93AD}
.cl-stats b{font-size:16px;font-weight:600}
.cl-stats i{font-style:normal;font-size:12px;color:#5B6582}
.cl-ch{margin-top:12px;display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:16px;border:1.5px solid #E6EAF3}
.cl-chi{width:40px;height:40px;flex-shrink:0;border-radius:12px;background:linear-gradient(135deg,#1652F0,#6E96FF);color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.cl-ch > span:last-child{display:flex;flex-direction:column;gap:2px}
.cl-ch b{font-size:15px;font-weight:600}.cl-ch > span:last-child span{font-size:13px;color:#5B6582}
.cl-lab{display:block;margin:16px 0 8px 0;font-size:12.5px;font-weight:500;color:#8A93AD}
.cl-do{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px}
.cl-do li{display:flex;align-items:flex-start;gap:10px;font-size:14.5px;line-height:1.5}
.cl-do svg{color:#1652F0;flex-shrink:0;margin-top:3px}
.cl-sum{margin-top:14px;display:grid;grid-template-columns:minmax(0,1fr) auto auto auto;align-items:center;gap:22px;padding:12px 18px 12px 12px;border-radius:16px;background:#F5F8FF}
.cl-sc{display:flex;align-items:center;gap:12px;min-width:0}
.cl-sc > span:last-child{display:flex;flex-direction:column;gap:2px;min-width:0}
.cl-sc b{font-size:15px;font-weight:600;white-space:nowrap}.cl-sc > span:last-child span{font-size:13px;color:#5B6582}
.cl-sv{display:flex;flex-direction:column;gap:2px}
.cl-sv em{font-style:normal;font-size:12.5px;color:#8A93AD}.cl-sv b{font-size:15px;font-weight:600;white-space:nowrap}
.cl-perm{margin-top:20px;display:grid;grid-template-columns:1fr 1fr;gap:12px}
.cl-pb{display:flex;flex-direction:column;align-items:flex-start;gap:10px;padding:16px 18px;border-radius:16px;border:1.5px solid #E6EAF3}
.cl-pb.ok{background:#F3FAF6;border-color:#D5EEDF}
.cl-pl{font-size:12.5px;font-weight:500;color:#8A93AD;margin-bottom:2px}
.cl-p{display:inline-flex;align-items:center;gap:7px;font-size:14px;color:#5B6582}
.cl-p svg{color:#8A93AD}
.cl-p.ok{color:#0B1433}.cl-p.ok svg{color:#0F6B45}
.cl-box{margin-top:18px;padding:14px;border-radius:16px;background:#F7F9FD;border:1.5px solid #E6EAF3}
.cl-box .cl-lab{margin:0 0 8px 0;color:#3A4566}
.cl-box textarea{width:100%;box-sizing:border-box;border-radius:12px;border:1.5px solid #D6DDEE;padding:10px 12px;font-family:inherit;font-size:14.5px;line-height:1.5;color:#0B1433;resize:none;outline:none;background:#FFFFFF}
.cl-box textarea:focus{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.cl-bf{margin-top:10px;display:flex;align-items:center;justify-content:space-between;gap:12px;font-size:13px;color:#5B6582}
.cl-sm{height:40px;padding:0 16px;font-size:14px}
.cl-red{color:#9A3B12;border-color:#F0C9B5}
.cl-note{margin-top:16px;display:flex;align-items:center;gap:10px;padding:12px 14px;border-radius:14px;background:#EAF0FF;color:#0E3BB8;font-size:14px;font-weight:500}
.cl-note.gy{background:#F1F3F8;color:#4A5578}
.cl-foot{margin-top:20px;padding-top:16px;border-top:1.5px solid #F0F2F8;display:flex;align-items:center;gap:12px}
.cl-tx{height:48px;padding:0 6px;border:0;background:none;font-family:inherit;font-size:15px;font-weight:600;color:#5B6582;cursor:pointer;margin-right:auto}
.cl-tx:hover{color:#0B1433}
.cl-ask{height:52px}
.cl-go{margin-left:0}
.cl-go.lp-off{background:#C9D3EC;box-shadow:none;pointer-events:none}.cl-go.lp-off .ob-arrow{color:#9AA8CC}
.cl-bk{height:52px;width:52px;padding:0}
.cl-bk + .cl-go{margin-left:auto}.cl-bk span{display:none}
.cl-cnt{margin-left:auto;font-size:14px;color:#5B6582}
.cl-ckw{margin-top:18px;border:1.5px solid #E6EAF3;border-radius:18px;overflow:hidden}
.cl-ckh{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:11px 18px;background:#F5F8FF;border-bottom:1.5px solid #E6EAF3;font-size:13px;font-weight:500;color:#4A5578}
.cl-ckh b{font-size:13px;font-weight:600;color:#1652F0}
.cl-cks{display:flex;flex-direction:column;max-height:296px;overflow-y:auto;scrollbar-width:thin;scrollbar-color:#CBD3E6 transparent;background:linear-gradient(#FFF 30%,rgba(255,255,255,0)) center top / 100% 40px no-repeat local,linear-gradient(rgba(255,255,255,0),#FFF 70%) center bottom / 100% 40px no-repeat local,radial-gradient(farthest-side at 50% 0,rgba(11,20,51,.14),transparent) center top / 100% 12px no-repeat scroll,radial-gradient(farthest-side at 50% 100%,rgba(11,20,51,.14),transparent) center bottom / 100% 12px no-repeat scroll}
.cl-ck{display:flex;align-items:flex-start;gap:14px;padding:14px 18px;border:0;border-top:1.5px solid #F0F2F8;background:transparent;font-family:inherit;text-align:left;cursor:pointer;color:#0B1433;transition:border-color .2s ease,background .2s ease}
.cl-ck:first-child{border-top:0}
.cl-ck:hover{background:#F7F9FD}
.cl-ck:hover .tk-box{border-color:#1652F0}
.cl-ck > span:last-child{display:flex;flex-direction:column;gap:2px}
.cl-ck b{font-size:14.5px;font-weight:500;line-height:1.4}
.cl-ck > span:last-child span{font-size:13px;line-height:1.45;color:#5B6582}
.cl-ck.tk-on b{color:#0B1433}
.cl-done{align-items:flex-start}
.cl-ok{width:60px;height:60px;border-radius:50%;background:#0F6B45;color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 8px #E7F5EE}
.cl-big{margin-top:22px;font-size:26px;letter-spacing:-0.02em}
.cl-done .cl-stats{width:100%;box-sizing:border-box;grid-template-columns:auto auto;gap:12px 48px}
.cl-done .cl-foot{width:100%;justify-content:flex-end}
.cl-glow{position:absolute;left:0;right:0;top:0;height:340px;z-index:-1;pointer-events:none;background:radial-gradient(60% 100% at 50% 0,rgba(22,82,240,.08),transparent 70%)}
.is-joined .cl-glow{background:radial-gradient(60% 100% at 50% 0,rgba(15,107,69,.12),transparent 70%)}
@media (max-width: 960px){
.cl{grid-template-columns:minmax(0,1fr);gap:36px;padding:32px 16px 0 16px}
.cl-side{position:static}
.cl-from b{font-size:14px}.cl-av{width:38px;height:38px;font-size:13px}
.cl-eb{margin-top:22px}
.cl-h1{font-size:24px;margin-top:6px}
.cl-sub,.cl-team{display:none}
.cl-meta{margin-top:16px}
.cl-steps{margin-top:28px;max-width:none}
.cl-panel{border:0;box-shadow:none;border-radius:0;padding:0;background:none}
.cl-ph{font-size:18px}
.cl-stats{grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;padding:12px 14px}
.cl-stats b{font-size:15px}.cl-stats i{display:none}
.cl-done .cl-stats{grid-template-columns:auto minmax(0,1fr);gap:10px 24px}
.cl-sum{margin-top:16px;grid-template-columns:repeat(3,auto);justify-content:space-between;gap:18px 12px;padding:16px}
.cl-lab{margin:28px 0 12px 0}
.cl-do{gap:12px}
.cl-sc{grid-column:1 / -1;padding-bottom:16px;border-bottom:1.5px solid #DDE5F7}
.cl-perm{grid-template-columns:minmax(0,1fr);gap:12px;margin-top:28px}
.cl-foot{position:sticky;bottom:0;z-index:4;margin:28px -16px 0 -16px;padding:12px 16px;background:#FFFFFF;border-top:1.5px solid #EEF1F7}
.cl-tx{margin-right:0;padding:0 4px;font-size:14.5px}
.cl-ask{width:52px;padding:0;flex-shrink:0}.cl-ask span{display:none}
.cl-done .cl-ask{display:none}
.cl-done .cl-foot{width:auto;align-self:stretch}
.cl-go{flex-grow:1;justify-content:space-between}
.cl-cnt{display:none}
.cl-cks{max-height:none;overflow:visible}
.cl-big{font-size:22px;margin-top:18px}
.cl-ok{width:52px;height:52px}
}
'''

SCRIPT = '''<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":820}}'>
class Component extends DCLogic {
  constructor(props) { super(props); const v = (props && props.variant) || 'review'; this.state = { v, cons: v === 'consent' ? { 0: 1, 1: 1, 2: 1 } : {}, ask: false, dec: false, sent: false, declined: false }; }
  renderVals() {
    const S = this.state, v = S.v, out = {};
    const n = Object.keys(S.cons).filter((k) => S.cons[k]).length;
    for (let i = 0; i < 6; i++) { const on = !!S.cons[i]; out['c' + i] = { on: on ? 'true' : 'false', cls: on ? 'tk-on' : '', pick: () => this.setState({ cons: Object.assign({}, S.cons, { [i]: !on }) }) }; }
    return Object.assign(out, {
      vReview: v === 'review', vConsent: v === 'consent', vJoined: v === 'joined', rootCls: v === 'joined' ? 'is-joined' : '',
      s0: v === 'review' ? 'on' : 'dn', s1: v === 'consent' ? 'on' : (v === 'joined' ? 'dn' : ''), s2: v === 'joined' ? 'dn' : '',
      asking: S.ask, declining: S.dec, sent: S.sent, declined: S.declined, goOff: S.declined ? 'lp-off' : '',
      ask: () => this.setState({ ask: !S.ask, dec: false }), decline: () => this.setState({ dec: !S.dec, ask: false }),
      send: () => this.setState({ ask: false, sent: true }), confirmDecline: () => this.setState({ dec: false, declined: true }),
      accept: () => {}, nOn: n, joinOff: n < 6 ? 'lp-off' : ''
    });
  }
}
</script>
</body>
</html>
'''
s = head.replace('</style>', CSS + '</style>', 1)
s = re.sub(r'<title>.*?</title>', '<title>Credalio · Collaboration invitation</title>', s)
wr('CR-COL-002.dc.html', s + body + SCRIPT)

# wrappers: COL-003 / COL-004 (desktop + mobile), COL-002 mobile
wd, wm = rd('CR-DASH-S03.dc.html'), rd('CR-CRED-002c-Mobile.dc.html')
for n, var in [('CR-COL-002', None), ('CR-COL-003', 'consent')]:
    imp = f'<dc-import name="CR-COL-002"' + (f' variant="{var}"' if var else '')
    if var:
        t = wd.replace('<dc-import name="CR-DASH-ST" variant="s03"', imp)
        wr(n + '.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} preview</title>', t))
    t = wm.replace('<dc-import name="CR-CRED-002" variant="badge"', imp)
    wr(n + '-Mobile.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} mobile preview</title>', t))
print('ok')

# ======================= CR-COL-004 · joined = standard success layout (from LIVE CR-POL-002) =======================
p2 = rd('CR-POL-002.dc.html')
p2 = p2.replace('<a href="CR-RDY-001.dc.html" class="lp-x" aria-label="Close and go back to readiness">', '<a href="CR-DASH-NEW.dc.html" class="lp-x" aria-label="Close and go back to your Studio">', 1)
p2 = re.sub(r'<div class="lp-title">.*?</div>', '<div class="lp-title"><span class="lp-t1" style="display: block">Collaboration invitation</span></div>', p2, count=1, flags=re.S)
a = p2.index('<div class="ko-row">'); b = p2.index('</div>\n</sc-if>', a) + 6
card = ('<div class="ko-row">\n<section class="ko-card ko-idc cj-card ob-in3" aria-label="Your collaboration">'
        '<span class="cj-av">BA</span><span class="ko-it"><b>Financial Modelling Basics</b><span>Dr. Bola Ade · Lead Creator, ABC Institute</span></span><span class="cj-role">Co-Creator</span>'
        '<div class="ko-rd cj-rd"><span class="cj-chi">' + BOOK + '</span><span class="cj-ct"><b>Chapter 3 · Revenue models</b><span>Your part · 3 lessons and Quiz 3</span></span></div></section>\n'
        '<section class="ko-next ob-in4" aria-label="Next for you"><span class="ko-ni">' + ic('<path d="M12 3l1.9 5.6L19.5 10.5l-5.6 1.9L12 18l-1.9-5.6L4.5 10.5l5.6-1.9z"></path>', 20) + '</span>'
        '<span class="ko-nt"><span class="ko-nl">Next for you</span><b>Start Chapter 3</b><span>Lesson 3.1 is ready to draft. Nova can sketch it with you.</span></span>'
        '<a href="#" class="ds-btn sm ko-go"><span>Open Course Studio</span><span class="ob-arrow">' + ARR + '</span></a></section>\n</div>')
p2 = p2[:a] + card + p2[b:]
p2 = re.sub(r'<div class="ko-links ob-in4">.*?</div>', '<div class="ko-links ob-in4"><a href="#">Assigned to me</a><span aria-hidden="true">·</span><a href="CR-DASH-NEW.dc.html">Back to my Studio</a></div>', p2, count=1, flags=re.S)
p2 = p2.replace("const T = ['ko-v', 'Complete', 'All policies accepted', 'You can read them again any time in Creator Centre.'];",
                "const T = ['ko-v', 'Joined', 'You’re now a collaborator', 'Chapter 3 is waiting in Assigned to me, and the team knows you’ve joined.'];")
assert 'You’re now a collaborator' in p2
p2 = p2.replace('</style>', '''
/* build18 COL-004 */
.cj-av{width:44px;height:44px;border-radius:50%;background:#0B1433;color:#FFFFFF;font-size:14px;font-weight:600;display:flex;align-items:center;justify-content:center}
.cj-role{display:inline-flex;align-items:center;height:30px;padding:0 12px;border-radius:999px;background:#EAF0FF;color:#0E3BB8;font-size:13px;font-weight:500}
.cj-rd{gap:12px}
.cj-chi{width:40px;height:40px;flex-shrink:0;border-radius:12px;background:linear-gradient(135deg,#1652F0,#6E96FF);color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.cj-ct{display:flex;flex-direction:column;gap:2px}
.cj-ct b{font-size:15px;font-weight:600}.cj-ct span{font-size:13px;color:#5B6582}
@media (max-width: 960px){.cj-role{grid-column:2;justify-self:start}}
</style>''', 1)
p2 = re.sub(r'<title>.*?</title>', '<title>Credalio · You’re now a collaborator</title>', p2)
wr('CR-COL-004.dc.html', p2)
t = wm.replace('<dc-import name="CR-CRED-002" variant="badge"', '<dc-import name="CR-COL-004"')
wr('CR-COL-004-Mobile.dc.html', re.sub(r'<title>.*?</title>', '<title>CR-COL-004 mobile preview</title>', t))
print('col4 ok')
