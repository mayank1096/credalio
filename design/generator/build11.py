# Batch 11 · Orientation learning player (focus mode): CR-ORI-002 module, 003 lesson, 004 check, 005 scenario, 006 module complete
exec(open('build10.py').read().split('# =====================================================================\n# CR-RDY-001')[0])
CHECK_I='<path d="m5 12.5 4.5 4.5L19 7.5"></path>'
Q_I='<circle cx="12" cy="12" r="9"></circle><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6v.6M12 17h.01"></path>'
SCEN_I='<path d="M12 3 21 12 12 21 3 12z"></path>'
LES_I='<circle cx="12" cy="12" r="4"></circle>'
KIND={'lesson':('Lesson',LES_I),'check':('Check',Q_I),'scen':('Scenario',SCEN_I)}

DEF_S='class Component extends DCLogic {\n  renderVals() { return {}; }\n}'
def PLAYER(fname, title, modlabel, steps, cur, content, prev=None, nxt=None, script=None, outline=True, extra_css='', bottom=True, nxt_hole=None):
    # steps: [(label, kind, state)] state: done|cur|todo
    segs=''.join(f'<span class="lp-seg lp-seg-{s}"></span>' for (_,_,s) in steps)
    ol=''
    for i,(l,k,s) in enumerate(steps):
        mk = ic('check',11,3.2) if s=='done' else ''
        ol+=f'<li class="lp-o lp-o-{s}"><span class="lp-om">{mk}</span><span class="lp-ot"><b>{l}</b><span>{KIND[k][0]}</span></span></li>'
    rail=f'''<aside class="lp-rail" aria-label="Module steps"><span class="lp-rl">{modlabel}</span><ol class="lp-ol">{ol}</ol></aside>''' if outline else ''
    stepn = f'Step {cur+1} of {len(steps)}' if cur is not None else f'{len(steps)} steps'
    navb=''
    if bottom:
        pv = f'<a href="{prev[1]}" class="lp-prev">{ic("back",16,2.2)}<span class="lp-hide-sm">{prev[0]}</span></a>' if prev else '<span class="lp-prev lp-dis">'+ic("back",16,2.2)+'<span class="lp-hide-sm">Previous</span></span>'
        nx = nxt_hole if nxt_hole else f'<a href="{nxt[1]}" class="ds-btn lp-next"><span>{nxt[0]}</span><span class="ob-arrow">{ic("arrow",18,2.4)}</span></a>'
        navb=f'<footer class="lp-bar"><div class="lp-barin">{pv}<span class="lp-stepn">{stepn}</span>{nx}</div></footer>'
    html=f'''<div class="lp-root">
<header class="lp-top">
<a href="CR-ORI-001.dc.html" class="lp-x" aria-label="Close and go back to Orientation">{ic('close',18,2.2)}</a>
<div class="lp-title"><span class="lp-t1">Creator Orientation</span><span class="lp-t2">{modlabel}</span></div>
<div class="lp-segs" aria-hidden="true">{segs}</div>
<span class="lp-tn">{stepn}</span>
</header>
<div class="lp-body{' lp-has-rail' if outline else ''}">
{rail}
<main class="lp-main{' lp-wide' if not outline else ''}">{content}</main>
</div>
{navb}
</div>'''
    open(P+fname,'w').write(f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">
<style>
{DASH_CSS}{COMMON_CSS}{LP_CSS}{extra_css}</style>
</helmet>
{html}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1440,"height":820}}}}'>
{script or DEF_S}
</script>
</body>
</html>
''')

LP_CSS='''body{background:#FFFFFF}
.lp-root{min-height:100vh;display:flex;flex-direction:column;background:#FFFFFF;font-family:'Google Sans','Google Sans Text','Helvetica Neue',system-ui,sans-serif;color:#0B1433}
.lp-top{position:sticky;top:0;z-index:5;height:64px;flex-shrink:0;box-sizing:border-box;display:flex;align-items:center;gap:16px;padding:0 20px;border-bottom:1.5px solid #EEF1F7;background:rgba(255,255,255,.94);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}
.lp-x{width:40px;height:40px;flex-shrink:0;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#3A4566;text-decoration:none}
.lp-x:hover{background:#F5F8FF;color:#0B1433}
.lp-title{display:flex;align-items:baseline;gap:8px;min-width:0}
.lp-t1{font-size:16px;font-weight:600;white-space:nowrap}
.lp-t2{font-size:14px;color:#5B6582;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lp-segs{display:flex;gap:4px;margin-left:auto}
.lp-seg{width:34px;height:4px;border-radius:4px;background:#E6EAF3}
.lp-seg-done{background:#1652F0}
.lp-seg-cur{background:linear-gradient(90deg,#1652F0 50%,#E6EAF3 50%)}
.lp-tn{font-size:13px;color:#5B6582;white-space:nowrap;min-width:84px;text-align:right}
.lp-body{flex-grow:1;display:flex;justify-content:center;gap:56px;padding:40px 32px 120px 32px}
.lp-rail{width:240px;flex-shrink:0;position:sticky;top:104px;align-self:flex-start}
.lp-rl{display:block;font-size:13px;font-weight:600;color:#5B6582;margin:0 0 12px 2px}
.lp-ol{list-style:none;margin:0;padding:0;position:relative}
.lp-ol::before{content:'';position:absolute;left:11px;top:16px;bottom:16px;width:2px;background:#E6EAF3}
.lp-o{position:relative;display:flex;align-items:center;gap:12px;min-height:52px}
.lp-om{position:relative;z-index:1;width:24px;height:24px;flex-shrink:0;box-sizing:border-box;border-radius:50%;border:2px solid #D6DDEE;background:#FFFFFF;display:flex;align-items:center;justify-content:center;color:#FFFFFF}
.lp-o-done .lp-om{background:#1652F0;border-color:#1652F0}
.lp-o-cur .lp-om{border:7px solid #1652F0}
.lp-ot{display:flex;flex-direction:column;gap:1px;min-width:0}
.lp-ot b{font-size:14px;font-weight:500;color:#3A4566}
.lp-ot span{font-size:12px;color:#8A93AD}
.lp-o-cur .lp-ot b{font-weight:600;color:#0B1433}
.lp-main{width:min(720px,100%);min-width:0}
.lp-wide{width:min(1100px,100%)}
.lp-body:has(.lp-wide){align-items:center;padding-bottom:64px}
.lp-eb{display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:500;color:#1652F0}
.lp-h1{margin:10px 0 0 0;font-size:clamp(30px,4.6vh,40px);line-height:1.12;font-weight:600;letter-spacing:-0.03em}
.lp-meta{margin:10px 0 0 0;font-size:14px;color:#5B6582}
.lp-p{margin:22px 0 0 0;font-size:17.5px;line-height:1.7;color:#1F2A4D}
.lp-bar{position:fixed;left:0;right:0;bottom:0;z-index:5;background:rgba(255,255,255,.94);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-top:1.5px solid #EEF1F7}
.lp-barin{max-width:1100px;margin:0 auto;height:76px;box-sizing:border-box;padding:0 24px;display:flex;align-items:center;justify-content:space-between;gap:16px}
.lp-prev{display:inline-flex;align-items:center;gap:8px;height:48px;padding:0 18px 0 14px;box-sizing:border-box;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;font-size:14.5px;font-weight:600;text-decoration:none;white-space:nowrap;max-width:300px;overflow:hidden;text-overflow:ellipsis}
.lp-prev:hover{border-color:#1652F0;background:#F5F8FF;color:#0B1433}
.lp-dis{opacity:.45;pointer-events:none}
.lp-stepn{font-size:13.5px;color:#5B6582}
.lp-next.lp-off{background:#C9D3EC;box-shadow:none;pointer-events:none}
.lp-next.lp-off .ob-arrow{color:#9AA8CC}
.lp-ask{margin-top:28px;display:inline-flex;align-items:center;gap:10px;height:44px;padding:0 16px 0 6px;border-radius:999px;border:1.5px solid #E6EAF3;background:#FFFFFF;color:#3A4566;font-size:14px;font-weight:500;text-decoration:none}
.lp-ask:hover{border-color:#AFC1F5;color:#0B1433}
.lp-call{margin-top:24px;padding:16px 18px;border-radius:16px;background:#F5F8FF;border:1.5px solid #E6EAF3;border-left:4px solid #1652F0}
.lp-call b{display:block;font-size:12.5px;font-weight:600;color:#1652F0;margin-bottom:4px}
.lp-call span{font-size:15.5px;line-height:1.6;color:#0B1433}
@media (max-width: 1100px){.lp-rail{display:none}.lp-body{gap:0}}
@media (max-width: 960px){
.lp-top{height:56px;padding:0 12px 0 6px;gap:8px;flex-wrap:wrap}
.lp-t1{display:none}
.lp-t2{font-size:14.5px;font-weight:600;color:#0B1433}
.lp-segs{position:absolute;left:16px;right:16px;bottom:-1px;margin:0;gap:3px}
.lp-seg{flex:1 1 0;width:auto;height:3px}
.lp-tn{display:none}
.lp-body{padding:28px 16px 112px 16px}
.lp-h1{font-size:25px}
.lp-meta{font-size:13px;margin-top:6px}
.lp-p{font-size:16px;line-height:1.65;margin-top:16px}
.lp-barin{height:72px;padding:0 16px;gap:10px}
.lp-hide-sm,.lp-stepn{display:none}
.lp-prev{width:48px;padding:0;justify-content:center;flex-shrink:0}
.lp-next{flex:1 1 auto;min-width:0;justify-content:space-between}
.lp-next > span:first-child{overflow:hidden;text-overflow:ellipsis}
.lp-call span{font-size:15px}
}
'''

M4=[('What validators look at','lesson'),('The validation case','lesson'),('Tiers and revalidation','lesson'),('Quick knowledge check','check')]
M5=[('Using your Copilot well','lesson'),('Review, disclose, own','lesson'),('Quick knowledge check','check'),('Scenario exercise','scen')]
def st(lst, cur): return [(l,k,'done' if i<cur else ('cur' if i==cur else 'todo')) for i,(l,k) in enumerate(lst)]

# ---------------- CR-ORI-002 · Module overview (Module 4) ----------------
rows=''
for i,(l,k) in enumerate(M4):
    s='done' if i==0 else ('next' if i==1 else 'todo')
    mark = ic('check',13,3) if s=='done' else ik(KIND[k][1],15,2)
    tag = '<span class="mo-up">Up next</span>' if s=='next' else ''
    rows+=f'<li class="mo-r mo-{s}"><span class="mo-m">{mark}</span><span class="mo-t"><b>{l}</b><span>{KIND[k][0]}{" · done" if s=="done" else ""}</span></span>{tag}</li>'
learn=''.join(f'<li>{ic("check",14,2.6)}<span>{t}</span></li>' for t in ['Validators are independent and criteria-based','One learning experience has one validation case','Material changes may need revalidation'])
c=f'''<div class="mo-grid">
<section class="mo-left">
<span class="lp-eb ob-in">Module 4 of 7</span>
<h1 class="lp-h1 ob-in">Understanding validation</h1>
<p class="mo-desc ob-in2">What validators look at, how a case runs, and what tiers mean.</p>
<div class="mo-facts ob-in2"><span>{ik(CLOCK_I,15,2.2)}About 12 minutes</span><span>{ik(LES_I,15,2.2)}3 lessons</span><span>{ik(Q_I,15,2.2)}Quick check</span></div>
<div class="mo-learn ob-in3"><span class="sec-h">You’ll come away knowing</span><ul>{learn}</ul></div>
</section>
<section class="ds-card mo-card ob-in2" aria-label="Steps in this module">
<div class="mo-ch"><span class="sec-h">Your progress</span><span class="mo-pc">1 of 4 steps</span></div>
<span class="mo-bar"><span style="width: 25%"></span></span>
<ol class="mo-list">{rows}</ol>
<a href="CR-ORI-003.dc.html" class="ds-btn mo-go"><span>Continue module</span><span class="ob-arrow">{ic('arrow',18,2.4)}</span></a>
</section>
</div>'''
MO_CSS='''.mo-grid{display:grid;grid-template-columns:minmax(0,1fr) 400px;gap:56px;align-items:start;padding-top:clamp(0px,4vh,40px)}
.lp-body:has(.mo-grid){padding-bottom:64px}
.mo-grid{width:min(1100px,100%)}
.mo-desc{margin:14px 0 0 0;font-size:18px;line-height:1.6;color:#3A4566;max-width:520px}
.mo-facts{margin-top:20px;display:flex;flex-wrap:wrap;gap:8px}
.mo-facts span{display:inline-flex;align-items:center;gap:7px;height:34px;padding:0 13px;border-radius:999px;background:#F5F8FF;color:#3A4566;font-size:13.5px;font-weight:500}
.mo-facts svg{color:#1652F0}
.mo-learn{margin-top:32px;padding-top:24px;border-top:1.5px solid #F0F2F8}
.mo-learn ul{list-style:none;margin:12px 0 0 0;padding:0;display:flex;flex-direction:column;gap:10px}
.mo-learn li{display:flex;align-items:flex-start;gap:10px;font-size:15.5px;line-height:1.5;color:#0B1433}
.mo-learn li svg{color:#0F6B45;margin-top:3px;flex-shrink:0}
.mo-card{padding:22px 22px 22px 22px;border-radius:22px;box-shadow:0 18px 44px rgba(22,82,240,.08)}
.mo-ch{display:flex;align-items:baseline;justify-content:space-between}
.mo-pc{font-size:13px;color:#5B6582}
.mo-bar{display:block;margin-top:10px;height:6px;border-radius:6px;background:#E6EAF3;overflow:hidden}
.mo-bar span{display:block;height:100%;border-radius:6px;background:#1652F0}
.mo-list{list-style:none;margin:16px 0 0 0;padding:0;position:relative}
.mo-list::before{content:'';position:absolute;left:17px;top:24px;bottom:24px;width:2px;background:linear-gradient(180deg,#1652F0 0%,#1652F0 30%,#E6EAF3 30%)}
.mo-r{position:relative;display:flex;align-items:center;gap:14px;min-height:60px}
.mo-m{position:relative;z-index:1;width:36px;height:36px;flex-shrink:0;box-sizing:border-box;border-radius:50%;border:2px solid #D6DDEE;background:#FFFFFF;color:#8A93AD;display:flex;align-items:center;justify-content:center}
.mo-done .mo-m{background:#1652F0;border-color:#1652F0;color:#FFFFFF}
.mo-next .mo-m{border-color:#1652F0;color:#1652F0;animation:ndPulse 2s ease-out infinite}
.mo-t{display:flex;flex-direction:column;gap:2px;min-width:0;flex-grow:1}
.mo-t b{font-size:15px;font-weight:600}
.mo-t span{font-size:12.5px;color:#5B6582}
.mo-done .mo-t b{color:#3A4566;font-weight:500}
.mo-up{font-size:12px;font-weight:500;color:#1652F0;background:#EAF0FF;border-radius:999px;padding:4px 10px;white-space:nowrap}
.mo-go{margin-top:18px;width:100%;justify-content:space-between}
@media (max-width: 960px){
.mo-grid{display:flex;flex-direction:column;align-items:stretch;gap:0;padding-top:0}
.mo-card{margin-top:20px}
.mo-desc{font-size:15.5px;margin-top:10px}
.mo-facts{margin-top:14px;flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;margin-left:-16px;margin-right:-16px;padding:0 16px}
.mo-facts span{flex-shrink:0;height:32px;font-size:13px}
.mo-learn{margin-top:22px;padding-top:0;border-top:0;order:2}
.mo-learn li{font-size:14.5px}
.mo-card{padding:16px;border-radius:18px}
.mo-r{min-height:52px}
.mo-m{width:32px;height:32px}
.mo-list::before{left:15px}
.mo-t b{font-size:14.5px}
.mo-left{display:contents}
}
'''
PLAYER('CR-ORI-002.dc.html','Credalio · Orientation module','Module 4 · Understanding validation',st(M4,1),None,c,outline=False,bottom=False,extra_css=MO_CSS)

# ---------------- CR-ORI-003 · Lesson (Module 4, lesson 2) ----------------
REQ=[('Clarification','A question about your work'),('Evidence','Proof behind a claim'),('Meeting','A short call to talk it through'),('Findings','Issues to fix before a decision')]
req=''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a,b in REQ)
c=f'''<span class="lp-eb ob-in">Lesson 2 of 3 · about 4 min read</span>
<h1 class="lp-h1 ob-in">The validation case</h1>
<p class="lp-p ob-in2">One learning experience has one validation case. Validators may ask for clarification or evidence, propose a meeting, or raise findings. All of it happens in the Validation Workspace.</p>
<figure class="vc ob-in3" aria-label="How a validation case works">
<div class="vc-flow">
<div class="vc-n"><span class="vc-i">{ic('course',20,1.9)}</span><b>Your course</b><span>One learning experience</span></div>
<span class="vc-l" aria-hidden="true"></span>
<div class="vc-n vc-hub"><span class="vc-i">{ic('valid',20,1.9)}</span><b>One validation case</b><span>Reviewed by independent experts</span></div>
</div>
<div class="vc-ws"><span class="vc-wl">{ik(DOC_I,15,2)}Validation Workspace · everything lands here</span><ul class="vc-req">{req}</ul></div>
</figure>
<div class="lp-call ob-in3"><b>With several creators</b><span>If a request is about a chapter Mary wrote, it goes to Mary. The Lead Creator can see it too.</span></div>
<a href="#" class="lp-ask ob-in4">{NOVA_AV(30,False)}Ask Nova about this lesson</a>'''
VC_CSS='''.vc{margin:28px 0 0 0;padding:22px;border-radius:22px;background:#F7F9FD;border:1.5px solid #E6EAF3}
.vc-flow{display:flex;align-items:stretch}
.vc-n{flex:1 1 0;display:flex;flex-direction:column;gap:3px;padding:16px;border-radius:16px;background:#FFFFFF;border:1.5px solid #E6EAF3}
.vc-i{width:40px;height:40px;border-radius:12px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center;margin-bottom:8px}
.vc-n b{font-size:15.5px;font-weight:600}
.vc-n span:last-child{font-size:13.5px;color:#5B6582}
.vc-hub{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.08)}
.vc-hub .vc-i{background:#1652F0;color:#FFFFFF}
.vc-l{flex:0 0 48px;align-self:center;height:3px;border-radius:3px;background:#1652F0;position:relative}
.vc-l::after{content:'';position:absolute;right:-1px;top:-4px;border:5.5px solid transparent;border-left:7px solid #1652F0;border-right:0}
.vc-ws{margin-top:16px;padding-top:16px;border-top:1.5px dashed #CBD3E6}
.vc-wl{display:inline-flex;align-items:center;gap:7px;font-size:13px;font-weight:500;color:#1652F0}
.vc-req{list-style:none;margin:12px 0 0 0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px}
.vc-req li{display:flex;flex-direction:column;gap:2px;padding:12px;border-radius:14px;background:#FFFFFF;border:1.5px solid #E6EAF3}
.vc-req b{font-size:14px;font-weight:600}
.vc-req span{font-size:12.5px;line-height:1.4;color:#5B6582}
@media (max-width: 960px){
.vc{padding:14px;border-radius:18px;margin-top:20px}
.vc-flow{flex-direction:column}
.vc-l{flex:0 0 22px;width:3px;height:auto;align-self:flex-start;margin-left:34px}
.vc-l::after{right:-4px;top:auto;bottom:-1px;border:5.5px solid transparent;border-top:7px solid #1652F0;border-bottom:0}
.vc-n{flex-direction:row;flex-wrap:wrap;align-items:center;column-gap:12px;padding:12px}
.vc-i{margin:0;width:36px;height:36px}
.vc-n b{font-size:14.5px;flex:1 1 60%}
.vc-n span:last-child{flex-basis:100%;padding-left:48px;margin-top:-6px}
.vc-req{grid-template-columns:repeat(2,minmax(0,1fr))}
}
'''
PLAYER('CR-ORI-003.dc.html','Credalio · Orientation lesson','Module 4 · Understanding validation',st(M4,1),1,c,prev=('What validators look at','CR-ORI-002.dc.html'),nxt=('Next: Tiers and revalidation','CR-ORI-004.dc.html'),extra_css=VC_CSS)

# ---------------- CR-ORI-004 · Quick knowledge check (Module 4) ----------------
c='''<span class="lp-eb ob-in">Quick knowledge check</span>
<h1 class="lp-h1 ob-in">Two quick questions</h1>
<p class="lp-meta ob-in2">Not an exam. You’ll see why straight away, and you can try again as often as you like.</p>
<sc-for list="{{qs}}" as="q" hint-placeholder-count="2"><section class="kc ob-in3" aria-label="{{q.n}}">
<span class="kc-n">{{q.n}} · {{q.kind}}</span>
<h2 class="kc-q">{{q.text}}</h2>
<div class="kc-opts" role="radiogroup" aria-label="{{q.text}}"><sc-for list="{{q.opts}}" as="o" hint-placeholder-count="3"><button type="button" role="radio" aria-checked="{{o.on}}" class="kc-o {{o.cls}}" onClick="{{o.pick}}"><span class="kc-r"><span class="kc-ok">'''+ic('check',11,3.2)+'''</span><span class="kc-no">'''+ic('close',10,3.2)+'''</span></span><span>{{o.label}}</span></button></sc-for></div>
<sc-if value="{{q.fbShown}}" hint-placeholder-val="{{false}}"><div class="kc-fb {{q.fbCls}} cp-pop" role="status"><b>{{q.fbHead}}</b><span>{{q.fbText}}</span></div></sc-if>
</section></sc-for>'''
KC_CSS='''.kc{margin-top:26px;padding:22px 22px 20px 22px;border-radius:22px;background:#FFFFFF;border:1.5px solid #E6EAF3}
.kc-n{font-size:12.5px;font-weight:500;color:#8A93AD}
.kc-q{margin:6px 0 0 0;font-size:19px;line-height:1.4;font-weight:600;letter-spacing:-0.01em}
.kc-opts{margin-top:16px;display:flex;flex-direction:column;gap:8px}
.kc-o{display:flex;align-items:center;gap:12px;min-height:52px;padding:10px 16px 10px 14px;box-sizing:border-box;border-radius:14px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;font-family:inherit;font-size:15.5px;font-weight:500;text-align:left;cursor:pointer;transition:border-color .2s ease,background .2s ease}
.kc-o:hover{border-color:#AFC1F5}
.kc-o:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:2px}
.kc-r{width:22px;height:22px;flex-shrink:0;box-sizing:border-box;border-radius:50%;border:2px solid #CBD3E6;display:flex;align-items:center;justify-content:center;color:#FFFFFF}
.kc-ok,.kc-no{display:none}
.kc-right{border-color:#0F6B45;background:#F1FAF5}
.kc-right .kc-r{background:#0F6B45;border-color:#0F6B45}.kc-right .kc-ok{display:flex}
.kc-wrong{border-color:#E0A23B;background:#FFF9EE}
.kc-wrong .kc-r{background:#B86E00;border-color:#B86E00}.kc-wrong .kc-no{display:flex}
.kc-fb{margin-top:12px;padding:12px 14px;border-radius:14px;display:flex;flex-direction:column;gap:2px;font-size:14.5px;line-height:1.5}
.kc-fb b{font-size:14.5px;font-weight:600}
.kc-fb-ok{background:#E7F5EE;color:#0B4A30}
.kc-fb-no{background:#FFF4E2;color:#6B4100}
@media (max-width: 960px){
.kc{margin-top:18px;padding:16px;border-radius:18px}
.kc-q{font-size:17px}
.kc-o{font-size:14.5px;min-height:48px}
}
'''
NEXT4='<a href="CR-ORI-005.dc.html" class="ds-btn lp-next {{nextCls}}" aria-disabled="{{nextDis}}"><span>{{nextLabel}}</span><span class="ob-arrow">'+ic('arrow',18,2.4)+'</span></a>'
S_KC='''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { a: [1, -1] }; }
  renderVals() {
    const Q = [
      ['Multiple choice', 'Where do you answer a validator’s evidence request?', ['In Messages', 'In the Validation Workspace', 'By email'], 1, 'All validation communication stays in the Validation Workspace, the single record of the case.'],
      ['True or false', 'A course with three creators gets three validation cases.', ['True', 'False'], 1, 'One learning experience, one case. Requests go to the creator they’re about.']
    ];
    const a = this.state.a;
    const qs = Q.map((q, qi) => {
      const pick = a[qi], ok = pick === q[3];
      return {
        n: 'Question ' + (qi + 1) + ' of ' + Q.length, kind: q[0], text: q[1],
        opts: q[2].map((label, oi) => ({ label, on: pick === oi ? 'true' : 'false', cls: pick === oi ? (oi === q[3] ? 'kc-right' : 'kc-wrong') : '', pick: () => { if (ok) return; const n = a.slice(); n[qi] = oi; this.setState({ a: n }); } })),
        fbShown: pick >= 0, fbCls: ok ? 'kc-fb-ok' : 'kc-fb-no', fbHead: ok ? 'Correct.' : 'Not quite.', fbText: ok ? q[4] : 'Have another look and try again.'
      };
    });
    const all = Q.every((q, i) => a[i] === q[3]);
    return { qs, nextCls: all ? '' : 'lp-off', nextDis: all ? 'false' : 'true', nextLabel: all ? 'Complete module' : 'Answer both to finish' };
  }
}'''
PLAYER('CR-ORI-004.dc.html','Credalio · Quick knowledge check','Module 4 · Understanding validation',st(M4,3),3,c,prev=('Tiers and revalidation','CR-ORI-003.dc.html'),script=S_KC,extra_css=KC_CSS,nxt_hole=NEXT4)

# ---------------- CR-ORI-005 · Scenario (Module 5, AI-generated lesson) ----------------
c='''<span class="lp-eb ob-in">'''+ik(SCEN_I,14,2.2)+'''Scenario</span>
<h1 class="lp-h1 ob-in">An AI-drafted lesson</h1>
<div class="sc-sit ob-in2">
<span class="sc-l">The situation</span>
<p>A creator asks AI to generate an entire lesson. It reads well and took seconds. What must happen before it’s submitted for validation?</p>
<div class="sc-doc" aria-hidden="true"><span class="sc-tag">'''+SPK+'''AI-drafted · not reviewed yet</span><b>Cleaning messy data, fast</b><span class="sc-ln" style="width: 92%"></span><span class="sc-ln" style="width: 78%"></span><span class="sc-ln" style="width: 85%"></span></div>
</div>
<h2 class="sc-q ob-in3">What should happen?</h2>
<div class="kc-opts ob-in3" role="radiogroup" aria-label="What should happen?"><sc-for list="{{opts}}" as="o" hint-placeholder-count="3"><button type="button" role="radio" aria-checked="{{o.on}}" class="kc-o {{o.cls}}" onClick="{{o.pick}}"><span class="kc-r"><span class="kc-ok">'''+ic('check',11,3.2)+'''</span><span class="kc-no">'''+ic('close',10,3.2)+'''</span></span><span>{{o.label}}</span></button></sc-for></div>
<sc-if value="{{fbShown}}" hint-placeholder-val="{{true}}"><div class="kc-fb {{fbCls}} cp-pop" role="status"><b>{{fbHead}}</b><span>{{fbText}}</span></div>
<p class="sc-pol">'''+ic('valid',15,2)+'''<span><b>Credalio policy</b> Creators are accountable for all content they submit, however it was produced.</span></p></sc-if>'''
SC_CSS=KC_CSS+'''.sc-sit{margin-top:22px;padding:22px;border-radius:22px;background:#0B1433;color:#FFFFFF;display:grid;grid-template-columns:minmax(0,1fr) 220px;gap:22px;align-items:center}
.sc-l{grid-column:1 / -1;font-size:12.5px;font-weight:500;color:#AFC1F5;margin-bottom:-12px}
.sc-sit p{margin:0;font-size:17px;line-height:1.6;color:#FFFFFF}
.sc-doc{padding:14px;border-radius:14px;background:#FFFFFF;color:#0B1433;display:flex;flex-direction:column;gap:7px;transform:rotate(2deg);box-shadow:0 14px 30px rgba(0,0,0,.25)}
.sc-tag{align-self:flex-start;display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:500;color:#8A5300;background:#FFF4E2;border-radius:999px;padding:3px 8px}
.sc-tag svg{width:11px;height:11px;color:#C27A00}
.sc-doc b{font-size:13.5px;font-weight:600;margin-top:2px}
.sc-ln{display:block;height:6px;border-radius:6px;background:#E6EAF3}
.sc-q{margin:28px 0 0 0;font-size:19px;font-weight:600}
.sc-q + .kc-opts{margin-top:12px}
.sc-pol{margin:12px 0 0 0;display:flex;align-items:flex-start;gap:10px;font-size:14px;line-height:1.5;color:#3A4566}
.sc-pol svg{color:#1652F0;flex-shrink:0;margin-top:2px}
.sc-pol b{font-weight:600;color:#0B1433;margin-right:4px}
@media (max-width: 960px){
.sc-sit{grid-template-columns:minmax(0,1fr);padding:16px;border-radius:18px;gap:14px;margin-top:16px}
.sc-l{margin-bottom:-6px}
.sc-sit p{font-size:15.5px}
.sc-doc{display:none}
.sc-q{font-size:17px;margin-top:22px}
}
'''
NEXT5='<a href="CR-ORI-006.dc.html" class="ds-btn lp-next {{nextCls}}" aria-disabled="{{nextDis}}"><span>Complete module</span><span class="ob-arrow">'+ic('arrow',18,2.4)+'</span></a>'
S_SC='''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { a: 1 }; }
  renderVals() {
    const O = ['Nothing. AI content is pre-approved', 'The creator reviews it for accuracy, checks sources, edits as needed and discloses AI assistance where required', 'The validator rewrites it'];
    const a = this.state.a, ok = a === 1;
    return {
      opts: O.map((label, i) => ({ label, on: a === i ? 'true' : 'false', cls: a === i ? (i === 1 ? 'kc-right' : 'kc-wrong') : '', pick: () => { if (!ok) this.setState({ a: i }); } })),
      fbShown: a >= 0, fbCls: ok ? 'kc-fb-ok' : 'kc-fb-no', fbHead: ok ? 'That’s right.' : 'Not quite. Try another response.',
      fbText: ok ? 'The creator reviews, verifies and takes responsibility for it, and AI assistance is disclosed as policy requires.' : 'Think about who is accountable for the content.',
      nextCls: ok ? '' : 'lp-off', nextDis: ok ? 'false' : 'true'
    };
  }
}'''
PLAYER('CR-ORI-005.dc.html','Credalio · Scenario exercise','Module 5 · AI & responsible creation',st(M5,3),3,c,prev=('Quick knowledge check','CR-ORI-004.dc.html'),script=S_SC,extra_css=SC_CSS,nxt_hole=NEXT5)

# ---------------- CR-ORI-006 · Module complete (Module 5) ----------------
nodes=''.join(f'<span class="dn-n {"dn-d" if i<5 else ""}{" dn-just" if i==4 else ""}">{ic("check",12,3.2) if i<5 else i+1}</span>' for i in range(7))
learned=''.join(f'<li>{ic("check",14,2.6)}<span>{t}</span></li>' for t in ['Nova can explain, suggest and prepare changes','You confirm anything consequential','You own AI-assisted content'])
resp=''.join(f'<li><span class="dn-dot"></span><span>{t}</span></li>' for t in ['Review everything before you approve it','Disclose AI assistance where required'])
c=f'''<div class="dn">
<div class="dn-badge ob-in" aria-hidden="true"><span class="dn-ring"></span><span class="dn-core">{ic('check',34,2.6)}</span></div>
<span class="lp-eb ob-in2" style="justify-content: center">Module 5 complete</span>
<h1 class="lp-h1 dn-h ob-in2">AI &amp; responsible creation</h1>
<p class="dn-sub ob-in2">Five of seven done. You’re well past halfway.</p>
<div class="dn-path ob-in3" aria-label="5 of 7 modules complete">{nodes}</div>
<div class="dn-cards ob-in3">
<section class="dn-c"><span class="sec-h">What you learned</span><ul class="dn-l">{learned}</ul></section>
<section class="dn-c dn-c2"><span class="sec-h">Your responsibilities</span><ul class="dn-l dn-l2">{resp}</ul></section>
</div>
<div class="dn-acts ob-in4">
<a href="#" class="ds-btn dn-go"><span>Next: Creator economy</span><span class="ob-arrow">{ic('arrow',18,2.4)}</span></a>
<a href="CR-ORI-001.dc.html" class="dn-back">Back to Orientation</a>
</div>
</div>'''
DN_CSS2='''.lp-body:has(.dn){padding-bottom:56px}
.dn{width:min(760px,100%);margin:0 auto;display:flex;flex-direction:column;align-items:center;text-align:center;padding-top:clamp(0px,2vh,20px)}
.dn-badge{position:relative;width:96px;height:96px;display:flex;align-items:center;justify-content:center}
.dn-ring{position:absolute;inset:0;border-radius:50%;background:radial-gradient(closest-side,rgba(22,82,240,.18),rgba(22,82,240,0));animation:dnGlow 2.6s ease-in-out infinite}
.dn-core{position:relative;width:68px;height:68px;border-radius:50%;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 14px 30px rgba(22,82,240,.35);animation:dnPop .6s cubic-bezier(.3,1.5,.5,1) .1s both}
@keyframes dnPop{from{transform:scale(.4);opacity:0}to{transform:none;opacity:1}}
@keyframes dnGlow{0%,100%{transform:scale(.9);opacity:.7}50%{transform:scale(1.15);opacity:1}}
.dn .lp-eb{margin-top:14px}
.dn-h{margin-top:6px}
.dn-sub{margin:10px 0 0 0;font-size:17px;color:#4A5578}
.dn-path{margin-top:24px;display:flex;gap:18px;position:relative}
.dn-path::before{content:'';position:absolute;left:13px;right:13px;top:13px;height:3px;border-radius:3px;background:linear-gradient(90deg,#1652F0 0%,#1652F0 66.6%,#E6EAF3 66.6%)}
.dn-n{position:relative;width:28px;height:28px;box-sizing:border-box;border-radius:50%;border:2px solid #D6DDEE;background:#FFFFFF;color:#8A93AD;font-size:12px;font-weight:600;display:flex;align-items:center;justify-content:center}
.dn-d{background:#1652F0;border-color:#1652F0;color:#FFFFFF}
.dn-just{animation:ndPulse 2s ease-out 3}
.dn-cards{margin-top:30px;width:100%;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;text-align:left}
.dn-c{padding:20px;border-radius:20px;background:#FFFFFF;border:1.5px solid #E6EAF3}
.dn-c2{background:#F5F8FF}
.dn-l{list-style:none;margin:12px 0 0 0;padding:0;display:flex;flex-direction:column;gap:10px}
.dn-l li{display:flex;align-items:flex-start;gap:10px;font-size:15px;line-height:1.5}
.dn-l li svg{color:#0F6B45;margin-top:3px;flex-shrink:0}
.dn-dot{width:7px;height:7px;border-radius:50%;background:#1652F0;margin-top:8px;flex-shrink:0}
.dn-acts{margin-top:28px;display:flex;align-items:center;gap:20px}
.dn-back{font-size:15px;font-weight:600;text-decoration:none;color:#3A4566}
.dn-back:hover{color:#1652F0}
@media (prefers-reduced-motion: reduce){.dn-ring,.dn-core,.dn-just{animation:none}}
@media (max-width: 960px){
.dn-badge{width:76px;height:76px}.dn-core{width:56px;height:56px}.dn-core svg{width:28px;height:28px}
.dn-sub{font-size:15px}
.dn-path{gap:10px;margin-top:18px}
.dn-n{width:26px;height:26px}
.dn-cards{grid-template-columns:minmax(0,1fr);margin-top:22px;gap:10px}
.dn-c{padding:16px;border-radius:18px}
.dn-l li{font-size:14.5px}
.dn-acts{flex-direction:column;align-items:stretch;width:100%;gap:14px;margin-top:22px}
.dn-go{justify-content:space-between}
.dn-back{text-align:center;font-size:14.5px}
}
'''
PLAYER('CR-ORI-006.dc.html','Credalio · Module complete','Module 5 · AI & responsible creation',[(l,k,'done') for l,k in M5],None,c,outline=False,bottom=False,extra_css=DN_CSS2)

for n,h in [('CR-ORI-002',900),('CR-ORI-003',844),('CR-ORI-004',844),('CR-ORI-005',844),('CR-ORI-006',844)]:
    WRAP(n+'-Mobile.dc.html',n,390,h,n+' mobile preview'); s=open(P+n+'-Mobile.dc.html').read().replace('background: #F7F9FD','background: #FFFFFF'); open(P+n+'-Mobile.dc.html','w').write(s)
print('build11 done')
