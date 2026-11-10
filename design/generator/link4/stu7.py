"""Link 4 · Batch 7: Manage Published Course part 2 — Pricing & Access (MGT-004), Course Updates & Versions (MGT-005),
Learner Access & Enrollment (MGT-006). Client copy word for word (prototype-only notes omitted).

Manage2.dc.html (prop page: p-a | p-edit | p-review | p-pending | p-done | p-invalid | p-hist |
                 v-a | v-none | v-create | v-compare | v-ready | v-val | v-chg | v-act | v-hist |
                 l-a | l-empty | l-detail | l-assign | l-impact | l-unpub)
Same creator-dashboard shell as batch 6 (stu6.cr_side / CR_TOP), right rail from rail.py.
"""
import json
from l4kit import *
from rail import *
from kit import coin, credit, emblem
import stu6
from stu6 import cr_side, CR_TOP, crumbs, COV

W = Toggles()
PAGES = []
def P(key, body):
    PAGES.append((key, body))

GB = '<span class="gb">%s<span>Gold Validated</span></span>' % ic('badge', 12, 2.2)
def head(section, h1, sub, back=('Back to Manage Course', 'MGT-001.dc.html'), right='', crumb_extra=None):
    c = [('Manage Course', 'MGT-001.dc.html'), (section, '' if not crumb_extra else crumb_extra[1])]
    if crumb_extra: c.append((crumb_extra[0], ''))
    return (crumbs(c) + '<header class="pg-h ob-in"><div class="pg-hl"><a class="ds-back" href="%s">%s<span>%s</span></a><h1 class="ds-h1">%s</h1>%s</div>%s</header>' % (
        back[1], ICON(I['back'], 15, 2), back[0], h1, ('<p class="ds-sub">%s</p>' % sub) if sub else '', ('<div class="pg-hr">%s</div>' % right) if right else ''))
def strip(meta, status='Published', tone='green', extra=''):
    return ('<section class="ds-card cst2 ob-in2">%s<div class="cst-b"><b>Data Analysis with SQL</b><span class="cst-t"><span class="ds-tag %s">%s</span>%s</span><span class="cst-p">%s</span></div>%s</section>') % (
        COV, tone, status, GB, meta, extra)
def wk(main, rail):
    return '<div class="wk"><div class="wk-m">%s</div><aside class="wk-r">%s</aside></div>' % (main, rail)
def steps(cur, labels):
    return '<ol class="stp" aria-label="Steps">%s</ol>' % ''.join(
        '<li class="%s"><i>%s</i><span>%s</span></li>' % ('dn' if i < cur else ('on' if i == cur else ''), ck(10) if i < cur else i + 1, l) for i, l in enumerate(labels))
def bar(left, right):
    return '<div class="ds-acts sb sv wk-a2"><span class="sv-s">%s</span><span class="sv-r">%s</span></div>' % (left, right)
def outcome(kind, icon, pill, h1, sub, body, acts_):
    return '<div class="ko-in ob-in"><div class="ko %s">%s<span class="ko-pill">%s</span><h1 class="ko-h1">%s</h1><p class="ko-sub">%s</p>%s<div class="ko-acts">%s</div></div></div>' % (
        kind, emblem() if kind == 'ok' else '<div class="ko-emb ko-v %s" aria-hidden="true"><span class="ko-halo"></span><span class="ko-disc">%s</span></div>' % (kind, ic(icon, 28, 2.2)), pill, h1, sub, body, acts_)
PROTECT = '''<section class="ds-card rx pr2 ob-in3"><span class="pr2-i">%s</span><b>Existing Learners Are Protected</b><p>Changes to pricing and future access options do not retroactively change completed purchases or existing learner entitlements.</p></section>''' % ic('valid', 20, 2)

# ======================================================================= MGT-004 Pricing & Access
def band(lo, hi, val, out=False, cls=''):
    pos = (val - lo) * 100.0 / (hi - lo)
    pos = max(0, min(100, pos)) if not out else 104
    return ('<div class="bd %s"><span class="bd-tr"><i></i></span><span class="bd-pin%s" style="left: %.1f%%"><em>%s</em></span>'
            '<span class="bd-l"><b>%s</b><span>Approved range</span><b>%s</b></span></div>') % (cls, ' out' if out else '', pos, '{:,}'.format(val), '{:,} Credits'.format(lo), '{:,} Credits'.format(hi))
OPT = '''<div class="ao2">
<article class="ao gold"><span class="ao-k">%s<span>Learn with DLP</span></span>%s<b class="ao-v">1,800 <small>DLP</small></b><p>Validated learning requirement · System-calculated</p><span class="ao-x">%s</span></article>
<article class="ao blue"><span class="ao-k">%s<span>Lifetime Access</span></span>%s<b class="ao-v">420 <small>Credits</small></b><p>Marketplace purchase price · Creator-selected</p><span class="ao-x">%s</span></article></div>''' % (
    coin(True), tag('%s Active' % ck(10), 'green'), coin(), credit(True), tag('%s Active' % ck(10), 'green'), credit())
def tg(on=True):
    k = W.new(on)
    return '<button type="button" class="tgl {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}" aria-label="Toggle"><i></i></button>' % (k, k, k)
P('p-a', head('Pricing & Access', 'Pricing & Access', 'Manage how new learners access your published course and review your approved pricing.',
              right='<a class="ds-ghost sm" href="MGT-006.dc.html">%s<span>Review Learner Access</span></a><a class="ds-ghost sm" href="MGT-004-I.dc.html">%s<span>View Pricing History</span></a>%s' % (
                  ic('users', 15, 2), ic('clock', 15, 2), btn('Edit Pricing &amp; Access', 'MGT-004-D.dc.html', 'sm2'))) +
  wk(strip('Version 1.0 · Course ID: CRS-20394') +
     '<section class="ob-in2"><h2 class="sh">Current Access Options</h2>%s</section>' % OPT +
     '''<section class="ds-card fc ap2 ob-in3"><div class="fc-h"><div><h2>Approved Pricing%s</h2></div></div>
<div class="ap2-g"><div class="ap2-d"><em>Validated DLP requirement</em><b>%s1,800 DLP</b><span class="ap2-lk">%s<span>Locked</span></span></div>
<div class="ap2-c"><div class="ap2-r"><span><em>Approved Credit price range</em><b>350–550 Credits</b></span><span class="r"><em>Current Credit price</em><b>%s420 Credits</b></span></div>%s</div></div></section>''' % (
         tip('Illustrative pricing values and range. Actual approved values must come from the course’s validation and pricing records.'), coin(), ic('lock', 12, 2.2), credit(), band(350, 550, 420)),
     '''<section class="ds-card rx aa ob-in3"><span class="rx-k">Access Availability</span>
<div class="aa-r"><span class="aa-i gold">%s</span><span><b>Subscription Access</b><em>Learners consume DLP through their plans.</em></span>%s</div>
<div class="aa-r"><span class="aa-i blue">%s</span><span><b>Marketplace Lifetime Access</b><em>Learners can purchase the course with Credits.</em></span>%s</div></section>''' % (
         coin(), tag('Enabled', 'green'), credit(), tag('Enabled', 'green')) + PROTECT))

REASONS = ['Pricing or commercial adjustment', 'Promotional pricing change', 'Changing future access availability', 'Other']
STOPS = [350, 400, 420, 450, 480, 500, 550]
P('p-edit', head('Pricing & Access', 'Edit Pricing & Access', 'Adjust your approved Marketplace Credit price and available access options for future learners.', crumb_extra=('Edit Settings', 'MGT-004.dc.html')) +
  steps(0, ['Edit settings', 'Review changes', 'Done']) +
  wk('''<section class="ds-card fc ob-in2"><div class="pe-h"><span class="pe-i blue">%s</span><div><h2>Marketplace Credit Price</h2>%s</div><b class="pe-v">420 <small>Credits</small></b></div>
<div class="pe-sl">%s<div class="pe-st">%s</div></div><p class="pe-n">Current published price: 420 Credits. Changes apply prospectively after approval or confirmation.</p></section>
<section class="ds-card fc pe-lk ob-in3"><div class="pe-h"><span class="pe-i gold">%s</span><div><h2>Subscription DLP</h2><span class="ds-tag">%s Locked</span></div><b class="pe-v">1,800 <small>DLP</small></b></div><p class="pe-n">This requirement was established through the approved learning experience. Update course content through Course Studio if recalculation is needed.</p></section>
<section class="ds-card fc ob-in3"><div class="fc-h"><div><h2>Access Channels</h2></div></div>
<div class="ch2"><div class="ch2-r"><span class="aa-i gold">%s</span><span><b>Subscription DLP Access</b><em>Allow new eligible learners to consume the course using DLP.</em></span>%s</div>
<div class="ch2-r"><span class="aa-i blue">%s</span><span><b>Marketplace Lifetime Access</b><em>Allow new learners to purchase lifetime access using Credits.</em></span>%s</div></div>
<p class="pe-w">%s<span>If both channels are disabled, you’ll be guided to Pause Enrollments or Unpublish Course rather than publishing a course no learner can access.</span></p></section>
<section class="ds-card fc ob-in4"><div class="fc-h"><div><h2>Reason for change</h2></div></div><div class="rs3">%s</div></section>''' % (
      credit(True), tag('%s Within Range' % ck(10), 'green'), band(350, 550, 420, cls='bl2'),
      ''.join('<button type="button" class="pe-s {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}">%s</button>' % ((lambda k: (k, k, k))(W.new(v == 420, 'stop')) + (v,)) for v in STOPS),
      coin(True), ic('lock', 11, 2.4), coin(), tg(), credit(), tg(), ic('warn', 15, 2.2),
      ''.join(W.opt('<span class="o-t"><b>%s</b></span>' % r, i == 0, 'why', 'sm') for i, r in enumerate(REASONS))) +
     bar('<a class="ds-link" href="MGT-004.dc.html">Cancel</a>', btn('Review Changes', 'MGT-004-E.dc.html')),
     '''<section class="ds-card rx pv3 ob-in3"><span class="rx-k">Learners will see</span><article class="pv-c"><span class="pv-cv"><i>SQL</i><em></em><em></em><em></em></span><b>Data Analysis with SQL</b><span class="pv3-p"><span>%s<b>1,800</b> DLP</span><span class="pv3-n">%s<b>420</b> Credits</span></span></article></section>''' % (coin(), credit()) + PROTECT))

CMP = [('DLP requirement', '1,800 DLP', '1,800 DLP'), ('Marketplace price', '420 Credits', '480 Credits'), ('Subscription access', 'Enabled', 'Enabled'),
       ('Lifetime purchases', 'Enabled', 'Enabled'), ('Publication status', 'Published', 'Published')]
IMP = [('Existing lifetime purchases', 'Unaffected', 'ok', 'check'), ('Active DLP access', 'Preserved', 'ok', 'check'), ('Future lifetime purchases', 'New price', 'cb', 'arrowr')]
P('p-review', head('Pricing & Access', 'Review Pricing Changes', 'Compare your current settings against the proposed update before confirming.', crumb_extra=('Review Changes', 'MGT-004.dc.html')) +
  steps(1, ['Edit settings', 'Review changes', 'Done']) +
  wk('''<section class="ds-card cmp ob-in2"><div class="cmp-r cmp-hd"><span>Setting comparison</span><span>Current</span><span></span><span>Proposed</span></div>%s</section>
<section class="ds-card fc ob-in3"><div class="fc-h"><div><h2>Impact on Existing Learners</h2><p>The proposed Marketplace Credit price will apply only to eligible future purchases after the effective time. Existing purchases retain their original purchase terms.</p></div></div>
<div class="im3">%s</div></section>''' % (
      ''.join('<div class="cmp-r%s"><span>%s</span><span class="cmp-o">%s</span><span class="cmp-a">%s</span><b class="cmp-n">%s</b></div>' % (' ch' if a != b else '', l, a, ic('arrowr', 14, 2.2) if a != b else '', b) for l, a, b in CMP),
      ''.join('<div class="im %s" style="--i: %d"><span class="im-i">%s</span><em>%s</em><b>%s</b></div>' % (k, i, ic(icn, 14, 2.4), l, v) for i, (l, v, k, icn) in enumerate(IMP))) +
     bar('<a class="ds-link" href="MGT-004-D.dc.html">Back</a>', btn('Confirm Changes', 'MGT-004-G.dc.html')),
     '''<section class="ds-card rx ef ob-in3"><span class="rx-k">When it applies</span><div class="ef-r"><span class="ef-i">%s</span><span><em>Effective date</em><b>Immediately after confirmation</b></span></div><div class="ef-r"><span class="ef-i">%s</span><span><em>Approval requirement</em><b>None</b></span></div></section>
<section class="ds-card rx pd ob-in3" aria-hidden="true"><span class="rx-k">Marketplace price</span><div class="pd-v"><s>420</s>%s<b>480</b><small>Credits</small></div><span class="pd-d">+60 Credits</span></section>''' % (ic('clock', 16, 2), ic('users', 16, 2), ic('arrowr', 18, 2.2))))

def pricenums(prop, star=''):
    return '<div class="pn3"><span><b>420</b><em>Previous price</em></span><i>%s</i><span class="nw"><b>%s%s</b><em>%s</em></span><span class="dlr"><b>1,800</b><em>DLP requirement</em></span></div>' % (
        ic('arrowr', 18, 2.2), prop, star, 'Proposed price' if star else 'New price')
P('p-done', outcome('ok', 'check', 'Active', 'Pricing Updated', 'Your new Marketplace Credit price has been applied to eligible future purchases of Data Analysis with SQL.',
                    pricenums('480'), btn('Return to Pricing &amp; Access', 'MGT-004.dc.html')))
P('p-pending', outcome('am', 'clock', 'Pending Approval', 'Pricing Change Submitted for Approval', 'The live price remains unchanged until organization approval and activation.',
                       pricenums('480', '*'), btn('Return to Pricing &amp; Access', 'MGT-004.dc.html')))
P('p-invalid', outcome('rd', 'warn', 'Restricted', 'Invalid Pricing Change', 'The proposed price falls outside the approved range, or this course’s validation status currently prevents commercial changes.',
                       '''<section class="ko-card"><div class="iv-g"><div><em>Proposed price</em><b class="rd">620 Credits</b><span class="ds-tag red">Outside approved range</span></div><div><em>Approved maximum</em><b>550 Credits</b></div></div>%s
<p class="ko-n">%s<span>Changes above the approved maximum must route through a pricing review rather than standard self-service edits.</span></p></section>''' % (band(350, 550, 620, True, 'iv'), ic('lock', 14, 2)),
                       '<a class="ds-ghost" href="MGT-004-D.dc.html">Back</a>' + btn('Request Pricing Review', '#')))

HIST = [('12 Sep 2026', 'Initial approved price', '—', '420 Credits', 'Active', 'green'), ('20 Sep 2026', 'Credit price change', '420', '480 Credits', 'Example', 'blue'), ('—', 'DLP recalculation', '1,800', '—', 'None', '')]
P('p-hist', head('Pricing & Access', 'Pricing History', 'How pricing and access settings have changed over time for Data Analysis with SQL.', crumb_extra=('Pricing History', 'MGT-004.dc.html')) +
  wk('<section class="ds-card ht ob-in2"><div class="ht-r ht-hd"><span>Effective date</span><span>Change</span><span>Previous</span><span>New</span><span>Status</span></div>%s</section>' % ''.join(
      '<div class="ht-r" style="--i: %d"><span class="ht-d"><i></i>%s</span><b>%s</b><span class="ht-p">%s</span><span class="ht-n">%s</span>%s</div>' % (i, d, c, p, n, tag(s, k)) for i, (d, c, p, n, s, k) in enumerate(HIST)),
     '''<section class="ds-card rx ob-in3"><span class="rx-k">Credit price over time</span><svg class="spk" viewBox="0 0 240 90" aria-hidden="true"><path class="spk-a" d="M10 62 L110 62 L130 34 L230 34" fill="none"></path><circle cx="10" cy="62" r="4"></circle><circle cx="130" cy="34" r="4"></circle><circle class="nw" cx="230" cy="34" r="5"></circle></svg>
<div class="spk-l"><span>12 Sep · 420</span><span>20 Sep · 480</span></div><p class="rx-p">Illustrative entries, not actual course transactions. A price change never overwrites historical prices used by completed orders.</p></section>'''))

# ======================================================================= MGT-005 Course Updates & Versions
LIVE_FACTS = [('Validation', 'Gold Validated', 'gold'), ('Approved DLP', '1,800 DLP', ''), ('Marketplace Price', '420 Credits', ''), ('Last Validated', '12 Sep 2026', '')]
def live_card(extra=''):
    return '''<article class="vc live ob-in2"><header><span class="vc-k">Current Live Version</span><span class="ds-tag green"><i class="lv-d"></i>Live</span></header><b class="vc-v">Version 1.0</b>
<dl>%s</dl><a class="ds-link sm" href="STU-PRV.dc.html">%s<span>View Live Version</span></a>%s</article>''' % (
        ''.join('<div><dt>%s</dt><dd class="%s">%s</dd></div>' % (l, k, v) for l, v, k in LIVE_FACTS), ic('eye', 14, 2), extra)
VHIST_D = [('v1.1', 'Current Update', 'Draft revision', 'Draft', 'amber', ''), ('v1.0', 'Original Published Version', 'Validated 12 Sep 2026', 'Live', 'green', '')]
def vhist(items):
    return '<section class="ds-card rx vh2 ob-in3"><div class="vh2-h"><span class="rx-k">Version History</span><a class="ds-link sm" href="MGT-005-HISTORY.dc.html">View All</a></div><ol>%s</ol></section>' % ''.join(
        '<li class="%s"><span class="vh2-d"></span><span><b>%s — %s</b><em>%s</em></span>%s</li>' % (k, v, t, d, tag(s, k)) for v, t, d, s, k, _ in items)
VSTRIP = strip('Technology / Data &amp; Analytics · Course ID: CRS-20394')
P('v-a', head('Course Updates & Versions', 'Course Updates &amp; Versions', 'Improve your course while keeping the published learning experience protected.') +
  wk(VSTRIP + '''<div class="vrow ob-in2">%s<span class="vrow-x" aria-hidden="true"><i></i></span>
<article class="vc draft"><header><span class="vc-k">Current Course Update</span><span class="ds-tag amber">Draft Update</span></header><b class="vc-v">Version 1.1</b><p class="vc-p">Your changes are saved separately and are not visible to learners yet.</p>
<div class="vc-n">%s</div><div class="vc-cr"><em>Change review</em>%s</div><div class="vc-a"><a class="ds-ghost sm" href="STU-020.dc.html">Continue Editing</a><a class="ds-link sm" href="MGT-005-COMPARE.dc.html">Compare Changes%s</a></div></article></div>
<section class="ds-card rdy ob-in3"><span class="rdy-i">%s</span><div><b>Ready for Review?</b><p>Check changes before submitting this version.</p></div>%s</section>''' % (
      live_card(), ''.join('<span><b>%s</b><em>%s</em></span>' % x for x in [('4', 'Lessons modified'), ('2', 'New resources'), ('1', 'Assessments changed')]), tag('Not submitted'), ic('arrowr', 13, 2.2),
      ic('check', 20, 2.2), btn('Review Update', 'MGT-005-READY.dc.html', 'sm2')),
     vhist(VHIST_D)))
P('v-none', head('Course Updates & Versions', 'Course Updates &amp; Versions', 'Improve your course while keeping the published learning experience protected.') +
  wk(VSTRIP + '''<div class="vrow ob-in2">%s<span class="vrow-x" aria-hidden="true"><i></i></span>
<article class="vc new"><span class="vc-pl" aria-hidden="true">%s</span><b>Keep Your Course Up to Date</b><p>Create a new version to improve lessons, assessments, resources or learning outcomes. Your published course will remain available while you work.</p>%s</article></div>''' % (
      live_card(), ic('plus', 22, 2.4), btn('Create Course Update', 'MGT-005-CREATE.dc.html', 'sm2')),
     vhist(VHIST_D[1:])))
AREAS = [('course', 'Lessons & Learning Content', 'Improve videos, explanations, examples and resources.', True), ('quiz', 'Assessments & Projects', 'Update quizzes, exams, grading rubrics and projects.', True),
         ('target', 'Learning Outcomes & Skills', 'Change what learners are expected to achieve.', False), ('layers', 'Curriculum & Learning Hours', 'Add, remove or reorganize chapters and lessons.', True),
         ('users', 'Learner Experience & Delivery', 'Update learning support, schedules and delivery settings.', False)]
P('v-create', head('Course Updates & Versions', 'Create Course Update', 'Start a new version of your published course. Your current live version will remain unchanged.', crumb_extra=('Create Update', 'MGT-005.dc.html')) +
  wk('''<section class="ds-card fc ob-in2"><div class="fc-h"><div><h2>What would you like to update?</h2><p>Select the areas you plan to improve. You can refine these selections later.</p></div></div><div class="ar">%s</div></section>''' % ''.join(
      W.opt('<span class="ar-i">%s</span><span class="o-t"><b>%s</b><span>%s</span></span>' % (ic(i, 18, 2), t, d), on, None, 'ar-o') for i, t, d, on in AREAS) +
     bar('<a class="ds-link" href="MGT-005-NONE.dc.html">Cancel</a>', btn('Create Draft &amp; Open Studio', 'STU-020.dc.html')),
     '''<section class="ds-card rx br ob-in3" aria-hidden="true"><span class="rx-k">Your new version</span><svg viewBox="0 0 260 150" class="br-s"><path class="br-m" d="M30 120 L230 120"></path><path class="br-b" d="M90 120 C130 120 130 40 180 40 L230 40"></path></svg>
<span class="br-n a"><em>Base version</em><b>v1.0</b></span><span class="br-n b"><em>New draft</em><b>v1.1</b></span></section>
<section class="ds-card rx ok2 ob-in3"><span class="ok2-i">%s</span><p>Your current published course will stay live while you work on this update. Credalio will determine the required review from the actual changes you make.</p></section>''' % ic('valid', 18, 2)))
SEC = [('Curriculum', 'Chapter 3 · New SQL joins lesson', 'Added', 'green', 'plus'), ('Lesson Content', 'Lesson 2.4 · Updated video and transcript', 'Modified', 'blue', 'edit'),
       ('Assessments', 'Final exam · Updated questions and passing criteria', 'Modified', 'blue', 'edit'), ('Resources', 'Two new downloadable practice datasets', 'Added', 'green', 'plus'),
       ('Learning Outcomes', 'No changes', 'Unchanged', '', 'check')]
P('v-compare', head('Course Updates & Versions', 'Compare Course Versions', 'Review changes between your current published course and the proposed update.', crumb_extra=('Compare Versions', 'MGT-005.dc.html')) +
  wk('''<section class="ds-card vs2 ob-in2"><div class="vs2-c"><em>Current Live</em><b>Version 1.0</b>%s</div><span class="vs2-x" aria-hidden="true">%s</span><div class="vs2-c dr"><em>Proposed Update</em><b>Version 1.1</b>%s</div>
<div class="vs2-n">%s</div></section>
<section class="ds-card fc ob-in3"><div class="fc-h"><div><h2>Changes by Section</h2></div>%s</div><ul class="cs3">%s</ul></section>''' % (
      GB, ic('arrowr', 18, 2.2), tag('Draft', 'amber'), ''.join('<span class="%s"><b>%s</b><em>%s</em></span>' % x for x in [('m', '4', 'Modified'), ('a', '2', 'Added'), ('r', '1', 'Removed')]),
      tag('7 Changes', 'blue'), ''.join('<li class="%s" style="--i: %d"><span class="cs3-i">%s</span><span><em>%s</em><b>%s</b></span>%s</li>' % (k or 'gy', i, ic(icn, 14, 2.4), s, d, tag(t, k)) for i, (s, d, t, k, icn) in enumerate(SEC))) +
     bar('', btn('Continue to Update Review', 'MGT-005-READY.dc.html')),
     '''<section class="ds-card rx dd ob-in3" aria-hidden="true"><span class="rx-k">7 Changes</span><div class="dd-b"><i class="m" style="flex: 4"></i><i class="a" style="flex: 2"></i><i class="r" style="flex: 1"></i></div><ul><li><i class="m"></i>Modified<b>4</b></li><li><i class="a"></i>Added<b>2</b></li><li><i class="r"></i>Removed<b>1</b></li></ul><p class="rx-p">Illustrative change records; actual changes must be calculated from versioned content.</p></section>'''))
RD = [(True, 'Updated lessons have required content'), (True, 'Learning outcomes remain mapped to evidence'), (False, 'Assessment changes have valid answer keys and rubrics'),
      (True, 'Updated resources are accessible'), (False, 'Completion requirements are consistent'), (True, 'Collaborator permissions and approvals are valid')]
P('v-ready', head('Course Updates & Versions', 'Update Readiness &amp; Revalidation', 'Determine whether the update is complete and what review it requires.', crumb_extra=('Readiness & Revalidation', 'MGT-005.dc.html')) +
  wk('''<section class="ds-card fc ob-in2"><div class="fc-h"><div><h2>Update Readiness</h2></div>%s</div><div class="rdb"><i style="flex: 4"></i><i class="f" style="flex: 2"></i></div><ul class="rl2">%s</ul></section>''' % (
      tag('2 Items to Resolve', 'amber'), ''.join('<li class="%s" style="--i: %d"><span>%s</span><b>%s</b>%s</li>' % ('ok' if o else 'no', i, ck(10) if o else ic('warn', 12, 2.4), t, '' if o else '<a class="ds-ghost xs" href="STU-020.dc.html">Fix</a>') for i, (o, t) in enumerate(RD))) +
     '<div class="ds-acts sb sv wk-a2"><span class="sv-s is-w">%s<span>Submission is disabled in this illustrative state until blocking readiness issues are resolved.</span></span><span class="sv-r"><span class="ds-btn is-dis" aria-disabled="true"><span>Submit for Revalidation</span><span class="ob-arrow">%s</span></span></span></div>' % (ic('lock', 14, 2), ARROW),
     '''<section class="ds-card rx cl3 ob-in3"><span class="rx-k">Provisional review classification</span><b class="cl3-v">Standard Update</b><div class="cl3-s"><i></i><i class="on"></i><i></i></div><div class="cl3-l"><span>Minor</span><span class="on">Standard</span><span>Major</span></div><p class="rx-p">Final classification will be determined by Credalio’s validation intake and applicable review rules.</p></section>'''))
def track2(status, tone, finding=''):
    return ('''<section class="ds-card tk2 %s ob-in2"><div class="tk2-l"><span class="tk2-r live"><i class="lv-d"></i><b>v1.0</b><em>Live</em></span><span class="tk2-line"><i></i></span><span class="tk2-r rv"><span class="tk2-dot"></span><b>v1.1</b><em>%s</em></span></div>
<dl class="tk2-f">%s</dl><p class="tk2-n">%s<span>Version 1.0 remains live while the update is reviewed.</span></p></section>%s''') % (
        tone, status, ''.join('<div><dt>%s</dt><dd>%s</dd></div>' % r for r in [('Submitted for revalidation', '%s' % tag(status, 'amber' if tone == 'am' else 'blue')), ('Validation case', 'VAL-01104'), ('Review classification', 'Standard Update'), ('Live version', '1.0')]),
        ic('valid', 15, 2), finding)
P('v-val', head('Course Updates & Versions', 'Version 1.1', '', crumb_extra=('Under Validation', 'MGT-005.dc.html')) +
  wk(track2('Under Validation', 'cb') + bar('', btn('View Validation Case', 'STU-055.dc.html')), vhist([('v1.1', 'Current Update', 'Submitted for revalidation · VAL-01104', 'Under Validation', 'blue', ''), VHIST_D[1]])))
P('v-chg', head('Course Updates & Versions', 'Version 1.1', '', crumb_extra=('Changes Requested', 'MGT-005.dc.html')) +
  wk(track2('Changes Requested', 'am', '''<section class="ds-card fd ob-in3"><span class="fd-i">%s</span><div><span class="sv-b2">Finding</span><b>Assessment answer key mismatch</b><p>The final exam’s updated question 7 does not have a matching answer key entry. Address this finding and resubmit to the same validation case.</p></div></section>''' % ic('warn', 18, 2.2)) +
     bar('', btn('Address Findings', 'STU-024.dc.html')), vhist([('v1.1', 'Current Update', 'Changes requested · VAL-01104', 'Changes Requested', 'amber', ''), VHIST_D[1]])))
TRANS = [('New enrollments', 'New version', 'cb', 'users'), ('Existing learners', 'Transition policy', 'am', 'path'), ('Completed credentials', 'Preserved', 'ok', 'cert2')]
P('v-act', head('Course Updates & Versions', 'Activate Course Update', 'Version 1.1 has passed the required review and is ready to become your live course.', crumb_extra=('Activate Update', 'MGT-005.dc.html')) +
  wk('''<section class="ds-card vt2 ob-in2"><div class="vt2-h"><span class="rx-k">Version transition</span>%s</div><div class="vt2-r"><div class="vt2-c"><em>Current live version</em><b>v1.0</b></div><span class="vt2-a" aria-hidden="true"><i></i><i></i><i></i></span><div class="vt2-c nw"><em>New approved version</em><b>v1.1</b></div><div class="vt2-c g"><em>New validation outcome</em><b>%sGold · From approval record</b></div></div></section>
<section class="ds-card fc ob-in3"><div class="fc-h"><div><h2>Learner Transition</h2><p>Before activation, Credalio determines which learners move to the new version and which continue on their existing version.</p></div></div><div class="im3">%s</div></section>''' % (
      tag('%s Approved · Ready to Activate' % ck(10), 'green'), ic('badge', 14, 2.2),
      ''.join('<div class="im %s" style="--i: %d"><span class="im-i">%s</span><em>%s</em><b>%s</b></div>' % (k, i, ic(icn, 14, 2.2), l, v) for i, (l, v, k, icn) in enumerate(TRANS))) +
     bar('<a class="ds-ghost sm" href="MGT-006-IMPACT.dc.html">Review Activation Impact</a>', btn('Activate Version 1.1', '#')),
     vhist([('v1.1', 'Current Update', 'Approved · Ready to Activate', 'Approved', 'green', ''), VHIST_D[1]])))
VH = [('v1.1', 'Draft / Under Review', 'amber', 'Pending', '—'), ('v1.0', 'Live', 'green', 'Gold', '12 Sep 2026')]
P('v-hist', head('Course Updates & Versions', 'Version History', 'Every version of Data Analysis with SQL, immutable once validated.', crumb_extra=('Version History', 'MGT-005.dc.html')) +
  wk('''<section class="ds-card vl ob-in2"><div class="vl-r vl-hd"><span>Version</span><span>Status</span><span>Validation</span><span>Activated</span><span>Actions</span></div>%s</section>''' % ''.join(
      '<div class="vl-r" style="--i: %d"><span class="vl-v"><i class="%s"></i><b>%s</b></span>%s<span>%s</span><span class="vl-d">%s</span><span class="vl-a"><a class="ds-ghost xs" href="#">View Snapshot</a><a class="ds-link sm" href="MGT-005-COMPARE.dc.html">Compare</a></span></div>' % (
          i, k, v, tag(s, k), ('<span class="gb sm">%s<span>Gold</span></span>' % ic('badge', 11, 2.2)) if val == 'Gold' else '<span class="vl-pd">%s</span>' % val, d) for i, (v, s, k, val, d) in enumerate(VH)),
     '''<section class="ds-card rx imm ob-in3"><span class="imm-i">%s</span><p>Version history is immutable — a previously validated version is never overwritten by a new draft.</p></section>''' % ic('lock', 18, 2)))

# ======================================================================= MGT-006 Learner Access & Enrollment
LS = [('AO', 'Amara Okafor', 'DLP', 'In Progress', 65, 'h1'), ('TB', 'Tunde Bello', 'Lifetime', 'Completed', 100, 'h2'), ('ZI', 'Zara Ibrahim', 'DLP', 'In Progress', 32, 'h3'),
      ('DM', 'Daniel Mensah', 'Lifetime', 'In Progress', 81, 'h4'), ('AN', 'Adaeze Nwosu', 'DLP', 'Access Ended', 40, 'h5')]
STC = {'In Progress': 'blue', 'Completed': 'green', 'Access Ended': ''}
def lrow(i, r, on=False, status=None):
    ini, n, acc, st, p, h = r
    st = status or st
    return ('<div class="lr%s" style="--i: %d"><span class="lr-n"><span class="la2 %s">%s</span><b>%s</b></span><span class="lr-ac %s">%s<span>%s</span></span>%s'
            '<span class="lr-p"><span class="lr-b"><i style="width: %d%%"></i></span><em>%d%% progress · v1.0</em></span><a class="ds-ghost xs" href="MGT-006-DETAIL.dc.html">View Details</a></div>') % (
        ' on' if on else '', i, h, ini, n, 'gold' if acc == 'DLP' else 'blue', coin() if acc == 'DLP' else credit(), acc, tag(st, STC[st]), p, p)
DIRH = '<div class="lr lr-hd"><span>Learner</span><span>Access</span><span>Status</span><span>Progress</span><span></span></div>'
STATS = [('248', 'Total Enrolled', 'Unique course learners', 'all'), ('86', 'Currently Learning', 'In-progress with active access', 'cb'),
         ('42', 'Lifetime Purchasers', 'Credit-based ownership', 'bl'), ('120', 'Completed', 'Verified completions', 'ok')]
def stats():
    return '<section class="ob-in2"><div class="sh2"><h2 class="sh">Enrollment Overview%s</h2><span class="ds-tag line">All time</span></div><div class="st4b">%s</div></section>' % (
        tip('Illustrative figures only. Metrics overlap: lifetime purchasers can also be active or completed learners.'),
        ''.join('<div class="sb %s" style="--i: %d"><b>%s</b><span>%s</span><em>%s</em></div>' % (k, i, n, l, d) for i, (n, l, d, k) in enumerate(STATS)))
def directory(rows, title='Enrollment Directory', tools=True, sel=None):
    t = ('<div class="dr-t"><label class="dr-s">%s<input placeholder="Search learners..." aria-label="Search learners"></label>%s%s<a class="ds-ghost xs" href="#">%s<span>Export</span></a></div>' % (
        ic('search', 15, 2), sel_('All Access Types'), sel_('All Statuses'), ic('download', 13, 2))) if tools else ''
    return '<section class="ds-card dr2 ob-in3"><div class="dr-h"><h2>%s</h2>%s</div>%s<div class="dr-l">%s%s</div></section>' % (
        title, '', t, DIRH, ''.join(rows))
def sel_(v):
    return '<label class="sel dr-f"><span class="sr-only">%s</span><select class="ds-in"><option>%s</option></select>%s</label>' % (v, v, ic('down', 14, 2))
BREAK = '''<section class="ds-card rx bk ob-in3"><span class="rx-k">Access Breakdown%s</span><div class="bk-b"><i class="g" style="flex: 206"></i><i class="b" style="flex: 42"></i></div>
<div class="bk-r"><span class="aa-i gold">%s</span><span><b>DLP-based access</b><em>206 learners</em></span><b class="bk-n">83%%</b></div><div class="bk-r"><span class="aa-i blue">%s</span><span><b>Lifetime Credit access</b><em>42 learners</em></span><b class="bk-n">17%%</b></div></section>''' % (
    tip('Example mutually exclusive primary-access categories. A learner may have multiple entitlements over time.'), coin(), credit())
VDIST = '''<section class="ds-card rx vd ob-in3"><div class="vd-h"><span class="rx-k">Course Version Distribution</span><a class="ds-link sm" href="MGT-006-ASSIGN.dc.html">View Version Assignments</a></div><div class="vd-r"><span class="vd-v">v1.0</span><span><b>Live v1.0</b><em>Learners assigned to v1.0</em></span><b class="vd-n">248</b></div><div class="vd-b"><i></i></div>
<p class="rx-p">When a new version is activated, learners may remain on an earlier version or move according to the approved transition policy.</p></section>'''
LPROT = '''<section class="ds-card rx pr2 ob-in4"><span class="pr2-i">%s</span><b>Learner Access Protection</b><p>Pausing enrollments, changing pricing, updating a course or unpublishing must not silently remove existing learner entitlements.</p><a class="ds-ghost sm" href="MGT-006-IMPACT.dc.html">Review Access Impact</a></section>''' % ic('valid', 20, 2)
LHEAD = head('Learner Access & Enrollment', 'Learner Access &amp; Enrollment', 'Understand who is learning, how they access your course, and which version they’re using.')
LSTRIP = strip('Live version 1.0 · %s1,800 DLP · %s420 Credits' % (coin(), credit()))
P('l-a', LHEAD + wk(LSTRIP + stats() + directory([lrow(i, r) for i, r in enumerate(LS)]), BREAK + VDIST + LPROT))
P('l-empty', head('Learner Access & Enrollment', 'Learner Access &amp; Enrollment', '') + strip('Version 1.0 · %s1,800 DLP · %s420 Credits' % (coin(), credit())) +
  '''<section class="ds-card emp2 ob-in3"><div class="emp2-v" aria-hidden="true"><span class="emp2-r"></span><span class="emp2-r b"></span><span class="emp2-c">%s</span><span class="emp2-s s1"></span><span class="emp2-s s2"></span><span class="emp2-s s3"></span></div>
<b>No Learners Yet</b><p>Your course is published, but no learners have enrolled yet. Once learners begin, you’ll be able to see their access, progress and assigned course version here.</p><a class="ds-ghost sm" href="STU-PRV.dc.html">%s<span>View Marketplace Listing</span></a></section>''' % (ic('users', 26, 2), ic('eye', 15, 2)))
DRAWER = '''<a class="ov-scrim" href="MGT-006.dc.html" aria-label="Close"></a>
<aside class="dw" role="dialog" aria-modal="true" aria-label="Learner Access Details"><header class="dw-h"><span class="rx-k">Learner Access Details</span><a class="ds-x sm" href="MGT-006.dc.html" aria-label="Close">%s</a></header>
<div class="dw-p"><span class="la2 h1 lg">AO</span><div><b>Amara Okafor</b><em>Learner ID: L-1001</em><span class="cst-t">%s%s</span></div></div>
<div class="dw-pg"><span class="dw-r">%s<span><b>65%%</b><em>Course progress</em></span></span></div>
%s%s%s
<p class="dw-n">%s<span>Subscription balances and unrelated wallet transactions are not visible to creators.</span></p>
<div class="dw-a"><a class="ds-ghost sm" href="#">View Learning Progress</a><a class="ds-ghost sm" href="#">Open Learner Support</a></div></aside>''' % (
    ic('x', 16, 2.2), tag('Access Active', 'green'), tag('In Progress', 'blue'), ring(65, 64, 11),
    *['<section class="dw-s"><span class="dw-k">%s</span><dl>%s</dl></section>' % (t, ''.join('<div><dt>%s</dt><dd>%s</dd></div>' % r for r in rows)) for t, rows in [
        ('Enrollment Information', [('Enrolled', '14 Sep 2026'), ('Enrollment source', 'Subscription'), ('Assigned version', 'v1.0')]),
        ('Access Entitlement', [('Access model', '%sDLP' % coin()), ('Entitlement status', 'Active'), ('Access window', 'Per entitlement policy')]),
        ('Learning Progress', [('Completion status', 'In Progress'), ('Verified achievement', 'Not Yet Earned')])]], ic('lock', 13, 2))
P('l-detail', LHEAD + wk(LSTRIP + directory([lrow(i, r, i == 0) for i, r in enumerate(LS[:3])], tools=False), BREAK + VDIST) + DRAWER)
P('l-assign', head('Learner Access & Enrollment', 'Course Version Assignments', 'See how learners are distributed across published course versions.', back=('Back to Learner Access', 'MGT-006.dc.html'), crumb_extra=('Version Assignments', 'MGT-006.dc.html')) +
  '''<div class="va2 ob-in2"><article class="ds-card va-c live"><header><span class="vd-v">v1.0</span><div><b>Version 1.0</b><em>248 learners · Gold Validated · Activated 12 Sep 2026</em></div><span class="ds-tag green"><i class="lv-d"></i>Current Live</span></header>
<div class="va-b"><i class="cb" style="flex: 86"></i><i class="ok" style="flex: 120"></i><i class="gy" style="flex: 42"></i></div><div class="va-s">%s</div></article>
<span class="va-x" aria-hidden="true"><i></i></span>
<article class="ds-card va-c up"><header><span class="vd-v dr">v1.1</span><div><b>Upcoming Version — v1.1</b><em>No learners are assigned to this version yet. Assignments can change only after approval and activation.</em></div>%s</header>
<div class="va-e" aria-hidden="true">%s</div><a class="ds-ghost sm" href="MGT-006-IMPACT.dc.html">Review Future Learner Transition</a></article></div>''' % (
      ''.join('<span class="%s"><i></i><b>%s</b><em>%s</em></span>' % x for x in [('cb', '86', 'In progress'), ('ok', '120', 'Completed'), ('gy', '42', 'Other learning states')]),
      tag('Draft Update', 'amber'), ''.join('<i style="--i: %d"></i>' % i for i in range(12))))
P('l-impact', head('Learner Access & Enrollment', 'Learner Access Impact', 'Preview how a course management action could affect your learners. This is a shared read-only component, reused from Publishing & Visibility and Pricing & Access.', back=('Back to Learner Access', 'MGT-006.dc.html'), crumb_extra=('Access Impact Review', 'MGT-006.dc.html')) +
  wk('''<section class="ds-card ma ob-in2"><span class="ma-i">%s</span><div><span class="rx-k">Management action</span><b>Unpublish Course</b><p>Stops new public discovery, enrollment and purchases while preserving applicable existing entitlements.</p></div></section>
<div class="im3 ob-in3">%s</div>
<section class="ob-in4"><h2 class="sh">Learner Groups to Check%s</h2><div class="lg3">%s</div></section>''' % (
      ic('eye', 20, 2), ''.join('<div class="im %s" style="--i: %d"><span class="im-i">%s</span><em>%s</em><b>%s</b></div>' % (k, i, ic(icn, 14, 2.4), l, v) for i, (l, v, k, icn) in enumerate(
          [('New enrollments', 'Blocked', 'rd', 'lock'), ('Existing entitlements', 'Preserved', 'ok', 'check'), ('Assigned course versions', 'Unchanged', 'gy', 'layers')])),
      tip('Sample counts; these groups may overlap.'), ''.join('<div class="lgp %s"><b>%s</b><em>%s</em><span class="lg-b"><i style="width: %d%%"></i></span></div>' % (k, n, l, int(n) * 100 / 248) for n, l, k in [('86', 'Active DLP learners', 'gold'), ('42', 'Lifetime purchasers', 'blue'), ('120', 'Completed learners', 'ok')])) +
     bar('', btn('View Detailed Impact', '#')),
     '''<section class="ds-card rx ob-in3"><span class="rx-k">Reused in</span><ul class="ru"><li>%s<span>Publishing &amp; Visibility</span></li><li>%s<span>Pricing &amp; Access</span></li></ul></section>''' % (ic('globe', 15, 2), ic('wallet', 15, 2))))
P('l-unpub', head('Learner Access & Enrollment', 'Learner Access &amp; Enrollment', '') +
  '''<div class="bn2 gy ob-in"><span class="bn2-i">%s</span><div><b>Course Unpublished</b><p>New enrollments are closed. Existing learner entitlements, progress and historical records remain available according to Credalio’s access policy.</p></div><a class="ds-ghost sm" href="MGT-002D.dc.html">Manage Publishing</a></div>''' % ic('eye', 18, 2.2) +
  wk(strip('Version 1.0 · %s1,800 DLP · %s420 Credits' % (coin(), credit()), 'Unpublished', '') + directory([lrow(0, LS[0], status='Access Ended'), lrow(1, LS[1])], 'Historical &amp; entitled learners', tools=False),
     BREAK + VDIST))

# ======================================================================= assembly
ACTIVE = 'My Creations'
def body():
    blocks = ['<sc-if value="{{p_%s}}" hint-placeholder-val="{{ %s }}">\n%s\n</sc-if>' % (k.replace('-', '_'), 'true' if k == 'p-a' else 'false', b) for k, b in PAGES]
    return '''<div class="ds-root cr-root">
%s
<div style="min-width: 0; display: flex; flex-direction: column">
%s
<main class="ds-main mg-main {{tone}}">
%s
</main>
</div>
</div>''' % (cr_side(ACTIVE), CR_TOP, '\n'.join(blocks))
TONE = {'p-done': 'ok', 'p-pending': 'am', 'p-invalid': 'rd', 'v-chg': 'am', 'v-act': 'ok', 'l-unpub': 'gy'}
JS = W.js() + '''var PG = %s, TONE = %s;
class Component extends DCLogic {
  renderVals() {
    var pg = this.props.page || 'p-a', v = togVals(this), self = this;
    PG.forEach(function (k) { v['p_'.concat(k.replace('-', '_'))] = k === pg; });
    v.tone = 'tn-'.concat(TONE[pg] || 'cb');
    v.navCls = this.state.nav ? 'ds-open' : '';
    v.toggleNav = function () { self.setState({ nav: !self.state.nav }); };
    return v;
  }
}''' % (json.dumps([p[0] for p in PAGES]), json.dumps(TONE))

CSS = stu6.MANAGE_CSS + r'''.cst2{display:flex;align-items:center;gap:16px;padding:16px 18px}
.cst2 .cv-t{width:52px;height:52px;border-radius:14px}
.cst2 .cst-b{flex:1;min-width:0;display:flex;flex-direction:column;gap:5px}
.cst2 .cst-b > b{font-size:16.5px;font-weight:600}
.wk-m{gap:16px}
.wk-m > section,.wk-m > div{margin-top:0}
.wk-m .sh{margin:6px 0 10px 0}
.fc-h p{margin:4px 0 0 0;font-size:14px;line-height:1.55;color:#5B6582}
.sh2{display:flex;align-items:center;justify-content:space-between;margin:6px 0 10px 0}
.sh2 .sh{margin:0;display:flex;align-items:center}
.ds-acts.wk-a2{position:sticky;bottom:0;z-index:5;margin:4px 0 0 0;padding:12px 12px 12px 22px;border-radius:999px;background:rgba(255,255,255,.94);border:1.5px solid #E6EAF3;box-shadow:0 18px 40px -24px rgba(11,20,51,.35);display:flex;align-items:center;justify-content:space-between;gap:16px;backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}
.ds-acts.wk-a2{flex-direction:row}
.wk-a2 .sv-s .ds-link{min-height:0}
.ds-acts.wk-a2:has(.sv-s:empty){align-self:flex-end;width:max-content;padding-left:12px}
.wk-m:has(> .wk-a2:has(.sv-s:empty)) .wk-a2{margin-left:auto}
.ar .ds-opt:last-child:nth-child(odd){grid-column:1 / -1}
.wk-a2 .sv-s{display:inline-flex;align-items:center;gap:8px;font-size:13.5px;color:#5B6582}
.wk-a2 .sv-r{display:inline-flex;align-items:center;gap:14px;margin-left:auto}
.sv-s.is-w{color:#8A5A00}.sv-s.is-w svg{color:#B76E00;flex-shrink:0}
.ds-btn.is-dis{background:#C9D2E6;box-shadow:none;cursor:not-allowed}.ds-btn.is-dis:hover{background:#C9D2E6;transform:none}.ds-btn.is-dis .ob-arrow{color:#8A93AD}
.stp{list-style:none;margin:18px 0 0 0;padding:0;display:flex;align-items:center;gap:0;max-width:560px}
.stp li{flex:1;display:flex;align-items:center;gap:8px;font-size:13px;font-weight:500;color:#8A93AD;position:relative}
.stp li + li::before{content:'';flex:0 0 28px;height:2px;margin-right:8px;background:#E6EAF3}
.stp li.dn + li::before,.stp li.on::before{background:linear-gradient(90deg,#0F6B45,#1652F0)}
.stp i{width:24px;height:24px;flex-shrink:0;box-sizing:border-box;border-radius:50%;border:2px solid #D6DDEE;background:#FFFFFF;font-style:normal;font-size:11.5px;font-weight:600;display:flex;align-items:center;justify-content:center;color:#8A93AD}
.stp .dn{color:#0F6B45}.stp .dn i{background:#0F6B45;border-color:#0F6B45;color:#FFFFFF}
.stp .on{color:#0B1433;font-weight:600}.stp .on i{background:#1652F0;border-color:#1652F0;color:#FFFFFF;box-shadow:0 0 0 5px rgba(22,82,240,.14)}
.ao2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.ao{position:relative;overflow:hidden;display:flex;flex-direction:column;gap:6px;padding:20px;border-radius:22px;border:1.5px solid}
.ao.gold{background:linear-gradient(150deg,#FFF6DD,#FFFFFF 70%);border-color:#F4D98E}
.ao.blue{background:linear-gradient(150deg,#EEF3FF,#FFFFFF 70%);border-color:#C9D7FA}
.ao-k{display:flex;align-items:center;gap:10px;font-size:14.5px;font-weight:600}
.ao > .ds-tag{position:absolute;top:18px;right:18px}
.ao-v{margin-top:10px;font-size:34px;font-weight:600;letter-spacing:-0.03em;line-height:1}
.ao-v small{font-size:15px;font-weight:500;color:#5B6582;letter-spacing:0}
.ao p{margin:0;font-size:13px;color:#5B6582}
.ao-x{position:absolute;right:-26px;bottom:-26px;opacity:.12;transform:rotate(-14deg)}
.ao-x .dlp-c,.ao-x .cr-c{width:120px;height:120px;font-size:64px}
.ao:hover .ao-x{animation:aoR 1.2s ease}
@keyframes aoR{50%{transform:rotate(6deg) scale(1.05)}}
.ap2-g{display:grid;grid-template-columns:220px minmax(0,1fr);gap:16px}
.ap2-d{display:flex;flex-direction:column;gap:6px;padding:16px;border-radius:16px;background:#FFFAEB;border:1.5px solid #F4E2B0}
.ap2-d em,.ap2-r em{font-style:normal;font-size:12.5px;color:#5B6582}
.ap2-d b,.ap2-r b{display:flex;align-items:center;gap:6px;font-size:18px;font-weight:600}
.ap2-d .dlp-c,.ap2-r .cr-c{width:20px;height:20px;font-size:11px}
.ap2-lk{display:inline-flex;align-items:center;gap:5px;font-size:12px;font-weight:500;color:#8A5A00}
.ap2-c{padding:16px 18px;border-radius:16px;background:#F7F9FD}
.ap2-r{display:flex;justify-content:space-between;gap:12px}
.ap2-r .r{text-align:right;align-items:flex-end;display:flex;flex-direction:column}
.ap2-r > span{display:flex;flex-direction:column;gap:4px}
.bd{position:relative;margin-top:28px}
.bd-tr{display:block;position:relative;height:10px;border-radius:10px;background:#E6EAF3;overflow:hidden}
.bd-tr i{position:absolute;inset:0;background:linear-gradient(90deg,#C9D7FA,#1652F0);transform-origin:left;animation:bdG 1s cubic-bezier(.2,.8,.2,1) .2s both}
@keyframes bdG{from{transform:scaleX(0)}}
.bd-pin{position:absolute;top:-6px;width:4px;height:22px;margin-left:-2px;border-radius:4px;background:#0B1433;box-shadow:0 0 0 3px #FFFFFF;animation:pnD .8s cubic-bezier(.2,.9,.3,1.4) .5s both}
@keyframes pnD{from{transform:translateY(-10px);opacity:0}}
.bd-pin em{position:absolute;bottom:calc(100% + 6px);left:50%;transform:translateX(-50%);padding:2px 8px;border-radius:7px;background:#0B1433;color:#FFFFFF;font-style:normal;font-size:11.5px;font-weight:600;white-space:nowrap}
.bd-pin.out{background:#B42318}.bd-pin.out em{background:#B42318}
.bd-l{margin-top:10px;display:flex;justify-content:space-between;align-items:center;font-size:12px;color:#8A93AD}
.bd-l b{font-size:12.5px;font-weight:600;color:#3A4566}
.bd.iv{margin:34px 4px 6px 4px}
.bd.iv .bd-tr{overflow:visible}
.bd.iv .bd-tr::after{content:'';position:absolute;left:100%;top:0;width:18%;height:100%;border-radius:0 10px 10px 0;background:repeating-linear-gradient(135deg,#FDECEA 0 5px,#F5C2BD 5px 10px)}
.aa-r,.ch2-r,.bk-r{display:flex;align-items:center;gap:12px;padding:12px 0;border-top:1.5px solid #F0F2F8}
.aa-r:nth-child(2),.ch2-r:first-child,.bk-r:nth-of-type(1){border-top:0}
.aa-r > span:nth-child(2),.ch2-r > span:nth-child(2),.bk-r > span:nth-child(2){flex:1;min-width:0;display:flex;flex-direction:column;gap:2px}
.aa-r b,.ch2-r b,.bk-r b{font-size:14px;font-weight:600}
.aa-r em,.ch2-r em,.bk-r em{font-style:normal;font-size:12.5px;line-height:1.45;color:#5B6582}
.aa-i{width:34px;height:34px;flex-shrink:0;border-radius:11px;display:flex;align-items:center;justify-content:center}
.aa-i.gold{background:#FFF6DD}.aa-i.blue{background:#EEF3FF}
.aa-i .dlp-c,.aa-i .cr-c{width:20px;height:20px;font-size:11px}
.pr2{display:flex;flex-direction:column;align-items:flex-start;gap:8px;background:linear-gradient(160deg,#F2FAF5,#FFFFFF 70%);border-color:#CFE8DB}
.pr2-i{width:40px;height:40px;border-radius:13px;background:#0F6B45;color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 0 rgba(15,107,69,.3);animation:prP 3s ease-out infinite}
@keyframes prP{0%{box-shadow:0 0 0 0 rgba(15,107,69,.3)}70%,100%{box-shadow:0 0 0 12px rgba(15,107,69,0)}}
.pr2 b{font-size:15px;font-weight:600;color:#0F6B45}
.pr2 p{margin:0;font-size:13px;line-height:1.55;color:#2C5240}
.pr2 .ds-ghost{margin-top:6px}
.pe-h{display:flex;align-items:center;gap:14px}
.pe-h > div{flex:1;display:flex;flex-direction:column;align-items:flex-start;gap:6px}
.pe-h h2{margin:0;font-size:17px;font-weight:600}
.pe-i{width:48px;height:48px;flex-shrink:0;border-radius:15px;display:flex;align-items:center;justify-content:center}
.pe-i.blue{background:#EEF3FF}.pe-i.gold{background:#FFF6DD}
.pe-v{font-size:30px;font-weight:600;letter-spacing:-0.03em}
.pe-v small{font-size:14px;font-weight:500;color:#5B6582;letter-spacing:0}
.pe-sl .bd{margin-top:34px}
.pe-st{margin-top:14px;display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:6px}
.pe-s{height:38px;border-radius:12px;border:1.5px solid #E6EAF3;background:#FFFFFF;font-family:inherit;font-size:13.5px;font-weight:600;color:#3A4566;cursor:pointer;transition:border-color .2s ease,background .2s ease,transform .2s ease}
.pe-s:hover{border-color:#9DB8F7;transform:translateY(-1px)}
.pe-s.on{border-color:#1652F0;background:#F5F8FF;color:#0E3BB8;box-shadow:0 0 0 3px rgba(22,82,240,.12)}
.pe-n{margin:14px 0 0 0;font-size:13px;line-height:1.5;color:#5B6582}
.pe-lk{background:linear-gradient(150deg,#FFFDF5,#FFFFFF 60%)}
.pe-lk .ds-tag{gap:4px}
.pe-w{margin:14px 0 0 0;display:flex;gap:10px;padding:12px 14px;border-radius:14px;background:#FFF8EA;font-size:13px;line-height:1.5;color:#6B4A00}
.pe-w svg{flex-shrink:0;margin-top:1px;color:#B76E00}
.tgl{position:relative;width:46px;height:26px;flex-shrink:0;border-radius:999px;border:0;background:#D6DDEE;cursor:pointer;transition:background .25s ease}
.tgl i{position:absolute;top:3px;left:3px;width:20px;height:20px;border-radius:50%;background:#FFFFFF;box-shadow:0 1px 3px rgba(11,20,51,.25);transition:left .25s cubic-bezier(.3,1.4,.5,1)}
.tgl.on{background:#1652F0}.tgl.on i{left:23px}
.rs3{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.ds-opt.sm{padding:12px 14px;border-radius:14px}
.ds-opt.sm .o-t b{font-size:14px;font-weight:500}
.pv3 .pv-c{display:block;border-radius:16px;border:1.5px solid #E6EAF3;overflow:hidden;background:#FFFFFF}
.pv3 .pv-cv{position:relative;display:block;height:96px;background:radial-gradient(circle at 85% 20%,rgba(92,134,255,.75),rgba(92,134,255,0) 55%),linear-gradient(140deg,#1652F0,#0B1433)}
.pv3 .pv-cv i{position:absolute;left:14px;bottom:8px;font-style:normal;font-size:24px;font-weight:600;color:#FFFFFF}
.pv3 .pv-cv em{position:absolute;right:14px;height:5px;border-radius:5px;background:rgba(255,255,255,.25)}
.pv3 .pv-cv em:nth-of-type(1){top:18px;width:60px}.pv3 .pv-cv em:nth-of-type(2){top:30px;width:40px}.pv3 .pv-cv em:nth-of-type(3){top:42px;width:52px}
.pv3 .pv-c > b{display:block;padding:10px 14px 0 14px;font-size:14.5px;font-weight:600}
.pv3-p{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));margin-top:10px;border-top:1.5px solid #F0F2F8}
.pv3-p > span{display:flex;align-items:center;gap:6px;padding:10px 14px;font-size:12px;color:#5B6582}
.pv3-p > span + span{border-left:1.5px solid #F0F2F8}
.pv3-p b{font-size:15px;font-weight:600;color:#0B1433}
.pv3-p .dlp-c,.pv3-p .cr-c{width:16px;height:16px;font-size:9px}
.pv3-n b{animation:pvN 2.4s ease-in-out infinite}
@keyframes pvN{50%{color:#1652F0}}
.cmp{padding:6px 20px}
.cmp-r{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr) 30px minmax(0,1fr);align-items:center;gap:12px;padding:13px 0;border-top:1.5px solid #F0F2F8;font-size:14px}
.cmp-r:first-child{border-top:0}
.cmp-hd{font-size:12.5px;font-weight:500;color:#8A93AD;padding:10px 0}
.cmp-r > span:first-child{color:#3A4566}
.cmp-o{color:#5B6582}
.cmp-n{font-weight:600}
.cmp-a{color:#1652F0;display:flex}
.cmp-r.ch{margin:0 -12px;padding:13px 12px;border-radius:14px;background:#F5F8FF;border-top-color:transparent}
.cmp-r.ch + .cmp-r{border-top-color:transparent}
.cmp-r.ch .cmp-o{text-decoration:line-through;text-decoration-thickness:1.5px}
.cmp-r.ch .cmp-n{color:#0E3BB8;animation:dfIn .5s ease .3s both}
@keyframes dfIn{from{opacity:0;transform:translateX(-6px)}}
.im3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.im{display:flex;flex-direction:column;gap:4px;padding:14px 16px;border-radius:16px;background:#F7F9FD;animation:obIn .5s ease both;animation-delay:calc(var(--i) * 80ms + 200ms)}
.wk-m > .im3 .im{background:#FFFFFF;border:1.5px solid #E6EAF3}
.im-i{width:26px;height:26px;margin-bottom:6px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#FFFFFF}
.im.ok .im-i{background:#0F6B45}.im.cb .im-i{background:#1652F0}.im.am .im-i{background:#B76E00}.im.rd .im-i{background:#B42318}.im.gy .im-i{background:#8A93AD}
.im em{font-style:normal;font-size:12.5px;color:#5B6582}
.im b{font-size:15px;font-weight:600}
.im.ok b{color:#0F6B45}.im.rd b{color:#B42318}
.ef-r{display:flex;align-items:center;gap:12px;padding:10px 0;border-top:1.5px solid #F0F2F8}
.ef-r:nth-child(2){border-top:0;padding-top:0}
.ef-i{width:34px;height:34px;flex-shrink:0;border-radius:11px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.ef-r > span:last-child{display:flex;flex-direction:column;gap:2px}
.ef-r em{font-style:normal;font-size:12px;color:#8A93AD}
.ef-r b{font-size:14px;font-weight:600}
.pd-v{display:flex;align-items:baseline;gap:10px}
.pd-v s{font-size:20px;color:#8A93AD;text-decoration-thickness:2px}
.pd-v svg{align-self:center;color:#1652F0}
.pd-v b{font-size:34px;font-weight:600;letter-spacing:-0.03em;color:#0E3BB8;animation:pdC 2.4s ease-in-out infinite}
@keyframes pdC{50%{transform:translateY(-2px)}}
.pd-v small{font-size:13px;color:#5B6582}
.pd-d{display:inline-flex;margin-top:8px;height:24px;align-items:center;padding:0 9px;border-radius:999px;background:#EAF0FF;color:#0E3BB8;font-size:12px;font-weight:600}
.ko-in{display:flex;justify-content:center;padding:30px 0 20px 0}
.ko{width:min(640px,100%);display:flex;flex-direction:column;align-items:center;text-align:center;--k:#0F6B45;--kb:#E7F5EE}
.ko-v.am{--k:#B97A10;--kb:#FFF4E0}.ko-v.rd{--k:#B42318;--kb:#FDECEA}
.ko.am .ko-pill{background:#FFF4E0;color:#8A5A00}.ko.rd .ko-pill{background:#FDECEA;color:#B42318}
.ko-h1{margin:14px 0 0 0;font-size:34px;line-height:1.12;font-weight:600;letter-spacing:-0.03em}
.ko-sub{margin:10px 0 0 0;max-width:540px;font-size:15.5px;line-height:1.55;color:#4A5578}
.ko-card{margin-top:24px;width:100%;box-sizing:border-box;padding:20px 22px;border-radius:22px;border:1.5px solid #E6EAF3;background:#FFFFFF;text-align:left}
.ko-acts{margin-top:24px;display:flex;align-items:center;justify-content:center;gap:12px}
.ko-n{margin:14px 0 0 0;display:flex;gap:10px;padding:12px 14px;border-radius:14px;background:#F7F9FD;font-size:13px;line-height:1.5;color:#3A4566}
.ko-n svg{flex-shrink:0;margin-top:2px;color:#8A93AD}
.pn3{margin-top:24px;width:100%;display:grid;grid-template-columns:1fr auto 1fr 1fr;align-items:center;gap:10px}
.pn3 > span{display:flex;flex-direction:column;gap:2px;padding:16px;border-radius:18px;background:#FFFFFF;border:1.5px solid #E6EAF3}
.pn3 > span b{font-size:28px;font-weight:600;letter-spacing:-0.03em}
.pn3 > span:first-child b{color:#8A93AD;text-decoration:line-through;text-decoration-thickness:2px}
.pn3 em{font-style:normal;font-size:12.5px;color:#5B6582}
.pn3 i{color:#1652F0;display:flex;animation:pnA 1.6s ease-in-out infinite}
@keyframes pnA{50%{transform:translateX(3px)}}
.pn3 .nw{border-color:#1652F0;background:#F5F8FF}
.pn3 .nw b{color:#0E3BB8}
.ko.am .pn3 .nw{border-color:#E0A030;background:#FFF8EA}.ko.am .pn3 .nw b{color:#8A5A00}
.pn3 .dlr{background:#FFFAEB;border-color:#F4E2B0}
.iv-g{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.iv-g > div{display:flex;flex-direction:column;align-items:flex-start;gap:4px;padding:14px;border-radius:16px;background:#F7F9FD}
.iv-g em{font-style:normal;font-size:12.5px;color:#5B6582}
.iv-g b{font-size:22px;font-weight:600}
.iv-g b.rd{color:#B42318}
.ht{padding:6px 20px}
.ht-r{display:grid;grid-template-columns:140px minmax(0,1.4fr) minmax(0,.8fr) minmax(0,.9fr) 100px;align-items:center;gap:12px;padding:14px 0;border-top:1.5px solid #F0F2F8;font-size:14px;animation:obIn .5s ease both;animation-delay:calc(var(--i,0) * 90ms + 150ms)}
.ht-r:first-child{border-top:0}
.ht-hd{font-size:12.5px;font-weight:500;color:#8A93AD;padding:10px 0}
.ht-d{display:flex;align-items:center;gap:10px;color:#3A4566;font-variant-numeric:tabular-nums}
.ht-d i{width:10px;height:10px;border-radius:50%;background:#1652F0;box-shadow:0 0 0 4px #EAF0FF}
.ht-r b{font-weight:600}
.ht-p{color:#8A93AD}
.ht-n{font-weight:600}
.ht-r .ds-tag{justify-self:start}
.spk{width:100%;height:auto;display:block}
.spk-a{stroke:#1652F0;stroke-width:3;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:300;stroke-dashoffset:300;animation:spD 1.4s ease .3s forwards}
@keyframes spD{to{stroke-dashoffset:0}}
.spk circle{fill:#FFFFFF;stroke:#1652F0;stroke-width:2.5}
.spk circle.nw{fill:#1652F0;animation:spP 2s ease-out 1.6s infinite}
@keyframes spP{0%{stroke-width:2.5}50%{stroke-width:7;stroke:rgba(22,82,240,.3)}100%{stroke-width:2.5}}
.spk-l{display:flex;justify-content:space-between;font-size:12px;color:#5B6582}
.vrow{display:grid;grid-template-columns:minmax(0,1fr) 34px minmax(0,1fr);align-items:stretch}
.vrow-x{position:relative;display:flex;align-items:center;justify-content:center}
.vrow-x i{width:100%;height:2px;background:repeating-linear-gradient(90deg,#9DB8F7 0 5px,transparent 5px 9px);background-size:18px 2px;animation:vrM 1s linear infinite}
@keyframes vrM{to{background-position:18px 0}}
.vc{display:flex;flex-direction:column;gap:10px;padding:20px;border-radius:22px;border:1.5px solid #E6EAF3;background:#FFFFFF}
.vc header{display:flex;align-items:center;justify-content:space-between;gap:10px}
.vc-k{font-size:12.5px;font-weight:500;color:#8A93AD}
.vc-v{font-size:26px;font-weight:600;letter-spacing:-0.02em}
.vc.live{background:linear-gradient(160deg,#F2FAF5,#FFFFFF 60%);border-color:#CFE8DB}
.vc.draft{background:linear-gradient(160deg,#FFF8EA,#FFFFFF 60%);border-color:#F4DDAA}
.vc dl{margin:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.vc dt{font-size:12px;color:#8A93AD}
.vc dd{margin:2px 0 0 0;font-size:14px;font-weight:600}
.vc dd.gold{color:#8A5A00}
.vc .ds-link{margin-top:auto;display:inline-flex;align-items:center;gap:6px}
.vc-p{margin:0;font-size:13.5px;line-height:1.5;color:#3A4566}
.vc-n{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px}
.vc-n span{display:flex;flex-direction:column;gap:1px;padding:10px;border-radius:12px;background:#FFFFFF;border:1.5px solid #F4E2B0}
.vc-n b{font-size:20px;font-weight:600}
.vc-n em{font-style:normal;font-size:11.5px;line-height:1.3;color:#5B6582}
.vc-cr{display:flex;align-items:center;justify-content:space-between;font-size:13px}
.vc-cr em{font-style:normal;color:#5B6582}
.vc-a{margin-top:auto;display:flex;align-items:center;gap:14px}
.vc.new{align-items:flex-start;justify-content:center;border-style:dashed;border-color:#C9D7FA;background:linear-gradient(160deg,#F5F8FF,#FFFFFF 60%)}
.vc.new b{font-size:17px;font-weight:600}
.vc-pl{width:46px;height:46px;border-radius:15px;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center;animation:vcP 2.4s ease-in-out infinite}
@keyframes vcP{50%{transform:rotate(90deg)}}
.rdy{display:flex;align-items:center;gap:14px;padding:16px 18px}
.rdy-i{width:42px;height:42px;flex-shrink:0;border-radius:13px;background:#EAF0FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.rdy > div{flex:1}
.rdy b{font-size:15px;font-weight:600}
.rdy p{margin:2px 0 0 0;font-size:13.5px;color:#5B6582}
.vh2-h{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px}
.vh2-h .rx-k{margin:0}
.vh2 ol{list-style:none;margin:0;padding:0;position:relative}
.vh2 ol::before{content:'';position:absolute;left:5px;top:12px;bottom:12px;width:2px;background:#E6EAF3}
.vh2 li{position:relative;display:flex;align-items:flex-start;gap:12px;padding:8px 0}
.vh2 li > span:nth-child(2){flex:1;display:flex;flex-direction:column;gap:2px;min-width:0}
.vh2 b{font-size:13.5px;font-weight:600}
.vh2 em{font-style:normal;font-size:12px;color:#5B6582}
.vh2-d{position:relative;z-index:1;width:12px;height:12px;flex-shrink:0;margin-top:3px;box-sizing:border-box;border-radius:50%;border:3px solid #FFFFFF;box-shadow:0 0 0 1.5px #CBD3E6;background:#8A93AD}
.vh2 li.amber .vh2-d{background:#E0A030}.vh2 li.green .vh2-d{background:#0F6B45}.vh2 li.blue .vh2-d{background:#1652F0}
.vh2 .ds-tag{height:22px;font-size:11px}
.ar{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.ds-opt.ar-o{align-items:flex-start;padding:14px}
.ds-opt.ar-o .o-t b{font-size:14.5px;font-weight:600}
.ds-opt.ar-o .o-t span{font-size:12.5px;line-height:1.45;color:#5B6582}
.ar-i{width:36px;height:36px;flex-shrink:0;border-radius:11px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.ds-opt.on .ar-i{background:#FFFFFF}
.br{position:relative}
.br-s{width:100%;height:auto;display:block}
.br-m{stroke:#0F6B45;stroke-width:4;stroke-linecap:round;fill:none}
.br-b{stroke:#E0A030;stroke-width:4;stroke-linecap:round;fill:none;stroke-dasharray:240;stroke-dashoffset:240;animation:spD 1.4s ease .4s forwards}
.br-n{position:absolute;display:flex;flex-direction:column;padding:6px 10px;border-radius:12px;background:#FFFFFF;border:1.5px solid #E6EAF3;box-shadow:0 8px 18px -12px rgba(11,20,51,.35)}
.br-n em{font-style:normal;font-size:11px;color:#8A93AD}
.br-n b{font-size:15px;font-weight:600}
.br-n.a{left:16px;bottom:16px;border-color:#CFE8DB}
.br-n.b{right:16px;top:40px;border-color:#F4DDAA;animation:obIn .5s ease 1.4s both}
.ok2{display:flex;gap:12px}
.ok2-i{width:34px;height:34px;flex-shrink:0;border-radius:11px;background:#E7F5EE;color:#0F6B45;display:flex;align-items:center;justify-content:center}
.ok2 p{margin:0;font-size:13px;line-height:1.55;color:#3A4566}
.vs2{display:grid;grid-template-columns:minmax(0,1fr) 40px minmax(0,1fr);align-items:center;gap:0 6px;padding:18px 20px}
.vs2-c{display:flex;flex-direction:column;align-items:flex-start;gap:6px;padding:14px 16px;border-radius:16px;background:#F2FAF5}
.vs2-c.dr{background:#FFF8EA}
.vs2-c em{font-style:normal;font-size:12px;color:#5B6582}
.vs2-c b{font-size:20px;font-weight:600}
.vs2-x{display:flex;justify-content:center;color:#1652F0;animation:pnA 1.6s ease-in-out infinite}
.vs2-n{grid-column:1 / -1;margin-top:14px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
.vs2-n span{display:flex;align-items:baseline;gap:8px;padding:12px 14px;border-radius:14px;border:1.5px solid #E6EAF3}
.vs2-n b{font-size:22px;font-weight:600}
.vs2-n .m b{color:#1652F0}.vs2-n .a b{color:#0F6B45}.vs2-n .r b{color:#B42318}
.vs2-n em{font-style:normal;font-size:13px;color:#5B6582}
.cs3{list-style:none;margin:0;padding:0}
.cs3 li{display:grid;grid-template-columns:32px minmax(0,1fr) auto;align-items:center;gap:12px;padding:13px 0;border-top:1.5px solid #F0F2F8;animation:obIn .5s ease both;animation-delay:calc(var(--i) * 80ms + 200ms)}
.cs3 li:first-child{border-top:0;padding-top:0}
.cs3-i{width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#FFFFFF}
.cs3 li.green .cs3-i{background:#0F6B45}.cs3 li.blue .cs3-i{background:#1652F0}.cs3 li.gy .cs3-i{background:#CBD3E6}
.cs3 li > span:nth-child(2){display:flex;flex-direction:column;gap:2px;min-width:0}
.cs3 em{font-style:normal;font-size:12px;font-weight:500;color:#8A93AD}
.cs3 b{font-size:14.5px;font-weight:500}
.cs3 li.gy b{color:#8A93AD}
.dd-b{display:flex;gap:3px;height:10px}
.dd-b i{border-radius:5px;transform-origin:left;animation:bdG .8s ease .3s both}
.dd-b .m,.dd ul i.m{background:#1652F0}.dd-b .a,.dd ul i.a{background:#0F6B45}.dd-b .r,.dd ul i.r{background:#D92D20}
.dd ul{list-style:none;margin:12px 0 0 0;padding:0;display:flex;flex-direction:column;gap:8px}
.dd li{display:flex;align-items:center;gap:8px;font-size:13.5px;color:#3A4566}
.dd li i{width:8px;height:8px;border-radius:50%}
.dd li b{margin-left:auto;font-weight:600;color:#0B1433}
.rdb{display:flex;gap:3px;height:8px;margin-bottom:12px}
.rdb i{border-radius:5px;background:#0F6B45;transform-origin:left;animation:bdG .8s ease .3s both}
.rdb i.f{background:#E0A030}
.rl2{list-style:none;margin:0;padding:0}
.rl2 li{display:flex;align-items:center;gap:12px;min-height:46px;border-top:1.5px solid #F0F2F8;font-size:14px;animation:obIn .5s ease both;animation-delay:calc(var(--i) * 70ms + 200ms)}
.rl2 li:first-child{border-top:0}
.rl2 li > span{width:22px;height:22px;flex-shrink:0;border-radius:50%;display:flex;align-items:center;justify-content:center}
.rl2 li.ok > span{background:#E7F5EE;color:#0F6B45}
.rl2 li.no{margin:4px -10px;padding:0 10px;border-radius:12px;background:#FFF8EA;border-top-color:transparent}
.rl2 li.no + li{border-top-color:transparent}
.rl2 li.no > span{background:#FFE7B8;color:#8A5A00}
.rl2 li b{flex:1;font-weight:500}
.rl2 li .ds-ghost{background:#FFFFFF}
.cl3-v{display:block;font-size:20px;font-weight:600}
.cl3-s{margin-top:14px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:4px}
.cl3-s i{height:8px;border-radius:4px;background:#E6EAF3}
.cl3-s i.on{background:#1652F0;animation:clP 2s ease-in-out infinite}
@keyframes clP{50%{opacity:.6}}
.cl3-l{margin-top:6px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));font-size:12px;color:#8A93AD;text-align:center}
.cl3-l .on{color:#0E3BB8;font-weight:600}
.tk2{padding:20px 22px}
.tk2-l{display:flex;align-items:center;gap:0;padding:16px;border-radius:18px;background:#F7F9FD}
.tk2-r{display:flex;align-items:center;gap:8px;padding:8px 12px;border-radius:999px;background:#FFFFFF;border:1.5px solid #E6EAF3;font-size:13px;white-space:nowrap}
.tk2-r b{font-weight:600}
.tk2-r em{font-style:normal;color:#5B6582}
.tk2-r.live{color:#0F6B45;border-color:#CFE8DB}
.tk2-r.rv{border-color:#C9D7FA}
.tk2.am .tk2-r.rv{border-color:#F4DDAA}
.tk2-dot{width:9px;height:9px;border-radius:50%;background:#1652F0;animation:rvP 1.6s ease-out infinite}
.tk2.am .tk2-dot{background:#E0A030}
@keyframes rvP{0%{box-shadow:0 0 0 0 rgba(22,82,240,.45)}100%{box-shadow:0 0 0 8px rgba(22,82,240,0)}}
.tk2-line{flex:1;height:2px;margin:0 8px;position:relative;overflow:hidden;background:#E6EAF3}
.tk2-line i{position:absolute;top:0;bottom:0;width:30%;background:linear-gradient(90deg,transparent,#1652F0,transparent);animation:tkS 1.8s ease-in-out infinite}
.tk2.am .tk2-line i{background:linear-gradient(90deg,transparent,#E0A030,transparent)}
@keyframes tkS{from{left:-30%}to{left:100%}}
.tk2-f{margin:16px 0 0 0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}
.tk2-f dt{font-size:12px;color:#8A93AD}
.tk2-f dd{margin:4px 0 0 0;font-size:14px;font-weight:600}
.tk2-n{margin:14px 0 0 0;display:flex;align-items:center;gap:8px;padding:10px 12px;border-radius:12px;background:#F2FAF5;font-size:13px;color:#2C5240}
.tk2-n svg{flex-shrink:0;color:#0F6B45}
.fd{display:flex;gap:14px;padding:18px 20px;border-color:#F4DDAA;background:linear-gradient(150deg,#FFF8EA,#FFFFFF 60%)}
.fd-i{width:42px;height:42px;flex-shrink:0;border-radius:13px;background:#B76E00;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.sv-b2{display:inline-flex;height:22px;align-items:center;padding:0 8px;border-radius:7px;background:#FFF4E0;color:#8A5A00;font-size:11px;font-weight:600;letter-spacing:.04em;text-transform:uppercase}
.fd b{display:block;margin-top:6px;font-size:15.5px;font-weight:600}
.fd p{margin:4px 0 0 0;font-size:13.5px;line-height:1.55;color:#3A4566}
.vt2{padding:20px 22px}
.vt2-h{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.vt2-h .rx-k{margin:0}
.vt2-r{display:grid;grid-template-columns:minmax(0,1fr) 70px minmax(0,1fr) minmax(0,1.3fr);align-items:center;gap:10px}
.vt2-c{display:flex;flex-direction:column;gap:4px;padding:14px 16px;border-radius:16px;background:#F7F9FD}
.vt2-c em{font-style:normal;font-size:12px;color:#5B6582}
.vt2-c b{display:flex;align-items:center;gap:6px;font-size:22px;font-weight:600}
.vt2-c.nw{background:#F5F8FF;box-shadow:inset 0 0 0 1.5px #1652F0}
.vt2-c.nw b{color:#0E3BB8}
.vt2-c.g{background:#FFFAEB}
.vt2-c.g b{font-size:14.5px;color:#8A5A00}
.vt2-a{display:flex;justify-content:center;gap:5px}
.vt2-a i{width:8px;height:8px;border-radius:50%;background:#1652F0;opacity:.25;animation:vtA 1.2s ease-in-out infinite}
.vt2-a i:nth-child(2){animation-delay:.2s}.vt2-a i:nth-child(3){animation-delay:.4s}
@keyframes vtA{50%{opacity:1;transform:scale(1.2)}}
.vl{padding:6px 20px}
.vl-r{display:grid;grid-template-columns:110px minmax(0,1.2fr) minmax(0,.9fr) minmax(0,.9fr) 210px;align-items:center;gap:12px;padding:14px 0;border-top:1.5px solid #F0F2F8;font-size:14px;animation:obIn .5s ease both;animation-delay:calc(var(--i,0) * 90ms + 150ms)}
.vl-r:first-child{border-top:0}
.vl-hd{font-size:12.5px;font-weight:500;color:#8A93AD;padding:10px 0}
.vl-v{display:flex;align-items:center;gap:10px}
.vl-v i{width:10px;height:10px;border-radius:50%}
.vl-v i.amber{background:#E0A030}.vl-v i.green{background:#0F6B45;animation:lvP 2s ease-out infinite}
.vl-v b{font-size:15px;font-weight:600}
.vl-r .ds-tag{justify-self:start}
.vl-pd{color:#8A93AD}
.vl-d{color:#3A4566}
.vl-a{display:flex;align-items:center;justify-content:flex-end;gap:12px}
.imm{display:flex;gap:12px}
.imm-i{width:36px;height:36px;flex-shrink:0;border-radius:11px;background:#0B1433;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.imm p{margin:0;font-size:13px;line-height:1.55;color:#3A4566}
.st4b{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}
.sb{position:relative;overflow:hidden;display:flex;flex-direction:column;gap:2px;padding:16px;border-radius:18px;background:#FFFFFF;border:1.5px solid #E6EAF3;animation:obIn .5s ease both;animation-delay:calc(var(--i) * 70ms + 150ms)}
.sb::after{content:'';position:absolute;left:0;right:0;bottom:0;height:4px;background:var(--c)}
.sb.all{--c:#0B1433}.sb.cb{--c:#1652F0}.sb.bl{--c:#5C86FF}.sb.ok{--c:#0F6B45}
.sb b{font-size:28px;font-weight:600;letter-spacing:-0.03em}
.sb span{font-size:13.5px;font-weight:600}
.sb em{font-style:normal;font-size:12px;color:#5B6582}
.dr2{padding:18px 20px 8px 20px}
.dr-h{display:flex;align-items:center;justify-content:space-between}
.dr-h h2{margin:0;font-size:16px;font-weight:600}
.dr-t{margin-top:14px;display:flex;align-items:center;gap:8px}
.dr-s{flex:1;display:flex;align-items:center;gap:8px;height:40px;padding:0 14px;border-radius:999px;background:#F7F9FD;color:#8A93AD}
.dr-s input{flex:1;min-width:0;border:0;background:none;outline:none;font-family:inherit;font-size:13.5px}
.dr-f{width:150px;flex-shrink:0}
.dr-f .ds-in{height:40px;font-size:13px;border-radius:999px;padding-left:14px}
.dr-l{margin-top:6px}
.lr{display:grid;grid-template-columns:minmax(0,1.4fr) 110px 120px minmax(0,1.2fr) 112px;align-items:center;gap:12px;padding:12px 0;border-top:1.5px solid #F0F2F8;animation:obIn .45s ease both;animation-delay:calc(var(--i,0) * 60ms + 250ms)}
.lr-hd{border-top:0;font-size:12.5px;font-weight:500;color:#8A93AD;padding:10px 0 6px 0;animation:none}
.lr.on{margin:0 -10px;padding:12px 10px;border-radius:14px;background:#F5F8FF;box-shadow:inset 3px 0 0 #1652F0}
.lr-n{display:flex;align-items:center;gap:10px;min-width:0}
.lr-n b{font-size:14.5px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.la2{width:36px;height:36px;flex-shrink:0;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;color:#FFFFFF}
.la2.lg{width:56px;height:56px;font-size:17px}
.h1{background:linear-gradient(135deg,#5C86FF,#1652F0)}.h2{background:linear-gradient(135deg,#34C38F,#0F6B45)}.h3{background:linear-gradient(135deg,#F4B860,#B76E00)}.h4{background:linear-gradient(135deg,#8A93AD,#3A4566)}.h5{background:linear-gradient(135deg,#C49BF5,#6B3FC2)}
.lr-ac{display:inline-flex;align-items:center;gap:6px;font-size:13px;font-weight:500}
.lr-ac .dlp-c,.lr-ac .cr-c{width:18px;height:18px;font-size:10px}
.lr .ds-tag{justify-self:start}
.lr-p{display:flex;flex-direction:column;gap:4px}
.lr-b{display:block;height:6px;border-radius:6px;background:#EEF1F7;overflow:hidden}
.lr-b i{display:block;height:100%;border-radius:6px;background:linear-gradient(90deg,#5C86FF,#1652F0);transform-origin:left;animation:bdG .9s ease .5s both}
.lr-p em{font-style:normal;font-size:12px;color:#5B6582}
.lr .ds-ghost{justify-self:end}
.bk-b{display:flex;gap:3px;height:12px;margin-bottom:6px}
.bk-b i{border-radius:6px;transform-origin:left;animation:bdG .9s ease .3s both}
.bk-b .g{background:linear-gradient(90deg,#F4D98E,#D99A1E)}.bk-b .b{background:#1652F0}
.bk-n{margin-left:auto;font-size:15px !important}
.vd-h{display:flex;align-items:flex-start;justify-content:space-between;gap:10px;margin-bottom:12px}
.vd-h .rx-k{margin:0}
.vd-r{display:flex;align-items:center;gap:12px}
.vd-r > span:nth-child(2){flex:1;display:flex;flex-direction:column;gap:2px}
.vd-r b{font-size:14px;font-weight:600}
.vd-r em{font-style:normal;font-size:12px;color:#5B6582}
.vd-v{width:44px;height:44px;flex-shrink:0;border-radius:13px;background:#0F6B45;color:#FFFFFF;font-size:13px;font-weight:600;display:flex;align-items:center;justify-content:center}
.vd-v.dr{background:#FFF4E0;color:#8A5A00;border:1.5px dashed #E0A030;box-sizing:border-box}
.vd-n{font-size:22px !important}
.vd-b{margin-top:12px;height:8px;border-radius:8px;background:#E7F5EE;overflow:hidden}
.vd-b i{display:block;width:100%;height:100%;background:#0F6B45;transform-origin:left;animation:bdG 1s ease .4s both}
.emp2{margin-top:16px;display:flex;flex-direction:column;align-items:center;gap:8px;padding:40px 24px;text-align:center}
.emp2-v{position:relative;width:180px;height:140px;margin-bottom:10px}
.emp2-r{position:absolute;left:50%;top:50%;width:110px;height:110px;margin:-55px 0 0 -55px;border-radius:50%;border:1.5px dashed #C9D7FA;animation:rmSpin 30s linear infinite}
.emp2-r.b{width:150px;height:150px;margin:-75px 0 0 -75px;border-color:#E6EAF3;animation-direction:reverse}
@keyframes rmSpin{to{transform:rotate(360deg)}}
.emp2-c{position:absolute;left:50%;top:50%;width:60px;height:60px;margin:-30px 0 0 -30px;border-radius:20px;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 14px 28px -12px rgba(22,82,240,.8)}
.emp2-s{position:absolute;width:12px;height:12px;border-radius:50%;background:#C9D7FA;animation:mtS 3.4s ease-in-out infinite}
.emp2-s.s1{left:16px;top:30px}.emp2-s.s2{right:12px;top:58px;animation-delay:-1.2s}.emp2-s.s3{left:46px;bottom:6px;animation-delay:-2.4s}
@keyframes mtS{50%{transform:translateY(-8px)}}
.emp2 > b{font-size:20px;font-weight:600}
.emp2 > p{margin:0 0 10px 0;max-width:460px;font-size:14.5px;line-height:1.6;color:#5B6582}
.dw{position:fixed;z-index:1001;top:0;right:0;bottom:0;width:440px;max-width:100vw;box-sizing:border-box;overflow-y:auto;padding:22px 24px;background:#FFFFFF;box-shadow:-24px 0 64px rgba(11,20,51,.2);display:flex;flex-direction:column;gap:16px;animation:dwIn .5s cubic-bezier(.2,.8,.2,1) both}
@keyframes dwIn{from{transform:translateX(40px);opacity:0}}
.dw-h{display:flex;align-items:center;justify-content:space-between}
.dw-h .rx-k{margin:0}
.dw-p{display:flex;align-items:center;gap:14px}
.dw-p > div{display:flex;flex-direction:column;gap:4px}
.dw-p b{font-size:18px;font-weight:600}
.dw-p em{font-style:normal;font-size:12.5px;color:#8A93AD}
.dw-pg{padding:14px;border-radius:16px;background:#F5F8FF}
.dw-r{display:flex;align-items:center;gap:14px}
.dw-r > span{display:flex;flex-direction:column}
.dw-r b{font-size:22px;font-weight:600}
.dw-r em{font-style:normal;font-size:12.5px;color:#5B6582}
.dw-s{border:1.5px solid #E6EAF3;border-radius:16px;padding:12px 14px}
.dw-k{display:block;margin-bottom:6px;font-size:12px;font-weight:600;color:#8A93AD}
.dw-s dl{margin:0}
.dw-s dl div{display:flex;justify-content:space-between;gap:12px;padding:7px 0;font-size:13.5px}
.dw-s dt{color:#5B6582}
.dw-s dd{margin:0;display:flex;align-items:center;gap:5px;font-weight:600}
.dw-s .dlp-c{width:16px;height:16px}
.dw-n{margin:0;display:flex;gap:8px;font-size:12.5px;line-height:1.5;color:#5B6582}
.dw-n svg{flex-shrink:0;margin-top:2px}
.dw-a{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;margin-top:auto}
.va2{margin-top:20px;display:grid;grid-template-columns:minmax(0,1.2fr) 40px minmax(0,1fr);align-items:center}
.va-c{display:flex;flex-direction:column;gap:14px;padding:20px}
.va-c header{display:flex;align-items:flex-start;gap:12px}
.va-c header > div{flex:1;display:flex;flex-direction:column;gap:3px;min-width:0}
.va-c header b{font-size:17px;font-weight:600}
.va-c header em{font-style:normal;font-size:13px;line-height:1.5;color:#5B6582}
.va-c.live{background:linear-gradient(160deg,#F2FAF5,#FFFFFF 60%);border-color:#CFE8DB}
.va-c.up{border-style:dashed;border-color:#F4DDAA;background:linear-gradient(160deg,#FFFCF5,#FFFFFF 60%)}
.va-b{display:flex;gap:3px;height:12px}
.va-b i{border-radius:6px;transform-origin:left;animation:bdG .9s ease .3s both}
.va-b .cb,.va-s .cb i{background:#1652F0}.va-b .ok,.va-s .ok i{background:#0F6B45}.va-b .gy,.va-s .gy i{background:#CBD3E6}
.va-s{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
.va-s > span{display:grid;grid-template-columns:8px auto;column-gap:8px;align-items:center}
.va-s i{width:8px;height:8px;border-radius:50%}
.va-s b{font-size:22px;font-weight:600}
.va-s em{grid-column:2;font-style:normal;font-size:12.5px;color:#5B6582}
.va-x{display:flex;align-items:center;justify-content:center}
.va-x i{width:100%;height:2px;background:repeating-linear-gradient(90deg,#F4C66A 0 5px,transparent 5px 9px);background-size:18px 2px;animation:vrM 1s linear infinite}
.va-e{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));gap:6px;padding:12px;border-radius:14px;background:#FFFFFF;border:1.5px dashed #F0DDAE}
.va-e i{aspect-ratio:1;border-radius:50%;border:1.5px dashed #E6C98A;animation:clP 2.4s ease-in-out infinite;animation-delay:calc(var(--i) * 120ms)}
.va-c.up .ds-ghost{align-self:flex-start}
.ma{display:flex;gap:16px;padding:20px;border-color:#F5D3CE;background:linear-gradient(150deg,#FFF7F6,#FFFFFF 60%)}
.ma-i{width:48px;height:48px;flex-shrink:0;border-radius:15px;background:#B42318;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.ma .rx-k{margin-bottom:4px}
.ma b{font-size:18px;font-weight:600}
.ma p{margin:4px 0 0 0;font-size:14px;line-height:1.55;color:#3A4566}
.lg3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.lgp{display:flex;flex-direction:column;gap:2px;padding:16px;border-radius:18px;background:#FFFFFF;border:1.5px solid #E6EAF3}
.lgp b{font-size:28px;font-weight:600;letter-spacing:-0.03em}
.lgp em{font-style:normal;font-size:12.5px;color:#5B6582}
.lg-b{margin-top:10px;height:6px;border-radius:6px;background:#EEF1F7;overflow:hidden}
.lg-b i{display:block;height:100%;border-radius:6px;transform-origin:left;animation:bdG .9s ease .4s both}
.lgp.gold .lg-b i{background:#D99A1E}.lgp.blue .lg-b i{background:#1652F0}.lgp.ok .lg-b i{background:#0F6B45}
.ru{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:8px}
.ru li{display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:12px;background:#F7F9FD;font-size:13.5px;font-weight:500}
.ru svg{color:#1652F0}
.bn2.gy{background:#F7F9FD;border-color:#E6EAF3}.bn2.gy .bn2-i{background:#5B6582}.bn2.gy p{color:#3A4566}
.bn2 .ds-ghost{align-self:center;flex-shrink:0}
@media (max-width: 1180px){.ap2-g{grid-template-columns:minmax(0,1fr)}.vrow,.va2{grid-template-columns:minmax(0,1fr)}.vrow-x,.va-x{height:24px}.vrow-x i,.va-x i{width:2px;height:100%;background:repeating-linear-gradient(180deg,#9DB8F7 0 5px,transparent 5px 9px)}.st4b{grid-template-columns:repeat(2,minmax(0,1fr))}.lr{grid-template-columns:minmax(0,1.4fr) 100px 110px minmax(0,1fr) 104px}}
@media (max-width: 960px){
.stp{margin-top:14px;max-width:none}
.stp li{flex:none;font-size:12px}
.stp li span{display:none}
.stp li.on span{display:inline}
.stp li + li::before{flex-basis:22px}
.cst2{padding:14px;gap:12px}
.cst2 .cv-t{width:44px;height:44px;border-radius:12px}
.cst2 .cst-b > b{font-size:15px}
.cst2 .cst-p{font-size:12.5px}
.wk-m{gap:14px}
.ds-acts.wk-a2{position:sticky;margin:6px -16px 0 -16px;padding:12px 16px 14px 16px;border-radius:0;border:0;border-top:1.5px solid #EEF1F7;box-shadow:none;flex-direction:column-reverse;align-items:stretch;gap:8px}
.wk-a2 .sv-r{flex-direction:column-reverse;align-items:stretch;gap:6px;margin:0;width:100%}
.wk-a2 .sv-r .ds-btn{width:100%;justify-content:space-between}
.wk-a2 .sv-r .ds-link,.wk-a2 .sv-r .ds-ghost,.wk-a2 .sv-s .ds-link,.wk-a2 .sv-s .ds-ghost{justify-content:center;min-height:40px}
.wk-a2 .sv-s{display:flex;justify-content:center;font-size:12.5px;text-align:center}
.wk-a2 .sv-s:empty{display:none}
.ds-acts.wk-a2:has(.sv-s:empty){width:auto;align-self:stretch;padding-left:16px}
.wk-a2:has(.sv-s .ds-link){flex-direction:column-reverse}
.ao2{grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.ao{padding:14px;border-radius:18px;gap:4px}
.ao-k{font-size:12.5px;gap:6px}
.ao-k .dlp-c,.ao-k .cr-c{width:22px;height:22px;font-size:12px}
.ao > .ds-tag{position:static;align-self:flex-start;height:22px;font-size:11px;order:-1}
.ao-v{margin-top:4px;font-size:24px}
.ao-v small{font-size:12px}
.ao p{font-size:11.5px;line-height:1.4}
.ao-x{right:-34px;bottom:-34px}
.ap2-g{gap:10px}
.ap2-d{flex-direction:row;flex-wrap:wrap;align-items:center;justify-content:space-between;padding:12px 14px}
.ap2-d em{flex-basis:100%}
.ap2-c{padding:14px}
.ap2-d b,.ap2-r b{font-size:16px}
.pe-h{flex-wrap:wrap;gap:10px 12px}
.pe-h > div{flex:1}
.pe-i{width:40px;height:40px;border-radius:13px}
.pe-v{font-size:24px}
.pe-h h2{font-size:15.5px}
.pe-st{grid-template-columns:repeat(7,minmax(46px,1fr));overflow-x:auto;margin:14px -18px 0 -18px;padding:0 18px 2px 18px;scrollbar-width:none}
.pe-st::-webkit-scrollbar{display:none}
.rs3{grid-template-columns:minmax(0,1fr);gap:0;border:1.5px solid #E6EAF3;border-radius:16px;overflow:hidden}
.rs3 .ds-opt{border:0;border-radius:0}
.rs3 .ds-opt + .ds-opt{border-top:1.5px solid #F0F2F8}
.rs3 .ds-opt.on{box-shadow:inset 3px 0 0 #1652F0}
.wk-r > .pv3{display:none}
.cmp{padding:2px 16px}
.cmp-hd{display:none}
.cmp-r{grid-template-columns:minmax(0,1fr) auto auto auto;gap:8px;font-size:13px}
.cmp-r > span:first-child{grid-column:1 / -1;font-size:12px;color:#8A93AD}
.cmp-r:not(.ch) .cmp-o,.cmp-r:not(.ch) .cmp-a{display:none}
.cmp-r:not(.ch){grid-template-columns:minmax(0,1fr) auto}
.cmp-r:not(.ch) > span:first-child{grid-column:1;font-size:13px;color:#3A4566}
.cmp-r.ch{margin:0 -8px;padding:12px 8px;grid-template-columns:auto auto auto 1fr}
.cmp-r.ch > span:first-child{color:#0E3BB8;font-weight:500}
.im3{grid-template-columns:repeat(3,minmax(0,1fr));gap:6px}
.im{padding:10px;border-radius:14px}
.im-i{width:22px;height:22px;margin-bottom:4px}
.im em{font-size:11px;line-height:1.3}
.im b{font-size:13px}
.wk-r > .pd{order:-1}
.ko-in{padding:16px 0 8px 0}
.ko-h1{font-size:26px}
.ko-sub{font-size:14.5px}
.pn3{grid-template-columns:1fr auto 1fr;gap:8px}
.pn3 .dlr{grid-column:1 / -1;flex-direction:row;align-items:baseline;justify-content:space-between}
.pn3 > span{padding:12px}
.pn3 > span b{font-size:22px}
.ko-card{padding:14px}
.ko-acts{flex-direction:column-reverse;width:100%;gap:8px}
.ko-acts .ds-btn{width:100%;justify-content:space-between}
.ko-acts .ds-ghost{width:100%}
.ht{padding:2px 16px}
.ht-hd{display:none}
.ht-r{grid-template-columns:minmax(0,1fr) auto;gap:4px 10px}
.ht-r > b{grid-column:1;grid-row:1}
.ht-r .ds-tag{grid-column:2;grid-row:1;justify-self:end}
.ht-d{grid-column:1;grid-row:2;font-size:12px}
.ht-p,.ht-n{display:none}
.ht-r .ht-n:not(:empty){display:block;grid-column:2;grid-row:2;justify-self:end;font-size:13px}
.vrow-x{height:16px}
.vc{padding:16px;border-radius:18px;gap:8px}
.vc-v{font-size:22px}
.vc dl{gap:8px}
.vc-a{flex-wrap:wrap;gap:8px 14px}
.vc-a .ds-ghost{flex:1}
.rdy{flex-wrap:wrap;padding:14px}
.rdy > div{flex-basis:calc(100% - 56px)}
.rdy .ds-btn{width:100%;justify-content:space-between}
.ar{grid-template-columns:minmax(0,1fr);gap:0;border:1.5px solid #E6EAF3;border-radius:16px;overflow:hidden}
.ar .ds-opt{border:0;border-radius:0;padding:12px 14px}
.ar .ds-opt + .ds-opt{border-top:1.5px solid #F0F2F8}
.ar .ds-opt.on{box-shadow:inset 3px 0 0 #1652F0}
.ar .o-t span{display:none}
.wk-r > .br{order:-1;padding:14px}
.br-s{max-height:110px}
.vs2{grid-template-columns:minmax(0,1fr) 28px minmax(0,1fr);padding:14px}
.vs2-c{padding:12px}
.vs2-c b{font-size:16px}
.vs2-n{gap:6px}
.vs2-n span{flex-direction:column;gap:0;padding:10px}
.vs2-n b{font-size:20px}
.vs2-n em{font-size:11.5px}
.wk-r > .dd{display:none}
.cs3 li{grid-template-columns:28px minmax(0,1fr) auto;gap:10px}
.cs3-i{width:28px;height:28px}
.cs3 li .ds-tag{height:22px;font-size:11px}
.rl2 li{font-size:13px;gap:10px}
.tk2{padding:14px}
.tk2-l{padding:10px;gap:0}
.tk2-r{padding:6px 10px;font-size:12px}
.tk2-f{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.fd{padding:14px}
.vt2{padding:14px}
.vt2-r{grid-template-columns:minmax(0,1fr) 36px minmax(0,1fr)}
.vt2-c.g{grid-column:1 / -1}
.vt2-c b{font-size:18px}
.vt2-a{gap:3px}
.vt2-a i{width:6px;height:6px}
.vl{padding:2px 16px}
.vl-hd{display:none}
.vl-r{grid-template-columns:auto minmax(0,1fr) auto;gap:6px 10px}
.vl-v{grid-row:1;grid-column:1}
.vl-r .ds-tag{grid-row:1;grid-column:3;justify-self:end}
.vl-r > span:nth-child(3){grid-row:1;grid-column:2}
.vl-d{grid-row:2;grid-column:1 / 3;font-size:12.5px;color:#8A93AD}
.vl-a{grid-row:2;grid-column:3}
.vl-a .ds-ghost{display:none}
.st4b{grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.sb{padding:12px 14px;border-radius:16px}
.sb b{font-size:22px}
.sb em{display:none}
.dr2{padding:14px 14px 4px 14px}
.dr-t{flex-wrap:wrap}
.dr-s{flex-basis:100%}
.dr-f{flex:1;width:auto}
.dr-t .ds-ghost{flex-shrink:0}
.lr-hd{display:none}
.lr{grid-template-columns:minmax(0,1fr) auto;gap:6px 10px}
.lr-n{grid-column:1;grid-row:1}
.lr .ds-tag{grid-column:2;grid-row:1;justify-self:end}
.lr-ac{grid-column:1;grid-row:2;padding-left:46px;font-size:12px}
.lr-p{grid-column:1 / -1;grid-row:3;padding-left:46px;flex-direction:row;align-items:center;gap:10px}
.lr-b{flex:1}
.lr-p em{white-space:nowrap;font-size:11.5px}
.lr .ds-ghost{grid-column:2;grid-row:2;height:30px;font-size:12px;padding:0 10px}
.lr.on{margin:0 -8px;padding:12px 8px}
.wk-r > .vd,.wk-r > .bk{order:3}
.wk-m > .wk-a2{order:6}
.wk-r > .cl3{order:3}
.pg-hr:has(.ds-btn){display:grid !important;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;width:100% !important;margin:0 !important;padding:0 !important;overflow:visible !important}
.pg-hr:has(.ds-btn) .ds-btn{order:-1;grid-column:1 / -1;justify-content:space-between}
.pg-hr:has(.ds-btn) .ds-ghost{justify-content:center;font-size:12.5px;padding:0 8px}
.ap2-c .bd{margin-top:36px}
.bd-pin.out em{left:auto;right:-4px;transform:none}
.dr-t .ds-ghost span{display:none}
.dr-t .ds-ghost{width:40px;padding:0;height:40px;border-radius:50%}
.wk-a2 .sv-r .ds-ghost{width:100%}
.vl-d{display:none}
.emp2{padding:28px 18px}
.dw{width:100%;top:auto;max-height:90vh;border-radius:24px 24px 0 0;padding:18px 16px;animation:dwUp .5s cubic-bezier(.2,.8,.2,1) both}
@keyframes dwUp{from{transform:translateY(40px);opacity:0}}
.va2{margin-top:16px}
.va-c{padding:16px}
.va-s b{font-size:18px}
.va-e{grid-template-columns:repeat(8,minmax(0,1fr))}
.va-e i:nth-child(n+9){display:none}
.ma{padding:16px;gap:12px}
.ma-i{width:40px;height:40px}
.lg3{grid-template-columns:repeat(3,minmax(0,1fr));gap:6px}
.lgp{padding:12px;border-radius:14px}
.lgp b{font-size:20px}
.lgp em{font-size:11px;line-height:1.3}
.bn2{flex-wrap:wrap}
.bn2 .ds-ghost{width:100%}
}
'''

write('Manage2.dc.html', doc('Manage Published Course · pricing, versions, learners · shared source', kit.KIT_CSS + '\n' + dash.DASH_CSS + BASE_CSS + WK_CSS + CSS, body(), JS))

BOARDS = [
    ('MGT-004', 'p-a', 'CR-COURSE-MGT-004 · Pricing & Access (default)'),
    ('MGT-004-D', 'p-edit', 'CR-COURSE-MGT-004-D · Edit Pricing & Access (Step 1/3)'),
    ('MGT-004-E', 'p-review', 'CR-COURSE-MGT-004-E · Review Pricing Changes (Step 2/3)'),
    ('MGT-004-G', 'p-done', 'CR-COURSE-MGT-004-G · Pricing Update Successful (Step 3/3)'),
    ('MGT-004-F', 'p-pending', 'CR-COURSE-MGT-004-F · Pricing Change — Pending Approval variant'),
    ('MGT-004-H', 'p-invalid', 'CR-COURSE-MGT-004-H · Restricted / Invalid Change'),
    ('MGT-004-I', 'p-hist', 'CR-COURSE-MGT-004-I · Pricing History'),
    ('MGT-005', 'v-a', 'CR-COURSE-MGT-005-A · Course Updates & Versions (live v1.0 + draft v1.1)'),
    ('MGT-005-NONE', 'v-none', 'CR-COURSE-MGT-005 · Course Updates & Versions (no active draft)'),
    ('MGT-005-CREATE', 'v-create', 'CR-COURSE-MGT-005A · Create Course Update'),
    ('MGT-005-COMPARE', 'v-compare', 'CR-COURSE-MGT-005B · Compare Versions'),
    ('MGT-005-READY', 'v-ready', 'CR-COURSE-MGT-005C · Update Readiness & Revalidation'),
    ('MGT-005-VALIDATE', 'v-val', 'CR-COURSE-MGT-005D · Update Under Validation'),
    ('MGT-005-CHANGES', 'v-chg', 'CR-COURSE-MGT-005 (changes requested) · Validator finding returned to creator'),
    ('MGT-005-ACTIVATE', 'v-act', 'CR-COURSE-MGT-005E · Approved Update & Activation'),
    ('MGT-005-HISTORY', 'v-hist', 'CR-COURSE-MGT-005F · Version History'),
    ('MGT-006', 'l-a', 'CR-COURSE-MGT-006A · Learner Access Dashboard'),
    ('MGT-006-EMPTY', 'l-empty', 'CR-COURSE-MGT-006A · Variant — Empty State (no learners)'),
    ('MGT-006-DETAIL', 'l-detail', 'CR-COURSE-MGT-006B · Learner Access Detail (drawer)'),
    ('MGT-006-ASSIGN', 'l-assign', 'CR-COURSE-MGT-006C · Course Version Assignments'),
    ('MGT-006-IMPACT', 'l-impact', 'CR-COURSE-MGT-006D · Learner Access Impact Review'),
    ('MGT-006-UNPUB', 'l-unpub', 'CR-COURSE-MGT-006A · Variant — Course Unpublished'),
]
BOARDS = [(c, 'Manage2', {'page': p}, t) for c, p, t in BOARDS]

if __name__ == '__main__':
    import sys
    H = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else {}
    for code, src, props, title in BOARDS:
        hd, hm = H.get(code, (3000, 3000))
        write(code + '.dc.html', wrapper(title + ' · Desktop', src, props, 1440, hd))
        write(code + '-Mobile.dc.html', wrapper(title + ' · Mobile', src, props, 390, hm))
    print('ok', len(BOARDS), 'boards; toggles', W.n)
