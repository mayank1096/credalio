"""Link 4 · Batch 1: course setup (focus flow) + course design (workspace).

Setup.dc.html  (prop step: type | delivery | review | how | welcome)   CR-STU-001, 002, 003, 004, 008
Studio.dc.html (prop page: home | basics | audience | career | careercert | skills | outcomes | skillmap | evidence |
                design | effort | summary)                              CR-STU-009 to CR-STU-019
Boards: STU-0xx(.dc.html) desktop 1440 + STU-0xx-Mobile 390, each a dc-import of its source.
"""
import json
from l4kit import *
from rail import *

# ======================================================================= SETUP (focus mode)
T = Toggles()

def fmt_card(icon, kicker, title, desc, best, cta, href):
    """Same card design as Link 1 Create new (CR-HOME-NEW .nw-f); client copy."""
    return ('<a class="nw-f" href="%s"><span class="nw-fi">%s</span><b>%s</b><span class="nw-fd">%s</span>'
            '<span class="nw-fm"><em>Best for</em>%s</span><span class="nw-go">%s%s</span></a>') % (
        href, ic(icon, 22), title, desc, ''.join('<span>%s</span>' % b for b in best), cta, ic('arrowr', 15, 2.2))

S_TYPE = '''<div class="fx-col">
<h1 class="fx-h1 ob-in">What will you create?</h1>
<p class="fx-sub ob-in2">Choose the type of learning experience that best matches the outcome you want learners to achieve.</p>
<div class="nw-g ob-in3">%s</div>
<div class="fx-nova ob-in4">%s<span class="fx-nl"><b>Not sure? Tell Nova</b> what you want learners to achieve.</span><label class="sr-only" for="fxq">What should learners achieve?</label><input id="fxq" placeholder="What should learners achieve?">%s</div>
</div>''' % (
    fmt_card('course', 'Course', 'Course', 'Teach a focused subject or skill.', ['Individual skills', 'Knowledge development', 'Self-paced or instructor-led learning'], 'Create Course', 'STU-002.dc.html') +
    fmt_card('cert', 'Professional Certification', 'Professional Certification', 'Assess and verify professional competence.', ['Professional standards', 'Competency verification', 'Formal assessment', 'Recognised proof'], 'Create Certification', '#') +
    fmt_card('path', 'Career Path', 'Career Path', 'Build a journey toward a role or career outcome.', ['Multiple connected skills', 'Career transitions', 'Courses + practice + credentials', 'Portfolio development'], 'Create Career Path', '#') +
    fmt_card('program', 'Learning Program', 'Learning Program', 'Deliver structured learning over time.', ['Cohorts', 'Institutions', 'Multi-course programs', 'Guided learning'], 'Create Learning Program', '#'),
    nova_av('sm'), nchip('Help Me Choose'))

VIDEO = '<span class="vz-vid"><span class="vz-play"></span><span class="vz-pb"><i></i></span></span>'
def lrows(n=3):
    return '<span class="vz-rows">%s</span>' % ''.join('<span class="vz-row%s"><i></i><b></b></span>' % c for c in ([' dn', ' dn', ' cur'][:n]))
CAL = '<span class="vz-cal">%s</span>' % ''.join('<span class="vz-day%s"><i></i></span>' % (' on' if i == 2 else '') for i in range(5))
SESS = '<span class="vz-sess"><span class="vz-live"></span><b></b>%s</span>' % stack([(F1, 'PN'), (M1, 'JA'), (M2, 'TA')], 20)
VIS = {
    'self': '<span class="vz vz-self">%s%s</span>' % (VIDEO, lrows()),
    'live': '<span class="vz vz-livec">%s%s</span>' % (CAL, SESS),
    'hyb': '<span class="vz vz-hyb">%s<span class="vz-link"><i></i><i></i><i></i></span><span class="vz-day on solo"><i></i></span></span>' % VIDEO,
}

def deliv(vis, title, desc, feats, on):
    inner = ('<span class="dv-vz" aria-hidden="true">%s</span><span class="dv-t"><b>%s</b><span>%s</span><span class="dv-f"><em>Features</em>%s</span></span>' %
             (VIS[vis], title, desc, ''.join('<span>%s%s</span>' % (ck(11), f) for f in feats)))
    return T.opt(inner, on, 'dlv', 'dv')

S_DELIV = """<div class="fx-col">
<a class="fx-back" href="STU-001.dc.html">%s<span>Back</span></a>
<h1 class="fx-h1 ob-in">How will learners experience this course?</h1>
<p class="fx-sub ob-in2">Self-paced courses can use video, audio, text, documents, interactive activities, projects and assessments.</p>
<div class="dv-g ob-in3" role="group" aria-label="Delivery type">%s</div>
<div class="ob-in4" style="margin-top: 18px">%s</div>
<div class="fx-acts">%s</div>
</div>""" % (
    ICON(I['back'], 16, 2),
    deliv('self', 'Self-Paced', 'Learners progress through lessons and activities at their own pace.', ['Video, audio, text, documents', 'Interactive activities', 'Projects and assessments'], False) +
    deliv('live', 'Live Instructor-Led', 'Learning happens primarily through scheduled live sessions.', ['Live classes and scheduled sessions', 'Attendance', 'Resources and assignments'], False) +
    deliv('hyb', 'Hybrid', 'Combine self-paced learning with scheduled live sessions.', ['Content lessons + live classes', 'Assignments and practice', 'Assessments'], True),
    nova_sg('Hybrid selected. I’ll help you structure which parts should be self-paced and which benefit from live instruction.'),
    btn('Continue', 'STU-003.dc.html'))

S_REVIEW = """<div class="fx-col n">
<a class="fx-back" href="STU-002.dc.html">%s<span>Back</span></a>
<h1 class="fx-h1 ob-in">Your course setup</h1>
<p class="fx-sub ob-in2">Nothing else to decide yet. You can change this any time.</p>
<div class="ds-card rs ob-in3">
<div class="rs-top"><span class="rs-cv">%s</span><span class="rs-tt"><em>Learning experience</em><b>Course</b></span></div>
<div class="rs-g">
<div class="rs-c"><em>Delivery</em><span class="rs-v"><span class="rs-vz" aria-hidden="true">%s</span><b>Hybrid</b></span></div>
<div class="rs-c"><em>Creator</em><span class="rs-v">%s<b>Ada Ononuju</b></span></div>
<div class="rs-c"><em>Status</em><span class="rs-v"><span class="rs-st"><i></i>Draft</span></span></div>
</div>
</div>
<div class="fx-acts"><a class="ds-ghost" href="STU-001.dc.html">Change Setup</a>%s</div>
</div>""" % (
    ICON(I['back'], 16, 2), ic('course', 30, 1.7), VIS['hyb'], av(ME, 'AO', 40),
    btn('Continue', 'STU-004.dc.html'))

def how(vis, kicker, title, desc, nxt, on):
    inner = '<span class="hw-v" aria-hidden="true">%s</span><span class="hw-t"><b>%s</b><span>%s</span><em>%s</em></span>' % (vis, title, desc, nxt)
    return T.opt(inner, on, 'how', 'hw')

V_SOLO = av(ME, 'AO', 44, 'hw-me')
V_CO = '<span class="hw-co">%s%s<span class="hw-plus">%s</span></span>' % (av(ME, 'AO', 40, 'hw-me'), av(M1, 'JA', 32), ic('plus', 12, 2.6))
V_OPEN = '<span class="hw-open"><span class="hw-ring"></span>%s<i style="left: 4px; top: 22px"></i><i style="right: 2px; top: 10px"></i><i style="right: 8px; bottom: 2px"></i><i style="left: 16px; bottom: 0"></i><i style="left: 30px; top: 0"></i></span>' % av(ME, 'AO', 32, 'hw-me')

S_HOW = '''<div class="fx-col">
<a class="fx-back" href="STU-003.dc.html">%s<span>Back</span></a>
<h1 class="fx-h1 ob-in">How will you create this course?</h1>
<div class="hw-g ob-in3" role="group" aria-label="How will you create this course?">%s</div>
<div class="fx-acts"><span class="fx-note">You can change this later from Collaborators in Course Studio.</span>%s</div>
</div>''' % (
    ICON(I['back'], 16, 2),
    how(V_SOLO, 'Solo', 'Create Solo', 'You are the primary and only creator. Go straight to building your course.', 'Next: Curriculum Builder', False) +
    how(V_CO, 'Co-Creators', 'Create with Co-Creators', 'Invite a specific person by name or email to contribute to this course.', 'Next: Invite Co-Creator', True) +
    how(V_OPEN, 'Open', 'Open to Collaboration', 'Make this opportunity discoverable to approved Credalio creators. Different from inviting someone directly.', 'Next: Open collaboration setup', False),
    btn('Continue', 'STU-008.dc.html'))

PLAN = [('Define', 'Tell us what you’re teaching and who it’s for.', 'Design'), ('Design', 'Define skills, outcomes and evidence.', 'Design'),
        ('Build', 'Create lessons, practice and assessments.', 'Build · Experience'), ('Review', 'Preview and test the learning experience.', 'Prepare'),
        ('Validate', 'Submit for independent validation.', 'Validate')]
S_WELCOME = '''<div class="fx-col n wl">
<div class="wl-nv ob-in">%s</div>
<h1 class="fx-h1 ob-in">Let’s build your course.</h1>
<p class="fx-sub ob-in2"><b>Nova</b>: I’ll help you turn your expertise into a structured learning experience.</p>
<div class="wl-tags ob-in2">%s%s<span class="ds-tag line">%s 3 creators</span></div>
<div class="xb-route ob-in3">
<div class="xb-rh"><span class="xb-rn">Your Studio is a workspace, not a wizard.%s</span></div>
<ol class="xb-steps">%s</ol>
</div>
<div class="xb-acts ob-in4">%s<span class="wl-alt"><a class="ds-link" href="#">%s<span>Import Existing Course</span></a><span aria-hidden="true">·</span><a class="ds-link" href="STU-009.dc.html">Go to Studio Home</a></span></div>
</div>''' % (
    nova_av('lg'), tag('Course', 'line'), tag('Hybrid', 'line'), stack(TEAM, 18),
    tip('Work in any order and come back whenever you like: everything saves as you go, and Studio Home always shows your next step. Only submitting for validation and publishing have requirements.', 'r'),
    ''.join('<li class="xb-s%s"><span class="xb-sn">%d</span><span class="xb-sl"><b>%s</b><span>%s</span><em>%s</em></span></li>' % (' xb-first' if i == 0 else '', i + 1, a, b, c) for i, (a, b, c) in enumerate(PLAN)),
    btn('Start Building', 'STU-010.dc.html', 'xb-go'), ic('import', 16, 2))

STEPS = [('type', 'Step 1 of 4', 25, S_TYPE), ('delivery', 'Step 2 of 4', 50, S_DELIV), ('review', 'Step 3 of 4', 75, S_REVIEW),
         ('how', 'Step 4 of 4', 100, S_HOW), ('welcome', '', 100, S_WELCOME)]

SETUP_BODY = '''<div class="fx-root">
<header class="fx-top">
<a href="#" class="fx-x fx-xm" aria-label="Save &amp; exit">%s</a>
<div class="fx-title"><span class="fx-t1">Creator Studio</span></div>
<span style="flex-grow: 1"></span>
<span class="fx-step">{{stepLabel}}</span>
<a href="#" class="ds-tok" aria-label="72,450 Creio">%s<span>72.4K</span></a>
<a href="#" class="ds-ghost fx-exit">Save &amp; exit</a>
<span class="fx-bar" style="width: {{barW}}"></span>
</header>
<main class="fx-main">
%s
</main>
</div>''' % (ic('x', 20, 2), COIN('fc', 26), '\n'.join('<sc-if value="{{s_%s}}" hint-placeholder-val="{{ %s }}">%s</sc-if>' % (k, 'true' if k == 'type' else 'false', html) for k, _, _, html in STEPS))

SETUP_CSS = r'''.nw-g{margin-top:32px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}
.nw-f{position:relative;display:flex;flex-direction:column;padding:20px;border-radius:20px;background:#FFFFFF;border:1.5px solid #E6EAF3;color:#0B1433;font-family:inherit;text-align:left;cursor:pointer;transition:border-color .2s ease,box-shadow .2s ease,transform .2s ease}
.nw-f:hover{border-color:#CBD7F5;box-shadow:0 14px 34px rgba(22,82,240,.08);transform:translateY(-2px)}
.nw-fi{width:46px;height:46px;border-radius:14px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.nw-f b{margin-top:14px;font-size:17px;font-weight:600}
.nw-fd{margin-top:6px;font-size:14px;line-height:1.5;color:#4A5578;flex-grow:1}
.nw-f{text-decoration:none}
.nw-k{margin-top:14px;font-size:11.5px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:#8A93AD}
.nw-k + b{margin-top:4px !important}
.nw-fm{margin-top:16px;padding-top:14px;border-top:1.5px solid #F0F2F8;display:flex;flex-direction:column;gap:6px;font-size:13.5px;color:#0B1433}
.nw-fm span::before{content:'';display:inline-block;width:5px;height:5px;border-radius:50%;background:#9DB8F7;margin:0 9px 2px 0}
.nw-go{margin-top:16px;display:inline-flex;align-items:center;gap:6px;font-size:14px;font-weight:600;color:#1652F0}
.nw-f:hover .nw-go svg{transform:translateX(3px)}
.nw-go svg{transition:transform .2s ease}
.fx-nl{flex-shrink:0;font-size:14px;color:#3A4566;white-space:nowrap}
.fx-nl b{font-weight:600;color:#0B1433}
.fx-nova input{border-left:1.5px solid #EEF1F7 !important;padding-left:14px !important}
.dv-f em{font-style:normal;font-size:12px;color:#8A93AD}
.hw-k{font-size:11.5px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:#8A93AD}
.fx-note{margin-right:auto;font-size:14px;color:#5B6582}
.fx-exit{height:40px;padding:0 16px;font-size:14px}
.fx-xm{display:none !important}
.xb-sl em{font-style:normal;font-size:11px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;color:#8A93AD;margin-top:2px}
.fx-sub b{font-weight:600;color:#0B1433}
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
.dv-g{margin-top:32px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.ds-opt.dv{flex-direction:column;align-items:stretch;gap:0;padding:10px 10px 22px 10px;border-radius:22px;transition:border-color .2s ease,box-shadow .2s ease,transform .2s ease}
.ds-opt.dv:hover{transform:translateY(-2px);box-shadow:0 18px 40px -22px rgba(22,82,240,.35)}
.ds-opt.dv.on{background:#FFFFFF;box-shadow:0 0 0 4px rgba(22,82,240,.12),0 22px 44px -24px rgba(22,82,240,.45)}
.dv .ds-opt-ck{position:absolute;top:22px;right:22px;margin:0;z-index:2}
.dv-vz{display:block;height:148px;border-radius:15px;background:linear-gradient(160deg,#F5F8FF,#EDF2FF);position:relative;overflow:hidden}
.ds-opt.on .dv-vz{background:linear-gradient(160deg,#EAF0FF,#DCE6FF)}
.dv-t{display:flex;flex-direction:column;gap:6px;min-width:0;padding:18px 12px 0 12px}
.dv-t b{font-size:18px;font-weight:600;letter-spacing:-0.01em}
.dv-t > span{font-size:14px;line-height:1.5;color:#4A5578}
.dv-f{margin-top:12px;padding-top:14px;border-top:1.5px solid #EEF1F7;display:flex;flex-direction:column;gap:8px}
.dv-f span{display:flex;align-items:center;gap:9px;font-size:13.5px;color:#3A4566}
.dv-f span svg{flex-shrink:0;width:18px;height:18px;padding:4px;box-sizing:border-box;border-radius:50%;background:#EAF0FF;color:#1652F0}
.ds-opt.on .dv-f span svg{background:#1652F0;color:#FFFFFF}
.vz{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;gap:12px;padding:18px}
.vz-vid{position:relative;width:118px;height:76px;flex-shrink:0;border-radius:12px;background:linear-gradient(140deg,#1652F0,#0B1433);box-shadow:0 12px 24px -12px rgba(11,20,51,.6)}
.vz-play{position:absolute;left:50%;top:44%;width:26px;height:26px;margin:-13px 0 0 -13px;border-radius:50%;background:#FFFFFF}
.vz-play::after{content:'';position:absolute;left:10px;top:7px;border-left:9px solid #1652F0;border-top:6px solid transparent;border-bottom:6px solid transparent}
.vz-pb{position:absolute;left:10px;right:10px;bottom:9px;height:4px;border-radius:4px;background:rgba(255,255,255,.28)}
.vz-pb i{display:block;width:58%;height:100%;border-radius:4px;background:#FFFFFF}
.vz-rows{display:flex;flex-direction:column;gap:8px;width:96px}
.vz-row{display:flex;align-items:center;gap:7px;height:20px;padding:0 7px;border-radius:7px;background:#FFFFFF;box-shadow:0 4px 10px -6px rgba(11,20,51,.25)}
.vz-row i{width:8px;height:8px;border-radius:50%;flex-shrink:0;border:1.5px solid #CBD3E6;box-sizing:border-box}
.vz-row.dn i{border:0;background:#0F6B45}
.vz-row.cur i{border:0;background:#1652F0;box-shadow:0 0 0 3px rgba(22,82,240,.18)}
.vz-row b{flex:1;height:5px;border-radius:5px;background:#E1E7F3}
.vz-row.cur b{background:#C9D7FA}
.vz-livec{flex-direction:column;gap:10px}
.vz-cal{display:flex;gap:6px}
.vz-day{width:30px;height:34px;box-sizing:border-box;border-radius:8px;background:#FFFFFF;box-shadow:0 4px 10px -6px rgba(11,20,51,.25);display:flex;align-items:flex-end;justify-content:center;padding-bottom:6px}
.vz-day i{width:14px;height:4px;border-radius:4px;background:#E1E7F3}
.vz-day.on{background:#1652F0;transform:translateY(-3px);box-shadow:0 10px 18px -8px rgba(22,82,240,.7)}
.vz-day.on i{background:rgba(255,255,255,.75)}
.vz-sess{display:flex;align-items:center;gap:8px;height:34px;padding:0 6px 0 10px;border-radius:999px;background:#FFFFFF;box-shadow:0 8px 16px -10px rgba(11,20,51,.35)}
.vz-sess b{width:52px;height:5px;border-radius:5px;background:#E1E7F3}
.vz-sess .avs .av + .av{margin-left:-6px}
.vz-live{width:8px;height:8px;border-radius:50%;background:#0F6B45;box-shadow:0 0 0 0 rgba(15,107,69,.45);animation:vzPulse 1.8s ease-out infinite}
@keyframes vzPulse{0%{box-shadow:0 0 0 0 rgba(15,107,69,.45)}100%{box-shadow:0 0 0 8px rgba(15,107,69,0)}}
.vz-hyb{gap:0}
.vz-hyb .vz-vid{width:104px;height:68px}
.vz-link{display:flex;align-items:center;gap:5px;padding:0 8px}
.vz-link i{width:5px;height:5px;border-radius:50%;background:#1652F0;opacity:.35}
.vz-link i:nth-child(2){opacity:.6}
.vz-link i:nth-child(3){opacity:.9}
.vz-day.solo{width:52px;height:60px;border-radius:12px;padding-bottom:10px;transform:none}
.vz-day.solo i{width:24px;height:5px}
.rs{margin-top:28px;overflow:hidden;padding:0}
.rs + .fx-acts .ds-ghost{margin-right:auto}
.rs-top{display:flex;align-items:center;gap:18px;padding:26px 28px;background:linear-gradient(120deg,#F2F6FF,#E6EEFF)}
.rs-cv{width:64px;height:64px;flex-shrink:0;border-radius:18px;background:linear-gradient(140deg,#1652F0,#0B1433);color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 14px 28px -14px rgba(22,82,240,.8)}
.rs-tt{display:flex;flex-direction:column;gap:2px}
.rs-tt em,.rs-c em{font-style:normal;font-size:12.5px;font-weight:500;color:#5B6582}
.rs-tt b{font-size:26px;font-weight:600;letter-spacing:-0.02em}
.rs-g{display:grid;grid-template-columns:1.3fr 1fr .8fr}
.rs-c{display:flex;flex-direction:column;gap:12px;padding:22px 28px 24px 28px}
.rs-c + .rs-c{border-left:1.5px solid #EEF1F7}
.rs-v{display:flex;align-items:center;gap:12px;min-height:44px}
.rs-v b{font-size:16px;font-weight:600}
.rs-vz{position:relative;width:96px;height:44px;flex-shrink:0;border-radius:10px;background:#F5F8FF;overflow:hidden}
.rs-vz .vz{padding:0;transform:scale(.42);transform-origin:center}
.rs-st{display:inline-flex;align-items:center;gap:8px;height:32px;padding:0 14px 0 12px;border-radius:999px;background:#F1F3F8;color:#3A4566;font-size:13.5px;font-weight:500}
.rs-st i{width:8px;height:8px;border-radius:50%;background:#8A93AD}
@media (prefers-reduced-motion: reduce){.vz-live{animation:none}}
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
.nw-f{display:grid;grid-template-columns:40px minmax(0,1fr);column-gap:14px;align-items:center;padding:14px 16px;border-radius:16px}
.nw-fi{width:40px;height:40px;border-radius:12px;grid-row:span 2}
.nw-f b{margin-top:0;font-size:15.5px}
.nw-fd{margin-top:2px;font-size:13.5px}
.nw-fm,.nw-go,.nw-k,.hw-k,.xb-sl em{display:none}
.fx-nl{white-space:normal;flex:1 1 calc(100% - 44px);font-size:13.5px}
.fx-nova input{border-left:0 !important;padding-left:0 !important;flex-basis:100% !important;order:3}
.fx-nova .nv-chip{order:4}
.fx-note{margin:0 0 6px 0;text-align:center;font-size:13px}
.fx-acts .ds-ghost{width:100%}
.fx-exit{display:none !important}
.fx-xm{display:flex !important}
.nw-ck{top:50%;transform:translateY(-50%);right:14px}
.fx-nova{height:auto;flex-wrap:wrap;border-radius:18px;padding:12px;gap:10px}
.fx-nova input{flex-basis:calc(100% - 44px);height:36px;font-size:14.5px}
.dv-g{margin-top:20px;gap:10px;grid-template-columns:minmax(0,1fr)}
.hw-g{margin-top:20px;grid-template-columns:minmax(0,1fr);gap:10px}
.hw-t b{font-size:15.5px}
.ds-opt.dv{display:grid;grid-template-columns:88px minmax(0,1fr);column-gap:14px;align-items:center;padding:10px 46px 10px 10px;border-radius:18px}
.dv-vz{height:88px;border-radius:12px}
.dv-vz .vz{inset:auto;left:50%;top:50%;width:250px;height:148px;margin:-74px 0 0 -125px;padding:0;transform:scale(.36)}
.dv-t{padding:0}
.dv-t b{font-size:15.5px}
.dv-t > span{font-size:13.5px}
.dv-f{display:none}
.dv .ds-opt-ck{top:50%;right:14px;transform:translateY(-50%)}
.rs-top{padding:18px;gap:14px}
.rs-cv{width:52px;height:52px;border-radius:14px}
.rs-tt b{font-size:21px}
.rs-g{grid-template-columns:minmax(0,1fr)}
.rs-c{flex-direction:row;align-items:center;justify-content:space-between;padding:14px 18px}
.rs-c + .rs-c{border-left:0;border-top:1.5px solid #EEF1F7}
.rs-v{min-height:0;gap:10px}
.rs-vz{display:none}
.rs-v b{font-size:15px}
.rs-v .av{width:32px !important;height:32px !important}
.ds-opt.hw{flex-direction:row;align-items:center;gap:14px;padding:16px 48px 16px 16px}
.hw .ds-opt-ck{top:50%;transform:translateY(-50%);right:16px}
.hw-v{height:44px;width:60px;flex-shrink:0;justify-content:center}
.hw-t span{font-size:13.5px}
.hw-t em{margin-top:2px;font-size:12.5px}
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
PAGES = []  # (key, nav, head, main, actions, rail)

def P(key, nav, head, main, actions, rail=''):
    PAGES.append((key, nav, head, main, actions, rail))

F_CAREER = [('Career & Progression Relevance', 'STU-012.dc.html'), ('Skills & Proficiency', 'STU-013.dc.html')]
F_OUT = [('Learning Outcomes', 'STU-014.dc.html'), ('Outcome → Skill Mapping', 'STU-015.dc.html'), ('Outcome → Evidence Mapping', 'STU-016.dc.html')]
F_LD = [('Course Design', 'STU-017.dc.html'), ('Learning Effort', 'STU-018.dc.html'), ('Your Learning Design', 'STU-019.dc.html')]

# ---------- CR-STU-009 Studio home
def row(icon, title, meta, st_label, st_kind, href, extra=''):
    return ('<a class="hm-r" href="%s"><span class="hm-ri">%s</span><span class="hm-rt"><span class="hm-tt"><b>%s</b>%s</span><span class="hm-m">%s</span></span>%s<span class="hm-go">%s</span></a>' %
            (href, ic(icon, 18), title, tag(st_label, st_kind), meta, extra, ic('chev', 16, 2)))

DET = [('5', 'chapters'), ('9', 'lessons'), ('5', 'videos'), ('8h 5m', 'detected learning time'), ('3', 'assessments'), ('35', 'questions'), ('1', 'projects'), ('4 (3 assessed)', 'outcomes')]
P('home', 'home', page_head('Studio Home', COURSE, 'Course · Hybrid · Draft') +
'''<section class="hm-next ob-in2" aria-label="Recommended next step">
<div class="hm-nl"><span class="pg-e">Recommended next step</span><h2>Define who this course is for and where it leads</h2><p>Set the career role, stage and relevance for the Become Engine.</p>
<div class="hm-seg" role="img" aria-label="Course Design: 4 of 9 sections complete"><i class="dn"></i><i class="dn"></i><i class="dn"></i><i class="dn"></i><i class="nx"></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><span class="hm-sl">4 of 9 sections complete</span></div>
<div class="hm-na">%s<span class="hm-pk">Picks up where you left off.</span></div></div>
<div class="hm-rc"><div class="hm-ring">%s<span><b>31%%</b><em>Course Health</em></span></div><span class="hm-rl">%s<a class="ds-link" href="#">See what’s missing</a></span></div>
</section>''' % (btn('Continue Building', 'STU-012.dc.html', 'wh'), ring(31, grad=('hmg', '#9DB8F7', '#FFFFFF'), track='rgba(255,255,255,.14)'),
    tip('Completeness and readiness. Not a quality score and not CEI.', 'r')),
'''<section class="ds-card hm-list ob-in3" aria-label="Course sections">
%s%s%s%s%s%s
</section>''' % (
    row('layers', 'Course Design', '4 of 9 sections complete · Next: define who this course is for and where it leads', 'In progress', 'blue', 'STU-010.dc.html'),
    row('course', 'Curriculum', '5 chapters · 9 lessons · 8h 5m detected learning time', 'Done', 'green', 'STU-020.dc.html'),
    row('quiz', 'Assessments', '3 assessments · 35 questions · 3 of 4 outcomes assessed', 'In progress', 'blue', 'STU-ASM.dc.html'),
    row('lock', 'Validation Readiness', 'Opens once Design and Build are complete', 'Locked', '', '#'),
    row('users', 'Collaborators', '3 people · Dr. John Adeyemi, ABC Institute', 'Done', 'green', '#', stack(TEAM, 26)),
    row('target', 'Learning Intelligence Profile', '9 of 13 signals · What Credalio understands about this course. Next: career role, proficiency levels.', 'In progress', 'blue', 'STU-019.dc.html'),
),
'',
nova_rail('Welcome back. I’ll keep track of what’s incomplete so you don’t have to.', nchip('What’s left before validation?')) +
'<section class="ds-card rx cr-rx"><div class="cr-n">%s<b>72,450</b><span>Creio</span></div><p>Everyday help just works.</p><div class="cr-a"><a class="ds-ghost sm" href="#">Buy Creio</a><a class="ds-link sm" href="#">View usage</a></div></section>' % kit.coin(True) +
'<section class="ds-card rx hm-det" aria-label="Detected by Credalio"><span class="rx-k">Detected by Credalio%s</span><div class="hm-dg">%s</div></section>' % (
    tip('Built from your course structure as you work. No manual entry.', 'dn'), ''.join('<span><b>%s</b><em>%s</em></span>' % d for d in DET)))

# ---------- CR-STU-010 Basics
SKILLS4 = ['SQL', 'Data Cleaning', 'Data Analysis', 'Relational Databases']
P('basics', 'basics', page_head('Design', 'Basics', 'Start with the course itself.'),
'''<section class="ds-card fc ob-in2">
<div class="fg">
%s
%s
<div class="fg fg2 cv2">%s%s</div>
%s
<div class="fg fg2 keep">%s%s%s%s</div>
</div>
</section>
<section class="ds-card fc ob-in3">
<div class="fc-h"><div><h2>A few questions will help us configure your course%s</h2></div></div>
<div class="qs">
%s%s%s
</div>
</section>''' % (
    field('Course title', '<div class="in-ai"><input class="ds-in lg" value="Data Analysis with SQL" aria-label="Course title">%s</div>' % nchip('Improve title')),
    field('Short description (marketplace card)', '<input class="ds-in" value="Write SQL to answer real business questions, from first query to a finished analysis." aria-label="Short description (marketplace card)"><span class="fl-f"><span class="in-help">%s</span><span class="cnt">85 / 140</span></span>' % nchip('Generate suggestion')),
    field('Course cover', '<div class="cov"><span class="cov-i" aria-hidden="true">SQL</span><span class="cov-t"><b>sql-course-cover.png</b></span><a class="ds-link" href="#">Replace</a></div>'),
    field('Skills', '<div class="chips">%s</div><span class="in-help">%s</span>' % (''.join(W.chip(x, True) for x in SKILLS4), nchip('Suggest skills from description'))),
    field('Full description', '<textarea class="ds-in" aria-label="Full description">A hybrid course for career changers and analysts. Learn SQL step by step, practise on realistic business data, join a live analysis clinic and finish with a portfolio project.</textarea><span class="in-help">%s</span>' % nchip('Help me write this')),
    field('Primary category', sel('Technology', 'Primary category')), field('Topic', sel('Data Analytics', 'Topic')),
    field('Subtopic', sel('SQL', 'Subtopic')), field('Language', sel('English', 'Language')),
    tip('Saved to your course profile so you won’t be asked again at validation.'),
    '<div class="q"><span class="q-n">1</span><div class="q-b"><b>Does this course require learners to use external software?</b>%s<span class="fl-sub">Which?</span><div class="chips">%s%s%s%s</div></div></div>' % (
        W.seg(['Yes', 'No'], 0), W.chip('SQL Server', False, cls='sm'), W.chip('MySQL', False, cls='sm'), W.chip('PostgreSQL', True, cls='sm'), W.chip('Other', False, cls='sm')),
    '<div class="q"><span class="q-n">2</span><div class="q-b"><b>Will learners work with real or simulated data?</b>%s</div></div>' % W.seg(['Real', 'Simulated', 'Both', 'Neither'], 1),
    '<div class="q"><span class="q-n">3</span><div class="q-b"><b>Does this course involve AI?</b><div class="chips">%s%s%s%s%s</div></div></div>' % (
        W.chip('No', True, 'ai'), W.chip('Learners use AI tools', False, 'ai'), W.chip('AI is taught as a subject', False, 'ai'), W.chip('AI-generated outputs are assessed', False, 'ai'), W.chip('Other', False, 'ai'))),
acts('STU-011.dc.html'),
nova_rail('I’ll help with wording. You approve every change.', nchip('Improve title') + nchip('Suggest skills')) +
'''<section class="ds-card rx pv"><span class="rx-k">Short description (marketplace card)</span>
<div class="pv-c"><span class="pv-cv"><i>SQL</i><em></em><em></em><em></em></span><span class="pv-tg">%s%s</span><b>Data Analysis with SQL</b><p>Write SQL to answer real business questions, from first query to a finished analysis.</p><span class="pv-sk">%s</span></div></section>''' % (
    tag('Course', 'line'), tag('Hybrid', 'line'), ''.join('<i>%s</i>' % x for x in SKILLS4)))

# ---------- CR-STU-011 Audience & prerequisites
def prq(skill, lvl, req):
    return ('<div class="pq-r"><span class="pq-s">%s</span>%s<div class="pq-q">%s</div><button type="button" class="ds-x sm" aria-label="Remove %s">%s</button></div>' %
            (skill, sel(lvl, 'Minimum proficiency for ' + skill), W.seg(['Required', 'Recommended'], 0 if req else 1), skill, ic('x', 15, 2)))
P('audience', 'audience', page_head('Design', 'Audience & Prerequisites', 'Who is this for, and what should they already know? Credalio stores this in a form it can match against learners.'),
'''<section class="ds-card fc ob-in2">
<div class="fg">
%s
%s
</div>
</section>
<section class="ds-card fc ob-in3">
<div class="fc-h"><div><h2>What should learners already know?</h2><p>Each prerequisite gets a minimum proficiency and whether it’s required.</p></div></div>
<div class="pq">
<div class="pq-r pq-hd"><span>Prerequisite</span><span>Minimum proficiency</span><span>Requirement</span><span></span></div>
%s%s
</div>
<div class="pq-add"><input class="ds-in" placeholder="Add prerequisite" aria-label="Add prerequisite"><button type="button" class="ds-ghost">Add</button></div>
</section>
<section class="ds-card fc ob-in4">
<div class="fc-h"><div><h2>Age considerations%s</h2></div></div>
<div class="opt3">%s%s%s</div>
</section>''' % (
    field('Who is this for?', '<div class="chips">%s%s%s%s</div>' % (W.chip('Beginner', True), W.chip('Intermediate'), W.chip('Advanced'), W.chip('Professional')), 'Select all that apply'),
    field('Intended context', '<div class="chips">%s%s%s%s%s</div>' % (W.chip('Career development', True), W.chip('Academic learning'), W.chip('Professional development', True), W.chip('Personal learning'), W.chip('Workplace training'))),
    prq('Excel', 'Foundation', True), prq('Statistics', 'Foundation', False),
    tip('This later helps validator assignment and risk classification.'),
    W.opt('<span class="o-t"><b>General audience</b></span>', True, 'age'),
    W.opt('<span class="o-t"><b>Adults only (18+)</b></span>', False, 'age'),
    W.opt('<span class="o-t"><b>Restricted / special audience</b></span>', False, 'age')),
acts('STU-012.dc.html', back_href='STU-010.dc.html'),
nova_rail('Tell me who it’s for and I’ll suggest prerequisites.', nchip('Suggest prerequisites')) +
'<section class="ds-card rx"><span class="rx-k">Learning Intelligence Profile:</span><ul class="lp">%s</ul></section>' % ''.join(
    '<li><span class="lp-i">%s</span><span><b>%s</b><em>%s · %s</em></span></li>' % (ck(10), s, l, r) for s, l, r in [('Excel', 'Foundation', 'Required'), ('Statistics', 'Foundation', 'Recommended')]))

# ---------- CR-STU-012 / 012b Career
ROLEMAP = '''<section class="ds-card rx rm"><div class="rm-v" aria-hidden="true"><span class="rm-o"></span><span class="rm-o b"></span>
<span class="rm-c">%s<b>Data Analyst</b><em>Entry Level</em></span><span class="rm-s s1"><b>BI Analyst</b></span><span class="rm-s s2"><b>Operations Analyst</b></span></div></section>''' % ic('target', 18, 2)
def career(cert):
    goals = ['Build a skill', 'Prepare for a career role', 'Change career', 'Advance in an existing career', 'Prepare for certification', 'Academic progression']
    on = {0, 1, 2} | ({4} if cert else set())
    certs = ''
    if cert:
        certs = '''<section class="ds-card fc ob-in4">
<div class="fc-h"><div><h2>Which certification does this course prepare for?%s</h2><p>Shown as “Prepares for” on your course page. The certification’s owner must approve the link.</p></div></div>
<div class="ce">
<div class="ce-r"><span class="ce-i">%s</span><span class="ce-t"><b>Professional Data Analyst Certification</b><span>ABC Institute · designed by Ada Ononuju</span></span><span class="ce-m">%s<span class="ce-s nl">Not linked</span></span><button type="button" class="ds-ghost sm">Link</button></div>
<div class="ce-r"><span class="ce-i">%s</span><span class="ce-t"><b>Certified BI Practitioner</b><span>Data Professionals Association</span></span><span class="ce-m">%s<span class="ce-s">%s<span>Requested · waiting for the certification owner to approve</span></span></span><button type="button" class="ds-link ce-x">Remove</button></div>
<div class="ce-r"><span class="ce-i">%s</span><span class="ce-t"><b>Associate Data Engineer</b><span>Acme Analytics Ltd</span></span><span class="ce-m">%s<span class="ce-s nl">Not linked</span></span><button type="button" class="ds-ghost sm">Request link</button></div>
</div>
</section>''' % (tip('Completing this course never awards the certification. Learners still register for it and pass its assessments. The course keeps its own completion certificate.'),
                 ic('badge', 18), tag('In validation', 'blue'), ic('badge', 18), tag('Validated', 'green'), ICON(EXTRA['clock'], 14, 2), ic('badge', 18), tag('Validated', 'green'))
    rel = (W.opt('<span class="o-t"><b>Core Skill</b><span>Essential to performing the role day to day.</span></span>', True, 'rel%d' % cert) +
           W.opt('<span class="o-t"><b>Supporting Skill</b><span>Helps in the role, but isn’t central to it.</span></span>', False, 'rel%d' % cert) +
           W.opt('<span class="o-t"><b>Specialized Skill</b><span>A niche or advanced capability within the role.</span></span>', False, 'rel%d' % cert))
    main = '''<section class="ds-card fc ob-in2">
<div class="fg">
%s
<div class="fg fg2">%s%s</div>
%s
%s
</div>
</section>%s''' % (
        field('This course primarily helps learners:', '<div class="chips">%s</div>' % ''.join(W.chip(g, i in on) for i, g in enumerate(goals)), 'Select all that apply'),
        field('Primary role', '<input class="ds-in" aria-label="Primary role">'),
        field('Related roles', '<div class="rr"><input class="ds-in" placeholder="Add related role" aria-label="Add related role"><button type="button" class="ds-ghost">Add</button></div>'),
        field('Career stage', W.seg(['Entry Level', 'Early Career', 'Mid Career', 'Advanced'], 0), 'Where in a career is this course most useful?'),
        field('Relevance to the role%s' % tip('Feeds the Become Engine: learners working towards the roles you set can find this course on their path. It never affects validation outcomes on its own.'), '<div class="opt3 v">%s</div>' % rel),
        certs)
    rail = (nova_rail('From your outcomes and skills, this course fits an entry-level Data Analyst path, with BI Analyst and Operations Analyst as related roles.',
                      '<button type="button" class="ds-btn sm wh2">Use suggestion</button>' + nchip('Suggest roles')) + ROLEMAP + flow(F_CAREER, 0))
    return (page_head('Design', 'Career & Progression Relevance', 'Where can this learning take someone? This connects your course to learners’ goals in the Become Engine.'),
            main, acts('STU-013.dc.html', back_href='STU-011.dc.html'), rail)
P('career', 'career', *career(False))
P('careercert', 'career', *career(True))

# ---------- CR-STU-013 Skills & proficiency
LV = ['Beginner', 'Foundation', 'Intermediate', 'Advanced', 'Expert']
def track(a, b):
    if a is None or b is None:
        return '<span class="tk tk-x">%s<span>Set both levels</span></span>' % ic('warn', 14, 2)
    dots = ''.join('<i class="%s"></i>' % ('on' if a <= i <= b else '') for i in range(5))
    return '<span class="tkw"><span class="tk" style="--a: %d; --b: %d" aria-hidden="true"><span class="tk-l"></span>%s</span><span class="tk-t">%s → %s</span></span>' % (a, b, dots, LV[a], LV[b])
def skr(skill, a, b):
    return ('<div class="sk-r"><span class="sk-s">%s</span>%s%s%s<button type="button" class="ds-x sm" aria-label="Remove %s">%s</button></div>' %
            (skill, sel(LV[a] if a is not None else 'Select level', 'Starting proficiency for ' + skill), sel(LV[b] if b is not None else 'Select level', 'Expected proficiency for ' + skill), track(a, b), skill, ic('x', 15, 2)))
P('skills', 'career', page_head('Design', 'Skills & Proficiency', 'What skills will learners develop, and how far will they progress? Starting proficiency should match your prerequisites.'),
'''<section class="ds-card fc ob-in2">
<div class="sk">
<div class="sk-r sk-hd"><span>Skill</span><span>Starting proficiency</span><span>Expected proficiency</span><span>Progression</span><span></span></div>
%s%s%s%s
</div>
<div class="pq-add"><input class="ds-in" placeholder="Add skill" aria-label="Add skill"><button type="button" class="ds-ghost">Add</button></div>
</section>''' % (skr('SQL', 0, 2), skr('Data Analysis', 1, 2), skr('Data Cleaning', 0, 2), skr('Relational Databases', None, None)),
acts('STU-014.dc.html', back_href='STU-012.dc.html'),
nova_rail('I identified 6 skills from your proposed curriculum. 4 are already listed. Add the others?',
          '<button type="button" class="ds-chip sm">%s<span>Joins</span></button><button type="button" class="ds-chip sm">%s<span>Aggregation</span></button><button type="button" class="ds-link sm">Dismiss</button>' % (ic('plus', 13, 2.4), ic('plus', 13, 2.4)) + nchip('Suggest proficiency levels')) +
'<section class="ds-card rx"><ol class="ld">%s</ol><p class="rx-p">Levels, lowest to highest: Beginner, Foundation, Intermediate, Advanced, Expert. Nova suggests; you confirm. Credalio checks these against your assessments during validation.</p></section>' % ''.join(
    '<li style="--i: %d"><i></i><span>%s</span></li>' % (i, l) for i, l in enumerate(LV)) + flow(F_CAREER, 1))

# ---------- CR-STU-014 Outcomes
def lo(n, text, warn=False):
    w = ''
    if warn:
        w = '<div class="lo-w">%s<p>“Understand SQL” may be difficult to assess. Consider: <b>Write SQL queries to retrieve, filter and aggregate structured data.</b></p><button type="button" class="ds-ghost sm">Use suggestion</button></div>' % nova_av('sm')
    return ('<div class="lo-r%s"><span class="lo-n">%d</span><div class="lo-b"><div class="lo-h"><span class="lo-k">Learning outcome %d</span><button type="button" class="ds-x sm" aria-label="Remove outcome %d">%s</button></div><textarea class="ds-in lo-in" rows="2" aria-label="Outcome %d">%s</textarea>%s</div></div>' %
            (' warn' if warn else '', n, n, n, ic('x', 15, 2), n, text, w))
P('outcomes', 'outcomes', page_head('Design', 'Learning Outcomes', 'What will learners be able to do by the end? Use observable verbs. You’ll connect each outcome to skills and evidence next.'),
'''<section class="ds-card fc ob-in2">
<div class="lo">%s%s%s%s</div>
<div class="lo-f"><button type="button" class="ds-ghost">%s<span>Add Outcome</span></button>%s</div>
</section>''' % (
    lo(1, 'Write SQL queries to retrieve and filter structured business data.'), lo(2, 'Combine multiple relational tables using joins.'),
    lo(3, 'Analyse business datasets and communicate findings.'), lo(4, 'Understand SQL', True), ic('plus', 16, 2.2), nchip('Generate from course goal')),
acts('STU-015.dc.html', back_href='STU-013.dc.html'),
nova_rail('“Understand SQL” may be hard to assess. I’ve suggested a measurable version on the card.', nchip('Check my outcomes')) + flow(F_OUT, 0))

# ---------- CR-STU-015 Outcome → skill map
SK = ['SQL · Intermediate', 'Data Analysis · Intermediate', 'Data Cleaning · Intermediate', 'Relational Databases']
LOS = [('Outcome 1', 'Write SQL queries to retrieve and filter structured business data.', [1, 1, 0, 0]),
       ('Outcome 2', 'Combine multiple relational tables using joins.', [1, 0, 0, 1]),
       ('Outcome 3', 'Analyse business datasets and communicate findings.', [0, 1, 1, 0]),
       ('Outcome 4', 'Understand SQL', [0, 0, 0, 0])]
def mx_cell(on, lo_, sk):
    k = W.new(bool(on))
    return '<button type="button" class="mx-c {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}" aria-label="%s develops %s"><span class="mx-ck">%s</span><span class="mx-l">%s</span></button>' % (k, k, k, lo_, sk, ck(13), sk.split(' · ')[0])
def mx_rows():
    h = ''
    for code, text, cells in LOS:
        warn = not any(cells)
        h += '<div class="mx-r%s"><span class="mx-o"><em>%s</em><span>%s</span>%s</span>%s</div>' % (
            ' warn' if warn else '', code, text, tag('No skills mapped to this outcome yet', 'amber') if warn else '', ''.join(mx_cell(c, code, SK[i]) for i, c in enumerate(cells)))
    return h
COV = [('SQL', 'Target: Intermediate', 'Developed by LO1, LO2', 2), ('Data Analysis', 'Target: Intermediate', 'Developed by LO1, LO3', 2),
       ('Data Cleaning', 'Target: Intermediate', 'Developed by LO3', 1), ('Relational Databases', 'Target: not set', 'Developed by LO2', 1)]
P('skillmap', 'outcomes', page_head('Design', 'Outcome → Skill Mapping', 'Connect each learning outcome to the skills it develops. This links your outcomes to the Learning Intelligence Profile.'),
'''<section class="ds-card fc ob-in2">
<div class="mx-w"><div class="mx" style="--n: 4">
<div class="mx-r mx-hd"><span>Skills developed</span>%s</div>
%s
</div></div>
</section>''' % (''.join('<span>%s</span>' % s for s in SK), mx_rows()),
acts('STU-016.dc.html', back_href='STU-014.dc.html'),
nova_rail('Every outcome should develop at least one skill.', nchip('Map skills for me')) +
'<section class="ds-card rx"><span class="rx-k">Skill coverage</span><ul class="cvl">%s</ul></section>' % ''.join(
    '<li class="%s"><span class="cvl-h"><b>%s</b><em>%s</em></span><span class="cvl-b">%s</span><span class="cvl-d">%s</span></li>' % (
        'amb' if 'not set' in t else '', n, t, ''.join('<i class="%s"></i>' % ('on' if j < c else '') for j in range(4)), d) for n, t, d, c in COV) + flow(F_OUT, 1))

# ---------- CR-STU-016 Evidence
EV = ['Practical exercise', 'Project', 'Quiz', 'Exam', 'Live demonstration', 'Portfolio artifact']
def ev_r(code, text, skills, on):
    sk = ''.join(tag(s, 'line') for s in skills) if skills else '<span class="ev-none">none mapped</span>'
    warn = '' if on else '<span class="ev-w">%s<span>No evidence selected yet</span></span>' % ic('warn', 14, 2)
    return ('<div class="ev-r%s"><div class="ev-o"><em>%s</em><b>%s</b><span class="ev-sk"><span class="ev-sl">Skills:</span>%s</span></div><div class="ev-q"><span class="ev-ql">How will learners prove this outcome?</span><div class="chips">%s</div>%s</div></div>' %
            ('' if on else ' warn', code, text, sk, ''.join(W.chip(e, i in on, cls='sm') for i, e in enumerate(EV)), warn))
CHAIN = [('LO1', [1, 1, 1, 1]), ('LO2', [1, 1, 1, 0]), ('LO3', [1, 1, 0, 1]), ('LO4', [1, 0, 0, 0])]
def chain():
    cols = ['Taught', 'Practised', 'Assessed', 'Proof']
    h = '<div class="ch-r ch-hd"><span></span>%s</div>' % ''.join('<span>%s</span>' % c for c in cols)
    for code, cells in CHAIN:
        h += '<div class="ch-r"><span class="ch-o">%s</span>%s</div>' % (code, ''.join(
            '<span class="ch-c %s" style="--i: %d">%s</span>' % ('ok' if c else 'no', i, ck(11) if c else '<i></i>') for i, c in enumerate(cells)))
    return h
P('evidence', 'outcomes', page_head('Design', 'Outcome → Evidence Mapping', 'How will learners prove each outcome? This completes the chain: Outcome → Skill → Evidence.'),
'''<section class="ds-card fc ob-in2">
<div class="ev">%s%s%s%s</div>
</section>''' % (
    ev_r('Outcome 1', 'Write SQL queries to retrieve and filter structured business data.', ['SQL · Intermediate', 'Data Analysis · Intermediate'], {0, 2}),
    ev_r('Outcome 2', 'Combine multiple relational tables using joins.', ['SQL · Intermediate', 'Relational Databases'], {0, 3}),
    ev_r('Outcome 3', 'Analyse business datasets and communicate findings.', ['Data Analysis · Intermediate', 'Data Cleaning · Intermediate'], {1, 5}),
    ev_r('Outcome 4', 'Understand SQL', [], set())),
acts('STU-017.dc.html', back_href='STU-015.dc.html'),
nova_rail('Choose how learners will prove each outcome.', nchip('Suggest evidence')) +
'<section class="ds-card rx"><span class="rx-k">Outcome → Learning → Practice → Assessment → Proof</span><div class="ch">%s</div></section>' % chain() + flow(F_OUT, 2))

# ---------- CR-STU-017 Course design
P('design', 'design', page_head('Design', 'Course Design', 'Declare how the course will assess and award. Credalio later checks the declared level against the actual content.'),
'''<section class="ds-card fc ob-in2">
<div class="fc-h"><div><h2>Assessment strategy</h2><p>Will this course include:</p></div></div>
<div class="as-g">%s</div>
</section>
<section class="ds-card fc ob-in3">
<div class="fc-h"><div><h2>What does successful completion award?</h2></div></div>
<div class="opt2 aw">%s%s</div>
</section>''' % (
    ''.join(W.opt('<span class="as-i">%s</span><span class="o-t"><b>%s</b></span>' % (ic(i, 18), t), on, cls='as')
            for i, t, on in [('check', 'Knowledge Checks', True), ('quiz', 'Quizzes', True), ('file', 'Exam', False),
                             ('edit', 'Assignments', True), ('project', 'Projects', True), ('target', 'Practical Activities', True)]),
    W.opt('<span class="aw-v cert" aria-hidden="true">%s</span><span class="o-t"><b>Course Completion Certificate</b></span>' % ic('cert2', 26, 1.7), True, cls='as awc'),
    W.opt('<span class="aw-v badge" aria-hidden="true">%s</span><span class="o-t"><b>Skill badge (subject to policy)</b></span>' % ic('badge', 26, 1.7), False, cls='as awc')),
acts('STU-018.dc.html', back_href='STU-016.dc.html'),
nova_rail('I compare your estimate with detected learning time as you build.') +
'<section class="ds-card rx inf"><span class="inf-i">%s</span><p>Difficulty tier is set per lesson. Creators pick a tier in each lesson editor (video, text, live class, applied learning, assessment). It feeds that item’s DLP estimate.</p><a class="ds-link sm" href="STU-020.dc.html">See the Curriculum Builder%s</a></section>' % (
    ic('layers', 18, 2), ic('arrowr', 14, 2.2)) + flow(F_LD, 0))

# ---------- CR-STU-018 Learning effort
EF = [('Structured learning', 'Videos, reading, interactive lessons', '10', '2h 15m', 135), ('Practice', 'Exercises, assignments, discussions', '6', '1h 40m', 100),
      ('Projects', 'Projects and portfolio work', '5', '2h', 120), ('Assessments', 'Knowledge checks, quizzes, exams', '3', '1h 10m', 70), ('Live instruction', 'Live sessions and clinics', '2', '1h', 60)]
P('effort', 'design', page_head('Design', 'Learning Effort', 'How much time will learners invest? Estimate now. As you build, Credalio calculates each figure from your actual content.'),
'''<section class="ds-card fc ob-in2">
<div class="ef">
<div class="ef-r ef-hd"><span>Type of effort</span><span>Your estimate (hours)</span><span>Detected from your build</span><span>Source</span></div>
%s
<div class="ef-r ef-tot"><span><b>Total</b></span><span><b>26 hours</b></span><span><b>8h 5m built so far</b></span><span></span></div>
</div>
</section>''' % (
    ''.join('<div class="ef-r"><span class="ef-t"><b>%s</b><span>%s</span></span><span class="ef-in"><input class="ds-in" value="%s" aria-label="Estimated hours for %s"></span><span class="ef-d"><b>%s</b><span class="ef-b"><i style="width: %d%%"></i></span></span><span class="ef-s">%s</span></div>' % (
        t, d, v, t, b, min(100, round(100 * m / (int(v) * 60))), tag('Estimate')) for t, d, v, b, m in EF)),
acts('STU-019.dc.html', back_href='STU-017.dc.html'),
nova_rail('Detected time grows as you build.') +
'''<section class="ds-card rx ls"><span class="rx-k">Learners will see</span><b class="ls-n">24–30 hours</b><p class="rx-p">Estimated effort, shown on the course page. Updated automatically as detected figures replace estimates.</p>
<div class="ls-r">%s<span><b>8h 5m</b><em>of 26 hours</em></span></div><p class="rx-p">You’ve built 8h 5m of an estimated 26 hours. Detected figures replace your estimates as the curriculum fills in.</p></section>''' % ring(31, 84, 12) + flow(F_LD, 1))

# ---------- CR-STU-019 Design summary
SUM = [('Target', 'No career role yet', 'pr', 'STU-012.dc.html'), ('Audience', 'Beginner · with Excel (foundation), Statistics (foundation)', 'ok', 'STU-011.dc.html'),
       ('Skills', '4: SQL, Data Analysis, Data Cleaning, Relational Databases', 'pr', 'STU-013.dc.html'), ('Outcomes', '4 learning outcomes', 'pr', 'STU-014.dc.html'),
       ('Evidence requirements', '4: Quiz, Practical exercise, Project, Portfolio artifact', 'pr', 'STU-016.dc.html'), ('Intended level', 'Intermediate', 'ok', 'STU-013.dc.html'),
       ('Estimated effort', '24–30 hours', 'ok', 'STU-018.dc.html')]
SIG = [('Industry', 1), ('Domain', 1), ('Topic', 1), ('Career role', 0), ('Skills', 1), ('Prerequisites', 1), ('Proficiency levels', 0),
       ('Outcomes', 1), ('Evidence', 0), ('Effort', 1), ('Modality', 1), ('Credential', 1), ('Progression', 0)]
P('summary', 'design', page_head('Design', 'Your Learning Design', 'Check the design before you build. Everything stays editable.'),
'''<section class="ds-card fc sm-c ob-in2">
<div class="sm">%s</div>
</section>''' % (
    ''.join('<a class="sm-r %s" href="%s">%s<span class="sm-l">%s</span><span class="sm-v">%s</span><span class="sm-e">Edit</span></a>' % (s, h, STATUS[s], l, v) for l, v, s, h in SUM)),
acts('STU-020.dc.html', 'Build Curriculum', back_href='STU-018.dc.html', note='You can start building now and come back to anything flagged.'),
nova_rail('Almost there. 4 items need attention: target, skills, outcomes, evidence requirements. You can still start building.') +
'''<section class="ds-card rx lip2"><span class="rx-k">Learning Intelligence Profile%s</span><div class="lip-r">%s<span><b>9</b><em>of 13 captured</em></span></div><div class="sg">%s</div></section>''' % (
    tip('You’ll confirm or correct the full profile in Prepare before validation.', 'r'), ring(69, 96, 12),
    ''.join('<span class="sg-i%s">%s%s</span>' % ('' if on else ' off', ck(11) if on else '<i></i>', n) for n, on in SIG)) + flow(F_LD, 2))

MST = [('Basics', 'STU-010.dc.html', 'basics', 'ok'), ('Audience & Prerequisites', 'STU-011.dc.html', 'audience', 'ok'), ('Career & Skills', 'STU-012.dc.html', 'career', 'pr'),
       ('Learning Outcomes', 'STU-014.dc.html', 'outcomes', 'pr'), ('Learning Design', 'STU-017.dc.html', 'design', None)]
def mstep(nav):
    if nav == 'home':
        return ''
    return '<nav class="mst" aria-label="Design sections">%s</nav>' % ''.join(
        '<a href="%s" class="mst-i%s"%s>%s<span>%s</span></a>' % (h, ' on' if k == nav else '', ' aria-current="page"' if k == nav else '', STATUS.get(st, '<span class="st to"></span>') if st else '<span class="st to"></span>', l)
        for l, h, k, st in MST)

STUDIO_CSS = r'''.hm-strip{display:flex;border-radius:16px;background:#FFFFFF;border:1.5px solid #E6EAF3}
.hm-strip > span{display:flex;flex-direction:column;gap:4px;padding:10px 18px}
.hm-strip > span + span{border-left:1.5px solid #EEF1F7}
.hm-strip em{display:flex;align-items:center;font-style:normal;font-size:12px;color:#5B6582}
.hm-strip b{font-size:17px;font-weight:600}
.hm-next{margin-top:24px;padding:34px 40px;border-radius:24px;display:flex;align-items:center;justify-content:space-between;gap:40px;position:relative;overflow:hidden;isolation:isolate;color:#FFFFFF;background:linear-gradient(125deg,#0B1433 0%,#102A7A 62%,#1652F0 130%);box-shadow:0 30px 60px -40px rgba(11,20,51,.8)}
.hm-next::before{content:'';position:absolute;z-index:-1;right:-120px;top:-160px;width:460px;height:460px;border-radius:50%;background:radial-gradient(circle,rgba(92,134,255,.45),rgba(92,134,255,0) 65%)}
.hm-next::after{content:'';position:absolute;z-index:-1;inset:0;background-image:radial-gradient(rgba(255,255,255,.09) 1px,transparent 1px);background-size:18px 18px;-webkit-mask-image:linear-gradient(90deg,transparent 30%,#000);mask-image:linear-gradient(90deg,transparent 30%,#000)}
.hm-next .pg-e{color:#9DB8F7}
.hm-nl{position:relative;min-width:0}
.hm-next h2{margin:0;max-width:600px;font-size:28px;line-height:1.2;font-weight:600;letter-spacing:-0.025em}
.hm-next p{margin:10px 0 0 0;font-size:15px;line-height:1.55;color:rgba(255,255,255,.72)}
.hm-seg{margin-top:22px;display:flex;align-items:center;gap:5px;max-width:520px}
.hm-seg i{flex:1;height:6px;border-radius:6px;background:rgba(255,255,255,.16)}
.hm-seg i.dn{background:#FFFFFF}
.hm-seg i.nx{background:#5C86FF;box-shadow:0 0 0 0 rgba(92,134,255,.6);animation:hmPulse 1.8s ease-out infinite}
@keyframes hmPulse{0%{box-shadow:0 0 0 0 rgba(92,134,255,.6)}100%{box-shadow:0 0 0 6px rgba(92,134,255,0)}}
.hm-sl{flex-shrink:0;margin-left:10px;font-size:13px;color:rgba(255,255,255,.72)}
.hm-na{margin-top:26px;display:flex;align-items:center;gap:20px}
.ds-btn.wh{background:#FFFFFF;color:#0B1433;box-shadow:0 12px 28px -12px rgba(0,0,0,.5)}
.ds-btn.wh:hover{background:#F5F8FF;color:#0B1433}
.ds-btn.wh .ob-arrow{background:#1652F0;color:#FFFFFF}
.hm-pk{font-size:13.5px;color:rgba(255,255,255,.62)}
.hm-rc{position:relative;flex-shrink:0;display:flex;flex-direction:column;align-items:center;gap:12px;padding:18px 22px 16px 22px;border-radius:20px;background:rgba(255,255,255,.06);box-shadow:inset 0 0 0 1px rgba(255,255,255,.1)}
.hm-ring{position:relative;flex-shrink:0;width:132px;height:132px}
.hm-ring span{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}
.hm-ring b{font-size:30px;font-weight:600;letter-spacing:-0.02em}
.hm-ring em{font-style:normal;font-size:12px;color:rgba(255,255,255,.7)}
.hm-rl{display:inline-flex;align-items:center;gap:2px}
.hm-rl .ds-link{font-size:13.5px;color:#FFFFFF}
.hm-rl .tip{margin:0 4px 0 0;color:rgba(255,255,255,.6)}
@media (prefers-reduced-motion: reduce){.hm-seg i.nx{animation:none}}
.hm-list,.hm-det{margin-top:16px;padding:8px 10px 10px 10px}
.hm-h{display:flex;align-items:center;margin:14px 14px 6px 14px;font-size:16px;font-weight:600}
.hm-r{display:flex;align-items:center;gap:14px;min-height:68px;padding:10px 14px;border-radius:14px;color:#0B1433;text-decoration:none}
.hm-r + .hm-r{box-shadow:0 -1.5px 0 #F0F2F8}
.hm-r:hover{background:#F7F9FD}
.hm-ri{width:40px;height:40px;flex-shrink:0;border-radius:12px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.hm-rt{flex:1;min-width:0;display:flex;flex-direction:column;gap:3px}
.hm-rt b{font-size:15px;font-weight:600}
.hm-m{font-size:13.5px;line-height:1.45;color:#5B6582}
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
.ce-s.nl{color:#5B6582}
.ce-x{border:0;background:none;font-family:inherit;cursor:pointer;font-size:14px}
.fc-h-r{justify-content:flex-end;margin-bottom:12px}
.fnote{margin:18px 0 0 0;font-size:13px;line-height:1.5;color:#5B6582}
.fl-f{display:flex;align-items:center;justify-content:space-between;gap:12px}
.fl-sub{font-size:13px;font-weight:500;color:#5B6582;margin-top:4px}
.lip{margin-top:18px;padding-top:16px;border-top:1.5px solid #F0F2F8;display:flex;flex-wrap:wrap;align-items:center;gap:8px}
.lip-l{font-size:13px;font-weight:500;color:#5B6582;margin-right:4px}
.lo-k{display:block;margin-bottom:6px;font-size:12px;font-weight:600;color:#8A93AD}
.tkw{display:flex;flex-direction:column;gap:4px}
.tk-t{font-size:12.5px;font-weight:500;color:#0F6B45}
.ev-sl{font-size:12.5px;color:#5B6582;margin-right:2px}
.ev-none{font-size:12.5px;color:#8A5A00}
.ev-q{display:flex;flex-direction:column;gap:8px}
.ev-ql{font-size:13px;font-weight:500;color:#3A4566}
.ev-w{display:inline-flex;align-items:center;gap:6px;font-size:13px;font-weight:500;color:#8A5A00}
.ev-w svg{color:#B76E00}
.ev-sk{align-items:center}
.hm-strip{align-items:center}
.hm-strip .ds-link{padding:0 18px;font-size:13.5px;border-left:1.5px solid #EEF1F7;align-self:stretch}
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
.ef-r{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(0,1fr) minmax(0,1fr) 110px;align-items:center;gap:16px;padding:12px 0;border-bottom:1.5px solid #F0F2F8}
.ef-hd{padding:0 0 8px 0;font-size:12.5px;font-weight:500;color:#8A93AD}
.ef-t{display:flex;flex-direction:column;gap:2px}
.ef-t b{font-size:15px;font-weight:600}
.ef-t span{font-size:13px;color:#5B6582}
.ef-in{position:relative;max-width:120px}
.ef-d{font-size:15px;font-weight:500;color:#0F6B45}
.ef-tot{border-bottom:0;padding-top:16px;font-size:15px}
.ef-sum{display:flex;align-items:center;justify-content:space-between;gap:32px}
.ef-l b{display:block;font-size:30px;font-weight:600;letter-spacing:-0.02em}
.ef-l p{margin:6px 0 0 0;font-size:14px;color:#5B6582}
.ef-p{flex:0 1 380px;display:flex;flex-direction:column;gap:10px;font-size:14px;color:#3A4566}
.ef-pb{height:8px;border-radius:8px;background:#EAF0FF;overflow:hidden}
.ef-pb i{display:block;height:100%;border-radius:8px;background:#1652F0}
.fc.sm-c{padding-top:14px;padding-bottom:14px}
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
.hm-next{margin-top:18px;padding:22px 18px;border-radius:20px;flex-direction:column-reverse;align-items:stretch;gap:18px}
.hm-next h2{font-size:21px}
.hm-next p{font-size:14px}
.hm-rc{flex-direction:row;justify-content:space-between;padding:10px 14px 10px 10px;border-radius:16px}
.hm-ring{width:72px;height:72px}
.hm-ring svg{width:72px;height:72px}
.hm-ring b{font-size:17px}
.hm-ring em{display:none}
.hm-seg{flex-wrap:wrap;gap:4px}
.hm-sl{flex-basis:100%;margin:6px 0 0 0}
.hm-na{flex-direction:column;align-items:stretch;gap:8px;margin-top:18px}
.hm-na .ds-btn{width:100%;justify-content:space-between}
.hm-pk{text-align:center}
.hm-list,.hm-det{padding:6px}
.hm-r{gap:12px;padding:10px;min-height:64px}
.hm-r .avs,.hm-go{display:none}
.hm-m{font-size:13px}
.hm-dg{grid-template-columns:repeat(2,minmax(0,1fr))}
.in-ai .ds-in{padding-right:14px}
.in-ai .nv-chip{position:static;transform:none;margin-top:8px}
.pq-r{grid-template-columns:minmax(0,1fr) 36px;gap:10px;padding:14px 0}
.pq-r .sel,.pq-r > div{grid-column:1}
.pq-r .ds-x{grid-row:1;grid-column:2}
.pq-hd{display:none}
.opt2,.opt3,.as-g{grid-template-columns:minmax(0,1fr)}
.ce-r{flex-wrap:wrap;padding:14px 0;gap:10px 12px}
.ce-r > .ds-tag,.ce-r > .ds-ghost,.ce-s,.ce-x{margin-left:52px}
.ce-s{flex-basis:calc(100% - 52px)}
.ce-t{flex:1 1 calc(100% - 54px)}
.ds-seg button{white-space:nowrap;padding:0 10px;font-size:13px}
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
.ef-r{grid-template-columns:minmax(0,1fr) 90px;gap:6px 10px}
.ef-s{grid-column:1}
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
.fc.sm-c{padding-top:6px;padding-bottom:6px}
}
'''

STUDIO_CSS += WK_CSS + r'''@media (max-width: 960px){
.as-g{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.ds-opt.as:not(.awc){flex-direction:column;align-items:flex-start;gap:10px;padding:14px 14px 16px 14px}
.ds-opt.as:not(.awc) .ds-opt-ck{position:absolute;top:12px;right:12px}
.ds-opt.as:not(.awc) .as-i{width:36px;height:36px;border-radius:11px}
.ds-opt.as:not(.awc) .o-t b{font-size:14.5px}
}
'''

def studio_body():
    blocks = []
    for key, nav, head, main, actions, rail in PAGES:
        body = '%s%s<div class="wk"><div class="wk-m">%s</div>%s<aside class="wk-r">%s</aside></div>' % (head, mstep(nav), main, actions.replace('class="ds-acts sb sv"', 'class="ds-acts sb sv wk-a"'), rail)
        blocks.append('<sc-if value="{{p_%s}}" hint-placeholder-val="{{ %s }}">\n%s\n</sc-if>' % (key, 'true' if key == 'home' else 'false', body))
    navs = []
    for nav in sorted(set(p[1] for p in PAGES)):
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
  componentDidMount() {
    try { var m = document.querySelector('.mst .on'); if (m && m.parentElement) { m.parentElement.scrollLeft = m.offsetLeft - 16; } } catch (e) {}
  }
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
}''' % (json.dumps({p[0]: p[1] for p in PAGES}), json.dumps(sorted(set(p[1] for p in PAGES))))

write('Studio.dc.html', doc('Course Studio · shared source', kit.KIT_CSS + '\n' + dash.DASH_CSS + BASE_CSS + CW_CSS + STUDIO_CSS, studio_body(), STUDIO_JS))

# ======================================================================= boards
BOARDS = [
    ('STU-001', 'Setup', {'step': 'type'}, 'CR-STU-001 · Choose learning experience'),
    ('STU-002', 'Setup', {'step': 'delivery'}, 'CR-STU-002 · Delivery type'),
    ('STU-003', 'Setup', {'step': 'review'}, 'CR-STU-003 · Setup review'),
    ('STU-004', 'Setup', {'step': 'how'}, 'CR-STU-004 · How will you create this course?'),
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
