# b4_1019: Link 3 batch 4 sources, built from the LIVE CR-CREIO-POP dashboard (Studio canvas).
#   CR-PM  : account menu (variants menu / one = PM-001 / PM-002) + role switch page (variant switch = PM-003)
#   CR-MSG : message pop-ups (variants pops / reply / sent / many / hidden = MSG-001 … 005)
# usage: python3 b4_1019.py <canvas2/project dir>   (writes CR-PM.dc.html + CR-MSG.dc.html there)
import re, sys, os
D = sys.argv[1]
base = open(os.path.join(D, 'CR-CREIO-POP.dc.html')).read()

def svg(d, w=18, sw=1.9):
    return ('<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>') % (w, w, sw, d)
INFO = svg('<circle cx="12" cy="12" r="9"></circle><path d="M12 11v5"></path><path d="M12 7.6v.2"></path>', 15, 2.2)
def tip(t, c='r'):
    return '<span class="tip" tabindex="0" aria-label="More info">%s<span class="tip-b %s" role="tooltip">%s</span></span>' % (INFO, c, t)
I_PEN = svg('<path d="M12 20h9"></path><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"></path>')
I_VAL = svg('<path d="M12 3v18M5 21h14M6 7h12"></path><path d="m6 7-3 7a3 3 0 0 0 6 0zM18 7l-3 7a3 3 0 0 0 6 0z"></path>')
I_LRN = svg('<path d="M4 19.5V5a2 2 0 0 1 2-2h14v18H6.5A2.5 2.5 0 0 1 4 18.5"></path><path d="M8 7h8"></path>')
I_EYE = svg('<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"></path><circle cx="12" cy="12" r="3"></circle>')
I_USR = svg('<circle cx="12" cy="8" r="4"></circle><path d="M4 21a8 8 0 0 1 16 0"></path>')
I_SET = svg('<circle cx="12" cy="12" r="3"></circle><path d="M12 2.5v2.2M12 19.3v2.2M4.6 4.6l1.6 1.6M17.8 17.8l1.6 1.6M2.5 12h2.2M19.3 12h2.2M4.6 19.4l1.6-1.6M17.8 6.2l1.6-1.6"></path>')
I_HLP = svg('<circle cx="12" cy="12" r="9"></circle><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6v.6M12 17h.01"></path>')
I_OUT = svg('<path d="M15 4h3a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2h-3"></path><path d="M10 17l-5-5 5-5M5 12h11"></path>')
I_X = svg('<path d="M7 7l10 10M17 7 7 17"></path>', 15, 2.2)
I_GEAR = svg('<circle cx="12" cy="12" r="3"></circle><path d="M12 2.5v2.2M12 19.3v2.2M4.6 4.6l1.6 1.6M17.8 17.8l1.6 1.6M2.5 12h2.2M19.3 12h2.2M4.6 19.4l1.6-1.6M17.8 6.2l1.6-1.6"></path>', 15, 2)
I_SEND = svg('<path d="M12 19V5"></path><path d="m5 12 7-7 7 7"></path>', 16, 2.4)
I_OK = svg('<path d="m5 12.5 4.5 4.5L19 7.5"></path>', 13, 3)
I_LOCK = svg('<rect x="5" y="11" width="14" height="10" rx="2.5"></rect><path d="M8 11V8a4 4 0 0 1 8 0v3"></path>', 14, 2)

# ---- shared: plain Creio pill instead of the open Creio popover
a = base.index('<div class="tp-w">'); b = base.index('</section></div>', a) + len('</section></div>')
tw = base[a:b]
pill = tw[tw.index('<a href="CR-NOVA-001.dc.html"'):tw.index('</a>') + 4].replace(' tp-on', '').replace(' aria-expanded="true"', '')
pill = pill.replace('{{tokL}}', '20,000 Creio').replace('{{tokT}}', '20K')
pill = re.sub(r'<sc-if value="\{\{low\}\}".*?</sc-if>', '', pill)
def shell(html, avatar_html, extra_css, overlay, title, script, variant_root=False):
    s = html.replace(tw, pill)
    av0 = re.search(r'<a href="#" aria-label="Your account".*?</a>', s).group(0)
    s = s.replace(av0, avatar_html)
    s = s.replace('<div class="tp-scrim" aria-hidden="true"></div>', '')
    s = s.replace('</style>', extra_css + '\n</style>', 1)
    s = re.sub(r'<title>[^<]*</title>', '<title>%s</title>' % title, s)
    s = s.replace('</main>', '</main>' + overlay, 1)
    js = s.index('class Component extends DCLogic {'); je = s.index('</script>', js)
    return s[:js] + script + s[je:]
AV = ('position: relative; width: 44px; height: 44px; flex-shrink: 0; border-radius: 50%; background: #0B1433; color: #FFFFFF; '
      'font-size: 14px; font-weight: 600; display: flex; align-items: center; justify-content: center; text-decoration: none')
DOT = '<span class="pm-dot {{dotCls}}"></span>'

# ================= CR-PM =================
pm_css = '''.pm-w{position:relative;flex-shrink:0}
.pm-av{border:0;cursor:pointer;font-family:inherit}
.pm-av.on{box-shadow:0 0 0 4px rgba(22,82,240,.18)}
.pm-dot{position:absolute;right:0;bottom:1px;width:11px;height:11px;border-radius:50%;background:#0F6B45;border:2px solid #F7F9FD}
.pm-p{position:absolute;right:-6px;top:calc(100% + 12px);z-index:30;width:340px;box-sizing:border-box;padding:8px;border-radius:20px;background:#FFFFFF;border:1.5px solid #E6EAF3;box-shadow:0 24px 60px rgba(11,20,51,.16);text-align:left;font-size:14px;color:#0B1433}
.pm-me{display:flex;align-items:center;gap:12px;padding:12px 12px 14px 12px}
.pm-a{position:relative;width:42px;height:42px;flex-shrink:0;border-radius:50%;background:#0B1433;color:#FFFFFF;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:600}
.pm-me > span:last-child{display:flex;flex-direction:column;gap:2px;min-width:0}.pm-me b{font-size:15.5px;font-weight:600}.pm-me > span > span{font-size:13px;color:#5B6582}
.pm-sec{padding:12px;border-top:1.5px solid #F0F2F8}
.pm-lab{display:flex;align-items:center;font-size:12.5px;font-weight:500;color:#8A93AD}
.pm-st{margin-top:10px;display:flex;gap:6px}
.pm-st button{flex:1;height:36px;padding:0 8px;border-radius:999px;border:1.5px solid #E6EAF3;background:#FFFFFF;font-family:inherit;font-size:13px;font-weight:500;color:#3A4566;display:inline-flex;align-items:center;justify-content:center;gap:6px;cursor:pointer;white-space:nowrap}
.pm-st button.on{background:#F5F8FF;border-color:#1652F0;color:#0E3BB8}
.pm-st i{width:8px;height:8px;border-radius:50%;background:#0F6B45}.pm-st .aw i{background:#D98A00}.pm-st .dn i{background:#8A93AD}
.pm-rl{margin-top:8px;display:flex;flex-direction:column;gap:2px}
.pm-r{display:flex;align-items:center;gap:12px;padding:8px;border-radius:14px;text-decoration:none;color:#0B1433}
a.pm-r:hover{background:#F5F8FF}
.pm-ri{width:36px;height:36px;flex-shrink:0;border-radius:11px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.pm-r.cur .pm-ri{background:#1652F0;color:#FFFFFF}
.pm-r > span:nth-child(2){flex:1;min-width:0;display:flex;flex-direction:column;gap:1px}.pm-r b{font-size:14.5px;font-weight:600}.pm-r > span > span{font-size:13px;color:#5B6582}
.pm-ck{color:#1652F0;display:flex}
.pm-bd{min-width:22px;height:22px;padding:0 7px;box-sizing:border-box;border-radius:999px;background:#1652F0;color:#FFFFFF;font-size:12px;font-weight:500;display:flex;align-items:center;justify-content:center}
.pm-l{padding:6px 4px;border-top:1.5px solid #F0F2F8;display:flex;flex-direction:column}
.pm-l a{display:flex;align-items:center;gap:12px;min-height:42px;padding:0 8px;border-radius:12px;font-size:14.5px;font-weight:500;color:#3A4566;text-decoration:none}
.pm-l a svg{color:#5B6582}.pm-l a:hover{background:#F5F8FF;color:#0B1433}
.pm-scrim{position:fixed;inset:0;z-index:9;background:rgba(11,20,51,.06);pointer-events:none}
.rs{min-height:100vh;box-sizing:border-box;display:flex;flex-direction:column;background:radial-gradient(55% 40% at 50% 0%,rgba(22,82,240,.12),rgba(22,82,240,0) 70%),#FFFFFF;font-family:'Google Sans','Google Sans Text','Helvetica Neue',system-ui,sans-serif;color:#0B1433}
.rs-top{height:64px;box-sizing:border-box;display:flex;align-items:center;padding:0 24px;border-bottom:1.5px solid #EEF1F7}
.rs-m{flex:1;width:min(560px,100%);box-sizing:border-box;margin:0 auto;padding:72px 24px 40px 24px;display:flex;flex-direction:column;align-items:center;text-align:center}
.rs-emb{position:relative;width:84px;height:84px;border-radius:50%;background:#EAF0FF;display:flex;align-items:center;justify-content:center}
.rs-emb::after{content:'';position:absolute;inset:-6px;border-radius:50%;border:2px solid transparent;border-top-color:#1652F0;animation:rsSpin 1.4s linear infinite}
@keyframes rsSpin{to{transform:rotate(360deg)}}
.rs-emb span{width:58px;height:58px;border-radius:50%;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 12px 28px rgba(11,20,51,.16)}
.rs-pill{margin-top:16px;height:30px;padding:0 13px;border-radius:999px;background:#EAF0FF;color:#1652F0;font-size:13px;font-weight:500;display:inline-flex;align-items:center}
.rs-h{margin:10px 0 0 0;font-size:clamp(26px,4.2vh,36px);font-weight:600;letter-spacing:-0.02em;line-height:1.15}
.rs-sub{margin:10px 0 0 0;font-size:16px;line-height:1.55;color:#4A5578}
.rs-back{margin-top:28px;display:inline-flex;align-items:center;gap:8px;font-size:14.5px;font-weight:600;color:#3A4566;text-decoration:none}
.rs-back:hover{color:#1652F0}
@media (prefers-reduced-motion: reduce){.rs-emb::after{animation:none}}
@media (max-width: 960px){
.pm-w{position:static}
.pm-p{position:fixed;left:8px;right:8px;top:68px;width:auto}
.pm-scrim{background:rgba(11,20,51,.28)}
.rs-m{padding:48px 16px 32px 16px}.rs-h{font-size:24px}.rs-sub{font-size:14.5px}
}'''
roles = ('<sc-if value="{{multi}}" hint-placeholder-val="{{true}}"><div class="pm-sec"><span class="pm-lab">Switch role</span><div class="pm-rl">'
         '<div class="pm-r cur" aria-current="true"><span class="pm-ri">' + I_PEN + '</span><span><b>Creator</b><span>You’re here</span></span><span class="pm-ck">' + svg('<path d="m5 12.5 4.5 4.5L19 7.5"></path>', 16, 2.6) + '</span></div>'
         '<a href="CR-PM-003.dc.html" class="pm-r"><span class="pm-ri">' + I_VAL + '</span><span><b>Validator</b><span>2 reviews waiting</span></span><span class="pm-bd">2</span></a>'
         '<a href="#" class="pm-r"><span class="pm-ri">' + I_LRN + '</span><span><b>Learner</b><span>Your courses and progress</span></span></a>'
         '</div></div></sc-if>')
menu = ('<sc-if value="{{open}}" hint-placeholder-val="{{true}}"><div class="pm-scrim" aria-hidden="true"></div><section class="pm-p" role="dialog" aria-label="Account menu">'
        '<div class="pm-me"><span class="pm-a">AO' + DOT + '</span><span><b>Ada Ononuju</b><span>ada.ononuju@example.com</span></span></div>'
        '<div class="pm-sec"><span class="pm-lab">Status' + tip('Same as Calendar › Presence. Away pauses pop-ups.') + '</span>'
        '<div class="pm-st" role="radiogroup" aria-label="Status">'
        '<button type="button" role="radio" aria-checked="{{st0.on}}" class="{{st0.cls}}" onClick="{{st0.pick}}"><i></i>Available</button>'
        '<button type="button" role="radio" aria-checked="{{st1.on}}" class="aw {{st1.cls}}" onClick="{{st1.pick}}"><i></i>Away</button>'
        '<button type="button" role="radio" aria-checked="{{st2.on}}" class="dn {{st2.cls}}" onClick="{{st2.pick}}"><i></i>Do not disturb</button></div></div>'
        + roles +
        '<nav class="pm-l" aria-label="Account">'
        '<a href="CR-PROF-002.dc.html">' + I_EYE + 'View public profile</a>'
        '<a href="CR-PROF-001.dc.html">' + I_USR + 'Edit creator profile</a>'
        '<a href="CR-SET-001.dc.html">' + I_SET + 'Settings</a>'
        '<a href="CR-HELP-001.dc.html">' + I_HLP + 'Help &amp; Support</a>'
        '<a href="CR-LOG-001.dc.html">' + I_OUT + 'Sign out</a></nav></section></sc-if>')
pm_avatar = ('<div class="pm-w"><button type="button" class="pm-av {{avCls}}" aria-label="Account menu" aria-expanded="{{openA}}" onClick="{{toggle}}" style="' + AV + '">AO' + DOT + '</button>' + menu + '</div>')
switch = ('<sc-if value="{{vSwitch}}" hint-placeholder-val="{{false}}"><div class="rs"><header class="rs-top"><span class="lg-word" role="img" aria-label="Credalio"></span></header>'
          '<main class="rs-m"><div class="rs-emb" aria-hidden="true"><span>' + svg('<path d="M12 3v18M5 21h14M6 7h12"></path><path d="m6 7-3 7a3 3 0 0 0 6 0zM18 7l-3 7a3 3 0 0 0 6 0z"></path>', 28, 1.9) + '</span></div>'
          '<span class="rs-pill">Switching role</span><h1 class="rs-h">Opening your Validator workspace</h1>'
          '<p class="rs-sub">2 reviews are waiting for you.' + tip('You’re never assigned to review learning experiences you created or contributed to.', 'l') + '</p>'
          '<a href="CR-DASH-NEW.dc.html" class="rs-back">' + svg('<path d="M19 12H5"></path><path d="m11 6-6 6 6 6"></path>', 16, 2.2) + 'Back to Creator</a></main></div></sc-if>')
pm_js = r'''class Component extends DCLogic {
  constructor(props) { super(props); const v = (props && props.variant) || 'menu'; this.state = { v, nav: false, open: v !== 'switch', st: 0 }; }
  renderVals() {
    const S = this.state, out = {};
    [0, 1, 2].forEach((i) => { const on = S.st === i; out['st' + i] = { on: on ? 'true' : 'false', cls: on ? 'on' : '', pick: () => this.setState({ st: i }) }; });
    return Object.assign(out, { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }),
      ideas: ['Data Analysis for beginners', 'Data & Analytics skills managers use', 'SQL basics'].map((label) => ({ label, pick: () => this.setState({ idea: label }) })), idea: this.state.idea || '', onIdea: (e) => this.setState({ idea: e.target.value }), askShown: false, askOpen: 'false', toggleAsk: () => {},
      open: S.open, openA: S.open ? 'true' : 'false', avCls: S.open ? 'on' : '', toggle: () => this.setState({ open: !S.open }),
      dotCls: ['', 'aw', 'dn'][S.st], multi: S.v !== 'one', vDash: S.v !== 'switch', vSwitch: S.v === 'switch' });
  }
}
'''
pm = shell(base, pm_avatar, pm_css + '\n.pm-dot.aw{background:#D98A00}.pm-dot.dn{background:#8A93AD}', '', 'CR-PM · Account menu · shared source', pm_js)
assert pm.count('<div class="ds-root">') == 1 and pm.count('\n</x-dc>') == 1
pm = pm.replace('<div class="ds-root">', '<sc-if value="{{vDash}}" hint-placeholder-val="{{true}}"><div class="ds-root">', 1)
pm = pm.replace('\n</x-dc>', '</sc-if>' + switch + '\n</x-dc>', 1)
open(os.path.join(D, 'CR-PM.dc.html'), 'w').write(pm)

# ================= CR-MSG =================
msg_css = '''.mg{position:fixed;right:24px;bottom:24px;z-index:40;width:384px;display:flex;flex-direction:column;gap:10px}
.mg-c{box-sizing:border-box;padding:14px 14px 12px 14px;border-radius:18px;background:#FFFFFF;border:1.5px solid #E6EAF3;box-shadow:0 18px 44px rgba(11,20,51,.14);text-align:left;color:#0B1433;font-size:14px}
.mg-h{display:flex;align-items:flex-start;gap:12px}
.mg-a{width:38px;height:38px;flex-shrink:0;border-radius:50%;background:#EAF0FF;color:#0E3BB8;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:600}
.mg-t{flex:1;min-width:0;display:flex;flex-direction:column;gap:2px}
.mg-n{display:flex;align-items:center;gap:8px;font-size:14.5px;font-weight:600}.mg-n em{font-style:normal;font-size:12px;font-weight:400;color:#8A93AD;margin-left:auto}
.mg-x{font-size:12.5px;color:#8A93AD;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.mg-ib{width:28px;height:28px;flex-shrink:0;border-radius:50%;border:0;background:transparent;color:#8A93AD;display:flex;align-items:center;justify-content:center;cursor:pointer;text-decoration:none}
.mg-ib:hover{background:#F1F3F8;color:#0B1433}
.mg-p{margin:10px 0 0 50px;font-size:14px;line-height:1.5;color:#3A4566;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.mg-hid{margin:10px 0 0 50px;display:flex;align-items:center;gap:7px;font-size:13.5px;color:#8A93AD}
.mg-f{margin:10px 0 0 50px;display:flex;align-items:center;gap:6px}
.mg-b{height:34px;padding:0 14px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:inherit;font-size:13.5px;font-weight:600;color:#0B1433;display:inline-flex;align-items:center;cursor:pointer;text-decoration:none}
.mg-b:hover{border-color:#1652F0;color:#1652F0}
.mg-o{height:34px;padding:0 10px;display:inline-flex;align-items:center;font-size:13.5px;font-weight:600;color:#1652F0;text-decoration:none}
.mg-in{margin:10px 0 0 50px;display:flex;align-items:center;gap:6px;height:44px;padding:0 5px 0 14px;border-radius:999px;border:1.5px solid #1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.mg-in input{flex:1;min-width:0;border:0;outline:none;background:none;font-family:inherit;font-size:14px;color:#0B1433}
.mg-go{width:34px;height:34px;flex-shrink:0;border-radius:50%;border:0;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center;cursor:pointer}
.mg-ok{margin:10px 0 0 50px;display:flex;align-items:center;gap:8px;font-size:13.5px;color:#0F6B45}
.mg-ok i{width:20px;height:20px;border-radius:50%;background:#E7F5EE;display:flex;align-items:center;justify-content:center}
.mg-more{box-sizing:border-box;height:44px;padding:0 16px;border-radius:999px;background:#0B1433;color:#FFFFFF;display:flex;align-items:center;justify-content:space-between;font-size:14px;font-weight:500;text-decoration:none;box-shadow:0 14px 34px rgba(11,20,51,.2)}
.mg-more b{font-weight:600}
@keyframes mgIn{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
.mg-c{animation:mgIn .4s ease both}.mg-c:nth-child(2){animation-delay:.08s}.mg-c:nth-child(3){animation-delay:.16s}
@media (prefers-reduced-motion: reduce){.mg-c{animation:none}}
@media (max-width: 960px){
.mg{left:8px;right:8px;top:70px;bottom:auto;width:auto}
.mg-p,.mg-hid,.mg-f,.mg-in,.mg-ok{margin-left:0}
}'''
card = ('<sc-for list="{{cards}}" as="m" hint-placeholder-count="3"><section class="mg-c" role="status" aria-label="{{m.aria}}"><div class="mg-h"><span class="mg-a" aria-hidden="true">{{m.ini}}</span>'
        '<span class="mg-t"><span class="mg-n">{{m.name}}<em>{{m.time}}</em></span><span class="mg-x">{{m.ctx}}</span></span>'
        '<sc-if value="{{m.gear}}" hint-placeholder-val="{{false}}"><a href="CR-MSG-006.dc.html" class="mg-ib" aria-label="Pop-up settings">' + I_GEAR + '</a></sc-if>'
        '<button type="button" class="mg-ib" aria-label="Dismiss">' + I_X + '</button></div>'
        '<sc-if value="{{m.text}}" hint-placeholder-val="{{true}}"><p class="mg-p">{{m.body}}</p></sc-if>'
        '<sc-if value="{{m.hidden}}" hint-placeholder-val="{{false}}"><span class="mg-hid">' + I_LOCK + 'Preview hidden</span></sc-if>'
        '<sc-if value="{{m.typing}}" hint-placeholder-val="{{false}}"><label class="mg-in"><span class="sr-only">Reply to {{m.name}}</span><input value="{{m.draft}}" placeholder="Write a reply…"><button type="button" class="mg-go" aria-label="Send">' + I_SEND + '</button></label></sc-if>'
        '<sc-if value="{{m.sent}}" hint-placeholder-val="{{false}}"><span class="mg-ok"><i>' + I_OK + '</i>Sent. Added to the conversation.</span></sc-if>'
        '<sc-if value="{{m.acts}}" hint-placeholder-val="{{true}}"><div class="mg-f"><sc-if value="{{m.canReply}}" hint-placeholder-val="{{true}}"><a href="CR-MSG-002.dc.html" class="mg-b">Reply</a></sc-if><a href="{{m.href}}" class="mg-o">{{m.open}}</a></div></sc-if>'
        '</section></sc-for>')
stack = ('<div class="mg" aria-live="polite">' + card +
         '<sc-if value="{{more}}" hint-placeholder-val="{{false}}"><a href="CR-NOT-001.dc.html" class="mg-more"><span><b>+3 more</b> messages</span><span>View all</span></a></sc-if></div>')
msg_js = r'''class Component extends DCLogic {
  constructor(props) { super(props); this.v = (props && props.variant) || 'pops'; this.state = { nav: false }; }
  renderVals() {
    const v = this.v;
    const M = [
      { ini: 'MO', name: 'Mary O.', ctx: 'Learner support · Data Analysis with SQL', time: 'now', body: 'I tried your hint but my GROUP BY still repeats rows. Is it the city column?', open: 'Open conversation', href: 'CR-SUP-002.dc.html', canReply: true },
      { ini: 'JA', name: 'John Adeyemi', ctx: 'Team chat · Financial Modelling Basics', time: '1 min', body: 'I’ve uploaded the Chapter 3 case study. Can you check the numbers before Friday?', open: 'Open Team chat', href: '#', canReply: true },
      { ini: 'AB', name: 'Dr. Amina Bello', ctx: 'Validation · VAL-00928', time: '3 min', body: 'Please share the dataset used in Lesson 4.3 so I can check the window-function results.', open: 'Open request', href: 'CR-VAL-MC-002.dc.html', canReply: false }
    ];
    const cards = (v === 'reply' || v === 'sent' ? M.slice(0, 1) : M).map((m, i) => Object.assign({}, m, {
      aria: 'New message from ' + m.name, gear: i === 0 && v !== 'reply' && v !== 'sent',
      text: v !== 'hidden' && v !== 'sent', hidden: v === 'hidden',
      typing: v === 'reply', draft: 'Group by customer_id only, then join city after. Try it on the Lesson 4.2 data.',
      sent: v === 'sent', acts: v !== 'reply', canReply: m.canReply && v !== 'sent' && v !== 'hidden',
      open: v === 'sent' ? 'Open conversation' : m.open }));
    return { navCls: this.state.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !this.state.nav }),
      ideas: ['Data Analysis for beginners', 'Data & Analytics skills managers use', 'SQL basics'].map((label) => ({ label, pick: () => this.setState({ idea: label }) })), idea: this.state.idea || '', onIdea: (e) => this.setState({ idea: e.target.value }), askShown: false, askOpen: 'false', toggleAsk: () => {},
      cards, more: v === 'many' };
  }
}
'''
msg_av = '<a href="CR-PM-001.dc.html" aria-label="Account menu" style="' + AV + '">AO<span style="position: absolute; right: 0; bottom: 1px; width: 11px; height: 11px; border-radius: 50%; background: #0F6B45; border: 2px solid #F7F9FD"></span></a>'
msg = shell(base, msg_av, msg_css, stack, 'CR-MSG · Message pop-ups · shared source', msg_js)
open(os.path.join(D, 'CR-MSG.dc.html'), 'w').write(msg)
print('ok')
