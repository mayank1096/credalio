from shell import *
import re
CLOUD='/_blob/020f1a8593e80e5fcee9e0f06637f153'; MARK='/_blob/f81e36d31295a0d0737959589ec1abd4'; WAVE='/_blob/3d4d999db1912d0cb0084365c58434d3'
import os
COIN=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'coin.css')).read()
CK='<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg>'
ARR=ARROW%(16,16,'#1652F0')
css=COIN+r'''
.jp-page{min-height:100%;overflow-x:clip;background:#FFFFFF url(CLOUD) center top / max(1440px,100%) auto no-repeat}
.jp-bar{max-width:1360px;margin:0 auto;height:72px;padding:0 24px;box-sizing:border-box;display:flex;align-items:center;justify-content:space-between;gap:16px}
.jp-right{display:flex;align-items:center;gap:10px}
.jp-login{height:40px;padding:0 12px;border-radius:999px;display:flex;align-items:center;font-size:15px;font-weight:600;color:#0B1433;text-decoration:none}
.jp-pill{height:36px;padding:0 12px 0 8px;border-radius:999px;background:rgba(255,255,255,.85);border:1px solid #DCE5FB;display:inline-flex;align-items:center;gap:8px;font-size:14px;font-weight:600;color:#0B1433;white-space:nowrap}
.jp-me{width:40px;height:40px;border-radius:999px;background:#DCE5FB;color:#1652F0;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:600}
.jp-wrap{max-width:1312px;margin:0 auto;padding:32px 48px 96px;box-sizing:border-box;display:grid;grid-template-columns:minmax(0,1fr) 380px;gap:0 56px;align-items:start}
.jp-main{min-width:0}
.jp-save{display:flex;align-items:center;justify-content:space-between;gap:20px;padding:16px 16px 16px 20px;border-radius:18px;background:rgba(255,255,255,.88);border:1px solid #DCE5FB;box-shadow:0 20px 44px -36px rgba(22,82,240,.6);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px)}
.jp-save b{display:block;font-size:15px;font-weight:600;color:#0B1433}
.jp-save span{display:block;margin-top:2px;font-size:13px;color:#5B6582}
.jp-ok{display:flex;align-items:center;justify-content:space-between;gap:20px;padding:16px 16px 16px 20px;border-radius:18px;background:#F3FBF6;border:1px solid #BFE3CF}
.jp-ok > div{display:flex;align-items:center;gap:12px}
.jp-okc{width:34px;height:34px;border-radius:999px;background:#0F6B45;color:#FFFFFF;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.jp-ok b{display:block;font-size:15px;font-weight:600;color:#0B1433}
.jp-ok > div > div > span{display:block;margin-top:2px;font-size:13px;color:#3A4566}
.jp-btn{box-sizing:border-box;height:52px;padding:0 6px 0 22px;border:none;border-radius:999px;background:#1652F0;color:#FFFFFF;display:inline-flex;align-items:center;gap:14px;font-family:'Google Sans',system-ui,sans-serif;font-size:15px;font-weight:600;cursor:pointer;text-decoration:none;white-space:nowrap;flex-shrink:0;transition:background .2s ease}
.jp-btn:hover{background:#0E3BB8}
.jp-btn i{width:40px;height:40px;border-radius:999px;background:#FFFFFF;display:flex;align-items:center;justify-content:center}
.jp-head{margin-top:36px}
.jp-k{font-size:14px;font-weight:500;color:#1652F0}
.jp-h1{margin:8px 0 0;font-size:44px;line-height:1.06;font-weight:600;letter-spacing:-1.4px;color:#0B1433}
.jp-stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));margin-top:20px;border-radius:16px;background:rgba(255,255,255,.85);border:1px solid #E3E8F3}
.jp-sv{display:flex;flex-direction:column;gap:3px;padding:14px 18px;transition:background .4s ease}
.jp-sv + .jp-sv{border-left:1px solid #EEF1F7}
.jp-sv > span{font-size:12px;font-weight:500;color:#8A93AD}
.jp-sv b{font-size:17px;font-weight:600;letter-spacing:-.2px;color:#0B1433}
.jp-sv-up b{color:#1652F0}
.jp-steps{margin-top:40px;display:flex;flex-direction:column;gap:16px}
.jp-st{position:relative;display:grid;grid-template-columns:44px minmax(0,1fr);gap:18px}
.jp-st:not(:last-child)::before{content:"";position:absolute;left:21px;top:44px;bottom:-16px;width:2px;background:#C9D7FA}
.jp-n{position:relative;z-index:1;width:44px;height:44px;border-radius:999px;background:#FFFFFF;border:2px solid #1652F0;color:#1652F0;display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:600;box-sizing:border-box}
.jp-st:first-child .jp-n{background:#1652F0;color:#FFFFFF;box-shadow:0 0 0 6px rgba(22,82,240,.12)}
.jp-st:last-child .jp-n{background:#0B1433;border-color:#0B1433;color:#FFFFFF}
.jp-sl{display:flex;align-items:center;gap:10px;height:44px;font-size:14px;font-weight:600;color:#0B1433}
.jp-sl em{font-style:normal;font-weight:500;color:#8A93AD}
.jp-up{height:24px;padding:0 9px;border-radius:999px;background:#EAF0FF;color:#1652F0;display:inline-flex;align-items:center;gap:5px;font-size:12px;font-weight:500}
.jp-card{margin-top:4px;padding:18px 20px;border-radius:18px;background:#FFFFFF;border:1.5px solid #E6EAF3;transition:border-color .4s ease,box-shadow .4s ease}
.jp-card-up{border-color:#1652F0;box-shadow:0 0 0 5px rgba(22,82,240,.08)}
.jp-ch{display:flex;align-items:flex-start;justify-content:space-between;gap:16px}
.jp-tag{height:24px;padding:0 9px;border-radius:999px;display:inline-flex;align-items:center;font-size:12px;font-weight:500}
.jp-t{display:flex;align-items:center;gap:8px;margin-top:10px;font-size:18px;font-weight:600;letter-spacing:-.3px;color:#0B1433}
.jp-m{margin-top:3px;font-size:13px;color:#5B6582}
.jp-d{margin:8px 0 0;font-size:14px;line-height:1.55;color:#3A4566;text-wrap:pretty}
.jp-a{font-size:14px;font-weight:600;color:#1652F0;text-decoration:none;white-space:nowrap}
.jp-list{margin:4px 0 0;padding:0;list-style:none;border-radius:18px;background:#FFFFFF;border:1.5px solid #E6EAF3;overflow:hidden;transition:border-color .4s ease}
.jp-li{box-sizing:border-box;display:flex;align-items:center;gap:14px;min-height:56px;padding:8px 18px}
.jp-li + .jp-li{border-top:1px solid #EEF1F7}
.jp-lk{width:30px;height:30px;border-radius:9px;background:#EAF0FF;color:#1652F0;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;flex-shrink:0}
.jp-lt{flex:1;min-width:0;font-size:15px;font-weight:500;color:#0B1433}
.jp-lm{font-size:12px;color:#8A93AD;white-space:nowrap}
.jp-new{height:22px;padding:0 8px;border-radius:999px;background:#EAF0FF;color:#1652F0;display:inline-flex;align-items:center;font-size:11px;font-weight:600}
.jp-proof{position:relative;isolation:isolate;overflow:hidden;margin-top:4px;padding:20px 22px;border-radius:18px;background:#0B1433;color:#FFFFFF}
.jp-proof::after{content:"";position:absolute;inset:0;z-index:-1;background:#0B1433 url(WAVE) center / cover no-repeat;transform:scale(1.5);transform-origin:0 35%;pointer-events:none}
.jp-pt{font-size:18px;font-weight:600;letter-spacing:-.3px}
.jp-pd{margin-top:3px;font-size:13px;color:rgba(255,255,255,.7)}
.jp-pg{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.jp-pg span{height:32px;padding:0 12px;border-radius:999px;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.16);display:inline-flex;align-items:center;gap:7px;font-size:13px;font-weight:500}
.jp-side{position:sticky;top:24px}
.jp-coach{display:flex;flex-direction:column;border-radius:22px;background:#FFFFFF;border:1px solid #E3E8F3;box-shadow:0 40px 80px -52px rgba(11,20,51,.5);overflow:hidden}
.jp-chd{display:flex;align-items:center;gap:12px;padding:18px 20px;border-bottom:1px solid #EEF1F7}
.jp-av{width:36px;height:36px;border-radius:999px;flex-shrink:0;background:#FFFFFF url(MARK) center / 62% no-repeat;box-shadow:0 0 0 1.5px #DCE5FB}
.jp-chd b{display:block;font-size:15px;font-weight:600;color:#0B1433}
.jp-chd span{display:block;font-size:12px;color:#8A93AD}
.jp-msgs{display:flex;flex-direction:column;gap:10px;padding:18px 20px;max-height:360px;overflow-y:auto}
.jp-ai{align-self:flex-start;max-width:92%;padding:11px 14px;border-radius:16px 16px 16px 4px;background:#F5F8FF;font-size:14px;line-height:1.5;color:#0B1433;text-wrap:pretty}
.jp-you{align-self:flex-end;max-width:85%;padding:10px 14px;border-radius:16px 16px 4px 16px;background:#0B1433;color:#FFFFFF;font-size:14px;line-height:1.5}
.jp-sugs{display:flex;flex-wrap:wrap;gap:8px;padding:0 20px 16px}
.jp-sug{height:34px;padding:0 13px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:'Google Sans',system-ui,sans-serif;font-size:13px;font-weight:500;color:#0B1433;cursor:pointer;white-space:nowrap}
.jp-sug:hover{border-color:#1652F0}
.jp-ask{display:flex;align-items:center;gap:8px;margin:0 16px 16px;height:50px;box-sizing:border-box;padding:4px 4px 4px 16px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF}
.jp-ask:focus-within{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.jp-ask input{flex:1;min-width:0;height:100%;border:none;outline:none;background:transparent;font-family:'Google Sans',system-ui,sans-serif;font-size:14px;color:#0B1433}
.jp-ask input::placeholder{color:#8A93AD}
.jp-send{width:40px;height:40px;border-radius:999px;border:none;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center;cursor:pointer}
.jp-mbar{display:none}
.jp-modal{position:fixed;inset:0;z-index:50;background:rgba(11,20,51,.42);display:flex;align-items:center;justify-content:center;padding:24px}
.jp-dlg{width:100%;max-width:440px;padding:28px;border-radius:24px;background:#FFFFFF;box-shadow:0 40px 80px -30px rgba(11,20,51,.6);box-sizing:border-box;display:flex;flex-direction:column;gap:14px}
.jp-dh{display:flex;align-items:flex-start;justify-content:space-between;gap:12px}
.jp-dh b{display:block;font-size:22px;font-weight:600;letter-spacing:-.4px;color:#0B1433}
.jp-dh span{display:block;margin-top:4px;font-size:14px;color:#5B6582}
.jp-x{width:40px;height:40px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;display:flex;align-items:center;justify-content:center;cursor:pointer;flex-shrink:0}
.jp-fl{display:flex;flex-direction:column;gap:6px;font-size:13px;font-weight:500;color:#3A4566}
.jp-fi{height:48px;box-sizing:border-box;padding:0 14px;border-radius:12px;border:1.5px solid #D6DDEE;font-family:'Google Sans',system-ui,sans-serif;font-size:15px;color:#0B1433;outline:none}
.jp-fi:focus{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.jp-err{font-size:13px;color:#B42318}
.jp-dlg .jp-btn{width:100%;justify-content:space-between}
.jp-sm{font-size:13px;color:#5B6582;text-align:center}
.jp-sm a{color:#1652F0;font-weight:600;text-decoration:none}
.jp-one{max-width:760px;margin:0 auto;padding:48px 24px 96px;box-sizing:border-box}
.jp-chips{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.jp-g{height:30px;padding:0 12px 0 9px;border-radius:999px;background:#E7F5EE;color:#0F6B45;display:inline-flex;align-items:center;gap:6px;font-size:13px;font-weight:500}
.jp-s{height:30px;padding:0 12px;border-radius:999px;background:#F1F3F8;color:#3A4566;display:inline-flex;align-items:center;font-size:13px;font-weight:500}
.jp-h1c{margin:18px 0 0;font-size:40px;line-height:1.08;font-weight:600;letter-spacing:-1.2px;color:#0B1433}
.jp-sub{margin:10px 0 0;font-size:16px;line-height:1.55;color:#4A5578}
.jp-ph{position:relative;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin-top:32px}
.jp-ph::before{content:"";position:absolute;left:12.5%;right:12.5%;top:15px;height:2px;background:linear-gradient(90deg,#1652F0 0 33%,#DCE5FB 33% 100%)}
.jp-pp{position:relative;display:flex;flex-direction:column;align-items:center;gap:8px;font-size:13px;font-weight:500;color:#8A93AD}
.jp-pn{width:32px;height:32px;border-radius:999px;background:#FFFFFF;border:2px solid #DCE5FB;box-sizing:border-box;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;color:#8A93AD}
.jp-pp:first-child{color:#0B1433}
.jp-pp:first-child .jp-pn{background:#1652F0;border-color:#1652F0;color:#FFFFFF;box-shadow:0 0 0 6px rgba(22,82,240,.12)}
.jp-week{margin-top:32px;border-radius:20px;border:1.5px solid #E6EAF3;background:#FFFFFF;overflow:hidden}
.jp-wh{display:flex;align-items:center;gap:12px;padding:16px 20px;border-bottom:1px solid #EEF1F7;font-size:15px;font-weight:600;color:#0B1433}
.jp-wi{box-sizing:border-box;display:flex;align-items:center;gap:14px;min-height:56px;padding:6px 20px}
.jp-wi + .jp-wi{border-top:1px solid #EEF1F7}
.jp-box{width:22px;height:22px;border-radius:999px;border:1.5px solid #CBD3E6;box-sizing:border-box;flex-shrink:0}
.jp-wt{flex:1;min-width:0;font-size:15px;color:#0B1433}
.jp-wm{font-size:13px;color:#8A93AD;white-space:nowrap}
.jp-acts{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-top:32px}
.jp-link{font-size:15px;font-weight:600;color:#1652F0;text-decoration:none;min-height:44px;display:inline-flex;align-items:center}
.jp-q{margin-top:40px;display:flex;flex-direction:column;gap:14px}
.jp-ql{font-size:17px;font-weight:600;letter-spacing:-.2px;color:#0B1433}
.jp-goal{height:60px;box-sizing:border-box;padding:0 20px;border-radius:16px;border:1.5px solid #D6DDEE;background:#FFFFFF;display:flex;align-items:center;box-shadow:0 20px 40px -32px rgba(11,20,51,.5)}
.jp-goal:focus-within{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.jp-goal input{flex:1;min-width:0;height:100%;border:none;outline:none;background:transparent;font-family:'Google Sans',system-ui,sans-serif;font-size:17px;color:#0B1433}
.jp-chip{height:38px;padding:0 15px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:'Google Sans',system-ui,sans-serif;font-size:14px;font-weight:500;color:#0B1433;cursor:pointer;display:inline-flex;align-items:center;gap:7px;white-space:nowrap}
.jp-chip:hover{border-color:#9DB8F7}
.jp-chip-on{background:#EAF0FF;border-color:#1652F0;color:#0E3BB8}
.jp-chip svg{display:none}
.jp-chip-on svg{display:block}
.jp-one-w{max-width:928px}
.jp-know{display:grid;grid-template-columns:1.3fr 1fr 1fr;border-radius:20px;border:1.5px solid #E6EAF3;background:#FFFFFF}
.jp-kc{display:flex;flex-direction:column;gap:10px;padding:18px 20px}
.jp-kc + .jp-kc{border-left:1px solid #EEF1F7}
.jp-kh{display:flex;align-items:baseline;gap:8px;font-size:13px;font-weight:500;color:#8A93AD}
.jp-kh b{font-size:24px;font-weight:600;letter-spacing:-.5px;color:#0B1433}
.jp-kl{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:6px;font-size:13px;line-height:1.4;color:#3A4566}
.jp-kl li{display:flex;gap:8px;align-items:flex-start}
.jp-kl svg{color:#0F6B45;flex-shrink:0;margin-top:2px}
.jp-ks{display:flex;flex-wrap:wrap;gap:6px}
.jp-ks span{height:26px;padding:0 10px;border-radius:999px;background:#E7F5EE;color:#0F6B45;display:inline-flex;align-items:center;font-size:12px;font-weight:500}
.jp-btn:focus-visible,.jp-sug:focus-visible,.jp-send:focus-visible,.jp-chip:focus-visible,.jp-a:focus-visible,.jp-link:focus-visible,.jp-x:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:3px}
@media (max-width: 1180px){.jp-wrap{grid-template-columns:minmax(0,1fr) 340px;gap:0 36px}}
@media (max-width: 960px){.jp-wrap{grid-template-columns:minmax(0,1fr)}.jp-side{position:static;margin-top:40px}.jp-know{grid-template-columns:minmax(0,1fr)}.jp-kc + .jp-kc{border-left:none;border-top:1px solid #EEF1F7}}
@media (max-width: 760px){
.jp-page{background-size:auto 300px}
.jp-bar{height:60px;padding:0 16px}
.jp-bar .sx-word{display:none}
.jp-wrap{padding:24px 20px 0}
.jp-save,.jp-ok{padding:14px;gap:12px}
.jp-save .jp-btn,.jp-ok .jp-btn{display:none}
.jp-head{margin-top:28px}
.jp-h1{font-size:28px;letter-spacing:-.8px}
.jp-stats{grid-template-columns:repeat(3,minmax(0,1fr))}
.jp-sv{padding:10px 12px}
.jp-sv b{font-size:14px}
.jp-sv > span{font-size:11px}
.jp-steps{margin-top:32px;gap:14px}
.jp-st{grid-template-columns:32px minmax(0,1fr);gap:12px}
.jp-st:not(:last-child)::before{left:15px;top:32px}
.jp-n{width:32px;height:32px;font-size:13px}
.jp-sl{height:32px;font-size:13px}
.jp-card{padding:14px 16px}
.jp-card{display:flex;flex-direction:column}
.jp-ch{display:contents}
.jp-card .jp-a{order:2;margin-top:10px}
.jp-t{font-size:16px}
.jp-li{padding:8px 14px;gap:12px}
.jp-lt{font-size:14px}
.jp-lm{display:none}
.jp-proof{padding:16px}
.jp-side{margin-top:32px}
.jp-coach{border-radius:20px}
.jp-msgs{padding:16px}
.jp-sugs{flex-wrap:nowrap;overflow-x:auto;padding:0 16px 14px;scrollbar-width:none}
.jp-sugs::-webkit-scrollbar{display:none}
.jp-mbar{display:flex;position:sticky;bottom:0;z-index:20;margin:28px -20px 0;padding:12px 16px;border-top:1px solid #E6EAF3;background:rgba(255,255,255,.94);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px)}
.jp-mbar .jp-btn{width:100%;justify-content:space-between}
.jp-modal{align-items:flex-end;padding:0}
.jp-dlg{max-width:none;border-radius:24px 24px 0 0;padding:22px 20px 24px}
.jp-one{padding:32px 20px 0}
.jp-h1c{font-size:28px;letter-spacing:-.8px}
.jp-sub{font-size:15px}
.jp-ph{margin-top:28px}
.jp-pp{font-size:11.5px}
.jp-week{margin-top:28px}
.jp-wi{padding:8px 16px;gap:12px}
.jp-wt{font-size:14px}
.jp-acts{position:sticky;bottom:0;z-index:20;flex-direction:column;gap:4px;margin:28px -20px 0;padding:12px 16px 10px;border-top:1px solid #E6EAF3;background:rgba(255,255,255,.94);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px)}
.jp-acts .jp-btn{width:100%;justify-content:space-between}
.jp-goal{height:54px;padding:0 16px;border-radius:14px}
.jp-goal input{font-size:16px}
.jp-q{margin-top:32px}
.jp-row{display:grid;grid-template-columns:1fr 1fr}
.jp-row .jp-chip{justify-content:center}
.jp-chip{flex-shrink:0}
}
'''.replace('CLOUD',CLOUD).replace('MARK',MARK).replace('WAVE',WAVE)
XIC='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"></path></svg>'
SEND='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'
body='''<div class="jp-page">
<header class="jp-bar">
<a class="sx-logo" href="#" aria-label="Credalio home"><span class="sx-mark" aria-hidden="true"></span><span class="sx-word" aria-hidden="true"></span></a>
<div class="jp-right">
<sc-if value="{{guest}}" hint-placeholder-val="{{ true }}"><a class="jp-login" href="#">Log in</a></sc-if>
<sc-if value="{{member}}" hint-placeholder-val="{{ false }}"><span class="jp-pill" aria-label="200 DLP available"><span class="dlp-c"></span>200</span><span class="jp-me" aria-label="Your account">MR</span></sc-if>
</div>
</header>

<sc-if value="{{isPlan}}" hint-placeholder-val="{{ true }}">
<div class="jp-wrap">
<div class="jp-main">
<sc-if value="{{guest}}" hint-placeholder-val="{{ true }}">
<div class="jp-save"><div><b>This journey isn’t saved yet</b><span>Save it free to start learning and keep every change.</span></div><button class="jp-btn" type="button" onClick="{{openSave}}">Save my journey<i aria-hidden="true">%(arr)s</i></button></div>
</sc-if>
<sc-if value="{{member}}" hint-placeholder-val="{{ false }}">
<div class="jp-ok"><div><span class="jp-okc">%(ck14)s</span><div><b>Saved to your account</b><span>Your AI Coach keeps adapting it as you learn.</span></div></div><button class="jp-btn" type="button" onClick="{{toStep1}}">Start step 1<i aria-hidden="true">%(arr)s</i></button></div>
</sc-if>
<div class="jp-head">
<span class="jp-k">Your journey</span>
<h1 class="jp-h1">Becoming a Data Analyst</h1>
<div class="jp-stats">
<div class="jp-sv {{upCls}}"><span>Time</span><b>{{time}}</b></div>
<div class="jp-sv {{upCls}}"><span>Each week</span><b>{{commit}} hrs</b></div>
<div class="jp-sv"><span>You start at</span><b>Related skills</b></div>
</div>
</div>
<div class="jp-steps">
<div class="jp-st"><span class="jp-n">1</span><div>
<div class="jp-sl">Build your foundation<sc-if value="{{up1}}" hint-placeholder-val="{{ false }}"><span class="jp-up">Updated</span></sc-if></div>
<div class="jp-card {{c1}}"><div class="jp-ch"><div><span class="jp-tag" style="background: #EAF0FF; color: #0E3BB8">Validated course</span><div class="jp-t">Data Foundations: Spreadsheets to SQL<i class="sx-tip" tabindex="0" data-tip="{{reason}}">i</i></div><div class="jp-m">{{s1meta}}</div></div><a class="jp-a" href="#">View course →</a></div></div>
</div></div>
<div class="jp-st"><span class="jp-n">2</span><div>
<div class="jp-sl">Build practical ability</div>
<div class="jp-card"><div class="jp-ch"><div><span class="jp-tag" style="background: #E7F5EE; color: #0F6B45">Project</span><div class="jp-t">Clean and analyse a real sales dataset</div></div><a class="jp-a" href="#">View project →</a></div><p class="jp-d">Use spreadsheets, SQL and your own judgement on real business data. A mentor reviews it.</p></div>
</div></div>
<div class="jp-st"><span class="jp-n">3</span><div>
<div class="jp-sl">Build job-ready skills<em>· {{nList}} courses</em><sc-if value="{{up3}}" hint-placeholder-val="{{ false }}"><span class="jp-up">Updated</span></sc-if></div>
<ul class="jp-list {{c3}}"><sc-for list="{{list}}" as="l" hint-placeholder-count="4"><li class="jp-li"><span class="jp-lk">{{l.k}}</span><span class="jp-lt">{{l.t}}</span><sc-if value="{{l.isNew}}" hint-placeholder-val="{{ false }}"><span class="jp-new">New</span></sc-if><span class="jp-lm">{{l.m}}</span></li></sc-for></ul>
</div></div>
<div class="jp-st"><span class="jp-n">4</span><div>
<div class="jp-sl">Prove your capability</div>
<div class="jp-card"><div class="jp-ch"><div><span class="jp-tag" style="background: #FFF6E5; color: #8A4F00">Certification</span><div class="jp-t">Professional Certificate in Data Analysis</div><div class="jp-m">Assessed · exam and case study</div></div><a class="jp-a" href="#">View certification →</a></div></div>
</div></div>
<div class="jp-st"><span class="jp-n">%(ck14)s</span><div>
<div class="jp-sl">Build your evidence</div>
<div class="jp-proof"><div class="jp-pt">Your Data Analyst portfolio</div><div class="jp-pd">Verified and ready to share from your Digital Backpack.</div><div class="jp-pg"><span>3 case studies</span><span>1 capstone project</span><span>Professional credential</span></div></div>
</div></div>
</div>
</div>
<aside class="jp-side" aria-label="Your AI Coach">
<div class="jp-coach">
<div class="jp-chd"><span class="jp-av" aria-hidden="true"></span><div><b>Your AI Coach</b><span>Ask anything, or tell me what to change</span></div></div>
<div class="jp-msgs" aria-live="polite"><sc-for list="{{msgs}}" as="m" hint-placeholder-count="1"><div class="{{m.cls}}">{{m.text}}</div></sc-for></div>
<div class="jp-sugs"><sc-for list="{{sugs}}" as="q" hint-placeholder-count="4"><button class="jp-sug" type="button" onClick="{{q.pick}}">{{q.label}}</button></sc-for></div>
<form class="jp-ask" onSubmit="{{send}}"><label for="jp-q" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Ask your AI Coach</label><input id="jp-q" type="text" placeholder="Ask or tell me what to change…" value="{{ask}}" onInput="{{onAsk}}" autocomplete="off"><button class="jp-send" type="submit" aria-label="Send">%(send)s</button></form>
</div>
</aside>
<div class="jp-mbar"><button class="jp-btn" type="button" onClick="{{mainAct}}">{{mainLabel}}<i aria-hidden="true">%(arr)s</i></button></div>
</div>
</sc-if>

<sc-if value="{{isStep1}}" hint-placeholder-val="{{ false }}">
<main class="jp-one">
<div class="jp-chips"><span class="jp-g">%(ck12)sJourney saved</span><span class="jp-s">Step 1 of 5</span></div>
<h1 class="jp-h1c">Data Foundations: Spreadsheets to SQL</h1>
<p class="jp-sub">Build your foundation · Validated course · 12 hrs</p>
<div class="jp-ph" aria-label="Learn, practise, prove, advance">
<span class="jp-pp"><span class="jp-pn">1</span>Learn</span><span class="jp-pp"><span class="jp-pn">2</span>Practise</span><span class="jp-pp"><span class="jp-pn">3</span>Prove</span><span class="jp-pp"><span class="jp-pn">4</span>Advance</span>
</div>
<div class="jp-week">
<div class="jp-wh"><span class="jp-av" style="width: 30px; height: 30px" aria-hidden="true"></span>Your AI Coach set up your first week</div>
<div class="jp-wi"><span class="jp-box" aria-hidden="true"></span><span class="jp-wt">Lesson 1 · Getting started</span><span class="jp-wm">12 min</span></div>
<div class="jp-wi"><span class="jp-box" aria-hidden="true"></span><span class="jp-wt">A short practice on what you learned</span><span class="jp-wm">15 min</span></div>
<div class="jp-wi"><span class="jp-box" aria-hidden="true"></span><span class="jp-wt">Check in with your AI Coach</span><span class="jp-wm">5 min</span></div>
</div>
<div class="jp-acts"><a class="jp-link" href="#" onClick="{{toPlan}}">Back to my journey</a><a class="jp-btn" href="#">Begin lesson 1<i aria-hidden="true">%(arr)s</i></a></div>
</main>
</sc-if>

<sc-if value="{{isBack}}" hint-placeholder-val="{{ false }}">
<main class="jp-one jp-one-w">
<div class="jp-chips" style="gap: 10px; font-size: 13px; font-weight: 500; color: #5B6582"><span class="jp-av" style="width: 30px; height: 30px" aria-hidden="true"></span>Your AI Coach</div>
<h1 class="jp-h1c">Welcome back, Maya.</h1>
<p class="jp-sub">You’re already on your way. Tell me your new goal and I’ll build on what you’ve proven.</p>
<div class="jp-q">
<label class="jp-ql" for="jp-goal">What’s your new goal?</label>
<div class="jp-goal"><input id="jp-goal" type="text" value="I want to become a data analyst" autocomplete="off"></div>
</div>
<div class="jp-q">
<span class="jp-ql">What I already know about you</span>
<div class="jp-know">
<div class="jp-kc"><span class="jp-kh"><b>4</b>completed courses</span><ul class="jp-kl"><li>%(ck11)sBusiness Communication Essentials</li><li>%(ck11)sData Foundations: Spreadsheets to SQL</li><li>%(ck11)sAgile Foundations</li><li>%(ck11)sPresenting with Impact</li></ul></div>
<div class="jp-kc"><span class="jp-kh"><b>2</b>verified projects</span><ul class="jp-kl"><li>%(ck11)sCustomer insights report</li><li>%(ck11)sTeam process improvement plan</li></ul></div>
<div class="jp-kc"><span class="jp-kh"><b>4</b>verified skills</span><div class="jp-ks"><span>Excel</span><span>SQL basics</span><span>Agile basics</span><span>Stakeholder communication</span></div></div>
</div>
</div>
<div class="jp-q">
<span class="jp-ql">How soon would you like to get there?</span>
<div class="jp-chips jp-row"><sc-for list="{{paces}}" as="p" hint-placeholder-count="5"><button class="jp-chip {{p.cls}}" type="button" aria-pressed="{{p.on}}" onClick="{{p.pick}}">%(ck13)s{{p.label}}</button></sc-for></div>
</div>
<div class="jp-acts" style="justify-content: flex-end"><a class="jp-btn" href="#">See my recommended journey<i aria-hidden="true">%(arr)s</i></a></div>
</main>
</sc-if>

<sc-if value="{{modal}}" hint-placeholder-val="{{ false }}">
<div class="jp-modal" role="dialog" aria-modal="true" aria-labelledby="jp-dt">
<form class="jp-dlg" onSubmit="{{create}}" novalidate>
<div class="jp-dh"><div><b id="jp-dt">Save your journey</b><span>Create a free account. No card needed.</span></div><button class="jp-x" type="button" aria-label="Close" onClick="{{closeSave}}">%(x)s</button></div>
<label class="jp-fl">Full name<input class="jp-fi" type="text" value="{{fName}}" onInput="{{onName}}" autocomplete="name"></label>
<label class="jp-fl">Email<input class="jp-fi" type="email" value="{{fEmail}}" onInput="{{onEmail}}" autocomplete="email"></label>
<label class="jp-fl">Password<input class="jp-fi" type="password" value="{{fPw}}" onInput="{{onPw}}" autocomplete="new-password" placeholder="At least 8 characters"></label>
<sc-if value="{{hasErr}}" hint-placeholder-val="{{ false }}"><span class="jp-err" role="alert">{{err}}</span></sc-if>
<button class="jp-btn" type="submit">Create free account<i aria-hidden="true">%(arr)s</i></button>
<span class="jp-sm">Already have an account? <a href="#">Log in</a></span>
</form>
</div>
</sc-if>
</div>'''%dict(arr=ARR,ck14=CK%(14,14),ck12=CK%(12,12),ck11=CK%(11,11),ck13=CK%(13,13),send=SEND,x=XIC)
script=r'''
class Component extends DCLogic {
  constructor(props) {
    super(props);
    var v = (props && props.view) || 'guest';
    this.state = { view: v, member: v !== 'guest', adj: {}, up: -1, log: [], ask: '', modal: false, fName: '', fEmail: '', fPw: '', err: '', pace: '3–6 months' };
  }
  renderVals() {
    var self = this, S = this.state, A = S.adj, set = function (p) { self.setState(p); };
    var lo = 3, hi = 4, commit = 6;
    if (A.faster) { lo = 2; hi = 3; commit = 10; }
    var base = ['SQL for Data Analysis', 'Data Visualisation with Power BI', 'Statistics for Analysts', A.swap ? 'Tableau Fundamentals' : 'Python for Data Analysis'];
    var list = base.map(function (t, i) { return { k: i + 1, t: t, m: A.swap && i === 3 ? '8 hrs' : ['14 hrs', '10 hrs', '12 hrs', '16 hrs'][i], isNew: !!(A.swap && i === 3) }; });
    if (A.practical) list.push({ k: '+', t: 'Weekly applied mini-projects', m: 'Alongside every course', isNew: true });
    var say = function (q, a, patch, up) { set({ adj: Object.assign({}, S.adj, patch || {}), up: up === undefined ? S.up : up, log: S.log.concat([{ u: 1, t: q }, { u: 0, t: a }]) }); };
    var Q = [
      ['Can I finish faster?', function (q) { say(q, 'Yes. At about 10 hours a week your journey drops to 2–3 months. I’ve updated your plan.', { faster: true }, 0); }],
      ['I already know SQL', function (q) { say(q, 'Then I won’t make you re-learn it. Step 1 is now a short SQL refresher.', { skip: true }, 1); }],
      ['Make it more practical', function (q) { say(q, 'Done. Step 3 now has a weekly mini-project alongside every course.', { practical: true }, 3); }],
      ['Swap a course', function (q) { say(q, 'I’ve swapped Python for Data Analysis for Tableau Fundamentals in Step 3. You can swap any course this way.', { swap: !A.swap }, 3); }],
      ['What jobs could this lead to?', function (q) { say(q, 'Junior data analyst, business analyst and reporting analyst roles. Your portfolio and certificate are what make you stand out.'); }]
    ].filter(function (q) { var key = { 'Can I finish faster?': 'faster', 'I already know SQL': 'skip', 'Make it more practical': 'practical' }[q[0]]; return !key || !A[key]; }).slice(0, 4);
    var intro = S.member ? 'Your journey is saved. I’ll keep adapting it as you learn. Ask me anything, or tell me what to change.' : 'I built this around becoming a data analyst, using the related skills you already have. Ask me anything, or tell me what to change.';
    var v = S.view, member = S.member || v !== 'guest';
    return {
      guest: !member, member: member,
      isPlan: v === 'guest' || v === 'saved', isStep1: v === 'step1', isBack: v === 'returning',
      time: lo + '–' + hi + ' months', commit: commit, upCls: S.up === 0 ? 'jp-sv-up' : '',
      reason: A.skip ? 'You already know SQL, so this is now a short refresher and you reach practice sooner.' : 'Your goal depends on SQL and solid data foundations. This fills the gaps before real projects.',
      s1meta: A.skip ? 'Refresher · 3 hrs · Intermediate' : '12 hrs · Beginner · Gold Validated',
      up1: S.up === 1, up3: S.up === 3, c1: S.up === 1 ? 'jp-card-up' : '', c3: S.up === 3 ? 'jp-card-up' : '',
      list: list, nList: list.filter(function (l) { return l.k !== '+'; }).length,
      msgs: [{ u: 0, t: intro }].concat(S.log).map(function (m) { return { cls: m.u ? 'jp-you' : 'jp-ai', text: m.t }; }),
      sugs: Q.map(function (q) { return { label: q[0], pick: function () { q[1](q[0]); } }; }),
      ask: S.ask, onAsk: function (e) { set({ ask: e.target.value }); },
      send: function (e) { e.preventDefault(); var q = (S.ask || '').trim(); if (!q) return; set({ ask: '', log: S.log.concat([{ u: 1, t: q }, { u: 0, t: member ? 'Noted. I’ll factor that in and flag any steps it changes.' : 'Good idea. Save your journey and I can act on requests like this as you learn.' }]) }); },
      openSave: function () { set({ modal: true }); }, closeSave: function () { set({ modal: false, err: '' }); }, modal: S.modal,
      fName: S.fName, fEmail: S.fEmail, fPw: S.fPw, err: S.err, hasErr: !!S.err,
      onName: function (e) { set({ fName: e.target.value }); }, onEmail: function (e) { set({ fEmail: e.target.value }); }, onPw: function (e) { set({ fPw: e.target.value }); },
      create: function (e) { e.preventDefault(); var err = !S.fName.trim() ? 'Add your full name.' : !/^\S+@\S+\.\S+$/.test(S.fEmail) ? 'Check your email address.' : (S.fPw.length < 8 ? 'Use at least 8 characters for your password.' : ''); if (err) { set({ err: err }); return; } set({ modal: false, member: true, view: 'saved', err: '', log: [] }); },
      toStep1: function () { set({ view: 'step1' }); }, toPlan: function (e) { if (e) e.preventDefault(); set({ view: 'saved' }); },
      mainLabel: member ? 'Start step 1' : 'Save my journey', mainAct: function () { if (member) set({ view: 'step1' }); else set({ modal: true }); },
      paces: ['No deadline', '1–3 months', '3–6 months', '6–12 months'].map(function (p) { var on = S.pace === p; return { label: p, on: on ? 'true' : 'false', cls: on ? 'jp-chip-on' : '', pick: function () { set({ pace: p }); } }; })
    };
  }
}
'''
open('/home/user/credalio/design/canvas3/project/JourneyPlan.dc.html','w').write(page('Your Journey',css,'',body,script,1537,'"view":{"editor":"enum","options":["guest","saved","step1","returning"],"default":"guest"},'))
