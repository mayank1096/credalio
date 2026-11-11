"""Link 4 · Batch 4: Prepare (course review → readiness) and Submit for validation. Client copy word for word
(Creio instead of "AI Tokens"; emoji stars become the badge icon).

Prepare.dc.html (prop page: review | market | profile | nova | ready | issues)       CR-STU-040 to CR-STU-044
Submit.dc.html  (prop step: intake | declare | creator | scope | quote | short | enough | done)
                same focus layout as Link 2's Submit for validation (CR-PAY-*)        CR-STU-045 to CR-STU-052
Preview.dc.html (prop view: course | lesson)  Creator Preview of the learner pages    PREVIEW, CR-LEARN-PRV-001
"""
import json
from l4kit import *
from rail import *
import stu2
from stu2 import CH
from kit import coin, credit, emblem

W = Toggles()
PAGES = []

def P(key, nav, head, main, actions, rail=''):
    PAGES.append((key, nav, head, main, actions, rail))

def src_tag(t):
    k = {'DECLARED': 'blue', 'DECLARED + NOVA': 'blue', 'PROFILE': 'blue', 'CALCULATED': 'green', 'DETECTED': 'green',
         'INFERRED · CHECK': 'amber', 'AFTER DECISION': 'line', 'AT PUBLISH': 'line'}.get(t, 'line')
    return tag(t.capitalize().replace('Nova', 'Nova').replace(' + nova', ' + Nova').replace(' · check', ' · check'), k)

def wkp(main, actions, rail):
    return '<div class="wk"><div class="wk-m">%s</div>%s<aside class="wk-r">%s</aside></div>' % (
        main, actions.replace('class="ds-acts sb sv"', 'class="ds-acts sb sv wk-a"'), rail)

def cont(href, label='Continue', back=None, note=''):
    return acts(href, label, back_href=back, note=note)

LOS = ['Write SQL queries to retrieve and filter structured business data.', 'Combine multiple relational tables using joins.',
       'Analyse business datasets and communicate findings.', 'Understand SQL']

# ---------------------------------------------------------------- CR-STU-040 Course Review (learner preview)
SEE = [('Learning time', '8h 5m', ''), ('Estimated DLP', '%s795' % coin(), ''), ('Subscription price', 'not set', 'ns'), ('Credit price', 'not set', 'ns')]
REQS = [(True, 'Complete all required lessons', '8 lessons'), (True, 'Pass all required assessments', '3 assessments'),
        (True, 'Submit required project', '4 projects and activities'), (False, 'Attend required live sessions', '0 live sessions')]
learner_view = '''<section class="ds-card lv ob-in2" aria-label="Learner Preview">
<div class="lv-bar"><span class="lv-dots"><i></i><i></i><i></i></span><span class="lv-url">credalio.com · course</span><a class="lv-full" href="STU-PRV.dc.html">%s<span>Preview as Learner</span></a></div>
<div class="lv-hero">
<div class="lv-hl"><span class="lv-k">Technology · Data Analytics · Intermediate</span><h2>Data Analysis with SQL</h2><p>Write SQL to answer real business questions, from first query to a finished analysis.</p>
<span class="lv-by">%s<span>By Ada Ononuju with Dr. John Adeyemi, ABC Institute · 8h 5m · Hybrid</span></span></div>
<span class="lv-cv" aria-hidden="true"><i>SQL</i><em></em><em></em><em></em></span>
</div>
<div class="lv-ph"><span class="lv-p">%s<span>Validation tier appears here after validation</span></span><span class="lv-p">%s<span>DLP / Lifetime Credits access set at publication</span></span><span class="lv-p ok">%s<span>Credential: Course Completion Certificate</span></span></div>
<div class="lv-g">
<div><h3>What you’ll be able to do</h3><ul class="lv-lo">%s</ul></div>
<div><h3>Curriculum</h3><ol class="lv-cu">%s</ol></div>
</div>
</section>''' % (ic('eye', 15, 2), stack([(ME, 'AO'), (M1, 'JA'), (None, 'AB')], 26), ic('badge', 14, 2), coin(), ic('cert2', 14, 2),
                 ''.join('<li class="%s"><span>%s</span>%s</li>' % ('warn' if i == 3 else '', ck(11) if i < 3 else ic('warn', 12, 2.2), t) for i, t in enumerate(LOS)),
                 ''.join('<li><b>%d</b><span>%s</span><em>%d items</em></li>' % (i + 1, c[0], len(c[6])) for i, c in enumerate(CH)))
creator_view = '''<section class="ds-card lv cvw ob-in2" aria-label="Creator View">
<div class="cvw-g">%s</div>
</section>''' % ''.join('<div class="cvw-c"><span class="cvw-n">%d</span><div><b>%s</b><span>%s · %s · %s DLP</span></div></div>' % (i + 1, c[0], c[1], c[2], c[3]) for i, c in enumerate(CH))
P('review', 'lprev',
  page_head('Prepare', 'Course Review', 'Experience the course exactly as a learner will, or switch to Creator View to see the structure behind it.',
            '<div class="ds-seg lvt"><button type="button" class="{{cLv}}" onClick="{{showLearner}}">%s<span>Learner Preview</span></button><button type="button" class="{{cCv}}" onClick="{{showCreator}}">%s<span>Creator View</span></button></div>' % (ic('eye', 15, 2), ic('layers', 15, 2))),
  '<sc-if value="{{isLearner}}" hint-placeholder-val="{{ true }}">%s</sc-if><sc-if value="{{isCreator}}" hint-placeholder-val="{{ false }}">%s</sc-if>' % (learner_view, creator_view),
  acts('STU-040M.dc.html', 'Continue', note='<a class="ds-ghost sm" href="STU-009.dc.html">Make Changes</a>'),
  nova_rail('Switch between Learner and Creator view. Nothing here changes your course.') +
  '''<section class="ds-card rx ws ob-in3"><div class="ws-h"><span class="rx-k">What learners will see</span>%s</div>
<div class="ws-g">%s</div>
<span class="ws-l">Completion requirements</span><ul class="ws-r">%s</ul>
<div class="ws-k"><span>Credential</span><b>Certificate of Completion · Credalio-verified once validated</b></div>
<div class="ws-k"><span>Curriculum</span><b>5 chapters · 16 learning items · 15 required · 1 optional</b></div></section>''' % (
      tag('Validation pending', ''), ''.join('<span class="ws-s %s"><em>%s</em><b>%s</b></span>' % (k, l, v) for l, v, k in SEE),
      ''.join('<li class="%s"><span>%s</span><b>%s</b><em>%s</em></li>' % ('' if on else 'off', ck(10) if on else '—', t, d) for on, t, d in REQS)))

# ---------------------------------------------------------------- CR-STU-040 Marketplace preview
SHOWN = [('Title & description', 'From Course Basics', 'DECLARED'), ('Creator', 'Ada Ononuju, Dr. John Adeyemi, ABC Institute', 'PROFILE'),
         ('Skills', 'SQL, Data Analysis, Data Cleaning, Relational Databases', 'DECLARED'), ('Level', 'Intermediate', 'DECLARED'),
         ('Effort', '24–30 hours', 'CALCULATED'), ('Validation tier', 'Pending validation', 'AFTER DECISION'), ('CEI', 'Shown after validation', 'AFTER DECISION'),
         ('DLP consumption', 'Set at publication', 'AT PUBLISH'), ('Lifetime Credit price', 'Set at publication', 'AT PUBLISH')]
GHOST = '<div class="mk-g" aria-hidden="true"><span class="mk-gc"></span><span class="mk-gl"></span><span class="mk-gl s"></span><span class="mk-gl t"></span></div>'
P('market', 'mprev', page_head('Prepare', 'Marketplace Preview', 'How your course will appear to learners browsing Credalio. Dashed items fill in after validation and publication.'),
  '''<section class="ds-card mk ob-in2"><div class="mk-h"><span class="rx-k">In search &amp; browse</span>%s</div>
<div class="mk-row">%s<article class="pv-c mk-c"><span class="pv-cv"><i>SQL</i><em></em><em></em><em></em></span>
<span class="mk-k">Data Analytics · Intermediate · Hybrid</span><b>Data Analysis with SQL</b><p class="mk-by">%s<span>By Ada Ononuju, Dr. John Adeyemi, ABC Institute</span></p>
<span class="pv-sk"><i>SQL</i><i>Data Analysis</i><i>Data Cleaning</i><i>+1</i></span>
<span class="mk-f"><span class="mk-d">CEI · after validation</span><span class="mk-d">%sDLP · Credits at publication</span></span></article>%s</div></section>
<section class="ds-card fc mk-t ob-in3"><div class="fc-h"><div><h2>What’s shown, and where it comes from%s</h2></div></div>
<div class="mk-tb">%s</div></section>''' % (
      tag('Pending validation', 'amber'), GHOST, stack([(ME, 'AO'), (M1, 'JA'), (None, 'AB')], 22), coin(), GHOST,
      tip('Validation tier (Gold, Silver or other tier per final rules) and CEI appear only after the validation decision. DLP consumption and Lifetime Credit price are set in Publish.'),
      ''.join('<div class="mk-r%s"><b>%s</b><span>%s</span>%s</div>' % (' later' if s in ('AFTER DECISION', 'AT PUBLISH') else '', l, v, src_tag(s)) for l, v, s in SHOWN)),
  acts('STU-041.dc.html', 'Continue', back_href='STU-040.dc.html'),
  nova_rail('Tier, CEI and pricing are placeholders until validation and publication.') +
  '''<section class="ds-card rx mk-lg ob-in3"><span class="rx-k">Where each item comes from</span><ul>%s</ul></section>''' % ''.join(
      '<li>%s<span>%s</span></li>' % (src_tag(t), d) for t, d in [('DECLARED', 'Title & description'), ('PROFILE', 'Creator'), ('CALCULATED', 'Effort'), ('AFTER DECISION', 'Validation tier'), ('AT PUBLISH', 'DLP consumption')]))

# ---------------------------------------------------------------- CR-STU-041 Learning Intelligence Profile
LIP = [('Role', 'Not set', 'DECLARED', 'STU-012.dc.html'), ('Career stage', 'Not set', 'DECLARED', 'STU-012.dc.html'),
       ('Skills', 'SQL, Data Analysis, Data Cleaning, Relational Databases', 'DECLARED + NOVA', 'STU-013.dc.html'),
       ('Level', 'Intermediate (declared) · content reads as Intermediate', 'INFERRED · CHECK', 'STU-013.dc.html'),
       ('Prerequisites', 'Excel · Foundation, Statistics · Foundation', 'DECLARED', 'STU-011.dc.html'),
       ('Outcomes', '4 verifiable capabilities, 3 with evidence', 'DETECTED', 'STU-014.dc.html'),
       ('Learning style', 'Primarily hands-on · hybrid (self-paced + live)', 'INFERRED · CHECK', 'STU-LX.dc.html'),
       ('Estimated effort', '24–30 hours (8h 5m built)', 'INFERRED · CHECK', 'STU-018.dc.html'),
       ('Credential', 'Course Completion Certificate', 'DECLARED', 'STU-017.dc.html')]
def lip_row(l, v, s, h):
    k = W.new(False)
    return ('<div class="lp-r%s%s"><span class="lp-l">%s</span><span class="lp-v">%s</span>%s<span class="lp-a"><button type="button" class="ds-ghost xs lp-ok {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}">%s<span>Confirm</span></button><a class="ds-link sm" href="%s">Correct</a></span></div>') % (
        ' ns' if v == 'Not set' else '', ' inf' if 'INFERRED' in s else '', l, v, src_tag(s), k, k, k, ck(11), h)
k0 = W.new(False)
P('profile', 'lip', page_head('Prepare', 'Learning Intelligence Profile', 'This is what Credalio understands about your course. It powers discovery and the Become Engine. Confirm it, or correct anything that’s wrong.',
                              '<span class="lp-cnt"><b>0</b> of 10 confirmed</span><button type="button" class="ds-ghost sm">%s<span>Confirm all</span></button>' % ck(13)),
  '''<section class="ds-card lpu ob-in2"><span class="rx-k">Credalio understands this course as</span>
<div class="lpu-c"><span class="lpu-n"><em>Industry</em><b>Technology</b></span><i></i><span class="lpu-n"><em>Domain</em><b>Data Analytics</b></span><i></i><span class="lpu-n on"><em>Topic</em><b>SQL</b></span></div>
<div class="lpu-a">%s<span class="lp-a"><button type="button" class="ds-ghost xs lp-ok {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}">%s<span>Confirm</span></button><a class="ds-link sm" href="STU-010.dc.html">Correct</a></span></div></section>
<section class="ds-card lp ob-in3">%s</section>''' % (src_tag('DECLARED'), k0, k0, k0, ck(11), ''.join(lip_row(*r) for r in LIP)),
  acts('STU-042.dc.html', 'Continue', back_href='STU-040M.dc.html'),
  nova_rail('Check the inferred rows. You have the final say on how your course is understood.') +
  '''<section class="ds-card rx lip2 ob-in3"><span class="rx-k">Learning Intelligence Profile</span><div class="lip-r">%s<span><b>9</b><em>of 13 signals captured</em></span></div>
<p class="rx-p">“Inferred” rows are Credalio’s reading of your content, not something you entered. You stay in control: correcting a row takes you to where it comes from.</p></section>''' % ring(69, 84, 11))

# ---------------------------------------------------------------- CR-STU-042 Nova Course Review
AREAS = [('Outcome gaps', 'target', [('Outcome 4 uses “understand”, which is hard to observe. A measurable verb makes it assessable.', 'Go to Outcomes', 'STU-014.dc.html'),
                                     ('Outcome 4 isn’t linked to any skill, so learners can’t see what it builds.', 'Go to Outcome → Skills', 'STU-015.dc.html')]),
         ('Assessment gaps', 'quiz', [('LO4 is taught but never assessed.', 'Go to Assessment Centre', 'STU-ASM.dc.html')]),
         ('Skill gaps', 'layers', [('Data Cleaning has no dedicated practice. Learners may not reach Intermediate.', 'Go to Practice & Projects', 'STU-PRA.dc.html'),
                                   ('Relational Databases has no dedicated practice. Learners may not reach the target level.', 'Go to Practice & Projects', 'STU-PRA.dc.html')]),
         ('Curriculum sequencing', 'course', [('Chapter 4 moves from instruction straight to a graded assignment. Add guided practice first.', 'Go to Curriculum', 'STU-020.dc.html')]),
         ('Prerequisite consistency', 'check', []),
         ('Accessibility', 'eye', [('2 videos have no captions.', 'Go to Lesson 3.1', 'STU-022A.dc.html'), ('Three images have no alternative text.', 'Go to Lesson 3.1', 'STU-022B.dc.html')]),
         ('Missing evidence', 'badge', [('Outcome 4 has no way for learners to prove it.', 'Go to Outcome → Evidence', 'STU-016.dc.html')])]
def area(i, a):
    name, icon, items = a
    if not items:
        return '<section class="nr-a clear" style="--i: %d"><header><span class="nr-i">%s</span><b>%s</b>%s</header><p class="nr-ok">%s<span>Nothing found</span></p></section>' % (i, ic(icon, 16, 2), name, tag('Clear', 'green'), ck(11))
    rows = ''
    for t, go, h in items:
        k = W.new(False)
        rows += '<li><p>%s</p><span class="nr-f"><a class="ds-link sm" href="%s">%s%s</a><button type="button" class="ds-chip xs nr-c {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}">%s<span>Mark as considered</span></button></span></li>' % (
            t, h, go, ic('arrowr', 14, 2.2), k, k, k, ck(12))
    return '<section class="nr-a" style="--i: %d"><header><span class="nr-i">%s</span><b>%s</b>%s</header><ul>%s</ul></section>' % (i, ic(icon, 16, 2), name, tag('%d to consider' % len(items), 'amber'), rows)
P('nova', 'nrev', page_head('Prepare', 'Nova Course Review', 'Nova reviews your course like an experienced instructional designer would.', nchip('Run review again')),
  '''<section class="crv ob-in2"><span class="crv-c">%s</span><div><b>A full review is a large AI action</b><p>It uses about 8,000–12,000 Creio. Nova shows the estimate before it runs. Last run used 9,800 Creio.</p></div><button type="button" class="ds-ghost sm">%s<span>Run full review</span></button></section>
<div class="wn info nr-w ob-in2">%s<span><b>Nova review is not validation.</b> Advisory only. This isn’t validation and doesn’t affect your validation outcome. Independent validators make that decision. Act on what’s useful.</span></div>
<div class="nr-s ob-in3"><b>9 suggestions across 6 areas</b><span>review #1</span></div>
<div class="nr ob-in3">%s</div>''' % (coin(True), SPARK, ic('lock', 16, 2), ''.join(area(i, a) for i, a in enumerate(AREAS))),
  acts('STU-043.dc.html', 'Continue', back_href='STU-041.dc.html'),
  nova_rail('These are suggestions, not validation. Mark what you’ve considered.') +
  '''<section class="ds-card rx nr-sum ob-in3"><span class="rx-k">9 suggestions across 6 areas</span><ul>%s</ul></section>''' % ''.join(
      '<li class="%s"><span>%s</span><i style="--w: %d"></i><b>%s</b></li>' % ('' if it else 'z', n, len(it), len(it) if it else '✓') for n, _, it in AREAS))

# ---------------------------------------------------------------- CR-STU-043 Validation Readiness
GROUPS = [('Structure', 'course', False, [(0, '1 required item has no completion rule', 'Set rules', 'STU-027.dc.html'), (1, 'Every learning item is assigned'), (1, 'Course title'), (1, 'Description')]),
          ('Assessments', 'quiz', False, [(1, '5 chapters'), (1, '9 lessons'), (1, '3 assessments'), (1, '1 project'), (1, 'Assessments present'), (0, 'Outcome 4 has no assessment evidence', 'Map evidence', 'STU-016.dc.html')]),
          ('Learning design', 'target', False, [(1, 'Outcomes defined'), (0, 'Outcomes mapped to evidence', '', 'STU-016.dc.html')]),
          ('Content & accessibility', 'eye', False, [(1, '5 videos'), (1, '6 documents'), (0, '2 videos missing captions', 'Generate captions', 'STU-022A.dc.html'), (0, '3 images missing alternative text', 'Add alt text', 'STU-022B.dc.html')]),
          ('Required information', 'file', True, [(1, 'Course basics complete'), (1, 'Audience set'), (1, 'Intended level declared'), (1, 'Delivery configured'), (1, 'Access intent saved')]),
          ('Commercial', 'wallet', False, [(1, 'Access model selected'), (0, 'Provisional pricing not selected yet', 'Set pricing', 'STU-034.dc.html'), (0, 'Maintenance burden not confirmed', 'Confirm', 'STU-033.dc.html')]),
          ('Creator', 'profile', True, [(1, 'Identity verified'), (1, 'Creator Orientation complete')])]
def grp(i, g):
    name, icon, ok, rows = g
    li = ''
    for r in rows:
        if r[0]:
            li += '<li class="ok"><span>%s</span>%s</li>' % (ck(10), r[1])
        else:
            act = ('<a class="ds-ghost xs" href="%s">%s</a>' % (r[3], r[2])) if r[2] else ''
            li += '<li class="no"><span>%s</span><b>%s</b>%s</li>' % (ic('warn', 12, 2.4), r[1], act)
    return '<section class="ds-card rd-g%s" style="--i: %d"><header><span class="rd-i">%s</span><b>%s</b>%s</header><ul>%s</ul></section>' % (
        ' pass' if ok else '', i, ic(icon, 17, 2) if icon in EXTRA or icon in I else '', name, tag('Pass', 'green') if ok else tag('Fail', 'amber'), li)
P('ready', 'ready', page_head('Prepare', 'Automated Readiness Checks', 'Deterministic checks of your course structure. Pass or fail, no AI opinions. These must pass before you can submit.'),
  '''<section class="ds-card rd-h ob-in2"><div class="rd-r">%s<span><b>67%%</b><em>Ready</em></span></div>
<div class="rd-s"><b>7 checks fail</b><div class="rd-b">%s</div><span class="rd-l"><i class="p"></i>2 groups pass<i class="f"></i>5 groups fail</span></div>
<a class="ds-ghost" href="STU-044.dc.html">%s<span>Fix 7 Issues</span></a></section>
<div class="rd ob-in3">%s</div>''' % (
      ring(67, 108, 12, track='#FFF1D6', color='#D99A1E'), ''.join('<i class="%s"></i>' % ('p' if g[2] else 'f') for g in GROUPS), ic('warn', 16, 2),
      ''.join(grp(i, g) for i, g in enumerate(GROUPS))),
  acts('STU-044.dc.html', 'See issues to resolve', back_href='STU-042.dc.html'),
  nova_rail('7 checks fail. These are rule-based, not my opinion.', nchip('What’s left before validation?')))

# ---------------------------------------------------------------- CR-STU-044 Issues to resolve
BLOCK = [('1 required item has no completion rule', 'Set rules', 'Fix in Lesson 3.1', 'STU-027.dc.html'), ('Outcomes mapped to evidence', '', 'Fix in Outcome → Evidence', 'STU-016.dc.html'),
         ('Outcome 4 has no assessment evidence', 'Map evidence', 'Fix in Assessment Centre', 'STU-ASM.dc.html'), ('2 videos missing captions', 'Generate captions', 'Fix in Lesson 3.1', 'STU-022A.dc.html'),
         ('3 images missing alternative text', 'Add alt text', 'Fix in Lesson 3.1', 'STU-022B.dc.html'), ('Provisional pricing not selected yet', 'Set pricing', 'Fix in Course Pricing', 'STU-034.dc.html'),
         ('Maintenance burden not confirmed', 'Confirm', 'Fix in Maintenance Burden', 'STU-033.dc.html')]
RECO = [('Skill proficiency incomplete', 'Every skill needs a starting and expected level.', 'Fix in Skills', 'STU-013.dc.html'),
        ('Outcomes not fully mapped to skills', 'Validators check that outcomes connect to the skills you claim.', 'Fix in Outcome → Skills', 'STU-015.dc.html'),
        ('Career relevance incomplete', 'Needed for the Become Engine and marketplace discovery.', 'Fix in Career Relevance', 'STU-012.dc.html'),
        ('Resource rights missing', 'retail-dataset.zip needs rights or source information.', 'Fix in Resources', 'STU-026.dc.html'),
        ('Practical work not fully linked', 'Each piece of practice should name a skill and an outcome.', 'Fix in Practice & Projects', 'STU-PRA.dc.html'),
        ('Learning Intelligence Profile not confirmed', 'Confirm or correct what Credalio inferred about your course.', 'Fix in Intelligence Profile', 'STU-041.dc.html')]
ADV = [('Guided practice before the Sales Analysis assignment', 'From Nova Course Review: Chapter 4 goes from instruction straight to a graded assignment.', 'Fix in Curriculum', 'STU-020.dc.html'),
       ('Built content is well under your effort estimate', '8h 5m built vs 26 hours estimated. Update the estimate or keep building.', 'Fix in Learning Effort', 'STU-018.dc.html')]
def iss(t, d, a, f, h, n, sev):
    act = ('<button type="button" class="ds-ghost xs">%s</button>' % a) if a else ''
    return '<li class="is-r %s"><span class="is-n">%d</span><div class="is-b"><b>%s</b><span>%s</span></div><span class="is-a">%s<a class="ds-link sm" href="%s">%s%s</a></span></li>' % (sev, n, t, d, act, h, f, ic('arrowr', 14, 2.2))
P('issues', 'ready', page_head('Prepare', 'Issues to Resolve', 'Everything that stands between this draft and submission, in order of importance. Each issue links to where you fix it.'),
  '''<div class="is-t ob-in2"><a class="is-k bl" href="#bl"><b>7</b><span>Blocking</span><em>Must fix before validation</em></a><a class="is-k rc" href="#rc"><b>6</b><span>Recommended</span><em>Strongly recommended</em></a><a class="is-k ad" href="#ad"><b>2</b><span>Advisory</span><em>Optional improvements</em></a></div>
<section class="ds-card is bl ob-in3" id="bl"><header><span class="is-d"></span><b>Blocking</b><em>Must fix before validation</em></header><ol>%s</ol></section>
<section class="ds-card is rc ob-in3" id="rc"><header><span class="is-d"></span><b>Recommended</b><em>Strongly recommended</em></header><ol>%s</ol></section>
<section class="ds-card is ad ob-in4" id="ad"><header><span class="is-d"></span><b>Advisory</b><em>Optional improvements</em></header><ol>%s</ol></section>''' % (
      ''.join(iss(t, 'Automated check failed.', a, f, h, i + 1, 'bl') for i, (t, a, f, h) in enumerate(BLOCK)),
      ''.join(iss(t, d, '', f, h, i + 1, 'rc') for i, (t, d, f, h) in enumerate(RECO)),
      ''.join(iss(t, d, '', f, h, i + 1, 'ad') for i, (t, d, f, h) in enumerate(ADV))),
  '<div class="ds-acts sb sv wk-a is-sv"><span class="sv-s">%s<span>7 blocking issues must be fixed first.</span></span><span class="sv-r"><a class="ds-link" href="STU-043.dc.html">Back</a><span class="ds-btn is-dis" aria-disabled="true"><span>Continue to Validation Intake</span><span class="ob-arrow">%s</span></span></span></div>' % (ic('lock', 14, 2), ARROW),
  nova_rail('Blocking issues stop submission. The rest are up to you.', nchip('What’s left before validation?')))

# ======================================================================= Prepare page assembly
MSTEP = [('Learner Preview', 'STU-040.dc.html', 'lprev'), ('Marketplace Preview', 'STU-040M.dc.html', 'mprev'), ('Intelligence Profile', 'STU-041.dc.html', 'lip'),
         ('Nova Review', 'STU-042.dc.html', 'nrev'), ('Validation Readiness', 'STU-043.dc.html', 'ready')]
def mstep(nav):
    return '<nav class="mst" aria-label="Prepare">%s</nav>' % ''.join(
        '<a href="%s" class="mst-i%s"%s><span class="mst-n">%d</span><span>%s</span></a>' % (h, ' on' if k == nav else '', ' aria-current="page"' if k == nav else '', i + 1, l)
        for i, (l, h, k) in enumerate(MSTEP))

def prep_body():
    blocks = []
    for key, nav, head, main, actions, rail in PAGES:
        body = head + ('' if key == 'review' else mstep(nav)) + wkp(main, actions, rail)
        blocks.append('<sc-if value="{{p_%s}}" hint-placeholder-val="{{ %s }}">\n%s\n</sc-if>' % (key, 'true' if key == 'review' else 'false', body))
    navs = ''.join('<sc-if value="{{n_%s}}" hint-placeholder-val="{{ %s }}">%s</sc-if>' % (n, 'true' if n == 'lprev' else 'false', sidebar(n))
                   for n in sorted(set(p[1] for p in PAGES)))
    return '''<div class="ds-root">
%s
<div style="min-width: 0; display: flex; flex-direction: column">
%s
<main class="ds-main pp-main">
%s
</main>
</div>
</div>''' % (navs, topbar(phase='Prepare'), '\n'.join(blocks))

PREP_JS = W.js() + '''var NAV = %s;
class Component extends DCLogic {
  componentDidMount() {
    try { var m = document.querySelector('.mst .on'); if (m && m.parentElement) { m.parentElement.scrollLeft = m.offsetLeft - 16; } } catch (e) {}
  }
  renderVals() {
    var pg = this.props.page || 'review';
    var v = togVals(this), self = this;
    Object.keys(NAV).forEach(function (k) { v['p_'.concat(k)] = k === pg; });
    %s.forEach(function (n) { v['n_'.concat(n)] = n === NAV[pg]; });
    var cv = this.state.cv === undefined ? this.props.view === 'creator' : this.state.cv;
    v.isLearner = !cv; v.isCreator = cv;
    v.cLv = cv ? '' : 'on'; v.cCv = cv ? 'on' : '';
    v.showLearner = function () { self.setState({ cv: false }); };
    v.showCreator = function () { self.setState({ cv: true }); };
    v.navCls = this.state.nav ? 'ds-open' : '';
    v.toggleNav = function () { self.setState({ nav: !self.state.nav }); };
    return v;
  }
}''' % (json.dumps({p[0]: p[1] for p in PAGES}), json.dumps(sorted(set(p[1] for p in PAGES))))

# ======================================================================= SUBMIT (focus flow, Link 2 CR-PAY layout)
S = Toggles()
STEPS = ['Intake', 'Declaration', 'Readiness', 'Scope', 'Quote', 'Payment']
DET = [('5', 'chapters'), ('9', 'lessons'), ('5', 'videos'), ('8h 5m', 'detected learning time'), ('3', 'assessments'), ('35', 'questions'), ('1', 'projects'), ('4 (4 assessed)', 'outcomes')]

def q(label, sub, inner, cls=''):
    return '<div class="iq%s"><div class="iq-t"><b>%s</b>%s</div>%s</div>' % ((' ' + cls) if cls else '', label, ('<span>%s</span>' % sub) if sub else '', inner)
def rchips(items, on, group):
    return '<div class="chips">%s</div>' % ''.join(S.chip(x, i == on, group, 'sm') for i, x in enumerate(items))
def mchips(items, on):
    return '<div class="chips">%s</div>' % ''.join(S.chip(x, i in on, None, 'sm') for i, x in enumerate(items))
PRE = '<span class="iq-pf">%s<span>Pre-filled from Basics.</span></span>'

def panel(h, p, body, foot):
    return '<section class="cl-panel ob-in2"><h2 class="cl-ph">%s</h2>%s%s<div class="cl-foot">%s</div></section>' % (h, ('<p class="cl-pp">%s</p>' % p) if p else '', body, foot)
def back(href):
    return '<a class="ds-ghost cl-bk" href="%s" aria-label="Back">%s<span>Back</span></a>' % (href, ICON(I['back'], 18, 2))

SUB = {}
SUB['intake'] = (0, '''<div class="cl-nx det"><span>Detected by Credalio</span><div class="det-g">%s</div></div>''' % ''.join('<span><b>%s</b><em>%s</em></span>' % d for d in DET),
    panel('Validation Intake', 'We only ask what Credalio can’t reliably derive from your course. Everything above the line is already known.',
          '<div class="iqs">%s%s%s%s%s%s</div>' % (
              q('AI usage', 'Does this learning experience involve AI? ' + (PRE % SPARK), rchips(['No', 'AI is taught', 'Learners use AI', 'AI outputs are assessed', 'AI is integrated into the learning experience'], 2, 'ai')),
              q('External tools', PRE % SPARK, rchips(['No external tools', 'Yes: PostgreSQL'], 1, 'tools')),
              q('Regulated subject matter', '', rchips(['Healthcare', 'Financial advice', 'Legal practice', 'Safety-critical activities', 'Other regulated areas', 'None'], 5, 'reg')),
              q('Professional claims', 'Does this course prepare learners for an external professional licence, certification or regulated activity?', S.seg(['Yes', 'No'], 1), 'row'),
              q('Sensitive data', 'Will learners upload personal, confidential or sensitive information?', S.seg(['Yes', 'No'], 1), 'row'),
              q('Who delivers live sessions?', '', mchips(['Creator', 'Co-Creator', 'Guest instructor'], {0}))),
          back('STU-044.dc.html') + btn('Continue', 'STU-046.dc.html', 'cl-go')))
DECL = ['The content is accurate to the best of my knowledge.', 'I hold the required rights and permissions for all materials.',
        'AI-generated content has been reviewed and approved by me.', 'The submitted content represents the course I intend to publish.',
        'I have made all required disclosures in the validation intake.', 'I understand that material changes after validation may trigger revalidation.']
def dbox(t):
    k = S.new(False)
    return '<button type="button" class="dc-r {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}"><span class="dc-b">%s</span><span>%s</span></button>' % (k, k, k, ck(12), t)
INTAKE = [('AI', 'Learners use AI'), ('External tools', 'Yes: PostgreSQL'), ('Regulated subject', 'None'), ('Professional claims', 'No'), ('Sensitive data', 'No')]
SUB['declare'] = (1, '''<div class="cl-nx fi"><span>From your intake</span><dl>%s</dl><a class="ds-link sm" href="STU-045.dc.html">Edit intake</a></div>''' % ''.join('<div><dt>%s</dt><dd>%s</dd></div>' % x for x in INTAKE),
    panel('Creator Declaration', 'Your formal statement about this course. Validators rely on it, and it becomes part of the validation record.',
          '<span class="dc-l">I declare that</span><div class="dc">%s</div>' % ''.join(dbox(t) for t in DECL),
          back('STU-045.dc.html') + btn('Sign &amp; Continue', 'STU-047.dc.html', 'cl-go')))
CRR = [('ok', 'Identity verified', ''), ('ok', 'KYC complete', ''), ('ok', 'Required credentials verified', ''), ('pr', 'Creator Orientation complete', '5 of 7 modules'), ('ok', 'Creator policies accepted', '')]
ORG = [('Business verification', 'Not required · individual creator'), ('Authorised representative', 'Not required · individual creator')]
def crr(st, t, d):
    if st == 'pr':
        return '<li class="cr-r pr"><span class="cr-s">%s</span><span class="cr-t"><b>%s</b><span class="cr-pb"><i style="width: 71%%"></i></span><em>%s</em></span><a class="ds-ghost xs" href="#">Resume</a></li>' % (STATUS['pr'], t, d)
    return '<li class="cr-r"><span class="cr-s">%s</span><span class="cr-t"><b>%s</b></span>%s</li>' % (STATUS['ok'], t, tag('Complete', 'green'))
SUB['creator'] = (2, '''<div class="cl-nx am"><span>Before submission</span><p>1 requirement remains before submission. No validation case is created yet.</p><a class="ds-ghost sm" href="#">Complete Requirement</a></div>''',
    panel('Creator Readiness', 'Requirements on you as a creator, separate from the course itself. Each trust layer is checked separately.',
          '<span class="dc-l">Creator</span><ul class="cr-l">%s</ul><span class="dc-l">Organisation</span><ul class="cr-l na">%s</ul>' % (
              ''.join(crr(*r) for r in CRR), ''.join('<li class="cr-r"><span class="cr-s"><span class="st na">–</span></span><span class="cr-t"><b>%s</b></span><span class="cr-na">%s</span></li>' % r for r in ORG)),
          back('STU-046.dc.html') + btn('Continue', 'STU-048.dc.html', 'cl-go')))
SUB['scope'] = (3, '''<div class="cl-nx"><span>Behind the scenes</span><p>Behind the scenes this uses workflow SV-001 Standard Course.</p></div>''',
    panel('Validation Scope', 'Credalio classifies your case from your course structure, intake and declaration. You don’t choose validators.',
          '''<div class="vs-seats"><div class="vs-s"><span class="vs-i">%s</span><b>Educational Validator</b><em>Independent · assigned by role</em></div><span class="vs-x" aria-hidden="true"></span><div class="vs-s lead"><span class="vs-i">%s</span><b>Subject Matter Validator</b><em><span class="vs-l">%s Case Lead</span></em></div></div>
<dl class="py-dl">%s</dl>''' % (ic('cap', 20, 2), ic('target', 20, 2), ic('badge', 12, 2.2), ''.join('<div class="tx"><dt>%s</dt><dd>%s</dd></div>' % r for r in [
              ('Validation type', 'Standard Course Validation'), ('Complexity', 'Intermediate'), ('Required validators', '2'), ('Estimated review window', 'X business days (SLA to be confirmed)')])),
          back('STU-047.dc.html') + btn('See your quote', 'STU-049.dc.html', 'cl-go')))
SUB['quote'] = (4, '''<div class="cl-nx"><span>What you’re paying for</span><ul class="pf">%s</ul></div>''' % ''.join('<li>%s<span>%s</span></li>' % (ck(10), t) for t in [
        'Independent review by 2 validators, assigned by role', 'A validation report with findings, whatever the decision', 'Clarification requests and case meetings within this case', 'One resubmission if improvements are required [TO CONFIRM]']),
    panel('Your Validation Quote', '', '''<span class="py-svc">Data Analysis with SQL · Standard Course Validation</span>
<dl class="py-dl"><div><dt>Educational Validation</dt><dd>200</dd></div><div><dt>Subject Matter Validation</dt><dd>220</dd></div><div class="sub"><dt>Validator fees subtotal</dt><dd>420</dd></div><div><dt>Credalio service fee (5%% per case)</dt><dd>21</dd></div><div class="py-tot"><dt>Total</dt><dd>%s441 Credits</dd></div></dl>
<p class="py-note">100%% of validator fees go to the validators.%s</p>''' % (credit(), tip('Fee amounts are illustrative until the fee table is set.')),
          back('STU-048.dc.html') + btn('Continue to Payment', 'STU-050.dc.html', 'cl-go')))
def pay(enough):
    checks = [(False, 'No blocking issues', '<a class="ds-link sm" href="STU-044.dc.html">Open</a>'), (True, 'Creator Declaration signed', ''), (True, 'Creator readiness complete', ''), (enough, 'Enough Creator Credits', '')]
    ul = ''.join('<li class="%s">%s<span>%s</span>%s</li>' % ('ok' if o else 'to', STATUS['ok'] if o else STATUS['to'], t, a) for o, t, a in checks)
    if enough:
        wal = '<div class="wl ok"><div class="wl-h">%s<b>Creator Credit Wallet</b></div><dl><div><dt>Balance</dt><dd>1,240 Credits</dd></div><div><dt>Required</dt><dd>441 Credits</dd></div><div class="r"><dt>Remaining after payment</dt><dd>799 Credits</dd></div></dl><div class="wl-bar"><i style="width: 35.6%%"></i></div></div>' % credit()
        foot = back('STU-049.dc.html') + btn('Pay 441 Credits &amp; Submit', 'STU-052.dc.html', 'cl-go')
    else:
        wal = ('<div class="wl short"><div class="wl-h">%s<b>Creator Credit Wallet</b></div><dl><div><dt>Balance</dt><dd>300 Credits</dd></div><div><dt>Required</dt><dd>441 Credits</dd></div><div class="r"><dt>Remaining after payment</dt><dd>—</dd></div></dl>'
               '<div class="wl-bar"><i style="width: 68%%"></i></div><p class="wl-n">%s<span>You need 141 more Credits.</span></p><div class="wl-t">%s</div></div>') % (
            credit(), ic('warn', 15, 2.2), ''.join(S.chip(x, i == 0, 'top', 'sm') for i, x in enumerate(['+ 250 Credits', '+ 500 Credits', '+ 1000 Credits'])))
        foot = back('STU-049.dc.html') + '<span class="ds-btn cl-go is-dis" aria-disabled="true"><span>Pay 441 Credits &amp; Submit</span><span class="ob-arrow">%s</span></span>' % ARROW
    return (5, '''<div class="cl-nx"><span>After you submit</span><p>A validation case is created with its own case ID. Validators are assigned by role and review independently. You’ll be notified when anything is needed from you. Editing is paused on submitted content until a decision.</p></div>''',
            panel('Payment', 'Pay from your Creator Credit Wallet to create your validation case. Creator Credits pay for validation and AI services; they’re separate from your earnings.',
                  '<span class="dc-l">Before you pay</span><ul class="bp">%s</ul>%s' % (ul, wal), foot))
SUB['short'] = pay(False)
SUB['enough'] = pay(True)

CASE = [('Case ID', 'VAL-2026-00482'), ('Course', 'Data Analysis with SQL'), ('Validation type', 'Standard Course Validation'),
        ('Validator roles', '2 · Educational Validator, Subject Matter Validator · <span class="vs-l">%s Case Lead</span>' % ic('badge', 12, 2.2)),
        ('Paid', '%s441 Creator Credits' % credit()), ('Estimated review window', '[TO CONFIRM: validation SLA]')]
TRACK = [('dn', 'Submitted'), ('on', 'Validator Assignment'), ('', 'Validation'), ('', 'Decision')]
DONE = '''<div class="ko-wrap ob-in"><div class="ko">%s<span class="ko-pill">Submitted</span><h1 class="ko-h1">Submitted for validation</h1><p class="ko-sub">Your validation case has been created.</p>
<ol class="ko-tr">%s</ol>
<section class="ko-card"><span class="ko-cl">Case summary</span><dl>%s</dl></section>
<p class="ko-note">%s<span>Nothing to do right now. We’ll notify you when validators are assigned or if anything is needed.</span></p>
<div class="ko-acts">%s<a class="ds-link" href="STU-009.dc.html">Back to Studio Home</a></div></div></div>''' % (
    emblem(), ''.join('<li class="%s"><i>%s</i><span>%s</span></li>' % (k, ck(10) if k == 'dn' else '', t) for k, t in TRACK),
    ''.join('<div><dt>%s</dt><dd>%s</dd></div>' % r for r in CASE), ic('bell', 16, 2) if 'bell' in I else '', btn('Open Validation Workspace', '#'))

def submit_body():
    blocks = []
    for k, (step, side, pnl) in SUB.items():
        steps = ''.join('<li class="%s"><i></i><span>%s</span></li>' % ('dn' if i < step else ('on' if i == step else ''), s) for i, s in enumerate(STEPS))
        blocks.append('<sc-if value="{{s_%s}}" hint-placeholder-val="{{ %s }}"><div class="cl"><aside class="cl-side ob-in"><h1 class="cl-h1">Data Analysis with SQL</h1><p class="cl-sub">Course validation · 5 chapters, 16 learning items and 3 assessments.</p><div class="cl-meta"><span>Hybrid</span><span>Intermediate</span><span>Step %d of 6</span></div><ol class="cl-steps">%s</ol>%s</aside>%s</div></sc-if>' % (
            k, 'true' if k == 'intake' else 'false', step + 1, steps, side, pnl))
    blocks.append('<sc-if value="{{s_done}}" hint-placeholder-val="{{ false }}">%s</sc-if>' % DONE)
    return '''<div class="tk-root {{rootCls}}"><span class="cl-glow"></span>
<header class="tk-top"><a class="lp-x" href="STU-043.dc.html" aria-label="Close">%s</a><span class="lp-title"><span class="lp-t1">Submit for validation</span></span><span style="flex-grow: 1"></span><a href="#" class="ds-tok" aria-label="72,450 Creio">%s<span>72.4K</span></a></header>
%s
</div>''' % (ic('x', 20, 2), COIN('tp', 26), '\n'.join(blocks))
SUBMIT_JS = S.js() + '''class Component extends DCLogic {
  renderVals() {
    var s = this.props.step || 'intake', v = togVals(this);
    %s.forEach(function (k) { v['s_'.concat(k)] = k === s; });
    v.rootCls = s === 'short' ? 'is-wait' : (s === 'enough' || s === 'done' ? 'is-ok' : '');
    return v;
  }
}''' % json.dumps(list(SUB) + ['done'])

# ======================================================================= PREVIEW (Creator Preview of learner pages; illustrative client sample data)
PV_STRIP = '''<div class="pvs"><span class="pvs-t">Creator Preview</span><p><b>%s</b> %s</p><span class="pvs-a">%s<a class="ds-ghost sm pvs-x" href="STU-040.dc.html">%s<span>Exit Preview</span></a></span></div>'''
LV_NAV = '''<header class="lh"><a class="lh-lg" href="#" aria-label="Credalio"><span class="lg-word"></span></a><nav class="lh-n"><a href="#">Browse</a><a href="#">Certifications</a><a href="#">Career Paths</a><a href="#">My Learning</a></nav>
<label class="lh-s">%s<input placeholder="Search courses, certifications, paths..." aria-label="Search"></label><span class="lh-na">No Learner Account Context</span></header>''' % ic('search', 16, 2) if 'search' in I else ''
OUTS = ['Write SQL queries to retrieve and analyze data', 'Clean and organize datasets for analysis', 'Combine tables and produce useful business insights', 'Complete a practical SQL analysis project']
SKL = [('SQL Queries', 'Intermediate'), ('Data Cleaning', 'Intermediate'), ('Database Joins', ''), ('Data Analysis', ''), ('Data Interpretation', 'Foundational'), ('Problem Solving', '')]
INCL = [('18 hours', 'Learning content'), ('14', 'Video lessons'), ('8', 'Downloadable resources'), ('5', 'Assessments'), ('1', 'Practical project')]
CH1 = [('Welcome to SQL', '8 min', True), ('Understanding Databases', '20 min', False), ('Setting Up Your Environment', '17 min', False), ('Knowledge Check', '10 min', False)]
CHS = ['Chapter 2: Working with Databases', 'Chapter 3: Filtering and Aggregating Data', 'Chapter 4: SQL Joins and Relationships', 'Chapter 5: Advanced Queries', 'Chapter 6: Final Project and Assessment']
FAQ = ['Can I learn with DLP?', 'What happens if I run out of DLP?', 'What does lifetime access include?', 'Do I need prior experience?', 'Will I receive a certificate?', 'Can I revisit completed lessons?', 'How do I get support?']
BARS = [('5', 78), ('4', 14), ('3', 5), ('2', 2), ('1', 1)]
AM = '<span class="av lc-av" style="width: %dpx; height: %dpx">AM</span>'
def sec(h, body, cls='', right=''):
    return '<section class="lc-s%s"><div class="lc-sh"><h2>%s</h2>%s</div>%s</section>' % ((' ' + cls) if cls else '', h, right, body)
COURSE_PAGE = '''<div class="lc">
%s
%s
<div class="lc-hero"><div class="lc-in">
<nav class="lc-bc" aria-label="Breadcrumb"><a href="#">Marketplace</a>%s<a href="#">Technology</a>%s<span>Data Analytics</span></nav>
<div class="lc-bd"><span class="lc-gold">%s<span>Gold Validated</span></span><span class="lc-cei"><b>CEI 87</b>/100</span><span class="lc-lv">Intermediate</span></div>
<h1>Data Analysis with SQL</h1>
<p class="lc-d">Learn how to query, clean and analyze real datasets using SQL, then apply your skills to practical business problems.</p>
<div class="lc-st"><span class="lc-r"><b>4.8</b><span class="lc-stars" aria-hidden="true"><i></i><i></i><i></i><i></i><i class="h"></i></span><em>(126 reviews)</em></span><span>2,418 learners</span><span>18 hours</span><span>6 chapters</span><span>English</span><span>Updated Sep 2026</span></div>
<div class="lc-by">%s<span>Created by <b>Alex Morgan</b> · Data Analytics Educator</span></div>
</div></div>
<div class="lc-body"><div class="lc-main">
%s%s%s%s%s%s%s%s%s%s%s
<p class="lc-ill">Illustrative page composition using sample course data. Actual content, validation details and access options come from the published course record.</p>
</div>
<aside class="lc-buy"><div class="lc-bx"><span class="lc-bv" aria-hidden="true"><i>SQL</i><em></em><em></em></span><div class="lc-bi"><b>Choose How to Learn</b>
<button type="button" class="lc-o on"><span class="lc-oi">%s</span><span class="lc-ot"><b>Subscription</b><em>Learn using your DLP allowance</em></span><span class="lc-op">1,800 <small>DLP</small></span></button>
<button type="button" class="lc-o"><span class="lc-oi">%s</span><span class="lc-ot"><b>Lifetime Access</b><em>Purchase continuing course access</em></span><span class="lc-op">420 <small>Credits</small></span></button>
<span class="ds-btn lc-cta is-dis" aria-disabled="true"><span>Choose Access Option</span><span class="ob-arrow">%s</span></span>
<p class="lc-tn">%s<span>Access and eligibility terms are shown before confirmation.</span></p>
<button type="button" class="lc-ask nova-card">%s<span>Ask Nova: Is this course right for me?</span></button></div></div></aside>
</div></div>''' % (
    PV_STRIP % ('Learner Preview', 'You’re viewing this course as a learner would see it before enrolling. Purchases, enrollments and learning rewards are disabled in preview mode.',
                '<a class="ds-ghost sm" href="STU-PRV-L.dc.html">%s<span>Preview Sample Lesson</span></a>' % ic('play', 15, 2), ic('x', 15, 2)),
    LV_NAV, ic('chev', 13, 2), ic('chev', 13, 2), ic('badge', 15, 2), AM % (40, 40),
    sec('What You’ll Be Able to Do', '<ul class="lc-ol">%s</ul>' % ''.join('<li><span>%s</span>%s</li>' % (ck(11), o) for o in OUTS)),
    sec('Skills You’ll Develop', '<div class="lc-sk">%s</div>' % ''.join('<span><b>%s</b>%s</span>' % (s, ('<em>%s</em>' % l) if l else '') for s, l in SKL)),
    '<div class="lc-2">%s%s</div>' % (
        sec('Who This Course Is For', '<ul class="lc-ul">%s</ul><p class="lc-p">Best for: career development, practical workplace skills, professional upskilling.</p>' % ''.join('<li>%s</li>' % x for x in ['Aspiring data analysts', 'Business professionals working with reports', 'Students with basic spreadsheet experience', 'Professionals transitioning into analytics'])),
        sec('What You Should Know First', '<dl class="lc-dl"><div><dt>Required knowledge</dt><dd>Basic spreadsheet familiarity.</dd></div><div><dt>Required tools</dt><dd>Computer and access to the SQL learning environment.</dd></div><div><dt>Recommended</dt><dd>Comfortable working with tables and simple data.</dd></div></dl>')),
    sec('What’s Included in This Course', '<p class="lc-p">Everything you need to learn, practice and apply your SQL skills.</p><div class="lc-in5">%s</div><span class="lc-al">Also Included</span><ul class="lc-ul ck">%s</ul>' % (
        ''.join('<span><b>%s</b><em>%s</em></span>' % x for x in INCL), ''.join('<li><span>%s</span>%s</li>' % (ck(10), x) for x in ['Practical exercises and knowledge checks', 'Access to course learning materials', 'Learner support as provided by the creator', 'Verified completion certificate when requirements are met'])),
        right=tip('Illustrative counts. In production, calculate lesson, assessment and resource totals from the approved published course version. Only features actually included are shown — downloadable resources (practice datasets, workbooks) are counted separately from PDF lessons in the curriculum.', 'r')),
    sec('Course Curriculum', '<div class="lc-cu"><details open><summary><b>Chapter 1 — Getting Started with SQL</b><em>4 lessons · 55 min</em>%s</summary><ol>%s</ol></details>%s</div>' % (
        ic('down', 16, 2), ''.join('<li>%s<span>%s</span><em>%s</em>%s</li>' % (ic('play', 14, 2), t, d, '<span class="lc-pv">Preview</span>' if p else '') for t, d, p in CH1),
        ''.join('<details><summary><b>%s</b><em>Lessons, practice and learning activities</em>%s</summary></details>' % (c, ic('down', 16, 2)) for c in CHS)), right='<span class="lc-meta">6 chapters · 18 hours</span>'),
    sec('Projects &amp; Evidence', '<div class="lc-pj"><span class="lc-pji">%s</span><div><span class="lc-k">What You’ll Build</span><b>SQL Business Analysis Project</b><p>Analyze a sample sales dataset, identify performance patterns and produce a structured report using SQL.</p><span class="lc-al">You’ll demonstrate:</span><ul class="lc-ul ck">%s</ul></div></div>' % (
        ic('project', 22, 2), ''.join('<li><span>%s</span>%s</li>' % (ck(10), x) for x in ['Query writing and data filtering', 'Combining and interpreting datasets', 'Presenting findings supported by evidence']))),
    sec('Completion &amp; Achievements', '<div class="lc-ce"><span class="lc-cei2">%s</span><div><b>Verified Course Completion Certificate</b><p>Complete the required lessons, pass mandatory assessments and submit the final project to qualify.</p></div></div>' % ic('cert2', 26, 1.8)),
    sec('Learner Reviews', '<div class="lc-rv"><div class="lc-rs"><b>4.8</b><span class="lc-stars" aria-hidden="true"><i></i><i></i><i></i><i></i><i class="h"></i></span><em>126 reviews · Verified learners</em><ul>%s</ul></div><blockquote class="lc-q"><p>The practical SQL exercises helped me understand how to work with real business data. The final project was particularly useful.</p><footer><span class="av lc-av" style="width: 36px; height: 36px">AO</span><span><b>Amara O.</b><em>Verified learner</em></span></footer></blockquote></div>' % ''.join(
        '<li><span>%s</span><i><b style="width: %d%%"></b></i><em>%d%%</em></li>' % (s, p, p) for s, p in BARS), right='<a class="ds-link sm" href="#">See All Reviews</a>'),
    sec('Meet Your Creator', '<div class="lc-cr">%s<div class="lc-crb"><span class="lc-crn"><b>Alex Morgan</b><span class="lc-vf">%s<span>Credentials Verified</span></span></span><em>Data Analytics Educator</em><p>Alex helps aspiring analysts and working professionals develop practical skills in SQL, reporting and business analytics.</p><div class="lc-crs"><span><b>8</b>Courses</span><span><b>12.4k</b>Learners</span><span><b>4.8</b>Rating</span></div><a class="ds-ghost sm" href="#">View Creator Profile</a></div></div>' % (AM % (72, 72), ck(10))),
    sec('Validation &amp; Quality', '<div class="lc-vq"><div class="lc-vb"><span class="lc-medal">%s</span><b>Gold Validated</b><span class="lc-ceir">%s<span><b>87</b><em>/ 100 CEI</em></span></span></div><div class="lc-vt"><p>This course has been reviewed against Credalio’s learning quality standards, including relevant learning design, subject accuracy and assessment requirements.</p><dl class="lc-vd"><div><dt>Course Version</dt><dd>v1.0</dd></div><div><dt>Originally Published</dt><dd>12 Sep 2026</dd></div><div><dt>Last Updated</dt><dd>Updated Sep 2026</dd></div></dl><p class="lc-fine">Validation reflects approved review scope. It does not guarantee employment, third-party certification or a particular professional outcome. “Last Updated” reflects the most recent approved version activated for the live course, not draft edit dates.</p></div></div>' % (
        ic('badge', 26, 1.8), ring(87, 76, 9, track='#F3EAD3', color='#C08A1E'))),
    sec('Frequently Asked Questions', '<div class="lc-faq">%s</div>' % ''.join('<details><summary>%s%s</summary></details>' % (f, ic('plus', 16, 2)) for f in FAQ)),
    coin(), credit(), ARROW, ic('lock', 13, 2), nova_av('sm'))

def _cut(page, h2):
    i = page.index('<section class="lc-s"><div class="lc-sh"><h2>%s' % h2)
    j = page.index('</section>', i) + len('</section>')
    return page[:i] + page[j:], page[i:j]
COURSE_PAGE, _v = _cut(COURSE_PAGE, 'Validation &amp; Quality')
COURSE_PAGE, _c = _cut(COURSE_PAGE, 'Completion &amp; Achievements')
COURSE_PAGE, _m = _cut(COURSE_PAGE, 'Meet Your Creator')
COURSE_PAGE = COURSE_PAGE.replace('</div></div></aside>', '</div></div>%s%s%s</aside>' % (_v, _c, _m))

LESSON = '''<div class="lp2">
%s
<header class="lpt"><a class="lpt-x" href="STU-PRV.dc.html">%s<span>Exit to Course</span></a><b class="lpt-t">Data Analysis with SQL</b><span style="flex-grow: 1"></span><span class="lpt-d">%s<b>1,800</b> DLP</span><span class="av" style="width: 36px; height: 36px">JM</span></header>
<div class="lpb"><aside class="lps"><div class="lps-p"><span>Course Progress</span><div class="lps-r">%s<b>62%%</b></div></div>
<div class="lps-c"><b>Chapter 1 — Getting Started with SQL</b><ol>%s</ol></div>
<div class="lps-c"><b>Chapter 2 — Working with Databases</b><ol>%s</ol></div></aside>
<main class="lpm"><div class="lpv" aria-label="Video"><span class="lpv-p">%s</span><span class="lpv-b"><i style="width: 38%%"></i></span><span class="lpv-tm">7:36 / 20:00</span></div>
<span class="lpm-k">Chapter 1 · Video Lesson</span><h1>Understanding Databases</h1>
<section class="lpn"><b>Lesson Notes</b><p>This lesson introduces relational databases, tables, rows and columns, and how data is organized before you start writing queries. By the end, you’ll understand how SQL fits into a database system.</p></section>
<div class="lpf"><a class="ds-ghost" href="#">%s<span>Previous</span></a>%s</div></main></div>
</div>''' % (
    PV_STRIP % ('Learning Preview', 'You’re viewing this course as a learner would see it before enrolling. Purchases, enrollments and learning rewards are disabled in preview mode.', '', ic('x', 15, 2)),
    ICON(I['back'], 16, 2), coin(), ring(62, 44, 7),
    ''.join('<li class="%s"><span class="lps-i">%s</span><span>%s</span><em>%s</em></li>' % (k, ck(9) if k == 'dn' else ic('play', 11, 2.2), t, d) for k, t, d in [('dn', 'Welcome to SQL', '8 min'), ('on', 'Understanding Databases', '20 min'), ('', 'Setting Up Your Environment', '17 min'), ('', 'Knowledge Check', '10 min')]),
    ''.join('<li><span class="lps-i">%s</span><span>%s</span></li>' % (ic('play', 11, 2.2), t) for t in ['Primary and Foreign Keys', 'Normalization Basics', 'Practice Activity']),
    ic('play', 28, 2), ICON(I['back'], 16, 2), btn('Next: Setting Up Your Environment', '#'))

# ======================================================================= CSS
PREP_CSS = r'''.pp-main .pg-h .ds-seg{flex-shrink:0}
.lvt button{gap:7px;padding:0 16px}
.lvt button svg{color:#8A93AD}
.lvt button.on svg{color:#1652F0}
.lv{padding:0;overflow:hidden}
.lv-bar{display:flex;align-items:center;gap:12px;height:44px;padding:0 10px 0 16px;background:#F7F9FD;border-bottom:1.5px solid #EEF1F7}
.lv-dots{display:flex;gap:6px}
.lv-dots i{width:9px;height:9px;border-radius:50%;background:#D6DDEE}
.lv-url{flex:1;height:26px;display:flex;align-items:center;padding:0 12px;border-radius:999px;background:#FFFFFF;font-size:12px;color:#8A93AD}
.lv-full{display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 12px;border-radius:999px;font-size:13px;font-weight:600;text-decoration:none}
.lv-full:hover{background:#EAF0FF}
.lv-hero{position:relative;display:grid;grid-template-columns:minmax(0,1fr) 200px;gap:28px;align-items:center;padding:28px 28px 24px 28px;background:linear-gradient(160deg,#0B1433,#13296E 70%,#1A45C7);color:#FFFFFF;overflow:hidden}
.lv-hero::after{content:'';position:absolute;right:-80px;top:-120px;width:360px;height:360px;border-radius:50%;background:radial-gradient(circle,rgba(92,134,255,.42),rgba(92,134,255,0) 65%)}
.lv-k{font-size:12.5px;font-weight:500;color:#9DB8F7}
.lv-hero h2{margin:8px 0 0 0;font-size:28px;line-height:1.15;font-weight:600;letter-spacing:-0.025em}
.lv-hero p{margin:10px 0 0 0;font-size:15px;line-height:1.55;color:rgba(255,255,255,.76)}
.lv-by{margin-top:16px;display:flex;align-items:center;gap:10px;font-size:13px;color:rgba(255,255,255,.8)}
.lv-by .avs .av{box-shadow:0 0 0 2px #13296E}
.lv-cv{position:relative;z-index:1;height:128px;border-radius:16px;background:radial-gradient(circle at 85% 20%,rgba(92,134,255,.85),rgba(92,134,255,0) 60%),linear-gradient(140deg,#1652F0,#0B1433);box-shadow:0 20px 40px -18px rgba(0,0,0,.6),inset 0 0 0 1px rgba(255,255,255,.12);overflow:hidden;animation:lvFloat 6s ease-in-out infinite}
.lv-cv i{position:absolute;left:16px;bottom:12px;font-style:normal;font-size:32px;font-weight:600;letter-spacing:-0.03em}
.lv-cv em{position:absolute;right:16px;height:6px;border-radius:6px;background:rgba(255,255,255,.24)}
.lv-cv em:nth-of-type(1){top:20px;width:72px}.lv-cv em:nth-of-type(2){top:34px;width:48px;background:rgba(255,255,255,.42)}.lv-cv em:nth-of-type(3){top:48px;width:60px}
@keyframes lvFloat{50%{transform:translateY(-5px) rotate(-1deg)}}
.lv-ph{display:flex;flex-wrap:wrap;gap:8px;padding:16px 28px;border-bottom:1.5px solid #F0F2F8}
.lv-p{display:inline-flex;align-items:center;gap:7px;height:34px;padding:0 13px;border-radius:999px;border:1.5px dashed #CBD3E6;color:#5B6582;font-size:13px;font-weight:500}
.lv-p svg{color:#8A93AD}
.lv-p .dlp-c{width:16px;height:16px}
.lv-p.ok{border-style:solid;border-color:#CFE8DB;background:#F2FAF5;color:#0F6B45}
.lv-p.ok svg{color:#0F6B45}
.lv-g{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:28px;padding:22px 28px 26px 28px}
.lv-g h3{margin:0 0 12px 0;font-size:15px;font-weight:600}
.lv-lo{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px}
.lv-lo li{display:grid;grid-template-columns:22px minmax(0,1fr);gap:10px;font-size:14px;line-height:1.45;color:#3A4566}
.lv-lo li > span{width:22px;height:22px;border-radius:50%;background:#E7F5EE;color:#0F6B45;display:flex;align-items:center;justify-content:center}
.lv-lo li.warn > span{background:#FFF4E0;color:#B76E00}
.lv-lo li.warn{color:#8A5A00}
.lv-cu{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;position:relative}
.lv-cu::before{content:'';position:absolute;left:13px;top:14px;bottom:14px;width:2px;background:linear-gradient(180deg,#1652F0,#C9D7FA)}
.lv-cu li{position:relative;display:grid;grid-template-columns:28px minmax(0,1fr) auto;align-items:center;gap:12px;min-height:40px}
.lv-cu b{z-index:1;width:28px;height:28px;border-radius:50%;background:#FFFFFF;border:2px solid #1652F0;color:#1652F0;font-size:12px;font-weight:600;display:flex;align-items:center;justify-content:center;box-sizing:border-box}
.lv-cu span{font-size:14px;font-weight:500}
.lv-cu em{font-style:normal;font-size:12.5px;color:#8A93AD}
.cvw{padding:22px}
.cvw-g{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.cvw-c{display:flex;align-items:center;gap:14px;padding:16px;border-radius:16px;background:#F7F9FD}
.cvw-n{width:36px;height:36px;flex-shrink:0;border-radius:12px;background:#1652F0;color:#FFFFFF;font-size:14px;font-weight:600;display:flex;align-items:center;justify-content:center}
.cvw-c div{display:flex;flex-direction:column;gap:2px;min-width:0}
.cvw-c b{font-size:14.5px;font-weight:600}
.cvw-c span{font-size:12.5px;color:#5B6582}
.sv-s .ds-ghost.sm{height:44px}
.ws-h{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px}
.ws-h .rx-k{margin:0}
.ws-h .ds-tag{height:24px;font-size:11.5px}
.ws-g{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:6px}
.ws-s{display:flex;flex-direction:column;gap:2px;padding:10px 12px;border-radius:12px;background:#F7F9FD}
.ws-s em{font-style:normal;font-size:12px;color:#5B6582}
.ws-s b{display:flex;align-items:center;gap:6px;font-size:16px;font-weight:600}
.ws-s b .dlp-c{width:18px;height:18px}
.ws-s.ns{background:#FFFFFF;border:1.5px dashed #D6DDEE}
.ws-s.ns b{font-size:13.5px;font-weight:500;color:#8A93AD}
.ws-l{display:block;margin:16px 0 8px 0;font-size:12.5px;font-weight:500;color:#8A93AD}
.ws-r{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:8px}
.ws-r li{display:grid;grid-template-columns:20px minmax(0,1fr);column-gap:10px;align-items:start}
.ws-r li > span{grid-row:1 / span 2;width:20px;height:20px;border-radius:50%;background:#E7F5EE;color:#0F6B45;display:flex;align-items:center;justify-content:center;font-size:12px}
.ws-r li.off > span{background:#F1F3F8;color:#8A93AD}
.ws-r b{font-size:13.5px;font-weight:600}
.ws-r li.off b{color:#5B6582;font-weight:500}
.ws-r em{font-style:normal;font-size:12px;color:#5B6582}
.ws-k{margin-top:14px;padding-top:12px;border-top:1.5px solid #F0F2F8;display:flex;flex-direction:column;gap:3px}
.ws-k span{font-size:12px;color:#8A93AD}
.ws-k b{font-size:13.5px;font-weight:500;line-height:1.45}
.mk{padding:20px 22px 24px 22px;overflow:hidden}
.mk-h{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px}
.mk-h .rx-k{margin:0}
.mk-row{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.25fr) minmax(0,1fr);gap:16px;align-items:center}
.mk-g{display:flex;flex-direction:column;gap:10px;padding:12px;border-radius:16px;border:1.5px solid #EEF1F7;opacity:.55;-webkit-mask-image:linear-gradient(90deg,#000,rgba(0,0,0,.25));mask-image:linear-gradient(90deg,#000,rgba(0,0,0,.25))}
.mk-g:last-child{-webkit-mask-image:linear-gradient(270deg,#000,rgba(0,0,0,.25));mask-image:linear-gradient(270deg,#000,rgba(0,0,0,.25))}
.mk-gc{height:96px;border-radius:12px;background:#EEF1F7}
.mk-gl{height:10px;border-radius:6px;background:#EEF1F7}
.mk-gl.s{width:70%}.mk-gl.t{width:45%}
.mk-c{position:relative;transform:scale(1.02);box-shadow:0 30px 60px -30px rgba(22,82,240,.55),0 0 0 1.5px #C9D7FA;animation:mkIn .8s cubic-bezier(.2,.8,.2,1) .3s both}
@keyframes mkIn{from{opacity:0;transform:translateY(14px) scale(.98)}}
.mk-k{display:block;padding:12px 14px 0 14px;font-size:11.5px;font-weight:500;color:#5B6582}
.mk-c b{padding-top:4px}
.mk-by{margin:6px 0 0 0 !important;display:flex;align-items:center;gap:8px;font-size:12.5px !important}
.mk-by .avs .av + .av{margin-left:-6px}
.mk-f{display:flex;flex-direction:column;gap:6px;padding:0 14px 14px 14px}
.mk-d{display:flex;align-items:center;gap:6px;height:30px;padding:0 10px;border-radius:10px;border:1.5px dashed #CBD3E6;color:#8A93AD;font-size:12px;font-weight:500}
.mk-d .dlp-c{width:14px;height:14px}
.mk-tb{display:flex;flex-direction:column}
.mk-r{display:grid;grid-template-columns:180px minmax(0,1fr) 150px;align-items:center;gap:16px;padding:12px 0;border-top:1.5px solid #F0F2F8}
.mk-r:first-child{border-top:0;padding-top:0}
.mk-r b{font-size:14.5px;font-weight:600}
.mk-r > span{font-size:14px;color:#3A4566}
.mk-r .ds-tag{justify-self:end}
.mk-r.later > span{color:#8A93AD}
.mk-r.later .ds-tag{border-style:dashed}
.mk-lg ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px}
.mk-lg li{display:flex;align-items:center;justify-content:space-between;gap:10px;font-size:13px;color:#3A4566}
.mk-lg li .ds-tag{order:2}
.lp-cnt{font-size:14px;color:#5B6582}
.lp-cnt b{font-size:18px;font-weight:600;color:#0B1433;margin-right:2px}
.lpu{padding:20px 22px}
.lpu-c{display:flex;align-items:center;flex-wrap:wrap;gap:0}
.lpu-n{display:flex;flex-direction:column;gap:2px;padding:12px 18px;border-radius:16px;background:#F5F8FF;border:1.5px solid #DCE5FB;animation:lpuIn .5s ease both}
.lpu-n:nth-child(3){animation-delay:.15s}.lpu-n:nth-child(5){animation-delay:.3s}
@keyframes lpuIn{from{opacity:0;transform:translateX(-8px)}}
.lpu-n em{font-style:normal;font-size:11.5px;font-weight:500;color:#8A93AD}
.lpu-n b{font-size:16px;font-weight:600}
.lpu-n.on{background:#1652F0;border-color:#1652F0;color:#FFFFFF;box-shadow:0 14px 28px -14px rgba(22,82,240,.8)}
.lpu-n.on em{color:rgba(255,255,255,.75)}
.lpu-c > i{width:28px;height:2px;background:linear-gradient(90deg,#9DB8F7,#1652F0);position:relative}
.lpu-c > i::after{content:'';position:absolute;right:-1px;top:-3px;border:4px solid transparent;border-left:6px solid #1652F0;border-right:0}
.lpu-a{margin-top:16px;padding-top:14px;border-top:1.5px solid #F0F2F8;display:flex;align-items:center;justify-content:space-between;gap:12px}
.lp{padding:6px 22px}
.lp-r{display:grid;grid-template-columns:150px minmax(0,1fr) auto auto;align-items:center;gap:16px;padding:14px 0;border-top:1.5px solid #F0F2F8}
.lp-r:first-child{border-top:0}
.lp-l{font-size:13.5px;font-weight:500;color:#5B6582}
.lp-v{font-size:14.5px;font-weight:500;line-height:1.45}
.lp-r.ns .lp-v{color:#8A5A00}
.lp-r.inf{position:relative}
.lp-r.inf::before{content:'';position:absolute;left:-22px;top:12px;bottom:12px;width:3px;border-radius:0 3px 3px 0;background:#E0A030}
.lp-a{display:flex;align-items:center;gap:10px}
.lp-ok{gap:6px}
.lp-ok svg{display:none}
.lp-ok.on{background:#E7F5EE;border-color:#BFE3CF;color:#0F6B45}
.lp-ok.on svg{display:block}
.crv{display:flex;align-items:center;gap:16px;padding:16px 18px;border-radius:20px;background:linear-gradient(160deg,#FFF1CF,#FFFAEB);border:1.5px solid #F4D98E}
.crv > div{flex:1;min-width:0}
.crv b{font-size:15px;font-weight:600;color:#5A3B00}
.crv p{margin:3px 0 0 0;font-size:13.5px;line-height:1.5;color:#6B4A00}
.crv .ds-ghost{background:#FFFFFF;border-color:#F0D08A;color:#5A3B00;gap:7px}
.crv .ds-ghost svg{color:#C08A1E}
.nr-w{margin:0 !important}
.nr-w b{margin-right:4px}
.nr-s{display:flex;align-items:baseline;gap:10px;margin-top:4px}
.nr-s b{font-size:17px;font-weight:600}
.nr-s span{font-size:13px;color:#8A93AD}
.nr{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;align-items:start}
.nr-a{padding:16px 18px 6px 18px;border-radius:20px;background:#FFFFFF;border:1.5px solid #E6EAF3;animation:nrIn .5s ease both;animation-delay:calc(var(--i) * 70ms + 150ms)}
@keyframes nrIn{from{opacity:0;transform:translateY(8px)}}
.nr-a header{display:flex;align-items:center;gap:10px;margin-bottom:6px}
.nr-a header b{flex:1;font-size:15px;font-weight:600}
.nr-a header .ds-tag{height:24px;font-size:11.5px}
.nr-i{width:32px;height:32px;border-radius:10px;background:#FFF4E0;color:#B76E00;display:flex;align-items:center;justify-content:center}
.nr-a.clear .nr-i{background:#E7F5EE;color:#0F6B45}
.nr-a ul{list-style:none;margin:0;padding:0}
.nr-a li{padding:12px 0;border-top:1.5px solid #F0F2F8}
.nr-a li:first-child{border-top:0}
.nr-a li p{margin:0;font-size:14px;line-height:1.5;color:#3A4566}
.nr-f{margin-top:10px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap}
.nr-f .ds-link{display:inline-flex;align-items:center;gap:5px}
.ds-chip.xs{height:30px;padding:0 11px;font-size:12.5px;gap:5px}
.nr-c svg{display:none}
.nr-c.on svg{display:block}
.nr-ok{display:flex;align-items:center;gap:8px;margin:6px 0 12px 0;font-size:13.5px;color:#0F6B45}
.nr-sum ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:9px}
.nr-sum li{display:grid;grid-template-columns:minmax(0,1fr) 60px 16px;align-items:center;gap:8px;font-size:13px;color:#3A4566}
.nr-sum li i{height:6px;border-radius:6px;background:linear-gradient(90deg,#E0A030,#F4C66A);width:calc(var(--w) * 50%);transform-origin:left;animation:ldGrow .9s cubic-bezier(.2,.8,.2,1) .3s both}
.nr-sum li b{font-size:12.5px;font-weight:600;text-align:right}
.nr-sum li.z b{color:#0F6B45}
.rd-h{display:grid;grid-template-columns:auto minmax(0,1fr) auto;align-items:center;gap:28px;padding:22px 26px;background:linear-gradient(120deg,#FFF8EA,#FFFFFF 60%);border-color:#F4DDAA}
.rd-r{position:relative;width:108px;height:108px}
.rd-r > span{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}
.rd-r b{font-size:26px;font-weight:600;letter-spacing:-0.02em;color:#8A5A00}
.rd-r em{font-style:normal;font-size:12px;color:#8A5A00}
.rd-s{display:flex;flex-direction:column;gap:10px;min-width:0}
.rd-s > b{font-size:20px;font-weight:600;letter-spacing:-0.01em}
.rd-b{display:flex;gap:4px}
.rd-b i{flex:1;height:8px;border-radius:6px;background:#E0A030;transform-origin:left;animation:ldGrow .7s ease both}
.rd-b i.p{background:#0F6B45}
.rd-b i:nth-child(2){animation-delay:.08s}.rd-b i:nth-child(3){animation-delay:.16s}.rd-b i:nth-child(4){animation-delay:.24s}.rd-b i:nth-child(5){animation-delay:.32s}.rd-b i:nth-child(6){animation-delay:.4s}.rd-b i:nth-child(7){animation-delay:.48s}
.rd-l{display:flex;align-items:center;gap:6px;font-size:12.5px;color:#5B6582}
.rd-l i{width:8px;height:8px;border-radius:50%}
.rd-l i.p{background:#0F6B45}.rd-l i.f{background:#E0A030;margin-left:10px}
.rd-h .ds-ghost{gap:8px;background:#FFFFFF}
.rd-h .ds-ghost svg{color:#B76E00}
.rd{columns:2;column-gap:14px}
.rd-g{break-inside:avoid;margin:0 0 14px 0;padding:16px 18px 10px 18px;animation:nrIn .5s ease both;animation-delay:calc(var(--i) * 60ms + 150ms)}
.rd-g header{display:flex;align-items:center;gap:10px;margin-bottom:8px}
.rd-g header b{flex:1;font-size:15px;font-weight:600}
.rd-g header .ds-tag{height:24px;font-size:11.5px}
.rd-i{width:32px;height:32px;border-radius:10px;background:#FFF4E0;color:#B76E00;display:flex;align-items:center;justify-content:center}
.rd-g.pass .rd-i{background:#E7F5EE;color:#0F6B45}
.rd-g ul{list-style:none;margin:0;padding:0}
.rd-g li{display:flex;align-items:center;gap:10px;min-height:36px;font-size:13.5px;color:#3A4566}
.rd-g li > span{width:20px;height:20px;flex-shrink:0;border-radius:50%;display:flex;align-items:center;justify-content:center}
.rd-g li.ok > span{background:#E7F5EE;color:#0F6B45}
.rd-g li.no{margin:4px -8px;padding:6px 8px;border-radius:12px;background:#FFF8EA}
.rd-g li.no > span{background:#FFE7B8;color:#8A5A00}
.rd-g li.no b{flex:1;font-weight:500;color:#0B1433}
.rd-g li .ds-ghost{background:#FFFFFF}
.is-t{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.is-k{position:relative;display:grid;grid-template-columns:auto minmax(0,1fr);column-gap:12px;align-items:center;padding:16px 18px;border-radius:18px;background:#FFFFFF;border:1.5px solid #E6EAF3;color:#0B1433;text-decoration:none;overflow:hidden;transition:transform .2s ease}
.is-k:hover{transform:translateY(-2px)}
.is-k::before{content:'';position:absolute;left:0;top:0;bottom:0;width:4px;background:var(--c)}
.is-k b{grid-row:1 / span 2;font-size:32px;font-weight:600;letter-spacing:-0.03em;color:var(--c)}
.is-k span{font-size:15px;font-weight:600}
.is-k em{font-style:normal;font-size:12.5px;color:#5B6582}
.is-k.bl,.is.bl{--c:#B76E00;--cb:#FFF4E0}
.is-k.rc,.is.rc{--c:#1652F0;--cb:#EAF0FF}
.is-k.ad,.is.ad{--c:#5B6582;--cb:#F1F3F8}
.is{padding:6px 22px 8px 22px}
.is header{display:flex;align-items:center;gap:10px;padding:14px 0 6px 0}
.is header b{font-size:16px;font-weight:600}
.is header em{font-style:normal;font-size:13px;color:#5B6582}
.is-d{width:10px;height:10px;border-radius:50%;background:var(--c);box-shadow:0 0 0 4px var(--cb)}
.is ol{list-style:none;margin:0;padding:0}
.is-r{display:grid;grid-template-columns:28px minmax(0,1fr) auto;align-items:center;gap:14px;padding:13px 0;border-top:1.5px solid #F0F2F8}
.is-r:first-child{border-top:0}
.is-n{width:28px;height:28px;border-radius:50%;background:var(--cb);color:var(--c);font-size:12.5px;font-weight:600;display:flex;align-items:center;justify-content:center}
.is-b{display:flex;flex-direction:column;gap:2px;min-width:0}
.is-b b{font-size:14.5px;font-weight:600}
.is-b span{font-size:13px;color:#5B6582}
.is-a{display:flex;align-items:center;gap:14px}
.is-a .ds-link{display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
.ds-btn.is-dis{background:#C9D2E6;box-shadow:none;cursor:not-allowed;color:#FFFFFF}
.ds-btn.is-dis:hover{background:#C9D2E6;transform:none}
.ds-btn.is-dis .ob-arrow{color:#8A93AD}
.is-sv .sv-s{display:inline-flex;align-items:center;gap:8px;color:#8A5A00}
.is-sv .sv-s svg{color:#B76E00}
.mst-n{width:20px;height:20px;border-radius:50%;background:#F1F3F8;color:#5B6582;font-size:11.5px;font-weight:600;display:inline-flex;align-items:center;justify-content:center}
.mst-i.on .mst-n{background:#1652F0;color:#FFFFFF}
@media (max-width: 1180px){.rd{columns:1}.nr{grid-template-columns:minmax(0,1fr)}.mk-row{grid-template-columns:minmax(0,1fr)}.mk-g{display:none}}
@media (max-width: 960px){
.pp-main .pg-h .ds-seg{width:100%}
.lvt button{flex:1}
.lv-bar{display:none}
.lv-hero{grid-template-columns:minmax(0,1fr);padding:22px 18px;gap:18px}
.lv-cv{display:none}
.lv-hero h2{font-size:22px}
.lv-hero p{font-size:14px}
.lv-by{align-items:flex-start}
.lv-ph{padding:14px 16px;flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none}
.lv-ph::-webkit-scrollbar{display:none}
.lv-p{flex-shrink:0;white-space:nowrap}
.lv-g{grid-template-columns:minmax(0,1fr);gap:22px;padding:18px 16px 20px 16px}
.cvw{padding:14px}
.cvw-g{grid-template-columns:minmax(0,1fr)}
.sv-s:has(.ds-ghost){display:flex;width:100%;order:2}
.sv-s .ds-ghost{width:100%}
.ws-g{grid-template-columns:repeat(2,minmax(0,1fr))}
.mk{padding:16px}
.mk-r{grid-template-columns:minmax(0,1fr) auto;gap:4px 12px;padding:12px 0}
.mk-r > span{grid-column:1;grid-row:2;font-size:13px}
.mk-r .ds-tag{grid-row:1 / span 2;grid-column:2}
.wk-r > .mk-lg{display:none}
.pg-hr:has(.lp-cnt){width:100%;justify-content:space-between}
.lpu{padding:16px}
.lpu-n{padding:10px 12px}
.lpu-n b{font-size:14px}
.lpu-c > i{width:14px}
.lp{padding:2px 16px}
.lp-r{grid-template-columns:minmax(0,1fr) auto;gap:6px 12px}
.lp-l{grid-column:1}
.lp-r .ds-tag{grid-column:2;grid-row:1;justify-self:end}
.lp-v{grid-column:1 / -1}
.lp-a{grid-column:1 / -1}
.lp-r.inf::before{left:-16px}
.crv{flex-wrap:wrap;padding:14px}
.crv .ds-ghost{width:100%}
.nr-a{padding:14px 14px 4px 14px}
.rd-h{grid-template-columns:auto minmax(0,1fr);gap:16px;padding:18px 16px}
.rd-r,.rd-r svg{width:84px;height:84px}
.rd-r b{font-size:20px}
.rd-h .ds-ghost{grid-column:1 / -1}
.rd-s > b{font-size:17px}
.rd-g{padding:14px 14px 8px 14px}
.is-t{display:flex;overflow-x:auto;margin:0 -16px;padding:0 16px 4px 16px;scrollbar-width:none}
.is-t::-webkit-scrollbar{display:none}
.is-k{flex:0 0 72%;box-sizing:border-box}
.is{padding:4px 16px 6px 16px}
.is-r{grid-template-columns:24px minmax(0,1fr);gap:8px 12px;align-items:start}
.is-n{width:24px;height:24px;font-size:11.5px}
.is-a{grid-column:2;justify-content:space-between;flex-wrap:wrap;gap:8px 12px}
.lvt button{white-space:nowrap;padding:0 10px;font-size:13px}
.is-sv .sv-s{display:flex;justify-content:center;font-size:13px}
}
'''

SUBMIT_CSS = open(os.path.join(HERE, 'submit_base.css')).read() + r'''
.cl{grid-template-columns:minmax(0,1fr) 600px}
.cl-steps{max-width:460px}
.cl-steps li{font-size:12px}
.cl-nx{margin-top:32px}
.cl-nx > span{display:block;margin-bottom:10px}
.cl-nx p{margin:0;font-size:14px;line-height:1.55;color:#3A4566}
.cl-nx.am{background:#FFF8EA;border-color:#F4DDAA}
.cl-nx.am > span{color:#8A5A00}
.cl-nx.am .ds-ghost{margin-top:14px;background:#FFFFFF}
.det-g{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:6px}
.det-g span{display:flex;flex-direction:column;gap:1px;padding:10px;border-radius:12px;background:#F7F9FD}
.det-g b{font-size:16px;font-weight:600}
.det-g em{font-style:normal;font-size:11.5px;line-height:1.3;color:#5B6582}
.fi dl{margin:0;display:flex;flex-direction:column}
.fi dl div{display:flex;justify-content:space-between;gap:12px;padding:8px 0;border-top:1.5px solid #F0F2F8;font-size:13.5px}
.fi dl div:first-child{border-top:0;padding-top:0}
.fi dt{color:#5B6582}
.fi dd{margin:0;font-weight:600}
.fi .ds-link{display:inline-block;margin-top:10px}
.pf{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px}
.pf li{display:grid;grid-template-columns:20px minmax(0,1fr);gap:10px;font-size:13.5px;line-height:1.45;color:#3A4566}
.pf li svg{margin-top:4px;width:20px;height:20px;padding:5px;box-sizing:border-box;border-radius:50%;background:#E7F5EE;color:#0F6B45}
.iqs{margin-top:18px;display:flex;flex-direction:column}
.iq{display:flex;flex-direction:column;gap:10px;padding:16px 0;border-top:1.5px solid #F0F2F8}
.iq:first-child{border-top:0;padding-top:4px}
.iq-t{display:flex;flex-direction:column;gap:3px}
.iq-t b{font-size:15px;font-weight:600}
.iq-t > span{font-size:13px;line-height:1.45;color:#5B6582}
.iq.row{flex-direction:row;align-items:center;justify-content:space-between;gap:20px}
.iq.row .ds-seg{flex-shrink:0;width:150px}
.iq-pf{display:inline-flex;align-items:center;gap:5px;margin-left:4px;height:22px;padding:0 9px;border-radius:999px;background:#EAF0FF;color:#0E3BB8;font-size:11.5px;font-weight:500;vertical-align:1px}
.iq-pf svg{width:11px;height:11px}
.dc-l{display:block;margin:18px 0 8px 0;font-size:12.5px;font-weight:500;color:#8A93AD}
.dc{display:flex;flex-direction:column;gap:8px}
.dc-r{display:flex;align-items:flex-start;gap:12px;padding:13px 14px;border-radius:14px;border:1.5px solid #E6EAF3;background:#FFFFFF;font-family:inherit;font-size:14px;line-height:1.5;color:#0B1433;text-align:left;cursor:pointer;transition:border-color .2s ease,background .2s ease}
.dc-r:hover{border-color:#AFC1F5}
.dc-b{width:20px;height:20px;flex-shrink:0;margin-top:1px;box-sizing:border-box;border-radius:6px;border:1.5px solid #CBD3E6;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.dc-b svg{opacity:0;transform:scale(.6);transition:opacity .2s ease,transform .2s ease}
.dc-r.on{border-color:#1652F0;background:#F5F8FF}
.dc-r.on .dc-b{border-color:#1652F0;background:#1652F0}
.dc-r.on .dc-b svg{opacity:1;transform:none}
.cr-l{list-style:none;margin:0;padding:2px 16px;border:1.5px solid #E6EAF3;border-radius:18px}
.cr-r{display:flex;align-items:center;gap:12px;min-height:52px;border-top:1.5px solid #F0F2F8}
.cr-r:first-child{border-top:0}
.cr-s{display:flex}
.cr-t{flex:1;min-width:0;display:flex;flex-direction:column;gap:5px}
.cr-t b{font-size:14.5px;font-weight:600}
.cr-t em{font-style:normal;font-size:12.5px;color:#1652F0}
.cr-pb{display:block;width:160px;height:6px;border-radius:6px;background:#EAF0FF;overflow:hidden}
.cr-pb i{display:block;height:100%;border-radius:6px;background:#1652F0}
.cr-r.pr{padding:10px 0}
.cr-r .ds-tag{height:24px;font-size:11.5px}
.cr-l.na .cr-t b{color:#5B6582;font-weight:500}
.st.na{border:1.5px dashed #CBD3E6;color:#8A93AD;font-size:11px}
.cr-na{font-size:12.5px;color:#8A93AD;text-align:right}
.vs-seats{margin-top:18px;display:flex;align-items:stretch;gap:0}
.vs-s{flex:1;display:flex;flex-direction:column;align-items:flex-start;gap:4px;padding:16px;border-radius:18px;background:#F7F9FD;border:1.5px solid #E6EAF3;animation:obIn .5s ease .2s both}
.vs-s.lead{background:#F5F8FF;border-color:#C9D7FA;animation-delay:.35s}
.vs-i{width:40px;height:40px;margin-bottom:6px;border-radius:12px;background:#FFFFFF;color:#1652F0;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 14px -8px rgba(22,82,240,.5)}
.vs-s b{font-size:14.5px;font-weight:600}
.vs-s em{font-style:normal;font-size:12.5px;color:#5B6582}
.vs-x{width:28px;align-self:center;height:2px;background:repeating-linear-gradient(90deg,#9DB8F7 0 4px,transparent 4px 8px)}
.vs-l{display:inline-flex;align-items:center;gap:4px;height:22px;padding:0 8px;border-radius:999px;background:#0B1433;color:#FFFFFF;font-size:11.5px;font-weight:500}
.py-dl .sub dt{color:#0B1433;font-weight:500}
.py-dl .sub{background:linear-gradient(90deg,#F7F9FD,#FFFFFF)}
.py-dl .tx dd{font-size:14px;text-align:right}
.py-tot dd .cr-c{margin-right:2px}
.py-note{display:flex;align-items:center}
.bp{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.bp li{display:flex;align-items:center;gap:10px;padding:11px 12px;border-radius:14px;background:#F7F9FD;font-size:13.5px;font-weight:500}
.bp li.to{background:#FFFFFF;border:1.5px dashed #D6DDEE;color:#3A4566}
.bp li span:not(.st){flex:1}
.wl{margin-top:16px;padding:16px 18px;border-radius:18px;border:1.5px solid #E6EAF3;background:linear-gradient(160deg,#F5F8FF,#FFFFFF)}
.wl-h{display:flex;align-items:center;gap:10px;margin-bottom:8px}
.wl-h b{font-size:14.5px;font-weight:600}
.wl dl{margin:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.wl dl div{display:flex;flex-direction:column;gap:2px}
.wl dt{font-size:12px;color:#5B6582}
.wl dd{margin:0;font-size:17px;font-weight:600;font-variant-numeric:tabular-nums}
.wl .r dd{color:#0F6B45}
.wl.short{background:linear-gradient(160deg,#FFF8EA,#FFFFFF);border-color:#F4DDAA}
.wl.short .r dd{color:#8A93AD}
.wl-bar{margin-top:14px;height:8px;border-radius:8px;background:#E6EAF3;overflow:hidden}
.wl-bar i{display:block;height:100%;border-radius:8px;background:linear-gradient(90deg,#1652F0,#5C86FF);transform-origin:left;animation:wlGrow 1s cubic-bezier(.2,.8,.2,1) .3s both}
.wl.short .wl-bar i{background:linear-gradient(90deg,#D99A1E,#F4C66A)}
@keyframes wlGrow{from{transform:scaleX(0)}}
.wl-n{margin:12px 0 0 0;display:flex;align-items:center;gap:8px;font-size:14px;font-weight:600;color:#8A5300}
.wl-n svg{color:#B76E00}
.wl-t{margin-top:10px;display:flex;flex-wrap:wrap;gap:8px}
.ds-btn.is-dis{background:#C9D2E6;box-shadow:none;cursor:not-allowed}
.ds-btn.is-dis:hover{background:#C9D2E6;transform:none}
.ds-btn.is-dis .ob-arrow{color:#8A93AD}
.ko-wrap{flex-grow:1;display:flex;justify-content:center;padding:44px 24px 64px 24px}
.ko{--k:#0F6B45;--kb:#E7F5EE;width:min(620px,100%);display:flex;flex-direction:column;align-items:center;text-align:center}
.ko-h1{margin:14px 0 0 0;font-size:36px;line-height:1.12;font-weight:600;letter-spacing:-0.03em}
.ko-sub{margin:10px 0 0 0;font-size:16px;color:#4A5578}
.ko-tr{list-style:none;margin:28px 0 0 0;padding:0;width:100%;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));position:relative}
.ko-tr::before{content:'';position:absolute;left:12.5%;right:12.5%;top:9px;height:2px;background:#E6EAF3}
.ko-tr::after{content:'';position:absolute;left:12.5%;width:25%;top:9px;height:2px;background:linear-gradient(90deg,#0F6B45,#1652F0);transform-origin:left;animation:wlGrow 1s ease .6s both}
.ko-tr li{position:relative;z-index:1;display:flex;flex-direction:column;align-items:center;gap:8px;font-size:13px;font-weight:500;color:#8A93AD}
.ko-tr i{width:20px;height:20px;box-sizing:border-box;border-radius:50%;border:2px solid #D6DDEE;background:#FFFFFF;display:flex;align-items:center;justify-content:center;color:#FFFFFF}
.ko-tr .dn{color:#0F6B45}.ko-tr .dn i{background:#0F6B45;border-color:#0F6B45}
.ko-tr .on{color:#0B1433;font-weight:600}.ko-tr .on i{border:5px solid #1652F0;box-shadow:0 0 0 5px rgba(22,82,240,.16);animation:koPulse 1.8s ease-out infinite}
@keyframes koPulse{0%{box-shadow:0 0 0 0 rgba(22,82,240,.35)}100%{box-shadow:0 0 0 9px rgba(22,82,240,0)}}
.ko-card{margin-top:26px;width:100%;box-sizing:border-box;padding:18px 22px;border-radius:20px;border:1.5px solid #E6EAF3;background:#FFFFFF;text-align:left}
.ko-cl{display:block;margin-bottom:6px;font-size:12.5px;font-weight:500;color:#8A93AD}
.ko-card dl{margin:0}
.ko-card dl div{display:grid;grid-template-columns:170px minmax(0,1fr);gap:12px;padding:10px 0;border-top:1.5px solid #F0F2F8;font-size:14px}
.ko-card dl div:first-child{border-top:0}
.ko-card dt{color:#5B6582}
.ko-card dd{margin:0;display:flex;align-items:center;flex-wrap:wrap;gap:6px;font-weight:600}
.ko-card dd .cr-c{width:18px;height:18px;font-size:10px}
.ko-note{margin:18px 0 0 0;display:flex;align-items:center;gap:10px;padding:12px 16px;border-radius:14px;background:#F5F8FF;font-size:14px;color:#3A4566;text-align:left}
.ko-note svg{flex-shrink:0;color:#1652F0}
.ko-acts{margin-top:26px;display:flex;flex-direction:column;align-items:center;gap:10px}
@media (max-width: 960px){
.cl{grid-template-columns:minmax(0,1fr);gap:20px}
.cl-sub{display:block;font-size:14px}
.cl-steps{gap:4px}
.cl-steps li span{display:none}
.cl-steps li.on span{display:block;white-space:nowrap}
.cl{display:flex;flex-direction:column}
.cl-side{display:contents}
.cl-side > *{order:0}
.cl-panel{order:1}
.cl-nx{order:2;margin-top:4px;padding:16px}
.cl-nx.det{order:0;margin-top:8px}
.det-g{grid-template-columns:repeat(4,minmax(0,1fr));gap:4px}
.det-g span{padding:8px}
.det-g b{font-size:14px}
.det-g em{font-size:10.5px}
.iq.row{flex-direction:column;align-items:stretch;gap:10px}
.iq.row .ds-seg{width:100%}
.bp{grid-template-columns:minmax(0,1fr)}
.wl dl{grid-template-columns:repeat(3,minmax(0,1fr));gap:6px}
.wl dd{font-size:15px}
.vs-seats{flex-direction:column}
.vs-x{width:2px;height:16px;align-self:center;background:repeating-linear-gradient(180deg,#9DB8F7 0 4px,transparent 4px 8px)}
.cr-pb{width:120px}
.cr-na{display:none}
.ko-wrap{padding:32px 16px 40px 16px}
.ko-h1{font-size:26px}
.ko-sub{font-size:15px}
.ko-tr li{font-size:11.5px;text-align:center}
.ko-card{padding:14px 16px}
.ko-card dl div{grid-template-columns:minmax(0,1fr);gap:2px}
.ko-acts{width:100%}
.ko-acts .ds-btn{width:100%;justify-content:space-between}
}
'''

PREVIEW_CSS = r'''body{background:#FFFFFF}
.cp{font-family:'Google Sans','Google Sans Text','Helvetica Neue',system-ui,sans-serif;color:#0B1433}
.lc,.lp2{min-height:100vh;background:#FFFFFF;font-family:'Google Sans','Google Sans Text','Helvetica Neue',system-ui,sans-serif;color:#0B1433}
.pvs{position:sticky;top:0;z-index:20;display:flex;align-items:center;gap:14px;padding:10px 20px;background:#FFF4DC;border-bottom:1.5px solid #F4D98E}
.pvs-t{flex-shrink:0;height:24px;display:inline-flex;align-items:center;padding:0 10px;border-radius:999px;background:#B76E00;color:#FFFFFF;font-size:11.5px;font-weight:600;letter-spacing:.05em;text-transform:uppercase}
.pvs p{flex:1;margin:0;font-size:13.5px;color:#6B4A00}
.pvs p b{color:#5A3B00;font-weight:600;margin-right:4px}
.pvs-a{display:flex;align-items:center;gap:8px;flex-shrink:0}
.pvs .ds-ghost.sm{height:36px;padding:0 14px;font-size:13.5px;gap:6px;background:#FFFFFF;border-color:#F0D08A}
.lh{display:flex;align-items:center;gap:28px;height:68px;padding:0 32px;border-bottom:1.5px solid #EEF1F7}
.lh-lg{display:flex}
.lh-n{display:flex;gap:22px}
.lh-n a{color:#3A4566;font-size:14.5px;font-weight:500;text-decoration:none}
.lh-s{flex:1;max-width:420px;display:flex;align-items:center;gap:10px;height:42px;padding:0 16px;border-radius:999px;background:#F5F7FB;color:#8A93AD}
.lh-s input{flex:1;border:0;background:none;font-family:inherit;font-size:14px;outline:none}
.lh-na{margin-left:auto;display:inline-flex;align-items:center;height:30px;padding:0 12px;border-radius:999px;border:1.5px dashed #CBD3E6;font-size:12.5px;font-weight:500;color:#5B6582}
.lc-hero{position:relative;overflow:hidden;background:linear-gradient(150deg,#0B1433,#102A7A 70%,#1652F0 130%);color:#FFFFFF}
.lc-hero::after{content:'';position:absolute;right:-100px;top:-180px;width:520px;height:520px;border-radius:50%;background:radial-gradient(circle,rgba(92,134,255,.4),rgba(92,134,255,0) 65%)}
.lc-in{position:relative;z-index:1;width:min(1200px,100%);box-sizing:border-box;margin:0 auto;padding:36px 32px 44px 32px;padding-right:calc(32px + 380px)}
.lc-bc{display:flex;align-items:center;gap:6px;font-size:13px;color:rgba(255,255,255,.65)}
.lc-bc a{color:rgba(255,255,255,.8);text-decoration:none}
.lc-bd{margin-top:18px;display:flex;flex-wrap:wrap;gap:8px}
.lc-bd > span{display:inline-flex;align-items:center;gap:6px;height:30px;padding:0 12px;border-radius:999px;font-size:13px;font-weight:500;background:rgba(255,255,255,.12);color:#FFFFFF}
.lc-gold{background:linear-gradient(135deg,#F7D98B,#C9952C) !important;color:#3D2700 !important}
.lc-cei b{font-weight:600}
.lc-hero h1{margin:14px 0 0 0;font-size:40px;line-height:1.1;font-weight:600;letter-spacing:-0.035em}
.lc-d{margin:12px 0 0 0;max-width:640px;font-size:16.5px;line-height:1.55;color:rgba(255,255,255,.78)}
.lc-st{margin-top:18px;display:flex;flex-wrap:wrap;align-items:center;gap:8px 18px;font-size:14px;color:rgba(255,255,255,.82)}
.lc-r{display:inline-flex;align-items:center;gap:6px}
.lc-r b{font-weight:600;color:#FFFFFF}
.lc-r em{font-style:normal}
.lc-stars{display:inline-flex;gap:2px}
.lc-stars i{width:13px;height:13px;background:#F4C66A;clip-path:polygon(50% 0,61% 35%,98% 35%,68% 57%,79% 91%,50% 70%,21% 91%,32% 57%,2% 35%,39% 35%)}
.lc-stars i.h{background:linear-gradient(90deg,#F4C66A 80%,rgba(255,255,255,.3) 80%)}
.lc-by{margin-top:22px;display:flex;align-items:center;gap:12px;font-size:14px;color:rgba(255,255,255,.8)}
.lc-by b{color:#FFFFFF;font-weight:600}
.lc-av{background:linear-gradient(140deg,#5C86FF,#1652F0) !important;color:#FFFFFF !important;font-size:13px !important}
.lc-body{width:min(1200px,100%);box-sizing:border-box;margin:0 auto;padding:0 32px 64px 32px;display:grid;grid-template-columns:minmax(0,1fr) 352px;gap:44px;align-items:start}
.lc-main{min-width:0;padding-top:12px}
.lc-s{padding:30px 0;border-bottom:1.5px solid #EEF1F7}
.lc-sh{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-bottom:16px}
.lc-sh h2{margin:0;font-size:22px;font-weight:600;letter-spacing:-0.02em}
.lc-meta{font-size:13.5px;color:#5B6582}
.lc-ol{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.lc-ol li{display:flex;align-items:flex-start;gap:12px;padding:16px;border-radius:16px;background:#F7F9FD;font-size:14.5px;line-height:1.45}
.lc-ol li > span{width:24px;height:24px;flex-shrink:0;border-radius:50%;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.lc-sk{display:flex;flex-wrap:wrap;gap:8px}
.lc-sk span{display:inline-flex;align-items:center;gap:8px;height:38px;padding:0 14px;border-radius:999px;border:1.5px solid #DCE5FB;background:#F5F8FF;font-size:14px}
.lc-sk b{font-weight:500}
.lc-sk em{font-style:normal;font-size:12px;font-weight:500;color:#0E3BB8;padding-left:8px;border-left:1.5px solid #CBD7F5}
.lc-2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:32px;border-bottom:1.5px solid #EEF1F7}
.lc-2 .lc-s{border-bottom:0}
.lc-ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px}
.lc-ul li{position:relative;padding-left:18px;font-size:14.5px;line-height:1.45;color:#3A4566}
.lc-ul li::before{content:'';position:absolute;left:2px;top:8px;width:6px;height:6px;border-radius:50%;background:#1652F0}
.lc-ul.ck li{padding-left:0;display:flex;align-items:flex-start;gap:10px}
.lc-ul.ck li::before{display:none}
.lc-ul.ck li > span{width:20px;height:20px;flex-shrink:0;border-radius:50%;background:#E7F5EE;color:#0F6B45;display:flex;align-items:center;justify-content:center;margin-top:1px}
.lc-p{margin:14px 0 0 0;font-size:14px;line-height:1.55;color:#5B6582}
.lc-sh + .lc-p{margin-top:0}
.lc-dl{margin:0;display:flex;flex-direction:column;gap:12px}
.lc-dl dt{font-size:12.5px;font-weight:500;color:#8A93AD}
.lc-dl dd{margin:2px 0 0 0;font-size:14.5px;line-height:1.45}
.lc-in5{margin-top:16px;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px}
.lc-in5 span{display:flex;flex-direction:column;gap:2px;padding:14px;border-radius:16px;background:#F7F9FD}
.lc-in5 b{font-size:22px;font-weight:600;letter-spacing:-0.02em}
.lc-in5 em{font-style:normal;font-size:12.5px;color:#5B6582}
.lc-al{display:block;margin:20px 0 10px 0;font-size:13px;font-weight:600}
.lc-cu{border:1.5px solid #E6EAF3;border-radius:18px;overflow:hidden}
.lc-cu details + details{border-top:1.5px solid #EEF1F7}
.lc-cu summary{list-style:none;display:grid;grid-template-columns:minmax(0,1fr) auto 20px;align-items:center;gap:14px;padding:16px 18px;cursor:pointer}
.lc-cu summary::-webkit-details-marker{display:none}
.lc-cu summary b{font-size:15px;font-weight:600}
.lc-cu summary em{font-style:normal;font-size:13px;color:#5B6582}
.lc-cu summary svg{color:#8A93AD;transition:transform .2s ease}
.lc-cu details[open] summary svg{transform:rotate(180deg)}
.lc-cu details[open] summary{background:#F7F9FD}
.lc-cu ol{list-style:none;margin:0;padding:6px 18px 12px 18px;background:#F7F9FD}
.lc-cu li{display:grid;grid-template-columns:18px minmax(0,1fr) auto auto;align-items:center;gap:12px;min-height:42px;font-size:14px;border-top:1.5px solid #EEF1F7}
.lc-cu li:first-child{border-top:0}
.lc-cu li svg{color:#1652F0}
.lc-cu li em{font-style:normal;font-size:13px;color:#5B6582}
.lc-pv{display:inline-flex;align-items:center;height:24px;padding:0 9px;border-radius:999px;background:#EAF0FF;color:#0E3BB8;font-size:12px;font-weight:500}
.lc-pj{display:grid;grid-template-columns:52px minmax(0,1fr);gap:18px;padding:22px;border-radius:20px;background:linear-gradient(160deg,#F5F8FF,#FFFFFF);border:1.5px solid #DCE5FB}
.lc-pji{width:52px;height:52px;border-radius:16px;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.lc-k{font-size:12.5px;font-weight:500;color:#1652F0}
.lc-pj b{display:block;margin-top:4px;font-size:17px;font-weight:600}
.lc-pj p{margin:6px 0 0 0;font-size:14.5px;line-height:1.55;color:#3A4566}
.lc-ce{display:flex;align-items:center;gap:18px;padding:20px;border-radius:20px;border:1.5px solid #E6EAF3}
.lc-cei2{width:56px;height:56px;flex-shrink:0;border-radius:16px;background:#EAF0FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.lc-ce b{font-size:16px;font-weight:600}
.lc-ce p{margin:4px 0 0 0;font-size:14px;line-height:1.5;color:#5B6582}
.lc-rv{display:grid;grid-template-columns:240px minmax(0,1fr);gap:28px;align-items:start}
.lc-rs > b{display:block;font-size:44px;font-weight:600;letter-spacing:-0.03em;line-height:1}
.lc-rs .lc-stars{margin-top:8px}
.lc-rs > em{display:block;margin-top:6px;font-style:normal;font-size:13px;color:#5B6582}
.lc-rs ul{list-style:none;margin:14px 0 0 0;padding:0;display:flex;flex-direction:column;gap:6px}
.lc-rs li{display:grid;grid-template-columns:12px minmax(0,1fr) 34px;align-items:center;gap:8px;font-size:12.5px;color:#5B6582}
.lc-rs li i{height:6px;border-radius:6px;background:#EEF1F7;overflow:hidden}
.lc-rs li i b{display:block;height:100%;border-radius:6px;background:#F4C66A}
.lc-rs li em{font-style:normal;text-align:right}
.lc-q{margin:0;padding:22px;border-radius:20px;background:#F7F9FD}
.lc-q p{margin:0;font-size:15px;line-height:1.6}
.lc-q footer{margin-top:16px;display:flex;align-items:center;gap:10px}
.lc-q footer span:last-child{display:flex;flex-direction:column}
.lc-q footer b{font-size:14px;font-weight:600}
.lc-q footer em{font-style:normal;font-size:12.5px;color:#5B6582}
.lc-cr{display:grid;grid-template-columns:72px minmax(0,1fr);gap:20px}
.lc-crb{display:flex;flex-direction:column;align-items:flex-start;gap:4px}
.lc-crn{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.lc-crn b{font-size:17px;font-weight:600}
.lc-vf{display:inline-flex;align-items:center;gap:5px;height:24px;padding:0 9px;border-radius:999px;background:#E7F5EE;color:#0F6B45;font-size:12px;font-weight:500}
.lc-crb > em{font-style:normal;font-size:13.5px;color:#5B6582}
.lc-crb p{margin:6px 0 0 0;font-size:14.5px;line-height:1.55;color:#3A4566}
.lc-crs{margin:10px 0 14px 0;display:flex;gap:22px}
.lc-crs span{display:flex;flex-direction:column;font-size:12.5px;color:#5B6582}
.lc-crs b{font-size:17px;font-weight:600;color:#0B1433}
.lc-vq{display:grid;grid-template-columns:200px minmax(0,1fr);gap:24px;padding:22px;border-radius:20px;border:1.5px solid #F0DDAE;background:linear-gradient(160deg,#FFFAEB,#FFFFFF 60%)}
.lc-vb{display:flex;flex-direction:column;align-items:center;gap:10px;text-align:center}
.lc-medal{width:60px;height:60px;border-radius:50%;background:linear-gradient(135deg,#F7D98B,#C9952C);color:#3D2700;display:flex;align-items:center;justify-content:center;box-shadow:0 12px 24px -12px rgba(160,110,20,.8)}
.lc-vb > b{font-size:16px;font-weight:600;color:#5A3B00}
.lc-ceir{position:relative;width:76px;height:76px}
.lc-ceir > span{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}
.lc-ceir b{font-size:20px;font-weight:600}
.lc-ceir em{font-style:normal;font-size:10px;color:#6B4A00}
.lc-vt p{margin:0;font-size:14.5px;line-height:1.55;color:#3A4566}
.lc-vd{margin:16px 0 0 0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.lc-vd dt{font-size:12px;color:#8A93AD}
.lc-vd dd{margin:2px 0 0 0;font-size:14px;font-weight:600}
.lc-fine{margin-top:16px !important;font-size:12.5px !important;color:#8A93AD !important}
.lc-faq{border:1.5px solid #E6EAF3;border-radius:18px;overflow:hidden}
.lc-faq details + details{border-top:1.5px solid #EEF1F7}
.lc-faq summary{list-style:none;display:flex;align-items:center;justify-content:space-between;gap:14px;padding:16px 18px;font-size:15px;font-weight:500;cursor:pointer}
.lc-faq summary::-webkit-details-marker{display:none}
.lc-faq summary svg{color:#8A93AD}
.lc-ill{margin:24px 0 0 0;font-size:12.5px;color:#8A93AD}
.lc-buy{position:relative;margin-top:-220px;z-index:5;display:flex;flex-direction:column;gap:14px}
.lc-buy .lc-s{padding:20px;border:1.5px solid #E6EAF3;border-radius:22px;background:#FFFFFF}
.lc-buy .lc-sh{margin-bottom:12px}
.lc-buy .lc-sh h2{font-size:17px}
.lc-buy .lc-vq{grid-template-columns:minmax(0,1fr);gap:14px;padding:0;border:0;background:none}
.lc-buy .lc-s:has(.lc-vq){border-color:#F0DDAE;background:linear-gradient(160deg,#FFFAEB,#FFFFFF 70%)}
.lc-buy .lc-vb{flex-direction:row;text-align:left}
.lc-buy .lc-ceir{margin-left:auto}
.lc-buy .lc-vt p{font-size:13.5px}
.lc-buy .lc-vd{grid-template-columns:repeat(3,minmax(0,1fr));gap:6px}
.lc-buy .lc-vd dd{font-size:12.5px}
.lc-buy .lc-ce{padding:0;border:0;align-items:flex-start;gap:14px}
.lc-buy .lc-cei2{width:44px;height:44px;border-radius:14px}
.lc-buy .lc-ce b{font-size:14.5px}
.lc-buy .lc-ce p{font-size:13px}
.lc-buy .lc-cr{grid-template-columns:52px minmax(0,1fr);gap:14px}
.lc-buy .lc-cr > .av{width:52px !important;height:52px !important}
.lc-buy .lc-crb p{font-size:13.5px}
.lc-bx{border-radius:24px;background:#FFFFFF;border:1.5px solid #E6EAF3;box-shadow:0 30px 60px -30px rgba(11,20,51,.45);overflow:hidden}
.lc-bv{position:relative;display:block;height:150px;background:radial-gradient(circle at 85% 20%,rgba(92,134,255,.85),rgba(92,134,255,0) 60%),linear-gradient(140deg,#1652F0,#0B1433)}
.lc-bv i{position:absolute;left:20px;bottom:14px;font-style:normal;font-size:38px;font-weight:600;letter-spacing:-0.03em;color:#FFFFFF}
.lc-bv em{position:absolute;right:20px;height:7px;border-radius:7px;background:rgba(255,255,255,.24)}
.lc-bv em:nth-of-type(1){top:24px;width:90px}.lc-bv em:nth-of-type(2){top:40px;width:60px;background:rgba(255,255,255,.42)}
.lc-bi{padding:20px;display:flex;flex-direction:column;gap:10px}
.lc-bi > b{font-size:16px;font-weight:600;margin-bottom:2px}
.lc-o{display:grid;grid-template-columns:auto minmax(0,1fr) auto;align-items:center;gap:12px;padding:14px;border-radius:16px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:inherit;color:#0B1433;text-align:left;cursor:pointer}
.lc-o.on{border-color:#1652F0;background:#F5F8FF}
.lc-ot{display:flex;flex-direction:column;gap:2px}
.lc-ot b{font-size:14.5px;font-weight:600}
.lc-ot em{font-style:normal;font-size:12.5px;color:#5B6582}
.lc-op{font-size:18px;font-weight:600;white-space:nowrap}
.lc-op small{font-size:12px;font-weight:500;color:#5B6582}
.lc-cta{width:100%;justify-content:space-between;margin-top:6px}
.ds-btn.is-dis{background:#C9D2E6;box-shadow:none;cursor:not-allowed}
.ds-btn.is-dis:hover{background:#C9D2E6;transform:none}
.ds-btn.is-dis .ob-arrow{color:#8A93AD}
.lc-tn{margin:0;display:flex;align-items:center;gap:6px;font-size:12.5px;color:#5B6582}
.lc-ask{display:flex;align-items:center;gap:10px;margin-top:6px;padding:12px 14px;border-radius:16px;border:1.5px solid #DCE5FB;font-family:inherit;font-size:14px;font-weight:600;color:#0E3BB8;text-align:left;cursor:pointer}
.lp2{display:flex;flex-direction:column;background:#F7F9FD}
.lpt{display:flex;align-items:center;gap:16px;height:64px;padding:0 20px;background:#FFFFFF;border-bottom:1.5px solid #EEF1F7}
.lpt-x{display:inline-flex;align-items:center;gap:8px;height:38px;padding:0 14px 0 10px;border-radius:999px;color:#3A4566;font-size:14px;font-weight:500;text-decoration:none}
.lpt-x:hover{background:#F5F8FF}
.lpt-t{font-size:15px;font-weight:600;padding-left:16px;border-left:1.5px solid #EEF1F7}
.lpt-d{display:inline-flex;align-items:center;gap:6px;height:36px;padding:0 12px;border-radius:999px;background:linear-gradient(160deg,#FFF1CF,#FFFAEB);border:1.5px solid #F4D98E;font-size:13px;color:#6B4A00}
.lpt-d b{font-weight:600;color:#5A3B00}
.lpt-d .dlp-c{width:16px;height:16px}
.lpb{flex-grow:1;display:grid;grid-template-columns:320px minmax(0,1fr)}
.lps{background:#FFFFFF;border-right:1.5px solid #EEF1F7;padding:20px 16px}
.lps-p{display:flex;flex-direction:column;gap:10px;padding:14px 16px;border-radius:16px;background:#F7F9FD}
.lps-p > span{font-size:12.5px;font-weight:500;color:#5B6582}
.lps-r{display:flex;align-items:center;gap:12px}
.lps-r b{font-size:22px;font-weight:600}
.lps-c{margin-top:18px}
.lps-c > b{display:block;padding:0 6px 8px 6px;font-size:13.5px;font-weight:600}
.lps-c ol{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:2px}
.lps-c li{display:grid;grid-template-columns:22px minmax(0,1fr) auto;align-items:center;gap:10px;min-height:42px;padding:0 10px;border-radius:12px;font-size:13.5px;color:#3A4566}
.lps-c li em{font-style:normal;font-size:12px;color:#8A93AD}
.lps-i{width:22px;height:22px;border-radius:50%;background:#F1F3F8;color:#5B6582;display:flex;align-items:center;justify-content:center}
.lps-c li.dn .lps-i{background:#E7F5EE;color:#0F6B45}
.lps-c li.on{background:#F5F8FF;color:#0B1433;font-weight:600;box-shadow:inset 3px 0 0 #1652F0}
.lps-c li.on .lps-i{background:#1652F0;color:#FFFFFF}
.lpm{padding:28px 40px 48px 40px;max-width:900px;box-sizing:border-box;width:100%;margin:0 auto}
.lpv{position:relative;aspect-ratio:16/9;border-radius:20px;overflow:hidden;background:radial-gradient(circle at 75% 25%,rgba(92,134,255,.6),rgba(92,134,255,0) 55%),linear-gradient(140deg,#13296E,#0B1433);box-shadow:0 30px 60px -36px rgba(11,20,51,.8)}
.lpv-p{position:absolute;left:50%;top:50%;width:72px;height:72px;margin:-36px 0 0 -36px;border-radius:50%;background:rgba(255,255,255,.95);color:#1652F0;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 10px rgba(255,255,255,.15);animation:lpvP 2.4s ease-out infinite}
@keyframes lpvP{0%{box-shadow:0 0 0 0 rgba(255,255,255,.35)}100%{box-shadow:0 0 0 22px rgba(255,255,255,0)}}
.lpv-b{position:absolute;left:20px;right:110px;bottom:22px;height:5px;border-radius:5px;background:rgba(255,255,255,.22)}
.lpv-b i{display:block;height:100%;border-radius:5px;background:#FFFFFF}
.lpv-tm{position:absolute;right:20px;bottom:16px;font-size:12.5px;color:rgba(255,255,255,.85)}
.lpm-k{display:block;margin-top:24px;font-size:13px;font-weight:500;color:#1652F0}
.lpm h1{margin:6px 0 0 0;font-size:30px;font-weight:600;letter-spacing:-0.03em}
.lpn{margin-top:18px;padding:20px 22px;border-radius:20px;background:#FFFFFF;border:1.5px solid #E6EAF3}
.lpn b{font-size:15px;font-weight:600}
.lpn p{margin:8px 0 0 0;font-size:15px;line-height:1.65;color:#3A4566}
.lpf{margin-top:24px;display:flex;align-items:center;justify-content:space-between;gap:12px}
.lpf .ds-ghost{gap:8px}
@media (max-width: 1180px){.lh-n{display:none}.lc-in5{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media (max-width: 960px){
.pvs{flex-wrap:wrap;gap:8px 10px;padding:10px 16px}
.pvs p{flex-basis:100%;order:3;font-size:12.5px}
.pvs-a{margin-left:auto}
.pvs-a .ds-ghost span{display:none}
.pvs-a .ds-ghost{width:36px;padding:0;justify-content:center;gap:0}
.pvs-a .ds-ghost svg{flex-shrink:0;width:16px;height:16px}
.lh{height:60px;padding:0 16px;gap:12px}
.lh-s{display:none}
.lh-na{font-size:11.5px;height:28px;padding:0 10px}
.lc-in{padding:24px 16px 30px 16px}
.lc-hero h1{font-size:28px}
.lc-d{font-size:15px}
.lc-st{gap:6px 12px;font-size:13px}
.lc-body{grid-template-columns:minmax(0,1fr);gap:0;padding:0 16px 24px 16px;display:flex;flex-direction:column;align-items:stretch}
.lc-main{min-width:0;width:100%}
.lc-buy{display:contents}
.lc-bx{order:-1;margin-top:-14px}
.lc-buy .lc-s{order:5;margin-top:14px;padding:18px 16px}
.lc-bv{display:none}
.lc-bi{padding:16px}
.lc-s{padding:24px 0}
.lc-sh h2{font-size:19px}
.lc-ol{grid-template-columns:minmax(0,1fr);gap:8px}
.lc-ol li{padding:12px 14px;font-size:14px}
.lc-sk{flex-wrap:nowrap;overflow-x:auto;margin:0 -16px;padding:0 16px;scrollbar-width:none}
.lc-sk::-webkit-scrollbar{display:none}
.lc-sk span{flex-shrink:0}
.lc-2{grid-template-columns:minmax(0,1fr);gap:0}
.lc-2 .lc-s + .lc-s{border-top:1.5px solid #EEF1F7}
.lc-in5{grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.lc-in5 span:first-child{grid-column:1 / -1}
.lc-cu summary{grid-template-columns:minmax(0,1fr) 20px;padding:14px}
.lc-cu summary em{grid-column:1;grid-row:2;font-size:12px}
.lc-cu summary svg{grid-row:1 / span 2;grid-column:2}
.lc-cu ol{padding:4px 14px 10px 14px}
.lc-pj{grid-template-columns:minmax(0,1fr);padding:18px;gap:12px}
.lc-rv{grid-template-columns:minmax(0,1fr);gap:18px}
.lc-cr{grid-template-columns:56px minmax(0,1fr);gap:14px}
.lc-cr > .av{width:56px !important;height:56px !important}
.lc-vq{grid-template-columns:minmax(0,1fr)}
.lc-vb{flex-direction:row;justify-content:flex-start;text-align:left}
.lc-ceir{margin-left:auto}
.lc-vd{grid-template-columns:repeat(3,minmax(0,1fr));gap:6px}
.lc-vd dd{font-size:13px}
.lpt{height:56px;padding:0 12px;gap:10px}
.lpt-x span,.lpt-t{display:none}
.lpb{grid-template-columns:minmax(0,1fr);display:flex;flex-direction:column}
.lps{order:2;border-right:0;border-top:1.5px solid #EEF1F7;padding:16px}
.lpm{padding:0 0 20px 0}
.lpv{border-radius:0}
.lpm-k,.lpm h1,.lpn,.lpf{margin-left:16px;margin-right:16px}
.lpm h1{font-size:23px}
.lpn{padding:16px}
.lpf{flex-direction:column-reverse;align-items:stretch}
.lpf .ds-btn{width:100%;justify-content:space-between}
.lpf .ds-btn span:first-child{white-space:normal;text-align:left}
}
'''

TEAM_CSS = r'''.lc-av.k2{background:linear-gradient(140deg,#3FB58A,#0F6B45) !important}
.lc-av.k3{background:linear-gradient(140deg,#F2B45A,#C2741A) !important}
.lc-av.k4{background:linear-gradient(140deg,#8A9BC4,#4A5578) !important}
.lc-av.k5{background:linear-gradient(140deg,#B48CF0,#7048C8) !important}
.lc-avs{display:inline-flex;align-items:center;flex-shrink:0;text-decoration:none}
.lc-avs > *{margin-left:-10px;box-shadow:0 0 0 2.5px #13296E;transition:margin .25s ease}
.lc-avs > *:first-child{margin-left:0}
.lc-by:hover .lc-avs > *{margin-left:-4px}
.lc-by:hover .lc-avs > *:first-child{margin-left:0}
.lc-more{width:40px;height:40px;border-radius:50%;background:rgba(255,255,255,.26);color:#FFFFFF;font-size:13px;font-weight:600;display:inline-flex;align-items:center;justify-content:center;backdrop-filter:blur(4px)}
.lc-va{color:#FFFFFF;font-weight:500;text-decoration:underline;text-decoration-color:rgba(255,255,255,.4);text-underline-offset:3px}
.lc-va:hover{text-decoration-color:#FFFFFF}
.mtc-p{margin:-6px 0 16px 0 !important}
.mtc{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.mtc-c{position:relative;display:flex;flex-direction:column;align-items:flex-start;gap:10px;padding:20px;border-radius:22px;border:1.5px solid #E6EAF3;background:#FFFFFF;overflow:hidden;transition:transform .25s ease,border-color .25s ease,box-shadow .25s ease;animation:obIn .5s ease both;animation-delay:calc(var(--i) * 90ms + 150ms)}
.mtc-c:hover{transform:translateY(-3px);border-color:#C9D7FA;box-shadow:0 22px 40px -30px rgba(22,82,240,.6)}
.mtc-c.lead{border-color:#C9D7FA;background:linear-gradient(170deg,#F5F8FF,#FFFFFF 45%)}
.mtc-c.lead::before{content:'';position:absolute;left:0;right:0;top:0;height:3px;background:linear-gradient(90deg,#1652F0,#5C86FF)}
.mtc-c header{display:flex;align-items:center;gap:14px}
.mtc-c header > div{display:flex;flex-direction:column;gap:3px;min-width:0}
.mtc-n{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.mtc-n b{font-size:16px;font-weight:600}
.mtc-r{display:inline-flex;align-items:center;height:22px;padding:0 9px;border-radius:999px;background:#EEF1F7;color:#3A4566;font-size:11.5px;font-weight:500}
.mtc-r.lead{background:#EAF0FF;color:#0E3BB8}
.mtc-c em,.cp-l em{font-style:normal;font-size:13px;color:#5B6582}
.mtc-v{display:inline-flex;align-items:center;gap:6px;font-size:12.5px;font-weight:500;color:#0F6B45}
.mtc-v svg{width:16px;height:16px;padding:3px;box-sizing:border-box;border-radius:50%;background:#E7F5EE}
.mtc-s{display:flex;flex-wrap:wrap;gap:4px 14px;font-size:13px;color:#5B6582}
.mtc-s b{color:#0B1433;font-weight:600}
.mtc-st{display:inline-flex;align-items:center;gap:4px}
.mtc-st i{width:12px;height:12px;background:#F4C66A;clip-path:polygon(50% 0,61% 35%,98% 35%,68% 57%,79% 91%,50% 70%,21% 91%,32% 57%,2% 35%,39% 35%)}
.mtc-k{align-self:stretch;margin:2px 0 0 0;padding:10px 12px;border-radius:12px;background:#F7F9FD;font-size:13px;line-height:1.5;color:#0B1433}
.mtc-k span,.cp-l p span{color:#8A93AD}
.mtc-c .ds-link,.cp-l .ds-link{display:inline-flex;align-items:center;gap:5px}
.mtc-c .ds-link{margin-top:auto}
.mtc-c .ds-link svg,.cp-l .ds-link svg{transition:transform .2s ease}
.mtc-c:hover .ds-link svg{transform:translateX(3px)}
.mtc-all{margin-top:14px;width:100%;justify-content:center;gap:10px}
.mtc-sa{display:inline-flex}
.mtc-sa > *{margin-left:-7px;box-shadow:0 0 0 2px #FFFFFF;font-size:9.5px !important}
.mtc-sa > *:first-child{margin-left:0}
.mtc-cp{margin-top:14px;display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:16px;border:1.5px dashed #F0D08A;background:#FFFAEB}
.mtc-cp p{flex:1;margin:0;font-size:13px;line-height:1.5;color:#6B4A00}
.mtc-cp .ds-ghost{flex-shrink:0;gap:7px;background:#FFFFFF;border-color:#F0D08A;color:#5A3B00}
.lc-s.lc-wim{display:none}
.lc-buy .lc-wir .lc-sh{margin-bottom:6px}
.lc-buy .lc-wir .lc-p{font-size:13px}
.lc-buy .lc-wir .lc-in5{margin-top:12px;grid-template-columns:repeat(2,minmax(0,1fr));gap:6px}
.lc-buy .lc-wir .lc-in5 span{padding:10px 12px;border-radius:12px}
.lc-buy .lc-wir .lc-in5 span:first-child{grid-column:1 / -1;flex-direction:row;align-items:baseline;gap:8px}
.lc-buy .lc-wir .lc-in5 b{font-size:18px}
.lc-buy .lc-wir .lc-in5 em{font-size:12px}
.lc-buy .lc-wir .lc-al{margin:14px 0 8px 0;font-size:12.5px}
.lc-buy .lc-wir .lc-ul{gap:7px}
.lc-buy .lc-wir .lc-ul li{font-size:13px}
.lc-main .mtc-cp{display:none}
.lc-buy .lc-s.mtc-cpr{display:flex;flex-direction:column;align-items:flex-start;gap:10px;border:1.5px dashed #F0D08A;background:#FFFAEB}
.mtc-cpr p{margin:0;font-size:13px;line-height:1.55;color:#6B4A00}
.mtc-cpr .ds-ghost{gap:7px;background:#FFFFFF;border-color:#F0D08A;color:#5A3B00}
.mtc-dots{display:none}
.mtc-c.lead header .av{box-shadow:0 0 0 3px #FFFFFF,0 0 0 5px #C9D7FA;animation:mtcR 3.2s ease-in-out infinite}
@keyframes mtcR{50%{box-shadow:0 0 0 3px #FFFFFF,0 0 0 7px rgba(22,82,240,.18)}}
.cp-l .mtc-s{font-size:12.5px;gap:2px 12px}
.cp-o{position:fixed;inset:0;z-index:1000;background:rgba(11,20,51,.38);backdrop-filter:blur(2px);-webkit-backdrop-filter:blur(2px);animation:cpF .3s ease both}
@keyframes cpF{from{opacity:0}}
.cp{position:fixed;z-index:1001;top:0;right:0;bottom:0;width:480px;max-width:100vw;box-sizing:border-box;display:flex;flex-direction:column;background:#FFFFFF;box-shadow:-24px 0 64px rgba(11,20,51,.2);animation:cpIn .5s cubic-bezier(.2,.8,.2,1) both}
@keyframes cpIn{from{transform:translateX(40px);opacity:0}}
.cp-h{display:flex;align-items:flex-start;gap:12px;padding:26px 24px 18px 24px;border-bottom:1.5px solid #EEF1F7}
.cp-h > div{flex:1}
.cp-avs{display:inline-flex;margin-bottom:14px}
.cp-avs > *{margin-left:-8px;box-shadow:0 0 0 2.5px #FFFFFF;font-size:10.5px !important;animation:cpA .5s cubic-bezier(.3,1.4,.5,1) both}
.cp-avs > *:first-child{margin-left:0}
.cp-avs > *:nth-child(2){animation-delay:.06s}.cp-avs > *:nth-child(3){animation-delay:.12s}.cp-avs > *:nth-child(4){animation-delay:.18s}.cp-avs > *:nth-child(5){animation-delay:.24s}
@keyframes cpA{from{transform:scale(.4);opacity:0}}
.cp-h h2{margin:0;font-size:22px;font-weight:600;letter-spacing:-0.015em}
.cp-h p{margin:6px 0 0 0;font-size:14px;line-height:1.55;color:#5B6582}
.cp-l{flex:1;overflow-y:auto;list-style:none;margin:0;padding:8px 24px}
.cp-l li{display:grid;grid-template-columns:44px minmax(0,1fr);align-items:start;column-gap:14px;padding:16px 0;border-top:1.5px solid #F0F2F8;animation:obIn .45s ease both;animation-delay:calc(var(--i) * 70ms + 200ms)}
.cp-l li:first-child{border-top:0}
.cp-l li > div{display:flex;flex-direction:column;gap:4px;min-width:0}
.cp-l .mtc-n b{font-size:15px}
.cp-l em{font-size:12.5px;line-height:1.45}
.cp-l p{margin:2px 0 0 0;font-size:13px;line-height:1.5}
.cp-l .ds-link{grid-column:2;justify-self:start;margin-top:8px;white-space:nowrap}
.cp-l li:hover .ds-link svg{transform:translateX(3px)}
.cp-f{display:flex;justify-content:flex-end;padding:14px 24px;border-top:1.5px solid #EEF1F7}
@media (max-width: 960px){
.lc-in{padding:26px 20px 44px 20px}
.lc-bc{font-size:12.5px}
.lc-bd{margin-top:20px}
.lc-hero h1{margin-top:16px;line-height:1.15}
.lc-d{margin-top:12px;line-height:1.6}
.lc-st{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px 0;margin-top:22px;padding:16px 0;border-top:1px solid rgba(255,255,255,.14);border-bottom:1px solid rgba(255,255,255,.14)}
.lc-st > .lc-r{grid-column:1 / -1;padding-bottom:12px;border-bottom:1px solid rgba(255,255,255,.1)}
.lc-st > span:not(.lc-r){line-height:1.35}
.lc-by{margin-top:18px;align-items:center;gap:12px;font-size:13.5px}
.lc-by > span:last-child{line-height:1.55}
.lc-bx{position:relative;z-index:2;margin-top:-22px}
.lc-bi{padding:20px 18px}
.lc-avs > *,.lc-more{width:30px !important;height:30px !important;font-size:10.5px !important}
.lc-avs > *{margin-left:-7px}
.lc-s.lc-wim{display:block}
.lc-buy .lc-s.lc-wir,.lc-buy .lc-s.mtc-cpr{display:none}
.mtc-dots{display:flex;justify-content:center;gap:6px;margin-top:4px}
.mtc-dots i{width:6px;height:6px;border-radius:6px;background:#D6DDEE}
.mtc-dots i.on{width:18px;background:#1652F0}
.mtc{display:flex;gap:10px;overflow-x:auto;scroll-snap-type:x mandatory;margin:0 -16px;padding:2px 16px 8px 16px;scrollbar-width:none}
.mtc::-webkit-scrollbar{display:none}
.mtc-c{flex:0 0 84%;box-sizing:border-box;scroll-snap-align:start;scroll-margin-left:16px;padding:16px;gap:8px;border-radius:18px}
.mtc-c:hover{transform:none}
.mtc-all{margin-top:8px}
.mtc-c .av{width:44px !important;height:44px !important}
.mtc-n b{font-size:15px}
.lc-main .mtc-cp{display:grid;grid-template-columns:auto minmax(0,1fr);align-items:center;gap:8px 10px;padding:12px}
.mtc-cp .pvs-t{justify-self:start}
.mtc-cp .ds-ghost{grid-column:2;grid-row:1;justify-self:end;height:34px;padding:0 12px;font-size:13px}
.mtc-cp p{grid-column:1 / -1;grid-row:2;font-size:12.5px}
.cp{top:auto;width:100%;max-height:88vh;border-radius:24px 24px 0 0;animation:cpUp .5s cubic-bezier(.2,.8,.2,1) both}
@keyframes cpUp{from{transform:translateY(60px);opacity:0}}
.cp::before{content:'';position:absolute;left:50%;top:8px;width:40px;height:4px;margin-left:-20px;border-radius:4px;background:#D6DDEE}
.cp-h{padding:22px 16px 14px 16px}
.cp-avs{margin-bottom:10px}
.cp-h h2{font-size:19px}
.cp-h p{font-size:13.5px}
.cp-l{padding:4px 16px}
.cp-l li{grid-template-columns:40px minmax(0,1fr);padding:14px 0}
.cp-l li > .av{width:40px !important;height:40px !important}
.cp-l .ds-link{grid-column:2;margin-top:8px;justify-self:start}
.cp-f{padding:12px 16px 16px 16px}
.cp-f .ds-ghost{width:100%;justify-content:center}
}
'''
PREVIEW_CSS += TEAM_CSS

# ======================================================================= write sources
write('Prepare.dc.html', doc('Course Studio · Prepare · shared source', kit.KIT_CSS + '\n' + dash.DASH_CSS + BASE_CSS + CW_CSS + WK_CSS + PREP_CSS, prep_body(), PREP_JS))
write('Submit.dc.html', doc('Submit for validation · shared source', kit.KIT_CSS + '\n' + dash.DASH_CSS + BASE_CSS + WK_CSS + SUBMIT_CSS, submit_body(), SUBMIT_JS))
# ======================================================================= TEAM CREDITS (CR-LEARN-CREATORS-2 / -5 / -PANEL): variants of the course page
TEAM = [('AM', 'Alex Morgan', 'Lead Creator', 'Data Analytics Educator', '12', '18,400', '4.8', 'Course lead · Chapters 1, 4 and 6', ''),
        ('JA', 'John Adeyemi', 'Co-Creator', 'Senior BI Analyst', '4', '3,200', '4.7', 'Chapters 2 and 3 · SQL Joins', 'k2'),
        ('SK', 'Sade Kolawole', 'Co-Creator', 'SQL Trainer for finance teams', '6', '5,100', '4.8', 'Chapter 4 practice sets', 'k3'),
        ('CO', 'Chidi Obi', 'Co-Creator', 'Analytics Engineer', '3', '1,900', '4.6', 'Assessments and answer keys', 'k4'),
        ('RB', 'Rita Bako', 'Co-Creator', 'Data Visualization Lead', '5', '2,700', '4.7', 'Chapter 5 dashboards', 'k5')]
def tav(m, n):
    return '<span class="av lc-av %s" style="width: %dpx; height: %dpx">%s</span>' % (m[8], n, n, m[0])
def trole(m):
    return '<span class="mtc-r%s">%s</span>' % (' lead' if m[2] == 'Lead Creator' else '', m[2])
PANEL_URL = 'LEARN-CREATORS-PANEL.dc.html'
SOLO_BY = '<div class="lc-by">%s<span>Created by <b>Alex Morgan</b> · Data Analytics Educator</span></div>' % (AM % (40, 40))
assert COURSE_PAGE.count(SOLO_BY) == 1
BY2 = '<div class="lc-by"><span class="lc-avs">%s</span><span>Created by <b>Alex Morgan</b> and <b>John Adeyemi</b> · <a class="lc-va" href="#lc-meet">View all creators</a></span></div>' % ''.join(tav(m, 40) for m in TEAM[:2])
BY5 = '<div class="lc-by"><a class="lc-avs" href="%s" aria-label="View all creators">%s<span class="lc-more">+2</span></a><span>Created by <b>Alex Morgan</b>, <b>John Adeyemi</b>, <b>Sade Kolawole</b> and <a class="lc-va" href="%s">2 others</a></span></div>' % (
    PANEL_URL, ''.join(tav(m, 40) for m in TEAM[:3]), PANEL_URL)
def tcard(i, m):
    return ('<article class="mtc-c%s" style="--i: %d"><header>%s<div><span class="mtc-n"><b>%s</b>%s</span><em>%s</em></div></header>'
            '<span class="mtc-v">%s<span>Verified expertise · Data Analytics</span></span>'
            '<div class="mtc-s"><span><b>%s</b> courses</span><span><b>%s</b> learners</span><span class="mtc-st"><b>%s</b><i></i></span></div>'
            '<p class="mtc-k"><span>Contributed:</span> %s</p><a class="ds-link sm" href="#">View profile%s</a></article>') % (
        ' lead' if i == 0 else '', i, tav(m, 52), m[1], trole(m), m[3], ck(10), m[4], m[5], m[6], m[7], ic('arrowr', 13, 2.2))
CP_NOTE = '<div class="mtc-cp"><span class="pvs-t">Creator Preview</span><p>%s</p><a class="ds-ghost sm" href="CREDITS.dc.html">%s<span>Change credits</span></a></div>'
DOTS = lambda n: '<div class="mtc-dots" aria-hidden="true">%s</div>' % ''.join('<i%s></i>' % (' class="on"' if j == 0 else '') for j in range(n))
MEET2 = sec('Meet the creators', ('<p class="lc-p mtc-p">Built by a Lead Creator and 1 Co-Creator.</p><div class="mtc">%s</div>' + DOTS(2) + '%s') % (
    ''.join(tcard(i, m) for i, m in enumerate(TEAM[:2])),
    CP_NOTE % ('Learners see 2 of 4 team members. 1 contributor and 1 reviewer are hidden, and 1 pending invitation is not shown.', ic('users', 15, 2))), 'mt')
MEET5 = sec('Meet the creators', ('<p class="lc-p mtc-p">Built by a Lead Creator and 4 Co-Creators.</p><div class="mtc">%s</div>' + DOTS(4) + '<a class="ds-ghost mtc-all" href="%s"><span class="mtc-sa">%s</span><span>View all 5 creators</span></a>%s') % (
    ''.join(tcard(i, m) for i, m in enumerate(TEAM[:4])), PANEL_URL, ''.join(tav(m, 24) for m in TEAM),
    CP_NOTE % ('Learners see 5 credited creators: 3 names on the page and 4 cards. Everyone is in the panel.', ic('users', 15, 2))), 'mt')
MEET2 = MEET2.replace('<section class="lc-s mt">', '<section class="lc-s mt" id="lc-meet">')
COURSE_PAGE = COURSE_PAGE.replace(SOLO_BY, '<sc-if value="{{t_solo}}" hint-placeholder-val="{{ true }}">%s</sc-if><sc-if value="{{t_2}}" hint-placeholder-val="{{ false }}">%s</sc-if><sc-if value="{{t_5}}" hint-placeholder-val="{{ false }}">%s</sc-if>' % (SOLO_BY, BY2, BY5))
assert COURSE_PAGE.count(_m) == 1
COURSE_PAGE = COURSE_PAGE.replace(_m, '<sc-if value="{{t_solo}}" hint-placeholder-val="{{ true }}">%s</sc-if>' % _m)
_wi = '<section class="lc-s"><div class="lc-sh"><h2>What’s Included'
assert COURSE_PAGE.count(_wi) == 1
CPR = '<section class="lc-s mtc-cpr"><span class="pvs-t">Creator Preview</span><p>%s</p><a class="ds-ghost sm" href="CREDITS.dc.html">%s<span>Change credits</span></a></section>'
_wi0 = COURSE_PAGE.index(_wi); _wis = COURSE_PAGE[_wi0:COURSE_PAGE.index('</section>', _wi0) + len('</section>')]
COURSE_PAGE = COURSE_PAGE.replace(_wis, _wis.replace('<section class="lc-s">', '<section class="lc-s lc-wim">', 1))
assert COURSE_PAGE.count(_c) == 1
COURSE_PAGE = COURSE_PAGE.replace(_c, _c + '<sc-if value="{{t_2}}" hint-placeholder-val="{{ false }}">%s</sc-if><sc-if value="{{t_5}}" hint-placeholder-val="{{ false }}">%s</sc-if>%s' % (
    CPR % ('Learners see 2 of 4 team members. 1 contributor and 1 reviewer are hidden, and 1 pending invitation is not shown.', ic('users', 15, 2)),
    CPR % ('Learners see 5 credited creators: 3 names on the page and 4 cards. Everyone is in the panel.', ic('users', 15, 2)),
    _wis.replace('<section class="lc-s">', '<section class="lc-s lc-wir">', 1)))
_wim = '<section class="lc-s lc-wim">'
assert COURSE_PAGE.count(_wim) == 1
COURSE_PAGE = COURSE_PAGE.replace(_wim, '<sc-if value="{{t_2}}" hint-placeholder-val="{{ false }}">%s</sc-if><sc-if value="{{t_5}}" hint-placeholder-val="{{ false }}">%s</sc-if>%s' % (MEET2, MEET5, _wim))
PANEL = '''<a class="cp-o" href="LEARN-CREATORS-5.dc.html" aria-label="Close"></a>
<aside class="cp" role="dialog" aria-modal="true" aria-label="Course creators"><header class="cp-h"><div><span class="cp-avs" aria-hidden="true">%s</span><h2>Course creators</h2><p>Data Analysis with SQL was created by 1 Lead Creator and 4 Co-Creators. Revenue arrangements are private and never shown.</p></div><a class="ds-x sm" href="LEARN-CREATORS-5.dc.html" aria-label="Close">%s</a></header>
<ol class="cp-l">%s</ol><footer class="cp-f"><a class="ds-ghost" href="LEARN-CREATORS-5.dc.html">Close</a></footer></aside>''' % (
    ''.join(tav(m, 30) for m in TEAM), ic('x', 16, 2.2),
    ''.join('<li style="--i: %d">%s<div><span class="mtc-n"><b>%s</b>%s</span><em>%s</em><span class="mtc-s"><span><b>%s</b> courses</span><span><b>%s</b> learners</span><span class="mtc-st"><b>%s</b><i></i></span></span><p><span>Contributed:</span> %s</p></div><a class="ds-link sm" href="#">View profile%s</a></li>' % (
        i, tav(m, 44), m[1], trole(m), m[3], m[4], m[5], m[6], m[7], ic('arrowr', 13, 2.2)) for i, m in enumerate(TEAM)))
COURSE_PAGE = COURSE_PAGE + '<sc-if value="{{s_panel}}" hint-placeholder-val="{{ false }}">%s</sc-if>' % PANEL

PREVIEW_JS = '''class Component extends DCLogic {
  renderVals() { var v = this.props.view || 'course', t = this.props.team || ''; return { s_course: v === 'course', s_lesson: v === 'lesson', t_solo: !t, t_2: t === '2', t_5: t === '5', s_panel: !!this.props.panel }; }
}'''
write('Preview.dc.html', doc('Creator Preview · learner pages · shared source', kit.KIT_CSS + '\n' + BASE_CSS + WK_CSS + PREVIEW_CSS,
                             '<sc-if value="{{s_course}}" hint-placeholder-val="{{ true }}">%s</sc-if><sc-if value="{{s_lesson}}" hint-placeholder-val="{{ false }}">%s</sc-if>' % (COURSE_PAGE, LESSON), PREVIEW_JS))

BOARDS = [
    ('STU-040', 'Prepare', {'page': 'review'}, 'CR-STU-040 · Course Review (learner preview)'),
    ('STU-040M', 'Prepare', {'page': 'market'}, 'CR-STU-040 · Marketplace preview'),
    ('STU-PRV', 'Preview', {'view': 'course'}, 'Creator Preview · Preview as Learner'),
    ('STU-PRV-L', 'Preview', {'view': 'lesson'}, 'Creator Preview · Learning Experience Preview (CR-LEARN-PRV-001)'),
    ('LEARN-CREATORS-2', 'Preview', {'view': 'course', 'team': '2'}, 'CR-LEARN-CREATORS-2 · Course Overview with 2 creators (Lead + 1 Co-Creator)'),
    ('LEARN-CREATORS-5', 'Preview', {'view': 'course', 'team': '5'}, 'CR-LEARN-CREATORS-5 · Course Overview with 5 creators (3 names + 2 others, 4 cards)'),
    ('LEARN-CREATORS-PANEL', 'Preview', {'view': 'course', 'team': '5', 'panel': True}, 'CR-LEARN-CREATORS-PANEL · Course creators panel'),
    ('STU-041', 'Prepare', {'page': 'profile'}, 'CR-STU-041 · Course Intelligence Profile'),
    ('STU-042', 'Prepare', {'page': 'nova'}, 'CR-STU-042 · Nova Course Review (not validation)'),
    ('STU-043', 'Prepare', {'page': 'ready'}, 'CR-STU-043 · Validation Readiness (incl. Commercial)'),
    ('STU-044', 'Prepare', {'page': 'issues'}, 'CR-STU-044 · Issues to resolve'),
    ('STU-045', 'Submit', {'step': 'intake'}, 'CR-STU-045 · Validation intake'),
    ('STU-046', 'Submit', {'step': 'declare'}, 'CR-STU-046 · Creator declaration'),
    ('STU-047', 'Submit', {'step': 'creator'}, 'CR-STU-047 · Creator readiness (1 requirement left)'),
    ('STU-048', 'Submit', {'step': 'scope'}, 'CR-STU-048 · Validation classification'),
    ('STU-049', 'Submit', {'step': 'quote'}, 'CR-STU-049 · Validation quote'),
    ('STU-050', 'Submit', {'step': 'short'}, 'CR-STU-050 · Payment · insufficient Credits'),
    ('STU-051', 'Submit', {'step': 'enough'}, 'CR-STU-050–051 · Payment & submit for validation'),
    ('STU-052', 'Submit', {'step': 'done'}, 'CR-STU-052 · Submission confirmation'),
]

if __name__ == '__main__':
    import sys
    H = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else {}
    for code, src, props, title in BOARDS:
        bg = '#F7F9FD' if src == 'Prepare' else '#FFFFFF'
        hd, hm = H.get(code, (3000, 3000))
        write(code + '.dc.html', wrapper(title + ' · Desktop', src, props, 1440, hd, bg))
        write(code + '-Mobile.dc.html', wrapper(title + ' · Mobile', src, props, 390, hm, bg))
    print('ok', len(BOARDS), 'boards; toggles', W.n, S.n)
