from shell import *
from detailcss import *
I={'live':'<path d="M15 10l5-3v10l-5-3z"></path><rect x="3" y="6" width="12" height="12" rx="2"></rect>',
'build':'<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"></path>',
'mentor':'<circle cx="9" cy="8" r="3.5"></circle><path d="M2.5 20c1-3.5 3.5-5 6.5-5s5.5 1.5 6.5 5M16 4.5a3.5 3.5 0 0 1 0 7M18 15c2 .6 3.2 2.2 3.5 5"></path>',
'cert':'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"></path><path d="M9 12l2 2 4-4"></path>',
'proj':'<path d="M3 7h18v13H3zM8 7V4h8v3"></path>',
'path':'<circle cx="6" cy="18" r="2.5"></circle><circle cx="18" cy="6" r="2.5"></circle><path d="M8.5 18H15a3 3 0 0 0 0-6H9a3 3 0 0 1 0-6h6.5"></path>'}
def ic(k,s=18): return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>'%(s,s,I[k])
css=CSS+r'''
.pd2-ok{height:28px;padding:0 11px;border-radius:999px;background:#E7F5EE;color:#0F6B45;display:inline-flex;align-items:center;gap:7px;font-size:13px;font-weight:500}
.pd2-ok i{width:7px;height:7px;border-radius:999px;background:#1E9E63;display:block}
.pd2-pil{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.pd2-pi{display:flex;flex-direction:column;gap:6px;padding:20px;border-radius:18px;background:#F5F8FF}
.pd2-pii{width:38px;height:38px;border-radius:12px;background:#FFFFFF;color:#1652F0;display:flex;align-items:center;justify-content:center;margin-bottom:6px}
.pd2-pi b{font-size:16px;font-weight:600;color:#0B1433}
.pd2-pi span{font-size:14px;line-height:1.5;color:#5B6582;text-wrap:pretty}
.pd2-ph{position:relative;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.pd2-ph::before{content:"";position:absolute;left:22px;right:calc(25% - 31px);top:21px;height:2px;background:linear-gradient(90deg,#1652F0,#9DB8F7)}
.pd2-p{position:relative;display:flex;flex-direction:column;gap:8px}
.pd2-pn{width:44px;height:44px;border-radius:999px;background:#FFFFFF;border:2px solid #1652F0;color:#1652F0;display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:600;box-sizing:border-box;margin-bottom:6px}
.pd2-p:last-child .pd2-pn{background:#1652F0;color:#FFFFFF;box-shadow:0 0 0 6px rgba(22,82,240,.12)}
.pd2-pw{font-size:12px;font-weight:500;color:#8A93AD}
.pd2-pt{font-size:16px;font-weight:600;letter-spacing:-.2px;color:#0B1433}
.pd2-pd{font-size:13px;line-height:1.5;color:#5B6582;text-wrap:pretty}
.pd2-pj{align-self:flex-start;margin-top:4px;height:26px;padding:0 10px 0 8px;border-radius:999px;background:#E7F5EE;color:#0F6B45;display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:500}
.pd2-leave{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-top:8px}
.pd2-lv{display:flex;align-items:center;gap:12px;padding:14px 16px;border-radius:16px;border:1.5px solid #E6EAF3}
.pd2-lvi{width:36px;height:36px;border-radius:11px;background:#EAF0FF;color:#1652F0;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.pd2-lv b{display:block;font-size:14px;font-weight:600;color:#0B1433}
.pd2-lv span{font-size:12.5px;color:#5B6582}
.pd2-week{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.pd2-day{display:flex;flex-direction:column;gap:4px;padding:18px;border-radius:18px;border:1.5px solid #E6EAF3;background:#FFFFFF}
.pd2-day-k{background:#0B1433;border-color:#0B1433;color:#FFFFFF}
.pd2-dn{font-size:12px;font-weight:600;letter-spacing:1.2px;color:#1652F0}
.pd2-day-k .pd2-dn{color:#9DB8F7}
.pd2-dt{font-size:16px;font-weight:600;color:inherit;margin-top:6px}
.pd2-dd{font-size:13px;color:#5B6582}
.pd2-day-k .pd2-dd{color:rgba(255,255,255,.7)}
.pd2-ppl{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.pd2-pp{display:flex;align-items:center;gap:14px;padding:16px;border-radius:18px;background:#F5F8FF}
.pd2-av{width:52px;height:52px;border-radius:999px;background:linear-gradient(150deg,#C9D7FA,#EAF0FF);color:#1652F0;display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:600;flex-shrink:0}
.pd2-pp b{display:block;font-size:15px;font-weight:600;color:#0B1433}
.pd2-pp span{font-size:13px;color:#5B6582}
.pd2-cohort{display:flex;align-items:center;gap:14px;padding:16px 18px;border-radius:16px;border:1.5px dashed #C9D7FA;font-size:14px;line-height:1.5;color:#3A4566}
.pd2-avs{display:flex;flex-shrink:0}
.pd2-avs span{width:30px;height:30px;margin-left:-8px;border-radius:999px;border:2px solid #FFFFFF;display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:600}
.pd2-avs span:first-child{margin-left:0}
.pd2-cohort b{font-weight:600;color:#0B1433}
.pd2-when{display:flex;align-items:center;gap:14px;padding:16px;margin:12px 12px 0;border-radius:16px;background:#F5F8FF}
.pd2-cal{width:56px;height:56px;border-radius:14px;background:#FFFFFF;display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1;box-shadow:0 10px 20px -14px rgba(11,20,51,.4);flex-shrink:0}
.pd2-cal b{font-size:22px;font-weight:600;color:#0B1433}
.pd2-cal span{font-size:10px;font-weight:600;letter-spacing:1.4px;color:#1652F0;margin-top:4px}
.pd2-when > div > b{display:block;font-size:16px;font-weight:600;color:#0B1433}
.pd2-when > div > span{font-size:13px;color:#5B6582}
.pd2-form{display:flex;flex-direction:column;gap:10px}
.pd2-fl{display:flex;flex-direction:column;gap:6px;font-size:13px;font-weight:500;color:#3A4566}
.pd2-fi{height:46px;box-sizing:border-box;padding:0 14px;border-radius:12px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:'Google Sans',system-ui,sans-serif;font-size:15px;color:#0B1433;outline:none}
.pd2-ta{height:84px;padding:10px 14px;resize:none;line-height:1.45}
.pd2-fi:focus{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.pd2-err{font-size:13px;color:#B42318}
.pd2-fi-bad{border-color:#D92D20}
.pd2-cancel{height:40px;border:none;background:none;font-family:'Google Sans',system-ui,sans-serif;font-size:14px;font-weight:600;color:#5B6582;cursor:pointer}
.pd2-done{display:flex;flex-direction:column;gap:6px;padding:16px;border-radius:16px;background:#E7F5EE;color:#0F6B45}
.pd2-done b{display:flex;align-items:center;gap:8px;font-size:15px;font-weight:600}
.pd2-done span{font-size:13px;line-height:1.5;color:#1E5A45}
@media (max-width: 1180px){.pd2-ph{grid-template-columns:repeat(2,minmax(0,1fr));row-gap:24px}.pd2-ph::before{display:none}.pd2-week{grid-template-columns:repeat(2,minmax(0,1fr))}.pd2-ppl,.pd2-leave{grid-template-columns:minmax(0,1fr)}.pd2-pil{grid-template-columns:minmax(0,1fr)}.pd2-pi{flex-direction:row;align-items:center;gap:14px}.pd2-pii{margin:0;flex-shrink:0}}
@media (max-width: 960px){.pd2-when{margin:0;border-radius:0;background:#F5F8FF}}
@media (max-width: 760px){
.pd2-pi{padding:14px;gap:12px}
.pd2-pi b{font-size:15px}
.pd2-pi span{font-size:13px}
.pd2-ph{grid-template-columns:minmax(0,1fr);row-gap:0}
.pd2-p{display:grid;grid-template-columns:36px minmax(0,1fr);column-gap:12px;row-gap:2px;padding-bottom:18px;position:relative}
.pd2-p::before{content:"";position:absolute;left:17px;top:36px;bottom:0;width:2px;background:#C9D7FA}
.pd2-p:last-child::before{display:none}
.pd2-pn{grid-row:1 / span 4;width:36px;height:36px;font-size:13px;margin:0}
.pd2-pw,.pd2-pt,.pd2-pd,.pd2-pj{grid-column:2}
.pd2-pj{justify-self:start}
.pd2-ppl{display:flex;overflow-x:auto;margin:0 -20px;padding:0 20px;gap:8px;scrollbar-width:none}
.pd2-ppl::-webkit-scrollbar{display:none}
.pd2-pp{flex:0 0 auto}
.pd2-week{gap:8px}
.pd2-day{padding:14px}
.pd2-dt{font-size:15px;margin-top:2px}
.pd2-pp{padding:12px}
.pd2-av{width:44px;height:44px;font-size:14px}
.pd2-cohort{align-items:flex-start;font-size:13px}
.pd2-when{padding:14px}
}
'''
tip_times='<i class="sx-tip" tabindex="0" data-tip="Times are shown in your time zone. Every live session is recorded.">i</i>'
top='''<div class="dt-top">
%(nav)s
<div class="dt-grid">
<div class="dt-main">
<div class="dt-hero">
<nav class="dt-crumb" aria-label="Breadcrumb"><a href="#">Learning programs</a><span aria-hidden="true">/</span><span>Accelerator</span></nav>
<div class="dt-tags"><span class="pd2-ok"><i></i>Places available</span><span class="dt-tag">Accelerator</span></div>
<h1 class="dt-h1">AI &amp; Data Analytics Accelerator</h1>
<p class="dt-sub">Twelve weeks of live, mentored learning, from data basics to applied AI, ending with a capstone you can show employers.</p>
<div class="dt-by">
<span class="dt-who"><span class="dt-av" aria-hidden="true">NU</span><span><b>Northgate University</b></span></span>
<span class="dt-sep" aria-hidden="true"></span>
<span class="dt-fact"><b>12 weeks</b></span>
<span class="dt-fact"><b>About 8 hrs a week</b></span>
</div>
</div>
%(tabs)s
<section class="dt-sec" ref="{{refOverview}}" aria-labelledby="pr-o">
<h2 id="pr-o" class="dt-h2">Learn it live, with people</h2>
<div class="pd2-pil">
<div class="pd2-pi"><span class="pd2-pii">%(live)s</span><div><b>Live every week</b><br><span>Expert-led sessions you can join or replay.</span></div></div>
<div class="pd2-pi"><span class="pd2-pii">%(build)s</span><div><b>Build, don’t just watch</b><br><span>A reviewed project in every phase.</span></div></div>
<div class="pd2-pi"><span class="pd2-pii">%(mentor)s</span><div><b>Mentored</b><br><span>Small-group support all the way through.</span></div></div>
</div>
<div class="dt-chips"><span class="dt-chl">Before you join</span><span class="dt-chip">Comfortable with spreadsheets</span><span class="dt-chip">A short application</span></div>
</section>

<section class="dt-sec" ref="{{refCurriculum}}" aria-labelledby="pr-c">
<h2 id="pr-c" class="dt-h2">Twelve weeks, four phases</h2>
<div class="pd2-ph">
<div class="pd2-p"><span class="pd2-pn">1</span><span class="pd2-pw">Weeks 1–3</span><span class="pd2-pt">Foundations</span><span class="pd2-pd">Data literacy, spreadsheets and SQL basics.</span></div>
<div class="pd2-p"><span class="pd2-pn">2</span><span class="pd2-pw">Weeks 4–6</span><span class="pd2-pt">Analysis in practice</span><span class="pd2-pd">SQL, visualisation and telling the story.</span><span class="pd2-pj">%(proj)sSales dashboard</span></div>
<div class="pd2-p"><span class="pd2-pn">3</span><span class="pd2-pw">Weeks 7–9</span><span class="pd2-pt">Applied AI</span><span class="pd2-pd">Machine learning concepts, AI tools and evaluation.</span><span class="pd2-pj">%(proj)sCustomer insights</span></div>
<div class="pd2-p"><span class="pd2-pn">%(check)s</span><span class="pd2-pw">Weeks 10–12</span><span class="pd2-pt">Capstone</span><span class="pd2-pd">Solve a real business problem and present it.</span><span class="pd2-pj">%(proj)sBusiness case</span></div>
</div>
<div class="pd2-leave">
<div class="pd2-lv"><span class="pd2-lvi">%(cert)s</span><div><b>Program certificate</b><span>In your Digital Backpack</span></div></div>
<div class="pd2-lv"><span class="pd2-lvi">%(projb)s</span><div><b>3 verified projects</b><span>Portfolio evidence</span></div></div>
<div class="pd2-lv"><span class="pd2-lvi">%(path)s</span><div><b>Counts toward</b><span>Professional Certificate in Data Analysis</span></div></div>
</div>
</section>

<section class="dt-sec" ref="{{refWeek}}" aria-labelledby="pr-w">
<h2 id="pr-w" class="dt-h2">Your week%(tip)s</h2>
<div class="pd2-week">
<div class="pd2-day pd2-day-k"><span class="pd2-dn">TUESDAY</span><span class="pd2-dt">Live session</span><span class="pd2-dd">90 minutes</span></div>
<div class="pd2-day"><span class="pd2-dn">THURSDAY</span><span class="pd2-dt">Mentor hours</span><span class="pd2-dd">60 minutes</span></div>
<div class="pd2-day"><span class="pd2-dn">YOUR TIME</span><span class="pd2-dt">Self-paced lessons</span><span class="pd2-dd">About 4 hours</span></div>
<div class="pd2-day"><span class="pd2-dn">SATURDAY</span><span class="pd2-dt">Project clinic</span><span class="pd2-dd">Optional</span></div>
</div>
</section>

<section class="dt-sec" ref="{{refPeople}}" aria-labelledby="pr-p">
<h2 id="pr-p" class="dt-h2">Who you’ll learn with</h2>
<div class="pd2-ppl">
<div class="pd2-pp"><span class="pd2-av" aria-hidden="true">SR</span><div><b>Dr Samuel Reed</b><span>Lead instructor</span></div></div>
<div class="pd2-pp"><span class="pd2-av" aria-hidden="true">PN</span><div><b>Priya Nair</b><span>AI instructor</span></div></div>
<div class="pd2-pp"><span class="pd2-av" aria-hidden="true">TH</span><div><b>Tom Hughes</b><span>Mentor lead</span></div></div>
</div>
<div class="pd2-cohort"><span class="pd2-avs" aria-hidden="true"><span style="background: #DCE5FB; color: #1652F0">AK</span><span style="background: #1652F0; color: #FFFFFF">MS</span><span style="background: #0B1433; color: #FFFFFF">JL</span><span style="background: #EAF0FF; color: #1652F0">+37</span></span><span>A cohort of <b>40 learners</b> in peer groups of five, with a shared community space and an alumni network after.</span></div>
</section>

<section class="dt-sec" ref="{{refFaq}}" aria-labelledby="pr-f">
<h2 id="pr-f" class="dt-h2">Questions</h2>
<div class="dt-faq">
<sc-for list="{{faqs}}" as="f" hint-placeholder-count="4">
<div class="dt-fq {{f.cls}}"><button class="dt-fh" type="button" aria-expanded="{{f.exp}}" onClick="{{f.toggle}}">{{f.q}}%(chev)s</button><sc-if value="{{f.open}}" hint-placeholder-val="{{ false }}"><p class="dt-fa">{{f.a}}</p></sc-if></div>
</sc-for>
</div>
</section>
</div>

<aside class="dt-side" aria-label="Apply to this program">
<div class="dt-card" ref="{{refCard}}">
<div class="pd2-when"><span class="pd2-cal" aria-hidden="true"><b>18</b><span>JAN</span></span><div><b>Cohort starts 18 January</b><span>Applications close 8 January</span></div></div>
<div class="dt-cbody">
<span class="dt-lab">Program fee<i class="sx-tip" tabindex="0" data-tip="Pay in full or in three monthly instalments. Scholarships cover up to half the fee for 10 learners per cohort. Placeholder figures to confirm.">i</i></span>
<div class="dt-amt"><b>$1,200</b><span>or 3 × $400</span></div>
<sc-if value="{{idle}}" hint-placeholder-val="{{ true }}">
<button class="dt-btn" type="button" onClick="{{openForm}}">Apply<i aria-hidden="true">%(arrow)s</i></button>
<a class="dt-ask" href="#"><span class="sx-orb" style="width: 22px; height: 22px" aria-hidden="true"></span>Is this right for my goal?</a>
</sc-if>
<sc-if value="{{form}}" hint-placeholder-val="{{ false }}">
<form class="pd2-form" onSubmit="{{submit}}" novalidate>
<label class="pd2-fl">Full name<input class="pd2-fi {{nameBad}}" type="text" value="{{fName}}" onInput="{{onName}}" autocomplete="name"></label>
<label class="pd2-fl">Email<input class="pd2-fi {{emailBad}}" type="email" value="{{fEmail}}" onInput="{{onEmail}}" autocomplete="email"></label>
<label class="pd2-fl">What do you want to achieve?<textarea class="pd2-fi pd2-ta {{whyBad}}" onInput="{{onWhy}}">{{fWhy}}</textarea></label>
<sc-if value="{{hasErr}}" hint-placeholder-val="{{ false }}"><span class="pd2-err" role="alert">{{err}}</span></sc-if>
<button class="dt-btn" type="submit">Send application<i aria-hidden="true">%(arrow)s</i></button>
<button class="pd2-cancel" type="button" onClick="{{cancel}}">Cancel</button>
</form>
</sc-if>
<sc-if value="{{done}}" hint-placeholder-val="{{ false }}">
<div class="pd2-done" role="status"><b>%(check)s Application sent</b><span>We’ll email {{fEmail}} with next steps before the cohort starts.</span></div>
</sc-if>
</div>
</div>
</aside>

<div class="dt-bar">
<div><b>Starts 18 Jan</b><span>$1,200 · places available</span></div>
<button class="dt-btn" type="button" onClick="{{openForm}}">{{barCta}}<i aria-hidden="true">%(arrow15)s</i></button>
</div>
</div>
</div>
%(foot)s''' % dict(nav=nav('Explore learning'), tabs=TABS_HTML, live=ic('live'), build=ic('build'), mentor=ic('mentor'), proj=ic('proj',13), projb=ic('proj',17), cert=ic('cert',17), path=ic('path',17), check=CHECK%(16,16), tip=tip_times, chev=CHEV, arrow=ARROW%(16,16,'#1652F0'), arrow15=ARROW%(15,15,'#1652F0'), foot=FOOT)
script=r'''
class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { tab: 'Overview', faq: 0, stage: 'idle', fName: '', fEmail: '', fWhy: '', err: '', bad: '' };
    var self = this;
    this.secs = {};
    this.mk = function (k) { return function (e) { self.secs[k] = e; }; };
    this.cardRef = this.mk('card');
    this.R = { Overview: this.mk('Overview'), Curriculum: this.mk('Curriculum'), 'Your week': this.mk('Your week'), People: this.mk('People'), Questions: this.mk('Questions') };
    this.F = [['Do I need a technical background?', 'No. You need to be comfortable with spreadsheets. Everything else is taught from the start.'], ['What if I miss a live session?', 'Every session is recorded, and mentors help you catch up in their weekly hours.'], ['Is the certificate recognised?', 'Your program certificate is verifiable, and the program counts toward the Professional Certificate in Data Analysis.'], ['Can my employer pay?', 'Yes. Choose employer invoicing when you accept your place.']];
  }
  renderVals() {
    var self = this, S = this.state;
    var names = ['Overview', 'Curriculum', 'Your week', 'People', 'Questions'];
    var openForm = function () { if (S.stage === 'idle') self.setState({ stage: 'form' }); if (self.secs.card && self.secs.card.scrollIntoView) self.secs.card.scrollIntoView({ block: 'center' }); };
    return {
      ''' + TABS_JS + r'''
      refOverview: this.R.Overview, refCurriculum: this.R.Curriculum, refWeek: this.R['Your week'], refPeople: this.R.People, refFaq: this.R.Questions, refCard: this.cardRef,
      faqs: this.F.map(function (f, i) { var open = S.faq === i; return { q: f[0], a: f[1], open: open, exp: open ? 'true' : 'false', cls: open ? 'dt-fq-open' : '', toggle: function () { self.setState({ faq: open ? -1 : i }); } }; }),
      idle: S.stage === 'idle', form: S.stage === 'form', done: S.stage === 'done',
      barCta: S.stage === 'done' ? 'Application sent' : 'Apply',
      openForm: openForm, cancel: function () { self.setState({ stage: 'idle', err: '', bad: '' }); },
      fName: S.fName, fEmail: S.fEmail, fWhy: S.fWhy, err: S.err, hasErr: !!S.err,
      nameBad: S.bad === 'name' ? 'pd2-fi-bad' : '', emailBad: S.bad === 'email' ? 'pd2-fi-bad' : '', whyBad: S.bad === 'why' ? 'pd2-fi-bad' : '',
      onName: function (e) { self.setState({ fName: e.target.value }); }, onEmail: function (e) { self.setState({ fEmail: e.target.value }); }, onWhy: function (e) { self.setState({ fWhy: e.target.value }); },
      submit: function (e) {
        e.preventDefault();
        var bad = !S.fName.trim() ? 'name' : !/^\S+@\S+\.\S+$/.test(S.fEmail) ? 'email' : S.fWhy.trim().length < 10 ? 'why' : '';
        var msg = { name: 'Add your full name.', email: 'Check your email address.', why: 'Tell us a little more about your goal.' }[bad] || '';
        self.setState(bad ? { err: msg, bad: bad } : { err: '', bad: '', stage: 'done' });
      }
    };
  }
}
'''
open('/home/user/credalio/design/canvas3/project/ProgramDetail.dc.html','w').write(page('Program Detail',css,'',top,script,2600))
