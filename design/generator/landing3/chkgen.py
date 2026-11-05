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
I_PATH = '<circle cx="6" cy="19" r="2.5"></circle><circle cx="18" cy="5" r="2.5"></circle><path d="M8.5 19H16a3.5 3.5 0 0 0 0-7H8a3.5 3.5 0 0 1 0-7h7.5"></path>'
CKS = '<i class="xb-ck" aria-hidden="true">' + ck(11, 3.4) + '</i>'
G = '<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"></path><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"></path><path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.84z"></path><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"></path></svg>'
A = '<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path fill="#0B1433" d="M16.37 12.63c-.02-2.2 1.8-3.26 1.88-3.31-1.03-1.5-2.62-1.7-3.19-1.73-1.36-.14-2.65.8-3.34.8-.69 0-1.75-.78-2.88-.76-1.48.02-2.85.86-3.61 2.19-1.54 2.67-.39 6.62 1.11 8.79.73 1.06 1.6 2.25 2.75 2.21 1.1-.04 1.52-.71 2.86-.71 1.33 0 1.71.71 2.88.69 1.19-.02 1.94-1.08 2.67-2.15.84-1.23 1.19-2.42 1.21-2.48-.03-.01-2.32-.89-2.34-3.54zM14.17 6.15c.61-.74 1.02-1.76.91-2.78-.88.04-1.94.59-2.57 1.32-.56.65-1.06 1.69-.93 2.69.98.08 1.98-.5 2.59-1.23z"></path></svg>'
M = {'card': '<rect x="3" y="5" width="18" height="14" rx="2.5"></rect><path d="M3 10h18M7 15h4"></path>',
     'local': '<rect x="7" y="2.5" width="10" height="19" rx="2.5"></rect><path d="M11 18h2"></path>',
     'mforge': '<path d="M6 3h12l3 6-9 12L3 9z"></path><path d="M3 9h18M9 3l3 18 3-18"></path>'}

CSS = r'''body{margin:0;background:#FFFFFF}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.tk-root{position:relative;isolation:isolate;overflow-x:hidden;min-height:100vh;display:flex;flex-direction:column;background:#FFFFFF;font-family:'Google Sans','Google Sans Text','Helvetica Neue',system-ui,sans-serif;color:#0B1433}
.tk-top{position:sticky;top:0;z-index:5;height:64px;flex-shrink:0;box-sizing:border-box;display:flex;align-items:center;gap:16px;padding:0 20px;border-bottom:1.5px solid #EEF1F7;background:rgba(255,255,255,.94);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}
.lp-x{width:40px;height:40px;flex-shrink:0;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#3A4566;text-decoration:none}
.lp-x:hover{background:#F5F8FF;color:#0B1433}
.lp-t1{font-size:16px;font-weight:600;white-space:nowrap}
.tk-safe{margin-left:auto;display:inline-flex;align-items:center;gap:7px;font-size:13px;font-weight:500;color:#5B6582}
.tk-root:has(.ko) .cl-glow{display:none}
.cl-glow{position:absolute;left:0;right:0;top:0;height:340px;z-index:-1;pointer-events:none;background:radial-gradient(60% 100% at 50% 0,rgba(22,82,240,.08),transparent 70%)}
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
.ck-perks{margin:16px 0 0;padding:16px 18px;list-style:none;border-radius:16px;background:#F7F9FD;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px 18px}
.ck-perks li{display:flex;align-items:flex-start;gap:9px;font-size:14px;line-height:1.4;color:#3A4566}
.ck-perks li i{width:18px;height:18px;border-radius:999px;background:#E7F5EE;color:#0F6B45;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px}
.cb-o{position:relative;display:flex;flex-direction:column;align-items:flex-start;gap:2px;text-align:left;padding:18px 16px 16px}
.cb-o b{display:flex;align-items:center;gap:8px;font-size:22px;font-weight:600}
.cb-o b .dlp-c{width:22px;height:22px}
.cb-o > span{font-size:13px;color:#5B6582}
.cb-d{margin-top:8px;font-size:12.5px !important;color:#5B6582 !important;line-height:1.4}
.cb-pop{position:absolute;top:-11px;left:14px;height:22px;padding:0 10px;border-radius:999px;background:#FFF1CF;border:1.5px solid #F4D98E;color:#6B4E16;font-size:11.5px;font-weight:500;font-style:normal;display:inline-flex;align-items:center;white-space:nowrap}
.ck-get{display:inline-flex;align-items:center;gap:8px}
.ck-fsum,.ck-more{display:none}
.wf-usd{margin-left:auto;font-size:16px;font-weight:600;color:#0B1433}
.ck-p .hp-lab{font-size:13px;color:#5B6582}
.ck-p b .dlp-c{width:22px;height:22px}
.ck-perks li{display:flex;align-items:flex-start;gap:9px;font-size:14px;line-height:1.4;color:#3A4566}
.ck-perks li i{width:18px;height:18px;border-radius:999px;background:#E7F5EE;color:#0F6B45;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px}
.ck-fit{margin:14px 0 0;display:flex;align-items:flex-start;gap:10px;font-size:14px;line-height:1.5;color:#3A4566}
.ck-fit i{width:20px;height:20px;border-radius:999px;flex-shrink:0;margin-top:1px;display:flex;align-items:center;justify-content:center;font-style:normal;font-size:12px;font-weight:700;color:#FFFFFF;background:#0F6B45}
.ck-fit.part i{background:#B97A10}
.wf-tot{margin-top:16px;display:flex;align-items:baseline;gap:10px;padding:14px 18px;border-radius:16px;background:#F5F8FF}
.wf-tot > span:first-child{font-size:14px;color:#3A4566}
.wf-tot b{font-size:20px;font-weight:600}
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
@media (prefers-reduced-motion: reduce){.ob-in,.ob-in2{animation:none}}
@keyframes obIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
.ob-in{animation:obIn .5s ease both}.ob-in2{animation:obIn .5s ease .08s both}.ob-in3{animation:obIn .5s ease .16s both}.ob-in4{animation:obIn .5s ease .24s both}
@media (prefers-reduced-motion: reduce){.ob-in,.ob-in2,.ob-in3,.ob-in4{animation:none}}
.sec-h{margin:0;font-size:13.5px;font-weight:600;color:#8A93AD}
.lp-h1{margin:10px 0 0 0;font-size:clamp(30px,4.6vh,40px);line-height:1.12;font-weight:600;letter-spacing:-0.03em}
@media (max-width: 960px){
.lp-h1{font-size:25px}
}
.ko{flex-grow:1;width:min(920px,100%);box-sizing:border-box;margin:0 auto;padding:clamp(20px,3.6vh,40px) 24px 32px 24px;display:flex;flex-direction:column;align-items:center;text-align:center;--k:#1652F0;--kb:#EAF0FF}
.tk-root:has(.ko){--glow:22,82,240;background:radial-gradient(55% 40% at 50% 0%,rgba(var(--glow),.12),rgba(var(--glow),0) 70%),#FFFFFF}
.tk-root:has(.ko-v){--glow:15,107,69}.tk-root:has(.ko-a){--glow:214,140,20}.tk-root:has(.ko-f){--glow:91,101,130}
.ko-v{--k:#0F6B45;--kb:#E7F5EE}.ko-a{--k:#B26A00;--kb:#FFF3DC}
.ko-emb{position:relative;width:84px;height:84px;display:flex;align-items:center;justify-content:center}
.ko-halo{position:absolute;inset:0;border-radius:50%;background:var(--kb)}
.ko-r .ko-halo::after{content:'';position:absolute;inset:-6px;border-radius:50%;border:2px solid transparent;border-top-color:#1652F0;animation:koSpin 1.4s linear infinite}
@keyframes koSpin{to{transform:rotate(360deg)}}
.ko-disc{position:relative;width:58px;height:58px;border-radius:50%;background:var(--k);color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 12px 28px rgba(11,20,51,.16)}
.ko-tick path{stroke-dasharray:1;stroke-dashoffset:1;animation:koDraw .6s ease .3s forwards}
@keyframes koDraw{to{stroke-dashoffset:0}}
.ko-pill{margin-top:14px;display:inline-flex;align-items:center;height:30px;padding:0 13px;border-radius:999px;background:var(--kb);color:var(--k);font-size:13px;font-weight:500}
.ko-h{margin-top:10px;font-size:clamp(28px,4.4vh,38px)}
.ko-sub{margin:10px 0 0 0;font-size:16.5px;line-height:1.55;color:#4A5578;max-width:520px}
.ko-card{margin-top:22px;width:100%;box-sizing:border-box;padding:18px 20px;border-radius:20px;background:#FFFFFF;border:1.5px solid #E6EAF3;text-align:left;max-width:640px}
.ko-path{list-style:none;margin:12px 0 0 0;padding:0;display:flex;flex-direction:column}
.ko-path li{position:relative;display:flex;align-items:flex-start;gap:12px;padding-bottom:12px}
.ko-path li:last-child{padding-bottom:0}
.ko-path li:not(:last-child)::before{content:'';position:absolute;left:10px;top:24px;bottom:2px;width:2px;border-radius:2px;background:#E6EAF3}
.ko-path li.ko-done::before{background:#1652F0}
.ko-dot{width:22px;height:22px;flex-shrink:0;box-sizing:border-box;border-radius:50%;border:2px solid #D6DDEE;background:#FFFFFF;display:flex;align-items:center;justify-content:center;color:#FFFFFF}
.ko-done .ko-dot{background:#1652F0;border-color:#1652F0}
.ko-now .ko-dot{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.14)}
.ko-now .ko-dot::after{content:'';width:8px;height:8px;border-radius:50%;background:#1652F0;animation:koBlink 1.6s ease-in-out infinite}
@keyframes koBlink{50%{opacity:.3}}
.ko-path li > span:last-child{display:flex;flex-direction:column;gap:2px;padding-top:1px}
.ko-path b{font-size:15px;font-weight:600}
.ko-path li > span:last-child > span{font-size:13.5px;color:#5B6582}
.ko-path li:not(.ko-done):not(.ko-now) b{color:#5B6582;font-weight:500}
.ko-next{margin-top:12px;width:100%;box-sizing:border-box;display:flex;align-items:center;gap:14px;padding:16px 16px 16px 18px;border-radius:20px;background:#F7F9FD;border:1.5px solid #E6EAF3;text-align:left}
.ko-ni{width:44px;height:44px;flex-shrink:0;border-radius:14px;background:#FFFFFF;color:#1652F0;display:flex;align-items:center;justify-content:center;border:1.5px solid #E6EAF3}
.ko-nt{flex-grow:1;display:flex;flex-direction:column;gap:2px}
.ko-nl{font-size:12.5px;font-weight:500;color:#8A93AD}
.ko-nt b{font-size:16px;font-weight:600}
.ko-nt > span:last-child{font-size:13.5px;line-height:1.45;color:#3A4566}
.ko-go{flex-shrink:0}
.ko-opts{margin-top:12px;display:flex;flex-direction:column;gap:8px}
.ko-opt{display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:16px;border:1.5px solid #E6EAF3;background:#FFFFFF;color:#0B1433;text-decoration:none;transition:all .2s ease}
.ko-opt:hover{border-color:#AFC1F5;background:#F5F8FF;color:#0B1433}
.ko-opt > span:nth-child(2){flex-grow:1;display:flex;flex-direction:column;gap:2px}
.ko-opt b{font-size:15px;font-weight:600}
.ko-opt > span:nth-child(2) > span{font-size:13.5px;line-height:1.45;color:#5B6582}
.ko-opt > svg{flex-shrink:0;color:#8A93AD}
.ko-oi{width:40px;height:40px;flex-shrink:0;border-radius:12px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.ko-cta{margin-top:20px;display:flex;flex-direction:column;align-items:center;gap:10px}
.ko-sub{max-width:600px}
.ko-opts{display:grid !important;grid-template-columns:minmax(0,1fr) minmax(0,1fr)}
.ko-a .ko-card{max-width:none}
.ko-links{margin-top:18px;display:flex;align-items:center;gap:10px;font-size:14.5px;color:#8A93AD}
.ko-links a{font-weight:600;text-decoration:none;color:#3A4566}
.ko-links a:hover{color:#1652F0}
@media (prefers-reduced-motion: reduce){.ko-r .ko-halo::after,.ko-now .ko-dot::after{animation:none}.ko-tick path{animation:none;stroke-dashoffset:0}}
@media (max-width: 960px){
.ko{padding:36px 16px 32px 16px;align-items:stretch;text-align:center}
.ko-emb{width:72px;height:72px;align-self:center}
.ko-disc{width:48px;height:48px}.ko-disc svg{width:24px;height:24px}
.ko-pill{align-self:center;margin-top:14px}
.ko-h{font-size:24px;margin-top:10px}
.ko-sub{font-size:14.5px;margin-top:8px}
.ko-card{margin-top:20px;padding:14px 16px;border-radius:18px}
.ko-opts{grid-template-columns:minmax(0,1fr) !important}
.ko-next{flex-wrap:wrap;padding:14px 16px;border-radius:18px}
.ko-ni{display:none}
.ko-go{width:100%;justify-content:space-between}
.ko-cta{position:sticky;bottom:0;margin:20px -16px 0 -16px;padding:12px 16px;background:#FFFFFF;border-top:1.5px solid #EEF1F7;align-items:stretch}
.ko-cta .ds-btn{justify-content:space-between}
.ko-links{justify-content:center;font-size:14px}
.ko-r{padding-top:48px;padding-bottom:28px}
.ko-r .ko-pill{margin-top:20px}
.ko-r .ko-h{margin-top:14px}
.ko-r .ko-sub{margin-top:10px;line-height:1.55}
.ko-r .ko-card{margin-top:32px;padding:18px 18px 20px 18px}
.ko-r .ko-path{margin-top:16px}
.ko-r .ko-path li{padding-bottom:22px}
.ko-r .ko-path li:last-child{padding-bottom:0}
.ko-r .ko-cta{position:static;margin:24px 0 0 0;padding:0;border-top:0;background:none}
.ko-r .ko-links{margin-top:auto;padding-top:28px}
}
.tk-scene{position:absolute;left:0;right:0;bottom:0;height:min(46vh,40vw);background:url(/_blob/b7fe5c1a1e0ae23ab09139f1d05e4281) 50% 100% / cover no-repeat;z-index:-1;pointer-events:none}
.tk-scene.lo{height:min(26vh,22vw);-webkit-mask-image:linear-gradient(to bottom,transparent,#000 40%);mask-image:linear-gradient(to bottom,transparent,#000 40%)}
@media (max-width: 760px){.tk-scene{height:240px;background-size:250% auto;background-position:52% 100%}
.tk-scene.lo{height:150px}}
.wo-one{max-width:560px}
.ko-cta:not(:has(.ds-btn)){margin-top:14px}
@media (max-width: 960px){.cf{--k:.56}}
@media (prefers-reduced-motion: reduce){.cf{display:none}}
.ko-halo,.ko-disc{z-index:1}
.ko-card:has(.ko-path){max-width:760px;margin-top:40px;padding:0;border:0;background:none}
.ko-card:has(.ko-path) .sec-h{display:none}
.ko-path{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));margin:0}
.ko-path li{flex-direction:column;align-items:center;gap:14px;padding:0 12px;text-align:center}
.ko-path li:not(:last-child)::before{left:calc(50% + 22px);right:calc(-50% + 22px);top:13px;bottom:auto;width:auto;height:2px}
.ko-path li.ko-now::before{background:repeating-linear-gradient(90deg,#1652F0 0 6px,transparent 6px 12px) 0 0 / 12px 2px;opacity:.55;animation:koFlow 1.2s linear infinite}
.ko-path .ko-dot{width:28px;height:28px}
.ko-path .ko-now .ko-dot::after{width:10px;height:10px}
.ko-card:has(.ko-path) ~ .ko-links,.ko-card:has(.ko-path) + .ko-links{margin-top:40px}
.ko-path li > span:last-child{align-items:center;gap:4px}
@keyframes koFlow{to{background-position:12px 0}}
@media (prefers-reduced-motion: reduce){.ko-path li.ko-now::before{animation:none}}
.ko-rc .ko-emb{display:none}
.rc{position:relative;width:100%;max-width:380px;align-self:center}
.rc .cf{top:40px}
.rc .cf i{animation-delay:calc(var(--dl) + 2.45s)}
.rc:not(.rc-go) .rc-paper{animation:none;transform:translateY(-100%)}
.rc:not(.rc-go) .rc-stamp{animation:none;opacity:0}
.rc:not(.rc-go) .cf i{animation:none}
.rc-slot{position:relative;z-index:2;height:34px;margin:0 -14px;border-radius:14px;background:linear-gradient(180deg,#FFFFFF,#EAF0FF);border:1.5px solid #D6DDEE;box-shadow:0 14px 34px rgba(22,82,240,.16)}
.rc-slot i{position:absolute;left:18px;right:18px;bottom:8px;height:6px;border-radius:6px;background:#0B1433;opacity:.18}
.rc-clip{position:relative;z-index:1;margin-top:-12px;overflow:hidden;padding:0 4px 18px 4px;filter:drop-shadow(0 1px 0 #D6DDEE) drop-shadow(1px 0 0 #E6EAF3) drop-shadow(-1px 0 0 #E6EAF3) drop-shadow(0 12px 18px rgba(11,20,51,.08))}
.rc-paper{position:relative;padding:28px 24px 30px 24px;background:linear-gradient(180deg,#F5F8FF,#FFFFFF 40%);text-align:left;--zz:conic-gradient(from -45deg at bottom,#0000,#000 1deg 89deg,#0000 90deg) 50% 100% / 14px 8px repeat-x,linear-gradient(#000 0 0) 0 0 / 100% calc(100% - 7px) no-repeat;-webkit-mask:var(--zz);mask:var(--zz);animation:rcPrint 2.2s cubic-bezier(.33,.8,.25,1) .25s both}
.rc-top{display:flex;align-items:flex-start;justify-content:space-between;gap:12px;padding-bottom:16px;border-bottom:1.5px dashed #D6DDEE}
.rc-k{display:block;font-size:12px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#0F6B45}
.rc-amt{display:block;margin-top:6px;font-size:28px;font-weight:600;letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.rc-m{display:block;margin-top:4px;font-size:12.5px;color:#5B6582}
.rc-stamp{flex-shrink:0;width:64px;height:64px;border-radius:50%;border:2px solid #0F6B45;box-shadow:inset 0 0 0 4px #FFFFFF,inset 0 0 0 5.5px #0F6B45;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1px;transform:rotate(-12deg);background:#E7F5EE;animation:rcStamp .45s cubic-bezier(.2,1.6,.4,1) 2.35s both}
.rc-stamp img{width:20px;height:20px}
.rc-stamp em{font-style:normal;font-size:10.5px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#0F6B45}
.rc-l{list-style:none;margin:0;padding:14px 0;display:flex;flex-direction:column;gap:9px;border-bottom:1.5px dashed #D6DDEE}
.rc-l li{display:flex;justify-content:space-between;gap:12px;font-size:13.5px;color:#3A4566;font-variant-numeric:tabular-nums}
.rc-tot{display:flex;justify-content:space-between;align-items:baseline;padding:14px 0;border-bottom:1.5px dashed #D6DDEE;font-size:14px;font-weight:600}
.rc-tot b{font-size:16px;font-weight:600;color:#1652F0;font-variant-numeric:tabular-nums}
.rc-ft{display:flex;justify-content:space-between;align-items:center;gap:10px;padding-top:14px;font-size:12.5px;color:#5B6582}
.rc-ft a{font-size:13px;font-weight:600}
@keyframes rcPrint{0%{transform:translateY(-100%)}22%{transform:translateY(-78%)}30%{transform:translateY(-74%)}52%{transform:translateY(-46%)}60%{transform:translateY(-42%)}82%{transform:translateY(-10%)}100%{transform:none}}
@keyframes rcStamp{from{opacity:0;transform:rotate(-12deg) scale(1.8)}to{opacity:1;transform:rotate(-12deg) scale(1)}}
@media (prefers-reduced-motion: reduce){.rc-paper,.rc-stamp{animation:none}}
.rc-nx{margin-top:0}
@media (min-width: 961px){
.ko-rc{width:min(1040px,100%);display:grid;grid-template-columns:minmax(0,1fr) 400px;grid-template-areas:". rc" "pill rc" "h rc" "sub rc" "nx rc" "lk rc" ". rc";grid-template-rows:1fr auto auto auto auto auto 1fr;column-gap:72px;align-content:center;align-items:start;text-align:left}
.ko-rc .rc{grid-area:rc;align-self:center}
.ko-rc .ko-pill{grid-area:pill;justify-self:start;margin-top:0}
.ko-rc .ko-h{grid-area:h;font-size:clamp(32px,4.6vh,42px)}
.ko-rc .ko-sub{grid-area:sub;max-width:460px}
.ko-rc .rc-nx{grid-area:nx;margin-top:32px;flex-direction:column;align-items:flex-start;gap:16px;padding:20px 22px}
.ko-rc .rc-nx .ko-ni{display:none}
.ko-rc .ko-links{grid-area:lk;justify-content:flex-start;margin-top:22px}
}
@media (max-width: 960px){
.rc{max-width:330px;margin:24px 0 4px 0}
.ko-rc .ko-pill{order:1;margin-top:0}.ko-rc .ko-h{order:2}.ko-rc .ko-sub{order:3}.ko-rc .rc{order:4}.ko-rc .rc-nx{order:5}.ko-rc .ko-links{order:6}
.rc-paper{padding:22px 18px 26px 18px}
.rc-amt{font-size:24px}
.rc-stamp{width:54px;height:54px}
.ko-rc .rc-nx{margin-top:22px}
}
@media (min-width: 961px){.ko{justify-content:center;padding-bottom:10vh}}
@media (max-width: 960px){
.ko-card:has(.ko-path){margin-top:28px;padding:0;border:0;background:none}
.ko-path li{padding:0 4px !important;gap:10px}
.ko-path li:not(:last-child)::before{left:calc(50% + 18px);right:calc(-50% + 18px)}
.ko-path b{font-size:13.5px}
.ko-path li > span:last-child > span{font-size:12px;line-height:1.35}
}
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
.cl-foot{flex-wrap:wrap;row-gap:10px}
.ck-pl.n3{grid-template-columns:minmax(0,1fr)}
.wf-ml{grid-template-columns:minmax(0,1fr)}
.wf-m{flex-direction:row;align-items:center;padding:14px}
.ck-f.h{grid-column:span 4}
.ck-f.q{grid-column:span 2}
.wf-dl{padding:2px 16px}
.ck-acc .ck-row{flex-direction:column}
.ck-acc .ck-row .ds-btn{justify-content:space-between}
.ck-sso{flex-direction:column}
.ck-sso a{flex:none}
}
@media (max-width: 760px){.ck-perks{grid-template-columns:minmax(0,1fr)}.ck-pl,.ck-pl.n3{grid-template-columns:minmax(0,1fr);gap:18px}.cb-o{flex-direction:row;align-items:baseline;gap:10px;padding:22px 18px 20px}.ck-pl .cb-o:has(.cb-pop){padding-top:30px}.ck-pl,.ck-pl.n3{gap:22px !important}.ck-perks{background:none;padding:4px 2px 0;gap:12px}.ck-perks:not(.all) li:nth-child(n+4){display:none}.ck-more{display:inline-flex;margin-top:12px;font-size:14px}.wf-tot{display:none}.ck-fsum{display:flex;width:100%;align-items:center;justify-content:space-between;gap:12px;font-size:14px;color:#3A4566}.ck-fsum b{display:inline-flex;align-items:center;gap:8px;font-size:16px;font-weight:600;color:#0B1433}.ck-fsum > span{font-weight:600;color:#0B1433}.cb-o b{font-size:19px}.cb-d{display:none}.wf-tot{flex-wrap:wrap}}
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
<sc-if value="{{showBal}}" hint-placeholder-val="{{ true }}"><div class="wf-bal">''' + coin(True) + '''<span><span class="hp-lab">Current balance</span><b>{{bal}} DLP</b></span></div></sc-if>
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
<div class="ck-pl {{plCls}}" role="radiogroup" aria-label="{{planH}}"><sc-for list="{{tiles}}" as="o" hint-placeholder-count="2"><button type="button" role="radio" aria-checked="{{o.on}}" class="wf-o cb-o ck-p {{o.cls}}" onClick="{{o.pick}}"><sc-if value="{{o.hasTag}}" hint-placeholder-val="{{ false }}"><em class="cb-pop">{{o.tag}}</em></sc-if><b>''' + coin() + '''{{o.dlp}}</b><span>{{o.sub}}</span><span class="cb-d">{{o.desc}}</span>''' + CKS + '''</button></sc-for></div>
<sc-if value="{{hasPerks}}" hint-placeholder-val="{{ true }}"><ul class="ck-perks {{perksCls}}" aria-label="Included"><sc-for list="{{perks}}" as="k" hint-placeholder-count="4"><li><i>''' + ck(10, 3.4) + '''</i>{{k.t}}</li></sc-for></ul><button type="button" class="ds-link ck-more" aria-expanded="{{perksExp}}" onClick="{{togglePerks}}">{{perksMore}}</button></sc-if>
<sc-if value="{{hasFit}}" hint-placeholder-val="{{ false }}"><p class="ck-fit {{fitCls}}"><i><sc-if value="{{fitOk}}" hint-placeholder-val="{{ true }}">''' + ck(11, 3.4) + '''</sc-if><sc-if value="{{fitPart}}" hint-placeholder-val="{{ false }}">!</sc-if></i><span>{{fit}}</span></p></sc-if>
<div class="wf-tot"><span>You’ll get</span><b class="ck-get">''' + coin() + '''{{getT}}</b><span class="wf-usd">{{payT}}</span></div>
<div class="cl-foot"><span class="ck-fsum"><b>''' + coin() + '''{{getT}}</b><span>{{payT}}</span></span><sc-if value="{{canBackPlan}}" hint-placeholder-val="{{ false }}"><button type="button" class="cl-bk" aria-label="Back" onClick="{{toAccount}}">''' + BACK + '''</button></sc-if>''' + btn('Choose payment', '#', '', 'onClick="{{toPay}}"', 'button') + '''</div>
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

<sc-if value="{{vOut}}" hint-placeholder-val="{{ false }}">
<main class="ko {{koCls}}">
<div class="ko-emb ob-in" aria-hidden="true"><span class="ko-halo"></span><span class="ko-disc">
<sc-if value="{{oR}}" hint-placeholder-val="{{ true }}"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 3h10M7 21h10"></path><path d="M8 3c0 5 8 5 8 9s-8 4-8 9"></path><path d="M16 3c0 5-8 5-8 9s8 4 8 9"></path></svg></sc-if>
<sc-if value="{{oV}}" hint-placeholder-val="{{ false }}"><svg class="ko-tick" width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5" pathLength="1"></path></svg></sc-if>
<sc-if value="{{oA}}" hint-placeholder-val="{{ false }}"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="6" width="18" height="14" rx="3"></rect><path d="M3 10h18M16 15h2"></path></svg></sc-if>
</span></div>
<sc-if value="{{oV}}" hint-placeholder-val="{{ false }}">
<div class="rc {{rcGo}}" aria-label="Receipt"><span class="cf" aria-hidden="true"><i style="--x:271;--y:-84;--f:438;--d:2.82s;--dl:0.34s;--sw:12px;--sd:0.81s;--fd:0.62s;--rx:-0.39;--r:-57deg"><b><s style="width:5px;height:12px;border-radius:1.5px;background:#1652F0"></s></b></i><i style="--x:61;--y:-94;--f:453;--d:3.38s;--dl:0.38s;--sw:14px;--sd:0.48s;--fd:0.58s;--rx:0.76;--r:73deg"><b><s style="width:5px;height:12px;border-radius:1.5px;background:#1652F0"></s></b></i><i style="--x:177;--y:-104;--f:399;--d:2.88s;--dl:0.27s;--sw:6px;--sd:0.49s;--fd:1.04s;--rx:-0.19;--r:61deg"><b><s style="width:5px;height:12px;border-radius:1.5px;background:#6E96FF"></s></b></i><i style="--x:132;--y:-105;--f:408;--d:2.68s;--dl:0.43s;--sw:10px;--sd:0.83s;--fd:0.84s;--rx:0.92;--r:-80deg"><b><s style="width:5px;height:12px;border-radius:1.5px;background:#F6C343"></s></b></i><i style="--x:-185;--y:-22;--f:478;--d:3.08s;--dl:0.20s;--sw:12px;--sd:0.80s;--fd:0.75s;--rx:-0.83;--r:5deg"><b><s style="width:5px;height:12px;border-radius:1.5px;background:#1652F0"></s></b></i><i style="--x:297;--y:-43;--f:404;--d:2.72s;--dl:0.20s;--sw:13px;--sd:0.53s;--fd:0.97s;--rx:-0.11;--r:-32deg"><b><s style="width:7px;height:7px;border-radius:50%;background:#AFC1F5"></s></b></i><i style="--x:-67;--y:-11;--f:466;--d:3.77s;--dl:0.37s;--sw:15px;--sd:0.46s;--fd:0.69s;--rx:0.99;--r:74deg"><b><s style="width:7px;height:7px;border-radius:50%;background:#6E96FF"></s></b></i><i style="--x:-293;--y:-129;--f:380;--d:3.33s;--dl:0.45s;--sw:9px;--sd:0.48s;--fd:0.71s;--rx:0.27;--r:-77deg"><b><s style="width:5px;height:12px;border-radius:1.5px;background:#3BB273"></s></b></i><i style="--x:-82;--y:-86;--f:428;--d:3.29s;--dl:0.46s;--sw:7px;--sd:0.52s;--fd:1.23s;--rx:0.64;--r:-17deg"><b><s style="width:8px;height:10px;border-radius:1.5px;background:#F6C343"></s></b></i><i style="--x:-218;--y:-61;--f:448;--d:3.07s;--dl:0.33s;--sw:6px;--sd:0.47s;--fd:0.63s;--rx:0.02;--r:-15deg"><b><s style="width:5px;height:12px;border-radius:1.5px;background:#F6C343"></s></b></i><i style="--x:153;--y:-95;--f:470;--d:3.19s;--dl:0.35s;--sw:15px;--sd:0.89s;--fd:0.64s;--rx:-0.04;--r:77deg"><b><s style="width:5px;height:12px;border-radius:1.5px;background:#6E96FF"></s></b></i><i style="--x:-140;--y:-21;--f:381;--d:2.92s;--dl:0.32s;--sw:6px;--sd:0.53s;--fd:0.83s;--rx:0.14;--r:-47deg"><b><s style="width:7px;height:7px;border-radius:50%;background:#6E96FF"></s></b></i><i style="--x:-88;--y:-25;--f:445;--d:3.43s;--dl:0.37s;--sw:7px;--sd:0.47s;--fd:0.56s;--rx:0.82;--r:-1deg"><b><s style="width:8px;height:10px;border-radius:1.5px;background:#1652F0"></s></b></i><i style="--x:-306;--y:-60;--f:453;--d:2.98s;--dl:0.50s;--sw:6px;--sd:0.70s;--fd:1.10s;--rx:0.80;--r:-47deg"><b><s style="width:5px;height:12px;border-radius:1.5px;background:#3BB273"></s></b></i><i style="--x:-94;--y:-54;--f:467;--d:3.10s;--dl:0.43s;--sw:14px;--sd:0.71s;--fd:1.02s;--rx:-0.24;--r:69deg"><b><s style="width:8px;height:10px;border-radius:1.5px;background:#1652F0"></s></b></i><i style="--x:69;--y:-138;--f:479;--d:3.66s;--dl:0.41s;--sw:9px;--sd:0.78s;--fd:0.99s;--rx:-0.12;--r:58deg"><b><s style="width:8px;height:10px;border-radius:1.5px;background:#6E96FF"></s></b></i><i style="--x:-121;--y:-137;--f:475;--d:2.74s;--dl:0.43s;--sw:12px;--sd:0.67s;--fd:1.22s;--rx:-0.26;--r:-44deg"><b><s style="width:7px;height:7px;border-radius:50%;background:#F6C343"></s></b></i><i style="--x:-100;--y:-19;--f:404;--d:3.09s;--dl:0.26s;--sw:12px;--sd:0.81s;--fd:1.12s;--rx:-0.60;--r:-26deg"><b><s style="width:5px;height:12px;border-radius:1.5px;background:#1652F0"></s></b></i><i style="--x:-179;--y:-21;--f:393;--d:3.02s;--dl:0.47s;--sw:6px;--sd:0.48s;--fd:1.29s;--rx:0.64;--r:-52deg"><b><s style="width:7px;height:7px;border-radius:50%;background:#F6C343"></s></b></i><i style="--x:211;--y:-96;--f:447;--d:3.46s;--dl:0.45s;--sw:12px;--sd:0.59s;--fd:1.17s;--rx:-0.44;--r:75deg"><b><s style="width:5px;height:12px;border-radius:1.5px;background:#1652F0"></s></b></i><i style="--x:114;--y:-110;--f:444;--d:3.28s;--dl:0.39s;--sw:10px;--sd:0.54s;--fd:1.13s;--rx:-0.47;--r:-44deg"><b><s style="width:5px;height:12px;border-radius:1.5px;background:#1652F0"></s></b></i><i style="--x:309;--y:-133;--f:433;--d:3.37s;--dl:0.30s;--sw:6px;--sd:0.54s;--fd:1.17s;--rx:-0.49;--r:-78deg"><b><s style="width:7px;height:7px;border-radius:50%;background:#F6C343"></s></b></i><i style="--x:-175;--y:-40;--f:474;--d:3.20s;--dl:0.50s;--sw:7px;--sd:0.83s;--fd:1.07s;--rx:-0.55;--r:25deg"><b><s style="width:5px;height:12px;border-radius:1.5px;background:#1652F0"></s></b></i><i style="--x:-236;--y:-86;--f:470;--d:3.05s;--dl:0.36s;--sw:14px;--sd:0.81s;--fd:1.26s;--rx:-0.07;--r:-28deg"><b><s style="width:8px;height:10px;border-radius:1.5px;background:#6E96FF"></s></b></i><i style="--x:142;--y:-35;--f:451;--d:2.86s;--dl:0.47s;--sw:15px;--sd:0.89s;--fd:0.95s;--rx:0.58;--r:2deg"><b><s style="width:8px;height:10px;border-radius:1.5px;background:#0F6B45"></s></b></i><i style="--x:262;--y:-30;--f:388;--d:3.13s;--dl:0.36s;--sw:13px;--sd:0.67s;--fd:0.57s;--rx:0.62;--r:-64deg"><b><s style="width:5px;height:12px;border-radius:1.5px;background:#1652F0"></s></b></i><i style="--x:191;--y:-125;--f:458;--d:2.77s;--dl:0.23s;--sw:11px;--sd:0.78s;--fd:1.18s;--rx:0.38;--r:46deg"><b><s style="width:5px;height:12px;border-radius:1.5px;background:#6E96FF"></s></b></i><i style="--x:165;--y:-88;--f:463;--d:3.27s;--dl:0.23s;--sw:11px;--sd:0.86s;--fd:0.74s;--rx:0.34;--r:76deg"><b><s style="width:5px;height:12px;border-radius:1.5px;background:#F6C343"></s></b></i><i style="--x:-125;--y:-130;--f:407;--d:3.20s;--dl:0.31s;--sw:7px;--sd:0.45s;--fd:0.83s;--rx:0.08;--r:-69deg"><b><s style="width:5px;height:12px;border-radius:1.5px;background:#1652F0"></s></b></i><i style="--x:-241;--y:-136;--f:473;--d:3.15s;--dl:0.47s;--sw:14px;--sd:0.63s;--fd:0.73s;--rx:-0.01;--r:6deg"><b><s style="width:7px;height:7px;border-radius:50%;background:#1652F0"></s></b></i><i style="--x:256;--y:-19;--f:432;--d:2.73s;--dl:0.31s;--sw:6px;--sd:0.57s;--fd:1.08s;--rx:0.95;--r:-71deg"><b><s style="width:8px;height:10px;border-radius:1.5px;background:#F6C343"></s></b></i><i style="--x:-220;--y:-148;--f:452;--d:2.89s;--dl:0.34s;--sw:10px;--sd:0.71s;--fd:1.19s;--rx:0.25;--r:-30deg"><b><s style="width:5px;height:12px;border-radius:1.5px;background:#1652F0"></s></b></i><i style="--x:-305;--y:-61;--f:441;--d:3.25s;--dl:0.46s;--sw:11px;--sd:0.55s;--fd:0.71s;--rx:0.09;--r:70deg"><b><s style="width:8px;height:10px;border-radius:1.5px;background:#AFC1F5"></s></b></i><i style="--x:-171;--y:-46;--f:470;--d:2.98s;--dl:0.28s;--sw:15px;--sd:0.55s;--fd:1.30s;--rx:0.78;--r:-46deg"><b><s style="width:8px;height:10px;border-radius:1.5px;background:#F6C343"></s></b></i></span><div class="rc-slot" aria-hidden="true"><i></i></div><div class="rc-clip"><div class="rc-paper">
<div class="rc-top"><div><span class="rc-k">Payment successful</span><b class="rc-amt">{{today}}</b><span class="rc-m">27 Sep 2026 · Visa •••• 4242</span></div><span class="rc-stamp" aria-hidden="true"><img src="/_blob/f81e36d31295a0d0737959589ec1abd4" alt=""><em>Paid</em></span></div>
<ul class="rc-l"><sc-for list="{{rcItems}}" as="it" hint-placeholder-count="2"><li><span>{{it.t}}</span><span>{{it.v}}</span></li></sc-for></ul>
<div class="rc-tot"><span>Total</span><b>{{today}}</b></div>
<div class="rc-ft"><span>{{rcFoot}}</span><a href="#" class="ds-link">Download</a></div>
</div></div></div>
</sc-if>
<span class="ko-pill ob-in2">{{oPill}}</span>
<h1 class="lp-h1 ko-h ob-in2">{{oH}}</h1>
<p class="ko-sub ob-in2">{{oSub}}</p>
<sc-if value="{{oR}}" hint-placeholder-val="{{ true }}">
<section class="ko-card wo-one ob-in3" aria-label="What happens next"><span class="sec-h">What happens next</span><ol class="ko-path"><li class="ko-done"><span class="ko-dot"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg></span><span><b>Payment sent</b><span>{{today}} by Visa •••• 4242</span></span></li><li class="ko-now"><span class="ko-dot"></span><span><b>Bank confirms</b><span>Usually under a minute</span></span></li><li><span class="ko-dot"></span><span><b>{{landT}}</b><span>{{landS}}</span></span></li></ol></section>
</sc-if>
<sc-if value="{{oA}}" hint-placeholder-val="{{ false }}">
<section class="ko-card wo-one ob-in3" aria-label="Other ways to pay"><span class="sec-h">Other ways to pay</span><div class="ko-opts"><a href="#" class="ko-opt" onClick="{{toLocal}}"><span class="ko-oi"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="7" y="2.5" width="10" height="19" rx="2.5"></rect><path d="M11 18h2"></path></svg></span><span><b>Local payment</b><span>Bank app, USSD or mobile money.</span></span><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"></path></svg></a><a href="#" class="ko-opt" onClick="{{toPayBack}}"><span class="ko-oi"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="6" width="18" height="14" rx="3"></rect><path d="M3 10h18M16 15h2"></path></svg></span><span><b>A different card</b><span>Or pay from your TruVault.</span></span><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"></path></svg></a></div></section>
<div class="ko-cta ob-in4">''' + btn('Try this card again', '#', '', 'onClick="{{pay}}"', 'button') + '''</div>
</sc-if>
<sc-if value="{{oV}}" hint-placeholder-val="{{ false }}">
<section class="ko-next rc-nx ob-in4" aria-label="Next for you"><span class="ko-ni">''' + ic(I_PATH, 20, 1.9) + '''</span><span class="ko-nt"><span class="ko-nl">Next for you</span><b>{{nxH}}</b><span>{{nxP}}</span></span>''' + btn('{{nextL}}', '{{nextH}}', 'sm ko-go') + '''</section>
</sc-if>
<div class="ko-links ob-in4"><a href="{{l1h}}">{{l1}}</a><span aria-hidden="true">·</span><a href="{{l2h}}">{{l2}}</a></div>
</main>
</sc-if>
<div class="{{sceneCls}}" aria-hidden="true"></div>
</div>'''

JS = r'''
class Component extends DCLogic {
  constructor(props) {
    super(props); var p = props || {};
    this.state = { step: p.step || 'plan', plan: p.plan || 'pro', pkg: p.from === 'course' ? 500 : 1000, method: 'card', email: '', go: true };
  }
  componentDidMount() {
    if (typeof IntersectionObserver !== 'function') return;
    var self = this, shown = true;
    this.io = new IntersectionObserver(function (es) {
      var r = es[es.length - 1].intersectionRatio;
      if (r >= 0.5 && !shown) { shown = true; self.setState({ go: false }, function () { requestAnimationFrame(function () { requestAnimationFrame(function () { self.setState({ go: true }); }); }); }); }
      else if (r < 0.05) shown = false;
    }, { threshold: [0, 0.05, 0.5] });
    this.io.observe(document.body);
  }
  componentWillUnmount() { clearTimeout(this._t); if (this.io) this.io.disconnect(); }
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
    var CTX = { pricing: ['Create your account, then confirm your plan. It takes about a minute.', 'Then a few quick questions'], onboarding: ['You chose Pro while building your journey. Set up your plan, then start learning.', 'Then back to your journey'],
      allowance: ['Upgrade to keep going with your Data Analyst journey. Your progress is saved.', 'Then back to SQL for Data Analysis'], path: ['Pick the plan that fits your Data Analyst path. The whole path needs about 3,800 DLP.', 'Then back to the Data Analyst path'],
      account: ['Change your plan. The new allowance starts straight away.', 'Then back to your allowance'], course: ['Add the DLP you need for Advanced Analytics with Python. Your plan stays the same.', 'Then back to your course'] }[from] || ['', ''];
    var NEXT = { pricing: ['Personalise Credalio', 'OnbAbout.dc.html'], onboarding: ['Start my journey', 'Dash-R.dc.html'], allowance: ['Continue to SQL for Data Analysis', 'Dash-E.dc.html'], path: ['Back to the Data Analyst path', 'PathDetail-Learner.dc.html'], account: ['Back to my allowance', 'Usage.dc.html'], course: ['Back to the course', 'CourseDetail-Learner.dc.html'] }[from];
    var base = { course: 150, allowance: 0 }[from]; if (base === undefined) base = 200;
    var pl = P[S.plan] || P.pro, price = top ? TOP[S.pkg] : pl.price, add = top ? S.pkg : pl.dlp;
    var go = function (s) { return function (e) { if (e && e.preventDefault) e.preventDefault(); self.setState({ step: s }); }; };
    var tiles = top ? [500, 1000, 2500].map(function (n) { var on = S.pkg === n; return { dlp: f(n), sub: 'DLP · $' + TOP[n] + ' one time', desc: 'About ' + (n / 100) + ' hours of learning', on: on ? 'true' : 'false', cls: on ? 'xb-on' : '', hasTag: n === 1000, tag: 'Most chosen', pick: function () { self.setState({ pkg: n }); } }; })
      : ['basic', 'pro'].map(function (k) { var q = P[k], on = S.plan === k; return { dlp: f(q.dlp), sub: q.name + ' · $' + q.price + ' a month', desc: 'DLP every month · about ' + q.hrs + ' learning hours', on: on ? 'true' : 'false', cls: on ? 'xb-on' : '', hasTag: k === 'pro', tag: 'Best for career paths', pick: function () { self.setState({ plan: k }); } }; });
    var ME = [['card', 'Card', 'Visa, Mastercard, Verve'], ['local', 'Local payment', 'Bank app, USSD or mobile money'], ['mforge', 'MFORGE', 'Pay from your TruVault']];
    return {
      barT: top ? 'Add DLP' : 'Your plan', closeHref: NEXT[1], glowCls: '',
      showFlow: ['account', 'plan', 'pay', 'review'].indexOf(st) > -1, vAccount: st === 'account', showBal: st !== 'account', vPlan: st === 'plan', vPay: st === 'pay', vReview: st === 'review', vOut: ['processing', 'done', 'failed'].indexOf(st) > -1, sceneCls: ['done', 'failed'].indexOf(st) > -1 ? 'tk-scene lo' : 'tk-scene', oR: st === 'processing', oV: st === 'done', oA: st === 'failed',
      koCls: { processing: 'ko-r', done: 'ko-v ko-rc', failed: 'ko-a' }[st] || '', rcGo: S.go ? 'rc-go' : '',
      toLocal: function (e) { if (e) e.preventDefault(); self.setState({ step: 'pay', method: 'local' }); },
      rcItems: (top ? [[f(add) + ' DLP top-up', '$' + price + '.00']] : [[pl.name + ' plan · monthly', '$' + price + '.00'], [f(add) + ' DLP each month', 'Included']]).map(function (x) { return { t: x[0], v: x[1] }; }),
      rcFoot: top ? 'New balance ' + f(base + add) + ' DLP' : 'Next payment 27 Oct',
      landT: top ? 'DLP lands' : 'Plan starts', landS: top ? f(add) + ' in your balance' : f(add) + ' DLP in your balance',
      l1: 'Usage and activity', l1h: 'Usage.dc.html', l2: st === 'failed' ? 'Contact support' : 'Dashboard', l2h: st === 'failed' ? '#' : 'Dash-E.dc.html',
      h1: top ? 'Add DLP' : (signedOut ? 'Get ' + pl.name : 'Choose your plan'), ctx: CTX[0], ret: CTX[1], hasRet: !!CTX[1], bal: f(base),
      steps: flow.map(function (t, i) { return { t: t, cls: i < idx ? 'dn' : (i === idx ? 'on' : '') }; }),
      email: S.email, onEmail: function (e) { self.setState({ email: e.target.value }); }, toPlan: go('plan'), toAccount: go('account'), canBackPlan: signedOut && !top,
      planH: top ? 'How much DLP?' : 'Which plan?', plCls: top ? 'n3' : '', tiles: tiles,
      hasPerks: !top, perks: (top ? [] : pl.perks).map(function (t) { return { t: t }; }), perksCls: S.perksAll ? 'all' : '', perksExp: S.perksAll ? 'true' : 'false', perksMore: S.perksAll ? 'Show less' : 'Everything in ' + pl.name + ' (' + pl.perks.length + ')', togglePerks: function () { self.setState({ perksAll: !S.perksAll }); },
      getT: f(add) + ' DLP' + (top ? '' : ' a month'), payT: '$' + price + '.00' + (top ? '' : ' a month'),
      today: '$' + price + '.00', then: top ? 'One time · your plan stays the same' : 'then $' + price + ' every month',
      toPay: go('pay'), toPlanBack: go('plan'), toReview: go('review'), toPayBack: go('pay'),
      methods: ME.map(function (m, i) { var on = S.method === m[0]; var v = { t: m[1], d: m[2], on: on ? 'true' : 'false', cls: on ? 'xb-on' : '', pick: function () { self.setState({ method: m[0] }); } }; for (var j = 0; j < 3; j++) v['i' + j] = j === i ? 'inline' : 'none'; return v; }),
      isCard: S.method === 'card', isOther: S.method !== 'card', otherNote: S.method === 'local' ? 'After you review, we’ll show you how to finish in your bank app or by USSD.' : 'After you review, approve the payment in TruVault.',
      rvK: top ? 'Top-up' : 'Plan', rvV: top ? 'One time' : pl.name, rvK2: top ? 'You’ll get' : 'Each month', rvV2: f(add) + ' DLP', isSub: !top, rvThen: '$' + price + ' every month from 27 October',
      totTip: top ? 'Added to your balance straight away. Your plan stays the same.' : 'Cancel anytime from your account. You keep your DLP until the end of the month.',
      payLabel: top ? 'Pay $' + price + ' and add DLP' : 'Pay $' + price + ' and start ' + pl.name,
      pay: function () { self.setState({ step: 'processing' }); clearTimeout(self._t); self._t = setTimeout(function () { self.setState({ step: 'done' }); }, 1800); },
      hasFit: (!top && (from === 'path' || from === 'allowance')) || (top && from === 'course'), fitOk: !(from === 'path' && S.plan === 'basic'), fitPart: from === 'path' && S.plan === 'basic', fitCls: (from === 'path' && S.plan === 'basic') ? 'part' : '',
      fit: top ? (S.pkg >= 250 ? 'You need 250 more for this course. ' + f(S.pkg) + ' covers it, with ' + f(S.pkg - 250) + ' to spare.' : '') : from === 'allowance' ? (S.plan === 'basic' ? 'Stage 2 needs about 1,400 DLP. Basic covers it, with room to spare.' : 'Pro covers Stage 2 and most of what comes after it.') : (S.plan === 'basic' ? 'The path needs about 3,800 DLP. Basic covers it over about two months.' : 'The path needs about 3,800 DLP. Pro covers it in your first month.'),
      oPill: { processing: 'Processing', failed: 'Not charged' }[st] || (top ? 'Added' : ((from === 'path' || from === 'account') ? 'Plan updated' : 'Plan active')),
      oH: st === 'processing' ? 'Processing your payment' : (st === 'failed' ? 'Your payment didn’t go through' : (top ? f(add) + ' DLP added' : 'You’re on ' + pl.name)),
      oSub: st === 'processing' ? 'We’re waiting for your bank. You can leave this page, and you won’t be charged twice.' : (st === 'failed' ? 'Your bank declined the $' + price + '.00 charge on Visa •••• 4242.' : (top ? 'It’s in your balance and ready to use. Your plan stays the same.' : f(add) + ' DLP is in your balance and ready to use.')),
      nxH: { pricing: 'Make Credalio yours', onboarding: 'Start your journey', allowance: 'Back to your journey', path: 'Back to the Data Analyst path', account: 'Your new allowance', course: 'Back to Advanced Analytics with Python' }[from],
      nxP: { pricing: 'A few quick questions so your AI Coach can help from day one.', onboarding: 'Your Data Analyst journey is ready. Stage 1 is covered.', allowance: 'SQL for Data Analysis is next, and your new DLP covers it.', path: 'The whole path is covered at your new allowance.', account: 'See what you have and what’s coming up.', course: 'You’re covered for the course now.' }[from],
      nextL: NEXT[0], nextH: NEXT[1]
    };
  }
}
'''

PROPS = {"plan": {"editor": "enum", "options": ["basic", "pro", "topup"], "default": "pro"},
         "from": {"editor": "enum", "options": ["pricing", "onboarding", "allowance", "path", "account", "course"], "default": "onboarding"},
         "step": {"editor": "enum", "options": ["account", "plan", "pay", "review", "processing", "done", "failed"], "default": "plan"},
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
