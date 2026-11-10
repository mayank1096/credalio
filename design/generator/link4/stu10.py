"""Link 4 · Batch 10: course-level collaboration, invite by name and manage collaborators (CR-COL-001 to CR-COL-005C).
Client copy word for word (prototype-only notes omitted). CR-COL-001-SOLO refused to open in the client file.

Collab.dc.html (prop page) in the Course Studio workspace shell (sidebar Manage > Collaborators).
Reuses: page_head / sidebar / topbar (l4kit), wk / bar / steps / outcome (stu7), kpis / note / facts / utabs / dc-r / hp-sw (stu8),
the .dl dialog (stu6) and the .dw drawer (stu7).
"""
import json
from l4kit import *
from rail import *
from kit import coin, credit, emblem
import stu7, stu8
from stu7 import wk, bar, steps, outcome
from stu8 import kpis, note, facts

W = Toggles()
PAGES = []
def P(key, body):
    PAGES.append((key, body))

# ---------------------------------------------------------------- people
PPL = {'AO': (ME, 'Ada Ononuju', '', 'h1'), 'JA': (M1, 'Dr. John Adeyemi', 'Data Analytics', 'h1'), 'JO': (None, 'Johnson Okafor', 'Software Dev', 'h3'),
       'MB': (None, 'Mercy Bello', 'Finance', 'h2'), 'TA': (None, 'Tunde Ade', 'Data', 'h4'), 'LM': (None, 'Lena Moyo', 'Data', 'h2'),
       'RB': (None, 'Rita Bako', 'BI', 'h5'), 'SK': (None, 'Sade Kolawole', '', 'h3')}
def pa(k, size=36):
    src, _, _, h = PPL[k]
    if src:
        return av(src, k, size)
    return '<span class="la2 %s" style="width: %dpx; height: %dpx; font-size: %dpx">%s</span>' % (h, size, size, max(10, size // 3), k)
def who(k, name=None, sub=None):
    src, n, ex, _ = PPL[k]
    sub = ex if sub is None else sub
    return '<span class="cm">%s<span class="cm-t"><b>%s</b>%s</span></span>' % (pa(k), name or n, ('<em>%s</em>' % sub) if sub else '')
def role(r):
    return '<span class="rl%s">%s</span>' % (' ld' if r.startswith('Lead') else '', r)
def share(p, kind='', label=None):
    return '<span class="shr %s"><b>%s</b><i><s style="--w: %d%%"></s></i></span>' % (kind, label or '%d%%' % p, min(100, p * 100 // 60 if kind != 'rs' else p * 10))
def ghost(label, href, cls=''):
    return '<a class="ds-ghost%s" href="%s">%s</a>' % ((' ' + cls) if cls else '', href, label)
ARR = ic('arrowr', 13, 2.2)
def link(label, href, cls='sm'):
    return '<a class="ds-link %s cl-a" href="%s">%s%s</a>' % (cls, href, label, ARR)

# ---------------------------------------------------------------- shared blocks
ALLOC = [('ld', 'Lead', 60), ('co', 'Co-Creators and Contributors', 30), ('rs', 'Reserved for pending', 10), ('fr', 'Available', 0)]
def alloc_card(title='Revenue allocation'):
    segs = ''.join('<i class="%s" style="flex: %d; --i: %d"></i>' % (k, v, i) for i, (k, _, v) in enumerate(ALLOC) if v)
    rows = ''.join('<li class="%s"><i></i><span>%s</span><b>%d%%</b></li>' % (k, l, v) for k, l, v in ALLOC)
    return '<section class="ds-card rx alc ob-in2"><span class="rx-k">%s</span><div class="alc-b">%s</div><ul>%s</ul></section>' % (title, segs, rows)
ACT = [('Today', 'Invitation sent to Tunde Ade (Contributor, 5%)', 'Ada Ononuju', 'send'), ('Yesterday', 'Invitation sent to Mercy Bello (Reviewer, 5%)', 'Ada Ononuju', 'send'),
       ('12 Oct', 'Johnson Okafor accepted Contributor (10%)', 'Johnson Okafor', 'check'), ('3 Oct', 'Lesson 3.2 moved from Chapter 2 to Chapter 3', 'Ada Ononuju', 'layers'),
       ('2 Sep', 'Lena Moyo ended: collaboration completed', 'Ada Ononuju', 'users')]
ACTIVE = [('AO', 'Ada Ononuju (you)', '', 'Lead Creator', 'Whole course', 60), ('JA', None, None, 'Co-Creator', 'Chapters 2–3', 20), ('JO', None, None, 'Contributor', 'Lesson 3.2', 10)]
PEND = [('MB', 'Reviewer', 5, '8 Nov'), ('TA', 'Contributor', 5, '9 Nov')]
COLLAB = 'Manage · Collaborators'

# ======================================================================= CR-COL-001 Course Collaboration Centre
P('hub', page_head(COLLAB, 'Course Collaboration', 'Data Analysis with SQL · Lead Creator',
                   right=ghost('Open Collaboration', '#') + btn('Invite Creator', 'COL-002.dc.html')) +
  kpis([('3', 'Active members', '', ''), ('2', 'Pending invitations', '', 'am'), ('0', 'Applications', '', ''), ('30%', 'Co-creator allocation', '', 'cb')]) +
  wk('''<section class="ds-card fc ob-in3"><div class="fc-h"><div><h2>Course Team</h2><p>Active members and what they are responsible for</p></div>%s</div>
<div class="ct3"><div class="ct3-r ct3-hd"><span>Member</span><span>Role</span><span>Scope</span><span>Share</span><span>Status</span></div>%s</div></section>
<section class="ds-card fc ob-in4"><div class="fc-h"><div><h2>Invitations</h2></div>%s</div>
<div class="ct3 pd"><div class="ct3-r ct3-hd"><span>Creator</span><span>Role</span><span></span><span>Share</span><span>Status</span></div>%s</div></section>''' % (
      link('Manage', 'COL-004.dc.html'),
      ''.join('<a class="ct3-r" href="%s" style="--i: %d">%s%s<span class="ct3-s">%s</span>%s%s</a>' % (
          'COL-004-DETAIL.dc.html' if k == 'JA' else 'COL-004.dc.html', i, who(k, n, '' if k == 'AO' else None), role(r), sc, share(p), tag('Active', 'green'))
          for i, (k, n, _, r, sc, p) in enumerate(ACTIVE)),
      link('Manage invitations', 'COL-004-PENDING.dc.html'),
      ''.join('<a class="ct3-r" href="COL-004-PENDING.dc.html" style="--i: %d">%s%s<span class="ct3-s"></span>%s<span class="pnd"><i></i>Pending</span></a>' % (
          i, who(k, sub=''), role(r), share(p, 'rs')) for i, (k, r, p, _) in enumerate(PEND))),
     alloc_card() +
     '''<section class="ds-card rx opn ob-in3"><span class="opn-v" aria-hidden="true"><i></i><i></i><i></i>%s</span><span class="rx-k">Open opportunity</span><p><b>None published.</b> Direct invitations and an open opportunity can run together on the same course.</p>%s</section>
<section class="ds-card rx acv ob-in4"><div class="acv-h"><span class="rx-k">Activity</span>%s</div><ol>%s</ol></section>''' % (
         ic('users', 18, 2), ghost('Open collaboration', '#', 'sm'), link('View all', 'COL-004-ACTIVITY.dc.html'),
         ''.join('<li style="--i: %d"><em>%s</em><span>%s</span></li>' % (i, w, e) for i, (w, e, _, _) in enumerate(ACT[:3])))))

# ======================================================================= CR-COL-002 Invite (+ ERR)
LATER = '''<div class="ltr ob-in">%s<p>Not ready to do this now? You can set up collaborators later from Collaborators. Your course stays fully editable.</p><a class="ds-link sm cl-a" href="STU-020.dc.html">Continue building course%s</a></div>''' % (ic('clock', 18, 2), ARR)
def invite(err=False):
    pct = '25' if err else '20'
    share_in = '''<div class="pcn%s"><input class="ds-in" value="%s" aria-label="Revenue share (%%)"%s><span>%%</span></div>''' % (' bad' if err else '', pct, ' aria-invalid="true"' if err else '')
    errm = '<p class="fe">%s<span>Revenue share exceeds the allocation still available (15%% left after 10%% reserved for pending invitations). Lower the share or withdraw a pending invitation.</span></p>' % ic('warn', 14, 2.2) if err else ''
    form = '''<section class="ds-card fc ivf ob-in2">
<div class="iv-2">%s%s</div>
<div class="iv-2">%s%s</div>
<div class="iv-sh">%s<div class="iv-al"><span class="rx-k">Allocation</span><div class="iv-ab"><i class="ld" style="flex: 60"></i><i class="co" style="flex: 15"></i><i class="rs" style="flex: 10"></i><i class="fr" style="flex: 15"></i></div><b>Available 15%% after reservations</b></div></div>%s
<div class="iv-2 dt">%s%s</div>
%s%s
<p class="iv-ag">%s<span>Collaboration agreement v3 and revenue policy shown to the recipient</span></p>
</section>''' % (
        field('Course', '<div class="ds-in ro">%s<span>Data Analysis with SQL (read-only)</span></div>' % ic('lock', 14, 2)),
        field('Creator', '<div class="ds-in pick">%s<span><b>Dr. John Adeyemi</b><em>Data Analytics</em></span><button type="button" class="ds-x xs" aria-label="Remove">%s</button></div><span class="fl-n">Invite a specific person by name or registered email. You cannot invite yourself.</span>' % (pa('JA', 28), ic('x', 12, 2.4))),
        field('Collaboration role', sel('Co-Creator', 'Collaboration role')), field('Contribution scope', sel('Selected chapters: 2, 3', 'Contribution scope')),
        field('Revenue share (%)', share_in + '<span class="fl-n">Applies to all distributable course earnings, including Marketplace Credit sales and subscription-based creator earnings.</span>', cls='bad' if err else ''),
        errm,
        field('Start date', '<div class="ds-in ic-in">%s<span>1 Nov 2026</span></div>' % ic('cal', 16, 2)),
        field('Invitation expiry', '<div class="iv-ex">%s%s</div>' % (sel('14 days', 'Invitation expiry'), tag('%s Within platform policy' % ck(10), 'green'))),
        field('Responsibilities', '<textarea class="ds-in ta3" rows="2" aria-label="Responsibilities">Develop the SQL Joins module, practical exercises and assessments.</textarea>'),
        field('Message (optional)', '<textarea class="ds-in ta3" rows="2" aria-label="Message">Hi John, your analytics background fits Chapters 2 and 3 perfectly.</textarea>'),
        ck(11))
    perm = ('Role permissions are set by policy: Co-Creator can edit assigned curriculum and upload resources; cannot publish, change pricing or remove the Lead Creator.' if err else
            'Co-Creator permissions (default): edit curriculum, create lessons and assessments, upload resources, respond to validation, view analytics. Cannot publish, change pricing, change revenue distribution or remove the Lead Creator.')
    rail = '''<section class="ds-card rx ivp ob-in3" aria-hidden="true"><div class="ivp-h"><span class="ivp-a">%s<span class="ivp-l"><i></i></span>%s</span></div>
<b class="ivp-n">Dr. John Adeyemi</b><span class="ivp-r">%s<span>Chapters 2–3</span></span><div class="ivp-s"><b>%s%%</b><span>Revenue share</span></div><div class="ivp-d"><span><em>Start date</em>1 Nov 2026</span><span><em>Invitation expiry</em>14 days</span></div></section>
<section class="ds-card rx ivq ob-in4"><span class="ivq-i">%s</span><p>%s</p>%s</section>''' % (
        pa('AO', 40), pa('JA', 40), role('Co-Creator'), pct, ic('valid', 18, 2), perm, '' if err else link('Review permissions', 'COL-002B.dc.html'))
    return (LATER + page_head(COLLAB + ' · Invite', 'Invite a Co-Creator', 'Data Analysis with SQL') +
            wk(form + note('A pending invitation reserves this percentage until it is accepted, declined, withdrawn or expires. An invitation is not an accepted agreement.') +
               bar('', ghost('Cancel', 'COL-001.dc.html') + btn('Review Invitation', 'COL-003.dc.html')), rail))
P('inv', invite())
P('inv-err', invite(True))

# ======================================================================= CR-COL-002B Roles & permissions (+ ROLE, EDIT, OFFER)
CAN = ['Edit curriculum', 'Create lessons', 'Create assessments', 'Upload resources', 'Respond to validation requests', 'View analytics']
CANT = ['Change ownership', 'Publish course', 'Change revenue distribution', 'Remove Lead Creator']
def perms(k, name, sub, rl, on, msg, save, back, kind='info'):
    tiles = ''
    for i, p in enumerate(CAN):
        t = W.new(bool(on[i]))
        tiles += '<button type="button" class="pmt {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}" style="--i: %d"><span class="pmt-b">%s</span><span>%s</span></button>' % (t, t, t, i, ck(11), p)
    main = '''<section class="ds-card pm ob-in2"><header class="pm-h">%s<div><b>%s</b><em>%s</em></div>%s</header>
<div class="pmg">%s</div><div class="pm-k"><span class="rx-k">Can</span><span class="pm-c"><b class="pm-n"></b> of 6</span></div></section>
<p class="pm-m %s">%s<span>%s</span></p>''' % (pa(k, 48), name, sub, field('Role', sel(rl, 'Role'), cls='pm-r'), tiles, kind, INFO if kind == 'info' else ic('warn', 16, 2), msg)
    rail = '''<section class="ds-card rx ldc ob-in3"><span class="rx-k">Lead Creator / Course owner</span><div class="ldc-p">%s<span><b>Ada Ononuju (you)</b>%s</span></div><p>Every course has exactly one Lead Creator. Only the Lead Creator can publish, change revenue distribution or transfer ownership.</p></section>
<section class="ds-card rx cnl ob-in4"><span class="rx-k">Cannot · Lead Creator only</span><ul>%s</ul><p class="rx-p">%s<span>Set by policy. Not adjustable per collaborator.</span></p></section>''' % (
        pa('AO', 40), tag('All permissions', 'blue'), ''.join('<li><span>%s</span>%s</li>' % (ic('x', 11, 2.6), c) for c in CANT), ic('lock', 13, 2.2))
    return (page_head(COLLAB, 'Roles &amp; permissions', 'Decide what this collaborator can do. You can adjust permissions within Credalio policy.') +
            wk(main + bar('<a class="ds-link" href="#">Reset to role defaults</a>', ghost('Cancel', back) + btn(save, back)), rail))
P('perm', perms('JA', 'Dr. John Adeyemi', 'Default permissions for Co-Creator · Pending invitation', 'Co-Creator', [1, 1, 1, 1, 1, 1],
                'These permissions are shown to the recipient in the invitation and apply once they accept. Skipping this step applies the role defaults.', 'Save permissions', 'COL-002.dc.html'))
P('perm-role', perms('JA', 'Dr. John Adeyemi', 'Default permissions for Content Contributor · Pending invitation', 'Content Contributor', [0, 1, 0, 1, 0, 0],
                     'Role changed. The checkboxes reset to Content Contributor defaults. The role on the invitation and review screens updates when you save.', 'Save permissions', 'COL-002.dc.html', 'am'))
P('perm-edit', perms('JA', 'Dr. John Adeyemi', 'Default permissions for Co-Creator · Accepted', 'Co-Creator', [1, 1, 0, 1, 1, 1],
                     'Permission changes inside Credalio policy apply straight away and need no agreement from John. He is notified. Changing his revenue share still needs his agreement.', 'Save changes', 'COL-004-DETAIL.dc.html'))
P('perm-offer', perms('SK', 'Sade Kolawole', 'Default permissions for Co-Creator · Applicant · offer not yet sent', 'Co-Creator', [1, 1, 1, 1, 1, 1],
                      'These permissions are part of the offer. She sees them before accepting.', 'Save permissions', '#'))

# ======================================================================= CR-COL-003 Review invitation (+ SENT)
REV = [('Course', 'Data Analysis with SQL · Personal ownership · Intermediate', ''), ('Invited creator', who('JA', sub=''), ''),
       ('Role &amp; responsibilities', 'Co-Creator · Chapters 2–3 (SQL Joins module, exercises, assessments)', ''),
       ('Permissions', 'Default Co-Creator: edit curriculum, lessons, assessments, resources, validation responses, analytics · %s' % link('Review', 'COL-002B.dc.html'), ''),
       ('Revenue share', '<b class="rv3-p">20%</b> of all distributable course earnings', 'hi'), ('Covered earnings', 'Marketplace Credit sales + subscription-based creator earnings', ''),
       ('Effective date', '1 Nov 2026', ''), ('Invitation expires', '8 Nov 2026 (14 days)', ''), ('Agreement version', 'Collaboration agreement v3', ''),
       ('Organization approval', tag('%s Not required (personal course)' % ck(10), 'green'), '')]
P('review', page_head(COLLAB + ' · Invite', 'Review invitation', 'Check everything before it reaches the recipient.') +
  wk('<section class="ds-card rv3 ob-in2"><dl>%s</dl></section>' % ''.join('<div class="%s" style="--i: %d"><dt>%s</dt><dd>%s</dd></div>' % (k, i, l, v) for i, (l, v, k) in enumerate(REV)) +
     note('Changing material terms after sending issues a revised offer; a delivered invitation is never silently edited. You can withdraw it or resend the notification.') +
     bar('<a class="ds-link" href="COL-002.dc.html">Back to Edit</a>', ghost('Cancel', 'COL-001.dc.html') + btn('Send Invitation', 'COL-003-SENT.dc.html')),
     '''<section class="ds-card rx hs3 ob-in3" aria-hidden="true"><div class="hs3-v">%s<span class="hs3-l"><i class="hs3-e">%s</i></span>%s</div><div class="hs3-n"><span>Ada Ononuju</span><span>Dr. John Adeyemi</span></div></section>
<section class="ds-card rx rsr ob-in4"><span class="rx-k">Revenue share</span><div class="rs3-r">%s<span><b>20%%</b></span></div><p class="rx-p">of all distributable course earnings</p></section>''' % (
         pa('AO', 52), ic('send', 14, 2.2), pa('JA', 52), ring(20, 120, 12))))
P('sent', outcome('ok', 'check', 'Pending', 'Invitation sent', 'Dr. John Adeyemi will see this in Creator Studio → Collaboration → Invitations, with an email as a secondary notice.',
                  '<section class="ko-card">%s</section>' % facts([('Sent', '25 Oct 2026'), ('Expires', '8 Nov 2026'), ('Reserved share', '20%')]),
                  btn('Continue building course', 'STU-020.dc.html') + '</div><div class="ko-lk"><a class="ds-link" href="COL-004-PENDING.dc.html">View Pending Invitation</a><a class="ds-link" href="COL-001.dc.html">Back to Collaboration</a>'))

# ======================================================================= CR-COL-004 Manage collaborators (tabs + detail + withdraw)
TABS = [('active', 'Active Members', '3', 'COL-004.dc.html'), ('pending', 'Pending Invitations', '2', 'COL-004-PENDING.dc.html'),
        ('past', 'Past Members', '', 'COL-004-PAST.dc.html'), ('activity', 'Activity History', '', 'COL-004-ACTIVITY.dc.html')]
def mtabs(cur):
    return '<nav class="utabs ob-in2" aria-label="Collaborators">%s</nav>' % ''.join(
        '<a href="%s" class="ut%s"%s>%s%s</a>' % (h, ' on' if k == cur else '', ' aria-current="page"' if k == cur else '', l, ('<em class="ut-n">%s</em>' % n) if n else '') for k, l, n, h in TABS)
def mhead(cur):
    return page_head(COLLAB, 'Manage collaborators', 'Data Analysis with SQL', right=btn('Invite Creator', 'COL-002.dc.html')) + mtabs(cur)
MRAIL = alloc_card()
def active_tbl(sel_=None):
    rows = ''
    for i, (k, n, _, r, sc, p) in enumerate(ACTIVE):
        act = '<a class="ds-ghost xs" href="#">View</a>' if k == 'AO' else '<a class="ds-ghost xs" href="COL-004-DETAIL.dc.html">View / Manage</a>'
        rows += '<div class="mt3-r%s" style="--i: %d">%s%s%s%s<span class="mt3-a">%s</span></div>' % (' sel' if sel_ == k else '', i, who(k, n.replace(' (you)', '') if n else None, 'Lead' if k == 'AO' else None), role(r), share(p), tag('Active', 'green'), act)
    return ('<section class="ds-card mt3 ob-in3"><div class="mt3-r mt3-hd"><span>Creator</span><span>Role</span><span>Revenue share</span><span>Status</span><span>Actions</span></div>%s</section>' % rows +
            note('Pending proposals reserve allocation. Another 5% invitation cannot be sent while active and reserved shares total 100%.'))
def pending_tbl():
    rows = ''.join('<div class="mt3-r pd" style="--i: %d">%s%s%s<span class="mt3-x">%s<span>%s</span></span><span class="mt3-a"><a class="ds-link sm dz-l" href="COL-004-WITHDRAW.dc.html">Withdraw</a><button type="button" class="ds-ghost xs">%s<span>Resend</span></button></span></div>' % (
        i, who(k), role(r), share(p, 'rs'), ic('clock', 13, 2), d, ic('send', 13, 2)) for i, (k, r, p, d) in enumerate(PEND))
    return ('<section class="ds-card mt3 ob-in3"><div class="mt3-r mt3-hd"><span>Creator</span><span>Role</span><span>Share (reserved)</span><span>Expires</span><span>Actions</span></div>%s</section>' % rows +
            note('Pending shares are reserved and released when an invitation is accepted, declined, withdrawn or expires. Changing terms issues a revised offer.'))
PAST = [('LM', 'Contributor', '8% (ended)', '2 Sep', 'Collaboration completed'), ('RB', 'Reviewer', '5% (ended)', '14 Aug', 'Creator requested to leave')]
P('m-active', mhead('active') + wk(active_tbl(), MRAIL))
P('m-pending', mhead('pending') + wk(pending_tbl(), MRAIL))
P('m-past', mhead('past') + wk(
    '<section class="ds-card mt3 ps3 ob-in3"><div class="mt3-r mt3-hd"><span>Creator</span><span>Role</span><span>Share</span><span>Ended</span><span>Reason</span></div>%s</section>' % ''.join(
        '<div class="mt3-r" style="--i: %d">%s%s<span class="shr ed"><b>%s</b></span><span class="mt3-x">%s</span><span class="mt3-y">%s</span></div>' % (i, who(k), role(r), s, d, why) for i, (k, r, s, d, why) in enumerate(PAST)) +
    note('Past members keep their earned balances and agreement history. Their shares are not given to the Lead Creator automatically.'), MRAIL))
P('m-activity', mhead('activity') + wk(
    '<section class="ds-card ah3 ob-in3"><ol>%s</ol></section>' % ''.join(
        '<li style="--i: %d"><span class="ah3-i">%s</span><div><b>%s</b><em>%s · %s</em></div></li>' % (i, ic(icn, 14, 2.2), e, w, by) for i, (w, e, by, icn) in enumerate(ACT)) +
    note('Every invitation, acceptance, role change, move and removal is recorded here.'), MRAIL))
DETAIL = '''<a class="ov-scrim" href="COL-004.dc.html" aria-label="Close"></a>
<aside class="dw cd3" role="dialog" aria-modal="true" aria-label="Dr. John Adeyemi"><header class="dw-h"><span class="rx-k">Collaborator</span><a class="ds-x sm" href="COL-004.dc.html" aria-label="Close">%s</a></header>
<div class="dw-p">%s<div><b>Dr. John Adeyemi</b><span class="cst-t">%s%s</span></div></div>
<div class="cd3-s">%s<span><b>20%%</b><em>Revenue share · Agreement #AG-2041</em></span></div>
<section class="dw-s"><dl>%s</dl></section>
<div class="cd3-a"><a class="ds-ghost sm" href="COL-002B-EDIT.dc.html">%s<span>Edit permissions</span></a><a class="ds-ghost sm" href="#">%s<span>Propose change</span></a><a class="ds-ghost sm dz-a" href="COL-005A.dc.html">Remove Co-Creator</a></div>
<p class="dw-n">%s<span>Changing accepted financial terms needs John’s agreement. Co-creators cannot see each other’s private agreements.</span></p></aside>''' % (
    ic('x', 16, 2.2), pa('JA', 56), role('Co-Creator'), tag('Active', 'green'), ring(20, 56, 9),
    ''.join('<div><dt>%s</dt><dd>%s</dd></div>' % r for r in [('Expertise', 'Data Analytics · SQL'), ('Assigned', 'Chapters 2–3'), ('Joined', '1 Nov 2026'), ('Contributions', '4 lessons, 2 assessments'),
                                                          ('Access', 'Edit assigned, upload resources'), ('Pending reviews', '1 assessment review')]),
    ic('valid', 14, 2), ic('edit', 14, 2), ic('lock', 13, 2))
P('m-detail', mhead('active') + wk(active_tbl('JA'), MRAIL) + DETAIL)
WITHDRAW = '''<a class="ov-scrim" href="COL-004-PENDING.dc.html" aria-label="Close"></a>
<div class="dl wd3" role="dialog" aria-modal="true" aria-label="Withdraw invitation to Mercy Bello?"><header class="dl-h"><span class="wd3-v">%s<span class="wd3-x">%s</span></span><a class="ds-x sm" href="COL-004-PENDING.dc.html" aria-label="Close">%s</a></header>
<div class="dl-b"><h2 class="wd3-h">Withdraw invitation to Mercy Bello?</h2><div class="wd3-m">%s<span>5%% share reserved</span><span>%s expires 8 Nov</span></div>
<p class="dl-p">She is told the invitation was withdrawn and can no longer accept it. The reserved 5%% is released. You can send a new invitation later.</p></div>
<footer class="dl-f"><a class="ds-ghost" href="COL-004-PENDING.dc.html">Cancel</a>%s</footer></div>''' % (
    pa('MB', 48), ic('x', 12, 2.6), ic('x', 16, 2.2), role('Reviewer'), ic('clock', 13, 2), btn('Withdraw invitation', 'COL-004-PENDING.dc.html').replace('class="ds-btn"', 'class="ds-btn btn-dz"', 1))
P('m-withdraw', mhead('pending') + wk(pending_tbl(), MRAIL) + WITHDRAW)

# ======================================================================= CR-COL-005 Remove a collaborator
RSTEPS = ['Select creator', 'Review impact', 'Reason', 'Confirm']
IMPACT = [('file', 'Contributed', '4 lessons, 2 assessments, 6 resources', ''), ('clock', 'Open assignments', '2 lessons unfinished (Chapter 3)', 'am'),
          ('quiz', 'Pending reviews', '1 assessment review waiting', 'am'), ('earn', 'Revenue agreement', '20% accepted · continues under notice and royalty terms', ''),
          ('wallet', 'Earned, unsettled', '%s120 Marketplace Credits' % credit(), ''), ('cert', 'Ownership &amp; licence', 'Contributions licensed to the course under agreement v3', ''),
          ('valid', 'Organization approval', 'Not required', 'ok')]
SEL = '''<section class="ds-card rx rmc ob-in2"><span class="rx-k">Selected creator</span><div class="rmc-p">%s<span><b>Dr. John Adeyemi</b>%s</span></div><div class="rmc-s">%s<span><b>20%%</b><em>Agreement #AG-2041</em></span></div></section>''' % (pa('JA', 52), role('Co-Creator'), ring(20, 52, 8))
P('rm-a', page_head(COLLAB, 'Remove Co-Creator', 'This affects access, content and revenue rights.') + steps(1, RSTEPS) +
  wk('<section class="ds-card fc ob-in3"><div class="fc-h"><div><h2>Impact</h2></div></div><div class="imp">%s</div></section>' % ''.join(
      '<div class="imp-c %s" style="--i: %d"><span class="imp-i">%s</span><span><em>%s</em><b>%s</b></span></div>' % (k, i, ic(icn, 17, 2), a, d) for i, (icn, a, d, k) in enumerate(IMPACT)) +
     bar('', ghost('Cancel', 'COL-004-DETAIL.dc.html') + btn('Continue', 'COL-005B.dc.html')), SEL))
RSN = [('Collaboration completed', ''), ('Creator requested to leave', ''), ('Responsibilities changed', ''), ('Inactivity or missed commitments', ''),
       ('Agreement or conduct issue', 'Needs a written explanation; may route to review'), ('Other', '')]
ka = W.new(True)
P('rm-b', page_head(COLLAB, 'Why are you removing Dr. John Adeyemi?', '') + steps(2, RSTEPS) +
  wk('''<section class="ds-card fc ob-in2"><div class="rsn">%s</div>%s</section>
<button type="button" class="dc-r ack {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}"><span class="dc-b">%s</span><span>I understand the impact on access, content and revenue rights.</span></button>''' % (
      ''.join(W.opt('<span class="o-t"><b>%s</b>%s</span>' % (r, ('<span>%s</span>' % s) if s else ''), i == 3, 'rsn', 'sm') for i, (r, s) in enumerate(RSN)),
      field('Details', '<textarea class="ds-in ta3" rows="2" aria-label="Details">John has not delivered Chapter 3 lessons since 2 Oct.</textarea><span class="fl-n">Visible to the removed creator and to Credalio review if the removal is disputed.</span>', cls='rsn-d'),
      ka, ka, ka, ck(12)) +
     bar('<a class="ds-link" href="COL-005A.dc.html">Back</a>', '<span class="cf-g {{c%s}}">%s</span>' % (ka, btn('Review Removal Confirmation', 'COL-005C.dc.html'))),
     SEL + '<section class="ds-card rx rmn ob-in3"><span class="rmn-i">%s</span><p>Removing a creator does not move their percentage to the Lead Creator. Future allocation follows the agreement: notice period, continuing royalties, replacement and approvals. If the removal is disputed or restricted, it goes to review instead of executing.</p></section>' % ic('earn', 18, 2)))
P('rm-done', outcome('gy', 'users', 'Executed', 'Co-Creator removed', 'John’s access ended. Saved contributions stay. His 20% share is handled under the agreement: 30-day notice, then continuing royalties as stated.',
                     '', btn('Back to Manage collaborators', 'COL-004.dc.html')))
P('rm-review', outcome('am', 'clock', 'Sent to review', 'Removal needs review', 'The agreement restricts removal, so this request goes to Credalio review. John keeps access until a decision. You will be notified.',
                       '', btn('View request status', '#')))

# ======================================================================= assembly
def body():
    blocks = '\n'.join('<sc-if value="{{p_%s}}" hint-placeholder-val="{{ %s }}">\n%s\n</sc-if>' % (k.replace('-', '_'), 'true' if k == 'hub' else 'false', b) for k, b in PAGES)
    return '''<div class="ds-root">
%s
<div style="min-width: 0; display: flex; flex-direction: column">
%s
<main class="ds-main cl-main">
%s
</main>
</div>
</div>''' % (sidebar('collab'), topbar(phase='Build'), blocks)
JS = W.js() + '''var PG = %s;
class Component extends DCLogic {
  renderVals() {
    var pg = this.props.page || 'hub', v = togVals(this), self = this;
    PG.forEach(function (k) { v['p_'.concat(k.replace('-', '_'))] = k === pg; });
    v.navCls = this.state.nav ? 'ds-open' : '';
    v.toggleNav = function () { self.setState({ nav: !self.state.nav }); };
    return v;
  }
}''' % json.dumps([p[0] for p in PAGES])

CSS = stu8.CSS.replace('.fx3:not(.col)', '.fx3').replace('.wk:has(.cr9){counter-reset:seen}', '').replace('.wk-r > .rx:has(.pr9){order:1}', '').replace(':not(.am):not(.rd):not(.ok)', ':not(.am):not(.ok)') + open(__file__.replace('stu10.py', 'stu10.css')).read()

write('Collab.dc.html', doc('Course collaboration · invite and manage · shared source', kit.KIT_CSS + '\n' + dash.DASH_CSS + BASE_CSS + CW_CSS + WK_CSS + CSS, body(), JS))

BOARDS = [
    ('COL-001', 'hub', 'CR-COL-001 · Course Collaboration Centre'),
    ('COL-002', 'inv', 'CR-COL-002 · Invite a Co-Creator'),
    ('COL-002-ERR', 'inv-err', 'CR-COL-002 · Invite (share exceeds allocation)'),
    ('COL-002B', 'perm', 'CR-COL-002B · Roles & permissions (invitation)'),
    ('COL-002B-ROLE', 'perm-role', 'CR-COL-002B · Roles & permissions (role changed)'),
    ('COL-002B-EDIT', 'perm-edit', 'CR-COL-002B · Roles & permissions (accepted collaborator)'),
    ('COL-002B-OFFER', 'perm-offer', 'CR-COL-002B · Roles & permissions (applicant offer)'),
    ('COL-003', 'review', 'CR-COL-003 · Review invitation'),
    ('COL-003-SENT', 'sent', 'CR-COL-003 · Invitation sent'),
    ('COL-004', 'm-active', 'CR-COL-004 · Manage collaborators (active)'),
    ('COL-004-PENDING', 'm-pending', 'CR-COL-004 · Pending invitations'),
    ('COL-004-PAST', 'm-past', 'CR-COL-004 · Past members'),
    ('COL-004-ACTIVITY', 'm-activity', 'CR-COL-004 · Activity history'),
    ('COL-004-DETAIL', 'm-detail', 'CR-COL-004 · Collaborator detail'),
    ('COL-004-WITHDRAW', 'm-withdraw', 'CR-COL-004 · Withdraw invitation'),
    ('COL-005A', 'rm-a', 'CR-COL-005A · Remove: review impact'),
    ('COL-005B', 'rm-b', 'CR-COL-005B · Remove: reason'),
    ('COL-005C', 'rm-done', 'CR-COL-005C · Removal executed'),
    ('COL-005C-REVIEW', 'rm-review', 'CR-COL-005C · Removal sent to review'),
]
BOARDS = [(c, 'Collab', {'page': p}, t) for c, p, t in BOARDS]

if __name__ == '__main__':
    import sys
    H = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else {}
    for code, src, props, title in BOARDS:
        hd, hm = H.get(code, (3000, 3000))
        write(code + '.dc.html', wrapper(title + ' · Desktop', src, props, 1440, hd))
        write(code + '-Mobile.dc.html', wrapper(title + ' · Mobile', src, props, 390, hm))
    print('ok', len(BOARDS), 'boards; toggles', W.n)
