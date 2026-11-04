# For Creators page (CRE-001..007). Built from LIVE shared pieces, never redrawn:
#   Landing.dc.html  -> creators door (ci-cr, Creator Studio window) as the hero, format cards (gc-*),
#                       step list (tx-step), final CTA band (fc-*)
#   Pricing.dc.html  -> step track (ko-path, Link 2 CR-WAL-OUT), unit card (pc-scale / pc-rate / pc-u)
#   Dashboard        -> Nova band (lr-nova nova-card), lr-card
# Usage: python3 cregen.py -> design/canvas3/project/Creators.dc.html
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from kit import AURORA_JS, KIT_CSS, NOVA, tip, btn, ck, credit
from shell import BASE_CSS, nav, FOOT
import dashgen, pricegen
DCSS = re.sub(r'^body\{[^}]*\}\n', '', dashgen.CSS)

P = os.path.join(HERE, '../../canvas3/project/')
OUT = P + 'Creators.dc.html'
L = open(P + 'Landing.dc.html').read()
style, block = pricegen.style, pricegen.block
ic = dashgen.ic
ARR = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'
AVN = '<span class="nv-av" aria-hidden="true"><img src="' + NOVA + '" alt=""></span>'
CKW = '<svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg>'
DONE = '<span class="ci-ck" style="background: #0F6B45">' + CKW + '</span>'
TODO = '<span class="ci-ck" style="background: #EAF0FF; border: 1.5px dashed #9DB8F7; box-sizing: border-box"></span>'
WARN = '<span class="ci-ck" style="background: #FFF4E5; color: #B54708; font-size: 11px; font-weight: 600">!</span>'

# ---------- hero: the Landing creators door, opened up ----------
DOOR = block(L, '<a class="ci-door ci-cr', 'a')
SEAL = re.search(r'<svg width="11" height="11" viewBox="0 0 100 100">.*?</svg>', DOOR, re.S).group(0)
FLOAT = re.search(r'<div class="ci-float".*?</div></div>|<div class="ci-float".*?£1,240 earned</span></span></div>', DOOR, re.S).group(0)
CDH = open(P + 'CourseDetail.dc.html').read()
GSEAL = re.search(r'<svg class="cd-seal".*?</svg>', CDH, re.S).group(0).replace('class="cd-seal"', 'class="cx-seal"').replace('cdGold', 'cxGold').replace('stroke="#FFFFFF" stroke-width="9"', 'stroke="#6B4E16" stroke-width="9"')
HERO = '''<section class="cx-top" aria-labelledby="cx-h">
<div class="ci-door ci-cr aur cx-hero">
<div class="ci-copy">
<h1 id="cx-h" class="ci-t">Share what you know.<br class="cx-br"> Earn from it.</h1>
<p class="ci-d">Create with AI, get validated, and reach learners across Credalio.</p>
<div class="cx-acts">''' + btn('Start creating', 'OnbWelcome.dc.html', 'ci-btn wh') + '''<a class="cx-wl" href="#cx-make">See what you can create</a></div>
</div>
<div class="cx-vis" aria-hidden="true">
<div class="cx-back">
<div class="cx-bk-h"><span>Creator Studio</span><span class="cx-bk-dots"><i></i><i></i><i></i></span></div>
<span class="cx-sk" style="width: 72%; height: 10px"></span><span class="cx-sk" style="width: 46%"></span>
<div class="cx-bk-r"><span class="ci-ck" style="background: #0F6B45">''' + CKW + '''</span><span class="cx-sk" style="width: 62%"></span></div>
<div class="cx-bk-r"><span class="ci-ck" style="background: #0F6B45">''' + CKW + '''</span><span class="cx-sk" style="width: 50%"></span></div>
<div class="cx-bk-r"><span class="ci-ck" style="background: #EAF0FF; border: 1.5px dashed #9DB8F7; box-sizing: border-box"></span><span class="cx-sk" style="width: 40%"></span><span class="cx-ai">AI draft</span></div>
</div>
<div class="cs-card cx-cc">
<div class="cs-th cx-cov"><svg class="cs-ico" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20V10M10 20V4M16 20v-7M2 20h20"></path></svg><span class="ds-tag glass">Course</span>''' + GSEAL + '''</div>
<div class="cs-cb">
<span class="cs-ct">Data Foundations: Spreadsheets to SQL</span>
<span class="cs-by"><span class="cs-cav">AO</span>Amara Okafor</span>
<span class="cs-meta"><span class="cs-star">★</span><b>4.8</b><span>(3.4k)</span><span class="cs-dot"></span><span>Beginner</span><span class="cs-dot"></span><span>12 hrs</span></span>
<div class="cx-lrn"><span class="cx-avs"><span class="ci-av" style="background: #DCE5FB; color: #1652F0">KB</span><span class="ci-av" style="background: #0B1433; color: #FFFFFF">JM</span><span class="ci-av" style="background: #E7F5EE; color: #0F6B45">SL</span></span><span><b>2,140</b> learners</span><span class="ds-tag blue cx-gt"><span class="cs-tdot" style="background: #C8961E"></span>Gold</span></div>
</div>
</div>
<div class="ci-float cx-nvf">''' + AVN + '''<span style="display: flex; flex-direction: column; gap: 1px"><span style="font-size: 11px; color: #8A93AD">Nova · just now</span><span style="font-size: 13.5px; font-weight: 600">Drafted 3 questions</span></span></div>
<div class="ci-float cx-ern"><div class="ci-bars cx-bars"><span style="height: 40%"></span><span style="height: 55%"></span><span style="height: 48%"></span><span style="height: 72%"></span><span style="height: 100%; background: #1652F0"></span></div><span style="display: flex; flex-direction: column; gap: 1px"><span style="font-size: 11px; color: #8A93AD">This month</span><span style="font-size: 16px; font-weight: 600">£1,240 <i class="cx-up">+18%</i></span></span></div>
</div>
</div>
</section>'''

# ---------- what you can create: Landing format cards, creator side ----------
GC = block(L, '<section aria-labelledby="gc-h"')
for a, b in [
    ('Choose how you want to grow', 'What you can create'),
    ('Not just courses. Learning shaped around the outcome you want.', 'Four ways to share what you know.'),
    ('Each format is built for a different kind of progress. Use one, or combine them into a single plan.', 'The same formats learners find on Credalio, built from your side of the studio.'),
    ('Not sure? Ask Nova, your AI Coach', 'Not sure where to start? Ask Nova'),
    ('<a class="ds-ghost nova-card gc-coach" href="#">', '<a class="ds-ghost nova-card gc-coach" href="OnbWelcome.dc.html">'),
    ('<section aria-labelledby="gc-h"', '<section id="cx-make" aria-labelledby="gc-h"'),
    ('padding: 120px 48px;', 'padding: 112px 48px;'),
    ('href="#" aria-label="Courses: browse courses"', 'href="OnbWelcome.dc.html" aria-label="Create a course"'),
    ('href="#" aria-label="Professional Certifications: see certifications"', 'href="OnbWelcome.dc.html" aria-label="Create a certification"'),
    ('href="#" aria-label="Career Paths: find your path"', 'href="OnbWelcome.dc.html" aria-label="Create a career path"'),
    ('href="#" aria-label="Learning Programs: explore programs"', 'href="OnbWelcome.dc.html" aria-label="Create a program"'),
    ('For learning one skill well', 'For one specific skill'),
    ('For proof employers trust', 'For proof of competence'),
    ('For moving into a new role', 'For a whole new role'),
    ('For learning with others', 'For learning over time'),
    ('Focused learning that builds one specific skill, at your own pace.', 'Lessons, activities, quizzes and projects built around one skill.'),
    ('Assessed programs that confirm you meet a professional standard.', 'Set the competencies, assessments and criteria someone must meet.'),
    ('A sequenced route of learning, practice and credentials toward a role.', 'Combine learning, practice and credentials into a route toward a role.'),
    ('Structured, cohort-based learning led by experts or institutions.', 'Run cohort-based or guided learning with schedules and instructors.'),
    ('Self-paced<span class="gc-sep" aria-hidden="true"></span>Short lessons', 'Create a course'),
    ('Assessed<span class="gc-sep" aria-hidden="true"></span>Verifiable', 'Create a certification'),
    ('Goal-led<span class="gc-sep" aria-hidden="true"></span>Step by step', 'Create a career path'),
    ('Cohort-based<span class="gc-sep" aria-hidden="true"></span>Expert-led', 'Create a program'),
]:
    assert GC.count(a) == 1, a
    GC = GC.replace(a, b)

# ---------- Creator Studio: Landing step list + studio window ----------
AREAS = [
    ('Shape it with AI', 'Nova drafts structure and questions. You decide.'),
    ('Build rich learning', 'Video, text, quizzes, projects and practical work.'),
    ('Create together', 'Invite co-creators and experts with clear roles.'),
    ('Check before you submit', 'Pre-check finds gaps before validators do.'),
]
STEPS = '<div class="tx-steps cx-steps" role="tablist" aria-label="Studio areas">' + ''.join(
    '<button type="button" role="tab" class="tx-step {{st.s%d.cls}}" aria-selected="{{st.s%d.sel}}" onClick="{{st.s%d.pick}}"><span class="tx-num">%d</span><span style="display: flex; flex-direction: column; gap: 2px"><span class="tx-st">%s</span><span class="tx-sd">%s</span></span></button>' % (i, i, i, i + 1, t, d)
    for i, (t, d) in enumerate(AREAS)) + '</div>'

def blk(icon, t, m):
    return '<div class="ci-row cx-blk"><span class="cx-bi">' + ic(icon, 16, 2) + '</span><span class="cx-bt">' + t + '</span><span class="cx-rm">' + m + '</span></div>'
I_VID = '<rect x="3" y="5" width="18" height="14" rx="3"></rect><path d="m10 9 5 3-5 3z"></path>'
I_TXT = '<path d="M5 6h14M5 11h14M5 16h9"></path>'
I_QZ = '<circle cx="12" cy="12" r="9"></circle><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6v.3M12 17h.01"></path>'
I_PRJ = '<path d="M4 7h16v12H4z"></path><path d="M9 7V5h6v2"></path>'
TYPES = ['Video', 'Text', 'Document', 'Interactive', 'Quiz', 'Knowledge check', 'Exam', 'Assignment', 'Project', 'Practical activity', 'Resources']

def person(ini, bg, fg, name, role, perm):
    return '<div class="ci-row cx-pp"><span class="ci-av" style="margin: 0; width: 32px; height: 32px; font-size: 11px; background: %s; color: %s">%s</span><span class="cx-pn"><b>%s</b><small>%s</small></span><span class="ds-tag">%s</span></div>' % (bg, fg, ini, name, perm, role)

WIN = '''<div class="ci-win cx-win" role="tabpanel" aria-label="{{st.name}}">
<div class="ci-wk"><span>Creator Studio · Data Foundations</span><span class="ds-tag {{st.tagCls}}">{{st.tag}}</span></div>
<sc-if value="{{st.a0}}" hint-placeholder-val="{{ true }}">
<ol class="cx-ol">
<li class="d"><i>''' + ck(11, 3.4) + '''</i><span><b>Working with spreadsheet data</b><small>Module 1 · 4 lessons</small></span></li>
<li class="d"><i>''' + ck(11, 3.4) + '''</i><span><b>Cleaning messy data</b><small>Module 2 · 4 lessons</small></span></li>
<li class="n"><i></i><span><b>Your first SQL queries</b><small>Module 3 · drafted with Nova</small></span></li>
</ol>
<div class="nova-card cx-sug">''' + AVN + '''<div><p>{{st.sug}}</p><div class="cx-sa"><button type="button" class="ds-ghost sm" onClick="{{st.accept}}">{{st.acceptLabel}}</button><button type="button" class="ds-link" onClick="{{st.skip}}">Not now</button></div></div></div>
</sc-if>
<sc-if value="{{st.a1}}" hint-placeholder-val="{{ false }}">
<span class="cx-wt">Lesson 2.3 · Removing duplicates</span>
''' + blk(I_VID, 'Video', '6 min') + blk(I_TXT, 'Text', 'Why duplicates happen') + blk(I_QZ, 'Knowledge check', '3 questions') + blk(I_PRJ, 'Practical activity', 'Clean a sales sheet') + '''
<span class="cx-add">Add a block</span>
<div class="cx-types">''' + ''.join('<span class="ds-tag">%s</span>' % t for t in TYPES) + '''</div>
</sc-if>
<sc-if value="{{st.a2}}" hint-placeholder-val="{{ false }}">
<span class="cx-wt">People on this course</span>
''' + person('AO', '#1652F0', '#FFFFFF', 'You', 'Lead', 'Full control') + person('PS', '#DCE5FB', '#1652F0', 'Priya Shah', 'Co-creator', 'Edits content · shares revenue') + person('TR', '#0B1433', '#FFFFFF', 'Tom Reed', 'Co-teacher', 'Runs live sessions · sees learners') + person('LO', '#E7F5EE', '#0F6B45', 'Dr Lena Ortiz', 'Subject expert', 'Reviews and comments') + '''
<div class="cx-wf"><span class="cx-add">Everyone gets only the access their role needs.</span><span class="ds-ghost sm">Invite</span></div>
</sc-if>
<sc-if value="{{st.a3}}" hint-placeholder-val="{{ false }}">
<span class="cx-wt">Pre-check</span>
<div class="ci-row">''' + DONE + '''Objectives for every module</div>
<div class="ci-row">''' + DONE + '''Assessments match the objectives</div>
<div class="ci-row">''' + DONE + '''Captions on every video</div>
<div class="ci-row cx-amb">''' + WARN + '''Module 3 needs a knowledge check<span class="cx-rm" style="color: #B54708">Fix</span></div>
<div class="cx-wf"><span class="cx-bar"><i style="width: 75%"></i></span><span class="cx-add">3 of 4 ready</span><span class="cx-sub">Submit for validation</span></div>
</sc-if>
</div>'''

STUDIO = '''<section class="pc-sec cx-sec" aria-labelledby="cx-st">
<div class="cx-studio">
<div class="cx-sl">
<span class="pc-k">Creator Studio</span>
<h2 id="cx-st" class="pc-h2">Everything you need to build great learning.</h2>
''' + STEPS + '''
</div>
''' + WIN + '''
</div>
</section>'''

# ---------- validation: Link 2 step track ----------
VSTEPS = [('Pre-check', 'Fix gaps before anyone else sees them.'), ('Submit', 'The cost is shown before anything is charged.'), ('Expert review', 'Independent validators check content, design and assessment.'), ('Resolve findings', 'Answer questions and update your work in the Studio.'), ('Validated', 'Your work earns the seal and a public record.'), ('Publish', 'Learners find it across Credalio.')]
VAL = '''<section class="pc-sec cx-sec" aria-labelledby="cx-va">
<div class="pc-sh cx-vh"><div><span class="pc-k">Validation</span><h2 id="cx-va" class="pc-h2">Build it. Then prove the quality behind it.</h2><p class="pc-p">Independent experts review your work. Validated learning carries the Credalio seal, linked to a public Validation Record.</p></div></div>
<ol class="ko-path cx-path">''' + ''.join('<li%s><span class="ko-dot">%s</span><span><b>%s</b><span>%s</span></span></li>' % (' class="cx-ok"' if i == 4 else '', SEAL.replace('width="11" height="11"', 'width="28" height="28"') if i == 4 else str(i + 1), t, d) for i, (t, d) in enumerate(VSTEPS)) + '''</ol>
<div class="cx-vb"><a class="ds-ghost" href="Validation.dc.html">How validation works''' + ARR.replace('currentColor', '#1652F0').replace('18', '16') + '''</a></div>
</section>'''

# ---------- earnings + creator services ----------
WAYS = [('wallet', 'Marketplace sales', 'Earn when learners buy your eligible learning.', ''),
        ('prog', 'Organisations', 'Offer your learning to institutions and teams, where eligible.', ''),
        ('send', 'Referrals', 'Introduce learners to your learning, or other eligible learning.', ''),
        ('reward', 'Creator rewards', 'Take part in Credalio’s creator reward economy.', 'Open to eligible creators, based on qualified contribution and platform rules.')]
EARN = '''<section class="pc-sec cx-sec" aria-label="Earnings and creator services">
<div class="cx-ec">
<div class="ds-card cx-earn">
<div class="cx-eh"><div><span class="pc-k">Creator economics</span><h2 class="pc-h2">Build knowledge. Create value.</h2></div>
<div class="ci-float cx-ef">''' + re.search(r'<div class="ci-bars">.*?</div>', FLOAT, re.S).group(0) + '''<span style="display: flex; flex-direction: column; gap: 1px"><span style="font-size: 11px; color: #8A93AD">This month</span><span style="font-size: 15px; font-weight: 600">£1,240 earned</span></span></div></div>
<div class="pc-units">''' + ''.join('<div class="pc-u"><span class="cx-ui">' + ic(dashgen.I[k], 20) + '</span><div><b>' + t + (tip(x, 'r') if x else '') + '</b><small>' + d + '</small></div></div>' for k, t, d, x in WAYS) + '''</div>
<a class="ds-link" href="#">How creator earnings work''' + dashgen.ARR_S + '''</a>
</div>
<div class="pc-scale cx-svc">
<span class="pc-k">Creator services</span>
<h2 class="pc-h2">No monthly creator subscription.</h2>
<p class="pc-p">Add Credits only when you need a paid service, like validation or some AI tools.</p>
<span class="pc-rate">$1 <span>=</span> ''' + credit(True) + '''10 Credits''' + tip('Creator Service Credits are your creator wallet. They are separate from learner DLP.', 'r') + '''</span>
<ul class="cx-ticks">
<li><i>''' + ck(11, 3.4) + '''</i>Pay only for the services you use</li>
<li><i>''' + ck(11, 3.4) + '''</i>See the cost before you’re charged</li>
<li><i>''' + ck(11, 3.4) + '''</i>Estimates live in your creator dashboard</li>
</ul>
</div>
</div>
</section>'''

# ---------- who can create ----------
WHO = [('skill', 'Independent experts', 'Share professional expertise.'), ('learn', 'Educators', 'Turn experience into structured digital learning.'), ('proj', 'Industry professionals', 'Pass on practical, current skills.'), ('comm', 'Teams', 'Co-create learning together.'), ('prog', 'Institutions', 'Publish under your institution’s name.')]
WHOS = '''<section class="pc-sec cx-sec" aria-labelledby="cx-wh">
<div class="pc-sh"><div><span class="pc-k">Who can create</span><h2 id="cx-wh" class="pc-h2">Expertise comes in many forms.</h2></div></div>
<div class="cx-who">''' + ''.join('<div class="cx-wt2"><span class="cx-ui">' + ic(dashgen.I[k], 20) + '</span><b>' + t + '</b><small>' + d + '</small></div>' for k, t, d in WHO) + '''</div>
</section>'''

# ---------- final CTA: Landing band ----------

# The Landing page's own footer (links, newsletter, 3D-logo illustration, socials): used on every marketing page.
LFOOT = block(L, '<footer class="lh-eng ft"', 'footer').replace('onSubmit="{{hero.onStart}}"', 'onSubmit="{{ftSub}}"')
FTSUB = "ftSub: function (e) { if (e && e.preventDefault) e.preventDefault(); }"

def compact_fc(fc):
    """Landing final CTA band as a compact one-row band (mark · text · button)."""
    fc = fc.replace('<section aria-labelledby="fc-h"', '<section class="cx-fc" aria-labelledby="fc-h"', 1)
    m = re.search(r'(<h2 id="fc-h" class="fc-h2">.*?</h2>\n<p class="fc-sub">.*?</p>\n)', fc, re.S)
    note = re.search(r'<span class="fc-note">.*?</span>\n', fc, re.S)
    inner = m.group(1) + (note.group(0) if note else '')
    if note: fc = fc.replace(note.group(0), '')
    return fc.replace(m.group(1), '<div class="cx-fct">' + inner + '</div>\n')
FC = block(L, '<section aria-labelledby="fc-h"')
FC = re.sub(r'<form class="ds-ask fc-form".*?</form>', btn('Start creating', 'OnbWelcome.dc.html', 'cx-fb'), FC, flags=re.S)
FC = FC.replace('Your next version starts here.', 'Ready to share what you know?').replace('Tell Credalio who you want to become. We’ll help you build the path.', 'Start free. Nova helps you shape your first course in minutes.')
FC = FC.replace('Free to start<i></i>No card needed', 'No subscription<i></i>Pay as you go')
FC = compact_fc(FC)

NAVH = nav('For creators').replace('<a class="sx-cta" href="#">Create account</a>', '<a class="sx-cta" href="OnbWelcome.dc.html">Create account</a>')
HERO = HERO.replace('<div class="ci-door ci-cr aur cx-hero">', '<div class="ci-door ci-cr aur cx-hero">\n' + NAVH.replace('<header class="sx-nav">', '<header class="sx-nav sx-in sx-dk">'), 1)

CSS = r'''.cx-top{padding:16px 16px 0;box-sizing:border-box}
.cx-hero{flex:none;height:620px;border-radius:28px}
.sx-in{position:relative;z-index:4;max-width:none;width:100%;height:84px;padding:0 28px 0 40px;flex-shrink:0}
.sx-dk .sx-word,.sx-dk .sx-mark{filter:brightness(0) invert(1)}
.ci-cr.cx-hero .tip{color:#FFFFFF}
.ci-cr.cx-hero .tip:hover,.ci-cr.cx-hero .tip:focus{color:#C9D7FB}
.sx-dk .sx-link{color:rgba(255,255,255,.78)}
.sx-dk .sx-link:hover{color:#FFFFFF;background:rgba(255,255,255,.1)}
.sx-dk .sx-link-on{color:#FFFFFF;background:rgba(255,255,255,.14)}
.sx-dk .sx-login{color:#FFFFFF !important}
.sx-dk .sx-cta{background:#FFFFFF;color:#0B1433}
.sx-dk .sx-cta:hover{background:#EAF0FF}
.sx-dk .sx-menu{color:#FFFFFF}
.sx-dk .sx-link:focus-visible,.sx-dk .sx-cta:focus-visible,.sx-dk .sx-menu:focus-visible,.sx-dk .sx-logo:focus-visible{outline-color:rgba(255,255,255,.6)}
.cx-hero .ci-copy{max-width:660px;padding:72px 0 0 64px;gap:20px}
.cx-hero .ci-t{margin:0;font-size:60px;line-height:1.04;letter-spacing:-2px}
.cx-hero .ci-d{margin:0;font-size:18px;max-width:500px}
.cx-acts{display:flex;align-items:center;gap:22px;margin-top:10px}
.cx-acts .ci-btn{margin:0}
.cx-wl{position:relative;color:#FFFFFF;font-size:15px;font-weight:600;text-decoration:none;opacity:.9}
.cx-wl:hover{opacity:1;text-decoration:underline;text-underline-offset:4px}
.cx-note{display:inline-flex;align-items:center;gap:6px;font-size:13.5px;color:rgba(255,255,255,.7)}
.cx-hero .ci-vis{right:64px;bottom:auto;top:150px;width:470px}
.cx-hero:hover .ci-vis{transform:none}
.cx-hero .ci-win{padding:20px;gap:10px}
.cx-wt{font-size:17px;font-weight:600;letter-spacing:-.2px;margin:2px 0 4px}
.cx-rm{margin-left:auto;font-size:11.5px;color:#8A93AD;white-space:nowrap}
.cx-nv{display:flex;align-items:flex-start;gap:10px;padding:12px;border-radius:14px;font-size:13px;line-height:1.5;color:#0B1433;margin-top:4px}
.cx-nv .nv-av{width:30px;height:30px;flex-shrink:0}
.cx-hero .cx-f1{left:-96px;bottom:-30px}
.cx-hero .cx-f2{right:-26px;top:-24px;animation-delay:-2.5s}
.cx-sec{padding-top:0}
.cx-studio{display:grid;grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr);gap:64px;align-items:start}
.cx-steps{margin-top:28px}
.cx-steps .tx-step{font-family:inherit;text-align:left;background:none;border-left:0;border-right:0;border-bottom:0;color:#0B1433;cursor:pointer;padding:16px 0}
.cx-steps .tx-step:hover{opacity:1}
.cx-steps .tx-step-run .tx-num{background:#1652F0;color:#FFFFFF}
.cx-win{height:auto;box-sizing:border-box;padding:24px;gap:10px;border-radius:22px;box-shadow:0 40px 80px -50px rgba(11,20,51,.45);background:linear-gradient(180deg,#FFFFFF 0%,#FFFFFF 70%,#F7F9FD 100%)}
.cx-win .ci-row{padding:12px 14px;font-size:13.5px;border-radius:12px}
.cx-win .ci-ck{width:20px;height:20px}
.cx-ol{list-style:none;margin:6px 0 0;padding:0;display:flex;flex-direction:column}
.cx-ol li{position:relative;display:flex;align-items:flex-start;gap:14px;padding:0 0 22px}
.cx-ol li:not(:last-child)::before{content:"";position:absolute;left:11px;top:26px;bottom:2px;width:2px;border-radius:2px;background:#0F6B45}
.cx-ol li.d + li.n::before,.cx-ol li:nth-child(2)::before{background:linear-gradient(#0F6B45,#9DB8F7)}
.cx-ol li > i{width:24px;height:24px;flex-shrink:0;box-sizing:border-box;border-radius:999px;display:flex;align-items:center;justify-content:center;color:#FFFFFF}
.cx-ol li.d > i{background:#0F6B45}
.cx-ol li.n > i{border:2px dashed #9DB8F7;background:#FFFFFF}
.cx-ol li > span{display:flex;flex-direction:column;gap:2px;padding-top:2px}
.cx-ol b{font-size:15px;font-weight:600;color:#0B1433}
.cx-ol small{font-size:13px;color:#5B6582}
.cx-ol li.n small{color:#1652F0}
.cx-ol li:last-child{padding-bottom:0}
.cx-sug{position:relative;display:flex;align-items:flex-start;gap:14px;margin:18px 0 0 38px;padding:18px 20px;border-radius:18px}
.cx-sug::before{content:"";position:absolute;left:-15px;top:-14px;width:14px;height:24px;border-left:2px dashed #9DB8F7;border-bottom:2px dashed #9DB8F7;border-bottom-left-radius:12px}
.cx-sug .nv-av{width:40px;height:40px;flex-shrink:0}
.cx-sug p{margin:2px 0 0;font-size:14.5px;line-height:1.55;color:#0B1433}
.cx-sa{display:flex;align-items:center;gap:16px;margin-top:12px}
.cx-blk .cx-bi{width:30px;height:30px;border-radius:9px;background:#FFFFFF;color:#1652F0;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.cx-bt{font-weight:600;color:#0B1433}
.cx-add{margin-top:8px;font-size:12.5px;font-weight:500;color:#8A93AD}
.cx-types{display:flex;flex-wrap:wrap;gap:6px}
.cx-pp{gap:12px}
.cx-pn{display:flex;flex-direction:column;gap:1px;min-width:0}
.cx-pn b{font-weight:600;color:#0B1433}
.cx-pn small{font-size:12px;color:#5B6582}
.cx-pp .ds-tag{margin-left:auto}
.cx-amb{background:#FFF8EC}
.cx-path{grid-template-columns:repeat(6,minmax(0,1fr))}
.cx-vh{justify-content:center;text-align:center;margin-bottom:44px}
.cx-vh > div{display:flex;flex-direction:column;align-items:center}
.cx-vh .pc-p{margin-left:auto;margin-right:auto}
.cx-vb{display:flex;justify-content:center;margin-top:44px}
.cx-path .ko-dot{background:#FFFFFF}
.cx-path li:first-child .ko-dot{background:#1652F0}
.cx-path .cx-ok .ko-dot{border:0;background:none}
.cx-ec{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:18px}
.cx-earn{padding:32px;border-radius:22px;display:flex;flex-direction:column}
.cx-eh{display:flex;align-items:flex-start;justify-content:space-between;gap:20px}
.cx-ef{position:relative;animation:none;flex-shrink:0}
.cx-earn .pc-units{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:26px 28px;margin:30px 0 28px}
.cx-earn .pc-u{align-items:flex-start;border:0;padding:0;background:none}
.cx-earn > .ds-link{margin-top:auto}
.cx-ui{width:40px;height:40px;border-radius:12px;background:#EAF0FF;color:#1652F0;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.cx-svc{display:flex;flex-direction:column;gap:0;padding:32px}
.cx-svc .pc-rate{margin-top:24px}
.cx-svc .pc-rate .cr-c{width:32px;height:32px;font-size:15px}
.cx-ticks{list-style:none;margin:22px 0 0;padding:0;display:flex;flex-direction:column;gap:12px}
.cx-ticks li{display:flex;align-items:center;gap:10px;font-size:15px;color:#3A4566}
.cx-ticks i{width:20px;height:20px;border-radius:999px;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.cx-who{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px}
.cx-wt2{display:flex;flex-direction:column;gap:6px;padding:22px 20px;border-radius:18px;border:1.5px solid #E6EAF3;background:#FFFFFF}
.cx-wt2 .cx-ui{margin-bottom:10px}
.cx-wt2 b{font-size:16px;font-weight:600}
.cx-wt2 small{font-size:14px;line-height:1.5;color:#4A5578}
.cx-wf{margin-top:auto;display:flex;align-items:center;gap:14px;padding-top:14px;border-top:1px solid #EEF1F7}
.cx-wf .cx-add{margin:0}
.cx-wf .ds-ghost{margin-left:auto;pointer-events:none}
.cx-bar{flex:1;max-width:180px;height:8px;border-radius:999px;background:#EEF1F7;overflow:hidden}
.cx-bar i{display:block;height:100%;border-radius:999px;background:#1652F0}
.cx-sub{margin-left:auto;height:40px;padding:0 18px;border-radius:999px;background:#EEF1F7;color:#8A93AD;font-size:14px;font-weight:600;display:inline-flex;align-items:center}
#cx-make{overflow:clip}
.cx-fb{position:relative;z-index:2;margin-top:14px}
.cx-vis{position:absolute;right:56px;top:128px;width:500px;height:420px;z-index:1}
.cx-back{position:absolute;left:0;top:0;width:290px;box-sizing:border-box;padding:16px 18px 18px;border-radius:18px;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);display:flex;flex-direction:column;gap:10px;transform:rotate(-6deg);box-shadow:0 30px 60px -30px rgba(0,0,0,.5);animation:cxBack .7s cubic-bezier(.2,.8,.2,1) .1s both}
.cx-bk-h{display:flex;justify-content:space-between;align-items:center;font-size:11px;font-weight:500;color:rgba(255,255,255,.7);margin-bottom:4px}
.cx-bk-dots{display:flex;gap:4px}
.cx-bk-dots i{width:6px;height:6px;border-radius:50%;background:rgba(255,255,255,.35)}
.cx-sk{display:block;height:8px;border-radius:6px;background:rgba(255,255,255,.28)}
.cx-bk-r{display:flex;align-items:center;gap:10px;padding:8px 10px;border-radius:10px;background:rgba(255,255,255,.08)}
.cx-bk-r .cx-sk{background:rgba(255,255,255,.4);height:7px}
.cx-ai{margin-left:auto;font-size:10.5px;font-weight:500;color:#C9D7FB}
.cx-cc{position:absolute;left:176px;top:58px;width:300px;transform:rotate(2deg);box-shadow:0 40px 70px -30px rgba(0,0,0,.6);animation:cxCard .8s cubic-bezier(.2,.8,.2,1) .3s both}
.cx-cc:hover{transform:rotate(2deg)}
.cx-cov{height:118px;background:linear-gradient(135deg,#2C5BFF 0%,#1652F0 35%,#0B1433 100%);align-items:flex-start}
.cx-cov .ds-tag{position:relative;z-index:1}
.cx-seal{position:absolute;right:12px;top:12px;width:58px;height:58px;z-index:2;filter:drop-shadow(0 8px 14px rgba(0,0,0,.35));animation:cxStamp .5s cubic-bezier(.2,1.5,.4,1) 1.15s both}
.cx-cc .cs-cb{padding-bottom:16px}
.cx-lrn{display:flex;align-items:center;gap:8px;font-size:12.5px;color:#5B6582;padding-top:12px;border-top:1px solid #EEF1F7}
.cx-lrn b{font-weight:600;color:#0B1433}
.cx-avs{display:flex;padding-left:7px}
.cx-avs .ci-av{width:24px;height:24px;font-size:8.5px}
.cx-gt{margin-left:auto}
.cx-nvf{left:-12px;top:236px;animation-delay:-1.5s}
.cx-nvf .nv-av{width:34px;height:34px;flex-shrink:0}
.cx-ern{right:-18px;bottom:6px;animation-delay:-3s}
.cx-up{font-style:normal;font-size:11.5px;font-weight:600;color:#0F6B45;background:#E7F5EE;border-radius:999px;padding:2px 6px;margin-left:4px;vertical-align:2px}
.cx-bars span{transform-origin:bottom;animation:cxBar .6s cubic-bezier(.2,.8,.2,1) both}
.cx-bars span:nth-child(1){animation-delay:1.3s}
.cx-bars span:nth-child(2){animation-delay:1.38s}
.cx-bars span:nth-child(3){animation-delay:1.46s}
.cx-bars span:nth-child(4){animation-delay:1.54s}
.cx-bars span:nth-child(5){animation-delay:1.62s}
@keyframes cxBack{from{opacity:0;transform:rotate(-12deg) translate(-20px,20px)}}
@keyframes cxCard{from{opacity:0;transform:rotate(8deg) translateY(40px)}}
@keyframes cxStamp{0%{opacity:0;transform:scale(2) rotate(-25deg)}60%{opacity:1;transform:scale(.9) rotate(4deg)}100%{opacity:1;transform:none}}
@keyframes cxBar{from{transform:scaleY(0)}}
@media (prefers-reduced-motion: reduce){.cx-back,.cx-cc,.cx-seal,.cx-bars span{animation:none}}
@media (max-width: 1180px){.cx-vis{right:20px;transform:scale(.86);transform-origin:top right}}
@media (max-width: 960px){.cx-vis{position:relative;right:auto;top:auto;width:300px;height:auto;margin:32px auto 32px;transform:none}.cx-back,.cx-nvf,.cx-ern{display:none}.cx-cc{position:relative;left:auto;top:auto;transform:none;width:100%}}

.cx-fc .fc-wrap{padding-bottom:56px}
.cx-fc .fc-band{flex-direction:row;align-items:center;text-align:left;gap:28px;padding:40px 48px}
.cx-fc .fc-horizon{bottom:-590px;opacity:.85}
.cx-fc .fc-mark{width:60px;height:60px;flex-shrink:0}
.cx-fc .fc-mark img{width:34px;height:34px}
.cx-fct{position:relative;display:flex;flex-direction:column;gap:8px;flex:1;min-width:0}
.cx-fc .fc-h2{margin:0;font-size:34px;letter-spacing:-1px;line-height:1.12}
.cx-fc .fc-sub{font-size:16px}
.cx-fc .fc-note{margin-top:4px;font-size:13px}
.cx-fc .cx-fb{margin:0;flex-shrink:0}
@media (max-width: 1180px){
.cx-hero .ci-copy{padding:36px 0 0 44px;max-width:470px}
.cx-hero .ci-t{font-size:44px}
.cx-hero .ci-vis{right:36px;width:400px}
.cx-path{grid-template-columns:repeat(3,minmax(0,1fr));row-gap:32px}
.cx-path li:nth-child(3)::before{display:none}
.cx-who{gap:10px}
.cx-wt2{padding:18px 16px}
.cx-wt2 b{font-size:15px}
.cx-wt2 small{font-size:13.5px}
}
@media (max-width: 960px){
.cx-top{padding:12px 12px 0}
.cx-hero{height:auto;padding-bottom:0}
.cx-hero .ci-copy{padding:44px 24px 0;max-width:none;gap:16px}
.sx-in{height:72px;padding:0 20px 0 24px}
.cx-hero .ci-t{font-size:34px;letter-spacing:-1px}
.cx-hero .ci-d{font-size:15.5px}
.cx-hero .ci-vis{display:block;position:relative;top:auto;right:auto;width:auto;margin:32px 20px -1px}
.cx-hero .ci-win{border-radius:18px 18px 0 0;border-bottom:0}
.cx-hero .ci-float{display:none}
.cx-studio{grid-template-columns:minmax(0,1fr);gap:24px}
.cx-win{height:auto;min-height:440px}
.cx-path{grid-template-columns:minmax(0,1fr);row-gap:0}
.cx-vh{text-align:left;margin-bottom:22px}
.cx-vh > div{align-items:flex-start}
.cx-vh .pc-p{margin-left:0}
.cx-vb{justify-content:flex-start;margin-top:28px}
.cx-path li:nth-child(3)::before{display:block}
.cx-path .cx-ok .ko-dot svg{width:28px;height:28px}
.cx-ec{grid-template-columns:minmax(0,1fr)}
.cx-who{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;margin:0 -20px;padding:0 20px 4px;scroll-padding:0 20px;scrollbar-width:none}
.cx-who::-webkit-scrollbar{display:none}
.cx-wt2{flex:0 0 220px;scroll-snap-align:start}
}
@media (max-width: 760px){
.cx-hero .ci-copy{padding:40px 20px 0}
.sx-in{height:64px;padding:0 10px 0 18px}
.cx-hero .ci-t{font-size:30px}
.cx-acts{flex-direction:column;align-items:stretch;gap:6px}
.cx-acts .ds-btn{justify-content:space-between;align-self:stretch}
.cx-wl{align-self:center;padding:12px 0}
.cx-note{align-self:center}
.cx-hero .ci-vis{margin:28px 12px -1px}
.cx-hero .ci-win{padding:16px;gap:8px}
.cx-hero .ci-row{font-size:12px}
.cx-hero .cx-rm{display:none}
.cx-steps{margin-top:18px}
.cx-steps .tx-step{padding:12px 0}
.cx-win{padding:16px;min-height:0;border-radius:18px}
.cx-win .ci-row{padding:10px 12px;font-size:13px}
.cx-blk .cx-rm{display:none}
.cx-pp .ds-tag{display:none}
.cx-sa{gap:12px;flex-wrap:wrap}
.cx-sug{margin-left:0;padding:14px;gap:10px}
.cx-sug::before{display:none}
.cx-sug .nv-av{width:32px;height:32px}
.cx-earn,.cx-svc{padding:24px 18px}
.cx-eh{flex-direction:column;gap:16px}
.cx-ec{gap:24px}
.cx-earn .pc-units{grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:12px;margin:24px 0 24px}
.cx-earn .pc-u{flex-direction:column;align-items:flex-start;gap:12px;padding:16px 14px;border-radius:16px;background:#F7F9FD}
.cx-earn .pc-u small{display:none}
.cx-earn .pc-u b{font-size:14.5px;line-height:1.3}
.cx-earn .cx-ui{width:36px;height:36px;border-radius:11px;background:#FFFFFF}
.cx-svc .pc-rate{margin-top:20px}
.cx-svc .pc-p{margin-top:12px}
.cx-ticks{gap:14px;margin-top:24px}
.cx-svc .pc-rate{font-size:22px}
.cx-ticks li{font-size:14.5px}
.cx-fb{align-self:stretch;justify-content:space-between}
.cx-fc .fc-band{flex-direction:column;text-align:center;gap:14px;padding:36px 20px 40px}
.cx-fct{align-items:center}
.cx-fc .fc-h2{font-size:26px}
.cx-fc .fc-sub{font-size:15px}
.cx-fc .fc-mark{width:48px;height:48px}
.cx-fc .fc-mark img{width:28px;height:28px}
.cx-fc .cx-fb{align-self:stretch}
}
'''

BODY = '''<div style="font-family: 'Google Sans', system-ui, sans-serif; color: #0B1433; background: #FFFFFF">
''' + HERO + '''
''' + GC + '''
''' + STUDIO + '''
''' + VAL + '''
''' + EARN + '''
''' + WHOS + '''
''' + FC + '''
''' + LFOOT + '''
</div>'''

JS = '''
var AREAS = ''' + str([a[0] for a in AREAS]).replace("'", '"') + ''';
class Component extends DCLogic {
''' + AURORA_JS + '''
  constructor(props) { super(props); this.state = { tab: 0, drafted: false, skipped: false }; }
  componentDidMount() { this.aurScan(); }
  componentWillUnmount() { if (this._aurMo) this._aurMo.disconnect(); }
  renderVals() {
    var self = this, t = this.state.tab, st = { name: AREAS[t] };
    for (var i = 0; i < 4; i++) (function (k) { st['s' + k] = { cls: k === t ? 'tx-step-run' : 'tx-step-wait', sel: k === t ? 'true' : 'false', pick: function () { self.setState({ tab: k }); } }; st['a' + k] = k === t; })(i);
    var tags = [['blue', 'Draft'], ['blue', 'Draft'], ['blue', '4 people'], ['amber', '1 to fix']];
    st.tagCls = tags[t][0]; st.tag = tags[t][1];
    st.sug = this.state.drafted ? 'Done. Three questions are in Module 3, ready for you to review and edit.' : (this.state.skipped ? 'No problem. I’ll keep it on your Pre-check list.' : 'Module 3 has no knowledge check yet. Shall I draft three questions for you to review?');
    st.acceptLabel = this.state.drafted ? 'Review questions' : 'Draft 3 questions';
    st.accept = function () { if (self.state.drafted) self.setState({ tab: 1 }); else self.setState({ drafted: true, skipped: false }); };
    st.skip = function () { self.setState({ skipped: true, drafted: false }); };
    return { st: st, ''' + FTSUB + ''' };
  }
}
'''

HTML = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>For Creators</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">
<style>
''' + BASE_CSS + style(L) + '\n' + KIT_CSS + '\n' + DCSS + '\n' + pricegen.CSS + '\n' + CSS + '''</style>
</helmet>
''' + BODY + '''
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":4540}}'>''' + JS + '''</script>
</body>
</html>
'''

if __name__ == '__main__':
    open(OUT, 'w').write(HTML)
    print('wrote', OUT, len(HTML))
