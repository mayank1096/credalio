"""Landing batch 6 (client review, Learning program detail). Patches the live ProgramDetail.dc.html in place.
Adds: at a glance, about, who it's for, roles and sectors, entry requirements, outcomes; "Your week" with days,
times, time zone and format; upcoming cohorts with places left (pick one); projects and assessments; community and
support; completion criteria; how applying works + the DLP or Credits routes; reviews; provider profile.
Application states via prop `app` = '' | draft | submitted | review | accepted | waitlisted | payment | full | closed.
Usage: python3 pg6.py <canvas3/project>"""
import re, sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import kit
from kit import tip, ck, nova_av, ARROW
D = sys.argv[1]; P = os.path.join(D, 'ProgramDetail.dc.html'); s = open(P).read()
assert 'p6-' not in s, 'already patched'
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:90], s.count(a)); s = s.replace(a, b)
def svg(d, w=18, sw=2):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (w, w, sw, d)
HEART = svg('<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"></path>', 17)
SHARE = svg('<path d="M12 15V4M8 8l4-4 4 4"></path><path d="M5 13v5a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-5"></path>', 17)
I = {'live': '<rect x="3" y="5" width="18" height="12" rx="2.5"></rect><path d="M8 21h8M12 17v4"></path>', 'self': '<path d="M5 4h10l4 4v12H5z"></path><path d="M9 12h6M9 16h6"></path>',
     'proj': '<rect x="3" y="7" width="18" height="13" rx="2.5"></rect><path d="M8 7V5h8v2"></path>', 'peer': '<circle cx="9" cy="8" r="3"></circle><circle cx="17" cy="9" r="2.5"></circle><path d="M3.5 19c.6-3 2.8-4.6 5.5-4.6s4.9 1.6 5.5 4.6M15 14.6c2.3.2 4 1.6 4.5 4.4"></path>',
     'chat': '<path d="M5 5h14v10H9l-4 4z"></path>', 'mentor': '<circle cx="12" cy="8" r="3.5"></circle><path d="M5 20c.8-3.6 3.6-5.5 7-5.5s6.2 1.9 7 5.5"></path>', 'alum': '<path d="M3 9l9-5 9 5-9 5z"></path><path d="M7 11.5V16c0 1.5 2.2 3 5 3s5-1.5 5-3v-4.5"></path>'}
def ico(k, w=18): return svg(I[k], w, 1.9)

# ---------------------------------------------------------------- hero
rep('<div class="dt-tags"><span class="ds-tag green lg">Places available</span><span class="ds-tag line lg">Accelerator</span></div>',
    '<div class="dt-tags"><span class="ds-tag blue lg"><i class="p6-dot"></i>Gold Validated</span><span class="ds-tag line lg">CEI 94%s</span><span class="ds-tag line lg">Accelerator</span><span class="p6-rt"><b>★ 4.9</b> (340)</span></div>' % tip(
        'Credalio Excellence Index: how well this program is built, scored by independent validators out of 100.'))
rep('<span class="dt-fact"><b>About 8 hrs a week</b></span>', '<span class="dt-fact"><b>6 hrs a week</b></span><span class="dt-fact"><b>Live online</b></span><span class="dt-fact"><b>Intermediate</b></span>')
rep('<a class="ds-link dt-askm" href="#">', '<div class="p6-acts"><button class="ds-ghost sm {{saveCls}}" type="button" aria-pressed="{{saveOn}}" onClick="{{toggleSave}}">%s<span>{{saveLabel}}</span></button>'
    '<button class="ds-ghost sm" type="button">%s<span>Share</span></button></div>\n<sc-if value="{{hasBan}}" hint-placeholder-val="{{ false }}"><div class="p6-ban {{banCls}}" role="status"><i class="p6-bd" aria-hidden="true"></i><span><b>{{banT}}</b><span>{{banD}}</span></span></div></sc-if>\n<a class="ds-link dt-askm" href="#">' % (HEART, SHARE))

# ---------------------------------------------------------------- overview block (before curriculum)
GL = [('Format', 'Live online'), ('Live sessions', 'Tue 18:00–19:30 GMT'), ('Mentor hours', 'Thu 12:30–13:30 GMT'), ('Cohort size', 'Up to 40'), ('Language', 'English'), ('Assessment', '3 projects + capstone')]
WHO = [('Career switchers', 'Moving into a data role from another field.'), ('Working professionals', 'Using data and AI in the job you already have.'), ('Recent graduates', 'Wanting structured, practical work for a portfolio.')]
ROLES = ['Junior Data Analyst', 'Business Analyst', 'Reporting Analyst', 'AI Operations Associate']
SECT = ['Retail', 'Financial services', 'Healthcare', 'Public sector', 'Logistics']
OUT = [('Prepare and query business data with SQL', 'Weeks 1–6 assignments'), ('Build dashboards decision-makers trust', 'Sales dashboard project'),
       ('Use AI tools responsibly to speed up analysis', 'Customer insights project'), ('Present a data-backed recommendation', 'Capstone presentation')]
OV = '''<section class="dt-sec" ref="{{refOverview}}" aria-labelledby="p6-ab">
<dl class="p6-gl">%s</dl>
<h2 id="p6-ab" class="dt-h2">About this program</h2>
<p class="p6-p">Many people can read a report but can’t yet build one or question it. This 12-week accelerator closes that gap. Each week pairs a live session with practice on real business data, so ideas are used within days. You work in small peer groups, get written feedback from instructors, and finish with a capstone you present to the cohort.</p>
</section>

<section class="dt-sec" ref="{{refWho}}" aria-labelledby="p6-wh">
<h2 id="p6-wh" class="dt-h2">Who it’s for</h2>
<div class="p6-g3">%s</div>
<p class="p6-fine">Not designed for complete beginners. If spreadsheets are new to you, start with Data Foundations.</p>
<div class="p6-rs"><div><span class="p6-k">Relevant roles</span><div class="p6-chips">%s</div></div><div><span class="p6-k">Sectors</span><div class="p6-chips">%s</div></div></div>
<p class="p6-fine">The program builds skills used in these roles and sectors. It doesn’t guarantee a job in them.</p>
</section>

<section class="dt-sec" ref="{{refReq}}" aria-labelledby="p6-rq">
<h2 id="p6-rq" class="dt-h2">Before you join</h2>
<div class="p6-req">
<div><span class="ds-tag p6-must">Required</span><b>Basic spreadsheet skills, a computer and time for the live sessions</b></div>
<div><span class="ds-tag line">Recommended</span><b>Some familiarity with business reporting or basic statistics</b></div>
<div><span class="ds-tag line">Admission</span><b>A short application and a 15-minute readiness check</b></div>
</div>
<div class="p6-rdy nova-card">%s<p><b>Not sure you’re ready?</b> Nova, your AI Coach, checks your answers against the entry requirements and suggests what to prepare. Admission follows the program’s published rules.</p><a class="ds-ghost sm" href="#">Check my readiness</a></div>
</section>

<section class="dt-sec" aria-labelledby="p6-oc">
<h2 id="p6-oc" class="dt-h2">What you’ll be able to do</h2>
<ul class="p6-out">%s</ul>
</section>

''' % (''.join('<div><dt>%s</dt><dd>%s</dd></div>' % g for g in GL),
       ''.join('<div class="p6-c"><span class="p6-ck">%s</span><b>%s</b><span>%s</span></div>' % (ck(12), t, d) for t, d in WHO),
       ''.join('<span class="ds-tag line lg">%s</span>' % r for r in ROLES), ''.join('<span class="ds-tag line lg">%s</span>' % r for r in SECT), nova_av(),
       ''.join('<li><span class="p6-ck">%s</span><span><b>%s</b><em>Assessed in: %s</em></span></li>' % (ck(11), t, m) for t, m in OUT))
rep('<section class="dt-sec" ref="{{refCurriculum}}"', OV + '<section class="dt-sec" ref="{{refCurriculum}}"')

# ---------------------------------------------------------------- your week: times, time zone, format
rep('<div class="pd2-day pd2-day-k"><span class="pd2-dn">TUESDAY</span><span class="pd2-dt">Live session</span><span class="pd2-dd">90 minutes</span></div>',
    '<div class="pd2-day pd2-day-k"><span class="pd2-dn">TUESDAY</span><span class="pd2-dt">Live session</span><span class="pd2-dd">18:00–19:30 GMT · online</span></div>')
rep('<div class="pd2-day"><span class="pd2-dn">THURSDAY</span><span class="pd2-dt">Mentor hours</span><span class="pd2-dd">60 minutes</span></div>',
    '<div class="pd2-day"><span class="pd2-dn">THURSDAY</span><span class="pd2-dt">Mentor hours</span><span class="pd2-dd">12:30–13:30 GMT · drop in</span></div>')
rep('<div class="pd2-day"><span class="pd2-dn">YOUR TIME</span><span class="pd2-dt">Self-paced lessons</span><span class="pd2-dd">About 4 hours</span></div>',
    '<div class="pd2-day"><span class="pd2-dn">YOUR TIME</span><span class="pd2-dt">Self-paced lessons</span><span class="pd2-dd">About 3 hours</span></div>')
rep('<div class="pd2-day"><span class="pd2-dn">SATURDAY</span><span class="pd2-dt">Project clinic</span><span class="pd2-dd">Optional</span></div>',
    '<div class="pd2-day"><span class="pd2-dn">SATURDAY</span><span class="pd2-dt">Project clinic</span><span class="pd2-dd">10:00–11:00 GMT · optional</span></div>')
rep('<h2 id="pr-w" class="dt-h2">Your week', '<div class="p6-sh"><h2 id="pr-w" class="dt-h2">Your week')
s = re.sub(r'(<h2 id="pr-w" class="dt-h2">Your week.*?</h2>)', r'\1<span class="p6-sm">About 6 hours · times in GMT (UTC+0)</span></div>', s, count=1, flags=re.S)
rep('</div>\n</section>\n\n<section class="dt-sec" ref="{{refPeople}}"',
    '</div>\n<p class="p6-fine">All live sessions are online, on video. Attend at least 80% of them; recordings stay up for 14 days. Signed in, times show in your own time zone.</p>\n</section>\n\n<section class="dt-sec" ref="{{refPeople}}"')

# ---------------------------------------------------------------- cohorts + projects + support + completion (after "Your week")
PROJ = [('Weekly assignments', 'Notebook or short write-up', 'Individual', 'Instructor feedback', 'Yes, 80% submitted'), ('Sales dashboard', 'Interactive dashboard', 'Peer group of 5', 'Rubric, instructor-marked', 'Yes, pass'),
        ('Customer insights', 'Analysis + AI workflow', 'Individual', 'Rubric, instructor-marked', 'Yes, pass'), ('Capstone', 'Recommendation + 10-min presentation', 'Individual', 'Panel of 2 instructors', 'Yes, pass')]
SUP = [('mentor', 'Mentor hours', 'A weekly drop-in with Tom’s mentor team.'), ('peer', 'Peer group of five', 'Your study group for the whole program.'),
       ('chat', 'Cohort space', 'Questions, notes and announcements. Opens when you enrol.'), ('alum', 'Alumni network', 'Stay in touch with past cohorts after you finish.')]
CRIT = ['Attend at least 80% of live sessions', 'Submit 80% of weekly assignments', 'Pass the two projects and the capstone']
NEW2 = '''<section class="dt-sec" ref="{{refCohorts}}" aria-labelledby="p6-co">
<div class="p6-sh"><h2 id="p6-co" class="dt-h2">Upcoming cohorts</h2><span class="p6-sm">Pick the one that fits your diary</span></div>
<div class="p6-cos" role="radiogroup" aria-label="Cohort"><sc-for list="{{cohorts}}" as="c" hint-placeholder-count="3"><button class="ds-opt p6-co {{c.cls}}" type="button" role="radio" aria-checked="{{c.on}}" onClick="{{c.pick}}">
<span class="pd2-cal" aria-hidden="true"><b>{{c.d}}</b><span>{{c.m}}</span></span><span class="p6-cot"><b>{{c.t}}</b><em>{{c.sub}}</em></span><span class="ds-tag {{c.tag}}">{{c.st}}</span><span class="ds-opt-ck">%s</span></button></sc-for></div>
<p class="p6-fine">Places are shown when they can be counted reliably. Each cohort has its own instructors and dates.</p>
</section>

<section class="dt-sec" aria-labelledby="p6-pj">
<h2 id="p6-pj" class="dt-h2">Projects and assessments</h2>
<div class="p6-tw"><table class="p6-t"><thead><tr><th scope="col">What</th><th scope="col">You hand in</th><th scope="col">Format</th><th scope="col">How it’s marked</th><th scope="col">Counts toward completion</th></tr></thead><tbody>%s</tbody></table></div>
</section>

<section class="dt-sec" aria-labelledby="p6-su">
<h2 id="p6-su" class="dt-h2">Support and community</h2>
<div class="p6-g4">%s</div>
</section>

<section class="dt-sec" aria-labelledby="p6-cp">
<h2 id="p6-cp" class="dt-h2">What you need to complete it</h2>
<div class="p6-cmp"><ul>%s</ul><div><b>Program certificate</b><span>Saved to your Digital Backpack. It isn’t a professional certification: the Professional Certificate in Data Analysis is assessed separately, with its own 150 Credits fee.</span><a class="ds-link" href="CertDetail.dc.html">See the certification →</a></div></div>
</section>

''' % (ck(12), ''.join('<tr><th scope="row">%s</th><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % r for r in PROJ),
       ''.join('<div class="p6-c"><span class="p6-ic">%s</span><b>%s</b><span>%s</span></div>' % (ico(k), t, d) for k, t, d in SUP),
       ''.join('<li><span class="p6-ck">%s</span>%s</li>' % (ck(11), c) for c in CRIT))
rep('<section class="dt-sec" ref="{{refPeople}}"', NEW2 + '<section class="dt-sec" ref="{{refPeople}}"')

# ---------------------------------------------------------------- applying + paying + reviews + provider (before FAQ)
STEPS = [('Apply', 'A short form about your goal and experience. About 10 minutes.'), ('Readiness check', '15 minutes, online. It shows where you’d start, not a pass or fail.'),
         ('Decision', 'Within 5 working days. Full cohorts go to the waitlist.'), ('Pay and enrol', 'Your place is held for 7 days while you pay.')]
REV = [('“The live sessions were the difference. Asking a question and seeing someone work through it on real data taught me more than any video.”', 'Ngozi A.', 'September 2026 cohort'),
       ('“My capstone became the case study I talked through in my interview. I start as a reporting analyst next month.”', 'Marcus T.', 'April 2026 cohort')]
NEW3 = '''<section class="dt-sec" ref="{{refApply}}" aria-labelledby="p6-ap">
<h2 id="p6-ap" class="dt-h2">How applying works</h2>
<ol class="p6-steps">%s</ol>
<div class="p6-pay">
<div class="p6-pc"><span class="p6-k">Pay with Credits</span><span class="p6-pv"><i class="cr-c" aria-hidden="true">C</i><b>1,200 Credits</b></span><span>Or 3 monthly payments of 400. Buys your place in the selected cohort and its recordings.</span></div>
<div class="p6-pc"><span class="p6-k">Use your plan</span><span class="p6-pv"><span class="dlp-c" aria-hidden="true"></span><b>6,000 DLP</b></span><span>On Pro, the self-paced parts and live sessions use DLP from your plan over the 12 weeks.</span></div>
</div>
<p class="p6-fine">DLP and Credits are separate routes, not one price converted. Credits buy this cohort only, not future cohorts. Up to 10 places per cohort are half-price scholarships.</p>
</section>

<section class="dt-sec" aria-labelledby="p6-rv">
<h2 id="p6-rv" class="dt-h2">What past learners say</h2>
<div class="p6-revs"><div class="p6-score"><b>4.9</b><span class="p6-stars" aria-label="4.9 out of 5">★★★★★</span><span>340 reviews from earlier cohorts</span><em>Instructors and schedules can differ for your cohort.</em></div>%s</div>
</section>

<section class="dt-sec" aria-labelledby="p6-pv2">
<h2 id="p6-pv2" class="dt-h2">Who runs it</h2>
<div class="p6-prov"><span class="p6-av">NU</span><div><span class="p6-k">Provider · verified institution</span><b>Northgate University</b><span>Runs this program and issues its certificate. 6 learning experiences on Credalio, including the Professional Certificate in Data Analysis.</span><a class="ds-link" href="#">View institution profile →</a></div></div>
</section>

''' % (''.join('<li><span class="p6-sn">%d</span><b>%s</b><span>%s</span></li>' % (i + 1, t, d) for i, (t, d) in enumerate(STEPS)),
       ''.join('<figure class="p6-rev"><blockquote>%s</blockquote><figcaption><b>%s</b> · %s</figcaption></figure>' % r for r in REV))
rep('<section class="dt-sec" ref="{{refFaq}}"', NEW3 + '<section class="dt-sec" ref="{{refFaq}}"')

# ---------------------------------------------------------------- side card: selected cohort + application state
rep('<div class="pd2-when"><span class="pd2-cal" aria-hidden="true"><b>18</b><span>JAN</span></span><div><b>Cohort starts 18 January</b><span>Applications close 8 January</span></div></div>',
    '<div class="pd2-when"><span class="pd2-cal" aria-hidden="true"><b>{{selD}}</b><span>{{selM}}</span></span><div><b>{{selT}}</b><span>{{selSub}}</span></div></div>')
rep('<div class="dt-amt"><i class="cr-c lg" aria-hidden="true">C</i><b>1,200</b><span>Credits, or 3 × 400</span></div>',
    '<div class="dt-amt"><i class="cr-c lg" aria-hidden="true">C</i><b>1,200</b><span>Credits, or 3 × 400</span></div>\n<span class="p6-alt"><span class="dlp-c" aria-hidden="true"></span>Or 6,000 DLP with Pro</span>\n'
    '<sc-if value="{{hasSt}}" hint-placeholder-val="{{ false }}"><div class="p6-st {{stCls}}" role="status"><span class="ds-tag {{stTag}}">{{stChip}}</span><b>{{stT}}</b><span>{{stD}}</span><sc-if value="{{hasSteps}}" hint-placeholder-val="{{ false }}"><span class="cd-pb" aria-hidden="true"><i style="width: {{stPct}}"></i></span></sc-if></div>'
    '<a class="ds-btn dt-cta {{stDis}}" href="{{stHref}}"><span>{{stCta}}</span><span class="ob-arrow">%s</span></a><sc-if value="{{hasSecond}}" hint-placeholder-val="{{ false }}"><a class="ds-ghost sm" href="#">{{second}}</a></sc-if></sc-if>' % ARROW)
rep('<sc-if value="{{idle}}" hint-placeholder-val="{{ true }}">\n<button class="ds-btn dt-cta"', '<sc-if value="{{idleOpen}}" hint-placeholder-val="{{ true }}">\n<button class="ds-btn dt-cta"')

# ---------------------------------------------------------------- JS
COH = [('18', 'JAN', 'January 2027', '12 Jan – 6 Apr · Tue 18:00 GMT', 'Places available', 'green', 'Apply by 8 January · 9 places left'),
       ('12', 'APR', 'April 2027', '12 Apr – 5 Jul · Tue 18:00 GMT', 'Applications open', 'blue', 'Apply by 2 April · 40 places'),
       ('13', 'SEP', 'September 2027', '13 Sep – 6 Dec · Wed 12:30 GMT', 'Opens in June', 'line', 'Get notified when applications open')]
ST = {'draft': ['blue', 'Draft saved', 'Your application is half done', '2 of 4 sections complete · saved 14 Nov', 'Continue application', '#', '50%', '', 'cb'],
      'submitted': ['blue', 'Submitted', 'Application sent', 'Expect a decision by 21 Nov. We’ll email you.', 'View application', '#', '', 'Withdraw application', 'cb'],
      'review': ['line', 'Under review', 'An admissions tutor is reading it', 'Readiness check done. Decision due by 21 Nov.', 'View application', '#', '', '', 'gy'],
      'accepted': ['green', 'Accepted', 'You have a place in the January cohort', 'Pay by 22 Nov to confirm it. Your place is held for 7 days.', 'Accept and pay', 'Chk-001.dc.html', '', 'Decline the offer', 'ok'],
      'waitlisted': ['amber', 'Waitlisted', 'You’re 4th on the waitlist', 'We’ll email you if a place opens before 8 January. Or apply to the April cohort.', 'Apply to April instead', '#', '', 'Leave the waitlist', 'am'],
      'payment': ['amber', 'Payment pending', 'Your place is held until 22 Nov', 'First payment of 400 Credits due. Pay in full or in 3 parts.', 'Complete payment', 'Chk-001.dc.html', '', '', 'am'],
      'full': ['line', 'Cohort full', 'January is full', 'Join the waitlist, or apply to the April cohort, which has places.', 'Join the waitlist', '#', '', 'Apply to April instead', 'gy'],
      'closed': ['line', 'Applications closed', 'January applications closed on 8 January', 'The April cohort is open. Applications close 2 April.', 'Apply to April', '#', '', '', 'gy']}
BAN = {'draft': ['cb', 'Application draft saved', 'Finish it before 8 January'], 'submitted': ['cb', 'Application submitted', 'Decision by 21 November'],
       'review': ['gy', 'Application under review', 'Decision by 21 November'], 'accepted': ['ok', 'You’re accepted', 'Pay by 22 November to confirm your place'],
       'waitlisted': ['am', 'You’re on the waitlist', 'Position 4 for the January cohort'], 'payment': ['am', 'Payment pending', 'Your place is held until 22 November'],
       'full': ['gy', 'January cohort is full', 'The April cohort has places'], 'closed': ['gy', 'Applications closed for January', 'The April cohort is open']}
rep("this.state = { tab: 'Curriculum',", "this.state = { coh: 0, saved: false, tab: 'Overview',")
rep("this.R = { Curriculum: this.mk('Curriculum'), 'Your week': this.mk('Your week'), People: this.mk('People'), Questions: this.mk('Questions') };",
    "this.R = {}; ['Overview', 'Who it’s for', 'Requirements', 'Curriculum', 'Your week', 'Cohorts', 'People', 'Applying', 'FAQ'].forEach(function (k) { self.R[k] = self.mk(k); });")
rep("var names = ['Curriculum', 'Your week', 'People', 'Questions'];", "var names = ['Overview', 'Who it’s for', 'Requirements', 'Curriculum', 'Your week', 'Cohorts', 'People', 'Applying', 'FAQ'];\n    var A = this.props.app || '', COH = COH_, STX = ST_, BANX = BAN_, x = STX[A], c = COH[S.coh];")
rep("refCurriculum: this.R.Curriculum, refWeek: this.R['Your week'], refPeople: this.R.People, refFaq: this.R.Questions,",
    "refOverview: this.R.Overview, refWho: this.R['Who it’s for'], refReq: this.R.Requirements, refCurriculum: this.R.Curriculum, refWeek: this.R['Your week'], refCohorts: this.R.Cohorts, refPeople: this.R.People, refApply: this.R.Applying, refFaq: this.R.FAQ,\n"
    "      cohorts: COH.map(function (k, i) { var on = S.coh === i; return { d: k[0], m: k[1], t: k[2], sub: k[3], st: k[4], tag: k[5], on: on ? 'true' : 'false', cls: on ? 'on' : '', pick: function () { self.setState({ coh: i }); } }; }),\n"
    "      selD: c[0], selM: c[1], selT: c[2] + ' cohort', selSub: c[6],\n"
    "      hasSt: !!x, stCls: x ? 'p6-st-' + x[8] : '', stTag: x ? x[0] : '', stChip: x ? x[1] : '', stT: x ? x[2] : '', stD: x ? x[3] : '', stCta: x ? x[4] : '', stHref: x ? x[5] : '#', hasSteps: !!(x && x[6]), stPct: x && x[6] ? x[6] : '0%', hasSecond: !!(x && x[7]), second: x ? x[7] : '', stDis: '',\n"
    "      hasBan: !!BANX[A], banCls: BANX[A] ? 'p6-ban-' + BANX[A][0] : '', banT: BANX[A] ? BANX[A][1] : '', banD: BANX[A] ? BANX[A][2] : '',\n"
    "      idleOpen: !x && S.stage === 'idle', saveOn: S.saved ? 'true' : 'false', saveCls: S.saved ? 'on' : '', saveLabel: S.saved ? 'Saved' : 'Save', toggleSave: function () { self.setState({ saved: !S.saved }); },")
rep("sideCls: S.stage === 'idle' ? '' : 'dt-side-show',", "sideCls: S.stage === 'idle' && !x ? '' : 'dt-side-show',")
rep("barCta: 'Apply',", "barCta: x ? x[4] : 'Apply',")
rep("barCls: S.stage === 'idle' ? '' : 'dt-bar-off',", "barCls: S.stage === 'idle' && !x ? '' : 'dt-bar-off',")
s = s.replace('COH_', json.dumps(COH, ensure_ascii=False)).replace('ST_', json.dumps(ST, ensure_ascii=False)).replace('BAN_', json.dumps(BAN, ensure_ascii=False))
rep("this.F = [['Do I need a technical background?', 'No. You need to be comfortable with spreadsheets. Everything else is taught from the start.']",
    "this.F = [['Do I need a technical background?', 'No coding is needed, but you should be comfortable with spreadsheets. The readiness check tells you where you’d start.'], ['What time zone are the sessions in?', 'GMT (UTC+0). Signed in, every time shows in your own time zone. All sessions are recorded.'], ['What if the cohort is full?', 'Join the waitlist. If a place opens before the start date, we offer it in order. You can also apply to a later cohort.']")
rep('"$preview":', '"app":{"editor":"enum","options":["","draft","submitted","review","accepted","waitlisted","payment","full","closed"],"default":""},"$preview":')

# ---------------------------------------------------------------- CSS
need = [l.strip() for l in kit.KIT_CSS.split('\n') if re.match(r'\.(ds-tag\.(amber|green|blue|line|lg)|ds-opt|ds-ghost|nv-av)[.:{,\s-]', l.strip())]
C = open(os.path.join(D, 'Courses.dc.html')).read()
DLP = '' if '.dlp-c{' in s else '\n'.join(re.findall(r'(?:^|\n)(\.dlp-c[^{]*\{[^}]*\})', C[C.find('<style>'):C.find('</style>')])) + '\n' + '\n'.join(re.findall(r'@keyframes dlp\w+\{(?:[^{}]*\{[^}]*\})*\}', C))
CSS = '\n'.join(need) + '\n' + DLP + '\n.nova-card{background:#FFFFFF url(' + kit.NOVA_BG + r''') center / cover no-repeat}
.p6-dot{width:8px;height:8px;border-radius:50%;background:#C8961E;font-style:normal}
.p6-rt{font-size:14px;color:#5B6582;margin-left:4px}
.p6-rt b{font-weight:600;color:#0B1433}
.p6-acts{display:flex;flex-wrap:wrap;gap:10px;margin-top:6px}
.p6-acts .ds-ghost{height:40px;padding:0 16px;font-size:14px}
.p6-acts .ds-ghost.on{background:#EAF0FF;border-color:#1652F0;color:#0E3BB8}
.p6-ban{display:flex;align-items:flex-start;gap:12px;margin-top:10px;padding:14px 16px;border-radius:16px;font-size:14px;line-height:1.45}
.p6-ban > span{display:flex;flex-direction:column;gap:2px}
.p6-ban b{font-weight:600}
.p6-ban span span{color:#3A4566}
.p6-bd{width:10px;height:10px;border-radius:50%;margin-top:5px;flex-shrink:0;font-style:normal;background:currentColor}
.p6-ban-ok{background:#E7F5EE;color:#0F6B45}
.p6-ban-cb{background:#EAF0FF;color:#0E3BB8}
.p6-ban-am{background:#FFF4E0;color:#8A5A00}
.p6-ban-gy{background:#F2F4F9;color:#3A4566}
.p6-k{font-size:12px;font-weight:500;color:#8A93AD}
.p6-sm{font-size:14px;color:#5B6582}
.p6-sh{display:flex;align-items:baseline;justify-content:space-between;gap:16px;flex-wrap:wrap}
.p6-p{margin:0;max-width:720px;font-size:16px;line-height:1.65;color:#3A4566}
.p6-fine{margin:0;font-size:13px;line-height:1.5;color:#8A93AD}
.p6-gl{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));margin:0 0 8px;border:1.5px solid #E6EAF3;border-radius:20px;overflow:hidden}
.p6-gl div{padding:16px 20px;border-right:1px solid #EEF1F7;border-bottom:1px solid #EEF1F7}
.p6-gl div:nth-child(3n){border-right:0}
.p6-gl div:nth-last-child(-n+3){border-bottom:0}
.p6-gl dt{font-size:12px;font-weight:500;color:#8A93AD}
.p6-gl dd{margin:4px 0 0;font-size:15px;font-weight:500;color:#0B1433}
.p6-g3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.p6-g4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.p6-c{display:flex;flex-direction:column;gap:6px;padding:18px 20px;border-radius:18px;border:1.5px solid #E6EAF3;background:#FFFFFF}
.p6-c b{font-size:15.5px;font-weight:600;color:#0B1433}
.p6-c > span:last-child{font-size:13.5px;line-height:1.5;color:#5B6582}
.p6-ck{width:22px;height:22px;border-radius:50%;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.p6-c .p6-ck{margin-bottom:4px}
.p6-ic{width:36px;height:36px;border-radius:11px;background:#EAF0FF;color:#1652F0;display:flex;align-items:center;justify-content:center;margin-bottom:4px}
.p6-rs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;padding:18px 20px;border-radius:18px;background:#F5F8FF}
.p6-rs > div{display:flex;flex-direction:column;gap:10px}
.p6-chips{display:flex;flex-wrap:wrap;gap:6px}
.p6-req{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.p6-req > div{display:flex;flex-direction:column;align-items:flex-start;gap:10px;padding:18px 20px;border-radius:18px;border:1.5px solid #E6EAF3}
.p6-req b{font-size:15px;font-weight:500;line-height:1.45;color:#0B1433}
.p6-must{background:#0B1433;color:#FFFFFF}
.p6-rdy{display:flex;align-items:center;gap:16px;padding:18px 20px;border-radius:20px;border:1.5px solid #DCE5FB}
.p6-rdy p{margin:0;flex:1;font-size:14.5px;line-height:1.5;color:#3A4566}
.p6-rdy p b{font-weight:600;color:#0B1433}
.p6-rdy .ds-ghost{flex-shrink:0}
.p6-out{margin:0;padding:0;list-style:none;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px 28px}
.p6-out li{display:flex;gap:12px}
.p6-out li > span:last-child{display:flex;flex-direction:column;gap:2px}
.p6-out b{font-size:15px;font-weight:500;color:#0B1433}
.p6-out em{font-style:normal;font-size:12.5px;color:#0E3BB8}
.p6-cos{display:flex;flex-direction:column;gap:10px}
.p6-co{padding:12px 16px 12px 12px}
.p6-co .pd2-cal{flex-shrink:0}
.p6-cot{flex:1;display:flex;flex-direction:column;gap:2px;min-width:0}
.p6-cot b{font-size:16px;font-weight:600;color:#0B1433}
.p6-cot em{font-style:normal;font-size:13.5px;color:#5B6582}
.p6-co .ds-tag{margin-left:auto}
.p6-co .ds-opt-ck{margin-left:12px}
.p6-tw{overflow-x:auto;border:1.5px solid #E6EAF3;border-radius:20px}
.p6-t{width:100%;border-collapse:collapse;font-size:14px}
.p6-t th,.p6-t td{text-align:left;padding:13px 16px;border-top:1px solid #EEF1F7;vertical-align:top;color:#0B1433}
.p6-t thead th{border-top:none;font-size:12px;font-weight:500;color:#8A93AD;background:#F7F9FD}
.p6-t tbody th{font-weight:600}
.p6-cmp{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:12px}
.p6-cmp ul{margin:0;padding:20px 22px;list-style:none;display:flex;flex-direction:column;gap:12px;border-radius:18px;border:1.5px solid #E6EAF3}
.p6-cmp li{display:flex;align-items:center;gap:12px;font-size:15px;color:#0B1433}
.p6-cmp > div{display:flex;flex-direction:column;align-items:flex-start;gap:8px;padding:20px 22px;border-radius:18px;background:#F5F8FF}
.p6-cmp > div b{font-size:16px;font-weight:600}
.p6-cmp > div > span{font-size:14px;line-height:1.55;color:#5B6582}
.p6-steps{margin:0;padding:0;list-style:none;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.p6-steps li{display:flex;flex-direction:column;gap:6px;padding:18px;border-radius:18px;background:#F5F8FF}
.p6-sn{width:28px;height:28px;border-radius:50%;background:#FFFFFF;border:1.5px solid #C9D7FA;color:#1652F0;font-size:13px;font-weight:600;display:flex;align-items:center;justify-content:center;margin-bottom:4px}
.p6-steps b{font-size:15px;font-weight:600;color:#0B1433}
.p6-steps li > span:last-child{font-size:13.5px;line-height:1.45;color:#5B6582}
.p6-pay{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.p6-pc{display:flex;flex-direction:column;gap:8px;padding:20px 22px;border-radius:20px;border:1.5px solid #E6EAF3}
.p6-pc:first-child{border-color:#1652F0;background:linear-gradient(180deg,#F5F8FF,#FFFFFF)}
.p6-pc > span:last-child{font-size:14px;line-height:1.55;color:#5B6582}
.p6-pv{display:flex;align-items:center;gap:8px}
.p6-pv b{font-size:24px;font-weight:600;letter-spacing:-.5px;color:#0B1433}
.p6-pv .dlp-c,.p6-pv .cr-c{width:24px;height:24px;font-size:12px}
.p6-revs{display:grid;grid-template-columns:220px minmax(0,1fr) minmax(0,1fr);gap:12px}
.p6-score{display:flex;flex-direction:column;gap:4px;padding:20px;border-radius:18px;background:#F5F8FF}
.p6-score b{font-size:40px;font-weight:600;letter-spacing:-1px;line-height:1}
.p6-stars{color:#E3A008;letter-spacing:2px}
.p6-score span:last-of-type{font-size:13px;color:#5B6582}
.p6-score em{margin-top:6px;font-style:normal;font-size:12px;line-height:1.4;color:#8A93AD}
.p6-rev{margin:0;display:flex;flex-direction:column;justify-content:space-between;gap:12px;padding:20px;border-radius:18px;border:1.5px solid #E6EAF3}
.p6-rev blockquote{margin:0;font-size:14.5px;line-height:1.55;color:#0B1433}
.p6-rev figcaption{font-size:13px;color:#5B6582}
.p6-rev b{font-weight:600;color:#0B1433}
.p6-prov{display:flex;gap:16px;padding:20px 22px;border-radius:20px;border:1.5px solid #E6EAF3}
.p6-prov > div{display:flex;flex-direction:column;align-items:flex-start;gap:4px}
.p6-prov b{font-size:17px;font-weight:600;color:#0B1433}
.p6-prov > div > span:not(.p6-k){font-size:14px;line-height:1.5;color:#5B6582}
.p6-av{width:52px;height:52px;border-radius:16px;background:#EAF0FF;color:#0E3BB8;font-size:16px;font-weight:600;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.p6-alt{display:flex;align-items:center;gap:8px;margin-top:-6px;font-size:13px;color:#5B6582}
.p6-st{display:flex;flex-direction:column;align-items:flex-start;gap:6px;padding:16px;border-radius:16px}
.p6-st b{font-size:16px;font-weight:600;color:#0B1433;line-height:1.3}
.p6-st > span:not(.ds-tag){font-size:13.5px;line-height:1.5;color:#3A4566}
.p6-st-ok{background:#E7F5EE}
.p6-st-cb{background:#EAF0FF}
.p6-st-am{background:#FFF8EB}
.p6-st-gy{background:#F2F4F9}
.cd-pb{display:block;align-self:stretch;height:6px;border-radius:3px;background:rgba(22,82,240,.15);overflow:hidden;margin-top:4px}
.cd-pb i{display:block;height:100%;border-radius:3px;background:#1652F0}
.dt-tabs{overflow-x:auto;scrollbar-width:none}
.dt-tabs::-webkit-scrollbar{display:none}
@media (max-width: 1180px){.p6-g4,.p6-steps{grid-template-columns:repeat(2,minmax(0,1fr))}.p6-revs{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}.p6-score{grid-column:1 / -1}}
@media (max-width: 760px){
.p6-p{font-size:15px}
.p6-gl{grid-template-columns:repeat(2,minmax(0,1fr))}
.p6-gl div{padding:12px 14px;border-right:1px solid #EEF1F7 !important;border-bottom:1px solid #EEF1F7 !important}
.p6-gl div:nth-child(2n){border-right:0 !important}
.p6-gl div:nth-last-child(-n+2){border-bottom:0 !important}
.p6-gl dd{font-size:14px}
.p6-g3,.p6-g4,.p6-req,.p6-pay,.p6-cmp,.p6-rs,.p6-steps,.p6-out{grid-template-columns:minmax(0,1fr);gap:10px}
.p6-rdy{display:grid;grid-template-columns:36px minmax(0,1fr);gap:12px;align-items:start}
.p6-rdy .ds-ghost{grid-column:1 / -1}
.p6-co{flex-wrap:wrap;padding:12px 44px 12px 12px}
.p6-co .ds-tag{margin-left:68px}
.p6-co .ds-opt-ck{position:absolute;right:14px;top:50%;transform:translateY(-50%);margin:0}
.p6-steps li{display:grid;grid-template-columns:28px minmax(0,1fr);column-gap:12px;padding:14px 16px}
.p6-sn{grid-row:span 2;margin:0}
.p6-revs{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;margin:0 -20px;padding:0 20px 4px;scroll-padding:0 20px;scrollbar-width:none}
.p6-revs > *{flex:0 0 82%;scroll-snap-align:start;box-sizing:border-box}
.p6-prov{flex-direction:column;gap:12px}
.dt-tabs{-webkit-mask-image:linear-gradient(90deg,#000 88%,transparent);mask-image:linear-gradient(90deg,#000 88%,transparent)}
.p6-t{min-width:640px}
}
'''
s = s.replace('<b>Counts toward</b>', '<b>Prepares you for</b>')
i = s.find('</style>'); s = s[:i] + CSS + s[i:]
open(P, 'w').write(s); print('patched ProgramDetail')
