# Learner dashboard (LRN-*): one responsive source, states as variants.
# Usage: python3 dashgen.py  -> writes design/canvas3/project/Dashboard.dc.html
# Never re-run over a live file the designer has edited; patch the live file instead.
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from kit import KIT_CSS, AUR_CSS, AURORA_JS, ARROW, CLOSE, NOVA, btn, tip, coin, ck, think

OUT = os.path.join(HERE, '../../canvas3/project/Dashboard.dc.html')

def ic(d, s=20, sw=1.8):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (s, s, sw, d)

I = {
 'dash': '<rect x="3.5" y="3.5" width="7" height="7" rx="2"></rect><rect x="13.5" y="3.5" width="7" height="7" rx="2"></rect><rect x="3.5" y="13.5" width="7" height="7" rx="2"></rect><rect x="13.5" y="13.5" width="7" height="7" rx="2"></rect>',
 'explore': '<circle cx="12" cy="12" r="9"></circle><path d="m15.5 8.5-2 5-5 2 2-5z"></path>',
 'learn': '<path d="M2.5 5.5C5 4 8.5 4 12 6c3.5-2 7-2 9.5-.5V19c-2.5-1.5-6-1.5-9.5.5-3.5-2-7-2-9.5-.5z"></path><path d="M12 6v13.5"></path>',
 'assign': '<rect x="5" y="4" width="14" height="17" rx="2"></rect><path d="M9 3.5h6v3H9zM9 12h6M9 16h4"></path>',
 'cal': '<rect x="3" y="5" width="18" height="16" rx="2"></rect><path d="M3 10h18M8 3v4M16 3v4"></path>',
 'pack': '<path d="M6 8h12a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2v-9a2 2 0 0 1 2-2z"></path><path d="M9 8V6a3 3 0 0 1 6 0v2M4 13h16M11 13v2h2v-2"></path>',
 'reward': '<path d="M8 4h8v5a4 4 0 0 1-8 0z"></path><path d="M8 6H5a3 3 0 0 0 3 4M16 6h3a3 3 0 0 1-3 4M12 13v4M8.5 21h7M10 17h4"></path>',
 'wallet': '<rect x="3" y="6" width="18" height="14" rx="3"></rect><path d="M3 10h18M16 15h2"></path>',
 'comm': '<circle cx="9" cy="8" r="3.5"></circle><path d="M2.5 20a6.5 6.5 0 0 1 13 0"></path><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14.5a6.5 6.5 0 0 1 3.5 5.5"></path>',
 'msg': '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"></path>',
 'help': '<circle cx="12" cy="12" r="9"></circle><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6v.6M12 17h.01"></path>',
 'settings': '<circle cx="12" cy="12" r="3"></circle><path d="M12 2.5v2.2M12 19.3v2.2M4.6 4.6l1.6 1.6M17.8 17.8l1.6 1.6M2.5 12h2.2M19.3 12h2.2M4.6 19.4l1.6-1.6M17.8 6.2l1.6-1.6"></path>',
 'search': '<circle cx="11" cy="11" r="7"></circle><path d="m20 20-3.5-3.5"></path>',
 'bell': '<path d="M18 16V11a6 6 0 1 0-12 0v5l-2 2h16z"></path><path d="M10 21h4"></path>',
 'menu': '<path d="M4 7h16M4 12h16M4 17h16"></path>',
 'lock': '<rect x="5" y="10.5" width="14" height="10" rx="2.5"></rect><path d="M8.5 10.5V8a3.5 3.5 0 0 1 7 0v2.5"></path>',
 'cred': '<circle cx="12" cy="9" r="6"></circle><path d="m8.5 13.8-1.5 7.2 5-3 5 3-1.5-7.2"></path>',
 'proj': '<rect x="3" y="4" width="18" height="16" rx="2.5"></rect><path d="M3 9h18M8 13h3M8 16h6"></path>',
 'skill': '<path d="M12 3l2.6 5.6 6.1.7-4.5 4.2 1.2 6L12 16.6 6.6 19.5l1.2-6-4.5-4.2 6.1-.7z"></path>',
 'path': '<circle cx="6" cy="19" r="2.5"></circle><circle cx="18" cy="5" r="2.5"></circle><path d="M8.5 19H16a3.5 3.5 0 0 0 0-7H8a3.5 3.5 0 0 1 0-7h7.5"></path>',
 'cert': '<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"></path><path d="m9 12 2 2 4-4"></path>',
 'prog': '<rect x="3" y="5" width="18" height="16" rx="2"></rect><path d="M3 10h18M8 3v4M16 3v4M7.5 14h3M7.5 17h6"></path>',
 'send': '<path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path>',
}
ARR_S = ic('<path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path>', 16, 2.2)

NAV = [(None, [('dash', 'Dashboard', 'Dashboard.dc.html'), ('explore', 'Explore learning', 'Explore.dc.html')]),
       ('Learning', [('learn', 'My learning', '#'), ('assign', 'Assignments', '#'), ('cal', 'Schedule', '#')]),
       ('Proof', [('pack', 'Digital Backpack', '#')]),
       ('Rewards', [('reward', 'Learning rewards', '#'), ('wallet', 'Wallets', '#')]),
       ('People', [('comm', 'Community', '#'), ('msg', 'Messages', '#')])]

def sidebar():
    h = ''
    for g, items in NAV:
        if g: h += '<span class="ds-glab">%s</span>' % g
        for k, label, href in items:
            on = label == 'Dashboard'
            bad = '<sc-if value="{{hasAsg}}" hint-placeholder-val="{{ false }}"><span class="ds-badge" aria-label="{{asgN}} due soon">{{asgN}}</span></sc-if>' if label == 'Assignments' else ''
            h += '<a href="%s" class="ds-item%s"%s>%s<span>%s</span>%s</a>' % (href, ' ds-on' if on else '', ' aria-current="page"' if on else '', ic(I[k], 19), label, bad)
    return h

CSS = r'''body{margin:0;background:#F7F9FD}
h1,h2,h3,p{text-wrap:pretty}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.ds-root{display:grid;grid-template-columns:264px minmax(0,1fr);min-height:100vh;background:#F7F9FD;font-family:'Google Sans','Google Sans Text','Helvetica Neue',system-ui,sans-serif;color:#0B1433}
.ds-side{position:sticky;top:0;height:100vh;overflow-y:auto;box-sizing:border-box;padding:22px 14px 18px 14px;background:#FFFFFF;border-right:1.5px solid #E6EAF3;display:flex;flex-direction:column;gap:2px;z-index:20}
.ds-glab{display:block;margin:14px 12px 6px 12px;font-size:12px;font-weight:600;color:#8A93AD}
.ds-item{display:flex;align-items:center;gap:12px;min-height:40px;padding:0 12px;border-radius:12px;color:#3A4566;font-size:14.5px;font-weight:500;text-decoration:none;background:none;border:0;font-family:inherit;text-align:left;cursor:pointer;transition:background .2s ease,color .2s ease}
.ds-item svg{flex-shrink:0;color:#5B6582}
.ds-item:hover{background:#F5F8FF;color:#0B1433}
.ds-on{background:#EAF0FF !important;color:#0E3BB8 !important;font-weight:600}
.ds-on svg{color:#1652F0}
.ds-top{position:sticky;top:0;z-index:10;height:72px;box-sizing:border-box;padding:0 clamp(20px,3vw,40px);display:flex;align-items:center;gap:12px;background:rgba(247,249,253,.88);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}
.ds-search{flex:1 1 auto;max-width:440px;height:44px;box-sizing:border-box;display:flex;align-items:center;gap:10px;padding:0 16px;border-radius:999px;background:#FFFFFF;border:1.5px solid #E6EAF3;color:#8A93AD;font-size:14px}
.ds-search input{border:0;outline:none;background:transparent;font-family:inherit;font-size:14px;color:#0B1433;flex-grow:1;min-width:0}
.ds-search input::placeholder{color:#8A93AD}
.ds-icon-btn{width:44px;height:44px;flex-shrink:0;box-sizing:border-box;border-radius:50%;border:1.5px solid #E6EAF3;background:#FFFFFF;color:#3A4566;display:flex;align-items:center;justify-content:center;cursor:pointer;position:relative;text-decoration:none}
.ds-icon-btn:hover{border-color:#AFC1F5}
.ds-main{box-sizing:border-box;width:100%;max-width:1200px;padding:12px clamp(20px,3vw,40px) 56px clamp(20px,3vw,40px)}
.ds-menu,.ds-scrim,.ds-mlogo,.ds-close,.lr-acct{display:none}
.lr-acct .cs-cav{width:26px;height:26px;font-size:10px;margin-left:-3px}
.ds-item:focus-visible,.ds-icon-btn:focus-visible,.lr-pill:focus-visible,.lr-coach:focus-visible,.lr-av:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:2px}
.lr-word{display:block;height:26px;aspect-ratio:292/56;background:url(/_blob/8acabcff7ece53343d63205e8b7321a2) left center/contain no-repeat}
.lr-logo{display:flex;align-items:center;padding:4px 12px 18px;text-decoration:none}
.lr-sfoot{margin-top:auto;padding-top:14px;display:flex;flex-direction:column;gap:2px}
.lr-plan{margin:0 4px 10px;padding:14px 14px 14px 16px;border-radius:16px;background:#F5F8FF;border:1.5px solid #E6EAF3;display:flex;align-items:center;justify-content:space-between;gap:10px}
.lr-plan b{display:block;font-size:14px;font-weight:600}
.lr-plan span{display:block;margin-top:2px;font-size:12.5px;color:#5B6582}
.lr-plan .ds-link{font-size:13.5px}
.lr-pill{height:44px;flex-shrink:0;box-sizing:border-box;display:inline-flex;align-items:center;gap:8px;padding:0 14px 0 10px;border-radius:999px;background:#FFFFFF;border:1.5px solid #E6EAF3;font-size:14.5px;font-weight:600;color:#0B1433;text-decoration:none;transition:border-color .2s ease}
.lr-pill:hover{border-color:#AFC1F5}
.lr-pill i{font-style:normal;font-weight:500;color:#5B6582}
.lr-coach{height:44px;flex-shrink:0;box-sizing:border-box;display:inline-flex;align-items:center;gap:9px;padding:0 16px 0 5px;border-radius:999px;border:1.5px solid #DCE5FB;background:#FFFFFF url(NOVABG) center / cover no-repeat;font-family:inherit;font-size:14.5px;font-weight:600;color:#0B1433;cursor:pointer;transition:border-color .2s ease,box-shadow .2s ease}
.lr-coach:hover{border-color:#9DB8F7;box-shadow:0 8px 20px -10px rgba(22,82,240,.45)}
.lr-coach .nv-av{width:32px;height:32px}
.lr-dot{position:absolute;right:10px;top:9px;width:8px;height:8px;border-radius:50%;background:#1652F0;box-shadow:0 0 0 2px #FFFFFF}
.lr-av{width:44px;height:44px;flex-shrink:0;border-radius:999px;background:#DCE5FB;color:#1652F0;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:600;text-decoration:none}
.lr-head{display:flex;align-items:flex-end;justify-content:space-between;gap:24px;margin:8px 0 22px}
.lr-date{display:block;font-size:13.5px;font-weight:500;color:#8A93AD}
.lr-h1{margin:6px 0 0;font-size:clamp(28px,2.5vw,36px);line-height:1.15;font-weight:600;letter-spacing:-.03em}
.lr-strip{display:flex;align-items:stretch;background:#FFFFFF;border:1.5px solid #E6EAF3;border-radius:16px;flex-shrink:0}
.lr-st{display:flex;flex-direction:column;justify-content:center;gap:3px;padding:10px 18px;min-width:0;text-decoration:none;color:#0B1433}
.lr-st + .lr-st{border-left:1px solid #EEF1F7}
.lr-st small{font-size:12px;color:#5B6582;white-space:nowrap}
.lr-st b{display:flex;align-items:center;gap:6px;font-size:16px;font-weight:600;white-space:nowrap}
.lr-gs{display:flex;align-items:center;gap:14px;padding:10px 16px 10px 18px;background:#FFFFFF;border:1.5px solid #E6EAF3;border-radius:16px}
.lr-gs-t{font-size:13px;color:#5B6582;white-space:nowrap}
.lr-gs-t b{display:block;font-size:14.5px;font-weight:600;color:#0B1433}
.lr-gs ol{display:flex;gap:6px;margin:0;padding:0;list-style:none}
.lr-gs li{display:flex}
.lr-gs-s{display:inline-flex;align-items:center;gap:7px;height:34px;padding:0 12px 0 6px;border-radius:999px;border:1.5px solid #E6EAF3;background:#FFFFFF;font-family:inherit;font-size:13px;font-weight:500;color:#3A4566;white-space:nowrap;text-decoration:none;cursor:pointer}
.lr-gs-s i{width:22px;height:22px;border-radius:999px;box-sizing:border-box;border:1.5px solid #CBD3E6;display:flex;align-items:center;justify-content:center;color:#FFFFFF}
.lr-gs-s.done{border-color:transparent;background:#E7F5EE;color:#0F6B45;cursor:default}
.lr-gs-s.done i{background:#0F6B45;border-color:#0F6B45}
.lr-gs-s.next{border-color:#1652F0;color:#0E3BB8;background:#F5F8FF}
.lr-gs-s.next i{border-color:#1652F0}
a.lr-gs-s.next:hover,button.lr-gs-s.next:hover{background:#EAF0FF}
.lr-focus{position:relative;border-radius:24px;padding:40px 44px;box-sizing:border-box;border:1.5px solid #DCE5FB;box-shadow:0 30px 60px -44px rgba(22,82,240,.4)}
.lr-disc{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:40px;align-items:center}
.lr-k{display:flex;align-items:center;gap:8px;font-size:13.5px;font-weight:500;color:#1652F0}
.lr-ft{margin:10px 0 0;font-size:40px;line-height:1.08;font-weight:600;letter-spacing:-.035em}
.lr-fs{margin:12px 0 0;max-width:560px;font-size:16px;line-height:1.55;color:#3A4566}
.lr-ask{margin-top:26px;max-width:620px}
.lr-chips{display:flex;align-items:center;gap:8px;margin-top:16px;flex-wrap:wrap}
.lr-chips small{font-size:13px;color:#5B6582;margin-right:4px}
.lr-chips .ds-chip,.lr-qs .ds-chip{text-decoration:none}
.lr-chips .ds-chip{background:rgba(255,255,255,.8)}
.lr-nv{position:relative;padding:22px;border-radius:20px;background:rgba(255,255,255,.82);border:1.5px solid #FFFFFF;box-shadow:0 24px 50px -36px rgba(11,20,51,.45);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}
.lr-nvh{display:flex;align-items:center;gap:12px}
.lr-nvh b{display:block;font-size:15px;font-weight:600}
.lr-nvh span{display:block;font-size:12.5px;color:#5B6582}
.lr-nv p{margin:14px 0 16px;font-size:15px;line-height:1.5;color:#0B1433}
.lr-jy{padding:34px 40px 30px}
.lr-jy .jy-jh{display:flex;align-items:flex-end;justify-content:space-between;gap:24px;flex-wrap:wrap}
.lr-jy .jy-jk{display:flex;align-items:center;gap:8px;font-size:13.5px;font-weight:500;color:#1652F0}
.lr-jy .jy-jt{display:block;margin-top:6px;font-size:36px;font-weight:600;letter-spacing:-1px;line-height:1.1}
.lr-jy .jy-jm{display:flex;gap:8px;flex-wrap:wrap}
.lr-jy .jy-jr{position:relative;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));margin:30px 0 0;padding:0;list-style:none}
.lr-jy .jy-jr::before{content:"";position:absolute;left:10%;right:10%;top:17px;height:2px;background:linear-gradient(90deg,#1652F0,#C9D7FA)}
.lr-jy .jy-js{position:relative;display:flex;flex-direction:column;align-items:center;gap:6px;text-align:center}
.lr-jy .jy-jn{width:36px;height:36px;border-radius:999px;background:#FFFFFF;border:2px solid #9DB8F7;color:#1652F0;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:600;box-sizing:border-box;margin-bottom:6px}
.lr-jy .jy-js.now .jy-jn{background:#1652F0;border-color:#1652F0;color:#FFFFFF;box-shadow:0 0 0 6px rgba(22,82,240,.14)}
.lr-jy .jy-js.done .jy-jn{background:#0F6B45;border-color:#0F6B45;color:#FFFFFF}
.lr-jy .jy-js.end .jy-jn{background:#0B1433;border-color:#0B1433;color:#FFFFFF}
.lr-jy .jy-jl{font-size:15px;font-weight:600}
.lr-jy .jy-jd{font-size:12px;color:#4A5578}
.lr-jf{display:flex;align-items:center;justify-content:space-between;gap:20px;margin-top:28px;padding-top:22px;border-top:1px solid rgba(22,82,240,.14)}
.lr-ok{display:flex;align-items:center;gap:10px;font-size:14.5px;color:#0B1433}
.lr-ok i{width:24px;height:24px;border-radius:999px;background:#0F6B45;color:#FFFFFF;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.lr-ok b{font-weight:600}
.lr-jf .ds-acts{margin:0}
.lr-sec{margin-top:36px}
.lr-sh{display:flex;align-items:flex-end;justify-content:space-between;gap:16px;margin-bottom:16px}
.lr-sh h2{margin:0;font-size:22px;font-weight:600;letter-spacing:-.4px}
.lr-sh p{margin:4px 0 0;font-size:14px;color:#5B6582}
.lr-g4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px}
.cs-card{position:relative;display:flex;flex-direction:column;border-radius:18px;background:#FFFFFF;border:1.5px solid #E6EAF3;box-shadow:0 22px 44px -38px rgba(11,20,51,.45);text-decoration:none;color:#0B1433;transition:transform .45s cubic-bezier(.2,.7,.2,1),box-shadow .45s ease,border-color .3s ease}
.cs-card:hover{transform:translateY(-4px);border-color:#D6DDEE;box-shadow:0 34px 60px -38px rgba(22,82,240,.45)}
.cs-card:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:2px}
.cs-th{position:relative;height:112px;overflow:hidden;border-radius:16.5px 16.5px 0 0;display:flex;align-items:flex-start;justify-content:space-between;padding:14px;box-sizing:border-box}
.cs-th::before{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.18) 1px,transparent 1.3px);background-size:12px 12px}
.cs-ico{position:absolute;right:-12px;bottom:-16px;width:116px;height:116px;opacity:.22}
.cs-cb{display:flex;flex-direction:column;gap:12px;padding:16px 16px 0;flex:1}
.cs-ct{font-size:16px;font-weight:600;letter-spacing:-.25px;line-height:1.3;min-height:42px;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.cs-by{display:flex;align-items:center;gap:8px;font-size:13px;color:#3A4566}
.cs-cav{width:24px;height:24px;border-radius:999px;background:#DCE5FB;color:#1652F0;display:flex;align-items:center;justify-content:center;font-size:9.5px;font-weight:600;flex-shrink:0}
.cs-meta{display:flex;align-items:center;flex-wrap:wrap;gap:6px;font-size:13px;color:#5B6582}
.cs-meta b{font-weight:600;color:#0B1433}
.cs-star{color:#0B1433}
.cs-dot{width:3px;height:3px;border-radius:9px;background:#CBD3E6}
.cs-tags{display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.cs-tdot{width:10px;height:10px;border-radius:999px;flex-shrink:0}
.cs-acc{margin-top:auto;display:flex;flex-direction:column;gap:8px;padding:14px 16px 16px;box-sizing:border-box;margin-left:-16px;margin-right:-16px;border-top:1px solid #EEF1F7}
.cs-ar{display:flex;align-items:center;font-size:14px;color:#5B6582}
.cs-ar b{display:inline-flex;align-items:center;gap:6px;font-weight:600;color:#0B1433}
.lr-why{display:flex;align-items:flex-start;gap:7px;font-size:13px;line-height:1.4;color:#3A4566}
.lr-why .nv-av{width:20px;height:20px;margin-top:-1px}
.lr-nova{display:flex;align-items:center;gap:22px;padding:26px 28px;border-radius:22px;border:1.5px solid #DCE5FB}
.lr-nova .nv-av{width:64px;height:64px;box-shadow:0 0 0 3px #FFFFFF,0 0 0 4.5px #D6DDEE}
.lr-nova-b{flex:1;min-width:0}
.lr-nova-k{font-size:13px;font-weight:500;color:#1652F0}
.lr-nova-b p{margin:4px 0 0;font-size:17px;line-height:1.45;font-weight:500;letter-spacing:-.1px}
.lr-nova-a{display:flex;align-items:center;gap:18px;flex-shrink:0}
.lr-g2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}
.lr-card{padding:26px 28px;border-radius:20px;background:#FFFFFF;border:1.5px solid #E6EAF3;box-sizing:border-box;display:flex;flex-direction:column}
.lr-ch{display:flex;align-items:center;justify-content:space-between;gap:12px}
.lr-ch h3{margin:0;display:flex;align-items:center;font-size:17px;font-weight:600}
.lr-card p{margin:8px 0 0;font-size:14.5px;line-height:1.55;color:#4A5578}
.lr-card > .ds-link{margin-top:auto;padding-top:18px;align-self:flex-start}
.lr-ico{width:44px;height:44px;border-radius:14px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.lr-cb{display:flex;align-items:flex-start;gap:16px;margin-top:18px}
.lr-cb h4{margin:0;font-size:15.5px;font-weight:600}
.lr-cb p{margin-top:4px}
.lr-seas{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-top:18px}
.lr-seas div{padding:12px 14px;border-radius:14px;background:#F7F9FD;border:1.5px dashed #D6DDEE}
.lr-seas b{display:block;font-size:13.5px;font-weight:600;color:#5B6582}
.lr-seas span{display:block;margin-top:2px;font-size:12px;color:#8A93AD}
.lr-bp{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-top:18px}
.lr-bp div{display:flex;align-items:center;gap:10px;padding:12px 14px;border-radius:14px;border:1.5px dashed #D6DDEE;font-size:13.5px;font-weight:500;color:#5B6582}
.lr-bp svg{color:#9DB8F7;flex-shrink:0}
.lr-posts{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}
.lr-post{display:flex;flex-direction:column;gap:10px;padding:20px 22px;border-radius:18px;background:#FFFFFF;border:1.5px solid #E6EAF3;text-decoration:none;color:#0B1433;transition:border-color .2s ease,transform .3s ease}
.lr-post:hover{border-color:#AFC1F5;transform:translateY(-2px)}
.lr-post b{font-size:15.5px;font-weight:600;line-height:1.35}
.lr-post small{display:flex;align-items:center;gap:8px;margin-top:auto;font-size:13px;color:#5B6582}
.lr-post .cs-cav{width:22px;height:22px;font-size:9px}
.lr-post .ds-tag{align-self:flex-start}
.lr-scrim,.lr-panel{font-family:'Google Sans','Google Sans Text','Helvetica Neue',system-ui,sans-serif;color:#0B1433}
.lr-scrim{position:fixed;inset:0;z-index:40;background:rgba(11,20,51,.28);animation:lrFade .25s ease both}
.lr-panel{position:fixed;right:0;top:0;bottom:0;z-index:41;width:420px;max-width:100vw;box-sizing:border-box;display:flex;flex-direction:column;background:#FFFFFF;box-shadow:-30px 0 80px -30px rgba(11,20,51,.35);animation:lrIn .4s cubic-bezier(.2,.8,.2,1) both}
.lr-ph{display:flex;align-items:center;gap:12px;padding:18px 18px 18px 22px;border-bottom:1.5px solid #EEF1F7}
.lr-ph b{display:block;font-size:16px;font-weight:600}
.lr-ph span{display:block;font-size:12.5px;color:#5B6582}
.lr-ph .ds-x{margin-left:auto}
.lr-pb{flex:1;overflow-y:auto;padding:22px;display:flex;flex-direction:column;gap:16px;background:linear-gradient(180deg,#F5F8FF,#FFFFFF 220px)}
.lr-msg{display:flex;align-items:flex-start;gap:10px;animation:lrUp .4s ease both}
.lr-msg .nv-av{width:30px;height:30px}
.lr-bub{padding:14px 16px;border-radius:4px 18px 18px 18px;background:#FFFFFF;border:1.5px solid #E6EAF3;font-size:15px;line-height:1.5;color:#0B1433;box-shadow:0 10px 24px -20px rgba(11,20,51,.4)}
.lr-me{align-self:flex-end;max-width:85%;padding:12px 16px;border-radius:18px 18px 4px 18px;background:#1652F0;color:#FFFFFF;font-size:15px;line-height:1.45}
.lr-name{display:flex;flex-direction:column;gap:12px;animation:lrUp .4s ease .1s both}
.lr-name label{font-size:13px;font-weight:500;color:#3A4566}
.lr-sugs{display:flex;gap:8px;flex-wrap:wrap}
.lr-sugs .ds-chip{padding-left:4px}
.lr-sugs .nv-av{width:24px;height:24px}
.lr-na{display:flex;align-items:center;gap:18px;margin-top:4px}
.lr-qs{display:flex;flex-direction:column;align-items:flex-start;gap:8px;margin-left:40px}
.lr-qs .ds-chip{height:auto;min-height:40px;padding:9px 14px;white-space:normal;text-align:left;line-height:1.35}
.lr-pf{padding:14px 16px 18px;border-top:1.5px solid #EEF1F7}
.lr-pf .ds-ask{box-shadow:none}
.ds-badge{margin-left:auto;min-width:22px;height:22px;padding:0 6px;box-sizing:border-box;border-radius:999px;background:#1652F0;color:#FFFFFF;font-size:12px;font-weight:600;display:flex;align-items:center;justify-content:center}
.lr-st b i{font-style:normal;font-weight:500;font-size:13px;color:#8A93AD}
.lr-st:hover small{color:#1652F0}
.lr-goal{display:grid;grid-template-columns:minmax(0,1fr) 400px;gap:40px;align-items:center}
.lr-fa{display:flex;align-items:center;gap:22px;margin-top:28px;flex-wrap:wrap}
.lr-gv{position:relative;width:400px;height:230px}
.lr-gv > svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.lr-gv-p{fill:none;stroke:#1652F0;stroke-width:3;stroke-linecap:round;stroke-dasharray:.5 10;animation:lrDash 1.4s linear infinite}
@keyframes lrDash{to{stroke-dashoffset:-10.5}}
.lr-gv-n{position:absolute;display:flex;flex-direction:column;align-items:center;gap:8px;font-size:13px;font-weight:600;white-space:nowrap}
.lr-gv-l{flex-direction:row-reverse;gap:12px;transform:translate(calc(-100% + 28px), -28px)}
.lr-gv-you{width:48px;height:48px;border-radius:999px;background:#DCE5FB;color:#1652F0;display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:600;box-shadow:0 0 0 5px #FFFFFF,0 14px 26px -12px rgba(11,20,51,.45)}
.lr-gv-flag{width:56px;height:56px;border-radius:999px;background:#0B1433;color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 6px rgba(255,255,255,.9),0 18px 32px -14px rgba(11,20,51,.6)}
.lr-gv-g{position:absolute;width:18px;height:18px;margin:-9px 0 0 -9px;border-radius:999px;background:#FFFFFF;border:2px dashed #7FA4FF;box-sizing:border-box}
.lr-gv-c{position:absolute;display:inline-flex;align-items:center;gap:8px;height:40px;padding:0 14px 0 4px;border-radius:999px;background:#FFFFFF;border:1.5px solid #DCE5FB;font-size:13px;font-weight:500;white-space:nowrap;box-shadow:0 16px 30px -18px rgba(22,82,240,.55)}
.lr-gv-c .nv-av{width:32px;height:32px}
.lr-nx{display:flex;align-items:center;gap:16px;min-width:0}
.lr-nx-i{width:52px;height:52px;border-radius:16px;background:#FFFFFF;border:1.5px solid #DCE5FB;color:#1652F0;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.lr-nx small{display:block;font-size:13px;color:#4A5578}
.lr-nx b{display:block;margin-top:2px;font-size:17px;font-weight:600;letter-spacing:-.2px}
.lr-nx-m{display:flex;align-items:center;gap:10px;margin-top:7px;font-size:13px;color:#4A5578}
.lr-bar{position:relative;display:block;flex-shrink:0;width:120px;height:6px;border-radius:9px;background:rgba(22,82,240,.14);overflow:hidden}
.lr-bar i{position:absolute;left:0;top:0;bottom:0;border-radius:9px;background:#1652F0}
.lr-bar.ok i{background:#0F6B45}
.lr-bar.lg{width:100%;height:8px;margin-top:14px}
.lr-week{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);padding:0}
.lr-week > div{padding:26px 28px;display:flex;flex-direction:column;min-width:0}
.lr-week > div + div{border-left:1px solid #EEF1F7}
.lr-wkd{font-size:13px;color:#5B6582}
.lr-days{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:4px;margin-top:16px}
.lr-day{display:flex;flex-direction:column;align-items:center;gap:4px;padding:8px 0;border-radius:12px;font-size:12px;color:#5B6582}
.lr-day b{font-size:15px;font-weight:600;color:#0B1433}
.lr-day i{width:5px;height:5px;border-radius:9px}
.lr-day.ev i{background:#1652F0}
.lr-day.today{background:#1652F0;color:#DCE5FB}
.lr-day.today b{color:#FFFFFF}
.lr-day.today i{background:#FFFFFF}
.lr-evs{margin-top:6px}
.lr-evd{display:block;margin-top:14px;font-size:12px;font-weight:600;color:#8A93AD}
.lr-ev{display:grid;grid-template-columns:72px minmax(0,1fr) auto;align-items:center;gap:12px;padding:9px 0;border-bottom:1px solid #EEF1F7}
.lr-ev time{font-size:13px;color:#5B6582}
.lr-ev b{min-width:0;font-size:14.5px;font-weight:500;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.lr-week .ds-link.lr-end{margin-top:auto;padding-top:16px;align-self:flex-start}
.lr-rows{display:flex;flex-direction:column;margin-top:10px}
.lr-row{display:flex;align-items:center;gap:14px;padding:14px 0;border-bottom:1px solid #EEF1F7}
.lr-row-i{width:40px;height:40px;border-radius:12px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.lr-row-b{flex:1;min-width:0}
.lr-row-b b{display:block;font-size:15px;font-weight:600}
.lr-row-b small{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-top:4px;font-size:13px;color:#5B6582}
.lr-goalw{margin-top:auto;padding:16px 18px;border-radius:16px;background:#F5F8FF}
.lr-goalw div{display:flex;align-items:baseline;justify-content:space-between;gap:12px;font-size:14px;color:#4A5578}
.lr-goalw b{font-size:15px;font-weight:600;color:#0B1433}
.lr-goalw .lr-bar{margin-top:10px}
.lr-goalw p{margin:10px 0 0;font-size:13px;color:#4A5578}
.lr-week .lr-rows + .lr-goalw{margin-top:18px}
.lr-tabs{display:flex;gap:8px;flex-wrap:wrap}
.lr-mlc{padding:20px 24px 8px}
.lr-mls{margin-top:8px}
.lr-mr{display:grid;grid-template-columns:40px minmax(0,1fr) 130px 180px 90px;align-items:center;gap:18px;padding:16px 0;border-top:1px solid #EEF1F7;text-decoration:none;color:#0B1433}
.lr-mr:first-child{border-top:0}
.lr-mr:hover .lr-mr-b b{color:#1652F0}
.lr-mr-b b{display:block;font-size:15.5px;font-weight:600;transition:color .2s ease}
.lr-mr-b small{display:block;margin-top:3px;font-size:13px;color:#5B6582}
.lr-mr .ds-tag{justify-self:start}
.lr-mr-p{display:flex;align-items:center;gap:10px;font-size:13px;font-weight:600}
.lr-mr .ds-link{justify-self:end}
.lr-mle{margin:0;padding:18px 0;font-size:14.5px;color:#5B6582}
.lr-g3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}
.lr-big{display:flex;align-items:baseline;gap:8px;margin-top:14px;font-size:36px;line-height:1;font-weight:600;letter-spacing:-1px}
.lr-big small{font-size:14px;font-weight:500;color:#5B6582;letter-spacing:0}
.lr-split{display:flex;gap:3px;height:8px;margin-top:16px}
.lr-split i{border-radius:9px;background:#1652F0}
.lr-split i + i{background:#9DB8F7}
.lr-leg{display:flex;gap:16px;flex-wrap:wrap;margin-top:10px;font-size:13px;color:#4A5578}
.lr-leg span{display:flex;align-items:center;gap:6px}
.lr-leg i{width:8px;height:8px;border-radius:9px;background:#1652F0}
.lr-leg span + span i{background:#9DB8F7}
.lr-rw{display:flex;flex-direction:column;margin-top:8px}
.lr-rw div{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:10px 0;border-bottom:1px solid #EEF1F7;font-size:14px}
.lr-bpf{padding:26px 28px}
.lr-bpb{display:flex;align-items:center;justify-content:space-between;gap:28px;margin-top:6px}
.lr-bpn{display:flex;align-items:center;gap:32px}
.lr-bps{display:flex}
.lr-bps span{display:flex;flex-direction:column;gap:2px;padding:0 20px;font-size:13px;color:#5B6582}
.lr-bps span + span{border-left:1px solid #EEF1F7}
.lr-bps b{font-size:18px;font-weight:600;color:#0B1433}
.lr-cred{display:flex;align-items:center;gap:14px;padding:14px 18px;border-radius:16px;background:#F7F9FD;border:1.5px solid #E6EAF3;min-width:0}
.lr-cred-i{width:44px;height:44px;border-radius:14px;background:#E7F5EE;color:#0F6B45;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.lr-cred b{display:block;font-size:15px;font-weight:600}
.lr-cred small{display:block;margin-top:2px;font-size:13px;color:#5B6582}
.lr-tut{display:flex;align-items:center;gap:12px;padding-left:22px;border-left:1.5px solid rgba(22,82,240,.16)}
.lr-tut .cs-cav{width:40px;height:40px;font-size:13px;background:#FFFFFF;box-shadow:inset 0 0 0 1.5px #DCE5FB}
.lr-tut small{display:block;font-size:12.5px;color:#4A5578}
.lr-tut .ds-link{font-size:14px}
@keyframes lrIn{from{transform:translateX(40px);opacity:0}to{transform:none;opacity:1}}
@keyframes lrFade{from{opacity:0}to{opacity:1}}
@keyframes lrUp{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion: reduce){.lr-panel,.lr-scrim,.lr-msg,.lr-name,.lr-gv-p{animation:none}}
@media (max-width: 1280px){
.lr-head{flex-direction:column;align-items:flex-start;gap:16px}
.lr-g4{grid-template-columns:repeat(3,minmax(0,1fr))}
.lr-g4 > :nth-child(4){display:none}
}
@media (max-width: 1180px){.ds-root{grid-template-columns:232px minmax(0,1fr)}.lr-disc{grid-template-columns:minmax(0,1fr) 300px;gap:28px}.lr-goal{grid-template-columns:minmax(0,1fr)}.lr-gv{display:none}.lr-mr{grid-template-columns:40px minmax(0,1fr) 160px 80px}.lr-mr .ds-tag{display:none}.lr-bpb{flex-direction:column;align-items:stretch}.lr-nova{flex-wrap:wrap}.lr-tut{padding-left:0;border-left:0;width:100%}}
@media (max-width: 960px){
.ds-root{grid-template-columns:minmax(0,1fr);overflow-x:hidden}
.ds-side{position:fixed;left:0;top:0;width:288px;max-width:86vw;transform:translateX(-102%);transition:transform .3s cubic-bezier(.2,.8,.2,1);box-shadow:0 24px 64px rgba(11,20,51,.18)}
.ds-side.ds-open{transform:none}
.ds-scrim.ds-open{display:block;position:fixed;inset:0;background:rgba(11,20,51,.32);z-index:15}
.ds-menu,.ds-mlogo{display:flex}
.ds-close{display:flex;position:absolute;right:12px;top:16px}
.ds-top{height:64px;padding:0 16px;gap:8px}
.ds-search,.ds-hide-sm{display:none !important}
.ds-icon-btn,.lr-av{width:40px;height:40px}
.lr-pill{height:40px;padding:0 12px 0 8px}
.lr-coach{height:40px;padding:0 5px}
.lr-coach span:last-child{display:none}
.lr-mlogo{flex-grow:1;display:flex;align-items:center;text-decoration:none}
.lr-mlogo .lr-word{height:20px}
.lr-av{display:none}
.lr-acct{display:flex}
.ds-main{padding:8px 16px 32px}
.lr-disc{grid-template-columns:minmax(0,1fr)}
.lr-g2,.lr-posts,.lr-g3{grid-template-columns:minmax(0,1fr)}
.lr-week{grid-template-columns:minmax(0,1fr)}
.lr-week > div + div{border-left:0;border-top:1px solid #EEF1F7}
}
@media (max-width: 760px){
.lr-head{margin:4px 0 18px;gap:14px}
.lr-h1{font-size:24px;line-height:1.2}
.lr-strip,.lr-gs{align-self:stretch}
.lr-gs{justify-content:space-between;gap:12px;padding:10px 10px 10px 14px}
.lr-gs li:has(.done){display:none}
.lr-st{flex:1;padding:10px 12px}
.lr-focus{margin:0 -16px;border-radius:0;border-left:0;border-right:0;padding:26px 16px 24px}
.lr-ft{font-size:28px;letter-spacing:-.025em}
.lr-fs{font-size:15px}
.lr-ask{margin-top:20px}
.lr-chips{flex-wrap:nowrap;overflow-x:auto;margin:14px -16px 0;padding:0 16px;scrollbar-width:none}
.lr-chips::-webkit-scrollbar{display:none}
.lr-chips small{display:none}
.lr-nv{padding:18px}
.lr-nv p{margin:12px 0 14px;font-size:14.5px}
.lr-jy .jy-jh{flex-direction:column;align-items:flex-start;gap:14px}
.lr-jy .jy-jt{font-size:26px;letter-spacing:-.5px}
.lr-jy .jy-jr{grid-template-columns:minmax(0,1fr);margin-top:22px}
.lr-jy .jy-jr::before{display:none}
.lr-jy .jy-js{display:grid;grid-template-columns:32px minmax(0,1fr) auto;align-items:center;column-gap:12px;text-align:left;padding-bottom:16px}
.lr-jy .jy-js:not(:last-child)::after{content:"";position:absolute;left:15px;top:32px;bottom:0;width:2px;background:rgba(22,82,240,.28)}
.lr-jy .jy-js:last-child{padding-bottom:0}
.lr-jy .jy-jn{width:32px;height:32px;margin:0;font-size:12px}
.lr-jy .jy-jl{font-size:14px}
.lr-jy .jy-jd{grid-column:3;font-size:12px}
.lr-jy .jy-here{grid-column:2;justify-self:start;margin-top:6px}
.lr-jf{flex-direction:column;align-items:stretch;gap:16px;margin-top:22px;padding-top:18px}
.lr-jf .ds-acts{position:static;margin:0;padding:0;border:0;background:none}
.lr-sec{margin-top:30px}
.lr-sh h2{font-size:19px}
.lr-sh p{display:none}
.lr-g4{display:flex;overflow-x:auto;gap:12px;margin:0 -16px;padding:2px 16px 6px;scroll-snap-type:x mandatory;scrollbar-width:none}
.lr-g4::-webkit-scrollbar{display:none}
.lr-g4 > *{flex:0 0 76%;scroll-snap-align:start}
.lr-g4 > :nth-child(4){display:flex}
.cs-th{height:96px}
.cs-ico{width:96px;height:96px}
.cs-ct{font-size:15px;min-height:0}
.lr-nova{flex-wrap:wrap;gap:14px;padding:20px 18px}
.lr-nova .nv-av{width:48px;height:48px}
.lr-nova-b{flex:1 1 calc(100% - 64px)}
.lr-nova-b p{font-size:15px}
.lr-nova-a{width:100%;justify-content:space-between}
.lr-card{padding:20px 18px}
.lr-seas,.lr-bp{display:none}
.lr-posts{display:flex;overflow-x:auto;gap:12px;margin:0 -16px;padding:0 16px;scrollbar-width:none}
.lr-posts::-webkit-scrollbar{display:none}
.lr-post{flex:0 0 78%;padding:16px 18px}
.lr-strip{display:grid;grid-template-columns:repeat(2,minmax(0,1fr))}
.lr-st + .lr-st{border-left:0}
.lr-st:nth-child(even){border-left:1px solid #EEF1F7}
.lr-st:nth-child(n+3){border-top:1px solid #EEF1F7}
.lr-fa{flex-direction:column;align-items:stretch;gap:10px;margin-top:22px}
.lr-fa .ds-btn{justify-content:space-between}
.lr-fa .ds-link{justify-content:center;min-height:40px}
.lr-nx b{font-size:15.5px}
.lr-nx-i{width:44px;height:44px;border-radius:14px}
.lr-bar{width:90px}
.lr-week > div{padding:20px 18px}
.lr-ev{grid-template-columns:62px minmax(0,1fr)}
.lr-ev .ds-tag{display:none}
.lr-mlc{padding:16px 16px 4px}
.lr-tabs{flex-wrap:nowrap;overflow-x:auto;margin:0 -16px;padding:0 16px;scrollbar-width:none}
.lr-tabs::-webkit-scrollbar{display:none}
.lr-mr{grid-template-columns:40px minmax(0,1fr) auto;gap:12px}
.lr-mr-p{grid-column:2;grid-row:2;margin-top:-6px}
.lr-mr .ds-link{grid-column:3;grid-row:1}
.lr-big{font-size:30px}
.lr-g3{display:flex;overflow-x:auto;gap:12px;margin:0 -16px;padding:0 16px 4px;scroll-snap-type:x mandatory;scrollbar-width:none}
.lr-g3::-webkit-scrollbar{display:none}
.lr-g3 > *{flex:0 0 80%;scroll-snap-align:start}
.lr-bpf{padding:20px 18px}
.lr-bpn{flex-direction:column;align-items:flex-start;gap:14px}
.lr-bps span{padding:0 12px}
.lr-bps span:first-child{padding-left:0}
.lr-cred{padding:12px 14px}
.lr-sh .ds-tag.lg{height:28px;font-size:12px}
.lr-panel{width:100vw}
.lr-pb{padding:18px 16px}
}
'''.replace('NOVABG', '/_blob/0b29db2e4cd6f4a89dc7ba8f12e59c8d')

CARD = '''<a class="cs-card" href="{{c.href}}" aria-label="{{c.t}}">
<div class="cs-th" style="background: {{c.bg}}">
<svg class="cs-ico" viewBox="0 0 24 24" fill="none" stroke="{{c.icoC}}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20V10M10 20V4M16 20v-7M2 20h20" style="display: {{c.i0}}"></path><path d="M12 20h9M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z" style="display: {{c.i1}}"></path><path d="M8 6l-6 6 6 6M16 6l6 6-6 6" style="display: {{c.i2}}"></path><path d="M3 7h18v13H3zM8 7V4h8v3" style="display: {{c.i4}}"></path></svg>
</div>
<div class="cs-cb">
<span class="cs-ct">{{c.t}}</span>
<span class="cs-by"><span class="cs-cav">{{c.ini}}</span>{{c.by}}</span>
<span class="cs-meta"><span class="cs-star" aria-hidden="true">★</span><b>{{c.rating}}</b><span>({{c.reviews}})</span><span class="cs-dot"></span><span>{{c.lvl}}</span><span class="cs-dot"></span><span>{{c.hrs}}</span></span>
<span class="cs-tags"><span class="ds-tag blue"><span class="cs-tdot" style="background: {{c.tierDot}}"></span>{{c.tierLabel}}</span></span>
<div class="cs-acc">
<span class="cs-ar"><b>''' + coin() + '''{{c.dlp}} DLP</b></span>
<span class="lr-why"><span class="nv-av" aria-hidden="true"><img src="{{coachSrc}}" alt="" style="left: {{coachL}}; top: {{coachT}}; width: {{coachW}}"></span><span>{{c.why}}</span></span>
</div>
</div>
</a>'''

def av(cls=''):
    return '<span class="nv-av%s" aria-hidden="true"><img src="{{coachSrc}}" alt="" style="left: {{coachL}}; top: {{coachT}}; width: {{coachW}}"></span>' % ((' ' + cls) if cls else '')

STEP = ('<li><sc-if value="{{g.isBtn}}" hint-placeholder-val="{{ false }}"><button type="button" class="lr-gs-s {{g.cls}}" onClick="{{g.go}}"><i>' + ck(12, 3.4) + '</i>{{g.t}}</button></sc-if>'
        '<sc-if value="{{g.isLink}}" hint-placeholder-val="{{ false }}"><a class="lr-gs-s {{g.cls}}" href="{{g.href}}"><i>' + ck(12, 3.4) + '</i>{{g.t}}</a></sc-if>'
        '<sc-if value="{{g.isDone}}" hint-placeholder-val="{{ true }}"><span class="lr-gs-s done"><i>' + ck(12, 3.4) + '</i>{{g.t}}</span></sc-if></li>')

MARKUP = '''<div class="ds-root">
<div class="ds-scrim {{navCls}}" onClick="{{toggleNav}}"></div>
<nav class="ds-side {{navCls}}" aria-label="Main">
<a class="lr-logo" href="Dashboard.dc.html" aria-label="Credalio home"><span class="lr-word"></span></a>
<button type="button" class="ds-icon-btn ds-close" onClick="{{toggleNav}}" aria-label="Close menu">''' + ic('<path d="M6 6l12 12M18 6 6 18"></path>', 18, 2) + '''</button>
''' + sidebar() + '''
<div class="lr-sfoot">
<div class="lr-plan"><div><b>{{planName}}</b><span>{{planSub}}</span></div><a class="ds-link" href="#">{{planCta}}</a></div>
<button type="button" class="ds-item" onClick="{{openPanel}}">''' + av('sm') + '''<span>{{coachNav}}</span></button>
<a href="#" class="ds-item">''' + ic(I['help'], 19) + '''<span>Help &amp; support</span></a>
<a href="#" class="ds-item">''' + ic(I['settings'], 19) + '''<span>Settings</span></a>
<a href="#" class="ds-item lr-acct"><span class="cs-cav">AO</span><span>Ada Ononuju</span></a>
</div>
</nav>
<div style="min-width: 0; display: flex; flex-direction: column">
<header class="ds-top">
<button type="button" class="ds-icon-btn ds-menu" onClick="{{toggleNav}}" aria-label="Open menu">''' + ic(I['menu'], 20) + '''</button>
<a class="ds-mlogo lr-mlogo" href="Dashboard.dc.html" aria-label="Credalio home"><span class="lr-word"></span></a>
<label class="ds-search">''' + ic(I['search'], 18) + '''<span class="sr-only">Search</span><input placeholder="Search courses, career paths, certifications…"></label>
<span class="ds-hide-sm" style="flex-grow: 1"></span>
<a href="#" class="lr-pill" aria-label="{{dlp}} DLP available">''' + coin() + '''<span>{{dlp}}</span><i class="ds-hide-sm">DLP</i></a>
<button type="button" class="lr-coach" onClick="{{openPanel}}" aria-label="{{coachBtn}}">''' + av() + '''<span>{{coachBtn}}</span></button>
<a href="#" class="ds-icon-btn" aria-label="Notifications, 1 new">''' + ic(I['bell'], 19) + '''<span class="lr-dot"></span></a>
<a href="#" class="lr-av" aria-label="Your account">AO</a>
</header>
<main class="ds-main">

<div class="lr-head">
<div><span class="lr-date">{{date}}</span><h1 class="lr-h1">{{greeting}}, Ada.</h1></div>
<sc-if value="{{isNew}}" hint-placeholder-val="{{ true }}">
<div class="lr-gs"><span class="lr-gs-t">Getting started<b>{{gsDone}} of 3 done</b></span><ol>
<sc-for list="{{gs}}" as="g" hint-placeholder-count="3">''' + STEP + '''</sc-for>
</ol></div>
</sc-if>
<sc-if value="{{isActive}}" hint-placeholder-val="{{ false }}">
<div class="lr-strip"><sc-for list="{{stats}}" as="s" hint-placeholder-count="4"><a class="lr-st" href="{{s.href}}"><small>{{s.k}}</small><b><sc-if value="{{s.coin}}" hint-placeholder-val="{{ false }}">''' + coin() + '''</sc-if>{{s.v}}<i>{{s.of}}</i></b></a></sc-for></div>
</sc-if>
</div>

<sc-if value="{{fDisc}}" hint-placeholder-val="{{ true }}">
<section class="lr-focus lr-disc aur aur-lt" aria-labelledby="lr-ft">
<div>
<span class="lr-k">{{dKicker}}</span>
<h2 id="lr-ft" class="lr-ft">What would you like to learn?</h2>
<p class="lr-fs">{{dSub}}</p>
<form class="ds-ask lr-ask" action="Explore.dc.html" role="search"><label class="sr-only" for="lr-q">Search learning</label><input id="lr-q" name="q" placeholder="Try ‘SQL’, ‘UX design’ or ‘leadership’" value="{{q}}" onInput="{{onQ}}">''' + btn('Explore', 'Explore.dc.html', 'sm') + '''</form>
<div class="lr-chips"><small>Or browse</small><sc-for list="{{disc}}" as="c" hint-placeholder-count="4"><a class="ds-chip" href="{{c.h}}">{{c.t}}</a></sc-for></div>
</div>
<aside class="lr-nv" aria-label="Your AI Coach">
<div class="lr-nvh">''' + av('lg') + '''<div><b>{{coachTitle}}</b><span>Your AI Coach</span></div></div>
<p>{{dNova}}</p>
<a class="ds-link" href="Journey.dc.html">{{dNovaCta}}''' + ARR_S + '''</a>
</aside>
</section>
</sc-if>

<sc-if value="{{fReady}}" hint-placeholder-val="{{ false }}">
<section class="lr-focus lr-jy aur aur-lt" aria-labelledby="lr-jt">
<div class="jy-jh"><div><span class="jy-jk"><span class="ds-tag green">Journey ready</span>Your journey to becoming</span><h2 id="lr-jt" class="jy-jt" style="margin: 6px 0 0">Data Analyst</h2></div>
<div class="jy-jm"><span class="ds-tag line lg">5 stages</span><span class="ds-tag line lg">3–4 months</span><span class="ds-tag line lg">''' + coin() + '''~3,800 DLP''' + tip('An estimate of the learning allowance the whole journey uses. You only spend DLP as you learn, stage by stage.', 'r') + '''</span></div></div>
<ol class="jy-jr" aria-label="Your five stages">
<sc-for list="{{route}}" as="r" hint-placeholder-count="5"><li class="jy-js {{r.cls}}"><span class="jy-jn">{{r.mark}}</span><span class="jy-jl">{{r.label}}</span><span class="jy-jd">{{r.note}}</span><sc-if value="{{r.here}}" hint-placeholder-val="{{ false }}"><span class="ds-tag blue jy-here">{{r.hereT}}</span></sc-if></li></sc-for>
</ol>
<div class="lr-jf">
<span class="lr-ok"><i>''' + ck(13, 3.2) + '''</i><span><b>You can start today.</b> Stage 1 uses 200 DLP, and that’s your balance.</span></span>
<div class="ds-acts"><a class="ds-link" href="JourneyPlan-Saved.dc.html">Review journey</a>''' + btn('Start Stage 1', 'CourseDetail-Learner.dc.html') + '''</div>
</div>
</section>
</sc-if>

<sc-if value="{{fGoal}}" hint-placeholder-val="{{ false }}">
<section class="lr-focus lr-goal aur aur-lt" aria-labelledby="lr-gt">
<div>
<span class="lr-k">Your goal</span>
<h2 id="lr-gt" class="lr-ft">Become a stronger leader</h2>
<p class="lr-fs">You haven’t chosen a path yet. Pick something below, or let {{coachTitle}} shape a journey around this goal.</p>
<div class="lr-fa">''' + btn('Continue with {{coachTitle}}', 'Journey.dc.html') + '''<a class="ds-link" href="Explore.dc.html">Explore leadership learning</a></div>
</div>
<div class="lr-gv" aria-hidden="true">
<svg viewBox="0 0 400 230"><path class="lr-gv-p" d="M40 190 Q85 185 130 160 T215 110 T290 75 T360 40"></path></svg>
<span class="lr-gv-g" style="left: 130px; top: 160px"></span><span class="lr-gv-g" style="left: 215px; top: 110px"></span><span class="lr-gv-g" style="left: 290px; top: 75px"></span>
<span class="lr-gv-n" style="left: 40px; top: 190px; transform: translate(-50%, -24px)"><span class="lr-gv-you">AO</span>You, today</span>
<span class="lr-gv-n lr-gv-l" style="left: 360px; top: 40px"><span class="lr-gv-flag">''' + ic('<path d="M7 21V4"></path><path d="M7 4h11l-2.6 4.5L18 13H7z" fill="currentColor"></path>', 24, 2) + '''</span>Stronger leader</span>
<span class="lr-gv-c" style="left: 186px; top: 156px">''' + av() + '''<span>{{coachTitle}} can map the steps</span></span>
</div>
</section>
</sc-if>

<sc-if value="{{fJourney}}" hint-placeholder-val="{{ false }}">
<section class="lr-focus lr-jy aur aur-lt" aria-labelledby="lr-jn">
<div class="jy-jh"><div><span class="jy-jk">{{jKicker}}</span><h2 id="lr-jn" class="jy-jt" style="margin: 6px 0 0">{{jTitle}}</h2></div>
<div class="jy-jm"><span class="ds-tag line lg">{{jPct}} complete</span><span class="ds-tag line lg">{{jStage}}</span></div></div>
<ol class="jy-jr" aria-label="Your five stages">
<sc-for list="{{route}}" as="r" hint-placeholder-count="5"><li class="jy-js {{r.cls}}"><span class="jy-jn">{{r.mark}}</span><span class="jy-jl">{{r.label}}</span><span class="jy-jd">{{r.note}}</span><sc-if value="{{r.here}}" hint-placeholder-val="{{ false }}"><span class="ds-tag blue jy-here">{{r.hereT}}</span></sc-if></li></sc-for>
</ol>
<div class="lr-jf">
<div class="lr-nx"><span class="lr-nx-i">''' + ic(I['learn'], 24) + '''</span><div><small>Next up · {{nxCtx}}</small><b>{{nxTitle}}</b><span class="lr-nx-m"><span class="lr-bar"><i style="width: {{nxPct}}"></i></span>{{nxMeta}}</span></div></div>
<div class="ds-acts"><a class="ds-link" href="{{jViewHref}}">View journey</a>''' + btn('{{jCta}}', '{{jCtaHref}}') + '''</div>
</div>
</section>
</sc-if>

<sc-if value="{{isActive}}" hint-placeholder-val="{{ false }}">
<section class="lr-sec lr-card lr-week" aria-label="This week">
<div>
<div class="lr-ch"><h3>This week</h3><span class="lr-wkd">{{wkRange}}</span></div>
<div class="lr-days"><sc-for list="{{days}}" as="d" hint-placeholder-count="7"><span class="lr-day {{d.cls}}"><span>{{d.w}}</span><b>{{d.n}}</b><i></i></span></sc-for></div>
<div class="lr-evs"><sc-for list="{{sched}}" as="e" hint-placeholder-count="5"><sc-if value="{{e.head}}" hint-placeholder-val="{{ false }}"><span class="lr-evd">{{e.day}}</span></sc-if><div class="lr-ev"><time>{{e.time}}</time><b>{{e.t}}</b><span class="ds-tag {{e.tc}}">{{e.type}}</span></div></sc-for></div>
<a class="ds-link lr-end" href="#">Open schedule''' + ARR_S + '''</a>
</div>
<div>
<div class="lr-ch"><h3>Due soon</h3><a class="ds-link" href="#">All assignments</a></div>
<div class="lr-rows"><sc-for list="{{assigns}}" as="a" hint-placeholder-count="2"><div class="lr-row"><span class="lr-row-i">''' + ic(I['assign'], 20) + '''</span><div class="lr-row-b"><b>{{a.t}}</b><small>{{a.ctx}}</small><small><span class="ds-tag {{a.dueCls}}">{{a.due}}</span>{{a.est}}</small></div><a class="ds-link" href="{{a.href}}">{{a.cta}}</a></div></sc-for></div>
<div class="lr-goalw"><div><span>Weekly goal</span><b>{{wgDone}} of {{wgAll}} hours</b></div><span class="lr-bar lg"><i style="width: {{wgPct}}"></i></span><p>{{wgNote}}</p></div>
</div>
</section>

<section class="lr-sec" aria-labelledby="lr-ml">
<div class="lr-sh"><div><h2 id="lr-ml">My learning</h2><p>Everything you’ve started, in one place.</p></div><a class="ds-link" href="#">View all</a></div>
<div class="lr-card lr-mlc">
<div class="lr-tabs" role="tablist" aria-label="Filter my learning"><sc-for list="{{mlTabs}}" as="t" hint-placeholder-count="5"><button type="button" role="tab" class="ds-chip sm {{t.cls}}" aria-selected="{{t.sel}}" onClick="{{t.pick}}">{{t.label}}<i>{{t.n}}</i></button></sc-for></div>
<div class="lr-mls">
<sc-for list="{{mlItems}}" as="m" hint-placeholder-count="4"><a class="lr-mr" href="{{m.href}}"><span class="lr-row-i"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><g style="display: {{m.i0}}">''' + I['path'] + '''</g><g style="display: {{m.i1}}">''' + I['learn'] + '''</g><g style="display: {{m.i2}}">''' + I['cert'] + '''</g><g style="display: {{m.i3}}">''' + I['prog'] + '''</g></svg></span><span class="lr-mr-b"><b>{{m.t}}</b><small>{{m.sub}}</small></span><span class="ds-tag line">{{m.type}}</span><span class="lr-mr-p"><span class="lr-bar {{m.barCls}}"><i style="width: {{m.pct}}"></i></span>{{m.pctLabel}}</span><span class="ds-link">{{m.cta}}</span></a></sc-for>
<sc-if value="{{mlEmpty}}" hint-placeholder-val="{{ false }}"><p class="lr-mle">Nothing in this group yet.</p></sc-if>
</div>
</div>
</section>
</sc-if>

<section class="lr-sec" aria-labelledby="lr-rec">
<div class="lr-sh"><div><h2 id="lr-rec">{{recTitle}}</h2><p>{{recSub}}</p></div><a class="ds-link" href="Explore.dc.html">Explore learning</a></div>
<div class="lr-g4"><sc-for list="{{recs}}" as="c" hint-placeholder-count="4">''' + CARD + '''</sc-for></div>
</section>

<sc-if value="{{showBand}}" hint-placeholder-val="{{ true }}">
<section class="lr-sec lr-nova nova-card" aria-label="Your AI Coach">
''' + av() + '''
<div class="lr-nova-b"><span class="lr-nova-k">{{novaKicker}}</span><p>{{novaMsg}}</p></div>
<div class="lr-nova-a"><sc-if value="{{novaIsLink}}" hint-placeholder-val="{{ false }}"><button type="button" class="ds-link" onClick="{{openPanel}}">{{novaLink}}</button></sc-if><sc-if value="{{novaIsBtn}}" hint-placeholder-val="{{ true }}"><button type="button" class="ds-ghost sm" onClick="{{openPanel}}">{{novaCta}}</button></sc-if><sc-if value="{{novaIsLink}}" hint-placeholder-val="{{ false }}"><a class="ds-ghost sm" href="{{novaHref}}">{{novaCta}}</a></sc-if></div>
<sc-if value="{{showTutor}}" hint-placeholder-val="{{ false }}"><div class="lr-tut"><span class="cs-cav">HC</span><div><small>Prefer a person?</small><a class="ds-link" href="#">Message Hannah, your tutor</a></div></div></sc-if>
</section>
</sc-if>

<sc-if value="{{seasonOn}}" hint-placeholder-val="{{ false }}">
<section class="lr-sec" aria-labelledby="lr-sn">
<div class="lr-sh"><div><h2 id="lr-sn">Your Learning Season</h2><p>Learning comes first. Rewards follow when the season closes.</p></div><span class="ds-tag blue lg">September · 3 days left</span></div>
<div class="lr-g3">
<section class="lr-card" aria-labelledby="lr-las"><div class="lr-ch"><h3 id="lr-las">Season LAS''' + tip('Your verified learning activity this season. It’s a score, not money, and has no fixed cash value.') + '''</h3></div>
<span class="lr-big">1,240<small>LAS</small></span>
<span class="lr-split" aria-hidden="true"><i style="width: 85%"></i><i style="width: 15%"></i></span>
<span class="lr-leg"><span><i></i>Learning 1,050</span><span><i></i>Community 190</span></span>
<a class="ds-link" href="#">View breakdown''' + ARR_S + '''</a></section>
<section class="lr-card" aria-labelledby="lr-stk"><div class="lr-ch"><h3 id="lr-stk">Learning streak</h3></div>
<span class="lr-big">18<small>days in a row</small></span>
<span class="lr-bar lg" aria-hidden="true"><i style="width: 60%"></i></span>
<p>12 more days to your 30-day milestone.</p>
<a class="ds-link" href="#">View activity''' + ARR_S + '''</a></section>
<section class="lr-card" aria-labelledby="lr-sr"><div class="lr-ch"><h3 id="lr-sr">Season rewards''' + tip('Rewards are worked out when the season closes. Credits reach your Wallets only after that.', 'r') + '''</h3><span class="ds-tag blue">Accumulating</span></div>
<div class="lr-rw"><div><span>Marketplace Credits</span><span class="ds-tag">Pending</span></div><div><span>Scholarship</span><span class="ds-tag">Pending</span></div><div><span>MFORGE</span><span class="ds-tag green">Eligible</span></div></div>
<a class="ds-link" href="#">View rewards''' + ARR_S + '''</a></section>
</div>
</section>
</sc-if>

<sc-if value="{{isNew}}" hint-placeholder-val="{{ true }}">
<div class="lr-sec lr-g2">
<section class="lr-card" aria-labelledby="lr-rw">
<div class="lr-ch"><h3 id="lr-rw">Learning rewards''' + tip('Each Learning Season, verified learning activity on a paid plan earns rewards such as Marketplace Credits. Learning always comes first.') + '''</h3><span class="ds-tag">Paid plans</span></div>
<div class="lr-cb"><span class="lr-ico">''' + ic(I['reward'], 22) + '''</span><div><h4>Learning Seasons come with paid plans.</h4><p>Your learning still builds your streak and your Digital Backpack, on any plan.</p></div></div>
<div class="lr-seas" aria-hidden="true"><div><b>Season LAS</b><span>Your activity score</span></div><div><b>Streak</b><span>Days in a row</span></div><div><b>Rewards</b><span>At season close</span></div></div>
<a class="ds-link" href="#">Compare plans''' + ARR_S + '''</a>
</section>
<section class="lr-card" aria-labelledby="lr-bp">
<div class="lr-ch"><h3 id="lr-bp">Digital Backpack''' + tip('Your verified proof: credentials, projects and skills you earn on Credalio, ready to share.') + '''</h3></div>
<div class="lr-cb"><span class="lr-ico">''' + ic(I['pack'], 22) + '''</span><div><h4>Your proof starts here.</h4><p>Everything you earn on Credalio lands here, verified and ready to share.</p></div></div>
<div class="lr-bp" aria-hidden="true"><div>''' + ic(I['cred'], 18) + '''Credentials</div><div>''' + ic(I['proj'], 18) + '''Projects</div><div>''' + ic(I['skill'], 18) + '''Skills</div></div>
<a class="ds-link" href="#">Open Backpack''' + ARR_S + '''</a>
</section>
</div>
</sc-if>

<sc-if value="{{isActive}}" hint-placeholder-val="{{ false }}">
<section class="lr-sec lr-card lr-bpf" aria-labelledby="lr-bpf">
<div class="lr-ch"><h3 id="lr-bpf">Digital Backpack''' + tip('Your verified proof: credentials, projects and skills you earn on Credalio, ready to share.') + '''</h3><a class="ds-link" href="#">Open Backpack</a></div>
<div class="lr-bpb">
<div class="lr-bpn"><span class="lr-big">12<small>verified achievements</small></span><div class="lr-bps"><span><b>4</b>Credentials</span><span><b>3</b>Projects</span><span><b>8</b>Skills</span><span><b>1</b>Career</span></div></div>
<div class="lr-cred"><span class="lr-cred-i">''' + ic(I['cred'], 22) + '''</span><div><b>Data Foundations</b><small>Course credential · issued 24 September</small></div><span class="ds-tag green">Verified</span></div>
</div>
</section>
</sc-if>

<section class="lr-sec" aria-labelledby="lr-cm">
<div class="lr-sh"><div><h2 id="lr-cm">From your learning community</h2><p>{{commSub}}</p></div><a class="ds-link" href="#">Open community</a></div>
<div class="lr-posts"><sc-for list="{{posts}}" as="p" hint-placeholder-count="3"><a class="lr-post" href="#"><span class="ds-tag line">{{p.tag}}</span><b>{{p.t}}</b><small><span class="cs-cav">{{p.ini}}</span>{{p.by}} · {{p.n}} replies</small></a></sc-for></div>
</section>

</main>
</div>
</div>

<sc-if value="{{panelOpen}}" hint-placeholder-val="{{ false }}">
<div class="lr-scrim" onClick="{{closePanel}}"></div>
<aside class="lr-panel" role="dialog" aria-modal="true" aria-label="{{coachTitle}}, your AI Coach">
<div class="lr-ph">''' + av() + '''<div><b>{{coachTitle}}</b><span>Your AI Coach</span></div><button type="button" class="ds-x" onClick="{{closePanel}}" aria-label="Close">''' + CLOSE + '''</button></div>
<div class="lr-pb">
<sc-if value="{{thinking}}" hint-placeholder-val="{{ false }}"><div class="lr-msg">''' + av() + think('{{thinkText}}') + '''</div></sc-if>
<sc-if value="{{showUnnamed}}" hint-placeholder-val="{{ true }}">
<div class="lr-msg">''' + av() + '''<div class="lr-bub">Hi Ada. I’m your AI Coach. I’ll help you choose what to learn and keep you moving. Want to give me a name?</div></div>
<div class="lr-name">
<label for="lr-nm">Name your coach</label>
<input id="lr-nm" class="ds-in" placeholder="Type a name" value="{{draft}}" onInput="{{onDraft}}">
<div class="lr-sugs"><sc-for list="{{nameSug}}" as="n" hint-placeholder-count="4"><button type="button" class="ds-chip sm {{n.cls}}" aria-pressed="{{n.on}}" onClick="{{n.pick}}"><span class="nv-av" aria-hidden="true"><img src="{{n.src}}" alt="" style="left: {{n.l}}; top: {{n.t}}; width: {{n.w}}"></span>{{n.label}}</button></sc-for></div>
<div class="lr-na">''' + btn('Save name', '#', 'sm', 'onClick="{{saveName}}"', 'button') + '''<button type="button" class="ds-link" onClick="{{closePanel}}">Not now</button></div>
</div>
</sc-if>
<sc-if value="{{showNamed}}" hint-placeholder-val="{{ false }}">
<div class="lr-msg">''' + av() + '''<div class="lr-bub">{{hello}}</div></div>
<div class="lr-qs"><sc-for list="{{askSug}}" as="a" hint-placeholder-count="3"><a class="ds-chip" href="{{a.href}}">{{a.t}}</a></sc-for></div>
</sc-if>
</div>
<sc-if value="{{showNamed}}" hint-placeholder-val="{{ false }}">
<div class="lr-pf"><form class="ds-ask sm" action="#"><label class="sr-only" for="lr-ask">Ask your coach</label><input id="lr-ask" placeholder="Ask {{coachTitle}} anything…"><button type="submit" class="ds-send" aria-label="Send">''' + ic(I['send'], 18, 2.4) + '''</button></form></div>
</sc-if>
</aside>
</sc-if>'''

JS = r'''
class Component extends DCLogic {
  constructor(props) {
    super(props);
    var p = props || {};
    this.state = { st: p.state || 'A', coach: p.coach === undefined || p.coach === null ? 'Nova' : p.coach, panel: p.panel === true || p.panel === 'true', nav: false, draft: '', q: '', thinking: false, ti: 0, tab: 'All' };
    this.CH = { Nova: ['/_blob/398ca91d2832bb0ab6b0af61319676f4', '-87.50%', '-57.81%', '294.06%'], Maya: ['/_blob/a1da64159da9c302c3a1835dea8e5266', '-68.75%', '-105.00%', '235.25%'], Alex: ['/_blob/22972224648e9b26d4acac7cc3f7c3a8', '-72.97%', '-112.16%', '254.32%'], Sage: ['/_blob/343a6c48a0cc4849f5a082d9a10a83a4', '-75.68%', '-114.86%', '254.32%'] };
    this.TONE = { Data: ['linear-gradient(150deg,#1C3AA8,#0B1433)', '#FFFFFF', 0], Design: ['linear-gradient(150deg,#7FA4FF,#4C7DFF)', '#FFFFFF', 1], Software: ['linear-gradient(150deg,#4C7DFF,#1652F0)', '#FFFFFF', 2], Business: ['linear-gradient(150deg,#DCE5FB,#EAF0FF)', '#1652F0', 4], Leadership: ['linear-gradient(150deg,#9DB8F7,#4C7DFF)', '#FFFFFF', 4] };
    this.TIER = { gold: ['Gold Validated', '#C8961E'], silver: ['Silver Validated', '#8E9BB0'], bronze: ['Bronze Validated', '#A8683A'] };
    var C = function (t, topic, by, lvl, tier, rating, reviews, hrs, dlp, why) { return { t: t, topic: topic, by: by, lvl: lvl, tier: tier, rating: rating, reviews: reviews, hrs: hrs, dlp: dlp, why: why }; };
    this.REC = {
      start: [C('Data Foundations: Spreadsheets to SQL', 'Data', 'Amara Okafor', 'Beginner', 'gold', '4.8', '3.4k', 12, 200, 'A popular first step on Credalio.'),
        C('UX and Product Design Foundations', 'Design', 'Lena Fischer', 'Beginner', 'silver', '4.7', '1.2k', 12, 900, 'Loved by career changers.'),
        C('Python for Everyday Automation', 'Software', 'Priya Nair', 'Beginner', 'bronze', '4.6', '1.6k', 9, 800, 'Trending this month.'),
        C('Stakeholder Communication', 'Business', 'Grace Adeyemi', 'Beginner', 'silver', '4.7', '890', 3, 300, 'Short, and useful in any role.')],
      ready: [C('Data Foundations: Spreadsheets to SQL', 'Data', 'Amara Okafor', 'Beginner', 'gold', '4.8', '3.4k', 12, 200, 'Stage 1 of your journey.'),
        C('SQL for Data Analysis', 'Data', 'Daniel Reyes', 'Beginner', 'gold', '4.8', '2.1k', 14, 500, 'Stage 2: your core skills.'),
        C('Statistics for Analysts', 'Business', 'Northgate University', 'Intermediate', 'silver', '4.7', '980', 12, 600, 'Picked for your starting level.'),
        C('Data Visualisation with Power BI', 'Software', 'Mia Lopez', 'Beginner', 'silver', '4.7', '1.4k', 10, 600, 'Where your journey heads next.')],
      interests: [C('Data Foundations: Spreadsheets to SQL', 'Data', 'Amara Okafor', 'Beginner', 'gold', '4.8', '3.4k', 12, 200, 'Matches your interest in Data.'),
        C('Introduction to AI', 'Software', 'Northgate University', 'Beginner', 'gold', '4.8', '2.6k', 8, 400, 'Matches your interest in AI.'),
        C('Business Analytics', 'Business', 'Harbour School of Finance', 'Beginner', 'silver', '4.7', '940', 10, 800, 'Where Data and Business meet.'),
        C('Prompt Writing for Work', 'Design', 'Priya Nair', 'Beginner', 'silver', '4.7', '1.8k', 4, 300, 'Quick, practical AI skills.')],
      goal: [C('Leadership Foundations', 'Leadership', 'Hannah Cole', 'Beginner', 'gold', '4.8', '1.1k', 8, 800, 'Built around your goal.'),
        C('Managing High-Performance Teams', 'Business', 'Westbridge Institute', 'Intermediate', 'silver', '4.7', '760', 10, 1000, 'The next step for new leaders.'),
        C('Communication for Leaders', 'Design', 'Grace Adeyemi', 'Beginner', 'silver', '4.7', '890', 5, 600, 'Popular with people who share your goal.'),
        C('Leading Remote Teams', 'Leadership', 'Tom Hughes', 'Intermediate', 'silver', '4.7', '460', 5, 600, 'Short and practical.')],
      active: [C('Advanced SQL', 'Data', 'Daniel Reyes', 'Intermediate', 'gold', '4.8', '1.3k', 12, 1200, 'Part of your Data Analyst path.'),
        C('Data Visualisation with Power BI', 'Software', 'Mia Lopez', 'Beginner', 'silver', '4.7', '1.4k', 10, 600, 'Next in Core skills.'),
        C('Python for Data Analysis', 'Design', 'Priya Nair', 'Intermediate', 'silver', '4.7', '1.6k', 16, 900, 'Picked from your progress so far.'),
        C('Statistics for Analysts', 'Business', 'Northgate University', 'Intermediate', 'silver', '4.7', '980', 12, 600, 'Makes your SQL work sharper.')]
    };
  }
  componentDidMount() { this.aurScan(); if (this.state.panel) this.think(); }
  componentWillUnmount() { if (this._aurMo) this._aurMo.disconnect(); clearTimeout(this._t); }
  think() {
    var self = this, steps = ['Reading your profile…', 'Checking what you’ve picked so far…', 'Getting ready to help…'];
    clearTimeout(this._t);
    this.setState({ thinking: true, ti: 0 });
    var tick = function (i) { self._t = setTimeout(function () { if (i < steps.length) { self.setState({ ti: i }); tick(i + 1); } else self.setState({ thinking: false }); }, 800); };
    this.steps = steps; tick(1);
  }
  renderVals() {
    var self = this, S = this.state, st = S.st;
    var name = (S.coach || '').trim(), named = !!name, ch = this.CH[name] || this.CH.Nova, coachN = named ? name : 'your AI Coach';
    var hr = new Date().getHours();
    var isNew = ['A', 'B', 'C', 'R'].indexOf(st) > -1, isActive = !isNew && st !== 'L';
    var tierK = { D: 'basic', E: 'basic', F: 'basic', G: 'basic', I: 'basic', W: 'basic', H: 'pro' }[st] || 'free', paid = tierK !== 'free';
    var dlpN = { A: 200, B: 200, C: 200, R: 200, D: 1460, E: 1460, F: 1320, G: 1450, H: 4800, I: 1460, L: 0, W: 180 }[st];
    var allow = { free: 200, basic: 2000, pro: 6000 }[tierK];
    var fmt = function (n) { return n.toLocaleString('en-GB'); };
    var tone = this.TONE, tier = this.TIER;
    var recKey = { R: 'ready', B: 'interests', C: 'goal' }[st] || (isActive ? 'active' : 'start');
    var recs = this.REC[recKey].map(function (c) {
      var tn = tone[c.topic], v = { t: c.t, by: c.by, lvl: c.lvl, rating: c.rating, reviews: c.reviews, hrs: c.hrs + ' hrs', dlp: fmt(c.dlp), why: c.why, href: c.dlp === 200 ? 'CourseDetail-Learner.dc.html' : 'CourseDetail.dc.html',
        ini: c.by.split(' ').map(function (w) { return w[0]; }).slice(0, 2).join(''), bg: tn[0], icoC: tn[1], tierLabel: tier[c.tier][0], tierDot: tier[c.tier][1] };
      for (var i = 0; i < 5; i++) v['i' + i] = tn[2] === i ? 'inline' : 'none';
      return v;
    });
    var open = function () { self.setState({ panel: true, nav: false }); self.think(); };
    var GS = {
      R: [['Account created', 'd'], ['Journey built', 'd'], ['Start Stage 1', 'l', 'CourseDetail-Learner.dc.html']],
      B: [['Account created', 'd'], ['Interests picked', 'd'], ['Start your first lesson', 'l', 'Explore.dc.html']],
      C: [['Account created', 'd'], ['Goal set', 'd'], ['Build your journey', 'l', 'Journey.dc.html']]
    };
    var gs = GS[st] || [['Account created', 'd'], named ? ['Coach named', 'd'] : ['Name your coach', 'b'], ['Start your first lesson', named ? 'l' : 'o', 'Explore.dc.html']];
    var firstOpen = true;
    var gsv = gs.map(function (g) { var nx = g[1] !== 'd' && firstOpen; if (g[1] !== 'd') firstOpen = false; var kind = g[1] === 'o' ? 'l' : g[1];
      return { t: g[0], isDone: g[1] === 'd', isBtn: kind === 'b', isLink: kind === 'l', href: g[2] || '#', go: open, cls: nx ? 'next' : '' }; });
    var NOVA = {
      A: ['Not sure where to begin? Tell me a goal and I’ll build a journey around it in about two minutes.', 'Build my journey', 'Journey.dc.html'],
      C: ['Leaders grow fastest with regular feedback practice. Want me to plan a short session for each week?', 'Plan my week', ''],
      R: ['I’ll adapt your journey as you learn. If something feels too easy, too slow or not for you, just tell me.', 'Ask about my journey', ''],
      D: ['You’re 62% through SQL for Data Analysis. Your last quiz suggests JOINs need a little more practice before you move on.', 'Practise with ' + (named ? name : 'your coach'), '']
    };
    NOVA.B = NOVA.A; NOVA.E = NOVA.D; NOVA.I = NOVA.D; NOVA.W = NOVA.D;
    var nv = NOVA[st] || NOVA.A;
    var postsNew = [['Getting started', 'What I wish I’d known in my first week', 'Priya Nair', 'PN', 31], ['Choosing a path', 'Course, path or certification: how I decided', 'Daniel Reyes', 'DR', 18], ['Learning habits', 'Twenty minutes a day changed everything', 'Grace Adeyemi', 'GA', 24]];
    var postsData = [['Data Analytics', 'How I finally understood JOINs', 'Daniel Reyes', 'DR', 12], ['Career change', 'From classroom to analyst in eight months', 'Priya Nair', 'PN', 28], ['SQL', 'Weekly SQL practice group: join us', 'Tom Hughes', 'TH', 9]];
    var postsLead = [['Leadership', 'The one-to-one question that changed my team', 'Tom Hughes', 'TH', 22], ['Feedback', 'Giving feedback without the dread', 'Grace Adeyemi', 'GA', 17], ['New managers', 'My first 90 days leading people', 'Priya Nair', 'PN', 26]];
    var posts = (st === 'C' ? postsLead : (isNew && st !== 'R' ? postsNew : postsData)).map(function (x) { return { tag: x[0], t: x[1], by: x[2], ini: x[3], n: x[4] }; });
    var CHN = this.CH;
    var ROUTES = {
      R: [['1', 'Foundation', '2 courses', 'now', 'You start here'], ['2', 'Core skills', '3 courses'], ['3', 'Practice', '2 projects'], ['4', 'Certification', '1 exam'], ['✓', 'Job-ready', 'Your portfolio', 'end']],
      D: [['✓', 'Foundation', 'Completed', 'done'], ['2', 'Core skills', '1 of 3 courses', 'now', 'You’re here'], ['3', 'Practice', '2 projects'], ['4', 'Certification', '1 exam'], ['✓', 'Job-ready', 'Your portfolio', 'end']]
    };
    var route = (ROUTES[st] || ROUTES.D).map(function (r) { return { mark: r[0], label: r[1], note: r[2], cls: r[3] || '', here: !!r[4], hereT: r[4] || '' }; });
    var stat = function (k, v, of, href, cn) { return { k: k, v: v, of: of || '', href: href, coin: !!cn }; };
    var counts = { D: [4, 8], E: [4, 8], F: [2, 2], G: [3, 5], H: [2, 6], I: [4, 8], W: [4, 8] }[st] || [0, 0];
    var ML = { D: [['Data Analyst', 'Career Path', 32, 'Stage 2 of 5'], ['SQL for Data Analysis', 'Course', 62, 'Module 4 of 8'], ['Professional Certificate in Data Analysis', 'Certification', 18, 'Learning 2 of 6'], ['Applied Data Program', 'Learning Program', -1, 'Starts 12 October']] };
    ML.E = ML.D; ML.I = ML.D; ML.W = ML.D;
    var items = ML[st] || [];
    var TABS = [['All', null], ['Career paths', 'Career Path'], ['Courses', 'Course'], ['Certifications', 'Certification'], ['Programs', 'Learning Program']];
    var tabT = (TABS.filter(function (t) { return t[0] === S.tab; })[0] || TABS[0])[1];
    var shown = items.filter(function (m) { return !tabT || m[1] === tabT; });
    var TI = { 'Career Path': 0, Course: 1, Certification: 2, 'Learning Program': 3 };
    var mlItems = shown.map(function (m) { var v = { t: m[0], type: m[1], sub: m[3], pct: (m[2] < 0 ? 0 : m[2]) + '%', pctLabel: m[2] < 0 ? 'Upcoming' : m[2] + '%', barCls: m[2] === 100 ? 'ok' : '',
      cta: m[2] < 0 ? 'View' : (m[2] === 100 ? 'Review' : 'Continue'), href: m[1] === 'Career Path' ? 'PathDetail-Learner.dc.html' : (m[1] === 'Certification' ? 'CertDetail.dc.html' : (m[1] === 'Learning Program' ? 'ProgramDetail.dc.html' : 'CourseDetail-Learner.dc.html')) };
      for (var i = 0; i < 4; i++) v['i' + i] = TI[m[1]] === i ? 'inline' : 'none'; return v; });
    var mlTabs = TABS.map(function (t) { var on = (S.tab || 'All') === t[0]; return { label: t[0], n: t[1] ? items.filter(function (m) { return m[1] === t[1]; }).length : items.length, cls: on ? 'on' : '', sel: on ? 'true' : 'false', pick: function () { self.setState({ tab: t[0] }); } }; });
    var EV = [[1, 'Today', '7:00 PM', 'SQL JOINs · Lesson 4', 'Lesson', 'blue'], [0, '', '8:00 PM', 'Tutor session with Hannah', 'Tutor', 'line'], [1, 'Tomorrow · Monday 28', '6:00 PM', 'Live session: Querying real datasets', 'Live', 'line'], [0, '', '11:59 PM', 'Knowledge Check due', 'Due', 'amber'], [1, 'Tuesday 29', '11:59 PM', 'SQL Data Cleaning Project due', 'Due', 'amber']];
    var DAYS = [['Sun', 27, 'today'], ['Mon', 28, 'ev'], ['Tue', 29, 'ev'], ['Wed', 30, ''], ['Thu', 1, 'ev'], ['Fri', 2, ''], ['Sat', 3, '']];
    var AS = [['Knowledge Check', 'SQL for Data Analysis', 'Due tomorrow', 'amber', '~15 min', 'Start'], ['SQL Data Cleaning Project', 'Data Analyst Career Path', 'Due Tue 29 Sep', '', '~1 hr 30 min', 'Continue']];
    var discSub = { B: 'You picked Data, Business and AI. Start with a suggestion below, or search for anything else.' }[st] || 'Search for something you’re curious about, or browse what people are learning.';
    var dNova = { B: 'I can turn your interests into a starting journey. It takes about two minutes.' }[st] || 'Not sure yet? Tell me where you’d like to be, and I’ll build a journey around it.';
    var REC_T = { R: ['Next on your journey', 'Picked by ' + coachN + ' for your Data Analyst journey.'], B: ['Picked for your interests', 'Based on Data, Business and AI.'], C: ['For your goal', 'Learning that builds towards becoming a stronger leader.'], active: ['Recommended for you', 'Based on your Data Analyst path and your progress.'], start: ['Good places to start', 'Popular first steps, while you find your direction.'] }[st === 'R' || st === 'B' || st === 'C' ? st : (isActive ? 'active' : 'start')];
    return {
      navCls: S.nav ? 'ds-open' : '', toggleNav: function () { self.setState({ nav: !S.nav }); },
      date: 'Sunday 27 September',
      greeting: hr < 12 ? 'Good morning' : (hr < 18 ? 'Good afternoon' : 'Good evening'),
      coachSrc: ch[0], coachL: ch[1], coachT: ch[2], coachW: ch[3],
      coachTitle: named ? name : 'AI Coach', coachBtn: named ? 'Ask ' + name : 'AI Coach', coachNav: named ? name + ' · AI Coach' : 'Your AI Coach',
      openPanel: open, closePanel: function () { clearTimeout(self._t); self.setState({ panel: false, thinking: false }); },
      panelOpen: S.panel, thinking: S.thinking, thinkText: (this.steps || ['Reading your profile…'])[S.ti] || '',
      showUnnamed: S.panel && !S.thinking && !named, showNamed: S.panel && !S.thinking && named,
      hello: st === 'R' ? 'Hi Ada. Your Data Analyst journey is ready. Want a quick tour of Stage 1, or shall we start?' : (isActive ? 'Hi Ada. You’re on Core skills, 62% through SQL for Data Analysis. What would help right now?' : 'Hi Ada. I’m ' + name + '. What would you like to do today?'),
      askSug: (st === 'R' ? [['What happens in Stage 1?', 'JourneyPlan-Saved.dc.html'], ['Do I have enough DLP for my journey?', '#'], ['Can I go faster?', 'JourneyPlan-Saved.dc.html']]
        : (isActive ? [['Give me a quick JOINs practice', '#'], ['Explain today’s lesson simply', '#'], ['Do I have enough DLP to finish my path?', '#']]
        : [['Help me choose what to learn', 'Journey.dc.html'], ['Build a journey towards a goal', 'Journey.dc.html'], ['Explain how DLP works', '#']])).map(function (a) { return { t: a[0], href: a[1] }; }),
      draft: S.draft, onDraft: function (e) { self.setState({ draft: e.target.value }); },
      nameSug: ['Nova', 'Maya', 'Alex', 'Sage'].map(function (n) { var on = S.draft.trim() === n, c = CHN[n]; return { label: n, src: c[0], l: c[1], t: c[2], w: c[3], on: on ? 'true' : 'false', cls: on ? 'on' : '', pick: function () { self.setState({ draft: n }); } }; }),
      saveName: function () { self.setState({ coach: S.draft.trim() || 'Nova', draft: '' }); },
      dlp: fmt(dlpN),
      planName: { free: 'Free plan', basic: 'Basic plan', pro: 'Pro plan' }[tierK], planSub: fmt(allow) + ' DLP each month', planCta: tierK === 'pro' ? 'Manage' : 'Upgrade',
      hasAsg: isActive, asgN: AS.length,
      isNew: isNew, isActive: isActive, gs: gsv, gsDone: gs.filter(function (g) { return g[1] === 'd'; }).length,
      stats: [stat('In progress', counts[0], '', '#'), stat('Completed', counts[1], '', '#'), stat('DLP', fmt(dlpN), '/ ' + fmt(allow), '#', true), stat('Season LAS', paid ? '1,240' : '—', '', '#')],
      fDisc: st === 'A' || st === 'B', fGoal: st === 'C', fReady: st === 'R', fJourney: ['D', 'E', 'I', 'W'].indexOf(st) > -1,
      dKicker: 'Welcome to Credalio', dSub: discSub, dNova: dNova, dNovaCta: 'Build my journey',
      q: S.q, onQ: function (e) { self.setState({ q: e.target.value }); },
      disc: [['Courses', 'Courses.dc.html'], ['Career paths', 'CareerPaths.dc.html'], ['Certifications', 'Certifications.dc.html'], ['Programs', 'Programs.dc.html']].map(function (d) { return { t: d[0], h: d[1] }; }),
      route: route,
      jKicker: st === 'D' ? 'Your current journey · Career Path' : 'Your current journey · built with ' + coachN, jTitle: 'Data Analyst', jPct: '32%', jStage: 'Stage 2 of 5',
      nxCtx: 'SQL for Data Analysis', nxTitle: 'SQL JOINs · Lesson 4', nxPct: '62%', nxMeta: '62% of the course · about 22 min',
      jViewHref: st === 'D' ? 'PathDetail-Learner.dc.html' : 'JourneyPlan-Saved.dc.html', jCta: 'Continue', jCtaHref: 'CourseDetail-Learner.dc.html',
      wkRange: '27 September – 3 October',
      days: DAYS.map(function (d) { return { w: d[0], n: d[1], cls: d[2] }; }),
      sched: EV.map(function (e) { return { head: !!e[0], day: e[1], time: e[2], t: e[3], type: e[4], tc: e[5] }; }),
      assigns: AS.map(function (a) { return { t: a[0], ctx: a[1], due: a[2], dueCls: a[3], est: a[4], cta: a[5], href: 'CourseDetail-Learner.dc.html' }; }),
      wgDone: 4, wgAll: 6, wgPct: '67%', wgNote: 'On track. Two more sessions this week will get you there.',
      mlTabs: mlTabs, mlItems: mlItems, mlEmpty: shown.length === 0,
      seasonOn: isActive && paid,
      recTitle: REC_T[0], recSub: REC_T[1], recs: recs,
      novaKicker: named ? name + ' · Your AI Coach' : 'Your AI Coach',
      novaMsg: named ? nv[0] : 'Want to make your coach your own? Give it a name and choose how it talks to you.',
      novaLink: named ? 'Ask ' + name : 'Ask a question',
      novaCta: named ? nv[1] : 'Name your coach', novaIsBtn: !named || !nv[2], novaIsLink: named && !!nv[2], novaHref: nv[2] || '#',
      showTutor: ['D', 'E', 'I', 'W'].indexOf(st) > -1,
      commSub: st === 'C' ? 'Conversations from learners growing as leaders.' : (st === 'R' || isActive ? 'Conversations from learners on a similar journey.' : 'Tips from learners who started where you are.'),
      posts: posts, showBand: !named || (st !== 'A' && st !== 'B')
    };
  }
''' + AURORA_JS + '''
}
'''

PROPS = {"state": {"editor": "enum", "options": ["A", "B", "C", "R", "D", "E", "F", "G", "H", "I", "L", "W"], "default": "A"},
         "coach": {"editor": "text", "default": "Nova"}, "panel": {"editor": "boolean", "default": False},
         "$preview": {"width": 1440, "height": 2000}}

HTML = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Learner dashboard</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">
<style>
''' + KIT_CSS + '\n' + AUR_CSS + '\n' + CSS + '''</style>
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
