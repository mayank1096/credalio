exec(open('gen2.py').read())
FORM_CSS='''.ob-lab{display:block;font-size:13px;font-weight:600;color:#0B1433;margin:0 0 6px 2px;text-align:left}
.ob-f{width:100%;height:52px;box-sizing:border-box;padding:0 16px;border-radius:14px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:inherit;font-size:15px;color:#0B1433;outline:none;transition:border-color .2s ease,box-shadow .2s ease}
.ob-f:focus{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.ob-f::placeholder{color:#8A93AD}
textarea.ob-f{height:auto;padding:12px 16px;line-height:1.5;resize:none}
select.ob-f{appearance:none;-webkit-appearance:none;padding-right:40px;cursor:pointer}
.ob-sel{position:relative}
.ob-sel svg{position:absolute;right:14px;top:50%;transform:translateY(-50%);pointer-events:none}
.ob-help{display:block;font-size:12.5px;line-height:1.4;color:#5B6582;margin:6px 0 0 2px;text-align:left}
.ob-chip{transition:all .2s ease}
.ob-chip:hover{border-color:#AFC1F5 !important}
.ob-chip:focus-visible,.ob-x:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:2px}
@media (max-height: 760px) and (min-width: 961px){.ob-f{height:46px}textarea.ob-f{height:auto}.ob-grid2{row-gap:10px !important}.ob-header{height:72px !important}.ob-track{top:68px !important}.ob-main{top:120px !important}.ob-caps{display:none !important}.ob-help{margin-top:4px}}
@media (max-width: 960px){.ob-grid2,.ob-two{grid-template-columns:minmax(0,1fr) !important}.ob-grid4{grid-template-columns:minmax(0,1fr) !important}.ob-side{display:none !important}}
'''
CHEV='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#5B6582" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"></path></svg>'
def FIELD(id,label,ph='',help=None,typ='text',val=None,auto=None):
    v=f' value="{val}"' if val else ''
    a=f' autocomplete="{auto}"' if auto else ''
    h=f'<span class="ob-help">{help}</span>' if help else ''
    return f'<div style="text-align: left"><label for="{id}" class="ob-lab">{label}</label><input id="{id}" class="ob-f" type="{typ}" placeholder="{ph}"{v}{a}>{h}</div>'
def SELECT(id,label,opts,help=None,sel=None):
    o=''.join(f'<option{" selected" if x==sel else ""}>{x}</option>' for x in opts)
    h=f'<span class="ob-help">{help}</span>' if help else ''
    return f'<div style="text-align: left"><label for="{id}" class="ob-lab">{label}</label><div class="ob-sel"><select id="{id}" class="ob-f">{o}</select>{CHEV}</div>{h}</div>'
CK='<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg>'
SPARK='<svg width="14" height="14" viewBox="0 0 24 24" fill="#1652F0" aria-hidden="true"><path d="M12 2l1.9 6.1L20 10l-6.1 1.9L12 18l-1.9-6.1L4 10l6.1-1.9z"></path></svg>'
def ORB(size=40): return f'<span style="width: {size}px; height: {size}px; flex-shrink: 0; border-radius: 50%; background: radial-gradient(circle at 35% 30%, #5B8CFF 0%, #1652F0 55%, #0E3BB8 100%); box-shadow: 0 0 0 4px rgba(22, 82, 240, 0.12); display: flex; align-items: center; justify-content: center"><svg width="{int(size*0.45)}" height="{int(size*0.45)}" viewBox="0 0 24 24" fill="#FFFFFF" aria-hidden="true"><path d="M12 2l1.9 6.1L20 10l-6.1 1.9L12 18l-1.9-6.1L4 10l6.1-1.9z"></path></svg></span>'

# ---------- 003c Password
c=H1('Choose a password.')+'\n'+SUB('One last thing to keep your work safe.',460)+'\n'
c+='''<div class="ob-in3" style="margin-top: clamp(20px, 3.6vh, 32px); width: 100%; display: flex; flex-direction: column; gap: 14px; text-align: left">
<div><label for="pw" class="ob-lab">Password</label><div style="position: relative"><input id="pw" class="ob-f" type="{{pwType}}" value="{{pw}}" onChange="{{onPw}}" autocomplete="new-password" placeholder="Create a password" style="padding-right: 64px"><button type="button" class="ob-x" onClick="{{toggle}}" aria-label="Show password" style="position: absolute; right: 8px; top: 8px; height: 36px; padding: 0 12px; border: 0; border-radius: 10px; background: #F5F8FF; color: #1652F0; font-family: inherit; font-size: 13px; font-weight: 600; cursor: pointer">{{showLabel}}</button></div>
<div aria-hidden="true" style="margin-top: 10px; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 6px"><span style="height: 4px; border-radius: 4px; background: {{s1}}; transition: background .25s ease"></span><span style="height: 4px; border-radius: 4px; background: {{s2}}; transition: background .25s ease"></span><span style="height: 4px; border-radius: 4px; background: {{s3}}; transition: background .25s ease"></span></div>
<div role="status" style="margin-top: 10px; display: flex; flex-wrap: wrap; gap: 6px 16px; font-size: 13px">
<span style="display: flex; align-items: center; gap: 6px; color: {{r1.c}}"><span style="width: 18px; height: 18px; border-radius: 50%; background: {{r1.bg}}; color: #FFFFFF; display: flex; align-items: center; justify-content: center">'''+CK+'''</span>8+ characters</span>
<span style="display: flex; align-items: center; gap: 6px; color: {{r2.c}}"><span style="width: 18px; height: 18px; border-radius: 50%; background: {{r2.bg}}; color: #FFFFFF; display: flex; align-items: center; justify-content: center">'''+CK+'''</span>A number</span>
<span style="display: flex; align-items: center; gap: 6px; color: {{r3.c}}"><span style="width: 18px; height: 18px; border-radius: 50%; background: {{r3.bg}}; color: #FFFFFF; display: flex; align-items: center; justify-content: center">'''+CK+'''</span>A symbol</span>
</div></div>
<div><label for="pw2" class="ob-lab">Confirm password</label><input id="pw2" class="ob-f" type="{{pwType}}" value="{{pw2}}" onChange="{{onPw2}}" autocomplete="new-password" placeholder="Type it once more"><span class="ob-help" style="color: {{matchColor}}">{{matchText}}</span></div>
</div>
'''+BTN('CR-ONB-004.dc.html','Create my account','clamp(18px, 3vh, 26px)')
S003c='''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { pw: '', pw2: '', show: false }; }
  renderVals() {
    const { pw, pw2, show } = this.state;
    const r = [pw.length >= 8, /\\d/.test(pw), /[^A-Za-z0-9]/.test(pw)];
    const n = r.filter(Boolean).length;
    const segC = n === 3 ? '#0F6B45' : '#1652F0';
    const rule = (ok) => ({ c: ok ? '#0F6B45' : '#5B6582', bg: ok ? '#0F6B45' : '#D6DDEE' });
    const match = pw2.length === 0 ? '' : (pw2 === pw ? 'Passwords match.' : 'These don’t match yet.');
    return {
      pw, pw2, pwType: show ? 'text' : 'password', showLabel: show ? 'Hide' : 'Show',
      onPw: (e) => this.setState({ pw: e.target.value }), onPw2: (e) => this.setState({ pw2: e.target.value }),
      toggle: () => this.setState({ show: !show }),
      s1: n >= 1 ? segC : '#E6EAF3', s2: n >= 2 ? segC : '#E6EAF3', s3: n >= 3 ? segC : '#E6EAF3',
      r1: rule(r[0]), r2: rule(r[1]), r3: rule(r[2]),
      matchText: match, matchColor: pw2 === pw ? '#0F6B45' : '#5B6582'
    };
  }
}'''
make('CR-ONB-003c.dc.html','Credalio onboarding: choose a password',440,c,back='CR-ONB-003v.dc.html',login=False,script=S003c,step=(1,'Your account'),illh='clamp(140px, calc((37vh - 58px) / 0.65), min(40vh, 33.33vw))',extra_css=FORM_CSS)

# ---------- 004 About you
TZ=['WAT (UTC+1) · Lagos','GMT (UTC+0) · Accra / London','CAT (UTC+2) · Johannesburg','EAT (UTC+3) · Nairobi']
LANG=['English','French','Yoruba','Hausa','Igbo','Swahili','Arabic']
c=H1('Nice to meet you.')+'\n'+SUB('Tell us how you’d like to appear. You can change this anytime.',520)+'\n'
c+='<div class="ob-grid2 ob-in3" style="margin-top: clamp(20px, 3.6vh, 32px); display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px 16px; width: 100%">'
c+=FIELD('fn','First name','Ada',auto='given-name')+FIELD('ln','Last name','Ononuju',auto='family-name')
c+=FIELD('dn','Display name','Ada O.',help='This is how learners will see you.')+FIELD('ph','Phone <span style="font-weight: 500; color: #5B6582">(optional)</span>','+234 800 000 0000',typ='tel',auto='tel')
c+=SELECT('lg','Preferred language',LANG,sel='English')+SELECT('tz','Time zone <span style="font-weight: 500; color: #5B6582">· detected</span>',TZ,sel=TZ[0])
c+='</div>\n'+BTN('CR-ONB-005.dc.html','Continue','clamp(20px, 3.4vh, 28px)')
make('CR-ONB-004.dc.html','Credalio onboarding: about you',640,c,back='CR-ONB-003c.dc.html',login=False,step=(2,'About you'),illh='clamp(140px, calc((22vh - 1px) / 0.65), min(40vh, 33.33vw))',extra_css=FORM_CSS)

# ---------- 005 Expertise · your field
IND=['Choose an industry','Technology','Finance','Health','Education','Energy','Creative industries','Public sector']
c=H1('What do you know best?')+'\n'+SUB('This helps your Copilot speak your language. Learners will see it on your profile.',560)+'\n'
c+='<div class="ob-grid2 ob-in3" style="margin-top: clamp(20px, 3.6vh, 32px); display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px 16px; width: 100%">'
c+=SELECT('ind','Industry',IND,sel='Technology')+FIELD('dom','Domain','e.g. Data &amp; Analytics',val='Data &amp; Analytics')
c+=FIELD('spec','Specialization','e.g. Business Intelligence',val='Business Intelligence')
c+='''<div style="text-align: left"><span class="ob-lab" id="exp-l">Years of experience</span><div role="radiogroup" aria-labelledby="exp-l" style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 6px; padding: 4px; border-radius: 14px; background: #F5F8FF; border: 1.5px solid #E6EAF3"><sc-for list="{{exp}}" as="e" hint-placeholder-count="3"><button type="button" role="radio" aria-checked="{{e.on}}" class="ob-chip" onClick="{{e.pick}}" style="height: 40px; border: 0; border-radius: 10px; background: {{e.bg}}; color: {{e.fg}}; box-shadow: {{e.sh}}; font-family: inherit; font-size: 14px; font-weight: 600; cursor: pointer">{{e.label}}</button></sc-for></div></div>'''
c+='</div>\n'+BTN('CR-ONB-005b.dc.html','Continue','clamp(20px, 3.4vh, 28px)')
S005='''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { exp: 2 }; }
  renderVals() {
    const L = ['Under 3', '3 to 7', '8 or more'];
    const exp = L.map((label, i) => { const on = this.state.exp === i; return { label, on: on ? 'true' : 'false', pick: () => this.setState({ exp: i }), bg: on ? '#FFFFFF' : 'transparent', fg: on ? '#0B1433' : '#4A5578', sh: on ? '0 1px 3px rgba(11, 20, 51, 0.10)' : 'none' }; });
    return { exp };
  }
}'''
make('CR-ONB-005.dc.html','Credalio onboarding: your field',640,c,back='CR-ONB-004.dc.html',login=False,script=S005,step=(3,'Your expertise'),illh='clamp(140px, calc((38vh - 47px) / 0.65), min(40vh, 33.33vw))',extra_css=FORM_CSS)

# ---------- 005b Expertise · what you'll teach
c=H1('What will you teach?')+'\n'+SUB('Add a few topics and a line about you. Your Copilot builds from here.',620)+'\n'
c+='''<div class="ob-two ob-in3" style="margin-top: clamp(18px, 3.2vh, 28px); width: 100%; display: grid; grid-template-columns: minmax(0, 1fr) 340px; gap: 24px; align-items: start; text-align: left">
<div style="display: flex; flex-direction: column; gap: 14px">
<div><label for="topic" class="ob-lab">Topics you know well</label>
<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 6px; min-height: 52px; box-sizing: border-box; padding: 7px 8px; border-radius: 14px; border: 1.5px solid #D6DDEE; background: #FFFFFF">
<sc-for list="{{tags}}" as="t" hint-placeholder-count="3"><span style="display: inline-flex; align-items: center; gap: 4px; height: 34px; padding: 0 6px 0 12px; border-radius: 999px; background: #EAF0FF; color: #0E3BB8; font-size: 13.5px; font-weight: 600">{{t.label}}<button type="button" class="ob-x" onClick="{{t.remove}}" aria-label="Remove {{t.label}}" style="width: 24px; height: 24px; border: 0; border-radius: 50%; background: transparent; color: #0E3BB8; display: flex; align-items: center; justify-content: center; cursor: pointer"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"></path></svg></button></span></sc-for>
<input id="topic" value="{{draft}}" onChange="{{onDraft}}" onKeyDown="{{onKey}}" placeholder="Add a topic, then Enter" style="flex: 1 1 140px; min-width: 120px; height: 34px; border: 0; outline: none; font-family: inherit; font-size: 14.5px; color: #0B1433; background: transparent">
</div></div>
<div><label for="bio" class="ob-lab">A line about you</label><textarea id="bio" class="ob-f" rows="2" maxlength="280" onChange="{{onBio}}" value="{{bio}}" placeholder="What do you help people do?"></textarea><div style="display: flex; align-items: center; justify-content: space-between; gap: 12px; margin-top: 8px"><button type="button" class="ob-ghost" style="display: flex; align-items: center; gap: 8px; height: 36px; padding: 0 14px; border-radius: 999px; border: 1.5px dashed #CBD3E6; background: #FFFFFF; color: #3A4566; font-family: inherit; font-size: 13.5px; font-weight: 600; cursor: pointer"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#1652F0" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14M5 12h14"></path></svg>Add a credential <span style="font-weight: 500; color: #5B6582">· optional</span></button><span style="font-size: 12.5px; color: #5B6582">{{count}}/280</span></div></div>
</div>
<aside class="ob-side" aria-label="Profile preview" style="padding: 18px; border-radius: 20px; background: #F5F8FF; border: 1.5px solid #E6EAF3; display: flex; flex-direction: column; gap: 12px">
<span style="font-size: 11.5px; font-weight: 700; letter-spacing: 0.08em; color: #5B6582">HOW LEARNERS WILL SEE YOU</span>
<div style="display: flex; align-items: center; gap: 12px"><span style="width: 44px; height: 44px; border-radius: 50%; background: #1652F0; color: #FFFFFF; font-size: 15px; font-weight: 600; display: flex; align-items: center; justify-content: center">AO</span><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600; color: #0B1433">Ada Ononuju</span><span style="font-size: 12.5px; color: #4A5578">Business Intelligence · 8+ years</span></span></div>
<div style="display: flex; flex-wrap: wrap; gap: 6px"><sc-for list="{{tags}}" as="t" hint-placeholder-count="3"><span style="padding: 4px 10px; border-radius: 999px; background: #FFFFFF; border: 1px solid #D6DDEE; color: #3A4566; font-size: 12.5px; font-weight: 500">{{t.label}}</span></sc-for></div>
<p style="margin: 0; font-size: 13.5px; line-height: 1.5; color: #3A4566">{{bioShown}}</p>
</aside>
</div>
'''+BTN('CR-ONB-006.dc.html','Continue','clamp(18px, 3vh, 26px)')
S005b='''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { tags: ['Data Analysis', 'SQL', 'Business Intelligence'], draft: '', bio: 'I help professionals turn messy data into decisions. Analyst, SQL teacher and BI lead.' }; }
  renderVals() {
    const { tags, draft, bio } = this.state;
    const add = () => { const v = draft.trim(); if (v && !tags.includes(v)) this.setState({ tags: [...tags, v], draft: '' }); else this.setState({ draft: '' }); };
    return {
      tags: tags.map((label) => ({ label, remove: () => this.setState({ tags: tags.filter((x) => x !== label) }) })),
      draft, onDraft: (e) => this.setState({ draft: e.target.value }),
      onKey: (e) => { if (e.key === 'Enter' || e.key === ',') { e.preventDefault(); add(); } },
      bio, onBio: (e) => this.setState({ bio: e.target.value.slice(0, 280) }), count: bio.length,
      bioShown: bio || 'Your line will appear here.'
    };
  }
}'''
make('CR-ONB-005b.dc.html','Credalio onboarding: what you will teach',760,c,back='CR-ONB-005.dc.html',login=False,script=S005b,step=(3,'Your expertise'),illh='clamp(140px, calc((52vh - 261px) / 0.65), min(40vh, 33.33vw))',extra_css=FORM_CSS)

# ---------- 006 Meet your Copilot
c=H1('Meet your Copilot.')+'\n'+SUB('It already knows your expertise, and it will build alongside you.',520)+'\n'
c+='''<div class="ob-in3" style="margin-top: clamp(18px, 3.2vh, 28px); width: 100%; box-sizing: border-box; padding: 18px 20px; border-radius: 20px; background: #F5F8FF; border: 1.5px solid #E6EAF3; text-align: left; display: flex; gap: 14px">
'''+ORB(40)+'''
<div style="display: flex; flex-direction: column; gap: 8px; min-width: 0">
<span style="font-size: 14px; font-weight: 600; color: #0B1433">{{name}} <span style="font-weight: 500; color: #5B6582">· Creator Copilot</span></span>
<p style="margin: 0; font-size: 15px; line-height: 1.55; color: #0B1433">Hi Ada, I’m {{name}}. I already know your 8+ years in Data &amp; Analytics. Together we’ll shape courses, outcomes and assessments, and get your work ready for validation.</p>

</div></div>
<div class="ob-in3" style="margin-top: clamp(16px, 3vh, 24px); width: 100%; text-align: left">
<span class="ob-lab" id="nm-l">What would you like to call it?</span>
<div role="radiogroup" aria-labelledby="nm-l" style="display: flex; flex-wrap: wrap; gap: 8px; align-items: center">
<sc-for list="{{names}}" as="n" hint-placeholder-count="4"><button type="button" role="radio" aria-checked="{{n.on}}" class="ob-chip" onClick="{{n.pick}}" style="height: 44px; padding: 0 18px; border-radius: 999px; border: 1.5px solid {{n.bd}}; background: {{n.bg}}; color: {{n.fg}}; box-shadow: {{n.sh}}; font-family: inherit; font-size: 14.5px; font-weight: 600; cursor: pointer">{{n.label}}</button></sc-for>
<button type="button" class="ob-chip" onClick="{{surprise}}" style="height: 44px; padding: 0 16px; border-radius: 999px; border: 1.5px dashed #CBD3E6; background: #FFFFFF; color: #1652F0; font-family: inherit; font-size: 14.5px; font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 6px">'''+SPARK+'''Surprise me</button>
<input aria-label="Or type your own name" value="{{custom}}" onChange="{{onCustom}}" placeholder="Or type your own" class="ob-f" style="height: 44px; width: 160px; border-radius: 999px; font-size: 14.5px">
</div></div>
'''+BTN('CR-ONB-007.dc.html','<span>Continue with {{name}}</span>','clamp(18px, 3vh, 26px)')
S006='''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { names: ['Nova', 'Maya', 'Alex', 'Sage'], sel: 'Nova', custom: '' }; }
  renderVals() {
    const { names, sel, custom } = this.state;
    const pool = ['Atlas', 'Iris', 'Kai', 'Juno', 'Orion', 'Luma', 'Remy', 'Zara'];
    const name = custom.trim() || sel;
    return {
      name, custom, onCustom: (e) => this.setState({ custom: e.target.value.slice(0, 16) }),
      surprise: () => { const fresh = pool.filter((p) => !names.includes(p)).slice(0, 4); const next = fresh.length ? fresh : pool.slice(0, 4); this.setState({ names: next, sel: next[0], custom: '' }); },
      names: names.map((label) => { const on = !custom.trim() && sel === label; return { label, on: on ? 'true' : 'false', pick: () => this.setState({ sel: label, custom: '' }), bd: on ? '#1652F0' : '#E6EAF3', bg: on ? '#F5F8FF' : '#FFFFFF', fg: on ? '#0E3BB8' : '#0B1433', sh: on ? '0 0 0 4px rgba(22, 82, 240, 0.12)' : 'none' }; }),
      caps: ['Design courses', 'Write outcomes', 'Build curriculum', 'Create assessments', 'Improve content', 'Prepare for validation']
    };
  }
}'''
make('CR-ONB-006.dc.html','Credalio onboarding: meet your Copilot',720,c,back='CR-ONB-005b.dc.html',login=False,script=S006,step=(4,'Meet your Copilot'),illh='clamp(140px, calc((25vh - 55px) / 0.65), min(40vh, 33.33vw))',extra_css=FORM_CSS)

# ---------- 007 Copilot style
SV='<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
ICONS={'concise':SV+'<path d="M13 2 4 14h7l-1 8 9-12h-7z"></path></svg>','collab':SV+'<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"></path><path d="M8.5 12h.01M12 12h.01M15.5 12h.01"></path></svg>','detailed':SV+'<path d="M4 5h16M4 10h16M4 15h10M4 20h7"></path></svg>','proactive':SV+'<circle cx="11" cy="11" r="7"></circle><path d="m20 20-3.5-3.5"></path><path d="M11 8v6M8 11h6"></path></svg>'}
cards=''
for k,t,d in [('concise','Concise','Short, direct suggestions.'),('collab','Collaborative','Thinks it through with me and asks questions.'),('detailed','Detailed','Thorough explanations and reasons.'),('proactive','Proactive','Spots gaps and suggests fixes as I build.')]:
    cards+=f'''<button type="button" role="radio" class="ob-opt" onClick="{{{{o.{k}.pick}}}}" aria-checked="{{{{o.{k}.checked}}}}" style="display: flex; align-items: center; gap: 14px; padding: 16px; min-height: 84px; box-sizing: border-box; border-radius: 18px; border: 1.5px solid {{{{o.{k}.border}}}}; background: {{{{o.{k}.bg}}}}; box-shadow: {{{{o.{k}.shadow}}}}; cursor: pointer; text-align: left; font-family: inherit">
<span style="width: 46px; height: 46px; flex-shrink: 0; border-radius: 13px; background: {{{{o.{k}.iconBg}}}}; color: {{{{o.{k}.iconFg}}}}; display: flex; align-items: center; justify-content: center; transition: all .25s ease">{ICONS[k]}</span>
<span style="display: flex; flex-direction: column; gap: 3px; flex-grow: 1; min-width: 0"><span style="font-size: 17px; font-weight: 600; letter-spacing: -0.01em; color: #0B1433">{t}</span><span style="font-size: 13.5px; line-height: 1.35; color: #4A5578">{d}</span></span>
</button>'''
c=H1('How should Nova work with you?')+'\n'+SUB('Pick a style. You can change it anytime in your AI preferences.',520)+'\n'
c+='<div role="radiogroup" aria-label="Copilot working style" class="ob-grid4 ob-in3" style="margin-top: clamp(20px, 3.6vh, 32px); width: 100%; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 14px">'+cards+'</div>\n'
c+='''<div class="ob-in3" aria-live="polite" style="margin-top: 16px; width: 100%; max-width: 720px; display: flex; flex-direction: column; gap: 8px; text-align: left">
<div style="align-self: flex-end; max-width: 80%; padding: 10px 14px; border-radius: 16px 16px 4px 16px; background: #0B1433; color: #FFFFFF; font-size: 14px; line-height: 1.45">Can you look at my learning outcomes?</div>
<div style="display: flex; gap: 10px; align-items: flex-end">'''+ORB(28)+'''<div style="max-width: 85%; padding: 10px 14px; border-radius: 16px 16px 16px 4px; background: #F5F8FF; border: 1px solid #E6EAF3; color: #0B1433; font-size: 14px; line-height: 1.5">{{reply}}</div></div>
</div>
'''+BTN('#','Continue','clamp(16px, 3vh, 24px)')
S007='''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { sel: 'collab' }; }
  renderVals() {
    const sel = this.state.sel;
    const replies = {
      concise: 'Outcome 2 is vague. Try: “Write SQL joins to combine two tables.” The rest look good.',
      collab: 'Happy to. First, who is this for, analysts or managers? Outcome 2 reads differently for each. Shall we start there?',
      detailed: 'Sure. Outcomes 1 and 3 are measurable. Outcome 2 uses “understand”, which is hard to assess. I’d rewrite it with an action verb and a clear context, then check the sequence.',
      proactive: 'Done. I also noticed lesson 4 has no practice task for outcome 3. Want me to draft one?'
    };
    const o = {};
    ['concise', 'collab', 'detailed', 'proactive'].forEach((id) => {
      const on = sel === id;
      o[id] = { pick: () => this.setState({ sel: id }), checked: on ? 'true' : 'false', border: on ? '#1652F0' : '#E6EAF3', bg: on ? '#F5F8FF' : '#FFFFFF', shadow: on ? '0 0 0 4px rgba(22, 82, 240, 0.12), 0 12px 28px rgba(22, 82, 240, 0.14)' : '0 1px 2px rgba(11, 20, 51, 0.04)', iconBg: on ? '#1652F0' : '#EAF0FF', iconFg: on ? '#FFFFFF' : '#1652F0' };
    });
    return { o, reply: replies[sel] };
  }
}'''
make('CR-ONB-007.dc.html','Credalio onboarding: Copilot style',1080,c,back='CR-ONB-006.dc.html',login=False,script=S007,step=(4,'Meet your Copilot'),illh='clamp(140px, calc((52vh - 212px) / 0.65), min(40vh, 33.33vw))',extra_css=FORM_CSS)
