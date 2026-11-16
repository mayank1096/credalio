"""Landing batch 5 (client review, Professional certificate detail). Patches the live CertDetail.dc.html in place.
Adds: target candidates, eligibility and prerequisites (mandatory vs recommended), competencies with the performance
standard and how each is assessed, assessment framework (duration, attempts, retake wait and fee, delivery),
requirements progress, issuer profile + recognition (what the badge does and doesn't mean), pricing split
(preparation learning in DLP or Credits vs the 150 Credits assessment fee), an inline 3-question eligibility check,
and states via prop `elig` = '' | meets | needs | not | enrolled | done.
Usage: python3 cd5.py <canvas3/project>"""
import re, sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import kit
from kit import tip, ck, nova_av, ARROW
D = sys.argv[1]; P = os.path.join(D, 'CertDetail.dc.html'); s = open(P).read()
assert 'c5-' not in s, 'already patched'

def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:90], s.count(a)); s = s.replace(a, b)
def svg(d, w=18, sw=2):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (w, w, sw, d)
HEART = svg('<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"></path>', 17)
SHARE = svg('<path d="M12 15V4M8 8l4-4 4 4"></path><path d="M5 13v5a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-5"></path>', 17)
XI = svg('<path d="M7 7l10 10M17 7 7 17"></path>', 11, 3)
WARN = svg('<path d="M12 8v5M12 16.5v.2"></path>', 12, 3)

# ---------------------------------------------------------------- hero
s, n = re.subn(r'<span class="ds-tag blue lg"><svg class="ce-seal".*?</svg> Credalio Validated</span>', lambda m: '<span class="ds-tag blue lg"><i class="c5-dot"></i>Gold Validated</span><span class="ds-tag line lg">CEI 93%s</span>' % tip(
    'Credalio Excellence Index: how well this certification is built, scored by independent validators out of 100.'), s, count=1, flags=re.S)
assert n == 1
rep('<span class="dt-fact"><b>3–4 months</b></span>', '<span class="dt-fact"><b>3–4 months</b> to prepare</span><span class="dt-fact"><b>★ 4.8</b> (860)</span>')
rep('<a class="ds-link dt-askm" href="#">', '<div class="c5-acts"><button class="ds-ghost sm {{saveCls}}" type="button" aria-pressed="{{saveOn}}" onClick="{{toggleSave}}">%s<span>{{saveLabel}}</span></button>'
    '<button class="ds-ghost sm" type="button">%s<span>Share</span></button></div>\n<sc-if value="{{hasBan}}" hint-placeholder-val="{{ false }}"><div class="c5-ban {{banCls}}" role="status"><i class="c5-bd" aria-hidden="true"></i><span><b>{{banT}}</b><span>{{banD}}</span></span></div></sc-if>\n'
    '<a class="ds-link dt-askm" href="#">' % (HEART, SHARE))

# ---------------------------------------------------------------- overview: about + who it's for (before "What it proves")
ABOUT = ('This certification checks that you can prepare data, query it with SQL, find what matters and explain it to people who make decisions. '
         'You earn it through assessment against a published standard, not by finishing courses.')
WHO = [('Designed for', 'Early-career analysts, business professionals and people moving into data analytics.'),
       ('Relevant roles', 'Junior Data Analyst, Reporting Analyst, Business Analyst, Data Operations Associate.'),
       ('Experience', 'Recommended, not required: about 6 months working with spreadsheets, reports or business data. Paid, volunteer or project work all count.')]
NEW1 = ('<section class="dt-sec" ref="{{refOverview}}" aria-labelledby="c5-ab">\n<h2 id="c5-ab" class="dt-h2">About this certification</h2>\n<p class="c5-p">%s</p>\n</section>\n\n'
        '<section class="dt-sec" ref="{{refWho}}" aria-labelledby="c5-wh">\n<h2 id="c5-wh" class="dt-h2">Who it’s for</h2>\n<div class="c5-who">%s</div>\n</section>\n\n') % (
    ABOUT, ''.join('<div><span class="c5-k">%s</span><span>%s</span></div>' % w for w in WHO))
rep('<section class="dt-sec" ref="{{refOverview}}" aria-labelledby="ce-o">\n<h2 id="ce-o" class="dt-h2">What it proves</h2>',
    NEW1 + '<section class="dt-sec" ref="{{refComp}}" aria-labelledby="ce-o">\n<div class="c5-sh"><h2 id="ce-o" class="dt-h2">Competencies you’re assessed on</h2><span class="c5-sm">The standard you need to meet</span></div>')

# competencies: standard + how assessed
COMP = {'Data preparation': ('Prepares a raw dataset for analysis with no errors that change the result.', 'Case study'),
        'Querying': ('Writes correct SQL with joins, filters and aggregation for a business question.', 'Exam + case study'),
        'Analysis': ('Identifies the trends that matter and supports each with evidence.', 'Case study'),
        'Visualisation': ('Builds charts a non-specialist reads correctly the first time.', 'Case study'),
        'Statistical reasoning': ('Uses averages, spread and comparison correctly, and says when data can’t support a claim.', 'Exam'),
        'Communication': ('Explains findings and a recommendation clearly in plain language.', 'Final review')}
def comp(m):
    name = m.group(2)
    std, how = COMP[name]
    return '%s<b>%s</b><span>%s</span><span class="c5-std"><em>Standard</em>%s</span><span class="ds-tag line c5-how">Assessed by: %s</span></div>' % (m.group(1), name, m.group(3), std, how)
s, n = re.subn(r'(<div class="ce-cp"><span class="ce-ci"><svg.*?</svg></span>)<b>([^<]+)</b><span>([^<]+)</span></div>', comp, s, flags=re.S)
assert n == 6, n

# ---------------------------------------------------------------- before you begin (after competencies)
NEW2 = '''<section class="dt-sec" ref="{{refReq}}" aria-labelledby="c5-bb">
<h2 id="c5-bb" class="dt-h2">Before you begin</h2>
<div class="c5-req">
<div class="c5-rq"><span class="ds-tag c5-must">Mandatory</span><b>18 or older</b><span>Checked when you register.</span></div>
<div class="c5-rq"><span class="ds-tag c5-must">Mandatory</span><b>Data Foundations, or an accepted equivalent</b><span>Completed on Credalio, or proof of an equivalent qualification reviewed by an assessor.</span></div>
<div class="c5-rq"><span class="ds-tag line">Recommended</span><b>About 6 months of hands-on experience</b><span>With spreadsheets, reports or business data.</span></div>
<div class="c5-rq"><span class="ds-tag line">Helpful knowledge</span><b>Formulas, basic statistics, reading tables and charts</b><span>The preparation courses cover all of it.</span></div>
</div>
<div class="c5-rdy nova-card">%s<p><b>Not sure you qualify?</b> The eligibility check takes three questions. Nova can suggest preparation, but only the check decides eligibility.</p><button class="ds-ghost sm" type="button" onClick="{{openQuiz}}">Check my eligibility</button></div>
</section>

''' % nova_av()
rep('<section class="dt-sec" ref="{{refEarn}}"', NEW2 + '<section class="dt-sec" ref="{{refEarn}}"')

# assessment framework details
rep('<div class="ce-sd">Timed, 60 questions on the six competencies.</div></div><span class="ds-tag ce-pm">Pass mark 70%</span></div></div></div>',
    '<div class="ce-sd">Timed, 60 questions on the six competencies.</div><div class="c5-ax"><span>90 minutes</span><span>Online, proctored</span><span>2 attempts</span></div></div><span class="ds-tag ce-pm">Pass mark 70%</span></div></div></div>')
rep('An assessor reviews it.</div></div><span class="ds-tag ce-pm">Pass mark 70%</span></div></div></div>',
    'An assessor reviews it.</div><div class="c5-ax"><span>10 days to submit</span><span>Reviewed within 7 days</span><span>2 submissions</span></div></div><span class="ds-tag ce-pm">Pass mark 70%</span></div></div></div>')
rep('<div class="ce-sd">A short conversation about your case study with an assessor.</div></div>',
    '<div class="ce-sd">A short conversation about your case study with an assessor.</div><div class="c5-ax"><span>30 minutes</span><span>Live video call</span><span>Booked when your case study passes</span></div></div>')
rep('<h2 id="ce-e" class="dt-h2">How you earn it</h2>', '<h2 id="ce-e" class="dt-h2">How you earn it</h2>\n<p class="c5-p c5-pf">Retakes: wait 14 days, then 40 Credits per attempt. Exam questions and marking rubrics are never shown.</p>')
rep('<div class="ce-sc">\n<div class="ce-shd"><div><div class="ce-sn">Required learning', '<div class="ce-sc">\n<div class="ce-shd"><div><div class="ce-sn">Preparation learning')

# requirements progress (enrolled / done)
REQS = ['Complete the preparation learning', 'Pass the core knowledge exam', 'Submit the practical case study', 'Pass the final review', 'Verify your identity', 'Agree to the code of conduct']
NEW3 = ('<sc-if value="{{showProg}}" hint-placeholder-val="{{ false }}"><section class="dt-sec" aria-labelledby="c5-pr">\n<div class="c5-sh"><h2 id="c5-pr" class="dt-h2">Your requirements</h2><span class="c5-sm">{{progLabel}}</span></div>\n'
        '<ol class="c5-rl"><sc-for list="{{reqs}}" as="r" hint-placeholder-count="6"><li class="{{r.cls}}"><span class="c5-rn">{{r.mark}}</span><b>{{r.t}}</b><span class="ds-tag {{r.tag}}">{{r.s}}</span></li></sc-for></ol>\n'
        '<p class="c5-fine">Progress comes from verified learning and assessment records. It can’t be ticked off by hand.</p>\n</section></sc-if>\n\n')
rep('<section class="dt-sec" ref="{{refCredential}}"', NEW3 + '<section class="dt-sec" ref="{{refCredential}}"')

# ---------------------------------------------------------------- issuer + recognition, pricing (after "What you get")
NEW4 = '''<section class="dt-sec" ref="{{refIssuer}}" aria-labelledby="c5-is">
<h2 id="c5-is" class="dt-h2">Who issues it</h2>
<div class="c5-iss">
<div class="c5-ip"><span class="c5-av">NU</span><div><span class="c5-k">Issuer</span><b>Northgate University</b><span>Verified institution · 3 certifications on Credalio. The issuer awards and signs the credential.</span></div></div>
<div class="c5-ip"><span class="c5-av">AO</span><div><span class="c5-k">Content developed by</span><b>Amara Okafor</b><span>Senior Data Analyst · affiliated creator for the preparation courses.</span></div></div>
</div>
<div class="c5-mean">
<div><span class="c5-k">What the Gold Validated badge means</span><ul><li><span class="c5-ok">%s</span>Independent validators checked the competencies, assessments and marking.</li><li><span class="c5-ok">%s</span>The assessment matches the published standard.</li></ul></div>
<div><span class="c5-k">What it doesn’t mean</span><ul><li><span class="c5-no">%s</span>It isn’t an external accreditation or a regulated licence.</li><li><span class="c5-no">%s</span>It doesn’t guarantee a job or a promotion.</li></ul></div>
</div>
<a class="ds-link" href="Record.dc.html">View the public validation record →</a>
</section>

<section class="dt-sec" ref="{{refPrice}}" aria-labelledby="c5-pc">
<div class="c5-sh"><h2 id="c5-pc" class="dt-h2">What it costs</h2><a class="ds-link" href="Pricing.dc.html">Compare plans →</a></div>
<div class="c5-cost">
<div class="c5-cc"><span class="c5-k">1 · Preparation learning</span><span class="c5-pv"><span class="dlp-c" aria-hidden="true"></span><b>1,700 DLP</b></span><span>The 4 courses use DLP from your plan, or own each with Credits (3,400 Credits for all four). Courses you’ve already finished aren’t charged again.</span></div>
<div class="c5-plus" aria-hidden="true">+</div>
<div class="c5-cc c5-fee"><span class="c5-k">2 · Assessment fee</span><span class="c5-pv"><i class="cr-c" aria-hidden="true">C</i><b>150 Credits</b></span><span>The exam, case study review, final review, credential and one retake of each. Charged separately. An employer or institution can sponsor it.</span></div>
</div>
<p class="c5-fine">DLP and Credits are separate. The assessment fee is never paid in DLP.</p>
</section>

''' % (ck(11), ck(11), XI, XI)
rep('<section class="dt-sec" ref="{{refFaq}}"', NEW4 + '<section class="dt-sec" ref="{{refFaq}}"')

# ---------------------------------------------------------------- side card
old = s[s.index('<div class="dt-cbody">'):s.index('</div>\n</div>\n</aside>')]
NEWCARD = '''<div class="dt-cbody">
<span class="dt-lab">Assessment fee%s</span>
<div class="dt-amt"><i class="cr-c lg" aria-hidden="true">C</i><b>150</b><span>Credits, one time</span></div>
<span class="c5-prep"><span class="dlp-c" aria-hidden="true"></span>Plus preparation: 1,700 DLP, or own the courses with Credits</span>
<sc-if value="{{isGuest}}" hint-placeholder-val="{{ true }}">
<sc-if value="{{quizClosed}}" hint-placeholder-val="{{ true }}"><p class="c5-cn">Check you meet the requirements before you choose how to pay.</p><button class="ds-btn dt-cta" type="button" onClick="{{openQuiz}}"><span>Check my eligibility</span><span class="ob-arrow">%s</span></button></sc-if>
<sc-if value="{{quizOpen}}" hint-placeholder-val="{{ false }}"><div class="c5-qz" role="group" aria-label="Eligibility check">
<span class="c5-k">Eligibility check · 3 questions</span>
<sc-for list="{{qs}}" as="q" hint-placeholder-count="3"><div class="c5-q"><b>{{q.t}}</b><div class="c5-qo"><sc-for list="{{q.opts}}" as="o" hint-placeholder-count="3"><button class="c5-o {{o.cls}}" type="button" aria-pressed="{{o.on}}" onClick="{{o.pick}}">{{o.label}}</button></sc-for></div></div></sc-for>
<button class="ds-btn dt-cta {{seeDis}}" type="button" onClick="{{seeResult}}"><span>See my result</span><span class="ob-arrow">%s</span></button>
</div></sc-if>
</sc-if>
<sc-if value="{{hasRes}}" hint-placeholder-val="{{ false }}"><div class="c5-res {{resCls}}" role="status"><span class="ds-tag {{resTag}}">{{resChip}}</span><b>{{resT}}</b>
<ul><sc-for list="{{resItems}}" as="r" hint-placeholder-count="3"><li><span class="c5-m {{r.k}}">{{r.m}}</span><span><em>{{r.t}}</em>{{r.s}}</span></li></sc-for></ul><p>{{resNote}}</p></div>
<a class="ds-btn dt-cta" href="{{resHref}}"><span>{{resCta}}</span><span class="ob-arrow">%s</span></a>
<sc-if value="{{canRedo}}" hint-placeholder-val="{{ false }}"><button class="ds-link c5-redo" type="button" onClick="{{redo}}">Change my answers</button></sc-if></sc-if>
<sc-if value="{{isEnrolled}}" hint-placeholder-val="{{ false }}"><div class="c5-res c5-cb" role="status"><span class="ds-tag blue">Enrolled · in progress</span><b>2 of 6 requirements complete</b><span class="cd-pb" aria-hidden="true"><i style="width: 33%%"></i></span><p><em>Next</em> Submit the practical case study · due 4 Dec · 1 of 2 submissions</p></div>
<a class="ds-btn dt-cta" href="#"><span>Continue certification</span><span class="ob-arrow">%s</span></a></sc-if>
<sc-if value="{{isDone}}" hint-placeholder-val="{{ false }}"><div class="c5-res c5-rok" role="status"><span class="ds-tag green">Certified · issued 12 Oct 2026</span><b>You hold this certification</b>
<dl class="c5-dl"><div><dt>Credential ID</dt><dd>7F2-91</dd></div><div><dt>Valid until</dt><dd>12 Oct 2029</dd></div><div><dt>Renewal</dt><dd>Short review of recent work</dd></div></dl></div>
<a class="ds-btn dt-cta" href="#"><span>View in Digital Backpack</span><span class="ob-arrow">%s</span></a><button class="ds-ghost sm" type="button">%sShare verification link</button></sc-if>
<a class="ds-ghost sm" href="#"><span class="nv-av sm" aria-hidden="true"><img src="''' % (
    tip('Covers the exam, case study review, final review, your credential and one retake of each. Preparation courses are separate and use DLP, or Credits if you own them.', 'r dn'.split()[0]) if False else tip('Covers the exam, case study review, final review, your credential and one retake of each. Preparation courses are separate and use DLP, or Credits if you own them.'),
    ARROW, ARROW, ARROW, ARROW, ARROW, SHARE) + kit.NOVA + '''" alt=""></span><span>Ask Nova if it fits my goal</span></a>
'''
s = s.replace(old, NEWCARD, 1)
rep('<div><b>150 Credits</b><span>One time</span></div>\n<button class="ds-btn" type="button" onClick="{{start}}"><span>{{barCta}}</span>',
    '<div><b>150 Credits</b><span>{{barSub}}</span></div>\n<button class="ds-btn" type="button" onClick="{{barGo}}"><span>{{barCta}}</span>')

# ---------------------------------------------------------------- JS
FAQ = [('Do I have to take the four courses?', 'Only if you need them. Nova compares what you already know with each competency, and finished courses are never charged again.'),
       ('What if I don’t pass first time?', 'One retake of each assessment is included. After that, wait 14 days and retake for 40 Credits. You get written feedback either way.'),
       ('Can my employer pay?', 'Yes. The assessment fee can be sponsored by an employer or institution. Choose sponsorship at checkout.'),
       ('Is this the same as finishing the Data Analyst path?', 'No. The path builds the skills. This certification is assessed separately against a published standard.'),
       ('How long is it valid?', 'Three years. Renew with a short review of recent work.')]
JS = r'''  constructor(props) {
    super(props);
    var e = (props && props.elig) || '';
    var A = { meets: ['y', 'cred', 'yr'], needs: ['y', 'eq', 'yr'], not: ['y', 'none', 'some'] }[e] || ['', '', ''];
    this.state = { tab: 'Overview', faq: 0, saved: false, quiz: false, q1: A[0], q2: A[1], q3: A[2], res: !!(e === 'meets' || e === 'needs' || e === 'not') };
    var self = this;
    this.secs = {};
    this.mk = function (k) { return function (el) { self.secs[k] = el; }; };
    this.R = {};
    ['Overview', 'Who it’s for', 'Competencies', 'Requirements', 'Assessment', 'Credential', 'Issuer', 'Cost', 'FAQ'].forEach(function (k) { self.R[k] = self.mk(k); });
    this.F = FAQ_;
  }
  renderVals() {
    var self = this, S = this.state, e = this.props.elig || '';
    var names = ['Overview', 'Who it’s for', 'Competencies', 'Requirements', 'Assessment', 'Credential', 'Issuer', 'Cost', 'FAQ'];
    var Q = [['q1', 'Are you 18 or older?', [['y', 'Yes'], ['n', 'No']]], ['q2', 'Have you done Data Foundations?', [['cred', 'Yes, on Credalio'], ['eq', 'An equivalent qualification'], ['none', 'Not yet']]],
      ['q3', 'Experience with spreadsheets or reports?', [['none', 'None yet'], ['some', 'Under a year'], ['yr', 'A year or more']]]];
    var all = S.q1 && S.q2 && S.q3;
    var kind = !S.res ? '' : (S.q1 === 'n' || S.q2 === 'none' ? 'not' : (S.q2 === 'eq' ? 'needs' : 'meets'));
    var exp = { none: 'none yet', some: 'under a year', yr: 'a year or more' }[S.q3] || '';
    var it = function (t, s, k) { return { t: t, s: s, k: k, m: k === 'ok' ? '✓' : (k === 'warn' ? '!' : '×') }; };
    var RES = {
      meets: ['green', 'Meets the requirements', 'You can register for this certification', [it('Age', '18 or older', 'ok'), it('Prerequisite', 'Data Foundations completed on Credalio', 'ok'), it('Experience', 'Recommended only · you have ' + exp, 'ok')], 'Next, choose how to access the preparation learning and pay the assessment fee.', 'Continue to access options', 'Chk-001.dc.html', 'c5-rok'],
      needs: ['amber', 'Evidence needed', 'Add proof of your equivalent qualification', [it('Age', '18 or older', 'ok'), it('Prerequisite', 'Equivalent claimed · proof needed', 'warn'), it('Experience', 'Recommended only', 'ok')], 'An assessor checks your evidence against the issuer’s rules, usually within 3 working days.', 'Upload evidence', '#', 'c5-am'],
      not: ['amber', 'Not yet eligible', 'One mandatory requirement isn’t met yet', [it('Age', S.q1 === 'n' ? 'You need to be 18 or older' : '18 or older', S.q1 === 'n' ? 'no' : 'ok'), it('Prerequisite', S.q2 === 'none' ? 'Data Foundations, or an equivalent, is needed' : 'Met', S.q2 === 'none' ? 'no' : 'ok'), it('Experience', 'Recommended only', 'ok')], 'Start with Data Foundations (12 hrs). It counts toward the preparation learning too.', 'Start Data Foundations', 'CourseDetail.dc.html', 'c5-am']
    };
    var r = RES[kind];
    var enrolled = e === 'enrolled', done = e === 'done';
    var RQ = REQS_;
    var reqs = RQ.map(function (t, i) {
      var st = done || (enrolled && i < 2) ? ['Complete', 'green', '✓', 'c5-dn'] : (enrolled && i === 2 ? ['In progress · due 4 Dec', 'blue', '3', 'c5-cur'] : ['Not started', 'line', String(i + 1), '']);
      return { t: t, s: st[0], tag: st[1], mark: st[2], cls: st[3] };
    });
    var BAN = { enrolled: ['cb', 'Enrolled · 2 of 6 requirements complete', 'Next: submit the practical case study by 4 Dec'], done: ['ok', 'Certified · issued 12 Oct 2026', 'Credential 7F2-91 · valid until 12 Oct 2029'] }[e];
    return {
      tabs: names.map(function (n) { var on = S.tab === n; return { label: n, on: on ? 'true' : 'false', cls: on ? 'dt-tab-on' : '', go: function () { self.setState({ tab: n }); var el = self.secs[n]; if (el && el.scrollIntoView) el.scrollIntoView({ behavior: 'smooth', block: 'start' }); } }; }),
      refOverview: this.R.Overview, refWho: this.R['Who it’s for'], refComp: this.R.Competencies, refReq: this.R.Requirements, refEarn: this.R.Assessment, refCredential: this.R.Credential, refIssuer: this.R.Issuer, refPrice: this.R.Cost, refFaq: this.R.FAQ,
      faqs: this.F.map(function (f, i) { var open = S.faq === i; return { q: f[0], a: f[1], open: open, exp: open ? 'true' : 'false', cls: open ? 'dt-fq-open' : '', toggle: function () { self.setState({ faq: open ? -1 : i }); } }; }),
      saveOn: S.saved ? 'true' : 'false', saveCls: S.saved ? 'on' : '', saveLabel: S.saved ? 'Saved' : 'Save', toggleSave: function () { self.setState({ saved: !S.saved }); },
      hasBan: !!BAN, banCls: BAN ? 'c5-ban-' + BAN[0] : '', banT: BAN ? BAN[1] : '', banD: BAN ? BAN[2] : '',
      isGuest: !enrolled && !done && !S.res, quizOpen: S.quiz && !S.res, quizClosed: !S.quiz,
      openQuiz: function () { self.setState({ quiz: true, res: false }); },
      qs: Q.map(function (q) { return { t: q[1], opts: q[2].map(function (o) { var on = S[q[0]] === o[0]; return { label: o[1], on: on ? 'true' : 'false', cls: on ? 'on' : '', pick: function () { var n = {}; n[q[0]] = o[0]; self.setState(n); } }; }) }; }),
      seeDis: all ? '' : 'cd-dis', seeResult: function () { if (all) self.setState({ res: true }); },
      hasRes: !!r && !enrolled && !done, resTag: r ? r[0] : '', resChip: r ? r[1] : '', resT: r ? r[2] : '', resItems: r ? r[3] : [], resNote: r ? r[4] : '', resCta: r ? r[5] : '', resHref: r ? r[6] : '#', resCls: r ? r[7] : '',
      canRedo: !e, redo: function () { self.setState({ res: false, quiz: true }); },
      isEnrolled: enrolled, isDone: done, sideCls: (S.quiz || S.res || enrolled || done) ? 'dt-side-show' : '',
      showProg: enrolled || done, progLabel: done ? 'All 6 complete' : '2 of 6 complete', reqs: reqs,
      barSub: enrolled ? '2 of 6 complete' : (done ? 'Certified' : 'Assessment fee'), barCta: enrolled ? 'Continue' : (done ? 'View credential' : (r ? r[5] : 'Check my eligibility')),
      barGo: function () { if (!enrolled && !done && !r) self.setState({ quiz: true }); }
    };
  }
}
'''.replace('FAQ_', json.dumps(FAQ, ensure_ascii=False)).replace('REQS_', json.dumps(REQS, ensure_ascii=False))
i = s.index('  constructor(props) {'); j = s.index('</script>', i)
s = s[:i] + JS + s[j:]
rep('"$preview":', '"elig":{"editor":"enum","options":["","meets","needs","not","enrolled","done"],"default":""},"$preview":')

# ---------------------------------------------------------------- CSS
need = [l.strip() for l in kit.KIT_CSS.split('\n') if re.match(r'\.(ds-tag\.(green|amber)|nv-av|dlp-c)[.:{,\s]', l.strip())]
DLP = '' if '.dlp-c{' in s else '\n'.join(re.findall(r'(?:^|\n)(\.dlp-c[^{]*\{[^}]*\})', open(os.path.join(D, 'Courses.dc.html')).read())) + '\n' + '\n'.join(re.findall(r'@keyframes dlp\w+\{(?:[^{}]*\{[^}]*\})*\}', open(os.path.join(D, 'Courses.dc.html')).read()))
CSS = '\n'.join(need) + '\n' + DLP + '\n.nova-card{background:#FFFFFF url(' + kit.NOVA_BG + r''') center / cover no-repeat}
.c5-dot{width:8px;height:8px;border-radius:50%;background:#C8961E;font-style:normal}
.c5-acts{display:flex;flex-wrap:wrap;gap:10px;margin-top:6px}
.c5-acts .ds-ghost{height:40px;padding:0 16px;font-size:14px}
.c5-acts .ds-ghost.on{background:#EAF0FF;border-color:#1652F0;color:#0E3BB8}
.c5-ban{display:flex;align-items:flex-start;gap:12px;margin-top:10px;padding:14px 16px;border-radius:16px;font-size:14px;line-height:1.45}
.c5-ban > span{display:flex;flex-direction:column;gap:2px}
.c5-ban b{font-weight:600}
.c5-ban span span{color:#3A4566}
.c5-bd{width:10px;height:10px;border-radius:50%;margin-top:5px;flex-shrink:0;font-style:normal;background:currentColor}
.c5-ban-ok{background:#E7F5EE;color:#0F6B45}
.c5-ban-cb{background:#EAF0FF;color:#0E3BB8}
.c5-k{font-size:12px;font-weight:500;color:#8A93AD}
.c5-sm{font-size:14px;color:#5B6582}
.c5-sh{display:flex;align-items:baseline;justify-content:space-between;gap:16px;flex-wrap:wrap}
.c5-p{margin:0;max-width:720px;font-size:16px;line-height:1.65;color:#3A4566}
.c5-pf{font-size:14px;color:#5B6582;margin-top:-6px}
.c5-fine{margin:0;font-size:13px;line-height:1.5;color:#8A93AD}
.c5-who{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));border:1.5px solid #E6EAF3;border-radius:20px;overflow:hidden}
.c5-who > div{display:flex;flex-direction:column;gap:6px;padding:18px 20px}
.c5-who > div + div{border-left:1px solid #EEF1F7}
.c5-who > div > span:last-child{font-size:14.5px;line-height:1.5;color:#0B1433}
.ce-cp .c5-std{display:flex;flex-direction:column;gap:2px;margin-top:8px;padding-top:10px;border-top:1px dashed #E6EAF3;font-size:13px;line-height:1.45;color:#0B1433}
.ce-cp .c5-std em{font-style:normal;font-size:11.5px;font-weight:500;color:#8A93AD}
.ce-cp .c5-how{align-self:flex-start;margin-top:8px}
.c5-req{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.c5-rq{display:flex;flex-direction:column;align-items:flex-start;gap:6px;padding:18px 20px;border-radius:18px;border:1.5px solid #E6EAF3}
.c5-rq b{font-size:15.5px;font-weight:600;color:#0B1433}
.c5-rq > span:last-child{font-size:13.5px;line-height:1.5;color:#5B6582}
.c5-must{background:#0B1433;color:#FFFFFF}
.c5-rdy{display:flex;align-items:center;gap:16px;padding:18px 20px;border-radius:20px;border:1.5px solid #DCE5FB}
.c5-rdy p{margin:0;flex:1;font-size:14.5px;line-height:1.5;color:#3A4566}
.c5-rdy p b{font-weight:600;color:#0B1433}
.c5-rdy .ds-ghost{flex-shrink:0}
.c5-ax{display:flex;flex-wrap:wrap;gap:6px 16px;margin-top:8px;font-size:12.5px;color:#0E3BB8}
.c5-ax span{display:inline-flex;align-items:center;gap:6px}
.c5-ax span + span::before{content:'';width:4px;height:4px;border-radius:50%;background:#9DB8F7;margin-right:10px}
.c5-rl{margin:0;padding:0;list-style:none;border:1.5px solid #E6EAF3;border-radius:20px;overflow:hidden}
.c5-rl li{display:flex;align-items:center;gap:14px;padding:14px 20px}
.c5-rl li + li{border-top:1px solid #EEF1F7}
.c5-rl b{flex:1;font-size:15px;font-weight:500;color:#0B1433}
.c5-rn{width:28px;height:28px;border-radius:50%;border:1.5px solid #CBD3E6;color:#5B6582;font-size:13px;font-weight:600;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.c5-dn .c5-rn{background:#0F6B45;border-color:#0F6B45;color:#FFFFFF}
.c5-cur .c5-rn{border-color:#1652F0;color:#1652F0;background:#EAF0FF}
.c5-iss{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.c5-ip{display:flex;gap:14px;padding:18px 20px;border-radius:18px;border:1.5px solid #E6EAF3}
.c5-ip > div{display:flex;flex-direction:column;gap:3px;min-width:0}
.c5-ip b{font-size:16px;font-weight:600;color:#0B1433}
.c5-ip > div > span:last-child{font-size:13.5px;line-height:1.5;color:#5B6582}
.c5-av{width:46px;height:46px;border-radius:14px;background:#EAF0FF;color:#0E3BB8;font-size:14px;font-weight:600;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.c5-mean{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.c5-mean > div{display:flex;flex-direction:column;gap:10px;padding:18px 20px;border-radius:18px;background:#F5F8FF}
.c5-mean ul{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px}
.c5-mean li{display:flex;gap:10px;font-size:14px;line-height:1.5;color:#0B1433}
.c5-ok,.c5-no{width:20px;height:20px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px}
.c5-ok{background:#0F6B45;color:#FFFFFF}
.c5-no{background:#E6EAF3;color:#5B6582}
.c5-cost{display:grid;grid-template-columns:minmax(0,1fr) 32px minmax(0,1fr);align-items:stretch}
.c5-cc{display:flex;flex-direction:column;gap:8px;padding:20px 22px;border-radius:20px;border:1.5px solid #E6EAF3}
.c5-cc > span:last-child{font-size:14px;line-height:1.55;color:#5B6582}
.c5-fee{border-color:#1652F0;background:linear-gradient(180deg,#F5F8FF,#FFFFFF)}
.c5-pv{display:flex;align-items:center;gap:8px}
.c5-pv b{font-size:24px;font-weight:600;letter-spacing:-.5px;color:#0B1433}
.c5-pv .dlp-c,.c5-pv .cr-c{width:24px;height:24px;font-size:12px}
.c5-plus{display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:500;color:#8A93AD}
.c5-prep{display:flex;align-items:center;gap:8px;margin-top:-6px;font-size:13px;line-height:1.4;color:#5B6582}
.c5-cn{margin:0;font-size:13.5px;line-height:1.5;color:#5B6582}
.c5-qz{display:flex;flex-direction:column;gap:14px;padding:16px;border-radius:16px;background:#F7F9FD}
.c5-q{display:flex;flex-direction:column;gap:8px}
.c5-q b{font-size:14px;font-weight:600;color:#0B1433}
.c5-qo{display:flex;flex-wrap:wrap;gap:6px}
.c5-o{min-height:36px;padding:0 12px;border-radius:12px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:inherit;font-size:13px;font-weight:500;color:#0B1433;cursor:pointer}
.c5-o:hover{border-color:#9DB8F7}
.c5-o.on{background:#EAF0FF;border-color:#1652F0;color:#0E3BB8}
.ds-btn.cd-dis{background:#E6EAF3;color:#8A93AD;box-shadow:none;pointer-events:none}
.ds-btn.cd-dis .ob-arrow{background:#FFFFFF;color:#8A93AD}
.c5-res{display:flex;flex-direction:column;align-items:flex-start;gap:10px;padding:16px;border-radius:16px}
.c5-res > b{font-size:16px;font-weight:600;color:#0B1433;line-height:1.3}
.c5-res ul{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:8px;align-self:stretch}
.c5-res li{display:flex;gap:10px;font-size:13.5px;line-height:1.45;color:#0B1433}
.c5-res li em{display:block;font-style:normal;font-size:12px;color:#8A93AD}
.c5-res p{margin:0;font-size:13px;line-height:1.5;color:#3A4566}
.c5-res p em{font-style:normal;font-weight:600;color:#0B1433;margin-right:4px}
.c5-res.c5-rok{background:#E7F5EE}
.c5-res.c5-am{background:#FFF8EB}
.c5-res.c5-cb{background:#EAF0FF}
.c5-m{width:20px;height:20px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:11px;font-weight:700;color:#FFFFFF}
.c5-m.ok{background:#0F6B45}
.c5-m.warn{background:#B7791F}
.c5-m.no{background:#8A93AD}
.c5-redo{align-self:center;font-size:14px}
@media (max-width: 760px){.ce-comp{grid-template-columns:minmax(0,1fr) !important}.ce-cp .c5-std{display:flex}.ce-cp .c5-std em{display:block}.ce-cp .c5-how{display:inline-flex}.ce-cp .c5-std{margin-top:4px}}
.c5-dl{margin:0;display:flex;flex-direction:column;gap:6px;align-self:stretch}
.c5-dl div{display:flex;justify-content:space-between;gap:12px;font-size:13.5px}
.c5-dl dt{color:#5B6582}
.c5-dl dd{margin:0;font-weight:600;color:#0B1433}
.cd-pb{display:block;align-self:stretch;height:6px;border-radius:3px;background:rgba(22,82,240,.15);overflow:hidden}
.cd-pb i{display:block;height:100%;border-radius:3px;background:#1652F0}
.dt-tabs{overflow-x:auto;scrollbar-width:none}
.dt-tabs::-webkit-scrollbar{display:none}
@media (max-width: 1180px){.c5-who{grid-template-columns:minmax(0,1fr)}.c5-who > div + div{border-left:0;border-top:1px solid #EEF1F7}}
@media (max-width: 760px){
.c5-p{font-size:15px}
.c5-req,.c5-iss,.c5-mean{grid-template-columns:minmax(0,1fr);gap:10px}
.c5-rdy{display:grid;grid-template-columns:36px minmax(0,1fr);gap:12px;align-items:start}
.c5-rdy .ds-ghost{grid-column:1 / -1}
.c5-cost{grid-template-columns:minmax(0,1fr);gap:8px}
.c5-plus{height:20px}
.c5-rl li{flex-wrap:wrap;padding:12px 16px;gap:8px 12px}
.c5-rl b{flex:1 1 calc(100% - 44px)}
.c5-rl .ds-tag{margin-left:40px}
.dt-tabs{-webkit-mask-image:linear-gradient(90deg,#000 88%,transparent);mask-image:linear-gradient(90deg,#000 88%,transparent)}
}
'''
i = s.find('</style>'); s = s[:i] + CSS + s[i:]
open(P, 'w').write(s); print('patched CertDetail')
