# Batch: 008 ready + Start creating (DASH-NEW, CREATE-001, CREATE-002A, CREATE-002Ab)
exec(open('gen2.py').read())
FORM_CSS = ''
# ---------- 008 Ready to create (onboarding frame)
CK='<span style="width: 26px; height: 26px; flex-shrink: 0; border-radius: 50%; background: #E7F5EE; color: #0F6B45; display: flex; align-items: center; justify-content: center"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg></span>'
SPK='<span style="width: 26px; height: 26px; flex-shrink: 0; border-radius: 50%; background: #EAF0FF; color: #1652F0; display: flex; align-items: center; justify-content: center"><svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l1.9 6.1L20 10l-6.1 1.9L12 18l-1.9-6.1L4 10l6.1-1.9z"></path></svg></span>'
def ROW(icon,label,value,sub=None,first=False):
    return f'''<li class="rd-row" style="display: grid; grid-template-columns: 26px 140px minmax(0, 1fr); align-items: center; gap: 14px; padding: 13px 0; {'' if first else 'border-top: 1px solid #E6EAF3; '}">{icon}<span style="font-size: 14px; color: #5B6582">{label}</span><span style="display: flex; flex-direction: column; gap: 2px; min-width: 0"><span style="font-size: 15px; font-weight: 600; color: #0B1433">{value}</span>'''+(f'<span style="font-size: 13px; color: #5B6582">{sub}</span>' if sub else '')+'</span></li>'
c=H1('You’re ready to create.')+'\n'+SUB('Your creator setup is complete. Here’s what you’re starting with.',520)+'\n'
c+='<ul class="ob-in3" aria-label="Your setup" style="list-style: none; margin: clamp(18px, 3vh, 26px) 0 0 0; padding: 6px 22px; width: 100%; box-sizing: border-box; border-radius: 20px; border: 1.5px solid #E6EAF3; background: #FFFFFF; box-shadow: 0 1px 2px rgba(11, 20, 51, 0.04), 0 18px 40px rgba(11, 20, 51, 0.05); text-align: left">'
c+=ROW(CK,'Creator profile','Ada Ononuju',first=True)+ROW(CK,'Expertise','Data &amp; Analytics · Data Analysis, SQL')+ROW(CK,'Your Copilot','Nova · Collaborative')+ROW(SPK,'Starter AI Tokens','20,000 for Nova','Powers Nova’s help. Top up anytime with Credits.')
c+='</ul>\n<p class="ob-in3" style="margin: 14px 0 0 0; max-width: 520px; font-size: 13.5px; line-height: 1.5; color: #5B6582; text-align: center">Identity, credentials, a short orientation and our policies come later, before validation. They never stop you building.</p>\n'
c+=BTN('CR-DASH-NEW.dc.html','Go to my Creator Studio','clamp(16px, 2.6vh, 24px)')
RD_CSS='@media (max-width: 960px){.rd-row{grid-template-columns:26px minmax(0,1fr) !important;row-gap:2px !important}.rd-row > span:nth-child(2){grid-column:2}.rd-row > span:nth-child(3){grid-column:2}}\n@media (max-height: 760px) and (min-width: 961px){.rd-row{padding:9px 0 !important}.ob-header{height:72px !important}.ob-track{top:68px !important}.ob-main{top:120px !important}}\n'
make('CR-ONB-008.dc.html','Credalio onboarding: ready to create',600,c,back='CR-ONB-007.dc.html',login=False,step=(5,'Ready to create'),illh='clamp(140px, calc((20vh - 12px) / 0.65), min(40vh, 33.33vw))',extra_css=RD_CSS)
print('008 built')

# ---------- dashboard screens
exec(open('dash.py').read())
NOVA_TXT='Tell me what you want people to come away with. One skill or subject usually means a Course. Proving competence against a standard is a Professional Certification. A route to a role is a Career Path. A group learning together over weeks is a Learning Program.'
TYPES=[('course','Course','Build a structured learning experience around a subject or skill.'),('cert','Professional Certification','Assess and verify professional competencies.'),('path','Career Path','Create a structured journey toward a career outcome.'),('program','Learning Program','Deliver coordinated learning over a structured period.')]
cards=''
for k,t,d in TYPES:
    cards+=f'''<a href="CR-CREATE-001.dc.html" class="dn-type"><span class="dn-tile">{ICON(I[k],24,1.7)}</span><span style="display: block; margin-top: 16px; font-size: 17px; font-weight: 600; letter-spacing: -0.01em; color: #0B1433">{t}</span><span style="display: block; margin-top: 6px; font-size: 14px; line-height: 1.5; color: #4A5578; flex-grow: 1">{d}</span><span class="dn-go">Create {ICON(I["arrow"],16,2.2)}</span></a>'''
def PILL(t,kind):
    c={'ok':('#E7F5EE','#0F6B45'),'todo':('#F1F3F8','#4A5578'),'warn':('#FFF4DE','#8A5A00')}[kind]
    return f'<span style="flex-shrink: 0; height: 26px; padding: 0 10px; border-radius: 999px; background: {c[0]}; color: {c[1]}; font-size: 12.5px; font-weight: 600; display: inline-flex; align-items: center; white-space: nowrap">{t}</span>'
def RROW(label,pill,done=False):
    ic = '<span style="width: 22px; height: 22px; flex-shrink: 0; border-radius: 50%; background: #0F6B45; color: #FFFFFF; display: flex; align-items: center; justify-content: center">'+ICON(I['check'],12,3.2)+'</span>' if done else '<span style="width: 22px; height: 22px; flex-shrink: 0; box-sizing: border-box; border-radius: 50%; border: 2px solid #CBD3E6"></span>'
    return f'<li style="display: flex; align-items: center; gap: 12px; padding: 12px 0; border-top: 1px solid #E6EAF3">{ic}<span style="flex-grow: 1; min-width: 0; font-size: 14.5px; color: #0B1433">{label}</span>{pill}</li>'
RING='''<svg width="64" height="64" viewBox="0 0 64 64" aria-hidden="true" style="flex-shrink: 0"><circle cx="32" cy="32" r="26" fill="none" stroke="#EAF0FF" stroke-width="7"></circle><circle cx="32" cy="32" r="26" fill="none" stroke="#1652F0" stroke-width="7" stroke-linecap="round" pathLength="1" stroke-dasharray="0.4 1" transform="rotate(-90 32 32)" style="animation: dsRing 1.1s cubic-bezier(.3,.8,.3,1) .3s both"></circle><text x="32" y="37" text-anchor="middle" font-family="Google Sans, system-ui, sans-serif" font-size="15" font-weight="600" fill="#0B1433">40%</text></svg>'''
c=f'''<section class="ob-in" style="margin-top: 8px">
<h1 class="ds-h1">Welcome to your Studio, Ada.</h1>
<p class="ds-sub">Turn what you know into learning people trust.</p>
</section>
<section class="ds-card ob-in2" aria-labelledby="dn-create" style="margin-top: 24px; padding: 24px">
<div style="display: flex; align-items: center; justify-content: space-between; gap: 12px; flex-wrap: wrap">
<h2 id="dn-create" style="margin: 0; font-size: 20px; font-weight: 600; letter-spacing: -0.015em">What would you like to create?</h2>
<button type="button" class="ds-ghost" onClick="{{{{toggleAsk}}}}" aria-expanded="{{{{askOpen}}}}" style="height: 44px; padding: 0 16px 0 6px; font-size: 14px">{NOVA_AV(32, False)}Not sure? Ask Nova</button>
</div>
<sc-if value="{{{{askShown}}}}" hint-placeholder-val="{{{{false}}}}"><div class="cp-pop" role="status" style="margin-top: 16px; display: flex; align-items: flex-start; gap: 12px">{NOVA_AV(36)}<p style="margin: 0; max-width: 760px; padding: 14px 16px; border-radius: 6px 18px 18px 18px; background: #F5F8FF; border: 1.5px solid #E6EAF3; font-size: 15px; line-height: 1.55; color: #0B1433">{NOVA_TXT}</p></div></sc-if>
<div class="dn-grid" style="margin-top: 18px; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 14px">{cards}</div>
</section>
<div class="dn-row ob-in3" style="margin-top: 18px; display: grid; grid-template-columns: minmax(0, 1.15fr) minmax(0, 1fr); gap: 18px; align-items: start">
<section class="ds-card" aria-labelledby="dn-ready" style="padding: 22px 24px">
<div style="display: flex; align-items: center; gap: 16px">{RING}<div style="min-width: 0"><h2 id="dn-ready" style="margin: 0; font-size: 18px; font-weight: 600; letter-spacing: -0.01em">Your creator readiness</h2><p style="margin: 4px 0 0 0; font-size: 14px; line-height: 1.5; color: #4A5578">It never stops you drafting. It’s needed before validation and publishing.</p></div></div>
<ul style="list-style: none; margin: 16px 0 0 0; padding: 0">{RROW('Creator profile',PILL('Complete','ok'),True)}{RROW('Identity verification',PILL('Not started','todo'))}{RROW('Professional credentials',PILL('Added · not verified','warn'))}{RROW('Creator Orientation',PILL('Not started','todo'))}{RROW('Policies',PILL('Not started','todo'))}</ul>
<a href="#" class="ds-link" style="margin-top: 8px">Continue setup {ICON(I["arrow"],16,2.2)}</a>
</section>
<section class="ds-card" aria-labelledby="dn-nova" style="padding: 22px 24px; background: #FFFFFF url(/_blob/d268046654a4206d2a726e62005bcc59) center top / 100% auto no-repeat">
<div style="display: flex; align-items: center; gap: 14px">{NOVA_AV(52)}<div><h2 id="dn-nova" style="margin: 0; font-size: 18px; font-weight: 600">Nova</h2><span style="display: flex; align-items: center; gap: 6px; margin-top: 2px; font-size: 13.5px; color: #4A5578"><span style="width: 8px; height: 8px; border-radius: 50%; background: #0F6B45"></span>Your Creator Copilot · Collaborative</span></div></div>
<p style="margin: 16px 0 0 0; padding: 14px 16px; border-radius: 6px 18px 18px 18px; background: #FFFFFF; border: 1.5px solid #E6EAF3; font-size: 15px; line-height: 1.55; color: #0B1433">I can help you decide what to create, or we can start one together.</p>
<div style="margin-top: 14px; display: flex; flex-wrap: wrap; gap: 8px"><button type="button" class="ds-chip" onClick="{{{{openAsk}}}}">Help me choose what to create</button><a href="CR-CREATE-002A.dc.html" class="ds-chip" style="text-decoration: none">Explore a course idea</a><button type="button" class="ds-chip">Explain validation</button><button type="button" class="ds-chip">Help me finish readiness</button></div>
</section>
</div>'''
DN_CSS='''.dn-type{display:flex;flex-direction:column;min-height:228px;box-sizing:border-box;padding:20px;border-radius:18px;border:1.5px solid #E6EAF3;background:#FFFFFF;text-decoration:none;transition:border-color .25s ease,transform .25s ease,box-shadow .25s ease}
.dn-type:hover{border-color:#AFC1F5;transform:translateY(-2px);box-shadow:0 14px 32px rgba(22,82,240,.10)}
.dn-type:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:2px}
.dn-tile{width:48px;height:48px;border-radius:14px;background:#EAF0FF;color:#1652F0;display:flex;align-items:center;justify-content:center;transition:all .25s ease}
.dn-type:hover .dn-tile{background:#1652F0;color:#FFFFFF}
.dn-go{display:inline-flex;align-items:center;gap:6px;margin-top:16px;color:#1652F0;font-size:14.5px;font-weight:600}
.dn-go svg{transition:transform .25s ease}.dn-type:hover .dn-go svg{transform:translateX(3px)}
@media (max-width: 1180px){.dn-grid{grid-template-columns:repeat(2,minmax(0,1fr)) !important}.dn-type{min-height:0}}
@media (max-width: 1080px){.dn-row{grid-template-columns:minmax(0,1fr) !important}}
@media (max-width: 960px){.ds-card{border-radius:18px}section.ds-card{padding:18px !important}}
@media (max-width: 560px){.dn-grid{grid-template-columns:minmax(0,1fr) !important;gap:10px !important}.dn-type{flex-direction:row !important;flex-wrap:wrap;align-items:center;column-gap:14px;padding:16px}.dn-type > span:nth-child(2){margin-top:0 !important;flex:1 1 0}.dn-type > span:nth-child(3){flex-basis:100%;margin-top:8px !important}.dn-go{display:none}}
'''
S_DN='''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { nav: false, ask: false }; }
  renderVals() {
    return { NAVJS,
      askShown: this.state.ask, askOpen: this.state.ask ? 'true' : 'false',
      toggleAsk: () => this.setState({ ask: !this.state.ask }), openAsk: () => this.setState({ ask: true }) };
  }
}'''.replace('NAVJS',NAV_JS)
open(P+'CR-DASH-NEW.dc.html','w').write(SHELL('Dashboard',c,'Credalio · Creator Studio',S_DN,DN_CSS,1000))
print('DASH-NEW built')

# ---------- CREATE-001
CHAR=f'<div class="c1-char" aria-hidden="true" style="position: absolute; right: 6px; bottom: -10px; width: 170px; aspect-ratio: 200 / 450; overflow: hidden; mix-blend-mode: multiply; -webkit-mask-image: linear-gradient(to bottom, #000 82%, transparent); mask-image: linear-gradient(to bottom, #000 82%, transparent)"><img src="{IMG}" alt="" style="position: absolute; left: -672.5%; top: -37.78%; width: 1086%; max-width: none; height: auto; "></div>'
c=f'''<a href="CR-DASH-NEW.dc.html" class="ds-back ob-in" style="margin-top: 4px">{ICON(I["back"],16,2.2)}Dashboard</a>
<h1 class="ds-h1 ob-in" style="margin-top: 10px">How would you like to create your course?</h1>
<p class="ds-sub ob-in2">Pick a starting point. You can switch at any time.</p>
<div class="c1-grid ob-in3" style="margin-top: 28px; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 18px">
<article class="ds-card c1-card" style="position: relative; overflow: hidden; padding: 28px; min-height: 380px; display: flex; flex-direction: column; border-color: #1652F0; box-shadow: 0 0 0 4px rgba(22, 82, 240, 0.10), 0 18px 40px rgba(22, 82, 240, 0.10); background: #FFFFFF url(/_blob/d268046654a4206d2a726e62005bcc59) center top / 100% auto no-repeat">
{CHAR}
<span style="align-self: flex-start; height: 28px; padding: 0 12px; border-radius: 999px; background: #FFFFFF; border: 1.5px solid #AFC1F5; color: #0E3BB8; font-size: 12.5px; font-weight: 600; display: inline-flex; align-items: center; gap: 6px"><svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l1.9 6.1L20 10l-6.1 1.9L12 18l-1.9-6.1L4 10l6.1-1.9z"></path></svg>Recommended</span>
<h2 style="margin: 18px 0 0 0; font-size: 24px; font-weight: 600; letter-spacing: -0.02em">Create with Nova</h2>
<p class="c1-txt" style="margin: 10px 0 0 0; max-width: 340px; font-size: 15.5px; line-height: 1.55; color: #3A4566">Tell Nova what learners should achieve. Nova drafts the first structure, and you approve every part before it reaches the Studio.</p>
<ul class="c1-txt" style="list-style: none; margin: 16px 0 0 0; padding: 0; display: flex; flex-direction: column; gap: 8px; font-size: 14px; color: #3A4566"><li style="display: flex; align-items: center; gap: 8px"><span style="color: #1652F0; display: flex">{ICON(I["check"],16,2.6)}</span>Five short questions</li><li style="display: flex; align-items: center; gap: 8px"><span style="color: #1652F0; display: flex">{ICON(I["check"],16,2.6)}</span>A first draft to review</li><li style="display: flex; align-items: center; gap: 8px"><span style="color: #1652F0; display: flex">{ICON(I["check"],16,2.6)}</span>Nothing changes without you</li></ul>
<span style="flex-grow: 1; min-height: 20px"></span>
{BTNA("CR-CREATE-002A.dc.html","Start with Nova",extra='style="align-self: flex-start; position: relative"')}
</article>
<article class="ds-card c1-card" style="padding: 28px; min-height: 380px; display: flex; flex-direction: column">
<span style="width: 52px; height: 52px; border-radius: 15px; background: #F1F3F8; color: #3A4566; display: flex; align-items: center; justify-content: center">{ICON(I["pencil"],24,1.7)}</span>
<h2 style="margin: 18px 0 0 0; font-size: 24px; font-weight: 600; letter-spacing: -0.02em">Build from scratch</h2>
<p style="margin: 10px 0 0 0; max-width: 360px; font-size: 15.5px; line-height: 1.55; color: #3A4566">Start with a blank course and set up every part yourself. Nova stays one click away on every screen.</p>
<span style="flex-grow: 1; min-height: 20px"></span>
<a href="#" class="ds-ghost" style="align-self: flex-start">Start from scratch</a>
</article>
</div>'''
C1_CSS='''@media (max-width: 860px){.c1-grid{grid-template-columns:minmax(0,1fr) !important}.c1-card{min-height:0 !important;padding:22px !important}.c1-card .ds-btn,.c1-card .ds-ghost{align-self:stretch !important}.c1-char{width:120px !important;right:-6px !important;top:24px;bottom:auto !important}.c1-txt{max-width:calc(100% - 96px) !important}}
'''
S_C1='class Component extends DCLogic {\n  constructor(props) { super(props); this.state = { nav: false }; }\n  renderVals() { return { NAVJS }; }\n}'.replace('NAVJS',NAV_JS)
open(P+'CR-CREATE-001.dc.html','w').write(SHELL('Create new',c,'Credalio · How would you like to create?',S_C1,C1_CSS,820))
print('CREATE-001 built')

# ---------- CREATE-002A / 002Ab (one source, variant prop)
SEG='<div aria-hidden="true" style="display: grid; grid-template-columns: repeat(5, 28px); gap: 5px"><sc-for list="{{segs}}" as="s" hint-placeholder-count="5"><span style="height: 4px; border-radius: 4px; background: {{s.c}}"></span></sc-for></div>'
OPT='<button type="button" class="ds-opt" onClick="{{r.X.pick}}" aria-pressed="{{r.X.on}}" style="height: 36px; padding: 0 12px; box-sizing: border-box; border-radius: 12px; border: 1.5px solid {{r.X.bd}}; background: {{r.X.bg}}; color: {{r.X.fg}}; font-family: inherit; font-size: 13.5px; font-weight: 600; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; gap: 6px; white-space: nowrap; transition: all .2s ease"><span style="display: {{r.X.ckd}}; color: #1652F0">'+ICON(I['check'],13,3)+'</span>{{r.X.label}}</button>'
c=f'''<a href="CR-CREATE-001.dc.html" class="ds-back ob-in" style="margin-top: 4px">{ICON(I["back"],16,2.2)}Back</a>
<div class="c2-head ob-in" style="margin-top: 10px; display: flex; align-items: flex-end; justify-content: space-between; gap: 20px; flex-wrap: wrap">
<div><h1 class="ds-h1">Create with Nova</h1><p class="ds-sub" style="max-width: 600px">A short conversation, then a draft for you to review. Nothing enters the Studio until you accept it.</p></div>
<div style="display: flex; flex-direction: column; align-items: flex-end; gap: 8px"><span style="font-size: 13.5px; color: #5B6582">{{{{progress}}}}</span>{SEG}</div>
</div>
<div class="c2-grid ob-in2" style="margin-top: 24px; display: grid; grid-template-columns: minmax(0, 1fr) 320px; gap: 18px; align-items: start">
<section class="ds-card" aria-label="Conversation with Nova" style="display: flex; flex-direction: column; overflow: hidden">
<div aria-live="polite" style="padding: 24px; display: flex; flex-direction: column; gap: 14px; min-height: 300px">
<sc-for list="{{{{msgs}}}}" as="m" hint-placeholder-count="2"><div class="cp-pop" style="display: {{{{m.nd}}}}; align-items: flex-end; gap: 10px">{NOVA_AV(32, False)}<div style="max-width: min(560px, 82%); padding: 12px 16px; border-radius: 18px 18px 18px 6px; background: #F5F8FF; border: 1.5px solid #E6EAF3; font-size: 15.5px; line-height: 1.55; color: #0B1433">{{{{m.text}}}}</div></div><div class="cp-pop" style="display: {{{{m.md}}}}; justify-content: flex-end"><div style="max-width: min(520px, 82%); padding: 12px 16px; border-radius: 18px 18px 6px 18px; background: #0B1433; font-size: 15.5px; line-height: 1.55; color: #FFFFFF">{{{{m.text}}}}</div></div><div style="display: {{{{m.dd}}}}; align-items: flex-end; gap: 10px">{NOVA_AV(32, False)}<div aria-label="Nova is typing" style="padding: 16px 18px; border-radius: 18px 18px 18px 6px; background: #F5F8FF; border: 1.5px solid #E6EAF3; display: inline-flex; gap: 5px"><span class="cp-dot"></span><span class="cp-dot" style="animation-delay: .15s"></span><span class="cp-dot" style="animation-delay: .3s"></span></div></div></sc-for>
</div>
<sc-if value="{{{{composerShown}}}}" hint-placeholder-val="{{{{true}}}}"><div style="padding: 16px 20px 20px 20px; border-top: 1.5px solid #E6EAF3; background: #FFFFFF">
<div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 12px"><sc-for list="{{{{chips}}}}" as="ch" hint-placeholder-count="3"><button type="button" class="ds-chip cp-pop" onClick="{{{{ch.pick}}}}">{{{{ch.label}}}}</button></sc-for></div>
<div style="display: flex; align-items: center; gap: 8px; height: 52px; box-sizing: border-box; padding: 0 6px 0 18px; border-radius: 999px; border: 1.5px solid #D6DDEE; background: #FFFFFF"><label class="sr-only" for="c2-in">Your answer</label><input id="c2-in" value="{{{{text}}}}" onChange="{{{{onText}}}}" onKeyDown="{{{{onKey}}}}" placeholder="Type your answer" autocomplete="off" style="flex-grow: 1; min-width: 0; border: 0; outline: none; background: transparent; font-family: inherit; font-size: 15px; color: #0B1433"><button type="button" onClick="{{{{sendText}}}}" aria-label="Send" style="width: 40px; height: 40px; flex-shrink: 0; border: 0; border-radius: 50%; background: {{{{sendBg}}}}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: background .2s ease">{ICON(I["send"],18,2.4)}</button></div>
</div></sc-if>
<sc-if value="{{{{readyShown}}}}" hint-placeholder-val="{{{{false}}}}"><div class="cp-pop" style="padding: 18px 20px 20px 20px; border-top: 1.5px solid #E6EAF3; display: flex; align-items: center; justify-content: space-between; gap: 12px; flex-wrap: wrap"><span style="font-size: 14px; color: #4A5578">All five answers are in. You can still change them in the draft.</span><button type="button" class="ds-btn" onClick="{{{{draft}}}}"><span style="display: inline-flex; align-items: center; gap: 8px"><svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l1.9 6.1L20 10l-6.1 1.9L12 18l-1.9-6.1L4 10l6.1-1.9z"></path></svg>Draft my course</span><span class="ob-arrow">{ICON(I["arrow"],18,2.4)}</span></button></div></sc-if>
</section>
<aside class="ds-card" aria-label="What Nova has so far" style="padding: 22px">
<h2 style="margin: 0; font-size: 15px; font-weight: 600">What Nova has so far</h2>
<ul style="list-style: none; margin: 12px 0 0 0; padding: 0"><sc-for list="{{{{facts}}}}" as="f" hint-placeholder-count="5"><li style="display: flex; gap: 10px; padding: 11px 0; border-top: 1px solid #E6EAF3"><span style="width: 20px; height: 20px; margin-top: 1px; flex-shrink: 0; box-sizing: border-box; border-radius: 50%; border: 2px solid {{{{f.bd}}}}; background: {{{{f.bg}}}}; color: #FFFFFF; display: flex; align-items: center; justify-content: center">{ICON(I["check"],11,3.4)}</span><span style="display: flex; flex-direction: column; gap: 2px; min-width: 0"><span style="font-size: 12.5px; color: #5B6582">{{{{f.label}}}}</span><span style="font-size: 14px; line-height: 1.45; color: {{{{f.fg}}}}">{{{{f.value}}}}</span></span></li></sc-for></ul>
</aside>
</div>
<sc-if value="{{{{propShown}}}}" hint-placeholder-val="{{{{false}}}}"><section id="c2-prop" class="ds-card cp-pop" aria-labelledby="c2-prop-t" style="margin-top: 18px; overflow: hidden; border-color: #AFC1F5; box-shadow: 0 0 0 4px rgba(22, 82, 240, 0.07), 0 18px 40px rgba(11, 20, 51, 0.06)">
<div style="padding: 22px 24px; display: flex; align-items: center; gap: 14px; flex-wrap: wrap; background: #FFFFFF url(/_blob/d268046654a4206d2a726e62005bcc59) center top / 100% auto no-repeat">{NOVA_AV(44)}<div style="flex: 1 1 260px; min-width: 0"><h2 id="c2-prop-t" style="margin: 0; font-size: 20px; font-weight: 600; letter-spacing: -0.015em">Nova’s first draft</h2><p style="margin: 3px 0 0 0; font-size: 14px; color: #4A5578">Review each part. Nothing enters the Studio until you accept it.</p></div><button type="button" class="ds-ghost" onClick="{{{{acceptAll}}}}" style="height: 44px">{ICON(I["check"],16,2.6)}Accept all</button></div>
<sc-for list="{{{{rows}}}}" as="r" hint-placeholder-count="7"><div class="pr-row" style="display: grid; grid-template-columns: 170px minmax(0, 1fr) auto; gap: 20px; align-items: start; padding: 18px 24px; border-top: 1.5px solid #E6EAF3; background: {{{{r.rowBg}}}}; transition: background .2s ease"><span style="font-size: 13.5px; font-weight: 600; color: #5B6582; padding-top: 2px">{{{{r.label}}}}</span><span style="font-size: 15px; line-height: 1.6; color: {{{{r.fg}}}}; white-space: pre-line; text-decoration: {{{{r.td}}}}">{{{{r.value}}}}</span><div class="pr-opts" role="group" aria-label="Decision for {{{{r.label}}}}" style="display: flex; gap: 6px">{OPT.replace("X","a")}{OPT.replace("X","e")}{OPT.replace("X","x")}</div></div></sc-for>
<div class="pr-foot" style="padding: 18px 24px; border-top: 1.5px solid #E6EAF3; background: #F7F9FD; display: flex; align-items: center; justify-content: space-between; gap: 16px; flex-wrap: wrap">
<div style="display: flex; flex-direction: column; gap: 8px; min-width: 200px"><span style="font-size: 14px; color: #3A4566"><span style="font-weight: 600; color: #0B1433">{{{{reviewed}}}} of 7</span> reviewed</span><span style="display: block; width: 220px; max-width: 100%; height: 6px; border-radius: 6px; background: #E6EAF3; overflow: hidden"><span style="display: block; height: 100%; width: {{{{pct}}}}; border-radius: 6px; background: #1652F0; transition: width .3s ease"></span></span><sc-if value="{{{{errShown}}}}" hint-placeholder-val="{{{{false}}}}"><span role="alert" style="font-size: 13.5px; color: #B42318">Review every part first: accept, edit later or reject.</span></sc-if></div>
<button type="button" class="ds-btn" onClick="{{{{open}}}}" aria-disabled="{{{{openDis}}}}" style="background: {{{{openBg}}}}; box-shadow: {{{{openSh}}}}"><span>Open Course Studio</span><span class="ob-arrow">{ICON(I["arrow"],18,2.4)}</span></button>
</div>
</section></sc-if>
<sc-if value="{{{{doneShown}}}}" hint-placeholder-val="{{{{false}}}}"><section id="c2-done" class="ds-card cp-pop" style="margin-top: 18px; padding: 36px 24px; display: flex; flex-direction: column; align-items: center; text-align: center">
<span style="width: 56px; height: 56px; border-radius: 50%; background: #E7F5EE; color: #0F6B45; display: flex; align-items: center; justify-content: center">{ICON(I["check"],26,2.8)}</span>
<h2 style="margin: 16px 0 0 0; font-size: 22px; font-weight: 600; letter-spacing: -0.015em">Your course draft is ready.</h2>
<p style="margin: 8px 0 0 0; max-width: 460px; font-size: 15px; line-height: 1.55; color: #4A5578">{{{{doneText}}}}</p>
{BTNA("#","Open Course Studio",extra='style="margin-top: 20px"')}
</section></sc-if>'''
C2_CSS='''.ds-opt:hover{border-color:#1652F0 !important}
@media (max-width: 1080px){.c2-grid{grid-template-columns:minmax(0,1fr) !important}}
@media (max-width: 860px){.pr-row{grid-template-columns:minmax(0,1fr) !important;gap:8px !important;padding:16px 18px !important}.pr-opts{display:grid !important;grid-template-columns:repeat(3,minmax(0,1fr));margin-top:6px}.pr-foot{flex-direction:column;align-items:stretch !important}.pr-foot .ds-btn{justify-content:space-between}.c2-head > div:last-child{align-items:flex-start !important}}
@media (max-width: 960px){section.ds-card > div[aria-live]{padding:18px !important}}
'''
S_C2='''class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.Q = [
      { q: 'What do you want someone to be able to do after learning from you?', k: 'Learners will be able to', chips: ['Analyse business data with SQL', 'Build dashboards managers use', 'Clean and prepare messy data'], demo: 'Analyse business data with SQL and present clear recommendations to managers.' },
      { q: 'Who is this course for?', k: 'Audience', chips: ['Early-career analysts', 'Career switchers', 'Managers who use data'], demo: 'Early-career analysts and career switchers' },
      { q: 'What experience should they already have?', k: 'Starting level', chips: ['Comfortable with spreadsheets', 'Some SQL', 'None yet'], demo: 'Comfortable with spreadsheets; no SQL yet' },
      { q: 'Which skills do you want them to develop?', k: 'Skills', chips: ['SQL', 'Data cleaning', 'Data storytelling'], demo: 'SQL, data cleaning, data storytelling' },
      { q: 'Which subject or domain does it sit in?', k: 'Domain', chips: ['Data & Analytics', 'Business', 'Technology'], demo: 'Data & Analytics' }
    ];
    this.P = [
      { k: 'title', label: 'Course title', value: 'SQL for Business Analysis' },
      { k: 'desc', label: 'Description', value: 'Learn to query, clean and analyse business data with SQL, and present clear recommendations managers can act on.' },
      { k: 'aud', label: 'Audience', value: 'Early-career analysts and career switchers\\nComfortable with spreadsheets; no SQL yet' },
      { k: 'pre', label: 'Prerequisites', value: 'Comfortable with spreadsheets (recommended)' },
      { k: 'skills', label: 'Skills', value: 'SQL · Beginner → Intermediate\\nData cleaning · Beginner → Intermediate\\nData storytelling · Beginner → Intermediate' },
      { k: 'out', label: 'Learning outcomes', value: 'Write SQL queries to retrieve, filter and aggregate business data.\\nClean and join tables to prepare data for analysis.\\nPresent findings and recommendations to non-technical stakeholders.' },
      { k: 'cur', label: 'First curriculum', value: '1. Why data and SQL matter\\n2. Querying with SELECT and WHERE\\n3. Joining and cleaning data\\n4. Aggregating for business questions\\n5. Presenting findings' }
    ];
    const full = (props || {}).variant === 'proposal';
    this.state = { nav: false, answers: full ? this.Q.map((x) => x.demo) : [], text: '', typing: false, phase: full ? 'proposal' : 'chat', dec: full ? { title: 'accept', desc: 'accept', aud: 'accept', pre: 'edit' } : {}, err: false };
  }
  componentWillUnmount() { clearTimeout(this.t); }
  send(v) {
    const t = (v || '').trim();
    if (!t || this.state.typing || this.state.answers.length >= 5) return;
    this.setState({ answers: [...this.state.answers, t], text: '', typing: true });
    this.t = setTimeout(() => this.setState({ typing: false }), 750);
  }
  draft() {
    this.setState({ phase: 'drafting' });
    this.t = setTimeout(() => { this.setState({ phase: 'proposal' }); setTimeout(() => { const el = document.getElementById('c2-prop'); if (el && el.scrollIntoView) el.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 60); }, 1400);
  }
  renderVals() {
    const { answers, typing, phase, dec, err, text } = this.state;
    const n = answers.length;
    const msgs = [{ who: 'n', text: 'Great, let’s shape your course. I’ll ask a few questions, then draft a structure for you to review.' }];
    for (let i = 0; i < 5; i++) {
      if (i < n) { msgs.push({ who: 'n', text: this.Q[i].q }); msgs.push({ who: 'm', text: answers[i] }); }
      else { msgs.push(typing ? { who: 'd', text: '' } : { who: 'n', text: this.Q[i].q }); break; }
    }
    if (n === 5) {
      if (typing) msgs.push({ who: 'd', text: '' });
      else {
        msgs.push({ who: 'n', text: 'Thanks, that’s everything I need. Ready for a draft?' });
        if (phase === 'drafting') msgs.push({ who: 'd', text: '' });
        if (phase === 'proposal' || phase === 'done') msgs.push({ who: 'n', text: 'Here’s a first draft. Accept, edit later or reject each part below. Nothing goes into the Studio until you do.' });
      }
    }
    const reviewed = this.P.filter((p) => dec[p.k]).length;
    const opt = (k, v, label) => { const on = dec[k] === v; return { label, on: on ? 'true' : 'false', pick: () => this.setState({ dec: { ...this.state.dec, [k]: on ? undefined : v }, err: false }), bd: on ? '#1652F0' : '#D6DDEE', bg: on ? '#EAF0FF' : '#FFFFFF', fg: on ? '#0E3BB8' : '#3A4566', ckd: on ? 'inline-flex' : 'none' }; };
    const accepted = this.P.filter((p) => dec[p.k] === 'accept').length;
    const later = this.P.filter((p) => dec[p.k] === 'edit').length;
    return {
      navCls: this.state.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !this.state.nav }),
      progress: n < 5 ? 'Question ' + (n + 1) + ' of 5' : 'All 5 answered',
      segs: [0, 1, 2, 3, 4].map((i) => ({ c: i < n ? '#1652F0' : (i === n ? '#AFC1F5' : '#E6EAF3') })),
      msgs: msgs.map((m) => ({ text: m.text, nd: m.who === 'n' ? 'flex' : 'none', md: m.who === 'm' ? 'flex' : 'none', dd: m.who === 'd' ? 'flex' : 'none' })),
      composerShown: n < 5, readyShown: n === 5 && !typing && phase === 'chat',
      chips: (n < 5 && !typing) ? this.Q[n].chips.map((label) => ({ label, pick: () => this.send(label) })) : [],
      text, onText: (e) => this.setState({ text: e.target.value }),
      onKey: (e) => { if (e.key === 'Enter') { e.preventDefault(); this.send(this.state.text); } },
      sendText: () => this.send(this.state.text), sendBg: text.trim() ? '#1652F0' : '#CBD3E6',
      draft: () => this.draft(),
      facts: this.Q.map((q, i) => ({ label: q.k, value: answers[i] || 'Not yet', fg: answers[i] ? '#0B1433' : '#8A93AD', bd: answers[i] ? '#0F6B45' : '#CBD3E6', bg: answers[i] ? '#0F6B45' : '#FFFFFF' })),
      propShown: phase === 'proposal', doneShown: phase === 'done',
      rows: this.P.map((p) => ({ label: p.label, value: p.value, fg: dec[p.k] === 'reject' ? '#8A93AD' : '#0B1433', td: dec[p.k] === 'reject' ? 'line-through' : 'none', rowBg: dec[p.k] === 'accept' ? '#FBFCFF' : '#FFFFFF', a: opt(p.k, 'accept', 'Accept'), e: opt(p.k, 'edit', 'Edit later'), x: opt(p.k, 'reject', 'Reject') })),
      reviewed, pct: Math.round(reviewed / 7 * 100) + '%', errShown: err,
      acceptAll: () => { const d = {}; this.P.forEach((p) => { d[p.k] = 'accept'; }); this.setState({ dec: d, err: false }); },
      openBg: reviewed === 7 ? '#1652F0' : '#AFC1F5', openSh: reviewed === 7 ? '0 1px 0 rgba(255,255,255,.25) inset, 0 10px 24px rgba(22,82,240,.24)' : 'none', openDis: reviewed === 7 ? 'false' : 'true',
      open: () => { if (reviewed < 7) this.setState({ err: true }); else this.setState({ phase: 'done' }); },
      doneText: accepted + ' accepted ' + (accepted === 1 ? 'part is' : 'parts are') + ' now in your new course draft.' + (later ? ' The ' + later + ' marked “edit later” ' + (later === 1 ? 'is' : 'are') + ' flagged for you in the Studio.' : '')
    };
  }
}'''
open(P+'CR-CREATE-002A.dc.html','w').write(SHELL('Create new',c,'Credalio · Create with Nova',S_C2,C2_CSS,900))
print('CREATE-002A built')

# ---------- preview wrappers
WRAP('CR-CREATE-002Ab.dc.html','CR-CREATE-002A',1440,2160,'Credalio · Nova’s first draft (proposal)',' variant="proposal"')
WRAP('CR-CREATE-002Ab-Mobile.dc.html','CR-CREATE-002A',390,3880,'Credalio · Nova’s first draft (mobile)',' variant="proposal"')
for n,h in [('CR-DASH-NEW',1860),('CR-CREATE-001',1090),('CR-CREATE-002A',1340)]:
    WRAP(n+'-Mobile.dc.html',n,390,h,n+' mobile preview')
print('wrappers built')
WRAP('CR-ONB-008-Mobile.dc.html','CR-ONB-008',390,1000,'CR-ONB-008 mobile preview')
s=open(P+'CR-ONB-008-Mobile.dc.html').read().replace('background: #F7F9FD','background: #FFFFFF'); open(P+'CR-ONB-008-Mobile.dc.html','w').write(s)
