"""Link 4 · Batch 11: open collaboration (lead creator), CR-COL-006A to CR-COL-010-WITHDRAW.
Client copy word for word (prototype-only notes omitted).

Collab2.dc.html (prop page) in the Course Studio workspace shell (Manage > Collaborators).
Reuses batch 10 (stu10: people, roles, share bars, banner, CSS) and stu7 / stu8 helpers.
"""
import json
from l4kit import *
from rail import *
from kit import coin, credit, emblem
import stu7, stu8, stu10
from stu7 import wk, bar, steps, outcome
from stu8 import kpis, note, facts, stars
from stu10 import pa, who, role, share, ghost, link, ARR, LATER, COLLAB, PPL

PPL['CO'] = (None, 'Chidi Obi', '', 'h4')
PPL['JK'] = (None, 'Jide Kehinde', '', 'h2')
PPL['SK'] = (None, 'Sade Kolawole', '', 'h3')

W = Toggles()
PAGES = []
def P(key, body):
    PAGES.append((key, body))
OC = COLLAB + ' · Open collaboration'
def red(label, href):
    return btn(label, href).replace('class="ds-btn"', 'class="ds-btn btn-dz"', 1)
def dlg(back, label, head, body, foot, cls=''):
    return ('<a class="ov-scrim" href="%s" aria-label="Close"></a><div class="dl %s" role="dialog" aria-modal="true" aria-label="%s"><header class="dl-h">%s<a class="ds-x sm" href="%s" aria-label="Close">%s</a></header>'
            '<div class="dl-b">%s</div><footer class="dl-f">%s</footer></div>') % (back, cls, label, head, back, ic('x', 16, 2.2), body, foot)
def ta(text, label, rows=2):
    return '<textarea class="ds-in ta3" rows="%d" aria-label="%s">%s</textarea>' % (rows, label, text)
def seats(filled, total=2):
    return '<span class="sts2" aria-label="%d of %d positions filled">%s</span>' % (filled, total, ''.join('<i class="%s"></i>' % ('on' if i < filled else '') for i in range(total)))

# ======================================================================= CR-COL-006A–E setup
STEPS = ['Opportunity', 'Expertise', 'Qualifications', 'Revenue', 'Review &amp; publish']
NXT = ['COL-006B', 'COL-006C', 'COL-006D', 'COL-006E', 'COL-006F']
PRV = ['COL-001', 'COL-006A', 'COL-006B', 'COL-006C', 'COL-006D']
TAGS = ['Data Analytics', 'SQL', 'Business Intelligence']
def opp_card(stage):
    """Live preview of the opportunity being built; fields fill in as steps complete."""
    k = lambda n: ' on' if stage >= n else ''
    return '''<section class="ds-card rx opv ob-in3" aria-hidden="true"><div class="opv-h"><span class="rx-k">Preview opportunity</span><span class="opv-st">%s</span></div>
<div class="opv-c"><div class="opv-t"><span class="opv-k">Open for Collaboration</span><span class="opv-p">%s<span>2 Positions</span></span></div>
<b>Data Analytics Co-Creators Needed</b><p>Help build a practical SQL and Business Intelligence course for aspiring data analysts.</p>
<div class="opv-g%s">%s</div>
<div class="opv-s"><span class="opv-r%s"><em>Requirements</em><b>Verified expertise · Reputation ≥ 70</b></span><span class="opv-r%s"><em>Total proposed share</em><b class="opv-pc">30%%</b></span><span class="opv-r on"><em>Application deadline</em><b>30 Nov</b></span></div></div></section>''' % (
        ''.join('<i class="%s"></i>' % ('on' if i <= stage else '') for i in range(5)), seats(0),
        k(1), ''.join('<span>%s</span>' % t for t in TAGS), k(2), k(3))
def setup(i, body, rail_extra='', acts=None):
    acts = acts or (ghost('Save draft', '#') + btn('Save &amp; continue', NXT[i] + '.dc.html'))
    return (LATER + page_head(OC, 'Open for Collaboration', 'Data Analysis with SQL · Opportunity setup') + steps(i, STEPS) +
            wk(body + bar('<a class="ds-link" href="%s.dc.html">Back</a>' % PRV[i], acts), opp_card(i) + rail_extra))

P('s-a', setup(0, '''<section class="ds-card fc ivf ob-in2">
<div class="iv-2">%s%s</div>%s<div class="iv-2 tx">%s%s</div>
<div class="iv-3 thr">%s%s%s</div></section>''' % (
    field('Course title', '<div class="ds-in ro">%s<span>Data Analysis with SQL</span></div>' % ic('lock', 14, 2)),
    field('Collaboration title', '<input class="ds-in" value="Data Analytics Co-Creators Needed" aria-label="Collaboration title">'),
    field('Short course summary', ta('Practical SQL and Business Intelligence course for aspiring data analysts.', 'Short course summary', 1).replace('ta3', 'ta3 one')),
    field('What help is needed', ta('Lessons, exercises, assessments and learning resources for the SQL Joins and Reporting chapters.', 'What help is needed')),
    field('Expected responsibilities', ta('Write and record lessons, build practice tasks, review peer work.', 'Expected responsibilities')),
    field('Positions', '<div class="stp3"><button type="button" class="ds-x xs" aria-label="Fewer">%s</button><b>2</b><button type="button" class="ds-x xs" aria-label="More">%s</button>%s</div>' % (ICON('<path d="M5 12h14"></path>', 14, 2.4), ic('plus', 14, 2.4), seats(0))),
    field('Contribution period', sel('8 weeks', 'Contribution period')),
    field('Application deadline', '<div class="ds-in ic-in">%s<span>30 Nov 2026</span></div>' % ic('cal', 16, 2)))))

TAX = [('Industry', 'Technology'), ('Domain', 'Data Analytics'), ('Subdomain', 'Business Intelligence')]
P('s-b', setup(1, '''<section class="ds-card fc ob-in2"><div class="fc-h"><div><h2>Match by expertise</h2><p>Same admin-managed taxonomy as Course Studio and validator domain mapping.</p></div></div>
<div class="tx3">%s</div>
<div class="fl tk3"><span class="fl-l">Skills / topics (more than one allowed)</span><div class="tk3-c">%s<button type="button" class="ds-chip adt">%s<span>Add topic</span></button></div></div></section>
<p class="pm-m">%s<span>Only creators whose expertise satisfies the mandatory criteria receive this as a recommendation. It is not shown to every creator.</span></p>''' % (
    ''.join('<div class="tx3-c" style="--i: %d">%s</div>%s' % (i, field(l, sel(v, l)), '<span class="tx3-a" aria-hidden="true">%s</span>' % ic('chev', 14, 2.2) if i < 2 else '') for i, (l, v) in enumerate(TAX)),
    ''.join(W.chip(t, True) for t in ['SQL', 'Power BI', 'Data Visualization']), ic('plus', 13, 2.4), INFO),
    '''<section class="ds-card rx mt4 ob-in4"><span class="rx-k">Who gets recommended</span><div class="mt4-v"><span class="mt4-r"></span><span class="mt4-r b"></span><span class="mt4-r c"></span>%s<i class="d1"></i><i class="d2"></i><i class="d3"></i><i class="x1"></i><i class="x2"></i></div><p class="rx-p">Technology › Data Analytics › Business Intelligence</p></section>''' % (
        '<span class="mt4-c">%s</span>' % ic('target', 20, 2))))

QUAL = [('Require verified subject expertise', 'Required', True), ('Prefer creators with published courses', 'Preferred', True),
        ('Prefer creators with verified learner reviews', 'Preferred', True), ('Prefer creators with completed course sales', 'Preferred', False)]
def qrow(i, t, kind, on):
    k = W.new(on)
    return '<button type="button" class="qr {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}" style="--i: %d"><span class="pmt-b">%s</span><span class="qr-t">%s</span><span class="qr-k %s">%s</span></button>' % (
        k, k, k, i, ck(11), t, 'rq' if kind == 'Required' else '', kind)
P('s-c', setup(2, '''<section class="ds-card fc ob-in2"><div class="fc-h"><div><h2>Preferred creator qualifications</h2><p>Use these to find strong matches. Required ones filter; preferred ones only rank.</p></div></div>
<div class="iv-2 q2"><div class="fl"><span class="fl-l">Minimum Creator Reputation Score</span><div class="rp3"><span class="rp3-t"><i style="width: 70%%"></i><s style="left: 70%%"><b>70</b></s></span><span class="rp3-l"><span>0</span><span>100</span></span></div></div>%s</div>
<div class="qrs">%s</div></section>
<p class="pm-m">%s<span>New creators with verified expertise are not excluded for having few platform sales unless you mark sales as required.</span></p>''' % (
    field('Time active on Credalio', sel('No minimum', 'Time active on Credalio')), ''.join(qrow(i, *q) for i, q in enumerate(QUAL)), INFO)))

RING2 = ('<svg class="rg rg2" viewBox="0 0 120 120" width="150" height="150" aria-hidden="true"><circle cx="60" cy="60" r="50" fill="none" stroke="#EAF0FF" stroke-width="16"></circle>'
         '<circle class="rg2-a" cx="60" cy="60" r="50" fill="none" stroke="#1652F0" stroke-width="16" stroke-dasharray="45.1 400" transform="rotate(-90 60 60)"></circle>'
         '<circle class="rg2-b" cx="60" cy="60" r="50" fill="none" stroke="#7FA2FF" stroke-width="16" stroke-dasharray="45.1 400" transform="rotate(-36.5 60 60)"></circle>'
         '<circle cx="60" cy="60" r="50" fill="none" stroke="#FFFFFF" stroke-width="16" stroke-dasharray="2.5 312" transform="rotate(-37 60 60)"></circle></svg>')
EC_BAR = '<div class="ec4-b" aria-hidden="true"><i class="l" style="flex: 70"></i><i class="a" style="flex: 30"></i></div>'
P('s-d', setup(3, '''<section class="ds-card fc ob-in2"><div class="fc-h"><div><h2>Revenue allocation</h2><p>Applies to all distributable course earnings.</p></div></div>
<div class="rv4"><div class="rv4-v">%s<span class="rv4-c"><b>30%%</b><em>Total offered</em></span></div><div class="rv4-k">
<div class="rv4-r cb"><i></i><span><b>30%%</b><em>Total offered, combined across 2 positions</em></span></div>
<div class="rv4-r lt"><i></i><span><b>15%%</b><em>Proposed per position</em></span></div>
<div class="rv4-r lk"><i></i><span><b>70%%</b><em>Lead keeps</em></span></div></div></div>
<div class="iv-3 thr rv4-f">%s%s%s</div></section>
<p class="pm-m">%s<span>The advertised percentage is not anyone’s contractual share. A specific offer is made to the chosen applicant, who must accept it.</span></p>''' % (
    RING2, field('Total percentage available', '<div class="pcn"><input class="ds-in" value="30" aria-label="Total percentage available"><span>%</span></div>', tipt='Combined, not per creator.'),
    field('Positions', '<div class="ds-in ro">2</div>'), field('Earliest effective date', '<div class="ds-in ic-in">%s<span>1 Dec 2026</span></div>' % ic('cal', 16, 2)), INFO),
    '<section class="ds-card rx ec4 ob-in4"><span class="rx-k">Existing commitments</span>%s<div class="ec4-r ec4-hd"><span></span><span>Share</span></div>%s</section>' % (EC_BAR, ''.join('<div class="ec4-r %s"><span>%s</span><b>%s</b></div>' % (k, l, v) for l, v, k in [
        ('Lead Creator', '70%', ''), ('Accepted collaborators', '0%', ''), ('Available for this opportunity', '30%', 'hi')]))))

REVW = [('Opportunity', 'Data Analytics Co-Creators Needed · 2 positions', 'COL-006A'), ('Matching', 'Technology › Data Analytics › Business Intelligence · SQL, Power BI, Data Visualization', 'COL-006B'),
        ('Requirements', 'Verified expertise (required) · Reputation ≥ 70 · Prefer published courses and reviews', 'COL-006C'),
        ('Compensation', '30% combined · 15% per position proposed · all distributable earnings', 'COL-006D'), ('Deadline', '30 Nov 2026', 'COL-006A')]
P('s-e', setup(4, '''<section class="ds-card rv5 ob-in2">%s</section>
<p class="pm-m">%s<span><b>Applicants will see</b> Course summary, responsibilities, revenue and requirements. Not your unpublished content or private financials.</span></p>''' % (
    ''.join('<div class="rv5-r" style="--i: %d"><span class="rv5-n">%s</span><div><em>%s</em><b>%s</b></div><a class="ds-link sm" href="%s.dc.html">Edit</a></div>' % (i, ck(10), l, v, h) for i, (l, v, h) in enumerate(REVW)), INFO),
    acts=ghost('Save draft', '#') + ghost('Preview as creator', 'COL-007.dc.html') + btn('Publish Opportunity', 'COL-006F.dc.html')))

NEXT4 = [('Matching creators are notified', 'Only creators who meet your mandatory criteria see it'), ('Applications arrive', 'You are notified, and they appear under Collaborators › Applications'),
         ('You shortlist and make an offer', 'Nothing is shared until an applicant accepts your offer'), ('Accepted creators join your team', 'They appear in Collaborators and on the course team')]
P('s-f', outcome('ok', 'check', 'Waiting for applications', 'Your collaboration opportunity is live',
                 '“Data Analytics Co-Creators Needed” is now visible to eligible creators. Applications are open until 30 Nov 2026. You do not need to wait: keep building your course while people respond.',
                 '<section class="ko-card nx5"><div class="nx5-h"><span class="rx-k">What happens next</span><span class="nx5-s">%s<b>0 / 2</b> positions filled</span></div><ol>%s</ol><p class="nt">%s<span>Waiting for people never blocks you. Your course stays fully editable, and you can check progress any time from Collaborators.</span></p></section>' % (
                     seats(0), ''.join('<li class="%s" style="--i: %d"><span>%d</span><div><b>%s</b><em>%s</em></div></li>' % ('on' if i == 0 else '', i, i + 1, t, d) for i, (t, d) in enumerate(NEXT4)), INFO),
                 btn('Continue building course', 'STU-020.dc.html') + '</div><div class="ko-lk"><a class="ds-link" href="COL-010.dc.html">View opportunity</a>'))

# ======================================================================= CR-COL-007 preview as creator
P('prv', '''<div class="pvb ob-in"><span class="pvb-t">%s<span>Preview</span></span><p><b>What eligible creators will see</b> Preview only. Nothing is published.</p><a class="ds-ghost sm" href="COL-006E.dc.html">%s<span>Back to setup</span></a></div>
<section class="oph ob-in2"><div class="oph-l"><div class="oph-t"><span class="oph-k">Open for Collaboration</span><span class="oph-b">Intermediate</span><span class="oph-b">%s 2 Positions</span></div>
<h1>Data Analytics Co-Creators Needed</h1><p>Help build a practical SQL and Business Intelligence course for aspiring data analysts.</p><div class="oph-g">%s</div></div>
<div class="oph-r"><div class="oph-s"><b>30%%</b><em>Total proposed share · combined across two positions · all distributable earnings</em></div><div class="oph-d">%s<span><b>30 Nov</b><em>Application deadline</em></span></div>
<span class="ds-btn is-dis oph-cta" aria-disabled="true"><span>Preview application experience</span><span class="ob-arrow">%s</span></span></div></section>
<div class="op2 ob-in3"><section class="ds-card fc"><span class="op2-i">%s</span><h2>What we’re looking for</h2><p>Creators with practical SQL experience who can contribute lessons, exercises, assessments and learning resources.</p></section>
<section class="ds-card fc"><span class="op2-i">%s</span><h2>Creator requirements</h2><p>Relevant Data Analytics expertise. Additional preferences may apply.</p></section></div>%s''' % (
    ic('eye', 13, 2.2) if 'eye' in EXTRA else ICON('<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"></path><circle cx="12" cy="12" r="3"></circle>', 13, 2.2), ICON(I['back'], 15, 2), seats(0), ''.join('<span>%s</span>' % t for t in TAGS), ic('cal', 18, 2), ARROW, ic('target', 18, 2), ic('valid', 18, 2),
    note('Mandatory rules are explicit; reputation and sales only rank unless you mark them required. No unpublished content, answers or private financials are exposed.', 'lock')))

# ======================================================================= CR-COL-008 applications (tabs, detail, clarify, decline, withdraw)
STAT = {'New': 'amber', 'Under review': '', 'Shortlisted': 'blue', 'Offered': 'blue', 'Declined': ''}
MATCH = {'Strong': 3, 'Good': 2, 'Fair': 1}
APPS = {'SK': ('Verified · 4 courses', 'Strong · SQL, BI', 86, '4.8 (120)', '3 yrs · verified sales'), 'CO': ('Verified', 'Strong · SQL', 79, '4.6 (44)', '1 yr'),
        'LM': ('Verified', 'Good · Power BI', 72, '4.5 (12)', '5 mo'), 'TA': ('New to Credalio', 'Good · SQL', None, 'n/a', '2 mo · no sales'),
        'RB': ('Verified', 'Good · BI', 74, '', ''), 'JK': ('Verified', 'Fair · Excel', 61, '', '')}
def mt(m):
    lvl, rest = m.split(' · ', 1)
    return '<span class="mch"><span class="mch-d">%s</span><span><b>%s</b> · %s</span></span>' % (''.join('<i class="%s"></i>' % ('on' if j < MATCH[lvl] else '') for j in range(3)), lvl, rest)
def rep(v):
    return '<span class="rpt">%s<b>%s</b></span>' % (ring(v, 38, 9, track='#EEF1F7'), v) if v else '<span class="rpt nil">n/a</span>'
TABS8 = [('all', 'All', 7, 'COL-008'), ('new', 'New', 3, 'COL-008-NEW'), ('short', 'Shortlisted', 2, 'COL-008-SHORTLISTED'), ('off', 'Offered', 1, 'COL-008-OFFERED'), ('dec', 'Declined', 1, 'COL-008-DECLINED')]
def ahead(cur):
    return (page_head(OC, 'Applications', '7 applicants · 2 positions', right='<span class="ps5">%s<span><b>0 / 2</b> filled</span></span>' % seats(0) + ghost('Manage opportunity', 'COL-010.dc.html')) +
            '<nav class="utabs ob-in2" aria-label="Applications">%s</nav>' % ''.join('<a href="%s.dc.html" class="ut%s"%s>%s<em class="ut-n">%d</em></a>' % (
                h, ' on' if k == cur else '', ' aria-current="page"' if k == cur else '', l, n) for k, l, n, h in TABS8))
def app_tbl(rows, full, sel_):
    hd = '<span>Creator</span><span>Expertise match</span><span>Reputation</span>' + ('<span>Learner feedback</span><span>History</span>' if full else '<span>Application</span>') + '<span>Status</span>'
    h = ''
    for i, (k, st, app) in enumerate(rows):
        d = APPS[k]
        mid = ('<span class="ap-f">%s</span><span class="ap-h">%s</span>' % (('<b>%s</b>%s' % (d[3].split(' ')[0], ('<em>%s</em>' % d[3].split(' ', 1)[1]) if ' ' in d[3] else '')) if d[3] != 'n/a' else '<span class="nil">n/a</span>', d[4])) if full else '<span class="ap-a">%s</span>' % app
        h += '<a class="ap-r%s" href="COL-008-DETAIL.dc.html" style="--i: %d"><span class="ap-s" aria-hidden="true"></span>%s%s%s%s%s</a>' % (
            ' pick' if k == sel_ else '', i, who(k, sub=d[0]), mt(d[1]), rep(d[2]), mid, tag(st, STAT[st]))
    return '<section class="ds-card ap3 %s ob-in3"><div class="ap-r ap-hd"><span></span>%s</div>%s</section>' % ('full' if full else 'part', hd, h)
def selbar(k, acts):
    return '<div class="sb5 ob-in4"><span class="sb5-w">%s<span><em>Selected</em><b>%s</b></span></span><span class="sb5-a">%s</span></div>' % (pa(k, 32), PPL[k][1], acts)
OPEN_SH_DEC = ghost('Open applicant', 'COL-008-DETAIL.dc.html', 'sm') + ghost('Shortlist', 'COL-008-SHORTLISTED.dc.html', 'sm') + '<a class="ds-link sm dz-l" href="COL-008-DECLINE-APP.dc.html">Decline</a>'
P('a-all', ahead('all') + app_tbl([('SK', 'Shortlisted', ''), ('CO', 'New', ''), ('LM', 'Under review', ''), ('TA', 'New', '')], True, 'CO') + selbar('CO', OPEN_SH_DEC) +
  note('Applicants cannot be added to the course directly. They must accept a specific offer.'))
P('a-new', ahead('new') + app_tbl([('CO', 'New', 'Joins module'), ('TA', 'New', 'Practice sets'), ('RB', 'New', 'Reporting chapter')], False, 'CO') + selbar('CO', OPEN_SH_DEC) +
  note('New: not yet reviewed. Open an applicant to shortlist, ask a question or decline.'))
P('a-short', ahead('short') + app_tbl([('SK', 'Shortlisted', 'Joins module + 4 practice sets'), ('LM', 'Shortlisted', 'Reporting chapter')], False, 'SK') +
  selbar('SK', ghost('Request Clarification', 'COL-008-CLARIFY.dc.html', 'sm') + btn('Make Offer', 'COL-009.dc.html', 'sm2')) +
  note('Shortlisted: compare these applicants, then make an offer. Offers need an individual role and percentage.'))
OFFERED = ahead('off') + app_tbl([('SK', 'Offered', '<b class="ap-o">15%</b> Co-Creator · offer expires 2 Dec')], False, 'SK') + selbar('SK', ghost('View offer', 'COL-009.dc.html', 'sm') + '<a class="ds-link sm dz-l" href="COL-008-WITHDRAW-OFFER.dc.html">Withdraw offer</a>') + \
    note('Offered: the offer sits in the applicant’s Invitations. If they accept, they join the team and a position fills. If they decline, you see their reason.')
P('a-off', OFFERED)
P('a-dec', ahead('dec') + app_tbl([('JK', 'Declined', 'Dashboard tasks')], False, None) +
  note('Declined: the applicant is told the outcome. Applicants who declined an offer also appear here with their reason.'))

# ---- applicant detail
DET_HEAD = '''<header class="adh ob-in"><a class="ds-back" href="COL-008-SHORTLISTED.dc.html">%s<span>Back to Shortlisted</span></a><div class="adh-r"><div class="adh-p">%s<div><span class="adh-k">%s</span><h1 class="ds-h1">%s</h1><p class="ds-sub">%s</p></div></div><div class="adh-a">%s</div></div></header>'''
def det_head(title, sub, acts, kicker=''):
    return '<span class="pg-e adh-e ob-in">%s</span>' % OC + DET_HEAD % (ICON(I['back'], 15, 2), pa('SK', 64), kicker, title, sub, acts)
DET_ACTS = ghost('Request Clarification', 'COL-008-CLARIFY.dc.html') + '<a class="ds-ghost dz-a" href="COL-008-DECLINE-APP.dc.html">Decline Application</a>' + btn('Make Offer', 'COL-009.dc.html')
PERF = '''<section class="ds-card rx pf5 ob-in3"><span class="rx-k">Performance (with sample size)</span><div class="pf5-r">%s<span><b>86</b><em>Reputation</em></span></div>
<div class="pf5-g"><span><b>4.8</b>%s<em>from 120 reviews</em></span><span><b>1,880</b><em>completed sales</em></span></div><p class="rx-p">Metrics always show sample size. Ranking signals not required by you are not used to exclude applicants.</p></section>''' % (ring(86, 64, 10), stars(5))
SKL = '''<section class="ds-card rx ob-in4"><span class="rx-k">Skills &amp; credentials</span><div class="sk5"><span>SQL</span><span>Power BI</span><span class="vf">%s Verified: Data Analytics</span></div></section>''' % ck(10)
PUBC = '<section class="ds-card rx pcr ob-in4"><span class="rx-k">Published courses</span><div class="pc5">%s</div></section>' % ''.join(
    '<div class="pc5-c"><span class="pc5-v">%s</span><div><b>%s</b><em>%s learners · %s ★</em></div></div>' % (ini, t, n, r) for ini, t, n, r in [('SQL', 'SQL for Analysts', '1,240', '4.8'), ('BI', 'Dashboards with Power BI', '640', '4.7')])
DETAIL = (det_head('Sade Kolawole', 'Verified subject expertise · 3 years on Credalio', DET_ACTS, tag('Shortlisted', 'blue')) +
          wk("""<section class="ds-card fc ob-in2"><div class="fc-h"><div><h2>Professional introduction</h2></div></div><p class="ad-p">Senior analyst with 8 years in BI. Teaches SQL workshops for finance teams.</p>
<div class="ad-sk"><span class="rx-k">Skills &amp; credentials</span><div class="sk5"><span>SQL</span><span>Power BI</span><span class="vf">%s Verified: Data Analytics</span></div></div></section>
<section class="ds-card fc ap5 ob-in3"><div class="fc-h"><div><h2>Application</h2></div></div><div class="ap5-g"><div><em>Proposed contribution</em><b>Joins module and 4 practice sets.</b></div><div><em>Availability</em><b>10 hrs/week from 1 Dec.</b></div></div>
<blockquote><em>Statement</em>I want to turn my workshop material into a structured course.</blockquote></section>""" % ck(10),
             PERF + PUBC))
P('a-det', DETAIL)
P('a-clar', DETAIL + dlg('COL-008-DETAIL.dc.html', 'Request clarification', '<span class="dl-i">%s</span><div class="dl-ht"><h2>Request clarification</h2></div>' % ic('chat', 20, 2),
  '''<p class="dl-p">Ask Sade Kolawole a question before you decide. This is not an offer and shares no revenue terms.</p>
<div class="iv-2">%s%s</div>%s
<button type="button" class="dc-r on" aria-pressed="true"><span class="dc-b">%s</span><span>Keep her in Shortlisted while I wait for the reply</span></button>
<p class="dl-n">%s<span>She sees this in My Applications and can reply in-app. Your course content, revenue terms and other applicants stay private.</span></p>''' % (
      field('To', '<div class="ds-in pick">%s<span><b>Sade Kolawole</b><em>Applicant</em></span></div>' % pa('SK', 26)), field('Reply needed by', sel('3 days', 'Reply needed by')),
      field('Your question', ta('Can you confirm you can start on 1 Dec and share a sample practice set you have written before?', 'Your question', 3)), ck(12), ic('lock', 14, 2)),
  ghost('Cancel', 'COL-008-DETAIL.dc.html') + btn('Send request', 'COL-008-CLARIFY-SENT.dc.html'), 'cq5'))
P('a-sent', outcome('ok', 'chat', 'Awaiting reply', 'Clarification requested', 'Sade Kolawole has been asked to reply by 28 Oct 2026. You will be notified when she answers. Nothing changes in her application until you decide.',
                    '<div class="ko-tg">%s%s</div>' % (tag('<i class="lv-d"></i>Awaiting reply', 'amber'), tag('Still shortlisted', 'blue')),
                    btn('Back to Shortlisted', 'COL-008-SHORTLISTED.dc.html') + '</div><div class="ko-lk"><a class="ds-link" href="#">See what the applicant sees</a><a class="ds-link" href="COL-008-CLARIFY-REPLY.dc.html">Next state: reply received</a>'))
P('a-reply', det_head('Sade Kolawole replied', 'Verified subject expertise · Shortlisted', DET_ACTS.replace('Request Clarification', 'Ask another question'), tag('%s Reply received' % ck(10), 'green')) +
  wk('''<section class="ds-card th5 ob-in2"><div class="th5-m mine" style="--i: 0"><div class="th5-b"><em>Your question · 25 Oct</em><p>Can you confirm you can start on 1 Dec and share a sample practice set you have written before?</p></div>%s</div>
<div class="th5-m" style="--i: 1">%s<div class="th5-b"><em>Her reply · 26 Oct</em><p>Yes, I can start on 1 Dec and give 10 hrs a week. I attached a 12-question SQL joins practice set from my workshop.</p>
<a class="th5-f" href="#"><span class="th5-fi">PDF</span><span><b>SQL-joins-practice-set.pdf</b><em>Attachment</em></span>%s</a></div></div></section>''' % (pa('AO', 34), pa('SK', 34), ic('file', 16, 2)) +
     note('A reply is information only. Nothing is offered or agreed until you send an offer and she accepts it.'), PERF + SKL))
P('a-decl', DETAIL + dlg('COL-008-DETAIL.dc.html', 'Decline application from Sade Kolawole', '<span class="wd3-v">%s<span class="wd3-x">%s</span></span>' % (pa('SK', 48), ic('x', 12, 2.6)),
  '''<h2 class="wd3-h">Decline application from Sade Kolawole</h2><p class="dl-p">She is told the outcome. This does not affect her Creator profile.</p>%s%s
<p class="dl-n">%s<span>She sees "Not selected" under My Applications › Declined. You can still find her under Applications › Declined.</span></p>''' % (
      field('Reason (shown to you only)', sel('Another applicant is a closer fit', 'Reason')),
      field('Message to applicant (optional)', ta('Thank you for your interest. We have chosen to continue with another applicant for this position.', 'Message to applicant')), INFO),
  ghost('Cancel', 'COL-008-DETAIL.dc.html') + red('Decline application', 'COL-008-DECLINED.dc.html'), 'wd3'))
P('a-wdo', OFFERED + dlg('COL-008-OFFERED.dc.html', 'Withdraw offer to Sade Kolawole', '<span class="wd3-v">%s<span class="wd3-x">%s</span></span>' % (pa('SK', 48), ic('x', 12, 2.6)),
  '''<h2 class="wd3-h">Withdraw offer to Sade Kolawole</h2><p class="dl-p">Only offers that have not been accepted can be withdrawn.</p><section class="ko-card wo5">%s</section>%s%s
<p class="dl-n">%s<span>Her offer is removed from her Invitations and she is told it was withdrawn. The 15%% reserved share is released and the position stays open. A withdrawn offer cannot be restored, but you can send a new one.</span></p>''' % (
      facts([('Role', 'Co-Creator'), ('Individual share', '15% (reserved)'), ('Sent', '25 Oct 2026'), ('Expires', '2 Dec 2026'), ('Status', 'Offered · awaiting reply')]),
      field('Reason (shown to you only)', sel('Selecting another applicant', 'Reason')),
      field('Message to applicant (optional)', ta('Thank you for applying. We have decided to go in a different direction for this position.', 'Message to applicant')), INFO),
  ghost('Keep offer', 'COL-008-OFFERED.dc.html') + red('Withdraw offer', 'COL-008-OFFER-WITHDRAWN.dc.html'), 'wd3 wo'))
P('a-wdn', outcome('gy', 'x', 'Offer withdrawn', 'Offer withdrawn', 'Sade Kolawole has been told. The 15% share is released and both positions are open again (0 / 2 filled).',
                   '<div class="ko-tg">%s%s</div>' % (tag('Offer withdrawn'), tag('Position still open', 'blue')),
                   ghost('Make a new offer', 'COL-009.dc.html') + btn('Review shortlisted applicants', 'COL-008-SHORTLISTED.dc.html') + '</div><div class="ko-lk"><a class="ds-link" href="#">What the applicant sees</a><a class="ds-link" href="COL-010.dc.html">Back to opportunity</a>'))

# ======================================================================= CR-COL-009 make an offer
FLOW = ['Application received', 'Review', 'Select applicant', 'Define role', 'Assign share', 'Send offer', 'Accept or decline']
P('offer', page_head(OC, 'Make an offer to Sade Kolawole', 'This becomes a standard invitation in her My Invitations. Direct invites and open-collaboration offers use one acceptance flow.') +
  '<ol class="fl5 ob-in2">%s</ol>' % ''.join('<li class="%s"><i>%s</i><span>%s</span></li>' % ('dn' if i < 3 else ('on' if i < 6 else ''), ck(9) if i < 3 else '', l) for i, l in enumerate(FLOW)) +
  wk('''<section class="ds-card fc ivf ob-in2"><div class="iv-3">%s%s%s</div>%s
<div class="pmr">%s<span>Role permissions: default Co-Creator (edit curriculum, lessons, assessments, resources).</span>%s</div>
<div class="iv-2 two">%s%s</div><p class="iv-ag">%s<span>Agreement v3 terms attached</span></p></section>''' % (
      field('Proposed role', sel('Co-Creator', 'Proposed role')),
      field('Individual revenue share (%)', '<div class="pcn"><input class="ds-in" value="15" aria-label="Individual revenue share (%)"><span>%</span></div>', tipt='Not the combined 30%.'),
      field('Effective date', '<div class="ds-in ic-in">%s<span>1 Dec 2026</span></div>' % ic('cal', 16, 2)),
      field('Accepted responsibilities', ta('Joins module and 4 practice sets (Chapter 4).', 'Accepted responsibilities')),
      ic('valid', 16, 2), link('Review permissions', 'COL-002B-OFFER.dc.html'),
      field('Covered earnings', '<div class="ds-in ro">All course channels</div>'), field('Offer expires', sel('7 days', 'Offer expires')), ck(11)) +
     bar('<a class="ds-link" href="COL-008-DETAIL.dc.html">Back</a>', btn('Send Offer', 'COL-008-OFFERED.dc.html')),
     '''<section class="ds-card rx ivp ob-in3" aria-hidden="true"><div class="ivp-h"><span class="ivp-a">%s<span class="ivp-l"><i></i></span>%s</span></div><b class="ivp-n">Sade Kolawole</b><span class="ivp-r">%s<span>Chapter 4</span></span>
<div class="ivp-s"><b>15%%</b><span>Individual revenue share</span></div><div class="iv-al"><div class="iv-alh"><span class="rx-k">Allocation check</span><b>30%% available, 15%% reserved by this offer.</b></div><div class="ac5"><i class="r"></i><i></i></div><div class="ac5-l"><span>This offer 15%%</span><span>Still open 15%%</span></div></div></section>''' % (
         pa('AO', 40), pa('SK', 40), role('Co-Creator'))))

# ======================================================================= CR-COL-010 manage opportunity (+ states + withdraw)
LIFE = ['Draft', 'Open', 'Paused', 'Filled', 'Closed', 'Expired', 'Cancelled']
ACTS10 = 'Actions: edit non-material details, adjust matching, pause/reopen, extend deadline, close remaining positions, withdraw, view accepted collaborators. Material changes to revenue or responsibilities are communicated to existing applicants; outstanding offers are never silently rewritten.'
def life(cur, acts=True):
    return '<section class="ds-card rx lf5 ob-in3"><span class="rx-k">Lifecycle</span><ol>%s</ol>%s</section>' % (
        ''.join('<li class="%s" style="--i: %d"><i></i><span>%s</span></li>' % ('on' if l in cur else ('dn' if LIFE.index(l) < LIFE.index(cur[0]) and l in ('Draft', 'Open') else ''), i, l) for i, l in enumerate(LIFE)),
        '<p class="rx-p">%s</p>' % ACTS10 if acts else '')
def stat10(st, kind, apps, filled, last):
    return '''<section class="ds-card st5 ob-in2"><div class="st5-c"><span class="st5-p %s"><i></i>%s</span><em>Status</em></div><div class="st5-c"><b>%s</b><em>Applications</em></div>
<div class="st5-c">%s<b>%s</b><em>Positions filled</em></div><div class="st5-c"><b>%s</b><em>%s</em></div></section>''' % (kind, st, apps, seats(int(filled[0])), filled, last[0], last[1])
def mhead10(sub, acts):
    return page_head(OC, 'Opportunity management', sub, right=acts)
OPEN_ACTS = ghost('Edit details', 'COL-006A.dc.html') + ghost('Pause', 'COL-010-PAUSED.dc.html') + '<a class="ds-ghost dz-a" href="COL-010-WITHDRAW.dc.html">Withdraw</a>'
LATEST = '''<section class="ds-card fc ob-in3"><div class="fc-h"><div><h2>Latest applications</h2></div>%s</div><div class="la5"><div class="la5-r la5-hd"><span>Creator</span><span>Status</span></div>%s</div></section>''' % (
    link('Review applicants', 'COL-008.dc.html'), ''.join('<a class="la5-r" href="COL-008-DETAIL.dc.html" style="--i: %d">%s%s</a>' % (i, who(k, sub=''), tag(s, STAT[s])) for i, (k, s) in enumerate([('SK', 'Shortlisted'), ('CO', 'New')])))
EMPTY = '''<section class="ds-card em5 ob-in3"><div class="em5-v" aria-hidden="true"><span class="em5-r"></span><span class="em5-r b"></span><span class="em5-s"></span><span class="em5-c">%s</span></div><b>No applications yet</b><p>Try widening the matching criteria or extending the deadline.</p>%s</section>''' % (ic('users', 22, 2), ghost('Revise matching criteria', 'COL-006B.dc.html', 'sm'))
def state_band(kind, icon, text):
    return '<section class="ds-card sb6 %s ob-in3"><span class="sb6-i">%s</span><p>%s</p></section>' % (kind, ic(icon, 18, 2), text)
REV_AREA = '''<section class="ds-card ra6 ob-in4"><span class="rx-k">Applications, offers and accepted collaborators:</span><div class="ra6-a">%s<a class="ds-link sm" href="COL-010.dc.html">Back to open opportunity</a></div></section>''' % ghost('Review applications', 'COL-008.dc.html', 'sm')
P('o-open', mhead10('Data Analytics Co-Creators Needed', OPEN_ACTS) + stat10('Open', 'ok', '7', '0 / 2', ('30 Nov', 'Deadline')) + wk(LATEST + note(ACTS10), life(['Open'], False)))
P('o-empty', mhead10('Data Analytics Co-Creators Needed', OPEN_ACTS) + stat10('Open', 'ok', '0', '0 / 2', ('30 Nov', 'Deadline')) + wk(EMPTY + note(ACTS10), life(['Open'], False)))
P('o-paused', mhead10('Data Analytics Co-Creators Needed · Paused', btn('Reopen', 'COL-010.dc.html') + '<a class="ds-ghost dz-a" href="COL-010-WITHDRAW.dc.html">Withdraw</a>') +
  stat10('Paused', 'am', '7', '0 / 2', ('30 Nov', 'Deadline')) + wk(state_band('am', 'clock', 'Paused: no new applications are accepted. Existing applications and offers keep going. Reopen any time.') + REV_AREA, life(['Paused'], False)))
P('o-filled', mhead10('Data Analytics Co-Creators Needed · Filled', btn('View accepted collaborators', 'COL-004.dc.html')) +
  stat10('Filled', 'ok', '7', '2 / 2', ('Closed', 'New applications')) + wk(state_band('ok', 'check', 'Filled: every position has an accepted collaborator. Remaining applicants are told the outcome.') + REV_AREA, life(['Filled'], False)))
P('o-closed', mhead10('Data Analytics Co-Creators Needed · Closed / Expired / Cancelled', ghost('Create new opportunity', 'COL-006A.dc.html') + btn('Reopen with new deadline', 'COL-010.dc.html')) +
  stat10('Closed', 'gy', '7', '1 / 2', ('30 Nov', 'Deadline')) + wk(state_band('gy', 'lock', 'Closed (by you), Expired (deadline passed) or Cancelled (withdrawn): no new applications. Outstanding offers follow their own expiry.') + REV_AREA, life(['Closed', 'Expired', 'Cancelled'], False)))
P('o-wd', mhead10('Data Analytics Co-Creators Needed', OPEN_ACTS) + stat10('Open', 'ok', '7', '0 / 2', ('30 Nov', 'Deadline')) + wk(LATEST + note(ACTS10), life(['Open'], False)) +
  dlg('COL-010.dc.html', 'Withdraw this opportunity?', '<span class="dl-i rd">%s</span><div class="dl-ht"><h2>Withdraw this opportunity?</h2></div>' % ic('warn', 20, 2),
      '''<div class="wd5">%s<span><b>Data Analytics Co-Creators Needed</b><em>7 applications · 0 / 2 filled</em></span></div>%s
<p class="dl-n">%s<span>No new applications are accepted. Applicants are told it was withdrawn. Offers already sent keep their own expiry unless you withdraw them first. Your course is not affected.</span></p>''' % (
          seats(0), field('Message to applicants (optional)', ta('This opportunity has been withdrawn. Thank you for applying.', 'Message to applicants')), INFO),
      ghost('Cancel', 'COL-010.dc.html') + red('Withdraw opportunity', 'COL-010-CLOSED.dc.html'), 'wd3'))

# ======================================================================= assembly
def body():
    blocks = '\n'.join('<sc-if value="{{p_%s}}" hint-placeholder-val="{{ %s }}">\n%s\n</sc-if>' % (k.replace('-', '_'), 'true' if k == 's-a' else 'false', b) for k, b in PAGES)
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
    var pg = this.props.page || 's-a', v = togVals(this), self = this;
    PG.forEach(function (k) { v['p_'.concat(k.replace('-', '_'))] = k === pg; });
    v.navCls = this.state.nav ? 'ds-open' : '';
    v.toggleNav = function () { self.setState({ nav: !self.state.nav }); };
    return v;
  }
}''' % json.dumps([p[0] for p in PAGES])

CSS = stu10.CSS + open(__file__.replace('stu11.py', 'stu11.css')).read()
write('Collab2.dc.html', doc('Open collaboration · setup, applications, offers, manage · shared source', kit.KIT_CSS + '\n' + dash.DASH_CSS + BASE_CSS + CW_CSS + WK_CSS + CSS, body(), JS))

BOARDS = [
    ('COL-006A', 's-a', 'CR-COL-006A · Open collaboration: opportunity (step 1 of 5)'),
    ('COL-006B', 's-b', 'CR-COL-006B · Open collaboration: expertise (step 2 of 5)'),
    ('COL-006C', 's-c', 'CR-COL-006C · Open collaboration: qualifications (step 3 of 5)'),
    ('COL-006D', 's-d', 'CR-COL-006D · Open collaboration: revenue (step 4 of 5)'),
    ('COL-006E', 's-e', 'CR-COL-006E · Open collaboration: review & publish (step 5 of 5)'),
    ('COL-006F', 's-f', 'CR-COL-006F · Opportunity published'),
    ('COL-007', 'prv', 'CR-COL-007 · Preview as creator'),
    ('COL-008', 'a-all', 'CR-COL-008 · Applications (all)'),
    ('COL-008-NEW', 'a-new', 'CR-COL-008 · Applications (new)'),
    ('COL-008-SHORTLISTED', 'a-short', 'CR-COL-008 · Applications (shortlisted)'),
    ('COL-008-OFFERED', 'a-off', 'CR-COL-008 · Applications (offered)'),
    ('COL-008-DECLINED', 'a-dec', 'CR-COL-008 · Applications (declined)'),
    ('COL-008-DETAIL', 'a-det', 'CR-COL-008 · Applicant detail'),
    ('COL-008-CLARIFY', 'a-clar', 'CR-COL-008 · Request clarification'),
    ('COL-008-CLARIFY-SENT', 'a-sent', 'CR-COL-008 · Clarification requested'),
    ('COL-008-CLARIFY-REPLY', 'a-reply', 'CR-COL-008 · Clarification reply received'),
    ('COL-008-DECLINE-APP', 'a-decl', 'CR-COL-008 · Decline application'),
    ('COL-008-WITHDRAW-OFFER', 'a-wdo', 'CR-COL-008 · Withdraw offer'),
    ('COL-008-OFFER-WITHDRAWN', 'a-wdn', 'CR-COL-008 · Offer withdrawn'),
    ('COL-009', 'offer', 'CR-COL-009 · Make an offer'),
    ('COL-010', 'o-open', 'CR-COL-010 · Opportunity management (open)'),
    ('COL-010-EMPTY', 'o-empty', 'CR-COL-010 · Opportunity management (no applications)'),
    ('COL-010-PAUSED', 'o-paused', 'CR-COL-010 · Opportunity paused'),
    ('COL-010-FILLED', 'o-filled', 'CR-COL-010 · Opportunity filled'),
    ('COL-010-CLOSED', 'o-closed', 'CR-COL-010 · Opportunity closed / expired / cancelled'),
    ('COL-010-WITHDRAW', 'o-wd', 'CR-COL-010 · Withdraw opportunity'),
]
BOARDS = [(c, 'Collab2', {'page': p}, t) for c, p, t in BOARDS]

if __name__ == '__main__':
    import sys
    H = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else {}
    for code, src, props, title in BOARDS:
        hd, hm = H.get(code, (3000, 3000))
        write(code + '.dc.html', wrapper(title + ' · Desktop', src, props, 1440, hd))
        write(code + '-Mobile.dc.html', wrapper(title + ' · Mobile', src, props, 390, hm))
    print('ok', len(BOARDS), 'boards; toggles', W.n)
