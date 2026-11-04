# Learner checkout (CHK-*): focus shell from Link 2 (CR-WAL-FUND / CR-CREIO-BUY), steps account / plan / pay / review / processing / done.
# Usage: python3 chkgen.py -> writes design/canvas3/project/Checkout.dc.html (props plan, from, step)
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from kit import KIT_CSS, btn, tip, coin, ck, emblem, CLOSE

OUT = os.path.join(HERE, '../../canvas3/project/Checkout.dc.html')

def ic(d, s=20, sw=1.8):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (s, s, sw, d)

BACK = ic('<path d="M19 12H5"></path><path d="m11 18-6-6 6-6"></path>', 18, 2.2)
RET = ic('<path d="M9 14 4 9l5-5"></path><path d="M4 9h11a5 5 0 0 1 0 10h-3"></path>', 15, 2.2)
CKS = '<i class="xb-ck" aria-hidden="true">' + ck(11, 3.4) + '</i>'
G = '<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"></path><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"></path><path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.84z"></path><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"></path></svg>'
A = '<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path fill="#0B1433" d="M16.37 12.63c-.02-2.2 1.8-3.26 1.88-3.31-1.03-1.5-2.62-1.7-3.19-1.73-1.36-.14-2.65.8-3.34.8-.69 0-1.75-.78-2.88-.76-1.48.02-2.85.86-3.61 2.19-1.54 2.67-.39 6.62 1.11 8.79.73 1.06 1.6 2.25 2.75 2.21 1.1-.04 1.52-.71 2.86-.71 1.33 0 1.71.71 2.88.69 1.19-.02 1.94-1.08 2.67-2.15.84-1.23 1.19-2.42 1.21-2.48-.03-.01-2.32-.89-2.34-3.54zM14.17 6.15c.61-.74 1.02-1.76.91-2.78-.88.04-1.94.59-2.57 1.32-.56.65-1.06 1.69-.93 2.69.98.08 1.98-.5 2.59-1.23z"></path></svg>'
M = {'card': '<rect x="3" y="5" width="18" height="14" rx="2.5"></rect><path d="M3 10h18M7 15h4"></path>',
     'local': '<rect x="7" y="2.5" width="10" height="19" rx="2.5"></rect><path d="M11 18h2"></path>',
     'mforge': '<path d="M6 3h12l3 6-9 12L3 9z"></path><path d="M3 9h18M9 3l3 18 3-18"></path>'}

CSS = r'''body{margin:0;background:#FFFFFF}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@keyframes obIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
@keyframes koSpin{to{transform:rotate(360deg)}}
.ob-in{animation:obIn .5s ease both}.ob-in2{animation:obIn .5s ease .08s both}
.tk-root{position:relative;isolation:isolate;overflow-x:hidden;min-height:100vh;display:flex;flex-direction:column;background:#FFFFFF;font-family:'Google Sans','Google Sans Text','Helvetica Neue',system-ui,sans-serif;color:#0B1433}
.tk-top{position:sticky;top:0;z-index:5;height:64px;flex-shrink:0;box-sizing:border-box;display:flex;align-items:center;gap:16px;padding:0 20px;border-bottom:1.5px solid #EEF1F7;background:rgba(255,255,255,.94);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}
.lp-x{width:40px;height:40px;flex-shrink:0;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#3A4566;text-decoration:none}
.lp-x:hover{background:#F5F8FF;color:#0B1433}
.lp-t1{font-size:16px;font-weight:600;white-space:nowrap}
.tk-safe{margin-left:auto;display:inline-flex;align-items:center;gap:7px;font-size:13px;font-weight:500;color:#5B6582}
.cl-glow{position:absolute;left:0;right:0;top:0;height:340px;z-index:-1;pointer-events:none;background:radial-gradient(60% 100% at 50% 0,rgba(22,82,240,.08),transparent 70%)}
.cl-glow.ok{background:radial-gradient(60% 100% at 50% 0,rgba(15,107,69,.10),transparent 70%)}
.cl{flex-grow:1;width:min(1280px,100%);box-sizing:border-box;margin:0 auto;padding:clamp(24px,5vh,52px) 32px 64px 32px;display:grid;grid-template-columns:minmax(0,1fr) 640px;gap:64px;align-items:start;align-content:start}
.cl-side{position:sticky;top:104px;display:flex;flex-direction:column;align-items:flex-start}
.cl-h1{margin:0;font-size:clamp(30px,4.4vh,38px);line-height:1.12;font-weight:600;letter-spacing:-0.03em}
.cl-sub{margin:10px 0 0 0;font-size:15.5px;line-height:1.65;color:#3A4566;max-width:460px}
.cl-steps{list-style:none;margin:32px 0 0 0;padding:0;display:flex;gap:6px;width:100%;max-width:420px}
.cl-steps li{flex:1 1 0;display:flex;flex-direction:column;gap:8px;font-size:13px;font-weight:500;color:#8A93AD}
.cl-steps i{display:block;height:4px;border-radius:4px;background:#E6EAF3}
.cl-steps .on i{background:#1652F0}.cl-steps .on{color:#0B1433}
.cl-steps .dn i{background:#0F6B45}.cl-steps .dn{color:#0F6B45}
.cl-panel{border-radius:24px;background:#FFFFFF;border:1.5px solid #E6EAF3;box-shadow:0 18px 44px rgba(22,82,240,.08);padding:24px 26px 18px 26px;display:flex;flex-direction:column}
.cl-ph{margin:0;font-size:20px;font-weight:600;letter-spacing:-0.01em}
.cl-pp{margin:8px 0 0 0;font-size:14.5px;line-height:1.55;color:#3A4566}
.cl-foot{margin-top:20px;padding-top:16px;border-top:1.5px solid #F0F2F8;display:flex;align-items:center;gap:12px}
.cl-bk{width:52px;height:52px;flex-shrink:0;border-radius:50%;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;display:flex;align-items:center;justify-content:center;cursor:pointer;font-family:inherit}
.cl-bk:hover{border-color:#1652F0}
.cl-foot .ds-btn{margin-left:auto}
.wf-ret{margin-top:14px;display:inline-flex;align-items:center;gap:8px;height:32px;padding:0 13px;border-radius:999px;background:#F5F8FF;border:1.5px solid #E1E9FF;color:#0E3BB8;font-size:13px;font-weight:500}
.hp-lab{display:block;font-size:12.5px;font-weight:500;color:#8A93AD}
.wf-bal{margin-top:20px;display:flex;align-items:center;gap:12px}
.wf-bal .dlp-c{width:36px;height:36px}
.wf-bal b{display:block;margin-top:2px;font-size:17px;font-weight:600}
.xb-ck{display:none;position:absolute;top:14px;right:14px;width:20px;height:20px;border-radius:50%;background:#1652F0;color:#FFFFFF;align-items:center;justify-content:center;font-style:normal}
.xb-on{border-color:#1652F0 !important;background:#F5F8FF !important;box-shadow:0 0 0 4px rgba(22,82,240,.10)}
.xb-on .xb-ck{display:inline-flex}
.wf-o,.wf-m{position:relative;font-family:inherit;text-align:left;cursor:pointer;color:#0B1433;background:#FFFFFF;border:1.5px solid #E6EAF3;border-radius:16px;transition:border-color .2s ease,background .2s ease}
.wf-o:hover,.wf-m:hover{border-color:#AFC1F5}
.ck-pl{margin-top:18px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.ck-pl.n3{grid-template-columns:repeat(3,minmax(0,1fr))}
.ck-p{display:flex;flex-direction:column;gap:3px;padding:18px 18px 16px}
.ck-p > .ds-tag{position:absolute;top:-12px;left:16px}
.ck-p .hp-lab{font-size:13px;color:#5B6582}
.ck-p b{display:flex;align-items:center;gap:8px;margin-top:2px;font-size:22px;font-weight:600;letter-spacing:-.4px}
.ck-p b .dlp-c{width:22px;height:22px}
.ck-p span.ck-pr{font-size:14px;color:#3A4566}
.ck-perks{margin:16px 0 0;padding:16px 18px;list-style:none;border-radius:16px;background:#F7F9FD;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px 18px}
.ck-perks li{display:flex;align-items:flex-start;gap:9px;font-size:14px;line-height:1.4;color:#3A4566}
.ck-perks li i{width:18px;height:18px;border-radius:999px;background:#E7F5EE;color:#0F6B45;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px}
.ck-fit{margin:14px 0 0;display:flex;align-items:flex-start;gap:10px;font-size:14px;line-height:1.5;color:#3A4566}
.ck-fit i{width:20px;height:20px;border-radius:999px;flex-shrink:0;margin-top:1px;display:flex;align-items:center;justify-content:center;font-style:normal;font-size:12px;font-weight:700;color:#FFFFFF;background:#0F6B45}
.ck-fit.part i{background:#B97A10}
.wf-tot{margin-top:16px;display:flex;align-items:baseline;gap:10px;padding:14px 18px;border-radius:16px;background:#F5F8FF}
.wf-tot > span:first-child{font-size:14px;color:#3A4566}
.wf-tot b{font-size:20px;font-weight:600}
.wf-tot small{margin-left:auto;font-size:13.5px;color:#5B6582}
.wf-ml{margin-top:18px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.wf-m{display:flex;flex-direction:column;align-items:flex-start;gap:12px;padding:16px;box-sizing:border-box}
.wf-mi{width:40px;height:40px;flex-shrink:0;border-radius:12px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.wf-m.xb-on .wf-mi{background:#FFFFFF}
.wf-mt{display:flex;flex-direction:column;gap:2px}
.wf-mt b{font-size:15px;font-weight:600}.wf-mt span{font-size:13px;line-height:1.4;color:#5B6582}
.ck-form{margin-top:16px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.ck-f{display:flex;flex-direction:column;gap:6px;grid-column:span 4}
.ck-f.h{grid-column:span 2}
.ck-f.q{grid-column:span 1}
.ck-f label{font-size:13px;font-weight:500;color:#3A4566}
.ck-f select.ds-in{appearance:none;-webkit-appearance:none;background:#FFFFFF url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%235B6582' stroke-width='2' stroke-linecap='round'%3E%3Cpath d='m6 9 6 6 6-6'/%3E%3C/svg%3E") right 14px center no-repeat;padding-right:40px}
.wf-dl{margin:16px 0 0 0;border:1.5px solid #E6EAF3;border-radius:18px;padding:4px 20px}
.wf-dl > div{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:13px 0;border-top:1.5px solid #F0F2F8}
.wf-dl > div:first-child{border-top:0}
.wf-dl dt{display:flex;align-items:center;font-size:14.5px;color:#5B6582}
.wf-dl dd{margin:0;font-size:15px;font-weight:600;display:flex;align-items:center;gap:8px;text-align:right}
.wf-dl .ds-link{font-size:13.5px;font-weight:600}
.wf-total{border-top:1.5px solid #D6DDEE !important}
.wf-total dt{font-size:16px;font-weight:600;color:#0B1433}.wf-total dd{font-size:22px}
.ck-acc .ck-row{margin-top:18px;display:flex;gap:10px}
.ck-acc .ck-row .ds-in{height:56px;border-radius:999px;padding:0 22px;font-size:16px}
.ck-or{margin:18px 0;display:flex;align-items:center;gap:14px;font-size:13px;color:#5B6582}
.ck-or span{flex-grow:1;height:1px;background:#E6EAF3}
.ck-sso{display:flex;gap:10px}
.ck-sso a{flex:1 1 0;display:flex;align-items:center;justify-content:center;gap:10px;height:52px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;font-size:15px;font-weight:600;text-decoration:none;transition:border-color .2s ease,background .2s ease}
.ck-sso a:hover{border-color:#1652F0;background:#F5F8FF}
.ck-terms{margin:16px 0 4px;font-size:12.5px;line-height:1.5;color:#5B6582}
.ck-terms a{color:#3A4566;font-weight:500}
.wf-solo{grid-template-columns:minmax(0,640px);justify-content:center;padding-top:clamp(40px,9vh,96px)}
.ck-out{display:flex;flex-direction:column;align-items:center;text-align:center}
.ck-out h1{margin:14px 0 0;font-size:clamp(32px,5vh,44px);line-height:1.1;font-weight:600;letter-spacing:-.035em}
.ck-out p.cl-pp{max-width:480px;font-size:16px}
.wf-spin{width:58px;height:58px;border-radius:50%;border:4px solid #EAF0FF;border-top-color:#1652F0;animation:koSpin 1s linear infinite;box-sizing:border-box}
.ck-wal{margin-top:26px;width:100%;max-width:460px;display:flex;align-items:center;gap:14px;padding:16px 20px;text-align:left;box-sizing:border-box}
.ck-wal .dlp-c{width:40px;height:40px}
.ck-wal b{display:block;font-size:20px;font-weight:600;letter-spacing:-.3px}
.ck-wal small{display:block;margin-top:2px;font-size:13.5px;color:#5B6582}
.ck-wal .ds-tag{margin-left:auto}
.ck-out .ds-acts{margin-top:28px}
.ck-safe{margin-top:22px;display:inline-flex;align-items:center;gap:8px;padding:10px 14px;border-radius:12px;background:#F5F8FF;font-size:13.5px;font-weight:500;color:#0E3BB8}
.ko-v.cb{--k:#1652F0;--kb:#EAF0FF}
@media (prefers-reduced-motion: reduce){.ob-in,.ob-in2,.wf-spin{animation:none}}
@media (max-width: 960px){
.tk-top{height:56px;padding:0 12px 0 6px;gap:8px}
.lp-t1{font-size:15px}
.tk-safe span{display:none}
.cl{grid-template-columns:minmax(0,1fr);gap:28px;padding:24px 16px 0 16px}
.cl-side{position:static}
.cl-h1{font-size:24px}
.cl-sub{display:none}
.wf-bal{display:none}
.cl-steps{margin-top:20px;max-width:none}
.cl-panel{border:0;box-shadow:none;border-radius:0;padding:0;background:none}
.cl-ph{font-size:18px}
.cl-foot{position:sticky;bottom:0;z-index:4;margin:28px -16px 0 -16px;padding:12px 16px;background:#FFFFFF;border-top:1.5px solid #EEF1F7}
.cl-foot .ds-btn{flex-grow:1;justify-content:space-between}
.ck-pl.n3{grid-template-columns:minmax(0,1fr)}
.ck-perks{grid-template-columns:minmax(0,1fr)}
.wf-ml{grid-template-columns:minmax(0,1fr)}
.wf-m{flex-direction:row;align-items:center;padding:14px}
.ck-f.h{grid-column:span 4}
.ck-f.q{grid-column:span 2}
.wf-dl{padding:2px 16px}
.ck-acc .ck-row{flex-direction:column}
.ck-acc .ck-row .ds-btn{justify-content:space-between}
.ck-sso{flex-direction:column}
.ck-sso a{flex:none}
.wf-solo{padding-top:40px}
.ck-out h1{font-size:28px}
.ck-out .ds-acts{position:static;margin:24px 0 0;padding:0;border:0;width:100%}
}
@media (max-width: 760px){.ck-pl{grid-template-columns:minmax(0,1fr);gap:16px}}
'''

STEPS = '<ol class="cl-steps" aria-label="Steps"><sc-for list="{{steps}}" as="s" hint-placeholder-count="3"><li class="{{s.cls}}"><i></i><span>{{s.t}}</span></li></sc-for></ol>'

MARKUP = '''<div class="tk-root">
<div class="cl-glow {{glowCls}}" aria-hidden="true"></div>
<header class="tk-top">
<a href="{{closeHref}}" class="lp-x" aria-label="Close and go back">''' + CLOSE + '''</a>
<span class="lp-t1">{{barT}}</span>
<span class="tk-safe">''' + ic('<rect x="5" y="10.5" width="14" height="10" rx="2.5"></rect><path d="M8.5 10.5V8a3.5 3.5 0 0 1 7 0v2.5"></path>', 15, 2) + '''<span>Secure checkout</span></span>
</header>

<sc-if value="{{showFlow}}" hint-placeholder-val="{{ true }}">
<main class="cl">
<aside class="cl-side ob-in">
<h1 class="cl-h1">{{h1}}</h1>
<p class="cl-sub">{{ctx}}</p>
<sc-if value="{{hasRet}}" hint-placeholder-val="{{ true }}"><span class="wf-ret">''' + RET + '''{{ret}}</span></sc-if>
<div class="wf-bal">''' + coin(True) + '''<span><span class="hp-lab">Current balance</span><b>{{bal}} DLP</b></span></div>
''' + STEPS + '''
</aside>
<div class="cl-main">

<sc-if value="{{vAccount}}" hint-placeholder-val="{{ false }}">
<section class="cl-panel ck-acc ob-in2" aria-labelledby="ck-ha">
<h2 id="ck-ha" class="cl-ph">First, create your account</h2>
<p class="cl-pp">Your plan, DLP and progress stay with you.</p>
<div class="ck-row"><label for="ck-em" class="sr-only">Email address</label><input id="ck-em" class="ds-in" type="email" autocomplete="email" placeholder="you@example.com" value="{{email}}" onInput="{{onEmail}}">''' + btn('Continue with Email', '#', '', 'onClick="{{toPlan}}"', 'button') + '''</div>
<div class="ck-or" aria-hidden="true"><span></span>or<span></span></div>
<div class="ck-sso"><a href="#" onClick="{{toPlan}}">''' + G + '''Continue with Google</a><a href="#" onClick="{{toPlan}}">''' + A + '''Continue with Apple</a></div>
<p class="ck-terms">By continuing, you agree to Credalio’s <a href="#">Terms</a> and <a href="#">Privacy Policy</a>.</p>
</section>
</sc-if>

<sc-if value="{{vPlan}}" hint-placeholder-val="{{ true }}">
<section class="cl-panel ob-in2" aria-labelledby="ck-hp">
<h2 id="ck-hp" class="cl-ph">{{planH}}</h2>
<div class="ck-pl {{plCls}}" role="radiogroup" aria-label="{{planH}}"><sc-for list="{{tiles}}" as="o" hint-placeholder-count="2"><button type="button" role="radio" aria-checked="{{o.on}}" class="wf-o ck-p {{o.cls}}" onClick="{{o.pick}}"><sc-if value="{{o.hasTag}}" hint-placeholder-val="{{ false }}"><span class="ds-tag solid">{{o.tag}}</span></sc-if><span class="hp-lab">{{o.name}}</span><b>''' + coin() + '''{{o.dlp}}</b><span class="ck-pr">{{o.sub}}</span>''' + CKS + '''</button></sc-for></div>
<sc-if value="{{hasPerks}}" hint-placeholder-val="{{ true }}"><ul class="ck-perks" aria-label="Included"><sc-for list="{{perks}}" as="k" hint-placeholder-count="4"><li><i>''' + ck(10, 3.4) + '''</i>{{k.t}}</li></sc-for></ul></sc-if>
<sc-if value="{{hasFit}}" hint-placeholder-val="{{ false }}"><p class="ck-fit {{fitCls}}"><i><sc-if value="{{fitOk}}" hint-placeholder-val="{{ true }}">''' + ck(11, 3.4) + '''</sc-if><sc-if value="{{fitPart}}" hint-placeholder-val="{{ false }}">!</sc-if></i><span>{{fit}}</span></p></sc-if>
<div class="wf-tot"><span>Today you pay</span><b>{{today}}</b><small>{{then}}</small></div>
<div class="cl-foot"><sc-if value="{{canBackPlan}}" hint-placeholder-val="{{ false }}"><button type="button" class="cl-bk" aria-label="Back" onClick="{{toAccount}}">''' + BACK + '''</button></sc-if>''' + btn('Choose payment', '#', '', 'onClick="{{toPay}}"', 'button') + '''</div>
</section>
</sc-if>

<sc-if value="{{vPay}}" hint-placeholder-val="{{ false }}">
<section class="cl-panel ob-in2" aria-labelledby="ck-hy">
<h2 id="ck-hy" class="cl-ph">How would you like to pay?</h2>
<div class="wf-ml" role="radiogroup" aria-label="Payment method"><sc-for list="{{methods}}" as="m" hint-placeholder-count="3"><button type="button" role="radio" aria-checked="{{m.on}}" class="wf-m {{m.cls}}" onClick="{{m.pick}}"><span class="wf-mi"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><g style="display: {{m.i0}}">''' + M['card'] + '''</g><g style="display: {{m.i1}}">''' + M['local'] + '''</g><g style="display: {{m.i2}}">''' + M['mforge'] + '''</g></svg></span><span class="wf-mt"><b>{{m.t}}</b><span>{{m.d}}</span></span>''' + CKS + '''</button></sc-for></div>
<sc-if value="{{isCard}}" hint-placeholder-val="{{ true }}">
<div class="ck-form">
<div class="ck-f"><label for="ck-cn">Name on card</label><input id="ck-cn" class="ds-in" autocomplete="cc-name" placeholder="Ada Ononuju"></div>
<div class="ck-f"><label for="ck-num">Card number</label><input id="ck-num" class="ds-in" inputmode="numeric" autocomplete="cc-number" placeholder="1234 5678 9012 3456"></div>
<div class="ck-f q"><label for="ck-ex">Expiry</label><input id="ck-ex" class="ds-in" autocomplete="cc-exp" placeholder="MM/YY"></div>
<div class="ck-f q"><label for="ck-cv">Security code</label><input id="ck-cv" class="ds-in" inputmode="numeric" autocomplete="cc-csc" placeholder="123"></div>
<div class="ck-f h"><label for="ck-co">Country</label><select id="ck-co" class="ds-in"><option>Nigeria</option><option>United Kingdom</option><option>Ghana</option><option>Kenya</option></select></div>
</div>
</sc-if>
<sc-if value="{{isOther}}" hint-placeholder-val="{{ false }}"><p class="cl-pp">{{otherNote}}</p></sc-if>
<div class="cl-foot"><button type="button" class="cl-bk" aria-label="Back" onClick="{{toPlanBack}}">''' + BACK + '''</button>''' + btn('Review', '#', '', 'onClick="{{toReview}}"', 'button') + '''</div>
</section>
</sc-if>

<sc-if value="{{vReview}}" hint-placeholder-val="{{ false }}">
<section class="cl-panel ob-in2" aria-labelledby="ck-hr">
<h2 id="ck-hr" class="cl-ph">Review and pay</h2>
<dl class="wf-dl">
<div><dt>{{rvK}}</dt><dd>{{rvV}}</dd></div>
<div><dt>{{rvK2}}</dt><dd>''' + coin() + '''{{rvV2}}</dd></div>
<sc-if value="{{isSub}}" hint-placeholder-val="{{ true }}"><div><dt>Then</dt><dd>{{rvThen}}</dd></div></sc-if>
<div><dt>Pay with</dt><dd>Visa •••• 4242 <button type="button" class="ds-link" onClick="{{toPayBack}}">Change</button></dd></div>
<div class="wf-total"><dt>Total today<span class="tip" tabindex="0" aria-label="More info">''' + ic('<circle cx="12" cy="12" r="9"></circle><path d="M12 11v5"></path><path d="M12 7.6v.2"></path>', 15, 2.2) + '''<span class="tip-b" role="tooltip">{{totTip}}</span></span></dt><dd>{{today}}</dd></div>
</dl>
<div class="cl-foot"><button type="button" class="cl-bk" aria-label="Back" onClick="{{toPayBack}}">''' + BACK + '''</button>''' + btn('{{payLabel}}', '#', '', 'onClick="{{pay}}"', 'button') + '''</div>
</section>
</sc-if>

</div>
</main>
</sc-if>

<sc-if value="{{vProc}}" hint-placeholder-val="{{ false }}">
<main class="cl wf-solo"><div class="ck-out ko-v cb ob-in">
<div class="ko-emb" aria-hidden="true"><span class="ko-halo"></span><span class="wf-spin" style="position: relative; z-index: 1"></span></div>
<span class="ko-pill">Processing</span>
<h1>{{procT}}</h1>
<p class="cl-pp">This takes a few seconds. You won’t be charged twice.</p>
<span class="ck-safe">''' + ic('<rect x="5" y="10.5" width="14" height="10" rx="2.5"></rect><path d="M8.5 10.5V8a3.5 3.5 0 0 1 7 0v2.5"></path>', 15, 2) + '''Payment secured by your bank</span>
</div></main>
</sc-if>

<sc-if value="{{vDone}}" hint-placeholder-val="{{ false }}">
<main class="cl wf-solo"><div class="ck-out ko-v ob-in">
''' + emblem(True) + '''
<span class="ko-pill">{{donePill}}</span>
<h1>{{doneT}}</h1>
<p class="cl-pp">{{doneB}}</p>
<div class="ds-card ck-wal">''' + coin(True) + '''<span><b>{{walN}} DLP</b><small>{{walSub}}</small></span><span class="ds-tag green">{{walTag}}</span></div>
<div class="ds-acts c"><a class="ds-link" href="#">View receipt</a>''' + btn('{{nextL}}', '{{nextH}}') + '''</div>
</div></main>
</sc-if>
</div>'''

JS = r'''
class Component extends DCLogic {
  constructor(props) {
    super(props); var p = props || {};
    this.state = { step: p.step || 'plan', plan: p.plan || 'pro', pkg: 1000, method: 'card', email: '' };
  }
  componentWillUnmount() { clearTimeout(this._t); }
  renderVals() {
    var self = this, S = this.state, p = this.props || {}, from = p.from || 'pricing', top = S.plan === 'topup', st = S.step;
    var f = function (n) { return n.toLocaleString('en-GB'); };
    var P = { basic: { name: 'Basic', dlp: 2000, price: 19, hrs: 20, perks: ['2,000 DLP every month', 'More time with your AI Coach', 'Validated courses and career paths', 'Practice, projects and assessments', 'Learning Season rewards', 'Cancel anytime'] },
      pro: { name: 'Pro', dlp: 6000, price: 39, hrs: 60, perks: ['6,000 DLP every month', 'The most time with your AI Coach', 'Built for career paths and certifications', 'Unused DLP rolls over, up to 18,000', 'Priority access to new learning', 'Cancel anytime'] } };
    var TOP = { 500: 6, 1000: 11, 2500: 25 };
    var signedOut = from === 'pricing';
    var flow = top ? ['Amount', 'Payment', 'Review'] : (signedOut ? ['Account', 'Plan', 'Payment', 'Review'] : ['Plan', 'Payment', 'Review']);
    var at = { account: 'Account', plan: top ? 'Amount' : 'Plan', pay: 'Payment', review: 'Review' }[st];
    var idx = flow.indexOf(at);
    var CTX = { pricing: ['Pick a plan and create your account. It takes about a minute.', 'Then a few quick questions'], onboarding: ['You chose Pro while building your journey. Set up your plan, then start learning.', 'Then back to your journey'],
      allowance: ['Upgrade to keep going with your Data Analyst journey. Your progress is saved.', 'Then back to SQL for Data Analysis'], path: ['Pick the plan that fits your Data Analyst path. The whole path needs about 3,800 DLP.', 'Then back to the Data Analyst path'],
      account: ['Change your plan. The new allowance starts straight away.', 'Then back to your allowance'], course: ['Add the DLP you need for Advanced Analytics with Python. Your plan stays the same.', 'Then back to your course'] }[from] || ['', ''];
    var NEXT = { pricing: ['Personalise Credalio', 'OnbAbout.dc.html'], onboarding: ['Start my journey', 'Dash-R.dc.html'], allowance: ['Continue to SQL for Data Analysis', 'Dash-E.dc.html'], path: ['Back to the Data Analyst path', 'PathDetail-Learner.dc.html'], account: ['Back to my allowance', 'Usage.dc.html'], course: ['Back to Advanced Analytics with Python', 'CourseDetail-Learner.dc.html'] }[from];
    var base = { course: 150, allowance: 0, account: 1460 }[from]; if (base === undefined) base = 200;
    var pl = P[S.plan] || P.pro, price = top ? TOP[S.pkg] : pl.price, add = top ? S.pkg : pl.dlp;
    var go = function (s) { return function (e) { if (e && e.preventDefault) e.preventDefault(); self.setState({ step: s }); }; };
    var tiles = top ? [500, 1000, 2500].map(function (n) { var on = S.pkg === n; return { name: f(n) + ' DLP', dlp: f(n), sub: '$' + TOP[n] + ' · one time', on: on ? 'true' : 'false', cls: on ? 'xb-on' : '', hasTag: n === 1000, tag: 'Most chosen', pick: function () { self.setState({ pkg: n }); } }; })
      : ['basic', 'pro'].map(function (k) { var q = P[k], on = S.plan === k; return { name: q.name, dlp: f(q.dlp) + ' a month', sub: '$' + q.price + ' a month · about ' + q.hrs + ' learning hours', on: on ? 'true' : 'false', cls: on ? 'xb-on' : '', hasTag: k === 'pro', tag: 'Best for career paths', pick: function () { self.setState({ plan: k }); } }; });
    var ME = [['card', 'Card', 'Visa, Mastercard, Verve'], ['local', 'Local payment', 'Bank app, USSD or mobile money'], ['mforge', 'MFORGE', 'Pay from your TruVault']];
    return {
      barT: top ? 'Add DLP' : 'Your plan', closeHref: NEXT[1], glowCls: st === 'done' ? 'ok' : '',
      showFlow: ['account', 'plan', 'pay', 'review'].indexOf(st) > -1, vAccount: st === 'account', vPlan: st === 'plan', vPay: st === 'pay', vReview: st === 'review', vProc: st === 'processing', vDone: st === 'done',
      h1: top ? 'Add DLP' : (signedOut ? 'Get ' + pl.name : 'Choose your plan'), ctx: CTX[0], ret: CTX[1], hasRet: !!CTX[1], bal: f(base),
      steps: flow.map(function (t, i) { return { t: t, cls: i < idx ? 'dn' : (i === idx ? 'on' : '') }; }),
      email: S.email, onEmail: function (e) { self.setState({ email: e.target.value }); }, toPlan: go('plan'), toAccount: go('account'), canBackPlan: signedOut && !top,
      planH: top ? 'How much DLP?' : 'Which plan?', plCls: top ? 'n3' : '', tiles: tiles,
      hasPerks: !top, perks: (top ? [] : pl.perks).map(function (t) { return { t: t }; }),
      today: '$' + price + '.00', then: top ? 'One time · your plan stays the same' : 'then $' + price + ' every month',
      toPay: go('pay'), toPlanBack: go('plan'), toReview: go('review'), toPayBack: go('pay'),
      methods: ME.map(function (m, i) { var on = S.method === m[0]; var v = { t: m[1], d: m[2], on: on ? 'true' : 'false', cls: on ? 'xb-on' : '', pick: function () { self.setState({ method: m[0] }); } }; for (var j = 0; j < 3; j++) v['i' + j] = j === i ? 'inline' : 'none'; return v; }),
      isCard: S.method === 'card', isOther: S.method !== 'card', otherNote: S.method === 'local' ? 'After you review, we’ll show you how to finish in your bank app or by USSD.' : 'After you review, approve the payment in TruVault.',
      rvK: top ? 'Top-up' : 'Plan', rvV: top ? 'One time' : pl.name, rvK2: top ? 'You’ll get' : 'Each month', rvV2: f(add) + ' DLP', isSub: !top, rvThen: '$' + price + ' every month from 27 October',
      totTip: top ? 'Added to your balance straight away. Your plan stays the same.' : 'Cancel anytime from your account. You keep your DLP until the end of the month.',
      payLabel: top ? 'Pay $' + price + ' and add DLP' : 'Pay $' + price + ' and start ' + pl.name,
      pay: function () { self.setState({ step: 'processing' }); clearTimeout(self._t); self._t = setTimeout(function () { self.setState({ step: 'done' }); }, 1800); },
      procT: top ? 'Adding ' + f(add) + ' DLP…' : 'Setting up your ' + pl.name + ' plan…',
      hasFit: !top && (from === 'path' || from === 'allowance'), fitOk: !(from === 'path' && S.plan === 'basic'), fitPart: from === 'path' && S.plan === 'basic', fitCls: (from === 'path' && S.plan === 'basic') ? 'part' : '',
      fit: from === 'allowance' ? (S.plan === 'basic' ? 'Stage 2 needs about 1,400 DLP. Basic covers it, with room to spare.' : 'Pro covers Stage 2 and most of what comes after it.') : (S.plan === 'basic' ? 'The path needs about 3,800 DLP. Basic covers it over about two months.' : 'The path needs about 3,800 DLP. Pro covers it in your first month.'),
      donePill: top ? 'DLP added' : ((from === 'path' || from === 'account') ? 'Plan updated' : 'Plan active'), doneT: top ? f(add) + ' DLP added.' : 'You’re on ' + pl.name + '.',
      doneB: top ? 'Your plan hasn’t changed. The extra DLP is ready to use now.' : ({ pricing: 'Next, tell us a little about what you want to learn, or explore straight away.', onboarding: 'Your starting journey is waiting for you.', allowance: 'Your Data Analyst journey is ready to continue.', path: 'Your Data Analyst path is ready to continue.', account: 'Your new allowance is ready to use.' }[from] || ''),
      walN: f(base + add), walSub: 'About ' + Math.round((base + add) / 100) + ' learning hours', walTag: top ? 'Plan unchanged' : pl.name + ' plan',
      nextL: NEXT[0], nextH: NEXT[1]
    };
  }
}
'''

PROPS = {"plan": {"editor": "enum", "options": ["basic", "pro", "topup"], "default": "pro"},
         "from": {"editor": "enum", "options": ["pricing", "onboarding", "allowance", "path", "account", "course"], "default": "onboarding"},
         "step": {"editor": "enum", "options": ["account", "plan", "pay", "review", "processing", "done"], "default": "plan"},
         "$preview": {"width": 1440, "height": 900}}

HTML = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Checkout</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">
<style>
''' + KIT_CSS + '\n' + CSS + '''</style>
</helmet>
''' + MARKUP + '''
</x-dc>
<script type="text/x-dc" data-dc-script data-props='%s'>%s</script>
</body>
</html>
''' % (json.dumps(PROPS), JS)

if __name__ == '__main__':
    open(OUT, 'w').write(HTML)
    print('wrote', OUT, len(HTML))
