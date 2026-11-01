from shell import *
from detailcss import *
css=CSS+r'''
.ce-seal{width:16px;height:16px}
.ce-comp{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.ce-cp{display:flex;flex-direction:column;gap:6px;padding:18px;border-radius:16px;background:#F5F8FF}
.ce-ci{width:34px;height:34px;border-radius:10px;background:#FFFFFF;color:#1652F0;display:flex;align-items:center;justify-content:center;margin-bottom:4px}
.ce-cp b{font-size:15px;font-weight:600;color:#0B1433}
.ce-cp span{font-size:13px;line-height:1.5;color:#5B6582;text-wrap:pretty}
.ce-steps{position:relative;display:flex;flex-direction:column;gap:12px}
.ce-st:not(:last-child)::before{content:"";position:absolute;left:21px;top:44px;bottom:-12px;width:2px;background:#1652F0}
.ce-st{position:relative;display:grid;grid-template-columns:44px minmax(0,1fr);gap:18px}
.ce-num{position:relative;z-index:1;width:44px;height:44px;border-radius:999px;background:#FFFFFF;border:2px solid #1652F0;color:#1652F0;display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:600;box-sizing:border-box}
.ce-st:last-child .ce-num{background:#1652F0;color:#FFFFFF;box-shadow:0 0 0 6px rgba(22,82,240,.12)}
.ce-sc{padding:16px 20px;border-radius:18px;border:1.5px solid #E6EAF3;background:#FFFFFF;display:flex;flex-direction:column;gap:10px}
.ce-shd{display:flex;align-items:flex-start;justify-content:space-between;gap:12px}
.ce-sn{font-size:17px;font-weight:600;letter-spacing:-.3px;color:#0B1433;display:flex;align-items:center;gap:8px}
.ce-sd{font-size:14px;line-height:1.5;color:#5B6582;margin-top:3px;text-wrap:pretty}
.ce-pm{height:26px;padding:0 10px;border-radius:999px;background:#F5F8FF;border:1px solid #E3E8F3;display:inline-flex;align-items:center;font-size:12px;font-weight:500;color:#3A4566;white-space:nowrap;flex-shrink:0}
.ce-cs{margin:0;padding:0;list-style:none;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.ce-cs li{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:10px 12px;border-radius:12px;background:#F5F8FF;font-size:14px;color:#0B1433}
.ce-cs li span{font-size:12px;color:#8A93AD;white-space:nowrap}
.ce-also{display:flex;align-items:center;flex-wrap:wrap;gap:8px;margin-top:2px;font-size:13px;color:#8A93AD}
.ce-also span{height:30px;padding:0 12px 0 10px;border-radius:999px;border:1px solid #E3E8F3;display:inline-flex;align-items:center;gap:6px;font-size:13px;font-weight:500;color:#3A4566}
.ce-also svg{color:#1652F0}
.ce-cred{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:28px;align-items:center;padding:28px;border-radius:22px;background:linear-gradient(180deg,#F5F8FF,#FFFFFF);border:1.5px solid #E6EAF3}
.ce-paper{position:relative;aspect-ratio:1.42;border-radius:12px;background:#FFFFFF;border:1px solid #E3E8F3;box-shadow:0 30px 60px -40px rgba(11,20,51,.5);padding:22px 24px;box-sizing:border-box;display:flex;flex-direction:column;gap:6px;transform:rotate(-2deg)}
.ce-paper::before{content:"";position:absolute;inset:8px;border:1px solid #DCE5FB;border-radius:7px;pointer-events:none}
.ce-ppl{font-size:9.5px;font-weight:600;letter-spacing:1.8px;color:#8A93AD}
.ce-ppn{font-size:22px;font-weight:600;letter-spacing:-.4px;line-height:1.15;color:#0B1433}
.ce-ppt{font-size:12px;color:#5B6582}
.ce-ppt b{display:block;font-size:15px;font-weight:600;color:#0B1433;margin-top:2px}
.ce-pps{position:absolute;right:20px;bottom:18px;width:56px;height:56px;filter:drop-shadow(0 8px 12px rgba(22,82,240,.3))}
.ce-ppf{margin-top:auto;display:flex;gap:18px;font-size:10px;color:#8A93AD}
.ce-cl{display:flex;flex-direction:column;gap:12px}
.ce-ct{font-size:20px;font-weight:600;letter-spacing:-.4px;color:#0B1433}
.ce-cl ul{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px}
.ce-cl li{display:flex;align-items:flex-start;gap:10px;font-size:14px;line-height:1.5;color:#3A4566}
.ce-ck{width:20px;height:20px;border-radius:999px;background:#EAF0FF;color:#1652F0;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px}
.ce-prev{position:relative;margin:12px 12px 0;height:140px;border-radius:14px;background:linear-gradient(180deg,#FFFFFF,#F5F8FF);border:1px solid #E3E8F3;padding:18px 20px;box-sizing:border-box;display:flex;flex-direction:column;gap:5px;overflow:hidden}
.ce-prev::before{content:"";position:absolute;inset:7px;border:1px solid #DCE5FB;border-radius:9px;pointer-events:none}
.ce-prog{display:flex;flex-direction:column;gap:8px}
.ce-pb{height:8px;border-radius:9px;background:#E6EAF3;overflow:hidden}
.ce-pb span{display:block;height:100%;width:8%;border-radius:9px;background:#1652F0}
.ce-pl{display:flex;justify-content:space-between;font-size:13px;color:#5B6582}
.ce-pl b{font-weight:600;color:#0B1433}
@media (max-width: 1180px){.ce-comp{grid-template-columns:repeat(2,minmax(0,1fr))}.ce-cs{grid-template-columns:minmax(0,1fr)}.ce-cred{grid-template-columns:minmax(0,1fr)}.ce-paper{max-width:380px}}
@media (max-width: 960px){.ce-prev{display:none}}
@media (max-width: 760px){
.ce-comp{grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:8px}
.ce-cp{padding:14px;gap:4px}
.ce-cp span{display:none}
.ce-ci{width:30px;height:30px}
.ce-cp b{font-size:14px}
.ce-st:not(:last-child)::before{left:15px;top:32px}
.ce-st{grid-template-columns:32px minmax(0,1fr);gap:12px}
.ce-num{width:32px;height:32px;font-size:13px}
.ce-sc{padding:14px}
.ce-shd{flex-direction:column;gap:8px}
.ce-sn{font-size:16px}
.ce-sd{font-size:13px}
.ce-cred{padding:18px;gap:18px}
.ce-ppn{font-size:18px}
.ce-paper{max-width:280px;transform:rotate(-1.5deg)}
.ce-pps{width:44px;height:44px}
}
'''
seal_big='<svg class="%s" viewBox="0 0 100 100" aria-hidden="true"><path d="'+SEAL+'" fill="#1652F0"></path><path d="M33 51l11 11 23-24" fill="none" stroke="#FFFFFF" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"></path></svg>'
ico={
 'prep':'<path d="M4 6h16M4 12h10M4 18h7"></path>',
 'query':'<path d="M8 6l-6 6 6 6M16 6l6 6-6 6"></path>',
 'analysis':'<path d="M4 20V10M10 20V4M16 20v-7M2 20h20"></path>',
 'viz':'<path d="M21 12a9 9 0 1 1-9-9v9z"></path><path d="M14 3.5A9 9 0 0 1 20.5 10H14z"></path>',
 'stats':'<path d="M3 17c3-8 5-12 9-12s6 4 9 12"></path><path d="M3 21h18"></path>',
 'comm':'<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"></path>'}
def i(k,s=16): return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>'%(s,s,ico[k])
comps=[('prep','Data preparation','Clean, structure and validate raw data.'),('query','Querying','Accurate SQL, including joins and aggregation.'),('analysis','Analysis','Find trends and answer business questions.'),('viz','Visualisation','Clear charts and dashboards.'),('stats','Statistical reasoning','Apply basic statistics correctly.'),('comm','Communication','Present findings to people outside data.')]
comp_html='\n'.join('<div class="ce-cp"><span class="ce-ci">%s</span><b>%s</b><span>%s</span></div>'%(i(k),t,d) for k,t,d in comps)
top='''<div class="dt-top">
%s
<div class="dt-grid">
<div class="dt-main">
<div class="dt-hero">
<nav class="dt-crumb" aria-label="Breadcrumb"><a href="#">Certifications</a><span aria-hidden="true">/</span><span>Data</span></nav>
<div class="dt-tags">
<span class="dt-tag">%s Credalio Validated</span>
<span class="dt-tag">Professional</span>
</div>
<h1 class="dt-h1">Professional Certificate in Data Analysis</h1>
<p class="dt-sub">Proof you can clean, query, analyse and present data to a professional standard.</p>
<div class="dt-by">
<span class="dt-who"><span class="dt-av" aria-hidden="true">NU</span><span><b>Northgate University</b></span></span>
<span class="dt-sep" aria-hidden="true"></span>
<span class="dt-fact"><b>Exam + case study</b></span>
<span class="dt-fact"><b>3–4 months</b></span>
</div>
</div>
%s
<section class="dt-sec" ref="{{refOverview}}" aria-labelledby="ce-o">
<h2 id="ce-o" class="dt-h2">What it proves</h2>
<p class="dt-p">That you can run the whole analysis cycle: prepare data, query it, find the pattern and explain what it means. It’s assessed, not just completed, so employers can trust it.</p>
<div class="ce-comp">
%s
</div>
<div class="dt-chips"><span class="dt-chl">Made for</span><span class="dt-chip">Career changers</span><span class="dt-chip">Early-career analysts</span><span class="dt-chip">Anyone formalising data skills</span></div>
</section>

<section class="dt-sec" ref="{{refEarn}}" aria-labelledby="ce-e">
<h2 id="ce-e" class="dt-h2">How you earn it</h2>
<div class="ce-steps">
<div class="ce-st"><span class="ce-num" aria-hidden="true">1</span><div class="ce-sc">
<div class="ce-shd"><div><div class="ce-sn">Required learning<i class="sx-tip" tabindex="0" data-tip="Already know some of this? Your AI Coach checks equivalent learning so you don’t repeat it.">i</i></div><div class="ce-sd">Four validated courses that cover every competency.</div></div><span class="ce-pm">36 hrs</span></div>
<ul class="ce-cs"><li>Data Foundations: Spreadsheets to SQL<span>12 hrs</span></li><li>SQL for Data Analysis<span>10 hrs</span></li><li>Data Visualisation with Power BI<span>6 hrs</span></li><li>Statistics Essentials<span>8 hrs</span></li></ul>
</div></div>
<div class="ce-st"><span class="ce-num" aria-hidden="true">2</span><div class="ce-sc"><div class="ce-shd"><div><div class="ce-sn">Core knowledge exam</div><div class="ce-sd">Timed, 60 questions on the six competencies.</div></div><span class="ce-pm">Pass mark 70%%</span></div></div></div>
<div class="ce-st"><span class="ce-num" aria-hidden="true">3</span><div class="ce-sc"><div class="ce-shd"><div><div class="ce-sn">Practical case study</div><div class="ce-sd">Clean a real dataset, analyse it, build a dashboard and recommend what to do. An assessor reviews it.</div></div><span class="ce-pm">Pass mark 70%%</span></div></div></div>
<div class="ce-st"><span class="ce-num" aria-hidden="true">%s</span><div class="ce-sc"><div class="ce-shd"><div><div class="ce-sn">Final review</div><div class="ce-sd">A short conversation about your case study with an assessor.</div></div><span class="ce-pm">Pass or not yet</span></div>
<div class="ce-also">Also needed<span>%s Verify your identity</span><span>%s Agree to the code of conduct</span></div>
</div></div>
</div>
</section>

<section class="dt-sec" ref="{{refCredential}}" aria-labelledby="ce-c">
<h2 id="ce-c" class="dt-h2">What you get</h2>
<div class="ce-cred">
<div class="ce-paper" aria-hidden="true"><span class="ce-ppl">PROFESSIONAL CERTIFICATE</span><span class="ce-ppn">Data Analysis</span><span class="ce-ppt">Awarded to<b>Your name</b></span><span class="ce-ppf"><span>Northgate University</span><span>Credential ID 7F2-91</span></span>%s</div>
<div class="ce-cl"><div class="ce-ct">A credential anyone can check</div>
<ul>
<li><span class="ce-ck">%s</span>Verifiable certificate and digital badge</li>
<li><span class="ce-ck">%s</span>Saved to your Digital Backpack with a share link</li>
<li><span class="ce-ck">%s</span>Valid for 3 years<i class="sx-tip" tabindex="0" data-tip="Renew with a short review of recent work. Placeholder period, to be confirmed by the issuer.">i</i></li>
<li><span class="ce-ck">%s</span>Completes the Data Analyst career path</li>
</ul></div>
</div>
</section>

<section class="dt-sec" ref="{{refFaq}}" aria-labelledby="ce-f">
<h2 id="ce-f" class="dt-h2">Questions</h2>
<div class="dt-faq">
<sc-for list="{{faqs}}" as="f" hint-placeholder-count="4">
<div class="dt-fq {{f.cls}}"><button class="dt-fh" type="button" aria-expanded="{{f.exp}}" onClick="{{f.toggle}}">{{f.q}}%s</button><sc-if value="{{f.open}}" hint-placeholder-val="{{ false }}"><p class="dt-fa">{{f.a}}</p></sc-if></div>
</sc-for>
</div>
</section>
</div>

<aside class="dt-side" aria-label="Start this certification">
<div class="dt-card">
<div class="ce-prev" aria-hidden="true"><span class="ce-ppl">PROFESSIONAL CERTIFICATE</span><span class="ce-ppn" style="font-size: 19px">Data Analysis</span><span class="ce-ppt" style="margin-top: auto">Northgate University</span>%s</div>
<div class="dt-cbody">
<span class="dt-lab">Certification fee<i class="sx-tip" tabindex="0" data-tip="Includes every assessment, the practical review, your credential and one resit. Courses use your DLP as usual. Blockchain-anchored certificate: optional $10 add-on on Pro.">i</i></span>
<div class="dt-amt"><b>$149</b><span>one time</span></div>
<sc-if value="{{notStarted}}" hint-placeholder-val="{{ true }}">
<button class="dt-btn" type="button" onClick="{{start}}">Start certification<i aria-hidden="true">%s</i></button>
</sc-if>
<sc-if value="{{started}}" hint-placeholder-val="{{ false }}">
<div class="ce-prog" role="status"><div class="ce-pl"><span>Your progress</span><b>1 of 6 in progress</b></div><div class="ce-pb"><span></span></div></div>
<a class="dt-btn" href="#">Continue<i aria-hidden="true">%s</i></a>
</sc-if>
<a class="dt-ask" href="#"><span class="sx-orb" style="width: 22px; height: 22px" aria-hidden="true"></span>Check my readiness</a>
</div>
</div>
</aside>

<div class="dt-bar">
<div><b>$149</b><span>One time</span></div>
<button class="dt-btn" type="button" onClick="{{start}}">{{barCta}}<i aria-hidden="true">%s</i></button>
</div>
</div>
</div>
%s'''%(nav('Certifications'), seal_big%'ce-seal', TABS_HTML, comp_html, CHECK%(16,16), CHECK%(12,12), CHECK%(12,12), seal_big%'ce-pps', CHECK%(11,11),CHECK%(11,11),CHECK%(11,11),CHECK%(11,11), CHEV, seal_big%'ce-pps', ARROW%(16,16,'#1652F0'), ARROW%(16,16,'#1652F0'), ARROW%(15,15,'#1652F0'), FOOT)
script=r'''
class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { tab: 'Overview', started: false, faq: 0 };
    var self = this;
    this.secs = {};
    this.mk = function (k) { return function (e) { self.secs[k] = e; }; };
    this.R = { Overview: this.mk('Overview'), 'How you earn it': this.mk('How you earn it'), 'What you get': this.mk('What you get'), Questions: this.mk('Questions') };
    this.F = [['Do I have to take the four courses?', 'Only if you need them. Your AI Coach compares what you already know with each competency and skips anything you can show evidence for.'], ['What if I don’t pass first time?', 'One resit of each assessment is included. You get written feedback on what to work on before you try again.'], ['How long does it take?', 'Most people finish in three to four months at around five hours a week, including the courses.'], ['Can my employer pay?', 'Yes. Choose employer invoicing at checkout and we send the invoice to them directly.']];
  }
  renderVals() {
    var self = this, S = this.state;
    var names = ['Overview', 'How you earn it', 'What you get', 'Questions'];
    var start = function () { self.setState({ started: true }); };
    return {
      ''' + TABS_JS + r'''
      refOverview: this.R.Overview, refEarn: this.R['How you earn it'], refCredential: this.R['What you get'], refFaq: this.R.Questions,
      faqs: this.F.map(function (f, i) { var open = S.faq === i; return { q: f[0], a: f[1], open: open, exp: open ? 'true' : 'false', cls: open ? 'dt-fq-open' : '', toggle: function () { self.setState({ faq: open ? -1 : i }); } }; }),
      started: S.started, notStarted: !S.started, start: start, barCta: S.started ? 'Continue' : 'Start certification'
    };
  }
}
'''
open('/home/user/credalio/design/canvas3/project/CertDetail.dc.html','w').write(page('Certification Detail',css,'',top,script,2600))
