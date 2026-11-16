"""Landing batch 3 (client review, Course detail): the page answers the six questions on its own.
Adds: at a glance, about, skills with target levels, who it's for (+ Nova readiness), how you'll learn,
assessment detail (attempts, pass marks, what counts), what you'll earn (criteria + certificate preview),
FAQ, related learning; access card with both routes (DLP from the plan, Credits to own it); save + share;
access states via prop `access`: guest | enough | short | subonly | progress | owned | done | temp | closed.
Patches the live CourseDetail.dc.html in place. Usage: python3 cd3.py <canvas3/project>"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import tip, ck, nova_av
D = sys.argv[1]; P = os.path.join(D, 'CourseDetail.dc.html'); s = open(P).read()
assert 'cd-gl' not in s, 'already patched'
KIT = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kit.py')).read()

def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:100], s.count(a)); s = s.replace(a, b)
def svg(d, w=18, sw=2):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (w, w, sw, d)
HEART = svg('<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"></path>', 17)
SHARE = svg('<path d="M12 15V4M8 8l4-4 4 4"></path><path d="M5 13v5a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-5"></path>', 17)
I = {'vid': '<rect x="3" y="5" width="18" height="14" rx="3"></rect><path d="m10 9 5 3-5 3z"></path>', 'read': '<path d="M5 4h10l4 4v12H5z"></path><path d="M9 12h6M9 16h6"></path>',
     'prac': '<path d="m8 9-4 3 4 3M16 9l4 3-4 3"></path>', 'quiz': '<circle cx="12" cy="12" r="9"></circle><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .8-1 1.5v.2M12 17h.01"></path>',
     'proj': '<rect x="3" y="7" width="18" height="13" rx="2.5"></rect><path d="M8 7V5h8v2"></path>', 'dl': '<path d="M12 4v11M7 10l5 5 5-5M5 20h14"></path>',
     'nova': '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"></path>', 'tutor': '<circle cx="9" cy="8" r="3.2"></circle><path d="M3.5 19c.6-3 2.8-4.6 5.5-4.6s4.9 1.6 5.5 4.6"></path><path d="M16 11.5l2 2 3.5-3.5"></path>',
     'chat': '<path d="M5 5h14v10H9l-4 4z"></path>'}
def ico(k, w=18): return svg(I[k], w, 1.9)

# ---------------------------------------------------------------- hero: status banner, save + share
rep('<a class="ds-link cd-askm" href="#">',
    '<sc-if value="{{hasBan}}" hint-placeholder-val="{{ false }}"><div class="cd-ban {{banCls}}" role="status"><i class="cd-bd" aria-hidden="true"></i><span><b>{{banT}}</b><span>{{banD}}</span></span></div></sc-if>\n'
    '<div class="cd-acts"><button class="ds-ghost sm {{saveCls}}" type="button" aria-pressed="{{wishOn}}" onClick="{{toggleWish}}">' + HEART + '<span>{{saveLabel}}</span></button>'
    '<button class="ds-ghost sm" type="button">' + SHARE + '<span>Share</span></button></div>\n<a class="ds-link cd-askm" href="#">')

# ---------------------------------------------------------------- overview: at a glance + about (outcomes keep their own section)
GL = [('Format', 'Self-paced'), ('Language', 'English'), ('Captions', 'English'), ('Assessment', 'Quizzes, project, practical test'), ('Last updated', '24 Sep 2026'), ('Version', '2.1, validated')]
ABOUT = ('Spreadsheets take you a long way, until the data gets big or messy. This course takes you from a tidy table to confident SQL, one small step at a time. '
         'Every module uses the same real sales data, so each new idea is put to work straight away. You finish with a project you can show: a real business question, answered with SQL and explained in plain words.')
rep('<section class="cd-sec" ref="{{refOverview}}" aria-labelledby="cd-o">\n<h2 id="cd-o" class="cd-h2">What you’ll be able to do</h2>',
    '<section class="cd-sec" ref="{{refOverview}}" aria-labelledby="cd-ab">\n<dl class="cd-gl">%s</dl>\n<h2 id="cd-ab" class="cd-h2">About this course</h2>\n<p class="cd-p">%s</p>\n</section>\n\n'
    '<section class="cd-sec" aria-labelledby="cd-o">\n<h2 id="cd-o" class="cd-h2">What you’ll be able to do</h2>' % (''.join('<div><dt>%s</dt><dd>%s</dd></div>' % g for g in GL), ABOUT))

# ---------------------------------------------------------------- skills + who it's for (before curriculum)
SK = [('Cleaning spreadsheet data', 2), ('Writing SQL queries', 2), ('Joining and summarising data', 1), ('Explaining findings', 1)]
LV = ['', 'Foundational', 'Intermediate', 'Advanced', 'Expert']
skills = ''.join('<div class="cd-skr"><span class="cd-skn">%s</span><span class="cd-skb" aria-hidden="true">%s</span><span class="cd-skl">%s</span></div>' % (
    n, ''.join('<i class="%s"></i>' % ('on' if k <= lv else '') for k in range(1, 5)), LV[lv]) for n, lv in SK)
AUD = [('Designed for', 'Office workers, career changers and new analysts who already live in spreadsheets.'), ('You’ll need', 'Basic spreadsheet use: sorting, filtering and simple formulas.'),
       ('Good to have', 'Nothing else. No coding experience needed.'), ('Tools', 'A laptop and a browser. The SQL practice editor runs inside Credalio, so there’s nothing to install.')]
NEW1 = ('<section class="cd-sec" aria-labelledby="cd-sk">\n<div class="cd-sh"><h2 id="cd-sk" class="cd-h2">Skills you’ll develop%s</h2><span class="cd-sm">Target level by the end</span></div>\n'
        '<div class="cd-sks">%s</div>\n</section>\n\n'
        '<section class="cd-sec" aria-labelledby="cd-au">\n<h2 id="cd-au" class="cd-h2">Who this course is for</h2>\n<div class="cd-aud">%s</div>\n'
        '<div class="cd-rdy nova-card">%s<p><b>Not sure you’re ready?</b> Nova, your AI Coach, compares what you know with these requirements and suggests where to start. It never stops you starting.</p>'
        '<a class="ds-ghost sm" href="#">Check my readiness</a></div>\n</section>\n\n') % (
    tip('Levels on the Credalio scale: Foundational, Intermediate, Advanced, Expert.'), skills,
    ''.join('<div class="cd-chk"><b>%s</b><span>%s</span></div>' % a for a in AUD), nova_av())
rep('<section class="cd-sec" ref="{{refCurriculum}}"', NEW1 + '<section class="cd-sec" ref="{{refCurriculum}}"')

# curriculum: free previews open the lesson preview screen
rep('<span class="cd-lt">{{l.t}}</span><span class="cd-lk">{{l.k}}</span>',
    '<span class="cd-lt">{{l.t}}</span><sc-if value="{{l.prev}}" hint-placeholder-val="{{ false }}"><a class="cd-pv" href="{{l.href}}">Free preview</a></sc-if><span class="cd-lk">{{l.k}}</span>')

# ---------------------------------------------------------------- how you'll learn (after curriculum)
FMT = [('vid', '2', 'Videos'), ('read', '9', 'Readings'), ('prac', '5', 'Practice tasks'), ('quiz', '5', 'Module checks'), ('proj', '3', 'Project steps'), ('dl', '4', 'Downloads')]
SUP = [('nova', 'Nova, your AI Coach, in every lesson', 'Ask for a hint, an example or another explanation.'), ('tutor', 'A human tutor when you need one', 'Nova hands over with your question and what you’ve tried.'),
       ('chat', 'Course Q&amp;A with Amara', 'Questions go to the course Q&amp;A, linked to your enrolment.')]
NEW2 = ('<section class="cd-sec" aria-labelledby="cd-hw">\n<div class="cd-sh"><h2 id="cd-hw" class="cd-h2">How you’ll learn</h2><span class="cd-sm">Self-paced · no live sessions</span></div>\n'
        '<div class="cd-fm">%s</div>\n<ul class="cd-sup">%s</ul>\n</section>\n\n') % (
    ''.join('<div><span class="cd-fi">%s</span><b>%s</b><span>%s</span></div>' % (ico(k), n, l) for k, n, l in FMT),
    ''.join('<li><span class="cd-ii">%s</span><span><b>%s</b><span>%s</span></span></li>' % (ico(k, 17), t, d) for k, t, d in SUP))
rep('<section class="cd-sec" ref="{{refProject}}"', NEW2 + '<section class="cd-sec" ref="{{refProject}}"')

# ---------------------------------------------------------------- assessments: attempts, pass marks, what counts
rep('<span class="cd-std">Quick quizzes that show what has stuck.</span></div>', '<span class="cd-std">Quick quizzes that show what has stuck.</span><span class="cd-sx">Unlimited attempts · don’t affect your result</span></div>')
rep('<span class="cd-std">Clean it, query it, explain it. Reviewed by a mentor.</span></div>', '<span class="cd-std">Clean it, query it, explain it. Reviewed by a mentor.</span><span class="cd-sx">2 submissions · needed for the certificate</span></div>')
rep('<span class="cd-std">Hands-on, not multiple choice. Pass mark 70%.</span></div>', '<span class="cd-std">Hands-on, not multiple choice. Pass mark 70%.</span><span class="cd-sx">2 attempts · needed for the certificate</span></div>')
rep('<span class="cd-sk">You earn</span><span class="cd-stt">Verified certificate</span><span class="cd-std">Saved to your Digital Backpack.</span></div>',
    '<span class="cd-sk">You earn</span><span class="cd-stt">Course certificate</span><span class="cd-std">Saved to your Digital Backpack.</span><span class="cd-sx">When the three above are done</span></div>')
rep('<h2 id="cd-pr" class="cd-h2">Prove it as you go', '<h2 id="cd-pr" class="cd-h2">Assessments')

# ---------------------------------------------------------------- what you'll earn (after assessments)
CRIT = ['Complete all 24 lessons', 'Pass the 5 module checks', 'Submit the sales project', 'Pass the practical SQL test (70%)']
NEW3 = ('<section class="cd-sec" aria-labelledby="cd-ea">\n<h2 id="cd-ea" class="cd-h2">What you’ll earn</h2>\n<div class="cd-earn">\n'
        '<div class="cd-crit"><span class="cd-req">To complete the course</span><ul>%s</ul><p class="cd-sm">Your certificate is saved to your Digital Backpack, with a link anyone can check.</p></div>\n'
        '<div class="cd-cert"><div class="cd-cp"><span class="cd-ck2">Certificate of completion</span><b>Data Foundations: Spreadsheets to SQL</b><span class="cd-cn2">Awarded to <em>Ada Ononuju</em></span>'
        '<span class="cd-cm">Issued by Amara Okafor · Gold Validated · VAL-CRD-004821</span><span class="cd-cseal" aria-hidden="true">%s</span></div>'
        '<span class="ds-tag line">A course certificate, not a Professional Certification</span>'
        '<a class="ds-link" href="CertDetail.dc.html">Want a professional credential? Professional Certificate in Data Analysis →</a></div>\n</div>\n</section>\n\n') % (
    ''.join('<li><span class="cd-ck" aria-hidden="true">%s</span>%s</li>' % (ck(11), c) for c in CRIT), ck(18))
rep('<section class="cd-sec" ref="{{refValidation}}"', NEW3 + '<section class="cd-sec" ref="{{refValidation}}"')

# ---------------------------------------------------------------- FAQ + related learning (after reviews, before the path band)
REL = [('Next course', 'SQL for Data Analysis', 'Go further with subqueries, window functions and reports.', 'CourseDetail.dc.html'),
       ('Professional certification', 'Professional Certificate in Data Analysis', 'This course covers 2 of its 6 competencies.', 'CertDetail.dc.html'),
       ('Learning program', 'AI &amp; Data Analytics Accelerator', 'Learn it live with a cohort, starting 18 January.', 'ProgramDetail.dc.html')]
NEW4 = ('<section class="cd-sec" ref="{{refFAQ}}" aria-labelledby="cd-fq">\n<h2 id="cd-fq" class="cd-h2">Questions learners ask</h2>\n<div class="cd-mods cd-fq">\n'
        '<sc-for list="{{faqs}}" as="f" hint-placeholder-count="5"><div class="cd-mod {{f.cls}}"><button class="cd-mh" type="button" aria-expanded="{{f.exp}}" onClick="{{f.toggle}}"><span class="cd-mt">{{f.q}}</span>'
        '<svg class="cd-chev" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"></path></svg></button>'
        '<sc-if value="{{f.open}}" hint-placeholder-val="{{ false }}"><p class="cd-fa">{{f.a}}</p></sc-if></div></sc-for>\n</div>\n</section>\n\n'
        '<section class="cd-sec" aria-labelledby="cd-rl">\n<h2 id="cd-rl" class="cd-h2">Keep learning</h2>\n<div class="cd-rel">%s</div>\n</section>\n\n') % (
    ''.join('<a class="cd-rc" href="%s"><span class="cd-sk">%s</span><b>%s</b><span>%s</span></a>' % (h, k, t, d) for k, t, d, h in REL))
rep('<a class="cd-path aur" href="PathDetail.dc.html">', NEW4 + '<a class="cd-path aur" href="PathDetail.dc.html">')

# ---------------------------------------------------------------- access card: two routes + states
old_body = s[s.index('<div class="cd-cbody">'):s.index('<ul class="cd-inc">')]
DLPC = '<span class="dlp-c" aria-hidden="true"></span>'
NEWBODY = ('<div class="cd-cbody">\n'
  '<sc-if value="{{showRoutes}}" hint-placeholder-val="{{ true }}"><span class="cd-req">Choose how to access%s</span>\n'
  '<div class="cd-rts" role="radiogroup" aria-label="Access route">'
  '<button class="ds-opt cd-rt {{rDlp}}" type="button" role="radio" aria-checked="{{aDlp}}" onClick="{{pickDlp}}">%s<span class="cd-rtt"><b>200 DLP</b><em>With your subscription</em></span><span class="ds-opt-ck">%s</span></button>'
  '<sc-if value="{{hasCr}}" hint-placeholder-val="{{ true }}"><button class="ds-opt cd-rt {{rCr}}" type="button" role="radio" aria-checked="{{aCr}}" onClick="{{pickCr}}"><i class="cr-c" aria-hidden="true">C</i><span class="cd-rtt"><b>400 Credits</b><em>Own it for life</em></span><span class="ds-opt-ck">%s</span></button></sc-if>'
  '</div>\n<p class="cd-rn">{{routeNote}}</p></sc-if>\n'
  '<sc-if value="{{hasSt}}" hint-placeholder-val="{{ false }}"><div class="cd-st {{stCls}}"><b>{{stT}}</b><span>{{stD}}</span><sc-if value="{{hasPct}}" hint-placeholder-val="{{ false }}"><span class="cd-pb" aria-hidden="true"><i style="width: {{pct}}"></i></span></sc-if></div></sc-if>\n'
  '<sc-if value="{{showFit}}" hint-placeholder-val="{{ true }}"><span class="ds-tag green lg" style="align-self: flex-start; margin-top: -4px">%s{{fit}}</span></sc-if>\n'
  '<sc-if value="{{notEnrolled}}" hint-placeholder-val="{{ true }}"><a class="ds-btn {{ctaDis}}" href="{{ctaHref}}" onClick="{{ctaClick}}" aria-disabled="{{ctaAria}}"><span>{{cta}}</span><span class="ob-arrow">%s</span></a></sc-if>\n'
  '<sc-if value="{{enrolled}}" hint-placeholder-val="{{ false }}"><span class="ds-tag green lg" role="status" style="align-self: flex-start">%sYou’re in. Lesson 1 is ready.</span><a class="ds-btn" href="LessonPreview.dc.html"><span>Start lesson 1</span><span class="ob-arrow">%s</span></a></sc-if>\n'
  '<sc-if value="{{hasSecond}}" hint-placeholder-val="{{ false }}"><a class="ds-ghost" href="{{secondHref}}">{{second}}</a></sc-if>\n'
  '<a class="ds-link cd-askc" href="#"><span class="nv-av sm" aria-hidden="true"><img src="/_blob/398ca91d2832bb0ab6b0af61319676f4" alt=""></span>Ask Nova, your AI Coach, if it fits</a>\n') % (
  tip('DLP is the learning allowance in your plan: you keep access while you learn, then 30 days to revise after you finish. Credits are bought separately and own the course for life, with its future updates. They are two routes, not one price converted.', ),
  DLPC, ck(12), ck(12), ck(12),
  svg('<path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path>', 18, 2.4), ck(12), svg('<path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path>', 18, 2.4))
s = s.replace(old_body, NEWBODY, 1)
rep('<button class="ds-ghost dk sm" type="button"><i aria-hidden="true">', '<a class="ds-ghost dk sm" href="LessonPreview.dc.html"><i aria-hidden="true">')
s = re.sub(r'(<a class="ds-ghost dk sm" href="LessonPreview\.dc\.html"><i aria-hidden="true">.*?</i>Preview lesson 1)</button>', r'\1</a>', s, count=1, flags=re.S)
rep('<div class="cd-binfo"><b><span class="dlp-c"></span>200 DLP</b><span aria-hidden="true">·</span><span>{{fitShort}}</span></div>',
    '<div class="cd-binfo"><b>{{barPrice}}</b><span aria-hidden="true">·</span><span>{{fitShort}}</span></div>')
s = re.sub(r'<button class="ds-btn" type="button" onClick="\{\{enrol\}\}"><span>\{\{barCta\}\}</span>', '<a class="ds-btn {{ctaDis}}" href="{{ctaHref}}" onClick="{{ctaClick}}"><span>{{barCta}}</span>', s, count=1)
s = re.sub(r'(<a class="ds-btn \{\{ctaDis\}\}" href="\{\{ctaHref\}\}" onClick="\{\{ctaClick\}\}"><span>\{\{barCta\}\}</span><span class="ob-arrow">.*?</span>)</button>', r'\1</a>', s, count=1, flags=re.S)

# ---------------------------------------------------------------- JS
rep('"viewer":{"editor":"enum","options":["guest","learner"],"default":"guest"}',
    '"viewer":{"editor":"enum","options":["guest","learner"],"default":"guest"},"access":{"editor":"enum","options":["guest","enough","short","subonly","progress","owned","done","temp","closed"],"default":"guest"}')
rep("this.state = { tab: 'Overview', open: 0, enrolled: false, wish: false };", "this.state = { tab: 'Overview', open: 0, enrolled: false, wish: false, route: 'dlp', faq: 0 };")
rep("Reviews: this.mk('Reviews') };", "Reviews: this.mk('Reviews'), FAQ: this.mk('FAQ') };")
rep("var names = ['Overview', 'Curriculum', 'Project', 'Validation', 'Creator', 'Reviews'];", "var names = ['Overview', 'Curriculum', 'Project', 'Validation', 'Creator', 'Reviews', 'FAQ'];\n    var LBL = { Project: 'Assessments' };")
rep("return { label: n, on:", "return { label: LBL[n] || n, on:")
rep("refReviews: this.R.Reviews,", "refReviews: this.R.Reviews, refFAQ: this.R.FAQ,")
rep("ls: m[1].map(function (l) { var v = { t: l[0], k: l[1] };", "ls: m[1].map(function (l, j) { var v = { t: l[0], k: l[1], prev: i === 0 && j < 2, href: j === 0 ? 'LessonPreview.dc.html' : 'LessonPreview-Reading.dc.html' };")
FAQS = [('How long do I keep access?', 'With your subscription you learn using DLP, then get 30 days to revise after you finish. Own it with Credits instead and it’s yours for life, including future updates.'),
        ('Are DLP and Credits the same thing?', 'No. They’re two separate routes. DLP comes with your plan; Credits are bought separately. One is never converted into the other.'),
        ('Do I need to know SQL already?', 'No. Basic spreadsheet skills are enough. Nova can check your readiness before you start.'),
        ('Is the certificate a Professional Certification?', 'No. It shows you completed this course. Professional Certifications are assessed separately, against a published standard.'),
        ('What happens when the course is updated?', 'If you own it with Credits, updates are included. Every major update is validated again before it goes live.')]
import json
JS_ST = r'''
    var A = this.props.access || (me ? 'enough' : 'guest');
    var X = {
      guest: { fit: 'Covered by the free plan', cta: 'Start free', enrol: 1 },
      enough: { fit: 'Covered by your 1,460 DLP', cta: 'Start learning', enrol: 1 },
      short: { fit: '', cta: 'Top up DLP', href: 'Chk-TOP.dc.html', st: ['am', '80 DLP short', 'Your balance is 120 DLP. Top up, change your plan, or own it with Credits.'], second: ['Own it for 400 Credits', '#'], bar: '80 DLP short' },
      subonly: { fit: 'Covered by your 1,460 DLP', cta: 'Start learning', enrol: 1, noCr: 1 },
      progress: { routes: 0, cta: 'Continue learning', href: 'LessonPreview-Reading.dc.html', ban: ['cb', 'In progress', 'Module 3 of 6 · 38% complete'], st: ['cb', 'Subscription access active', 'You keep access while you learn, then 30 days to revise after you finish.', '38%'], bar: '38% complete' },
      owned: { routes: 0, cta: 'Open course', href: 'LessonPreview.dc.html', ban: ['ok', 'You own this course', 'Bought with Credits on 2 Oct 2026'], st: ['ok', 'Lifetime access', 'Includes this course and its future updates. Other courses and paid certifications aren’t included.'], bar: 'Owned for life' },
      done: { routes: 0, cta: 'Revisit for 100 DLP', href: '#', ban: ['ok', 'Completed 12 Oct 2026', 'Your certificate is in your Digital Backpack'], st: ['gy', 'Revision period ended 11 Nov 2026', 'Your completion and certificate stay on your record. Revisiting uses 100 DLP.'], second: ['Own it for 400 Credits', '#'], bar: 'Completed' },
      temp: { routes: 0, cta: 'Continue learning', href: 'LessonPreview-Reading.dc.html', ban: ['am', 'Temporary access ends 28 Nov', '12 days left, through Northgate University'], st: ['am', 'Access ends in 12 days', 'Keep learning after 28 Nov with your DLP, or own it with Credits.'], second: ['Own it for 400 Credits', '#'], bar: '12 days left' },
      closed: { routes: 0, cta: 'Not available', dis: 1, ban: ['gy', 'Not open to new learners', 'Everyone already enrolled keeps their access.'], st: ['gy', 'This version has been retired', 'The creator may publish a replacement. Nova can suggest similar courses.'], second: ['See similar courses', 'Courses.dc.html'], bar: 'Not available' }
    };
    var x = X[A] || X.guest, cr = !x.noCr && S.route === 'cr';
    var go = x.enrol ? function (e) { if (e && e.preventDefault) e.preventDefault(); enrol(); } : function () {};
    var FQ = FAQS_;
'''
rep("    var enrol = function () { self.setState({ enrolled: true }); };", "    var enrol = function () { self.setState({ enrolled: true }); };" + JS_ST.replace('FAQS_', json.dumps(FAQS, ensure_ascii=False)))
old_ret = s[s.index("      fit: me ? 'Covered by your 1,460 DLP' : 'Covered by the free plan',"):s.index("      wishOn:")]
NEW_RET = r'''      fit: cr ? 'Yours for life, with future updates' : x.fit, showFit: !!x.fit && x.routes !== 0,
      fitShort: x.bar || (cr ? 'Own it for life' : x.fit),
      barPrice: cr ? '400 Credits' : '200 DLP',
      showRoutes: x.routes !== 0, hasCr: !x.noCr,
      rDlp: !cr ? 'on' : '', aDlp: !cr ? 'true' : 'false', rCr: cr ? 'on' : '', aCr: cr ? 'true' : 'false',
      pickDlp: function () { self.setState({ route: 'dlp' }); }, pickCr: function () { self.setState({ route: 'cr' }); },
      routeNote: x.noCr ? 'This creator offers subscription access only.' : (cr ? 'Credits are bought separately from your plan. You keep the course for life.' : 'Uses DLP from your plan. You get 30 days to revise after you finish.'),
      hasBan: !!x.ban, banCls: x.ban ? 'cd-ban-' + x.ban[0] : '', banT: x.ban ? x.ban[1] : '', banD: x.ban ? x.ban[2] : '',
      hasSt: !!x.st, stCls: x.st ? 'cd-st-' + x.st[0] : '', stT: x.st ? x.st[1] : '', stD: x.st ? x.st[2] : '', hasPct: !!(x.st && x.st[3]), pct: x.st && x.st[3] ? x.st[3] : '0%',
      cta: cr ? 'Own it for 400 Credits' : x.cta, ctaHref: cr ? '#' : (x.href || '#'), ctaClick: cr ? function () {} : go, ctaDis: x.dis ? 'cd-dis' : '', ctaAria: x.dis ? 'true' : 'false',
      hasSecond: !!x.second, second: x.second ? x.second[0] : '', secondHref: x.second ? x.second[1] : '#',
      barCta: S.enrolled ? 'Start lesson 1' : (cr ? 'Own it for 400 Credits' : x.cta),
      enrolled: S.enrolled, notEnrolled: !S.enrolled, enrol: enrol,
      faqs: FQ.map(function (f, i) { var o = S.faq === i; return { q: f[0], a: f[1], open: o, exp: o ? 'true' : 'false', cls: o ? 'cd-mod-open' : '', toggle: function () { self.setState({ faq: o ? -1 : i }); } }; }),
      saveCls: S.wish ? 'on' : '', saveLabel: S.wish ? 'Saved' : 'Save',
'''
s = s.replace(old_ret, NEW_RET, 1)

# ---------------------------------------------------------------- CSS
need = [l.strip() for l in KIT.split('\n') if re.match(r'\.(ds-opt|cr-c)', l.strip())]
CSS = '\n'.join(need) + r'''
.nova-card{background:#FFFFFF url(/_blob/0b29db2e4cd6f4a89dc7ba8f12e59c8d) center / cover no-repeat}
.cd-acts{display:flex;flex-wrap:wrap;gap:10px;margin-top:6px}
.cd-acts .ds-ghost{height:40px;padding:0 16px;font-size:14px}
.cd-acts .ds-ghost.on{color:#0E3BB8}
.cd-acts .ds-ghost.on svg path{fill:currentColor}
.cd-ban{display:flex;align-items:flex-start;gap:12px;margin-top:10px;padding:14px 16px;border-radius:16px;font-size:14px;line-height:1.45}
.cd-ban > span{display:flex;flex-direction:column;gap:2px}
.cd-ban b{font-weight:600}
.cd-bd{width:10px;height:10px;border-radius:50%;margin-top:5px;flex-shrink:0;font-style:normal;background:currentColor}
.cd-ban-ok{background:#E7F5EE;color:#0F6B45}
.cd-ban-cb{background:#EAF0FF;color:#0E3BB8}
.cd-ban-am{background:#FFF4E0;color:#8A5A00}
.cd-ban-gy{background:#F2F4F9;color:#3A4566}
.cd-ban span span{color:#3A4566}
.cd-gl{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));margin:0;border:1.5px solid #E6EAF3;border-radius:20px;overflow:hidden}
.cd-gl div{padding:16px 20px;border-right:1px solid #EEF1F7;border-bottom:1px solid #EEF1F7}
.cd-gl div:nth-child(3n){border-right:0}
.cd-gl div:nth-last-child(-n+3){border-bottom:0}
.cd-gl dt{font-size:12px;font-weight:500;color:#8A93AD}
.cd-gl dd{margin:4px 0 0;font-size:15px;font-weight:500;color:#0B1433}
.cd-p{margin:0;max-width:720px;font-size:16px;line-height:1.65;color:#3A4566;text-wrap:pretty}
.cd-sks{display:flex;flex-direction:column;border:1.5px solid #E6EAF3;border-radius:20px;padding:6px 22px}
.cd-skr{display:grid;grid-template-columns:minmax(0,1fr) 220px 110px;align-items:center;gap:20px;min-height:56px}
.cd-skr + .cd-skr{border-top:1px solid #EEF1F7}
.cd-skn{font-size:15px;font-weight:500;color:#0B1433}
.cd-skb{display:grid;grid-template-columns:repeat(4,1fr);gap:4px}
.cd-skb i{height:8px;border-radius:4px;background:#EEF1F7}
.cd-skb i.on{background:#1652F0}
.cd-skl{font-size:13px;font-weight:500;color:#0E3BB8;text-align:right}
.cd-aud{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.cd-aud .cd-chk{padding:16px 18px;border-radius:16px}
.cd-aud .cd-chk b{font-size:13px;font-weight:500;color:#8A93AD}
.cd-aud .cd-chk span{font-size:15px;line-height:1.5;color:#0B1433}
.cd-rdy{display:flex;align-items:center;gap:16px;padding:18px 20px;border-radius:20px;border:1.5px solid #DCE5FB}
.cd-rdy p{margin:0;flex:1;font-size:14.5px;line-height:1.5;color:#3A4566}
.cd-rdy p b{font-weight:600;color:#0B1433}
.cd-rdy .ds-ghost{flex-shrink:0}
.cd-pv{margin-left:auto;font-size:12px;font-weight:500;color:#0E3BB8;background:#EAF0FF;border-radius:999px;padding:3px 10px;text-decoration:none;white-space:nowrap}
.cd-pv + .cd-lk{margin-left:10px}
.cd-l .cd-lt{flex:1;min-width:0}
.cd-fm{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:10px}
.cd-fm > div{display:flex;flex-direction:column;gap:2px;padding:16px;border-radius:16px;background:#F5F8FF}
.cd-fi{width:34px;height:34px;border-radius:10px;background:#FFFFFF;color:#1652F0;display:flex;align-items:center;justify-content:center;margin-bottom:8px}
.cd-fm b{font-size:22px;font-weight:600;letter-spacing:-.4px;color:#0B1433}
.cd-fm span{font-size:13px;color:#5B6582}
.cd-sup{margin:0;padding:0;list-style:none;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.cd-sup li{display:flex;gap:12px;padding:16px;border-radius:16px;border:1.5px solid #E6EAF3}
.cd-sup li > span:last-child{display:flex;flex-direction:column;gap:3px}
.cd-sup b{font-size:14.5px;font-weight:600;color:#0B1433}
.cd-sup li > span:last-child > span{font-size:13px;line-height:1.45;color:#5B6582}
.cd-sup .cd-ii{width:34px;height:34px;border-radius:10px;background:#EAF0FF;color:#1652F0;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.cd-sx{margin-top:6px;font-size:12px;font-weight:500;color:#0E3BB8}
.cd-step > .cd-sx{grid-column:2}
.cd-earn{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr);gap:20px;align-items:stretch}
.cd-crit{display:flex;flex-direction:column;gap:14px;padding:22px;border-radius:20px;border:1.5px solid #E6EAF3}
.cd-crit ul{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:12px}
.cd-crit li{display:flex;align-items:center;gap:12px;font-size:15px;color:#0B1433}
.cd-crit .cd-sm{margin:4px 0 0;padding-top:14px;border-top:1px solid #EEF1F7;font-size:13.5px;line-height:1.5}
.cd-cert{display:flex;flex-direction:column;align-items:flex-start;gap:12px}
.cd-cp{position:relative;align-self:stretch;display:flex;flex-direction:column;gap:6px;padding:24px 26px;border-radius:18px;background:linear-gradient(160deg,#FFFFFF,#F5F8FF);border:1.5px solid #DCE5FB;box-shadow:inset 0 0 0 6px #FFFFFF,inset 0 0 0 7px #E6EAF3}
.cd-ck2{font-size:11px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:#8A93AD}
.cd-cp b{font-size:20px;font-weight:600;letter-spacing:-.3px;color:#0B1433;max-width:80%}
.cd-cn2{font-size:14px;color:#5B6582}
.cd-cn2 em{font-style:normal;font-weight:600;color:#0B1433}
.cd-cm{margin-top:8px;font-size:12.5px;color:#8A93AD}
.cd-cseal{position:absolute;right:22px;top:22px;width:44px;height:44px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#F9DC7A,#C38712);color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 14px -6px rgba(150,96,0,.6)}
.cd-cert .ds-link{font-size:14px;white-space:normal;display:block;line-height:1.5}
.cd-fq .cd-mh{padding-left:22px}
.cd-fa{margin:0;padding:0 22px 18px;font-size:14.5px;line-height:1.6;color:#3A4566}
.cd-rel{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.cd-rc{display:flex;flex-direction:column;gap:6px;padding:18px 20px;border-radius:18px;border:1.5px solid #E6EAF3;text-decoration:none;color:#0B1433;transition:border-color .2s ease,transform .3s ease}
.cd-rc:hover{border-color:#9DB8F7;transform:translateY(-2px)}
.cd-rc b{font-size:16px;font-weight:600;line-height:1.3}
.cd-rc > span:last-child{font-size:13.5px;line-height:1.45;color:#5B6582}
.cd-rts{display:flex;flex-direction:column;gap:8px;margin-top:-6px}
.cd-rt{padding:12px 14px}
.cd-rt .dlp-c,.cd-rt .cr-c{width:26px;height:26px;font-size:13px}
.cd-rtt{display:flex;flex-direction:column;gap:1px}
.cd-rtt b{font-size:17px;font-weight:600;color:#0B1433}
.cd-rtt em{font-style:normal;font-size:13px;color:#5B6582}
.cd-rn{margin:-6px 0 0;font-size:12.5px;line-height:1.5;color:#5B6582}
.cd-st{display:flex;flex-direction:column;gap:4px;padding:14px 16px;border-radius:16px;font-size:13.5px;line-height:1.5}
.cd-st b{font-size:15px;font-weight:600}
.cd-st span{color:#3A4566}
.cd-st-ok{background:#E7F5EE;color:#0F6B45}
.cd-st-cb{background:#EAF0FF;color:#0E3BB8}
.cd-st-am{background:#FFF4E0;color:#8A5A00}
.cd-st-gy{background:#F2F4F9;color:#3A4566}
.cd-pb{display:block;height:6px;border-radius:3px;background:rgba(22,82,240,.15);margin-top:8px;overflow:hidden}
.cd-pb i{display:block;height:100%;border-radius:3px;background:#1652F0}
.ds-btn.cd-dis{background:#E6EAF3;color:#8A93AD;box-shadow:none;pointer-events:none}
.ds-btn.cd-dis .ob-arrow{background:#FFFFFF;color:#8A93AD}
.cd-askc{justify-content:center;gap:8px;font-size:14px}
@media (max-width: 960px){.cd-fm{grid-template-columns:repeat(3,minmax(0,1fr))}.cd-sup,.cd-rel{grid-template-columns:minmax(0,1fr)}.cd-earn{grid-template-columns:minmax(0,1fr)}}
@media (max-width: 760px){
.cd-gl{grid-template-columns:repeat(2,minmax(0,1fr))}
.cd-gl div{padding:12px 14px;border-right:1px solid #EEF1F7 !important;border-bottom:1px solid #EEF1F7 !important}
.cd-gl div:nth-child(2n){border-right:0 !important}
.cd-gl div:nth-last-child(-n+2){border-bottom:0 !important}
.cd-gl dd{font-size:14px}
.cd-p{font-size:15px}
.cd-sks{padding:4px 16px}
.cd-skr{grid-template-columns:minmax(0,1fr) auto;row-gap:8px;padding:12px 0;min-height:0}
.cd-skb{grid-column:1 / -1;grid-row:2}
.cd-aud{grid-template-columns:minmax(0,1fr);gap:0;border:1.5px solid #E6EAF3;border-radius:18px;overflow:hidden}
.cd-aud .cd-chk{border-radius:0;background:#FFFFFF;padding:14px 16px}
.cd-aud .cd-chk + .cd-chk{border-top:1px solid #EEF1F7}
.cd-rdy{flex-direction:column;align-items:stretch;text-align:left}
.cd-rdy .nv-av{align-self:flex-start}
.cd-fm{grid-template-columns:repeat(2,minmax(0,1fr))}
.cd-fm > div{padding:14px}
.cd-acts{margin-top:2px}
.cd-cp b{font-size:17px}
.cd-l{flex-wrap:wrap}
}
@media (max-width: 760px){.cd-aud .cd-chk{border-radius:0 !important;display:flex !important;flex-direction:column}.cd-aud .cd-chk span{display:block !important}.cd-pv + .cd-lk{display:none}.cd-pv{margin-left:auto}.cd-rdy{display:grid;grid-template-columns:36px minmax(0,1fr);gap:12px;align-items:start}.cd-rdy .ds-ghost{grid-column:1 / -1}}
'''
i = s.find('</style>'); s = s[:i] + CSS + s[i:]
open(P, 'w').write(s); print('patched CourseDetail')
