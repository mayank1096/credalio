from shell import *
CLOUD='/_blob/020f1a8593e80e5fcee9e0f06637f153'; WAVE='/_blob/3d4d999db1912d0cb0084365c58434d3'
I={'live':'<path d="M15 10l5-3v10l-5-3z"></path><rect x="3" y="6" width="12" height="12" rx="2"></rect>',
'proj':'<path d="M3 7h18v13H3zM8 7V4h8v3"></path>',
'mentor':'<circle cx="9" cy="8" r="3.5"></circle><path d="M2.5 20c1-3.5 3.5-5 6.5-5s5.5 1.5 6.5 5M16 4.5a3.5 3.5 0 0 1 0 7M18 15c2 .6 3.2 2.2 3.5 5"></path>',
'cert':'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"></path><path d="M9 12l2 2 4-4"></path>'}
css=r'''
.pg-hero{background:#FFFFFF url(CLOUD) center top / max(1440px,100%) auto no-repeat}
.pg-hin{max-width:960px;margin:0 auto;padding:72px 24px 40px;box-sizing:border-box;display:flex;flex-direction:column;align-items:center;text-align:center;gap:18px}
.pg-h1{margin:0;font-size:56px;line-height:1.04;font-weight:600;letter-spacing:-1.8px;color:#0B1433}
.pg-h1 em{font-style:normal;color:#1652F0}
.pg-sub{margin:0;max-width:640px;font-size:18px;line-height:1.55;color:#4A5578}
.pg-types{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin-top:10px}
.pg-t{height:36px;padding:0 15px;border-radius:10px;border:1px solid #E3E8F3;background:rgba(255,255,255,.8);font-family:'Google Sans',system-ui,sans-serif;font-size:14px;font-weight:500;color:#3A4566;cursor:pointer;transition:border-color .2s ease}
.pg-t:hover{border-color:#C9D7FA}
.pg-t-on{background:#0B1433;border-color:#0B1433;color:#FFFFFF}
.pg-body{max-width:1312px;margin:0 auto;padding:16px 48px 96px;box-sizing:border-box;display:flex;flex-direction:column;gap:20px}
.pg-feat{position:relative;isolation:isolate;overflow:hidden;display:grid;grid-template-columns:minmax(0,1fr) auto;align-items:end;gap:32px;padding:36px 40px;border-radius:24px;background:#0B1433;color:#FFFFFF;text-decoration:none;transition:transform .45s cubic-bezier(.2,.7,.2,1)}
.pg-feat::after{content:"";position:absolute;inset:0;z-index:-1;background:#0B1433 url(WAVE) center / cover no-repeat;transform:scale(1.5);transform-origin:0 35%;pointer-events:none}
.pg-feat:hover{transform:translateY(-3px)}
.pg-fk{display:flex;align-items:center;gap:10px;flex-wrap:wrap;font-size:13px;font-weight:500;color:#9DB8F7}
.pg-fk span{height:26px;padding:0 10px;border-radius:999px;background:rgba(255,255,255,.14);color:#FFFFFF;display:inline-flex;align-items:center;gap:6px}
.pg-fk i{width:7px;height:7px;border-radius:999px;background:#5FD49B;display:block}
.pg-ft{margin:12px 0 0;font-size:34px;line-height:1.1;font-weight:600;letter-spacing:-1px}
.pg-fd{margin:10px 0 0;max-width:620px;font-size:16px;line-height:1.55;color:rgba(255,255,255,.78)}
.pg-fm{display:flex;align-items:center;gap:18px;margin-top:18px;font-size:14px;color:rgba(255,255,255,.8)}
.pg-fm b{font-weight:600;color:#FFFFFF}
.pg-fgo{height:52px;padding:0 8px 0 22px;border-radius:999px;background:#FFFFFF;color:#0B1433;display:inline-flex;align-items:center;gap:12px;font-size:15px;font-weight:600;white-space:nowrap}
.pg-fgo i{width:38px;height:38px;border-radius:999px;background:#1652F0;display:flex;align-items:center;justify-content:center}
.pg-sh{display:flex;align-items:center;justify-content:space-between;margin-top:16px}
.pg-st{font-size:22px;font-weight:600;letter-spacing:-.4px;color:#0B1433}
.pg-n{font-size:14px;color:#8A93AD}
.pg-list{display:flex;flex-direction:column;gap:10px}
.pg-row{display:grid;grid-template-columns:72px minmax(0,1fr) auto 170px 40px;align-items:center;gap:24px;padding:16px 20px 16px 16px;border-radius:18px;background:#FFFFFF;border:1px solid #E3E8F3;text-decoration:none;color:#0B1433;transition:border-color .3s ease,box-shadow .4s ease,transform .4s cubic-bezier(.2,.7,.2,1)}
.pg-row:hover{border-color:#C9D7FA;box-shadow:0 24px 48px -36px rgba(22,82,240,.5);transform:translateY(-2px)}
.pg-date{width:72px;height:72px;border-radius:16px;background:#F5F8FF;display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1}
.pg-date b{font-size:26px;font-weight:600;letter-spacing:-.6px;color:#0B1433}
.pg-date > span{font-size:11px;font-weight:600;letter-spacing:1.4px;color:#1652F0;margin-top:5px}
.pg-any b{font-size:13px;letter-spacing:0}
.pg-rt{font-size:18px;font-weight:600;letter-spacing:-.3px;line-height:1.25}
.pg-rm{font-size:14px;color:#5B6582;margin-top:4px}
.pg-inc{display:flex;gap:6px}
.pg-ic{position:relative;width:34px;height:34px;border-radius:10px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.pg-ic-off{background:transparent;color:#CBD3E6}
.pg-ic:hover::after{content:attr(aria-label);position:absolute;left:50%;bottom:calc(100% + 8px);transform:translateX(-50%);padding:6px 10px;border-radius:8px;background:#0B1433;color:#FFFFFF;font-size:12px;white-space:nowrap;z-index:20}
.pg-stat{display:inline-flex;align-items:center;gap:7px;font-size:13px;font-weight:500;white-space:nowrap}
.pg-stat i{width:8px;height:8px;border-radius:999px;display:block}
.pg-go{width:40px;height:40px;border-radius:999px;border:1.5px solid #D6DDEE;display:flex;align-items:center;justify-content:center;color:#1652F0;transition:background .2s ease,border-color .2s ease}
.pg-row:hover .pg-go{background:#1652F0;border-color:#1652F0;color:#FFFFFF}
.pg-empty{padding:40px;border-radius:20px;background:#F5F8FF;text-align:center;font-size:15px;color:#5B6582}
.pg-ai{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,520px);gap:40px;align-items:center;margin-top:28px;padding:36px 40px;border-radius:24px;background:#FFFFFF url(CLOUD) center top / cover no-repeat;border:1px solid #E3E8F3}
.pg-al{display:flex;align-items:flex-start;gap:16px}
.pg-ah{margin:0;font-size:26px;line-height:1.15;font-weight:600;letter-spacing:-.6px;color:#0B1433}
.pg-ap{margin:6px 0 0;font-size:15px;line-height:1.55;color:#4A5578}
.pg-af{height:56px;box-sizing:border-box;padding:5px 5px 5px 20px;border-radius:999px;background:#FFFFFF;border:1.5px solid #D6DDEE;display:flex;align-items:center;gap:10px;box-shadow:0 20px 40px -30px rgba(11,20,51,.5)}
.pg-af:focus-within{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.pg-in{flex:1;min-width:0;height:100%;border:none;outline:none;background:transparent;font-family:'Google Sans',system-ui,sans-serif;font-size:15px;color:#0B1433}
.pg-in::placeholder{color:#8A93AD}
.pg-ab{height:44px;padding:0 6px 0 18px;border:none;border-radius:999px;background:#1652F0;color:#FFFFFF;font-family:'Google Sans',system-ui,sans-serif;font-size:14px;font-weight:600;display:flex;align-items:center;gap:10px;cursor:pointer;white-space:nowrap;flex-shrink:0}
.pg-ab:hover{background:#0E3BB8}
.pg-ab span{width:32px;height:32px;border-radius:999px;background:rgba(255,255,255,.18);display:flex;align-items:center;justify-content:center}
.pg-t:focus-visible,.pg-feat:focus-visible,.pg-row:focus-visible,.pg-ab:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:3px}
@media (max-width: 1180px){.pg-row{grid-template-columns:72px minmax(0,1fr) 160px 40px}.pg-inc{display:none}}
@media (max-width: 960px){.pg-ai{grid-template-columns:minmax(0,1fr);gap:22px;padding:30px}.pg-feat{grid-template-columns:minmax(0,1fr);gap:22px}.pg-fgo{justify-self:start}}
@media (max-width: 760px){
.pg-hero{background-size:auto 340px}
.pg-hin{padding:44px 20px 24px;gap:14px}
.pg-h1{font-size:32px;letter-spacing:-.9px}
.pg-sub{font-size:15px}
.pg-types{flex-wrap:nowrap;overflow-x:auto;justify-content:flex-start;align-self:stretch;margin:6px -20px 0;padding:0 20px;scrollbar-width:none}
.pg-types::-webkit-scrollbar{display:none}
.pg-t{flex-shrink:0;height:34px;font-size:13px}
.pg-body{padding:12px 20px 72px;gap:12px}
.pg-feat{padding:22px 20px;border-radius:20px;gap:18px}
.pg-ft{font-size:24px;letter-spacing:-.6px}
.pg-fd{font-size:14px}
.pg-fm{gap:12px;font-size:13px;flex-wrap:wrap}
.pg-fgo{height:48px;font-size:14px}
.pg-fgo i{width:34px;height:34px}
.pg-sh{margin-top:12px}
.pg-st{font-size:19px}
.pg-row{grid-template-columns:56px minmax(0,1fr);gap:14px;padding:12px 14px 12px 12px;border-radius:16px}
.pg-date{width:56px;height:56px;border-radius:13px}
.pg-date b{font-size:20px}
.pg-date > span{font-size:10px;margin-top:3px}
.pg-rt{font-size:15px}
.pg-rm{font-size:12.5px;margin-top:2px}
.pg-stat{grid-column:2;font-size:12px;margin-top:-10px}
.pg-go{display:none}
.pg-by{display:none}
.pg-ai{padding:24px 20px 20px;border-radius:20px;background-size:auto 300px;margin-top:16px}
.pg-ah{font-size:21px}
.pg-ap{font-size:14px}
.pg-af{flex-direction:column;align-items:stretch;height:auto;padding:0;gap:10px;border:none;background:none;box-shadow:none;border-radius:0}
.pg-af:focus-within{box-shadow:none}
.pg-in{flex:none;height:50px;box-sizing:border-box;padding:0 18px;border-radius:999px;background:#FFFFFF;border:1.5px solid #D6DDEE}
.pg-ab{height:50px;justify-content:space-between;padding:0 6px 0 20px;font-size:15px}
.pg-ab span{width:38px;height:38px}
}
'''.replace('CLOUD',CLOUD).replace('WAVE',WAVE)
def ic(k): return '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>'%I[k]
inc=''.join('<span class="pg-ic {{p.%s}}" role="img" aria-label="%s">%s</span>'%(k,lab,ic(k)) for k,lab in [('live','Live sessions'),('proj','Projects'),('mentor','Mentorship'),('cert','Certificate')])
top='''<div class="pg-hero">
%s
<div class="pg-hin">
<h1 class="pg-h1">Go deeper, <em>together</em>.</h1>
<p class="pg-sub">Live, expert-led programs with real projects and a cohort beside you.</p>
<div class="pg-types" role="group" aria-label="Program type">
<sc-for list="{{types}}" as="t" hint-placeholder-count="7"><button class="pg-t {{t.cls}}" type="button" aria-pressed="{{t.on}}" onClick="{{t.pick}}">{{t.label}}</button></sc-for>
</div>
</div>
</div>'''%nav('Explore learning')
body='''<div class="pg-body">
<sc-if value="{{showFeat}}" hint-placeholder-val="{{ true }}">
<a class="pg-feat" href="#">
<div>
<div class="pg-fk">Next cohort<span><i></i>Places available</span></div>
<h2 class="pg-ft">AI &amp; Data Analytics Accelerator</h2>
<p class="pg-fd">Twelve weeks of live, mentored learning, from data basics to applied AI, ending with a capstone you can show employers.</p>
<div class="pg-fm"><span>Starts <b>18 January</b></span><span><b>12 weeks</b></span><span>Northgate University</span></div>
</div>
<span class="pg-fgo">See program<i aria-hidden="true">%s</i></span>
</a>
</sc-if>
<div class="pg-sh"><span class="pg-st">Upcoming programs</span><span class="pg-n">{{count}}</span></div>
<div class="pg-list">
<sc-for list="{{progs}}" as="p" hint-placeholder-count="8">
<a class="pg-row" href="#">
<span class="pg-date {{p.dcls}}" aria-label="{{p.when}}"><b>{{p.d}}</b><span>{{p.m}}</span></span>
<span><span class="pg-rt" style="display: block">{{p.t}}</span><span class="pg-rm" style="display: block">{{p.meta}}<span class="pg-by"> · {{p.by}}</span></span></span>
<span class="pg-inc">%s</span>
<span class="pg-stat" style="color: {{p.sc}}"><i style="background: {{p.sd}}"></i>{{p.status}}</span>
<span class="pg-go" aria-hidden="true">%s</span>
</a>
</sc-for>
<sc-if value="{{none}}" hint-placeholder-val="{{ false }}"><div class="pg-empty">No programs of this type are open right now.</div></sc-if>
</div>
<section class="pg-ai" aria-labelledby="pg-ai-h">
<div class="pg-al"><span class="sx-orb" style="width: 44px; height: 44px; box-shadow: 0 0 0 6px rgba(22,82,240,.08),0 10px 24px -8px rgba(22,82,240,.6)" aria-hidden="true"></span><div><h2 id="pg-ai-h" class="pg-ah">Is a program right for you?</h2><p class="pg-ap">Your AI Coach compares programs with self‑paced options for your time and goal.</p></div></div>
<form class="pg-af" onSubmit="{{onSubmit}}"><label for="pg-goal" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Your goal</label><input id="pg-goal" class="pg-in" type="text" placeholder="I have about 5 hours a week…" autocomplete="off"><button class="pg-ab" type="submit">Compare for me<span aria-hidden="true">%s</span></button></form>
</section>
</div>
%s'''%(ARROW%(15,15,'#FFFFFF'), inc, ARROW%(15,15,'currentColor'), ARROW%(14,14,'#FFFFFF'), FOOT)
script=r'''
class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { type: 'All' };
    var P = function (t, type, len, by, d, m, inc, st) { return { t: t, type: type, len: len, by: by, d: d, m: m, inc: inc, st: st }; };
    this.L = [
      P('Applied Project Leadership', 'Institution', '10 weeks', 'Westbridge Institute', '12', 'JAN', 'lpmc', 'apps'),
      P('AI & Data Analytics Accelerator', 'Accelerator', '12 weeks', 'Northgate University', '18', 'JAN', 'lpmc', 'open'),
      P('Frontend Engineering Bootcamp', 'Bootcamp', '16 weeks', 'Mia Lopez', '19', 'JAN', 'lpm', 'open'),
      P('Product Design Cohort', 'Cohort', '10 weeks', 'Lena Fischer', '26', 'JAN', 'lpm', 'open'),
      P('AI for Business Leaders', 'Executive', '6 weeks', 'Northgate University', '2', 'FEB', 'lmc', 'wait'),
      P('Clinical Data Programme', 'Institution', '24 weeks', 'City University', '9', 'FEB', 'pmc', 'apps'),
      P('Executive Leadership in the AI Era', 'Executive', '6 weeks', 'Westbridge Institute', '23', 'FEB', 'lc', 'wait'),
      P('Cloud & Security Pathway', 'Self-paced', '5 courses', 'Westbridge Institute', '', '', 'pc', 'any')
    ];
    this.ST = { open: ['Places available', '#0F6B45', '#1E9E63'], apps: ['Applications open', '#1652F0', '#1652F0'], wait: ['Waitlist open', '#8A4F00', '#D9A21B'], any: ['Start any time', '#1652F0', '#1652F0'] };
    this.NAMES = { Accelerator: 'Accelerator', Institution: 'Institution program', Bootcamp: 'Bootcamp', Cohort: 'Cohort program', Executive: 'Executive learning', 'Self-paced': 'Self-paced program' };
  }
  renderVals() {
    var self = this, S = this.state;
    var list = this.L.filter(function (p) { return S.type === 'All' || p.type === S.type; });
    return {
      types: ['All', 'Cohort', 'Bootcamp', 'Accelerator', 'Institution', 'Executive', 'Self-paced'].map(function (t) { var on = S.type === t; return { label: t === 'All' ? 'All programs' : t, on: on ? 'true' : 'false', cls: on ? 'pg-t-on' : '', pick: function () { self.setState({ type: t }); } }; }),
      showFeat: S.type === 'All' || S.type === 'Accelerator',
      count: list.length + (list.length === 1 ? ' program' : ' programs'),
      progs: list.map(function (p) { var st = self.ST[p.st]; return { t: p.t, meta: self.NAMES[p.type] + ' · ' + p.len, by: p.by, d: p.d || 'Any', m: p.m || 'TIME', dcls: p.d ? '' : 'pg-any', when: p.d ? 'Starts ' + p.d + ' ' + p.m : 'Start any time', status: st[0], sc: st[1], sd: st[2],
        live: p.inc.indexOf('l') > -1 ? '' : 'pg-ic-off', proj: p.inc.indexOf('p') > -1 ? '' : 'pg-ic-off', mentor: p.inc.indexOf('m') > -1 ? '' : 'pg-ic-off', cert: p.inc.indexOf('c') > -1 ? '' : 'pg-ic-off' }; }),
      none: list.length === 0,
      onSubmit: function (e) { e.preventDefault(); }
    };
  }
}
'''
open('/home/user/credalio/design/canvas3/project/Programs.dc.html','w').write(page('Learning Programs',css,'',top+'\n'+body,script,2000))
