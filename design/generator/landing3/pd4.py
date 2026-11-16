"""Landing batch 4 (client review, Career path detail): explore the path before personalising it.
Adds to the live PathDetail.dc.html (patched in place): validation + rating + Share + Check my readiness in the hero,
journey snapshot, about, who it's for, starting skills and readiness, career outcomes, skills progression,
assessments and milestones (certification optional and separate), what you'll achieve, access and pricing
(DLP, Credits per course, path package), the people behind the path, path reviews and FAQ.
The route and "Make it yours" stay; the panel also shows the path package. Usage: python3 pd4.py <canvas3/project>"""
import re, sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import kit
from kit import tip, ck, nova_av
D = sys.argv[1]; P = os.path.join(D, 'PathDetail.dc.html'); s = open(P).read()
assert 'pd4-' not in s, 'already patched'

def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:90], s.count(a)); s = s.replace(a, b)
def svg(d, w=18, sw=2):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (w, w, sw, d)
SHARE = svg('<path d="M12 15V4M8 8l4-4 4 4"></path><path d="M5 13v5a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-5"></path>', 17)
ARR = svg('<path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path>', 18, 2)
CHEV = '<svg class="pd4-chev" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"></path></svg>'
I = {'flag': '<path d="M5 21V4h11l-2 4 2 4H5"></path>', 'role': '<rect x="3" y="7" width="18" height="13" rx="2.5"></rect><path d="M8 7V5h8v2"></path>', 'rec': '<path d="M6 3h9l3 3v15H6z"></path><path d="m9 13 2 2 4-4"></path>',
     'port': '<rect x="3" y="4" width="18" height="14" rx="2.5"></rect><path d="M8 21h8M12 18v3"></path>', 'sk': '<path d="m12 3 2.5 5.2 5.5.8-4 3.9 1 5.6L12 16l-5 2.5 1-5.6-4-3.9 5.5-.8z"></path>'}
def ico(k, w=18): return svg(I[k], w, 1.9)

# ---------------------------------------------------------------- hero
rep('<h1 class="pd-h1">Become a Data Analyst</h1>',
    '<div class="pd4-tags"><span class="ds-tag blue lg"><i class="pd4-dot"></i>Gold Validated</span><span class="ds-tag line lg">CEI 92%s</span><span class="pd4-rt"><b>★ 4.8</b> (2.4k path reviews)</span></div>\n<h1 class="pd-h1">Become a Data Analyst</h1>' % tip(
        'Credalio Excellence Index: how well this path is built, scored by independent validators out of 100.'))
rep('<span class="pd-note">12,480 learners on this path</span>',
    '<button class="ds-ghost sm" type="button">' + SHARE + 'Share</button><a class="ds-ghost sm" href="#">' + nova_av('sm') + 'Check my readiness</a>'
    '<span class="pd-note">Lead creator <b>Amara Okafor</b> · 12,480 learners</span>')

# ---------------------------------------------------------------- before the route
AUD = [('Complete beginners', 'Start without any analytics experience.'), ('Career switchers', 'Move into a data role from another field.')]
ROLES = [('Junior Data Analyst', 'Clean data, run queries and answer questions from the business.'), ('Reporting Analyst', 'Build the weekly and monthly reports teams rely on.'),
         ('BI Assistant', 'Maintain dashboards and help people find what they need.'), ('Data Operations Associate', 'Keep data accurate, complete and ready to use.')]
BEFORE = '''<section class="pd4-sec" aria-labelledby="pd4-js">
<h2 id="pd4-js" class="pd-h2">From where you are to where you want to be</h2>
<div class="pd4-snap">
<div class="pd4-end"><span class="pd4-k">Your starting point</span><b>Complete beginner</b><span>Basic computer and spreadsheet use. No analytics experience.</span></div>
<div class="pd4-mid" aria-hidden="true"><span class="pd4-line"></span><span class="pd4-chip">5 stages · 8 courses · 4 projects</span><span class="pd4-chip">6–8 months</span></div>
<div class="pd4-end pd4-to"><span class="pd4-k">Your destination</span><b>Data Analyst</b><span>Analyse data, build dashboards and present evidence-based insights.</span></div>
</div>
</section>

<section class="pd4-sec" aria-labelledby="pd4-ab">
<h2 id="pd4-ab" class="pd-h2">About this path</h2>
<p class="pd4-p">This path takes you from tidy spreadsheets to SQL, data visualisation and analysis in a business setting. Every stage pairs validated courses with practice, and the projects build into a portfolio that shows you’re ready for entry-level analytical work.</p>
</section>

<section class="pd4-sec" aria-labelledby="pd4-fr">
<h2 id="pd4-fr" class="pd-h2">Is this path right for you?</h2>
<div class="pd4-g2">%s</div>
<div class="pd4-req">
<div><span class="pd4-k">You’ll need</span><b>Basic computer use and simple spreadsheets</b></div>
<div><span class="pd4-k">Helpful, not required</span><b>Formulas, charts and everyday maths</b></div>
</div>
<div class="pd4-rdy nova-card">%s<p><b>Already know some of this?</b> Nova, your AI Coach, checks whether you can start at a later stage. Skipping a stage never awards its completion, credentials or project evidence.</p><a class="ds-ghost sm" href="#">Check my readiness</a></div>
</section>

<section class="pd4-sec" aria-labelledby="pd4-out">
<h2 id="pd4-out" class="pd-h2">Where it can lead</h2>
<div class="pd4-roles">%s</div>
<p class="pd4-fine">This path builds skills relevant to these roles. Getting a job also depends on things outside the path.</p>
</section>

''' % (''.join('<div class="pd4-c"><span class="pd4-ck">%s</span><b>%s</b><span>%s</span></div>' % (ck(12), t, d) for t, d in AUD), nova_av(),
       ''.join('<div class="pd4-c"><span class="pd4-ic">%s</span><b>%s</b><span>%s</span></div>' % (ico('role'), t, d) for t, d in ROLES))
rep('<section aria-labelledby="pd-r">', BEFORE + '<section aria-labelledby="pd-r">')

# ---------------------------------------------------------------- after the route
SK = [('SQL', 2), ('Spreadsheets', 3), ('Data visualisation', 2), ('Statistics', 1), ('Explaining insights', 2)]
LV = ['', 'Foundational', 'Intermediate', 'Advanced', 'Expert']
MS = [('Finish the required learning', 'The courses and activities in each stage.'), ('Show your skills', 'Pass the assessments and submit the projects.'),
      ('Reach each milestone', 'Meet a stage’s requirements before moving on.'), ('Complete your portfolio', 'Publish your final evidence.')]
ACH = [('rec', 'Path completion record', 'Issued when all 5 stages are complete. It isn’t a professional certification.'), ('port', 'Portfolio evidence', '3 case studies and a capstone, ready to share.'),
       ('sk', 'Verified skills', 'Skills backed by assessed evidence, in your Digital Backpack.')]
ACC = [('dlp', '3,800 DLP', 'With your plan', 'Each course uses DLP as you take it. You get 30 days to revise after finishing a course.'),
       ('cr', 'From 400 Credits', 'Buy courses one by one', 'Own each course you buy for life, including its updates.'),
       ('cr', '7,600 Credits', 'Path package', 'Own all 8 courses in the path for life, with their future updates.')]
TEAM = [('AO', 'Amara Okafor', 'Lead creator', 'Senior Data Analyst · designed the route and stages 1–3'), ('DK', 'Daniel Kim', 'Co-creator', 'Designed stages 4 and 5'),
        ('+5', '5 course creators', 'Contributors', 'Each is credited on their own course'), ('NU', 'Northgate University', 'Affiliated institution', 'Co-created the path')]
REV = [('“I came from retail management with no data background. The stages made it feel possible, and the capstone got me my first interview.”', 'Grace A.', 'Now a junior analyst'),
       ('“What I liked most: I could skip the spreadsheet stage after Nova’s check, and still had to prove it.”', 'Tom H.', 'Career switcher')]
FAQS = [('How long does the path take?', 'Most learners finish in 6 to 8 months at about 5 hours a week. If Nova confirms you already know a stage, you can start later.'),
        ('Is the professional certification included?', 'The preparation course is part of stage 5. The certification itself is assessed separately and has its own 150 Credits fee.'),
        ('Can I take the courses on their own?', 'Yes. Every course in the path has its own page. Courses you finish count toward the path.'),
        ('What does the path package include?', 'All 8 courses, owned for life with their future updates. It doesn’t include the certification fee or other paths.')]
AFTER = '''<section class="pd4-sec" aria-labelledby="pd4-sk">
<div class="pd-sh"><h2 id="pd4-sk" class="pd-h2">Skills you’ll build%s</h2><span class="pd4-sm">Target level by the end</span></div>
<div class="pd4-sks">%s</div>
<p class="pd4-fine">Finishing content isn’t proof on its own. A level only counts as verified after assessed evidence.</p>
</section>

<section class="pd4-sec" aria-labelledby="pd4-ms">
<h2 id="pd4-ms" class="pd-h2">How you’ll show progress</h2>
<ol class="pd4-ms">%s</ol>
<div class="pd4-cert"><span class="ds-tag line">Optional · assessed and charged separately</span><b>Professional Certificate in Data Analysis</b><span>Finishing the path doesn’t award the certification. It has its own eligibility check, assessment and a 150 Credits fee.</span><a class="ds-link" href="CertDetail.dc.html">View the certification →</a></div>
</section>

<section class="pd4-sec" aria-labelledby="pd4-ac">
<h2 id="pd4-ac" class="pd-h2">What you’ll have at the end</h2>
<div class="pd4-g3">%s</div>
</section>

<section class="pd4-sec" aria-labelledby="pd4-pr">
<div class="pd-sh"><h2 id="pd4-pr" class="pd-h2">Ways to access it</h2><a class="ds-link" href="Pricing.dc.html">Compare plans →</a></div>
<div class="pd4-g3 pd4-acc">%s</div>
<p class="pd4-fine">DLP and Credits are separate routes, not one price converted. The certification fee is always separate.</p>
</section>

<section class="pd4-sec" aria-labelledby="pd4-tm">
<h2 id="pd4-tm" class="pd-h2">The people behind this path</h2>
<div class="pd4-team">%s</div>
</section>

<section class="pd4-sec" aria-labelledby="pd4-rv">
<h2 id="pd4-rv" class="pd-h2">What learners say</h2>
<div class="pd4-revs"><div class="pd4-score"><b>4.8</b><span class="pd4-stars" aria-label="4.8 out of 5">★★★★★</span><span>410 verified path reviews</span><em>Path reviews only. Course ratings aren’t carried over.</em></div>%s</div>
</section>

<section class="pd4-sec" aria-labelledby="pd4-fq">
<h2 id="pd4-fq" class="pd-h2">Questions learners ask</h2>
<div class="pd4-fqs"><sc-for list="{{faqs}}" as="f" hint-placeholder-count="4"><div class="pd4-f {{f.cls}}"><button class="pd4-fh" type="button" aria-expanded="{{f.exp}}" onClick="{{f.toggle}}"><span>{{f.q}}</span>%s</button><sc-if value="{{f.open}}" hint-placeholder-val="{{ false }}"><p>{{f.a}}</p></sc-if></div></sc-for></div>
</section>
''' % (tip('Levels on the Credalio scale: Foundational, Intermediate, Advanced, Expert.'),
       ''.join('<div class="pd4-skr"><span class="pd4-skn">%s</span><span class="pd4-skb" aria-hidden="true">%s</span><span class="pd4-skl">%s</span></div>' % (n, ''.join('<i class="%s"></i>' % ('on' if k <= l else '') for k in range(1, 5)), LV[l]) for n, l in SK),
       ''.join('<li><span class="pd4-msn">%d</span><b>%s</b><span>%s</span></li>' % (i + 1, t, d) for i, (t, d) in enumerate(MS)),
       ''.join('<div class="pd4-c"><span class="pd4-ic">%s</span><b>%s</b><span>%s</span></div>' % (ico(k), t, d) for k, t, d in ACH),
       ''.join('<div class="pd4-c pd4-a%s"><span class="pd4-k">%s</span><span class="pd4-pv">%s<b>%s</b></span><span>%s</span></div>' % (
           ' pd4-pkg' if t == 'Path package' else '', t, '<span class="dlp-c" aria-hidden="true"></span>' if k == 'dlp' else '<i class="cr-c" aria-hidden="true">C</i>', v, d) for k, v, t, d in ACC),
       ''.join('<div class="pd4-p1"><span class="pd4-av">%s</span><div><span class="pd4-k">%s</span><b>%s</b><span>%s</span></div></div>' % (a, r, n, d) for a, n, r, d in TEAM),
       ''.join('<figure class="pd4-rev"><blockquote>%s</blockquote><figcaption><b>%s</b> · %s</figcaption></figure>' % q for q in REV), CHEV)
# insert after the route section (its end is the first </section> after id="pd-r")
k = s.index('aria-labelledby="pd-r"'); e = s.index('</section>', k) + len('</section>')
s = s[:e] + '\n\n' + AFTER + s[e:]

# ---------------------------------------------------------------- panel: path package
rep('<div class="pd-cov">', '<div class="pd4-pk"><i class="cr-c" aria-hidden="true">C</i><span>Or own the whole path: <b>7,600 Credits</b>%s</span></div>\n<div class="pd-cov">' % tip(
    'The path package buys all 8 courses for life, with future updates. The certification fee is separate.'))

# ---------------------------------------------------------------- JS
rep("this.state = { known: {}, plan: 'Free', saved: false };", "this.state = { known: {}, plan: 'Free', saved: false, faq: 0 };")
rep("toggleSave: function () { self.setState({ saved: !S.saved }); }\n    };",
    "toggleSave: function () { self.setState({ saved: !S.saved }); },\n      faqs: FAQS_.map(function (f, i) { var o = S.faq === i; return { q: f[0], a: f[1], open: o, exp: o ? 'true' : 'false', cls: o ? 'on' : '', toggle: function () { self.setState({ faq: o ? -1 : i }); } }; })\n    };".replace('FAQS_', json.dumps(FAQS, ensure_ascii=False)))

# ---------------------------------------------------------------- CSS
need = [l.strip() for l in kit.KIT_CSS.split('\n') if re.match(r'\.(ds-tag\.(blue|line|lg)|cr-c|nv-av)[.:{,\s]', l.strip())]
CSS = '\n'.join(need) + '\n.nova-card{background:#FFFFFF url(' + kit.NOVA_BG + r''') center / cover no-repeat}
.pd4-tags{display:flex;align-items:center;flex-wrap:wrap;gap:8px}
.pd4-dot{width:8px;height:8px;border-radius:50%;background:#C8961E;font-style:normal}
.pd4-rt{font-size:14px;color:#5B6582;margin-left:4px}
.pd4-rt b{font-weight:600;color:#0B1433}
.pd-note b{font-weight:600;color:#0B1433}
.pd-acts{flex-wrap:wrap}
.pd-acts .ds-ghost{height:40px;padding:0 16px;font-size:14px}
.pd-acts .nv-av{width:24px;height:24px}
.pd4-sec{display:flex;flex-direction:column;gap:18px;padding-bottom:48px}
section[aria-labelledby="pd-r"]{padding-bottom:56px}
.pd4-sec > .pd-h2,.pd4-sec > .pd-sh{margin-bottom:2px}
.pd4-k{font-size:12px;font-weight:500;color:#8A93AD}
.pd4-sm{font-size:14px;color:#5B6582}
.pd4-p{margin:0;max-width:720px;font-size:16px;line-height:1.65;color:#3A4566}
.pd4-fine{margin:0;font-size:13px;line-height:1.5;color:#8A93AD}
.pd4-snap{display:grid;grid-template-columns:minmax(0,1fr) 200px minmax(0,1fr);align-items:stretch;border:1.5px solid #E6EAF3;border-radius:22px;overflow:hidden}
.pd4-end{display:flex;flex-direction:column;gap:4px;padding:22px}
.pd4-end b{font-size:20px;font-weight:600;letter-spacing:-.3px;color:#0B1433}
.pd4-end > span:last-child{font-size:14px;line-height:1.5;color:#5B6582}
.pd4-to{background:linear-gradient(160deg,#F5F8FF,#EAF0FF)}
.pd4-mid{position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;padding:16px}
.pd4-line{position:absolute;left:0;right:0;top:50%;height:2px;background:linear-gradient(90deg,#C9D7FA,#1652F0)}
.pd4-chip{position:relative;z-index:1;padding:5px 12px;border-radius:999px;background:#FFFFFF;border:1.5px solid #DCE5FB;font-size:12.5px;font-weight:500;color:#0E3BB8;white-space:nowrap}
.pd4-g2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.pd4-g3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.pd4-c{display:flex;flex-direction:column;gap:6px;padding:18px 20px;border-radius:18px;border:1.5px solid #E6EAF3;background:#FFFFFF}
.pd4-c b{font-size:16px;font-weight:600;color:#0B1433}
.pd4-c > span:last-child{font-size:14px;line-height:1.5;color:#5B6582}
.pd4-ck{width:24px;height:24px;border-radius:50%;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center;margin-bottom:4px}
.pd4-ic{width:36px;height:36px;border-radius:11px;background:#EAF0FF;color:#1652F0;display:flex;align-items:center;justify-content:center;margin-bottom:4px}
.pd4-req{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));border:1.5px solid #E6EAF3;border-radius:18px;overflow:hidden}
.pd4-req > div{display:flex;flex-direction:column;gap:4px;padding:16px 20px}
.pd4-req > div + div{border-left:1px solid #EEF1F7}
.pd4-req b{font-size:15px;font-weight:500;color:#0B1433}
.pd4-rdy{display:flex;align-items:center;gap:16px;padding:18px 20px;border-radius:20px;border:1.5px solid #DCE5FB}
.pd4-rdy p{margin:0;flex:1;font-size:14.5px;line-height:1.5;color:#3A4566}
.pd4-rdy p b{font-weight:600;color:#0B1433}
.pd4-rdy .ds-ghost{flex-shrink:0}
.pd4-roles{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.pd4-sks{display:flex;flex-direction:column;border:1.5px solid #E6EAF3;border-radius:20px;padding:6px 22px}
.pd4-skr{display:grid;grid-template-columns:minmax(0,1fr) 220px 110px;align-items:center;gap:20px;min-height:56px}
.pd4-skr + .pd4-skr{border-top:1px solid #EEF1F7}
.pd4-skn{font-size:15px;font-weight:500;color:#0B1433}
.pd4-skb{display:grid;grid-template-columns:repeat(4,1fr);gap:4px}
.pd4-skb i{height:8px;border-radius:4px;background:#EEF1F7}
.pd4-skb i.on{background:#1652F0}
.pd4-skl{font-size:13px;font-weight:500;color:#0E3BB8;text-align:right}
.pd4-ms{margin:0;padding:0;list-style:none;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.pd4-ms li{display:flex;flex-direction:column;gap:6px;padding:18px;border-radius:18px;background:#F5F8FF}
.pd4-msn{width:28px;height:28px;border-radius:50%;background:#FFFFFF;border:1.5px solid #C9D7FA;color:#1652F0;font-size:13px;font-weight:600;display:flex;align-items:center;justify-content:center;margin-bottom:4px}
.pd4-ms b{font-size:15px;font-weight:600;color:#0B1433}
.pd4-ms li > span:last-child{font-size:13.5px;line-height:1.45;color:#5B6582}
.pd4-cert{display:flex;flex-direction:column;align-items:flex-start;gap:6px;padding:20px 22px;border-radius:18px;border:1.5px dashed #CBD7F5}
.pd4-cert b{font-size:16px;font-weight:600;color:#0B1433;margin-top:4px}
.pd4-cert > span:not(.ds-tag){font-size:14px;line-height:1.5;color:#5B6582}
.pd4-pv{display:flex;align-items:center;gap:8px}
.pd4-pv b{font-size:22px !important;letter-spacing:-.4px}
.pd4-pv .dlp-c,.pd4-pv .cr-c{width:22px;height:22px;font-size:11px}
.pd4-pkg{border-color:#1652F0;background:linear-gradient(180deg,#F5F8FF,#FFFFFF)}
.pd4-team{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.pd4-p1{display:flex;gap:14px;padding:16px 18px;border-radius:18px;border:1.5px solid #E6EAF3}
.pd4-p1 > div{display:flex;flex-direction:column;gap:2px;min-width:0}
.pd4-p1 b{font-size:15.5px;font-weight:600;color:#0B1433}
.pd4-p1 > div > span:last-child{font-size:13.5px;line-height:1.45;color:#5B6582}
.pd4-av{width:44px;height:44px;border-radius:50%;background:#EAF0FF;color:#0E3BB8;font-size:14px;font-weight:600;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.pd4-revs{display:grid;grid-template-columns:220px minmax(0,1fr) minmax(0,1fr);gap:12px}
.pd4-score{display:flex;flex-direction:column;gap:4px;padding:20px;border-radius:18px;background:#F5F8FF}
.pd4-score b{font-size:40px;font-weight:600;letter-spacing:-1px;line-height:1}
.pd4-stars{color:#E3A008;letter-spacing:2px}
.pd4-score span:last-of-type{font-size:13px;color:#5B6582}
.pd4-score em{margin-top:6px;font-style:normal;font-size:12px;line-height:1.4;color:#8A93AD}
.pd4-rev{margin:0;display:flex;flex-direction:column;justify-content:space-between;gap:12px;padding:20px;border-radius:18px;border:1.5px solid #E6EAF3}
.pd4-rev blockquote{margin:0;font-size:14.5px;line-height:1.55;color:#0B1433}
.pd4-rev figcaption{font-size:13px;color:#5B6582}
.pd4-rev b{font-weight:600;color:#0B1433}
.pd4-fqs{border:1.5px solid #E6EAF3;border-radius:20px;overflow:hidden}
.pd4-f + .pd4-f{border-top:1px solid #EEF1F7}
.pd4-fh{width:100%;display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:58px;padding:0 22px;border:0;background:#FFFFFF;font-family:inherit;font-size:15.5px;font-weight:500;color:#0B1433;text-align:left;cursor:pointer}
.pd4-chev{flex-shrink:0;color:#5B6582;transition:transform .2s ease}
.pd4-f.on .pd4-chev{transform:rotate(180deg)}
.pd4-f p{margin:0;padding:0 22px 18px;font-size:14.5px;line-height:1.6;color:#3A4566}
.pd4-pk{display:flex;align-items:center;gap:10px;padding:12px 14px;border-radius:14px;background:#F5F8FF;font-size:13.5px;color:#3A4566}
.pd4-pk b{font-weight:600;color:#0B1433}
@media (max-width: 1180px){.pd4-ms{grid-template-columns:repeat(2,minmax(0,1fr))}.pd4-revs{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}.pd4-score{grid-column:1 / -1}}
@media (max-width: 760px){
.pd4-sec{gap:14px;padding-bottom:40px}
.pd4-p{font-size:15px}
.pd4-snap{grid-template-columns:minmax(0,1fr)}
.pd4-mid{flex-direction:row;padding:12px}
.pd4-line{left:50%;right:auto;top:0;bottom:0;width:2px;height:auto;background:linear-gradient(180deg,#C9D7FA,#1652F0)}
.pd4-end{padding:16px 18px}
.pd4-end b{font-size:18px}
.pd4-g2,.pd4-g3,.pd4-roles,.pd4-team,.pd4-revs{grid-template-columns:minmax(0,1fr);gap:10px}
.pd4-req{grid-template-columns:minmax(0,1fr)}
.pd4-req > div + div{border-left:0;border-top:1px solid #EEF1F7}
.pd4-rdy{display:grid;grid-template-columns:36px minmax(0,1fr);gap:12px;align-items:start}
.pd4-rdy .ds-ghost{grid-column:1 / -1}
.pd4-sks{padding:4px 16px}
.pd4-skr{grid-template-columns:minmax(0,1fr) auto;row-gap:8px;padding:12px 0;min-height:0}
.pd4-skb{grid-column:1 / -1;grid-row:2}
.pd4-ms{grid-template-columns:minmax(0,1fr);gap:8px}
.pd4-ms li{display:grid;grid-template-columns:28px minmax(0,1fr);column-gap:12px;padding:14px 16px}
.pd4-msn{grid-row:span 2;margin:0}
.pd4-revs{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;margin:0 -20px;padding:0 20px 4px;scrollbar-width:none;scroll-padding:0 20px}
.pd4-revs > *{flex:0 0 82%;scroll-snap-align:start;box-sizing:border-box}
.pd4-fh{padding:14px 18px;min-height:0;font-size:15px}
.pd4-f p{padding:0 18px 16px}
.pd-acts .ds-ghost{height:40px}
}
'''
i = s.find('</style>'); s = s[:i] + CSS + s[i:]
open(P, 'w').write(s); print('patched PathDetail')
