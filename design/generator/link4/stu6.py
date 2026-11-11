"""Link 4 · Batch 6: Manage Published Course (hub, Publishing & Visibility, unpublish) + downstream states.
Client copy word for word (prototype-only notes omitted).

Manage.dc.html   (prop page: hub | a | edit | review | b | c | d | e | f | g | notice | ds-ov | ds-cr)   creator dashboard shell
Unpublish.dc.html (prop step: impact | reason | confirm | done | blocked)                               focus flow, same layout as Submit
Learner.dc.html  (prop page: mylearning)                                                                 learner app (separate interface)
Course Overview and My Creations reuse the Link 1/2 designs (CR-COURSE-OV-001, CR-HOME-EXP).
"""
import json
from l4kit import *
from rail import *
from kit import coin, credit, emblem
import stu2

W = Toggles()
COV = '<span class="cv-t" aria-hidden="true"><i>SQL</i></span>'
PRICE = 'Version 1.0 · %s1,800 DLP · %s420 Credits' % (coin(), credit())

# ---------------------------------------------------------------- creator dashboard shell (same nav as Links 1/2)
CNAV = [('', [('dash', 'Dashboard', '#')]),
        ('Create', [('exp', 'My Creations', 'MGT-DS-CR.dc.html'), ('new', 'Create new', 'STU-001.dc.html')]),
        ('Collaboration', [('send', 'Invitations', 'INV-001.dc.html'), ('path', 'Opportunities', 'OPP-001.dc.html'), ('pencil', 'My Applications', 'OPP-004.dc.html'), ('program', 'Shared Courses', 'NAV-002.dc.html')]),
        ('Work', [('assigned', 'Assigned to me', '#'), ('valid', 'Validation Centre', '#'), ('disc', 'Discussions', '#'), ('support', 'Learner support', '#'), ('cal', 'Calendar', '#')]),
        ('Insights', [('learners', 'Learners', '#'), ('analytics', 'Analytics', '#')]),
        ('Economy', [('earn', 'Earnings & payouts', '#'), ('wallet', 'Credit Wallet', '#')]),
        ('Creator', [('nova', 'Nova · your Copilot', '#'), ('centre', 'Creator Centre', '#'), ('profile', 'Creator profile', '#'), ('ready', 'Verification & readiness', '#')]),
        ('Account', [('settings', 'Settings', '#')])]
BADGE = {'Invitations': '2', 'Validation Centre': '1', 'Discussions': '7', 'Learner support': '2'}
def cr_side(active):
    h = ''
    for g, items in CNAV:
        if g: h += '<span class="ds-glab">%s</span>' % g
        for k, l, href in items:
            on = l == active
            h += '<a href="%s" class="ds-item%s"%s>%s<span class="ci-t">%s</span>%s</a>' % (
                href, ' ds-on' if on else '', ' aria-current="page"' if on else '', ICON(I[k], 19), l, ('<span class="ds-badge">%s</span>' % BADGE[l]) if l in BADGE else '')
    return '''<div class="ds-scrim {{navCls}}" onClick="{{toggleNav}}"></div>
<nav class="ds-side {{navCls}}" aria-label="Main"><a class="cr-lg" href="#" aria-label="Credalio"><span class="lg-word"></span></a>
<button type="button" class="ds-icon-btn ds-close" onClick="{{toggleNav}}" aria-label="Close menu">%s</button>%s</nav>''' % (ic('x', 18), h)
CR_TOP = '''<header class="ds-top">
<button type="button" class="ds-icon-btn ds-menu" onClick="{{toggleNav}}" aria-label="Open menu">%s</button>
<span class="ds-mlogo"><span class="lg-word"></span></span>
<label class="ds-search">%s<span class="sr-only">Search</span><input placeholder="Search your learning experiences, learners, discussions..."></label>
<span style="flex-grow: 1"></span>
<a href="#" class="ds-tok" aria-label="72,450 Creio">%s<span>72.4K</span></a>
<a href="#" class="ds-icon-btn ds-hide-sm" aria-label="Help">%s</a>
<a href="#" class="ds-icon-btn" aria-label="Notifications, 9 new">%s<span class="bl-c">9</span></a>
<a href="#" class="cw-me" aria-label="Your account">%s</a>
</header>''' % (ic('menu', 20), ic('search', 18), COIN('tp', 26), ic('help', 19), ic('bell', 19), av(ME, 'AO', 40))

def crumbs(items):
    return '<nav class="bc" aria-label="Breadcrumb">%s</nav>' % ''.join(
        ('<a href="%s">%s</a>%s' % (h, l, ic('chev', 13, 2))) if h else '<span>%s</span>' % l for l, h in items)

def course_strip(status, tone, extra=''):
    return ('<section class="ds-card cst ob-in2">%s<div class="cst-b"><b>Data Analysis with SQL</b><span class="cst-t"><span class="ds-tag %s">%s</span><span class="gb">%s<span>Gold Validated</span></span></span>'
            '<span class="cst-p">%s</span></div>%s</section>') % (COV, tone, status, ic('badge', 12, 2.2), PRICE, extra)

PAGES = []
def P(key, active, body):
    PAGES.append((key, active, body))

# ---------------------------------------------------------------- CR-COURSE-MGT-001 Manage hub
FACTS = [('Course ID', 'CRS-20394'), ('Industry / Domain', 'Technology / Data & Analytics'), ('DLP requirement', '%s1,800 DLP' % coin()),
         ('Lifetime access price', '%s420 Credits' % credit()), ('Last validated', '12 Sep 2026')]
STAT = [('Marketplace', 'Visible', 'New learners can discover', 'globe', 'ok'), ('Enrollment', 'Open', 'Eligible learners can enroll', 'users', 'ok'),
        ('Validation', 'Gold', 'Current live version', 'badge', 'gold'), ('Revision', 'Draft Pending', 'Separate from live v1.0', 'layers', 'am')]
MGT = [('globe', 'Publishing & Visibility', 'Unpublish the course or manage marketplace availability and new enrollments.', 'Manage Publishing', 'MGT-002.dc.html', ''),
       ('wallet', 'Pricing & Access', 'Manage approved DLP and Credit prices for new purchases within policy limits.', 'Manage Pricing', '#', ''),
       ('layers', 'Course Updates & Versions', 'View live and draft versions, revisions and revalidation status.', 'Manage Versions', '#', 'dot'),
       ('users', 'Learner Access & Enrollment', 'Review learners, active access and the impact of enrollment changes.', 'View Learner Access', '#', ''),
       ('valid', 'Validation History', 'View validation results, decisions and revalidation cases for this course.', 'View Validation', '#', ''),
       ('analytics', 'Insights & Engagement', 'Learning performance, assessments, content health, reviews, learner support and discussion.', 'View Insights', '#', ''),
       ('profile', 'Course Credits & Visibility', 'Choose which creators learners see on the course page. Lead Creator and Co-Creators show by default.', 'Manage Credits', 'CREDITS.dc.html', ''),
       ('trash', 'Archive & Removal', 'Restricted lifecycle actions: archiving and permanent removal requests.', 'Manage Removal', '#', 'warn')]
def mcard(i, m):
    icon, t, d, cta, href, k = m
    return '<a class="mc %s" href="%s" style="--i: %d"><span class="mc-i">%s</span><b>%s</b><p>%s</p><span class="mc-a">%s%s</span>%s</a>' % (
        k, href, i, ic(icon, 20, 1.9) if icon in EXTRA or icon in I else '', t, d, cta, ic('arrowr', 14, 2.2), '<span class="mc-d" aria-label="Has a pending draft"></span>' if k == 'dot' else '')
P('hub', 'My Creations',
  crumbs([('My Creations', 'MGT-DS-CR.dc.html'), ('Courses', 'MGT-DS-CR.dc.html'), ('Data Analysis with SQL', 'MGT-DS-OV.dc.html'), ('Manage', '')]) +
  '''<header class="pg-h ob-in"><div class="pg-hl"><h1 class="ds-h1">Manage Course</h1><p class="ds-sub">Control how your published course is available, accessed and maintained.</p></div>
<div class="pg-hr hub-a"><a class="ds-ghost sm" href="MGT-DS-OV.dc.html">%s<span>Back to Overview</span></a><a class="ds-ghost sm" href="STU-PRV.dc.html">%s<span>Preview as Learner</span></a><a class="ds-ghost sm" href="STU-009.dc.html">%s<span>Edit Course</span></a></div></header>
<section class="ds-card mh ob-in2"><div class="mh-t">%s<div class="mh-b"><span class="cst-t"><span class="ds-tag green"><i class="lv-d"></i>Published</span><span class="gb">%s<span>Gold Validated</span></span></span><h2>Data Analysis with SQL</h2><span class="cst-p">%s</span></div>
<div class="mh-pu"><span class="mh-pk">Pending update</span><b>Draft update pending assessment</b><span class="ds-tag amber">v1.1 draft</span></div></div>
<dl class="mh-f">%s</dl></section>
<section class="ob-in3"><h2 class="sh">Course Status</h2><div class="ms4">%s</div></section>
<section class="ob-in4"><h2 class="sh">Course Management</h2><div class="mcs">%s</div></section>''' % (
      ICON(I['back'], 15, 2), ic('eye', 15, 2), ic('edit', 15, 2), COV, ic('badge', 12, 2.2), PRICE,
      ''.join('<div><dt>%s</dt><dd>%s</dd></div>' % f for f in FACTS),
      ''.join('<div class="ms %s"><span class="ms-i">%s</span><span class="ms-b"><em>%s</em><b>%s%s</b><span>%s</span></span></div>' % (
          k, ic(i, 18, 2) if i in EXTRA or i in I else '', l, ('<i class="lv-d"></i>' if k == 'ok' else ''), v, d) for l, v, d, i, k in STAT),
      ''.join(mcard(i, m) for i, m in enumerate(MGT))))

# ---------------------------------------------------------------- CR-COURSE-MGT-002 Publishing & Visibility (states)
PUB_D = {'Published': 'The current version is approved and published.', 'Unpublished': 'Voluntarily withdrawn from new public access.',
         'Restricted': 'Credalio has restricted availability for this course.'}
VIS_D = 'Controls whether new learners can discover this course.'
ENR_D = 'Controls whether eligible learners can start or purchase access.'
VAL_IC = {'Published': ('check', 'ok'), 'Unpublished': ('eye', 'gy'), 'Restricted': ('lock', 'rd'), 'Visible': ('eye', 'ok'), 'Hidden': ('eye', 'gy'),
          'Open': ('users', 'ok'), 'Paused': ('clock', 'am'), 'Closed': ('lock', 'gy'), 'System-controlled': ('lock', 'gy')}
STATES = {
    'a': ('Published', 'Visible', 'Open', None, 'Manage Availability', 'MGT-002-EDIT.dc.html', True),
    'b': ('Published', 'Visible', 'Paused', ('ok', 'check', 'Enrollment Paused', 'New enrollments have been paused. Your course remains visible in the marketplace.'), 'Resume Enrollments', 'MGT-002.dc.html', True),
    'c': ('Published', 'Hidden', 'Paused', ('ok', 'eye', 'Course Hidden', 'Your course is no longer discoverable in the public marketplace. New enrollments have been paused.'), 'Show Course', 'MGT-002.dc.html', True),
    'd': ('Unpublished', 'Hidden', 'Closed', None, 'Republish Course', '#', False),
    'e': ('Restricted', 'System-controlled', 'System-controlled', ('rd', 'lock', 'Publishing Controls Unavailable', 'Credalio has temporarily restricted this course. Review the notice in your Validation Centre for next steps. Creators cannot override a Restricted state by switching visibility back on.'), 'Review Restriction', 'MGT-002-NOTICE.dc.html', False),
    'f': ('Published', 'Visible', 'Open', ('am', 'users', 'Organization Approval Required', 'This course belongs to an organization. Being the Lead Creator for content validation does not automatically grant authority to change publication settings — organization publishing policy must be honored.'), 'Request Approval', '#', True),
    'g': ('Published', 'Visible', 'Open', ('rd', 'warn', 'Couldn’t save your change', 'Another authorized team member changed these settings while you were editing — or the backend did not confirm the update. Your previous state has been preserved. Retry or refresh to see the latest state before saving again.'), 'Manage Availability', 'MGT-002-EDIT.dc.html', True),
}
def stile(label, val, desc, sw=True, i=0):
    icon, k = VAL_IC[val]
    tr = '<span class="sw-tr" aria-hidden="true"><i></i></span>' if sw else '<span class="sw-pd" aria-hidden="true"></span>'
    return '<div class="sw %s%s" style="--i: %d"><span class="sw-l">%s</span><span class="sw-v"><span class="sw-i">%s</span><b>%s</b></span><p>%s</p>%s</div>' % (
        k, ' lg' if len(val) > 12 else '', i, label, ic(icon, 16, 2.2), val, desc, tr)
HIST = [('12 Sep 2026', 'Course Published', 'Lead Creator'), ('12 Sep 2026', 'Gold Validation Applied', 'Credalio')]
RAIL_PUB = '''<section class="ds-card rx lap ob-in3"><span class="rx-k">Learner Access Protection</span><p>Changing visibility or pausing enrollment does not automatically revoke existing learner entitlements.</p>
<div class="lap-n"><span><b>86</b><em>Active DLP Learners</em></span><span><b>42</b><em>Lifetime Purchasers</em></span></div><p class="rx-p">Learners who already have access keep it according to their current entitlement rules.</p><a class="ds-link sm" href="#">View Learner Access%s</a></section>
<section class="ds-card rx ph2 ob-in4"><div class="ph2-h"><span class="rx-k">Publication History</span><a class="ds-link sm" href="#">View Full History</a></div><ol>%s</ol></section>''' % (
    ic('arrowr', 14, 2.2), ''.join('<li><span class="ph2-d"></span><span><em>%s · %s</em><b>%s</b></span></li>' % (d, w, e) for d, e, w in HIST))
UNPUB = '''<section class="ds-card dz ob-in4"><span class="dz-i">%s</span><div class="dz-b"><b>Unpublish Course</b><p>Remove this course from public availability and stop new enrollments. This is different from temporarily pausing enrollments.</p><span class="dz-n">%s<span>Requires impact review and confirmation</span></span></div><a class="ds-ghost dz-a" href="MGT-003A.dc.html">Unpublish Course</a></section>''' % (ic('eye', 20, 2), ic('lock', 12, 2.2))

def pub_page(state, overlay=''):
    pub, vis, enr, ban, act, href, unp = STATES[state]
    tone = {'Published': 'green', 'Unpublished': '', 'Restricted': 'red'}[pub]
    banner = ''
    if ban:
        k, icon, h, t = ban
        banner = '<div class="bn2 %s ob-in">%s<span class="bn2-i">%s</span><div><b>%s</b><p>%s</p></div></div>' % (k, '<span class="bn2-g"></span>' if k == 'ok' else '', ic(icon, 18, 2.2), h, t)
    main = '''<section class="ds-card pv2 ob-in2"><div class="pv2-h">%s<div class="cst-b"><b>Data Analysis with SQL</b><span class="cst-t"><span class="ds-tag %s">%s</span><span class="gb">%s<span>Gold Validated</span></span></span><span class="cst-p">%s</span></div><a class="ds-ghost sm pv2-l" href="STU-PRV.dc.html">%s<span>View Live Listing</span></a></div>
<div class="sws">%s%s%s</div><div class="pv2-a">%s</div></section>%s''' % (
        COV, tone, pub, ic('badge', 12, 2.2), PRICE, ic('eye', 15, 2),
        stile('Publication Status', pub, PUB_D[pub], False, 0), stile('Marketplace Visibility', vis, VIS_D, True, 1), stile('New Enrollments', enr, ENR_D, True, 2),
        ('<a class="ds-btn sm2" href="%s"><span>%s</span><span class="ob-arrow">%s</span></a>' % (href, act, ARROW)), UNPUB if unp else '')
    return (crumbs([('Manage Course', 'MGT-001.dc.html'), ('Publishing & Visibility', '')]) +
            '<header class="pg-h ob-in"><div class="pg-hl"><a class="ds-back" href="MGT-001.dc.html">%s<span>Back to Manage Course</span></a><h1 class="ds-h1">Publishing &amp; Visibility</h1><p class="ds-sub">Control how learners discover and enroll in your published course.</p></div></header>%s'
            % (ICON(I['back'], 15, 2), banner) +
            '<div class="wk"><div class="wk-m">%s</div><aside class="wk-r">%s</aside></div>%s' % (main, RAIL_PUB, overlay))

# ---------- availability dialogs (step 2 / step 3 of 4)
def aopt(t, d, on, grp, tag_=''):
    return W.opt('<span class="o-t"><b>%s%s</b><span>%s</span></span>' % (t, tag_, d), on, grp, 'sm avo')
AV_EDIT = '''<div class="ov-scrim"></div>
<div class="dl av-dl" role="dialog" aria-modal="true" aria-label="Manage Availability"><header class="dl-h"><span class="dl-i">%s</span><div class="dl-ht"><span class="dl-k">Step 2 of 4 · Choose New Settings</span><h2>Manage Availability</h2></div><a class="ds-x sm" href="MGT-002.dc.html" aria-label="Close">%s</a></header>
<div class="dl-b"><p class="dl-p">Choose a valid combination. Hiding the course automatically pauses new enrollments to prevent unlisted public enrollment.</p>
<span class="dl-l">Marketplace Visibility</span><div class="av-g">%s%s</div>
<span class="dl-l">New Enrollments</span><div class="av-g">%s%s</div>
<p class="dl-n">%s<span><b>Example</b> A creator updating the course wants to avoid new enrollments while preserving its public listing: Visibility stays Visible, Enrollment becomes Paused.</span></p></div>
<footer class="dl-f"><a class="ds-ghost" href="MGT-002.dc.html">Back</a>%s</footer></div>''' % (
    ic('globe', 20, 2), ic('x', 16, 2.2),
    aopt('Visible in Marketplace', 'Appears in search, categories, recommendations and public listings.', True, 'vis'),
    aopt('Hidden from Marketplace', 'Excluded from discovery. Automatically pauses new enrollment.', False, 'vis'),
    aopt('Open', 'New eligible learners can enroll using DLP or purchase lifetime access.', False, 'enr'),
    aopt('Paused', 'New enrollments and lifetime purchases are temporarily blocked.', True, 'enr'),
    ic('bulb', 16, 2), btn('Review Impact', 'MGT-002-REVIEW.dc.html'))
AV_REVIEW = '''<div class="ov-scrim"></div>
<div class="dl av-dl" role="dialog" aria-modal="true" aria-label="Pause New Enrollments?"><header class="dl-h"><span class="dl-i am">%s</span><div class="dl-ht"><span class="dl-k">Step 3 of 4 · Review Impact</span><h2>Pause New Enrollments?</h2></div><a class="ds-x sm" href="MGT-002.dc.html" aria-label="Close">%s</a></header>
<div class="dl-b"><p class="dl-p">New learners will not be able to enroll in Data Analysis with SQL or purchase lifetime access while enrollment is paused. Existing learners will retain access according to their current entitlements.</p>
<div class="dif">%s</div>
<p class="dl-n">%s<span>An audit event will be recorded and the public listing will show “Enrollment temporarily unavailable,” not “Course unavailable.”</span></p></div>
<footer class="dl-f"><a class="ds-ghost" href="MGT-002-EDIT.dc.html">Cancel</a>%s</footer></div>''' % (
    ic('clock', 20, 2), ic('x', 16, 2.2),
    ''.join('<div class="dif-r %s"><span>%s</span><b>%s</b></div>' % (k, l, v) for l, v, k in [
        ('Marketplace discovery', 'Unchanged · Visible', ''), ('New enrollment', 'Open <i>%s</i> <em>Paused</em>' % ic('arrowr', 13, 2.4), 'ch'), ('Existing learner access', 'Unaffected', 'ok')]),
    ic('file', 16, 2), btn('Pause Enrollments', 'MGT-002B.dc.html'))

for k in 'abcdefg':
    P(k, 'My Creations', pub_page(k))
P('edit', 'My Creations', pub_page('a', AV_EDIT))
P('review', 'My Creations', pub_page('a', AV_REVIEW))

# ---------------------------------------------------------------- MGT-002-E2 Restriction notice
NSUM = [('Restricted by', 'Credalio Validation'), ('Restriction type', 'Temporary · pending review'), ('Applied', '14 Oct 2026'), ('Linked case', 'VAL-00928')]
AFF = [('New enrollments', 'Paused by Credalio', 'am', 'users'), ('Marketplace visibility', 'Hidden from discovery', 'am', 'eye'), ('Pricing changes', 'Locked', 'gy', 'lock'), ('Existing learners', 'Access preserved', 'ok', 'check')]
NEXT = ['Review the finding', 'Fix the course in Course Studio', 'Resubmit for validation', 'Restriction lifted by Credalio']
P('notice', 'My Creations',
  crumbs([('Manage Course', 'MGT-001.dc.html'), ('Publishing & Visibility', 'MGT-002E.dc.html'), ('Restriction Notice', '')]) +
  '''<header class="pg-h ob-in"><div class="pg-hl"><a class="ds-back" href="MGT-002E.dc.html">%s<span>Back to Publishing &amp; Visibility</span></a><h1 class="ds-h1">Restriction Notice</h1><p class="ds-sub">Why Credalio restricted Data Analysis with SQL, what is affected, and what you can do next. This notice is read-only.</p></div></header>
<div class="wk"><div class="wk-m">
<section class="ds-card rn2 ob-in2"><div class="rn2-h"><span class="rn2-i">%s</span><div><span class="rx-k">Restriction summary</span><span class="ds-tag red">Restricted</span></div></div>
<div class="rn2-r"><span>Reason</span><b>Assessment answer key mismatch reported by learners</b></div><dl class="rn2-g">%s</dl></section>
<section class="ob-in3"><h2 class="sh">What is affected</h2><div class="af4">%s</div></section>
</div><aside class="wk-r"><section class="ds-card rx nx4 ob-in3"><span class="rx-k">Next steps</span><ol>%s</ol></section><section class="ds-card rx wcd ob-in4"><span class="rx-k">What you can do</span><p>Creators cannot override a restriction by switching visibility back on. Review the findings, correct the issue, and resubmit for validation. Credalio lifts the restriction once the case is resolved.</p>
<div class="wcd-a">%s<a class="ds-ghost sm" href="#">Open Validation History</a><a class="ds-link" href="#">View Learner Access</a></div></section></aside></div>''' % (
      ICON(I['back'], 15, 2), ic('lock', 22, 2), ''.join('<div><dt>%s</dt><dd>%s</dd></div>' % r for r in NSUM),
      ''.join('<div class="af %s" style="--i: %d"><span class="af-i">%s</span><em>%s</em><b>%s</b></div>' % (k, i, ic(icn, 17, 2.2) if icn in EXTRA else ic(icn, 17, 2.2), l, v) for i, (l, v, k, icn) in enumerate(AFF)),
      ''.join('<li class="%s" style="--i: %d"><span class="nx-n">%d</span><b>%s</b></li>' % ('on' if i == 0 else '', i, i + 1, t) for i, t in enumerate(NEXT)),
      btn('Review Findings', 'STU-055D.dc.html', 'sm2')))

# ---------------------------------------------------------------- Downstream · Course Overview (unpublished) — CR-COURSE-OV-001 design
P('ds-ov', 'My Creations',
  '''<a class="ds-back ob-in" href="MGT-DS-CR.dc.html">%s<span>My Creations</span></a>
<header class="ovh ob-in"><span class="ovh-i">%s</span><div class="ovh-t"><h1 class="ds-h1">Data Analysis with SQL</h1><span class="cst-t"><span class="ds-tag">Unpublished</span><span class="gb">%s<span>Gold Validated</span></span><span class="ovh-v">Version 1.0 · Unpublished 22 Oct 2026</span></span></div>
<div class="ovh-a"><a class="ds-ghost sm" href="STU-PRV.dc.html">Preview as Learner</a><a class="ds-ghost sm" href="STU-009.dc.html">Edit Course</a>%s</div></header>
<section class="ds-card up2 ob-in2"><div class="up2-v" aria-hidden="true"><span class="up2-c">%s</span><span class="up2-x"></span></div><div class="up2-b"><b>This course is unpublished</b><p>It no longer accepts new enrollments or appears in the marketplace. Existing learner entitlements remain preserved. Historical validation (Gold · VAL-00928) remains recorded. Republishing may require revalidation if material changes occurred.</p>
<div class="up2-s">%s</div><a class="ds-link" href="MGT-002D.dc.html">%s<span>Back to Manage Course</span></a></div></section>''' % (
      ICON(I['back'], 15, 2), ic('course', 26, 1.8), ic('badge', 12, 2.2), btn('Republish Course', '#', 'sm2'), COV,
      ''.join('<span class="%s">%s<span><em>%s</em><b>%s</b></span></span>' % (k, ic(i, 15, 2.2), l, v) for l, v, i, k in [
          ('Marketplace', 'Hidden', 'eye', 'gy'), ('New enrollments', 'Closed', 'lock', 'gy'), ('Existing entitlements', 'Preserved', 'check', 'ok'), ('Validation', 'Gold · VAL-00928', 'badge', 'gold')]),
      ICON(I['back'], 14, 2)))

# ---------------------------------------------------------------- Downstream · My Creations (unpublished card) — CR-HOME-EXP design
ROWS = [('Data Analysis with SQL', 'Unpublished', '', 'Gold · v1.0', True), ('Python for Beginners', 'Published', 'green', '', False), ('Business Intelligence Basics', 'Published', 'green', '', False)]
P('ds-cr', 'My Creations',
  '''<header class="pg-h row ob-in"><div class="pg-hl"><h1 class="ds-h1">My Creations</h1></div><div class="pg-hr">%s</div></header>
<nav class="ft2 ob-in2" aria-label="Type"><a class="on" href="#">Courses</a><a href="#">Certifications</a><a href="#">Career Paths</a><a href="#">Learning Programs</a></nav>
<section class="ds-card mcl ob-in2"><div class="mcl-r mcl-hd"><span>Courses</span><span>Status</span><span>Validation</span><span></span></div>%s</section>''' % (
      btn('Create new', 'STU-001.dc.html', 'sm2'),
      ''.join('<div class="mcl-r%s"><span class="mcl-n"><span class="mcl-i">%s</span><b>%s</b></span>%s<span class="mcl-v">%s</span><span class="mcl-a">%s</span></div>' % (
          ' un' if u else '', ic('course', 17, 2), n, tag(s, t), ('<span class="gb sm">%s<span>%s</span></span>' % (ic('badge', 11, 2.2), v)) if v else '<span class="mcl-dash">—</span>',
          ('<a class="ds-ghost xs" href="MGT-DS-OV.dc.html">View Overview</a><a class="ds-ghost xs" href="MGT-001.dc.html">Manage</a><a class="ds-link sm" href="STU-009.dc.html">Edit</a>') if u else '<a class="ds-ghost xs" href="#">Open</a>') for n, s, t, v, u in ROWS)))

def manage_body():
    blocks = []
    for key, active, body in PAGES:
        blocks.append('<sc-if value="{{p_%s}}" hint-placeholder-val="{{ %s }}">\n%s\n</sc-if>' % (key.replace('-', '_'), 'true' if key == 'hub' else 'false', body))
    return '''<div class="ds-root cr-root">
%s
<div style="min-width: 0; display: flex; flex-direction: column">
%s
<main class="ds-main mg-main {{tone}}">
%s
</main>
</div>
</div>''' % (cr_side('My Creations'), CR_TOP, '\n'.join(blocks))
TONE = {'b': 'ok', 'c': 'ok', 'e': 'rd', 'f': 'am', 'g': 'rd', 'notice': 'rd', 'd': 'gy', 'ds-ov': 'gy'}
MANAGE_JS = W.js() + '''var PG = %s, TONE = %s;
class Component extends DCLogic {
  renderVals() {
    var pg = this.props.page || 'hub', v = togVals(this), self = this;
    PG.forEach(function (k) { v['p_'.concat(k.replace('-', '_'))] = k === pg; });
    v.tone = 'tn-'.concat(TONE[pg] || 'cb');
    v.navCls = this.state.nav ? 'ds-open' : '';
    v.toggleNav = function () { self.setState({ nav: !self.state.nav }); };
    return v;
  }
}''' % (json.dumps([p[0] for p in PAGES]), json.dumps(TONE))

# ======================================================================= UNPUBLISH (focus flow)
U = Toggles()
USTEPS = ['Review Impact', 'Select Reason', 'Confirm', 'Completed']
def uside(step, extra=''):
    li = ''.join('<li class="%s"><i></i><span>%s</span></li>' % ('dn' if i < step else ('on' if i == step else ''), s) for i, s in enumerate(USTEPS))
    return ('<aside class="cl-side ob-in"><span class="pb-k rd">Unpublish Course · Step %d of 4</span><h1 class="cl-h1">Data Analysis with SQL</h1><div class="cl-meta"><span class="ds-tag green">Published</span>%s</div>'
            '<p class="cl-pr">%s</p><ol class="cl-steps">%s</ol>%s</aside>') % (step + 1, '<span class="gb">%s<span>Gold Validated</span></span>' % ic('badge', 12, 2.2), PRICE, li, extra)
def upanel(h, p, body, foot):
    return '<section class="cl-panel ob-in2"><h2 class="cl-ph">%s</h2>%s%s<div class="cl-foot">%s</div></section>' % (h, ('<p class="cl-pp">%s</p>' % p) if p else '', body, foot)
def ubk(href, label='Back'):
    return '<a class="ds-ghost cl-bk2" href="%s">%s</a>' % (href, label)
IMP = [('248', 'Total enrolled', 'all'), ('86', 'Active DLP learners', 'dlp'), ('42', 'Lifetime purchasers', 'lt'), ('120', 'Completed learners', 'dn')]
ACCESS = ['Lifetime purchasers retain their existing course entitlement.', 'Current DLP learners continue according to their active access rights.', 'Completed achievements and verified credentials remain recorded.']
UN = {}
UN['impact'] = uside(0, '''<div class="cl-nx ea"><span>Existing Learner Access</span><p>Unpublishing stops new public access. It does not automatically remove access already granted to learners.</p><ul>%s</ul></div>''' % ''.join('<li>%s<span>%s</span></li>' % (ck(10), t) for t in ACCESS)) + upanel(
    'Unpublish Course', 'Review how removing this course from new enrollments will affect your learners.',
    '''<span class="dc-l">Learner Impact Overview%s</span><div class="im4">%s</div>
<span class="dc-l">Check Course Dependencies</span><p class="cl-pp sm">This course may be part of Career Paths, Certifications, Learning Programs or active organizational learning commitments.</p>
<div class="dep">%s</div><a class="ds-link sm dep-l" href="#">View Dependency Details%s</a>''' % (
        tip('Illustrative figures only; production must display actual course data. Figures are not mutually exclusive — a learner may appear in more than one count.'),
        ''.join('<span class="im %s" style="--i: %d"><b>%s</b><em>%s</em></span>' % (k, i, n, l) for i, (n, l, k) in enumerate(IMP)),
        ''.join('<div class="dep-r"><span class="dep-i">%s</span><b>%s</b>%s</div>' % (ic(i, 16, 2) if i in EXTRA or i in I else '', l, tag(v, 'amber')) for i, l, v in [('path', 'Dependent learning experiences', 'Review required'), ('users', 'Active cohorts or commitments', 'Check status')]),
        ic('arrowr', 13, 2.2)),
    ubk('MGT-002.dc.html', 'Cancel') + btn('Continue', 'MGT-003B.dc.html', 'cl-go'))
REASONS = [('Temporarily unavailable', 'Standard unpublish flow.'), ('Updating or improving course content', 'Offers a link to create or continue a draft revision.'),
           ('Course content is outdated', 'Credalio assesses whether existing learners need a notice.'), ('Discontinuing this course', 'Checks dependencies and long-term learner access obligations.'),
           ('Other reason', 'Capture explanation and apply normal checks.')]
kn = U.new(True)
UN['reason'] = uside(1, '''<div class="cl-nx np"><span>Learner notification preview</span><div class="np-ph"><span class="np-n"><span class="lg-m"></span><b>Credalio</b><em>now</em></span><p>“Data Analysis with SQL will no longer accept new enrollments. If you already have access, your learning experience remains available according to your existing entitlement.”</p></div></div>''') + upanel(
    'Why are you unpublishing?', 'Help us understand your decision and how existing learners should be supported.',
    '''<span class="dc-l">Reason for unpublishing</span><div class="rs2">%s</div>
<label class="fl rs-d"><span class="fl-l">Additional details</span><textarea class="ds-in" rows="2" aria-label="Additional details" placeholder="Pausing to refresh module 3 with updated SQL window-function examples..."></textarea></label>
<span class="dc-l">Existing Learner Transition</span><p class="cl-pp sm">What is your proposed approach for learners who already have access?</p><div class="rs2">%s%s</div>
<p class="tr-n">%s<span>Creators cannot independently revoke existing paid entitlements. Any exceptional transition requires review.</span></p>
<button type="button" class="dc-r {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}"><span class="dc-b">%s</span><span>Send an informational update to affected learners when appropriate</span></button>''' % (
        ''.join(U.opt('<span class="o-t"><b>%s</b><span>%s</span></span>' % (t, d), i == 0, 'why', 'sm rs') for i, (t, d) in enumerate(REASONS)),
        U.opt('<span class="o-t"><b>Maintain existing learner access under current entitlements</b></span>', True, 'tr', 'sm rs'),
        U.opt('<span class="o-t"><b>Request Credalio review of a special learner transition</b></span>', False, 'tr', 'sm rs'),
        ic('lock', 14, 2), kn, kn, kn, ck(12)),
    ubk('MGT-003A.dc.html') + btn('Review Confirmation', 'MGT-003C.dc.html', 'cl-go'))
DIFF = [('Current status', 'Published', 'Unpublished'), ('Marketplace visibility', 'Visible', 'Hidden'), ('New enrollments', 'Open', 'Closed'), ('Existing entitlements', 'Preserved', 'Preserved')]
WILL = [('eye', 'The course will be removed from public discovery and recommendations.'), ('lock', 'New DLP enrollments and lifetime purchases will stop.'),
        ('check', 'Existing learner rights, progress and verified achievements will be retained.'), ('course', 'The course and its historical records will remain in Creator Studio.')]
kc = U.new(False)
UN['confirm'] = uside(2, '''<div class="cl-nx wh"><span>What will happen</span><ul>%s</ul></div>''' % ''.join('<li><span class="wh-i">%s</span><span>%s</span></li>' % (ic(i, 14, 2.2), t) for i, t in WILL)) + upanel(
    'Confirm Course Unpublishing', 'You’re about to remove this course from new public availability. Review the changes before confirming.',
    '''<span class="dc-l">Review before unpublishing · Data Analysis with SQL</span><div class="df2">%s</div>
<button type="button" class="dc-r ack {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}"><span class="dc-b">%s</span><span>I understand that unpublishing stops new access but does not automatically revoke existing learner entitlements.</span></button>''' % (
        ''.join('<div class="df2-r%s"><span>%s</span><span class="df2-v"><s>%s</s>%s<b>%s</b></span></div>' % (' same' if a == b else '', l, a if a != b else '', ic('arrowr', 13, 2.4) if a != b else '', b) for l, a, b in DIFF),
        kc, kc, kc, ck(12)),
    ubk('MGT-003B.dc.html') + '<span class="cf-g {{c%s}}"><a class="ds-btn danger cl-go" href="MGT-003D.dc.html"><span>Confirm Unpublish</span></a></span>' % kc)
def emb(kind, icon):
    return '<div class="ko-emb ko-v %s" aria-hidden="true"><span class="ko-halo"></span><span class="ko-disc">%s</span></div>' % (kind, ic(icon, 28, 2.2))
UN['done'] = '''<div class="ko-wrap ob-in"><div class="ko gy">%s<span class="ko-pill">Unpublished</span><h1 class="ko-h1">Course Unpublished</h1><p class="ko-sub">Data Analysis with SQL is no longer available for new learners to discover or enroll in.</p>
<ol class="ko-st">%s</ol>
<section class="ko-card"><dl>%s</dl><div class="ko-pres"><span class="ko-pi">%s</span><span><b>Existing learner access</b><em>Preserved — 86 active DLP learners and 42 lifetime purchasers retain their current entitlements.</em></span></div></section>
<div class="ko-acts">%s<a class="ds-link" href="MGT-DS-OV.dc.html">View Course Overview</a></div></div></div>''' % (
    emb('gy', 'eye'), ''.join('<li class="dn"><i>%s</i><span>%s</span></li>' % (ck(10), s) for s in USTEPS),
    ''.join('<div><dt>%s</dt><dd>%s</dd></div>' % r for r in [('Publication status', 'Unpublished'), ('Marketplace', 'Hidden'), ('New enrollments', 'Closed')]), ic('check', 16, 2.4),
    btn('Return to Manage Course', 'MGT-002D.dc.html'))
BLK = [('Approval Required', 'Authorized organization approval is needed', 'amber', 'users'), ('Transition Plan Required', 'Existing learner/cohort obligations need a plan', 'amber', 'path'),
       ('Under Review', 'Credalio or organization is evaluating the request', 'blue', 'clock')]
UN['blocked'] = '''<div class="ko-wrap ob-in"><div class="ko am">%s<span class="ko-pill">Action needed</span><h1 class="ko-h1">Unpublishing Requires Review</h1><p class="ko-sub">This course has active learning commitments that need to be reviewed before its publication status can change.</p>
<section class="ko-card"><span class="ko-cl">Items requiring attention</span><ul class="ira">%s</ul><div class="irs">%s</div></section>
<div class="ko-acts">%s<a class="ds-link" href="MGT-003A.dc.html">Back</a></div></div></div>''' % (
    emb('am', 'lock'), ''.join('<li>%s<span>%s</span></li>' % (ic('warn', 15, 2.2), t) for t in ['An active Learning Program depends on this course.', 'Organization approval may be required.']),
    ''.join('<div class="irs-r"><span class="irs-i %s">%s</span><span><b>%s</b><em>%s</em></span><span class="irs-d %s"></span></div>' % (k, ic(i, 16, 2.2) if i in EXTRA or i in I else '', t, d, k) for t, d, k, i in BLK),
    btn('Review Requirements', '#'))

def un_body():
    blocks = []
    for k, h in UN.items():
        inner = h if k in ('done', 'blocked') else '<div class="cl">%s</div>' % h
        blocks.append('<sc-if value="{{s_%s}}" hint-placeholder-val="{{ %s }}">%s</sc-if>' % (k, 'true' if k == 'impact' else 'false', inner))
    return '''<div class="tk-root {{rootCls}}"><span class="cl-glow"></span>
<header class="tk-top"><a class="lp-x" href="MGT-002.dc.html" aria-label="Close">%s</a><span class="lp-title"><span class="lp-t1">Unpublish course</span></span><span style="flex-grow: 1"></span><a href="#" class="ds-tok" aria-label="72,450 Creio">%s<span>72.4K</span></a></header>
%s
</div>''' % (ic('x', 20, 2), COIN('tp', 26), '\n'.join(blocks))
UN_JS = U.js() + '''class Component extends DCLogic {
  renderVals() {
    var s = this.props.step || 'impact', v = togVals(this);
    %s.forEach(function (k) { v['s_'.concat(k)] = k === s; });
    v.rootCls = s === 'blocked' ? 'is-wait' : (s === 'done' ? 'is-gy' : 'is-rd');
    return v;
  }
}''' % json.dumps(list(UN))

# ======================================================================= LEARNER APP · My Learning (access states after unpublish)
LST = [('Active entitlement', 'ok', '62% complete · DLP access active', 'Continue Learning', 62, ''),
       ('Entitlement expired', 'am', 'Your DLP access period has ended. Renew to continue.', 'Renew Access', 0, 'Access Ended'),
       ('Special withdrawal', 'gy', 'A special access review applies to your enrollment.', 'View Details', 0, 'Access Restricted')]
def lcard(i, c):
    st, k, d, cta, pct, h = c
    body = ('<div class="lc2-p">%s<span><b>62%%</b><em>%s</em></span></div>' % (ring(62, 52, 12), d)) if k == 'ok' else '<div class="lc2-x"><b>%s</b><p>%s</p></div>' % (h, d)
    a = btn(cta, '#', 'sm2') if k == 'ok' else '<a class="ds-ghost sm" href="#">%s</a>' % cta
    return '<article class="lc2 %s" style="--i: %d"><span class="lc2-cv"><i>SQL</i><em></em><em></em><span class="lc2-s">%s<span>%s</span></span></span><div class="lc2-b"><b>Data Analysis with SQL</b>%s<div class="lc2-a">%s</div></div></article>' % (
        k, i, {'ok': ic('check', 12, 2.6), 'am': ic('clock', 12, 2.4), 'gy': ic('lock', 12, 2.4)}[k], st, body, a)
LEARN = '''<div class="la">
<header class="lh"><a class="lh-lg" href="#" aria-label="Credalio"><span class="lg-word"></span></a><nav class="lh-n"><a href="#">Browse</a><a href="#">Certifications</a><a href="#">Career Paths</a><a href="#" class="on">My Learning</a></nav><span style="flex-grow: 1"></span><span class="lh-tag">Learner app</span><span class="av" style="width: 36px; height: 36px">JM</span></header>
<main class="la-m"><span class="pg-e">My Learning</span><h1 class="ds-h1">My Learning — course-access states after unpublish</h1><p class="ds-sub">Three distinct learner-facing states, shown side by side for comparison.</p>
<div class="lc3">%s</div></main></div>''' % ''.join(lcard(i, c) for i, c in enumerate(LST))

# ======================================================================= CSS
SHARED = r'''.cv-t{position:relative;display:block;width:64px;height:64px;flex-shrink:0;border-radius:16px;overflow:hidden;background:radial-gradient(circle at 85% 15%,rgba(92,134,255,.85),rgba(92,134,255,0) 60%),linear-gradient(140deg,#1652F0,#0B1433);box-shadow:0 12px 24px -14px rgba(22,82,240,.8)}
.cv-t i{position:absolute;left:9px;bottom:7px;font-style:normal;font-size:15px;font-weight:600;color:#FFFFFF;letter-spacing:-0.02em}
.gb{display:inline-flex;align-items:center;gap:5px;height:26px;padding:0 10px;border-radius:999px;background:linear-gradient(135deg,#F7D98B,#C9952C);color:#3D2700;font-size:12px;font-weight:600;white-space:nowrap}
.gb.sm{height:22px;font-size:11.5px;padding:0 8px}
.ds-tag.red{background:#FDECEA;color:#B42318}
.lv-d{width:7px;height:7px;border-radius:50%;background:currentColor;box-shadow:0 0 0 0 currentColor;animation:lvP 2s ease-out infinite}
@keyframes lvP{0%{box-shadow:0 0 0 0 rgba(15,107,69,.5)}100%{box-shadow:0 0 0 7px rgba(15,107,69,0)}}
.cst-t{display:flex;flex-wrap:wrap;align-items:center;gap:6px}
.cst-p{display:inline-flex;align-items:center;flex-wrap:wrap;gap:5px;font-size:13.5px;color:#5B6582}
.cst-p .dlp-c,.cst-p .cr-c{width:16px;height:16px;font-size:9px;margin-left:4px}
.ds-btn.danger{background:#B42318;padding:0 26px;box-shadow:0 10px 24px rgba(180,35,24,.24)}
.ds-btn.danger:hover{background:#912018}
.ds-btn.sm2{height:44px;font-size:14.5px;padding-left:20px;gap:12px}
.ds-btn.sm2 .ob-arrow{width:34px;height:34px}
.lg-m{display:block;width:22px;height:22px;border-radius:7px;background:#FFFFFF url(MARK) center / 70% no-repeat}
'''.replace('MARK', MARK)

MANAGE_CSS = SHARED + r'''.cr-root{grid-template-columns:264px minmax(0,1fr)}
.cr-lg{display:block;padding:4px 10px 16px 10px}
.cr-lg .lg-word{height:24px}
.ci-t{flex-grow:1;min-width:0}
.ds-mlogo{flex-grow:1}
.ds-mlogo .lg-word{height:20px}
.fc{padding:24px 26px 26px 26px}
.fc-h{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-bottom:14px}
.fc-h h2{margin:0;display:flex;align-items:center;font-size:17px;font-weight:600;letter-spacing:-0.01em}
.bl-c{position:absolute;right:-3px;top:-3px;min-width:18px;height:18px;padding:0 4px;box-sizing:border-box;border-radius:999px;background:#E5484D;color:#FFFFFF;font-size:10.5px;font-weight:600;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 2px #F7F9FD}
.cw-me{display:flex;border-radius:50%}
.mg-main{position:relative;isolation:isolate;max-width:1240px}
.mg-main::before{content:'';position:absolute;z-index:-1;left:0;right:0;top:-80px;height:300px;pointer-events:none;background:radial-gradient(60% 100% at 30% 0,rgba(22,82,240,.07),transparent 70%)}
.mg-main:has(.ov-scrim){z-index:30}
.mg-main.tn-ok::before{background:radial-gradient(60% 100% at 30% 0,rgba(15,107,69,.09),transparent 70%)}
.mg-main.tn-am::before{background:radial-gradient(60% 100% at 30% 0,rgba(214,140,20,.11),transparent 70%)}
.mg-main.tn-rd::before{background:radial-gradient(60% 100% at 30% 0,rgba(217,45,32,.08),transparent 70%)}
.mg-main.tn-gy::before{background:radial-gradient(60% 100% at 30% 0,rgba(91,101,130,.08),transparent 70%)}
.bc{display:flex;align-items:center;flex-wrap:wrap;gap:4px;margin:4px 0 14px 0;font-size:13px;color:#8A93AD}
.bc a{color:#5B6582;text-decoration:none}
.bc a:hover{color:#1652F0}
.bc svg{color:#AEB6CC}
.bc span{color:#0B1433;font-weight:500}
.pg-h{display:flex;align-items:flex-end;justify-content:space-between;gap:24px}
.pg-hl{min-width:0}
.pg-hl .ds-back{margin-bottom:6px}
.pg-hr{flex-shrink:0;display:flex;align-items:center;gap:8px}
.ds-ghost.sm{height:42px;padding:0 16px;font-size:14px;gap:7px}
.ds-ghost.xs{height:34px;padding:0 12px;font-size:13px;border-width:1.5px}
.ds-link.sm{font-size:13.5px}
.sh{margin:28px 0 12px 0;font-size:17px;font-weight:600;letter-spacing:-0.01em}
.mh{margin-top:22px;padding:22px 24px 18px 24px}
.mh-t{display:flex;align-items:center;gap:18px}
.mh-t .cv-t{width:76px;height:76px;border-radius:20px}
.mh-b{flex:1;min-width:0;display:flex;flex-direction:column;gap:6px}
.mh-b h2{margin:2px 0 0 0;font-size:22px;font-weight:600;letter-spacing:-0.02em}
.mh-pu{flex-shrink:0;display:grid;grid-template-columns:auto auto;align-items:center;gap:4px 10px;padding:12px 16px;border-radius:16px;background:#FFF8EA;border:1.5px solid #F4DDAA}
.mh-pk{grid-column:1 / -1;font-size:12px;font-weight:500;color:#8A5A00}
.mh-pu b{font-size:14px;font-weight:600}
.mh-f{margin:18px 0 0 0;padding-top:16px;border-top:1.5px solid #F0F2F8;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px}
.mh-f dt{font-size:12px;color:#8A93AD}
.mh-f dd{margin:3px 0 0 0;display:flex;align-items:center;gap:6px;font-size:14px;font-weight:600}
.mh-f .dlp-c,.mh-f .cr-c{width:16px;height:16px;font-size:9px}
.ms4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.ms{display:flex;align-items:center;gap:14px;padding:16px 18px;border-radius:18px;background:#FFFFFF;border:1.5px solid #E6EAF3}
.ms-i{width:42px;height:42px;flex-shrink:0;border-radius:13px;display:flex;align-items:center;justify-content:center}
.ms.ok .ms-i{background:#E7F5EE;color:#0F6B45}
.ms.gold .ms-i{background:linear-gradient(135deg,#F7D98B,#C9952C);color:#3D2700}
.ms.am .ms-i{background:#FFF4E0;color:#B76E00}
.ms-b{display:flex;flex-direction:column;gap:1px;min-width:0}
.ms-b em{font-style:normal;font-size:12px;color:#8A93AD}
.ms-b b{display:flex;align-items:center;gap:7px;font-size:17px;font-weight:600}
.ms.ok .ms-b b{color:#0F6B45}
.ms.am .ms-b b{color:#8A5A00}
.ms-b > span{font-size:12.5px;color:#5B6582}
.mcs{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.mc{position:relative;display:flex;flex-direction:column;gap:6px;padding:18px;border-radius:20px;background:#FFFFFF;border:1.5px solid #E6EAF3;color:#0B1433;text-decoration:none;overflow:hidden;transition:transform .25s ease,border-color .25s ease,box-shadow .25s ease;animation:obIn .5s ease both;animation-delay:calc(var(--i) * 50ms + 200ms)}
.mc::after{content:'';position:absolute;inset:0;background:radial-gradient(240px 140px at 100% 0,rgba(22,82,240,.08),transparent 70%);opacity:0;transition:opacity .25s ease;pointer-events:none}
.mc:hover{transform:translateY(-3px);border-color:#AFC1F5;box-shadow:0 22px 40px -28px rgba(22,82,240,.6)}
.mc:hover::after{opacity:1}
.mc-i{width:40px;height:40px;margin-bottom:6px;border-radius:13px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center;transition:transform .3s cubic-bezier(.3,1.4,.5,1)}
.mc:hover .mc-i{transform:scale(1.08) rotate(-4deg)}
.mc b{font-size:15px;font-weight:600}
.mc p{flex:1;margin:0;font-size:13px;line-height:1.5;color:#5B6582}
.mc-a{margin-top:8px;display:inline-flex;align-items:center;gap:6px;font-size:13.5px;font-weight:600;color:#1652F0}
.mc-a svg{transition:transform .25s ease}
.mc:hover .mc-a svg{transform:translateX(3px)}
.mc-d{position:absolute;top:18px;right:18px;width:9px;height:9px;border-radius:50%;background:#E0A030;box-shadow:0 0 0 4px #FFF4E0}
.mc.warn .mc-i{background:#FDECEA;color:#B42318}
.mc.warn .mc-a{color:#B42318}
.mc.warn:hover{border-color:#F5C2BD;box-shadow:0 22px 40px -28px rgba(180,35,24,.5)}
.bn2{position:relative;overflow:hidden;margin-top:18px;display:flex;align-items:flex-start;gap:14px;padding:16px 18px;border-radius:18px;border:1.5px solid}
.bn2 > div{flex:1;min-width:0}
.bn2 b{display:block;font-size:15.5px;font-weight:600}
.bn2 p{margin:3px 0 0 0;font-size:14px;line-height:1.55}
.bn2-i{width:38px;height:38px;flex-shrink:0;border-radius:12px;display:flex;align-items:center;justify-content:center;color:#FFFFFF}
.bn2.ok{background:#F2FAF5;border-color:#CFE8DB}.bn2.ok .bn2-i{background:#0F6B45}.bn2.ok p{color:#2C5240}
.bn2.am{background:#FFF8EA;border-color:#F4DDAA}.bn2.am .bn2-i{background:#B76E00}.bn2.am p{color:#6B4A00}
.bn2.rd{background:#FFF5F4;border-color:#F5C2BD}.bn2.rd .bn2-i{background:#B42318}.bn2.rd p{color:#7A271A}
.bn2-g{position:absolute;inset:0;background:linear-gradient(100deg,transparent 30%,rgba(255,255,255,.7) 50%,transparent 70%);background-size:250% 100%;animation:bnSh 2.6s ease .4s 1 both;pointer-events:none}
@keyframes bnSh{from{background-position:150% 0}to{background-position:-100% 0}}
.wk{margin-top:18px}
.cst{display:flex;align-items:center;gap:16px;padding:16px 18px}
.cst-b{flex:1;min-width:0;display:flex;flex-direction:column;gap:6px}
.cst-b > b{font-size:17px;font-weight:600}
.pv2{padding:20px}
.sws{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.sw{position:relative;display:flex;flex-direction:column;gap:8px;padding:16px;border-radius:18px;background:#F7F9FD;overflow:hidden}
.sw-l{font-size:12.5px;font-weight:500;color:#5B6582}
.sw-v{display:flex;align-items:center;gap:10px}
.sw-i{width:32px;height:32px;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#FFFFFF}
.sw-v b{font-size:19px;font-weight:600;letter-spacing:-0.01em}
.sw.lg .sw-v b{font-size:15.5px}
.sw p{margin:0;font-size:12.5px;line-height:1.5;color:#5B6582}
.sw-tr{position:absolute;right:14px;top:14px;width:34px;height:20px;border-radius:999px;background:#D6DDEE}
.sw-tr i{position:absolute;top:3px;left:3px;width:14px;height:14px;border-radius:50%;background:#FFFFFF;box-shadow:0 1px 3px rgba(11,20,51,.25);transition:left .3s ease}
.sw.ok .sw-i{background:#0F6B45}.sw.ok .sw-tr{background:#0F6B45}.sw.ok .sw-tr i{left:17px}.sw.ok b{color:#0F6B45}
.sw.am{background:#FFF8EA}.sw.am .sw-i{background:#B76E00}.sw.am .sw-tr{background:#E0A030}.sw.am b{color:#8A5A00}
.sw.gy .sw-i{background:#8A93AD}.sw.gy b{color:#3A4566}
.sw.rd{background:#FFF5F4}.sw.rd .sw-i{background:#B42318}.sw.rd b{color:#B42318}.sw.rd .sw-tr{display:none}
.sw.gy .sw-tr{background:repeating-linear-gradient(45deg,#E6EAF3 0 4px,#F1F3F8 4px 8px)}
.pv2-a{margin-top:16px;padding-top:16px;border-top:1.5px solid #F0F2F8;display:flex;align-items:center;gap:18px}
.dz{display:flex;align-items:center;gap:16px;padding:18px 20px;border-color:#F5D3CE;background:linear-gradient(120deg,#FFFAF9,#FFFFFF 60%)}
.dz-i{width:44px;height:44px;flex-shrink:0;border-radius:14px;background:#FDECEA;color:#B42318;display:flex;align-items:center;justify-content:center}
.dz-b{flex:1;min-width:0}
.dz-b b{font-size:15.5px;font-weight:600}
.dz-b p{margin:3px 0 0 0;font-size:13.5px;line-height:1.5;color:#5B6582}
.dz-n{margin-top:8px;display:inline-flex;align-items:center;gap:6px;font-size:12.5px;font-weight:500;color:#8A93AD}
.dz-a{color:#B42318;border-color:#F5C2BD}
.dz-a:hover{border-color:#B42318;background:#FFF5F4;color:#912018}
.lap p{margin:0 0 12px 0;font-size:13.5px;line-height:1.5;color:#3A4566}
.lap-n{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.lap-n span{display:flex;flex-direction:column;gap:2px;padding:12px;border-radius:14px;background:#F2FAF5}
.lap-n b{font-size:24px;font-weight:600;letter-spacing:-0.02em;color:#0F6B45}
.lap-n em{font-style:normal;font-size:12px;color:#2C5240}
.lap .rx-p{margin:12px 0 10px 0}
.lap .ds-link,.mk-l a{display:inline-flex;align-items:center;gap:5px}
.ph2-h{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px}
.ph2-h .rx-k{margin:0}
.ph2 ol{list-style:none;margin:0;padding:0;position:relative}
.ph2 ol::before{content:'';position:absolute;left:5px;top:8px;bottom:8px;width:2px;background:#E6EAF3}
.ph2 li{position:relative;display:flex;gap:12px;padding:6px 0}
.ph2-d{position:relative;z-index:1;width:12px;height:12px;flex-shrink:0;margin-top:3px;box-sizing:border-box;border-radius:50%;border:3px solid #FFFFFF;background:#0F6B45;box-shadow:0 0 0 1.5px #CFE8DB}
.ph2 li > span:last-child{display:flex;flex-direction:column;gap:2px}
.ph2 em{font-style:normal;font-size:11.5px;color:#8A93AD}
.ph2 b{font-size:13.5px;font-weight:500}
.ov-scrim{position:fixed;inset:0;z-index:1000;background:rgba(11,20,51,.38);backdrop-filter:blur(2px);-webkit-backdrop-filter:blur(2px)}
.dl{position:fixed;z-index:1001;left:50%;top:50%;transform:translate(-50%,-50%);width:560px;max-width:calc(100vw - 32px);max-height:calc(100vh - 48px);overflow-y:auto;box-sizing:border-box;border-radius:24px;background:#FFFFFF;box-shadow:0 40px 90px -30px rgba(11,20,51,.5);animation:dlIn .45s cubic-bezier(.2,.9,.3,1.2) both}
@keyframes dlIn{from{opacity:0;transform:translate(-50%,-46%) scale(.97)}}
.dl-h{position:relative;display:flex;flex-direction:column;align-items:center;gap:14px;padding:28px 56px 0 56px;text-align:center}
.dl-h > .ds-x{position:absolute;top:14px;right:14px}
.dl-ht{min-width:0;display:flex;flex-direction:column;align-items:center}
.dl-k{font-size:12.5px;font-weight:500;color:#1652F0}
.dl-h h2{margin:4px 0 0 0;font-size:21px;line-height:1.3;font-weight:600;letter-spacing:-0.015em}
.dl-i{width:46px;height:46px;flex-shrink:0;border-radius:15px;background:#EAF0FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.dl-i.am{background:#FFF4E0;color:#B76E00}
.ds-x.sm{width:36px;height:36px;border-color:transparent;color:#5B6582}
.dl-b{padding:14px 24px 4px 24px;display:flex;flex-direction:column;gap:8px}
.dl-p{margin:0 0 4px 0;text-align:center;font-size:14.5px;line-height:1.55;color:#3A4566}
.dl-l{margin-top:8px;font-size:12.5px;font-weight:600;color:#8A93AD}
.av-g{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.ds-opt.avo{align-items:flex-start;padding:14px}
.ds-opt.avo .o-t b{font-size:14.5px;font-weight:600}
.ds-opt.avo .o-t span{font-size:12.5px;line-height:1.45;color:#5B6582}
.o-t{display:flex;flex-direction:column;gap:3px;min-width:0}
.dl-n{margin:8px 0 0 0;display:flex;gap:10px;padding:12px 14px;border-radius:14px;background:#F7F9FD;font-size:13.5px;line-height:1.5;color:#3A4566}
.dl-n svg{flex-shrink:0;margin-top:2px;color:#1652F0}
.dl-n b{font-weight:600;margin-right:4px;color:#0B1433}
.dl-f{display:flex;justify-content:center;gap:10px;padding:20px 24px 24px 24px}
.dif{display:flex;flex-direction:column;border:1.5px solid #E6EAF3;border-radius:16px;padding:2px 16px}
.dif-r{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:12px 0;border-top:1.5px solid #F0F2F8;font-size:14px}
.dif-r:first-child{border-top:0}
.dif-r > span{color:#5B6582}
.dif-r b{display:inline-flex;align-items:center;gap:6px;font-weight:600}
.dif-r i{display:flex;color:#AEB6CC}
.dif-r em{font-style:normal;color:#8A5A00;background:#FFF4E0;padding:2px 9px;border-radius:999px}
.dif-r.ok b{color:#0F6B45}
.rn2{padding:20px 22px}
.rn2-h{display:flex;align-items:center;gap:14px}
.rn2-h > div{display:flex;flex-direction:column;align-items:flex-start;gap:6px}
.rn2-h .rx-k{margin:0}
.rn2-i{width:48px;height:48px;border-radius:15px;background:#B42318;color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 12px 24px -12px rgba(180,35,24,.7)}
.rn2-r{margin-top:16px;padding:14px 16px;border-radius:14px;background:#FFF5F4;display:flex;flex-direction:column;gap:3px}
.rn2-r span{font-size:12px;color:#B42318;font-weight:500}
.rn2-r b{font-size:15.5px;font-weight:600}
.rn2-g{margin:14px 0 0 0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}
.rn2-g dt{font-size:12px;color:#8A93AD}
.rn2-g dd{margin:3px 0 0 0;font-size:14px;font-weight:600}
.af4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}
.af{display:flex;flex-direction:column;gap:4px;padding:16px;border-radius:18px;background:#FFFFFF;border:1.5px solid #E6EAF3;animation:obIn .5s ease both;animation-delay:calc(var(--i) * 70ms + 200ms)}
.af-i{width:34px;height:34px;margin-bottom:6px;border-radius:11px;display:flex;align-items:center;justify-content:center}
.af.am .af-i{background:#FFF4E0;color:#B76E00}.af.gy .af-i{background:#F1F3F8;color:#5B6582}.af.ok .af-i{background:#E7F5EE;color:#0F6B45}
.af em{font-style:normal;font-size:12.5px;color:#5B6582}
.af b{font-size:15px;font-weight:600}
.af.ok b{color:#0F6B45}
.wcd p{margin:0;font-size:13.5px;line-height:1.55;color:#3A4566}
.wk-r .wcd-a{flex-direction:column;align-items:stretch;gap:8px}
.wk-r .wcd-a .ds-btn{justify-content:space-between}
.wk-r .wcd-a .ds-ghost,.wk-r .wcd-a .ds-link{justify-content:center}
.wk-r > .wcd{order:2}
.wcd-a{margin-top:16px;display:flex;align-items:center;flex-wrap:wrap;gap:12px 16px}
.wk > .wk-m > .wcd{margin-top:16px}
.nx4 ol{list-style:none;margin:0;padding:0;position:relative;display:flex;flex-direction:column;gap:4px}
.nx4 ol::before{content:'';position:absolute;left:13px;top:14px;bottom:14px;width:2px;background:repeating-linear-gradient(180deg,#CBD3E6 0 4px,transparent 4px 8px)}
.nx4 li{position:relative;display:flex;align-items:center;gap:12px;min-height:46px;animation:obIn .5s ease both;animation-delay:calc(var(--i) * 100ms + 250ms)}
.nx-n{position:relative;z-index:1;width:28px;height:28px;flex-shrink:0;border-radius:50%;background:#FFFFFF;border:2px solid #CBD3E6;color:#5B6582;font-size:12.5px;font-weight:600;display:flex;align-items:center;justify-content:center;box-sizing:border-box}
.nx4 li.on .nx-n{border-color:#B42318;background:#B42318;color:#FFFFFF;box-shadow:0 0 0 5px #FDECEA}
.nx4 li:last-child .nx-n{border-color:#0F6B45;color:#0F6B45}
.nx4 b{font-size:14px;font-weight:500}
.nx4 li.on b{font-weight:600}
.ds-back{margin-left:-10px}
.ovh{margin-top:8px;display:flex;align-items:center;gap:16px}
.ovh-i{width:56px;height:56px;flex-shrink:0;border-radius:16px;background:#8A93AD;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.ovh-t{flex:1;min-width:0;display:flex;flex-direction:column;gap:8px}
.ovh-v{font-size:13px;color:#5B6582}
.ovh-a{flex-shrink:0;display:flex;align-items:center;gap:8px}
.up2{margin-top:22px;display:grid;grid-template-columns:240px minmax(0,1fr);gap:28px;align-items:center;padding:26px 28px;background:linear-gradient(120deg,#F7F9FD,#FFFFFF 55%)}
.up2-v{position:relative;height:150px;border-radius:20px;background:repeating-linear-gradient(135deg,#F1F3F8 0 10px,#F7F9FD 10px 20px);display:flex;align-items:center;justify-content:center;overflow:hidden}
.up2-c .cv-t{width:96px;height:96px;border-radius:24px;filter:grayscale(.85);opacity:.7}
.up2-x{position:absolute;width:150%;height:3px;background:#8A93AD;transform:rotate(-24deg);border-radius:3px;animation:upX .8s cubic-bezier(.2,.8,.2,1) .4s both;transform-origin:center}
@keyframes upX{from{width:0}}
.up2-b > b{display:block;font-size:19px;font-weight:600;letter-spacing:-0.01em}
.up2-b p{margin:8px 0 0 0;font-size:14.5px;line-height:1.6;color:#3A4566}
.up2-s{margin:16px 0 14px 0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px}
.up2-s > span{display:flex;align-items:center;gap:8px;padding:10px 12px;border-radius:14px;background:#FFFFFF;border:1.5px solid #E6EAF3}
.up2-s > span > svg{flex-shrink:0}
.up2-s .gy > svg{color:#8A93AD}.up2-s .ok > svg{color:#0F6B45}.up2-s .gold > svg{color:#B07A12}
.up2-s span span{display:flex;flex-direction:column}
.up2-s em{font-style:normal;font-size:11.5px;color:#8A93AD}
.up2-s b{font-size:13px;font-weight:600}
.ft2{margin-top:18px;display:flex;gap:24px;border-bottom:1.5px solid #E6EAF3}
.ft2 a{height:42px;display:inline-flex;align-items:center;margin-bottom:-1.5px;border-bottom:2.5px solid transparent;color:#5B6582;font-size:14.5px;font-weight:500;text-decoration:none}
.ft2 a.on{color:#0B1433;font-weight:600;border-bottom-color:#1652F0}
.mcl{margin-top:18px;padding:6px 18px}
.mcl-r{display:grid;grid-template-columns:minmax(0,1fr) 140px 150px 330px;align-items:center;gap:14px;padding:14px 0;border-top:1.5px solid #F0F2F8}
.mcl-r:first-child{border-top:0}
.mcl-hd{font-size:12.5px;font-weight:500;color:#8A93AD;padding:10px 0}
.mcl-n{display:flex;align-items:center;gap:12px;min-width:0}
.mcl-i{width:38px;height:38px;flex-shrink:0;border-radius:11px;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.mcl-n b{font-size:15px;font-weight:600}
.mcl-r.un .mcl-i{background:#8A93AD}
.mcl-r.un{margin:0 -10px;padding:14px 10px;border-radius:14px;background:#F7F9FD}
.mcl-r .ds-tag{justify-self:start}
.mcl-dash{color:#AEB6CC}
.mcl-a{display:flex;align-items:center;justify-content:flex-end;gap:8px}
@media (max-width: 1180px){.mcs{grid-template-columns:repeat(2,minmax(0,1fr))}.mh-f{grid-template-columns:repeat(3,minmax(0,1fr))}.ms4{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width: 960px){
.cr-root{grid-template-columns:minmax(0,1fr)}
.bc{margin-bottom:10px;font-size:12px}
.pg-h{flex-direction:column;align-items:flex-start;gap:12px}
.pg-h.row{flex-direction:row;align-items:center;justify-content:space-between}
.pg-h.row .pg-hr{width:auto;margin:0;padding:0}
.fc{padding:18px 16px 20px 16px;border-radius:18px}
.pg-hr{width:calc(100% + 32px);margin:0 -16px;padding:0 16px 2px 16px;overflow-x:auto;scrollbar-width:none}
.pg-hr::-webkit-scrollbar{display:none}
.pg-hr > *{flex-shrink:0}
.ds-ghost.sm{height:38px;font-size:13.5px;padding:0 14px}
.sh{margin:22px 0 10px 0;font-size:16px}
.mh{padding:16px}
.mh-t{flex-wrap:wrap;gap:14px}
.mh-t .cv-t{width:56px;height:56px;border-radius:16px}
.mh-b{flex-basis:calc(100% - 70px)}
.mh-b h2{font-size:18px}
.mh-pu{width:100%;box-sizing:border-box;grid-template-columns:minmax(0,1fr) auto}
.mh-f{grid-template-columns:repeat(2,minmax(0,1fr));gap:12px 10px}
.mh-f div:first-child{grid-column:1 / -1}
.ms4{display:flex;overflow-x:auto;margin:0 -16px;padding:0 16px 4px 16px;gap:10px;scrollbar-width:none;scroll-snap-type:x mandatory}
.ms4::-webkit-scrollbar{display:none}
.ms{flex:0 0 68%;box-sizing:border-box;scroll-snap-align:start;padding:14px}
.mcs{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.mc{padding:14px;border-radius:18px}
.mc-i{width:36px;height:36px;margin-bottom:4px}
.mc b{font-size:14px;line-height:1.3}
.mc p{display:none}
.mc-a{margin-top:6px;font-size:12.5px}
.mc-d{top:14px;right:14px}
.bn2{padding:14px;gap:12px}
.bn2-i{width:34px;height:34px}
.bn2 b{font-size:15px}
.bn2 p{font-size:13.5px}
.cst{padding:14px;gap:12px;align-items:flex-start}
.cst .cv-t{width:48px;height:48px;border-radius:13px}
.pv2{padding:14px}
.sws{grid-template-columns:minmax(0,1fr);gap:8px}
.sw{display:grid;grid-template-columns:minmax(0,1fr) auto;align-items:center;gap:4px 10px;padding:14px}
.sw-l{grid-column:1}
.sw-v{grid-column:1}
.sw p{grid-column:1 / -1;display:none}
.sw-tr{position:relative;right:auto;top:auto;grid-column:2;grid-row:1 / span 2}
.sw{padding:12px 14px}
.sw-v b{font-size:16.5px}
.sw-i{width:28px;height:28px}
.pv2-a{flex-direction:column;align-items:stretch;gap:10px}
.pv2-a .ds-btn{justify-content:space-between}
.pv2-a .ds-link{justify-content:center;min-height:40px}
.dz{flex-wrap:wrap;padding:16px}
.dz-b{flex-basis:calc(100% - 60px)}
.dz-a{width:100%}
.wk-r > .lap{order:3}
.wk-r > .ph2{order:4}
.dl{top:auto;bottom:0;left:0;right:0;transform:none;width:100%;max-width:none;max-height:92vh;border-radius:24px 24px 0 0;animation:dlUp .45s cubic-bezier(.2,.9,.3,1) both}
@keyframes dlUp{from{transform:translateY(40px);opacity:0}}
.dl-h{padding:24px 52px 0 52px}
.dl-b{padding:12px 16px 4px 16px}
.av-g{grid-template-columns:minmax(0,1fr)}
.dl-f{padding:16px;flex-direction:column-reverse}
.dl-f .ds-btn{position:relative;justify-content:center}
.dl-f .ds-btn .ob-arrow{position:absolute;right:5px;top:50%;margin:0;transform:translateY(-50%)}
.rn2{padding:16px}
.rn2-g{grid-template-columns:repeat(2,minmax(0,1fr))}
.af4{grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.af{padding:14px}
.wcd-a{flex-direction:column;align-items:stretch}
.wcd-a .ds-btn{justify-content:space-between}
.wcd-a .ds-ghost,.wcd-a .ds-link{justify-content:center}
.wk-r > .nx4{order:3}
.wk-r > .wcd{order:4}
.ovh{flex-wrap:wrap;gap:12px}
.ovh-i{width:48px;height:48px}
.ovh-t{flex-basis:calc(100% - 64px)}
.ovh-a{width:100%;flex-wrap:wrap}
.ovh-a .ds-btn{order:-1;width:100%;justify-content:space-between}
.ovh-a .ds-ghost{flex:1}
.up2{grid-template-columns:minmax(0,1fr);gap:16px;padding:16px}
.up2-v{height:110px}
.up2-s{grid-template-columns:repeat(2,minmax(0,1fr))}
.ft2{overflow-x:auto;scrollbar-width:none;gap:20px}
.ft2 a{flex-shrink:0}
.mcl{padding:2px 14px}
.mcl-hd{display:none}
.mcl-r{grid-template-columns:minmax(0,1fr) auto;gap:8px 10px}
.mcl-r.un{margin:0 -8px;padding:14px 8px}
.mcl-r .ds-tag{grid-column:2;grid-row:1;justify-self:end}
.mcl-v{grid-column:1;padding-left:50px}
.mcl-v:has(.mcl-dash){display:none}
.mcl-a{grid-column:1 / -1;justify-content:flex-start;padding-left:50px;flex-wrap:wrap}
.mcl-r:not(.un) .mcl-a{display:none}
}

.pv2-h{display:flex;align-items:center;gap:16px;padding-bottom:18px;margin-bottom:18px;border-bottom:1.5px solid #F0F2F8}
.pv2-h .cst-b{flex:1;min-width:0;display:flex;flex-direction:column;gap:6px}
.pv2-h .cst-b > b{font-size:17px;font-weight:600}
.pv2-l{flex-shrink:0}
.pv2-a{border-top:0;padding-top:0;margin-top:16px}
.sw{animation:obIn .5s ease both;animation-delay:calc(var(--i) * 90ms + 150ms)}
.sw-tr i{animation:swK .6s cubic-bezier(.3,1.4,.5,1) both;animation-delay:calc(var(--i) * 90ms + 450ms)}
@keyframes swK{from{left:3px}}
.sw.gy .sw-tr i{animation:none}
.sw-pd{position:absolute;right:16px;top:18px;width:9px;height:9px;border-radius:50%;background:#0F6B45;animation:lvP 2s ease-out infinite}
.sw.gy .sw-pd{background:#8A93AD;animation:none}
.sw.rd .sw-pd{background:#B42318;animation:rdP 2s ease-out infinite}
@keyframes rdP{0%{box-shadow:0 0 0 0 rgba(180,35,24,.45)}100%{box-shadow:0 0 0 7px rgba(180,35,24,0)}}
.sw.gy:not(:first-child)::after{content:'';position:absolute;inset:0;background:repeating-linear-gradient(135deg,rgba(203,211,230,.18) 0 8px,transparent 8px 16px);pointer-events:none}
.mh-t .cv-t::after,.pv2-h .cv-t::after{content:'';position:absolute;inset:0;background:linear-gradient(115deg,transparent 35%,rgba(255,255,255,.45) 50%,transparent 65%);background-size:250% 100%;animation:cvSh 4s ease-in-out 1s infinite}
@keyframes cvSh{0%{background-position:150% 0}50%,100%{background-position:-100% 0}}
@media (max-width: 960px){
.bc:has(+ .pg-h .ds-back){display:none}
.hub-a{display:grid !important;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;width:100% !important;margin:0 !important;padding:0 !important;overflow:visible !important}
.hub-a .ds-ghost{flex-direction:column;height:auto;min-height:62px;padding:10px 6px;gap:5px;font-size:12.5px;line-height:1.25;white-space:normal;text-align:center;border-radius:16px}
.mh-t{display:grid;grid-template-columns:56px minmax(0,1fr);column-gap:14px;row-gap:6px;align-items:center}
.mh-t .cv-t{grid-row:1 / span 2}
.mh-b{display:contents}
.mh-b .cst-t{grid-column:2;grid-row:1;align-self:end}
.mh-b h2{grid-column:2;grid-row:2;align-self:start;margin:0}
.mh-b .cst-p{grid-column:1 / -1;grid-row:3;margin-top:6px;font-size:13px}
.mh-pu{grid-column:1 / -1;grid-row:4;margin-top:8px;grid-template-columns:minmax(0,1fr) auto;padding:10px 12px}
.mh-pu b{font-size:13.5px}
.mh-f{margin-top:14px;padding-top:12px}
.ms4{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;margin:0;padding:0;overflow:visible}
.ms{flex:none;padding:12px;gap:10px;border-radius:16px}
.ms-i{width:34px;height:34px;border-radius:11px}
.ms-b b{font-size:15px}
.ms-b > span{display:none}
.pv2-h{display:grid;grid-template-columns:48px minmax(0,1fr);column-gap:12px;row-gap:6px;padding-bottom:14px;margin-bottom:14px}
.pv2-h .cv-t{width:48px;height:48px;border-radius:13px;grid-row:1 / span 2}
.pv2-h .cst-b{display:contents}
.pv2-h .cst-b > b{grid-column:2;grid-row:1;align-self:end;font-size:16px}
.pv2-h .cst-t{grid-column:2;grid-row:2;align-self:start}
.pv2-h .cst-p{grid-column:1 / -1;grid-row:3;margin-top:4px;font-size:12.5px}
.pv2-l{grid-column:1 / -1;grid-row:4;margin-top:6px;justify-content:center}
.sws{gap:0;border-radius:16px;background:#F7F9FD;overflow:hidden}
.sw{border-radius:0;background:none !important;padding:12px 14px}
.sw + .sw{border-top:1.5px solid #EEF1F7}
.sw.am{background:#FFF8EA !important}.sw.rd{background:#FFF5F4 !important}
.sw-pd{position:static;grid-column:2;grid-row:1 / span 2;margin-right:12px}
.sw-l{font-size:12px}
.pv2-a{margin-top:14px}
.pv2-a .ds-btn{width:100%}
.dz{display:grid;grid-template-columns:40px minmax(0,1fr);gap:4px 12px;align-items:center}
.dz-i{width:40px;height:40px;border-radius:12px}
.dz-b{display:contents}
.dz-b b{grid-column:2;grid-row:1}
.dz-b p,.dz-n{grid-column:1 / -1}
.dz-b p{margin-top:6px}
.dz-n{margin-top:4px}
.dz-a{grid-column:1 / -1;margin-top:10px}
.cst{display:grid;grid-template-columns:48px minmax(0,1fr)}
.hub-a .ds-ghost{justify-content:flex-start;padding-top:12px;height:64px;min-height:0}
.sw.gy .sw-tr{display:none}
.mcs{display:flex;flex-direction:column;gap:0;border-radius:18px;background:#FFFFFF;border:1.5px solid #E6EAF3;overflow:hidden}
.mc{flex-direction:row;align-items:center;gap:12px;padding:12px 14px;border:0;border-radius:0;background:none;box-shadow:none !important;transform:none !important}
.mc + .mc{border-top:1.5px solid #F0F2F8}
.mc-i{margin:0;width:36px;height:36px;flex-shrink:0}
.mc b{flex:1;font-size:14.5px}
.mc-a{margin:0;font-size:0;gap:0}
.mc-a svg{width:16px;height:16px;color:#AEB6CC}
.mc.warn .mc-a svg{color:#B42318}
.mc-d{position:static;order:2;flex-shrink:0}
.mc::after{display:none}
}
'''

UN_CSS = open(os.path.join(HERE, 'submit_base.css')).read() + SHARED + r'''
.is-rd .cl-glow{background:radial-gradient(60% 100% at 50% 0,rgba(217,45,32,.07),transparent 70%)}
.is-gy .cl-glow{background:radial-gradient(60% 100% at 50% 0,rgba(91,101,130,.09),transparent 70%)}
.cl{grid-template-columns:minmax(0,1fr) 620px}
.pb-k{font-size:13px;font-weight:600;color:#1652F0}
.pb-k.rd{color:#B42318}
.cl-meta{align-items:center}
.cl-meta .ds-tag{height:28px}
.cl-meta .gb{background:linear-gradient(135deg,#F7D98B,#C9952C) !important;color:#3D2700 !important;font-weight:600 !important;padding:0 10px !important}
.cl-meta .gb span{background:none !important;padding:0 !important;height:auto !important;color:inherit !important;font-weight:600 !important}
.cl-meta .ds-tag.green{background:#E7F5EE !important;color:#0F6B45 !important}
.cl-pr{margin:10px 0 0 0;display:flex;align-items:center;flex-wrap:wrap;gap:4px;font-size:13.5px;color:#5B6582}
.cl-pr .dlp-c,.cl-pr .cr-c{width:16px;height:16px;font-size:9px;margin-left:4px}
.cl-steps{max-width:440px}
.cl-steps .on i{background:#B42318}
.cl-nx > span{display:block;margin-bottom:10px;font-size:12.5px;font-weight:500;color:#8A93AD}
.cl-nx p{margin:0;font-size:13.5px;line-height:1.55;color:#3A4566}
.ea ul,.wh ul{list-style:none;margin:12px 0 0 0;padding:0;display:flex;flex-direction:column;gap:10px}
.ea li,.wh li{display:grid;grid-template-columns:22px minmax(0,1fr);gap:10px;font-size:13.5px;line-height:1.5;color:#3A4566}
.ea li svg{margin-top:3px;width:22px;height:22px;padding:6px;box-sizing:border-box;border-radius:50%;background:#E7F5EE;color:#0F6B45}
.wh-i{width:22px;height:22px;border-radius:50%;background:#F1F3F8;color:#5B6582;display:flex;align-items:center;justify-content:center;margin-top:1px}
.wh li:nth-child(3) .wh-i,.wh li:nth-child(4) .wh-i{background:#E7F5EE;color:#0F6B45}
.dc-l{display:flex;align-items:center;margin:20px 0 10px 0;font-size:12.5px;font-weight:500;color:#8A93AD}
.cl-pp.sm{margin:-4px 0 10px 0;font-size:13.5px}
.im4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px}
.im{position:relative;display:flex;flex-direction:column;gap:2px;padding:14px 12px;border-radius:16px;background:#F7F9FD;overflow:hidden;animation:obIn .5s ease both;animation-delay:calc(var(--i) * 80ms + 200ms)}
.im::after{content:'';position:absolute;left:0;right:0;bottom:0;height:4px;background:var(--c,#CBD3E6)}
.im.all{--c:#0B1433}.im.dlp{--c:#E0A030}.im.lt{--c:#1652F0}.im.dn{--c:#0F6B45}
.im b{font-size:26px;font-weight:600;letter-spacing:-0.02em}
.im em{font-style:normal;font-size:12px;line-height:1.35;color:#5B6582}
.dep{display:flex;flex-direction:column;border:1.5px solid #E6EAF3;border-radius:16px;padding:2px 14px}
.dep-r{display:flex;align-items:center;gap:12px;min-height:54px;border-top:1.5px solid #F0F2F8}
.dep-r:first-child{border-top:0}
.dep-i{width:32px;height:32px;flex-shrink:0;border-radius:10px;background:#FFF4E0;color:#B76E00;display:flex;align-items:center;justify-content:center}
.dep-r b{flex:1;font-size:14px;font-weight:500}
.dep-l{display:inline-flex;align-items:center;gap:5px;margin-top:10px}
.rs2{display:flex;flex-direction:column;gap:8px}
.ds-opt.rs{padding:12px 14px;border-radius:14px}
.ds-opt.rs .o-t b{font-size:14.5px;font-weight:600}
.ds-opt.rs .o-t span{font-size:12.5px;color:#5B6582}
.o-t{display:flex;flex-direction:column;gap:2px;min-width:0}
.rs-d{margin-top:14px}
.rs-d textarea.ds-in{min-height:64px}
.tr-n{margin:10px 0 0 0;display:flex;align-items:center;gap:8px;font-size:12.5px;color:#5B6582}
.tr-n svg{flex-shrink:0;color:#8A93AD}
.dc-r{margin-top:12px;width:100%;display:flex;align-items:flex-start;gap:12px;padding:13px 14px;border-radius:14px;border:1.5px solid #E6EAF3;background:#FFFFFF;font-family:inherit;font-size:14px;line-height:1.5;color:#0B1433;text-align:left;cursor:pointer;transition:border-color .2s ease,background .2s ease}
.dc-b{width:20px;height:20px;flex-shrink:0;margin-top:1px;box-sizing:border-box;border-radius:6px;border:1.5px solid #CBD3E6;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.dc-b svg{opacity:0;transform:scale(.6);transition:opacity .2s ease,transform .2s ease}
.dc-r.on{border-color:#1652F0;background:#F5F8FF}
.dc-r.on .dc-b{border-color:#1652F0;background:#1652F0}
.dc-r.on .dc-b svg{opacity:1;transform:none}
.dc-r.ack{margin-top:16px}
.np-ph{padding:14px;border-radius:18px;background:#0B1433;box-shadow:0 20px 40px -26px rgba(11,20,51,.8);animation:npIn .7s cubic-bezier(.2,.9,.3,1.3) .4s both}
@keyframes npIn{from{opacity:0;transform:translateY(-10px) scale(.96)}}
.np-n{display:flex;align-items:center;gap:8px;margin-bottom:8px}
.np-n b{font-size:13px;font-weight:600;color:#FFFFFF}
.np-n em{margin-left:auto;font-style:normal;font-size:11.5px;color:rgba(255,255,255,.5)}
.np-ph p{margin:0 !important;font-size:13.5px !important;line-height:1.55;color:rgba(255,255,255,.85) !important}
.df2{display:flex;flex-direction:column;border:1.5px solid #E6EAF3;border-radius:16px;padding:2px 16px}
.df2-r{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:50px;border-top:1.5px solid #F0F2F8;font-size:14px}
.df2-r:first-child{border-top:0}
.df2-r > span:first-child{color:#5B6582}
.df2-v{display:inline-flex;align-items:center;gap:8px}
.df2-v s{color:#8A93AD;text-decoration-thickness:1.5px}
.df2-v svg{color:#AEB6CC}
.df2-v b{font-weight:600;padding:3px 10px;border-radius:999px;background:#FDECEA;color:#B42318;animation:dfIn .5s ease both .3s}
@keyframes dfIn{from{opacity:0;transform:translateX(-6px)}}
.df2-r.same b{background:#E7F5EE;color:#0F6B45}
.cl-bk2{margin-right:auto}
.cl-foot .cf-g{margin-left:auto;display:flex}
.cf-g .ds-btn{transition:opacity .25s ease,filter .25s ease}
.cf-g:not(.on) .ds-btn{opacity:.45;filter:saturate(.4);pointer-events:none}
.cf-g.on .ds-btn{animation:cfIn .5s cubic-bezier(.3,1.4,.5,1)}
@keyframes cfIn{50%{transform:scale(1.04)}}
.dep-r .ds-tag::before{content:'';width:6px;height:6px;border-radius:50%;background:currentColor;animation:lvP2 2s ease-out infinite}
@keyframes lvP2{0%{box-shadow:0 0 0 0 rgba(224,160,48,.45)}100%{box-shadow:0 0 0 6px rgba(224,160,48,0)}}
.ko-wrap{flex-grow:1;display:flex;justify-content:center;padding:44px 24px 64px 24px}
.ko{width:min(620px,100%);display:flex;flex-direction:column;align-items:center;text-align:center}
.ko-v.gy{--k:#5B6582;--kb:#EEF1F7}
.ko-v.am{--k:#B97A10;--kb:#FFF4E0}
.ko.gy .ko-pill{--k:#3A4566;--kb:#EEF1F7}
.ko.am .ko-pill{--k:#8A5A00;--kb:#FFF4E0}
.ko-pill{background:var(--kb);color:var(--k)}
.ko-h1{margin:14px 0 0 0;font-size:36px;line-height:1.12;font-weight:600;letter-spacing:-0.03em}
.ko-sub{margin:10px 0 0 0;max-width:520px;font-size:16px;line-height:1.55;color:#4A5578}
.ko-st{list-style:none;margin:24px 0 0 0;padding:0;display:flex;gap:6px}
.ko-st li{display:inline-flex;align-items:center;gap:6px;height:30px;padding:0 12px 0 6px;border-radius:999px;background:#F1F3F8;font-size:12.5px;font-weight:500;color:#3A4566;animation:obIn .4s ease both}
.ko-st li:nth-child(2){animation-delay:.1s}.ko-st li:nth-child(3){animation-delay:.2s}.ko-st li:nth-child(4){animation-delay:.3s}
.ko-st i{width:18px;height:18px;border-radius:50%;background:#5B6582;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.ko-card{margin-top:24px;width:100%;box-sizing:border-box;padding:18px 22px;border-radius:20px;border:1.5px solid #E6EAF3;background:#FFFFFF;text-align:left}
.ko-card dl{margin:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.ko-card dl div{display:flex;flex-direction:column;gap:3px;padding:12px;border-radius:14px;background:#F7F9FD}
.ko-card dt{font-size:12px;color:#8A93AD}
.ko-card dd{margin:0;font-size:15px;font-weight:600}
.ko-pres{margin-top:12px;display:flex;gap:12px;padding:14px;border-radius:14px;background:#F2FAF5}
.ko-pi{width:32px;height:32px;flex-shrink:0;border-radius:50%;background:#0F6B45;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.ko-pres span:last-child{display:flex;flex-direction:column;gap:2px}
.ko-pres b{font-size:14.5px;font-weight:600;color:#0F6B45}
.ko-pres em{font-style:normal;font-size:13.5px;line-height:1.5;color:#2C5240}
.ko-cl{display:block;margin-bottom:12px;font-size:12.5px;font-weight:500;color:#8A93AD}
.ira{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:8px}
.ira li{display:flex;align-items:center;gap:10px;padding:12px 14px;border-radius:14px;background:#FFF8EA;font-size:14px;font-weight:500}
.ira svg{flex-shrink:0;color:#B76E00}
.irs{margin-top:12px;display:flex;flex-direction:column}
.irs-r{display:grid;grid-template-columns:36px minmax(0,1fr) auto;align-items:center;gap:12px;padding:12px 0;border-top:1.5px solid #F0F2F8}
.irs-r:first-child{border-top:0}
.irs-i{width:36px;height:36px;border-radius:12px;display:flex;align-items:center;justify-content:center}
.irs-i.amber{background:#FFF4E0;color:#B76E00}.irs-i.blue{background:#EAF0FF;color:#1652F0}
.irs-r > span:nth-child(2){display:flex;flex-direction:column;gap:2px}
.irs-d{width:10px;height:10px;border-radius:50%;background:#E0A030;animation:lvP2 2s ease-out infinite}
.irs-d.blue{background:#1652F0}
@keyframes lvP2{0%{box-shadow:0 0 0 0 rgba(224,160,48,.45)}100%{box-shadow:0 0 0 8px rgba(224,160,48,0)}}
.irs-r b{font-size:14.5px;font-weight:600}
.irs-r em{font-style:normal;font-size:13px;color:#5B6582}
.ko-acts{margin-top:26px;display:flex;flex-direction:column;align-items:center;gap:12px}
@media (max-width: 960px){
.cl{display:flex;flex-direction:column;gap:0;padding-top:24px}
.cl-side{display:contents}
.cl-side > *{order:0}
.cl-h1{margin-top:6px}
.cl-meta{margin-top:12px}
.cl-pr{font-size:12.5px}
.cl-steps{margin-top:18px}
.cl-steps li span{display:none}
.cl-steps li.on span{display:block;white-space:nowrap}
.cl-panel{order:1;margin-top:24px}
.cl-nx{order:2;margin-top:20px;padding:16px}
.im4{grid-template-columns:repeat(2,minmax(0,1fr))}
.cl-foot{flex-wrap:nowrap}
.cl-foot .ds-btn,.cl-foot .cf-g{flex:1}
.cf-g .ds-btn{width:100%;justify-content:center}
.cl-bk2{flex-shrink:0}
.ko-wrap{padding:32px 16px 40px 16px}
.ko-h1{font-size:27px}
.ko-sub{font-size:15px}
.ko-st{flex-wrap:wrap;justify-content:center}
.ko-card{padding:16px}
.ko-card dl{grid-template-columns:repeat(3,minmax(0,1fr));gap:6px}
.ko-card dl div{padding:10px}
.ko-card dd{font-size:13.5px}
.ko-acts{width:100%}
.ko-acts .ds-btn{width:100%;justify-content:space-between}
}

@media (max-width: 960px){
.rs2{gap:0;border:1.5px solid #E6EAF3;border-radius:16px;overflow:hidden}
.ds-opt.rs{border:0;border-radius:0;padding:12px 14px}
.ds-opt.rs + .ds-opt.rs{border-top:1.5px solid #F0F2F8}
.ds-opt.rs.on{background:#F5F8FF;box-shadow:inset 3px 0 0 #1652F0}
.ko-st{gap:4px;flex-wrap:nowrap}
.ko-st li{height:26px;padding:0 8px 0 4px;font-size:11px;gap:4px}
.ko-st i{width:16px;height:16px}
.im{padding:12px}
.im b{font-size:22px}
}
'''

LEARN_CSS = SHARED + r'''body{background:#F7F9FD}
.la{min-height:100vh;background:#F7F9FD;font-family:'Google Sans','Google Sans Text','Helvetica Neue',system-ui,sans-serif;color:#0B1433}
.lh{display:flex;align-items:center;gap:28px;height:68px;padding:0 32px;background:#FFFFFF;border-bottom:1.5px solid #EEF1F7}
.lh-lg{display:flex}
.lh-lg .lg-word{height:24px}
.lh-n{display:flex;gap:22px}
.lh-n a{color:#3A4566;font-size:14.5px;font-weight:500;text-decoration:none;padding:24px 0;border-bottom:2.5px solid transparent}
.lh-n a.on{color:#0B1433;font-weight:600;border-bottom-color:#1652F0}
.lh-tag{display:inline-flex;align-items:center;height:28px;padding:0 11px;border-radius:999px;border:1.5px dashed #CBD3E6;font-size:12px;font-weight:500;color:#5B6582}
.la-m{width:min(1180px,100%);box-sizing:border-box;margin:0 auto;padding:36px 32px 56px 32px}
.pg-e{display:block;margin-bottom:8px;font-size:13px;font-weight:600;color:#1652F0}
.lc3{margin-top:26px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.lc2{display:flex;flex-direction:column;border-radius:22px;background:#FFFFFF;border:1.5px solid #E6EAF3;overflow:hidden;animation:obIn .55s ease both;animation-delay:calc(var(--i) * 120ms + 150ms)}
.lc2-cv{position:relative;display:block;height:132px;background:radial-gradient(circle at 85% 20%,rgba(92,134,255,.8),rgba(92,134,255,0) 55%),linear-gradient(140deg,#1652F0,#0B1433)}
.lc2-cv i{position:absolute;left:18px;bottom:12px;font-style:normal;font-size:30px;font-weight:600;letter-spacing:-0.03em;color:#FFFFFF}
.lc2-cv em{position:absolute;right:18px;height:6px;border-radius:6px;background:rgba(255,255,255,.22)}
.lc2-cv em:nth-of-type(1){top:56px;width:80px}.lc2-cv em:nth-of-type(2){top:70px;width:52px;background:rgba(255,255,255,.4)}
.lc2.am .lc2-cv{filter:saturate(.35)}
.lc2.gy .lc2-cv{filter:grayscale(1);opacity:.75}
.lc2-s{position:absolute;left:14px;top:14px;display:inline-flex;align-items:center;gap:6px;height:28px;padding:0 11px 0 7px;border-radius:999px;font-size:12.5px;font-weight:600;background:#FFFFFF}
.lc2-s svg{width:18px;height:18px;padding:3px;box-sizing:border-box;border-radius:50%;color:#FFFFFF}
.lc2.ok .lc2-s{color:#0F6B45}.lc2.ok .lc2-s svg{background:#0F6B45}
.lc2.am .lc2-s{color:#8A5A00}.lc2.am .lc2-s svg{background:#B76E00}
.lc2.gy .lc2-s{color:#3A4566}.lc2.gy .lc2-s svg{background:#5B6582}
.lc2-b{flex:1;display:flex;flex-direction:column;gap:12px;padding:18px 20px 20px 20px}
.lc2-b > b{font-size:17px;font-weight:600}
.lc2-p{display:flex;align-items:center;gap:14px}
.lc2-p > span{display:flex;flex-direction:column;gap:2px}
.lc2-p b{font-size:20px;font-weight:600}
.lc2-p em{font-style:normal;font-size:13px;color:#5B6582}
.lc2-x{padding:12px 14px;border-radius:14px}
.lc2.am .lc2-x{background:#FFF8EA}
.lc2.gy .lc2-x{background:#F1F3F8}
.lc2-x b{font-size:14.5px;font-weight:600}
.lc2.am .lc2-x b{color:#8A5A00}
.lc2-x p{margin:3px 0 0 0;font-size:13.5px;line-height:1.5;color:#3A4566}
.lc2-a{margin-top:auto;display:flex}
.lc2-a .ds-btn,.lc2-a .ds-ghost{width:100%;justify-content:space-between}
.lc2-a .ds-ghost{justify-content:center;height:44px}
@media (max-width: 960px){
.lh{height:60px;padding:0 16px;gap:12px}
.lh-n{display:none}
.la-m{padding:24px 16px 32px 16px}
.ds-h1{font-size:24px}
.lc3{grid-template-columns:minmax(0,1fr);gap:12px;margin-top:20px}
.lc2{display:grid;grid-template-columns:96px minmax(0,1fr)}
.lc2-cv{height:auto;min-height:100%}
.lc2-cv i{font-size:18px;left:10px;bottom:8px}
.lc2-cv em{display:none}
.lc2-s{left:auto;right:auto;top:auto;bottom:auto;position:static;margin:10px 0 0 0;height:auto;padding:0;background:none;font-size:12px}
.lc2-cv .lc2-s{display:none}
.lc2-b{padding:14px;gap:10px}
.lc2-b > b{font-size:15px}
.lc2-p b{font-size:17px}
.lc2-x{padding:10px 12px}
}
'''

write('Manage.dc.html', doc('Manage Published Course · shared source', kit.KIT_CSS + '\n' + dash.DASH_CSS + BASE_CSS + WK_CSS + MANAGE_CSS, manage_body(), MANAGE_JS))
write('Unpublish.dc.html', doc('Unpublish course · shared source', kit.KIT_CSS + '\n' + dash.DASH_CSS + BASE_CSS + UN_CSS, un_body(), UN_JS))
write('Learner.dc.html', doc('Learner app · My Learning · shared source', kit.KIT_CSS + '\n' + dash.DASH_CSS + BASE_CSS + WK_CSS + LEARN_CSS, LEARN,
                             'class Component extends DCLogic {\n  renderVals() { return {}; }\n}'))

BOARDS = [
    ('MGT-001', 'Manage', {'page': 'hub'}, 'CR-COURSE-MGT-001 · Manage Course Hub'),
    ('MGT-002', 'Manage', {'page': 'a'}, 'CR-COURSE-MGT-002-A · Publishing & Visibility (default)'),
    ('MGT-002-EDIT', 'Manage', {'page': 'edit'}, 'MGT-002 · Manage Availability — Step 2 of 4'),
    ('MGT-002-REVIEW', 'Manage', {'page': 'review'}, 'MGT-002 · Manage Availability — Step 3 of 4'),
    ('MGT-002B', 'Manage', {'page': 'b'}, 'MGT-002-B · Published / Visible / Paused (success)'),
    ('MGT-002C', 'Manage', {'page': 'c'}, 'MGT-002-C · Published / Hidden / Paused'),
    ('MGT-002D', 'Manage', {'page': 'd'}, 'MGT-002-D · Unpublished — Republish available'),
    ('MGT-002E', 'Manage', {'page': 'e'}, 'MGT-002-E · Restricted by Credalio'),
    ('MGT-002F', 'Manage', {'page': 'f'}, 'MGT-002-F · Organization Approval Required'),
    ('MGT-002G', 'Manage', {'page': 'g'}, 'MGT-002-G · Saving / Error / Conflict'),
    ('MGT-002-NOTICE', 'Manage', {'page': 'notice'}, 'MGT-002-E2 · Restriction Notice'),
    ('MGT-003A', 'Unpublish', {'step': 'impact'}, 'CR-COURSE-MGT-003A · Unpublish — Review Learner Impact'),
    ('MGT-003B', 'Unpublish', {'step': 'reason'}, 'CR-COURSE-MGT-003B · Unpublish — Reason & Transition Plan'),
    ('MGT-003C', 'Unpublish', {'step': 'confirm'}, 'CR-COURSE-MGT-003C · Unpublish — Final Confirmation'),
    ('MGT-003D', 'Unpublish', {'step': 'done'}, 'CR-COURSE-MGT-003D · Unpublish — Success'),
    ('MGT-003E', 'Unpublish', {'step': 'blocked'}, 'CR-COURSE-MGT-003E · Unpublish — Restricted / Approval Required'),
    ('MGT-DS-OV', 'Manage', {'page': 'ds-ov'}, 'Downstream · Course Overview — Unpublished state'),
    ('MGT-DS-CR', 'Manage', {'page': 'ds-cr'}, 'Downstream · My Creations — Unpublished card state'),
    ('MGT-DS-ML', 'Learner', {}, 'Downstream · My Learning — learner access states (learner app)'),
]

if __name__ == '__main__':
    import sys
    H = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else {}
    for code, src, props, title in BOARDS:
        bg = '#FFFFFF' if src == 'Unpublish' else '#F7F9FD'
        hd, hm = H.get(code, (3000, 3000))
        write(code + '.dc.html', wrapper(title + ' · Desktop', src, props, 1440, hd, bg))
        write(code + '-Mobile.dc.html', wrapper(title + ' · Mobile', src, props, 390, hm, bg))
    print('ok', len(BOARDS), 'boards; toggles', W.n, U.n)
