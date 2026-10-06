# Dashboard shell (sidebar + top bar) for Creator Studio screens
P='/home/user/credalio/design/canvas/project/'
IMG='/_blob/bad84659fa9f24b3a7efb7e88696e531'

def ICON(d, size=20, sw=1.8):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'
SPARK_D='<path d="M12 2l1.9 6.1L20 10l-6.1 1.9L12 18l-1.9-6.1L4 10l6.1-1.9z" fill="currentColor" stroke="none"></path>'
I={
 'dash':'<rect x="3.5" y="3.5" width="7" height="7" rx="2"></rect><rect x="13.5" y="3.5" width="7" height="7" rx="2"></rect><rect x="3.5" y="13.5" width="7" height="7" rx="2"></rect><rect x="13.5" y="13.5" width="7" height="7" rx="2"></rect>',
 'exp':'<path d="M4 19.5V5a2 2 0 0 1 2-2h14v18H6.5A2.5 2.5 0 0 1 4 18.5"></path><path d="M8 7h8"></path>',
 'new':'<circle cx="12" cy="12" r="9"></circle><path d="M12 8v8M8 12h8"></path>',
 'assigned':'<rect x="5" y="4" width="14" height="17" rx="2"></rect><path d="M9 3.5h6v3H9zM9 12h6M9 16h4"></path>',
 'valid':'<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"></path><path d="m9 12 2 2 4-4"></path>',
 'disc':'<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"></path>',
 'support':'<circle cx="12" cy="12" r="9"></circle><circle cx="12" cy="12" r="3.5"></circle><path d="m5.6 5.6 3.9 3.9M14.5 14.5l3.9 3.9M18.4 5.6l-3.9 3.9M9.5 14.5l-3.9 3.9"></path>',
 'cal':'<rect x="3" y="5" width="18" height="16" rx="2"></rect><path d="M3 10h18M8 3v4M16 3v4"></path>',
 'learners':'<circle cx="9" cy="8" r="3.5"></circle><path d="M2.5 20a6.5 6.5 0 0 1 13 0"></path><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14.5a6.5 6.5 0 0 1 3.5 5.5"></path>',
 'analytics':'<path d="M3 20h18M6.5 16v-5M11.5 16V6M16.5 16v-8"></path>',
 'earn':'<circle cx="12" cy="12" r="9"></circle><path d="M15 9.5c-.5-1-1.6-1.5-3-1.5-1.7 0-3 .9-3 2s1.3 1.7 3 2 3 .9 3 2-1.3 2-3 2c-1.4 0-2.5-.5-3-1.5M12 6v2M12 16v2"></path>',
 'wallet':'<rect x="3" y="6" width="18" height="14" rx="3"></rect><path d="M3 10h18M16 15h2"></path>',
 'nova':SPARK_D,
 'centre':'<path d="m2 9 10-5 10 5-10 5z"></path><path d="M6 11v5c0 1.5 2.7 3 6 3s6-1.5 6-3v-5"></path>',
 'profile':'<circle cx="12" cy="8" r="4"></circle><path d="M4 21a8 8 0 0 1 16 0"></path>',
 'ready':'<path d="M12 3l2.3 1.7 2.9-.1.9 2.7 2.3 1.7-.9 2.7.9 2.7-2.3 1.7-.9 2.7-2.9-.1L12 21l-2.3-1.7-2.9.1-.9-2.7L3.6 15l.9-2.7-.9-2.7 2.3-1.7.9-2.7 2.9.1z"></path><path d="m9 12 2 2 4-4"></path>',
 'settings':'<circle cx="12" cy="12" r="3"></circle><path d="M12 2.5v2.2M12 19.3v2.2M4.6 4.6l1.6 1.6M17.8 17.8l1.6 1.6M2.5 12h2.2M19.3 12h2.2M4.6 19.4l1.6-1.6M17.8 6.2l1.6-1.6"></path>',
 'search':'<circle cx="11" cy="11" r="7"></circle><path d="m20 20-3.5-3.5"></path>',
 'bell':'<path d="M18 16V11a6 6 0 1 0-12 0v5l-2 2h16z"></path><path d="M10 21h4"></path>',
 'help':'<circle cx="12" cy="12" r="9"></circle><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6v.6M12 17h.01"></path>',
 'menu':'<path d="M4 7h16M4 12h16M4 17h16"></path>',
 'close':'<path d="M6 6l12 12M18 6 6 18"></path>',
 'arrow':'<path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path>',
 'back':'<path d="M19 12H5"></path><path d="m11 18-6-6 6-6"></path>',
 'check':'<path d="m5 12.5 4.5 4.5L19 7.5"></path>',
 'pencil':'<path d="M4 20h4L19 9a2.8 2.8 0 0 0-4-4L4 16z"></path><path d="m13.5 6.5 4 4"></path>',
 'send':'<path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path>',
 'course':'<path d="M2.5 5.5C5 4 8.5 4 12 6c3.5-2 7-2 9.5-.5V19c-2.5-1.5-6-1.5-9.5.5-3.5-2-7-2-9.5-.5z"></path><path d="M12 6v13.5"></path>',
 'cert':'<circle cx="12" cy="9" r="6"></circle><path d="m8.5 13.8-1.5 7.2 5-3 5 3-1.5-7.2"></path>',
 'path':'<circle cx="6" cy="19" r="2.5"></circle><circle cx="18" cy="5" r="2.5"></circle><path d="M8.5 19H16a3.5 3.5 0 0 0 0-7H8a3.5 3.5 0 0 1 0-7h7.5"></path>',
 'program':'<rect x="3" y="5" width="18" height="16" rx="2"></rect><path d="M3 10h18M8 3v4M16 3v4M7.5 14h3M7.5 17h6"></path>',
}

def NOVA_AV(d, ring=True):
    sh = 'box-shadow: 0 0 0 3px #FFFFFF, 0 0 0 4.5px #D6DDEE; ' if ring else ''
    return f'<span aria-hidden="true" style="position: relative; flex-shrink: 0; width: {d}px; height: {d}px; border-radius: 50%; overflow: hidden; background: #EAF0FF; {sh}display: block"><img src="/_blob/b8f0756720795e1bd3b02e9c2655cb25" alt="" style="position: absolute; left: -87.50%; top: -57.81%; width: 294.06%; max-width: none; height: auto; mix-blend-mode: multiply"></span>'

NAV=[('Dashboard',[('dash','Dashboard','CR-DASH-NEW.dc.html',None)]),
 ('Create',[('exp','My learning experiences','#',None),('new','Create new','CR-CREATE-001.dc.html',None)]),
 ('Work',[('assigned','Assigned to me','#',None),('valid','Validation Centre','#',None),('disc','Discussions','#',None),('support','Learner support','#',None),('cal','Calendar','#',None)]),
 ('Insights',[('learners','Learners','#',None),('analytics','Analytics','#',None)]),
 ('Economy',[('earn','Earnings & payouts','#',None),('wallet','Credit Wallet','#',None)]),
 ('Creator',[('nova','Nova · your Copilot','#',None),('centre','Creator Centre','CR-CTR-001.dc.html',None),('profile','Creator profile','#',None),('ready','Verification & readiness','CR-RDY-001.dc.html','3')]),
 ('Account',[('settings','Settings','#',None)])]

def SIDEBAR(active):
    h=''
    for gi,(g,items) in enumerate(NAV):
        if gi>0: h+=f'<span class="ds-glab">{g}</span>'
        for k,label,href,badge in items:
            on = (label==active)
            cur=' aria-current="page"' if on else ''
            cls=' ds-on' if on else ''
            h+=f'<a href="{href}" class="ds-item{cls}"{cur}>{ICON(I[k],19)}<span style="flex-grow: 1; min-width: 0">{label}</span>'+(f'<span class="ds-badge" aria-label="{badge} to do">{badge}</span>' if badge else '')+'</a>'
    return h

LOGO='''<a href="CR-DASH-NEW.dc.html" style="display: flex; align-items: center; gap: 10px; text-decoration: none">
<span style="width: 32px; height: 32px; border-radius: 9px; background: #1652F0; display: flex; align-items: center; justify-content: center"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" aria-hidden="true"><path d="M17.5 7.2A7 7 0 1 0 17.5 16.8"></path></svg></span>
<span class="ds-brand" style="font-size: 20px; font-weight: 600; letter-spacing: -0.02em; color: #0B1433">Credalio</span></a>'''

DASH_CSS='''body{margin:0;background:#F7F9FD}
a{color:#1652F0}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@keyframes obIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
@keyframes cpPop{from{opacity:0;transform:translateY(8px) scale(.98)}to{opacity:1;transform:none}}
@keyframes cpDot{0%,80%,100%{opacity:.25;transform:translateY(0)}40%{opacity:1;transform:translateY(-3px)}}
@keyframes dsRing{from{stroke-dashoffset:1}}
.ob-in{animation:obIn .5s ease both}.ob-in2{animation:obIn .5s ease .08s both}.ob-in3{animation:obIn .5s ease .16s both}.ob-in4{animation:obIn .5s ease .24s both}
.cp-pop{animation:cpPop .4s ease both}
.cp-dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:#1652F0;animation:cpDot 1.2s ease-in-out infinite}
.ds-root{display:grid;grid-template-columns:264px minmax(0,1fr);min-height:100vh;background:#F7F9FD;font-family:'Google Sans','Google Sans Text','Helvetica Neue',system-ui,sans-serif;color:#0B1433}
.ds-side{position:sticky;top:0;height:100vh;overflow-y:auto;box-sizing:border-box;padding:22px 14px 24px 14px;background:#FFFFFF;border-right:1.5px solid #E6EAF3;display:flex;flex-direction:column;gap:2px;z-index:20}
.ds-glab{display:block;margin:16px 12px 6px 12px;font-size:12px;font-weight:600;color:#8A93AD}
.ds-item{display:flex;align-items:center;gap:12px;min-height:40px;padding:0 12px;border-radius:12px;color:#3A4566;font-size:14.5px;font-weight:500;text-decoration:none;transition:background .2s ease,color .2s ease}
.ds-item svg{flex-shrink:0;color:#5B6582}
.ds-item:hover{background:#F5F8FF;color:#0B1433}
.ds-on{background:#EAF0FF !important;color:#0E3BB8 !important;font-weight:600}
.ds-on svg{color:#1652F0}
.ds-badge{min-width:22px;height:22px;padding:0 6px;box-sizing:border-box;border-radius:999px;background:#1652F0;color:#FFFFFF;font-size:12px;font-weight:600;display:flex;align-items:center;justify-content:center}
.ds-top{position:sticky;top:0;z-index:10;height:72px;box-sizing:border-box;padding:0 clamp(20px,3vw,40px);display:flex;align-items:center;gap:12px;background:rgba(247,249,253,.88);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}
.ds-search{flex:1 1 auto;max-width:440px;height:44px;box-sizing:border-box;display:flex;align-items:center;gap:10px;padding:0 16px;border-radius:999px;background:#FFFFFF;border:1.5px solid #E6EAF3;color:#8A93AD;font-size:14px}
.ds-search input{border:0;outline:none;background:transparent;font-family:inherit;font-size:14px;color:#0B1433;flex-grow:1;min-width:0}
.ds-search input::placeholder{color:#8A93AD}
.ds-icon-btn{width:44px;height:44px;flex-shrink:0;box-sizing:border-box;border-radius:50%;border:1.5px solid #E6EAF3;background:#FFFFFF;color:#3A4566;display:flex;align-items:center;justify-content:center;cursor:pointer;position:relative;text-decoration:none}
.ds-icon-btn:hover{border-color:#AFC1F5}
.ds-tok{height:44px;flex-shrink:0;box-sizing:border-box;display:flex;align-items:center;gap:7px;padding:0 14px 0 7px;border-radius:999px;background:linear-gradient(135deg,#FFFAEB,#FFF1CF);border:1.5px solid #F4D98E;font-size:14.5px;font-weight:600;color:#4A3300;text-decoration:none;box-shadow:0 6px 16px rgba(214,150,30,.12);transition:box-shadow .2s ease}
.ds-tok:hover{box-shadow:0 8px 20px rgba(214,150,30,.24)}
.ds-main{box-sizing:border-box;width:100%;max-width:1200px;padding:12px clamp(20px,3vw,40px) 56px clamp(20px,3vw,40px)}
.ds-h1{margin:0;font-size:clamp(28px,2.5vw,36px);line-height:1.15;font-weight:600;letter-spacing:-0.03em;color:#0B1433}
.ds-sub{margin:8px 0 0 0;font-size:16px;line-height:1.55;color:#4A5578}
.ds-card{background:#FFFFFF;border:1.5px solid #E6EAF3;border-radius:20px;box-shadow:0 1px 2px rgba(11,20,51,.03)}
.ds-btn{display:inline-flex;align-items:center;gap:14px;height:52px;padding:0 6px 0 24px;box-sizing:border-box;border-radius:999px;background:#1652F0;color:#FFFFFF;font-family:inherit;font-size:15.5px;font-weight:600;text-decoration:none;white-space:nowrap;border:0;cursor:pointer;box-shadow:0 1px 0 rgba(255,255,255,.25) inset,0 10px 24px rgba(22,82,240,.24);transition:background .2s ease,transform .2s ease}
.ds-btn:hover{background:#0E3BB8;color:#FFFFFF;transform:translateY(-1px)}
.ds-btn .ob-arrow{width:40px;height:40px;border-radius:50%;background:#FFFFFF;color:#1652F0;display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:transform .3s cubic-bezier(.3,1.4,.5,1)}
.ds-btn:hover .ob-arrow{transform:translateX(3px)}
.ds-ghost{display:inline-flex;align-items:center;justify-content:center;gap:8px;height:48px;padding:0 20px;box-sizing:border-box;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;font-family:inherit;font-size:15px;font-weight:600;text-decoration:none;white-space:nowrap;cursor:pointer;transition:border-color .2s ease,background .2s ease}
.ds-ghost:hover{border-color:#1652F0;background:#F5F8FF;color:#0B1433}
.ds-link{display:inline-flex;align-items:center;gap:6px;color:#1652F0;font-weight:600;font-size:14.5px;text-decoration:none}
.ds-link:hover{color:#0E3BB8}
.ds-back{display:inline-flex;align-items:center;gap:8px;height:40px;padding:0 14px 0 10px;border-radius:999px;color:#3A4566;font-size:14px;font-weight:500;text-decoration:none;margin-left:-10px}
.ds-back:hover{background:#FFFFFF;color:#0B1433}
.ds-chip{display:inline-flex;align-items:center;height:40px;padding:0 16px;box-sizing:border-box;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;font-family:inherit;font-size:14px;font-weight:500;cursor:pointer;transition:border-color .2s ease,background .2s ease}
.ds-chip:hover{border-color:#1652F0;background:#F5F8FF}
.ds-menu,.ds-scrim,.ds-mlogo,.ds-close{display:none}
.ds-btn:focus-visible,.ds-ghost:focus-visible,.ds-chip:focus-visible,.ds-item:focus-visible,.ds-icon-btn:focus-visible,.ds-opt:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:2px}
@media (prefers-reduced-motion: reduce){.ob-in,.ob-in2,.ob-in3,.ob-in4,.cp-pop,.cp-dot{animation:none}}
@media (max-width: 440px){.ds-mlogo .ds-brand{display:none}}
@media (max-width: 1180px){.ds-root{grid-template-columns:232px minmax(0,1fr)}}
@media (max-width: 960px){
.ds-root{grid-template-columns:minmax(0,1fr)}
.ds-side{position:fixed;left:0;top:0;width:288px;max-width:86vw;transform:translateX(-102%);transition:transform .3s cubic-bezier(.2,.8,.2,1);box-shadow:0 24px 64px rgba(11,20,51,.18)}
.ds-side.ds-open{transform:none}
.ds-scrim.ds-open{display:block;position:fixed;inset:0;background:rgba(11,20,51,.32);z-index:15}
.ds-menu,.ds-mlogo{display:flex}
.ds-close{display:flex;position:absolute;right:12px;top:16px}
.ds-top{height:64px;padding:0 16px;gap:8px}
.ds-search,.ds-hide-sm{display:none !important}
.ds-tok{padding:0 12px 0 6px;height:40px}
.ds-icon-btn{width:40px;height:40px}
.ds-h1{font-size:24px !important;line-height:1.2}
.ds-sub{font-size:14.5px;margin-top:6px}
.ds-back{height:36px;font-size:13.5px}
.ds-chip{height:36px;font-size:13.5px;padding:0 14px}
.ds-btn{height:48px;font-size:15px}
.ds-btn .ob-arrow{width:36px;height:36px}
.ds-ghost{height:44px;font-size:14.5px}
.ds-root{overflow-x:hidden}
.ds-main{padding:12px 16px 32px 16px}
.ds-btn{justify-content:space-between}
}
'''

def COIN(uid, size=52):
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 64 64" aria-hidden="true" style="flex-shrink: 0; display: block"><defs><linearGradient id="{uid}a" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFE9A3"></stop><stop offset="0.45" stop-color="#F6C343"></stop><stop offset="1" stop-color="#D08A12"></stop></linearGradient><linearGradient id="{uid}b" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F9CF5A"></stop><stop offset="1" stop-color="#E2A024"></stop></linearGradient></defs><circle cx="32" cy="34" r="29" fill="#B8740A" opacity="0.35"></circle><circle cx="32" cy="32" r="29" fill="url(#{uid}a)"></circle><circle cx="32" cy="32" r="22" fill="url(#{uid}b)" stroke="#FFF1C2" stroke-opacity="0.7" stroke-width="1.5"></circle><path d="M32 18l2.9 9.3 9.3 2.9-9.3 2.9L32 42.4l-2.9-9.3-9.3-2.9 9.3-2.9z" fill="#FFF8DF"></path><ellipse cx="23" cy="19" rx="9" ry="5" fill="#FFFFFF" opacity="0.35" transform="rotate(-30 23 19)"></ellipse></svg>'''


def SHELL(active, content, title, script, extra_css='', preview_h=900):
    top = f'''<header class="ds-top">
<button type="button" class="ds-icon-btn ds-menu" onClick="{{{{toggleNav}}}}" aria-label="Open menu">{ICON(I["menu"],20)}</button>
<span class="ds-mlogo" style="flex-grow: 1">{LOGO}</span>
<label class="ds-search">{ICON(I["search"],18)}<span class="sr-only">Search</span><input placeholder="Search your learning experiences, learners, discussions…"></label>
<span class="ds-hide-sm" style="flex-grow: 1"></span>
<a href="#" class="ds-tok" aria-label="20,000 AI Tokens">{COIN('tp',28)}<span>20K</span><span class="ds-hide-sm" style="font-weight: 500; color: #6B4E16">AI Tokens</span></a>
<a href="#" class="ds-icon-btn ds-hide-sm" aria-label="Help">{ICON(I["help"],19)}</a>
<a href="#" class="ds-icon-btn" aria-label="Notifications, 1 new">{ICON(I["bell"],19)}<span style="position: absolute; right: 10px; top: 9px; width: 8px; height: 8px; border-radius: 50%; background: #E5484D; box-shadow: 0 0 0 2px #FFFFFF"></span></a>
<a href="#" aria-label="Your account" style="position: relative; width: 44px; height: 44px; flex-shrink: 0; border-radius: 50%; background: #0B1433; color: #FFFFFF; font-size: 14px; font-weight: 600; display: flex; align-items: center; justify-content: center; text-decoration: none">AO<span style="position: absolute; right: 0; bottom: 1px; width: 11px; height: 11px; border-radius: 50%; background: #0F6B45; border: 2px solid #F7F9FD"></span></a>
</header>'''
    side = f'''<div class="ds-scrim {{{{navCls}}}}" onClick="{{{{toggleNav}}}}"></div>
<nav class="ds-side {{{{navCls}}}}" aria-label="Main">
<div style="padding: 0 6px 14px 6px">{LOGO}</div>
<button type="button" class="ds-icon-btn ds-close" onClick="{{{{toggleNav}}}}" aria-label="Close menu">{ICON(I["close"],18)}</button>
{SIDEBAR(active)}
</nav>'''
    return f'''<!doctype html>
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
{DASH_CSS}{extra_css}</style>
</helmet>
<div class="ds-root">
{side}
<div style="min-width: 0; display: flex; flex-direction: column">
{top}
<main class="ds-main">
{content}
</main>
</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1440,"height":{preview_h}}}}}'>
{script}
</script>
</body>
</html>
'''

def BTNA(href, label, cls='ds-btn', extra=''):
    return f'<a href="{href}" class="{cls}" {extra}><span>{label}</span><span class="ob-arrow">{ICON(I["arrow"],18,2.4)}</span></a>'

NAV_JS = "navCls: this.state.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !this.state.nav })"

def WRAP(name, target, w, h, title, props=''):
    open(P+name,'w').write(f'''<!doctype html>
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
<style>body{{margin:0}}</style>
</helmet>
<div style="width: {w}px; height: {h}px; overflow: hidden; background: #F7F9FD">
<dc-import name="{target}"{props} hint-size="{w}px,{h}px"></dc-import>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
''')
