# For Institutions page (ENT-001..009). Built from LIVE shared pieces, never redrawn:
#   Landing.dc.html  -> institutions door (ci-in, workspace window, credentials float) as the hero, step list (tx-step), final CTA (fc-*)
#   Creators page    -> hero layout, tab list + window (cx-*), who tiles (cx-who), validation track (ko-path)
#   Dashboard        -> Backpack proof tiles (lr-pf), Nova (nv-av, nova-card)
#   Link 2 CR-SET    -> switch (hp-sw)
# Usage: python3 insgen.py -> design/canvas3/project/Institutions.dc.html
import os, re, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from kit import AURORA_JS, KIT_CSS, NOVA, tip, btn, ck
from shell import BASE_CSS, nav, FOOT
import dashgen, pricegen, cregen

P = os.path.join(HERE, '../../canvas3/project/')
OUT = P + 'Institutions.dc.html'
L = cregen.L
block, style, ic = pricegen.block, pricegen.style, dashgen.ic
AVN = cregen.AVN
TALK = 'Partner.dc.html'

# ---------- hero: the Landing institutions door, opened up ----------
DOOR = block(L, '<a class="ci-door ci-in"', 'a')
FLOAT = re.search(r'<div class="ci-float".*?issued</span></span></div>', DOOR, re.S).group(0)
FLOAT = FLOAT.replace(' style="left: -128px; top: 128px"', '').replace('<div class="ci-float">', '<div class="ci-float cx-f1">').replace('186 issued', '2,214 issued this term')
LIVE = re.search(r'<span class="ds-tag green">.*?Live</span>', DOOR, re.S).group(0)
KPIS = [('4,820', 'Learners'), ('126', 'Creators'), ('84', 'Programs'), ('72%', 'Active learning')]
HERO = '''<section class="cx-top" aria-labelledby="in-h">
<div class="ci-door ci-in cx-hero in-hero">
<div class="ci-copy">
<span class="ci-k" style="color: #1652F0; opacity: 1">Credalio for Institutions</span>
<h1 id="in-h" class="ci-t">Build learning that moves your people forward.</h1>
<p class="ci-d" style="color: #3A4566; opacity: 1">Create and deliver learning, manage people, set up AI, validate quality and issue verifiable credentials. All in one place.</p>
<div class="cx-acts">''' + btn('Talk to Credalio', TALK, 'ci-btn') + '''<a class="cx-wl" href="#in-do">See what you can do</a></div>
</div>
<div class="ci-vis" aria-hidden="true">
<div class="ci-win">
<div class="ci-wk"><span>Meridian University · Workspace</span>''' + LIVE + '''</div>
<span class="cx-wt">Autumn term</span>
<div class="in-kp">''' + ''.join('<span class="in-k"><b>%s</b>%s</span>' % k for k in KPIS) + '''</div>
<div class="in-bar"><span>Learner progress<b>68%</b></span><i><s style="width: 68%"></s></i></div>
<div class="ci-row"><span>Programs in delivery</span><b class="in-rv">84 live</b></div>
<div class="ci-row"><span>Validation</span><b class="in-rv" style="color: #B54708">12 in review</b></div>
</div>
''' + FLOAT + '''
</div>
</div>
</section>'''

# ---------- who it is for: Creators who tiles ----------
I_UNI = '<path d="M3 9l9-5 9 5-9 5z"></path><path d="M7 11.5V16c0 1.5 2.2 3 5 3s5-1.5 5-3v-4.5"></path>'
I_BRF = '<rect x="3" y="7" width="18" height="13" rx="2.5"></rect><path d="M9 7V5h6v2"></path>'
I_GOV = '<path d="M4 20h16M5 10h14M12 4l8 4H4z"></path><path d="M7 10v7M12 10v7M17 10v7"></path>'
WHO = [(I_UNI, 'Universities & colleges', 'Extend learning beyond the classroom.'), (dashgen.I['learn'], 'Training providers', 'Create and run professional learning at scale.'), (I_BRF, 'Companies', 'Upskill and reskill your people.'), (dashgen.I['cert'], 'Professional bodies', 'Deliver assessed CPD and credentials.'), (I_GOV, 'Government & workforce', 'Coordinate learning across large groups.')]
WHOS = '''<section class="pc-sec cx-sec in-first" aria-labelledby="in-wh">
<div class="pc-sh"><div><span class="pc-k">Who it’s for</span><h2 id="in-wh" class="pc-h2">Built for organizations that grow people.</h2></div></div>
<div class="cx-who">''' + ''.join('<div class="cx-wt2"><span class="cx-ui">' + ic(i, 20) + '</span><b>' + t + '</b><small>' + d + '</small></div>' for i, t, d in WHO) + '''</div>
</section>'''

# ---------- what you can do: Creators tab list + workspace window ----------
G, B, A, N = 'green', 'blue', 'amber', ''
AREAS = [
    ('Create', 'Courses, certifications, career paths and programs.', 'Programs', '84 programs', [('84', 'Programs'), ('12', 'Career paths'), ('9', 'Certifications'), ('410', 'Courses')],
     [('Graduate Data Program', 76, 'Live', G), ('MBA Foundations', 64, 'Live', G), ('Nursing CPD', 55, 'Live', G), ('Cloud & Security Pathway', 48, 'Enrolling', B), ('Teaching Excellence', 20, 'Draft', N)]),
    ('Deliver', 'Enrol learners, run cohorts, keep learning on track.', 'Cohorts', 'Autumn intake', [('46', 'Active cohorts'), ('28', 'Average size'), ('7', 'Starting soon'), ('94%', 'Seats filled')],
     [('Data 2026A', 82, 'Week 6 of 12', B), ('MBA 2026-1', 60, 'Week 4 of 16', B), ('Nursing CPD Oct', 40, 'Week 2 of 8', B), ('Security Oct', 10, 'Starts 14 Oct', A), ('Research Methods B', 95, 'Final week', G)]),
    ('Manage', 'Learners, creators, admins and what each can do.', 'People', 'All departments', [('4,820', 'Learners'), ('126', 'Creators'), ('14', 'Admins'), ('312', 'Need support')],
     [('School of Business', 74, 'On track', G), ('School of Computing', 81, 'On track', G), ('School of Health', 59, 'Watch', A), ('Continuing Education', 66, 'On track', G), ('Foundation Year', 52, 'Watch', A)]),
    ('Understand', 'Enrolment, progress, completion and results.', 'Analytics', 'Autumn term', [('72%', 'Active learning'), ('64%', 'Completion'), ('78%', 'Avg. assessment'), ('+11%', 'vs last term')],
     [('Enrolment', 92, 'High', G), ('Engagement', 72, 'Good', G), ('Progress', 68, 'Good', G), ('Assessment performance', 78, 'Good', G), ('Credential achievement', 46, 'Rising', B)]),
    ('Validate', 'Submit learning for independent review.', 'Validation', 'Institutional learning', [('31', 'Validated'), ('12', 'In review'), ('4', 'Findings open'), ('2', 'Revalidation due')],
     [('Graduate Data Program', 100, 'Validated', G), ('Nursing CPD', 100, 'Validated', G), ('MBA Foundations', 60, 'In review', A), ('Cloud & Security Pathway', 40, 'Findings open', A), ('Teaching Excellence', 0, 'Not submitted', N)]),
    ('Credential', 'Issue verifiable credentials to Backpacks.', 'Credentials', 'This term', [('2,214', 'Issued'), ('61%', 'Shared by learners'), ('9', 'Credential types'), ('0', 'Revoked')],
     [('Program Completion', 72, '1,120', G), ('Professional Certificate', 45, '384', G), ('Verified Project', 58, '520', G), ('Competency Badge', 33, '190', G), ('Micro-credential', 12, 'Draft', N)]),
]
STEPS = '<div class="tx-steps cx-steps in-steps" role="tablist" aria-label="What institutions can do">' + ''.join(
    '<button type="button" role="tab" class="tx-step {{ws.s%d.cls}}" aria-selected="{{ws.s%d.sel}}" onClick="{{ws.s%d.pick}}"><span class="tx-num">%d</span><span style="display: flex; flex-direction: column; gap: 2px"><span class="tx-st">%s</span><span class="tx-sd">%s</span></span></button>' % (i, i, i, i + 1, a[0], a[1])
    for i, a in enumerate(AREAS)) + '</div>'
WIN = '''<div class="ci-win cx-win in-win" role="tabpanel" aria-label="{{ws.title}}">
<div class="ci-wk"><span>Meridian University · {{ws.title}}</span><span class="ds-tag">{{ws.sub}}</span></div>
<div class="in-kp">
<sc-for list="{{ws.kpis}}" as="k" hint-placeholder-count="4"><span class="in-k"><b>{{k.v}}</b>{{k.k}}</span></sc-for>
</div>
<sc-for list="{{ws.rows}}" as="r" hint-placeholder-count="5"><div class="ci-row in-r"><span class="in-rn">{{r.a}}</span><i class="in-rb"><s style="width: {{r.pct}}"></s></i><span class="ds-tag {{r.cls}}">{{r.tag}}</span></div></sc-for>
<span class="cx-add in-ill">Meridian University is an illustrative example.</span>
</div>'''
DO = '''<section class="pc-sec cx-sec" id="in-do" aria-labelledby="in-dh">
<div class="cx-studio">
<div class="cx-sl">
<span class="pc-k">What you can do</span>
<h2 id="in-dh" class="pc-h2">One place for your whole learning ecosystem.</h2>
''' + STEPS + '''
</div>
''' + WIN + '''
</div>
</section>'''

# ---------- AI for institutions: Nova card with Link 2 switches ----------
AIS = [('AI Learning Coach', 'Supports learners with their course and progress context.'), ('AI Creator Assistance', 'Helps educators build and improve learning.'), ('AI Recommendations', 'Suggests personal learning pathways.'), ('AI Support', 'Answers common questions, then hands over to people.'), ('Assessment help', 'Hints during graded work.')]
AI = '''<section class="pc-sec cx-sec" aria-labelledby="in-ai">
<div class="in-ai">
<div><span class="pc-k">AI for institutions</span><h2 id="in-ai" class="pc-h2">AI that works inside your learning environment.</h2><p class="pc-p">It uses your learners’ course and progress context. You decide how it’s set up, area by area.</p></div>
<div class="nova-card in-aic">
<div class="in-aih">''' + AVN + '''<span><b>AI settings</b><small>Meridian University</small></span></div>
<sc-for list="{{ai.rows}}" as="a" hint-placeholder-count="5"><div class="in-air"><span><b>{{a.t}}</b><small>{{a.d}}</small></span><button type="button" class="hp-sw {{a.cls}}" role="switch" aria-checked="{{a.on}}" aria-label="{{a.t}}" onClick="{{a.flip}}"></button></div></sc-for>
</div>
</div>
</section>'''

# ---------- structure + credentials ----------
def grp(t, d, chips):
    return '<li><span class="in-gt"><b>%s</b><small>%s</small></span>%s</li>' % (t, d, ('<span class="in-gc">' + ''.join('<span class="ds-tag">%s</span>' % c for c in chips) + '</span>') if chips else '')
PROOF = [(dashgen.I['cred'], 'Professional Certificate'), (dashgen.I['proj'], 'Verified Project'), (dashgen.I['cert'], 'Program Completion'), (dashgen.I['skill'], 'Competency Badge')]
SC = '''<section class="pc-sec cx-sec" aria-label="Structure and credentials">
<div class="in-sc">
<div class="ds-card in-card">
<span class="pc-k">Institutional structure</span>
<h2 class="pc-h2">Your organization, with roles that fit.''' + tip('Role-based permissions decide what each person can see and do.') + '''</h2>
<div class="in-tree"><span class="in-root"><span class="in-rm">MU</span>Meridian University</span>
<ul>''' + grp('Admins', 'Workspace, billing and permissions', []) + grp('Creators', 'Build the learning', ['Teachers', 'Experts', 'Teams']) + grp('Validators', 'Review quality', ['Educational', 'Subject matter', 'Assessment']) + grp('Learners', 'Students, employees and members', []) + '''</ul></div>
</div>
<div class="ds-card in-card">
<span class="pc-k">Credentials</span>
<h2 class="pc-h2">Give achievement somewhere to live.</h2>
<p class="pc-p">Eligible achievements become verifiable credentials in each learner’s Digital Backpack.</p>
<div class="lr-pfs in-pfs">''' + ''.join('<div class="lr-pf"><span class="lr-pf-top"><span class="lr-pf-i">' + ic(i, 22) + '</span><span class="lr-pf-ok" title="Verifiable" aria-label="Verifiable">' + ck(11, 3.4) + '</span></span><b>' + t + '</b><small>Issued by Meridian University</small></div>' for i, t in PROOF) + '''</div>
</div>
</div>
</section>'''

# ---------- validation: same track as Creators ----------
VSTEPS = [('Create', 'Your team builds the program.'), ('Submit', 'Send applicable learning for review.'), ('Validators assigned', 'Qualified, independent experts.'), ('Review', 'Questions and clarifications in one place.'), ('Validated', 'A clear decision and a public record.'), ('Visible status', 'Learners see the seal on your program.')]
VAL = cregen.VAL.replace('cx-va', 'in-va').replace('Build it. Then prove the quality behind it.', 'Quality you can demonstrate.').replace('Independent experts review your work. Validated learning carries the Credalio seal, linked to a public Validation Record.', 'Submit applicable programs for independent validation. Validated programs carry the Credalio seal and a public Validation Record.')
ol = re.search(r'<ol class="ko-path cx-path">.*?</ol>', VAL, re.S).group(0)
VAL = VAL.replace(ol, '<ol class="ko-path cx-path">' + ''.join('<li%s><span class="ko-dot">%s</span><span><b>%s</b><span>%s</span></span></li>' % (' class="cx-ok"' if i == 4 else '', cregen.SEAL.replace('width="11" height="11"', 'width="28" height="28"') if i == 4 else str(i + 1), t, d) for i, (t, d) in enumerate(VSTEPS)) + '</ol>')

# ---------- enterprise integration ----------
I_KEY = '<circle cx="8" cy="15" r="4"></circle><path d="m11 12 9-9M17 6l3 3"></path>'
I_PLUG = '<path d="M9 3v5M15 3v5M6 8h12v3a6 6 0 0 1-12 0zM12 17v4"></path>'
I_SHLD = '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"></path><path d="m9 12 2 2 4-4"></path>'
I_PAL = '<path d="M12 3a9 9 0 1 0 0 18c1.1 0 1.6-.9 1.2-1.8-.5-1-.1-2.2 1.1-2.2H17a4 4 0 0 0 4-4c0-5.5-4-10-9-10z"></path><circle cx="7.5" cy="11" r="1"></circle><circle cx="12" cy="7.5" r="1"></circle><circle cx="16.5" cy="11" r="1"></circle>'
INT = [(I_KEY, 'SSO & identity'), (dashgen.I['lock'], 'Role-based access'), (I_PLUG, 'APIs & integrations'), (dashgen.I['settings'], 'Custom AI setup'), (dashgen.I['dash'], 'Reporting'), (dashgen.I['help'], 'Enterprise support'), (I_SHLD, 'Data & privacy controls'), (I_PAL, 'Your branding')]
INTS = '''<section class="pc-sec cx-sec" aria-labelledby="in-it">
<div class="pc-sh"><div><span class="pc-k">Enterprise integration</span><h2 id="in-it" class="pc-h2">Built to fit your environment.</h2></div></div>
<div class="in-int">''' + ''.join('<span class="in-i"><span class="cx-ui">' + ic(i, 20) + '</span>' + t + '</span>' for i, t in INT) + '''</div>
</section>'''

# ---------- final CTA: Landing band ----------
FC = block(L, '<section aria-labelledby="fc-h"')
FC = re.sub(r'<form class="ds-ask fc-form".*?</form>', btn('Talk to Credalio', TALK, 'cx-fb'), FC, flags=re.S)
FC = FC.replace('Your next version starts here.', 'Let’s shape Credalio around your institution.').replace('Tell Credalio who you want to become. We’ll help you build the path.', 'Tell us about your organization. We’ll show you a workspace that fits.')
FC = re.sub(r'<span class="fc-note">.*?</span>\n', '', FC, flags=re.S)
FC = cregen.compact_fc(FC)

NAVH = nav('For institutions').replace('<a class="sx-cta" href="#">Create account</a>', '<a class="sx-cta" href="OnbWelcome.dc.html">Create account</a>')
HERO = HERO.replace('<div class="ci-door ci-in cx-hero in-hero">', '<div class="ci-door ci-in cx-hero in-hero">\n' + NAVH.replace('<header class="sx-nav">', '<header class="sx-nav sx-in">'), 1)

CSS = r'''.in-hero .cx-wl{color:#1652F0}
.in-hero .ci-copy{max-width:540px}
.in-hero .ci-vis{top:156px}
.in-hero .sx-link:hover{background:rgba(255,255,255,.7)}
.in-hero .sx-link-on{background:#FFFFFF}
.in-hero .cx-f1{left:-110px;bottom:-50px}
.in-kp{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px}
.in-k{display:flex;flex-direction:column;gap:2px;padding:10px 12px;border-radius:12px;background:#F5F8FF;font-size:11.5px;color:#5B6582}
.in-kp b{font-size:18px;font-weight:600;color:#0B1433;letter-spacing:-.3px}
.in-bar{display:flex;flex-direction:column;gap:6px;padding:4px 2px}
.in-bar span{display:flex;justify-content:space-between;font-size:12px;color:#5B6582}
.in-bar b{font-weight:600;color:#0B1433}
.in-bar i,.in-rb{display:block;height:8px;border-radius:9px;background:#EEF1F7;overflow:hidden}
.in-bar s,.in-rb s{display:block;height:100%;border-radius:9px;background:#1652F0}
.in-rv{margin-left:auto;font-weight:600;color:#0B1433}
.in-first{padding-top:96px}
.in-steps .tx-step{padding:13px 0}
.in-win{height:auto;min-height:0}
.in-win .in-kp b{font-size:20px}
.in-r{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr) 116px;gap:14px}
.in-rn{font-weight:500;color:#0B1433;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.in-r .ds-tag{justify-self:end}
.in-ill{margin-top:auto;padding-top:6px}
.in-ai{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:64px;align-items:center}
.in-aic{border-radius:22px;padding:24px;display:flex;flex-direction:column;gap:8px}
.in-aih{display:flex;align-items:center;gap:12px;margin-bottom:8px}
.in-aih .nv-av{width:44px;height:44px}
.in-aih span{display:flex;flex-direction:column}
.in-aih b,.in-air b{font-size:15px;font-weight:600}
.in-aih small,.in-air small{font-size:13px;color:#5B6582}
.in-air{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:14px 16px;border-radius:14px;background:rgba(255,255,255,.82)}
.in-air > span{display:flex;flex-direction:column;gap:2px}
.hp-sw{position:relative;width:44px;height:26px;flex-shrink:0;border-radius:999px;border:0;background:#CBD3E6;cursor:pointer;transition:background .2s ease}
.hp-sw::after{content:'';position:absolute;top:3px;left:3px;width:20px;height:20px;border-radius:50%;background:#FFFFFF;box-shadow:0 1px 3px rgba(11,20,51,.2);transition:left .2s ease}
.hp-sw.on{background:#1652F0}
.hp-sw.on::after{left:21px}
.in-sc{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:18px}
.in-card{padding:32px;border-radius:22px;display:flex;flex-direction:column}
.in-card .pc-h2{font-size:30px}
.in-tree{margin-top:26px}
.in-root{display:inline-flex;align-items:center;gap:10px;height:44px;padding:0 16px 0 6px;border-radius:999px;background:#0B1433;color:#FFFFFF;font-size:14px;font-weight:600}
.in-rm{width:32px;height:32px;border-radius:999px;background:#1652F0;display:flex;align-items:center;justify-content:center;font-size:11px}
.in-tree ul{list-style:none;margin:0 0 0 21px;padding:8px 0 0;border-left:2px solid #1652F0;display:flex;flex-direction:column;gap:10px}
.in-tree li{position:relative;margin-left:22px;padding:12px 14px;border-radius:14px;background:#F5F8FF;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
.in-tree li::before{content:'';position:absolute;left:-24px;top:50%;width:22px;height:2px;background:#1652F0}
.in-tree li:last-child::after{content:'';position:absolute;left:-26px;top:calc(50% + 2px);bottom:-12px;width:4px;background:#FFFFFF}
.in-gt{display:flex;flex-direction:column;gap:1px}
.in-gt b{font-size:15px;font-weight:600}
.in-gt small{font-size:13px;color:#5B6582}
.in-gc{display:flex;flex-wrap:wrap;gap:6px}
.in-gc .ds-tag{background:#FFFFFF}
.in-pfs{grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin-top:24px}
.in-pfs .lr-pf{padding:18px}
.in-pfs .lr-pf:hover{transform:none;box-shadow:none;border-color:#E6EAF3}
.in-int{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.in-i{display:flex;align-items:center;gap:14px;padding:16px 18px;border-radius:18px;border:1.5px solid #E6EAF3;font-size:15px;font-weight:600}
@media (min-width: 961px){
.in-hero{height:660px}
}
@media (max-width: 1180px){
.in-int{grid-template-columns:repeat(2,minmax(0,1fr))}
}
@media (max-width: 960px){
.in-first{padding-top:64px}
.in-ai,.in-sc{grid-template-columns:minmax(0,1fr);gap:24px}
.in-hero .ci-vis{top:auto}
}
@media (max-width: 760px){
.in-hero .cx-wl{align-self:center}
.in-hero .ci-row,.in-hero .in-bar{display:none}
.in-steps{flex-direction:row;gap:8px;overflow-x:auto;margin:20px -20px 0;padding:2px 20px 4px;scroll-padding:0 20px;scroll-snap-type:x mandatory;scrollbar-width:none}
.in-steps::-webkit-scrollbar{display:none}
.in-steps .tx-step{flex:0 0 auto;display:flex;align-items:center;gap:8px;height:44px;padding:0 16px 0 6px !important;border:1.5px solid #E6EAF3 !important;border-radius:999px;scroll-snap-align:start;opacity:1}
.in-steps .tx-step-run{border-color:#1652F0 !important;background:#EAF0FF}
.in-steps .tx-num{width:30px;height:30px;font-size:12px;box-shadow:none !important}
.in-steps .tx-sd{display:none}
.in-steps .tx-st{font-size:14.5px;font-weight:500;white-space:nowrap}
.in-kp{grid-template-columns:repeat(2,minmax(0,1fr))}
.in-r{grid-template-columns:minmax(0,1fr) auto}
.in-rb{display:none !important}
.in-aic{padding:18px 14px}
.in-air{padding:12px}
.in-card{padding:24px 18px}
.in-card .pc-h2{font-size:24px}
.in-tree li{margin-left:18px}
.in-tree li::before{left:-20px;width:18px}
.in-tree li:last-child::after{left:-22px}
.in-pfs{display:grid;overflow:visible;margin:20px 0 0;padding:0;grid-template-columns:minmax(0,1fr) minmax(0,1fr)}
.in-pfs > *{padding:14px}
.in-int{grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:10px}
.in-i{flex-direction:column;align-items:flex-start;gap:10px;padding:14px;font-size:14px}
}
'''

BODY = '''<div style="font-family: 'Google Sans', system-ui, sans-serif; color: #0B1433; background: #FFFFFF">
''' + HERO + '''
''' + WHOS + '''
''' + DO + '''
''' + AI + '''
''' + SC + '''
''' + VAL + '''
''' + INTS + '''
''' + FC + '''
''' + cregen.LFOOT + '''
</div>'''

DATA = [[a[0], a[2], a[3], a[4], a[5]] for a in AREAS]
JS = '''
var AREAS = ''' + json.dumps(DATA, ensure_ascii=False) + ''';
var AIS = ''' + json.dumps(AIS, ensure_ascii=False) + ''';
class Component extends DCLogic {
  constructor(props) { super(props); this.state = { tab: 0, ai: [true, true, true, true, false] }; }
  renderVals() {
    var self = this, t = this.state.tab, a = AREAS[t], ws = { title: a[1], sub: a[2] };
    AREAS.forEach(function (x, k) { ws['s' + k] = { cls: k === t ? 'tx-step-run' : 'tx-step-wait', sel: k === t ? 'true' : 'false', pick: function () { self.setState({ tab: k }); } }; });
    ws.kpis = a[3].map(function (k) { return { v: k[0], k: k[1] }; });
    ws.rows = a[4].map(function (r) { return { a: r[0], pct: r[1] + '%', tag: r[2], cls: r[3] }; });
    var rows = AIS.map(function (x, i) { var on = self.state.ai[i]; return { t: x[0], d: i === 4 && !on ? 'Off by your policy. ' + x[1] : x[1], on: on ? 'true' : 'false', cls: on ? 'on' : '', flip: function () { var n = self.state.ai.slice(); n[i] = !n[i]; self.setState({ ai: n }); } }; });
    return { ws: ws, ai: { rows: rows }, ''' + cregen.FTSUB + ''' };
  }
}
'''

HTML = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>For Institutions</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">
<style>
''' + BASE_CSS + style(L) + '\n' + KIT_CSS + '\n' + cregen.DCSS + '\n' + pricegen.CSS + '\n' + cregen.CSS + '\n' + CSS + '''</style>
</helmet>
''' + BODY + '''
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":4680}}'>''' + JS + '''</script>
</body>
</html>
'''

if __name__ == '__main__':
    open(OUT, 'w').write(HTML)
    print('wrote', OUT, len(HTML))
