"""Link 4 · Batch 13: creator side, Opportunities / Apply / My Applications / Update Creator Profile (CR-OPP-001 to 005).
Client copy word for word (prototype-only notes omitted).

Collab4.dc.html (prop page) in the creator dashboard shell. The opportunity detail reuses the COL-007 creator-preview hero
(.oph) so the opportunity looks the same to the lead creator's preview and to the applicant.
"""
import json
from l4kit import *
from rail import *
from kit import coin, credit, emblem
import stu6, stu7, stu8, stu10, stu11, stu12
from stu6 import cr_side, CR_TOP, crumbs
from stu7 import wk, bar, steps, outcome
from stu8 import note, facts
from stu10 import pa, role, ghost, link, ARR, PPL
from stu11 import seats, dlg, ta
from stu12 import red, cov, COV

COV.update({'Data Analytics Co-Creators Needed': ('SQL', 'c1'), 'Excel Modelling Content Contributor': ('XL', 'c4'), 'Excel Modelling Contributor': ('XL', 'c4'),
            'Python Data Cleaning Contributor': ('PY', 'c3'), 'Dashboard Design with Power BI': ('BI', 'c2'), 'Statistics Refresher Co-Creator': ('ST', 'c6'),
            'Finance Modelling Reviewer': ('FM', 'c5')})
LEADS = {'Ada Ononuju': ('AO', 'h1'), 'Mercy Bello': ('MB', 'h2'), 'Tunde Ade': ('TA', 'h4'), 'Sade Kolawole': ('SK', 'h3'), 'Lena Moyo': ('LM', 'h2'), 'Chidi Obi': ('CO', 'h4')}
def lav(name, n=26):
    i, h = LEADS[name]
    return '<span class="la2 %s" style="width: %dpx; height: %dpx; font-size: %dpx">%s</span>' % (h, n, n, max(9, n // 3), i)

W = Toggles()
PAGES = []
def P(key, nav, body):
    PAGES.append((key, nav, body))
def ph(path, h1, sub, right='', links=None):
    links = links or {}
    return (crumbs([(x, '' if i == len(path) - 1 else links.get(x, '#')) for i, x in enumerate(path)]) +
            '<header class="pg-h ob-in"><div class="pg-hl"><h1 class="ds-h1">%s</h1>%s</div>%s</header>' % (h1, ('<p class="ds-sub">%s</p>' % sub) if sub else '', ('<div class="pg-hr">%s</div>' % right) if right else ''))
L = {'Opportunities': 'OPP-001.dc.html', 'My Applications': 'OPP-004.dc.html', 'Details': 'OPP-002.dc.html'}

# ======================================================================= CR-OPP-001 Opportunities
OPPS = [('Data Analytics Co-Creators Needed', 'Data Analytics', 'Intermediate', 2, 'Ada Ononuju', '30 Nov', 'Data Analytics › SQL, Business Intelligence', 30, 'OPP-002', ['SQL', 'Business Intelligence']),
        ('Excel Modelling Content Contributor', 'Finance', 'Advanced', 1, 'Mercy Bello', '12 Dec', 'Finance › Modelling', 10, '#', ['Modelling'])]
def ocard(i, o):
    t, cat, lvl, pos, lead, dl, why, pct, h, hits = o
    w = why.split(' › ')
    return '''<a class="oc7" href="%s" style="--i: %d"><div class="oc7-h">%s<div class="oc7-t"><span class="oc7-k"><span class="oc7-o"><i></i>Open</span><span>%s</span><span>%s</span><span class="oc7-p">%s %d position%s</span></span><b>%s</b>
<span class="oc7-l">%s<span>Lead Creator: <b>%s</b><span class="oc7-dl"> · Deadline %s</span></span></span></div></div>
<div class="oc7-w"><span class="oc7-wi">%s</span><span><em>Why you match:</em> %s › %s</span></div>
<div class="oc7-f"><span class="oc7-s"><b>%d%%</b><em>combined, all earnings</em></span><span class="ds-btn sm2"><span>View</span><span class="ob-arrow">%s</span></span></div></a>''' % (
        h if h != '#' else '#', i, cov(t, 52), cat, lvl, seats(0, pos), pos, '' if pos == 1 else 's', t, lav(lead, 22), lead, dl, ic('target', 15, 2),
        w[0], ', '.join('<mark>%s</mark>' % x for x in w[1].split(', ')), pct, ARROW)
P('list', 'Opportunities', ph(['Creator Studio', 'Collaboration', 'Opportunities'], 'Opportunities', 'Recommended for your expertise. Not every opportunity is visible to every creator.') +
  '<div class="fl7 ob-in2"><label class="ds-in sr6">%s<input placeholder="Search opportunities" aria-label="Search"></label><div class="fl7-s">%s%s</div></div>' % (
      ic('search', 16, 2), field('Category', sel('Data Analytics', 'Category')), field('Roles', sel('Any', 'Roles'))) +
  '<div class="oc7s ob-in3">%s</div>' % ''.join(ocard(i, o) for i, o in enumerate(OPPS)) +
  note('Recommendations only appear when you meet the mandatory eligibility criteria.'))

# ======================================================================= CR-OPP-002 details (+ ineligible) — same hero as COL-007
TAGS = ['Data Analytics', 'SQL', 'Business Intelligence']
def hero(cta):
    return '''<section class="oph ob-in2"><div class="oph-l"><div class="oph-t"><span class="oph-k">Open for Collaboration</span><span class="oph-b">Intermediate</span><span class="oph-b">%s 2 Positions</span></div>
<h1>Data Analytics Co-Creators Needed</h1><p class="oph-lc">%s<span>Lead Creator: <b>Ada Ononuju</b> · <a href="#">View profile</a></span></p><div class="oph-g">%s</div></div>
<div class="oph-r"><div class="oph-s"><b>30%%</b><em>combined · final share set in your individual offer</em></div><div class="oph-d">%s<span><b>30 Nov 2026</b><em>Deadline</em></span></div>%s</div></section>''' % (
        seats(0), lav('Ada Ononuju', 26), ''.join('<span>%s</span>' % t for t in TAGS), ic('cal', 18, 2), cta)
DET = [('course', 'Course overview', 'Practical SQL and Business Intelligence for aspiring data analysts.', 'w'), ('target', 'Skills required', ''.join('<span class="ds-tag line">%s</span>' % s for s in ['SQL', 'Power BI', 'Data Visualization']), ''),
       ('layers', 'Responsibilities', 'Lessons, exercises, assessments, resources', ''), ('clock', 'Contribution period', '8 weeks', 's'), ('users', 'Positions', '2', 's'),
       ('earn', 'Revenue offered', '30% combined · final share set in your individual offer', ''), ('wallet', 'Revenue sources', 'Marketplace Credit sales + subscription earnings', ''),
       ('valid', 'Eligibility', 'Verified Data Analytics expertise · Reputation ≥ 70 preferred', ''), ('file', 'Agreement', 'Collaboration agreement v3 overview', '')]
P('det', 'Opportunities', ph(['Collaboration', 'Opportunities', 'Details'], '', '', links=L).replace('<header class="pg-h ob-in"><div class="pg-hl"><h1 class="ds-h1"></h1></div></header>', '') +
  hero(btn('Apply to Collaborate', 'OPP-003.dc.html', 'oph-go')) +
  '<section class="ds-card dt7 ob-in3">%s</section>' % ''.join(
      '<div class="dt7-c %s" style="--i: %d"><span class="dt7-i">%s</span><div><em>%s</em><b>%s</b></div></div>' % (w, i, ic(icn, 16, 2), l, v) for i, (icn, l, v, w) in enumerate(DET)) +
  note('Applying does not accept a final revenue agreement.'))
P('inel', 'Opportunities', ph(['Collaboration', 'Opportunities', 'Details'], '', '', links=L).replace('<header class="pg-h ob-in"><div class="pg-hl"><h1 class="ds-h1"></h1></div></header>', '') +
  hero('<span class="ds-btn is-dis oph-cta" aria-disabled="true"><span>Apply to Collaborate</span><span class="ob-arrow">%s</span></span>' % ic('lock', 16, 2.2)).replace('Lead Creator: <b>Ada Ononuju</b> · <a href="#">View profile</a>', 'Lead Creator: <b>Ada Ononuju</b>') +
  '''<section class="ds-card ie7 ob-in3"><div class="ie7-v" aria-hidden="true"><span class="ie7-r"></span><span class="ie7-c">%s</span></div>
<div class="ie7-b"><p>This opportunity requires verified Data Analytics expertise. Add and verify it in Creator Profile to become eligible. (Matching and ranking rules are not shown.)</p>
<div class="ie7-g"><div><em>Eligibility</em><b>Verified Data Analytics expertise</b></div><div class="am"><em>Your status</em><b>%s Not yet verified</b></div><div class="nx"><em>Next step</em>%s</div></div></div></section>''' % (
      ic('lock', 22, 2), ic('clock', 14, 2.2), btn('Update Creator Profile', 'OPP-005.dc.html', 'sm2')))

TRACK = ['Applied', 'Under review', 'Shortlisted', 'Offer', 'Accepted']
def track(n):
    if n < 0:
        return '<ol class="tr7 end"><li class="dn"><i>%s</i><span>Applied</span></li><li class="x"><i>%s</i><span>%s</span></li></ol>' % (ck(9), ic('x', 9, 2.6), 'Not selected' if n == -1 else 'Withdrawn')
    return '<ol class="tr7">%s</ol>' % ''.join('<li class="%s" style="--i: %d"><i>%s</i><span>%s</span></li>' % ('dn' if j < n or n == 4 else ('on' if j == n else ''), j, ck(9) if j < n or (n == 4 and j == 4) else '', l) for j, l in enumerate(TRACK))
# ======================================================================= CR-OPP-003 apply
ka = W.new(True)
P('apply', 'Opportunities', ph(['Collaboration', 'Opportunities', 'Apply'], 'Apply to Collaborate', 'Data Analytics Co-Creators Needed · Intermediate', links=L) +
  wk('''<section class="ds-card fc ivf ob-in2">%s<div class="iv-2 tx">%s%s</div><div class="iv-2">%s%s</div>
<div class="fl"><span class="fl-l">Work samples</span><div class="up7">%s<span><b>Upload files</b><em>PDF, slides, video links or repositories</em></span></div></div></section>
<button type="button" class="dc-r ack {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}"><span class="dc-b">%s</span><span>I acknowledge the advertised revenue terms (30%% combined).<em class="ack-n">The final percentage and responsibilities come in an individual offer.</em></span></button>''' % (
      field('Why are you interested in this course?', ta('I teach SQL to finance teams and want to reach analysts.', 'Why are you interested in this course?')),
      field('Relevant expertise and skills', ta('SQL, Power BI, 8 years in BI.', 'Relevant expertise and skills')),
      field('Relevant published courses or portfolio', ta('SQL for Analysts · Dashboards with Power BI', 'Relevant published courses or portfolio')),
      field('Proposed contribution', ta('Joins module and 4 practice sets.', 'Proposed contribution')),
      field('Availability', '<div class="ds-in ic-in">%s<span>10 hrs/week from 1 Dec</span></div>' % ic('clock', 16, 2)),
      ic('plus', 20, 2), ka, ka, ka, ck(12)) +
     bar('<a class="ds-link" href="OPP-002.dc.html">Cancel</a>', '<span class="cf-g {{c%s}}">%s</span>' % (ka, btn('Submit Application', 'OPP-004.dc.html'))),
     '''<section class="ds-card rx opv ob-in3" aria-hidden="true"><div class="opv-h"><span class="rx-k">Applying to</span></div><div class="opv-c"><div class="opv-t"><span class="opv-k">Open for Collaboration</span><span class="opv-p">%s<span>2 Positions</span></span></div>
<b>Data Analytics Co-Creators Needed</b><div class="opv-g on">%s</div><div class="opv-s"><span class="opv-r on"><em>Lead Creator</em><b>Ada Ononuju</b></span><span class="opv-r on"><em>Total proposed share</em><b class="opv-pc">30%%</b></span><span class="opv-r on"><em>Application deadline</em><b>30 Nov</b></span></div></div></section>''' % (
         seats(0), ''.join('<span>%s</span>' % t for t in TAGS)) + '<section class="ds-card rx ob-in4"><span class="rx-k">Progress</span>%s</section>' % track(0).replace('class="tr7"', 'class="tr7 v"')))

# ======================================================================= CR-OPP-004 My Applications (7 tabs)
TABS = [('pend', 'Pending', 'OPP-004'), ('rev', 'Under Review', 'OPP-004-REVIEW'), ('short', 'Shortlisted', 'OPP-004-SHORTLISTED'), ('off', 'Offer Received', 'OPP-004-OFFER'),
        ('acc', 'Accepted', 'OPP-004-ACCEPTED'), ('dec', 'Declined', 'OPP-004-DECLINED'), ('wd', 'Withdrawn', 'OPP-004-WITHDRAWN')]
def atabs(cur):
    return '<nav class="utabs ob-in2" aria-label="My Applications">%s</nav>' % ''.join(
        '<a href="%s.dc.html" class="ut%s"%s>%s<em class="ut-n">1</em></a>' % (h, ' on' if k == cur else '', ' aria-current="page"' if k == cur else '', l) for k, l, h in TABS)
APPS = {
    'pend': ('Excel Modelling Contributor', 'Mercy Bello', '22 Oct', 'Pending', 'amber', 0, 'am', '<a class="ds-ghost dz-a sm" href="OPP-004-WITHDRAW.dc.html">Withdraw</a>',
             'Pending: submitted, not opened by the Lead Creator yet. You can withdraw.'),
    'rev': ('Data Analytics Co-Creators Needed', 'Ada Ononuju', '18 Oct', 'Under review', 'blue', 1, 'cb', ghost('View application', 'OPP-004-CLARIFY.dc.html', 'sm'),
            'Under review: the Lead Creator is reading your application. If they ask a question you answer it here.'),
    'short': ('Python Data Cleaning Contributor', 'Tunde Ade', '12 Oct', 'Shortlisted', 'blue', 2, 'cb', ghost('View application', 'OPP-004-CLARIFY.dc.html', 'sm'),
              'Shortlisted: you are in the final group. An individual offer comes next, if you are chosen.'),
    'off': ('SQL for Finance Teams', 'Sade Kolawole', '8 Oct', 'Offer received · 15%', 'green', 3, 'ok', btn('Open offer', 'INV-002.dc.html', 'sm2'),
            'Offer received: the final percentage and responsibilities are in the offer. It opens under Invitations, where you accept or decline.'),
    'acc': ('Dashboard Design with Power BI', 'Lena Moyo', '1 Oct', 'Accepted', 'green', 4, 'ok', btn('Go to Course Studio', 'STU-020-CO.dc.html', 'sm2'),
            'Accepted: you are a collaborator. The course now appears under Shared Courses.'),
    'dec': ('Statistics Refresher Co-Creator', 'Chidi Obi', '28 Sep', 'Not selected', '', -1, 'gy', ghost('Find other opportunities', 'OPP-001.dc.html', 'sm'),
            'Declined: the Lead Creator chose someone else. This does not affect your Creator Reputation Score.'),
    'wd': ('Finance Modelling Reviewer', 'Mercy Bello', '20 Sep', 'Withdrawn by you', '', -2, 'gy', '<span class="ap7-x">—</span>',
           'Withdrawn: you cancelled this application. You can apply again while the opportunity is still open.'),
}
def acard(k):
    t, lead, d, st, tone, n, kind, act, nt = APPS[k]
    return '''<article class="rc6 ap7 %s ob-in3"><div class="rc6-m">%s<div class="rc6-h"><b>%s</b><span class="ic6-f">%s<span>Lead Creator <b>%s</b></span></span></div></div>
<div class="rc6-k"><span><em>Applied</em><b class="ap7-d">%s</b></span><span><em>Status</em>%s</span></div><div class="rc6-a">%s</div>%s<p class="rc6-n">%s<span>%s</span></p></article>''' % (
        kind, cov(t, 60), t, lav(lead, 22), lead, d, tag(st, tone), act, track(n), INFO, nt)
APP_H = ph(['Creator Studio', 'Collaboration', 'My Applications'], 'My Applications', 'Every application you have sent, by status.')
for k, l, h in TABS:
    P('a-' + k, 'My Applications', APP_H.replace('<span>My Applications</span>', '<a href="OPP-004.dc.html">My Applications</a>%s<span>%s</span>' % (ic('chev', 13, 2), l)) + atabs(k) + acard(k))
P('a-wdc', 'My Applications', APP_H + atabs('pend') + acard('pend') +
  dlg('OPP-004.dc.html', 'Withdraw your application?', '<span class="wd3-v">%s<span class="wd3-x">%s</span></span>' % (cov('Excel Modelling Contributor', 44), ic('x', 12, 2.6)),
      '''<h2 class="wd3-h">Withdraw your application?</h2><p class="dl-p">Excel Modelling Contributor · Mercy Bello</p>%s<p class="dl-n">%s<span>The Lead Creator is told you withdrew. You can apply again while the opportunity is still open.</span></p>''' % (
          field('Reason (optional, shown to the Lead Creator)', ta('I am no longer available during this period.', 'Reason')), INFO),
      ghost('Keep application', 'OPP-004.dc.html') + red('Withdraw application', 'OPP-004-WITHDRAWN.dc.html'), 'wd3'))

# ---- clarification reply
P('a-clar', 'My Applications', ph(['Creator Studio', 'Collaboration', 'My Applications', 'Application'], 'Your application', 'Data Analytics Co-Creators Needed · Ada Ononuju', right=tag('Shortlisted', 'blue'), links=L) +
  wk('''<section class="ds-card th5 cl7 ob-in2"><div class="th5-m" style="--i: 0">%s<div class="th5-b"><em>Question from the Lead Creator · reply by 28 Oct</em><p>Can you confirm you can start on 1 Dec and share a sample practice set you have written before?</p></div></div>
<div class="cl7-r"><span class="fl-l">Your reply</span><div class="cl7-c">%s<div class="cl7-t"><span class="th5-f cl7-f"><span class="th5-fi">PDF</span><span><b>SQL-joins-practice-set.pdf</b><em>Attach file</em></span>%s</span></div></div></div>
<p class="nt">%s<span>Your reply goes only to the Lead Creator. It is not an acceptance of anything.</span></p></section>''' % (
      lav('Ada Ononuju', 34), ta('Yes, I can start on 1 Dec and give 10 hrs a week. Attached is a sample practice set.', 'Your reply', 3), ic('x', 14, 2.2), ic('lock', 14, 2)) +
     bar('<a class="ds-link" href="OPP-004-SHORTLISTED.dc.html">Back</a>', btn('Send reply', 'OPP-004-SHORTLISTED.dc.html')),
     '''<section class="ds-card rx aw7 ob-in3"><span class="rx-k">What you applied with</span><div><em>Proposed contribution</em><b>Joins module and 4 practice sets.</b></div><div><em>Availability</em><b>10 hrs/week from 1 Dec.</b></div></section>
<section class="ds-card rx ob-in4"><span class="rx-k">Progress</span>%s</section>''' % track(2).replace('class="tr7"', 'class="tr7 v"')))

# ======================================================================= CR-OPP-005 update profile (+ submitted)
kc = W.new(True)
P('prof', 'Opportunities', ph(['Collaboration', 'Opportunities', 'Details', 'Update Creator Profile'], 'Update your Creator Profile', 'To apply for “Data Analytics Co-Creators Needed” you need verified Data Analytics expertise.', links=L) +
  '<div class="bn6 cb ob-in">%s<p>Why you are here: the Lead Creator requires verified Data Analytics expertise. Matching and ranking rules are not shown.</p></div>' % INFO +
  wk('''<section class="ds-card fc ivf ob-in2"><div class="fc-h"><div><h2>Add expertise</h2></div></div><div class="iv-3 thr ex7">%s%s%s</div>%s</section>
<button type="button" class="dc-r ack {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}"><span class="dc-b">%s</span><span>I confirm this evidence is mine and accurate.</span></button>
<p class="pm-m">%s<span>Verification usually takes 2 business days. You will be notified in Creator Studio, and Apply to Collaborate switches on once you are verified.</span></p>''' % (
      field('Expertise area', sel('Technology › Data Analytics', 'Expertise area')), field('Years of experience', sel('3', 'Years of experience')), field('Level', sel('Intermediate', 'Level')),
      field('Evidence', '<div class="up7 ev">%s<span><b>Link to a certificate, course, portfolio or employer letter.</b><em>Our team reviews it before the expertise shows as verified.</em></span></div>' % ic('file', 20, 2)),
      kc, kc, kc, ck(12), ic('clock', 16, 2)) +
     bar('<a class="ds-link" href="OPP-002-INELIGIBLE.dc.html">Cancel</a>', '<span class="cf-g {{c%s}}">%s</span>' % (kc, btn('Submit for verification', 'OPP-005-SUBMITTED.dc.html'))),
     '''<section class="ds-card rx rq7 ob-in3"><span class="rx-k">Requirements for this opportunity</span><ul><li class="miss">%s<span>Verified Data Analytics expertise</span>%s</li><li>%s<span>Published course or verified sales</span>%s</li></ul>
<div class="rq7-y"><span class="rx-k">Your verified expertise</span><div class="sk5"><span class="vf">%s Python</span><span class="vf">%s Excel</span><span class="nwx">%s Data Analytics</span></div></div></section>''' % (
         ic('x', 12, 2.6), tag('Missing', 'amber'), ck(10), tag('Not required'), ck(10), ck(10), ic('plus', 11, 2.6))))
P('sub', 'Opportunities', outcome('ok', 'check', 'Under review', 'Submitted for verification', 'Data Analytics (3 years, Intermediate) is under review. We will notify you when it is verified, usually within 2 business days.',
                                  '<div class="ko-tg">%s%s</div>' % (tag('<i class="lv-d"></i>Under review', 'amber'), tag('%s Apply is off until verified' % ic('lock', 11, 2.4))),
                                  ghost('Find other opportunities', 'OPP-001.dc.html') + btn('Back to opportunity', 'OPP-002.dc.html') + '</div><div class="ko-lk"><a class="ds-link" href="OPP-002.dc.html">Next state: verified, can apply</a>'))

# ======================================================================= assembly
NAVS = sorted(set(p[1] for p in PAGES))
def body():
    blocks = '\n'.join('<sc-if value="{{p_%s}}" hint-placeholder-val="{{ %s }}">\n%s\n</sc-if>' % (k.replace('-', '_'), 'true' if k == 'list' else 'false', b) for k, _, b in PAGES)
    sides = '\n'.join('<sc-if value="{{n_%d}}" hint-placeholder-val="{{ %s }}">%s</sc-if>' % (i, 'true' if n == 'Opportunities' else 'false', cr_side(n)) for i, n in enumerate(NAVS))
    return '''<div class="ds-root cr-root">
%s
<div style="min-width: 0; display: flex; flex-direction: column">
%s
<main class="ds-main mg-main cl-main {{tone}}">
%s
</main>
</div>
</div>''' % (sides, CR_TOP, blocks)
TONE = {'a-dec': 'gy', 'a-wd': 'gy', 'a-off': 'ok', 'a-acc': 'ok', 'a-pend': 'am', 'inel': 'am'}
JS = W.js() + '''var PG = %s, NV = %s, TONE = %s;
class Component extends DCLogic {
  renderVals() {
    var pg = this.props.page || 'list', v = togVals(this), self = this;
    Object.keys(PG).forEach(function (k) { v['p_'.concat(k.replace('-', '_'))] = k === pg; });
    NV.forEach(function (n, i) { v['n_'.concat(i)] = PG[pg] === n; });
    v.tone = 'tn-'.concat(TONE[pg] || 'cb');
    v.navCls = this.state.nav ? 'ds-open' : '';
    v.toggleNav = function () { self.setState({ nav: !self.state.nav }); };
    return v;
  }
}''' % (json.dumps({k: n for k, n, _ in PAGES}), json.dumps(NAVS), json.dumps(TONE))

CSS = stu12.CSS.replace('.wk:has(.rv5) .wk-r > .opv{display:none}', '') + open(__file__.replace('stu13.py', 'stu13.css')).read()
write('Collab4.dc.html', doc('Collaboration · opportunities, applications, creator profile · shared source', kit.KIT_CSS + '\n' + dash.DASH_CSS + BASE_CSS + WK_CSS + CSS, body(), JS))

BOARDS = [
    ('OPP-001', 'list', 'CR-OPP-001 · Opportunities'),
    ('OPP-002', 'det', 'CR-OPP-002 · Opportunity details'),
    ('OPP-002-INELIGIBLE', 'inel', 'CR-OPP-002 · Opportunity details (not eligible)'),
    ('OPP-003', 'apply', 'CR-OPP-003 · Apply to Collaborate'),
    ('OPP-004', 'a-pend', 'CR-OPP-004 · My Applications (pending)'),
    ('OPP-004-REVIEW', 'a-rev', 'CR-OPP-004 · My Applications (under review)'),
    ('OPP-004-SHORTLISTED', 'a-short', 'CR-OPP-004 · My Applications (shortlisted)'),
    ('OPP-004-OFFER', 'a-off', 'CR-OPP-004 · My Applications (offer received)'),
    ('OPP-004-ACCEPTED', 'a-acc', 'CR-OPP-004 · My Applications (accepted)'),
    ('OPP-004-DECLINED', 'a-dec', 'CR-OPP-004 · My Applications (declined)'),
    ('OPP-004-WITHDRAWN', 'a-wd', 'CR-OPP-004 · My Applications (withdrawn)'),
    ('OPP-004-WITHDRAW', 'a-wdc', 'CR-OPP-004 · Withdraw application'),
    ('OPP-004-CLARIFY', 'a-clar', 'CR-OPP-004 · Reply to clarification'),
    ('OPP-005', 'prof', 'CR-OPP-005 · Update Creator Profile'),
    ('OPP-005-SUBMITTED', 'sub', 'CR-OPP-005 · Submitted for verification'),
]
BOARDS = [(c, 'Collab4', {'page': p}, t) for c, p, t in BOARDS]

if __name__ == '__main__':
    import sys
    H = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else {}
    for code, src, props, title in BOARDS:
        hd, hm = H.get(code, (3000, 3000))
        write(code + '.dc.html', wrapper(title + ' · Desktop', src, props, 1440, hd))
        write(code + '-Mobile.dc.html', wrapper(title + ' · Mobile', src, props, 390, hm))
    print('ok', len(BOARDS), 'boards; toggles', W.n)
