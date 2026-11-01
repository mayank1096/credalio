from shell import *
CLOUD='/_blob/020f1a8593e80e5fcee9e0f06637f153'
SEAL='M56.5 9.0 Q64.2 6.3 68.8 13.0 Q77.0 12.8 79.3 20.7 Q87.2 23.0 87.0 31.2 Q93.7 35.8 91.0 43.5 Q96.0 50.0 91.0 56.5 Q93.7 64.2 87.0 68.8 Q87.2 77.0 79.3 79.3 Q77.0 87.2 68.8 87.0 Q64.2 93.7 56.5 91.0 Q50.0 96.0 43.5 91.0 Q35.8 93.7 31.2 87.0 Q23.0 87.2 20.7 79.3 Q12.8 77.0 13.0 68.8 Q6.3 64.2 9.0 56.5 Q4.0 50.0 9.0 43.5 Q6.3 35.8 13.0 31.2 Q12.8 23.0 20.7 20.7 Q23.0 12.8 31.2 13.0 Q35.8 6.3 43.5 9.0 Q50.0 4.0 56.5 9.0Z'
css=r'''
.ct-hero{background:#FFFFFF url(%s) center top / max(1440px,100%%) auto no-repeat}
.ct-hin{max-width:960px;margin:0 auto;padding:72px 24px 40px;box-sizing:border-box;display:flex;flex-direction:column;align-items:center;text-align:center;gap:18px}
.ct-h1{margin:0;font-size:56px;line-height:1.04;font-weight:600;letter-spacing:-1.8px;color:#0B1433}
.ct-h1 em{font-style:normal;color:#1652F0}
.ct-sub{margin:0;max-width:640px;font-size:18px;line-height:1.55;color:#4A5578}
.ct-search{width:100%%;max-width:640px;height:58px;box-sizing:border-box;margin-top:6px;padding:6px 6px 6px 20px;border-radius:999px;background:#FFFFFF;border:1.5px solid #D6DDEE;display:flex;align-items:center;gap:12px;box-shadow:0 24px 50px -32px rgba(11,20,51,.55);transition:border-color .2s ease,box-shadow .2s ease}
.ct-search:focus-within{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12),0 24px 50px -32px rgba(11,20,51,.55)}
.ct-in{flex:1;min-width:0;height:100%%;border:none;outline:none;background:transparent;font-family:'Google Sans',system-ui,sans-serif;font-size:16px;color:#0B1433}
.ct-in::placeholder{color:#8A93AD}
.ct-go{height:46px;padding:0 22px;border:none;border-radius:999px;background:#1652F0;color:#FFFFFF;font-family:'Google Sans',system-ui,sans-serif;font-size:15px;font-weight:600;cursor:pointer}
.ct-go:hover{background:#0E3BB8}
.ct-how{display:flex;align-items:center;gap:0;margin-top:14px;font-size:13px;font-weight:500;color:#3A4566}
.ct-how span{display:inline-flex;align-items:center;gap:8px;white-space:nowrap}
.ct-how i{width:22px;height:22px;border-radius:999px;background:#FFFFFF;border:1.5px solid #C9D7FA;color:#1652F0;display:flex;align-items:center;justify-content:center;font-style:normal;font-size:11px;font-weight:600;box-sizing:border-box}
.ct-how span:last-child i{background:#1652F0;border-color:#1652F0;color:#FFFFFF}
.ct-how b{display:block;width:40px;height:2px;margin:0 12px;background:linear-gradient(90deg,#C9D7FA,#1652F0);border-radius:2px}
.ct-body{max-width:1312px;margin:0 auto;padding:24px 48px 96px;box-sizing:border-box;display:flex;flex-direction:column;gap:28px}
.ct-bar{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;min-width:0}
.ct-fields{display:flex;gap:8px;flex-wrap:wrap;min-width:0}
.ct-f{height:36px;padding:0 15px;border-radius:10px;border:1px solid #E3E8F3;background:#FFFFFF;font-family:'Google Sans',system-ui,sans-serif;font-size:14px;font-weight:500;color:#3A4566;cursor:pointer;transition:border-color .2s ease}
.ct-f:hover{border-color:#C9D7FA}
.ct-f-on{background:#0B1433;border-color:#0B1433;color:#FFFFFF}
.ct-by{display:flex;align-items:center;gap:10px;font-size:13px;color:#8A93AD}
.ct-seg{display:flex;gap:2px;padding:3px;border-radius:999px;background:#F1F3F8}
.ct-seg button{height:30px;padding:0 13px;border:none;border-radius:999px;background:transparent;font-family:'Google Sans',system-ui,sans-serif;font-size:13px;font-weight:500;color:#5B6582;cursor:pointer}
.ct-seg .ct-seg-on{background:#FFFFFF;color:#0B1433;box-shadow:0 4px 10px -6px rgba(11,20,51,.3)}
.ct-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
.ct-card{display:flex;flex-direction:column;border-radius:20px;background:#FFFFFF;border:1px solid #E3E8F3;box-shadow:0 22px 44px -38px rgba(11,20,51,.45);overflow:hidden;text-decoration:none;color:#0B1433;transition:transform .45s cubic-bezier(.2,.7,.2,1),box-shadow .45s ease,border-color .3s ease}
.ct-card:hover{transform:translateY(-4px);border-color:#D6DDEE;box-shadow:0 34px 60px -38px rgba(22,82,240,.45)}
.ct-paper{position:relative;margin:12px 12px 0;height:150px;border-radius:12px;background:linear-gradient(180deg,#FFFFFF,#F5F8FF);border:1px solid #E3E8F3;padding:20px 22px;box-sizing:border-box;display:flex;flex-direction:column;gap:6px;overflow:hidden}
.ct-paper::before{content:"";position:absolute;inset:7px;border:1px solid #DCE5FB;border-radius:7px;pointer-events:none}
.ct-pl{font-size:9.5px;font-weight:600;letter-spacing:1.8px;color:#8A93AD}
.ct-pn{font-size:21px;font-weight:600;letter-spacing:-.4px;line-height:1.15;color:#0B1433;max-width:80%%}
.ct-pi{margin-top:auto;font-size:12px;color:#5B6582}
.ct-seal{position:absolute;right:18px;bottom:16px;width:52px;height:52px;filter:drop-shadow(0 8px 12px rgba(22,82,240,.3))}
.ct-rev{position:absolute;right:16px;top:16px;height:24px;padding:0 9px;border-radius:999px;background:#F1F3F8;color:#5B6582;display:inline-flex;align-items:center;gap:6px;font-size:11.5px;font-weight:500}
.ct-rev i{width:9px;height:9px;border-radius:999px;border:1.5px dashed #8A93AD;box-sizing:border-box}
.ct-cb{display:flex;flex-direction:column;gap:12px;padding:16px 20px 18px;flex:1}
.ct-meta{display:flex;align-items:center;gap:8px;font-size:13px;color:#5B6582}
.ct-meta b{font-weight:600;color:#0B1433}
.ct-fmt{display:flex;align-items:center;gap:10px;font-size:14px;color:#3A4566}
.ct-fi{width:30px;height:30px;border-radius:9px;background:#EAF0FF;color:#1652F0;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.ct-skills{display:flex;flex-wrap:wrap;gap:6px}
.ct-sk{height:26px;padding:0 10px;border-radius:999px;background:#F5F8FF;border:1px solid #E6EAF3;display:inline-flex;align-items:center;font-size:12px;font-weight:500;color:#3A4566}
.ct-foot{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-top:auto;padding-top:14px;border-top:1px solid #EEF1F7;font-size:13px;color:#8A93AD}
.ct-pre{display:inline-flex;align-items:center;gap:6px}
.ct-go2{font-size:14px;font-weight:600;color:#1652F0;white-space:nowrap}
.ct-empty{grid-column:1 / -1;padding:40px;border-radius:20px;background:#F5F8FF;text-align:center;font-size:15px;color:#5B6582}
.ct-ai{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,520px);gap:40px;align-items:center;margin-top:16px;padding:36px 40px;border-radius:24px;background:#FFFFFF url(%s) center top / cover no-repeat;border:1px solid #E3E8F3}
.ct-al{display:flex;align-items:flex-start;gap:16px}
.ct-ah{margin:0;font-size:26px;line-height:1.15;font-weight:600;letter-spacing:-.6px;color:#0B1433}
.ct-ap{margin:6px 0 0;font-size:15px;line-height:1.55;color:#4A5578}
.ct-af{height:56px;box-sizing:border-box;padding:5px 5px 5px 20px;border-radius:999px;background:#FFFFFF;border:1.5px solid #D6DDEE;display:flex;align-items:center;gap:10px;box-shadow:0 20px 40px -30px rgba(11,20,51,.5)}
.ct-af:focus-within{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.ct-ab{height:44px;padding:0 6px 0 18px;border:none;border-radius:999px;background:#1652F0;color:#FFFFFF;font-family:'Google Sans',system-ui,sans-serif;font-size:14px;font-weight:600;display:flex;align-items:center;gap:10px;cursor:pointer;white-space:nowrap;flex-shrink:0}
.ct-ab:hover{background:#0E3BB8}
.ct-ab span{width:32px;height:32px;border-radius:999px;background:rgba(255,255,255,.18);display:flex;align-items:center;justify-content:center}
.ct-card:focus-visible,.ct-f:focus-visible,.ct-seg button:focus-visible,.ct-go:focus-visible,.ct-ab:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:3px}
@media (max-width: 1180px){.ct-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width: 960px){.ct-ai{grid-template-columns:minmax(0,1fr);gap:22px;padding:30px}}
@media (max-width: 760px){
.ct-hero{background-size:auto 340px}
.ct-hin{padding:44px 20px 24px;gap:14px}
.ct-h1{font-size:32px;letter-spacing:-.9px;text-wrap:balance}
.ct-sub{font-size:15px}
.ct-search{height:54px;padding:4px 4px 4px 16px}
.ct-in{font-size:15px}
.ct-go{height:44px;padding:0 16px;font-size:14px}
.ct-how{display:none}
.ct-body{padding:12px 20px 72px;gap:20px}
.ct-bar{flex-direction:column;flex-wrap:nowrap;align-items:stretch;gap:12px}
.ct-fields{flex-wrap:nowrap;overflow-x:auto;margin:0 -20px;padding:0 20px;scrollbar-width:none}
.ct-fields::-webkit-scrollbar{display:none}
.ct-f{flex-shrink:0;height:34px;font-size:13px}
.ct-by{justify-content:space-between}
.ct-grid{grid-template-columns:minmax(0,1fr);gap:12px}
.ct-paper{height:118px;padding:16px 18px}
.ct-pn{font-size:18px}
.ct-seal{width:42px;height:42px}
.ct-cb{padding:14px 16px 14px;gap:10px}
.ct-skills{display:none}
.ct-foot{padding-top:0;border-top:none}
.ct-ai{padding:24px 20px 20px;border-radius:20px;background-size:auto 300px}
.ct-ah{font-size:21px}
.ct-ap{font-size:14px}
.ct-af{flex-direction:column;align-items:stretch;height:auto;padding:0;gap:10px;border:none;background:none;box-shadow:none;border-radius:0}
.ct-af:focus-within{box-shadow:none}
.ct-af .ct-in{flex:none;height:50px;box-sizing:border-box;padding:0 18px;border-radius:999px;background:#FFFFFF;border:1.5px solid #D6DDEE}
.ct-ab{height:50px;justify-content:space-between;padding:0 6px 0 20px;font-size:15px}
.ct-ab span{width:38px;height:38px}
}
'''%(CLOUD,CLOUD)
top='''<div class="ct-hero">
%s
<div class="ct-hin">
<h1 class="ct-h1">Prove you meet the <em>standard</em>.</h1>
<p class="ct-sub">Assessed credentials that employers can check in one click.</p>
<form class="ct-search" role="search" onSubmit="{{onSubmit}}">
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#5B6582" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex-shrink: 0"><circle cx="11" cy="11" r="7"></circle><path d="M20 20l-3.5-3.5"></path></svg>
<label for="ct-q" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Search certifications</label>
<input id="ct-q" class="ct-in" type="search" placeholder="Search certifications" value="{{q}}" onInput="{{onQ}}" autocomplete="off">
<button class="ct-go" type="submit">Search</button>
</form>
<div class="ct-how" aria-label="How certification works">
<span><i>1</i>Required learning</span><b></b><span><i>2</i>Practical work</span><b></b><span><i>3</i>Assessments</span><b></b><span><i><svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg></i>Credential in your Backpack</span>
</div>
</div>
</div>'''%nav('Certifications')
body='''<div class="ct-body">
<div class="ct-bar">
<div class="ct-fields" role="group" aria-label="Field">
<sc-for list="{{fields}}" as="f" hint-placeholder-count="6"><button class="ct-f {{f.cls}}" type="button" aria-pressed="{{f.on}}" onClick="{{f.pick}}">{{f.label}}</button></sc-for>
</div>
<div class="ct-by"><span>Issued by</span><div class="ct-seg" role="group" aria-label="Issued by"><sc-for list="{{issuers}}" as="i" hint-placeholder-count="3"><button type="button" class="{{i.cls}}" aria-pressed="{{i.on}}" onClick="{{i.pick}}">{{i.label}}</button></sc-for></div></div>
</div>
<div class="ct-grid">
<sc-for list="{{certs}}" as="c" hint-placeholder-count="6">
<a class="ct-card" href="#">
<div class="ct-paper">
<span class="ct-pl">PROFESSIONAL CERTIFICATE</span>
<span class="ct-pn">{{c.short}}</span>
<span class="ct-pi">{{c.issuer}}</span>
<sc-if value="{{c.ok}}" hint-placeholder-val="{{ true }}"><svg class="ct-seal" viewBox="0 0 100 100" aria-label="Credalio Validated"><path d="SEAL" fill="#1652F0"></path><path d="M33 51l11 11 23-24" fill="none" stroke="#FFFFFF" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"></path></svg></sc-if>
<sc-if value="{{c.rev}}" hint-placeholder-val="{{ false }}"><span class="ct-rev"><i></i>In review</span></sc-if>
</div>
<div class="ct-cb">
<span class="ct-meta"><b>{{c.level}}</b><span aria-hidden="true">·</span>{{c.time}}</span>
<span class="ct-fmt"><span class="ct-fi" aria-hidden="true"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11l3 3 8-8"></path><path d="M20 12v7a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h9"></path></svg></span>{{c.format}}</span>
<span class="ct-skills"><sc-for list="{{c.skills}}" as="s" hint-placeholder-count="3"><span class="ct-sk">{{s}}</span></sc-for></span>
<span class="ct-foot"><span class="ct-pre">Before you start<i class="sx-tip" tabindex="0" data-tip="{{c.pre}}">i</i></span><span class="ct-go2">View →</span></span>
</div>
</a>
</sc-for>
<sc-if value="{{none}}" hint-placeholder-val="{{ false }}"><div class="ct-empty">No certifications match yet. Try another field, or ask your AI Coach.</div></sc-if>
</div>
<section class="ct-ai" aria-labelledby="ct-ai-h">
<div class="ct-al"><span class="sx-orb" style="width: 44px; height: 44px; box-shadow: 0 0 0 6px rgba(22,82,240,.08),0 10px 24px -8px rgba(22,82,240,.6)" aria-hidden="true"></span><div><h2 id="ct-ai-h" class="ct-ah">Not sure which one fits?</h2><p class="ct-ap">Your AI Coach checks your readiness and plans what to learn first.</p></div></div>
<form class="ct-af" onSubmit="{{onSubmit}}"><label for="ct-goal" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Your goal</label><input id="ct-goal" class="ct-in" type="text" placeholder="I want to prove I can…" autocomplete="off"><button class="ct-ab" type="submit">Check my readiness<span aria-hidden="true">%s</span></button></form>
</section>
</div>
%s'''.replace('SEAL',SEAL)%(ARROW%(14,14,'#FFFFFF'),FOOT)
script=r'''
class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { q: '', field: 'All', issuer: 'Anyone' };
    var R = function (t, short, field, issuer, type, level, time, format, skills, pre, ok) { return { t: t, short: short, field: field, issuer: issuer, type: type, level: level, time: time, format: format, skills: skills, pre: pre, ok: ok }; };
    this.L = [
      R('Professional Certificate in Data Analysis', 'Data Analysis', 'Data', 'Northgate University', 'Institutions', 'Professional', '3–4 months', 'Timed exam + case study', ['SQL', 'Data cleaning', 'Statistics'], 'Recommended first: Data Foundations or equivalent. Your AI Coach can check what you already know.', true),
      R('Professional Certificate in Product Design', 'Product Design', 'Design', 'Lena Fischer', 'Creators', 'Professional', '4–5 months', 'Portfolio review + design challenge', ['User research', 'Interaction design', 'Prototyping'], 'Recommended first: UX and Product Design Foundations.', true),
      R('Professional Certification in Security Operations', 'Security Operations', 'Cybersecurity', 'Westbridge Institute', 'Institutions', 'Professional', '4–6 months', 'Simulation lab + exam', ['Threat detection', 'Incident response', 'SIEM'], 'Recommended first: Networking and Security Fundamentals.', true),
      R('Professional Certificate in Project Management', 'Project Management', 'Business', 'Westbridge Institute', 'Institutions', 'Foundation', '3 months', 'Scenario exam + project plan', ['Planning', 'Risk', 'Agile'], 'No prerequisites. Open to anyone.', true),
      R('Applied AI Practitioner Certification', 'Applied AI Practitioner', 'AI', 'David Mensah', 'Creators', 'Professional', '2–3 months', 'Practical build + oral review', ['Prompting', 'AI workflows', 'Evaluation'], 'Recommended first: Prompt Engineering for Professionals.', false),
      R('Professional Certificate in Financial Analysis', 'Financial Analysis', 'Finance', 'Harbour School of Finance', 'Institutions', 'Professional', '3–4 months', 'Timed exam + modelling case', ['Modelling', 'Valuation', 'Reporting'], 'Recommended first: Financial Modelling Essentials.', true)
    ];
  }
  renderVals() {
    var self = this, S = this.state, q = S.q.trim().toLowerCase();
    var list = this.L.filter(function (c) { return (S.field === 'All' || c.field === S.field) && (S.issuer === 'Anyone' || c.type === S.issuer) && (!q || (c.t + ' ' + c.skills.join(' ') + ' ' + c.issuer).toLowerCase().indexOf(q) > -1); });
    return {
      q: S.q, onQ: function (e) { self.setState({ q: e.target.value }); }, onSubmit: function (e) { e.preventDefault(); },
      fields: ['All', 'Data', 'Design', 'Cybersecurity', 'Business', 'AI', 'Finance'].map(function (f) { var on = S.field === f; return { label: f === 'All' ? 'All fields' : f, on: on ? 'true' : 'false', cls: on ? 'ct-f-on' : '', pick: function () { self.setState({ field: f }); } }; }),
      issuers: ['Anyone', 'Institutions', 'Creators'].map(function (f) { var on = S.issuer === f; return { label: f, on: on ? 'true' : 'false', cls: on ? 'ct-seg-on' : '', pick: function () { self.setState({ issuer: f }); } }; }),
      certs: list.map(function (c) { return { short: c.short, issuer: c.issuer, level: c.level, time: c.time, format: c.format, skills: c.skills, pre: c.pre, ok: c.ok, rev: !c.ok }; }),
      none: list.length === 0
    };
  }
}
'''
open('/home/user/credalio/design/canvas3/project/Certifications.dc.html','w').write(page('Certifications',css,top,body,script,1800))
