# Learning access (ACC-001..004): course needs more DLP (Free / Pro), zero DLP, low DLP during a lesson.
# Usage: python3 accgen.py  -> writes design/canvas3/project/Access.dc.html (prop kind)
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from kit import KIT_CSS, btn, tip, coin, ck, opts
from shell import BASE_CSS

OUT = os.path.join(HERE, '../../canvas3/project/Access.dc.html')

def ic(d, s=20, sw=1.8):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (s, s, sw, d)

BACK = ic('<path d="M19 12H5"></path><path d="m11 18-6-6 6-6"></path>', 16, 2.2)
LINKS = ['Explore learning', 'Career paths', 'Certifications', 'Pricing', 'For creators', 'For institutions']

CSS = r'''.sx-dlp{height:36px;padding:0 12px 0 8px;border-radius:999px;background:#F5F8FF;border:1px solid #DCE5FB;display:flex;align-items:center;gap:8px;font-size:14px;font-weight:600;color:#0B1433;text-decoration:none;white-space:nowrap}
.sx-dlp.low{background:#FFFAEB;border-color:#F4D98E;color:#8A5A00}
.ac-avl{font-weight:500;color:#5B6582}
.sx-av{width:40px;height:40px;border-radius:999px;background:#DCE5FB;color:#1652F0;text-decoration:none;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:600}
.ac-root{position:relative;min-height:100vh;font-family:'Google Sans','Google Sans Text','Helvetica Neue',system-ui,sans-serif;color:#0B1433;background:#FFFFFF;overflow:hidden}
.ac-glow{position:absolute;left:50%;top:-260px;width:1100px;height:560px;transform:translateX(-50%);border-radius:50%;pointer-events:none;filter:blur(10px)}
.ac-glow.am{background:radial-gradient(closest-side,rgba(244,201,110,.32),rgba(244,201,110,0))}
.ac-glow.cb{background:radial-gradient(closest-side,rgba(22,82,240,.16),rgba(22,82,240,0))}
.ac-root > header,.ac-main{position:relative}
.ac-main{max-width:1100px;margin:0 auto;padding:12px 24px 64px;box-sizing:border-box}
.ac-back{display:inline-flex;align-items:center;gap:8px;height:40px;padding:0 14px 0 10px;margin-left:-10px;border-radius:999px;color:#3A4566;font-size:14px;font-weight:500;text-decoration:none}
.ac-back:hover{background:#F5F8FF;color:#0B1433}
.ac-out{display:flex;flex-direction:column;align-items:center;text-align:center;max-width:820px;margin:8px auto 0}
.ac-h1{margin:14px 0 0;font-size:clamp(30px,3vw,42px);line-height:1.12;font-weight:600;letter-spacing:-.03em;text-wrap:balance}
.ac-sub{margin:12px 0 0;max-width:560px;font-size:16px;line-height:1.55;color:#4A5578;text-wrap:balance}
.ac-need{width:100%;max-width:640px;margin-top:28px;display:flex;align-items:center;justify-content:space-between;gap:20px;padding:16px 20px;text-align:left;box-sizing:border-box}
.ac-c{display:flex;align-items:center;gap:14px;min-width:0}
.ac-th{width:48px;height:48px;border-radius:14px;flex-shrink:0;background:linear-gradient(150deg,#1C3AA8,#0B1433)}
.ac-th.py{background:linear-gradient(150deg,#7FA4FF,#4C7DFF)}
.ac-c small{display:block;font-size:12.5px;color:#5B6582}
.ac-c b{display:block;margin-top:2px;font-size:15.5px;font-weight:600}
.ac-n{display:flex;flex-shrink:0}
.ac-n div{display:flex;flex-direction:column;gap:3px;padding:0 16px}
.ac-n div + div{border-left:1px solid #EEF1F7}
.ac-n span{font-size:12.5px;color:#5B6582;white-space:nowrap}
.ac-n b{display:flex;align-items:center;gap:6px;font-size:16px;font-weight:600}
.ac-n .am b{color:#8A5A00}
.ac-saved{width:100%;max-width:560px;margin-top:28px;display:flex;align-items:center;gap:14px;padding:14px 18px;text-align:left;box-sizing:border-box}
.ac-saved .ac-ic{width:44px;height:44px;border-radius:14px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.ac-saved div{flex:1;min-width:0}
.ac-saved b{display:block;font-size:15px;font-weight:600}
.ac-saved small{display:block;margin-top:2px;font-size:13px;color:#5B6582}
.ac-opts{width:100%;margin-top:36px}
.ac-opts.n2{max-width:680px}
.ac-more{margin-top:24px}
.ko-disc .ac-x{font-size:28px;font-weight:700;line-height:1}
.ac-les{display:grid;grid-template-columns:280px minmax(0,1fr);gap:24px;margin-top:8px}
.ac-toc{padding:20px 18px;align-self:start}
.ac-toc small{display:block;padding:0 6px 10px;font-size:12.5px;font-weight:600;color:#8A93AD}
.ac-toc ol{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:2px}
.ac-toc li{display:flex;align-items:center;gap:10px;min-height:40px;padding:0 8px;border-radius:12px;font-size:14px;color:#3A4566}
.ac-toc li i{width:22px;height:22px;border-radius:999px;box-sizing:border-box;border:1.5px solid #CBD3E6;display:flex;align-items:center;justify-content:center;flex-shrink:0;color:#FFFFFF;font-style:normal;font-size:11px;font-weight:600}
.ac-toc li.d i{background:#0F6B45;border-color:#0F6B45}
.ac-toc li.n{background:#EAF0FF;color:#0E3BB8;font-weight:600}
.ac-toc li.n i{background:#1652F0;border-color:#1652F0}
.ac-art{padding:34px 40px 30px}
.ac-art .ac-k{font-size:13.5px;font-weight:500;color:#1652F0}
.ac-art h1{margin:8px 0 0;font-size:34px;line-height:1.15;font-weight:600;letter-spacing:-.02em}
.ac-art p{margin:16px 0 0;max-width:640px;font-size:16.5px;line-height:1.65;color:#3A4566}
.ac-code{margin:20px 0 0;padding:18px 20px;border-radius:14px;background:#0B1433;color:#DCE5FB;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:14px;line-height:1.7;overflow-x:auto}
.ac-code b{color:#9DB8F7;font-weight:600}
.ac-art-f{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-top:30px;padding-top:22px;border-top:1px solid #EEF1F7}
.ac-toast{position:fixed;left:50%;bottom:28px;z-index:20;transform:translateX(-50%);width:min(680px,calc(100% - 32px));box-sizing:border-box;display:flex;align-items:center;gap:14px;padding:14px 16px 14px 18px;border-radius:18px;background:#FFFFFF;border:1.5px solid #F4D98E;box-shadow:0 30px 60px -24px rgba(11,20,51,.35),0 0 0 6px rgba(244,217,142,.25);animation:acUp .45s cubic-bezier(.2,.8,.2,1) both}
.ac-ti{width:30px;height:30px;border-radius:999px;background:#B97A10;color:#FFFFFF;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:16px;font-weight:700}
.ac-toast div:nth-child(2){flex:1;min-width:0}
.ac-toast b{display:block;font-size:15px;font-weight:600}
.ac-toast p{margin:2px 0 0;font-size:14px;line-height:1.45;color:#4A5578;text-wrap:pretty}
.ac-toast-a{display:flex;align-items:center;gap:16px;flex-shrink:0}
@keyframes acUp{from{opacity:0;transform:translate(-50%,16px)}to{opacity:1;transform:translate(-50%,0)}}
@media (prefers-reduced-motion: reduce){.ac-toast{animation:none}}
@media (max-width: 960px){.ac-les{grid-template-columns:minmax(0,1fr)}.ac-toc{display:none}}
@media (max-width: 760px){
.ac-main{padding:4px 16px 120px}
.ac-avl{display:none}
.ac-out{margin-top:4px}
.ac-h1{font-size:26px}
.ac-sub{font-size:15px}
.ac-need{flex-direction:column;align-items:stretch;gap:14px;padding:14px 16px}
.ac-n{justify-content:space-between}
.ac-n div{padding:0 12px 0 0;flex:1}
.ac-n div + div{padding-left:12px}
.ac-opts{margin-top:28px;text-align:left}
.ac-art{padding:22px 18px 20px;margin:0 -16px;border-radius:0;border-left:0;border-right:0}
.ac-art h1{font-size:26px}
.ac-art p{font-size:15.5px}
.ac-code{font-size:13px;padding:14px 16px}
.ac-art-f{flex-direction:column-reverse;align-items:stretch}
.ac-art-f .ds-btn{justify-content:space-between}
.ac-art-f .ds-link{justify-content:center}
.ac-toast{bottom:12px;flex-wrap:wrap;align-items:flex-start;padding:14px}
.ac-toast div:nth-child(2){flex:1 1 calc(100% - 44px)}
.ac-toast-a{width:100%;justify-content:space-between;padding-left:44px;box-sizing:border-box}
}
'''

EXCL = '<span class="ac-x" aria-hidden="true">!</span>'
ARR_R = ic('<path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path>', 26, 2.6)

HEADER = '''<header class="sx-nav">
<a class="sx-logo" href="Dashboard.dc.html" aria-label="Credalio home"><span class="sx-mark" aria-hidden="true"></span><span class="sx-word" aria-hidden="true"></span></a>
<nav class="sx-links" aria-label="Main">
''' + '\n'.join('<a class="sx-link%s" href="%s"%s>%s</a>' % (' sx-link-on' if l == 'Explore learning' else '', 'Explore.dc.html' if l == 'Explore learning' else '#', ' aria-current="page"' if l == 'Explore learning' else '', l) for l in LINKS) + '''
</nav>
<div style="display: flex; align-items: center; gap: 8px; flex-shrink: 0">
<a class="sx-dlp {{pillCls}}" href="Usage.dc.html" aria-label="{{pill}} DLP available. View usage">''' + coin() + '''<b style="font-weight: 600">{{pill}}<span class="ac-avl"> available</span></b></a>
<a class="sx-av" href="Dashboard.dc.html" aria-label="Your dashboard">AO</a>
<button class="sx-menu" type="button" aria-label="Open menu"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"></path></svg></button>
</div>
</header>'''

MARKUP = '''<div class="ac-root">
<div class="ac-glow {{glow}}" aria-hidden="true"></div>
''' + HEADER + '''
<main class="ac-main">
<sc-if value="{{isOut}}" hint-placeholder-val="{{ true }}">
<a class="ac-back" href="CourseDetail-Learner.dc.html">''' + BACK + '''<span>{{backT}}</span></a>
<div class="ac-out ko-v {{tone}}">
<div class="ko-emb ko-v {{tone}}" aria-hidden="true"><span class="ko-halo"></span><span class="ko-disc"><sc-if value="{{isZero}}" hint-placeholder-val="{{ false }}">''' + ARR_R + '''</sc-if><sc-if value="{{isCourse}}" hint-placeholder-val="{{ true }}">''' + EXCL + '''</sc-if></span></div>
<span class="ko-pill">{{koPill}}</span>
<h1 class="ac-h1">{{h1}}</h1>
<p class="ac-sub">{{sub}}</p>
<sc-if value="{{isCourse}}" hint-placeholder-val="{{ true }}">
<div class="ds-card ac-need"><div class="ac-c"><span class="ac-th {{thCls}}" aria-hidden="true"></span><div><small>Validated course</small><b>{{course}}</b></div></div>
<div class="ac-n"><div><span>Needs</span><b>''' + coin() + '''{{need}}</b></div><div><span>You have</span><b>''' + coin() + '''{{have}}</b></div><div class="am"><span>Still needed</span><b>''' + coin() + '''{{short}}</b></div></div></div>
</sc-if>
<sc-if value="{{isZero}}" hint-placeholder-val="{{ false }}">
<div class="ds-card ac-saved"><span class="ac-ic">''' + ic('<path d="M2.5 5.5C5 4 8.5 4 12 6c3.5-2 7-2 9.5-.5V19c-2.5-1.5-6-1.5-9.5.5-3.5-2-7-2-9.5-.5z"></path><path d="M12 6v13.5"></path>', 22) + '''</span><div><b>SQL for Data Analysis · Lesson 6</b><small>You’ll pick up right here.</small></div><span class="ds-tag green">Saved</span></div>
</sc-if>
<div class="ac-opts {{optsCls}}">''' + opts() + '''</div>
<a class="ds-link ac-more" href="{{moreHref}}">{{more}}</a>
</div>
</sc-if>
<sc-if value="{{isLow}}" hint-placeholder-val="{{ false }}">
<a class="ac-back" href="CourseDetail-Learner.dc.html">''' + BACK + '''<span>SQL for Data Analysis</span></a>
<div class="ac-les">
<aside class="ds-card ac-toc" aria-label="Lessons"><small>SQL for Data Analysis</small><ol>
<li class="d"><i>''' + ck(11, 3.4) + '''</i>Why SQL</li><li class="d"><i>''' + ck(11, 3.4) + '''</i>SELECT and WHERE</li><li class="d"><i>''' + ck(11, 3.4) + '''</i>Sorting results</li><li class="n" aria-current="step"><i>4</i>GROUP BY basics</li><li><i></i>Filtering groups</li><li><i></i>Practice set</li>
</ol></aside>
<article class="ds-card ac-art">
<span class="ac-k">Lesson 4 of 6</span>
<h1>GROUP BY basics</h1>
<p>GROUP BY collects rows that share a value, so you can summarise each group with COUNT, SUM or AVG.</p>
<pre class="ac-code"><b>SELECT</b> region, <b>COUNT</b>(*) <b>AS</b> orders
<b>FROM</b> sales
<b>GROUP BY</b> region;</pre>
<p>Each region becomes one row, and COUNT tells you how many orders it had. Next, you’ll filter those groups with HAVING.</p>
<div class="ac-art-f"><a class="ds-link" href="#">Previous lesson</a>''' + btn('Next lesson', '#') + '''</div>
</article>
</div>
<sc-if value="{{showToast}}" hint-placeholder-val="{{ true }}">
<div class="ac-toast" role="status"><span class="ac-ti" aria-hidden="true">!</span><div><b>Your allowance is running low.</b><p>You have 120 DLP, and your next lesson uses about 200.</p></div><div class="ac-toast-a"><button type="button" class="ds-link" onClick="{{dismiss}}">Continue for now</button><a class="ds-ghost sm" href="#">Get more DLP</a></div></div>
</sc-if>
</sc-if>
</main>
</div>'''

JS = r'''
class Component extends DCLogic {
  constructor(props) { super(props); this.state = { toast: true }; }
  renderVals() {
    var self = this, k = (this.props || {}).kind || 'freeCourse';
    var D = {
      freeCourse: { course: 'SQL for Data Analysis', th: '', need: 500, have: 200, h1: 'You need 300 more DLP for this course.', sub: 'Your progress is saved, so nothing is lost while you decide.', more: 'Compare plans', moreHref: '#',
        opts: [['Upgrade to Basic', '2,000 DLP every month. Covers this course and what comes next.', 'Upgrade', 'Chk-003.dc.html', 1], ['Top up instead', 'Stay on Free and add just what this course needs.', 'Add 300 DLP', '#', 0]] },
      proCourse: { course: 'Advanced Analytics with Python', th: 'py', need: 400, have: 150, h1: 'You need 250 more DLP for this course.', sub: 'You’re on Pro, so there’s no bigger plan. Add what you need, or wait for your refresh.', more: 'See my usage', moreHref: 'Usage.dc.html',
        opts: [['Top up now', 'Added straight away. Your plan stays the same.', 'Add 250 DLP', '#', 1], ['Wait for your refresh', 'Your next 6,000 DLP arrives on 12 October. We’ll remind you.', 'Remind me', '#', 0]] },
      zero: { h1: 'You’re ready for the next step.', sub: 'You’ve used this month’s learning allowance. Your progress is saved exactly where you stopped.', more: 'Explore learning that needs no DLP', moreHref: 'Explore.dc.html',
        opts: [['Upgrade to Pro', '6,000 DLP every month, for learning at full pace.', 'Upgrade', '#', 1], ['Top up instead', 'Keep Basic and add only what you need.', 'Add DLP', '#', 0], ['Wait for your refresh', 'Your next 2,000 DLP arrives on 12 October.', 'Remind me', '#', 0]] }
    };
    var d = D[k] || D.freeCourse, isCourse = k === 'freeCourse' || k === 'proCourse', f = function (n) { return n.toLocaleString('en-GB'); };
    var pill = { freeCourse: 200, proCourse: 150, zero: 0, low: 120 }[k];
    return {
      isOut: k !== 'low', isLow: k === 'low', isCourse: isCourse, isZero: k === 'zero',
      pill: f(pill), pillCls: (k === 'zero' || k === 'low') ? 'low' : '', glow: k === 'zero' ? 'cb' : 'am', tone: k === 'zero' ? 'cb' : 'am',
      backT: k === 'zero' ? 'Back to SQL for Data Analysis' : 'Back to course',
      koPill: isCourse ? f((d.need || 0) - (d.have || 0)) + ' DLP short' : 'Progress saved',
      h1: d.h1 || '', sub: d.sub || '', course: d.course || '', thCls: d.th || '', need: f(d.need || 0), have: f(d.have || 0), short: f((d.need || 0) - (d.have || 0)),
      more: d.more || '', moreHref: d.moreHref || '#',
      optN: (d.opts || []).length, optsCls: (d.opts || []).length === 2 ? 'n2' : '',
      opts: (d.opts || []).map(function (o) { return { t: o[0], d: o[1], cta: o[2], href: o[3], rec: !!o[4], plain: !o[4], cls: o[4] ? 'rec' : '' }; }),
      showToast: this.state.toast, dismiss: function () { self.setState({ toast: false }); }
    };
  }
}
'''

PROPS = {"kind": {"editor": "enum", "options": ["freeCourse", "proCourse", "zero", "low"], "default": "freeCourse"}, "$preview": {"width": 1440, "height": 900}}

HTML = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Learning access</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">
<style>
''' + BASE_CSS + KIT_CSS + '\n' + CSS + '''</style>
</helmet>
''' + MARKUP + '''
</x-dc>
<script type="text/x-dc" data-dc-script data-props='%s'>%s</script>
</body>
</html>
''' % (json.dumps(PROPS), JS)

if __name__ == '__main__':
    open(OUT, 'w').write(HTML)
    print('wrote', OUT, len(HTML))
