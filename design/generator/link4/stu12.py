"""Link 4 · Batch 12: creator side of collaboration, My Invitations (CR-INV-001 to 005G) + Shared Courses (CR-NAV-002).
Client copy word for word (prototype-only notes omitted).

Collab3.dc.html (prop page) in the creator dashboard shell (stu6 cr_side / CR_TOP, new Collaboration nav group).
Reuses stu10/stu11 people, roles, share bars, CSS; stu7 wk / bar / steps / outcome; stu8 note / facts.
"""
import json
from l4kit import *
from rail import *
from kit import coin, credit, emblem
import stu6, stu7, stu8, stu10, stu11
from stu6 import cr_side, CR_TOP, crumbs
from stu7 import wk, bar, steps, outcome
from stu8 import note, facts
from stu10 import pa, role, ghost, link, ARR, PPL

PPL['AM'] = (None, 'Alex Morgan', '', 'h1')
PPL['SY'] = (None, 'Sara Yusuf', '', 'h5')
PPL['AO'] = (ME, 'Ada Ononuju', '', 'h1')

W = Toggles()
PAGES = []
def P(key, nav, body):
    PAGES.append((key, nav, body))
def red(label, href):
    return btn(label, href).replace('class="ds-btn"', 'class="ds-btn btn-dz"', 1)
def ph(path, h1, sub, right=''):
    return (crumbs([(x, '' if i == len(path) - 1 else ('INV-001.dc.html' if x == 'Invitations' else '#')) for i, x in enumerate(path)]) +
            '<header class="pg-h ob-in"><div class="pg-hl"><h1 class="ds-h1">%s</h1>%s</div>%s</header>' % (h1, ('<p class="ds-sub">%s</p>' % sub) if sub else '', ('<div class="pg-hr">%s</div>' % right) if right else ''))
INV_PATH = ['Creator Studio', 'Collaboration', 'Invitations']
DET_PATH = ['Collaboration', 'Invitations']
COV = {'Data Analysis with SQL': ('SQL', 'c1'), 'SQL for Finance Teams': ('FIN', 'c2'), 'Python for Beginners': ('PY', 'c3'), 'Excel Dashboards': ('XL', 'c4'),
       'Intro to R': ('R', 'c5'), 'Stats Basics': ('ST', 'c6')}
def cov(t, n=44):
    i, c = COV[t]
    return '<span class="cv6 %s" style="width: %dpx; height: %dpx" aria-hidden="true">%s</span>' % (c, n, n, i)
STC = {'Pending': 'amber', 'Accepted': 'green', 'Declined': '', 'Expired': '', 'Withdrawn': '', 'Active': 'green'}

# ======================================================================= CR-INV-001 My Invitations (tabs)
TABS = [('pend', 'Pending', '2', 'INV-001'), ('acc', 'Accepted', '', 'INV-001-ACCEPTED'), ('dec', 'Declined', '', 'INV-001-DECLINED'), ('all', 'All', '', 'INV-001-ALL')]
def itabs(cur, n='2', search=False):
    t = ''.join('<a href="%s.dc.html" class="ut%s"%s>%s%s</a>' % (h, ' on' if k == cur else '', ' aria-current="page"' if k == cur else '', l, ('<em class="ut-n">%s</em>' % (n if k == 'pend' else c)) if (c or k == 'pend') else '') for k, l, c, h in TABS)
    s = '<label class="ds-in sr6">%s<input placeholder="Search by course, Lead Creator or status" aria-label="Search"></label>' % ic('search', 16, 2) if search else ''
    return '<div class="tb6 ob-in2"><nav class="utabs" aria-label="Invitations">%s</nav>%s</div>' % (t, s)
PENDING = [('Data Analysis with SQL', 'AM', 'Direct invite', 'Expires in 5 days', 5, 'Co-Creator', 20, 'INV-002'),
           ('SQL for Finance Teams', 'SK', 'Open collaboration offer', 'Expires in 6 days', 6, 'Co-Creator', 15, 'INV-002')]
def icard(i, c):
    t, k, kind, exp, days, r, pct, h = c
    return '''<article class="ic6" style="--i: %d"><div class="ic6-t">%s<div class="ic6-h"><span class="ic6-k"><span class="ic6-p"><i></i><span>Awaiting response</span></span><span class="ic6-y%s">%s</span></span><b>%s</b><span class="ic6-f">%s<span>Invited by <b>%s</b> · Lead Creator · Role: %s</span></span></div></div>
<div class="ic6-s"><div class="ic6-r"><span class="ic6-rg">%s<b>%d%%</b></span><em>Marketplace + Subscription earnings</em></div><div class="ic6-e"><span class="ic6-d" style="--d: %d">%s</span><em>%s</em></div><div class="ic6-a">%s</div></div>
</article>''' % (
        i, cov(t, 56), ' oc' if 'open' in kind else '', kind, t, pa(k, 22), PPL[k][1], r, ring(pct, 52, 10), pct, days, ''.join('<i class="%s"></i>' % ('on' if j < days else '') for j in range(14)), exp, btn('Review Invitation', h + '.dc.html'))
P('i-pend', 'Invitations', ph(INV_PATH, 'My Invitations', '2 pending. Direct invitations and offers from open collaboration appear here.') + itabs('pend', search=True) +
  '<div class="ic6s ob-in3">%s</div>' % ''.join(icard(i, c) for i, c in enumerate(PENDING)) +
  note('A course does not appear under Shared Courses merely because an invitation was received. Expired and withdrawn invitations stay in history.'))

ALL = [('Data Analysis with SQL', 'AM', 'Co-Creator', '20%', 'Pending', ''), ('SQL for Finance Teams', 'SK', 'Co-Creator', '15%', 'Pending', ''),
       ('Python for Beginners', 'SY', 'Contributor', '15%', 'Accepted', ''), ('Excel Dashboards', 'MB', 'Reviewer', '5%', 'Declined', ''),
       ('Intro to R', 'TA', 'Co-Creator', '10%', 'Expired', ''), ('Stats Basics', 'RB', 'Contributor', '8%', 'Withdrawn', '')]
HREF = {'Pending': 'INV-002.dc.html', 'Expired': 'INV-002-EXPIRED.dc.html', 'Withdrawn': 'INV-002-WITHDRAWN.dc.html', 'Accepted': 'INV-001-ACCEPTED.dc.html', 'Declined': 'INV-001-DECLINED.dc.html'}
def itable(rows, act=None):
    h = ''
    for i, (t, k, r, sh, st, x) in enumerate(rows):
        a = act(t, st) if act else ''
        h += '<a class="it6-r%s" href="%s" style="--i: %d"><span class="it6-c">%s<b>%s</b></span><span class="it6-f">%s<span>%s<em class="it6-m"> · %s</em></span></span>%s<b class="it6-s">%s</b><span class="it6-st">%s%s</span></a>' % (
            ' dim' if st in ('Expired', 'Withdrawn') else '', HREF.get(st, '#'), i, cov(t, 36), t, pa(k, 26), PPL[k][1], r, role(r), sh, tag(st if not x else '%s · %s' % (st, x), STC[st]), a)
    return '<section class="ds-card it6 ob-in3"><div class="it6-r it6-hd"><span>Course</span><span>From</span><span>Role</span><span>Share</span><span>Status</span></div>%s</section>' % h
def acts_all(t, st):
    return '<span class="ds-link sm cl-a">%s%s</span>' % ('Review' if st == 'Pending' else 'View', ARR)
P('i-all', 'Invitations', ph(INV_PATH + ['All'], 'My Invitations', '') + itabs('all') + itable(ALL, acts_all) + note('All statuses, including expired and withdrawn, are kept in history.'))
def rcard(t, k, r, pct, st, kind, act, nt, nicon):
    return '''<article class="rc6 %s ob-in3"><div class="rc6-m">%s<div class="rc6-h"><b>%s</b><span class="ic6-f">%s<span>From <b>%s</b></span></span></div></div>
<div class="rc6-k"><span><em>Role</em>%s</span><span><em>Share</em><span class="rc6-rg">%s<b>%d%%</b></span></span><span><em>Status</em>%s</span></div>
<div class="rc6-a">%s</div><p class="rc6-n">%s<span>%s</span></p></article>''' % (kind, cov(t, 60), t, pa(k, 22), PPL[k][1], role(r), ring(pct, 40, 12, track='#EEF1F7', color='#0F6B45' if kind == 'ok' else '#AEB6CC'), pct, tag(st, STC[st]), act, nicon, nt)
P('i-acc', 'Invitations', ph(INV_PATH + ['Accepted'], 'My Invitations', '') + itabs('acc') +
  rcard('Python for Beginners', 'SY', 'Content Contributor', 15, 'Accepted', 'ok', btn('Open', 'NAV-002.dc.html', 'sm2'), 'Accepted invitations become courses under Shared Courses.', ic('program', 15, 2)))
P('i-dec', 'Invitations', ph(INV_PATH + ['Declined'], 'My Invitations', '') + itabs('dec') +
  rcard('Excel Dashboards', 'MB', 'Reviewer', 5, 'Declined', 'gy', '<span class="rc6-why">%s<span>Declined · timeline conflict</span></span>' % ic('clock', 14, 2), 'Declined invitations stay here for your records. The Lead Creator can send a revised offer.', INFO))
P('i-empty', 'Invitations', ph(INV_PATH, 'My Invitations', '') + itabs('pend', '0') +
  '''<section class="ds-card em6 ob-in3"><div class="em6-v" aria-hidden="true"><span class="em6-e"><i></i></span><span class="em6-o o1">%s</span><span class="em6-o o2">%s</span><span class="em6-o o3">%s</span></div>
<b>You don’t have any invitations yet</b><p>Browse open collaboration to find courses that match your expertise.</p>%s</section>''' % (
      ic('users', 16, 2), ic('send', 15, 2), ic('target', 15, 2), btn('Explore Opportunities', '#')))

# ======================================================================= CR-INV-002 details (+ expired, withdrawn)
TERMS = [('Responsibilities', 'Develop the SQL Joins module, exercises and related assessments.'), ('Contribution period', '8 weeks from 1 Nov 2026'),
         ('Edit permissions', 'Assigned chapters only'), ('Organization approval', 'Not required'),
         ('About the course', 'Intermediate Data Analytics course focused on SQL and business analysis.')]
def detail(expired=False):
    st = tag('Expired', '') if expired else tag('<i class="lv-d"></i>Pending', 'amber')
    band = ('<div class="bn6 am ob-in">%s<p>This invitation expired on 20 Oct 2026. Accept is disabled. Ask the Lead Creator to send a new invitation.</p></div>' % ic('clock', 18, 2)) if expired else ''
    exp_tile = '<div class="kt6 %s"><span class="kt6-i">%s</span><b>%s</b><em>%s</em></div>' % ('x' if expired else 'am', ic('clock', 18, 2), '<s>5 days</s>' if expired else '5 days', 'Expired' if expired else 'Expires in')
    acts = ('<span class="ds-ghost is-dis" aria-disabled="true">Decline</span><span class="ds-btn is-dis" aria-disabled="true"><span>Accept Invitation</span><span class="ob-arrow">%s</span></span>' % ARROW) if expired else \
        ('<a class="ds-ghost dz-a" href="INV-004.dc.html">Decline</a>' + btn('Accept Invitation', 'INV-003.dc.html'))
    main = '''<section class="ds-card lt6 ob-in2"><div class="lt6-h">%s<div><span class="lt6-k">Collaboration Invitation %s</span><p>You’ve been invited to collaborate on <b>Data Analysis with SQL</b>. Alex Morgan (Lead Creator · Personal course) invited you as <b>Co-Creator</b>.</p></div></div>
<div class="kt6s"><div class="kt6"><span class="kt6-i">%s</span><b>Co-Creator</b><em>Your role</em></div><div class="kt6 cb"><span class="kt6-i">%s</span><b>20%%</b><em>Revenue share</em></div>%s</div>
<p class="lt6-n">%s<span>20%% of eligible distributable course earnings, including subscription-based earnings and Marketplace Credit sales. Continuing royalties after departure: per agreement v3.</span></p></section>
<section class="ds-card fc ob-in3"><dl class="tm6">%s</dl></section>''' % (
        cov('Data Analysis with SQL', 64), st, ic('users', 18, 2), ring(20, 40, 14), exp_tile, ic('earn', 15, 2),
        ''.join('<div class="%s"><dt>%s</dt><dd>%s</dd></div>' % ('w' if l == 'Responsibilities' else '', l, v) for l, v in TERMS if l != 'About the course'))
    rail = '''<section class="ds-card rx fr6 ob-in3"><span class="rx-k">From</span><div class="fr6-p">%s<span><b>Alex Morgan</b>%s</span></div><div class="fr6-a"><span class="rx-k">About the course</span><p>Intermediate Data Analytics course focused on SQL and business analysis.</p></div></section>
<section class="ds-card rx ag6 ob-in3"><span class="ag6-i">%s</span><div><span class="rx-k">Agreement &amp; terms</span><p>Revenue sharing, content ownership, access, termination and settlement</p>%s</div></section>
<section class="ds-card rx pt6 ob-in4"><span class="pt6-i">%s</span><p>You see a limited course summary only. Protected course materials stay hidden until you are an accepted collaborator.</p><div class="pt6-b" aria-hidden="true"><i></i><i></i><i></i></div></section>''' % (
        pa('AM', 44), role('Lead Creator'), ic('file', 18, 2), link('View full terms', '#'), ic('lock', 18, 2))
    return band + ph(DET_PATH + ['Details'], 'Collaboration Invitation', '') + wk(main + bar('', acts), rail)
P('d-pend', 'Invitations', detail())
P('d-exp', 'Invitations', detail(True))
P('d-wd', 'Invitations', outcome('gy', 'x', 'Withdrawn', 'Collaboration Offer', 'Ada Ononuju withdrew this offer on 26 Oct 2026. Accept and Decline are no longer available. Your application is closed. You can find other opportunities.',
                                 '<section class="ko-card">%s</section>' % facts([('Course', 'Data Analysis with SQL'), ('Role', 'Co-Creator'), ('Share', '15%'), ('Status', 'Withdrawn')]).replace('class="fx3 "', 'class="fx3 four"'),
                                 ghost('Back to Invitations', 'INV-001.dc.html') + btn('Find other opportunities', '#')))

# ======================================================================= CR-INV-003 accept
k1, k2 = W.new(True), W.new(True)
def chk(k, t):
    return '<button type="button" class="dc-r {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}"><span class="dc-b">%s</span><span>%s</span></button>' % (k, k, k, ck(12), t)
VER = ['still pending and not expired', 'belongs to you', 'terms not superseded', 'you remain eligible', 'allocation available', 'organization approval', 'agreement and identity verification complete']
P('accept', 'Invitations', ph(DET_PATH + ['Accept'], 'Accept Collaboration Invitation', 'Review the terms, confirm, and Credalio verifies the offer before activating your access.') +
  steps(1, ['Review terms', 'Confirm', 'Processing', 'Done']) +
  wk('''<section class="ds-card ac6 ob-in2"><div class="ac6-h">%s<p>You’re accepting the role of <b>Co-Creator</b> on <b>Data Analysis with SQL</b>, with a proposed <b>20%%</b> share of distributable course earnings.</p></div>%s</section>
<div class="ac6-k ob-in3">%s%s</div>''' % (cov('Data Analysis with SQL', 52), facts([('Role', 'Co-Creator'), ('Revenue share', '20%'), ('Covered earnings', 'All course channels')]),
          chk(k1, 'I understand my role, responsibilities and contribution requirements.'), chk(k2, 'I have reviewed and agree to the collaboration and revenue-sharing terms.')) +
     bar('<a class="ds-link" href="INV-002.dc.html">Back</a>', '<span class="cf-g {{c%s}}">%s</span>' % (k2, btn('Confirm Acceptance', 'INV-005A.dc.html'))),
     '''<section class="ds-card rx vf6 ob-in3"><span class="rx-k">Checked on confirm</span><ul>%s</ul></section>''' % ''.join(
         '<li style="--i: %d"><span class="vf6-s"></span><span>%s</span></li>' % (i, v) for i, v in enumerate(VER))))

# ======================================================================= CR-INV-004 decline
RSN = [('I’m not available at this time', ''), ('The course isn’t a good match for my expertise', ''), ('The proposed revenue share doesn’t meet my expectations', 'Lead Creator may send a revised offer'),
       ('The responsibilities don’t match my interests', ''), ('The timeline doesn’t work for me', ''), ('Other reason', '')]
P('decline', 'Invitations', ph(DET_PATH + ['Decline'], 'Decline Collaboration Invitation', 'Let the Lead Creator know why you’re unable to participate.') +
  wk('''<section class="ds-card fc ob-in2"><div class="fc-h"><div><h2>Reason for declining (required)</h2></div></div><div class="rsn d6">%s</div>%s</section>''' % (
      ''.join(W.opt('<span class="o-t"><b>%s</b>%s</span>' % (r, ('<span>%s</span>' % s) if s else ''), i == 2, 'drs', 'sm') for i, (r, s) in enumerate(RSN)),
      field('Additional details (optional)', '<textarea class="ds-in ta3" rows="2" aria-label="Additional details">Happy to join at 25%.</textarea>', cls='rsn-d')) +
     bar('<a class="ds-link" href="INV-002.dc.html">Cancel</a>', red('Confirm Decline', 'INV-005C.dc.html')),
     '''<section class="ds-card rx dn6 ob-in3"><div class="dn6-c">%s<span><b>Data Analysis with SQL</b><em>Co-Creator · 20%%</em></span></div></section><section class="ds-card rx dn6n ob-in4"><span class="dn6-i">%s</span><p>Your selected reason is shared with the Lead Creator. Declining does not affect your Creator Reputation Score. The invitation closes and cannot be accepted afterwards.</p></section>''' % (cov('Data Analysis with SQL', 40), INFO)))

# ======================================================================= CR-INV-005A–G outcomes
LK = lambda *a: '</div><div class="ko-lk">%s' % ''.join('<a class="ds-link" href="%s">%s</a>' % (h, l) for l, h in a)
P('o-a', 'Invitations', outcome('ok', 'check', 'Accepted', 'You’re now part of the course team', 'You’re now a Co-Creator on Data Analysis with SQL. Your assigned scope opens in a restricted Course Studio.',
                                 '<div class="tj6">%s<span class="tj6-l"><i></i></span>%s</div>' % (pa('AM', 44), pa('AO', 44)), btn('Go to Course Studio', 'STU-020-CO.dc.html') + LK(('View My Collaborations', 'NAV-002.dc.html'))))
P('o-b', 'Invitations', outcome('am', 'clock', 'Accepted · Activation Pending', 'Acceptance recorded, activation pending', 'Organization approval or verification is still required. You will get access as soon as it completes.',
                                 '<ol class="pg6"><li class="dn"><i>%s</i>Accepted</li><li class="on"><i></i>Approval &amp; verification</li><li><i></i>Access</li></ol>' % ck(10), btn('View Invitation Status', 'INV-001.dc.html')))
P('o-c', 'Invitations', outcome('gy', 'x', 'Declined', 'Invitation declined', 'You’ve declined the invitation to collaborate on Data Analysis with SQL. Your response is recorded and the Lead Creator will be notified.', '',
                                 ghost('Explore Collaboration Opportunities', '#') + btn('Back to My Invitations', 'INV-001.dc.html')))
P('o-d', 'Invitations', outcome('gy', 'clock', 'Expired', 'This invitation has expired', 'You can no longer respond. The Lead Creator can send a new invitation.', '', btn('Back to My Invitations', 'INV-001.dc.html')))
P('o-e', 'Invitations', outcome('gy', 'x', 'Withdrawn', 'The Lead Creator withdrew this invitation', 'Nothing else is needed from you.', '', btn('Back to My Invitations', 'INV-001.dc.html')))
P('o-f', 'Invitations', outcome('cb', 'check', 'Already responded', 'You’ve already responded', 'This invitation was answered on 24 Oct 2026.', '', btn('View Decision', 'INV-001-ALL.dc.html')))
P('o-g', 'Invitations', outcome('am', 'layers', 'Superseded', 'A revised invitation is available', 'The terms changed, so this offer can’t be accepted. Review the new one.', '', btn('Review New Invitation', 'INV-002.dc.html')))

# ======================================================================= CR-NAV-002 Shared Courses
SHARED = [('Data Analysis with SQL', 'AM', 'Co-Creator', 20, 'Chapters 2–3'), ('Python for Beginners', 'SY', 'Content Contributor', 15, '')]
P('shared', 'Shared Courses', ph(['Creator Studio', 'Collaboration', 'Shared Courses'], 'Courses', 'Courses you lead and courses you collaborate on are kept apart.', right=btn('Create New', 'STU-001.dc.html')) +
  '<div class="sc6 ob-in2">%s</div>' % ''.join(
      '''<article class="sc6-c" style="--i: %d"><div class="sc6-v">%s<span class="sc6-g"></span></div><div class="sc6-b"><span class="sc6-t"><span class="sc6-mc">%s</span><b>%s</b></span><span class="sc6-f">%s<span><em>Lead Creator</em>%s</span></span>
<div class="sc6-m"><span><em>Your role</em>%s</span><span><em>Your share</em><b>%d%%</b></span><span><em>Status</em>%s</span></div><a class="ds-btn sm2 sc6-o" href="%s"><span>Open Course Studio</span><span class="ob-arrow">%s</span></a></div></article>''' % (
          i, cov(t, 64), cov(t, 44), t, pa(k, 28), PPL[k][1], role(r), p, tag('Active', 'green'), 'STU-020-CO.dc.html' if i == 0 else '#', ARROW) for i, (t, k, r, p, sc) in enumerate(SHARED)) +
  '<section class="ds-card rs6 ob-in3"><span class="rs6-i">%s</span><p>Shared courses open a restricted Course Studio: only your assigned scope is editable. Ownership, pricing, publishing and team controls belong to the Lead Creator.</p></section>' % ic('lock', 18, 2))

# ======================================================================= assembly
NAVS = sorted(set(p[1] for p in PAGES))
def body():
    blocks = '\n'.join('<sc-if value="{{p_%s}}" hint-placeholder-val="{{ %s }}">\n%s\n</sc-if>' % (k.replace('-', '_'), 'true' if k == 'i-pend' else 'false', b) for k, _, b in PAGES)
    sides = '\n'.join('<sc-if value="{{n_%d}}" hint-placeholder-val="{{ %s }}">%s</sc-if>' % (i, 'true' if n == 'Invitations' else 'false', cr_side(n)) for i, n in enumerate(NAVS))
    return '''<div class="ds-root cr-root">
%s
<div style="min-width: 0; display: flex; flex-direction: column">
%s
<main class="ds-main mg-main cl-main {{tone}}">
%s
</main>
</div>
</div>''' % (sides, CR_TOP, blocks)
TONE = {'o-b': 'am', 'o-c': 'gy', 'o-d': 'gy', 'o-e': 'gy', 'd-wd': 'gy', 'd-exp': 'am', 'o-g': 'am', 'o-a': 'ok'}
JS = W.js() + '''var PG = %s, NV = %s, TONE = %s;
class Component extends DCLogic {
  renderVals() {
    var pg = this.props.page || 'i-pend', v = togVals(this), self = this;
    Object.keys(PG).forEach(function (k) { v['p_'.concat(k.replace('-', '_'))] = k === pg; });
    NV.forEach(function (n, i) { v['n_'.concat(i)] = PG[pg] === n; });
    v.tone = 'tn-'.concat(TONE[pg] || 'cb');
    v.navCls = this.state.nav ? 'ds-open' : '';
    v.toggleNav = function () { self.setState({ nav: !self.state.nav }); };
    return v;
  }
}''' % (json.dumps({k: n for k, n, _ in PAGES}), json.dumps(NAVS), json.dumps(TONE))

CSS = stu11.CSS.replace('.bc:has(+ .pg-h .ds-back){display:none}', '').replace('.ko:has(.nx5){max-width:860px}', '').replace('.mg-main:has(.ov-scrim){z-index:30}', '').replace('.cl-main .pg-hr:has(.ps5){display:flex !important}', '') + open(__file__.replace('stu12.py', 'stu12.css')).read()
write('Collab3.dc.html', doc('Collaboration · my invitations and shared courses · shared source', kit.KIT_CSS + '\n' + dash.DASH_CSS + BASE_CSS + WK_CSS + CSS, body(), JS))

BOARDS = [
    ('INV-001', 'i-pend', 'CR-INV-001 · My Invitations (pending)'),
    ('INV-001-ACCEPTED', 'i-acc', 'CR-INV-001 · My Invitations (accepted)'),
    ('INV-001-DECLINED', 'i-dec', 'CR-INV-001 · My Invitations (declined)'),
    ('INV-001-ALL', 'i-all', 'CR-INV-001 · My Invitations (all)'),
    ('INV-001-EMPTY', 'i-empty', 'CR-INV-001 · My Invitations (empty)'),
    ('INV-002', 'd-pend', 'CR-INV-002 · Invitation details'),
    ('INV-002-EXPIRED', 'd-exp', 'CR-INV-002 · Invitation details (expired)'),
    ('INV-002-WITHDRAWN', 'd-wd', 'CR-INV-002 · Offer withdrawn'),
    ('INV-003', 'accept', 'CR-INV-003 · Accept invitation'),
    ('INV-004', 'decline', 'CR-INV-004 · Decline invitation'),
    ('INV-005A', 'o-a', 'CR-INV-005A · Accepted'),
    ('INV-005B', 'o-b', 'CR-INV-005B · Accepted, activation pending'),
    ('INV-005C', 'o-c', 'CR-INV-005C · Declined'),
    ('INV-005D', 'o-d', 'CR-INV-005D · Expired'),
    ('INV-005E', 'o-e', 'CR-INV-005E · Withdrawn'),
    ('INV-005F', 'o-f', 'CR-INV-005F · Already responded'),
    ('INV-005G', 'o-g', 'CR-INV-005G · Superseded'),
    ('NAV-002', 'shared', 'CR-NAV-002 · Shared Courses'),
]
BOARDS = [(c, 'Collab3', {'page': p}, t) for c, p, t in BOARDS]

if __name__ == '__main__':
    import sys
    H = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else {}
    for code, src, props, title in BOARDS:
        hd, hm = H.get(code, (3000, 3000))
        write(code + '.dc.html', wrapper(title + ' · Desktop', src, props, 1440, hd))
        write(code + '-Mobile.dc.html', wrapper(title + ' · Mobile', src, props, 390, hm))
    print('ok', len(BOARDS), 'boards; toggles', W.n)
