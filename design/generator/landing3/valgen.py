# How Validation Works (TRST-001..005, 007, 008). Built from LIVE shared pieces, never redrawn:
#   Landing.dc.html  -> Trusted learning section (tx-*, TrustPart animation, seal, status pill states) as the hero, final CTA (fc-*)
#   Creators page    -> tab list + window (cx-*), ticks (cx-ticks), icon tile (cx-ui); Institutions -> mobile pill tabs (in-steps)
#   Link 2 CR-VAL-WS -> request thread (rq-thread, rq-m, va avatars, rq-att), dl meta (rq-meta)
#   Pricing          -> step track (ko-path, Link 2 CR-WAL-OUT)
# Usage: python3 valgen.py -> design/canvas3/project/Validation.dc.html
import os, re, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from kit import AURORA_JS, KIT_CSS, tip, btn, ck
from shell import BASE_CSS, nav, FOOT
import dashgen, pricegen, cregen, insgen

P = os.path.join(HERE, '../../canvas3/project/')
OUT = P + 'Validation.dc.html'
L = cregen.L
block, style, ic = pricegen.block, pricegen.style, dashgen.ic
V2 = open(os.path.join(HERE, '../../canvas2/project/CR-VAL-WS.dc.html')).read()
RQCSS = '\n'.join(l for l in style(V2).split('\n') if re.match(r'\.(rq-(thread|m|who|att)\b|rq-m |rq-m\.|rq-meta|va\{|va\.(v2|me|mo|sm)\{)', l) and '@' not in l and not l.startswith('.rq-m .va'))
# first-definition only (the CR-VAL-WS mobile overrides follow later in its sheet)
seen = set(); keep = []
for l in RQCSS.split('\n'):
    sel = l.split('{')[0]
    if sel in seen: continue
    seen.add(sel); keep.append(l)
RQCSS = '\n'.join(keep)

# ---------- hero: Landing Trusted learning section ----------
TX = block(L, '<section aria-labelledby="tx-h"')
SEALBIG = re.search(r'<svg viewBox="0 0 100 100" style="position: absolute; inset: 0; width: 100%; height: 100%">.*?</svg>', TX, re.S).group(0)
def seal(n, size):
    return SEALBIG.replace('txSg', 'vSg' + n).replace('txSt', 'vSt' + n).replace(' style="position: absolute; inset: 0; width: 100%; height: 100%"', ' width="%d" height="%d" aria-hidden="true"' % (size, size))
OKI = re.search(r'<sc-if value="\{\{tv.pOk\}\}"[^>]*>(.*?)</sc-if>', TX, re.S).group(1)
ARR = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'
for a, b in [
    ('<section aria-labelledby="tx-h"', '<section class="vx-hero" aria-labelledby="tx-h"'),
    ('padding: 112px 48px;', 'padding: 48px 48px 72px;'),
    ('>Trusted learning</span>', '>Credalio Validation</span>'),
    ('<h2 id="tx-h" class="tx-h2 tx-o1">Know the quality before you commit your time.</h2>', '<h1 id="tx-h" class="tx-h2 tx-o1">See what stands behind the learning.</h1>'),
    ('Independent experts can take a course apart and check every layer before it earns the seal.', 'Qualified validators review learning independently, each in their own area, before a decision is made. You see the result on every course.'),
]:
    assert TX.count(a) == 1, a
    TX = TX.replace(a, b)
TX = re.sub(r'<a class="ds-ghost tx-link" href="[^"]*">How validation works<svg.*?</svg></a>', '<div class="cx-acts vx-acts">' + btn('Explore validated learning', 'Courses.dc.html', 'ci-btn') + '<a class="ds-link" href="#">Become a validator' + ARR + '</a></div>', TX, flags=re.S)
assert 'vx-acts' in TX

# ---------- statuses: the hero pill states ----------
STAT = [('green', OKI, 'Credalio Validated', 'Reviewed and approved', 'The validation process is complete for the version you see. Only this status carries the seal.'),
        ('blue', '<span class="tx-spin"></span>', 'Review in progress', 'Submitted, being reviewed', 'Validators are reviewing it now. It isn’t validated yet.'),
        ('line', '<span class="vx-ring"></span>', 'Not yet validated', 'No completed review', 'You can still learn from it. It just hasn’t been through a validator review.')]
STATS = '''<section class="pc-sec cx-sec" aria-labelledby="vx-st">
<div class="pc-sh"><div><span class="pc-k">Validation status</span><h2 id="vx-st" class="pc-h2">Only one status carries the seal.</h2></div></div>
<div class="vx-stats">''' + ''.join('<div class="vx-s%s">%s<span class="ds-tag lg %s">%s%s</span><b>%s</b><p>%s</p></div>' % (' vx-s-ok' if i == 0 else '', ('<span class="vx-seal">' + seal('a', 72) + '</span>') if i == 0 else '', c, ico, t, sub, d) for i, (c, ico, t, sub, d) in enumerate(STAT)) + '''</div>
</section>'''

# ---------- what gets reviewed ----------
I_EDU = '<path d="M3 9l9-5 9 5-9 5z"></path><path d="M7 11.5V16c0 1.5 2.2 3 5 3s5-1.5 5-3v-4.5"></path>'
I_ACC = '<circle cx="11" cy="11" r="7"></circle><path d="m20 20-3.5-3.5"></path><path d="m8 11 2 2 4-4"></path>'
I_ASM = '<path d="M9 4h6v3H9z"></path><path d="M7 5H5v16h14V5h-2"></path><path d="m9 14 2 2 4-4"></path>'
ROLES = [(I_EDU, 'Educational Validator', 'Educational quality', ['Clear learning outcomes', 'Lessons match the outcomes', 'Activities build understanding', 'Progression makes sense'], 'Subject accuracy outside their expertise.'),
         (I_ACC, 'Subject Matter Validator', 'Subject accuracy', ['Facts and technical detail', 'Relevance and depth', 'Current material', 'Practical relevance'], 'Whether the learning design or assessments work.'),
         (I_ASM, 'Assessment Validator', 'Assessment quality', ['Aligned with the outcomes', 'Measures real competence', 'Right difficulty', 'Fair, defensible scoring'], 'Subject accuracy of the content.')]
COND = [('AI Validator', 'Where the learning uses AI features.'), ('Security & Privacy Validator', 'Where it handles personal data or connected systems.')]
CK11 = ck(11, 3.4)
REV = '''<section class="pc-sec cx-sec" aria-labelledby="vx-rv">
<div class="pc-sh"><div><span class="pc-k">What gets reviewed</span><h2 id="vx-rv" class="pc-h2">Different experts look at different things.</h2><p class="pc-p">No single validator checks everything. Each one reviews only their own area.</p></div></div>
<div class="vx-roles">''' + ''.join('<div class="ds-card vx-r"><span class="cx-ui">' + ic(i, 20) + '</span><span class="vx-rk">' + k + '</span><h3>' + t + tip('Doesn’t decide: ' + no, 'r') + '</h3><ul class="cx-ticks">' + ''.join('<li><i>' + CK11 + '</i>' + x + '</li>' for x in L4) + '</ul></div>' for i, k, t, L4, no in ROLES) + '''</div>
<div class="vx-cond">''' + ''.join('<div class="vx-c"><span class="ds-tag">When needed</span><b>' + t + '</b><small>' + d + '</small></div>' for t, d in COND) + '''</div>
</section>'''

# ---------- the journey: Creators tab list + window ----------
G, B, A, N = 'green', 'blue', 'amber', ''
J = [
    ('Submit', 'The creator asks for validation.', 'Submission', [('Experience', 'Data Foundations: Spreadsheets to SQL', None), ('Version', 'v2.1', None), ('Submitted', '2 September 2026', None)], None),
    ('Scope', 'Credalio works out which reviews apply.', 'Standard course · required reviews', [('Educational', 'Required', G), ('Subject matter', 'Required', G), ('Assessment', 'Where applicable', G), ('AI · Security & Privacy', 'Added where needed', N)], None),
    ('Assign', 'Qualified validators are matched.', 'Review team', None, [('EV', 'Educational Validator', 'Learning design'), ('SM', 'Subject Matter Validator', 'Data analytics'), ('AV', 'Assessment Validator', 'Assessment design')]),
    ('Review', 'Each validator reviews their own area.', 'Example checklist', [('Learning outcomes are clear', 'Meets standard', G), ('Module 3 benchmark is sourced', 'Clarification required', B), ('Practice activity difficulty', 'Revision required', A), ('Final assessment matches outcomes', 'Meets standard', G)], None),
    ('Clarify', 'Findings are answered with evidence.', 'Finding #3', [('Clarification requested', 'Evidence requested', B), ('Creator response', 'Source attached', N), ('Validator review', 'Finding resolved', G)], None),
    ('Decide', 'A decision once everything is met.', 'Possible outcomes', [('All requirements met', 'Credalio Validated', G), ('Requirements outstanding', 'Revisions first', A)], None),
    ('Publish', 'The seal and record go live.', 'Published', [('Validation ID', 'VAL-CRD-004821', None), ('Version validated', 'v2.1', None), ('Seal', 'Credalio Validated', G), ('Record', 'Public', None)], None),
    ('Revalidate', 'Major updates are reviewed again.', 'Version status', [('v2.1', 'Validated', G), ('v3.0 · major update', 'Revalidation required', A)], None),
]
STEPS = '<div class="tx-steps cx-steps in-steps vx-steps" role="tablist" aria-label="The validation journey">' + ''.join(
    '<button type="button" role="tab" class="tx-step {{jv.s%d.cls}}" aria-selected="{{jv.s%d.sel}}" onClick="{{jv.s%d.pick}}"><span class="tx-num">%d</span><span style="display: flex; flex-direction: column; gap: 2px"><span class="tx-st">%s</span><span class="tx-sd">%s</span></span></button>' % (i, i, i, i + 1, a[0], a[1])
    for i, a in enumerate(J)) + '</div>'
WIN = '''<div class="ci-win cx-win vx-win" role="tabpanel" aria-label="{{jv.name}}">
<div class="ci-wk"><span>Validation · Data Foundations</span><span class="ds-tag blue"><span>Step {{jv.n}} of 8</span></span></div>
<span class="cx-wt">{{jv.panel}}</span>
<sc-if value="{{jv.isRows}}" hint-placeholder-val="{{ true }}"><sc-for list="{{jv.rows}}" as="r" hint-placeholder-count="4"><div class="ci-row vx-row"><span class="vx-k">{{r.k}}</span><sc-if value="{{r.tag}}" hint-placeholder-val="{{ false }}"><span class="ds-tag {{r.cls}}">{{r.v}}</span></sc-if><sc-if value="{{r.plain}}" hint-placeholder-val="{{ true }}"><b class="vx-v">{{r.v}}</b></sc-if></div></sc-for></sc-if>
<sc-if value="{{jv.isTeam}}" hint-placeholder-val="{{ false }}"><sc-for list="{{jv.team}}" as="c" hint-placeholder-count="3"><div class="ci-row cx-pp"><span class="va v2">{{c.i}}</span><span class="cx-pn"><b>{{c.role}}</b><small>{{c.exp}}</small></span></div></sc-for></sc-if>
<div class="vx-wf"><button type="button" class="ds-link" onClick="{{jv.prev}}" aria-label="Previous step">Previous</button><button type="button" class="ds-ghost sm" onClick="{{jv.next}}">{{jv.nextLabel}}</button></div>
</div>'''
JOUR = '''<section class="pc-sec cx-sec" aria-labelledby="vx-jh">
<div class="cx-studio vx-jr">
<div class="cx-sl">
<span class="pc-k">The validation journey</span>
<h2 id="vx-jh" class="pc-h2">From submission to Credalio Validated.</h2>
''' + STEPS + '''
</div>
''' + WIN + '''
</div>
</section>'''

# ---------- clarification: Link 2 request thread ----------
PDF = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"></path><path d="M14 3v5h5"></path></svg>'
CLAR = '''<section class="pc-sec cx-sec" aria-labelledby="vx-cl">
<div class="in-ai vx-cl">
<div><span class="pc-k">Clarification & revision</span><h2 id="vx-cl" class="pc-h2">Validation isn’t just a checkbox.</h2><p class="pc-p">Findings are raised, answered with evidence and resolved on the record. Nobody simply presses Approve.</p></div>
<div class="ds-card vx-th">
<div class="vx-thh"><span class="ds-tag">Finding #3 · Subject matter</span><span class="ds-tag green">Resolved</span></div>
<div class="rq-thread">
<div class="rq-m"><span class="va v2">SM</span><div><span class="rq-who"><b>Subject Matter Validator</b> · Clarification required</span><p>The source for the industry benchmark in Module 3 can’t be verified. Please add evidence.</p></div></div>
<div class="rq-m me"><span class="va me">CR</span><div><span class="rq-who"><b>Creator</b> · Evidence submitted</span><p>Updated the source and attached the supporting dataset.</p><span class="rq-att">''' + PDF + '''benchmark-source.pdf</span></div></div>
<div class="rq-m"><span class="va v2">SM</span><div><span class="rq-who"><b>Subject Matter Validator</b> · Finding resolved</span><p>Evidence reviewed. The benchmark now has a verifiable source.</p></div></div>
</div>
</div>
</div>
</section>'''

# ---------- decision + versioning ----------
VERS = [('v2.1', 'Validated', 'green'), ('v3.0', 'Revalidation required', 'amber'), ('v3.0', 'Validated', 'green')]
DEC = '''<section class="pc-sec cx-sec" aria-label="Decision and versioning">
<div class="in-sc">
<div class="ds-card in-card vx-dec">
<div class="vx-dh">''' + seal('b', 64) + '''<div><span class="pc-k">The decision</span><h2 class="pc-h2">Credalio Validated</h2></div></div>
<p class="pc-p">Given when every applicable requirement is met.</p>
<dl class="vx-dl"><div><dt>Validation ID</dt><dd>VAL-CRD-004821</dd></div><div><dt>Experience</dt><dd>Data Foundations</dd></div><div><dt>Version reviewed</dt><dd>v2.1</dd></div><div><dt>Validated</dt><dd>24 September 2026</dd></div></dl>
<div class="vx-sc"><span class="vx-k">Scope</span><span class="ds-tag">Educational quality</span><span class="ds-tag">Subject matter</span><span class="ds-tag">Assessment</span></div>
<a class="ds-link" href="#">View Validation Record''' + dashgen.ARR_S + '''</a>
</div>
<div class="ds-card in-card vx-ver">
<span class="pc-k">Versioning</span>
<h2 class="pc-h2">Validation belongs to the version reviewed.''' + tip('A course can’t be validated once, then rewritten under the same seal. Each validated version gets its own entry on the public record.', 'r') + '''</h2>
<p class="pc-p">When a creator publishes a major update, the new version is reviewed again.</p>
<ol class="ko-path vx-vp">''' + ''.join('<li class="vx-v-%s"><span class="ko-dot">%s</span><span><b>%s</b><span class="ds-tag %s">%s</span></span></li>' % (c, CK11 if c == 'green' else '!', v, c, s) for v, s, c in VERS) + '''</ol>
<div class="vx-vn"><span>Major update published</span><span>Validator review</span></div>
</div>
</div>
</section>'''

# ---------- final CTA ----------
FC = block(L, '<section aria-labelledby="fc-h"')
FC = re.sub(r'<form class="ds-ask fc-form".*?</form>', btn('Explore validated learning', 'Courses.dc.html', 'cx-fb'), FC, flags=re.S)
FC = FC.replace('Your next version starts here.', 'Learn with confidence.').replace('Tell Credalio who you want to become. We’ll help you build the path.', 'Look for the seal, then check the record behind it.')
FC = re.sub(r'<span class="fc-note">.*?</span>\n', '', FC, flags=re.S)

NAVH = nav('').replace('<a class="sx-cta" href="#">Create account</a>', '<a class="sx-cta" href="OnbWelcome.dc.html">Create account</a>')

CSS = RQCSS + r'''
.vx-hero .tx-h2{margin:0}
.vx-acts{margin-top:16px}
.vx-acts .ds-link{display:inline-flex;align-items:center;gap:6px;font-size:15px;font-weight:600}
.vx-stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.vx-stats > div{position:relative;display:flex;flex-direction:column;align-items:flex-start;gap:10px;padding:28px;border-radius:22px;border:1.5px solid #E6EAF3;background:#FFFFFF;overflow:hidden}
.vx-stats b{margin-top:6px;font-size:17px;font-weight:600}
.vx-stats p{margin:0;font-size:15px;line-height:1.55;color:#4A5578}
.vx-s-ok{border-color:#DCE5FB !important;background:linear-gradient(160deg,#F5F8FF 0%,#FFFFFF 70%) !important}
.vx-seal{position:absolute;right:20px;top:18px;filter:drop-shadow(0 10px 18px rgba(22,82,240,.25))}
.vx-ring{width:12px;height:12px;border-radius:999px;border:2px solid #CBD3E6;box-sizing:border-box}
.vx-roles{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.vx-r{padding:28px;border-radius:22px;display:flex;flex-direction:column;align-items:flex-start}
.vx-rk{margin-top:16px;font-size:13px;font-weight:500;color:#8A93AD}
.vx-r h3{margin:4px 0 0;display:flex;align-items:center;font-size:21px;font-weight:600;letter-spacing:-.3px}
.vx-r .cx-ticks{margin-top:18px}
.vx-r .cx-ticks li{font-size:14.5px}
.vx-r .cx-ticks i{background:#E7F5EE;color:#0F6B45}
.vx-cond{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px;margin-top:16px}
.vx-c{display:flex;align-items:center;gap:14px;padding:16px 20px;border-radius:18px;background:#F7F9FD}
.vx-c b{font-size:15px;font-weight:600;white-space:nowrap}
.vx-c small{font-size:14px;color:#5B6582}
.vx-steps .tx-step{padding:10px 0}
.vx-steps .tx-sd{font-size:13.5px}
.vx-win{height:auto;min-height:400px}
.vx-row{gap:14px}
.vx-row .ds-tag{margin-left:auto}
.vx-k{color:#3A4566}
.vx-v{margin-left:auto;font-weight:600;color:#0B1433;text-align:right}
.vx-win .cx-pp .va{width:32px;height:32px;font-size:11px}
.vx-wf{margin-top:auto;display:flex;align-items:center;justify-content:space-between;padding-top:14px;border-top:1px solid #EEF1F7}
.vx-wf .ds-link{position:relative}
.vx-th{padding:24px;border-radius:22px}
.vx-thh{display:flex;align-items:center;justify-content:space-between;gap:10px}
.vx-th .rq-thread{margin-top:18px}
.vx-dh{display:flex;align-items:center;gap:16px}
.vx-dh .pc-h2{margin-top:2px}
.vx-ver .pc-h2{display:block}
.vx-ver .pc-h2 .tip{display:inline-flex;vertical-align:middle;margin-left:6px}
.vx-dec .pc-p,.vx-ver .pc-p{font-size:15.5px}
.vx-dl{margin:22px 0 0;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px;padding:18px;border-radius:16px;background:#F7F9FD}
.vx-dl dt{font-size:12.5px;color:#8A93AD}
.vx-dl dd{margin:3px 0 0;font-size:15px;font-weight:600}
.vx-sc{display:flex;flex-wrap:wrap;align-items:center;gap:6px;margin:18px 0 22px}
.vx-sc .vx-k{margin-right:6px;font-size:13px;color:#8A93AD}
.vx-dec > .ds-link{margin-top:auto}
.vx-vp{grid-template-columns:repeat(3,minmax(0,1fr));margin-top:32px}
.vx-vp li{padding:0 8px}
.vx-vp b{font-size:18px}
.vx-vp li > span:last-child{gap:8px}
.vx-vp .ko-dot{background:#FFFFFF}
.vx-vp li.vx-v-green .ko-dot{background:#0F6B45;border-color:#0F6B45;color:#FFFFFF}
.vx-vp li.vx-v-amber .ko-dot{background:#FFF4E0;border-color:#E8A33D;color:#8A5A00}
.vx-vp li:not(:last-child)::before{background:#CBD3E6}
.vx-vn{display:grid;grid-template-columns:1fr 1fr;margin:20px 16.6% 0;text-align:center;font-size:12.5px;color:#8A93AD}
@media (max-width: 1180px){
.vx-cond{grid-template-columns:minmax(0,1fr)}
}
@media (max-width: 960px){
.vx-stats,.vx-roles{grid-template-columns:minmax(0,1fr);gap:12px}
.vx-win{min-height:0}
.vx-vp{grid-template-columns:repeat(3,minmax(0,1fr)) !important;gap:0}
.vx-vp li{flex-direction:column !important;align-items:center !important;text-align:center !important;padding:0 4px !important}
.vx-vp li:not(:last-child)::before{left:calc(50% + 18px) !important;right:calc(-50% + 18px) !important;top:13px !important;bottom:auto !important;width:auto !important;height:2px !important}
.vx-vp li > span:last-child{align-items:center !important}
}
@media (max-width: 760px){
.vx-hero .tx-wrap{padding:24px 20px 48px !important}
.vx-acts{order:5;flex-direction:column;align-items:stretch;gap:6px}
.vx-acts .ds-btn{justify-content:space-between}
.vx-acts .ds-link{align-self:center;padding:12px 0}
.vx-th .rq-m .va{display:none}
.vx-roles{display:flex;overflow-x:auto;gap:12px;margin:0 -20px;padding:2px 20px 6px;scroll-padding:0 20px;scroll-snap-type:x mandatory;scrollbar-width:none}
.vx-roles::-webkit-scrollbar{display:none}
.vx-r{flex:0 0 84%;box-sizing:border-box;scroll-snap-align:start}
.vx-stats > div,.vx-r{padding:22px 18px}
.vx-seal svg{width:56px;height:56px}
.vx-c{flex-direction:column;align-items:flex-start;gap:6px}
.vx-th{padding:18px 14px}
.vx-thh{flex-wrap:wrap}
.vx-dl{grid-template-columns:minmax(0,1fr) minmax(0,1fr);padding:14px}
.vx-dh{gap:12px}
.vx-dh svg{width:52px;height:52px}
.vx-vp b{font-size:16px}
.vx-vp .ds-tag{white-space:normal;height:auto;padding:5px 8px;text-align:center;line-height:1.25}
.vx-vn{margin:16px 0 0;grid-template-columns:1fr 1fr;gap:8px;font-size:12px}
.vx-wf .ds-link::after{content:'';position:absolute;inset:-12px -8px}
}
'''

BODY = '''<div style="font-family: 'Google Sans', system-ui, sans-serif; color: #0B1433; background: #FFFFFF">
''' + NAVH + '''
''' + TX + '''
''' + STATS + '''
''' + REV + '''
''' + JOUR + '''
''' + CLAR + '''
''' + DEC + '''
''' + FC + '''
''' + FOOT + '''
</div>'''

JD = [[a[0], a[2], a[3], a[4]] for a in J]
PART = L[L.index('class Part {'):L.index('function momentVals')]
def jsblock(name):
    i = L.index('class ' + name); j = L.index('\nclass ', i + 10)
    return L[i:j]
TRUST = jsblock('TrustPart')
JS = '\nvar J = ' + json.dumps(JD, ensure_ascii=False) + ';\n' + PART + TRUST + '''
class JourneyPart extends Part {
  constructor(host) { super(host); this.state = { j: 0 }; }
  renderVals() {
    var self = this, t = this.state.j, a = J[t], o = { name: a[0], panel: a[1], n: t + 1, isRows: !!a[2], isTeam: !!a[3] };
    J.forEach(function (x, k) { o['s' + k] = { cls: k === t ? 'tx-step-run' : (k < t ? 'tx-step-done' : 'tx-step-wait'), sel: k === t ? 'true' : 'false', pick: function () { self.setState({ j: k }); } }; });
    o.rows = (a[2] || []).map(function (r) { var tag = r[2] !== null; return { k: r[0], v: r[1], tag: tag, plain: !tag, cls: r[2] || '' }; });
    o.team = (a[3] || []).map(function (c) { return { i: c[0], role: c[1], exp: c[2] }; });
    o.prev = function () { self.setState({ j: Math.max(0, t - 1) }); };
    o.next = function () { self.setState({ j: t < 7 ? t + 1 : 0 }); };
    o.nextLabel = t < 7 ? 'Next: ' + J[t + 1][0] : 'Back to start';
    return o;
  }
}
class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { v: 0 };
    this.parts = { tv: new TrustPart(this), jv: new JourneyPart(this) };
  }
  bump(now) {
    var self = this;
    if (now) { this.setState({ v: this.state.v + 1 }); return; }
    if (this.pend) return;
    this.pend = true;
    requestAnimationFrame(function () { self.pend = false; self.setState({ v: self.state.v + 1 }); });
  }
  componentDidMount() { for (var k in this.parts) if (this.parts[k].componentDidMount) this.parts[k].componentDidMount(); }
  componentWillUnmount() { for (var k in this.parts) if (this.parts[k].componentWillUnmount) this.parts[k].componentWillUnmount(); }
  renderVals() { var o = {}; for (var k in this.parts) o[k] = this.parts[k].renderVals(); return o; }
}
'''

HTML = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>How Validation Works</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">
<style>
''' + BASE_CSS + style(L) + '\n' + KIT_CSS + '\n' + cregen.DCSS + '\n' + pricegen.CSS + '\n' + cregen.CSS + '\n' + insgen.CSS + '\n' + CSS + '''</style>
</helmet>
''' + BODY + '''
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":4580}}'>''' + JS + '''</script>
</body>
</html>
'''

if __name__ == '__main__':
    open(OUT, 'w').write(HTML)
    print('wrote', OUT, len(HTML))
