"""Link 4 · Batch 1: course setup (focus flow) + course design (workspace).

Setup.dc.html  (prop step: type | delivery | review | how | welcome)   CR-STU-001, 002, 003, 004, 008
Studio.dc.html (prop page: home | basics | audience | career | careercert | skills | outcomes | skillmap | evidence |
                design | effort | summary)                              CR-STU-009 to CR-STU-019
Boards: STU-0xx(.dc.html) desktop 1440 + STU-0xx-Mobile 390, each a dc-import of its source.
"""
import json
from l4kit import *

# ======================================================================= SETUP (focus mode)
T = Toggles()

def fmt_card(icon, title, desc, best, size, on):
    k = T.new(on, 'fmt')
    return ('<button type="button" class="nw-f {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}"><span class="nw-fi">%s</span>'
            '<span class="nw-ck">%s</span><b>%s</b><span class="nw-fd">%s</span><span class="nw-fm"><span><em>Best for</em>%s</span>'
            '<span><em>Typical size</em>%s</span></span></button>') % (k, k, k, ic(icon, 22), ck(11), title, desc, best, size)

S_TYPE = '''<div class="fx-col">
<h1 class="fx-h1 ob-in">What will you create?</h1>
<p class="fx-sub ob-in2">Pick the format that fits what learners should be able to do at the end.</p>
<div class="nw-g ob-in3" role="group" aria-label="Format">%s</div>
<div class="fx-nova ob-in4">%s<label class="sr-only" for="fxq">What should learners achieve?</label><input id="fxq" placeholder="What should learners achieve?">%s</div>
<div class="fx-acts">%s</div>
</div>''' % (
    fmt_card('course', 'Course', 'A focused subject or skill, learned step by step.', 'One skill or topic', '2 to 30 hours', True) +
    fmt_card('cert', 'Professional certification', 'Assess and verify that someone can do the job.', 'Proving competence', 'Exam + practical', False) +
    fmt_card('path', 'Career path', 'A journey of courses, practice and credentials toward a role.', 'Getting into a role', 'Several courses', False) +
    fmt_card('program', 'Learning program', 'Structured learning over time, often with a cohort.', 'Groups and institutions', 'Weeks, with cohorts', False),
    nova_av('sm'), nchip('Help me choose'), btn('Continue', 'STU-002.dc.html'))

def deliv(icon, title, desc, feats, on):
    inner = '<span class="dv-i">%s</span><span class="dv-t"><b>%s</b><span>%s</span><span class="dv-f">%s</span></span>' % (
        ic(icon, 22), title, desc, ''.join('<span>%s</span>' % f for f in feats))
    return T.opt(inner, on, 'dlv', 'dv')

S_DELIV = '''<div class="fx-col">
<a class="fx-back" href="STU-001.dc.html">%s<span>Back</span></a>
<h1 class="fx-h1 ob-in">How will learners take this course?</h1>
<p class="fx-sub ob-in2">You can mix formats later. This sets what the Studio offers you.</p>
<div class="dv-g ob-in3" role="group" aria-label="Delivery">%s</div>
<div class="ob-in4" style="margin-top: 18px">%s</div>
<div class="fx-acts">%s</div>
</div>''' % (
    ICON(I['back'], 16, 2),
    deliv('play', 'Self-paced', 'Learners move through lessons in their own time.', ['Video, audio, text', 'Interactive activities', 'Projects and assessments'], False) +
    deliv('live', 'Live, instructor-led', 'Learning happens in scheduled live sessions.', ['Live classes', 'Attendance', 'Resources and assignments'], False) +
    deliv('mix', 'Hybrid', 'Self-paced lessons with scheduled live sessions.', ['Lessons + live classes', 'Practice and assignments', 'Assessments'], True),
    nova_sg('Hybrid works well for SQL. I’ll help you decide which parts land best live, like a weekly analysis clinic.'),
    btn('Continue', 'STU-003.dc.html'))

def rv(label, value, href):
    return '<div class="rv-r"><span class="rv-l">%s</span><span class="rv-v">%s</span>%s</div>' % (
        label, value, ('<a class="ds-link" href="%s">Change</a>' % href) if href else '<span></span>')

S_REVIEW = '''<div class="fx-col n">
<a class="fx-back" href="STU-002.dc.html">%s<span>Back</span></a>
<h1 class="fx-h1 ob-in">Your course setup</h1>
<p class="fx-sub ob-in2">Nothing else to decide yet. You can change this any time.</p>
<div class="ds-card rv ob-in3">%s</div>
<div class="fx-acts">%s</div>
</div>''' % (
    ICON(I['back'], 16, 2),
    rv('Format', '<span class="rv-ic">%s</span>Course' % ic('course', 16), 'STU-001.dc.html') +
    rv('Delivery', '<span class="rv-ic">%s</span>Hybrid' % ic('mix', 16), 'STU-002.dc.html') +
    rv('Lead creator', '%s Ada Ononuju' % av(ME, 'AO', 26), None) +
    rv('Status', tag('Draft'), None),
    btn('Continue', 'STU-004.dc.html'))

def how(vis, title, desc, nxt, on):
    inner = '<span class="hw-v" aria-hidden="true">%s</span><span class="hw-t"><b>%s</b><span>%s</span><em>%s</em></span>' % (vis, title, desc, nxt)
    return T.opt(inner, on, 'how', 'hw')

V_SOLO = av(ME, 'AO', 44, 'hw-me')
V_CO = '<span class="hw-co">%s%s<span class="hw-plus">%s</span></span>' % (av(ME, 'AO', 40, 'hw-me'), av(M1, 'JA', 32), ic('plus', 12, 2.6))
V_OPEN = '<span class="hw-open"><span class="hw-ring"></span>%s<i style="left: 4px; top: 22px"></i><i style="right: 2px; top: 10px"></i><i style="right: 8px; bottom: 2px"></i><i style="left: 16px; bottom: 0"></i><i style="left: 30px; top: 0"></i></span>' % av(ME, 'AO', 32, 'hw-me')

S_HOW = '''<div class="fx-col">
<a class="fx-back" href="STU-003.dc.html">%s<span>Back</span></a>
<h1 class="fx-h1 ob-in">How will you create it?</h1>
<p class="fx-sub ob-in2">You can change this later from Collaborators.</p>
<div class="hw-g ob-in3" role="group" aria-label="How you'll create">%s</div>
<div class="fx-acts">%s</div>
</div>''' % (
    ICON(I['back'], 16, 2),
    how(V_SOLO, 'On my own', 'You’re the only creator. Go straight to building.', 'Next: your Studio', False) +
    how(V_CO, 'With co-creators', 'Invite people you know by name or email.', 'Next: invite co-creators', True) +
    how(V_OPEN, 'Open to collaboration', 'Let approved Credalio creators apply to join.', 'Next: describe the opportunity', False),
    btn('Continue', 'STU-008.dc.html'))

PLAN = [('Define', 'What it is and who it’s for'), ('Design', 'Skills, outcomes and evidence'), ('Build', 'Lessons, practice, assessments'),
        ('Review', 'Preview and test it'), ('Validate', 'Independent review')]
S_WELCOME = '''<div class="fx-col n wl">
<div class="wl-nv ob-in">%s</div>
<h1 class="fx-h1 ob-in">Let’s build your course.</h1>
<p class="fx-sub ob-in2">I’m Nova. I’ll help turn what you know into a course people finish. You approve every change.</p>
<div class="wl-tags ob-in2">%s%s<span class="ds-tag line">%s With 2 co-creators</span></div>
<div class="xb-route ob-in3">
<div class="xb-rh"><span class="hp-lab">Your plan</span><span class="xb-rn">Work in any order%s</span></div>
<ol class="xb-steps">%s</ol>
</div>
<div class="xb-acts ob-in4">%s<span class="wl-alt"><a class="ds-link" href="#">%s<span>Import an existing course</span></a><span aria-hidden="true">·</span><a class="ds-link" href="STU-009.dc.html">Go to Studio home</a></span></div>
</div>''' % (
    nova_av('lg'), tag('Course', 'line'), tag('Hybrid', 'line'), stack([(M1, 'JA'), (F1, 'AB')], 18),
    tip('Your Studio is a workspace, not a wizard. Everything saves as you go, and Studio home always shows your next step. Only submitting for validation and publishing have requirements.', 'r'),
    ''.join('<li class="xb-s%s"><span class="xb-sn">%d</span><span class="xb-sl"><b>%s</b><span>%s</span></span></li>' % (' xb-first' if i == 0 else '', i + 1, a, b) for i, (a, b) in enumerate(PLAN)),
    btn('Start building', 'STU-010.dc.html', 'xb-go'), ic('import', 16, 2))

STEPS = [('type', 'Step 1 of 4', 25, S_TYPE), ('delivery', 'Step 2 of 4', 50, S_DELIV), ('review', 'Step 3 of 4', 75, S_REVIEW),
         ('how', 'Step 4 of 4', 100, S_HOW), ('welcome', 'Ready', 100, S_WELCOME)]

SETUP_BODY = '''<div class="fx-root">
<header class="fx-top">
<a href="#" class="fx-x" aria-label="Close setup">%s</a>
<div class="fx-title"><span class="fx-t1">New course</span><span class="fx-t2">Setup</span></div>
<span style="flex-grow: 1"></span>
<span class="fx-step">{{stepLabel}}</span>
<a href="#" class="ds-tok" aria-label="72,450 Creio">%s<span>72.4K</span></a>
<span class="fx-bar" style="width: {{barW}}"></span>
</header>
<main class="fx-main">
%s
</main>
</div>''' % (ic('x', 18, 2.2), COIN('fc', 26), '\n'.join('<sc-if value="{{s_%s}}" hint-placeholder-val="{{ %s }}">%s</sc-if>' % (k, 'true' if k == 'type' else 'false', html) for k, _, _, html in STEPS))

SETUP_CSS = r'''.nw-g{margin-top:32px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}
.nw-f{position:relative;display:flex;flex-direction:column;padding:20px;border-radius:20px;background:#FFFFFF;border:1.5px solid #E6EAF3;color:#0B1433;font-family:inherit;text-align:left;cursor:pointer;transition:border-color .2s ease,box-shadow .2s ease,transform .2s ease}
.nw-f:hover{border-color:#CBD7F5;box-shadow:0 14px 34px rgba(22,82,240,.08);transform:translateY(-2px)}
.nw-fi{width:46px;height:46px;border-radius:14px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.nw-f b{margin-top:14px;font-size:17px;font-weight:600}
.nw-fd{margin-top:6px;font-size:14px;line-height:1.5;color:#4A5578;flex-grow:1}
.nw-fm{margin-top:16px;padding-top:14px;border-top:1.5px solid #F0F2F8;display:flex;flex-direction:column;gap:8px;font-size:13.5px;color:#0B1433}
.nw-fm em{display:block;font-style:normal;font-size:12px;color:#8A93AD}
.nw-ck{display:none;position:absolute;top:16px;right:16px;width:22px;height:22px;border-radius:50%;background:#1652F0;color:#FFFFFF;align-items:center;justify-content:center}
.nw-f.on{border-color:#1652F0;background:#F8FAFF;box-shadow:0 0 0 4px rgba(22,82,240,.12);transform:none}
.nw-f.on .nw-fi{background:#1652F0;color:#FFFFFF}
.nw-f.on .nw-ck{display:flex}
.nw-f:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:2px}
.fx-nova{margin-top:20px;display:flex;align-items:center;gap:12px;height:60px;box-sizing:border-box;padding:6px 8px 6px 12px;border-radius:999px;border:1.5px solid #DCE5FB;background:#FFFFFF}
.fx-nova:focus-within{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.fx-nova input{flex:1;min-width:0;height:100%;border:0;outline:none;background:transparent;font-family:inherit;font-size:15.5px;color:#0B1433}
.fx-nova input::placeholder{color:#8A93AD}
.dv-g{margin-top:32px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.ds-opt.dv{align-items:flex-start;padding:22px 20px;border-radius:18px}
.dv-i{width:46px;height:46px;flex-shrink:0;border-radius:14px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.ds-opt.on .dv-i{background:#FFFFFF}
.dv-t{display:flex;flex-direction:column;gap:6px;min-width:0;flex:1}
.dv-t b{font-size:17px;font-weight:600}
.dv-t > span{font-size:14px;line-height:1.5;color:#4A5578}
.dv-f{margin-top:8px;padding-top:12px;border-top:1.5px solid #EEF1F7;display:flex;flex-direction:column;gap:6px}
.dv-f span{font-size:13.5px;color:#3A4566}
.dv-f span::before{content:'';display:inline-block;width:5px;height:5px;border-radius:50%;background:#9DB8F7;margin:0 9px 2px 0}
.ds-opt.on .dv-f{border-color:#C9D7FA}
.dv .ds-opt-ck{margin-left:0}
.rv{margin-top:28px;padding:6px 28px}
.rv-r{display:grid;grid-template-columns:150px minmax(0,1fr) auto;align-items:center;gap:16px;min-height:64px;border-bottom:1.5px solid #F0F2F8}
.rv-r:last-child{border-bottom:0}
.rv-l{font-size:14px;color:#5B6582}
.rv-v{display:flex;align-items:center;gap:10px;font-size:15.5px;font-weight:600}
.rv-ic{width:32px;height:32px;border-radius:10px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.hw-g{margin-top:32px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.ds-opt.hw{flex-direction:column;align-items:flex-start;gap:18px;padding:24px 22px 22px 22px;border-radius:18px}
.hw .ds-opt-ck{position:absolute;top:18px;right:18px;margin:0}
.hw-v{height:52px;display:flex;align-items:center}
.hw-co{position:relative;display:flex;align-items:center}
.hw-co .av + .av{margin-left:-10px;box-shadow:0 0 0 2.5px #FFFFFF}
.hw-plus{margin-left:-8px;width:24px;height:24px;border-radius:50%;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 2.5px #FFFFFF}
.hw-open{position:relative;width:56px;height:52px;display:flex;align-items:center;justify-content:center}
.hw-ring{position:absolute;inset:2px;border-radius:50%;border:1.5px dashed #9DB8F7}
.hw-open i{position:absolute;width:8px;height:8px;border-radius:50%;background:#AFC1F5}
.hw-t{display:flex;flex-direction:column;gap:6px}
.hw-t b{font-size:17px;font-weight:600}
.hw-t span{font-size:14px;line-height:1.5;color:#4A5578}
.hw-t em{margin-top:8px;font-style:normal;font-size:13px;font-weight:500;color:#1652F0}
.wl{align-items:center;text-align:center}
.wl-nv{margin-bottom:22px}
.wl .fx-sub{margin-left:auto;margin-right:auto;max-width:720px}
.wl-tags{margin-top:18px;display:flex;flex-wrap:wrap;justify-content:center;gap:8px}
.wl-tags .avs .av + .av{margin-left:-6px}
.xb-route{margin-top:28px;width:100%;box-sizing:border-box;padding:22px 26px 22px 26px;border-radius:22px;background:#FFFFFF;border:1.5px solid #E6EAF3;box-shadow:0 18px 44px rgba(22,82,240,.08);text-align:left}
.xb-rh{display:flex;align-items:center;justify-content:space-between;gap:12px}
.hp-lab{font-size:13px;font-weight:600;color:#8A93AD}
.xb-rn{display:inline-flex;align-items:center;font-size:13px;color:#5B6582}
.xb-steps{list-style:none;margin:22px 0 2px 0;padding:0;display:flex;position:relative}
.xb-steps::before{content:'';position:absolute;left:16px;right:16px;top:15px;height:3px;border-radius:3px;background:linear-gradient(90deg,#1652F0,#AFC1F5 30%,#E6EAF3 60%)}
.xb-s{flex:1 1 0;min-width:0;display:flex;flex-direction:column;align-items:center;gap:10px;text-align:center;position:relative}
.xb-s:first-child{align-items:flex-start;text-align:left}
.xb-s:last-child{align-items:flex-end;text-align:right}
.xb-sn{position:relative;z-index:1;width:32px;height:32px;box-sizing:border-box;border-radius:50%;border:2px solid #D6DDEE;background:#FFFFFF;color:#5B6582;font-size:13px;font-weight:600;display:flex;align-items:center;justify-content:center}
.xb-sl{display:flex;flex-direction:column;gap:3px;padding:0 2px}
.xb-sl b{font-size:14px;font-weight:600;color:#0B1433}
.xb-sl span{font-size:12.5px;line-height:1.4;color:#5B6582}
.xb-first .xb-sn{background:#1652F0;border-color:#1652F0;color:#FFFFFF;animation:ndPulse 2s ease-out infinite}
@keyframes ndPulse{0%{box-shadow:0 0 0 0 rgba(22,82,240,.35)}100%{box-shadow:0 0 0 10px rgba(22,82,240,0)}}
.xb-acts{margin-top:30px;display:flex;flex-direction:column;align-items:center;gap:16px}
.wl-alt{display:flex;align-items:center;gap:14px;color:#8A93AD;font-size:14px}
.wl-alt .ds-link{font-size:14px}
@media (prefers-reduced-motion: reduce){.xb-first .xb-sn{animation:none}}
@media (max-width: 1180px){.nw-g{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width: 960px){
.fx-step{display:none}
.nw-g{margin-top:20px;grid-template-columns:minmax(0,1fr);gap:10px}
.nw-f{display:grid;grid-template-columns:40px minmax(0,1fr);column-gap:14px;align-items:center;padding:14px 46px 14px 16px;border-radius:16px}
.nw-fi{width:40px;height:40px;border-radius:12px;grid-row:span 2}
.nw-f b{margin-top:0;font-size:15.5px}
.nw-fd{margin-top:2px;font-size:13.5px}
.nw-fm{display:none}
.nw-ck{top:50%;transform:translateY(-50%);right:14px}
.fx-nova{height:auto;flex-wrap:wrap;border-radius:18px;padding:12px;gap:10px}
.fx-nova input{flex-basis:calc(100% - 44px);height:36px;font-size:14.5px}
.fx-nova .nv-chip{margin-left:42px}
.dv-g,.hw-g{margin-top:20px;grid-template-columns:minmax(0,1fr);gap:10px}
.ds-opt.dv{padding:16px}
.dv-f{display:none}
.dv .ds-opt-ck{margin-left:auto}
.dv-i{width:40px;height:40px;border-radius:12px}
.dv-t b,.hw-t b{font-size:15.5px}
.ds-opt.hw{flex-direction:row;align-items:center;gap:14px;padding:16px 48px 16px 16px}
.hw .ds-opt-ck{top:50%;transform:translateY(-50%);right:16px}
.hw-v{height:44px;width:60px;flex-shrink:0;justify-content:center}
.hw-t span{font-size:13.5px}
.hw-t em{margin-top:2px;font-size:12.5px}
.rv{margin-top:20px;padding:4px 16px}
.rv-r{grid-template-columns:minmax(0,1fr) auto;row-gap:2px;padding:12px 0}
.rv-l{grid-column:1 / -1;font-size:13px}
.wl{align-items:stretch;text-align:left}
.wl-nv{margin-bottom:16px}
.wl-tags{justify-content:flex-start}
.xb-route{margin-top:20px;padding:18px 16px;border-radius:18px}
.xb-steps{flex-direction:column;margin-top:16px;gap:0}
.xb-steps::before{left:13px;right:auto;top:14px;bottom:14px;width:3px;height:auto;background:linear-gradient(180deg,#1652F0,#AFC1F5 30%,#E6EAF3 60%)}
.xb-s,.xb-s:first-child,.xb-s:last-child{flex-direction:row;align-items:center;text-align:left;gap:14px;min-height:52px}
.xb-sn{width:28px;height:28px;font-size:12px}
.xb-acts{align-items:stretch;margin-top:20px}
.xb-go{justify-content:space-between}
.wl-alt{flex-direction:column;gap:6px}
.wl-alt > span[aria-hidden]{display:none}
}
'''

SETUP_JS = T.js() + '''class Component extends DCLogic {
  renderVals() {
    var st = this.props.step || 'type';
    var S = %s;
    var cur = S[st] || S.type;
    var v = togVals(this);
    v.stepLabel = cur[0]; v.barW = String(cur[1]).concat('%%');
    Object.keys(S).forEach(function (k) { v['s_'.concat(k)] = k === st; });
    return v;
  }
}''' % json.dumps({k: [l, w] for k, l, w, _ in STEPS})

write('Setup.dc.html', doc('Course setup · shared source', kit.KIT_CSS + '\n' + dash.DASH_CSS + BASE_CSS + FOCUS_CSS + SETUP_CSS, SETUP_BODY, SETUP_JS))

# ======================================================================= STUDIO (course workspace)
W = Toggles()
PAGES = []  # (key, nav, html)

def P(key, nav, html):
    PAGES.append((key, nav, html))

CS_TABS = [('Career', 'STU-012.dc.html'), ('Skills', 'STU-013.dc.html')]
LO_TABS = [('Outcomes', 'STU-014.dc.html'), ('Skills map', 'STU-015.dc.html'), ('Evidence', 'STU-016.dc.html')]
LD_TABS = [('Assessment & award', 'STU-017.dc.html'), ('Effort', 'STU-018.dc.html'), ('Summary', 'STU-019.dc.html')]

# ---------- CR-STU-009 Studio home
def row(icon, title, meta, st_label, st_kind, href, extra=''):
    return ('<a class="hm-r" href="%s"><span class="hm-ri">%s</span><span class="hm-rt"><b>%s</b><span>%s</span></span>%s%s<span class="hm-go">%s</span></a>' %
            (href, ic(icon, 18), title, meta, extra, tag(st_label, st_kind), ic('chev', 16, 2)))

DET = [('5', 'chapters'), ('9', 'lessons'), ('5', 'videos'), ('8h 5m', 'learning time'), ('3', 'assessments'), ('35', 'questions'), ('1', 'project'), ('4', 'outcomes')]
P('home', 'home', page_head('Studio home', COURSE, 'Pick up where you left off. Everything saves as you go.',
    '<div class="hm-strip"><span><em>Course health%s</em><b>31%%</b></span><span><em>Course profile%s</em><b>9 of 13</b></span></div>' % (
        tip('How complete and ready the course is. Not a quality score.', 'dn'),
        tip('What Credalio understands about this course, built quietly from your work. It helps learners find it and validators review it.', 'dn r'))) +
'''<section class="ds-card hm-next ob-in2" aria-label="Recommended next step">
<div class="hm-nl"><span class="pg-e">Next step</span><h2>Define who this course is for and where it leads</h2><p>Set the career role and stage so learners heading there can find it.</p>
<div class="hm-na">%s<a class="ds-link" href="#">%s<span>Ask Nova what’s left</span></a></div></div>
<div class="hm-ring" aria-hidden="true"><svg viewBox="0 0 120 120" width="132" height="132"><circle cx="60" cy="60" r="50" fill="none" stroke="#EAF0FF" stroke-width="10"></circle><circle cx="60" cy="60" r="50" fill="none" stroke="#1652F0" stroke-width="10" stroke-linecap="round" stroke-dasharray="97 314" transform="rotate(-90 60 60)"></circle></svg><span><b>31%%</b><em>health</em></span></div>
</section>
<section class="ds-card hm-list ob-in3" aria-label="Your course">
<h2 class="hm-h">Your course</h2>
%s%s%s%s%s
</section>
<section class="ds-card hm-det ob-in4" aria-label="Detected from your build">
<div class="hm-dh"><h2 class="hm-h">Detected from your build%s</h2></div>
<div class="hm-dg">%s</div>
</section>''' % (
    btn('Continue building', 'STU-012.dc.html'), SPARK,
    row('layers', 'Course design', '4 of 9 sections done', 'In progress', 'blue', 'STU-010.dc.html'),
    row('course', 'Curriculum', '5 chapters · 9 lessons · 8h 5m', 'Done', 'green', '#'),
    row('quiz', 'Assessments', '3 assessments · 35 questions · 3 of 4 outcomes assessed', 'In progress', 'blue', '#'),
    row('users', 'Collaborators', 'Dr John Adeyemi, ABC Institute', 'Done', 'green', '#', stack(TEAM, 26)),
    row('lock', 'Validation readiness', 'Opens once Design and Build are done', 'Locked', '', '#'),
    tip('Counted from your curriculum as you work. Nothing to fill in.', 'dn'),
    ''.join('<span><b>%s</b><em>%s</em></span>' % d for d in DET)))

# ---------- CR-STU-010 Basics
P('basics', 'basics', page_head('Design', 'Basics', 'Start with the course itself.') +
'''<section class="ds-card fc ob-in2">
<div class="fg">
%s
<div class="fg fg2">%s%s</div>
%s
<div class="fg fg2">%s%s</div>
<div class="fg fg2">%s%s</div>%s
%s
</div>
</section>
<section class="ds-card fc ob-in3">
<div class="fc-h"><div><h2>A few quick questions%s</h2></div></div>
<div class="fg">
%s%s%s
</div>
</section>''' % (
    field('Course title', '<div class="in-ai"><input class="ds-in lg" value="Data Analysis with SQL" aria-label="Course title">%s</div>' % nchip('Improve')),
    field('Short description', '<input class="ds-in" value="Write SQL to answer real business questions, from first query to finished analysis." aria-label="Short description"><span class="cnt">85 / 140</span>', 'Shown on the course card.'),
    field('Course cover', '<div class="cov"><span class="cov-i" aria-hidden="true">SQL</span><span class="cov-t"><b>sql-course-cover.png</b><span>1600 × 900</span></span><a class="ds-link" href="#">Replace</a></div>'),
    field('Full description', '<textarea class="ds-in" aria-label="Full description">A hybrid course for career changers and analysts. Learn SQL step by step, practise on realistic business data, join a live analysis clinic and finish with a portfolio project.</textarea><span class="in-help">%s</span>' % nchip('Help me write this')),
    field('Primary category', sel('Technology', 'Primary category')), field('Topic', sel('Data Analytics', 'Topic')),
    field('Subtopic', sel('SQL', 'Subtopic')), field('Language', sel('English', 'Language')),
    '',
    field('Skills', '<div class="chips">%s%s%s%s<button type="button" class="ds-chip add">%s<span>Add skill</span></button></div><span class="in-help">%s</span>' % (
        W.chip('SQL', True), W.chip('Data cleaning', True), W.chip('Data analysis', True), W.chip('Relational databases', True), ic('plus', 14, 2.2), nchip('Suggest from description'))),
    tip('Saved to your course profile, so you won’t be asked again at validation.'),
    field('Do learners need outside software?', '<div class="chips">%s</div><div class="chips sub">%s%s%s%s</div>' % (
        W.seg(['Yes', 'No'], 0), W.chip('SQL Server', False, cls='sm'), W.chip('MySQL', False, cls='sm'), W.chip('PostgreSQL', True, cls='sm'), W.chip('Other', False, cls='sm'))),
    field('Will learners work with real or simulated data?', '<div class="chips">%s</div>' % W.seg(['Real', 'Simulated', 'Both', 'Neither'], 1)),
    field('Does this course involve AI?', '<div class="chips">%s%s%s%s</div>' % (
        W.chip('No', True, 'ai'), W.chip('Learners use AI tools', False, 'ai'), W.chip('AI is the subject', False, 'ai'), W.chip('AI outputs are assessed', False, 'ai')))) +
acts('STU-011.dc.html'))

# ---------- CR-STU-011 Audience & prerequisites
def prq(skill, lvl, req):
    return ('<div class="pq-r"><span class="pq-s">%s</span>%s<div>%s</div><button type="button" class="ds-x sm" aria-label="Remove %s">%s</button></div>' %
            (skill, sel(lvl, 'Minimum level for ' + skill), W.seg(['Required', 'Recommended'], 0 if req else 1), skill, ic('x', 15, 2)))
P('audience', 'audience', page_head('Design', 'Audience', 'Who is this for, and what should they already know?') +
'''<section class="ds-card fc ob-in2">
<div class="fg">
%s
%s
</div>
</section>
<section class="ds-card fc ob-in3">
<div class="fc-h"><div><h2>Before they start%s</h2><p>Each prerequisite gets a minimum level and whether it’s required.</p></div>%s</div>
<div class="pq">
<div class="pq-r pq-hd"><span>Skill</span><span>Minimum level</span><span>Requirement</span><span></span></div>
%s%s
</div>
<div class="pq-add"><input class="ds-in" placeholder="Add a prerequisite, like Spreadsheets" aria-label="Add a prerequisite"><button type="button" class="ds-ghost">Add</button></div>
</section>''' % (
    field('Level', '<div class="chips">%s%s%s%s</div>' % (W.chip('Beginner', True), W.chip('Intermediate'), W.chip('Advanced'), W.chip('Professional')), 'Select all that apply.'),
    field('Why they’re learning', '<div class="chips">%s%s%s%s%s</div>' % (W.chip('Career development', True), W.chip('Professional development', True), W.chip('Workplace training'), W.chip('Academic learning'), W.chip('Personal learning'))),
    tip('Matched against learners, so the right people find the course.'),
    nchip('Suggest prerequisites'),
    prq('Excel', 'Foundation', True), prq('Statistics', 'Foundation', False)) +
'''<section class="ds-card fc ob-in4">
<div class="fc-h"><div><h2>Age%s</h2></div></div>
<div class="opt3">%s%s%s</div>
</section>''' % (tip('Helps match the right validators and checks.'),
    W.opt('<span class="o-t"><b>General audience</b><span>Anyone can take it</span></span>', True, 'age'),
    W.opt('<span class="o-t"><b>Adults only</b><span>18 and over</span></span>', False, 'age'),
    W.opt('<span class="o-t"><b>Restricted audience</b><span>Special or protected groups</span></span>', False, 'age')) +
acts('STU-012.dc.html', back_href='STU-010.dc.html'))

# ---------- CR-STU-012 / 012b Career
def career(cert):
    goals = ['Build a skill', 'Prepare for a career role', 'Change career', 'Advance in their career', 'Prepare for a certification', 'Academic progression']
    on = {0, 1, 2} | ({4} if cert else set())
    certs = ''
    if cert:
        certs = '''<section class="ds-card fc ob-in4">
<div class="fc-h"><div><h2>Prepares for a certification%s</h2><p>Shown as “Prepares for” on your course page. The certification’s owner approves the link.</p></div></div>
<div class="ce">
<div class="ce-r"><span class="ce-i">%s</span><span class="ce-t"><b>Professional Data Analyst Certification</b><span>ABC Institute · designed by you</span></span>%s<button type="button" class="ds-ghost sm">Link</button></div>
<div class="ce-r"><span class="ce-i">%s</span><span class="ce-t"><b>Certified BI Practitioner</b><span>Data Professionals Association</span></span>%s<span class="ce-s">%s<span>Waiting for the owner</span><button type="button" class="ds-link">Remove</button></span></div>
<div class="ce-r"><span class="ce-i">%s</span><span class="ce-t"><b>Associate Data Engineer</b><span>Acme Analytics Ltd</span></span>%s<button type="button" class="ds-ghost sm">Request link</button></div>
</div>
</section>''' % (tip('Completing this course never awards the certification. Learners still register for it and pass its assessments.'),
                 ic('badge', 18), tag('In validation', 'blue'), ic('badge', 18), tag('Validated', 'green'), ICON(EXTRA['clock'], 14, 2), ic('badge', 18), tag('Validated', 'green'))
    rel = (W.opt('<span class="o-t"><b>Core skill</b><span>Essential to the role day to day</span></span>', True, 'rel%d' % cert) +
           W.opt('<span class="o-t"><b>Supporting skill</b><span>Helps, but isn’t central</span></span>', False, 'rel%d' % cert) +
           W.opt('<span class="o-t"><b>Specialised skill</b><span>A niche or advanced capability</span></span>', False, 'rel%d' % cert))
    return (page_head('Design', 'Career & skills', 'Where can this course take someone?', '', subtabs(CS_TABS, 0)) +
'''<div class="ob-in2" style="margin-top: 20px">%s</div>
<section class="ds-card fc ob-in3">
<div class="fg">
%s
<div class="fg fg2">%s%s</div>
%s
%s
</div>
</section>%s''' % (
        nova_sg('From your outcomes and skills, this fits an entry-level <b>Data Analyst</b> path, with BI Analyst and Operations Analyst as related roles.',
                '<button type="button" class="ds-ghost sm">Use suggestion</button>'),
        field('This course mainly helps learners', '<div class="chips">%s</div>' % ''.join(W.chip(g, i in on) for i, g in enumerate(goals)), 'Select all that apply.'),
        field('Main role', '<input class="ds-in" placeholder="Search roles, like Data Analyst" aria-label="Main role">'),
        field('Related roles', '<div class="rr"><input class="ds-in" placeholder="Add a related role" aria-label="Add a related role"><button type="button" class="ds-ghost">Add</button></div>'),
        field('Career stage', W.seg(['Entry level', 'Early career', 'Mid career', 'Advanced'], 0), 'Where in a career this course is most useful.'),
        field('How it relates to the role%s' % tip('Learners heading for these roles find this course on their path. It never affects validation on its own.'), '<div class="opt3">%s</div>' % rel),
        certs) + acts('STU-013.dc.html', back_href='STU-011.dc.html'))
P('career', 'career', career(False))
P('careercert', 'career', career(True))

# ---------- CR-STU-013 Skills & proficiency
LV = ['Beginner', 'Foundation', 'Intermediate', 'Advanced', 'Expert']
def track(a, b):
    if a is None or b is None:
        return '<span class="tk tk-x">%s<span>Set both levels</span></span>' % ic('warn', 14, 2)
    dots = ''.join('<i class="%s"></i>' % ('on' if a <= i <= b else '') for i in range(5))
    return '<span class="tk" style="--a: %d; --b: %d" aria-label="%s to %s"><span class="tk-l"></span>%s</span>' % (a, b, LV[a], LV[b], dots)
def skr(skill, a, b):
    return ('<div class="sk-r"><span class="sk-s">%s</span>%s%s%s<button type="button" class="ds-x sm" aria-label="Remove %s">%s</button></div>' %
            (skill, sel(LV[a] if a is not None else 'Choose a level', 'Starting level for ' + skill), sel(LV[b] if b is not None else 'Choose a level', 'Expected level for ' + skill), track(a, b), skill, ic('x', 15, 2)))
P('skills', 'career', page_head('Design', 'Career & skills', 'What will learners develop, and how far will they get?', '', subtabs(CS_TABS, 1)) +
'''<div class="ob-in2" style="margin-top: 20px">%s</div>
<section class="ds-card fc ob-in3">
<div class="fc-h"><div><h2>Skills and levels%s</h2><p>Starting levels should match your prerequisites.</p></div>%s</div>
<div class="sk">
<div class="sk-r sk-hd"><span>Skill</span><span>Starting level</span><span>Expected level</span><span>Progression</span><span></span></div>
%s%s%s%s
</div>
<div class="pq-add"><input class="ds-in" placeholder="Add a skill" aria-label="Add a skill"><button type="button" class="ds-ghost">Add</button></div>
</section>''' % (
    nova_sg('I found 6 skills in your curriculum. 4 are listed. Add the other two?',
            '<button type="button" class="ds-chip sm">%s<span>Joins</span></button><button type="button" class="ds-chip sm">%s<span>Aggregation</span></button><button type="button" class="ds-link">Dismiss</button>' % (ic('plus', 13, 2.4), ic('plus', 13, 2.4))),
    tip('Levels, lowest to highest: Beginner, Foundation, Intermediate, Advanced, Expert. Credalio checks them against your assessments during validation.'),
    nchip('Suggest levels'),
    skr('SQL', 0, 2), skr('Data analysis', 1, 2), skr('Data cleaning', 0, 2), skr('Relational databases', None, None)) +
acts('STU-014.dc.html', back_href='STU-012.dc.html'))

# ---------- CR-STU-014 Outcomes
def lo(n, text, warn=False):
    w = ''
    if warn:
        w = '<div class="lo-w">%s<p><b>Hard to assess.</b> Try: “Write SQL queries to retrieve, filter and aggregate structured data.”</p><button type="button" class="ds-ghost sm">Use suggestion</button></div>' % nova_av('sm')
    return ('<div class="lo-r%s"><span class="lo-n">%d</span><div class="lo-b"><input class="ds-in" value="%s" aria-label="Outcome %d">%s</div><button type="button" class="ds-x sm" aria-label="Remove outcome %d">%s</button></div>' %
            (' warn' if warn else '', n, text, n, w, n, ic('x', 15, 2)))
P('outcomes', 'outcomes', page_head('Design', 'Outcomes', 'What will learners be able to do by the end?', '', subtabs(LO_TABS, 0)) +
'''<section class="ds-card fc ob-in2">
<div class="fc-h"><div><h2>Learning outcomes%s</h2><p>Start with a verb learners can show: write, build, analyse.</p></div>%s</div>
<div class="lo">%s%s%s%s</div>
<button type="button" class="ds-ghost lo-add">%s<span>Add an outcome</span></button>
</section>''' % (
    tip('You’ll connect each outcome to skills and evidence next.'), nchip('Generate from course goal'),
    lo(1, 'Write SQL queries to retrieve and filter structured business data.'), lo(2, 'Combine multiple relational tables using joins.'),
    lo(3, 'Analyse business datasets and communicate findings.'), lo(4, 'Understand SQL', True), ic('plus', 16, 2.2)) +
acts('STU-015.dc.html', back_href='STU-013.dc.html'))

# ---------- CR-STU-015 Outcome → skill map
SK = ['SQL', 'Data analysis', 'Data cleaning', 'Relational databases']
LOS = [('LO1', 'Write SQL queries to retrieve and filter business data', [1, 1, 0, 0]),
       ('LO2', 'Combine multiple relational tables using joins', [1, 0, 0, 1]),
       ('LO3', 'Analyse business datasets and communicate findings', [0, 1, 1, 0]),
       ('LO4', 'Understand SQL', [0, 0, 0, 0])]
def mx_cell(on, lo_, sk):
    k = W.new(bool(on))
    return '<button type="button" class="mx-c {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}" aria-label="%s develops %s"><span class="mx-ck">%s</span><span class="mx-l">%s</span></button>' % (k, k, k, lo_, sk, ck(13), sk)
def mx_rows():
    h = ''
    for code, text, cells in LOS:
        warn = not any(cells)
        h += '<div class="mx-r%s"><span class="mx-o"><em>%s</em><span>%s</span>%s</span>%s</div>' % (
            ' warn' if warn else '', code, text, tag('No skills yet', 'amber') if warn else '', ''.join(mx_cell(c, code, SK[i]) for i, c in enumerate(cells)))
    cov = [('Intermediate', 'LO1, LO2', ''), ('Intermediate', 'LO1, LO3', ''), ('Intermediate', 'LO3', ''), ('Target not set', 'LO2', 'amber')]
    h += '<div class="mx-r mx-cov"><span class="mx-o"><em>Coverage</em><span>Target level and outcomes</span></span>%s</div>' % ''.join(
        '<span class="mx-k"><em class="mx-l">%s</em><b class="%s">%s</b><span>%s</span></span>' % (SK[i], k, t, d) for i, (t, d, k) in enumerate(cov))
    return h
P('skillmap', 'outcomes', page_head('Design', 'Outcomes', 'Which skills does each outcome develop?', '', subtabs(LO_TABS, 1)) +
'''<section class="ds-card fc ob-in2">
<div class="fc-h"><div><h2>Skills map%s</h2><p>Every outcome should develop at least one skill.</p></div>%s</div>
<div class="mx-w"><div class="mx" style="--n: 4">
<div class="mx-r mx-hd"><span></span>%s</div>
%s
</div></div>
</section>''' % (tip('This links your outcomes to the course profile Credalio builds as you work.'), nchip('Map skills for me'),
               ''.join('<span>%s</span>' % s for s in SK), mx_rows()) +
acts('STU-016.dc.html', back_href='STU-014.dc.html'))

# ---------- CR-STU-016 Evidence
EV = ['Practical exercise', 'Project', 'Quiz', 'Exam', 'Live demonstration', 'Portfolio piece']
def ev_r(code, text, skills, on):
    sk = ''.join(tag(s, 'line') for s in skills) if skills else tag('No skills mapped', 'amber')
    return ('<div class="ev-r"><div class="ev-o"><em>%s</em><b>%s</b><span class="ev-sk">%s</span></div><div class="chips">%s</div></div>' %
            (code, text, sk, ''.join(W.chip(e, i in on, cls='sm') for i, e in enumerate(EV))))
CHAIN = [('LO1', [1, 1, 1, 1]), ('LO2', [1, 1, 1, 0]), ('LO3', [1, 1, 0, 1]), ('LO4', [1, 0, 0, 0])]
def chain():
    cols = ['Taught', 'Practised', 'Assessed', 'Proof']
    h = '<div class="ch-r ch-hd"><span>Outcome</span>%s</div>' % ''.join('<span>%s</span>' % c for c in cols)
    for code, cells in CHAIN:
        h += '<div class="ch-r"><span class="ch-o">%s</span>%s</div>' % (code, ''.join(
            '<span class="ch-c %s">%s</span>' % ('ok' if c else 'no', ck(12) if c else '<i></i>') for c in cells))
    return h
P('evidence', 'outcomes', page_head('Design', 'Outcomes', 'How will learners prove each outcome?', '', subtabs(LO_TABS, 2)) +
'''<section class="ds-card fc ob-in2">
<div class="fc-h"><div><h2>Evidence%s</h2><p>Pick how each outcome is proved.</p></div>%s</div>
<div class="ev">%s%s%s%s</div>
</section>
<section class="ds-card fc ob-in3">
<div class="fc-h"><div><h2>Learning chain%s</h2><p>From outcome to proof. Gaps fill in as you build.</p></div></div>
<div class="ch">%s</div>
</section>''' % (
    tip('This completes the chain: outcome, skill, evidence.'), nchip('Suggest evidence'),
    ev_r('LO1', 'Write SQL queries to retrieve and filter business data', ['SQL · Intermediate', 'Data analysis · Intermediate'], {0, 2}),
    ev_r('LO2', 'Combine multiple relational tables using joins', ['SQL · Intermediate', 'Relational databases'], {0, 3}),
    ev_r('LO3', 'Analyse business datasets and communicate findings', ['Data analysis · Intermediate', 'Data cleaning · Intermediate'], {1, 5}),
    ev_r('LO4', 'Understand SQL', [], set()),
    tip('Taught in lessons, practised in activities, assessed in quizzes or exams, and proved by evidence learners keep.'), chain()) +
acts('STU-017.dc.html', back_href='STU-015.dc.html'))

# ---------- CR-STU-017 Course design (assessment & award)
P('design', 'design', page_head('Design', 'Learning design', 'How will the course assess and award?', '', subtabs(LD_TABS, 0)) +
'''<section class="ds-card fc ob-in2">
<div class="fc-h"><div><h2>Assessment%s</h2><p>Will this course include:</p></div></div>
<div class="as-g">%s</div>
</section>
<section class="ds-card fc ob-in3">
<div class="fc-h"><div><h2>What completion awards%s</h2></div></div>
<div class="opt2">%s%s</div>
</section>''' % (
    tip('Credalio later checks what you declare against the actual content. Difficulty is set per lesson, in each lesson editor.'),
    ''.join(W.opt('<span class="as-i">%s</span><span class="o-t"><b>%s</b><span>%s</span></span>' % (ic(i, 18), t, d), on, cls='as')
            for i, t, d, on in [('check', 'Knowledge checks', 'Quick checks inside lessons', True), ('quiz', 'Quizzes', 'Short scored sets', True),
                                ('file', 'Exam', 'A final, timed assessment', False), ('edit', 'Assignments', 'Written or practical work', True),
                                ('project', 'Projects', 'Larger pieces learners keep', True), ('target', 'Practical activities', 'Hands-on tasks with data', True)]),
    tip('A skill badge depends on the validation outcome and Credalio’s badge policy.'),
    W.opt('<span class="as-i">%s</span><span class="o-t"><b>Course completion certificate</b><span>Issued when learners finish</span></span>' % ic('cert2', 18), True, cls='as'),
    W.opt('<span class="as-i">%s</span><span class="o-t"><b>Skill badge</b><span>Subject to policy</span></span>' % ic('badge', 18), False, cls='as')) +
acts('STU-018.dc.html', back_href='STU-016.dc.html'))

# ---------- CR-STU-018 Learning effort
EF = [('Structured learning', 'Videos, reading, interactive lessons', '10', '2h 15m'), ('Practice', 'Exercises, assignments, discussions', '6', '1h 40m'),
      ('Projects', 'Projects and portfolio work', '5', '2h'), ('Assessments', 'Knowledge checks, quizzes, exams', '3', '1h 10m'), ('Live instruction', 'Live sessions and clinics', '2', '1h')]
P('effort', 'design', page_head('Design', 'Learning design', 'How much time will learners put in?', '', subtabs(LD_TABS, 1)) +
'''<section class="ds-card fc ob-in2">
<div class="fc-h"><div><h2>Effort%s</h2><p>Estimate now. Detected figures replace your estimates as you build.</p></div></div>
<div class="ef">
<div class="ef-r ef-hd"><span>Type of effort</span><span>Your estimate</span><span>Built so far</span></div>
%s
<div class="ef-r ef-tot"><span><b>Total</b></span><span><b>26 hours</b></span><span><b>8h 5m</b></span></div>
</div>
</section>
<section class="ds-card fc ef-sum ob-in3">
<div class="ef-l"><span class="pg-e">Learners will see</span><b>24–30 hours</b><p>Shown on the course page, and updated as you build.</p></div>
<div class="ef-p"><div class="ef-pb"><i style="width: 31%%"></i></div><span><b>8h 5m</b> built of 26 hours estimated</span></div>
</section>''' % (
    tip('Credalio calculates each figure from your actual content as the curriculum fills in.'),
    ''.join('<div class="ef-r"><span class="ef-t"><b>%s</b><span>%s</span></span><span class="ef-in"><input class="ds-in" value="%s" aria-label="Estimated hours for %s"><em>hours</em></span><span class="ef-d">%s</span></div>' % (t, d, v, t, b) for t, d, v, b in EF)) +
acts('STU-019.dc.html', back_href='STU-017.dc.html'))

# ---------- CR-STU-019 Design summary
SUM = [('Target', 'No career role yet', 'pr', 'STU-012.dc.html'), ('Audience', 'Beginner · Excel (Foundation), Statistics (Foundation)', 'ok', 'STU-011.dc.html'),
       ('Skills', 'SQL, Data analysis, Data cleaning, Relational databases', 'pr', 'STU-013.dc.html'), ('Outcomes', '4 learning outcomes', 'pr', 'STU-014.dc.html'),
       ('Evidence', 'Quiz, practical exercise, project, portfolio piece', 'pr', 'STU-016.dc.html'), ('Intended level', 'Intermediate', 'ok', 'STU-013.dc.html'),
       ('Estimated effort', '24–30 hours', 'ok', 'STU-018.dc.html')]
SIG = [('Industry', 1), ('Domain', 1), ('Topic', 1), ('Career role', 0), ('Skills', 1), ('Prerequisites', 1), ('Levels', 0),
       ('Outcomes', 1), ('Evidence', 0), ('Effort', 1), ('Delivery', 1), ('Credential', 1), ('Progression', 0)]
P('summary', 'design', page_head('Design', 'Learning design', 'Check the design before you build. Everything stays editable.', '', subtabs(LD_TABS, 2)) +
'''<div class="ob-in2" style="margin-top: 20px">%s</div>
<section class="ds-card fc ob-in3">
<div class="fc-h"><div><h2>Your design</h2></div><span class="sm-c">%s 3 ready · %s 4 need attention</span></div>
<div class="sm">%s</div>
</section>
<section class="ds-card fc ob-in4">
<div class="fc-h"><div><h2>Course profile%s</h2><p>9 of 13 signals captured.</p></div></div>
<div class="sg">%s</div>
</section>''' % (
    nova_sg('Almost there. 4 items need a look: target, skills, outcomes and evidence. You can still start building.'),
    STATUS['ok'], STATUS['pr'],
    ''.join('<a class="sm-r" href="%s">%s<span class="sm-l">%s</span><span class="sm-v">%s</span><span class="sm-e">Edit</span></a>' % (h, STATUS[s], l, v) for l, v, s, h in SUM),
    tip('You’ll confirm the full profile in Prepare, before validation.'),
    ''.join('<span class="sg-i%s">%s%s</span>' % ('' if on else ' off', ck(11) if on else '<i></i>', n) for n, on in SIG)) +
acts('#', 'Build curriculum', back_href='STU-018.dc.html'))

STUDIO_CSS = r'''.hm-strip{display:flex;border-radius:16px;background:#FFFFFF;border:1.5px solid #E6EAF3}
.hm-strip > span{display:flex;flex-direction:column;gap:4px;padding:10px 18px}
.hm-strip > span + span{border-left:1.5px solid #EEF1F7}
.hm-strip em{display:flex;align-items:center;font-style:normal;font-size:12px;color:#5B6582}
.hm-strip b{font-size:17px;font-weight:600}
.hm-next{margin-top:24px;padding:30px 34px;display:flex;align-items:center;justify-content:space-between;gap:32px;position:relative;overflow:hidden}
.hm-next::before{content:'';position:absolute;inset:0;background:linear-gradient(120deg,#F2F6FF,rgba(242,246,255,0) 60%);pointer-events:none}
.hm-nl{position:relative;min-width:0}
.hm-next h2{margin:0;max-width:580px;font-size:26px;line-height:1.2;font-weight:600;letter-spacing:-0.02em}
.hm-next p{margin:10px 0 0 0;font-size:15px;line-height:1.55;color:#4A5578}
.hm-na{margin-top:22px;display:flex;align-items:center;gap:22px}
.hm-na .ds-link svg{color:#1652F0}
.hm-ring{position:relative;flex-shrink:0;width:132px;height:132px}
.hm-ring span{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}
.hm-ring b{font-size:26px;font-weight:600;letter-spacing:-0.02em}
.hm-ring em{font-style:normal;font-size:12px;color:#5B6582}
.hm-list,.hm-det{margin-top:16px;padding:8px 10px 10px 10px}
.hm-h{display:flex;align-items:center;margin:14px 14px 6px 14px;font-size:16px;font-weight:600}
.hm-r{display:flex;align-items:center;gap:14px;min-height:68px;padding:10px 14px;border-radius:14px;color:#0B1433;text-decoration:none}
.hm-r + .hm-r{box-shadow:0 -1.5px 0 #F0F2F8}
.hm-r:hover{background:#F7F9FD}
.hm-ri{width:40px;height:40px;flex-shrink:0;border-radius:12px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.hm-rt{flex:1;min-width:0;display:flex;flex-direction:column;gap:3px}
.hm-rt b{font-size:15px;font-weight:600}
.hm-rt span{font-size:13.5px;color:#5B6582}
.hm-go{color:#8A93AD;display:flex}
.hm-dh{display:flex;align-items:center;justify-content:space-between}
.hm-dg{display:grid;grid-template-columns:repeat(8,minmax(0,1fr));gap:8px;padding:4px 4px 4px 4px}
.hm-dg span{display:flex;flex-direction:column;gap:2px;padding:12px 12px;border-radius:12px;background:#F7F9FD}
.hm-dg b{font-size:18px;font-weight:600}
.hm-dg em{font-style:normal;font-size:12.5px;color:#5B6582}
.in-ai{position:relative}
.in-ai .ds-in{padding-right:130px}
.in-ai .nv-chip{position:absolute;right:10px;top:50%;transform:translateY(-50%)}
.cnt{align-self:flex-end;margin-top:-2px;font-size:12px;color:#8A93AD}
.in-help{display:flex}
.cov{display:flex;align-items:center;gap:14px;height:56px;padding:0 16px 0 6px;border-radius:12px;border:1.5px solid #D6DDEE}
.cov-i{width:58px;height:42px;border-radius:9px;background:linear-gradient(140deg,#1652F0,#0B1433);color:#FFFFFF;font-size:11px;font-weight:600;display:flex;align-items:center;justify-content:center}
.cov-t{flex:1;min-width:0;display:flex;flex-direction:column}
.cov-t b{font-size:14px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cov-t span{font-size:12.5px;color:#5B6582}
.ds-chip.add{border-style:dashed;color:#3A4566}
.chips.sub{margin-top:4px}
.ds-x.sm{width:36px;height:36px;border-color:transparent;color:#5B6582}
.ds-x.sm:hover{border-color:#D6DDEE;color:#0B1433}
.ds-ghost.sm{height:40px;padding:0 16px;font-size:14px}
.pq-r{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr) minmax(0,1.3fr) 36px;align-items:center;gap:14px;padding:10px 0;border-bottom:1.5px solid #F0F2F8}
.pq-hd{padding:0 0 8px 0;font-size:12.5px;font-weight:500;color:#8A93AD}
.pq-s{font-size:15px;font-weight:600}
.pq-add{margin-top:16px;display:flex;gap:10px;max-width:520px}
.pq-add .ds-ghost{height:48px}
.opt2,.opt3{display:grid;gap:12px}
.opt2{grid-template-columns:repeat(2,minmax(0,1fr))}
.opt3{grid-template-columns:repeat(3,minmax(0,1fr))}
.o-t{display:flex;flex-direction:column;gap:3px;min-width:0}
.o-t b{font-size:15px;font-weight:600}
.o-t span{font-size:13.5px;line-height:1.45;color:#5B6582}
.rr{display:flex;gap:10px}
.rr .ds-ghost{height:48px}
.ce{display:flex;flex-direction:column}
.ce-r{display:flex;align-items:center;gap:14px;min-height:72px;border-bottom:1.5px solid #F0F2F8}
.ce-r:last-child{border-bottom:0}
.ce-i{width:40px;height:40px;flex-shrink:0;border-radius:12px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.ce-t{flex:1;min-width:0;display:flex;flex-direction:column;gap:3px}
.ce-t b{font-size:15px;font-weight:600}
.ce-t span{font-size:13.5px;color:#5B6582}
.ce-s{display:inline-flex;align-items:center;gap:8px;font-size:13.5px;color:#8A5A00}
.ce-s .ds-link{font-size:13.5px;border:0;background:none;font-family:inherit;cursor:pointer;margin-left:8px}
.sk-r{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr) minmax(0,1fr) minmax(0,1.2fr) 36px;align-items:center;gap:14px;padding:10px 0;border-bottom:1.5px solid #F0F2F8}
.sk-hd{padding:0 0 8px 0;font-size:12.5px;font-weight:500;color:#8A93AD}
.sk-s{font-size:15px;font-weight:600}
.tk{position:relative;display:flex;align-items:center;justify-content:space-between;height:24px;padding:0 2px}
.tk::before{content:'';position:absolute;left:6px;right:6px;top:50%;height:2px;margin-top:-1px;background:#E6EAF3}
.tk-l{position:absolute;top:50%;height:4px;margin-top:-2px;border-radius:4px;background:#1652F0;left:calc(6px + (100% - 12px) * var(--a) / 4);right:calc(6px + (100% - 12px) * (4 - var(--b)) / 4)}
.tk i{position:relative;z-index:1;width:10px;height:10px;box-sizing:border-box;border-radius:50%;background:#FFFFFF;border:2px solid #CBD3E6}
.tk i.on{background:#1652F0;border-color:#1652F0}
.tk-x{justify-content:flex-start;gap:8px;font-size:13px;font-weight:500;color:#8A5A00}
.tk-x::before{display:none}
.tk-x svg{color:#B76E00}
.lo{display:flex;flex-direction:column;gap:12px}
.lo-r{display:grid;grid-template-columns:36px minmax(0,1fr) 36px;gap:12px;align-items:start}
.lo-n{width:36px;height:36px;margin-top:6px;border-radius:50%;background:#EAF0FF;color:#0E3BB8;font-size:14px;font-weight:600;display:flex;align-items:center;justify-content:center}
.lo-r .ds-x{margin-top:6px}
.lo-r.warn .ds-in{border-color:#E8B54A}
.lo-r.warn .lo-n{background:#FFF4E0;color:#8A5A00}
.lo-w{margin-top:10px;display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:14px;background:#FFFAF0;border:1.5px solid #F4DDAA}
.lo-w p{margin:0;flex:1;font-size:14px;line-height:1.5;color:#3A4566}
.lo-w p b{color:#8A5A00;font-weight:600}
.lo-add{margin-top:16px}
.mx-w{overflow-x:auto;margin:0 -8px;padding:0 8px}
.mx{min-width:720px}
.mx-r{display:grid;grid-template-columns:minmax(260px,2fr) repeat(var(--n),minmax(92px,1fr));align-items:center;gap:8px;padding:8px 0;border-bottom:1.5px solid #F0F2F8}
.mx-hd{padding:0 0 10px 0;font-size:13px;font-weight:600;color:#3A4566;text-align:center}
.mx-o{display:flex;flex-direction:column;gap:4px;align-items:flex-start;padding-right:8px}
.mx-o em{font-style:normal;font-size:12px;font-weight:600;color:#1652F0}
.mx-o > span{font-size:14.5px;line-height:1.4}
.mx-r.warn .mx-o em{color:#8A5A00}
.mx-c{justify-self:center;width:44px;height:44px;border-radius:12px;border:1.5px dashed #CBD3E6;background:#FFFFFF;color:#FFFFFF;display:flex;align-items:center;justify-content:center;cursor:pointer;font-family:inherit;transition:background .2s ease,border-color .2s ease}
.mx-c:hover{border-color:#1652F0}
.mx-ck{display:flex;opacity:0}
.mx-l{display:none}
.mx-c.on{border:1.5px solid #1652F0;background:#1652F0}
.mx-c.on .mx-ck{opacity:1}
.mx-c:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:2px}
.mx-cov{border-bottom:0;background:#F7F9FD;border-radius:14px;padding:12px 0 12px 14px;margin-top:8px}
.mx-k{display:flex;flex-direction:column;align-items:center;gap:2px;text-align:center}
.mx-k b{font-size:13px;font-weight:600}
.mx-k b.amber{color:#8A5A00}
.mx-k span{font-size:12px;color:#5B6582}
.ev{display:flex;flex-direction:column}
.ev-r{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.6fr);gap:24px;align-items:center;padding:16px 0;border-bottom:1.5px solid #F0F2F8}
.ev-r:last-child{border-bottom:0}
.ev-o{display:flex;flex-direction:column;gap:6px;min-width:0}
.ev-o em{font-style:normal;font-size:12px;font-weight:600;color:#1652F0}
.ev-o b{font-size:15px;font-weight:600;line-height:1.4}
.ev-sk{display:flex;flex-wrap:wrap;gap:6px}
.ch{display:flex;flex-direction:column;gap:6px}
.ch-r{display:grid;grid-template-columns:120px repeat(4,minmax(0,1fr));align-items:center;position:relative}
.ch-r:not(.ch-hd)::before{content:'';position:absolute;left:calc(120px + 12.5% - 30px);right:calc(12.5% - 22px);top:50%;height:2px;background:linear-gradient(90deg,#1652F0,#AFC1F5)}
.ch-hd{font-size:12.5px;font-weight:500;color:#8A93AD;text-align:center}
.ch-hd span:first-child{text-align:left}
.ch-o{font-size:14px;font-weight:600}
.ch-c{position:relative;z-index:1;justify-self:center;width:30px;height:30px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.ch-c.ok{background:#1652F0;color:#FFFFFF;box-shadow:0 0 0 4px #FFFFFF}
.ch-c.no{background:#FFFFFF;box-shadow:0 0 0 4px #FFFFFF}
.ch-c.no i{width:26px;height:26px;box-sizing:border-box;border-radius:50%;border:2px dashed #CBD3E6}
.as-g{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.ds-opt.as{align-items:center}
.as-i{width:40px;height:40px;flex-shrink:0;border-radius:12px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.ds-opt.on .as-i{background:#FFFFFF}
.ef-r{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(0,1fr) minmax(0,1fr);align-items:center;gap:16px;padding:12px 0;border-bottom:1.5px solid #F0F2F8}
.ef-hd{padding:0 0 8px 0;font-size:12.5px;font-weight:500;color:#8A93AD}
.ef-t{display:flex;flex-direction:column;gap:2px}
.ef-t b{font-size:15px;font-weight:600}
.ef-t span{font-size:13px;color:#5B6582}
.ef-in{position:relative;max-width:150px}
.ef-in .ds-in{padding-right:60px}
.ef-in em{position:absolute;right:14px;top:50%;transform:translateY(-50%);font-style:normal;font-size:13px;color:#8A93AD}
.ef-d{font-size:15px;font-weight:500;color:#0F6B45}
.ef-tot{border-bottom:0;padding-top:16px;font-size:15px}
.ef-sum{display:flex;align-items:center;justify-content:space-between;gap:32px}
.ef-l b{display:block;font-size:30px;font-weight:600;letter-spacing:-0.02em}
.ef-l p{margin:6px 0 0 0;font-size:14px;color:#5B6582}
.ef-p{flex:0 1 380px;display:flex;flex-direction:column;gap:10px;font-size:14px;color:#3A4566}
.ef-pb{height:8px;border-radius:8px;background:#EAF0FF;overflow:hidden}
.ef-pb i{display:block;height:100%;border-radius:8px;background:#1652F0}
.sm-c{display:inline-flex;align-items:center;gap:8px;font-size:13.5px;color:#5B6582}
.sm-c .st{margin-left:6px}
.sm-r{display:grid;grid-template-columns:18px 180px minmax(0,1fr) auto;align-items:center;gap:16px;min-height:58px;padding:0 6px;border-bottom:1.5px solid #F0F2F8;color:#0B1433;text-decoration:none;border-radius:10px}
.sm-r:last-child{border-bottom:0}
.sm-r:hover{background:#F7F9FD}
.sm-l{font-size:15px;font-weight:600}
.sm-v{font-size:14.5px;color:#3A4566}
.sm-e{font-size:14px;font-weight:600;color:#1652F0}
.sg{display:flex;flex-wrap:wrap;gap:8px}
.sg-i{display:inline-flex;align-items:center;gap:7px;height:34px;padding:0 13px 0 10px;border-radius:999px;background:#E7F5EE;color:#0F6B45;font-size:13px;font-weight:500}
.sg-i.off{background:#F1F3F8;color:#5B6582}
.sg-i.off i{width:11px;height:11px;box-sizing:border-box;border-radius:50%;border:1.5px dashed #8A93AD}
@media (max-width: 1180px){.hm-dg{grid-template-columns:repeat(4,minmax(0,1fr))}.as-g{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width: 960px){
.hm-strip{width:100%}
.hm-strip > span{flex:1}
.hm-strip em{white-space:nowrap}
.hm-next{margin-top:18px;padding:22px 18px;flex-direction:column-reverse;align-items:flex-start;gap:16px}
.hm-next h2{font-size:20px}
.hm-next p{font-size:14px}
.hm-ring{width:84px;height:84px;align-self:flex-start}
.hm-ring svg{width:84px;height:84px}
.hm-ring b{font-size:18px}
.hm-ring em{display:none}
.hm-na{flex-direction:column;align-items:stretch;gap:8px;margin-top:18px}
.hm-na .ds-btn{width:100%;justify-content:space-between}
.hm-na .ds-link{justify-content:center;min-height:40px}
.hm-list,.hm-det{padding:6px}
.hm-r{gap:12px;padding:10px;min-height:64px}
.hm-r .avs,.hm-go{display:none}
.hm-rt span{font-size:13px}
.hm-dg{grid-template-columns:repeat(2,minmax(0,1fr))}
.in-ai .ds-in{padding-right:14px}
.in-ai .nv-chip{position:static;transform:none;margin-top:8px}
.pq-r{grid-template-columns:minmax(0,1fr) 36px;gap:10px;padding:14px 0}
.pq-r .sel,.pq-r > div{grid-column:1}
.pq-r .ds-x{grid-row:1;grid-column:2}
.pq-hd{display:none}
.opt2,.opt3,.as-g{grid-template-columns:minmax(0,1fr)}
.ce-r{flex-wrap:wrap;padding:14px 0;gap:10px 12px}
.ce-r > .ds-tag,.ce-r > .ds-ghost,.ce-s{margin-left:52px}
.sk-r{position:relative;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;padding:14px 0}
.sk-s{grid-column:1 / -1;padding-right:44px}
.sk-r .ds-x{position:absolute;right:0;top:8px}
.sk-r .ds-in{font-size:14px;padding-left:12px}
.tk{grid-column:1 / -1}
.sk-hd{display:none}
.lo-r{grid-template-columns:minmax(0,1fr) 36px;gap:10px}
.lo-n{display:none}
.lo-w{flex-wrap:wrap}
.lo-w p{flex-basis:calc(100% - 42px)}
.lo-w .ds-ghost{margin-left:40px}
.mx-w{margin:0;padding:0;overflow:visible}
.mx{min-width:0}
.mx-r.mx-hd{display:none}
.mx-r{display:flex;flex-wrap:wrap;gap:8px;padding:14px 0}
.mx-o{width:100%;padding:0 0 4px 0}
.mx-c{justify-self:auto;width:auto;height:36px;padding:0 13px;border-radius:999px;border-style:solid;color:#0B1433;gap:6px;font-size:13px;font-weight:500}
.mx-c .mx-ck{display:none}
.mx-c.on{color:#FFFFFF}
.mx-c.on .mx-ck{display:flex}
.mx-l{display:inline}
.mx-cov{padding:12px 14px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.mx-cov .mx-o{grid-column:1 / -1}
.mx-k{align-items:flex-start;text-align:left}
.mx-k em{font-style:normal;font-size:12px;color:#5B6582}
.ev-r{grid-template-columns:minmax(0,1fr);gap:12px}
.ch-r{grid-template-columns:52px repeat(4,minmax(0,1fr))}
.ch-r:not(.ch-hd)::before{left:calc(52px + 12.5% - 18px)}
.ch-hd{font-size:11.5px}
.ef-r{grid-template-columns:minmax(0,1fr) 110px;gap:10px}
.ef-d{grid-column:1;font-size:13.5px}
.ef-hd{display:none}
.ef-in{grid-row:1 / span 2;grid-column:2}
.ef-tot{grid-template-columns:minmax(0,1fr) auto}
.ef-tot span:nth-child(3){grid-column:1}
.ef-sum{flex-direction:column;align-items:stretch;gap:18px}
.ef-l b{font-size:24px}
.ef-p{flex-basis:auto}
.sm-r{grid-template-columns:18px minmax(0,1fr) auto;row-gap:2px;padding:12px 4px}
.sm-v{grid-column:2 / -1;font-size:13.5px}
.sm-e{grid-row:1;grid-column:3}
.sm-c{display:none}
}
'''

def studio_body():
    blocks = []
    for key, nav, html in PAGES:
        blocks.append('<sc-if value="{{p_%s}}" hint-placeholder-val="{{ %s }}">\n%s\n</sc-if>' % (key, 'true' if key == 'home' else 'false', html))
    # one sidebar per active nav item (so the active state is static markup)
    navs = []
    for nav in sorted(set(n for _, n, _ in PAGES)):
        navs.append('<sc-if value="{{n_%s}}" hint-placeholder-val="{{ %s }}">%s</sc-if>' % (nav, 'true' if nav == 'home' else 'false', sidebar(nav)))
    return '''<div class="ds-root">
%s
<div style="min-width: 0; display: flex; flex-direction: column">
%s
<main class="ds-main">
%s
</main>
</div>
</div>''' % ('\n'.join(navs), topbar(), '\n'.join(blocks))

STUDIO_JS = W.js() + '''var NAV = %s;
class Component extends DCLogic {
  renderVals() {
    var pg = this.props.page || 'home';
    var v = togVals(this);
    var self = this;
    Object.keys(NAV).forEach(function (k) { v['p_'.concat(k)] = k === pg; });
    var nav = NAV[pg] || 'home';
    %s.forEach(function (n) { v['n_'.concat(n)] = n === nav; });
    v.navCls = this.state.nav ? 'ds-open' : '';
    v.toggleNav = function () { self.setState({ nav: !self.state.nav }); };
    return v;
  }
}''' % (json.dumps({k: n for k, n, _ in PAGES}), json.dumps(sorted(set(n for _, n, _ in PAGES))))

write('Studio.dc.html', doc('Course Studio · shared source', kit.KIT_CSS + '\n' + dash.DASH_CSS + BASE_CSS + CW_CSS + STUDIO_CSS, studio_body(), STUDIO_JS))

# ======================================================================= boards
BOARDS = [
    ('STU-001', 'Setup', {'step': 'type'}, 'CR-STU-001 · What will you create?'),
    ('STU-002', 'Setup', {'step': 'delivery'}, 'CR-STU-002 · Delivery'),
    ('STU-003', 'Setup', {'step': 'review'}, 'CR-STU-003 · Setup review'),
    ('STU-004', 'Setup', {'step': 'how'}, 'CR-STU-004 · How will you create it?'),
    ('STU-008', 'Setup', {'step': 'welcome'}, 'CR-STU-008 · Studio welcome'),
    ('STU-009', 'Studio', {'page': 'home'}, 'CR-STU-009 · Studio home'),
    ('STU-010', 'Studio', {'page': 'basics'}, 'CR-STU-010 · Basics'),
    ('STU-011', 'Studio', {'page': 'audience'}, 'CR-STU-011 · Audience & prerequisites'),
    ('STU-012', 'Studio', {'page': 'career'}, 'CR-STU-012 · Career & progression'),
    ('STU-012b', 'Studio', {'page': 'careercert'}, 'CR-STU-012b · Career: prepares for a certification'),
    ('STU-013', 'Studio', {'page': 'skills'}, 'CR-STU-013 · Skills & proficiency'),
    ('STU-014', 'Studio', {'page': 'outcomes'}, 'CR-STU-014 · Learning outcomes'),
    ('STU-015', 'Studio', {'page': 'skillmap'}, 'CR-STU-015 · Outcome → skill map'),
    ('STU-016', 'Studio', {'page': 'evidence'}, 'CR-STU-016 · Outcome → evidence'),
    ('STU-017', 'Studio', {'page': 'design'}, 'CR-STU-017 · Assessment & award'),
    ('STU-018', 'Studio', {'page': 'effort'}, 'CR-STU-018 · Learning effort'),
    ('STU-019', 'Studio', {'page': 'summary'}, 'CR-STU-019 · Design summary'),
]

if __name__ == '__main__':
    import sys
    H = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else {}
    for code, src, props, title in BOARDS:
        bg = '#FFFFFF' if src == 'Setup' else '#F7F9FD'
        hd, hm = H.get(code, (900, 844))
        write(code + '.dc.html', wrapper(title + ' · Desktop', src, props, 1440, hd, bg))
        write(code + '-Mobile.dc.html', wrapper(title + ' · Mobile', src, props, 390, hm, bg))
    print('ok', len(BOARDS), 'boards; toggles', T.n, W.n)
