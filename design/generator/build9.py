# v3 · CR-CREATE-002A / 002Ab — focused creation mode (no sidebar), chat with docked composer,
# live blueprint; review = the course rendered as a real page + a review rail.
# Needs dash.py names (ICON, I, NOVA_AV, COIN, BTNA, P, IMG). One source, prop variant="proposal".
BGI='/_blob/d268046654a4206d2a726e62005bcc59'
def ic(k, s=18, w=2): return ICON(I[k], s, w)
SPK='<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l1.9 6.1L20 10l-6.1 1.9L12 18l-1.9-6.1L4 10l6.1-1.9z"></path></svg>'
DOC_I='<rect x="5" y="3" width="14" height="18" rx="2.5"></rect><path d="M9 8h6M9 12h6M9 16h3"></path>'
USERS='<circle cx="9" cy="8" r="3.5"></circle><path d="M2.5 20a6.5 6.5 0 0 1 13 0"></path><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14.5a6.5 6.5 0 0 1 3.5 5.5"></path>'
BARS='<path d="M5 20v-4M10 20v-8M15 20V8M20 20V4"></path>'
X_I='<path d="M6 6l12 12M18 6 6 18"></path>'
DOTS='<span class="fx-dots" aria-label="Nova is typing"><span class="cp-dot"></span><span class="cp-dot" style="animation-delay: .15s"></span><span class="cp-dot" style="animation-delay: .3s"></span></span>'

# ---------------- top bar (focus mode) ----------------
TOP='''<header class="fx-top">
<a href="CR-CREATE-001.dc.html" class="fx-x" aria-label="Close and go back">'''+ICON(X_I,18,2.2)+'''</a>
<div class="fx-title"><span class="fx-t1">New course</span><span class="fx-t2">{{stageLabel}}</span></div>
<div class="fx-steps" aria-label="{{progress}}"><sc-for list="{{segs}}" as="s" hint-placeholder-count="5"><span style="background: {{s.c}}"></span></sc-for><em>{{progress}}</em></div>
<span style="flex-grow: 1"></span>
<button type="button" class="fx-bpbtn" onClick="{{toggleBp}}" aria-expanded="{{bpOpen}}" style="visibility: {{bpBtnV}}">'''+ICON(DOC_I,17,1.9)+'''<span>Blueprint</span><b>{{bpCount}}</b></button>
<a href="#" class="ds-tok fx-tok" aria-label="20,000 AI Tokens">'''+COIN('fxc',26)+'''<span>20K</span></a>
</header>'''

# ---------------- chat ----------------
MSG='''<sc-for list="{{msgs}}" as="m" hint-placeholder-count="3"><div class="fx-msg fx-nova cp-pop" style="display: {{m.nd}}">'''+NOVA_AV(32, False)+'''<div class="fx-mb"><span class="fx-who">Nova<em style="display: {{m.qd}}">{{m.ql}}</em></span><p>{{m.text}}</p></div></div><div class="fx-msg fx-me cp-pop" style="display: {{m.md}}"><button type="button" class="fx-edit" onClick="{{m.edit}}" aria-label="Edit this answer">'''+ic('pencil',14,1.9)+'''</button><p>{{m.text}}</p></div><div class="fx-msg fx-nova" style="display: {{m.dd}}">'''+NOVA_AV(32, False)+'''<div class="fx-mb"><span class="fx-who">Nova</span>'''+DOTS+'''</div></div></sc-for>'''
DOCK='''<div class="fx-dock">
<div class="fx-col">
<sc-if value="{{composerShown}}" hint-placeholder-val="{{true}}">
<div class="fx-sugg" aria-label="Suggestions"><sc-for list="{{chips}}" as="ch" hint-placeholder-count="3"><button type="button" class="fx-chip" onClick="{{ch.pick}}">'''+SPK+'''{{ch.label}}</button></sc-for></div>
<div class="fx-comp"><label class="sr-only" for="fx-in">Your answer</label><input id="fx-in" value="{{text}}" onChange="{{onText}}" onKeyDown="{{onKey}}" placeholder="Type your answer…" autocomplete="off"><button type="button" class="fx-send" onClick="{{sendText}}" aria-label="Send" style="background: {{sendBg}}">'''+ic('send',18,2.4)+'''</button></div>
<span class="fx-hint">Press Enter to send · You can edit any answer later</span>
</sc-if>
<sc-if value="{{readyShown}}" hint-placeholder-val="{{false}}"><div class="fx-ready cp-pop"><button type="button" class="ds-btn" onClick="{{draft}}"><span style="display: inline-flex; align-items: center; gap: 8px">'''+SPK+'''Draft my course</span><span class="ob-arrow">'''+ic('arrow',18,2.4)+'''</span></button><span class="fx-hint" style="margin: 0">Uses about 1,200 of your AI Tokens</span></div></sc-if>
<sc-if value="{{draftingShown}}" hint-placeholder-val="{{false}}"><div class="fx-ready" role="status"><span class="fx-bar"><span></span></span><span class="fx-hint" style="margin: 0">Nova is drafting your course…</span></div></sc-if>
</div>
</div>'''
FACTS='''<sc-for list="{{facts}}" as="f" hint-placeholder-count="5"><li class="fx-fact"><span class="fx-fdot" style="background: {{f.dot}}; border-color: {{f.dbd}}">'''+ic('check',10,3.4)+'''</span><span style="display: flex; flex-direction: column; gap: 3px; min-width: 0; flex-grow: 1"><span class="fx-fl">{{f.label}}</span><span class="fx-fv c2-new" style="display: {{f.vd}}">{{f.value}}</span><span class="c2-shim" style="display: {{f.sd}}; height: 9px; width: {{f.w}}; margin-top: 4px"></span></span></li></sc-for>'''
BP='''<aside class="fx-bp {{bpCls}}" aria-label="Course blueprint">
<div class="fx-bph"><span style="display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 600; color: #0B1433">'''+ICON(DOC_I,17,1.9)+'''Course blueprint</span><span class="fx-live"><i></i>{{bpState}}</span><button type="button" class="fx-bpclose" onClick="{{toggleBp}}" aria-label="Close blueprint">'''+ICON(X_I,16,2.2)+'''</button></div>
<div class="fx-sheet">
<span style="display: block; font-size: 12px; color: #8A93AD">Course title</span>
<span style="display: block; margin-top: 6px; font-size: 17px; font-weight: 600; color: #B4BCD0">Nova names it at the end</span>
<ul style="list-style: none; margin: 16px 0 0 0; padding: 0">'''+FACTS+'''</ul>
</div>
<p class="fx-bpnote">'''+SPK+'''From these five answers Nova drafts a title, description, outcomes and a first curriculum.</p>
</aside>'''
CHAT='''<sc-if value="{{chatView}}" hint-placeholder-val="{{true}}">
<div class="fx-body">
<section class="fx-chat" aria-label="Conversation with Nova">
<div class="fx-scroll"><div class="fx-col fx-msgs" aria-live="polite">
<div class="fx-hello">'''+NOVA_AV(56)+'''<h1>Let’s sketch your course</h1><p>Five quick questions. Then I’ll draft it, and you decide what stays.</p></div>
'''+MSG+'''
</div></div>
'''+DOCK+'''
</section>
'''+BP+'''
<div class="fx-scrim {{bpCls}}" onClick="{{toggleBp}}"></div>
</div>
</sc-if>'''

# ---------------- review (the course, rendered as a page) ----------------
def TOOLS(k,label):
    def b(v,icon,name,cls):
        return f'<button type="button" class="rv-b {cls}" onClick="{{{{d.{k}.{v}.pick}}}}" aria-pressed="{{{{d.{k}.{v}.on}}}}" title="{name}" style="background: {{{{d.{k}.{v}.bg}}}}; color: {{{{d.{k}.{v}.fg}}}}; border-color: {{{{d.{k}.{v}.bd}}}}">{icon}<span>{name}</span></button>'
    return f'<div class="rv-tools" role="group" aria-label="Review: {label}">'+b('a',ic('check',15,2.6),'Accept','')+b('e',ic('pencil',14,2),'Edit later','')+b('x',ICON(X_I,14,2.4),'Reject','')+'</div>'
def SEC(k,label,body,cls=''):
    return f'''<section id="rv-{k}" class="rv-sec {cls}" style="box-shadow: {{{{d.{k}.ring}}}}"><div class="rv-h"><span class="rv-lab">{label}<span class="rv-st" style="display: {{{{d.{k}.sd}}}}; background: {{{{d.{k}.sb}}}}; color: {{{{d.{k}.sc}}}}">{{{{d.{k}.st}}}}</span></span>{TOOLS(k,label)}</div><div class="rv-body" style="opacity: {{{{d.{k}.op}}}}; text-decoration: {{{{d.{k}.td}}}}">{body}</div></section>'''
def LVL(n): return f'<li><span class="rv-sk">{n}</span><span class="rv-lv" aria-label="Beginner to Intermediate"><i class="on1"></i><i class="on2"></i><i></i></span><span class="rv-lt">Beginner → Intermediate</span></li>'
OUTS=''.join(f'<li><span class="rv-oc">{ic("check",12,3)}</span>{t}</li>' for t in ['Write SQL queries to retrieve, filter and aggregate business data.','Clean and join tables to prepare data for analysis.','Present findings and recommendations to non-technical stakeholders.'])
MODS=''.join(f'<li><span class="rv-mn">{i+1}</span><span class="rv-mt">{t}</span></li>' for i,t in enumerate(['Why data and SQL matter','Querying with SELECT and WHERE','Joining and cleaning data','Aggregating for business questions','Presenting findings']))
PAGE=('<article class="rv-page" aria-label="Your draft course">'
 +'<div class="rv-hero"><span class="rv-kicker">'+ic('course',15,1.9)+'Course · Draft by Nova</span>'
 +SEC('title','Title','<h2 class="rv-title">SQL for Business Analysis</h2>','rv-in-hero')
 +SEC('desc','Description','<p class="rv-desc">Learn to query, clean and analyse business data with SQL, and present clear recommendations managers can act on.</p>','rv-in-hero')
 +'</div><div class="rv-grid2">'
 +SEC('aud','Who it’s for',f'<p class="rv-line"><span>{ICON(USERS,17,1.8)}</span>Early-career analysts and career switchers</p><p class="rv-line"><span>{ICON(BARS,17,1.8)}</span>Comfortable with spreadsheets; no SQL yet</p>')
 +SEC('pre','Before you start',f'<p class="rv-line"><span>{ic("check",15,2.4)}</span>Comfortable with spreadsheets</p><span class="rv-tag">Recommended, not required</span>')
 +'</div>'
 +SEC('skills','Skills you’ll build',f'<ul class="rv-skills">{LVL("SQL")}{LVL("Data cleaning")}{LVL("Data storytelling")}</ul>')
 +SEC('out','By the end, learners can',f'<ul class="rv-outs">{OUTS}</ul>')
 +SEC('cur','Curriculum · 5 modules',f'<ol class="rv-mods">{MODS}</ol>')
 +'</article>')
NOTES=''.join(f'<li>{SPK}<span>{t}</span></li>' for t in ['Short modules, since many learners are switching careers.','Skills start at Beginner, because they haven’t used SQL yet.','It ends with presenting, so learners leave with something managers can use.'])
RAIL=('<aside class="rv-rail" aria-label="Your review">'
 +'<div class="rv-card"><div class="rv-prog"><span class="rv-ring" style="background: conic-gradient(#1652F0 {{pctDeg}}, #EAF0FF 0)"><b>{{reviewed}}/7</b></span><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 600; color: #0B1433">Review the draft</span><span style="font-size: 13px; color: #5B6582">Accept, edit later or reject each part.</span></span></div>'
 +'<ol class="rv-list"><sc-for list="{{parts}}" as="p" hint-placeholder-count="7"><li><a href="{{p.href}}"><span class="rv-dot" style="background: {{p.dot}}; border-color: {{p.dbd}}"></span><span class="rv-pl">{{p.label}}</span><span class="rv-ps" style="color: {{p.sc}}">{{p.st}}</span></a></li></sc-for></ol>'
 +'<sc-if value="{{errShown}}" hint-placeholder-val="{{false}}"><span role="alert" class="rv-err">Review every part first.</span></sc-if>'
 +'<button type="button" class="ds-btn rv-open" onClick="{{open}}" aria-disabled="{{openDis}}" style="background: {{openBg}}; box-shadow: {{openSh}}"><span>Open Course Studio</span><span class="ob-arrow">'+ic('arrow',18,2.4)+'</span></button>'
 +'<button type="button" class="rv-rest" onClick="{{acceptRest}}">Accept the rest</button></div>'
 +'<div class="rv-card rv-why"><button type="button" class="rv-whyh" onClick="{{toggleNotes}}" aria-expanded="{{notesOpen}}">'+NOVA_AV(28,False)+'<span>Why Nova drafted it this way</span><span style="display: flex; transform: {{notesRot}}; transition: transform .2s ease"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"></path></svg></span></button>'
 +'<sc-if value="{{notesShown}}" hint-placeholder-val="{{true}}"><ul class="rv-notes">'+NOTES+'</ul><div class="rv-ask"><label class="sr-only" for="rv-ask">Ask Nova to change something</label><input id="rv-ask" placeholder="Ask Nova to change something"><button type="button" aria-label="Send">'+ic('send',15,2.4)+'</button></div></sc-if></div>'
 +'</aside>')
MBAR=('<div class="rv-mbar"><span class="rv-mp"><span><b>{{reviewed}} of 7</b> reviewed</span><button type="button" onClick="{{acceptRest}}">Accept the rest</button></span>'
 +'<button type="button" class="ds-btn" onClick="{{open}}" aria-disabled="{{openDis}}" style="background: {{openBg}}"><span>Open Course Studio</span><span class="ob-arrow">'+ic('arrow',18,2.4)+'</span></button></div>')
REVIEW=('<sc-if value="{{reviewView}}" hint-placeholder-val="{{false}}"><div class="rv-body-wrap"><div class="rv-wrap">'
 +'<div class="rv-intro">'+NOVA_AV(36)+'<p><b>Here’s your first draft.</b> It’s built from your five answers. Nothing reaches the Studio until you accept it.</p><button type="button" class="rv-back" onClick="{{backToChat}}">'+ic('back',15,2.2)+'Answers</button></div>'
 +'<div class="rv-cols">'+PAGE+RAIL+'</div></div>'+MBAR+'</div></sc-if>')
DONE=('<sc-if value="{{doneView}}" hint-placeholder-val="{{false}}"><div class="rv-done cp-pop"><span class="rv-doneic">'+ic('check',30,2.8)+'</span><h1>Your course draft is ready.</h1><p>{{doneText}}</p>'
 +BTNA('#','Open Course Studio',extra='style="margin-top: 24px"')+'</div></sc-if>')

CSS='''body{margin:0;background:#F7F9FD}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@keyframes cpPop{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
@keyframes cpDot{0%,80%,100%{opacity:.25;transform:translateY(0)}40%{opacity:1;transform:translateY(-3px)}}
@keyframes c2Shim{0%{background-position:-200px 0}100%{background-position:200px 0}}
@keyframes c2New{0%{background:#EAF0FF}100%{background:transparent}}
@keyframes fxLive{0%{box-shadow:0 0 0 0 rgba(22,82,240,.4)}100%{box-shadow:0 0 0 7px rgba(22,82,240,0)}}
@keyframes fxBar{0%{transform:translateX(-100%)}100%{transform:translateX(250%)}}
.cp-pop{animation:cpPop .4s ease both}
.cp-dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:#1652F0;animation:cpDot 1.2s ease-in-out infinite}
.c2-shim{border-radius:6px;background:linear-gradient(90deg,#EEF1F7 0px,#F7F9FD 80px,#EEF1F7 160px);background-size:400px 100%;animation:c2Shim 1.6s linear infinite}
.c2-new{border-radius:6px;animation:c2New 1.2s ease both}
.ds-tok{height:40px;flex-shrink:0;box-sizing:border-box;display:flex;align-items:center;gap:7px;padding:0 13px 0 6px;border-radius:999px;background:linear-gradient(135deg,#FFFAEB,#FFF1CF);border:1.5px solid #F4D98E;font-size:14px;font-weight:600;color:#4A3300;text-decoration:none}
.ds-btn{display:inline-flex;align-items:center;gap:14px;height:52px;padding:0 6px 0 24px;box-sizing:border-box;border-radius:999px;background:#1652F0;color:#FFFFFF;font-family:inherit;font-size:15.5px;font-weight:600;text-decoration:none;white-space:nowrap;border:0;cursor:pointer;box-shadow:0 1px 0 rgba(255,255,255,.25) inset,0 10px 24px rgba(22,82,240,.24);transition:background .2s ease,transform .2s ease}
.ds-btn:hover{background:#0E3BB8;transform:translateY(-1px)}
.ds-btn .ob-arrow{width:40px;height:40px;border-radius:50%;background:#FFFFFF;color:#1652F0;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.fx-root{height:100vh;display:flex;flex-direction:column;background:#FFFFFF;font-family:'Google Sans','Google Sans Text','Helvetica Neue',system-ui,sans-serif;color:#0B1433;overflow:hidden}
.fx-top{height:64px;flex-shrink:0;box-sizing:border-box;display:flex;align-items:center;gap:16px;padding:0 20px;border-bottom:1.5px solid #EEF1F7;background:#FFFFFF;z-index:5}
.fx-x{width:40px;height:40px;flex-shrink:0;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#3A4566;text-decoration:none;transition:background .2s ease}
.fx-x:hover{background:#F5F8FF;color:#0B1433}
.fx-title{display:flex;align-items:baseline;gap:8px;min-width:0}
.fx-t1{font-size:16px;font-weight:600;white-space:nowrap}
.fx-t2{font-size:14px;color:#5B6582;white-space:nowrap}
.fx-steps{display:flex;align-items:center;gap:4px;margin-left:16px}
.fx-steps > span{width:26px;height:4px;border-radius:4px;transition:background .3s ease}
.fx-steps em{font-style:normal;font-size:13px;color:#5B6582;margin-left:10px;white-space:nowrap}
.fx-bpbtn{display:none}
.fx-body{flex-grow:1;min-height:0;display:grid;grid-template-columns:minmax(0,1fr) 400px;background:#FFFFFF}
.fx-chat{display:flex;flex-direction:column;min-height:0;min-width:0}
.fx-scroll{flex-grow:1;min-height:0;overflow-y:auto;display:flex;flex-direction:column}
.fx-col{width:100%;max-width:720px;margin:0 auto;box-sizing:border-box;padding:0 32px}
.fx-msgs{flex-grow:1;display:flex;flex-direction:column;justify-content:flex-end;gap:20px;padding-top:32px;padding-bottom:12px}
.fx-hello{display:flex;flex-direction:column;align-items:center;text-align:center;padding:8px 0 20px 0;margin:auto 0;position:relative;isolation:isolate}
.fx-chat{position:relative;isolation:isolate}
.fx-chat::before{content:'';position:absolute;z-index:-1;left:0;right:0;top:0;height:min(300px,45%);pointer-events:none;background:linear-gradient(90deg,rgba(22,82,240,0) 0%,rgba(22,82,240,.22) 18%,rgba(140,175,255,.30) 34%,rgba(22,82,240,0) 50%,rgba(22,82,240,.22) 68%,rgba(140,175,255,.30) 84%,rgba(22,82,240,0) 100%);background-size:200% 100%;-webkit-mask-image:linear-gradient(180deg,#000 0%,rgba(0,0,0,.5) 45%,transparent 100%);mask-image:linear-gradient(180deg,#000 0%,rgba(0,0,0,.5) 45%,transparent 100%);animation:fxFlow 10s linear infinite}
@keyframes fxFlow{from{background-position:0% 0}to{background-position:-200% 0}}
@media (prefers-reduced-motion: reduce){.fx-chat::before{animation:none}}
.fx-hello h1{margin:14px 0 0 0;font-size:26px;font-weight:600;letter-spacing:-0.02em}
.fx-hello p{margin:6px 0 0 0;font-size:15px;color:#5B6582}
.fx-msg{display:flex;gap:12px;align-items:flex-start}
.fx-mb{display:flex;flex-direction:column;gap:4px;min-width:0}
.fx-who{display:flex;align-items:center;gap:8px;font-size:13px;font-weight:600;color:#0B1433}
.fx-who em{font-style:normal;font-weight:500;font-size:12px;color:#1652F0;background:#EAF0FF;border-radius:999px;padding:2px 8px}
.fx-nova p{margin:0;font-size:16.5px;line-height:1.6;color:#0B1433}
.fx-me{justify-content:flex-end;align-items:center}
.fx-me p{margin:0;max-width:78%;padding:11px 16px;border-radius:18px 18px 6px 18px;background:#EAF0FF;font-size:15.5px;line-height:1.5;color:#0B1433}
.fx-edit{width:30px;height:30px;flex-shrink:0;border:0;border-radius:50%;background:transparent;color:#8A93AD;display:flex;align-items:center;justify-content:center;cursor:pointer;opacity:0;transition:opacity .2s ease,background .2s ease}
.fx-me:hover .fx-edit,.fx-edit:focus-visible{opacity:1}
.fx-edit:hover{background:#F5F8FF;color:#1652F0}
.fx-dots{display:inline-flex;gap:5px;padding:10px 0}
.fx-dock{flex-shrink:0;padding:10px 0 20px 0;background:linear-gradient(180deg,rgba(255,255,255,0),#FFFFFF 22%)}
.fx-sugg{display:flex;gap:8px;overflow-x:auto;padding:2px 0 10px 0;scrollbar-width:none}
.fx-sugg::-webkit-scrollbar{display:none}
.fx-chip{flex-shrink:0;display:inline-flex;align-items:center;gap:7px;height:38px;padding:0 14px 0 12px;box-sizing:border-box;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;font-family:inherit;font-size:14px;font-weight:500;cursor:pointer;white-space:nowrap;transition:border-color .2s ease,background .2s ease}
.fx-chip svg{color:#1652F0}
.fx-chip:hover{border-color:#1652F0;background:#F5F8FF}
.fx-comp{display:flex;align-items:center;gap:8px;height:58px;box-sizing:border-box;padding:0 8px 0 20px;border-radius:20px;border:1.5px solid #D6DDEE;background:#FFFFFF;box-shadow:0 10px 30px rgba(11,20,51,.06);transition:border-color .2s ease,box-shadow .2s ease}
.fx-comp:focus-within{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12),0 10px 30px rgba(11,20,51,.06)}
.fx-comp input{flex-grow:1;min-width:0;border:0;outline:none;background:transparent;font-family:inherit;font-size:16px;color:#0B1433}
.fx-comp input::placeholder{color:#8A93AD}
.fx-send{width:42px;height:42px;flex-shrink:0;border:0;border-radius:14px;color:#FFFFFF;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:background .2s ease}
.fx-hint{display:block;margin-top:8px;text-align:center;font-size:12px;color:#8A93AD}
.fx-ready{display:flex;flex-direction:column;align-items:center;gap:10px;padding:6px 0}
.fx-bar{display:block;width:260px;height:6px;border-radius:6px;background:#EAF0FF;overflow:hidden}
.fx-bar span{display:block;width:40%;height:100%;border-radius:6px;background:#1652F0;animation:fxBar 1.2s ease-in-out infinite}
.fx-bp{border-left:1.5px solid #EEF1F7;background:#F7F9FD url(BGI) center top / 100% auto no-repeat;padding:22px 24px;overflow-y:auto;min-height:0}
.fx-bph{display:flex;align-items:center;justify-content:space-between;gap:10px}
.fx-bph svg{color:#1652F0}
.fx-live{display:inline-flex;align-items:center;gap:6px;font-size:12.5px;font-weight:500;color:#0E3BB8}
.fx-live i{width:8px;height:8px;border-radius:50%;background:#1652F0;animation:fxLive 1.6s ease-out infinite}
.fx-bpclose{display:none}
.fx-sheet{margin-top:16px;padding:20px;border-radius:18px;background:#FFFFFF;border:1.5px solid #E6EAF3;box-shadow:0 14px 32px rgba(22,82,240,.08)}
.fx-fact{display:flex;gap:12px;padding:12px 0;border-top:1px solid #EEF1F7}
.fx-fdot{width:18px;height:18px;margin-top:1px;flex-shrink:0;box-sizing:border-box;border-radius:50%;border:2px solid;color:#FFFFFF;display:flex;align-items:center;justify-content:center;transition:all .3s ease}
.fx-fl{font-size:12px;color:#5B6582}
.fx-fv{font-size:14px;line-height:1.45;font-weight:500;color:#0B1433}
.fx-bpnote{display:flex;gap:8px;margin:14px 2px 0 2px;font-size:13px;line-height:1.5;color:#5B6582}
.fx-bpnote svg{color:#1652F0;flex-shrink:0;margin-top:2px}
.fx-scrim{display:none}
/* review */
.rv-body-wrap{flex-grow:1;min-height:0;overflow-y:auto;background:#F7F9FD}
.rv-wrap{max-width:1180px;margin:0 auto;padding:22px 32px 40px 32px;box-sizing:border-box}
.rv-intro{display:flex;align-items:center;gap:12px}
.rv-intro p{margin:0;flex-grow:1;font-size:15px;line-height:1.5;color:#3A4566}
.rv-intro b{color:#0B1433;font-weight:600}
.rv-back{display:inline-flex;align-items:center;gap:6px;height:38px;padding:0 14px;border-radius:999px;border:1.5px solid #E6EAF3;background:#FFFFFF;color:#3A4566;font-family:inherit;font-size:14px;font-weight:500;cursor:pointer;flex-shrink:0}
.rv-back:hover{border-color:#AFC1F5}
.rv-cols{margin-top:18px;display:grid;grid-template-columns:minmax(0,1fr) 320px;gap:24px;align-items:start}
.rv-page{background:#FFFFFF;border:1.5px solid #E6EAF3;border-radius:24px;overflow:hidden;display:flex;flex-direction:column}
.rv-hero{padding:28px 28px 14px 28px;background:#FFFFFF url(BGI) center top / cover no-repeat}
.rv-kicker{display:inline-flex;align-items:center;gap:7px;height:28px;padding:0 12px;border-radius:999px;background:rgba(255,255,255,.85);font-size:12.5px;font-weight:500;color:#0E3BB8}
.rv-sec{position:relative;padding:16px 28px 20px 28px;border-top:1px solid #EEF1F7;transition:box-shadow .2s ease,background .2s ease}
.rv-in-hero{padding:14px 0 10px 0;border-top:0;border-radius:14px;box-shadow:none !important}
.rv-hero .rv-sec + .rv-sec{border-top:1px solid rgba(203,211,230,.5)}
.rv-h{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:34px}
.rv-lab{display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:600;color:#5B6582}
.rv-st{display:none !important;height:22px;padding:0 9px;border-radius:999px;font-size:11.5px;font-weight:500;align-items:center}
.rv-tools{display:inline-flex;gap:4px;opacity:.55;transition:opacity .2s ease}
.rv-sec:hover .rv-tools,.rv-tools:focus-within,.rv-tools:has([aria-pressed=true]){opacity:1}
.rv-b{height:32px;padding:0 10px;box-sizing:border-box;border-radius:10px;border:1.5px solid;display:inline-flex;align-items:center;gap:6px;font-family:inherit;font-size:13px;font-weight:500;cursor:pointer;transition:all .2s ease}
.rv-b span{display:none}
.rv-b[aria-pressed=true] span{display:inline}
.rv-b:hover span{display:inline}
.rv-b:focus-visible,.rv-rest:focus-visible,.rv-back:focus-visible,.fx-chip:focus-visible,.fx-x:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:2px}
.rv-body{margin-top:6px;transition:opacity .2s ease}
.rv-title{margin:0;font-size:32px;line-height:1.15;font-weight:600;letter-spacing:-0.03em}
.rv-desc{margin:0;font-size:17px;line-height:1.6;color:#3A4566;max-width:640px}
.rv-grid2{display:grid;grid-template-columns:1fr 1fr}
.rv-grid2 .rv-sec + .rv-sec{border-left:1px solid #EEF1F7}
.rv-line{display:flex;align-items:center;gap:10px;margin:6px 0 0 0;font-size:15px;color:#0B1433}
.rv-line span{color:#1652F0;display:flex}
.rv-tag{display:inline-flex;margin-top:10px;height:26px;padding:0 10px;align-items:center;border-radius:999px;background:#F5F8FF;font-size:12.5px;font-weight:500;color:#4A5578}
.rv-skills{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.rv-skills li{padding:14px;border-radius:14px;background:#F7F9FD;display:flex;flex-direction:column;gap:8px}
.rv-sk{font-size:15px;font-weight:600}
.rv-lv{display:grid;grid-template-columns:repeat(3,1fr);gap:4px}
.rv-lv i{height:6px;border-radius:3px;background:#E6EAF3}
.rv-lv i.on1{background:#AFC1F5}.rv-lv i.on2{background:#1652F0}
.rv-lt{font-size:12.5px;color:#5B6582}
.rv-outs{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px}
.rv-outs li{display:flex;gap:12px;font-size:15.5px;line-height:1.5}
.rv-oc{width:22px;height:22px;margin-top:1px;flex-shrink:0;border-radius:50%;background:#EAF0FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.rv-mods{list-style:none;margin:0;padding:0;position:relative}
.rv-mods:before{content:"";position:absolute;left:15px;top:16px;bottom:16px;width:2px;background:linear-gradient(#1652F0,#AFC1F5)}
.rv-mods li{position:relative;display:flex;align-items:center;gap:14px;padding:8px 0}
.rv-mn{width:32px;height:32px;flex-shrink:0;border-radius:50%;background:#FFFFFF;border:2px solid #1652F0;color:#1652F0;font-size:13.5px;font-weight:600;display:flex;align-items:center;justify-content:center;z-index:1}
.rv-mt{font-size:15.5px}
.rv-rail{position:sticky;top:0;display:flex;flex-direction:column;gap:14px}
.rv-card{background:#FFFFFF;border:1.5px solid #E6EAF3;border-radius:20px;padding:18px}
.rv-prog{display:flex;align-items:center;gap:14px}
.rv-ring{width:56px;height:56px;flex-shrink:0;border-radius:50%;display:flex;align-items:center;justify-content:center;position:relative}
.rv-ring:before{content:"";position:absolute;inset:6px;border-radius:50%;background:#FFFFFF}
.rv-ring b{position:relative;font-size:14px;font-weight:600}
.rv-list{list-style:none;margin:14px 0 0 0;padding:0}
.rv-list a{display:flex;align-items:center;gap:10px;padding:9px 6px;border-radius:10px;text-decoration:none;color:#0B1433}
.rv-list a:hover{background:#F5F8FF}
.rv-dot{width:12px;height:12px;flex-shrink:0;box-sizing:border-box;border-radius:50%;border:2px solid}
.rv-pl{flex-grow:1;font-size:14px}
.rv-ps{font-size:12.5px}
.rv-err{display:block;margin-top:10px;font-size:13px;color:#B42318}
.rv-open{width:100%;justify-content:space-between;margin-top:14px}
.rv-rest{display:block;width:100%;margin-top:8px;height:40px;border:0;background:none;color:#1652F0;font-family:inherit;font-size:14px;font-weight:500;cursor:pointer;border-radius:999px}
.rv-rest:hover{background:#F5F8FF}
.rv-whyh{display:flex;align-items:center;gap:10px;width:100%;border:0;background:none;padding:0;font-family:inherit;font-size:14.5px;font-weight:600;color:#0B1433;cursor:pointer;text-align:left}
.rv-whyh > span:nth-child(2){flex-grow:1}
.rv-notes{list-style:none;margin:12px 0 0 0;padding:0}
.rv-notes li{display:flex;gap:10px;padding:9px 0;border-top:1px solid #EEF1F7;font-size:13.5px;line-height:1.5}
.rv-notes svg{color:#1652F0;flex-shrink:0;margin-top:3px}
.rv-ask{margin-top:10px;display:flex;align-items:center;gap:6px;height:44px;box-sizing:border-box;padding:0 5px 0 14px;border-radius:14px;border:1.5px solid #D6DDEE}
.rv-ask input{flex-grow:1;min-width:0;border:0;outline:none;font-family:inherit;font-size:14px}
.rv-ask button{width:34px;height:34px;border:0;border-radius:10px;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center;cursor:pointer}
.rv-mbar{display:none}
.rv-done{flex-grow:1;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:24px;background:#FFFFFF url(BGI) center top / 100% auto no-repeat}
.rv-doneic{width:68px;height:68px;border-radius:50%;background:#0F6B45;color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 10px rgba(15,107,69,.12)}
.rv-done h1{margin:22px 0 0 0;font-size:30px;font-weight:600;letter-spacing:-0.03em}
.rv-done p{margin:8px 0 0 0;max-width:460px;font-size:15.5px;line-height:1.55;color:#4A5578}
@media (prefers-reduced-motion: reduce){.cp-pop,.cp-dot,.c2-shim,.c2-new,.fx-live i,.fx-bar span{animation:none}}
@media (max-width: 1180px){.fx-body{grid-template-columns:minmax(0,1fr) 340px}.rv-cols{grid-template-columns:minmax(0,1fr) 290px}.rv-skills{grid-template-columns:minmax(0,1fr)}}
@media (max-width: 960px){
.fx-root{height:100vh;height:100dvh}
.fx-top{height:56px;gap:8px;padding:0 10px 0 6px}
.fx-t2,.fx-tok,.fx-steps em{display:none}
.fx-steps{display:none !important}
.fx-bpbtn{display:inline-flex;align-items:center;gap:6px;height:36px;padding:0 10px;border-radius:999px;border:1.5px solid #E6EAF3;background:#FFFFFF;color:#0B1433;font-family:inherit;font-size:13px;font-weight:500;cursor:pointer}
.fx-bpbtn svg{color:#1652F0}
.fx-bpbtn b{font-weight:600;color:#1652F0}
.fx-body{grid-template-columns:minmax(0,1fr);position:relative}
.fx-col{padding:0 16px}
.fx-msgs{gap:16px;padding-top:20px}
.fx-hello{padding:4px 0 8px 0}.fx-hello h1{font-size:21px;margin-top:10px}.fx-hello p{font-size:14px}
.fx-hello .fx-av,.fx-hello > span:first-child{width:44px !important;height:44px !important}
.fx-nova p{font-size:15.5px}
.fx-me p{font-size:15px;max-width:85%}
.fx-edit{opacity:1}
.fx-dock{padding:8px 0 12px 0;border-top:1px solid #EEF1F7;background:#FFFFFF}
.fx-sugg{margin:0 -16px;padding:0 16px 8px 16px}
.fx-chip{height:36px;font-size:13.5px}
.fx-comp{height:52px;border-radius:16px;padding:0 6px 0 16px}
.fx-comp input{font-size:16px}
.fx-send{width:40px;height:40px;border-radius:12px}
.fx-hint{display:none}
.fx-bp{position:absolute;left:0;right:0;bottom:0;max-height:78%;border-left:0;border-radius:22px 22px 0 0;box-shadow:0 -20px 50px rgba(11,20,51,.18);transform:translateY(105%);transition:transform .3s cubic-bezier(.2,.8,.2,1);z-index:6;padding:18px 16px 24px 16px}
.fx-bp.fx-open{transform:none}
.fx-bpclose{display:flex;width:32px;height:32px;border:0;border-radius:50%;background:#FFFFFF;color:#3A4566;align-items:center;justify-content:center;cursor:pointer}
.fx-live{margin-left:auto}
.fx-scrim.fx-open{display:block;position:absolute;inset:0;background:rgba(11,20,51,.28);z-index:5}
.rv-wrap{padding:14px 16px 120px 16px}
.rv-intro{flex-wrap:wrap;gap:10px}.rv-intro p{font-size:14px;flex-basis:calc(100% - 60px)}
.rv-back{display:none}
.rv-cols{grid-template-columns:minmax(0,1fr);margin-top:14px;gap:14px}
.rv-rail{position:static;order:-1}
.rv-rail > .rv-card:first-child{display:none}
.rv-why{padding:14px}
.rv-page{border-radius:20px}
.rv-hero{padding:18px 16px 8px 16px}
.rv-sec{padding:12px 16px 16px 16px}
.rv-in-hero{padding:12px 0 8px 0}
.rv-h{flex-wrap:wrap;gap:8px}
.rv-tools{opacity:1}
.rv-b:hover span{display:none}.rv-b[aria-pressed=true] span{display:inline}
.rv-title{font-size:23px}.rv-desc{font-size:15px}
.rv-grid2{grid-template-columns:minmax(0,1fr)}.rv-grid2 .rv-sec + .rv-sec{border-left:0}
.rv-line,.rv-outs li,.rv-mt{font-size:14.5px}
.rv-mbar{display:flex;flex-direction:column;gap:10px;position:fixed;left:0;right:0;bottom:0;padding:12px 16px 16px 16px;background:rgba(255,255,255,.96);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-top:1.5px solid #E6EAF3;z-index:6}
.rv-mp{display:flex;align-items:center;justify-content:space-between;font-size:13.5px;color:#4A5578}
.rv-mp b{color:#0B1433;font-weight:600}
.rv-mp button{border:0;background:none;color:#1652F0;font-family:inherit;font-size:13.5px;font-weight:500;cursor:pointer;padding:6px 0}
.rv-mbar .ds-btn{width:100%;justify-content:space-between;height:50px}
.rv-done h1{font-size:24px}
}
'''.replace('BGI',BGI)

S='''class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.Q = [
      { q: 'What should someone be able to do after learning from you?', k: 'Learners will be able to', chips: ['Analyse business data with SQL', 'Build dashboards managers use', 'Clean and prepare messy data'], demo: 'Analyse business data with SQL and present clear recommendations to managers.' },
      { q: 'Who is this course for?', k: 'For', chips: ['Early-career analysts', 'Career switchers', 'Managers who use data'], demo: 'Early-career analysts and career switchers' },
      { q: 'What should they already know?', k: 'Starting level', chips: ['Comfortable with spreadsheets', 'Some SQL', 'Nothing yet'], demo: 'Comfortable with spreadsheets; no SQL yet' },
      { q: 'Which skills should they build?', k: 'Skills', chips: ['SQL', 'Data cleaning', 'Data storytelling'], demo: 'SQL, data cleaning, data storytelling' },
      { q: 'Which subject does it sit in?', k: 'Subject', chips: ['Data & Analytics', 'Business', 'Technology'], demo: 'Data & Analytics' }
    ];
    this.K = [['title', 'Title'], ['desc', 'Description'], ['aud', 'Who it’s for'], ['pre', 'Before you start'], ['skills', 'Skills'], ['out', 'Outcomes'], ['cur', 'Curriculum']];
    const full = (props || {}).variant === 'proposal';
    this.state = { answers: full ? this.Q.map((x) => x.demo) : [], text: '', typing: false, phase: full ? 'proposal' : 'chat', dec: full ? { title: 'a', desc: 'a', aud: 'a', pre: 'e' } : {}, err: false, bp: false, notes: false };
  }
  componentWillUnmount() { clearTimeout(this.t); }
  send(v) {
    const t = (v || '').trim();
    if (!t || this.state.typing || this.state.answers.length >= 5) return;
    this.setState({ answers: [...this.state.answers, t], text: '', typing: true });
    this.t = setTimeout(() => this.setState({ typing: false }), 700);
  }
  renderVals() {
    const { answers, typing, phase, dec, err, text, bp, notes } = this.state;
    const n = answers.length;
    const msgs = [];
    const nova = (t, ql) => ({ text: t, nd: 'flex', md: 'none', dd: 'none', qd: ql ? 'inline' : 'none', ql: ql || '', edit: () => {} });
    answers.forEach((a, i) => {
      msgs.push(nova(this.Q[i].q, 'Question ' + (i + 1) + ' of 5'));
      msgs.push({ text: a, nd: 'none', md: 'flex', dd: 'none', qd: 'none', ql: '', edit: () => this.setState({ answers: answers.slice(0, i), text: a, phase: 'chat', typing: false }) });
    });
    if (typing) msgs.push({ text: '', nd: 'none', md: 'none', dd: 'flex', qd: 'none', ql: '', edit: () => {} });
    else if (n < 5) msgs.push(nova(this.Q[n].q, 'Question ' + (n + 1) + ' of 5'));
    else msgs.push(nova('That’s everything I need. I’ll draft a title, description, skills, outcomes and a first curriculum. You review every part.', ''));
    const reviewed = this.K.filter(([k]) => dec[k]).length;
    const d = {};
    const col = { a: ['#E7F5EE', '#0F6B45', 'Accepted'], e: ['#FFF4DE', '#8A5A00', 'Edit later'], x: ['#F1F3F8', '#4A5578', 'Rejected'] };
    this.K.forEach(([k]) => {
      const v = dec[k];
      const o = (val) => { const on = v === val; const c = col[val]; return { on: on ? 'true' : 'false', pick: () => this.setState({ dec: { ...this.state.dec, [k]: on ? undefined : val }, err: false }), bg: on ? c[0] : '#FFFFFF', fg: on ? c[1] : '#4A5578', bd: on ? c[1] : '#E6EAF3' }; };
      d[k] = { a: o('a'), e: o('e'), x: o('x'), sd: v ? 'inline-flex' : 'none', st: v ? col[v][2] : '', sb: v ? col[v][0] : '', sc: v ? col[v][1] : '',
        op: v === 'x' ? '0.4' : '1', td: v === 'x' ? 'line-through' : 'none', ring: v === 'a' ? 'inset 3px 0 0 #0F6B45' : (v === 'e' ? 'inset 3px 0 0 #E2A024' : 'none') };
    });
    const accepted = this.K.filter(([k]) => dec[k] === 'a').length;
    const later = this.K.filter(([k]) => dec[k] === 'e').length;
    const widths = ['82%', '64%', '72%', '58%', '46%'];
    return {
      chatView: phase === 'chat' || phase === 'drafting', reviewView: phase === 'proposal', doneView: phase === 'done',
      stageLabel: phase === 'proposal' ? 'Review Nova’s draft' : (phase === 'done' ? 'Draft ready' : 'Sketch it with Nova'),
      progress: phase === 'proposal' || phase === 'done' ? 'Draft ready' : (n < 5 ? 'Question ' + (n + 1) + ' of 5' : 'All five answered'),
      segs: [0, 1, 2, 3, 4].map((i) => ({ c: (i < n || phase !== 'chat') ? '#1652F0' : (i === n ? '#AFC1F5' : '#E6EAF3') })),
      msgs, composerShown: n < 5 && phase === 'chat', readyShown: n === 5 && !typing && phase === 'chat', draftingShown: phase === 'drafting',
      chips: (n < 5 && !typing) ? this.Q[n].chips.map((label) => ({ label, pick: () => this.send(label) })) : [],
      text, onText: (e) => this.setState({ text: e.target.value }),
      onKey: (e) => { if (e.key === 'Enter') { e.preventDefault(); this.send(this.state.text); } },
      sendText: () => this.send(this.state.text), sendBg: text.trim() ? '#1652F0' : '#CBD3E6',
      draft: () => { this.setState({ phase: 'drafting' }); this.t = setTimeout(() => this.setState({ phase: 'proposal' }), 1600); },
      bpBtnV: (phase === 'chat' || phase === 'drafting') ? 'visible' : 'hidden', bpState: phase === 'drafting' ? 'Drafting' : 'Taking shape', bpCount: n + '/5',
      bpCls: bp ? 'fx-open' : '', bpOpen: bp ? 'true' : 'false', toggleBp: () => this.setState({ bp: !this.state.bp }),
      facts: this.Q.map((q, i) => ({ label: q.k, value: answers[i] || '', vd: answers[i] ? 'block' : 'none', sd: answers[i] ? 'none' : 'block', w: widths[i], dot: answers[i] ? '#0F6B45' : '#FFFFFF', dbd: answers[i] ? '#0F6B45' : '#CBD3E6' })),
      backToChat: () => this.setState({ phase: 'chat' }),
      d, reviewed, pctDeg: Math.round(reviewed / 7 * 360) + 'deg', errShown: err,
      parts: this.K.map(([k, label]) => { const v = dec[k]; return { label, href: '#rv-' + k, st: v ? col[v][2] : 'To review', sc: v ? col[v][1] : '#8A93AD', dot: v ? col[v][1] : '#FFFFFF', dbd: v ? col[v][1] : '#CBD3E6' }; }),
      acceptRest: () => { const nd = { ...this.state.dec }; this.K.forEach(([k]) => { if (!nd[k]) nd[k] = 'a'; }); this.setState({ dec: nd, err: false }); },
      openBg: reviewed === 7 ? '#1652F0' : '#AFC1F5', openSh: reviewed === 7 ? '0 1px 0 rgba(255,255,255,.25) inset, 0 10px 24px rgba(22,82,240,.24)' : 'none', openDis: reviewed === 7 ? 'false' : 'true',
      open: () => { if (reviewed < 7) this.setState({ err: true }); else this.setState({ phase: 'done' }); },
      notesShown: notes, notesOpen: notes ? 'true' : 'false', notesRot: notes ? 'rotate(180deg)' : 'none', toggleNotes: () => this.setState({ notes: !this.state.notes }),
      doneText: accepted + ' accepted ' + (accepted === 1 ? 'part is' : 'parts are') + ' now in your new course draft.' + (later ? ' ' + later + ' marked “edit later” ' + (later === 1 ? 'is' : 'are') + ' flagged for you in the Studio.' : '')
    };
  }
}'''
html='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Credalio · New course with Nova</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">
<style>
'''+CSS+'''</style>
</helmet>
<div class="fx-root">
'''+TOP+'''
'''+CHAT+'''
'''+REVIEW+'''
'''+DONE+'''
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":820}}'>
'''+S+'''
</script>
</body>
</html>
'''
open(P+'CR-CREATE-002A.dc.html','w').write(html)
print('CREATE-002A v3 built')
