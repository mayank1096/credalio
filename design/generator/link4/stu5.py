"""Link 4 · Batch 5: Validate (case, workspace, decision, revision) and Publish. Client copy word for word
(Creio for "AI Tokens"; the star emoji becomes the badge icon).

Validate.dc.html (prop page: wait | assigned | ws | req | ev | meet | find | improve | revise | resub | passed)   CR-STU-053 to 059
Publish.dc.html  (prop step: price | priceout | revenue | listing | live)                                          CR-STU-060 to 062, 065
Workspace tabs and request rows follow the Link 1 Validation Workspace (CR-VAL-WS): underline tabs, case-linked rows.
"""
import json
import l4kit
from l4kit import *
from rail import *
from kit import coin, credit, emblem
import stu2

W = Toggles()
PAGES = []
def P(key, head, main, actions, rail=''):
    PAGES.append((key, head, main, actions, rail))

CASE = 'VAL-2026-00482'
LEAD = '<span class="lead">%s<span>Case Lead</span></span>' % ic('badge', 12, 2.2)
def lead_txt(t):
    return t.replace('⭐ Case Lead', LEAD).replace('⭐ CASE LEAD', LEAD)

def wkp(main, actions, rail):
    return '<div class="wk"><div class="wk-m">%s</div>%s<aside class="wk-r">%s</aside></div>' % (
        main, actions.replace('class="ds-acts sb sv"', 'class="ds-acts sb sv wk-a"'), rail)

def sidebar_val(active):
    nav = []
    for g, items in l4kit.NAV:
        it = []
        for label, href, st, key in items:
            if key == 'ready': st = 'ok'
            if key == 'val': st = 'pr'
            it.append((label, href, st, key))
        nav.append((g, it))
    old = l4kit.NAV
    l4kit.NAV = nav
    h = sidebar(active)
    l4kit.NAV = old
    return h.replace('<span class="ds-tag">Draft</span>', '<span class="ds-tag blue">In validation</span>')

TRACK = ['Submitted', 'Validator Assignment', 'Validation', 'Decision']
def tracker(cur, tone='cb'):
    li = ''
    for i, t in enumerate(TRACK):
        k = 'dn' if i < cur else ('on' if i == cur else '')
        li += '<li class="%s"><i>%s</i><span>%s</span></li>' % (k, ck(10) if i < cur else '', t)
    return '<ol class="vt %s" style="--p: %d" aria-label="Validation progress">%s</ol>' % (tone, cur, li)

def case_head(status, tone, h1, sub, cur, extra=''):
    return ('<section class="vh %s ob-in"><div class="vh-t"><div><span class="vh-k"><b>%s</b><span>%s</span></span><h1 class="ds-h1">%s</h1>%s</div>%s</div>%s%s</section>') % (
        tone, CASE, status, h1, ('<p class="ds-sub">%s</p>' % sub) if sub else '', extra, tracker(cur, tone), '')

TABS = [('ws', 'Overview', '', 'STU-055.dc.html'), ('find', 'Findings', '4', 'STU-055D.dc.html'), ('req', 'Requests', '2', 'STU-055A.dc.html'),
        ('ev', 'Evidence', '', 'STU-055B.dc.html'), ('meet', 'Meetings', '1', 'STU-055C.dc.html'), ('conv', 'Conversation', '', '#'), ('time', 'Timeline', '', '#')]
def ws_tabs(cur, counts=None):
    counts = counts or {}
    h = ''
    for k, l, n, href in TABS:
        n = counts.get(k, n)
        h += '<a href="%s" class="ut%s"%s><span>%s</span>%s</a>' % (href, ' on' if k == cur else '', ' aria-current="page"' if k == cur else '',
                                                                   l, ('<i>%s</i>' % n) if n else '')
    return '<nav class="utabs vtabs ob-in2" aria-label="Validation workspace">%s</nav>' % h

def ws_head(cur, decided=False):
    if decided:
        return (case_head('Improvements required', 'am', 'Validation Workspace', 'Data Analysis with SQL · Standard Course Validation', 3,
                          '<span class="vh-s am"><i></i>Decision issued: improvements required.</span>') + ws_tabs(cur, {'find': '3', 'req': '', 'meet': ''}))
    return (case_head('Action required', 'am', 'Validation Workspace', 'Data Analysis with SQL · Standard Course Validation', 2,
                      '<span class="vh-s am"><i></i>Validation is underway. A validator needs something from you.</span>') + ws_tabs(cur))

NOVA_WAIT = 'I’m here if you need help.'
NOVA_WS = 'I’ll notify you when action is needed.'
CASE_CARD = '''<section class="ds-card rx cs-c"><span class="rx-k">Case</span><dl>%s</dl></section>''' % ''.join(
    '<div><dt>%s</dt><dd>%s</dd></div>' % r for r in [('Case ID', CASE), ('Validation type', 'Standard Course Validation'), ('Paid', '%s441 Creator Credits' % credit())])

# ---------------------------------------------------------------- CR-STU-053 Awaiting assignment
NOW = [('dn', 'Your case is in the assignment queue'), ('on', 'Credalio is matching validators by role: Educational Validator, Subject Matter Validator'),
       ('', 'Each validator confirms no conflict of interest [TO CONFIRM protocol]')]
P('wait', case_head('Awaiting assignment', 'cb', 'Finding the right validators', '', 1),
  '''<section class="ds-card ok-n ob-in2"><span class="ok-i">%s</span><div><b>No action required</b><p>You’ll be notified as soon as validators are assigned.</p></div></section>
<section class="ds-card fc ob-in3"><div class="fc-h"><div><h2>What’s happening now</h2></div></div><ol class="hn">%s</ol></section>
<section class="ds-card fc ww ob-in4"><div class="fc-h"><div><h2>While you wait</h2></div></div><p>The submitted version is locked until a decision so validators all review the same thing. You can keep working on other drafts, and nothing about this case needs you until a validator asks.</p><span class="ww-t">%s<span>Typical assignment time [TO CONFIRM]</span></span></section>''' % (
      ck(16), ''.join('<li class="%s"><span class="hn-d">%s</span><span>%s</span></li>' % (k, ck(10) if k == 'dn' else '', t) for k, t in NOW), ic('clock', 15, 2)),
  acts('STU-055.dc.html', 'Open Validation Workspace', note='<a class="ds-link" href="STU-009.dc.html">Back to Studio Home</a>'),
  nova_rail(NOVA_WAIT) + '''<section class="ds-card rx mt ob-in3" aria-hidden="true"><span class="rx-k">Matching by role</span><div class="mt-v"><span class="mt-c">%s</span><span class="mt-o"></span><span class="mt-r a">%s</span><span class="mt-r b">%s</span><span class="mt-r c">%s</span><span class="mt-r d">%s</span></div><div class="mt-l"><span>Educational Validator</span><span>Subject Matter Validator</span></div></section>''' % (
      ic('course', 20, 2), ic('cap', 14, 2), ic('target', 14, 2), ic('user', 14, 2), ic('user', 14, 2)) + CASE_CARD)

# ---------------------------------------------------------------- CR-STU-054 Validators assigned
ROLES = [('cap', 'Educational Validator', 'Assigned', 'Reviews: Learning design, outcomes, assessment alignment, accessibility.', False, True),
         ('target', 'Subject Matter Validator', 'Assigned', 'Reviews: Accuracy, currency, evidence quality and professional claims.', True, True),
         ('quiz', 'Assessment Validator', 'Not required', 'Reviews: Assessment validity and rubric quality. Only assigned when the case requires it.', False, False)]
def role(i, r):
    icon, t, st, d, lead, on = r
    return ('<article class="vr%s" style="--i: %d"><div class="vr-h"><span class="vr-i">%s</span>%s</div><b>%s</b>%s<p>%s</p><span class="vr-s"><span class="vr-sh">%s</span><em>%s</em></span></article>') % (
        '' if on else ' off', i, ic(icon, 22, 1.9), tag('%s%s' % (ck(10) + ' ' if on else '', st), 'green' if on else ''), t,
        ('<span class="vr-l">%s<span>coordinates requests and meetings</span></span>' % LEAD) if lead else '', d,
        ic('lock', 12, 2) if on else '', 'Identity protected' if on else 'Not on this case')
P('assigned', case_head('Validation underway', 'cb', 'Validators assigned', 'Each role reviews your course independently. You see roles, not identities.', 2),
  '<div class="vrs ob-in2">%s</div><div class="wn info ob-in3">%s<span>Validator identities are protected under the validation protocol. All contact happens inside the Validation Workspace, so every request, meeting and message stays on the case record.</span></div>' % (
      ''.join(role(i, r) for i, r in enumerate(ROLES)), ic('lock', 16, 2)),
  acts('STU-055.dc.html', 'Open Validation Workspace'),
  nova_rail(NOVA_WAIT) + CASE_CARD)

# ---------------------------------------------------------------- CR-STU-055 Workspace overview
ATT = [('chat', 'Answer clarification', 'REQ-01 Subject Matter Validator · due 3 Oct', 'Respond', 'STU-055A.dc.html'),
       ('upload', 'Submit evidence for REQ-02', 'Educational Validator · due 4 Oct', 'Upload', 'STU-055B.dc.html'),
       ('cal', 'Choose a meeting time', 'Practical assessment methodology · 30 min', 'Choose', 'STU-055C.dc.html')]
P('ws', ws_head('ws'),
  '''<div class="vs3 ob-in2"><a class="vs-t am" href="STU-055A.dc.html"><b>2</b><span><em>Open requests</em>A validator is waiting on you</span></a><a class="vs-t" href="STU-055D.dc.html"><b>4</b><span><em>Findings to act on</em>5 findings shared so far</span></a><a class="vs-t" href="STU-055C.dc.html"><b>1</b><span><em>Meeting</em>Choose a time</span></a></div>
<section class="ds-card fc na ob-in3"><div class="fc-h"><div><h2>Needs your attention</h2></div></div><ul>%s</ul></section>
<section class="ds-card fc ob-in4"><div class="fc-h"><div><h2>Review progress by role%s</h2></div></div><div class="rp">%s</div></section>''' % (
      ''.join('<li><span class="na-i">%s</span><span class="na-t"><b>%s</b><em>%s</em></span><a class="ds-ghost sm" href="%s">%s</a></li>' % (ic(i, 17, 2) if i in EXTRA or i in I else '', t, lead_txt(d), h, a) for i, t, d, a, h in ATT),
      tip('Validator identities are protected under the validation protocol.'),
      ''.join('<div class="rp-r"><span class="rp-n"><b>%s</b>%s</span><span class="rp-b"><i style="--w: %d%%"></i></span>%s</div>' % (n, l, w, tag('In progress', 'blue')) for n, l, w in [('Educational Review', '', 55), ('Subject Matter Review', LEAD, 40)])),
  '',
  nova_rail(NOVA_WS) + CASE_CARD)

# ---------------------------------------------------------------- CR-STU-055A Requests
def reqc(kind, role_, prio, due, text, meta, body, cls=''):
    return ('<article class="ds-card rq%s"><header><span class="rq-k">%s<span>%s</span></span><span class="rq-m">%s<span class="rq-d">%s<span>Due %s</span></span>%s</span></header>'
            '<p class="rq-q">%s</p><span class="rq-x">%s</span>%s</article>') % (
        (' ' + cls) if cls else '', kind, lead_txt(role_), tag(prio, 'amber' if prio.startswith('High') else ''), ic('clock', 13, 2), due, tag('Open', 'blue'), text, meta, body)
REQ1 = reqc('Clarification', 'Subject Matter Validator', 'Normal priority', '3 Oct', 'Please provide the source used for the industry benchmark referenced in Chapter 4, Lesson 2.',
            'REQ-01 · Evidence quality · Chapter 4 · Lesson 2',
            '<div class="rq-r"><label class="fl"><span class="fl-l">Your response</span><textarea class="ds-in" rows="3" aria-label="Your response"></textarea></label><div class="rq-a"><button type="button" class="ds-ghost sm">%s<span>Upload Evidence</span></button>%s</div></div>' % (
                ic('upload', 15, 2), btn('Send Response', '#', 'sm2')), 'on')
REQ2 = reqc('Evidence request', 'Educational Validator', 'High priority', '4 Oct', 'Upload one anonymised Final Project submission marked against your rubric, so we can see how the criteria are applied.',
            'REQ-02 · Assessment evidence · Final Project', '<a class="ds-link rq-go" href="STU-055B.dc.html">Respond in Evidence%s</a>' % ic('arrowr', 14, 2.2))
P('req', ws_head('req'), '<div class="rqs ob-in3">%s%s</div><p class="vn">%s<span>Requests are always case-linked. Replies, files and links stay on the case record, and validators can’t message you outside it.</span></p>' % (REQ1, REQ2, ic('lock', 14, 2)),
  '', nova_rail(NOVA_WS) + CASE_CARD)

# ---------------------------------------------------------------- CR-STU-055B Evidence
AUD = [('30 Sep 09:10', 'Credalio', 'Case created · fee paid'), ('30 Sep 09:12', 'Credalio', 'Validators assigned by role'),
       ('30 Sep 14:02', 'Subject Matter Validator', 'REQ-01 clarification requested'), ('30 Sep 14:20', 'Educational Validator', 'REQ-02 evidence requested')]
P('ev', ws_head('ev'),
  reqc('Evidence request', 'Educational Validator', 'High priority', '4 Oct', 'Upload one anonymised Final Project submission marked against your rubric, so we can see how the criteria are applied.',
       'REQ-02 · Assessment evidence · Final Project',
       '''<div class="up"><label class="up-d"><span class="up-i">%s</span><b>Upload</b><span>Choose file</span></label><div class="up-f"><label class="fl"><span class="fl-l">Or link</span><input class="ds-in" placeholder="https://" aria-label="Or link"></label><label class="fl"><span class="fl-l">Description</span><textarea class="ds-in" rows="2" aria-label="Description"></textarea></label></div></div><div class="rq-a">%s</div>''' % (
           ic('upload', 22, 2), btn('Submit evidence', '#', 'sm2')), 'on ob-in3') +
  '<section class="ds-card fc evl ob-in4"><div class="fc-h"><div><h2>Evidence on this case</h2></div></div><div class="emp"><span class="emp-i">%s</span><b>No evidence yet</b><span>Files and links you submit to this case appear here.</span></div></section>' % ic('clip', 20, 2),
  '',
  nova_rail(NOVA_WS) + '<section class="ds-card rx au ob-in3"><span class="rx-k">Audit trail</span><ol>%s</ol></section>' % ''.join(
      '<li style="--i: %d"><span class="au-d"></span><span class="au-t"><em>%s · %s</em><b>%s</b></span></li>' % (i, t, w, e) for i, (t, w, e) in enumerate(AUD)))

# ---------------------------------------------------------------- CR-STU-055C Meeting
SLOTS = [('Wed', '1 Oct', '2:00 PM'), ('Thu', '2 Oct', '10:00 AM'), ('Thu', '2 Oct', '4:30 PM')]
def slot(d, dt, t, on):
    k = W.new(on, 'slot')
    return '<button type="button" class="sl {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}"><em>%s</em><b>%s</b><span>%s</span><i>%s</i></button>' % (k, k, k, d, dt.split()[0], dt.split()[1] + ' · ' + t, ck(11))
P('meet', ws_head('meet'),
  '''<article class="ds-card mr ob-in3"><header><span class="rq-k">Meeting request<span>Case-linked</span></span>%s</header>
<h2>Clarification of practical assessment methodology</h2><p class="mr-by">Requested by Subject Matter Validator · %s</p>
<div class="mr-g"><div class="mr-k"><span>Participants</span><b class="mr-p"><i>You</i><i>Subject Matter Validator</i><i>Educational Validator</i></b></div><div class="mr-k"><span>Linked to</span><b>Final Project · rubric (FND-2048-027)</b></div><div class="mr-k"><span>Length</span><b>30 minutes</b></div></div>
<p class="mr-w">The validators want to understand how the Final Project’s practical work is marked before finalising their assessment findings. 30 minutes.</p>
<span class="mr-sl">Suggested times (your time zone, WAT)</span><div class="sls">%s</div>
<div class="rq-a">%s%s</div></article>
<p class="vn">%s<span>Meetings are part of the validation case, not a private call. The agenda, attendance and any agreed actions are recorded and remain attached to VAL-2026-00482.</span></p>''' % (
      tag('Awaiting your response', 'amber'), LEAD, ''.join(slot(d, dt, t, i == 0) for i, (d, dt, t) in enumerate(SLOTS)),
      '<button type="button" class="ds-ghost sm">Suggest Another Time</button>', btn('Accept', '#', 'sm2'), ic('lock', 14, 2)),
  '', nova_rail(NOVA_WS) + CASE_CARD)

# ---------------------------------------------------------------- CR-STU-055D Findings
SEV = {'MAJOR': 'mj', 'MINOR': 'mn', 'OBSERVATION': 'ob'}
FIND = [('MAJOR', 'FND-2048-027', 'The rubric doesn’t evidence LO4 (publishing and maintaining a dashboard).', 'Educational Validator', 'Final Project · rubric', 'Requires Change'),
        ('MINOR', 'FND-2048-029', 'Question 7 has two defensible answers.', 'Subject Matter Validator', 'Final Exam · Q7', 'Requires Change'),
        ('MINOR', 'FND-2048-014', 'Time estimate doesn’t match the content.', 'Educational Validator', 'Chapter 3 · Lesson 1', 'Requires Change'),
        ('MINOR', 'FND-2048-011', 'Industry benchmark needs a cited source.', 'Subject Matter Validator', 'Chapter 4 · Lesson 2', 'Resolved'),
        ('OBSERVATION', 'FND-2048-006', 'Strong scaffolding from single-table queries to joins.', 'Educational Validator', 'Chapter 2', 'Accepted')]
STC = {'Requires Change': 'amber', 'Resolved': 'green', 'Accepted': 'green', 'Open': 'blue'}
P('find', ws_head('find', True),
  '''<div class="ff ob-in2"><span class="ff-l">Validator role</span>%s<span class="ff-l">Status</span>%s</div>
<section class="ds-card ft ob-in3"><div class="ft-r ft-hd"><span>Severity</span><span>Finding · what the validator found</span><span>Role · section</span><span>Status</span></div>%s</section>''' % (
      W.seg(['All', 'Educational', 'Subject Matter'], 0), W.seg(['All', 'Open', 'Requires Change', 'Resolved', 'Accepted'], 0),
      ''.join('<a class="ft-r %s" href="%s"><span class="sv-b %s">%s</span><span class="ft-f"><b>%s</b><em>%s</em></span><span class="ft-rs"><em>%s</em>%s</span>%s</a>' % (
          SEV[s], 'STU-057.dc.html' if st == 'Requires Change' else '#', SEV[s], s.capitalize(), t, i, r, sec, tag(st, STC[st])) for s, i, t, r, sec, st in FIND)),
  acts('STU-056.dc.html', 'See your action plan'),
  nova_rail(NOVA_WS) + '''<section class="ds-card rx fs ob-in3"><span class="rx-k">Findings by severity</span><div class="fs-b"><i class="mj" style="flex: 1"></i><i class="mn" style="flex: 3"></i><i class="ob" style="flex: 1"></i></div><ul>%s</ul></section>''' % ''.join(
      '<li><i class="%s"></i><span>%s</span><b>%d</b></li>' % (k, l, n) for k, l, n in [('mj', 'Major', 1), ('mn', 'Minor', 3), ('ob', 'Observation', 1)]))

# ---------------------------------------------------------------- CR-STU-056 Improvements required
PLAN = [('MAJOR', 'FND-2048-027', 'Final Project · rubric', 'The Final Project rubric doesn’t evidence LO4 (publishing and maintaining a dashboard). Add a criterion that assesses it.'),
        ('MINOR', 'FND-2048-029', 'Final Exam · Q7', 'Question 7 has two defensible answers. Accept both or reword the question.'),
        ('MINOR', 'FND-2048-014', 'Chapter 3 · Lesson 1', 'The time estimate (8 min) doesn’t match the content (about 20 min).')]
P('improve', case_head('Decision issued 3 Oct', 'am', 'Improvements Required', 'Your course is close. Here’s your action plan: fix what’s required, then resubmit. Only the affected findings are rechecked.', 3),
  '''<div class="vs3 ob-in2"><div class="vs-t am"><span class="vs-ic">%s</span><span><em>Deadline</em><b class="sm">17 Oct</b></span></div><div class="vs-t"><span class="vs-ic">%s</span><span><em>Revalidation scope</em><b class="sm">Minor · SV-006</b></span></div><div class="vs-t"><span class="vs-ic pr">%s</span><span><em>Progress</em><b class="sm">0 of 3 addressed</b></span></div></div>
<section class="ds-card fc ap ob-in3"><div class="fc-h"><div><h2>Action plan</h2></div></div><ol>%s</ol></section>''' % (
      ic('cal', 18, 2), ic('layers', 18, 2), ring(0, 34, 12),
      ''.join('<li style="--i: %d"><span class="ap-n">%d</span><div class="ap-b"><span class="ap-m"><span class="sv-b %s">%s</span><em>%s · %s</em></span><p>%s</p></div><a class="ds-ghost sm" href="STU-057.dc.html">Fix%s</a></li>' % (
          i, i + 1, SEV[s], s.capitalize(), fid, sec, t, ic('arrowr', 14, 2.2)) for i, (s, fid, sec, t) in enumerate(PLAN))),
  acts('STU-057.dc.html', 'Start revising', note='<a class="ds-link" href="STU-058.dc.html">Go to resubmission</a>'),
  nova_rail('Congratulations. Publication is next.') + CASE_CARD)

# ---------------------------------------------------------------- CR-STU-057 Course revision
RUB = [('Query correctness', 'LO1, LO2'), ('Analysis quality', 'LO3'), ('Communication of findings', 'LO3')]
k_add = W.new(False)
P('revise', '''<header class="pg-h ob-in"><div class="pg-hl"><span class="pg-e rv-e"><span class="rv-dot"></span>Revision mode · v1.1 draft</span><h1 class="ds-h1">Course Revision</h1><p class="ds-sub">Each validator finding sits next to the content it affects. Fix it here, note what you changed, and mark it addressed.</p></div><div class="pg-hr"><span class="rv-p">%s<span><b>0</b> of 3 addressed</span></span></div></header>''' % ring(0, 40, 12),
  '''<div class="rvw ob-in2"><nav class="rvl" aria-label="Findings">%s</nav>
<div class="rvc"><section class="ds-card vf"><span class="vf-k"><span class="sv-b mj">Major</span>Validator finding · Educational Validator</span><p>The Final Project rubric doesn’t evidence LO4 (publishing and maintaining a dashboard). Add a criterion that assesses it.</p><em>FND-2048-027 · Final Project · rubric</em></section>
<span class="rv-ln" aria-hidden="true"></span>
<section class="ds-card ac"><div class="ac-h"><span class="rx-k">Affected content</span><a class="ds-link sm" href="STU-PRA.dc.html">Open in Practice &amp; Projects%s</a></div><b class="ac-t">Final Project · marking rubric</b>
<ul class="rb">%s<li class="add {{c%s}}"><button type="button" aria-pressed="{{a%s}}" onClick="{{x%s}}">%s<span>Add criterion: Publishes and maintains a dashboard (LO4)</span></button></li></ul>
<label class="fl ac-n"><span class="fl-l">What did you change?</span><textarea class="ds-in" rows="2" aria-label="What did you change?"></textarea></label>
<div class="rq-a"><button type="button" class="ds-ghost sm">%s<span>Mark as addressed</span></button></div></section></div></div>''' % (
      ''.join('<a class="rvl-i%s" href="#"><span class="sv-b %s">%s</span><b>%s</b><em>%s</em>%s</a>' % (' on' if i == 0 else '', SEV[s], s.capitalize(), fid, sec, tag('Open', 'blue')) for i, (s, fid, sec, t) in enumerate(PLAN)),
      ic('arrowr', 14, 2.2), ''.join('<li><span class="rb-g">%s</span><b>%s</b><em>%s</em></li>' % (ic('grip', 14, 2), c, l) for c, l in RUB), k_add, k_add, k_add, ic('plus', 15, 2.4), ck(12)),
  acts('STU-058.dc.html', 'Continue to resubmission'),
  nova_rail('Each finding is shown next to the content it affects.'))

# ---------------------------------------------------------------- CR-STU-058 Resubmission
P('resub', page_head('Validate', 'Resubmission', 'Show validators what changed. Only the affected findings are rechecked.'),
  '''<section class="ds-card fc ob-in2"><div class="fc-h"><div><h2>Changes made</h2></div></div><ul class="cm2">%s</ul>
<span class="ws-l">Evidence on this case</span><div class="evf">%s</div></section>
<section class="ds-card fc ob-in3"><label class="fl"><span class="fl-l">Notes for validators</span><textarea class="ds-in" rows="3" aria-label="Notes for validators"></textarea></label></section>''' % (
      ''.join('<li><span class="st to"></span><div><span class="ap-m"><span class="sv-b %s">%s</span><em>%s</em></span><p><b>Not addressed yet:</b> %s</p></div><a class="ds-ghost sm" href="STU-057.dc.html">Fix</a></li>' % (SEV[s], s.capitalize(), fid, t) for s, fid, sec, t in PLAN),
      ''.join('<span class="evf-i">%s<span><b>%s</b><em>%s</em></span></span>' % (ic('file', 16, 2), f, m) for f, m in [('benchmark-source.pdf', 'REQ-01 · Chapter 4 · Lesson 2'), ('final-project-marked-sample.pdf', 'REQ-02 · Final Project')])),
  '<div class="ds-acts sb sv"><span class="sv-s rs-w">%s<span>The Major finding must be addressed before you can resubmit.</span></span><span class="sv-r"><a class="ds-link" href="STU-057.dc.html">Back</a><span class="ds-btn is-dis" aria-disabled="true"><span>Submit Changes</span><span class="ob-arrow">%s</span></span></span></div>' % (ic('lock', 14, 2), ARROW),
  nova_rail('Only the affected findings are rechecked.') + '''<section class="ds-card rx rvx ob-in3"><span class="rx-k">Revalidation</span><div class="rvx-v"><span>v1.0</span><i></i><span class="on">v1.1</span></div><dl>%s</dl></section>''' % ''.join(
      '<div><dt>%s</dt><dd>%s</dd></div>' % r for r in [('Scope', 'Minor Revalidation · SV-006'), ('Rechecked', 'Only the findings listed here'), ('Version', 'v1.0 → v1.1'), ('Fee', '[TO CONFIRM: revalidation fee rules]')]))

# ---------------------------------------------------------------- CR-STU-059 Decision: passed
P('passed', '',
  '''<div class="ko-in ob-in"><div class="ko">%s<span class="ko-pill gold">%s<span>Gold Validated</span></span><h1 class="ko-h1">Your course has passed validation</h1><p class="ko-sub">VAL-2026-00482 · decision issued 3 Oct · tier calculated under the final validation rules</p></div>
<div class="dg"><section class="ds-card fc vrp"><div class="fc-h"><div><h2>Validation report</h2></div><a class="ds-link sm" href="#">View full validation report</a></div>
<div class="vrp-r"><span class="vr-i sm">%s</span><span class="vrp-t"><b>Educational Validator</b><em>Learning design, outcomes, assessment alignment</em></span>%s</div>
<div class="vrp-r"><span class="vr-i sm">%s</span><span class="vrp-t"><b>Subject Matter Validator · %s</b><em>Accuracy, currency, evidence quality</em></span>%s</div>
<div class="vrp-f"><span>Findings</span><b>0 Critical · 2 Major (resolved in v1.1) · 4 Minor</b></div></section>
<section class="ds-card fc wm"><div class="fc-h"><div><h2>What this means</h2></div></div><ul>%s</ul></section></div></div>''' % (
      emblem(), ic('badge', 14, 2), ic('cap', 18, 2), tag('%s Meets standard' % ck(10), 'green'), ic('target', 18, 2), LEAD, tag('%s Meets standard' % ck(10), 'green'),
      ''.join('<li><span class="wm-i">%s</span><span><b>%s</b><em>%s</em></span></li>' % (ic(i, 17, 2), t, d) for i, t, d in [
          ('badge', 'Gold Validated badge', 'Shown on your course page and marketplace card once you publish.'),
          ('analytics', 'Creator Evidence Index (CEI)', 'Validation is how this course counts toward your CEI. The contribution follows the CEI rules [TO CONFIRM].'),
          ('layers', 'Future changes', 'Significant edits after publishing trigger a revalidation check (minor, standard or major).'),
          ('rocket', 'Next step', 'Set marketplace access and pricing, then publish.')])),
  acts('STU-060.dc.html', 'Continue to Publication'),
  '')

def val_body():
    blocks = []
    for key, head, main, actions, rail in PAGES:
        body = head + (wkp(main, actions, rail) if rail else '<div class="ko-page">%s%s</div>' % (main, actions))
        blocks.append('<sc-if value="{{p_%s}}" hint-placeholder-val="{{ %s }}">\n%s\n</sc-if>' % (key, 'true' if key == 'ws' else 'false', body))
    return '''<div class="ds-root">
%s
<div style="min-width: 0; display: flex; flex-direction: column">
%s
<main class="ds-main vv-main {{tone}}">
%s
</main>
</div>
</div>''' % (sidebar_val('val'), topbar(phase='Validate'), '\n'.join(blocks))
TONE = {'wait': 'cb', 'assigned': 'cb', 'ws': 'am', 'req': 'am', 'ev': 'am', 'meet': 'am', 'find': 'am', 'improve': 'am', 'revise': 'am', 'resub': 'am', 'passed': 'ok'}
VAL_JS = W.js() + '''var PG = %s, TONE = %s;
class Component extends DCLogic {
  renderVals() {
    var pg = this.props.page || 'ws', v = togVals(this), self = this;
    PG.forEach(function (k) { v['p_'.concat(k)] = k === pg; });
    v.tone = 'tn-'.concat(TONE[pg] || 'cb');
    v.navCls = this.state.nav ? 'ds-open' : '';
    v.toggleNav = function () { self.setState({ nav: !self.state.nav }); };
    return v;
  }
}''' % (json.dumps([p[0] for p in PAGES]), json.dumps(TONE))

# ======================================================================= PUBLISH (focus flow)
U = Toggles()
PSTEPS = ['Final pricing', 'Revenue', 'Listing', 'Preview', 'Publish']
GOLD = '<span class="gb">%s<span>Gold Validated</span></span>' % ic('badge', 14, 2)
def pside(step, extra):
    li = ''.join('<li class="%s"><i></i><span>%s</span></li>' % ('dn' if i < step or (i in (1, 2) and step == 0) or (i == 2 and step == 1) or (i == 1 and step == 2) else ('on' if i == step else ''), s) for i, s in enumerate(PSTEPS))
    return ('<aside class="cl-side ob-in"><span class="pb-k">Publish · Step %d of 5</span><h1 class="cl-h1">Data Analysis with SQL</h1><div class="cl-meta">%s<span>VAL-2026-00482</span></div><ol class="cl-steps">%s</ol>%s</aside>') % (step + 1, GOLD, li, extra)
def ppanel(h, p, body, foot):
    return '<section class="cl-panel ob-in2"><h2 class="cl-ph">%s</h2>%s%s<div class="cl-foot">%s</div></section>' % (h, ('<p class="cl-pp">%s</p>' % p) if p else '', body, foot)
def bk(href):
    return '<a class="ds-ghost cl-bk" href="%s" aria-label="Back">%s<span>Back</span></a>' % (href, ICON(I['back'], 18, 2))

def range_card(kind, ok, lo, hi, sel, unit, extra='', stops=None):
    pos = (sel - lo) * 100.0 / (hi - lo) if hi > lo else 50
    pos_cls = '' if 0 <= pos <= 100 else ' out'
    pos = max(0, min(100, pos))
    stops_h = ''
    if stops:
        stops_h = '<span class="pr-sl">Select a price within the final range</span><div class="pr-st">%s</div>' % ''.join(
            '<button type="button" class="pr-s {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}">%s<b>%s</b></button>' % ((lambda k: (k, k, k))(U.new(i == 0, 'stop')) + (coin() if unit == 'DLP' else credit(), s)) for i, s in enumerate(stops))
    return ('<article class="pr-c %s%s"><header><span class="pr-ic">%s</span><span class="pr-k">%s</span>%s</header>%s'
            '<div class="pr-r"><span>Final permitted range</span><b>%s–%s %s</b></div><div class="pr-band"><span class="pr-tr"></span><span class="pr-pin%s" style="left: %.1f%%"><em>%s</em></span></div>'
            '<div class="pr-r sel"><span>Your selection</span><b>%s %s</b></div>%s</article>') % (
        'gold' if unit == 'DLP' else 'blue', '' if ok else ' bad', coin(True) if unit == 'DLP' else credit(True), kind,
        tag('%s Within range' % ck(10), 'green') if ok else tag('%s Outside range' % ic('x', 10, 2.6), 'red'), extra,
        '{:,}'.format(lo), '{:,}'.format(hi), unit, pos_cls, pos, '{:,}'.format(sel), '{:,}'.format(sel), unit, stops_h)

PSIDE_PRICE = '''<div class="cl-nx vb"><span class="vb-m">%s</span><b>Your course is validated</b><p>★ Gold Validated VAL-2026-00482 · final ranges reflect the validated course</p></div>'''.replace('★ ', '') % ic('badge', 22, 1.9)
PUB = {}
PUB['price'] = pside(0, PSIDE_PRICE) + ppanel('Your course is validated', 'Now confirm learner access. Credalio has set the final permitted ranges for your validated course.',
    '<div class="prs">%s%s</div>' % (range_card('Subscription', True, 700, 900, 800, 'DLP'), range_card('Marketplace', True, 130, 210, 170, 'Credits', '<div class="pr-r"><span>Maintenance burden</span><b>Medium</b></div>')),
    '<a class="ds-ghost cl-ch" href="STU-034.dc.html">Change Pricing</a>' + btn('Confirm Pricing', 'STU-061.dc.html', 'cl-go'))
PUB['priceout'] = pside(0, PSIDE_PRICE) + ppanel('Your course is validated', 'Now confirm learner access. Credalio has set the final permitted ranges for your validated course.',
    '<div class="prs">%s%s</div><p class="pr-w">%s<span>Your provisional price is no longer within the permitted range. Select another allowed value to continue.</span></p>' % (
        range_card('Subscription', False, 900, 1100, 700, 'DLP', stops=['900', '1,000', '1,100']), range_card('Marketplace', True, 170, 270, 170, 'Credits', '<div class="pr-r"><span>Maintenance burden</span><b>Medium</b></div>'), ic('warn', 16, 2.2)),
    '<a class="ds-ghost cl-ch" href="STU-034.dc.html">Change Pricing</a>' + btn('Confirm Pricing', 'STU-061.dc.html', 'cl-go'))
SPLIT = [((ME, 'AO'), 'Ada Ononuju', 'Lead Creator', 60, True), ((M1, 'JA'), 'Dr. John Adeyemi', 'Co-Creator', 25, False), ((None, 'AB'), 'ABC Institute', 'Content Contributor', 15, False)]
def donut():
    c = 2 * 3.14159 * 50; off = 0; segs = ''
    cols = ['#1652F0', '#5C86FF', '#AFC1F5']
    for i, (_, _, _, p, _) in enumerate(SPLIT):
        d = c * p / 100.0
        segs += '<circle class="dn-s" cx="60" cy="60" r="50" fill="none" stroke="%s" stroke-width="16" stroke-dasharray="%.1f %.1f" stroke-dashoffset="%.1f" transform="rotate(-90 60 60)" style="--i: %d"></circle>' % (cols[i], d - 2, c - d + 2, -off, i)
        off += d
    return '<svg class="dn" viewBox="0 0 120 120" width="150" height="150" aria-hidden="true">%s</svg>' % segs
PUB['revenue'] = pside(1, '''<div class="cl-nx rv"><span>Revenue split</span><div class="rv-d">%s<span class="rv-c"><b>100 %%</b><em>Total</em></span></div><ul>%s</ul></div>''' % (
        donut(), ''.join('<li><i style="background: %s"></i><span>%s</span><b>%d %%</b></li>' % (c, n, p) for c, (_, n, _, p, _) in zip(['#1652F0', '#5C86FF', '#AFC1F5'], SPLIT)))) + ppanel(
    'Revenue Confirmation', 'Every collaborator must accept the revenue split before a monetised course can go live.',
    '''<div class="sp"><div class="sp-r sp-hd"><span>Collaborator</span><span>Role</span><span>Share</span><span>Agreement</span></div>%s<div class="sp-r sp-tot"><span>Total</span><span></span><b>100 %%</b><span></span></div></div>
<div class="sp-w"><span class="sp-wi">%s</span><p>2 collaborators haven’t accepted yet. You can finish the other steps, but you can’t publish until they do.</p><button type="button" class="ds-ghost sm">%s<span>Send reminder</span></button></div>
<p class="py-note">Changing the split after publication needs everyone to accept again. Only the Lead Creator can change revenue distribution.</p>''' % (
        ''.join('<div class="sp-r"><span class="sp-n">%s<b>%s</b></span><span class="sp-ro">%s</span><b class="sp-p">%d %%</b>%s</div>' % (
            av(p[0], p[1], 32), n, r, s, tag('%s Accepted' % ck(10), 'green') if ok else tag('%s Pending' % ic('clock', 11, 2.2), 'amber')) for p, n, r, s, ok in SPLIT),
        ic('clock', 16, 2), ic('send', 14, 2) if 'send' in I else ''),
    bk('STU-060.dc.html') + '<a class="ds-link cl-ch" href="#">Edit split</a>' + btn('Continue to Marketplace Listing', 'STU-062.dc.html', 'cl-go'))
LF = [('Category', 'Technology · Data Analytics · SQL', 'Edit'), ('Skills', 'SQL, Data Analysis, Data Cleaning, Relational Databases', 'Edit'),
      ('Validated tier', 'Gold Validated', 'Locked · validation'), ('CEI', '92', 'Locked · calculated'),
      ('Creators', 'Ada Ononuju, Dr. John Adeyemi, ABC Institute', 'Edit'), ('Prepares for', 'No certification', 'Edit'),
      ('DLP access', '850 DLP', 'Edit'), ('Lifetime price', '500 Credits', 'Edit')]
LIVE_CARD = '''<div class="cl-nx lvp"><span>Live preview</span><article class="pv-c mk-c2"><span class="pv-cv"><i>SQL</i><em></em><em></em><em></em><span class="lvp-b">%s<span>Gold Validated</span></span><span class="lvp-cei">CEI 92</span></span>
<span class="mk-k">Data Analytics · Intermediate · Hybrid</span><b>Data Analysis with SQL</b><p>Write SQL to answer real business questions, from first query to a finished analysis.</p><p class="mk-by">%s<span>By Ada Ononuju, Dr. John Adeyemi, ABC Institute</span></p>
<span class="pv-sk"><i>SQL</i><i>Data Analysis</i><i>Data Cleaning</i><i>+1</i></span><span class="lvp-p"><span>%s<b>850</b> DLP</span><span>%s<b>500</b> Credits</span></span></article></div>''' % (
    ic('badge', 12, 2.2), stack([(ME, 'AO'), (M1, 'JA'), (None, 'AB')], 22), coin(), credit())
PUB['listing'] = pside(2, LIVE_CARD) + ppanel('Marketplace Listing', 'Most of this is already filled from your course. Edit the marketing copy; validation details are locked.',
    '''<div class="ls2"><label class="fl"><span class="fl-l">Title</span><input class="ds-in" value="Data Analysis with SQL" aria-label="Title"></label>
<label class="fl"><span class="fl-l">Short description</span><textarea class="ds-in" rows="2" aria-label="Short description">Write SQL to answer real business questions, from first query to a finished analysis.</textarea><span class="fl-f"><span class="cnt">85 / 160 characters</span></span></label>%s
<div class="fl"><span class="fl-l">Thumbnail</span><div class="cov"><span class="cov-i" aria-hidden="true">SQL</span><span class="cov-t"><b>sql-course-cover.png</b></span><a class="ds-link" href="#">Replace</a></div></div>
<dl class="lf">%s</dl></div>''' % (nova_sg('I can tighten your short description for search.'), ''.join('<div class="%s"><dt>%s</dt><dd>%s</dd>%s</div>' % (
        'lk' if a.startswith('Locked') else '', l, v, ('<span class="lf-l">%s%s</span>' % (ic('lock', 12, 2), a)) if a.startswith('Locked') else '<a class="ds-link sm" href="#">Edit</a>') for l, v, a in LF)),
    bk('STU-061.dc.html') + btn('Continue to Final Preview', 'STU-PRV.dc.html', 'cl-go'))
NEXT = [('search', 'Learners can find it in the marketplace', 'Search and browse listings usually update within minutes.'),
        ('badge', 'Your Gold badge and CEI are shown', 'Both appear on the course page and marketplace card.'),
        ('layers', 'Future edits are checked', 'Credalio tells you if a change needs revalidation before it goes live.')]
PUB['live'] = '''<div class="ko-wrap ob-in"><div class="ko">%s<span class="ko-pill">Public Marketplace</span><h1 class="ko-h1">Your course is live</h1><p class="ko-sub">Data Analysis with SQL</p>
<div class="lv-s">%s<span class="lv-cei"><b>CEI 92</b></span><span class="lv-pr">850 DLP · 500 Credits lifetime</span></div>
<section class="ko-card"><span class="ko-cl">What happens now</span><ul class="ko-nx">%s</ul></section>
<div class="ko-acts">%s<span class="ko-2"><a class="ds-ghost" href="#">Go to Manage</a><a class="ds-link" href="STU-001.dc.html">Create Another Experience</a></span></div></div></div>''' % (
    emblem(), GOLD, ''.join('<li><span class="ko-ni">%s</span><span><b>%s</b><em>%s</em></span></li>' % (ic(i, 17, 2) if i in EXTRA or i in I else '', t, d) for i, t, d in NEXT),
    btn('Share &amp; Promote', '#'))

def pub_body():
    blocks = []
    for k, h in PUB.items():
        inner = h if k == 'live' else '<div class="cl">%s</div>' % h
        blocks.append('<sc-if value="{{s_%s}}" hint-placeholder-val="{{ %s }}">%s</sc-if>' % (k, 'true' if k == 'price' else 'false', inner))
    return '''<div class="tk-root {{rootCls}}"><span class="cl-glow"></span>
<header class="tk-top"><a class="lp-x" href="STU-059.dc.html" aria-label="Close">%s</a><span class="lp-title"><span class="lp-t1">Publish your course</span></span><span style="flex-grow: 1"></span><a href="#" class="ds-tok" aria-label="72,450 Creio">%s<span>72.4K</span></a></header>
%s
</div>''' % (ic('x', 20, 2), COIN('tp', 26), '\n'.join(blocks))
PUB_JS = U.js() + '''class Component extends DCLogic {
  renderVals() {
    var s = this.props.step || 'price', v = togVals(this);
    %s.forEach(function (k) { v['s_'.concat(k)] = k === s; });
    v.rootCls = s === 'priceout' ? 'is-wait' : (s === 'live' ? 'is-ok' : '');
    return v;
  }
}''' % json.dumps(list(PUB))

# ======================================================================= CSS
VAL_CSS = r'''.wn{margin-top:14px;display:flex;align-items:center;gap:10px;padding:12px 16px;border-radius:14px;background:#FFF8EA;border:1.5px solid #F4DDAA;font-size:14px;color:#3A4566}
.wn svg{flex-shrink:0;color:#B76E00}
.wn b{font-weight:600;color:#0B1433}
.wn.info{background:#F5F8FF;border-color:#DCE5FB}
.wn.info svg{color:#1652F0}
.utabs{margin-top:20px;display:flex;gap:28px;border-bottom:1.5px solid #E6EAF3}
.ut{display:inline-flex;align-items:center;gap:8px;height:46px;margin-bottom:-1.5px;border-bottom:2.5px solid transparent;color:#5B6582;font-size:14.5px;font-weight:500;text-decoration:none;white-space:nowrap}
.ut:hover{color:#0B1433}
.ut.on{color:#0B1433;font-weight:600;border-bottom-color:#1652F0}
.ut.on svg{color:#1652F0}
.utabs{overflow-x:auto}
.vv-main{position:relative;isolation:isolate}
.vv-main::before{content:'';position:absolute;z-index:-1;left:0;right:0;top:-80px;height:320px;pointer-events:none;background:radial-gradient(60% 100% at 30% 0,rgba(22,82,240,.08),transparent 70%)}
.vv-main.tn-am::before{background:radial-gradient(60% 100% at 30% 0,rgba(214,140,20,.11),transparent 70%)}
.vv-main.tn-ok::before{background:radial-gradient(60% 100% at 50% 0,rgba(15,107,69,.10),transparent 70%)}
.lead{display:inline-flex;align-items:center;gap:4px;height:22px;padding:0 8px;border-radius:999px;background:#0B1433;color:#FFFFFF;font-size:11.5px;font-weight:500;vertical-align:1px;white-space:nowrap}
.lead svg{color:#F4C66A}
.ds-tag.red{background:#FDECEA;color:#B42318}
.vh-t{display:flex;align-items:flex-start;justify-content:space-between;gap:24px}
.vh-k{display:flex;align-items:center;gap:10px;margin-bottom:8px;font-size:13px}
.vh-k b{font-weight:600;color:#5B6582;font-variant-numeric:tabular-nums}
.vh-k > span{display:inline-flex;align-items:center;height:26px;padding:0 11px;border-radius:999px;font-weight:500;background:#EAF0FF;color:#0E3BB8}
.vh.am .vh-k > span{background:#FFF4E0;color:#8A5A00}
.vh-s{flex-shrink:0;display:inline-flex;align-items:center;gap:10px;max-width:320px;padding:12px 16px;border-radius:16px;background:#FFFFFF;border:1.5px solid #E6EAF3;font-size:13.5px;line-height:1.45;font-weight:500}
.vh-s.am{border-color:#F4DDAA;background:#FFFAF0;color:#6B4A00}
.vh-s i{width:10px;height:10px;flex-shrink:0;border-radius:50%;background:#E0A030;box-shadow:0 0 0 0 rgba(224,160,48,.5);animation:amP 1.8s ease-out infinite}
@keyframes amP{100%{box-shadow:0 0 0 8px rgba(224,160,48,0)}}
.vt{list-style:none;margin:22px 0 0 0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));position:relative;max-width:760px}
.vt::before{content:'';position:absolute;left:10px;right:calc(25% - 10px);top:10px;height:2px;background:#E6EAF3}
.vt::after{content:'';position:absolute;left:10px;top:10px;height:2px;width:calc(25% * var(--p));background:linear-gradient(90deg,#0F6B45,#1652F0);transform-origin:left;animation:vtG 1s cubic-bezier(.2,.8,.2,1) .3s both}
@keyframes vtG{from{transform:scaleX(0)}}
.vt li{position:relative;z-index:1;display:flex;flex-direction:column;align-items:flex-start;gap:8px;font-size:13px;font-weight:500;color:#8A93AD}
.vt i{width:22px;height:22px;box-sizing:border-box;border-radius:50%;border:2px solid #D6DDEE;background:#FFFFFF;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.vt .dn{color:#0F6B45}.vt .dn i{background:#0F6B45;border-color:#0F6B45}
.vt .on{color:#0B1433;font-weight:600}.vt .on i{border:6px solid #1652F0;animation:koPulse 1.8s ease-out infinite}
.vt.am .on i{border-color:#D99A1E;animation-name:amP}
@keyframes koPulse{0%{box-shadow:0 0 0 0 rgba(22,82,240,.35)}100%{box-shadow:0 0 0 9px rgba(22,82,240,0)}}
.vtabs{gap:24px;overflow-x:auto;scrollbar-width:none}
.vtabs::-webkit-scrollbar{display:none}
.vtabs .ut i{font-style:normal;min-width:20px;height:20px;padding:0 6px;box-sizing:border-box;border-radius:999px;background:#FFF4E0;color:#8A5A00;font-size:11.5px;font-weight:600;display:inline-flex;align-items:center;justify-content:center}
.vtabs + .wk{margin-top:20px}
.ok-n{display:flex;align-items:center;gap:16px;padding:18px 20px;background:linear-gradient(120deg,#F2FAF5,#FFFFFF 70%);border-color:#CFE8DB}
.ok-i{width:44px;height:44px;flex-shrink:0;border-radius:50%;background:#0F6B45;color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 6px #E7F5EE}
.ok-n b{font-size:16px;font-weight:600}
.ok-n p{margin:2px 0 0 0;font-size:14px;color:#3A4566}
.hn{list-style:none;margin:0;padding:0;position:relative;display:flex;flex-direction:column;gap:6px}
.hn::before{content:'';position:absolute;left:13px;top:14px;bottom:14px;width:2px;background:linear-gradient(180deg,#0F6B45 30%,#1652F0 30% 62%,#E6EAF3 62%)}
.hn li{position:relative;display:flex;align-items:center;gap:14px;min-height:44px;font-size:14.5px;color:#5B6582}
.hn-d{position:relative;z-index:1;width:28px;height:28px;flex-shrink:0;box-sizing:border-box;border-radius:50%;border:2px solid #D6DDEE;background:#FFFFFF;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.hn li.dn{color:#0B1433}.hn li.dn .hn-d{background:#0F6B45;border-color:#0F6B45}
.hn li.on{color:#0B1433;font-weight:600}.hn li.on .hn-d{border:7px solid #1652F0;animation:koPulse 1.8s ease-out infinite}
.ww p{margin:0;font-size:14.5px;line-height:1.6;color:#3A4566}
.ww-t{margin-top:14px;display:inline-flex;align-items:center;gap:8px;height:32px;padding:0 12px;border-radius:999px;background:#F5F8FF;color:#0E3BB8;font-size:13px;font-weight:500}
.mt{overflow:hidden}
.mt-v{position:relative;height:150px}
.mt-c{position:absolute;left:50%;top:50%;width:52px;height:52px;margin:-26px 0 0 -26px;border-radius:16px;background:linear-gradient(140deg,#1652F0,#0B1433);color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 14px 26px -12px rgba(22,82,240,.8)}
.mt-o{position:absolute;left:50%;top:50%;width:124px;height:124px;margin:-62px 0 0 -62px;border-radius:50%;border:1.5px dashed #BBCBF3;animation:rmSpin 30s linear infinite}
@keyframes rmSpin{to{transform:rotate(360deg)}}
.mt-r{position:absolute;width:32px;height:32px;border-radius:50%;background:#FFFFFF;border:1.5px solid #D6DDEE;color:#8A93AD;display:flex;align-items:center;justify-content:center;animation:mtS 4s ease-in-out infinite}
.mt-r.a{left:calc(50% - 76px);top:16px;color:#1652F0;border-color:#9DB8F7}.mt-r.b{right:calc(50% - 76px);top:16px;color:#1652F0;border-color:#9DB8F7;animation-delay:-1s}
.mt-r.c{left:calc(50% - 90px);bottom:20px;animation-delay:-2s}.mt-r.d{right:calc(50% - 90px);bottom:20px;animation-delay:-3s}
@keyframes mtS{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
.mt-l{display:flex;justify-content:space-between;gap:8px;font-size:12px;font-weight:500;color:#1652F0}
.cs-c dl{margin:0;display:flex;flex-direction:column}
.cs-c dl div{display:flex;justify-content:space-between;align-items:center;gap:10px;padding:9px 0;border-top:1.5px solid #F0F2F8;font-size:13px}
.cs-c dl div:first-child{border-top:0;padding-top:0}
.cs-c dt{color:#5B6582}
.cs-c dd{margin:0;display:flex;align-items:center;gap:6px;font-weight:600;text-align:right}
.cs-c .cr-c{width:16px;height:16px;font-size:9px}
.vrs{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.vr{position:relative;display:flex;flex-direction:column;gap:8px;padding:20px;border-radius:22px;background:#FFFFFF;border:1.5px solid #E6EAF3;animation:vrIn .6s cubic-bezier(.2,.8,.2,1) both;animation-delay:calc(var(--i) * 140ms + 150ms)}
@keyframes vrIn{from{opacity:0;transform:translateY(14px) scale(.98)}}
.vr:not(.off){border-color:#C9D7FA;background:linear-gradient(170deg,#F5F8FF,#FFFFFF 55%)}
.vr.off{background:#FBFCFE;border-style:dashed}
.vr-h{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px}
.vr-i{width:48px;height:48px;border-radius:16px;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 12px 22px -12px rgba(22,82,240,.9)}
.vr-i.sm{width:40px;height:40px;border-radius:13px;flex-shrink:0}
.vr.off .vr-i{background:#F1F3F8;color:#8A93AD;box-shadow:none}
.vr > b{font-size:16.5px;font-weight:600}
.vr-l{display:flex;align-items:center;flex-wrap:wrap;gap:6px;font-size:12.5px;color:#5B6582}
.vr p{margin:0;flex:1;font-size:13.5px;line-height:1.55;color:#3A4566}
.vr.off p,.vr.off > b{color:#5B6582}
.vr-s{margin-top:8px;padding-top:12px;border-top:1.5px solid #EEF1F7;display:flex;align-items:center;gap:8px;font-size:12.5px;color:#5B6582}
.vr-sh{width:26px;height:26px;border-radius:50%;background:#0B1433;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.vr.off .vr-sh{display:none}
.vr-s em{font-style:normal}
.vs3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.vs-t{display:flex;align-items:center;gap:14px;padding:16px 18px;border-radius:18px;background:#FFFFFF;border:1.5px solid #E6EAF3;color:#0B1433;text-decoration:none;transition:transform .2s ease,border-color .2s ease}
a.vs-t:hover{transform:translateY(-2px);border-color:#AFC1F5}
.vs-t > b{font-size:34px;font-weight:600;letter-spacing:-0.03em;color:#1652F0;line-height:1}
.vs-t.am{background:#FFF8EA;border-color:#F4DDAA}
.vs-t.am > b{color:#B76E00}
.vs-t > span:last-child{display:flex;flex-direction:column;gap:2px;font-size:13px;color:#5B6582}
.vs-t em{font-style:normal;font-size:14.5px;font-weight:600;color:#0B1433}
.vs-t b.sm{font-size:17px;font-weight:600;color:#0B1433}
.vs-t > span:last-child em{font-size:12.5px;font-weight:500;color:#5B6582}
.vs-t:has(b.sm) em{order:-1}
.vs-ic{width:40px;height:40px;flex-shrink:0;border-radius:13px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.vs-t.am .vs-ic{background:#FFFFFF;color:#B76E00}
.vs-ic.pr{background:none}
.na ul{list-style:none;margin:0;padding:0}
.na li{display:flex;align-items:center;gap:14px;padding:14px 0;border-top:1.5px solid #F0F2F8}
.na li:first-child{border-top:0;padding-top:0}
.na-i{width:40px;height:40px;flex-shrink:0;border-radius:13px;background:#FFF4E0;color:#B76E00;display:flex;align-items:center;justify-content:center}
.na-t{flex:1;min-width:0;display:flex;flex-direction:column;gap:3px}
.na-t b{font-size:15px;font-weight:600}
.na-t em{font-style:normal;font-size:13px;color:#5B6582;display:flex;align-items:center;flex-wrap:wrap;gap:6px}
.rp{display:flex;flex-direction:column;gap:14px}
.rp-r{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr) auto;align-items:center;gap:16px}
.rp-n{display:flex;align-items:center;flex-wrap:wrap;gap:8px}
.rp-n b{font-size:14.5px;font-weight:600}
.rp-b{height:8px;border-radius:8px;background:#EAF0FF;overflow:hidden}
.rp-b i{display:block;height:100%;width:var(--w);border-radius:8px;background:linear-gradient(90deg,#1652F0,#5C86FF);position:relative;overflow:hidden;transform-origin:left;animation:vtG 1s ease .3s both}
.rp-b i::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.6),transparent);transform:translateX(-100%);animation:rpSh 2.4s ease-in-out 1.4s infinite}
@keyframes rpSh{to{transform:translateX(100%)}}
.rqs{display:flex;flex-direction:column;gap:14px}
.rq{padding:20px 22px}
.rq.on{border-color:#C9D7FA;box-shadow:0 20px 40px -32px rgba(22,82,240,.6)}
.rq header{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
.rq-k{display:flex;align-items:center;flex-wrap:wrap;gap:8px;font-size:12.5px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:#1652F0}
.rq-k > span{text-transform:none;letter-spacing:0;font-weight:500;color:#5B6582;display:inline-flex;align-items:center;gap:6px}
.rq-k > span::before{content:'·';color:#AEB6CC}
.rq-m{display:flex;align-items:center;gap:8px}
.rq-d{display:inline-flex;align-items:center;gap:5px;font-size:12.5px;font-weight:500;color:#3A4566}
.rq-q{margin:14px 0 0 0;font-size:16px;line-height:1.5;font-weight:500}
.rq-x{display:block;margin-top:8px;font-size:12.5px;color:#8A93AD}
.rq-r{margin-top:16px;padding-top:16px;border-top:1.5px solid #F0F2F8;display:flex;flex-direction:column;gap:12px}
.rq-a{display:flex;align-items:center;justify-content:flex-end;gap:12px;margin-top:14px}
.rq-r .rq-a{margin-top:0}
.ds-btn.sm2{height:44px;font-size:14.5px;padding-left:20px;gap:12px}
.ds-btn.sm2 .ob-arrow{width:34px;height:34px}
.rq-go{display:inline-flex;align-items:center;gap:6px;margin-top:14px;font-size:14px}
.vn{display:flex;align-items:center;gap:10px;margin:0;font-size:13px;color:#5B6582}
.vn svg{flex-shrink:0;color:#8A93AD}
.up{margin-top:16px;display:grid;grid-template-columns:200px minmax(0,1fr);gap:16px}
.up-d{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;padding:18px;border-radius:18px;border:2px dashed #C9D7FA;background:#F7F9FF;cursor:pointer;text-align:center;transition:border-color .2s ease,background .2s ease}
.up-d:hover{border-color:#1652F0;background:#F2F6FF}
.up-i{width:46px;height:46px;margin-bottom:6px;border-radius:50%;background:#FFFFFF;color:#1652F0;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 18px -10px rgba(22,82,240,.7);animation:mtS 3s ease-in-out infinite}
.up-d b{font-size:14.5px;font-weight:600}
.up-d span:last-child{font-size:12.5px;color:#5B6582}
.up-f{display:flex;flex-direction:column;gap:12px}
.up-f textarea.ds-in{min-height:64px}
.emp{display:flex;flex-direction:column;align-items:center;gap:4px;padding:20px;border-radius:16px;background:#F7F9FD;text-align:center}
.emp-i{width:40px;height:40px;margin-bottom:6px;border-radius:12px;background:#FFFFFF;color:#8A93AD;display:flex;align-items:center;justify-content:center}
.emp b{font-size:14.5px;font-weight:600}
.emp > span:last-child{font-size:13px;color:#5B6582}
.au ol{list-style:none;margin:0;padding:0;position:relative}
.au ol::before{content:'';position:absolute;left:5px;top:8px;bottom:8px;width:2px;background:#E6EAF3}
.au li{position:relative;display:flex;gap:12px;padding:6px 0;animation:nrIn .5s ease both;animation-delay:calc(var(--i) * 90ms + 200ms)}
@keyframes nrIn{from{opacity:0;transform:translateY(6px)}}
.au-d{position:relative;z-index:1;width:12px;height:12px;flex-shrink:0;margin-top:3px;box-sizing:border-box;border-radius:50%;border:3px solid #FFFFFF;background:#1652F0;box-shadow:0 0 0 1.5px #C9D7FA}
.au-t{display:flex;flex-direction:column;gap:2px}
.au-t em{font-style:normal;font-size:11.5px;color:#8A93AD}
.au-t b{font-size:13px;font-weight:500}
.mr{padding:22px 24px}
.mr header{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
.mr h2{margin:14px 0 0 0;font-size:21px;font-weight:600;letter-spacing:-0.015em}
.mr-by{margin:6px 0 0 0;display:flex;align-items:center;flex-wrap:wrap;gap:6px;font-size:13.5px;color:#5B6582}
.mr-g{margin-top:18px;display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,1fr) auto;gap:10px}
.mr-k{display:flex;flex-direction:column;gap:6px;padding:12px 14px;border-radius:14px;background:#F7F9FD}
.mr-k span{font-size:12px;color:#5B6582}
.mr-k b{font-size:13.5px;font-weight:600}
.mr-p{display:flex;flex-wrap:wrap;gap:5px}
.mr-p i{font-style:normal;height:24px;display:inline-flex;align-items:center;padding:0 9px;border-radius:999px;background:#FFFFFF;border:1.5px solid #E6EAF3;font-size:12px;font-weight:500}
.mr-w{margin:16px 0 0 0;font-size:14.5px;line-height:1.6;color:#3A4566}
.mr-sl{display:block;margin:18px 0 10px 0;font-size:13px;font-weight:600}
.sls{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.sl{position:relative;display:flex;flex-direction:column;align-items:flex-start;gap:0;padding:14px 16px;border-radius:16px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:inherit;color:#0B1433;text-align:left;cursor:pointer;transition:border-color .2s ease,background .2s ease}
.sl:hover{border-color:#AFC1F5}
.sl em{font-style:normal;font-size:12px;font-weight:500;color:#5B6582}
.sl b{font-size:26px;font-weight:600;letter-spacing:-0.02em;line-height:1.2}
.sl span{font-size:13px;color:#3A4566}
.sl i{position:absolute;top:12px;right:12px;width:22px;height:22px;border-radius:50%;background:#1652F0;color:#FFFFFF;display:none;align-items:center;justify-content:center}
.sl.on{border-color:#1652F0;background:#F5F8FF}
.sl.on i{display:flex}
.ff{display:flex;flex-wrap:wrap;align-items:center;gap:10px 14px}
.ff-l{font-size:13px;font-weight:500;color:#5B6582}
.ff .ds-seg button{padding:0 12px;font-size:13px;height:34px;white-space:nowrap}
.ft{padding:6px 20px}
.ft-r{display:grid;grid-template-columns:118px minmax(0,1fr) 168px 128px;align-items:center;gap:14px;padding:14px 0;border-top:1.5px solid #F0F2F8;color:#0B1433;text-decoration:none}
.ft-r:first-child{border-top:0}
a.ft-r{margin:0 -10px;padding:14px 10px;border-radius:14px;transition:background .2s ease}
a.ft-r:hover{background:#F7F9FD}
.ft-hd{font-size:12.5px;font-weight:500;color:#8A93AD;padding:10px 0}
.ft-id{font-size:12.5px;font-weight:500;color:#5B6582;font-variant-numeric:tabular-nums}
.ft-f{display:flex;flex-direction:column;gap:3px;min-width:0}
.ft-f b{font-size:14.5px;font-weight:500;line-height:1.45}
.ft-f em{font-style:normal;font-size:12px;color:#8A93AD;font-variant-numeric:tabular-nums}
.ft-r.ob .ft-f b{color:#3A4566}
.ft-rs{display:flex;flex-direction:column;gap:2px;font-size:13px}
.ft-rs em{font-style:normal;color:#5B6582;font-size:12.5px}
.ft-r .ds-tag{justify-self:start}
.sv-b{display:inline-flex;align-items:center;gap:6px;height:24px;padding:0 9px;border-radius:7px;font-size:11.5px;font-weight:600;letter-spacing:.03em;text-transform:uppercase;justify-self:start}
.sv-b::before{content:'';width:6px;height:6px;border-radius:50%;background:currentColor}
.sv-b.mj{background:#FDECEA;color:#B42318}
.sv-b.mn{background:#FFF4E0;color:#8A5A00}
.sv-b.ob{background:#E7F5EE;color:#0F6B45}
.fs-b{display:flex;gap:3px;height:10px}
.fs-b i{border-radius:5px;transform-origin:left;animation:vtG .8s ease .3s both}
.fs-b i.mj,.fs ul i.mj{background:#D92D20}.fs-b i.mn,.fs ul i.mn{background:#E0A030}.fs-b i.ob,.fs ul i.ob{background:#0F6B45}
.fs ul{list-style:none;margin:14px 0 0 0;padding:0;display:flex;flex-direction:column;gap:8px}
.fs li{display:flex;align-items:center;gap:10px;font-size:13.5px}
.fs li i{width:8px;height:8px;border-radius:50%}
.fs li span{flex:1;color:#3A4566}
.fs li b{font-weight:600}
.ap ol{list-style:none;margin:0;padding:0;position:relative}
.ap li{display:grid;grid-template-columns:32px minmax(0,1fr) auto;align-items:center;gap:16px;padding:16px 0;border-top:1.5px solid #F0F2F8;animation:nrIn .5s ease both;animation-delay:calc(var(--i) * 110ms + 200ms)}
.ap li:first-child{border-top:0;padding-top:0}
.ap-n{width:32px;height:32px;box-sizing:border-box;border-radius:50%;border:2px dashed #CBD3E6;color:#5B6582;font-size:13px;font-weight:600;display:flex;align-items:center;justify-content:center}
.ap-b{min-width:0}
.ap-m{display:flex;align-items:center;flex-wrap:wrap;gap:10px}
.ap-m em{font-style:normal;font-size:12.5px;color:#5B6582}
.ap-b p,.cm2 p{margin:8px 0 0 0;font-size:14.5px;line-height:1.5}
.ap .ds-ghost{gap:6px}
.rv-e{display:inline-flex !important;align-items:center;gap:8px;color:#B76E00 !important}
.rv-dot{width:8px;height:8px;border-radius:50%;background:#E0A030;animation:amP 1.8s ease-out infinite}
.rv-p{display:inline-flex;align-items:center;gap:10px;height:52px;padding:0 16px 0 8px;border-radius:999px;background:#FFFFFF;border:1.5px solid #E6EAF3;font-size:13.5px;color:#5B6582}
.rv-p b{font-size:16px;color:#0B1433}
.rvw{margin-top:24px;display:grid;grid-template-columns:260px minmax(0,1fr);gap:20px;align-items:start}
.rvl{display:flex;flex-direction:column;gap:8px;position:sticky;top:92px}
.rvl-i{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:6px 8px;padding:14px;border-radius:16px;background:#FFFFFF;border:1.5px solid #E6EAF3;color:#0B1433;text-decoration:none}
.rvl-i .sv-b{grid-column:1}
.rvl-i .ds-tag{grid-row:1;grid-column:2}
.rvl-i b{grid-column:1 / -1;font-size:14px;font-weight:600}
.rvl-i em{grid-column:1 / -1;font-style:normal;font-size:12.5px;color:#5B6582}
.rvl-i.on{border-color:#1652F0;background:#F5F8FF;box-shadow:inset 3px 0 0 #1652F0}
.rvc{display:flex;flex-direction:column;min-width:0}
.vf{padding:18px 20px;border-color:#F5C2BD;background:linear-gradient(160deg,#FFF7F6,#FFFFFF 60%)}
.vf-k{display:flex;align-items:center;flex-wrap:wrap;gap:10px;font-size:12.5px;font-weight:500;color:#5B6582}
.vf p{margin:10px 0 0 0;font-size:16px;line-height:1.5;font-weight:500}
.vf em{display:block;margin-top:8px;font-style:normal;font-size:12.5px;color:#8A93AD}
.rv-ln{align-self:center;width:2px;height:22px;background:repeating-linear-gradient(180deg,#D92D20 0 4px,transparent 4px 8px);opacity:.5}
.ac{padding:18px 20px 20px 20px}
.ac-h{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:8px}
.ac-h .rx-k{margin:0}
.ac-h .ds-link{display:inline-flex;align-items:center;gap:5px}
.ac-t{display:block;font-size:16px;font-weight:600}
.rb{list-style:none;margin:12px 0 0 0;padding:0;display:flex;flex-direction:column;gap:8px}
.rb li{display:grid;grid-template-columns:18px minmax(0,1fr) auto;align-items:center;gap:12px;padding:12px 14px;border-radius:14px;background:#F7F9FD;font-size:14.5px}
.rb-g{color:#AEB6CC;display:flex}
.rb b{font-weight:500}
.rb em{font-style:normal;font-size:12.5px;font-weight:500;color:#0E3BB8;padding:3px 8px;border-radius:999px;background:#EAF0FF}
.rb li.add{display:block;padding:0;background:none}
.rb li.add button{width:100%;display:flex;align-items:center;gap:10px;padding:13px 14px;border-radius:14px;border:1.5px dashed #9DB8F7;background:#FFFFFF;font-family:inherit;font-size:14.5px;font-weight:600;color:#1652F0;text-align:left;cursor:pointer;animation:addG 2.6s ease-in-out infinite}
.rb li.add.on button{border-style:solid;border-color:#1652F0;background:#F5F8FF;animation:none}
@keyframes addG{50%{box-shadow:0 0 0 4px rgba(22,82,240,.1)}}
.ac-n{margin-top:16px}
.ac-n textarea.ds-in{min-height:70px}
.cm2{list-style:none;margin:0;padding:0}
.cm2 li{display:grid;grid-template-columns:18px minmax(0,1fr) auto;align-items:start;gap:14px;padding:14px 0;border-top:1.5px solid #F0F2F8}
.cm2 li:first-child{border-top:0;padding-top:0}
.cm2 li > .st{margin-top:3px}
.cm2 p b{font-weight:600;color:#8A5A00}
.ws-l{display:block;margin:18px 0 10px 0;font-size:12.5px;font-weight:500;color:#8A93AD}
.evf{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.evf-i{display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:14px;background:#F7F9FD}
.evf-i svg{flex-shrink:0;color:#1652F0}
.evf-i span{display:flex;flex-direction:column;gap:2px;min-width:0}
.evf-i b{font-size:13.5px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.evf-i em{font-style:normal;font-size:12px;color:#5B6582}
.rs-w{display:inline-flex;align-items:center;gap:8px;color:#8A5A00}
.rs-w svg{color:#B76E00}
.ds-btn.is-dis{background:#C9D2E6;box-shadow:none;cursor:not-allowed}
.ds-btn.is-dis:hover{background:#C9D2E6;transform:none}
.ds-btn.is-dis .ob-arrow{color:#8A93AD}
.rvx-v{display:flex;align-items:center;gap:8px;margin-bottom:12px}
.rvx-v span{height:30px;display:inline-flex;align-items:center;padding:0 12px;border-radius:999px;background:#F1F3F8;font-size:13px;font-weight:600;color:#5B6582}
.rvx-v span.on{background:#1652F0;color:#FFFFFF}
.rvx-v i{flex:1;height:2px;background:repeating-linear-gradient(90deg,#9DB8F7 0 5px,transparent 5px 9px);background-size:18px 2px;animation:rvM 1s linear infinite}
@keyframes rvM{to{background-position:18px 0}}
.rvx dl{margin:0;display:flex;flex-direction:column}
.rvx dl div{display:flex;flex-direction:column;gap:2px;padding:9px 0;border-top:1.5px solid #F0F2F8}
.rvx dt{font-size:12px;color:#8A93AD}
.rvx dd{margin:0;font-size:13.5px;font-weight:500}
.ko-page{max-width:1000px;margin:0 auto}
.ko-in .ko{display:flex;flex-direction:column;align-items:center;text-align:center;--k:#0F6B45;--kb:#E7F5EE;padding-top:8px}
.ko-h1{margin:14px 0 0 0;font-size:36px;line-height:1.12;font-weight:600;letter-spacing:-0.03em}
.ko-sub{margin:10px 0 0 0;font-size:15px;color:#4A5578}
.ko-pill.gold{gap:6px;background:linear-gradient(135deg,#F7D98B,#C9952C);color:#3D2700}
.dg{margin-top:28px;display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:16px;text-align:left}
.dg .fc{margin:0}
.vrp-r{display:flex;align-items:center;gap:14px;padding:14px 0;border-top:1.5px solid #F0F2F8}
.vrp-r:nth-child(2){border-top:0;padding-top:0}
.vrp-t{flex:1;min-width:0;display:flex;flex-direction:column;gap:3px}
.vrp-t b{display:flex;align-items:center;flex-wrap:wrap;gap:6px;font-size:14.5px;font-weight:600}
.vrp-t em{font-style:normal;font-size:13px;color:#5B6582}
.vrp-f{margin-top:6px;padding:12px 14px;border-radius:14px;background:#F7F9FD;display:flex;flex-direction:column;gap:3px}
.vrp-f span{font-size:12px;color:#8A93AD}
.vrp-f b{font-size:13.5px;font-weight:600}
.vrp .fc-h{align-items:center}
.wm ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:14px}
.wm li{display:flex;gap:12px}
.wm-i{width:36px;height:36px;flex-shrink:0;border-radius:12px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.wm li:first-child .wm-i{background:linear-gradient(135deg,#F7D98B,#C9952C);color:#3D2700}
.wm li span:last-child{display:flex;flex-direction:column;gap:2px}
.wm b{font-size:14.5px;font-weight:600}
.wm em{font-style:normal;font-size:13.5px;line-height:1.5;color:#5B6582}
.ko-page > .sv{margin-top:24px;justify-content:center;background:none;border:0;box-shadow:none;backdrop-filter:none;-webkit-backdrop-filter:none}
.ko-page > .sv .sv-s{display:none}
@media (max-width: 1180px){.vrs{grid-template-columns:minmax(0,1fr)}}
@media (max-width: 960px){
.vh-t{flex-direction:column;gap:14px}
.ap li{align-items:start}
.vrp-r{flex-wrap:wrap}
.vrp-r > .ds-tag{margin-left:54px}
.vv-main .wk-r > .cs-c,.vv-main .wk-r > .mt{display:none}
.vv-main .wk-r > .rn{order:3}
.vh-s{max-width:none}
.vt{margin-top:18px}
.vt li{font-size:11.5px;align-items:center;text-align:center}
.vt li:first-child{align-items:flex-start;text-align:left}
.vt::before{left:12.5%}
.vt li span{max-width:80px}
.vt{grid-template-columns:repeat(4,minmax(0,1fr))}
.vt::before,.vt::after{left:11px}
.vtabs{margin:16px -16px 0 -16px;padding:0 16px;gap:20px}
.ok-n{padding:16px}
.vs3{display:flex;overflow-x:auto;margin:0 -16px;padding:0 16px 4px 16px;gap:10px;scrollbar-width:none}
.vs3::-webkit-scrollbar{display:none}
.vs-t{flex:0 0 76%;box-sizing:border-box}
.na li{flex-wrap:wrap}
.na-t{flex-basis:calc(100% - 54px)}
.na li .ds-ghost{margin-left:54px}
.rp-r{grid-template-columns:minmax(0,1fr) auto;gap:8px 12px}
.rp-b{grid-column:1 / -1;grid-row:2}
.rq{padding:16px}
.rq-q{font-size:15px}
.rq-a{flex-direction:column-reverse;align-items:stretch}
.rq-a .ds-btn{justify-content:space-between}
.up{grid-template-columns:minmax(0,1fr)}
.mr{padding:16px}
.mr h2{font-size:18px}
.mr-g{grid-template-columns:minmax(0,1fr)}
.sls{grid-template-columns:minmax(0,1fr);gap:8px}
.sl{flex-direction:row;align-items:baseline;gap:10px;padding:12px 14px}
.sl b{font-size:20px}
.sl i{top:50%;margin-top:-11px}
.ff{flex-direction:column;align-items:stretch;gap:8px}
.ff .ds-seg{overflow-x:auto;scrollbar-width:none}
.ff .ds-seg button{flex-shrink:0}
.ft{padding:2px 16px}
.ft-hd{display:none}
.ft-r{grid-template-columns:minmax(0,1fr) auto;gap:6px 10px}
a.ft-r{margin:0 -8px;padding:14px 8px}
.ft-r .sv-b{grid-column:1;grid-row:1}
.ft-r .ds-tag{grid-column:2;grid-row:1;justify-self:end}
.ft-f{grid-column:1 / -1}
.ft-rs{grid-column:1 / -1;flex-direction:row;flex-wrap:wrap;gap:4px 8px}
.ap li{grid-template-columns:28px minmax(0,1fr);gap:10px 12px}
.ap-n{width:28px;height:28px}
.ap li .ds-ghost{grid-column:2;justify-self:start}
.pg-hr:has(.rv-p){width:100%}
.rvw{grid-template-columns:minmax(0,1fr);gap:14px}
.rvl{position:static;flex-direction:row;overflow-x:auto;margin:0 -16px;padding:0 16px 2px 16px;scrollbar-width:none}
.rvl::-webkit-scrollbar{display:none}
.rvl-i{flex:0 0 72%;box-sizing:border-box}
.vf,.ac{padding:16px}
.cm2 li{grid-template-columns:18px minmax(0,1fr);gap:10px}
.cm2 li .ds-ghost{grid-column:2;justify-self:start}
.evf{grid-template-columns:minmax(0,1fr)}
.ko-h1{font-size:26px}
.dg{grid-template-columns:minmax(0,1fr);margin-top:22px}
.vrp .fc-h{flex-direction:column;align-items:flex-start;gap:6px}
}
'''

PUB_CSS = open(os.path.join(HERE, 'submit_base.css')).read() + r'''
.cl{grid-template-columns:minmax(0,1fr) 620px}
.pb-k{font-size:13px;font-weight:600;color:#1652F0}
.cl-meta{align-items:center}
.gb{display:inline-flex !important;align-items:center;gap:6px;height:28px;padding:0 11px;border-radius:999px;background:linear-gradient(135deg,#F7D98B,#C9952C) !important;color:#3D2700 !important;font-size:12.5px;font-weight:600}
.cl-steps{max-width:460px}
.cl-nx{margin-top:32px}
.cl-nx > span{display:block;margin-bottom:12px;font-size:12.5px;font-weight:500;color:#8A93AD}
.vb{display:flex;flex-direction:column;align-items:flex-start;gap:6px;background:linear-gradient(160deg,#FFFAEB,#FFFFFF 70%);border-color:#F0DDAE}
.cl-nx > span.vb-m{display:flex;margin:0 0 6px 0}
.gb span{background:none !important;padding:0 !important;height:auto !important;color:inherit !important;font-weight:600 !important}
.vb-m{width:52px;height:52px;margin-bottom:6px;border-radius:50%;background:linear-gradient(135deg,#F7D98B,#C9952C);color:#3D2700;display:flex;align-items:center;justify-content:center;box-shadow:0 12px 24px -12px rgba(160,110,20,.8);animation:vbS 4s ease-in-out infinite}
@keyframes vbS{50%{transform:rotate(-8deg) scale(1.04)}}
.vb b{font-size:15.5px;font-weight:600;color:#5A3B00}
.vb p{margin:0;font-size:13.5px;line-height:1.5;color:#6B4A00}
.prs{margin-top:18px;display:flex;flex-direction:column;gap:12px}
.pr-c{padding:16px 18px;border-radius:18px;border:1.5px solid #E6EAF3;background:#FFFFFF}
.pr-c header{display:flex;align-items:center;gap:10px;margin-bottom:10px}
.pr-ic{display:flex}
.pr-k{flex:1;font-size:13px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:#5B6582}
.pr-c .ds-tag svg{width:10px;height:10px}
.pr-c.bad{border-color:#F5C2BD;background:linear-gradient(160deg,#FFF7F6,#FFFFFF 60%)}
.ds-tag.red{background:#FDECEA;color:#B42318}
.pr-r{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:6px 0;font-size:14px;color:#5B6582}
.pr-r b{font-size:15px;font-weight:600;color:#0B1433;font-variant-numeric:tabular-nums}
.pr-r.sel b{font-size:18px}
.pr-c.bad .pr-r.sel b{color:#B42318;text-decoration:line-through;text-decoration-thickness:1.5px}
.pr-band{position:relative;height:34px;margin:4px 0}
.pr-tr{position:absolute;left:0;right:0;top:15px;height:6px;border-radius:6px}
.gold .pr-tr{background:linear-gradient(90deg,#FFE7A8,#E8B44A)}
.blue .pr-tr{background:linear-gradient(90deg,#C9D7FA,#1652F0)}
.pr-pin{position:absolute;top:6px;width:4px;height:24px;margin-left:-2px;border-radius:4px;background:#0B1433;box-shadow:0 0 0 3px #FFFFFF;animation:pnD .8s cubic-bezier(.2,.9,.3,1.4) .3s both}
@keyframes pnD{from{transform:translateY(-10px);opacity:0}}
.pr-pin em{position:absolute;bottom:calc(100% + 2px);left:50%;transform:translateX(-50%);font-style:normal;font-size:11px;font-weight:600;color:#0B1433;white-space:nowrap;display:none}
.pr-pin.out{background:#D92D20}
.pr-sl{display:block;margin:10px 0 8px 0;font-size:13px;font-weight:600}
.pr-st{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
.pr-s{display:flex;align-items:center;justify-content:center;gap:8px;height:46px;border-radius:14px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:inherit;color:#0B1433;cursor:pointer}
.pr-s b{font-size:16px;font-weight:600}
.pr-s .dlp-c{width:18px;height:18px}
.pr-s.on{border-color:#1652F0;background:#F5F8FF;box-shadow:0 0 0 3px rgba(22,82,240,.12)}
.pr-w{margin:14px 0 0 0;display:flex;align-items:center;gap:10px;padding:12px 14px;border-radius:14px;background:#FDECEA;color:#912018;font-size:13.5px;font-weight:500}
.pr-w svg{flex-shrink:0;color:#B42318}
.cl-ch{margin-right:auto}
.cl-bk + .cl-ch{margin-left:0}
.cl-foot .ds-link.cl-ch{margin-left:12px}
.rv-d{position:relative;width:150px;height:150px;margin:0 auto 14px auto}
.dn-s{animation:dnIn 1s cubic-bezier(.2,.8,.2,1) both;animation-delay:calc(var(--i) * 180ms + 200ms)}
@keyframes dnIn{from{stroke-dasharray:0 400}}
.rv-c{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}
.rv-c b{font-size:22px;font-weight:600}
.rv-c em{font-style:normal;font-size:12px;color:#5B6582}
.rv ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:8px}
.rv li{display:flex;align-items:center;gap:10px;font-size:13.5px}
.rv li i{width:10px;height:10px;border-radius:3px}
.rv li span{flex:1;color:#3A4566}
.rv li b{font-weight:600}
.sp{margin-top:18px;border:1.5px solid #E6EAF3;border-radius:18px;padding:2px 16px}
.sp-r{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr) 64px 112px;align-items:center;gap:12px;padding:12px 0;border-top:1.5px solid #F0F2F8}
.sp-r:first-child{border-top:0}
.sp-hd{font-size:12px;font-weight:500;color:#8A93AD;padding:10px 0}
.sp-n{display:flex;align-items:center;gap:10px;min-width:0}
.sp-n b{font-size:14px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sp-ro{font-size:13px;color:#5B6582}
.sp-p{font-size:16px;font-weight:600;font-variant-numeric:tabular-nums}
.sp-r .ds-tag{justify-self:start}
.sp-r .ds-tag svg{width:11px;height:11px}
.sp-tot{border-top:1.5px solid #D6DDEE}
.sp-tot > span:first-child{font-weight:600}
.sp-tot b{font-size:16px;font-weight:600}
.sp-w{margin-top:14px;display:flex;align-items:center;gap:12px;padding:14px 16px;border-radius:16px;background:#FFF8EA;border:1.5px solid #F4DDAA}
.sp-wi{width:36px;height:36px;flex-shrink:0;border-radius:50%;background:#FFFFFF;color:#B76E00;display:flex;align-items:center;justify-content:center}
.sp-w p{flex:1;margin:0;font-size:13.5px;line-height:1.5;color:#6B4A00}
.sp-w .ds-ghost{background:#FFFFFF;gap:6px;flex-shrink:0}
.py-note{margin:12px 0 0 0;font-size:13px;line-height:1.5;color:#5B6582}
.ls2{margin-top:18px;display:flex;flex-direction:column;gap:16px}
.ls2 textarea.ds-in{min-height:0}
.fl-f{display:flex;align-items:center;justify-content:flex-end;gap:12px}
.ls2 .nv-sg{margin-top:-6px;padding:10px 14px}
.ls2 .nv-sg p{font-size:13.5px}
.cnt{font-size:12px;color:#8A93AD}
.cov{display:flex;align-items:center;gap:14px;height:56px;padding:0 16px 0 6px;border-radius:12px;border:1.5px solid #D6DDEE}
.cov-i{width:58px;height:42px;border-radius:9px;background:linear-gradient(140deg,#1652F0,#0B1433);color:#FFFFFF;font-size:11px;font-weight:600;display:flex;align-items:center;justify-content:center}
.cov-t{flex:1;min-width:0}
.cov-t b{font-size:14px;font-weight:600}
.lf{margin:0;border:1.5px solid #E6EAF3;border-radius:18px;padding:2px 16px}
.lf div{display:grid;grid-template-columns:120px minmax(0,1fr) auto;align-items:center;gap:12px;padding:11px 0;border-top:1.5px solid #F0F2F8}
.lf div:first-child{border-top:0}
.lf dt{font-size:13px;color:#5B6582}
.lf dd{margin:0;font-size:14px;font-weight:500}
.lf .lk dd{font-weight:600}
.lf-l{display:inline-flex;align-items:center;gap:5px;font-size:12px;font-weight:500;color:#8A93AD;white-space:nowrap}
.lvp{padding:18px}
.mk-c2{position:relative;display:block;border-radius:18px;border:1.5px solid #E6EAF3;overflow:hidden;background:#FFFFFF;box-shadow:0 26px 50px -30px rgba(22,82,240,.6);animation:obIn .6s ease .3s both}
.pv-cv{position:relative;display:block;height:124px;overflow:hidden;background:radial-gradient(circle at 85% 20%,rgba(92,134,255,.75),rgba(92,134,255,0) 55%),linear-gradient(140deg,#1652F0,#0B1433)}
.pv-cv i{position:absolute;left:16px;bottom:10px;font-style:normal;font-size:30px;font-weight:600;letter-spacing:-0.03em;color:#FFFFFF}
.pv-cv em{position:absolute;right:16px;height:6px;border-radius:6px;background:rgba(255,255,255,.22)}
.pv-cv em:nth-of-type(1){top:50px;width:84px}.pv-cv em:nth-of-type(2){top:64px;width:56px;background:rgba(255,255,255,.4)}.pv-cv em:nth-of-type(3){top:78px;width:70px}
.lvp-b{position:absolute;left:12px;top:12px;display:inline-flex;align-items:center;gap:5px;height:24px;padding:0 9px;border-radius:999px;background:linear-gradient(135deg,#F7D98B,#C9952C);color:#3D2700;font-size:11.5px;font-weight:600}
.lvp-cei{position:absolute;right:12px;top:12px;height:24px;display:inline-flex;align-items:center;padding:0 9px;border-radius:999px;background:rgba(255,255,255,.16);color:#FFFFFF;font-size:11.5px;font-weight:600}
.mk-k{display:block;padding:12px 14px 0 14px;font-size:11.5px;font-weight:500;color:#5B6582}
.mk-c2 > b{display:block;padding:4px 14px 0 14px;font-size:16px;font-weight:600}
.mk-c2 > p{margin:4px 0 0 0;padding:0 14px;font-size:13px;line-height:1.5;color:#5B6582}
.mk-by{display:flex;align-items:center;gap:8px;font-size:12.5px !important}
.mk-by .avs .av + .av{margin-left:-6px}
.pv-sk{display:flex;flex-wrap:wrap;gap:6px;padding:10px 14px 0 14px}
.pv-sk i{font-style:normal;font-size:12px;font-weight:500;padding:4px 9px;border-radius:999px;background:#F5F8FF;color:#0E3BB8}
.lvp-p{margin-top:12px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));border-top:1.5px solid #F0F2F8}
.lvp-p > span{display:flex;align-items:center;gap:6px;padding:12px 14px;font-size:12.5px;color:#5B6582}
.lvp-p > span + span{border-left:1.5px solid #F0F2F8}
.lvp-p b{font-size:16px;font-weight:600;color:#0B1433}
.lvp-p .dlp-c{width:18px;height:18px}
.ko-wrap{flex-grow:1;display:flex;justify-content:center;padding:44px 24px 64px 24px}
.ko{--k:#0F6B45;--kb:#E7F5EE;width:min(620px,100%);display:flex;flex-direction:column;align-items:center;text-align:center}
.ko-h1{margin:14px 0 0 0;font-size:38px;line-height:1.12;font-weight:600;letter-spacing:-0.03em}
.ko-sub{margin:8px 0 0 0;font-size:17px;font-weight:500;color:#3A4566}
.lv-s{margin-top:16px;display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:8px}
.lv-cei{height:28px;display:inline-flex;align-items:center;padding:0 11px;border-radius:999px;background:#0B1433;color:#FFFFFF;font-size:12.5px}
.lv-cei b{font-weight:600}
.lv-pr{height:28px;display:inline-flex;align-items:center;padding:0 11px;border-radius:999px;background:#F1F3F8;color:#3A4566;font-size:12.5px;font-weight:500}
.ko-card{margin-top:26px;width:100%;box-sizing:border-box;padding:18px 22px;border-radius:20px;border:1.5px solid #E6EAF3;background:#FFFFFF;text-align:left}
.ko-cl{display:block;margin-bottom:12px;font-size:12.5px;font-weight:500;color:#8A93AD}
.ko-nx{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:14px}
.ko-nx li{display:flex;gap:12px}
.ko-ni{width:36px;height:36px;flex-shrink:0;border-radius:12px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.ko-nx li span:last-child{display:flex;flex-direction:column;gap:2px}
.ko-nx b{font-size:14.5px;font-weight:600}
.ko-nx em{font-style:normal;font-size:13.5px;color:#5B6582}
.ko-acts{margin-top:26px;display:flex;flex-direction:column;align-items:center;gap:14px}
.ko-2{display:flex;align-items:center;gap:18px}
@media (max-width: 960px){
.cl{display:flex;flex-direction:column;gap:20px}
.cl-side{display:contents}
.cl-side > *{order:0}
.cl-panel{order:1}
.cl-nx{order:2;margin-top:4px;padding:16px}
.cl-steps li span{display:none}
.cl-steps li.on span{display:block;white-space:nowrap}
.pr-st{gap:6px}
.cl-nx.vb{display:none}
.sp{padding:2px 12px}
.sp-r{grid-template-columns:minmax(0,1fr) auto;gap:6px 10px}
.sp-hd{display:none}
.sp-ro{grid-column:1;grid-row:2;padding-left:42px;font-size:12.5px}
.sp-p{grid-column:2;grid-row:1;text-align:right}
.sp-r .ds-tag{grid-column:2;grid-row:2;justify-self:end}
.sp-tot .sp-ro,.sp-tot span:nth-child(4){display:none}
.sp-w{flex-wrap:wrap}
.sp-w p{flex-basis:calc(100% - 48px)}
.sp-w .ds-ghost{width:100%;justify-content:center}
.lf{padding:2px 12px}
.lf div{grid-template-columns:minmax(0,1fr) auto;gap:2px 10px}
.lf dd{grid-column:1;grid-row:2}
.lf div > :last-child{grid-row:1 / span 2;grid-column:2}
.cl-foot{flex-wrap:wrap}
.cl-ch{order:3;width:100%;justify-content:center;margin:0 !important}
.ko-wrap{padding:32px 16px 40px 16px}
.ko-h1{font-size:28px}
.ko-card{padding:16px}
.ko-acts{width:100%}
.ko-acts .ds-btn{width:100%;justify-content:space-between}
.ko-2{flex-direction:column;width:100%;gap:8px}
.ko-2 .ds-ghost{width:100%}
}
'''

write('Validate.dc.html', doc('Course Studio · Validate · shared source', kit.KIT_CSS + '\n' + dash.DASH_CSS + BASE_CSS + CW_CSS + WK_CSS + VAL_CSS, val_body(), VAL_JS))
write('Publish.dc.html', doc('Publish your course · shared source', kit.KIT_CSS + '\n' + dash.DASH_CSS + BASE_CSS + PUB_CSS, pub_body(), PUB_JS))

BOARDS = [
    ('STU-053', 'Validate', {'page': 'wait'}, 'CR-STU-053 · Awaiting assignment'),
    ('STU-054', 'Validate', {'page': 'assigned'}, 'CR-STU-054 · Validators assigned (roles)'),
    ('STU-055', 'Validate', {'page': 'ws'}, 'CR-STU-055 · Validation workspace · overview'),
    ('STU-055A', 'Validate', {'page': 'req'}, 'CR-STU-055A · Clarification request'),
    ('STU-055B', 'Validate', {'page': 'ev'}, 'CR-STU-055B · Evidence request'),
    ('STU-055C', 'Validate', {'page': 'meet'}, 'CR-STU-055C · Meeting request'),
    ('STU-055D', 'Validate', {'page': 'find'}, 'CR-STU-055D · Findings'),
    ('STU-056', 'Validate', {'page': 'improve'}, 'CR-STU-056 · Improvements required (action plan)'),
    ('STU-057', 'Validate', {'page': 'revise'}, 'CR-STU-057 · Course revision (findings in context)'),
    ('STU-058', 'Validate', {'page': 'resub'}, 'CR-STU-058 · Resubmission'),
    ('STU-059', 'Validate', {'page': 'passed'}, 'CR-STU-059 · Validation decision'),
    ('STU-060', 'Publish', {'step': 'price'}, 'CR-STU-060 · Final Pricing Confirmation'),
    ('STU-060b', 'Publish', {'step': 'priceout'}, 'CR-STU-060 · Final pricing: provisional price now outside the range'),
    ('STU-061', 'Publish', {'step': 'revenue'}, 'CR-STU-061 · Revenue share confirmation (1 pending)'),
    ('STU-062', 'Publish', {'step': 'listing'}, 'CR-STU-062 · Marketplace listing'),
    ('STU-065', 'Publish', {'step': 'live'}, 'CR-STU-065 · Published success'),
]

if __name__ == '__main__':
    import sys
    H = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else {}
    for code, src, props, title in BOARDS:
        bg = '#F7F9FD' if src == 'Validate' else '#FFFFFF'
        hd, hm = H.get(code, (3000, 3000))
        write(code + '.dc.html', wrapper(title + ' · Desktop', src, props, 1440, hd, bg))
        write(code + '-Mobile.dc.html', wrapper(title + ' · Mobile', src, props, 390, hm, bg))
    print('ok', len(BOARDS), 'boards; toggles', W.n, U.n)
