from shell import *
CLOUD='/_blob/020f1a8593e80e5fcee9e0f06637f153'
MARK='/_blob/f81e36d31295a0d0737959589ec1abd4'
CK='<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg>'
css=r'''
.jy-page{min-height:100%;overflow-x:clip;background:#FFFFFF url(CLOUD) center top / max(1440px,100%) auto no-repeat}
.jy-bar{max-width:1360px;margin:0 auto;height:72px;padding:0 24px;box-sizing:border-box;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:16px}
.jy-steps{display:flex;align-items:center;gap:0;font-size:13px;font-weight:500;color:#8A93AD}
.jy-st{display:inline-flex;align-items:center;gap:8px;white-space:nowrap}
.jy-st i{width:24px;height:24px;border-radius:999px;border:1.5px solid #CBD3E6;background:#FFFFFF;display:flex;align-items:center;justify-content:center;font-style:normal;font-size:11px;font-weight:600;color:#8A93AD;box-sizing:border-box}
.jy-st-on{color:#0B1433}
.jy-st-on i{border-color:#1652F0;color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.jy-st-done i{background:#1652F0;border-color:#1652F0;color:#FFFFFF}
.jy-ln{width:44px;height:2px;margin:0 12px;border-radius:2px;background:#DCE5FB}
.jy-ln-on{background:#1652F0}
.jy-right{display:flex;align-items:center;justify-content:flex-end;gap:8px}
.jy-login{height:40px;padding:0 12px;border-radius:999px;display:flex;align-items:center;font-size:15px;font-weight:600;color:#0B1433;text-decoration:none}
.jy-x{width:44px;height:44px;border-radius:999px;border:1.5px solid #D6DDEE;background:rgba(255,255,255,.8);color:#0B1433;display:flex;align-items:center;justify-content:center;cursor:pointer;text-decoration:none}
.jy-main{max-width:760px;margin:0 auto;padding:48px 24px 96px;box-sizing:border-box}
.jy-coach{display:flex;align-items:center;gap:10px;font-size:13px;font-weight:500;color:#5B6582}
.jy-av{width:32px;height:32px;border-radius:999px;flex-shrink:0;background:#FFFFFF url(MARK) center / 62% no-repeat;box-shadow:0 0 0 1.5px #DCE5FB,0 8px 18px -10px rgba(22,82,240,.5)}
.jy-h1{margin:16px 0 0;font-size:42px;line-height:1.08;font-weight:600;letter-spacing:-1.3px;color:#0B1433}
.jy-sub{margin:12px 0 0;font-size:17px;line-height:1.55;color:#4A5578}
.jy-q{margin-top:44px;display:flex;flex-direction:column;gap:14px}
.jy-ql{display:flex;align-items:baseline;justify-content:space-between;gap:12px;font-size:17px;font-weight:600;letter-spacing:-.2px;color:#0B1433}
.jy-ql em{font-style:normal;font-size:13px;font-weight:500;color:#8A93AD}
.jy-goal{height:60px;box-sizing:border-box;padding:0 20px;border-radius:16px;border:1.5px solid #D6DDEE;background:#FFFFFF;display:flex;align-items:center;gap:12px;box-shadow:0 20px 40px -32px rgba(11,20,51,.5);transition:border-color .2s ease,box-shadow .2s ease}
.jy-goal:focus-within{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.jy-goal input{flex:1;min-width:0;height:100%;border:none;outline:none;background:transparent;font-family:'Google Sans',system-ui,sans-serif;font-size:17px;color:#0B1433}
.jy-goal input::placeholder{color:#8A93AD}
.jy-sugs{display:flex;align-items:center;flex-wrap:wrap;gap:8px}
.jy-chip{height:38px;padding:0 15px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:'Google Sans',system-ui,sans-serif;font-size:14px;font-weight:500;color:#0B1433;cursor:pointer;display:inline-flex;align-items:center;gap:7px;transition:border-color .2s ease,background .2s ease}
.jy-chip:hover{border-color:#9DB8F7}
.jy-chip-on{background:#EAF0FF;border-color:#1652F0;color:#0E3BB8}
.jy-chip svg{display:none}
.jy-chip-on svg{display:block}
.jy-opts{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.jy-opt{position:relative;display:flex;align-items:center;gap:14px;min-height:60px;box-sizing:border-box;padding:14px 18px;border-radius:14px;border:1.5px solid #E3E8F3;background:#FFFFFF;text-align:left;font-family:'Google Sans',system-ui,sans-serif;cursor:pointer;transition:border-color .2s ease,background .2s ease}
.jy-opt:hover{border-color:#C9D7FA}
.jy-opt-on{background:#EAF0FF;border-color:#1652F0}
.jy-rad{width:20px;height:20px;border-radius:999px;border:1.5px solid #CBD3E6;background:#FFFFFF;box-sizing:border-box;flex-shrink:0;display:flex;align-items:center;justify-content:center;color:#FFFFFF}
.jy-opt-on .jy-rad{background:#1652F0;border-color:#1652F0}
.jy-ot{display:block;font-size:15px;font-weight:600;color:#0B1433}
.jy-err{font-size:13px;color:#B42318}
.jy-date{height:44px;box-sizing:border-box;padding:0 14px;border-radius:12px;border:1.5px solid #D6DDEE;font-family:'Google Sans',system-ui,sans-serif;font-size:15px;color:#0B1433;align-self:flex-start}
.jy-acts{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-top:48px;padding-top:24px;border-top:1px solid #EEF1F7}
.jy-acts-end{justify-content:flex-end}
.jy-back{height:52px;padding:0 20px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:'Google Sans',system-ui,sans-serif;font-size:15px;font-weight:600;color:#0B1433;cursor:pointer;display:inline-flex;align-items:center;gap:8px}
.jy-btn{box-sizing:border-box;height:56px;padding:0 8px 0 26px;border:none;border-radius:999px;background:#1652F0;color:#FFFFFF;display:inline-flex;align-items:center;gap:16px;font-family:'Google Sans',system-ui,sans-serif;font-size:16px;font-weight:600;cursor:pointer;text-decoration:none;white-space:nowrap;transition:background .2s ease}
.jy-btn:hover{background:#0E3BB8}
.jy-btn i{width:40px;height:40px;border-radius:999px;background:#FFFFFF;display:flex;align-items:center;justify-content:center}
.jy-lv{display:flex;flex-direction:column;border-radius:16px;border:1.5px solid #E6EAF3;overflow:hidden}
.jy-lr{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:12px 12px 12px 18px;background:#FFFFFF}
.jy-lr + .jy-lr{border-top:1px solid #EEF1F7}
.jy-ln2{font-size:15px;font-weight:600;color:#0B1433}
.jy-seg{display:flex;gap:2px;padding:3px;border-radius:999px;background:#F1F3F8}
.jy-seg button{height:34px;padding:0 14px;border:none;border-radius:999px;background:transparent;font-family:'Google Sans',system-ui,sans-serif;font-size:13px;font-weight:500;color:#5B6582;cursor:pointer}
.jy-seg .jy-seg-on{background:#FFFFFF;color:#0E3BB8;box-shadow:0 4px 10px -6px rgba(11,20,51,.3)}
.jy-cv{display:flex;align-items:center;gap:16px;padding:16px 18px;border-radius:16px;border:1.5px dashed #C9D7FA;background:rgba(245,248,255,.7)}
.jy-cvi{position:relative;width:44px;height:44px;border-radius:12px;background:#FFFFFF;color:#1652F0;display:flex;align-items:center;justify-content:center;flex-shrink:0;box-shadow:0 8px 18px -12px rgba(22,82,240,.6)}
.jy-cvi::after{content:"";position:absolute;inset:-1px;border-radius:13px;border:1.5px solid rgba(22,82,240,.35);animation:jyHalo 2.4s ease-out infinite;pointer-events:none}
.jy-cv-on .jy-cvi::after{display:none}
.jy-up{animation:jyUp 1.6s ease-in-out infinite}
.jy-pop{animation:jyPop .5s cubic-bezier(.2,.9,.3,1.3) both}
.jy-tick{stroke-dasharray:12;stroke-dashoffset:12;animation:jyTick .45s .2s ease-out forwards}
@keyframes jyUp{0%,100%{transform:translateY(1.5px);opacity:.55}50%{transform:translateY(-2px);opacity:1}}
@keyframes jyHalo{0%{transform:scale(1);opacity:.9}100%{transform:scale(1.35);opacity:0}}
@keyframes jyPop{from{transform:scale(.6);opacity:0}to{transform:scale(1);opacity:1}}
@keyframes jyTick{to{stroke-dashoffset:0}}
.jy-cvt{flex:1;min-width:0}
.jy-cvt b{display:flex;align-items:center;gap:8px;font-size:15px;font-weight:600;color:#0B1433}
.jy-cvt span{display:block;margin-top:2px;font-size:13px;color:#5B6582}
.jy-file{height:40px;padding:0 16px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:'Google Sans',system-ui,sans-serif;font-size:14px;font-weight:600;color:#0B1433;cursor:pointer;white-space:nowrap}
.jy-cv-on{border-style:solid;border-color:#BFE3CF;background:#F3FBF6}
.jy-cv-on .jy-cvi{color:#0F6B45}
.jy-build{max-width:640px;margin:0 auto;padding:64px 24px 96px;box-sizing:border-box;display:flex;flex-direction:column;align-items:center;text-align:center}
.jy-ring{position:relative;width:112px;height:112px}
.jy-ring svg{position:absolute;inset:0;transform:rotate(-90deg)}
.jy-ring-c{position:absolute;inset:22px;border-radius:999px;background:#FFFFFF url(MARK) center / 56% no-repeat;box-shadow:0 0 0 1.5px #DCE5FB,0 20px 40px -20px rgba(22,82,240,.6)}
.jy-arc{transition:stroke-dashoffset .6s cubic-bezier(.2,.7,.2,1)}
.jy-bh{margin:28px 0 0;font-size:34px;line-height:1.12;font-weight:600;letter-spacing:-1px;color:#0B1433}
.jy-bs{margin:10px 0 0;font-size:16px;line-height:1.55;color:#4A5578}
.jy-list{width:fit-content;max-width:100%;margin:36px auto 0;padding:0;list-style:none;display:flex;flex-direction:column;gap:0;text-align:left}
.jy-li{position:relative;display:flex;align-items:center;gap:14px;min-height:46px;font-size:15px;font-weight:500;color:#8A93AD;transition:color .3s ease}
.jy-li:not(:last-child)::before{content:"";position:absolute;left:11px;top:34px;bottom:-12px;width:2px;background:#E6EAF3}
.jy-li-done:not(:last-child)::before{background:#1652F0}
.jy-dot{position:relative;z-index:1;width:24px;height:24px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;box-sizing:border-box;flex-shrink:0;display:flex;align-items:center;justify-content:center;color:#FFFFFF}
.jy-li-done{color:#0B1433}
.jy-li-done .jy-dot{background:#1652F0;border-color:#1652F0}
.jy-li-now{color:#0B1433;font-weight:600}
.jy-li-now .jy-dot{border-color:#1652F0;border-top-color:transparent;animation:jySpin .9s linear infinite}
.jy-shim{background:linear-gradient(90deg,#0B1433 0%,#0B1433 40%,#9DB8F7 50%,#0B1433 60%,#0B1433 100%);background-size:220% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:jyShim 1.6s linear infinite}
@keyframes jySpin{to{transform:rotate(360deg)}}
@keyframes jyShim{from{background-position:120% 0}to{background-position:-120% 0}}
.jy-ready{max-width:960px;margin:0 auto;padding:56px 24px 96px;box-sizing:border-box;display:flex;flex-direction:column;align-items:center;text-align:center;position:relative}
.jy-ok{position:relative;width:56px;height:56px;border-radius:999px;background:#E7F5EE;color:#0F6B45;display:flex;align-items:center;justify-content:center}
.jy-rh{position:relative;margin:20px 0 0;font-size:42px;line-height:1.08;font-weight:600;letter-spacing:-1.3px;color:#0B1433}
.jy-rs{position:relative;margin:12px 0 0;font-size:17px;line-height:1.55;color:#4A5578}
.jy-jc{position:relative;isolation:isolate;overflow:hidden;width:100%;margin-top:36px;padding:32px 36px 34px;border-radius:24px;background:#0B1433;color:#FFFFFF;box-sizing:border-box;text-align:left;box-shadow:0 40px 80px -48px rgba(11,20,51,.7)}
.jy-jc::after{content:"";position:absolute;inset:0;z-index:-1;background:#0B1433 url(/_blob/3d4d999db1912d0cb0084365c58434d3) center / cover no-repeat;transform:scale(1.5);transform-origin:0 35%;pointer-events:none}
.jy-jh{display:flex;align-items:flex-end;justify-content:space-between;gap:24px;flex-wrap:wrap}
.jy-jk{display:block;font-size:13px;font-weight:500;color:#9DB8F7}
.jy-jt{display:block;margin-top:4px;font-size:32px;font-weight:600;letter-spacing:-.8px;line-height:1.1}
.jy-jm{display:flex;gap:8px;flex-wrap:wrap}
.jy-jm > span{height:36px;padding:0 14px 0 11px;border-radius:999px;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.16);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);display:inline-flex;align-items:center;gap:8px;font-size:14px;font-weight:500;white-space:nowrap}
.jy-jr{position:relative;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));margin:34px 0 0;padding:0;list-style:none}
.jy-jr::before{content:"";position:absolute;left:10%;right:10%;top:17px;height:2px;background:linear-gradient(90deg,#FFFFFF,rgba(157,184,247,.5))}
.jy-js{position:relative;display:flex;flex-direction:column;align-items:center;gap:6px;text-align:center}
.jy-jn{width:36px;height:36px;border-radius:999px;background:#14286E;border:2px solid rgba(157,184,247,.7);color:#C9D7FA;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:600;box-sizing:border-box;margin-bottom:6px}
.jy-js:first-child .jy-jn{background:#FFFFFF;border-color:#FFFFFF;color:#1652F0;box-shadow:0 0 0 6px rgba(255,255,255,.16)}
.jy-js:last-child .jy-jn{background:#FFFFFF;border-color:#FFFFFF;color:#0B1433}
.jy-jl{font-size:15px;font-weight:600}
.jy-jd{font-size:12px;color:rgba(255,255,255,.65)}
.jy-here{margin-top:4px;height:22px;padding:0 9px;border-radius:999px;background:#FFFFFF;color:#1652F0;display:inline-flex;align-items:center;font-size:11px;font-weight:600}
.jy-cta{position:relative;margin-top:32px;display:flex;flex-direction:column;align-items:center;gap:14px}
.jy-link{font-size:14px;font-weight:600;color:#1652F0;text-decoration:none;background:none;border:none;cursor:pointer;font-family:'Google Sans',system-ui,sans-serif;min-height:44px}
.jy-cf{position:absolute;width:8px;height:12px;border-radius:2px;top:0;opacity:0;animation:jyConf 2.4s cubic-bezier(.2,.7,.2,1) .2s 1 both}
@keyframes jyConf{0%{opacity:0;transform:translate(0,0) rotate(0)}12%{opacity:1}100%{opacity:0;transform:translate(var(--dx),var(--dy)) rotate(var(--r))}}
.jy-opt:focus-visible,.jy-chip:focus-visible,.jy-btn:focus-visible,.jy-back:focus-visible,.jy-seg button:focus-visible,.jy-file:focus-visible,.jy-x:focus-visible,.jy-link:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:3px}
@media (prefers-reduced-motion: reduce){.jy-li-now .jy-dot,.jy-shim,.jy-cf,.jy-up,.jy-cvi::after,.jy-pop{animation:none}.jy-tick{animation:none;stroke-dashoffset:0}.jy-shim{color:#0B1433;background:none}}
@media (max-width: 760px){
.jy-page{background-size:auto 300px}
.jy-bar{height:60px;padding:0 16px;grid-template-columns:auto 1fr auto}
.jy-bar .sx-word{display:none}
.jy-steps{justify-content:center}
.jy-st > span{display:none}
.jy-ln{width:22px;margin:0 6px}
.jy-login{display:none}
.jy-x{width:40px;height:40px}
.jy-main{padding:32px 20px 0}
.jy-h1{font-size:28px;letter-spacing:-.8px;margin-top:14px}
.jy-sub{font-size:15px;margin-top:10px}
.jy-q{margin-top:36px;gap:12px}
.jy-ql{font-size:16px}
.jy-goal{height:54px;padding:0 16px;border-radius:14px}
.jy-goal input{font-size:16px}
.jy-sugs{flex-wrap:nowrap;overflow-x:auto;margin:0 -20px;padding:0 20px;scrollbar-width:none}
.jy-sugs::-webkit-scrollbar{display:none}
.jy-chip{flex-shrink:0;height:38px;font-size:14px}
.jy-row{flex-wrap:nowrap !important;overflow-x:auto;margin:0 -20px !important;padding:0 20px !important;scrollbar-width:none}
.jy-row::-webkit-scrollbar{display:none}
.jy-opts{grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.jy-opt{padding:12px;gap:10px;min-height:64px;align-items:flex-start}
.jy-opt .jy-rad{margin-top:1px}
.jy-ot{font-size:14px;line-height:1.3}
.jy-acts{position:sticky;bottom:0;z-index:10;margin:40px -20px 0;padding:12px 16px;border-top:1px solid #E6EAF3;background:rgba(255,255,255,.94);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px)}
.jy-acts .jy-btn{flex:1;justify-content:space-between;height:52px}
.jy-acts .jy-btn i{width:38px;height:38px}
.jy-back{height:52px;width:52px;padding:0;justify-content:center}
.jy-back span{display:none}
.jy-lr{flex-direction:column;align-items:stretch;gap:10px;padding:14px}
.jy-seg button{flex:1}
.jy-cv{flex-wrap:wrap;padding:14px;gap:12px}
.jy-cvi{width:40px;height:40px}
.jy-build{padding:40px 20px 72px}
.jy-ring{width:96px;height:96px}
.jy-ring-c{inset:18px}
.jy-bh{font-size:24px;letter-spacing:-.6px;margin-top:24px}
.jy-bs{font-size:15px}
.jy-list{margin-top:28px}
.jy-li{font-size:14px;min-height:44px}
.jy-ready{padding:40px 20px 0}
.jy-ok{width:48px;height:48px}
.jy-rh{font-size:28px;letter-spacing:-.8px;margin-top:16px}
.jy-rs{font-size:15px}
.jy-jc{margin-top:28px;padding:22px 20px 20px;border-radius:20px}
.jy-jh{flex-direction:column;align-items:flex-start;gap:14px}
.jy-jt{font-size:24px;letter-spacing:-.5px}
.jy-jm > span{height:32px;font-size:13px}
.jy-jr{grid-template-columns:minmax(0,1fr);margin-top:22px}
.jy-jr::before{display:none}
.jy-js{display:grid;grid-template-columns:32px minmax(0,1fr) auto;align-items:center;column-gap:12px;text-align:left;padding-bottom:16px}
.jy-js:not(:last-child)::after{content:"";position:absolute;left:15px;top:32px;bottom:0;width:2px;background:rgba(157,184,247,.45)}
.jy-js:last-child{padding-bottom:0}
.jy-jn{width:32px;height:32px;margin:0;font-size:12px}
.jy-jl{font-size:14px}
.jy-jd{grid-column:3;font-size:12px}
.jy-here{grid-column:2;grid-row:2;justify-self:start;margin-top:4px}
.jy-cta{position:sticky;bottom:0;z-index:10;align-self:stretch;margin:28px -20px 0;padding:12px 16px 14px;box-sizing:border-box;border-top:1px solid #E6EAF3;background:rgba(255,255,255,.94);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px);gap:4px}
.jy-cta .jy-btn{width:100%;justify-content:space-between;height:52px}
.jy-cta .jy-link{min-height:40px}
}
'''.replace('CLOUD',CLOUD).replace('MARK',MARK)
ARR=ARROW%(16,16,'#1652F0')
XIC='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"></path></svg>'
BACK='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M11 6l-6 6 6 6"></path></svg>'
body='''<div class="jy-page">
<header class="jy-bar">
<a class="sx-logo" href="#" aria-label="Credalio home"><span class="sx-mark" aria-hidden="true"></span><span class="sx-word" aria-hidden="true"></span></a>
<div class="jy-steps" aria-label="Progress">
<span class="jy-st {{s1}}"><i>{{n1}}</i><span>Your goal</span></span><b class="jy-ln {{l1}}"></b>
<span class="jy-st {{s2}}"><i>{{n2}}</i><span>What you know</span></span><b class="jy-ln {{l2}}"></b>
<span class="jy-st {{s3}}"><i>3</i><span>Your journey</span></span>
</div>
<div class="jy-right"><a class="jy-login" href="#">Log in</a><sc-if value="{{canClose}}" hint-placeholder-val="{{ true }}"><a class="jy-x" href="#" aria-label="Leave and go back">%(x)s</a></sc-if></div>
</header>

<sc-if value="{{isGoal}}" hint-placeholder-val="{{ true }}">
<main class="jy-main">
<div class="jy-coach"><span class="jy-av" aria-hidden="true"></span>Your AI Coach</div>
<h1 class="jy-h1">Let’s see where you’re starting from.</h1>
<p class="jy-sub">Four quick answers, then I build your journey.</p>
<div class="jy-q">
<label class="jy-ql" for="jy-goal">Who do you want to become?</label>
<div class="jy-goal"><input id="jy-goal" type="text" placeholder="I want to become…" value="{{goalText}}" onInput="{{onGoal}}" autocomplete="off"></div>
<div class="jy-sugs"><sc-for list="{{sugs}}" as="c" hint-placeholder-count="4"><button class="jy-chip {{c.cls}}" type="button" aria-pressed="{{c.on}}" onClick="{{c.pick}}">%(ck)s{{c.label}}</button></sc-for></div>
</div>
<div class="jy-q" role="radiogroup" aria-labelledby="jy-lvl">
<span class="jy-ql" id="jy-lvl">Where are you starting from?</span>
<div class="jy-opts">
<sc-for list="{{levels}}" as="o" hint-placeholder-count="4"><button class="jy-opt {{o.cls}}" type="button" role="radio" aria-checked="{{o.on}}" onClick="{{o.pick}}"><span class="jy-rad">%(ck11)s</span><span class="jy-ot">{{o.title}}</span></button></sc-for>
</div>
<sc-if value="{{showErr}}" hint-placeholder-val="{{ false }}"><span class="jy-err" role="alert">{{errText}}</span></sc-if>
</div>
<div class="jy-q">
<span class="jy-ql">What do you want from it?<em>Choose any</em></span>
<div class="jy-sugs jy-row" style="flex-wrap: wrap; margin: 0; padding: 0"><sc-for list="{{aims}}" as="a" hint-placeholder-count="6"><button class="jy-chip {{a.cls}}" type="button" aria-pressed="{{a.on}}" onClick="{{a.pick}}">%(ck)s{{a.label}}</button></sc-for></div>
</div>
<div class="jy-q">
<span class="jy-ql">How soon would you like to get there?</span>
<div class="jy-sugs jy-row" style="flex-wrap: wrap; margin: 0; padding: 0"><sc-for list="{{paces}}" as="p" hint-placeholder-count="5"><button class="jy-chip {{p.cls}}" type="button" aria-pressed="{{p.on}}" onClick="{{p.pick}}">%(ck)s{{p.label}}</button></sc-for></div>
<sc-if value="{{pickDate}}" hint-placeholder-val="{{ false }}"><input class="jy-date" type="date" aria-label="Target date"></sc-if>
</div>
<div class="jy-acts jy-acts-end"><button class="jy-btn" type="button" onClick="{{toKnow}}">Continue<i aria-hidden="true">%(arr)s</i></button></div>
</main>
</sc-if>

<sc-if value="{{isKnow}}" hint-placeholder-val="{{ false }}">
<main class="jy-main">
<div class="jy-coach"><span class="jy-av" aria-hidden="true"></span>Your AI Coach</div>
<h1 class="jy-h1">You may be closer than you think.</h1>
<p class="jy-sub">Tell me what you already know, so I only add learning you need.</p>
<div class="jy-q">
<span class="jy-ql"><span>Skills for becoming {{roleA}}</span><em>Choose any</em></span>
<div class="jy-sugs" style="flex-wrap: wrap; margin: 0; padding: 0"><sc-for list="{{skills}}" as="k" hint-placeholder-count="8"><button class="jy-chip {{k.cls}}" type="button" aria-pressed="{{k.on}}" onClick="{{k.pick}}">%(ck)s{{k.label}}</button></sc-for></div>
</div>
<sc-if value="{{hasSkills}}" hint-placeholder-val="{{ true }}">
<div class="jy-q">
<span class="jy-ql">How well do you know them?</span>
<div class="jy-lv">
<sc-for list="{{rows}}" as="r" hint-placeholder-count="2"><div class="jy-lr"><span class="jy-ln2">{{r.name}}</span><div class="jy-seg" role="group" aria-label="{{r.name}} level"><sc-for list="{{r.levels}}" as="l" hint-placeholder-count="3"><button type="button" class="{{l.cls}}" aria-pressed="{{l.on}}" onClick="{{l.pick}}">{{l.label}}</button></sc-for></div></div></sc-for>
</div>
</div>
</sc-if>
<div class="jy-q">
<div class="jy-cv {{cvCls}}">
<span class="jy-cvi" aria-hidden="true"><sc-if value="{{noCv}}" hint-placeholder-val="{{ true }}"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"></path><path d="M14 3v5h5"></path><g class="jy-up"><path d="M12 18v-6M9 15l3-3 3 3"></path></g></svg></sc-if><sc-if value="{{hasCv}}" hint-placeholder-val="{{ false }}"><svg class="jy-pop" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"></path><path d="M14 3v5h5"></path><path class="jy-tick" d="M8.5 14.5l2.5 2.5 4.5-5"></path></svg></sc-if></span>
<span class="jy-cvt"><b>{{cvTitle}}<sc-if value="{{noCv}}" hint-placeholder-val="{{ true }}"><i class="sx-tip" tabindex="0" data-tip="Your AI Coach reads your experience to set a fairer starting point. Only you can see it.">i</i></sc-if></b><span>{{cvSub}}</span></span>
<button class="jy-file" type="button" onClick="{{toggleCv}}">{{cvBtn}}</button>
</div>
</div>
<div class="jy-acts"><button class="jy-back" type="button" onClick="{{toGoal}}">%(back)s<span>Back</span></button><button class="jy-btn" type="button" onClick="{{toBuild}}">Build my journey<i aria-hidden="true">%(arr)s</i></button></div>
</main>
</sc-if>

<sc-if value="{{isBuild}}" hint-placeholder-val="{{ false }}">
<main class="jy-build" aria-live="polite">
<div class="jy-ring" aria-hidden="true"><svg viewBox="0 0 112 112" width="100%%" height="100%%"><circle cx="56" cy="56" r="52" fill="none" stroke="#E6EAF3" stroke-width="4"></circle><circle class="jy-arc" cx="56" cy="56" r="52" fill="none" stroke="#1652F0" stroke-width="4" stroke-linecap="round" stroke-dasharray="326.7" style="stroke-dashoffset: {{arc}}"></circle></svg><span class="jy-ring-c"></span></div>
<h1 class="jy-bh">Building your journey to becoming {{roleA}}</h1>
<ol class="jy-list">
<sc-for list="{{stages}}" as="g" hint-placeholder-count="6"><li class="jy-li {{g.cls}}"><span class="jy-dot">%(ck11)s</span><span class="{{g.tcls}}">{{g.label}}</span></li></sc-for>
</ol>
</main>
</sc-if>

<sc-if value="{{isReady}}" hint-placeholder-val="{{ false }}">
<main class="jy-ready">
<span aria-hidden="true">%(conf)s</span>
<span class="jy-ok" aria-hidden="true"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg></span>
<h1 class="jy-rh">Your journey is ready.</h1>
<p class="jy-rs">Built around your goal, what you already know and the outcome you want.</p>
<div class="jy-jc">
<div class="jy-jh"><div><span class="jy-jk">Your journey to becoming</span><span class="jy-jt">{{roleT}}</span></div><div class="jy-jm"><span><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="M12 7v5l3 2"></path></svg>{{time}}</span><span><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="3"></rect><path d="M8 3v4M16 3v4M3 10h18"></path></svg>{{commit}} hrs a week</span></div></div>
<ol class="jy-jr" aria-label="Your five steps">
<sc-for list="{{route}}" as="r" hint-placeholder-count="5"><li class="jy-js"><span class="jy-jn">{{r.mark}}</span><span class="jy-jl">{{r.label}}</span><span class="jy-jd">{{r.note}}</span><sc-if value="{{r.first}}" hint-placeholder-val="{{ false }}"><span class="jy-here">You start here</span></sc-if></li></sc-for>
</ol>
</div>
<div class="jy-cta"><a class="jy-btn" href="#">View my journey<i aria-hidden="true">%(arr)s</i></a><button class="jy-link" type="button" onClick="{{toGoal}}">Change my answers</button></div>
</main>
</sc-if>
</div>'''
import random
random.seed(7)
cols=['#1652F0','#9DB8F7','#1E9E63','#F4D98E','#0B1433']
conf=''.join('<i class="jy-cf" style="left: %d%%; background: %s; --dx: %dpx; --dy: %dpx; --r: %ddeg; animation-delay: %.2fs"></i>'%(random.randint(10,90),cols[k%5],random.randint(-160,160),random.randint(120,320),random.randint(-300,300),random.random()*.4) for k in range(22))
body=body%dict(x=XIC,ck=CK%(13,13),ck11=CK%(11,11),arr=ARR,back=BACK,conf=conf)
script=r'''
class Component extends DCLogic {
  constructor(props) {
    super(props);
    var st = (props && props.step) || 'goal';
    if (st === 'building') st = 'build';
    var pre = st !== 'goal';
    this.state = { step: st, goalText: 'I want to become a data analyst', goalKey: 'data', level: pre ? 'related' : '', aims: pre ? { 'Change careers': true } : {}, pace: pre ? '3–6 months' : '', showErr: false,
      skills: (st === 'know' || pre) ? { Excel: 'Comfortable', SQL: 'Basic' } : {}, none: false, cv: false, buildStep: st === 'build' ? 3 : (st === 'ready' ? 6 : 0) };
    this.G = {
      data: { chip: 'Data analyst', title: 'Data Analyst', a: 'a data analyst', text: 'I want to become a data analyst', skills: ['Excel', 'SQL', 'Python', 'Statistics', 'Power BI', 'Tableau', 'Data cleaning'], core: 'SQL' },
      design: { chip: 'Product designer', title: 'Product Designer', a: 'a product designer', text: 'I want to become a product designer', skills: ['Figma', 'User research', 'Wireframing', 'Prototyping', 'Visual design', 'Usability testing', 'Design systems'], core: 'Figma' },
      cyber: { chip: 'Cybersecurity analyst', title: 'Cybersecurity Analyst', a: 'a cybersecurity analyst', text: 'I want to become a cybersecurity analyst', skills: ['Networking', 'Linux', 'Security basics', 'SIEM tools', 'Scripting', 'Incident response', 'Risk assessment'], core: 'Networking' },
      pm: { chip: 'Project manager', title: 'Project Manager', a: 'a project manager', text: 'I want to become a project manager', skills: ['Planning', 'Agile', 'Stakeholders', 'Risk', 'Budgeting', 'Jira', 'Reporting'], core: 'Agile' }
    };
  }
  componentWillUnmount() { if (this.timer) clearInterval(this.timer); }
  run(from) {
    var self = this, n = from || 0;
    if (this.timer) clearInterval(this.timer);
    this.setState({ step: 'build', buildStep: n });
    this.timer = setInterval(function () {
      n++; self.setState({ buildStep: n });
      if (n >= 6) { clearInterval(self.timer); self.timer = null; setTimeout(function () { self.setState({ step: 'ready' }); }, 700); }
    }, 750);
  }
  keyFor(t) { t = (t || '').toLowerCase(); if (/data\s*analy/.test(t)) return 'data'; if (/product\s*design|ux|ui\s*design/.test(t)) return 'design'; if (/cyber|security/.test(t)) return 'cyber'; if (/project\s*manag/.test(t)) return 'pm'; return ''; }
  renderVals() {
    var self = this, S = this.state, G = this.G, set = function (p) { self.setState(p); };
    var g = G[S.goalKey];
    if (!g) { var c = (S.goalText || '').replace(/^\s*i\s+(want|would\s+like)\s+to\s+(become|be)\s+/i, '').replace(/^(a|an)\s+/i, '').trim(); g = { a: c ? ((/^[aeiou]/i.test(c) ? 'an ' : 'a ') + c) : 'your goal', skills: ['Industry tools', 'Communication', 'Problem solving', 'Project work'], core: '' }; }
    var chk = function (on) { return on ? 'jy-chip-on' : ''; };
    var lv = [['new', 'I’m completely new', 'I haven’t studied or worked in this area.'], ['basics', 'I know the basics', 'I’ve already done some learning.'], ['related', 'I have related experience', 'Transferable skills from other work.'], ['working', 'I already work in this area', 'I want to advance or specialise.']];
    var sel = g.skills.filter(function (k) { return !!S.skills[k]; });
    var strong = sel.filter(function (k) { return S.skills[k] !== 'Basic'; }).length;
    var base = { 'new': [4, 6], basics: [3, 5], related: [3, 4], working: [2, 3] }[S.level || 'new'], lo = base[0], hi = base[1];
    if (strong >= 2) { lo = Math.max(1, lo - 1); hi = Math.max(lo + 1, hi - 1); }
    var commit = { 'No deadline': 5, '1–3 months': 10, '3–6 months': 6, '6–12 months': 4, 'Pick a date': 6 }[S.pace] || 5;
    var stageLabels = ['Understanding your goal', 'Reviewing the skills you have', 'Finding the gaps', 'Choosing trusted, validated learning', 'Adding practice and proof', 'Putting your journey together'];
    var step = S.step, idx = { goal: 1, know: 2, build: 3, ready: 3 }[step];
    return {
      canClose: step !== 'ready', isGoal: step === 'goal', isKnow: step === 'know', isBuild: step === 'build', isReady: step === 'ready',
      s1: idx > 1 ? 'jy-st-done' : 'jy-st-on', s2: idx > 2 ? 'jy-st-done' : (idx === 2 ? 'jy-st-on' : ''), s3: idx === 3 ? (step === 'ready' ? 'jy-st-done' : 'jy-st-on') : '',
      n1: idx > 1 ? '✓' : '1', n2: idx > 2 ? '✓' : '2', l1: idx > 1 ? 'jy-ln-on' : '', l2: idx > 2 ? 'jy-ln-on' : '',
      goalText: S.goalText, onGoal: function (e) { var v = e.target.value; set({ goalText: v, goalKey: self.keyFor(v), skills: {} }); },
      sugs: Object.keys(G).map(function (k) { var on = S.goalKey === k; return { label: G[k].chip, on: on ? 'true' : 'false', cls: chk(on), pick: function () { set({ goalKey: k, goalText: G[k].text, skills: {} }); } }; }),
      levels: lv.map(function (l) { var on = S.level === l[0]; return { title: l[1], desc: l[2], on: on ? 'true' : 'false', cls: on ? 'jy-opt-on' : '', pick: function () { set({ level: l[0], showErr: false }); } }; }),
      showErr: S.showErr, errText: !S.goalText.trim() ? 'Tell me who you want to become first.' : 'Choose where you’re starting from.',
      aims: ['Get my first job', 'Change careers', 'Grow in my current role', 'Earn a recognised credential'].map(function (a) { var on = !!S.aims[a]; return { label: a, on: on ? 'true' : 'false', cls: chk(on), pick: function () { var n = Object.assign({}, S.aims); if (on) delete n[a]; else n[a] = true; set({ aims: n }); } }; }),
      paces: ['No deadline', '1–3 months', '3–6 months', '6–12 months', 'Pick a date'].map(function (p) { var on = S.pace === p; return { label: p, on: on ? 'true' : 'false', cls: chk(on), pick: function () { set({ pace: p }); } }; }),
      pickDate: S.pace === 'Pick a date',
      toKnow: function () { if (!S.goalText.trim() || !S.level) { set({ showErr: true }); return; } set({ step: 'know', showErr: false }); },
      roleA: g.a,
      skills: g.skills.map(function (k) { var on = !!S.skills[k]; return { label: k, on: on ? 'true' : 'false', cls: chk(on), pick: function () { var n = Object.assign({}, S.skills); if (on) delete n[k]; else n[k] = 'Basic'; set({ skills: n, none: false }); } }; }),
      hasSkills: sel.length > 0,
      rows: sel.map(function (k) { return { name: k, levels: ['Basic', 'Comfortable', 'Advanced'].map(function (l) { var on = S.skills[k] === l; return { label: l, on: on ? 'true' : 'false', cls: on ? 'jy-seg-on' : '', pick: function () { var n = Object.assign({}, S.skills); n[k] = l; set({ skills: n }); } }; }) }; }),
      cvCls: S.cv ? 'jy-cv-on' : '', noCv: !S.cv, hasCv: S.cv, cvTitle: S.cv ? 'Maya_Rahman_CV.pdf' : 'Add your CV', cvSub: S.cv ? 'Added. Your AI Coach will read it.' : 'Optional. PDF or Word, up to 5 MB.', cvBtn: S.cv ? 'Remove' : 'Choose file', toggleCv: function () { set({ cv: !S.cv }); },
      toGoal: function () { if (self.timer) clearInterval(self.timer); set({ step: 'goal' }); },
      toBuild: function () { self.run(0); },
      arc: (326.7 * (1 - Math.min(6, S.buildStep) / 6)).toFixed(1),
      stages: stageLabels.map(function (l, i) { var done = i < S.buildStep, now = i === S.buildStep && S.buildStep < 6; return { label: l, cls: done ? 'jy-li-done' : (now ? 'jy-li-now' : ''), tcls: now ? 'jy-shim' : '' }; }),
      time: lo + '–' + hi + ' months', commit: commit,
      roleT: g.title || g.a.replace(/^(a|an) /, '').replace(/\b\w/g, function (c) { return c.toUpperCase(); }),
      route: [['Foundation', '2 courses'], ['Core skills', '3 courses'], ['Practice', '2 projects'], ['Certification', '1 exam'], ['Job-ready', 'Your portfolio']].map(function (r, i) { return { mark: i === 4 ? '✓' : i + 1, label: r[0], note: r[1], first: i === 0 }; })
    };
  }
}
'''
open('/home/user/credalio/design/canvas3/project/Journey.dc.html','w').write(page('Start Your Journey',css,'',body,script,1400,'"step":{"editor":"enum","options":["goal","know","building","ready"],"default":"goal"},'))
