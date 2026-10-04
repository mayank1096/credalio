# Redesign v2: 008 reveal, Studio launchpad, create-mode choice, Nova blueprint chat, draft review
exec(open('dash.py').read())
BG='/_blob/d268046654a4206d2a726e62005bcc59'

def STAR(x,y,s,c,d):
    return f'<svg class="rc-tw" aria-hidden="true" width="{s}" height="{s}" viewBox="0 0 24 24" style="position: absolute; left: {x}; top: {y}; animation-delay: {d}s"><path d="M12 2l2.2 7.8L22 12l-7.8 2.2L12 22l-2.2-7.8L2 12l7.8-2.2z" fill="{c}"></path></svg>'

HEAD='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>TITLE</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">
<style>
CSS</style>
</helmet>
'''
TAIL='''
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":820}}'>
SCRIPT
</script>
</body>
</html>
'''
LOGO_ONB='''<div style="display: flex; align-items: center; gap: 10px"><span style="width: 32px; height: 32px; border-radius: 9px; background: #1652F0; display: flex; align-items: center; justify-content: center"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" aria-hidden="true"><path d="M17.5 7.2A7 7 0 1 0 17.5 16.8"></path></svg></span><span class="rc-brand" style="font-size: 21px; font-weight: 600; letter-spacing: -0.02em; color: #0B1433">Credalio</span></div>'''

# =============== 008 · You're a Creator ===============
RC_CSS='''body{margin:0;background:#FFFFFF}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@keyframes obIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
@keyframes rcDrop{0%{opacity:0;transform:translateY(-70px) rotate(10deg)}30%{opacity:1;transform:translateY(0) rotate(-7deg)}48%{transform:rotate(4.6deg)}64%{transform:rotate(-2.8deg)}78%{transform:rotate(1.5deg)}90%{transform:rotate(-.6deg)}100%{opacity:1;transform:rotate(0deg)}}
@keyframes rcSway{0%{transform:rotate(0deg)}25%{transform:rotate(4deg)}75%{transform:rotate(-4deg)}100%{transform:rotate(0deg)}}
@keyframes rcShine{0%{transform:translateX(-120%) skewX(-18deg)}100%{transform:translateX(320%) skewX(-18deg)}}
@keyframes rcDraw{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}
@keyframes rcPop{0%{opacity:0;transform:scale(.3)}70%{opacity:1;transform:scale(1.15)}100%{opacity:1;transform:scale(1)}}
@keyframes rcTw{0%,100%{opacity:.25;transform:scale(.7)}50%{opacity:1;transform:scale(1)}}
@keyframes rcCoin{0%{opacity:0;transform:translateY(-14px) rotate(-30deg) scale(.6)}60%{opacity:1;transform:translateY(3px) rotate(8deg) scale(1.05)}100%{opacity:1;transform:none}}
.rc-in{animation:obIn .6s ease both}.rc-in2{animation:obIn .6s ease .1s both}.rc-in3{animation:obIn .6s ease .2s both}.rc-in4{animation:obIn .6s ease .3s both}.rc-in5{animation:obIn .6s ease .4s both}
.rc-hang{transform-origin:50% -150px;animation:rcDrop 2.6s cubic-bezier(.33,.66,.4,1) .2s both}
.rc-sway{transform-origin:50% -150px;animation:rcSway 5.2s ease-in-out 2.8s infinite}
.rc-shine{position:absolute;top:0;left:0;width:40%;height:100%;background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.55),rgba(255,255,255,0));animation:rcShine 1.4s ease 1.2s both;pointer-events:none}
.rc-line{stroke-dasharray:1;animation:rcDraw 1.4s cubic-bezier(.4,0,.2,1) .2s both}
.rc-node{transform-box:fill-box;transform-origin:center;animation:rcPop .45s ease both}
.rc-tw{animation:rcTw 2.4s ease-in-out infinite}
.rc-coin{animation:rcCoin .8s cubic-bezier(.3,1.4,.5,1) 1s both}
.rc-btn{transition:background .2s ease,transform .2s ease}
.rc-btn:hover{background:#0E3BB8 !important;transform:translateY(-1px)}
.rc-btn .ob-arrow{transition:transform .3s cubic-bezier(.3,1.4,.5,1)}
.rc-btn:hover .ob-arrow{transform:translateX(4px)}
.rc-btn:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:3px}
@media (prefers-reduced-motion: reduce){.rc-in,.rc-in2,.rc-in3,.rc-in4,.rc-in5,.rc-hang,.rc-sway,.rc-shine,.rc-line,.rc-node,.rc-tw,.rc-coin{animation:none}.rc-shine{display:none}}
@media (max-height: 760px) and (min-width: 961px){.rc-h1{font-size:46px !important}.rc-stage{transform:scale(.88);transform-origin:center}.rc-hdr{height:72px !important}.rc-main{top:72px !important}}
@media (max-width: 1100px) and (min-width: 961px){.rc-stage{transform:scale(.86);transform-origin:center}}
@media (max-width: 960px){
.rc-root{height:auto !important;min-height:100vh !important;display:flex;flex-direction:column}
.rc-hdr{position:relative !important;height:60px !important;padding:0 20px !important;flex-shrink:0}
.rc-main{position:relative !important;top:0 !important;flex-grow:1;display:flex !important;flex-direction:column-reverse;justify-content:flex-end;gap:0 !important;padding:0 24px 24px 24px !important;max-width:none !important;width:100%}
.rc-stage{width:100% !important;height:auto !important;display:flex;justify-content:center;padding:0 !important;transform:none !important}
.rc-cardwrap{position:relative !important;left:auto !important;top:auto !important;width:min(280px,80%) !important;margin-top:52px}
.rc-mh,.rc-tw,.rc-in{display:none !important}
.rc-lan{top:-56px !important;height:62px !important}
.rc-hang,.rc-sway{transform-origin:50% -56px}
.rc-cardwrap article > div{padding:18px 20px 16px 20px !important}
.rc-cardwrap h2{font-size:21px !important;margin-top:12px !important}
.rc-av{width:60px !important;height:60px !important;font-size:20px !important}
.rc-av .rc-node{width:22px !important;height:22px !important;border-width:2px !important;right:-5px !important;bottom:-3px !important}
.rc-left{flex-grow:1;align-items:center !important;text-align:center;max-width:none !important;margin-top:36px}
.rc-h1{font-size:28px !important;margin-top:0 !important}
.rc-left p.rc-in3{font-size:15px !important;margin-top:10px !important;max-width:320px}
.rc-tok{margin:20px 0 32px 0 !important;width:auto !important;padding:6px 14px 6px 6px !important;gap:10px !important;border-radius:999px !important;box-shadow:none !important}
.rc-tokc svg{width:30px;height:30px}
.rc-tokt{font-size:14.5px !important}
.rc-toks{display:none !important}
.rc-btn{margin-top:auto !important;align-self:stretch !important;width:100% !important;height:54px !important;justify-content:space-between}
.rc-left p.rc-note{font-size:12px !important;margin-top:12px !important;max-width:320px}
}
'''
tags=''.join(f'<span style="height: 28px; padding: 0 11px; border-radius: 999px; background: #F5F8FF; border: 1px solid #E6EAF3; color: #3A4566; font-size: 12.5px; font-weight: 500; display: inline-flex; align-items: center">{t}</span>' for t in ['Data Analysis','SQL','Business Intelligence'])
LANYARD='''<span class="rc-lan" aria-hidden="true" style="position: absolute; left: 50%; top: -150px; width: 16px; height: 156px; transform: translateX(-50%); border-radius: 3px; background: linear-gradient(180deg, rgba(22, 82, 240, 0) 0%, #1652F0 38%, #0E3BB8 100%); box-shadow: inset 4px 0 0 rgba(255, 255, 255, 0.18)"></span><span aria-hidden="true" style="position: absolute; left: 50%; top: -12px; width: 30px; height: 24px; transform: translateX(-50%); border-radius: 8px; background: linear-gradient(180deg, #F3F5FA, #B9C2D6); box-shadow: 0 3px 6px rgba(11, 20, 51, 0.18), inset 0 1px 0 #FFFFFF; z-index: 2"><span style="position: absolute; left: 50%; top: 7px; width: 12px; height: 10px; transform: translateX(-50%); border-radius: 5px; border: 2px solid #8A93AD; box-sizing: border-box"></span></span>'''
CARD=f'''<div class="rc-cardwrap" style="position: absolute; left: 150px; top: 96px; width: 350px">
<div class="rc-hang"><div class="rc-sway" style="position: relative">{LANYARD}
<article aria-label="Your creator profile" style="position: relative; border-radius: 24px; background: #FFFFFF url({BG}) center top / 100% auto no-repeat; border: 1.5px solid #E6EAF3; box-shadow: 0 2px 4px rgba(11, 20, 51, 0.04), 0 30px 60px rgba(22, 82, 240, 0.16); overflow: hidden">
<div class="rc-shine" aria-hidden="true"></div><span aria-hidden="true" style="position: absolute; left: 50%; top: 9px; width: 40px; height: 7px; transform: translateX(-50%); border-radius: 4px; background: rgba(11, 20, 51, 0.16)"></span>
<div style="padding: 22px 24px 20px 24px">
<div style="display: flex; align-items: flex-start; justify-content: space-between">
<span class="rc-av" style="position: relative; width: 76px; height: 76px; border-radius: 50%; background: #0B1433; border: 4px solid #FFFFFF; box-sizing: border-box; box-shadow: 0 10px 24px rgba(11, 20, 51, 0.18); color: #FFFFFF; font-size: 24px; font-weight: 600; letter-spacing: 0.02em; display: flex; align-items: center; justify-content: center">AO<span class="rc-node" title="Creator" style="position: absolute; right: -6px; bottom: -4px; width: 28px; height: 28px; border-radius: 50%; background: #1652F0; border: 3px solid #FFFFFF; color: #FFFFFF; display: flex; align-items: center; justify-content: center; animation-delay: 1.1s"><svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l1.9 6.1L20 10l-6.1 1.9L12 18l-1.9-6.1L4 10l6.1-1.9z"></path></svg></span></span>
<span class="rc-mh" style="height: 28px; padding: 0 12px; border-radius: 999px; background: rgba(255, 255, 255, 0.85); color: #0E3BB8; font-size: 12.5px; font-weight: 500; display: inline-flex; align-items: center">Creator since today</span>
</div>
<h2 style="margin: 16px 0 0 0; font-size: 24px; font-weight: 600; letter-spacing: -0.02em; color: #0B1433">Ada Ononuju</h2>
<p style="margin: 4px 0 0 0; font-size: 14.5px; color: #4A5578">Data &amp; Analytics · 8+ years</p>
<p class="rc-mh" style="margin: 14px 0 0 0; font-size: 14.5px; line-height: 1.55; color: #0B1433">I help professionals turn messy data into decisions.</p>
<div class="rc-mh" style="margin-top: 14px; display: flex; flex-wrap: wrap; gap: 6px">{tags}</div>
<div style="margin-top: 18px; padding-top: 16px; border-top: 1px solid #E6EAF3; display: flex; align-items: center; gap: 12px">{NOVA_AV(38)}<span style="display: flex; flex-direction: column; gap: 1px; flex-grow: 1; min-width: 0"><span style="font-size: 14.5px; font-weight: 600; color: #0B1433">Nova</span><span style="font-size: 12.5px; color: #5B6582">Your Copilot · Collaborative</span></span><span style="display: inline-flex; align-items: center; gap: 6px; font-size: 12.5px; font-weight: 600; color: #0F6B45"><span style="width: 8px; height: 8px; border-radius: 50%; background: #0F6B45; box-shadow: 0 0 0 3px rgba(15, 107, 69, 0.15)"></span>Ready</span></div>
</div>
</article>

</div></div>
{STAR('-34px','120px',14,'#1652F0',0.2)}{STAR('360px','190px',12,'#F6C343',0.9)}{STAR('300px','-30px',10,'#1652F0',1.5)}{STAR('-12px','430px',10,'#F6C343',0.6)}
</div>'''
# journey line: 4 completed steps flowing into the card
PTS=[(14,546,'0.35'),(64,520,'0.55'),(108,470,'0.75'),(140,398,'0.95')]
nodes=''.join(f'<g class="rc-node" style="animation-delay: {d}s"><circle cx="{x}" cy="{y}" r="11" fill="#1652F0" stroke="#FFFFFF" stroke-width="3"></circle><path d="M{x-4.5} {y+0.5} l3 3 l6 -6" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"></path></g>' for x,y,d in PTS)
PATH=f'''<svg class="rc-path" aria-hidden="true" viewBox="0 0 520 580" style="position: absolute; left: 0; top: 0; width: 520px; height: 580px; overflow: visible"><path d="M14 546 Q 130 520 162 300" fill="none" stroke="#1652F0" stroke-opacity="0.16" stroke-width="14" stroke-linecap="round"></path><path class="rc-line" pathLength="1" d="M14 546 Q 130 520 162 300" fill="none" stroke="#1652F0" stroke-width="3" stroke-linecap="round"></path>{nodes}</svg>'''
STAGE=f'<div class="rc-stage" style="position: relative; width: 520px; height: 580px; justify-self: center">{CARD}</div>'
LEFT=f'''<section class="rc-left" style="display: flex; flex-direction: column; align-items: flex-start; max-width: 520px">
<span class="rc-in" style="height: 32px; padding: 0 14px 0 10px; border-radius: 999px; background: #E7F5EE; color: #0F6B45; font-size: 13.5px; font-weight: 600; display: inline-flex; align-items: center; gap: 8px"><span style="width: 18px; height: 18px; border-radius: 50%; background: #0F6B45; color: #FFFFFF; display: flex; align-items: center; justify-content: center">{ICON(I["check"],11,3.4)}</span>Setup complete</span>
<h1 class="rc-h1 rc-in2" style="margin: 18px 0 0 0; font-size: clamp(44px, 6.4vh, 60px); line-height: 1.06; font-weight: 600; letter-spacing: -0.04em; color: #0B1433">Ada, you’re a <span style="color: #1652F0">Creator</span>.</h1>
<p class="rc-in3" style="margin: 16px 0 0 0; font-size: 17px; line-height: 1.55; color: #4A5578">Your profile is ready and Nova is by your side. Let’s make something people will love learning from.</p>
<div class="rc-in4 rc-tok" style="margin-top: 24px; width: fit-content; max-width: 100%; box-sizing: border-box; display: flex; align-items: center; gap: 16px; padding: 14px 18px 14px 14px; border-radius: 20px; background: linear-gradient(135deg, #FFFAEB 0%, #FFF1CF 100%); border: 1.5px solid #F4D98E; box-shadow: 0 10px 28px rgba(214, 150, 30, 0.14)"><span class="rc-tokc" style="display: flex">{COIN('tk',52)}</span><span style="display: flex; flex-direction: column; gap: 3px; min-width: 0"><span style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap"><span class="rc-tokt" style="font-size: 19px; font-weight: 600; letter-spacing: -0.01em; color: #4A3300">20,000 AI Tokens</span><span style="height: 22px; padding: 0 9px; border-radius: 999px; background: #FFFFFF; border: 1px solid #F0CF73; color: #8A5A00; font-size: 12px; font-weight: 500; display: inline-flex; align-items: center">Starter gift</span></span><span class="rc-toks" style="font-size: 13.5px; line-height: 1.45; color: #6B4E16">Powers Nova’s help. Top up anytime.</span></span></div>
<a href="CR-DASH-NEW.dc.html" class="rc-btn rc-in5" style="margin-top: 26px; display: flex; align-items: center; gap: 16px; height: 58px; padding: 0 6px 0 28px; box-sizing: border-box; border-radius: 999px; background: #1652F0; color: #FFFFFF; font-size: 16.5px; font-weight: 600; text-decoration: none; white-space: nowrap; box-shadow: 0 1px 0 rgba(255, 255, 255, 0.25) inset, 0 14px 30px rgba(22, 82, 240, 0.30)"><span>Enter my Creator Studio</span><span class="ob-arrow" style="width: 46px; height: 46px; border-radius: 50%; background: #FFFFFF; color: #1652F0; display: flex; align-items: center; justify-content: center">{ICON(I["arrow"],18,2.4)}</span></a>
<p class="rc-in5 rc-note" style="margin: 16px 0 0 0; font-size: 13.5px; line-height: 1.5; color: #5B6582">Identity, credentials, a short orientation and policies come later, before validation. They never stop you building.</p>
</section>'''
body=f'''<div class="rc-root" style="width: 100%; height: 100vh; min-height: 640px; position: relative; overflow: hidden; background: #FFFFFF; font-family: 'Google Sans', 'Google Sans Text', 'Helvetica Neue', system-ui, sans-serif; color: #0B1433">
<div aria-hidden="true" style="position: absolute; right: -10%; top: 10%; width: 60%; height: 90%; background: radial-gradient(closest-side, rgba(22, 82, 240, 0.10), rgba(22, 82, 240, 0)); pointer-events: none"></div>
<header class="rc-hdr" style="position: absolute; left: 0; top: 0; width: 100%; height: 88px; box-sizing: border-box; padding: 0 clamp(24px, 6.67vw, 96px); display: flex; align-items: center; z-index: 3">{LOGO_ONB}</header>
<main class="rc-main" style="position: absolute; left: 0; right: 0; top: 88px; bottom: 0; box-sizing: border-box; max-width: 1280px; margin: 0 auto; padding: 0 clamp(24px, 6.67vw, 96px) 24px clamp(24px, 6.67vw, 96px); display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); align-items: center; gap: clamp(24px, 4vw, 64px); z-index: 2">
{LEFT}
{STAGE}
</main>
</div>'''
s=HEAD.replace('TITLE','Credalio · You’re a Creator').replace('CSS',RC_CSS)+body+TAIL.replace('SCRIPT','class Component extends DCLogic {\n  renderVals() { return {}; }\n}')
open(P+'CR-ONB-008.dc.html','w').write(s)
print('008 built')

# =============== DASH-NEW · launchpad (v3: one hero holds every way to start) ===============
NOVA_TXT='Tell me what you want people to come away with. One skill or subject usually means a Course. Proving competence against a standard is a Professional Certification. A route to a role is a Career Path. A group learning together over weeks is a Learning Program.'
FMTS=[('course','Course'),('cert','Professional Certification'),('path','Career Path'),('program','Learning Program')]
fmts=''.join(f'<a href="CR-CREATE-001.dc.html" class="dn-fmt"><span style="color: #1652F0; display: flex">{ICON(I[k],18,1.8)}</span>{t}</a>' for k,t in FMTS)
MS=[('Creator profile','Complete','done',None),('Identity','Not started','next','Verify'),('Credentials','Added · not verified','todo','Verify'),('Orientation','Not started','todo','Start'),('Policies','Not started','todo','Review')]
ms=''
for i,(l,st,kind,act) in enumerate(MS):
    if kind=='done': dot=f'<span class="dn-dot" style="background: #0F6B45; border-color: #0F6B45; color: #FFFFFF">{ICON(I["check"],13,3)}</span>'
    elif kind=='next': dot='<span class="dn-dot dn-next" style="background: #FFFFFF; border-color: #1652F0"><span style="width: 9px; height: 9px; border-radius: 50%; background: #1652F0"></span></span>'
    else: dot='<span class="dn-dot" style="background: #FFFFFF; border-color: #CBD3E6"></span>'
    a_=f'<a href="#" class="ds-link dn-act">{act}</a>' if act else '<span></span>'
    ms+=f'<li class="dn-ms">{dot}<span style="display: flex; flex-direction: column; min-width: 0"><span class="dn-msl">{l}</span><span class="dn-mss" style="color: {"#0F6B45" if kind=="done" else "#5B6582"}">{st}</span></span>{a_}</li>'
HERO_CHAR=f'<div class="dn-char" aria-hidden="true" style="position: absolute; right: 36px; bottom: -48px; width: 176px; aspect-ratio: 200 / 450; mix-blend-mode: multiply"><div style="position: absolute; inset: 0; overflow: hidden; -webkit-mask-image: linear-gradient(to bottom, #000 76%, transparent); mask-image: linear-gradient(to bottom, #000 76%, transparent)"><img src="{IMG}" alt="" style="position: absolute; left: -672.5%; top: -37.78%; width: 1086%; max-width: none; height: auto"></div></div>'
c=f'''<section class="dn-hero ob-in" aria-labelledby="dn-h" style="position: relative; overflow: hidden; margin-top: 8px; border-radius: 24px; border: 1.5px solid #E6EAF3; background: #FFFFFF url({BG}) center top / cover no-repeat; padding: 30px 36px 28px 36px">
{HERO_CHAR}
<div class="dn-in" style="position: relative; max-width: calc(100% - 210px)">
<p class="dn-wel" style="margin: 0; font-size: 15px; color: #3A4566">Welcome to your Studio, Ada.</p>
<h1 id="dn-h" class="ds-h1" style="margin-top: 4px; font-size: clamp(30px, 2.8vw, 40px)">What will you teach first?</h1>
<div class="dn-comp" style="margin-top: 18px; max-width: 720px; border-radius: 20px; background: #FFFFFF; border: 1.5px solid #D6DDEE; box-shadow: 0 14px 34px rgba(22, 82, 240, 0.10); padding: 14px 14px 12px 20px">
<label for="dn-idea" class="sr-only">Describe your idea</label>
<textarea id="dn-idea" rows="2" value="{{{{idea}}}}" onChange="{{{{onIdea}}}}" placeholder="Describe an idea. For example: SQL for analysts who’ve only used spreadsheets." style="display: block; width: 100%; box-sizing: border-box; border: 0; outline: none; resize: none; background: transparent; font-family: inherit; font-size: 16.5px; line-height: 1.5; color: #0B1433"></textarea>
<div class="dn-comp-foot" style="margin-top: 6px; display: flex; align-items: center; justify-content: space-between; gap: 12px">
<span class="dn-help" style="display: flex; align-items: center; gap: 8px; font-size: 13.5px; color: #5B6582">{NOVA_AV(26, False)}Nova turns it into a first draft you shape.</span>
{BTNA("CR-CREATE-002A.dc.html","Start with Nova")}
</div>
</div>
<div class="dn-ideas" style="margin-top: 12px; display: flex; align-items: center; gap: 8px"><span class="dn-lab">From your expertise</span><sc-for list="{{{{ideas}}}}" as="t" hint-placeholder-count="3"><button type="button" class="ds-chip dn-idea" onClick="{{{{t.pick}}}}">{{{{t.label}}}}</button></sc-for></div>
<div style="margin-top: 22px; padding-top: 18px; border-top: 1px solid rgba(203, 211, 230, 0.7)">
<div style="display: flex; align-items: center; justify-content: space-between; gap: 12px; max-width: 760px"><span class="dn-lab">Or start from a format</span><button type="button" class="ds-link dn-why" onClick="{{{{toggleAsk}}}}" aria-expanded="{{{{askOpen}}}}">Not sure which fits?</button></div>
<div class="dn-fmts" style="margin-top: 10px; display: flex; flex-wrap: wrap; align-items: center; gap: 8px">{fmts}</div>
<sc-if value="{{{{askShown}}}}" hint-placeholder-val="{{{{false}}}}"><div class="cp-pop" role="status" style="margin-top: 12px; display: flex; align-items: flex-start; gap: 10px">{NOVA_AV(30)}<p style="margin: 0; padding: 12px 14px; border-radius: 6px 16px 16px 16px; background: #FFFFFF; border: 1.5px solid #E6EAF3; font-size: 14.5px; line-height: 1.55; color: #0B1433">{NOVA_TXT}</p></div></sc-if>
</div>
</div>
</section>
<section class="ds-card ob-in2 dn-path" aria-labelledby="dn-p" style="margin-top: 18px; padding: 20px 24px 22px 24px">
<div class="dn-ph" style="display: flex; align-items: center; justify-content: space-between; gap: 12px"><div><h2 id="dn-p" style="margin: 0; font-size: 17px; font-weight: 600; letter-spacing: -0.01em">Your path to publishing</h2><p class="dn-psub" style="margin: 3px 0 0 0; font-size: 14px; color: #4A5578">Draft freely now. These five unlock validation and publishing.</p></div><span style="flex-shrink: 0; height: 28px; padding: 0 11px; border-radius: 999px; background: #F5F8FF; border: 1px solid #E6EAF3; font-size: 12.5px; font-weight: 500; color: #0E3BB8; display: inline-flex; align-items: center">1 of 5 done</span></div>
<ol class="dn-track" style="list-style: none; margin: 18px 0 0 0; padding: 0; position: relative; display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 12px"><span class="dn-rail" aria-hidden="true"><span style="display: block; width: 12%; height: 100%; background: #0F6B45; border-radius: 3px"></span></span>{ms}</ol>
</section>'''
DN_CSS='''.dn-comp:focus-within{border-color:#1652F0 !important;box-shadow:0 0 0 4px rgba(22,82,240,.12),0 14px 34px rgba(22,82,240,.10) !important}
.dn-comp textarea::placeholder{color:#8A93AD}
.dn-lab{font-size:13.5px;color:#4A5578;white-space:nowrap}
.dn-idea{height:34px !important;font-size:13.5px !important;padding:0 13px !important;background:rgba(255,255,255,.92) !important;white-space:nowrap;flex-shrink:0}
.dn-fmt{display:inline-flex;align-items:center;gap:8px;height:42px;padding:0 16px 0 13px;box-sizing:border-box;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;font-size:14.5px;font-weight:500;text-decoration:none;white-space:nowrap;transition:border-color .2s ease,background .2s ease,transform .2s ease}
.dn-fmt:hover{border-color:#1652F0;background:#F5F8FF;transform:translateY(-1px)}
.dn-fmt:focus-visible,.dn-why:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:2px}
.dn-why{border:0;background:none;padding:0;height:32px;cursor:pointer;font-family:inherit;font-size:13.5px}
.dn-ms{position:relative;display:flex;flex-direction:column;gap:9px;z-index:1}
.dn-msl{font-size:14.5px;font-weight:600;color:#0B1433}
.dn-mss{font-size:13px;margin-top:2px}
.dn-act{font-size:13.5px}
.dn-dot{width:28px;height:28px;box-sizing:border-box;border-radius:50%;border:2px solid;display:flex;align-items:center;justify-content:center;flex-shrink:0}
@keyframes dnPulse{0%{box-shadow:0 0 0 0 rgba(22,82,240,.35)}100%{box-shadow:0 0 0 9px rgba(22,82,240,0)}}
.dn-next{animation:dnPulse 2s ease-out infinite}
.dn-rail{position:absolute;left:14px;right:calc(20% - 14px);top:12px;height:4px;border-radius:3px;background:#E6EAF3;z-index:0;display:block}
@media (max-width: 1180px){.dn-char{display:none}.dn-in{max-width:none !important}}
@media (max-width: 960px){
.dn-hero{padding:18px 16px 16px 16px !important;border-radius:20px !important;margin-top:4px !important}
.dn-wel{font-size:13.5px !important}
.dn-hero .ds-h1{font-size:24px !important}
.dn-comp{margin-top:14px !important;padding:12px 12px 12px 14px !important;border-radius:16px !important}
.dn-comp textarea{font-size:15px !important;min-height:66px}
.dn-help{display:none !important}
.dn-comp-foot .ds-btn{flex-grow:1;justify-content:space-between}
.dn-ideas{overflow-x:auto;margin-left:-16px !important;margin-right:-16px;padding:0 16px;scrollbar-width:none}
.dn-ideas::-webkit-scrollbar{display:none}
.dn-ideas .dn-lab{display:none}
.dn-hero > .dn-in > div:last-child{margin-top:16px !important;padding-top:14px !important}
.dn-fmts{display:grid !important;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px !important}
.dn-fmt{height:44px;font-size:13.5px;padding:0 10px;gap:7px;white-space:normal;line-height:1.2;border-radius:14px}

.dn-path{padding:16px !important;margin-top:14px !important}
.dn-psub{display:none}
.dn-track{grid-template-columns:minmax(0,1fr) !important;gap:0 !important;margin-top:10px !important}
.dn-ms{display:grid !important;grid-template-columns:28px minmax(0,1fr) auto;align-items:center;gap:12px !important;padding:9px 0}
.dn-msl{font-size:14px}
.dn-mss{font-size:12.5px;margin-top:1px}
.dn-rail{left:12px !important;right:auto !important;top:22px !important;bottom:22px;width:4px !important;height:auto !important}
.dn-rail > span{width:100% !important;height:8% !important}
}
'''
S_DN='''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { nav: false, ask: false, idea: '' }; }
  renderVals() {
    const ideas = ['SQL for business analysis', 'Dashboards managers use', 'Data cleaning basics'];
    return { NAVJS,
      idea: this.state.idea, onIdea: (e) => this.setState({ idea: e.target.value }),
      ideas: ideas.map((label) => ({ label, pick: () => this.setState({ idea: label }) })),
      askShown: this.state.ask, askOpen: this.state.ask ? 'true' : 'false', toggleAsk: () => this.setState({ ask: !this.state.ask }) };
  }
}'''.replace('NAVJS',NAV_JS)
open(P+'CR-DASH-NEW.dc.html','w').write(SHELL('Dashboard',c,'Credalio · Creator Studio',S_DN,DN_CSS,1000))
print('DASH-NEW built')

# =============== CREATE-001 · choose how ===============
mini_lines=''.join(f'<span class="c1-l" style="display: block; height: 7px; border-radius: 4px; background: {c}; width: {w}; margin-top: 9px; animation-delay: {d}s"></span>' for c,w,d in [('#C9D6FA','86%',1.0),('#C9D6FA','70%',1.25),('#C9D6FA','78%',1.5),('#C9D6FA','56%',1.75)])
PREV_NOVA=f'''<div class="c1-prev" aria-hidden="true" style="background: #FFFFFF url({BG}) center top / cover no-repeat">
<div class="c1-chat" style="display: flex; flex-direction: column; gap: 8px; width: 46%">
<span class="c1-b" style="display: flex; align-items: flex-end; gap: 6px; animation-delay: .2s">{NOVA_AV(22, False)}<span style="padding: 7px 10px; border-radius: 12px 12px 12px 4px; background: #FFFFFF; border: 1px solid #E6EAF3; font-size: 11.5px; line-height: 1.35; color: #0B1433">Who is it for?</span></span>
<span class="c1-b" style="align-self: flex-end; padding: 7px 10px; border-radius: 12px 12px 4px 12px; background: #0B1433; font-size: 11.5px; line-height: 1.35; color: #FFFFFF; animation-delay: .5s">Career switchers</span>
<span class="c1-b c1-b3" style="display: flex; align-items: flex-end; gap: 6px; animation-delay: .8s">{NOVA_AV(22, False)}<span style="padding: 7px 10px; border-radius: 12px 12px 12px 4px; background: #FFFFFF; border: 1px solid #E6EAF3; font-size: 11.5px; line-height: 1.35; color: #0B1433">Drafting your course…</span></span>
</div>
<span style="color: #1652F0; display: flex; flex-shrink: 0">{ICON(I["arrow"],18,2.2)}</span>
<div class="c1-doc" style="width: 40%; padding: 14px; box-sizing: border-box; border-radius: 12px; background: #FFFFFF; border: 1px solid #E6EAF3; box-shadow: 0 10px 24px rgba(22, 82, 240, 0.12)"><span style="display: block; height: 9px; width: 64%; border-radius: 5px; background: #1652F0"></span>{mini_lines}<span style="display: flex; gap: 5px; margin-top: 12px"><span style="height: 16px; width: 34%; border-radius: 8px; background: #EAF0FF"></span><span style="height: 16px; width: 26%; border-radius: 8px; background: #EAF0FF"></span></span></div>
</div>'''
slots=''.join(f'<span style="display: flex; align-items: center; gap: 8px; height: 30px; padding: 0 10px; margin-top: 8px; border-radius: 9px; border: 1.5px dashed #CBD3E6; font-size: 11.5px; color: #8A93AD">{t}</span>' for t in ['+ Add a learning outcome','+ Add a module','+ Add an assessment'])
PREV_SCR=f'''<div class="c1-prev c1-prev-s" aria-hidden="true" style="background: #F7F9FD; justify-content: center">
<div style="width: 70%; padding: 16px; box-sizing: border-box; border-radius: 12px; background: #FFFFFF; border: 1px solid #E6EAF3"><span style="display: flex; align-items: center; gap: 2px; font-size: 14px; font-weight: 600; color: #8A93AD">Untitled course<span class="c1-caret"></span></span>{slots}</div>
</div>'''
def MODE(card_cls, prev, title, text, meta, cta, extra=''):
    m=''.join(f'<span style="display: inline-flex; align-items: center; gap: 6px; font-size: 13.5px; color: #3A4566"><span style="color: #1652F0; display: flex">{ICON(I["check"],14,2.8)}</span>{x}</span>' for x in meta)
    return f'''<article class="ds-card c1-card {card_cls}" style="padding: 14px; display: flex; flex-direction: column; {extra}">{prev}<div style="padding: 20px 12px 12px 12px; display: flex; flex-direction: column; flex-grow: 1"><h2 style="margin: 0; font-size: 22px; font-weight: 600; letter-spacing: -0.02em">{title}</h2><p style="margin: 8px 0 0 0; font-size: 15px; line-height: 1.55; color: #3A4566">{text}</p><div class="c1-meta" style="margin-top: 14px; display: flex; flex-wrap: wrap; gap: 8px 18px">{m}</div><span style="flex-grow: 1; min-height: 20px"></span>{cta}</div></article>'''
c=f'''<a href="CR-DASH-NEW.dc.html" class="ds-back ob-in" style="margin-top: 4px">{ICON(I["back"],16,2.2)}Studio</a>
<div class="c1-wrap" style="max-width: 1000px; margin: 0 auto">
<div class="ob-in" style="margin-top: 6px; display: flex; flex-direction: column; align-items: center; text-align: center">
<span style="display: inline-flex; align-items: center; gap: 8px; height: 34px; padding: 0 6px 0 10px; border-radius: 999px; background: #FFFFFF; border: 1.5px solid #E6EAF3; font-size: 13.5px; font-weight: 500; color: #0B1433"><span style="color: #1652F0; display: flex">{ICON(I["course"],17,1.8)}</span>Course<a href="CR-DASH-NEW.dc.html" style="height: 24px; padding: 0 10px; border-radius: 999px; background: #F5F8FF; color: #1652F0; font-size: 12.5px; font-weight: 500; text-decoration: none; display: inline-flex; align-items: center">Change</a></span>
<h1 class="ds-h1" style="margin-top: 14px">How would you like to build it?</h1>
<p class="ds-sub">Either way, everything stays editable until you publish.</p>
</div>
<div class="c1-grid ob-in2" style="margin-top: 28px; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 20px">
{MODE('c1-rec',PREV_NOVA,'Build it with Nova','Answer five short questions. Nova sketches a first draft, and you decide what stays.',['5 questions','You approve every part'],BTNA("CR-CREATE-002A.dc.html","Start with Nova",extra='style="align-self: flex-start"'),'border-color: #1652F0; box-shadow: 0 0 0 4px rgba(22, 82, 240, 0.10), 0 18px 40px rgba(22, 82, 240, 0.10)')}
{MODE('',PREV_SCR,'Start from a blank page','Set up every part yourself, step by step. Nova is one click away whenever you want a hand.',['Full control','Help on every screen'],'<a href="#" class="ds-ghost" style="align-self: flex-start">Start from scratch</a>')}
</div>
</div>'''
C1_CSS='''.c1-prev{position:relative;height:200px;border-radius:14px;overflow:hidden;display:flex;align-items:center;justify-content:space-between;gap:10px;padding:18px;box-sizing:border-box}
@keyframes c1B{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
@keyframes c1L{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes c1Blink{0%,49%{opacity:1}50%,100%{opacity:0}}
.c1-b{animation:c1B .45s ease both}
.c1-l{transform-origin:left;animation:c1L .5s ease both}
.c1-caret{display:inline-block;width:2px;height:16px;background:#1652F0;margin-left:2px;animation:c1Blink 1s steps(1) infinite}
.c1-card{transition:transform .25s ease,box-shadow .25s ease}
.c1-card:hover{transform:translateY(-2px)}
@media (prefers-reduced-motion: reduce){.c1-b,.c1-l,.c1-caret{animation:none}}
@media (max-width: 860px){.c1-grid{grid-template-columns:minmax(0,1fr) !important;gap:12px !important;margin-top:18px !important}.c1-card{padding:10px !important}.c1-card > div{padding:14px 8px 8px 8px !important}.c1-card h2{font-size:19px !important}.c1-card p{font-size:14.5px !important;margin-top:6px !important}.c1-card .ds-btn,.c1-card .ds-ghost{align-self:stretch !important}.c1-card .ds-btn{justify-content:space-between}.c1-prev{height:128px;padding:16px 14px;gap:12px}.c1-b3{display:none !important}.c1-chat{width:auto !important;flex:1 1 auto;gap:12px !important}.c1-doc{width:96px !important;flex-shrink:0;padding:12px !important}.c1-doc .c1-l{margin-top:7px !important}.c1-doc > span:last-child{display:none !important}.c1-wrap .ds-h1{text-wrap:balance}.c1-prev-s,.c1-meta{display:none !important}.c1-wrap .ds-h1{font-size:22px !important}.c1-card > div > span[style*="flex-grow"]{min-height:14px !important}}
'''
S_C1='class Component extends DCLogic {\n  constructor(props) { super(props); this.state = { nav: false }; }\n  renderVals() { return { NAVJS }; }\n}'.replace('NAVJS',NAV_JS)
open(P+'CR-CREATE-001.dc.html','w').write(SHELL('Create new',c,'Credalio · How would you like to build it?',S_C1,C1_CSS,820))
print('CREATE-001 built')
exec(open('build8b.py').read())
# ---------- preview wrappers (v2 sizes)
WRAP('CR-CREATE-002Ab.dc.html','CR-CREATE-002A',1440,1720,'Credalio · Review your course',' variant="proposal"')
WRAP('CR-CREATE-002Ab-Mobile.dc.html','CR-CREATE-002A',390,2130,'Credalio · Review your course (mobile)',' variant="proposal"')
for n,h in [('CR-DASH-NEW',980),('CR-CREATE-001',844),('CR-CREATE-002A',844)]:
    WRAP(n+'-Mobile.dc.html',n,390,h,n+' mobile preview')
WRAP('CR-ONB-008-Mobile.dc.html','CR-ONB-008',390,844,'CR-ONB-008 mobile preview')
s=open(P+'CR-ONB-008-Mobile.dc.html').read().replace('background: #F7F9FD','background: #FFFFFF'); open(P+'CR-ONB-008-Mobile.dc.html','w').write(s)
print('wrappers v2')
