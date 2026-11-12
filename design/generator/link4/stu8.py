"""Link 4 · Batch 8: Manage Published Course part 3 — Validation History (MGT-007), Archive & Removal (MGT-008),
Insights & Engagement (MGT-009 + A–F). Client copy word for word (prototype-only notes omitted).

Manage3.dc.html (prop page: h-* | a-* | i-*). Same creator shell as batches 6–7; reuses stu7 helpers.
Insights pages follow the Link 2 Analytics / Discussions / Learner support patterns (one-card KPI strip,
chapter funnel with Biggest drop, discussion rows with avatar + Unanswered tag).
"""
import json
from l4kit import *
from rail import *
from kit import coin, credit, emblem
import stu6, stu7
from stu6 import cr_side, CR_TOP, crumbs, COV
from stu7 import head, strip, wk, bar, steps, outcome, GB, sel_

W = Toggles()
EXTRA['restore'] = '<path d="M3.5 12a8.5 8.5 0 1 0 2.6-6.1L3.5 8.5"></path><path d="M3.5 3.5v5h5"></path>'
PAGES = []
def P(key, body):
    PAGES.append((key, body))
def note(t, icon='info'):
    return '<p class="nt">%s<span>%s</span></p>' % (ic('lock', 13, 2) if icon == 'lock' else INFO, t)
def facts(rows, cls=''):
    return '<dl class="fx3 %s">%s</dl>' % (cls, ''.join('<div><dt>%s</dt><dd>%s</dd></div>' % r for r in rows))

# ======================================================================= MGT-007 Validation History
VH_H = lambda h1, sub, ce=None, back=('Back to Validation History', 'MGT-007.dc.html'): head('Validation History', h1, sub, back=back, crumb_extra=ce)
CEI = '''<div class="cei">%s<span class="cei-v"><b>87</b><em>/ 100</em></span></div>''' % ring(87, 132, 10, track='#F3EAD3', grad=('ceig', '#F7D98B', '#C08A1E'))
TL = [('1', 'Version 1.1 — Revalidation Submitted', 'Under review · Date from case record', 'Updated learning content and assessments submitted for review.', 'cb'),
      ('2', 'Version 1.0 — Gold Validation Approved', '12 Sep 2026', 'Course approved for publication with CEI score 87.', 'ok')]
CASES = [('VAL-00928', 'v1.0', 'Approved', 'green'), ('Assigned case ID', 'v1.1', 'In Review', 'blue')]
P('h-a', head('Validation History', 'Validation History', 'Review your course’s validation status, decisions and approved learning versions.') +
  wk(strip('Live Version 1.0 · Technology / Data &amp; Analytics') +
     '''<section class="ds-card lv2 ob-in2"><div class="lv2-l">%s<span class="gb lg2">%s<span>Gold Validated</span></span></div>
<div class="lv2-r"><span class="rx-k">Current Live Validation</span><b class="lv2-t">Course Excellence Index</b>%s
<div class="lv2-n">%s<span><b>CEI is a distinct metric from validation tier</b>The Course Excellence Index reflects the approved quality evaluation. Tier is determined by Credalio’s rubric and tier policy — a high CEI does not automatically mean Gold.</span></div>
<div class="lv2-a"><a class="ds-ghost sm" href="MGT-007A.dc.html">View Validation Details</a><a class="ds-link sm" href="STU-PRV.dc.html">View Validated Version%s</a></div></div></section>
<section class="ds-card rv2 ob-in3"><div class="rv2-h"><div><span class="rx-k">Current Revalidation</span><b>A newer course version is being reviewed.</b></div>%s</div>
<div class="tk2-l"><span class="tk2-r live"><i class="lv-d"></i><b>v1.0</b><em>Live version</em></span><span class="tk2-line"><i></i></span><span class="tk2-r rv"><span class="tk2-dot"></span><b>v1.1</b><em>Proposed version</em></span></div>
<p class="rv2-n">%s<span>Your published version 1.0 remains live while the proposed update is reviewed. No changes have been applied to the marketplace course.</span></p><a class="ds-link sm" href="STU-055.dc.html">View Revalidation Case%s</a></section>
<section class="ds-card fc ob-in4"><div class="fc-h"><div><h2>Validation Timeline</h2></div>%s</div><ol class="vtl">%s</ol></section>''' % (
         CEI, ic('badge', 12, 2.2), facts([('Validated Version', 'v1.0'), ('Validation Date', '12 Sep 2026'), ('Validation Case', 'VAL-00928')]), INFO, ic('arrowr', 13, 2.2),
         tag('Under Review', 'blue'), ic('valid', 15, 2), ic('arrowr', 13, 2.2), tag('2 Records', 'line'),
         ''.join('<li class="%s" style="--i: %d"><span class="vtl-n">%s</span><div><b>%s</b><em>%s</em><p>%s</p></div></li>' % (k, i, n, t, d, p) for i, (n, t, d, p, k) in enumerate(TL))),
     '''<section class="ds-card rx ch3 ob-in3"><div class="vh2-h"><span class="rx-k">Validation Case History</span><a class="ds-link sm" href="MGT-007B.dc.html">View All</a></div><div class="ch3-r ch3-hd"><span>Case</span><span>Version</span><span>Status</span></div>%s</section>
<section class="ds-card rx ca ob-in4"><span class="ca-i">%s</span><b>Current Validation Actions</b><p>There are no outstanding actions for the currently published version. Any new findings for version 1.1 will appear in its linked validation case.</p><a class="ds-ghost sm" href="MGT-007C.dc.html">View Findings &amp; Decisions</a></section>''' % (
         ''.join('<div class="ch3-r"><b>%s</b><span>%s</span>%s</div>' % (c, v, tag(s, k)) for c, v, s, k in CASES), ic('check', 18, 2.4))))

AREAS7 = [('target', 'Learning Design & Pedagogy', 'Educational Validator'), ('cap', 'Subject Accuracy & Relevance', 'Subject Matter Validator'), ('quiz', 'Assessments & Evidence', 'Assessment Validator')]
P('h-rec', VH_H('Validation Record', 'Case VAL-00928 · Data Analysis with SQL · Version 1.0', ('Case Details', 'MGT-007.dc.html')) +
  wk('''<section class="ds-card vr3 ob-in2"><div class="vr3-h"><span class="vr3-s">%s</span><div><span class="ds-tag green">%s Approved</span><b>Final decision</b></div></div>%s</section>
<section class="ds-card fc ob-in3"><div class="fc-h"><div><h2>Validation Areas</h2></div></div><div class="va3">%s</div></section>
<section class="ds-card fc fds ob-in4"><span class="fds-q" aria-hidden="true">“</span><div class="fc-h"><div><h2>Final Decision Summary</h2></div></div><p>The course demonstrates clear learning design, accurate SQL instruction aligned to stated outcomes, and assessments that sufficiently evidence claimed skills. Approved for Gold validation at full course scope.</p><a class="ds-ghost sm" href="#">%s<span>Download Validation Summary</span></a></section>''' % (
      ic('valid', 26, 2), ck(10), facts([('Validation type', 'Initial Validation'), ('Final decision', 'Approved'), ('Validation tier', '<span class="gb sm">%s<span>Gold</span></span>' % ic('badge', 11, 2.2)), ('CEI score', '87 / 100'), ('Decision date', '12 Sep 2026')], 'five'),
      ''.join('<div class="va3-c" style="--i: %d"><span class="va3-i">%s</span><b>%s</b><em>%s</em>%s</div>' % (i, ic(icn, 18, 2), t, r, tag('%s Reviewed' % ck(10), 'green')) for i, (icn, t, r) in enumerate(AREAS7)),
      ic('download', 15, 2)),
     '''<section class="ds-card rx ceis ob-in3"><span class="rx-k">CEI score</span>%s</section><section class="ds-card rx imm ob-in4"><span class="imm-i">%s</span><p>Validator identities, private deliberations and internal risk signals are not shown here — only the official, approved creator-facing decision.</p></section>''' % (CEI, ic('lock', 18, 2))))

CH7 = [('VAL-00928', 'v1.0', 'Initial', 'Approved — Gold', 'green', '12 Sep 2026'), ('Assigned case ID', 'v1.1', 'Revalidation', 'Under Review', 'blue', '—')]
P('h-cases', VH_H('Validation Case History', 'Search and filter the validation records associated with this course.', ('Case History', 'MGT-007.dc.html')) +
  '''<section class="ds-card ct ob-in2"><div class="dr-t">%s%s</div><div class="ct-r ct-hd"><span>Case ID</span><span>Version</span><span>Validation Type</span><span>Decision / Status</span><span>Date</span></div>%s</section>%s''' % (
      sel_('All Statuses'), sel_('All Types'),
      ''.join('<a class="ct-r" href="MGT-007A.dc.html" style="--i: %d"><b>%s</b><span class="ct-v">%s</span><span>%s</span>%s<span class="ct-d">%s</span></a>' % (i, c, v, t, tag(s, k), d) for i, (c, v, t, s, k, d) in enumerate(CH7)),
      note('Interactive example with fictional case history. Production supports multiple revalidation cycles, appeals and rejected submissions, each with its own linked case ID.')))

FIND7 = [('Assessment Alignment', 'Version 1.0 · Assessment Validation', 'An assessment required clearer alignment between its questions and the stated learning outcomes.',
          'Creator submitted revised assessment mapping. The correction was accepted during validation.'),
         ('Content Clarification', 'Version 1.0 · Subject Matter Validation', 'A lesson explanation required additional clarification to support factual accuracy.', '')]
P('h-find', VH_H('Findings &amp; Decisions', 'Review validation feedback and the status of required corrections.', ('Findings & Decisions', 'MGT-007.dc.html')) +
  '''<div class="fv3"><div class="fs3 ob-in2"><span class="fs3-z"><b>0</b><em>Open — Live v1.0</em></span><span class="fs3-h"><b>2</b><em>Historical Findings</em></span><p class="fs3-n">%s<span>Illustrative findings, not actual validator decisions. Open findings route through the active Validation Centre workflow, never editing a historical approved record.</span></p></div><div class="fd3g">%s</div></div>''' % (ic('lock', 15, 2), ''.join(
      '<article class="ds-card fd3 ob-in3"><header><span class="fd3-i">%s</span><div><b>%s</b><em>%s</em></div>%s</header><p>%s</p>%s%s</article>' % (
          ck(14), t, m, tag('%s Resolved' % ck(10), 'green'), d, ('<div class="fd3-r"><span class="rx-k">Resolution</span><p>%s</p></div>' % r) if r else '', '<a class="ds-link sm" href="#">View Finding Details%s</a>' % ic('arrowr', 13, 2.2) if r else '') for t, m, d, r in FIND7)))

P('h-ver', VH_H('Validated Course Versions', 'Which validation decisions apply to which course versions.', ('Version Relationship', 'MGT-007.dc.html')) +
  '''<div class="vp ob-in2"><article class="ds-card vpc live"><header><span class="vd-v">v1.0</span><div><b>Version 1.0</b></div><span class="ds-tag green"><i class="lv-d"></i>Live</span></header>%s</article>
<span class="vp-x" aria-hidden="true"><span class="vp-l"></span><span class="vp-b">%s</span></span>
<article class="ds-card vpc rv"><header><span class="vd-v dr">v1.1</span><div><b>Version 1.1</b></div>%s</header>%s</article></div>
<section class="ds-card cr3 ob-in3"><span class="cr3-i">%s</span><div><span class="rx-k">Core rule</span><p>The validation decision belongs to a specific immutable version or approved scope. If v1.1 is rejected, v1.0 does not automatically lose its valid approval — though a serious problem also present in v1.0 can open a separate compliance review against the live version.</p></div></section>''' % (
      facts([('Validation', '<span class="gb sm">%s<span>Gold · CEI 87</span></span>' % ic('badge', 11, 2.2)), ('Case', 'VAL-00928'), ('Approval status', 'Approved')], 'col'), ic('lock', 14, 2.2),
      tag('Under Revalidation', 'blue'), facts([('Validation outcome', 'Pending'), ('Marketplace status', 'Not Live'), ('Learner assignments', 'None')], 'col'), ic('layers', 20, 2)))

VBACK = '<a class="ds-ghost" href="MGT-007.dc.html">Back to Validation History</a>'
P('h-chg', outcome('am', 'warn', 'Required Action', 'Changes Requested', 'Validators have requested corrections to your submitted course update.',
                   '<section class="ko-card">%s</section>' % facts([('Course', 'Data Analysis with SQL'), ('Submitted update', 'v1.1'), ('Live version', 'v1.0')]), VBACK + btn('View Findings', 'MGT-005-CHANGES.dc.html')))
P('h-rev', outcome('am', 'layers', 'Required Action', 'Revalidation Required', 'Changes to your course require review before the updated version can be published.',
                   '<section class="ko-card">%s</section>' % facts([('Course', 'Data Analysis with SQL'), ('Proposed version', 'v1.1'), ('Live version', 'v1.0')]), VBACK + btn('Review Update', 'MGT-005-READY.dc.html')))

# ======================================================================= MGT-008 Archive & Removal
AR_H = lambda h1, sub, ce, back=('Back to Archive & Removal', 'MGT-008.dc.html'): head('Archive & Removal', h1, sub, back=back, crumb_extra=ce)
PROTREC = '''<section class="ds-card rx pr2 ob-in3"><span class="pr2-i">%s</span><b>Protected Learner Records</b><p>Archiving does not delete enrollments, progress, lifetime purchases, completed assessments, verified credentials or required validation records.</p></section>''' % ic('valid', 20, 2)
P('a-a', head('Archive & Removal', 'Archive &amp; Removal', 'Retire a course from active management or request a review for permanent removal.') +
  wk(strip('Live v1.0 · %s1,800 DLP · %s420 Credits' % (coin(), credit())) +
     '''<div class="arw ob-in2"><article class="ds-card arc"><span class="arc-i">%s</span><b>Archive Course</b><p>Move this course out of your active creations while preserving required course records and existing learner access.</p>
<div class="arc-s"><div><em>Publication status</em>%s</div><div><em>Archive eligibility</em>%s</div></div><p class="arc-n">%s<span>This course must be unpublished before it can be archived.</span></p><a class="ds-ghost sm" href="MGT-003A.dc.html">Unpublish Course First</a></article>
<article class="ds-card arc rm"><span class="arc-i">%s</span><b>Request Course Removal</b><p>For exceptional situations where you need Credalio to review the removal of eligible course content or records.</p>
<div class="arc-w"><b>What removal does not guarantee</b><p>Existing learner entitlements, financial records, verified achievements and required validation evidence may need to remain available.</p></div><a class="ds-ghost sm dz-a" href="MGT-008F.dc.html">Request Removal Review</a></article></div>''' % (
         ic('layers', 20, 2), tag('Published', 'green'), tag('Unpublish First', 'amber'), ic('lock', 13, 2.2), ic('trash', 20, 2)),
     PROTREC))

DEPS = ['Active learning programs', 'Career Path dependencies', 'Open validation cases', 'Organization commitments']
CHG = ['The course moves from Active Creations to Archived Courses.', 'New enrollments and purchases remain unavailable.', 'The archived course is locked against normal content editing.', 'Eligible existing learners retain access under their entitlements.']
IMP8 = [('248', 'Total enrolled', 'all'), ('42', 'Lifetime purchasers', 'bl'), ('86', 'Active DLP learners', 'cb'), ('120', 'Completed learners', 'ok')]
P('a-impact', AR_H('Before You Archive', 'Review what will happen to this course and the learners who already have access.', ('Review Impact', 'MGT-008.dc.html')) +
  steps(0, ['Review impact', 'Confirm', 'Archived']) +
  wk(strip('Version 1.0 · %s1,800 DLP · %s420 Credits' % (coin(), credit()), 'Unpublished', '') +
     '''<section class="ob-in2"><h2 class="sh">Learner Impact%s</h2><div class="st4b">%s</div></section>
<section class="ds-card fc ob-in3"><div class="fc-h"><div><h2>What Archiving Changes</h2></div></div><ol class="wac">%s</ol></section>''' % (
         tip('Illustrative figures; production must use actual enrollment and entitlement records.'),
         ''.join('<div class="sb %s" style="--i: %d"><b>%s</b><span>%s</span></div>' % (k, i, n, l) for i, (n, l, k) in enumerate(IMP8)),
         ''.join('<li style="--i: %d"><span>%d</span><p>%s</p></li>' % (i, i + 1, t) for i, t in enumerate(CHG))) +
     bar('<a class="ds-link" href="MGT-008.dc.html">Back</a>', btn('Continue', 'MGT-008B.dc.html')),
     '''<section class="ds-card rx dpc ob-in3"><span class="rx-k">Dependency Checks</span><ul>%s</ul><p class="rx-p">Actual eligibility is determined by the backend. Archiving must not break required learner delivery.</p></section>''' % ''.join(
         '<li style="--i: %d"><span class="dpc-s"></span><b>%s</b>%s</li>' % (i, d, tag('Check required', 'amber')) for i, d in enumerate(DEPS))))

AREASONS = ['I no longer offer this course', 'This course has been replaced by another course', 'The content is outdated', 'I’m reorganizing my course library', 'Other reason']
ADIFF = [('Current status', 'Unpublished', 'Archived'), ('New enrollment', '', 'Disabled'), ('Existing entitlements', '', 'Preserved')]
kc = W.new(False)
P('a-confirm', AR_H('Confirm Course Archive', 'Tell us why you’re archiving this course and review the resulting changes.', ('Confirmation', 'MGT-008.dc.html')) +
  steps(1, ['Review impact', 'Confirm', 'Archived']) +
  wk('''<section class="ds-card fc ob-in2"><div class="fc-h"><div><h2>Reason for archiving</h2></div></div><div class="rs3">%s</div></section>
<button type="button" class="dc-r ack {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}"><span class="dc-b">%s</span><span>I understand this course will be removed from active management and that existing learner rights and required records will remain protected.</span></button>''' % (
      ''.join(W.opt('<span class="o-t"><b>%s</b></span>' % r, i == 0, 'ar', 'sm') for i, r in enumerate(AREASONS)), kc, kc, kc, ck(12)) +
     bar('<a class="ds-link" href="MGT-008A.dc.html">Back</a>', '<span class="cf-g {{c%s}}">%s</span>' % (kc, btn('Confirm Archive', 'MGT-008C.dc.html'))),
     '''<section class="ds-card rx asm ob-in3"><span class="rx-k">Archive Summary</span><div class="asm-v"><span class="asm-a">%s<em>Unpublished</em></span><i></i><span class="asm-b">%s<em>Archived</em></span></div>%s</section>''' % (
         ic('eye', 18, 2), ic('layers', 18, 2), ''.join('<div class="asm-r"><span>%s</span>%s</div>' % (l, ('<s>%s</s>' % a if a else '') + '<b>%s</b>' % b) for l, a, b in ADIFF))))

P('a-done', outcome('gy', 'layers', 'Archived', 'Course Archived', 'Data Analysis with SQL has been moved to Archived Courses. Existing learner entitlements and required records remain protected.',
                    '<div class="ko4">%s</div>' % ''.join('<span class="%s"><em>%s</em><b>%s</b></span>' % (k, l, v) for l, v, k in [('Course status', 'Archived', ''), ('Public listing', 'Hidden', ''), ('New enrollment', 'Closed', ''), ('Existing access', 'Protected', 'ok')]),
                    '<a class="ds-ghost" href="#">View Archived Courses</a>' + btn('View Archived Course', 'MGT-008D.dc.html')))

RECS = [('course', 'Course Overview', 'MGT-DS-OV.dc.html'), ('users', 'Learner Access & Enrollment', 'MGT-006.dc.html'), ('valid', 'Validation History', 'MGT-007.dc.html'),
        ('layers', 'Version History', 'MGT-005-HISTORY.dc.html'), ('wallet', 'Pricing & Order History', 'MGT-004-I.dc.html')]
P('a-detail', crumbs([('My Creations', 'MGT-DS-CR.dc.html'), ('Archived Courses', '#'), ('Data Analysis with SQL', '')]) +
  '''<header class="pg-h ob-in"><div class="pg-hl"><a class="ds-back" href="MGT-008.dc.html">%s<span>Back to Archive &amp; Removal</span></a><h1 class="ds-h1">Data Analysis with SQL</h1></div></header>''' % ICON(I['back'], 15, 2) +
  '<div class="bn2 gy ob-in"><span class="bn2-i">%s</span><div><b>This course is archived and no longer available for new enrollments.</b></div></div>' % ic('layers', 18, 2.2) +
  wk('<section class="ds-card fc ob-in2">%s</section>' % facts([('Archived on', 'From archive record'), ('Last live version', 'v1.0'), ('Validation', 'Gold'), ('Marketplace', 'Hidden')], 'four') +
     '<section class="ob-in3"><h2 class="sh">Available Records</h2><div class="rcd">%s</div></section>' % ''.join(
         '<a class="rcd-c" href="%s" style="--i: %d"><span class="rcd-i">%s</span><b>%s</b>%s</a>' % (h, i, ic(icn, 18, 2), t, ic('arrowr', 14, 2.2)) for i, (icn, t, h) in enumerate(RECS)),
     '''<section class="ds-card rx rst ob-in3"><span class="rst-i">%s</span><b>Restore Course</b><p>Move this course back into your active management library. Restoration does not automatically republish the course.</p><a class="ds-ghost sm" href="MGT-008E.dc.html">Review Restoration</a></section>''' % ic('restore', 18, 2.1)))

RST = [('Course lifecycle', 'Archived', 'Active'), ('Publication', 'Unpublished', 'Unpublished'), ('Marketplace visibility', 'Hidden', 'Hidden'), ('Enrollment', 'Closed', 'Closed'),
       ('Course editing', 'Locked', 'Available, subject to permissions'), ('Existing entitlements', 'Preserved', 'Preserved')]
P('a-restore', head('Archive & Removal', 'Restore Archived Course', 'Restore this course to your active creations. It will remain unpublished until you complete the required publishing checks.', back=('Back to Archived Course', 'MGT-008D.dc.html'), crumb_extra=('Restore', 'MGT-008D.dc.html')) +
  wk('<section class="ds-card cmp ob-in2"><div class="cmp-r cmp-hd"><span>Setting</span><span>Before</span><span></span><span>After</span></div>%s</section>' % ''.join(
      '<div class="cmp-r%s"><span>%s</span><span class="cmp-o">%s</span><span class="cmp-a">%s</span><b class="cmp-n">%s</b></div>' % (' ch' if a != b else '', l, a, ic('arrowr', 14, 2.2) if a != b else '', b) for l, a, b in RST) +
     bar('<a class="ds-link" href="MGT-008D.dc.html">Back</a>', btn('Restore Course', 'MGT-001.dc.html')),
     '''<section class="ds-card rx rsv ob-in3" aria-hidden="true"><span class="rx-k">Archived → Active</span><div class="rsv-v"><span class="rsv-b a">%s</span><span class="rsv-p"><i></i><i></i><i></i></span><span class="rsv-b b">%s</span></div><div class="rsv-l"><span>Archived Courses</span><span>Active Creations</span></div></section>''' % (ic('layers', 22, 2), ic('course', 22, 2))))

SCOPE = ['Removal of specific course content or assets', 'Permanent deletion of eligible course records', 'Other removal request']
RREAS = ['Content ownership or licensing concern', 'Privacy or personal information concern', 'Duplicate or incorrectly created record', 'Legal or compliance concern', 'Other']
P('a-req', AR_H('Request Course Removal', 'Submit a request for Credalio to review the removal of eligible course content or records.', ('Removal Request', 'MGT-008.dc.html')) +
  wk('''<section class="ds-card fc ob-in2"><div class="fc-h"><div><h2>What would you like reviewed?</h2></div></div><div class="sc3">%s</div></section>
<section class="ds-card fc ob-in3"><div class="fc-h"><div><h2>Reason for request</h2></div></div><div class="rs3">%s</div></section>''' % (
      ''.join(W.opt('<span class="sc3-i">%s</span><span class="o-t"><b>%s</b></span>' % (ic(i, 18, 2), t), k == 0, 'scope', 'sc3-o') for k, (i, t) in enumerate(zip(['file', 'trash', 'more'], SCOPE))),
      ''.join(W.opt('<span class="o-t"><b>%s</b></span>' % r, i == 0, 'rr', 'sm') for i, r in enumerate(RREAS))) +
     bar('<a class="ds-link" href="MGT-008.dc.html">Back</a>', btn('Review Removal Request', 'MGT-008G.dc.html')),
     '''<section class="ds-card rx ii ob-in3"><span class="ii-i">%s</span><b>Important Information</b><p>Submitting this request does not immediately remove your course. Credalio will review the requested scope, learner entitlements, required retention and any relevant restrictions before deciding what can be removed.</p></section>''' % ic('warn', 18, 2.2)))

RTL = [('dn', 'Request submitted'), ('on', 'Eligibility and impact review'), ('', 'Decision and approved scope'), ('', 'Execution and audit confirmation')]
P('a-status', AR_H('Removal Request', '', ('Removal Request', 'MGT-008.dc.html')) +
  ('''<div class="rq3w"><section class="ds-card rq3 ob-in2"><div class="rq3-h"><span class="rq3-i">%s</span><div><span class="ds-tag blue"><i class="lv-d"></i>Under Review</span><em>Request ID generated by backend</em></div></div>%s</section>
<section class="ds-card fc ob-in3"><div class="fc-h"><div><h2>Request Timeline</h2></div></div><ol class="rtl">%s</ol>%s</section></div>''' % (
      ic('file', 22, 2), facts([('Course', 'Data Analysis with SQL'), ('Requested scope', 'Content Assets'), ('Course status', 'Unchanged')], 'three'),
      ''.join('<li class="%s" style="--i: %d"><span class="rtl-n">%s</span><b>%s</b></li>' % (k, i, ck(11) if k == 'dn' else i + 1, t) for i, (k, t) in enumerate(RTL)), note('A pending request does not authorize removal or change the course’s publication status automatically.', 'lock'))))

P('a-blocked', outcome('am', 'lock', 'Restricted', 'Action Requires Review', 'This course has active obligations or restrictions that must be resolved before the requested lifecycle action can proceed.',
          '<section class="ko-card"><span class="rx-k">Possible requirements</span><ul class="pr4">%s</ul>%s</section>' % (
              ''.join('<li>%s<span>%s</span></li>' % (ic(i, 16, 2), t) for i, t in [('users', 'Active learner or cohort commitments'), ('profile', 'Organization approval'), ('valid', 'Validation, legal or compliance restrictions')]),
              note('The exact reason must come from the backend. Not every possible blocker applies to every course.')),
          '<a class="ds-ghost" href="MGT-008.dc.html">Back to Archive &amp; Removal</a>' + btn('View Requirements', '#')))

# ======================================================================= MGT-009 Insights & Engagement
TABS9 = [('perf', 'Learning Performance', 'MGT-009A.dc.html'), ('asm', 'Assessment Analytics', 'MGT-009B.dc.html'), ('health', 'Content Health', 'MGT-009C.dc.html'),
         ('rev', 'Reviews & Feedback', 'MGT-009D.dc.html'), ('sup', 'Questions & Support', 'MGT-009E.dc.html'), ('disc', 'Discussion', 'MGT-009F.dc.html')]
def tabs9(cur):
    return '<nav class="utabs vtabs ob-in2" aria-label="Insights">%s</nav>' % ''.join(
        '<a href="%s" class="ut%s"%s>%s</a>' % (h, ' on' if k == cur else '', ' aria-current="page"' if k == cur else '', l) for k, l, h in TABS9)
def ih(cur, h1, sub, ce):
    return head('Insights & Engagement', h1, sub, back=('Back to Insights &amp; Engagement', 'MGT-009.dc.html'), crumb_extra=(ce, 'MGT-009.dc.html')) + tabs9(cur)
def kpis(items):
    return '<section class="ds-card kp ob-in2">%s</section>' % ''.join(
        '<div class="kp-c %s" style="--i: %d"><b>%s</b><span>%s</span>%s</div>' % (k, i, v, l, ('<em>%s</em>' % d) if d else '') for i, (v, l, d, k) in enumerate(items))
def bars(rows, cls='', thr=None, drop=None):
    h = ''
    for i, (l, v) in enumerate(rows):
        h += '<div class="hb%s" style="--i: %d"><span class="hb-l">%s</span><span class="hb-t"><i style="--w: %d%%"></i>%s</span><b>%d%%</b></div>' % (
            ' dr' if drop == i else '', i, l, v, ('<s style="left: %d%%"></s>' % thr) if thr else '', v)
    return '<div class="hbs %s">%s</div>' % (cls, h)

# ---------- hub
HUB9 = [('analytics', 'Learning Performance', 'See outcome performance, chapter completion and where learners drop off.', 'View Performance', 'MGT-009A.dc.html', 'bars'),
        ('quiz', 'Assessment Analytics', 'Review pass rates, question difficulty and assessment patterns.', 'View Assessments', 'MGT-009B.dc.html', 'dots'),
        ('valid', 'Content Health', 'Automated checks and what learner behaviour says about your content.', 'View Content Health', 'MGT-009C.dc.html', 'ring'),
        ('badge', 'Reviews & Feedback', 'Ratings, written reviews and structured feedback. Reply publicly.', 'View Reviews', 'MGT-009D.dc.html', 'stars'),
        ('support', 'Questions & Support', 'AI Coach escalations and tutor requests. Private to the learner.', 'View Support', 'MGT-009E.dc.html', 'chat'),
        ('disc', 'Discussion', 'Public Q&A between enrolled learners and your team.', 'View Discussion', 'MGT-009F.dc.html', 'thread')]
VIS9 = {'bars': '<span class="v9 bars"><i style="--h: 92%"></i><i style="--h: 84%"></i><i style="--h: 70%"></i><i style="--h: 52%"></i><i style="--h: 45%"></i></span>',
        'dots': '<span class="v9 dots">%s</span>' % ''.join('<i class="%s"></i>' % ('lo' if j == 13 else '') for j in range(18)),
        'ring': '<span class="v9 rg9">%s<b>96%%</b></span>' % ring(96, 64, 12, track='#E7F5EE', color='#0F6B45'),
        'stars': '<span class="v9 st9"><b>4.8</b><span class="lc-stars"><i></i><i></i><i></i><i></i><i class="h"></i></span></span>',
        'chat': '<span class="v9 ch9"><i class="a"></i><i class="b"></i><i class="a s"></i></span>',
        'thread': '<span class="v9 th9"><i></i><i></i><i></i></span>'}
P('i-hub', head('Insights & Engagement', 'Insights &amp; Engagement', 'Understand how learners are doing, what needs fixing, and how your course is received.') +
  '<div class="i9 ob-in2">%s</div>' % ''.join(
      '<a class="i9c" href="%s" style="--i: %d"><div class="i9c-v">%s</div><span class="mc-i">%s</span><b>%s</b><p>%s</p><span class="mc-a">%s%s</span></a>' % (
          h, i, VIS9[v], ic(icn, 20, 1.9), t, d, cta, ic('arrowr', 14, 2.2)) for i, (icn, t, d, cta, h, v) in enumerate(HUB9)))

# ---------- A Learning Performance
OUTS = [('LO1 · Write SELECT queries', 88), ('LO2 · Join relational tables', 81), ('LO3 · Analyse business data', 72), ('LO4 · Publish a dashboard', 54)]
CHS9 = [('1 · Introduction', 96), ('2 · SQL Foundations', 91), ('3 · Aggregation', 84), ('4 · Joining tables', 62), ('5 · Final Project', 55)]
LOWL = [('Lesson 7 · Joining tables (video)', 62), ('Lesson 9 · Subqueries', 71), ('Lesson 11 · Window functions', 74)]
P('i-perf', ih('perf', 'Learning Performance', 'How well learners are reaching each outcome, and where they drop off.', 'Learning Performance') +
  kpis([('48%', 'Completion rate', '', ''), ('9h 10m', 'Median time to complete', '', ''), ('72%', 'Outcomes demonstrated', 'LO4 is lowest', 'am'), ('Ch. 4', 'Biggest drop-off', '−22% vs Chapter 3', 'rd')]) +
  '''<div class="g9 ob-in3"><section class="ds-card fc"><div class="fc-h"><div><h2>Outcome performance</h2><p>Share of learners who have demonstrated each outcome</p></div></div>%s</section>
<section class="ds-card fc"><div class="fc-h"><div><h2>Completion by chapter</h2><p>Share of enrolled learners who finished each chapter</p></div></div>%s</section></div>
<section class="ds-card fc ob-in4"><div class="fc-h"><div><h2>Lessons with the lowest engagement</h2><p>Share of learners who start the lesson and finish it</p></div><div class="fc-a"><a class="ds-ghost sm" href="MGT-009C.dc.html">Open Content Health</a><a class="ds-link sm" href="MGT-009B.dc.html">View Assessment Analytics%s</a></div></div><div class="ll">%s</div></section>''' % (
      bars(OUTS, 'out'), bars(CHS9, 'fun', drop=3), ic('arrowr', 13, 2.2),
      ''.join('<div class="ll-c" style="--i: %d">%s<span><b>%s</b><em>finish rate</em></span><p>%s</p></div>' % (i, ring(v, 52, 12, track='#FFF1D6', color='#D99A1E'), '%d%%' % v, l) for i, (l, v) in enumerate(LOWL))))

# ---------- B Assessment Analytics
PASS = [('Knowledge Check 1', 97), ('Quiz 1', 89), ('Quiz 2', 81), ('Quiz 3', 64), ('Final Exam (pass ≥ 70%)', 83), ('Final Project', 86)]
QP = [('Q14', 'LO4', 'Which chart type best shows revenue share by region over time?', 31, 'Split between B and D: likely ambiguous wording', 'rd'),
      ('Q9', 'LO3', 'Which query returns each region’s top product by revenue?', 58, 'Hard, but answers spread normally', 'am'),
      ('Q3', 'LO2', 'What does an INNER JOIN return?', 87, 'Performing as expected', 'ok'),
      ('Q1', 'LO1', 'Which keyword removes duplicate rows?', 97, 'Possibly too easy: consider replacing', 'cb')]
P('i-asm', ih('asm', 'Assessment Analytics', 'Pass rates, question performance and difficulty patterns.', 'Assessment Analytics') +
  kpis([('78%', 'Final Exam average', '', ''), ('86%', 'Final Project pass rate', '', 'ok'), ('64%', 'Quiz 3 pass rate', 'Lowest of all assessments', 'am'), ('Q14', 'Hardest question', '31% correct', 'rd')]) +
  wk('''<section class="ds-card fc ob-in3"><div class="fc-h"><div><h2>Question performance · Quiz 3</h2><p>Sorted by lowest correct rate</p></div></div>
<div class="qp"><div class="qp-r qp-hd"><span>Question</span><span>Outcome</span><span>Question text</span><span>Correct</span><span>Pattern</span></div>%s</div></section>
<section class="ds-card q14 ob-in4"><span class="q14-i">%s</span><div><b>Q14 · 31%% correct</b><p>Split between B and D: likely ambiguous wording</p></div>%s</section>''' % (
      ''.join('<div class="qp-r %s" style="--i: %d"><b class="qp-q">%s</b><span class="qp-o">%s</span><span class="qp-t">%s</span><span class="qp-c"><i style="--w: %d%%"></i><b>%d%%</b></span><span class="qp-p">%s</span></div>' % (
          k, i, q, o, t, c, c, p) for i, (q, o, t, c, p, k) in enumerate(QP)), nova_av(), btn('Add Q14 fix to draft update', 'MGT-005.dc.html', 'sm2')),
     '<section class="ds-card rx ob-in3"><span class="rx-k">Pass rate by assessment</span>%s<span class="hb-k"><s></s>Pass mark 70%%</span></section>' % bars(PASS, 'pr9', thr=70)))

# ---------- C Content Health
CHK = [('ok', 'Broken links: none', ''), ('am', 'Outdated references: 1', 'PostgreSQL docs link points to v14. Update to v17.'), ('ok', 'Captions on all videos: 100%', ''), ('ok', 'Accessibility issues: none', '')]
NOVA9 = [('Lesson 7 has unusually high abandonment: 38% leave before the end.', 'Most leave around the 9-minute mark of the video, where the JOIN diagram appears.', False),
         ('Question 14 in Quiz 3 has a significantly higher failure rate: 69% get it wrong.', 'Learners pick option B almost as often as the correct answer, which suggests ambiguous wording.', True),
         ('Learners frequently ask about LEFT JOIN row counts: 18 questions this month.', 'A worked example in Lesson 4.2 would likely answer most of them.', True)]
P('i-health', ih('health', 'Content Health', 'Automated checks plus what learner behaviour says about your content.', 'Content Health') +
  wk('''<section class="ds-card ob-in2 nf"><div class="nf-h">%s<span><b>What Nova found in learner behaviour</b><em>Nova · Creator Copilot</em></span></div>%s</section>''' % (
      nova_av(), ''.join('<article class="nf-c" style="--i: %d"><span class="nf-s">%s</span><div><b>%s</b><p>%s</p></div>%s</article>' % (
          i, SPARK, t, d, tag('%s In draft update' % ck(10), 'green') if done else '<a class="ds-ghost xs" href="MGT-005.dc.html">Add fix to update</a>') for i, (t, d, done) in enumerate(NOVA9))),
     '''<section class="ds-card rx chr ob-in2"><span class="rx-k">Content Health</span><div class="chr-r">%s<span><b>96%%</b></span></div><p class="rx-p">Automated checks plus learner signals. Not a quality score.</p></section>
<section class="ds-card rx ac9 ob-in3"><span class="rx-k">Automated checks</span><ul>%s</ul></section>''' % (
         ring(96, 120, 10, track='#E7F5EE', color='#0F6B45'),
         ''.join('<li class="%s"><span class="ac9-s">%s</span><span><b>%s</b>%s</span></li>' % (k, ck(10) if k == 'ok' else ic('warn', 11, 2.4), t, ('<em>%s</em><a class="ds-link sm" href="MGT-005.dc.html">Fix in update</a>' % d) if d else '') for k, t, d in CHK))))

# ---------- D Reviews & Feedback
HIST9 = [(5, 74), (4, 18), (3, 5), (2, 2), (1, 1)]
SF = [('Clarity of explanations', 4.8), ('Practical relevance', 4.9), ('Pace', 4.2), ('Assessment fairness', 4.1)]
REVS = [('SK', 'Sarah K.', 5, '2 days ago', 'Best SQL course I’ve taken. The final project gave me something real to show in interviews.', 'h1'),
        ('TB', 'Tunde B.', 3, '5 days ago', 'Great content, but Chapter 4 moves too fast. The JOIN lessons need more examples.', 'h2'),
        ('GM', 'Grace M.', 4, '1 week ago', 'Clear explanations and the practice datasets were very helpful. Wish there were more of them.', 'h3')]
def stars(n):
    return '<span class="lc-stars" aria-label="%d out of 5">%s</span>' % (n, ''.join('<i%s></i>' % ('' if j < n else ' class="o"') for j in range(5)))
P('i-rev', ih('rev', 'Reviews &amp; Feedback', 'Ratings, written reviews and structured feedback collected at completion.', 'Reviews & Feedback') +
  wk('<div class="rvl2 ob-in3">%s</div>' % ''.join(
      '<article class="ds-card rvc" style="--i: %d"><header><span class="la2 %s">%s</span><div><b>%s</b>%s</div><em>%s</em></header><p>%s</p><div class="rvc-r"><input class="ds-in" placeholder="Reply publicly" aria-label="Reply publicly"><button type="button" class="ds-ghost sm">Reply</button></div></article>' % (
          i, h, ini, n, stars(s), w, t) for i, (ini, n, s, w, t, h) in enumerate(REVS)),
     '''<section class="ds-card rx rsm ob-in2"><div class="rsm-t"><b>4.8</b><span>%s<em>126 reviews · 248 learners</em></span></div><div class="rh">%s</div></section>
<section class="ds-card rx sf ob-in3"><span class="rx-k">Structured feedback</span><p class="rx-p">Average of learner ratings out of 5, asked at completion</p>%s</section>''' % (
         stars(5), ''.join('<div class="rh-r" style="--i: %d"><span>%d<i></i></span><span class="rh-b"><i style="--w: %d%%"></i></span><em>%d%%</em></div>' % (i, s, p, p) for i, (s, p) in enumerate(HIST9)),
         ''.join('<div class="sf-r" style="--i: %d"><span>%s</span><b>%s<em> / 5</em></b><span class="sf-b"><i style="--w: %d%%"></i></span></div>' % (i, l, v, int(v * 20)) for i, (l, v) in enumerate(SF)))))

# ---------- E Questions & Support
TICK = [('esc', 'AI → Tutor escalation', 'Open 2h', 'Why does my LEFT JOIN return more rows than the left table has?', 'Amara Okafor · Lesson 7 · Joining tables', 'AO', 'h1',
         'Explained join cardinality with an example. The learner was still stuck after two follow-ups, so it escalated.', 'reply', ''),
        ('tut', 'Tutor request', 'Open 5h', 'I think Question 14 has two correct answers. Can you check?', 'Tunde Bello · Quiz 3 · Question 14', 'TB', 'h2', '', 'reply', 'See Q14 data'),
        ('tut', 'Tutor request', 'Answered', 'Can I use PostgreSQL instead of MySQL for the project?', 'Zara Ibrahim · Final Project', 'ZI', 'h3', '', 'You: Yes. Any SQL dialect is fine as long as your queries run on the dataset.', ''),
        ('ai', 'Resolved by AI Coach', 'Resolved by AI', 'What’s the difference between WHERE and HAVING?', 'Daniel Mensah · Lesson 2.2', 'DM', 'h4', 'Answered with the lesson’s own example. The learner marked it helpful.', '', '')]
def ticket(i, t):
    kind, k, st, q, who, ini, h, ai, rep, extra = t
    stc = 'amber' if st.startswith('Open') else ('green' if 'AI' in st or st == 'Answered' else '')
    body = ('<div class="tk-ai"><span class="tk-ai-k">%s<span>AI Coach tried first:</span></span><p>%s</p></div>' % (SPARK, ai)) if ai else ''
    if rep == 'reply':
        body += '<div class="rvc-r"><input class="ds-in" placeholder="Write a reply" aria-label="Write a reply"><button type="button" class="ds-ghost sm">Reply</button>%s</div>' % (
            ('<a class="ds-link sm" href="MGT-009B.dc.html">%s%s</a>' % (extra, ic('arrowr', 13, 2.2))) if extra else '')
    elif rep:
        body += '<div class="tk-you">%s<p>%s</p></div>' % (av(ME, 'AO', 26), rep)
    return '<article class="ds-card tk %s" style="--i: %d"><header><span class="tk-k">%s</span>%s</header><b class="tk-q">“%s”</b><span class="tk-w"><span class="la2 %s sm">%s</span>%s</span>%s</article>' % (
        kind, i, k, tag(st, stc), q, h, ini, who, body)
P('i-sup', ih('sup', 'Learner Questions &amp; Support', 'AI Coach escalations and tutor requests. Private to the learner and your team.', 'Learner Questions & Support') +
  kpis([('2', 'Waiting for a tutor', 'Target: reply within 24 hours', 'am'), ('41', 'Resolved by AI Coach', 'This month', 'ok'), ('9', 'Escalated to tutor', 'This month', ''), ('4h', 'Median tutor response', '', 'cb')]) +
  '<div class="tks ob-in3">%s</div>%s' % (''.join(ticket(i, t) for i, t in enumerate(TICK)), note('Private support. Only the learner and your team see these. Public Q&amp;A lives in Course Discussion.', 'lock')))

# ---------- F Discussion
THR = [('Tips for the final project dataset', 'Pinned', 'blue', 'Alex (you)', '14', '3h ago', True, 'h1', 'AX'), ('Is anyone else getting NULLs after a LEFT JOIN?', 'Unanswered', 'amber', 'Amara O.', '0', '1h ago', False, 'h1', 'AO'),
       ('Share your Chapter 3 dashboards here', 'Active', 'green', 'Emeka O.', '22', 'Yesterday', False, 'h4', 'EO'), ('Study group for the final project', 'Active', 'green', 'Zara I.', '6', '2 days ago', False, 'h3', 'ZI'),
       ('Which chapter was hardest for you?', 'Unanswered', 'amber', 'Adaeze N.', '0', '4 days ago', False, 'h5', 'AN')]
P('i-disc', ih('disc', 'Course Discussion', 'Public Q&amp;A between enrolled learners and your team.', 'Course Discussion') +
  kpis([('23', 'Threads', '', ''), ('2', 'Unanswered', 'Nobody has replied yet', 'am'), ('187', 'Learner replies this month', '', 'cb')]) +
  '''<section class="ds-card th ob-in3"><div class="th-r th-hd"><span>Thread</span><span>Started by</span><span>Replies</span><span>Last activity</span><span></span></div>%s</section>%s''' % (
      ''.join('<div class="th-r%s" style="--i: %d"><span class="th-t"><b>%s</b>%s</span><span class="th-b"><span class="la2 %s sm">%s</span>%s</span><span class="th-n%s">%s<b>%s</b></span><span class="th-d">%s</span><span class="th-a"><button type="button" class="ds-link sm">%s</button><button type="button" class="ds-ghost xs">Reply</button></span></div>' % (
          ' pin' if pin else (' un' if s == 'Unanswered' else ''), i, t, tag(s, k), h, ini, by, ' z' if n == '0' else '', ic('chat', 13, 2), n, d, 'Unpin' if pin else 'Pin') for i, (t, s, k, by, n, d, pin, h, ini) in enumerate(THR)),
      note('Course Discussion is public to everyone enrolled. It’s separate from private questions and support.')))

# ======================================================================= CR-COURSE-CREDITS (+ ASK dialog)
kj, kl = W.new(True), W.new(False)
def sw(k, label):
    return '<button type="button" class="hp-sw {{c%s}}" role="switch" aria-checked="{{a%s}}" onClick="{{x%s}}" aria-label="%s"></button>' % (k, k, k, label)
def swl(on, label):
    return '<span class="hp-sw lk%s" role="switch" aria-checked="%s" aria-disabled="true" aria-label="%s"></span>' % (' on' if on else '', 'true' if on else 'false', label)
CREW = [('AM', 'h1', 'Alex Morgan', 'Lead Creator', 'blue', 'Course lead', swl(True, 'Alex Morgan always shown'), 'ok', 'Always shown', ''),
        ('JA', 'h4', 'John Adeyemi', 'Co-Creator', 'blue', 'Chapters 2–3', sw(kj, 'Show John Adeyemi'), 'ok', 'Shown by default', ''),
        ('JO', 'h3', 'Johnson Okafor', 'Contributor', 'line', 'Lesson 3.2 resources', swl(False, 'Johnson Okafor hidden'), 'gy', 'Hidden by default', 'ask'),
        ('MB', 'h2', 'Mercy Bello', 'Reviewer', 'line', 'Assessment review', swl(False, 'Mercy Bello hidden'), 'gy', 'Hidden by default', 'ask'),
        ('TA', 'h5', 'Tunde Ade', 'Pending invitation', 'amber', 'Not started', '<span class="cr9-na">—</span>', 'gy', 'Not shown until accepted', ''),
        ('LM', 'h2', 'Lena Moyo', 'Past member', '', 'Earlier version', sw(kl, 'Show Lena Moyo'), 'gy', 'Optional: “Contributed to earlier versions”', '')]
RULES = [('Default', 'Lead Creator and Co-Creators are shown. Contributors and reviewers are hidden.'), ('Order', 'Lead Creator first, then Co-Creators by contribution'),
         ('Names shown on', 'Course page, marketplace card and certificates'), ('Never shown', 'Revenue shares, agreements, pending invitations and applicants'),
         ('Contributors and reviewers', 'Shown only after the person agrees to be credited')]
def crew_row(i, m):
    ini, h, n, role, rk, contrib, swh, dk, st, ask = m
    return ('<div class="cr9-r%s" style="--i: %d"><span class="cr9-m"><span class="la2 %s">%s</span><b>%s</b></span><span class="cr9-ro">%s</span><span class="cr9-c">%s</span><span class="cr9-s">%s</span>'
            '<span class="cr9-st %s"><i></i><span>%s</span>%s</span></div>') % (
        (' pd' if role == 'Pending invitation' else '') + (' tm' if i < 4 else ''), i, h, ini, n, tag(role, rk), contrib, swh, dk, st,
        '<a class="ds-link sm" href="CREDITS-ASK.dc.html">Ask to credit</a>' if ask else '')
CREDITS = (head('Course Credits & Visibility', 'Course credits &amp; visibility', 'Choose who learners see on the course page. Lead Creator and Co-Creators are shown by default.',
                right='<a class="ds-ghost sm" href="LEARN-CREATORS-2.dc.html">%s<span>Preview as learner</span></a>' % ic('eye', 15, 2), crumb_extra=('Credits', 'MGT-001.dc.html')) +
  wk('''<section class="ds-card cr9 ob-in2"><div class="cr9-r cr9-hd"><span>Team member</span><span>Role</span><span>Contribution</span><span>Shown</span><span>Status on course page</span></div>%s</section>''' % ''.join(crew_row(i, m) for i, m in enumerate(CREW)) +
     bar('%s<span>Changes apply to the live course page straight away. They do not change anyone’s role, permissions or revenue share.</span>' % INFO,
         '<a class="ds-ghost" href="MGT-001.dc.html">Cancel</a>' + btn('Save changes', 'MGT-001.dc.html')),
     '''<a class="ds-card rx cpv ob-in2" href="LEARN-CREATORS-2.dc.html"><span class="rx-k">Course page</span><div class="cpv-h"><span class="cpv-k">%s<span>Gold Validated</span></span><b>Data Analysis with SQL</b>
<div class="cpv-by"><span class="cpv-avs"><span class="la2 h1">AM</span><span class="la2 h4 cpv-j {{c%s}}">JA</span><span class="la2 h2 cpv-j {{c%s}}">LM</span></span><span>Created by <b>Alex Morgan</b><span class="cpv-j {{c%s}}"> and <b>John Adeyemi</b></span></span></div>
<span class="cpv-l cpv-j {{c%s}}">Lena Moyo · Contributed to earlier versions</span></div><span class="cpv-c"><span class="cpv-n" aria-live="polite"></span><span>Learners see <b class="cpv-x"></b> of 4 team members</span></span></a>
<section class="ds-card rx cw9 ob-in3"><span class="rx-k">How credits work</span><dl>%s</dl></section>''' % (
         ic('badge', 11, 2.2), kj, kl, kj, kl, ''.join('<div><dt>%s</dt><dd>%s</dd></div>' % r for r in RULES))))
ASK = '''<a class="ov-scrim" href="CREDITS.dc.html" aria-label="Close"></a>
<div class="dl ak" role="dialog" aria-modal="true" aria-label="Ask Johnson Okafor to be credited"><header class="dl-h"><span class="ak-v" aria-hidden="true"><span class="la2 h1">AM</span><span class="la2 h4">JA</span><span class="la2 h3 ak-n">JO</span></span><a class="ds-x sm" href="CREDITS.dc.html" aria-label="Close">%s</a></header>
<div class="dl-b"><h2 class="ak-h">Ask Johnson Okafor to be credited</h2><p class="dl-p">He decides whether his name appears on the course page.</p>
<div class="ak-w"><span class="la2 h3">JO</span><span><b>Johnson Okafor</b><em>Lesson 3.2 resources</em></span>%s</div>
<label class="dl-l" for="ak-m">Message</label><textarea id="ak-m" class="ds-in ak-t" rows="3">Hi Johnson, would you like to be credited on the Data Analysis with SQL course page as a Contributor?</textarea>
<p class="dl-n">%s<span>He sees the request in Invitations. If he says yes, he is shown under “Meet the creators” as a Contributor. If he declines, nothing changes.</span></p></div>
<footer class="dl-f"><a class="ds-ghost" href="CREDITS.dc.html">Cancel</a>%s</footer></div>''' % (ic('x', 16, 2.2), tag('Contributor', 'line'), INFO, btn('Send request', 'CREDITS.dc.html'))
P('c-credits', CREDITS)
P('c-ask', CREDITS + ASK)

# ======================================================================= assembly + CSS
def body():
    blocks = ['<sc-if value="{{p_%s}}" hint-placeholder-val="{{ %s }}">\n%s\n</sc-if>' % (k.replace('-', '_'), 'true' if k == 'h-a' else 'false', b) for k, b in PAGES]
    return '''<div class="ds-root cr-root">
%s
<div style="min-width: 0; display: flex; flex-direction: column">
%s
<main class="ds-main mg-main {{tone}}">
%s
</main>
</div>
</div>''' % (cr_side('My Creations'), CR_TOP, '\n'.join(blocks))
TONE = {'h-chg': 'am', 'h-rev': 'am', 'a-done': 'gy', 'a-detail': 'gy', 'a-blocked': 'am', 'a-req': 'rd', 'i-health': 'ok'}
JS = W.js() + '''var PG = %s, TONE = %s;
class Component extends DCLogic {
  renderVals() {
    var pg = this.props.page || 'h-a', v = togVals(this), self = this;
    PG.forEach(function (k) { v['p_'.concat(k.replace('-', '_'))] = k === pg; });
    v.tone = 'tn-'.concat(TONE[pg] || 'cb');
    v.navCls = this.state.nav ? 'ds-open' : '';
    v.toggleNav = function () { self.setState({ nav: !self.state.nav }); };
    return v;
  }
}''' % (json.dumps([p[0] for p in PAGES]), json.dumps(TONE))

CSS = stu7.CSS + r'''.cr9{padding:6px 22px}
.cr9-r{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1.05fr) minmax(0,1.15fr) 60px minmax(0,1.6fr);align-items:center;gap:12px;padding:15px 0;border-top:1.5px solid #F0F2F8;font-size:13.5px;animation:obIn .45s ease both;animation-delay:calc(var(--i,0) * 70ms + 200ms)}
.cr9-hd{border-top:0;padding:12px 0;font-size:12.5px;font-weight:500;color:#8A93AD;animation:none}
.cr9-m{display:flex;align-items:center;gap:10px;min-width:0}
.cr9-m b{font-size:14.5px;font-weight:600}
.cr9-ro .ds-tag{height:24px;font-size:11.5px}
.cr9-c{color:#3A4566}
.cr9-st{display:grid;grid-template-columns:7px minmax(0,1fr);align-items:center;column-gap:9px;row-gap:2px;color:#3A4566;line-height:1.4}
.cr9-st > i{width:7px;height:7px;border-radius:50%;background:#AEB6CC}
.cr9-st .ds-link{grid-column:2;justify-self:start}
.cr9-st.ok > i{background:#0F6B45;box-shadow:0 0 0 3px #E7F5EE}
.cr9-st .ds-link{font-size:13px}
.cr9-r.pd .cr9-m,.cr9-r.pd .cr9-c{opacity:.6}
.cr9-na{color:#AEB6CC;padding-left:16px}
.hp-sw{position:relative;display:block;width:44px;height:26px;flex-shrink:0;border-radius:999px;border:0;background:#CBD3E6;cursor:pointer;transition:background .2s ease}
.hp-sw::after{content:'';position:absolute;top:3px;left:3px;width:20px;height:20px;border-radius:50%;background:#FFFFFF;box-shadow:0 1px 3px rgba(11,20,51,.2);transition:left .2s ease}
.hp-sw.on{background:#1652F0}
.hp-sw.on::after{left:21px}
.hp-sw.lk{cursor:default;opacity:.45}
.hp-sw.lk.on{opacity:.55}
.wk-a2 .sv-s{display:flex;align-items:center;gap:8px;font-size:12.5px;line-height:1.45;color:#5B6582}
.wk-a2 .sv-s svg{flex-shrink:0;width:15px;height:15px;color:#8A93AD}
.wk-a2 .sv-r{flex-shrink:0;display:flex;align-items:center;gap:10px}
.cpv{display:block;padding:14px;color:#0B1433;text-decoration:none;transition:transform .25s ease,box-shadow .25s ease}
.cpv:hover{transform:translateY(-2px);box-shadow:0 22px 40px -28px rgba(22,82,240,.6)}
.cpv .rx-k{margin:0 4px 10px 4px}
.cpv-h{position:relative;overflow:hidden;display:flex;flex-direction:column;align-items:flex-start;gap:8px;padding:16px;border-radius:16px;background:linear-gradient(160deg,#0B1433,#13296E 70%,#1A45C7);color:#FFFFFF}
.cpv-h::after{content:'';position:absolute;right:-60px;top:-70px;width:180px;height:180px;border-radius:50%;background:radial-gradient(circle,rgba(92,134,255,.45),rgba(92,134,255,0) 65%)}
.cpv-k{display:inline-flex;align-items:center;gap:4px;height:20px;padding:0 8px;border-radius:999px;background:linear-gradient(110deg,#F7D98B,#C9952C);color:#4A3000;font-size:10.5px;font-weight:600}
.cpv-h > b{font-size:16px;font-weight:600}
.cpv-by{position:relative;z-index:1;display:flex;align-items:center;gap:8px;font-size:12px;line-height:1.4;color:rgba(255,255,255,.8)}
.cpv-by b{color:#FFFFFF;font-weight:600}
.cpv-avs{display:inline-flex;flex-shrink:0}
.cpv-avs .la2{width:26px;height:26px;font-size:9.5px;margin-left:-7px;box-shadow:0 0 0 2px #13296E;transition:opacity .25s ease,transform .3s cubic-bezier(.3,1.4,.5,1)}
.cpv-avs .la2:first-child{margin-left:0}
.cpv-j:not(.on){display:none}
.cpv-avs .cpv-j.on{animation:cpvIn .4s cubic-bezier(.3,1.4,.5,1)}
@keyframes cpvIn{from{transform:scale(.3);opacity:0}}
.cpv-l{font-size:11.5px;color:rgba(255,255,255,.65)}
.wk:has(.cr9){counter-reset:seen}
.cr9-r.tm:has(.hp-sw.on){counter-increment:seen}
.cpv-x::before{content:counter(seen)}
.cpv-c{margin:12px 4px 0 4px;display:flex;align-items:center;gap:10px;font-size:13px;color:#3A4566}
.cpv-c b{font-weight:600;color:#0B1433}
.cpv-n{position:relative;width:34px;height:6px;flex-shrink:0;border-radius:6px;background:#EEF1F7;overflow:hidden}
.cpv-n::after{content:'';position:absolute;left:0;top:0;bottom:0;width:50%;border-radius:6px;background:linear-gradient(90deg,#5C86FF,#1652F0);transition:width .35s ease}
.wk:has(.cr9-r.tm .hp-sw:not(.lk):not(.on)) .cpv-n::after{width:25%}
.cw9 dl{margin:0}
.cw9 dl div{display:flex;flex-direction:column;gap:2px;padding:9px 0;border-top:1.5px solid #F0F2F8}
.cw9 dl div:first-child{border-top:0;padding-top:0}
.cw9 dt{font-size:12px;font-weight:500;color:#8A93AD}
.cw9 dd{margin:0;font-size:13px;line-height:1.5;color:#0B1433}
.ak{width:520px}
.ak-v{display:inline-flex}
.ak-v .la2{width:40px;height:40px;margin-left:-10px;box-shadow:0 0 0 3px #FFFFFF}
.ak-v .la2:first-child{margin-left:0}
.ak-n{position:relative;outline:2px dashed #1652F0;outline-offset:3px;animation:akP 2.4s ease-in-out infinite}
@keyframes akP{50%{outline-offset:6px;outline-color:rgba(22,82,240,.35)}}
.ak-h{margin:0;text-align:center;font-size:21px;line-height:1.3;font-weight:600;letter-spacing:-0.015em}
.ak-w{display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:16px;background:#F7F9FD}
.ak-w > span:nth-child(2){flex:1;display:flex;flex-direction:column;gap:1px}
.ak-w b{font-size:14.5px;font-weight:600}
.ak-w em{font-style:normal;font-size:12.5px;color:#5B6582}
.ak-t{height:auto;min-height:96px;padding:12px 14px;border-radius:14px;font-family:inherit;font-size:14.5px;line-height:1.55;resize:vertical}
.ak .dl-n{display:flex;gap:8px}
.utabs{margin-top:20px;display:flex;gap:26px;border-bottom:1.5px solid #E6EAF3;overflow-x:auto;scrollbar-width:none}
.utabs::-webkit-scrollbar{display:none}
.ut{flex-shrink:0;display:inline-flex;align-items:center;gap:8px;height:46px;margin-bottom:-1.5px;border-bottom:2.5px solid transparent;color:#5B6582;font-size:14.5px;font-weight:500;text-decoration:none;white-space:nowrap}
.ut:hover{color:#0B1433}
.ut.on{color:#0B1433;font-weight:600;border-bottom-color:#1652F0}
.utabs + .wk,.utabs + .kp{margin-top:20px}
.ko-v.gy{--k:#5B6582;--kb:#EEF1F7}
.ko.gy .ko-pill{background:#EEF1F7;color:#3A4566}
.nt{margin:14px 0 0 0;display:flex;align-items:flex-start;gap:8px;font-size:12.5px;line-height:1.5;color:#8A93AD}
.nt svg{flex-shrink:0;margin-top:2px;width:14px;height:14px}
.lc-stars{display:inline-flex;gap:2px}
.lc-stars i{width:13px;height:13px;background:#F4C66A;clip-path:polygon(50% 0,61% 35%,98% 35%,68% 57%,79% 91%,50% 70%,21% 91%,32% 57%,2% 35%,39% 35%)}
.lc-stars i.h{background:linear-gradient(90deg,#F4C66A 80%,#E6EAF3 80%)}
.lc-stars i.o{background:#E6EAF3}
.dc-r{width:100%;display:flex;align-items:flex-start;gap:12px;padding:13px 14px;border-radius:14px;border:1.5px solid #E6EAF3;background:#FFFFFF;font-family:inherit;font-size:14px;line-height:1.5;color:#0B1433;text-align:left;cursor:pointer}
.dc-b{width:20px;height:20px;flex-shrink:0;margin-top:1px;box-sizing:border-box;border-radius:6px;border:1.5px solid #CBD3E6;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.dc-b svg{opacity:0;transform:scale(.6);transition:opacity .2s ease,transform .2s ease}
.dc-r.on{border-color:#1652F0;background:#F5F8FF}.dc-r.on .dc-b{border-color:#1652F0;background:#1652F0}.dc-r.on .dc-b svg{opacity:1;transform:none}
.cf-g{display:flex}
.cf-g .ds-btn{transition:opacity .25s ease,filter .25s ease}
.cf-g:not(.on) .ds-btn{opacity:.45;filter:saturate(.4);pointer-events:none}
.cf-g.on .ds-btn{animation:cfIn .5s cubic-bezier(.3,1.4,.5,1)}
@keyframes cfIn{50%{transform:scale(1.04)}}
.fx3{margin:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
.fx3.five{grid-template-columns:repeat(5,minmax(0,1fr))}
.fx3.four{grid-template-columns:repeat(4,minmax(0,1fr))}
.fx3.col{grid-template-columns:minmax(0,1fr)}
.fx3 div{display:flex;flex-direction:column;gap:3px;padding:12px 14px;border-radius:14px;background:#F7F9FD}
.fx3 dt{font-size:12px;color:#8A93AD}
.fx3 dd{margin:0;display:flex;align-items:center;font-size:14.5px;font-weight:600}
.cei{position:relative;width:132px;height:132px}
.cei-v{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}
.cei-v b{font-size:38px;font-weight:600;letter-spacing:-0.03em;line-height:1;color:#5A3B00}
.cei-v em{font-style:normal;font-size:12.5px;color:#8A5A00}
.lv2{display:grid;grid-template-columns:180px minmax(0,1fr);gap:24px;padding:22px 24px;background:linear-gradient(150deg,#FFFAEB,#FFFFFF 55%);border-color:#F0DDAE}
.lv2-l{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px}
.gb.lg2{height:30px;font-size:13px;padding:0 12px;animation:gbS 4s ease-in-out infinite;background-size:200% 100%;background-image:linear-gradient(110deg,#F7D98B 20%,#FFF1C9 40%,#C9952C 60%)}
@keyframes gbS{0%,100%{background-position:100% 0}50%{background-position:0 0}}
.lv2-r{display:flex;flex-direction:column;gap:12px;min-width:0}
.lv2-r .rx-k{margin:0}
.lv2-t{font-size:20px;font-weight:600;letter-spacing:-0.01em}
.lv2-r .fx3 div{background:#FFFFFF;border:1.5px solid #F4E9C8}
.lv2-n{display:flex;gap:10px;padding:12px 14px;border-radius:14px;background:#FFFFFF;border:1.5px dashed #E8D6A6;font-size:13px;line-height:1.5;color:#3A4566}
.lv2-n svg{flex-shrink:0;margin-top:2px;color:#B07A12}
.lv2-n b{display:block;color:#0B1433;font-weight:600}
.lv2-a{display:flex;align-items:center;gap:16px}
.lv2-a .ds-link,.rv2 > .ds-link,.fd3 .ds-link{display:inline-flex;align-items:center;gap:5px}
.rv2{padding:20px 22px;display:flex;flex-direction:column;gap:14px}
.rv2-h{display:flex;align-items:flex-start;justify-content:space-between;gap:12px}
.rv2-h .rx-k{margin-bottom:4px}
.rv2-h b{display:block;font-size:16px;font-weight:600}
.rv2-n{margin:0;display:flex;gap:8px;align-items:center;font-size:13px;color:#2C5240;padding:10px 12px;border-radius:12px;background:#F2FAF5}
.rv2-n svg{flex-shrink:0;color:#0F6B45}
.vtl{list-style:none;margin:0;padding:0;position:relative}
.vtl li:not(:last-child)::before{content:'';position:absolute;left:15px;top:42px;bottom:-10px;width:2px;background:linear-gradient(180deg,#1652F0,#0F6B45)}
.vtl li{position:relative;display:flex;gap:14px;padding:10px 0;animation:obIn .5s ease both;animation-delay:calc(var(--i) * 120ms + 200ms)}
.vtl-n{position:relative;z-index:1;width:32px;height:32px;flex-shrink:0;border-radius:50%;color:#FFFFFF;font-size:13px;font-weight:600;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 5px #FFFFFF}
.vtl .cb .vtl-n{background:#1652F0;animation:rvP 1.8s ease-out infinite}
.vtl .ok .vtl-n{background:#0F6B45}
.vtl li > div{display:flex;flex-direction:column;gap:2px;padding-top:4px}
.vtl b{font-size:15px;font-weight:600}
.vtl em{font-style:normal;font-size:12.5px;color:#8A93AD}
.vtl p{margin:4px 0 0 0;font-size:13.5px;line-height:1.5;color:#3A4566}
.ch3-r{display:grid;grid-template-columns:minmax(0,1.3fr) 44px auto;align-items:center;gap:8px;padding:10px 0;border-top:1.5px solid #F0F2F8;font-size:13px}
.ch3-hd{border-top:0;padding-top:0;font-size:11.5px;color:#8A93AD}
.ch3-r b{font-weight:600}
.ch3-r .ds-tag{height:22px;font-size:11px;justify-self:end}
.ca{display:flex;flex-direction:column;align-items:flex-start;gap:8px}
.ca-i{width:38px;height:38px;border-radius:12px;background:#E7F5EE;color:#0F6B45;display:flex;align-items:center;justify-content:center}
.ca b{font-size:15px;font-weight:600}
.ca p{margin:0;font-size:13px;line-height:1.55;color:#3A4566}
.vr3{padding:20px 22px}
.vr3-h{display:flex;align-items:center;gap:14px;margin-bottom:16px}
.vr3-h > div{display:flex;flex-direction:column;align-items:flex-start;gap:6px}
.vr3-h b{font-size:18px;font-weight:600}
.vr3-s{width:54px;height:54px;border-radius:17px;background:#0F6B45;color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 0 rgba(15,107,69,.35);animation:prP 3s ease-out infinite}
.va3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.va3-c{display:flex;flex-direction:column;align-items:flex-start;gap:4px;padding:16px;border-radius:18px;background:#F7F9FD;animation:obIn .5s ease both;animation-delay:calc(var(--i) * 100ms + 200ms)}
.va3-i{width:38px;height:38px;margin-bottom:6px;border-radius:12px;background:#FFFFFF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.va3-c b{font-size:14.5px;font-weight:600}
.va3-c em{font-style:normal;font-size:12.5px;color:#5B6582;margin-bottom:6px}
.fds{position:relative;overflow:hidden}
.fds-q{position:absolute;right:20px;top:-10px;font-size:120px;line-height:1;font-weight:600;color:#EAF0FF}
.fds p{position:relative;margin:0 0 16px 0;font-size:15.5px;line-height:1.65;color:#0B1433}
.ceis .cei{margin:4px auto 0 auto}
.vr3 .fx3.five{grid-template-columns:repeat(4,minmax(0,1fr))}
.vr3 .fx3 > div:nth-child(4){display:none}
.ct{margin-top:24px;padding:16px 20px 8px 20px}
.ct .dr-t{margin:0 0 6px 0}
.ct .dr-f{width:170px}
.ct-r{display:grid;grid-template-columns:minmax(0,1.2fr) 90px minmax(0,1fr) minmax(0,1fr) 120px;align-items:center;gap:12px;padding:14px 0;border-top:1.5px solid #F0F2F8;font-size:14px;color:#0B1433;text-decoration:none;animation:obIn .45s ease both;animation-delay:calc(var(--i,0) * 80ms + 200ms)}
a.ct-r{margin:0 -10px;padding:14px 10px;border-radius:14px}
a.ct-r:hover{background:#F7F9FD}
.ct-hd{font-size:12.5px;font-weight:500;color:#8A93AD;padding:10px 0;animation:none}
.ct-r .ds-tag{justify-self:start}
.ct-v{font-weight:600}
.ct-d{color:#5B6582}
.fv3{margin-top:24px;display:flex;flex-direction:column;gap:16px}
.fs3{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr) minmax(0,2fr);gap:10px}
.fs3-n{margin:0;display:flex;align-items:center;gap:12px;padding:14px 18px;border-radius:18px;background:#FFFFFF;border:1.5px solid #E6EAF3;font-size:13px;line-height:1.5;color:#5B6582}
.fs3-n svg{flex-shrink:0;width:30px;height:30px;padding:8px;box-sizing:border-box;border-radius:10px;background:#0B1433;color:#FFFFFF}
.fd3g{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;align-items:stretch}
.fs3 > span{display:flex;align-items:baseline;gap:10px;padding:16px 18px;border-radius:18px;background:#FFFFFF;border:1.5px solid #E6EAF3}
.fs3 b{font-size:30px;font-weight:600;letter-spacing:-0.03em}
.fs3 em{font-style:normal;font-size:13.5px;color:#5B6582}
.fs3-z{background:linear-gradient(150deg,#F2FAF5,#FFFFFF 70%) !important;border-color:#CFE8DB !important}
.fs3-z b{color:#0F6B45}
.fd3{padding:18px 20px;display:flex;flex-direction:column;gap:10px}
.fd3 header{display:flex;align-items:center;gap:12px}
.fd3 header > div{flex:1;display:flex;flex-direction:column;gap:2px}
.fd3 header b{font-size:15.5px;font-weight:600}
.fd3 header em{font-style:normal;font-size:12.5px;color:#8A93AD}
.fd3-i{width:34px;height:34px;flex-shrink:0;border-radius:50%;background:#E7F5EE;color:#0F6B45;display:flex;align-items:center;justify-content:center}
.fd3 > p{margin:0;font-size:14px;line-height:1.55;color:#3A4566}
.fd3-r{padding:12px 14px;border-radius:14px;background:#F2FAF5;border-left:3px solid #0F6B45}
.fd3-r .rx-k{margin:0 0 4px 0}
.fd3-r p{margin:0;font-size:13.5px;line-height:1.55;color:#2C5240}
.vp{margin-top:20px;display:grid;grid-template-columns:minmax(0,1fr) 90px minmax(0,1fr);align-items:stretch}
.vpc{display:flex;flex-direction:column;gap:14px;padding:20px}
.vpc header{display:flex;align-items:center;gap:12px}
.vpc header > div{flex:1}
.vpc header b{font-size:17px;font-weight:600}
.vpc.live{background:linear-gradient(160deg,#F2FAF5,#FFFFFF 60%);border-color:#CFE8DB}
.vpc.rv{background:linear-gradient(160deg,#F5F8FF,#FFFFFF 60%);border-color:#C9D7FA;border-style:dashed}
.vpc .fx3 div{flex-direction:row;justify-content:space-between;align-items:center;background:#FFFFFF;border:1.5px solid #EEF1F7}
.vp-x{position:relative;display:flex;align-items:center;justify-content:center}
.vp-l{position:absolute;left:0;right:0;top:50%;height:2px;background:repeating-linear-gradient(90deg,#CBD3E6 0 5px,transparent 5px 10px)}
.vp-b{position:relative;width:38px;height:38px;border-radius:50%;background:#0B1433;color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 6px #F7F9FD}
.cr3{margin-top:16px;display:flex;gap:16px;padding:18px 20px}
.cr3-i{width:44px;height:44px;flex-shrink:0;border-radius:14px;background:#EAF0FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.cr3 .rx-k{margin:0 0 6px 0}
.cr3 p{margin:0;font-size:14.5px;line-height:1.6;color:#3A4566}
.arw{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;align-items:stretch}
.arc{position:relative;overflow:hidden;display:flex;flex-direction:column;align-items:flex-start;gap:10px;padding:22px}
.arc b{font-size:17px;font-weight:600}
.arc > p{margin:0;font-size:13.5px;line-height:1.55;color:#3A4566}
.arc .ds-ghost{margin-top:auto}
.arc-i{width:46px;height:46px;border-radius:15px;background:#EEF1F7;color:#3A4566;display:flex;align-items:center;justify-content:center}
.arc.rm{border-color:#F5D3CE;background:linear-gradient(150deg,#FFF7F6,#FFFFFF 60%)}
.arc.rm .arc-i{background:#FDECEA;color:#B42318}
.arc-s{width:100%;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.arc-s > div{display:flex;flex-direction:column;align-items:flex-start;gap:6px;padding:12px;border-radius:14px;background:#F7F9FD}
.arc-s em{font-style:normal;font-size:12px;color:#8A93AD}
.arc-n{margin:0;display:flex;align-items:flex-start;gap:8px;font-size:13px;line-height:1.5;color:#8A5A00}
.arc-n svg{flex-shrink:0;margin-top:3px;color:#B76E00}
.arc-w{padding:12px 14px;border-radius:14px;background:#FFFFFF;border:1.5px solid #F5D3CE}
.arc-w b{font-size:13.5px}
.arc-w p{margin:4px 0 0 0;font-size:13px;line-height:1.5;color:#5B6582}
.wac{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.wac li{display:flex;gap:12px;padding:14px;border-radius:16px;background:#F7F9FD;animation:obIn .5s ease both;animation-delay:calc(var(--i) * 80ms + 200ms)}
.wac li > span{width:26px;height:26px;flex-shrink:0;border-radius:50%;background:#0B1433;color:#FFFFFF;font-size:12px;font-weight:600;display:flex;align-items:center;justify-content:center}
.wac p{margin:2px 0 0 0;font-size:13.5px;line-height:1.5;color:#3A4566}
.dpc ul{list-style:none;margin:0;padding:0}
.dpc li{display:flex;align-items:center;gap:10px;padding:10px 0;border-top:1.5px solid #F0F2F8;animation:obIn .5s ease both;animation-delay:calc(var(--i) * 90ms + 300ms)}
.dpc li:first-child{border-top:0;padding-top:0}
.dpc li b{flex:1;font-size:13.5px;font-weight:500}
.dpc .ds-tag{height:22px;font-size:11px}
.dpc-s{width:16px;height:16px;flex-shrink:0;box-sizing:border-box;border-radius:50%;border:2px solid #F4DDAA;border-top-color:#D99A1E;animation:rmSpin 1.2s linear infinite}
.asm-v{display:flex;align-items:center;gap:10px;margin-bottom:12px}
.asm-v > span{flex:1;display:flex;flex-direction:column;align-items:center;gap:6px;padding:12px;border-radius:14px;background:#F7F9FD}
.asm-v em{font-style:normal;font-size:12.5px;font-weight:600}
.asm-a{color:#8A93AD}.asm-b{background:#0B1433 !important;color:#FFFFFF}
.asm-v > i{width:22px;height:2px;background:repeating-linear-gradient(90deg,#9DB8F7 0 4px,transparent 4px 8px);background-size:16px 2px;animation:vrM 1s linear infinite}
.asm-r{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:9px 0;border-top:1.5px solid #F0F2F8;font-size:13px}
.asm-r > span{color:#5B6582}
.asm-r s{color:#8A93AD;margin-right:6px}
.asm-r b{font-weight:600}
.ko4{margin-top:22px;width:100%;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px}
.ko4 span{display:flex;flex-direction:column;gap:3px;padding:14px;border-radius:16px;background:#FFFFFF;border:1.5px solid #E6EAF3}
.ko4 em{font-style:normal;font-size:12px;color:#8A93AD}
.ko4 b{font-size:15px;font-weight:600}
.ko4 .ok b{color:#0F6B45}
.rcd{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:10px}
.rcd-c{grid-column:span 2}
.rcd-c:nth-child(n+4){grid-column:span 3}
.bn2:not(:has(p)){align-items:center}
.rcd-c{display:flex;align-items:center;gap:12px;padding:14px 16px;border-radius:16px;background:#FFFFFF;border:1.5px solid #E6EAF3;color:#0B1433;text-decoration:none;transition:transform .2s ease,border-color .2s ease;animation:obIn .5s ease both;animation-delay:calc(var(--i) * 60ms + 200ms)}
.rcd-c:hover{transform:translateY(-2px);border-color:#AFC1F5}
.rcd-c b{flex:1;font-size:14px;font-weight:600}
.rcd-c > svg{color:#AEB6CC}
.rcd-i{width:36px;height:36px;flex-shrink:0;border-radius:11px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.rst{display:flex;flex-direction:column;align-items:flex-start;gap:8px;background:linear-gradient(160deg,#F5F8FF,#FFFFFF 60%);border-color:#C9D7FA}
.rst-i{width:40px;height:40px;border-radius:13px;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 20px -10px rgba(22,82,240,.7)}
.rst b{font-size:15px;font-weight:600}
.rst p{margin:0;font-size:13px;line-height:1.55;color:#3A4566}
.rsv-v{display:flex;align-items:center;gap:8px}
.rsv-b{width:56px;height:56px;border-radius:17px;display:flex;align-items:center;justify-content:center}
.rsv-b.a{background:#EEF1F7;color:#8A93AD}.rsv-b.b{background:#1652F0;color:#FFFFFF;box-shadow:0 12px 24px -12px rgba(22,82,240,.8)}
.rsv-p{flex:1;display:flex;justify-content:center;gap:6px}
.rsv-p i{width:8px;height:8px;border-radius:50%;background:#1652F0;opacity:.25;animation:vtA 1.2s ease-in-out infinite}
.rsv-p i:nth-child(2){animation-delay:.2s}.rsv-p i:nth-child(3){animation-delay:.4s}
@keyframes vtA{50%{opacity:1;transform:scale(1.2)}}
.rsv-l{margin-top:8px;display:flex;justify-content:space-between;font-size:12px;color:#5B6582}
.sc3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.ds-opt.sc3-o{flex-direction:column;align-items:flex-start;gap:10px;padding:16px}
.ds-opt.sc3-o .ds-opt-ck{position:absolute;top:14px;right:14px}
.ds-opt.sc3-o .o-t b{font-size:14px;font-weight:600;line-height:1.4}
.sc3-i{width:38px;height:38px;border-radius:12px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.ds-opt.on .sc3-i{background:#FFFFFF}
.ii{display:flex;flex-direction:column;align-items:flex-start;gap:8px;background:#FFF8EA;border-color:#F4DDAA}
.ii-i{width:38px;height:38px;border-radius:12px;background:#B76E00;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.ii b{font-size:15px;font-weight:600}
.ii p{margin:0;font-size:13px;line-height:1.55;color:#6B4A00}
.rq3w{margin-top:24px;display:flex;flex-direction:column;gap:16px}
.rq3w .fc{margin:0}
.rq3w .nt{margin-top:22px;padding-top:14px;border-top:1.5px solid #F0F2F8}
.rq3{padding:20px 22px}
.rq3-h{display:flex;align-items:center;gap:14px;margin-bottom:16px}
.rq3-h > div{display:flex;flex-direction:column;align-items:flex-start;gap:6px}
.rq3-h em{font-style:normal;font-size:12.5px;color:#8A93AD}
.rq3-i{width:52px;height:52px;border-radius:16px;background:#EAF0FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.rtl{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));position:relative}
.rtl::before{content:'';position:absolute;left:12.5%;right:12.5%;top:15px;height:2px;background:#E6EAF3}
.rtl::after{content:'';position:absolute;left:12.5%;width:25%;top:15px;height:2px;background:linear-gradient(90deg,#0F6B45,#1652F0);transform-origin:left;animation:bdG 1s ease .3s both}
.rtl li{position:relative;z-index:1;display:flex;flex-direction:column;align-items:center;gap:8px;text-align:center}
.rtl-n{width:32px;height:32px;box-sizing:border-box;border-radius:50%;border:2px solid #D6DDEE;background:#FFFFFF;color:#8A93AD;font-size:13px;font-weight:600;display:flex;align-items:center;justify-content:center}
.rtl .dn .rtl-n{background:#0F6B45;border-color:#0F6B45;color:#FFFFFF}
.rtl .on .rtl-n{background:#1652F0;border-color:#1652F0;color:#FFFFFF;animation:rvP 1.8s ease-out infinite}
.rtl b{font-size:13px;font-weight:500;color:#3A4566;max-width:150px}
.rtl .on b{color:#0B1433;font-weight:600}
.pr4{list-style:none;margin:10px 0 0 0;padding:0;display:flex;flex-direction:column;gap:8px}
.pr4 li{display:flex;align-items:center;gap:10px;padding:12px 14px;border-radius:14px;background:#FFF8EA;font-size:14px;font-weight:500}
.pr4 svg{color:#B76E00;flex-shrink:0}
.i9{margin-top:22px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.i9c{position:relative;display:flex;flex-direction:column;gap:6px;padding:18px;border-radius:22px;background:#FFFFFF;border:1.5px solid #E6EAF3;color:#0B1433;text-decoration:none;overflow:hidden;transition:transform .25s ease,border-color .25s ease,box-shadow .25s ease;animation:obIn .5s ease both;animation-delay:calc(var(--i) * 70ms + 150ms)}
.i9c:hover{transform:translateY(-3px);border-color:#AFC1F5;box-shadow:0 22px 40px -28px rgba(22,82,240,.6)}
.i9c b{font-size:16px;font-weight:600}
.i9c p{flex:1;margin:0;font-size:13.5px;line-height:1.5;color:#5B6582}
.i9c .mc-i{margin:-30px 0 4px 0;position:relative;z-index:1;box-shadow:0 0 0 5px #FFFFFF}
.i9c:hover .mc-a svg{transform:translateX(3px)}
.i9c-v{height:96px;margin:-18px -18px 0 -18px;padding:16px 18px;box-sizing:border-box;background:linear-gradient(160deg,#F5F8FF,#FFFFFF);display:flex;align-items:flex-end;justify-content:flex-end}
.v9{display:flex}
.v9.bars{align-items:flex-end;gap:6px;height:60px}
.v9.bars i{width:16px;height:var(--h);border-radius:5px 5px 2px 2px;background:linear-gradient(180deg,#5C86FF,#1652F0);transform-origin:bottom;animation:mbUp .8s cubic-bezier(.2,.8,.2,1) both}
.v9.bars i:nth-child(4){background:linear-gradient(180deg,#F4C66A,#D99A1E)}
@keyframes mbUp{from{transform:scaleY(0)}}
.v9.dots{display:grid;grid-template-columns:repeat(6,10px);gap:5px}
.v9.dots i{width:10px;height:10px;border-radius:3px;background:#C9D7FA}
.v9.dots i:nth-child(odd){background:#1652F0}
.v9.dots i.lo{background:#D92D20;animation:clP 1.6s ease-in-out infinite}
@keyframes clP{50%{opacity:.5}}
.v9.rg9{position:relative;width:64px;height:64px}
.v9.rg9 b{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:600;color:#0F6B45}
.v9.st9{flex-direction:column;align-items:flex-end;gap:4px}
.v9.st9 b{font-size:28px;font-weight:600;line-height:1}
.v9.ch9{flex-direction:column;align-items:flex-end;gap:5px}
.v9.ch9 i{height:14px;border-radius:8px}
.v9.ch9 .a{width:70px;background:#EAF0FF}.v9.ch9 .b{width:90px;background:#1652F0}.v9.ch9 .s{width:46px}
.v9.th9{flex-direction:column;gap:5px}
.v9.th9 i{width:110px;height:10px;border-radius:5px;background:#EEF1F7}
.v9.th9 i:first-child{background:#C9D7FA;width:90px}
.kp{display:grid;grid-template-columns:repeat(auto-fit,minmax(0,1fr));grid-auto-flow:column;padding:6px}
.kp-c{display:flex;flex-direction:column;gap:2px;padding:14px 18px;animation:obIn .5s ease both;animation-delay:calc(var(--i) * 70ms + 150ms)}
.kp-c + .kp-c{border-left:1.5px solid #F0F2F8}
.kp-c b{font-size:28px;font-weight:600;letter-spacing:-0.03em}
.kp-c span{font-size:13px;font-weight:500;color:#3A4566}
.kp-c em{margin-top:4px;align-self:flex-start;font-style:normal;font-size:11.5px;font-weight:500;padding:2px 8px;border-radius:999px;background:#F1F3F8;color:#5B6582}
.kp-c.am b{color:#B76E00}.kp-c.am em{background:#FFF4E0;color:#8A5A00}
.kp-c.rd b{color:#B42318}.kp-c.rd em{background:#FDECEA;color:#B42318}
.kp-c.ok b{color:#0F6B45}.kp-c.ok em{background:#E7F5EE;color:#0F6B45}
.kp-c.cb b{color:#1652F0}.kp-c.cb em{background:#EAF0FF;color:#0E3BB8}
@media (min-width: 961px){.kp-c{display:grid;grid-template-columns:auto minmax(0,1fr);align-items:center;column-gap:10px;row-gap:2px}.kp-c b{grid-column:1;grid-row:1}.kp-c em{grid-column:2;grid-row:1;margin-top:0;justify-self:start}.kp-c span{grid-column:1 / -1;grid-row:2}}
.g9{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin-top:16px}
.g9 .fc{margin:0;display:flex;flex-direction:column}
.g9 .hbs{flex:1;justify-content:space-between}
.g9 + .fc{margin-top:16px}
.fc-a{display:flex;align-items:center;gap:14px;flex-shrink:0}
.fc-a .ds-link{display:inline-flex;align-items:center;gap:5px}
.hbs{display:flex;flex-direction:column;gap:12px}
.hb{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1.6fr) 44px;align-items:center;gap:12px;font-size:13.5px}
.hb-l{color:#3A4566;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.hb-t{position:relative;height:10px;border-radius:10px;background:#EEF1F7}
.hb-t i{position:absolute;left:0;top:0;bottom:0;width:var(--w);border-radius:10px;background:linear-gradient(90deg,#5C86FF,#1652F0);transform-origin:left;animation:bdG .9s cubic-bezier(.2,.8,.2,1) both;animation-delay:calc(var(--i) * 80ms + 200ms)}
.hb-t s{position:absolute;top:-4px;bottom:-4px;width:2px;background:#0B1433;border-radius:2px}
.hb b{text-align:right;font-weight:600}
.hbs.fun .hb{grid-template-columns:minmax(0,1.7fr) minmax(0,1.3fr) 44px}
.hb.dr .hb-l{overflow:visible}
.hbs.out .hb:last-child .hb-t i{background:linear-gradient(90deg,#F4C66A,#D99A1E)}
.hb.dr{margin:0 -10px;padding:8px 10px;border-radius:12px;background:#FFF5F4}
.hb.dr .hb-t i{background:linear-gradient(90deg,#F5A097,#D92D20)}
.hb.dr .hb-l::after{content:'Biggest drop';margin-left:8px;padding:2px 7px;border-radius:999px;background:#FDECEA;color:#B42318;font-size:11px;font-weight:500}
.hbs.pr9 .hb:nth-child(4) .hb-t i{background:linear-gradient(90deg,#F4C66A,#D99A1E)}
.hbs.pr9 .hb{grid-template-columns:minmax(0,1fr) 40px;row-gap:4px}
.hbs.pr9 .hb-t{grid-column:1 / -1;grid-row:2}
.hb-k{display:flex;align-items:center;gap:6px;margin-top:12px;font-size:12px;color:#5B6582}
.hb-k s{width:2px;height:12px;background:#0B1433;border-radius:2px}
.ll{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.ll-c{display:grid;grid-template-columns:52px minmax(0,1fr);align-items:center;column-gap:12px;row-gap:4px;padding:14px;border-radius:16px;background:#FFFAEB;animation:obIn .5s ease both;animation-delay:calc(var(--i) * 90ms + 250ms)}
.ll-c .rg{grid-row:1 / span 2}
.ll-c > span{display:flex;align-items:baseline;gap:6px}
.ll-c > span b{font-size:20px;font-weight:600;color:#8A5A00}
.ll-c > span em{font-style:normal;font-size:12px;color:#8A93AD}
.ll-c p{margin:0;font-size:13px;font-weight:500;line-height:1.4}
.qp{display:flex;flex-direction:column}
.qp-r{display:grid;grid-template-columns:50px 50px minmax(0,1.5fr) 110px minmax(0,1.1fr);align-items:center;gap:12px;padding:13px 0;border-top:1.5px solid #F0F2F8;font-size:13.5px;animation:obIn .45s ease both;animation-delay:calc(var(--i,0) * 80ms + 250ms)}
.qp-hd{border-top:0;padding-top:0;font-size:12px;font-weight:500;color:#8A93AD;animation:none}
.qp-q{font-weight:600}
.qp-o{display:inline-flex;justify-self:start;padding:2px 7px;border-radius:7px;background:#EAF0FF;color:#0E3BB8;font-size:11.5px;font-weight:600}
.qp-c{display:flex;align-items:center;gap:8px}
.qp-c i{flex:1;height:6px;border-radius:6px;background:linear-gradient(90deg,var(--c) var(--w),#EEF1F7 var(--w))}
.qp-c b{width:34px;text-align:right;font-weight:600}
.qp-r.rd{--c:#D92D20}.qp-r.am{--c:#D99A1E}.qp-r.ok{--c:#0F6B45}.qp-r.cb{--c:#1652F0}
.qp-p{font-size:12.5px;line-height:1.45;color:#5B6582}
.qp-r.rd .qp-p{color:#B42318;font-weight:500}
.qp-r.rd{margin:0 -10px;padding:13px 10px;border-radius:12px;background:#FFF5F4;border-top-color:transparent}
.qp-r.rd + .qp-r{border-top-color:transparent}
.q14{display:flex;align-items:center;gap:14px;padding:16px 18px;border-color:#DCE5FB;background:#FFFFFF url(NOVABG) center / cover no-repeat}
.q14 > div{flex:1}
.q14 b{font-size:15px;font-weight:600}
.q14 p{margin:2px 0 0 0;font-size:13.5px;color:#3A4566}
.nf{padding:20px;border-color:#DCE5FB;background:#FFFFFF url(NOVABG) center top / cover no-repeat}
.nf-h{display:flex;align-items:center;gap:12px;margin-bottom:14px}
.nf-h > span{display:flex;flex-direction:column}
.nf-h b{font-size:16px;font-weight:600}
.nf-h em{font-style:normal;font-size:12.5px;color:#5B6582}
.nf-c{display:grid;grid-template-columns:32px minmax(0,1fr) auto;align-items:center;gap:12px;padding:14px;border-radius:16px;background:rgba(255,255,255,.88);border:1px solid #E1E8FA;animation:obIn .5s ease both;animation-delay:calc(var(--i) * 120ms + 250ms)}
.nf-c + .nf-c{margin-top:8px}
.nf-s{align-self:start;width:32px;height:32px;border-radius:50%;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center;animation:nfS 3s ease-in-out infinite}
@keyframes nfS{50%{transform:rotate(20deg) scale(1.08)}}
.nf-c b{font-size:14.5px;font-weight:600;line-height:1.4}
.nf-c p{margin:4px 0 0 0;font-size:13px;line-height:1.5;color:#5B6582}
.chr-r{position:relative;width:120px;height:120px;margin:4px auto 0 auto}
.chr-r > span{position:absolute;inset:0;display:flex;align-items:center;justify-content:center}
.chr-r b{font-size:28px;font-weight:600;color:#0F6B45}
.ac9 ul{list-style:none;margin:0;padding:0}
.ac9 li{display:flex;gap:10px;padding:10px 0;border-top:1.5px solid #F0F2F8}
.ac9 li:first-child{border-top:0;padding-top:0}
.ac9-s{width:20px;height:20px;flex-shrink:0;border-radius:50%;display:flex;align-items:center;justify-content:center}
.ac9 li.ok .ac9-s{background:#E7F5EE;color:#0F6B45}
.ac9 li.am .ac9-s{background:#FFE7B8;color:#8A5A00}
.ac9 li > span:last-child{display:flex;flex-direction:column;gap:3px}
.ac9 b{font-size:13.5px;font-weight:500}
.ac9 em{font-style:normal;font-size:12.5px;line-height:1.45;color:#5B6582}
.ac9 .ds-link{align-self:flex-start}
.rvl2{display:flex;flex-direction:column;gap:12px}
.rvc{padding:18px 20px;display:flex;flex-direction:column;gap:12px;animation:obIn .5s ease both;animation-delay:calc(var(--i) * 100ms + 200ms)}
.rvc header{display:flex;align-items:center;gap:12px}
.rvc header > div{flex:1;display:flex;flex-direction:column;gap:3px}
.rvc header b{font-size:14.5px;font-weight:600}
.rvc header em{font-style:normal;font-size:12.5px;color:#8A93AD}
.rvc > p{margin:0;font-size:15px;line-height:1.6}
.rvc-r{display:flex;align-items:center;gap:8px}
.rvc-r .ds-in{flex:1;height:42px;font-size:13.5px;border-radius:999px;padding:0 16px}
.rvc-r .ds-ghost{flex-shrink:0}
.la2.sm{width:28px;height:28px;font-size:10.5px}
.rsm-t{display:flex;align-items:center;gap:14px;margin-bottom:14px}
.rsm-t > b{font-size:46px;font-weight:600;letter-spacing:-0.03em;line-height:1}
.rsm-t > span{display:flex;flex-direction:column;gap:4px}
.rsm-t em{font-style:normal;font-size:12.5px;color:#5B6582}
.rh{display:flex;flex-direction:column;gap:6px}
.rh-r{display:grid;grid-template-columns:28px minmax(0,1fr) 36px;align-items:center;gap:8px;font-size:12.5px;color:#5B6582}
.rh-r > span:first-child{display:flex;align-items:center;gap:3px;font-weight:600;color:#0B1433}
.rh-r > span:first-child i{width:10px;height:10px;background:#F4C66A;clip-path:polygon(50% 0,61% 35%,98% 35%,68% 57%,79% 91%,50% 70%,21% 91%,32% 57%,2% 35%,39% 35%)}
.rh-b{height:8px;border-radius:8px;background:#EEF1F7;overflow:hidden}
.rh-b i{display:block;width:var(--w);height:100%;border-radius:8px;background:#F4C66A;transform-origin:left;animation:bdG .9s ease both;animation-delay:calc(var(--i) * 80ms + 300ms)}
.rh-r em{font-style:normal;text-align:right}
.sf .rx-p{margin:-6px 0 12px 0}
.sf-r{display:grid;grid-template-columns:minmax(0,1fr) auto;row-gap:6px;padding:8px 0}
.sf-r > span:first-child{font-size:13px;color:#3A4566}
.sf-r b{font-size:13.5px;font-weight:600}
.sf-r b em{font-style:normal;font-weight:400;color:#8A93AD}
.sf-b{grid-column:1 / -1;height:6px;border-radius:6px;background:#EEF1F7;overflow:hidden}
.sf-b i{display:block;width:var(--w);height:100%;border-radius:6px;background:linear-gradient(90deg,#5C86FF,#1652F0);transform-origin:left;animation:bdG .9s ease both;animation-delay:calc(var(--i) * 80ms + 300ms)}
.tks{margin-top:16px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;align-items:start}
.tk{padding:18px 20px;display:flex;flex-direction:column;gap:10px;animation:obIn .5s ease both;animation-delay:calc(var(--i) * 90ms + 200ms)}
.tk.esc{border-color:#F4DDAA;background:linear-gradient(160deg,#FFFAF0,#FFFFFF 50%)}
.tk header{display:flex;align-items:center;justify-content:space-between;gap:10px}
.tk-k{font-size:11.5px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;color:#8A93AD}
.tk.esc .tk-k{color:#B76E00}
.tk-q{font-size:15.5px;font-weight:600;line-height:1.45}
.tk-w{display:flex;align-items:center;gap:8px;font-size:12.5px;color:#5B6582}
.tk-ai{padding:10px 12px;border-radius:12px;background:#F5F8FF}
.tk-ai-k{display:flex;align-items:center;gap:6px;font-size:12px;font-weight:600;color:#0E3BB8}
.tk-ai-k svg{width:12px;height:12px}
.tk-ai p{margin:4px 0 0 0;font-size:13px;line-height:1.5;color:#3A4566}
.tk-you{display:flex;align-items:flex-start;gap:10px;padding:10px 12px;border-radius:12px;background:#F2FAF5}
.tk-you p{margin:0;font-size:13.5px;line-height:1.5;color:#2C5240}
.tk .rvc-r .ds-link{flex-shrink:0;display:inline-flex;align-items:center;gap:4px}
.th{margin-top:16px;padding:6px 20px}
.th-r{display:grid;grid-template-columns:minmax(0,2fr) minmax(0,1fr) 80px 100px 150px;align-items:center;gap:12px;padding:14px 0;border-top:1.5px solid #F0F2F8;font-size:13.5px;animation:obIn .45s ease both;animation-delay:calc(var(--i,0) * 70ms + 250ms)}
.th-hd{border-top:0;font-size:12.5px;font-weight:500;color:#8A93AD;padding:10px 0;animation:none}
.th-t{display:flex;align-items:center;gap:10px;flex-wrap:wrap;min-width:0}
.th-t b{font-size:14.5px;font-weight:600}
.th-t .ds-tag{height:22px;font-size:11px}
.th-b{display:flex;align-items:center;gap:8px;color:#3A4566}
.th-n{display:inline-flex;align-items:center;gap:6px;color:#5B6582}
.th-n b{color:#0B1433;font-weight:600}
.th-n.z b{color:#B76E00}
.th-d{color:#5B6582}
.th-a{display:flex;align-items:center;justify-content:flex-end;gap:10px}
.th-a .ds-link{border:0;background:none;font-family:inherit;cursor:pointer;padding:0}
.th-r.pin{margin:0 -10px;padding:14px 10px;border-radius:14px;background:#F5F8FF;border-top-color:transparent}
.th-r.pin + .th-r{border-top-color:transparent}
.th-r.un .th-t b::before{content:'';display:inline-block;width:7px;height:7px;margin-right:8px;border-radius:50%;background:#E0A030;vertical-align:2px;animation:lvP2 2s ease-out infinite}
@keyframes lvP2{0%{box-shadow:0 0 0 0 rgba(224,160,48,.45)}100%{box-shadow:0 0 0 6px rgba(224,160,48,0)}}
@media (max-width: 1180px){.i9{grid-template-columns:repeat(2,minmax(0,1fr))}.g9{grid-template-columns:minmax(0,1fr)}.tks{grid-template-columns:minmax(0,1fr)}.arw{grid-template-columns:minmax(0,1fr)}}
@media (max-width: 960px){
.cf-g{width:100%}
.cf-g .ds-btn{width:100%;justify-content:space-between}
.utabs{margin:14px -16px 0 -16px;padding:0 16px;gap:20px;-webkit-mask-image:linear-gradient(90deg,#000 88%,transparent);mask-image:linear-gradient(90deg,#000 88%,transparent);}
.ut{height:42px;font-size:13.5px}
.fx3:not(.col),.fx3.five,.fx3.four,.vr3 .fx3.five{grid-template-columns:minmax(0,1fr);gap:0;padding:2px 14px;border-radius:14px;background:#F7F9FD}
.fx3:not(.col) > div{flex-direction:row;justify-content:space-between;align-items:center;gap:12px;padding:11px 0;border-radius:0;background:none}
.fx3:not(.col) > div + div{border-top:1.5px solid #EEF1F7}
.vr3 .fx3 > div:nth-child(4){display:flex}
.wk-r > .ceis{display:none}
.fx3 dd{font-size:13.5px;text-align:right}
.lv2-r .fx3:not(.col){background:#FFFFFF;border:1.5px solid #F4E9C8}
.lv2-r .fx3:not(.col) > div{border:0;background:none}
.lv2-r .fx3:not(.col) > div + div{border-top:1.5px solid #F7EED6}
.ko-card .fx3{background:none;padding:0 2px}
.lv2{grid-template-columns:minmax(0,1fr);gap:14px;padding:16px}
.lv2-l{flex-direction:row;justify-content:flex-start;gap:16px}
.cei,.cei .rg{width:96px;height:96px}
.cei-v b{font-size:28px}
.lv2-t{font-size:17px}
.lv2-a{flex-wrap:wrap;gap:8px 14px}
.lv2-a .ds-ghost{flex:1}
.rv2{padding:14px}
.vtl b{font-size:14px}
.vr3{padding:14px}
.va3{grid-template-columns:minmax(0,1fr);gap:0;border:1.5px solid #E6EAF3;border-radius:16px;overflow:hidden}
.va3-c{display:grid;grid-template-columns:38px minmax(0,1fr) auto;column-gap:12px;row-gap:2px;align-items:center;border-radius:0;padding:12px 14px;background:#FFFFFF}
.va3-c + .va3-c{border-top:1.5px solid #F0F2F8}
.va3-i{grid-row:1 / span 2;margin:0;background:#F5F8FF}
.va3-c em{margin:0;grid-column:2}
.va3-c .ds-tag{grid-row:1 / span 2;grid-column:3;height:22px;font-size:11px}
.fds-q{font-size:80px;right:12px}
.fds p{font-size:14.5px}
.ct{padding:14px 14px 4px 14px}
.ct .dr-t{flex-wrap:nowrap}
.ct .dr-f{flex:1;width:auto}
.ct-hd{display:none}
.ct{margin-top:20px}
.ct-r{grid-template-columns:auto auto minmax(0,1fr);gap:4px 0}
a.ct-r{margin:0 -8px;padding:12px 8px}
.ct-r > b{grid-column:1 / 3;grid-row:1}
.ct-r .ds-tag{grid-column:3;grid-row:1;justify-self:end}
.ct-v,.ct-r > span:nth-child(3),.ct-d{grid-row:2;font-size:12.5px;color:#5B6582;font-weight:400}
.ct-v{grid-column:1}
.ct-r > span:nth-child(3){grid-column:2}
.ct-r > span:nth-child(3)::before{content:'·';margin:0 6px}
.ct-d{grid-column:3;justify-self:end}
.fv3{margin-top:20px;gap:10px}
.fs3{grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.fs3-n{grid-column:1 / -1;padding:12px 14px;font-size:12.5px}
.fs3-n svg{width:26px;height:26px;padding:6px}
.fd3g{grid-template-columns:minmax(0,1fr);gap:10px}
.fs3 > span{padding:12px 14px}
.fs3 b{font-size:24px}
.fs3 em{font-size:12px}
.fd3{padding:14px}
.vp{grid-template-columns:minmax(0,1fr);margin-top:16px}
.vp-x{height:40px}
.vp-l{left:50%;right:auto;top:0;bottom:0;width:2px;height:auto;background:repeating-linear-gradient(180deg,#CBD3E6 0 5px,transparent 5px 10px)}
.vp-b{width:30px;height:30px}
.vpc{padding:16px;gap:10px}
.vpc .fx3{grid-template-columns:minmax(0,1fr)}
.cr3{padding:14px;gap:12px}
.cr3 p{font-size:13.5px}
.arc{padding:16px}
.arc .ds-ghost{align-self:stretch;justify-content:center}
.wk-m > .ack{order:4}
.wk-r > .asm{order:3}
.wk-r > .rsv{display:none}
.wac{grid-template-columns:minmax(0,1fr);gap:6px}
.wac li{padding:12px}
.wk-r > .dpc{order:2}
.asm-v > span{padding:10px}
.ko4{grid-template-columns:repeat(2,minmax(0,1fr))}
.rcd{grid-template-columns:minmax(0,1fr);gap:0;border:1.5px solid #E6EAF3;border-radius:16px;overflow:hidden;background:#FFFFFF}
.rcd-c,.rcd-c:nth-child(n+4){grid-column:auto;border:0;border-radius:0;padding:12px 14px}
.rcd-c + .rcd-c{border-top:1.5px solid #F0F2F8}
.wk-r > .rst{order:2}
.sc3{grid-template-columns:minmax(0,1fr);gap:0;border:1.5px solid #E6EAF3;border-radius:16px;overflow:hidden}
.sc3 .ds-opt{flex-direction:row;align-items:center;border:0;border-radius:0;padding:12px 14px}
.sc3 .ds-opt + .ds-opt{border-top:1.5px solid #F0F2F8}
.sc3 .ds-opt.on{box-shadow:inset 3px 0 0 #1652F0}
.ds-opt.sc3-o .ds-opt-ck{position:static;margin-left:auto}
.sc3-i{width:32px;height:32px;flex-shrink:0}
.wk-r > .ii{order:1;display:grid;grid-template-columns:34px minmax(0,1fr);align-items:center;gap:10px 12px}
.ii-i{width:34px;height:34px;border-radius:11px}
.ii p{grid-column:1 / -1}
.rq3w{margin-top:20px;gap:12px}
.rq3{padding:14px}
.rtl{grid-template-columns:minmax(0,1fr);gap:4px}
.rtl::before{left:15px;right:auto;top:16px;bottom:16px;width:2px;height:auto}
.rtl::after{display:none}
.rtl li{flex-direction:row;text-align:left;gap:12px;min-height:44px}
.rtl b{max-width:none}
.i9{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-top:18px}
.i9c{padding:14px;border-radius:18px;gap:4px}
.i9c-v{height:70px;margin:-14px -14px 0 -14px;padding:10px 12px}
.i9c .mc-i{width:34px;height:34px;margin-top:-24px}
.i9c b{flex:1;font-size:14px;line-height:1.3}
.i9c p{display:none}
.i9c .mc-a{font-size:12.5px}
.v9.bars{height:46px;gap:4px}.v9.bars i{width:11px}
.v9.dots{grid-template-columns:repeat(6,7px);gap:4px}.v9.dots i{width:7px;height:7px}
.v9.rg9,.v9.rg9 .rg{width:48px;height:48px}.v9.rg9 b{font-size:11px}
.v9.st9 b{font-size:20px}
.v9.th9 i{width:80px}.v9.th9 i:first-child{width:64px}
.v9.ch9 .b{width:70px}.v9.ch9 .a{width:54px}
.kp{grid-auto-flow:row;grid-template-columns:repeat(2,minmax(0,1fr));padding:4px}
.kp-c{padding:12px}
.kp-c + .kp-c{border-left:0}
.kp-c:nth-child(even){border-left:1.5px solid #F0F2F8}
.kp-c:nth-child(n+3){border-top:1.5px solid #F0F2F8}
.kp:has(> .kp-c:nth-child(3):last-child){grid-template-columns:repeat(3,minmax(0,1fr))}
.kp-c:nth-child(3):last-child{border-top:0;border-left:1.5px solid #F0F2F8}
.kp-c b{font-size:22px}
.kp-c span{font-size:12px}
.kp-c em{margin-top:2px;padding:0;background:none !important;font-size:11.5px;line-height:1.35}
.kp-c:not(.am):not(.rd):not(.ok):not(.cb) em{color:#8A93AD}
.g9{gap:14px;margin-top:14px}
.hb,.hbs.fun .hb{grid-template-columns:minmax(0,1fr) 40px;row-gap:5px;font-size:13px}
.hb-t{grid-column:1 / -1;grid-row:2}
.hb-l{white-space:normal}
.fc-a{display:none}
.g9 + .fc{margin-top:14px}
.ll{grid-template-columns:minmax(0,1fr);gap:8px}
.qp-hd{display:none}
.qp-r{grid-template-columns:auto auto minmax(0,1fr);gap:6px 10px}
.qp-q{grid-row:1;grid-column:1}
.qp-o{grid-row:1;grid-column:2}
.qp-c{grid-row:1;grid-column:3}
.qp-t{grid-column:1 / -1;grid-row:2;font-size:13px}
.qp-p{grid-column:1 / -1;grid-row:3}
.qp-r.rd{margin:0 -8px;padding:12px 8px}
.wk-r > .rx:has(.pr9){order:1}
.q14{flex-wrap:wrap;padding:14px}
.q14 > div{flex-basis:calc(100% - 50px)}
.q14 .ds-btn{width:100%;justify-content:space-between}
.nf{padding:14px}
.nf-c{grid-template-columns:minmax(0,1fr);gap:10px;padding:12px 14px}
.nf-s{display:none}
.nf-c > .ds-ghost,.nf-c > .ds-tag{justify-self:start}
.wk-r > .chr{order:1}
.wk-r > .chr .chr-r,.wk-r > .chr .chr-r .rg{width:84px;height:84px}
.wk-r > .chr .chr-r b{font-size:20px}
.wk-r > .chr{display:grid;grid-template-columns:84px minmax(0,1fr);column-gap:14px;align-items:center}
.wk-r > .chr .rx-k{grid-column:2;margin:0}
.wk-r > .chr .chr-r{grid-row:1 / span 2;margin:0}
.wk-r > .chr .rx-p{grid-column:2;margin:4px 0 0 0}
.wk-r > .ac9{order:1}
.wk-r > .rsm{order:1}
.wk-r > .sf{order:1}
.rsm-t > b{font-size:38px}
.rvc{padding:14px}
.rvc > p{font-size:14px}
.tks{grid-template-columns:minmax(0,1fr);gap:10px}
.tk{padding:14px}
.tk-q{font-size:14.5px}
.rvc-r{flex-wrap:wrap}
.rvc-r .ds-in{min-width:0;height:44px}
.rvc-r .ds-ghost{height:44px}
.tk .rvc-r .ds-link{flex-basis:100%;min-height:32px}
.th{padding:2px 14px}
.th-hd{display:none}
.th-r{grid-template-columns:minmax(0,1fr) auto;gap:6px 10px}
.th-t{grid-column:1 / -1}
.th-b{grid-column:1;font-size:12.5px}
.th-n{grid-column:2;grid-row:2;justify-self:end;font-size:12.5px}
.th-d{display:none}
.th-a{grid-column:1 / -1;justify-content:flex-start}
.th-r.pin{margin:0 -8px;padding:14px 8px}
.cr9{padding:2px 14px}
.cr9-hd{display:none}
.cr9-r{grid-template-columns:42px auto minmax(0,1fr) auto;gap:6px 0;padding:14px 0}
.cr9-m{grid-column:1 / 4;grid-row:1;gap:10px}
.cr9-m .la2{width:32px;height:32px;font-size:11px}
.cr9-s{grid-column:4;grid-row:1 / span 3;align-self:center;padding-left:10px}
.cr9-ro{grid-column:2;grid-row:2}
.cr9-ro .ds-tag{height:22px;font-size:11px}
.cr9-c{grid-column:3;grid-row:2;align-self:center;min-width:0;padding-left:8px;font-size:12.5px;color:#5B6582;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cr9-st{grid-column:2 / 4;grid-row:3;grid-template-columns:7px auto minmax(0,1fr);column-gap:8px;font-size:12.5px}
.cr9-st .ds-link{grid-column:3;grid-row:1;font-size:12.5px;margin-left:4px}
.cr9-na{display:block;width:44px;text-align:center;padding:0}
.wk-a2 .sv-s{order:1;align-items:flex-start;text-align:left;padding:0 4px 4px 4px}
.wk-r > .cpv{order:1}
.wk-r > .cw9{order:3;padding:16px 0 12px 0}
.wk-r > .cw9 .rx-k{margin:0 16px 10px 16px}
.cw9 dl{display:flex;gap:8px;overflow-x:auto;scroll-snap-type:x mandatory;padding:0 16px 4px 16px;scrollbar-width:none;-webkit-mask-image:linear-gradient(90deg,#000 88%,transparent);mask-image:linear-gradient(90deg,#000 88%,transparent);}
.cw9 dl::-webkit-scrollbar{display:none}
.cw9 dl div,.cw9 dl div:first-child{flex:0 0 68%;box-sizing:border-box;scroll-snap-align:start;scroll-margin-left:16px;padding:12px 14px;border:0;border-radius:14px;background:#F7F9FD}
.wk-a2 .sv-s{font-size:12px}
.ak .dl-b{padding:6px 16px 4px 16px}
.ak .dl-h{padding:22px 52px 0 52px}
.ak-h{font-size:19px}
.dl.ak{width:100%}
}
'''.replace('NOVABG', __import__('kit').NOVA_BG)

write('Manage3.dc.html', doc('Manage Published Course · validation, archive, insights · shared source', kit.KIT_CSS + '\n' + dash.DASH_CSS + BASE_CSS + WK_CSS + CSS, body(), JS))

BOARDS = [
    ('MGT-007', 'h-a', 'CR-COURSE-MGT-007 · Validation History (default)'),
    ('MGT-007A', 'h-rec', 'CR-COURSE-MGT-007A · Validation Record Details'),
    ('MGT-007B', 'h-cases', 'CR-COURSE-MGT-007B · Full Validation Case History'),
    ('MGT-007C', 'h-find', 'CR-COURSE-MGT-007C · Findings & Decisions'),
    ('MGT-007D', 'h-ver', 'CR-COURSE-MGT-007D · Validation & Version Relationship'),
    ('MGT-007E-REV', 'h-rev', 'CR-COURSE-MGT-007E · Required Action — Revalidation Required'),
    ('MGT-007E-CHG', 'h-chg', 'CR-COURSE-MGT-007E · Required Action — Changes Requested'),
    ('MGT-008', 'a-a', 'CR-COURSE-MGT-008 · Archive & Removal (home)'),
    ('MGT-008A', 'a-impact', 'CR-COURSE-MGT-008A · Archive Impact Review (Step 1/3)'),
    ('MGT-008B', 'a-confirm', 'CR-COURSE-MGT-008B · Archive Reason & Confirmation (Step 2/3)'),
    ('MGT-008C', 'a-done', 'CR-COURSE-MGT-008C · Archive Success (Step 3/3)'),
    ('MGT-008D', 'a-detail', 'CR-COURSE-MGT-008D · Archived Course Detail'),
    ('MGT-008E', 'a-restore', 'CR-COURSE-MGT-008E · Restore Archived Course'),
    ('MGT-008F', 'a-req', 'CR-COURSE-MGT-008F · Request Course Removal'),
    ('MGT-008G', 'a-status', 'CR-COURSE-MGT-008G · Removal Review & Status'),
    ('MGT-008H', 'a-blocked', 'CR-COURSE-MGT-008H · Restricted Action (branch)'),
    ('MGT-009', 'i-hub', 'CR-COURSE-MGT-009 · Insights & Engagement (hub)'),
    ('MGT-009A', 'i-perf', 'CR-COURSE-MGT-009A · Learning Performance'),
    ('MGT-009B', 'i-asm', 'CR-COURSE-MGT-009B · Assessment Analytics'),
    ('MGT-009C', 'i-health', 'CR-COURSE-MGT-009C · Content Health'),
    ('MGT-009D', 'i-rev', 'CR-COURSE-MGT-009D · Reviews & Feedback'),
    ('MGT-009E', 'i-sup', 'CR-COURSE-MGT-009E · Learner Questions & Support'),
    ('MGT-009F', 'i-disc', 'CR-COURSE-MGT-009F · Course Discussion'),
    ('CREDITS', 'c-credits', 'CR-COURSE-CREDITS · Course Credits & Visibility'),
    ('CREDITS-ASK', 'c-ask', 'CR-COURSE-CREDITS-ASK · Ask a contributor to be credited'),
]
BOARDS = [(c, 'Manage3', {'page': p}, t) for c, p, t in BOARDS]

if __name__ == '__main__':
    import sys
    H = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else {}
    for code, src, props, title in BOARDS:
        hd, hm = H.get(code, (3000, 3000))
        write(code + '.dc.html', wrapper(title + ' · Desktop', src, props, 1440, hd))
        write(code + '-Mobile.dc.html', wrapper(title + ' · Mobile', src, props, 390, hm))
    print('ok', len(BOARDS), 'boards; toggles', W.n)
