# CREATE-002A (blueprint chat) + 002Ab (draft review), one source
SEG='<div aria-hidden="true" style="display: grid; grid-template-columns: repeat(5, 22px); gap: 4px"><sc-for list="{{segs}}" as="s" hint-placeholder-count="5"><span style="height: 4px; border-radius: 4px; background: {{s.c}}; transition: background .3s ease"></span></sc-for></div>'
DOTS='<span style="display: inline-flex; gap: 5px; padding: 8px 0" aria-label="Nova is typing"><span class="cp-dot"></span><span class="cp-dot" style="animation-delay: .15s"></span><span class="cp-dot" style="animation-delay: .3s"></span></span>'
SPK14='<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l1.9 6.1L20 10l-6.1 1.9L12 18l-1.9-6.1L4 10l6.1-1.9z"></path></svg>'

CHAT=f'''<sc-if value="{{{{chatView}}}}" hint-placeholder-val="{{{{true}}}}">
<a href="CR-CREATE-001.dc.html" class="ds-back ob-in" style="margin-top: 4px">{ICON(I["back"],16,2.2)}Back</a>
<div class="ob-in" style="margin-top: 8px"><h1 class="ds-h1">Let’s sketch your course</h1><p class="ds-sub">Five quick questions. Then Nova drafts it, and you decide what stays.</p></div>
<div class="c2-grid ob-in2" style="margin-top: 24px; display: grid; grid-template-columns: minmax(0, 1fr) 380px; gap: 20px; align-items: start">
<section class="ds-card c2-conv" aria-label="Conversation with Nova" style="padding: 26px 28px; display: flex; flex-direction: column; box-sizing: border-box">
<div style="display: flex; align-items: center; justify-content: space-between; gap: 12px"><span style="font-size: 13.5px; font-weight: 600; color: #4A5578">{{{{progress}}}}</span>{SEG}</div>
<ol aria-label="Your answers so far" style="list-style: none; margin: 14px 0 0 0; padding: 0; display: flex; flex-direction: column; gap: 6px"><sc-for list="{{{{hist}}}}" as="h" hint-placeholder-count="0"><li class="c2-h"><span style="display: flex; flex-direction: column; gap: 2px; min-width: 0; flex-grow: 1"><span style="font-size: 12.5px; color: #5B6582">{{{{h.q}}}}</span><span style="font-size: 14.5px; font-weight: 600; color: #0B1433">{{{{h.a}}}}</span></span><button type="button" class="c2-edit" onClick="{{{{h.edit}}}}" aria-label="Edit this answer">{ICON(I["pencil"],15,1.9)}</button></li></sc-for></ol>
<div style="height: 22px"></div>
<sc-if value="{{{{typingShown}}}}" hint-placeholder-val="{{{{false}}}}"><div style="display: flex; align-items: center; gap: 14px">{NOVA_AV(44)}{DOTS}</div></sc-if>
<sc-if value="{{{{askShown}}}}" hint-placeholder-val="{{{{true}}}}"><div class="cp-pop" aria-live="polite" style="display: flex; align-items: flex-start; gap: 14px">{NOVA_AV(44)}<h2 class="c2-q" style="margin: 6px 0 0 0; font-size: clamp(20px, 1.8vw, 24px); line-height: 1.35; font-weight: 600; letter-spacing: -0.015em; color: #0B1433">{{{{question}}}}</h2></div>
<div style="margin-top: 18px; padding-left: 58px" class="c2-ans">
<div style="display: flex; flex-wrap: wrap; gap: 8px"><sc-for list="{{{{chips}}}}" as="ch" hint-placeholder-count="3"><button type="button" class="ds-chip cp-pop" onClick="{{{{ch.pick}}}}">{{{{ch.label}}}}</button></sc-for></div>
<div class="c2-in" style="margin-top: 12px; display: flex; align-items: center; gap: 8px; height: 54px; box-sizing: border-box; padding: 0 7px 0 18px; border-radius: 999px; border: 1.5px solid #D6DDEE; background: #FFFFFF"><label class="sr-only" for="c2-in">Your answer</label><input id="c2-in" value="{{{{text}}}}" onChange="{{{{onText}}}}" onKeyDown="{{{{onKey}}}}" placeholder="Or type your own answer" autocomplete="off" style="flex-grow: 1; min-width: 0; border: 0; outline: none; background: transparent; font-family: inherit; font-size: 15px; color: #0B1433"><button type="button" onClick="{{{{sendText}}}}" aria-label="Send" style="width: 40px; height: 40px; flex-shrink: 0; border: 0; border-radius: 50%; background: {{{{sendBg}}}}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: background .2s ease">{ICON(I["send"],18,2.4)}</button></div>
</div></sc-if>
<sc-if value="{{{{readyShown}}}}" hint-placeholder-val="{{{{false}}}}"><div class="cp-pop" style="display: flex; align-items: flex-start; gap: 14px">{NOVA_AV(44)}<div><h2 style="margin: 6px 0 0 0; font-size: clamp(20px, 1.8vw, 24px); font-weight: 600; letter-spacing: -0.015em">That’s everything I need.</h2><p style="margin: 6px 0 0 0; font-size: 15px; line-height: 1.55; color: #4A5578">I’ll draft a title, description, skills, outcomes and a first curriculum. You review every part.</p><button type="button" class="ds-btn" onClick="{{{{draft}}}}" style="margin-top: 18px"><span style="display: inline-flex; align-items: center; gap: 8px">{SPK14}Draft my course</span><span class="ob-arrow">{ICON(I["arrow"],18,2.4)}</span></button></div></div></sc-if>
<sc-if value="{{{{draftingShown}}}}" hint-placeholder-val="{{{{false}}}}"><div class="cp-pop" role="status" style="display: flex; align-items: center; gap: 14px">{NOVA_AV(44)}<div><span style="font-size: 18px; font-weight: 600">Drafting your course</span>{DOTS}</div></div></sc-if>
</section>
<aside class="ds-card c2-bp" aria-label="Course blueprint" style="padding: 22px; position: sticky; top: 88px; background: #FFFFFF url({BG}) center top / 100% auto no-repeat">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 13.5px; font-weight: 600; color: #0B1433">Course blueprint</span><span style="display: inline-flex; align-items: center; gap: 6px; font-size: 12.5px; font-weight: 600; color: #0E3BB8"><span class="c2-live"></span>{{{{bpState}}}}</span></div>
<div style="margin-top: 16px; padding: 18px; border-radius: 16px; background: #FFFFFF; border: 1.5px solid #E6EAF3; box-shadow: 0 12px 28px rgba(22, 82, 240, 0.08)">
<span style="display: block; font-size: 12px; font-weight: 600; color: #8A93AD">Course</span>
<span class="c2-shim" style="display: block; margin-top: 8px; height: 14px; width: 70%"></span>
<ul style="list-style: none; margin: 14px 0 0 0; padding: 0"><sc-for list="{{{{facts}}}}" as="f" hint-placeholder-count="5"><li style="padding: 11px 0; border-top: 1px solid #EEF1F7"><span style="display: block; font-size: 12px; color: #5B6582">{{{{f.label}}}}</span><span class="c2-new" style="display: {{{{f.vd}}}}; margin-top: 3px; font-size: 14px; line-height: 1.45; font-weight: 500; color: #0B1433">{{{{f.value}}}}</span><span class="c2-shim" style="display: {{{{f.sd}}}}; margin-top: 7px; height: 10px; width: {{{{f.w}}}}"></span></li></sc-for></ul>
</div>
<p style="margin: 14px 0 0 0; font-size: 13px; line-height: 1.5; color: #5B6582">Nova drafts the rest from this: title, description, outcomes and a first curriculum.</p>
</aside>
</div>
</sc-if>'''

def OPT(k,v,label):
    return f'<button type="button" class="c3-opt" onClick="{{{{d.{k}.{v}.pick}}}}" aria-pressed="{{{{d.{k}.{v}.on}}}}" style="border-color: {{{{d.{k}.{v}.bd}}}}; background: {{{{d.{k}.{v}.bg}}}}; color: {{{{d.{k}.{v}.fg}}}}"><span style="display: {{{{d.{k}.{v}.ckd}}}}">{ICON(I["check"],12,3.2)}</span>{label}</button>'
def BLOCK(k,label,content):
    return f'''<div class="c3-blk" style="border-left-color: {{{{d.{k}.bar}}}}; background: {{{{d.{k}.bg}}}}">
<div class="c3-head"><span style="display: inline-flex; align-items: center; gap: 8px; font-size: 13.5px; font-weight: 600; color: #4A5578">{label}<span style="display: {{{{d.{k}.sd}}}}; height: 22px; padding: 0 8px; border-radius: 999px; background: {{{{d.{k}.sb}}}}; color: {{{{d.{k}.sc}}}}; font-size: 11.5px; font-weight: 500; align-items: center">{{{{d.{k}.st}}}}</span></span><div class="c3-seg" role="group" aria-label="Decision for {label}">{OPT(k,"a","Accept")}{OPT(k,"e","Edit later")}{OPT(k,"x","Reject")}</div></div>
<div style="margin-top: 10px; opacity: {{{{d.{k}.op}}}}; text-decoration: {{{{d.{k}.td}}}}; transition: opacity .2s ease">{content}</div>
</div>'''
def LVL(name):
    return f'<li style="display: flex; align-items: center; justify-content: space-between; gap: 14px; padding: 10px 0; border-top: 1px solid #EEF1F7"><span style="font-size: 15px; font-weight: 600; color: #0B1433">{name}</span><span style="display: inline-flex; align-items: center; gap: 10px; font-size: 13px; color: #4A5578"><span aria-hidden="true" style="display: inline-grid; grid-template-columns: repeat(3, 18px); gap: 3px"><span style="height: 6px; border-radius: 3px; background: #AFC1F5"></span><span style="height: 6px; border-radius: 3px; background: #1652F0"></span><span style="height: 6px; border-radius: 3px; background: #E6EAF3"></span></span>Beginner → Intermediate</span></li>'
OUT=''.join(f'<li style="display: flex; gap: 10px; padding: 6px 0; font-size: 15px; line-height: 1.5; color: #0B1433"><span style="width: 22px; height: 22px; flex-shrink: 0; margin-top: 1px; border-radius: 50%; background: #EAF0FF; color: #1652F0; display: flex; align-items: center; justify-content: center">{ICON(I["check"],12,3)}</span>{t}</li>' for t in ['Write SQL queries to retrieve, filter and aggregate business data.','Clean and join tables to prepare data for analysis.','Present findings and recommendations to non-technical stakeholders.'])
MODS=''.join(f'<li style="display: flex; align-items: center; gap: 12px; padding: 10px 12px; border-radius: 12px; background: #FFFFFF; border: 1px solid #E6EAF3"><span style="width: 28px; height: 28px; flex-shrink: 0; border-radius: 9px; background: #0B1433; color: #FFFFFF; font-size: 13px; font-weight: 600; display: flex; align-items: center; justify-content: center">{i+1}</span><span style="font-size: 15px; color: #0B1433">{t}</span></li>' for i,t in enumerate(['Why data and SQL matter','Querying with SELECT and WHERE','Joining and cleaning data','Aggregating for business questions','Presenting findings']))
USERS='<circle cx="9" cy="8" r="3.5"></circle><path d="M2.5 20a6.5 6.5 0 0 1 13 0"></path><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14.5a6.5 6.5 0 0 1 3.5 5.5"></path>'
BARS='<path d="M5 20v-4M10 20v-8M15 20V8M20 20V4"></path>'
DOC=''.join([
 BLOCK('title','Course title','<p class="c3-t" style="margin: 0; font-size: 22px; font-weight: 600; letter-spacing: -0.02em; color: #0B1433">SQL for Business Analysis</p>'),
 BLOCK('desc','Description','<p class="c3-d" style="margin: 0; font-size: 16px; line-height: 1.6; color: #0B1433">Learn to query, clean and analyse business data with SQL, and present clear recommendations managers can act on.</p>'),
 BLOCK('aud','Audience',f'<div style="display: flex; flex-direction: column; gap: 8px; font-size: 15px; color: #0B1433"><span style="display: flex; align-items: center; gap: 10px"><span style="color: #1652F0; display: flex">{ICON(USERS,18)}</span>Early-career analysts and career switchers</span><span style="display: flex; align-items: center; gap: 10px"><span style="color: #1652F0; display: flex">{ICON(BARS,18)}</span>Comfortable with spreadsheets; no SQL yet</span></div>'),
 BLOCK('pre','Prerequisites','<p style="margin: 0; font-size: 15px; color: #0B1433">Comfortable with spreadsheets <span style="color: #5B6582">(recommended)</span></p>'),
 BLOCK('skills','Skills',f'<ul style="list-style: none; margin: 0; padding: 0" class="c3-first">{LVL("SQL")}{LVL("Data cleaning")}{LVL("Data storytelling")}</ul>'),
 BLOCK('out','Learning outcomes',f'<ul style="list-style: none; margin: 0; padding: 0">{OUT}</ul>'),
 BLOCK('cur','First curriculum',f'<ol style="list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 8px">{MODS}</ol>'),
])
NOTES=''.join(f'<li style="display: flex; gap: 10px; padding: 10px 0; border-top: 1px solid #EEF1F7; font-size: 14px; line-height: 1.5; color: #0B1433"><span style="color: #1652F0; display: flex; margin-top: 3px">{SPK14}</span>{t}</li>' for t in ['Modules are short, since many of your learners are switching careers.','Skills start at Beginner, because they haven’t used SQL yet.','It ends with presenting, so learners leave with something managers can use.'])
REVIEW=f'''<sc-if value="{{{{reviewView}}}}" hint-placeholder-val="{{{{false}}}}">
<button type="button" class="ds-back ob-in" onClick="{{{{backToChat}}}}" style="margin-top: 4px; border: 0; background: none; cursor: pointer; font-family: inherit">{ICON(I["back"],16,2.2)}Back to questions</button>
<div class="ob-in" style="margin-top: 8px"><span style="display: inline-flex; align-items: center; gap: 8px; font-size: 13.5px; color: #4A5578">{NOVA_AV(26, False)}Nova’s first draft · from your 5 answers</span><h1 class="ds-h1" style="margin-top: 8px">Review your course</h1><p class="ds-sub">Accept, edit later or reject each part. Nothing enters the Studio until you say so.</p></div>
<button type="button" class="c3-why" onClick="{{{{toggleNotes}}}}" aria-expanded="{{{{notesOpen}}}}">{NOVA_AV(26, False)}<span style="flex-grow: 1; text-align: left">Why Nova drafted it this way</span><span style="display: flex; transform: {{{{notesRot}}}}; transition: transform .2s ease"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"></path></svg></span></button>
<div class="c3-grid ob-in2" style="margin-top: 22px; display: grid; grid-template-columns: minmax(0, 1fr) 320px; gap: 20px; align-items: start">
<section id="c2-prop" class="ds-card" aria-label="Draft course" style="padding: 8px; display: flex; flex-direction: column; gap: 6px">{DOC}</section>
<aside class="c3-rail {{{{notesCls}}}}" style="position: sticky; top: 88px; display: flex; flex-direction: column; gap: 14px">
<div class="ds-card" style="padding: 20px; background: #FFFFFF url({BG}) center top / 100% auto no-repeat"><div style="display: flex; align-items: center; gap: 10px">{NOVA_AV(36)}<span style="font-size: 15px; font-weight: 600">Why it looks like this</span></div><ul style="list-style: none; margin: 12px 0 0 0; padding: 0">{NOTES}</ul>
<div style="margin-top: 12px; display: flex; align-items: center; gap: 6px; height: 46px; box-sizing: border-box; padding: 0 5px 0 14px; border-radius: 999px; border: 1.5px solid #D6DDEE; background: #FFFFFF"><label class="sr-only" for="c3-ask">Ask Nova to change something</label><input id="c3-ask" placeholder="Ask Nova to change something" style="flex-grow: 1; min-width: 0; border: 0; outline: none; background: transparent; font-family: inherit; font-size: 14px; color: #0B1433"><button type="button" aria-label="Send" style="width: 36px; height: 36px; flex-shrink: 0; border: 0; border-radius: 50%; background: #1652F0; color: #FFFFFF; display: flex; align-items: center; justify-content: center; cursor: pointer">{ICON(I["send"],16,2.4)}</button></div></div>
</aside>
</div>
<div class="c3-bar" role="region" aria-label="Review progress">
<div class="c3-prog" style="display: flex; flex-direction: column; gap: 7px; min-width: 170px"><span style="font-size: 14px; color: #3A4566"><span style="font-weight: 600; color: #0B1433">{{{{reviewed}}}} of 7</span> reviewed</span><span class="c3-pbar" style="display: block; width: 180px; height: 6px; border-radius: 6px; background: #E6EAF3; overflow: hidden"><span style="display: block; height: 100%; width: {{{{pct}}}}; border-radius: 6px; background: #1652F0; transition: width .3s ease"></span></span></div>
<sc-if value="{{{{errShown}}}}" hint-placeholder-val="{{{{false}}}}"><span role="alert" style="font-size: 13.5px; color: #B42318">Review every part first.</span></sc-if>
<span class="c3-sp" style="flex-grow: 1"></span>
<button type="button" class="ds-ghost c3-rest" onClick="{{{{acceptRest}}}}">Accept the rest</button>
<button type="button" class="ds-btn" onClick="{{{{open}}}}" aria-disabled="{{{{openDis}}}}" style="background: {{{{openBg}}}}; box-shadow: {{{{openSh}}}}"><span>Open Course Studio</span><span class="ob-arrow">{ICON(I["arrow"],18,2.4)}</span></button>
</div>
</sc-if>
<sc-if value="{{{{doneView}}}}" hint-placeholder-val="{{{{false}}}}"><section class="ds-card cp-pop" style="margin: 40px auto 0 auto; max-width: 620px; padding: 40px 28px; display: flex; flex-direction: column; align-items: center; text-align: center; background: #FFFFFF url({BG}) center top / 100% auto no-repeat">
<span style="width: 64px; height: 64px; border-radius: 50%; background: #0F6B45; color: #FFFFFF; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 0 8px rgba(15, 107, 69, 0.12)">{ICON(I["check"],28,2.8)}</span>
<h1 class="ds-h1" style="margin-top: 20px">Your course draft is ready.</h1>
<p class="ds-sub" style="max-width: 460px">{{{{doneText}}}}</p>
{BTNA("#","Open Course Studio",extra='style="margin-top: 22px"')}
</section></sc-if>'''
C2_CSS='''@keyframes c2Shim{0%{background-position:-200px 0}100%{background-position:200px 0}}
@keyframes c2New{0%{background:#EAF0FF}100%{background:transparent}}
@keyframes c2Live{0%{box-shadow:0 0 0 0 rgba(22,82,240,.4)}100%{box-shadow:0 0 0 7px rgba(22,82,240,0)}}
.c2-shim{border-radius:6px;background:linear-gradient(90deg,#EEF1F7 0px,#F7F9FD 80px,#EEF1F7 160px);background-size:400px 100%;animation:c2Shim 1.6s linear infinite}
.c2-new{border-radius:6px;animation:c2New 1.2s ease both}
.c2-live{width:8px;height:8px;border-radius:50%;background:#1652F0;animation:c2Live 1.6s ease-out infinite}
.c2-h{display:flex;align-items:center;gap:12px;padding:10px 12px;border-radius:14px;background:#F7F9FD;animation:cpPop .35s ease both}
.c2-edit{width:36px;height:36px;flex-shrink:0;border:0;border-radius:50%;background:transparent;color:#5B6582;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:background .2s ease,color .2s ease}
.c2-edit:hover{background:#FFFFFF;color:#1652F0}
.c2-in:focus-within{border-color:#1652F0 !important;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.c2-in input::placeholder{color:#8A93AD}
.c3-blk{border-left:3px solid transparent;border-radius:14px;padding:18px 20px;transition:background .2s ease,border-color .2s ease}
.c3-head{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
.c3-seg{display:inline-flex;gap:4px;padding:3px;border-radius:13px;background:#F5F8FF}
.c3-opt{height:32px;padding:0 11px;box-sizing:border-box;border-radius:10px;border:1.5px solid transparent;font-family:inherit;font-size:13px;font-weight:600;cursor:pointer;display:inline-flex;align-items:center;gap:5px;white-space:nowrap;transition:all .2s ease}
.c3-opt:hover{color:#0B1433 !important}
.c3-opt:focus-visible,.c2-edit:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:2px}
.c3-first > li:first-child{border-top:0 !important}
.c3-why{display:none}
.c3-bar{position:sticky;bottom:16px;z-index:5;margin-top:18px;display:flex;align-items:center;flex-wrap:wrap;gap:12px 16px;padding:12px 12px 12px 22px;border-radius:22px;background:rgba(255,255,255,.94);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border:1.5px solid #E6EAF3;box-shadow:0 18px 40px rgba(11,20,51,.12)}
@media (prefers-reduced-motion: reduce){.c2-shim,.c2-new,.c2-live,.c2-h{animation:none}}
@media (max-width: 1180px){.c3-grid{grid-template-columns:minmax(0,1fr) !important}.c3-rail{position:static !important}}
@media (max-width: 1080px){.c2-grid{grid-template-columns:minmax(0,1fr) !important}.c2-bp{position:static !important}}
@media (max-width: 860px){
.c2-grid,.c3-grid{margin-top:14px !important}
.c2-conv{padding:16px !important}
.c2-bp{display:none !important}
.c2-ans{padding-left:0 !important;margin-top:14px !important}
.c2-q{font-size:19px !important;margin-top:4px !important}
.c2-h{padding:8px 10px !important;border-radius:12px !important}
.c2-h span span:first-child{font-size:12px !important}
.c2-h span span:last-child{font-size:13.5px !important}
.c2-edit{width:32px;height:32px}
.c2-in{height:48px !important;padding:0 5px 0 14px !important}
.c3-why{display:flex;align-items:center;gap:10px;width:100%;margin-top:14px;height:48px;padding:0 14px 0 8px;box-sizing:border-box;border-radius:14px;border:1.5px solid #E6EAF3;background:#FFFFFF;color:#0B1433;font-family:inherit;font-size:14px;font-weight:600;cursor:pointer}
.c3-rail{display:none !important;order:-1}
.c3-rail.c3-open{display:flex !important}
.c3-head{flex-direction:column;align-items:stretch !important;gap:8px !important}
.c3-seg{display:grid !important;grid-template-columns:repeat(3,minmax(0,1fr))}
.c3-opt{justify-content:center;height:34px}
.c3-blk{padding:14px 12px !important}
.c3-t{font-size:19px !important}
.c3-d{font-size:15px !important}
.c3-blk li{font-size:14px !important}
.c3-first li > span:last-child > span[aria-hidden]{display:none !important}
.c3-bar{display:grid !important;grid-template-columns:minmax(0,1fr) auto;gap:10px !important;padding:12px !important;bottom:8px;border-radius:18px !important}
.c3-sp{display:none}
.c3-prog{min-width:0 !important}
.c3-pbar{width:100% !important}
.c3-rest{height:36px !important;font-size:13.5px !important;padding:0 12px !important}
.c3-bar .ds-btn{grid-column:1/-1;justify-content:space-between}
.c3-bar [role=alert]{grid-column:1/-1}
}
'''
S_C2='''class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.Q = [
      { q: 'What should someone be able to do after learning from you?', k: 'Learners will be able to', chips: ['Analyse business data with SQL', 'Build dashboards managers use', 'Clean and prepare messy data'], demo: 'Analyse business data with SQL and present clear recommendations to managers.' },
      { q: 'Who is this course for?', k: 'For', chips: ['Early-career analysts', 'Career switchers', 'Managers who use data'], demo: 'Early-career analysts and career switchers' },
      { q: 'What should they already know?', k: 'Starting level', chips: ['Comfortable with spreadsheets', 'Some SQL', 'Nothing yet'], demo: 'Comfortable with spreadsheets; no SQL yet' },
      { q: 'Which skills should they build?', k: 'Skills', chips: ['SQL', 'Data cleaning', 'Data storytelling'], demo: 'SQL, data cleaning, data storytelling' },
      { q: 'Which subject does it sit in?', k: 'Subject', chips: ['Data & Analytics', 'Business', 'Technology'], demo: 'Data & Analytics' }
    ];
    this.K = ['title', 'desc', 'aud', 'pre', 'skills', 'out', 'cur'];
    const full = (props || {}).variant === 'proposal';
    this.state = { nav: false, answers: full ? this.Q.map((x) => x.demo) : [], text: '', typing: false, phase: full ? 'proposal' : 'chat', dec: full ? { title: 'a', desc: 'a', aud: 'a', pre: 'e' } : {}, err: false };
  }
  componentWillUnmount() { clearTimeout(this.t); }
  send(v) {
    const t = (v || '').trim();
    if (!t || this.state.typing || this.state.answers.length >= 5) return;
    this.setState({ answers: [...this.state.answers, t], text: '', typing: true });
    this.t = setTimeout(() => this.setState({ typing: false }), 700);
  }
  renderVals() {
    const { answers, typing, phase, dec, err, text } = this.state;
    const n = answers.length;
    const reviewed = this.K.filter((k) => dec[k]).length;
    const d = {};
    this.K.forEach((k) => {
      const v = dec[k];
      const o = (val) => { const on = v === val; return { on: on ? 'true' : 'false', pick: () => this.setState({ dec: { ...this.state.dec, [k]: on ? undefined : val }, err: false }), bd: on ? '#1652F0' : 'transparent', bg: on ? '#EAF0FF' : 'transparent', fg: on ? '#0E3BB8' : '#4A5578', ckd: on ? 'inline-flex' : 'none' }; };
      d[k] = { a: o('a'), e: o('e'), x: o('x'),
        bar: v === 'a' ? '#0F6B45' : (v === 'e' ? '#E2A024' : (v === 'x' ? '#CBD3E6' : 'transparent')),
        bg: v === 'a' ? '#FAFDFB' : (v === 'e' ? '#FFFCF3' : '#FFFFFF'),
        op: v === 'x' ? '0.45' : '1', td: v === 'x' ? 'line-through' : 'none',
        sd: v ? 'inline-flex' : 'none', st: v === 'a' ? 'Accepted' : (v === 'e' ? 'Edit later' : 'Rejected'),
        sb: v === 'a' ? '#E7F5EE' : (v === 'e' ? '#FFF4DE' : '#F1F3F8'), sc: v === 'a' ? '#0F6B45' : (v === 'e' ? '#8A5A00' : '#4A5578') };
    });
    const accepted = this.K.filter((k) => dec[k] === 'a').length;
    const later = this.K.filter((k) => dec[k] === 'e').length;
    const widths = ['82%', '64%', '72%', '58%', '46%'];
    return {
      navCls: this.state.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !this.state.nav }),
      chatView: phase === 'chat' || phase === 'drafting', reviewView: phase === 'proposal', doneView: phase === 'done',
      progress: n < 5 ? 'Question ' + (n + 1) + ' of 5' : 'All five answered',
      segs: [0, 1, 2, 3, 4].map((i) => ({ c: i < n ? '#1652F0' : (i === n ? '#AFC1F5' : '#E6EAF3') })),
      hist: answers.map((a, i) => ({ q: this.Q[i].q, a, edit: () => this.setState({ answers: answers.slice(0, i), text: a, phase: 'chat', typing: false }) })),
      typingShown: typing, askShown: n < 5 && !typing, question: n < 5 ? this.Q[n].q : '',
      readyShown: n === 5 && !typing && phase === 'chat', draftingShown: phase === 'drafting',
      chips: n < 5 ? this.Q[n].chips.map((label) => ({ label, pick: () => this.send(label) })) : [],
      text, onText: (e) => this.setState({ text: e.target.value }),
      onKey: (e) => { if (e.key === 'Enter') { e.preventDefault(); this.send(this.state.text); } },
      sendText: () => this.send(this.state.text), sendBg: text.trim() ? '#1652F0' : '#CBD3E6',
      draft: () => { this.setState({ phase: 'drafting' }); this.t = setTimeout(() => this.setState({ phase: 'proposal' }), 1600); },
      bpState: phase === 'drafting' ? 'Drafting' : 'Taking shape',
      facts: this.Q.map((q, i) => ({ label: q.k, value: answers[i] || '', vd: answers[i] ? 'block' : 'none', sd: answers[i] ? 'none' : 'block', w: widths[i] })),
      backToChat: () => this.setState({ phase: 'chat' }),
      notesCls: this.state.notes ? 'c3-open' : '', notesOpen: this.state.notes ? 'true' : 'false', notesRot: this.state.notes ? 'rotate(180deg)' : 'none', toggleNotes: () => this.setState({ notes: !this.state.notes }),
      d, reviewed, pct: Math.round(reviewed / 7 * 100) + '%', errShown: err,
      acceptRest: () => { const nd = { ...this.state.dec }; this.K.forEach((k) => { if (!nd[k]) nd[k] = 'a'; }); this.setState({ dec: nd, err: false }); },
      openBg: reviewed === 7 ? '#1652F0' : '#AFC1F5', openSh: reviewed === 7 ? '0 1px 0 rgba(255,255,255,.25) inset, 0 10px 24px rgba(22,82,240,.24)' : 'none', openDis: reviewed === 7 ? 'false' : 'true',
      open: () => { if (reviewed < 7) this.setState({ err: true }); else this.setState({ phase: 'done' }); },
      doneText: accepted + ' accepted ' + (accepted === 1 ? 'part is' : 'parts are') + ' now in your new course draft.' + (later ? ' ' + later + ' marked “edit later” ' + (later === 1 ? 'is' : 'are') + ' flagged for you in the Studio.' : '')
    };
  }
}'''
open(P+'CR-CREATE-002A.dc.html','w').write(SHELL('Create new',CHAT+REVIEW,'Credalio · Create with Nova',S_C2,C2_CSS,900))
print('CREATE-002A built')
