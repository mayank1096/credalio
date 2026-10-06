# Batch 12 · CR-ORI-007 Orientation complete · CR-KYC-001 intro · CR-KYC-002 (Sumsub panel; variants photos / liveness = 002b / 002c)
exec(open('build11.py').read().split('# ---------------- CR-ORI-002')[0])
CAP_I='<path d="m2 9 10-5 10 5-10 5z"></path><path d="M6 11v5c0 1.5 2.7 3 6 3s6-1.5 6-3v-5"></path><path d="M22 9v5"></path>'
PASS_I='<rect x="5" y="3" width="14" height="18" rx="2.5"></rect><circle cx="12" cy="10" r="3"></circle><path d="M9 16h6"></path>'
CARD_I=ID_I
CAR_I='<rect x="3" y="5" width="18" height="14" rx="2.5"></rect><path d="M7 15h4M7 11h10"></path>'
HOME_I='<path d="M4 11 12 4l8 7"></path><path d="M6 10v10h12V10"></path>'
FACE_I='<circle cx="12" cy="9" r="4"></circle><path d="M4.5 20a7.5 7.5 0 0 1 15 0"></path>'
CAM_I='<rect x="3" y="7" width="18" height="13" rx="3"></rect><path d="M8.5 7 10 4.5h4L15.5 7"></path><circle cx="12" cy="13.5" r="3.5"></circle>'
SUN_I='<circle cx="12" cy="12" r="4"></circle><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"></path>'
UP_I='<path d="M12 16V4"></path><path d="m7 9 5-5 5 5"></path><path d="M4 16v3a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-3"></path>'
PHONE_I='<rect x="7" y="2.5" width="10" height="19" rx="2.5"></rect><path d="M11 18.5h2"></path>'

_t=open('build11.py').read(); _a=_t.index("DN_CSS2='''"); _b=_t.index("'''\n",_a+12)+3; exec(_t[_a:_b])
# ---------------- CR-ORI-007 · Orientation complete ----------------
nodes=''.join(f'<span class="dn-n dn-d">{ic("check",12,3.2)}</span>' for i in range(7))
c=f'''<div class="oc">
<div class="dn-badge ob-in" aria-hidden="true"><span class="dn-ring"></span><span class="dn-core">{ik(CAP_I,32,2)}</span></div>
<span class="lp-eb ob-in2" style="justify-content: center">Creator Orientation</span>
<h1 class="lp-h1 dn-h ob-in2">You’ve finished Orientation.</h1>
<p class="dn-sub ob-in2">Seven modules, about 70 minutes, done on 1 October 2026. You know how trusted learning works here.</p>
<div class="dn-path ob-in3" aria-label="All 7 modules complete" style="--full: 1">{nodes}</div>
<div class="oc-grid ob-in3">
<section class="oc-rd" aria-label="Readiness updated">
{ring(60,84,10,'oc','<b style="font-size: 18px">60%</b>')}
<span class="oc-rt"><span class="oc-rl">Readiness, updated automatically</span><b>3 of 5 done</b><span class="oc-ch">{ic('check',12,3)}Orientation ticked off</span></span>
</section>
<section class="oc-next" aria-label="Next for you">
<span class="oc-nl">Next for you</span>
<b>Credentials &amp; expertise</b>
<span class="oc-nd">Your MSc certificate scan is unreadable. Upload a clearer copy and it’s done.</span>
<a href="#" class="ds-btn sm oc-go"><span>Fix my credentials</span><span class="ob-arrow">{ic('arrow',16,2.4)}</span></a>
</section>
</div>
<div class="oc-links ob-in4"><a href="CR-RDY-001.dc.html">View readiness</a><span aria-hidden="true">·</span><a href="CR-DASH-NEW.dc.html">Back to my Studio</a></div>
</div>'''
OC_CSS=DN_CSS2.replace('.dn{','.dn,.oc{').replace('.lp-body:has(.dn)','.lp-body:has(.oc)')+'''.oc{width:min(820px,100%);margin:0 auto;display:flex;flex-direction:column;align-items:center;text-align:center}
.oc .lp-eb{margin-top:14px}
.dn-path[style]::before{background:#1652F0}
.oc-grid{margin-top:30px;width:100%;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.25fr);gap:14px;text-align:left}
.oc-rd{display:flex;align-items:center;gap:18px;padding:20px;border-radius:20px;background:#FFFFFF;border:1.5px solid #E6EAF3}
.oc-rt{display:flex;flex-direction:column;gap:3px}
.oc-rl{font-size:12.5px;font-weight:500;color:#5B6582}
.oc-rt b{font-size:18px;font-weight:600}
.oc-ch{display:inline-flex;align-items:center;gap:6px;font-size:13px;font-weight:500;color:#0F6B45}
.oc-next{display:flex;flex-direction:column;align-items:flex-start;gap:4px;padding:20px;border-radius:20px;background:#F5F8FF;border:1.5px solid #CBD7F5}
.oc-nl{font-size:12.5px;font-weight:500;color:#1652F0}
.oc-next b{font-size:17px;font-weight:600}
.oc-nd{font-size:14px;line-height:1.5;color:#3A4566}
.oc-go{margin-top:12px}
.oc-links{margin-top:22px;display:flex;align-items:center;gap:10px;font-size:14.5px;color:#8A93AD}
.oc-links a{font-weight:600;text-decoration:none;color:#3A4566}
.oc-links a:hover{color:#1652F0}
@media (max-width: 960px){
.oc-grid{grid-template-columns:minmax(0,1fr);gap:10px;margin-top:22px}
.oc-rd{padding:14px 16px;gap:14px;border-radius:18px}
.oc-rd .rg,.oc-rd .rg svg{width:60px !important;height:60px !important}
.oc-rd .rg-in b{font-size:14px !important}
.oc-rt b{font-size:16px}
.oc-next{padding:16px;border-radius:18px}
.oc-next b{font-size:16px}
.oc-go{width:100%;justify-content:space-between}
.oc-links{margin-top:18px;font-size:14px}
}
'''
PLAYER('CR-ORI-007.dc.html','Credalio · Orientation complete','All 7 modules complete',[('m','lesson','done')]*7,None,c,outline=False,bottom=False,extra_css=OC_CSS)
s=open(P+'CR-ORI-007.dc.html').read().replace('<span class="lp-tn">7 steps</span>','<span class="lp-tn">Complete</span>'); open(P+'CR-ORI-007.dc.html','w').write(s)

# ---------------- KYC task shell ----------------
def TASK(fname, title, content, script, css, task='Verify your identity'):
    html=f'''<div class="tk-root">
<header class="tk-top">
<a href="CR-RDY-001.dc.html" class="lp-x" aria-label="Close and go back to readiness">{ic('close',18,2.2)}</a>
<div class="lp-title"><span class="lp-t1">{task}</span><span class="lp-t2">Readiness · task 1 of 5</span></div>
<span style="flex-grow: 1"></span>
<span class="tk-sec">{ik(LOCK_I,14,2.2)}<span>Secure · encrypted</span></span>
</header>
{content}
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
{DASH_CSS}{COMMON_CSS}{LP_CSS}{TK_CSS}{css}</style>
</helmet>
{html}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1440,"height":820}}}}'>
{script}
</script>
</body>
</html>
''')
TK_CSS='''.tk-root{min-height:100vh;display:flex;flex-direction:column;background:#FFFFFF;font-family:'Google Sans','Google Sans Text','Helvetica Neue',system-ui,sans-serif;color:#0B1433}
.tk-top{position:sticky;top:0;z-index:5;height:64px;flex-shrink:0;box-sizing:border-box;display:flex;align-items:center;gap:16px;padding:0 20px;border-bottom:1.5px solid #EEF1F7;background:rgba(255,255,255,.94);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}
.tk-sec{display:inline-flex;align-items:center;gap:7px;height:34px;padding:0 13px 0 11px;border-radius:999px;background:#E7F5EE;color:#0F6B45;font-size:13px;font-weight:500;white-space:nowrap}
.tk-check{display:flex;align-items:flex-start;gap:12px;font-size:14px;line-height:1.5;color:#3A4566;cursor:pointer}
.tk-box{width:22px;height:22px;flex-shrink:0;box-sizing:border-box;border-radius:7px;border:2px solid #CBD3E6;background:#FFFFFF;color:#FFFFFF;display:flex;align-items:center;justify-content:center;margin-top:1px;transition:all .2s ease}
.tk-on .tk-box{background:#1652F0;border-color:#1652F0}
@media (max-width: 960px){
.tk-top{height:56px;padding:0 12px 0 6px;gap:8px}
.tk-top .lp-t1{display:block;font-size:15px}
.tk-top .lp-t2{display:none}
.tk-sec span{display:none}
.tk-sec{width:34px;padding:0;justify-content:center}
}
'''

# ---------------- CR-KYC-001 · Before you start ----------------
NEED=[(CARD_I,'A valid ID'),(FACE_I,'A selfie'),(CAM_I,'A camera'),(SUN_I,'Good light')]
nd=''.join(f'<li class="k1-n"><span class="k1-ni">{ik(i,20,1.9)}</span><b>{t}</b></li>' for i,t in NEED)
c=f'''<main class="k1">
<section class="k1-l">
<span class="lp-eb ob-in">{ik(CLOCK_I,14,2.2)}About 3 to 5 minutes</span>
<h1 class="lp-h1 ob-in">Let’s confirm it’s you.</h1>
<p class="k1-sub ob-in2">Verified creators are how learners know real experts stand behind what they learn.</p>
<span class="sec-h k1-sh ob-in2">You’ll need</span>
<ul class="k1-need ob-in3">{nd}</ul>
</section>
<aside class="k1-card ob-in2">
<span class="k1-ptn"><span class="k1-logo">S</span><span><b>Verified by Sumsub</b><span>Our identity partner</span></span></span>
<p class="k1-priv">{ik(LOCK_I,15,2.2)}<span>Your ID images stay with Sumsub. No one on Credalio sees them.</span></p>
<label class="tk-check {H('ckCls')}" onClick="{H('toggle')}"><span class="tk-box">{ic('check',12,3.2)}</span><span>I agree to Sumsub processing my ID and biometric data to verify me. <a href="#">Privacy notice</a></span></label>
<a href="CR-KYC-002.dc.html" class="ds-btn k1-go {H('goCls')}"><span>Start verification</span><span class="ob-arrow">{ic('arrow',18,2.4)}</span></a>
<span class="k1-later">You can keep drafting while we verify.</span>
</aside>
</main>'''
K1_CSS='''.k1{flex-grow:1;width:min(1120px,100%);box-sizing:border-box;margin:0 auto;padding:clamp(28px,6vh,64px) 32px 48px 32px;display:grid;grid-template-columns:minmax(0,1fr) 420px;gap:64px;align-items:start}
.k1-sub{margin:14px 0 0 0;font-size:17.5px;line-height:1.6;color:#3A4566;max-width:560px}
.k1-sh{display:block;margin:32px 0 12px 2px}
.k1-need{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;max-width:620px}
.k1-n{display:flex;flex-direction:column;align-items:flex-start;gap:12px;padding:16px;border-radius:18px;background:#F7F9FD;border:1.5px solid #EEF1F7}
.k1-n b{font-size:14.5px;font-weight:600;line-height:1.3}
.k1-ni{width:42px;height:42px;flex-shrink:0;border-radius:13px;background:#FFFFFF;color:#1652F0;display:flex;align-items:center;justify-content:center;box-shadow:0 1px 2px rgba(11,20,51,.05)}
.k1-nt{display:flex;flex-direction:column;gap:3px}
.k1-nt b{font-size:15px;font-weight:600}
.k1-nt span{font-size:13.5px;line-height:1.45;color:#5B6582}
.k1-card{padding:24px;gap:18px !important;border-radius:24px;background:#FFFFFF;border:1.5px solid #E6EAF3;box-shadow:0 18px 44px rgba(22,82,240,.08);display:flex;flex-direction:column;gap:16px;position:sticky;top:96px}
.k1-ptn{display:flex;align-items:center;gap:12px}
.k1-ptn > span:last-child{display:flex;flex-direction:column;gap:1px}
.k1-ptn b{font-size:15px;font-weight:600}
.k1-ptn > span:last-child > span{font-size:12.5px;color:#5B6582}
.k1-logo{width:40px;height:40px;border-radius:12px;background:#0B1433;color:#FFFFFF;font-size:18px;font-weight:600;display:flex;align-items:center;justify-content:center}
.k1-how{margin:0;font-size:14.5px;line-height:1.55;color:#0B1433}
.k1-priv{margin:0;display:flex;align-items:center;gap:8px;font-size:13.5px;line-height:1.5;color:#3A4566}
.k1-priv svg{color:#0F6B45;flex-shrink:0}
.k1-go{width:100%;justify-content:space-between}
.k1-go.lp-off{background:#C9D3EC;box-shadow:none;pointer-events:none}
.k1-go.lp-off .ob-arrow{color:#9AA8CC}
.k1-later{font-size:13px;color:#5B6582;text-align:center;margin-top:-4px}
@media (max-width: 960px){
.k1{grid-template-columns:minmax(0,1fr);gap:22px;padding:24px 16px 32px 16px;align-content:start}
.k1-sub{font-size:15px;margin-top:10px}
.k1-sh{margin:22px 0 10px 2px}
.k1-need{grid-template-columns:minmax(0,1fr);gap:0;border:1.5px solid #EEF1F7;border-radius:18px;background:#F7F9FD;overflow:hidden}
.k1-n{flex-direction:row;border:0;border-radius:0;background:transparent;padding:12px 14px;gap:12px;align-items:center}
.k1-n b{font-size:14px}
.k1-n + .k1-n{border-top:1.5px solid #EEF1F7}
.k1-ni{width:36px;height:36px;border-radius:11px}
.k1-ni svg{width:18px;height:18px}
.k1-nt b{font-size:14px}.k1-nt span{display:none}
.k1-need{grid-template-columns:repeat(2,minmax(0,1fr))}
.k1-n + .k1-n{border-top:0}
.k1-n:nth-child(n+3){border-top:1.5px solid #EEF1F7 !important}
.k1-n:nth-child(even){border-left:1.5px solid #EEF1F7}
.k1-how{display:none}
.k1-card{position:static;padding:0;border:0;box-shadow:none;border-radius:0;gap:14px}
.k1-how{font-size:14px}
}
'''
S_K1='''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { ok: false }; }
  renderVals() { const ok = this.state.ok; return { ckCls: ok ? 'tk-on' : '', goCls: ok ? '' : 'lp-off', toggle: (e) => { if (e && e.target && e.target.tagName === 'A') return; if (e && e.preventDefault) e.preventDefault(); this.setState({ ok: !ok }); } }; }
}'''
TASK('CR-KYC-001.dc.html','Credalio · Verify your identity',c,S_K1,K1_CSS)

# ---------------- CR-KYC-002 · Sumsub panel (one source, 3 steps) ----------------
DOCS=[(PASS_I,'Passport'),(CARD_I,'National ID card'),(CAR_I,'Driver’s licence'),(HOME_I,'Residence permit')]
dc=''.join(f'<button type="button" role="radio" class="k2-doc {H("d"+str(i))}" aria-checked="{H("da"+str(i))}" onClick="{H("dp"+str(i))}"><span class="k2-di">{ik(ic_,20,1.9)}</span><span>{l}</span><span class="xb-ck">{ic("check",10,3.4)}</span></button>' for i,(ic_,l) in enumerate(DOCS))
QR=''.join(f'<rect x="{x}" y="{y}" width="1" height="1"></rect>' for x in range(21) for y in range(21) if ((x*7+y*13+x*y)%5<2) and not ((x<7 and y<7) or (x>13 and y<7) or (x<7 and y>13)))
for (ox,oy) in [(0,0),(14,0),(0,14)]:
    QR+=f'<rect x="{ox+.5}" y="{oy+.5}" width="6" height="6" fill="none" stroke="#0B1433" stroke-width="1"></rect><rect x="{ox+2}" y="{oy+2}" width="3" height="3"></rect>'
TIPS='<sc-for list="{{tips}}" as="t" hint-placeholder-count="3"><li>'+ic('check',13,2.8)+'<span>{{t}}</span></li></sc-for>'
c='''<main class="k2">
<aside class="k2-side">
<span class="lp-eb">Step {{stepN}} of 4</span>
<h1 class="k2-h">{{sideH}}</h1>
<p class="k2-sp">You’re in Sumsub’s secure verification. When you finish, you come straight back here.</p>
<span class="sec-h k2-tl">Tips</span>
<ul class="k2-tips">'''+TIPS+'''</ul>
</aside>
<section class="k2-panel" aria-label="Sumsub verification">
<ol class="k2-steps"><sc-for list="{{steps}}" as="s" hint-placeholder-count="4"><li class="k2-s {{s.cls}}"><span class="k2-sd">{{s.n}}</span><span>{{s.label}}</span></li></sc-for></ol>
<div class="k2-body">
<sc-if value="{{s0}}" hint-placeholder-val="{{true}}">
<h2 class="k2-ph">Choose your document</h2>
<label class="ob-lab" for="k2-c" style="margin-top: 14px">Issuing country</label>
<div class="ob-sel k2-sel"><select id="k2-c" class="ob-f"><option selected>Nigeria</option><option>Ghana</option><option>Kenya</option><option>South Africa</option><option>United Kingdom</option><option>Other</option></select>'''+ik('<path d="m6 9 6 6 6-6"></path>',16,2)+'''</div>
<span class="ob-lab" style="margin-top: 14px">Document type</span>
<div class="k2-docs" role="radiogroup" aria-label="Document type">'''+dc+'''</div>
</sc-if>
<sc-if value="{{s1}}" hint-placeholder-val="{{false}}">
<h2 class="k2-ph">Photos of your national ID card</h2>
<div class="k2-ups">
<button type="button" class="k2-up {{fCls}}" onClick="{{addF}}"><span class="k2-ui">{{fIcon}}</span><b>{{fHead}}</b><span>{{fSub}}</span></button>
<button type="button" class="k2-up {{bCls}}" onClick="{{addB}}"><span class="k2-ui">{{bIcon}}</span><b>{{bHead}}</b><span>{{bSub}}</span></button>
</div>
<div class="k2-qr"><svg viewBox="0 0 21 21" width="56" height="56" fill="#0B1433" aria-hidden="true">'''+QR+'''</svg><span><b>'''+ik(PHONE_I,15,2)+'''Use your phone’s camera</b><span>Scan this code to take the photos on your phone. This screen updates by itself.</span></span></div>
</sc-if>
<sc-if value="{{s2}}" hint-placeholder-val="{{false}}">
<h2 class="k2-ph">Liveness check</h2>
<p class="k2-pp">Look at the camera and follow the prompts. It confirms you’re a real person and matches you to your document.</p>
<div class="k2-face {{lvCls}}"><span class="k2-oval"><span class="k2-sil">'''+ik(FACE_I,64,1.4)+'''</span><span class="k2-ok">'''+ic('check',34,2.6)+'''</span></span><span class="k2-fl">{{lvLabel}}</span></div>
</sc-if>
</div>
<footer class="k2-foot"><button type="button" class="ds-ghost k2-back" onClick="{{back}}">'''+ic('back',16,2.2)+'''<span>Back</span></button><button type="button" class="ds-btn k2-go {{goCls}}" onClick="{{go}}"><span>{{goLabel}}</span><span class="ob-arrow">'''+ic('arrow',18,2.4)+'''</span></button></footer>
<span class="k2-pw">'''+ik(LOCK_I,12,2.4)+'''Powered by Sumsub · secure and encrypted</span>
</section>
</main>'''
K2_CSS=FORM_CSS_LITE='''.ob-lab{display:block;font-size:13px;font-weight:600;color:#0B1433;margin:0 0 6px 2px;text-align:left}
.ob-f{width:100%;height:48px;box-sizing:border-box;padding:0 40px 0 16px;border-radius:14px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:inherit;font-size:15px;color:#0B1433;outline:none;appearance:none;-webkit-appearance:none}
.ob-f:focus{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.ob-sel{position:relative}.ob-sel svg{position:absolute;right:14px;top:50%;transform:translateY(-50%);pointer-events:none;color:#5B6582}
'''+'''.k2{flex-grow:1;width:min(1120px,100%);box-sizing:border-box;margin:0 auto;padding:clamp(24px,5vh,56px) 32px 48px 32px;display:grid;grid-template-columns:minmax(0,1fr) 560px;gap:64px;align-items:start}
.k2-side{position:sticky;top:104px;padding-top:8px}
.k2-h{margin:10px 0 0 0;font-size:clamp(30px,4.6vh,40px);line-height:1.12;font-weight:600;letter-spacing:-0.03em}
.k2-sp{margin:12px 0 0 0;font-size:16px;line-height:1.6;color:#3A4566;max-width:440px}
.k2-tl{display:block;margin:28px 0 10px 2px}
.k2-tips{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px}
.k2-tips li{display:flex;align-items:flex-start;gap:10px;font-size:15px;line-height:1.5;color:#0B1433}
.k2-tips svg{color:#0F6B45;flex-shrink:0;margin-top:3px}
.k2-panel{border-radius:24px;background:#FFFFFF;border:1.5px solid #E6EAF3;box-shadow:0 18px 44px rgba(22,82,240,.08);padding:22px 24px 16px 24px;display:flex;flex-direction:column}
.k2-steps{list-style:none;margin:0;padding:0 0 16px 0;border-bottom:1.5px solid #F0F2F8;display:flex;gap:6px}
.k2-s{flex:1 1 0;display:flex;align-items:center;gap:8px;font-size:13px;font-weight:500;color:#8A93AD}
.k2-s::after{content:'';flex-grow:1;height:2px;border-radius:2px;background:#E6EAF3;margin-right:4px}
.k2-s:last-child{flex:0 0 auto}.k2-s:last-child::after{display:none}
.k2-sd{width:24px;height:24px;flex-shrink:0;box-sizing:border-box;border-radius:50%;border:2px solid #D6DDEE;display:flex;align-items:center;justify-content:center;font-size:11.5px;font-weight:600}
.k2-done{color:#0F6B45}.k2-done .k2-sd{background:#0F6B45;border-color:#0F6B45;color:#FFFFFF;font-size:0}
.k2-done .k2-sd::before{content:'';width:8px;height:4px;border-left:2px solid #FFFFFF;border-bottom:2px solid #FFFFFF;transform:rotate(-45deg) translate(1px,-1px)}
.k2-done::after{background:#0F6B45}
.k2-cur{color:#0B1433;font-weight:600}.k2-cur .k2-sd{border-color:#1652F0;background:#1652F0;color:#FFFFFF}
.k2-body{padding:18px 0 2px 0}
.k2-ph{margin:0;font-size:20px;font-weight:600;letter-spacing:-0.01em}
.k2-pp{margin:8px 0 0 0;font-size:14.5px;line-height:1.55;color:#3A4566}
.k2-docs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.k2-doc{display:flex;align-items:center;gap:10px;height:50px;padding:0 12px 0 10px;box-sizing:border-box;border-radius:14px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;font-family:inherit;font-size:14.5px;font-weight:500;cursor:pointer;text-align:left;transition:all .2s ease}
.k2-doc:hover{border-color:#AFC1F5}
.k2-doc > span:nth-child(2){flex-grow:1}
.k2-di{width:32px;height:32px;border-radius:10px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.k2-doc.xb-on{border-color:#1652F0;background:#F5F8FF;color:#0E3BB8;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.k2-doc.xb-on .k2-di{background:#FFFFFF}
.xb-ck{display:none;width:18px;height:18px;border-radius:50%;background:#1652F0;color:#FFFFFF;align-items:center;justify-content:center;flex-shrink:0}
.xb-on .xb-ck{display:inline-flex}
.k2-ups{margin-top:16px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.k2-up{height:104px;box-sizing:border-box;border-radius:16px;border:2px dashed #CBD3E6;background:#F7F9FD;color:#0B1433;font-family:inherit;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;cursor:pointer;padding:10px;transition:all .2s ease}
.k2-up:hover{border-color:#1652F0;background:#F5F8FF}
.k2-ui{width:34px;height:34px;border-radius:10px;background:#FFFFFF;color:#1652F0;display:flex;align-items:center;justify-content:center;margin-bottom:4px;font-size:0}
.k2-ui::before{content:'';width:18px;height:18px;background:currentColor;-webkit-mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M12 16V4'/%3E%3Cpath d='m7 9 5-5 5 5'/%3E%3Cpath d='M4 16v3a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-3'/%3E%3C/svg%3E") center / contain no-repeat;mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M12 16V4'/%3E%3Cpath d='m7 9 5-5 5 5'/%3E%3Cpath d='M4 16v3a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-3'/%3E%3C/svg%3E") center / contain no-repeat}
.k2-up b{font-size:14.5px;font-weight:600}
.k2-up > span:last-child{font-size:12.5px;color:#5B6582}
.k2-upd{border-style:solid;border-color:#0F6B45;background:#F1FAF5}
.k2-upd .k2-ui{background:#0F6B45;color:#FFFFFF}
.k2-upd .k2-ui::before{-webkit-mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='m5 12.5 4.5 4.5L19 7.5'/%3E%3C/svg%3E") center / contain no-repeat;mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='m5 12.5 4.5 4.5L19 7.5'/%3E%3C/svg%3E") center / contain no-repeat}
.k2-qr{margin-top:10px;display:flex;align-items:center;gap:14px;padding:10px 14px 10px 10px;border-radius:16px;border:1.5px solid #E6EAF3}
.k2-qr svg{flex-shrink:0;padding:6px;background:#FFFFFF;border-radius:10px;border:1px solid #EEF1F7}
.k2-qr > span{display:flex;flex-direction:column;gap:4px}
.k2-qr b{display:inline-flex;align-items:center;gap:7px;font-size:14.5px;font-weight:600}
.k2-qr b svg{padding:0;border:0;color:#1652F0}
.k2-qr > span > span{font-size:13px;line-height:1.5;color:#5B6582}
.k2-face{margin-top:14px;display:flex;flex-direction:column;align-items:center;gap:14px}
.k2-oval{position:relative;width:132px;height:162px;border-radius:50%;background:#F5F8FF;display:flex;align-items:center;justify-content:center;color:#AFC1F5}
.k2-oval::before{content:'';position:absolute;inset:-8px;border-radius:50%;border:3px dashed #1652F0;animation:k2Pulse 2.2s ease-in-out infinite}
@keyframes k2Pulse{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(1.04);opacity:.55}}
.k2-ok{display:none;width:72px;height:72px;border-radius:50%;background:#0F6B45;color:#FFFFFF;align-items:center;justify-content:center}
.k2-fl{font-size:14.5px;font-weight:500;color:#3A4566}
.k2-pass .k2-oval{background:#F1FAF5}
.k2-pass .k2-oval::before{border-style:solid;border-color:#0F6B45;animation:none}
.k2-pass .k2-sil{display:none}.k2-pass .k2-ok{display:flex}
.k2-pass .k2-fl{color:#0F6B45;font-weight:600}
.k2-foot{margin-top:14px;padding-top:14px;border-top:1.5px solid #F0F2F8;display:flex;align-items:center;justify-content:space-between;gap:12px}
.k2-back{height:48px}
.k2-go.lp-off{background:#C9D3EC;box-shadow:none;pointer-events:none}
.k2-go.lp-off .ob-arrow{color:#9AA8CC}
.k2-pw{margin-top:10px;display:inline-flex;align-items:center;justify-content:center;gap:6px;font-size:12px;color:#8A93AD}
@media (prefers-reduced-motion: reduce){.k2-oval::before{animation:none}}
@media (max-width: 960px){
.k2{grid-template-columns:minmax(0,1fr);gap:0;padding:0 0 0 0}
.k2-side{position:static;padding:20px 16px 0 16px}
.k2-h{font-size:24px;margin-top:6px}
.k2-sp,.k2-tl,.k2-tips{display:none}
.k2-panel{border:0;box-shadow:none;border-radius:0;padding:16px 16px 0 16px;min-height:calc(100vh - 140px);box-sizing:border-box}
.k2-steps{order:-1;padding-bottom:14px}
.k2-s > span:last-child{display:none}
.k2-cur > span:last-child{display:inline}
.k2-body{min-height:0;flex-grow:1;padding-top:16px}
.k2-ph{font-size:18px}
.k2-docs{grid-template-columns:minmax(0,1fr);gap:8px}
.k2-doc{height:54px}
.k2-up{height:128px}
.k2-qr{display:none}
.k2-oval{width:150px;height:184px}
.k2-up{height:112px}
.k2-foot{position:sticky;bottom:0;background:#FFFFFF;margin:0 -16px;padding:12px 16px;border-top:1.5px solid #EEF1F7}
.k2-back{width:48px;padding:0;flex-shrink:0}
.k2-back span{display:none}
.k2-go{flex-grow:1;justify-content:space-between}
.k2-pw{display:none}
}
'''
S_K2='''class Component extends DCLogic {
  constructor(props) {
    super(props);
    const v = (props || {}).variant;
    const step = v === 'liveness' ? 2 : (v === 'photos' ? 1 : 0);
    this.state = { step, doc: step > 0 ? 1 : -1, f: step > 0, b: step > 1, live: false };
  }
  renderVals() {
    const { step, doc, f, b, live } = this.state;
    const L = ['Document', 'Photos', 'Liveness', 'Submit'];
    const TIPS = [
      ['Use an ID that isn’t expired', 'The name must match your Credalio account', 'Any of the four types works'],
      ['All four corners visible', 'No glare or reflections', 'Not a photocopy or a screenshot'],
      ['Good, even light on your face', 'Look straight at the camera', 'Follow the prompts as they appear']
    ];
    const SH = ['Pick the ID you’ll use', 'Take clear photos', 'A quick selfie check'];
    const ok = step === 0 ? doc >= 0 : (step === 1 ? (f && b) : live);
    const v = {
      stepN: step + 1, sideH: SH[step], tips: TIPS[step],
      steps: L.map((label, i) => ({ label, n: i + 1, cls: i < step ? 'k2-done' : (i === step ? 'k2-cur' : '') })),
      s0: step === 0, s1: step === 1, s2: step === 2,
      fCls: f ? 'k2-upd' : '', fIcon: '', fHead: f ? 'Front added' : 'Front', fSub: f ? 'nin-front.jpg' : 'Click to upload or take a photo', addF: () => this.setState({ f: true }),
      bCls: b ? 'k2-upd' : '', bIcon: '', bHead: b ? 'Back added' : 'Back', bSub: b ? 'nin-back.jpg' : 'Click to upload or take a photo', addB: () => this.setState({ b: true }),
      lvCls: live ? 'k2-pass' : '', lvLabel: live ? 'Liveness check passed' : 'Ready when you are',
      goCls: (ok || (step === 2 && !live)) ? '' : 'lp-off',
      goLabel: step === 2 ? (live ? 'Continue' : 'Start liveness check') : 'Continue',
      go: () => { if (step === 2 && !live) { this.setState({ live: true }); return; } if (ok && step < 2) this.setState({ step: step + 1 }); },
      back: () => { if (step > 0) this.setState({ step: step - 1 }); }
    };
    for (let i = 0; i < 4; i++) { v['d' + i] = doc === i ? 'xb-on' : ''; v['da' + i] = doc === i ? 'true' : 'false'; v['dp' + i] = () => this.setState({ doc: i }); }
    return v;
  }
}'''
TASK('CR-KYC-002.dc.html','Credalio · Verify your identity (Sumsub)',c,S_K2,K2_CSS)
for n,t,prop in [('CR-KYC-002b','Credalio · Verify your identity: photos',' variant="photos"'),('CR-KYC-002c','Credalio · Verify your identity: liveness',' variant="liveness"')]:
    WRAP(n+'.dc.html','CR-KYC-002',1440,820,t,prop)
    s=open(P+n+'.dc.html').read().replace('background: #F7F9FD','background: #FFFFFF'); open(P+n+'.dc.html','w').write(s)
for n,tg,prop in [('CR-ORI-007','CR-ORI-007',''),('CR-KYC-001','CR-KYC-001',''),('CR-KYC-002','CR-KYC-002',''),('CR-KYC-002b','CR-KYC-002',' variant="photos"'),('CR-KYC-002c','CR-KYC-002',' variant="liveness"')]:
    WRAP(n+'-Mobile.dc.html',tg,390,844,n+' mobile preview',prop)
    s=open(P+n+'-Mobile.dc.html').read().replace('background: #F7F9FD','background: #FFFFFF'); open(P+n+'-Mobile.dc.html','w').write(s)
print('build12 done')
