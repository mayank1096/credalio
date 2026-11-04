# Learner pages inside the Dashboard shell (TV-001, TV-002, TUT-001). Built from LIVE shared pieces:
#   Link 2 CR-SET  -> settings layout (se, se-nav, se-p, se-ph), rows (ss-l / ss-r / ss-ic / hp-rb), sign-in icons, dialog (dl-*)
#   Link 2 CR-SUP  -> support conversation (sc-g, sc-chat, sc-hd, sc-sum, sc-msg, sc-cmp, sc-side)
#   Dashboard      -> lr-head, Backpack proof tiles (lr-pf), Nova avatar; kit -> ko-* emblem + confetti, ds-tag, tip
import os, re, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from kit import tip, btn, ck, emblem
import wow

C2 = os.path.join(HERE, '../../canvas2/project/')
SET = open(C2 + 'CR-SET.dc.html').read()
SUP = open(C2 + 'CR-SUP.dc.html').read()
def _style(s): return re.search(r'<style>(.*?)</style>', s, re.S).group(1)

def pick(css, rx):
    out, i, n = [], 0, len(css)
    def rules(body):
        res, j = [], 0
        while j < len(body):
            o = body.find('{', j)
            if o < 0: break
            c = body.find('}', o)
            sel = body[j:o].strip()
            if re.search(rx, sel) and ':has(' not in sel: res.append(sel + '{' + body[o + 1:c] + '}')
            j = c + 1
        return res
    while i < n:
        o = css.find('{', i)
        if o < 0: break
        head = css[i:o].strip()
        if head.startswith('@'):
            d, k = 1, o + 1
            while d:
                if css[k] == '{': d += 1
                elif css[k] == '}': d -= 1
                k += 1
            if head.startswith('@media'):
                r = rules(css[o + 1:k - 1])
                if r: out.append(head + '{\n' + '\n'.join(r) + '\n}')
            i = k
        else:
            c = css.find('}', o)
            if re.search(rx, head) and ':has(' not in head: out.append(head + '{' + css[o + 1:c] + '}')
            i = c + 1
    return '\n'.join(out)

SETCSS = pick(_style(SET), r'^\.(se|se-(lc|nav|n|p|ph)|ss-(l|r|ic|t)|sg-(ic|l|lg|sm)|hp-rb|hp-lab|pg-back|st|so-t|dl|dl-(ov|x|ft|n))\b|^\.(se-n|ss-r|ss-t|so-t|st|dl|dl-x|se-ph|hp-rb|sg-l|se-lc|se) |^\.(se-n|st)\.|^\.dl h2|^\.dl > p|^\.se > \.se-p')
SUPCSS = pick(_style(SUP), r'^\.(sc-(g|chat|hd|body|sum|sl|day|msg|tm|cmp|send|side)|av)\b|^\.sc-')
_sg = SET[SET.find('<ul class="ss-l sg-l">'):]
ICO = [m.group(1) for m in re.finditer(r'<span class="ss-ic sg-ic">(<svg.*?</svg>)</span>', _sg[:6000], re.S)][:3]
ARRB = re.search(r'<button type="button" class="sc-send"[^>]*>(<svg.*?</svg>)</button>', SUP, re.S)
SENDI = ARRB.group(1) if ARRB else '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'
BACK = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5"></path><path d="m11 18-6-6 6-6"></path></svg>'
CLOSE = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"></path></svg>'

def ic(d, s=20, sw=1.8):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (s, s, sw, d)
I_TV = '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"></path><circle cx="12" cy="11" r="2.2"></circle><path d="M12 13.2V16"></path>'
I_WAL = '<rect x="3" y="6" width="18" height="13" rx="3"></rect><path d="M3 10h18M16 14.5h2"></path>'
I_LINK = '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"></path><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"></path>'
I_UNI = '<path d="M3 9l9-5 9 5-9 5z"></path><path d="M7 11.5V16c0 1.5 2.2 3 5 3s5-1.5 5-3v-4.5"></path>'
CK = ck(12, 3.2)

def pages(I, av):
    """I = dashgen icon map, av = dashgen coach avatar helper."""
    pf = lambda k: ic(I[k], 22)
    PROOF = [('cred', 'Certificate', 'Data Foundations: Spreadsheets to SQL', 'Issued 25 Sep 2026', True), ('proj', 'Verified project', 'Retail sales analysis', 'Issued 25 Sep 2026', False), ('skill', 'Competency badge', 'SQL Practitioner', 'Issued 25 Sep 2026', False)]
    tiles = ''.join('<div class="lr-pf"><span class="lr-pf-top"><span class="lr-pf-i">%s</span>%s<span class="lr-pf-ok" title="Verified" aria-label="Verified">%s</span></span><b>%s</b><small>%s · %s</small></div>' % (pf(k), '<span class="ds-tag blue bk-new">New</span>' if new else '', ck(11, 3.4), t, kind, d) for k, kind, t, d, new in PROOF)
    BACKPACK = '''<sc-if value="{{pBack}}" hint-placeholder-val="{{ false }}">
<div class="lr-head"><div><h1 class="lr-h1">Digital Backpack</h1></div></div>
<sc-if value="{{tvBand}}" hint-placeholder-val="{{ true }}">
<section class="ds-card bk-tv" aria-labelledby="bk-tvh"><span class="bk-tvi">''' + ic(I_TV, 22) + '''</span><div class="bk-tvt"><b id="bk-tvh">Secure your Backpack with TruVault''' + tip('TruVault manages eligible verifiable credentials, your ecosystem identity and supported digital assets. It’s optional: your credentials are already safe here.') + '''</b><span>Optional. Your credentials are already safe here.</span></div>
<div class="bk-tva"><button type="button" class="ds-link" onClick="{{tvLater}}">Later</button>''' + btn('{{tvCta}}', '#', 'sm bk-go {{tvBusyCls}}', 'onClick="{{tvConnect}}"', 'button') + '''</div></section>
</sc-if>
<sc-if value="{{tvDone}}" hint-placeholder-val="{{ false }}"><div class="bk-ok" role="status"><i>''' + CK + '''</i><span>TruVault connected. Your eligible credentials are secured.</span><a class="ds-link" href="Dash-TV-Set.dc.html">Manage</a></div></sc-if>
<div class="lr-pfs bk-pfs"><div class="lr-pf lr-pf-sum"><span class="lr-pf-n">3</span><b>verified achievements</b><small>From Data Foundations<br>and its project</small></div>''' + tiles + '''</div>
<sc-if value="{{tvModal}}" hint-placeholder-val="{{ false }}">
<div class="dl-ov" onClick="{{tvLater}}"></div>
<div class="dl bk-dl ko-v" role="dialog" aria-modal="true" aria-labelledby="bk-dh"><button type="button" class="dl-x" onClick="{{tvLater}}" aria-label="Close">''' + CLOSE + '''</button>
<sc-if value="{{tvBusy}}" hint-placeholder-val="{{ false }}">''' + wow.VAULT.replace('CREDI', pf('cred')).replace('CKI', ck(14, 3.2)) + '''<h2 id="bk-dh" class="vt-h">Securing your credential…</h2><p>Connecting TruVault to your Backpack.</p></sc-if>
<sc-if value="{{tvIdle}}" hint-placeholder-val="{{ true }}">''' + emblem() + '''
<span class="ko-pill">New credential</span>
<h2 id="bk-dh">You’ve earned your first verified credential.</h2>
<p>It’s already safe in your Backpack. TruVault lets you manage it across the ecosystem. It’s optional.</p>
<div class="bk-cred"><span class="lr-pf-i">''' + pf('cred') + '''</span><span class="so-t"><b>Data Foundations: Spreadsheets to SQL</b><span>Certificate · Issued 25 Sep 2026</span></span><span class="lr-pf-ok" aria-label="Verified">''' + ck(11, 3.4) + '''</span></div>
<div class="dl-ft bk-ft"><button type="button" class="ds-ghost" onClick="{{tvLater}}">I’ll do this later</button>''' + btn('{{tvCta}}', '#', 'bk-go {{tvBusyCls}}', 'onClick="{{tvConnect}}"', 'button') + '''</div>
</sc-if>
</div>
</sc-if>
</sc-if>'''

    SNAV = [('Profile', I['learn'], False), ('Account & sign-in', I['lock'], False), ('Roles', I['comm'], False), ('AI Coach', I['skill'], False), ('Notifications', I['bell'], False), ('TruVault & connections', I_LINK, True), ('Privacy', I['settings'], False)]
    def row(key, icon, name, sub):
        return ('<li class="ss-r"><span class="ss-ic sg-ic">%s</span><span class="ss-t"><b>%s</b><span>%s</span></span>'
                '<sc-if value="{{cn.%s.tag}}" hint-placeholder-val="{{ false }}"><span class="ds-tag green tv-st">Connected</span></sc-if>'
                '<sc-if value="{{cn.%s.btn}}" hint-placeholder-val="{{ true }}"><button type="button" class="hp-rb {{cn.%s.cls}}" onClick="{{cn.%s.flip}}" aria-label="{{cn.%s.aria}}">{{cn.%s.label}}</button></sc-if>'
                '<sc-if value="{{cn.%s.lock}}" hint-placeholder-val="{{ false }}"><span class="tv-lk">{{cn.%s.label}}</span></sc-if></li>') % (icon, name, sub, key, key, key, key, key, key, key, key)
    SETTINGS = '''<sc-if value="{{pSet}}" hint-placeholder-val="{{ false }}">
<div class="se"><div class="se-lc"><div class="lr-head"><div><h1 class="lr-h1">Settings</h1></div></div>
<nav class="se-nav" aria-label="Settings">''' + ''.join('<a href="#" class="se-n%s"%s>%s<span>%s</span></a>' % (' on' if on else '', ' aria-current="page"' if on else '', ic(d, 18), t.replace('&', '&amp;')) for t, d, on in SNAV) + '''</nav></div>
<section class="ds-card se-p" aria-labelledby="tv-h">
<div class="se-ph"><div><h2 id="tv-h" class="tv-h">TruVault &amp; connections''' + tip('Connections add capabilities to your one Credalio account. They aren’t separate identities.', 'r') + '''</h2></div></div>
<span class="hp-lab tv-lab">Your roles</span>
<div class="tv-roles"><span class="ds-tag blue lg">Learner</span><a class="ds-chip sm" href="Creators.dc.html">+ Add Creator</a><a class="ds-chip sm" href="#">+ Apply as Validator</a></div>
<span class="hp-lab tv-lab">Sign-in''' + tip('Signing in always works with email, Google or Apple. Wallets never replace your sign-in.', 'r') + '''</span>
<ul class="ss-l sg-l">''' + row('email', ICO[0], 'Email and password', 'ada.ononuju@example.com') + row('google', ICO[1], 'Google', 'ada.ononuju@gmail.com') + row('apple', ICO[2], 'Apple', 'Not connected') + '''</ul>
<span class="hp-lab tv-lab">Wallets &amp; identity</span>
<ul class="ss-l sg-l">''' + row('truvault', '<span class="tv-ic">' + ic(I_TV, 20) + '</span>', 'TruVault', 'Credentials, ecosystem identity and digital assets') + row('metamask', ic(I_WAL, 20), 'MetaMask', 'External wallet') + row('wc', ic(I_LINK, 20), 'WalletConnect', 'Supported wallet providers') + row('sso', ic(I_UNI, 20), 'Institution SSO', 'Added when an institution invites you') + '''</ul>
</section></div>
</sc-if>'''

    TUTOR = '''<sc-if value="{{pTut}}" hint-placeholder-val="{{ false }}">
<a href="#" class="pg-back">''' + BACK + '''Lesson 4 · Joining tables with SQL</a>
<div class="sc-g">
<section class="ds-card sc-chat tu-chat" aria-label="Conversation with your tutor">
<header class="sc-hd"><span class="av tu-av">TA</span><span><b>Tobi Adeyemi</b><span>SQL tutor · Data Foundations · Active now</span></span><a href="#" class="hp-rb"><span class="sg-lg">Book a live session</span><span class="sg-sm">Book</span></a></header>
<div class="sc-body">
<div class="sc-sum">''' + wow.baton(av('')) + '''<span class="sc-sl">''' + av('tu-nv') + '''<span>Handed over by {{coachName}}</span>''' + tip('You chose to share this. Your tutor sees the summary, the lesson and what you’ve tried, not the rest of your account.', 'r') + '''</span>
<p>You asked why the LEFT JOIN leaves some customers with an empty total. {{coachName}} tried two explanations and a worked example, and you were still unsure.</p>
<button type="button" class="ds-link tu-tg" aria-expanded="{{tOpen}}" onClick="{{toggleT}}">{{tLabel}}</button>
<sc-if value="{{showT}}" hint-placeholder-val="{{ false }}"><ol class="tu-tr"><sc-for list="{{tr}}" as="t" hint-placeholder-count="4"><li><b class="{{t.cls}}">{{t.who}}</b><span>{{t.text}}</span></li></sc-for></ol></sc-if>
</div>
<span class="sc-day">Today</span>
<sc-for list="{{msgs}}" as="m" hint-placeholder-count="2"><div class="sc-msg {{m.cls}}"><sc-if value="{{m.tutor}}" hint-placeholder-val="{{ true }}"><span class="av tu-av">TA</span></sc-if><div><p>{{m.text}}</p></div></div></sc-for>
<sc-if value="{{typing}}" hint-placeholder-val="{{ false }}"><div class="sc-msg"><span class="av tu-av">TA</span><div class="tu-typ" role="status"><i></i><i></i><i></i><span class="sr-only">Tobi is typing</span></div></div></sc-if>
</div>
<form class="sc-cmp" onSubmit="{{send}}"><label for="tu-in" class="sr-only">Message your tutor</label><input id="tu-in" class="tu-in" placeholder="Message Tobi…" value="{{tdraft}}" onInput="{{onTDraft}}" autocomplete="off"><button type="submit" class="sc-send" aria-label="Send">''' + SENDI + '''</button></form>
</section>
<aside class="ds-card sc-side tu-side" aria-label="Shared with your tutor">
<span class="hp-lab">You’re viewing</span><b>Lesson 4 · Joining tables with SQL</b><span>Data Foundations · Module 4 of 6</span>
<pre class="tu-code"><b>SELECT</b> c.name, o.total
<b>FROM</b> customers c
<b>LEFT JOIN</b> orders o
  <b>ON</b> o.customer_id = c.id;</pre>
<span class="hp-lab tu-lab">Shared with Tobi</span>
<ul class="tu-sh">''' + ''.join('<li><i>%s</i><span>%s</span></li>' % (ck(10, 3.4), t) for t in ['Your question', 'Your conversation with {{coachName}}', 'This lesson', 'What you’ve tried']) + '''</ul>
<a href="#" class="ds-link">Back to lesson</a>
</aside>
</div>
</sc-if>'''
    return BACKPACK + '\n' + SETTINGS + '\n' + TUTOR

CSS = SETCSS + '\n' + SUPCSS + r'''
.lr-pf-top .bk-new{margin-left:auto;margin-right:8px;align-self:center}
.bk-tv{display:flex;align-items:center;gap:16px;padding:18px 20px;border-radius:20px;margin-bottom:20px}
.bk-tvi,.tv-ic{width:44px;height:44px;flex-shrink:0;border-radius:14px;background:#0B1433;color:#9DB8F7;display:flex;align-items:center;justify-content:center}
.tv-ic{width:42px;height:42px;border-radius:12px;margin:-1.5px}
.bk-tvt{flex:1;display:flex;flex-direction:column;gap:2px;min-width:0}
.bk-tvt b{display:flex;align-items:center;font-size:15.5px;font-weight:600}
.bk-tvt > span{font-size:13.5px;color:#5B6582}
.bk-tva{display:flex;align-items:center;gap:18px;flex-shrink:0}
.bk-go.busy{background:#C9D3EC;box-shadow:none;pointer-events:none}
.bk-ok{display:flex;align-items:center;gap:10px;margin-bottom:20px;padding:12px 16px;border-radius:16px;background:#E7F5EE;color:#0F6B45;font-size:14.5px;font-weight:500}
.bk-ok i{width:22px;height:22px;border-radius:999px;background:#0F6B45;color:#FFFFFF;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.bk-ok span{flex:1}
.bk-pfs{grid-template-columns:repeat(4,minmax(0,1fr))}
.bk-dl{display:flex;flex-direction:column;align-items:center;text-align:center;padding:36px 32px 28px}
.bk-dl h2{margin-top:14px;padding:0}
.bk-dl > p{max-width:420px}
.bk-cred{display:flex;align-items:center;gap:14px;width:100%;box-sizing:border-box;margin-top:22px;padding:14px 16px;border-radius:16px;border:1.5px solid #E6EAF3;text-align:left}
.bk-cred .lr-pf-i{width:42px;height:42px;flex-shrink:0}
.bk-ft{width:100%;justify-content:center}
.vt-h{margin-top:6px !important}
.tv-h{display:flex;align-items:center}
.tv-lab{display:flex;align-items:center;margin-top:26px}
.tv-roles{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin-top:12px}
.tv-roles .ds-chip{text-decoration:none}
.tv-st{margin-right:2px}
.tv-lk{font-size:13px;font-weight:500;color:#8A93AD;white-space:nowrap;padding:0 4px}
.dl-x{border:0;background:none;cursor:pointer}
.tu-av{background:#0B1433;color:#FFFFFF}
.tu-chat{height:auto;min-height:600px}
.tu-nv{width:22px !important;height:22px !important}
.sc-sum .sc-sl{gap:8px}
.tu-tg{margin-top:10px;font-size:13.5px}
.tu-tr{list-style:none;margin:12px 0 0;padding:12px 0 0;border-top:1.5px solid #E2E9FB;display:flex;flex-direction:column;gap:8px}
.tu-tr li{display:grid;grid-template-columns:72px minmax(0,1fr);gap:10px;font-size:13.5px;line-height:1.45;color:#3A4566}
.tu-tr b{font-weight:600;color:#1652F0}
.tu-tr b.nv{color:#5B6582}
.sc-msg.me{align-self:flex-end}
.sc-msg.me > div{border-radius:18px 4px 18px 18px;background:#EAF0FF}
.tu-typ{display:flex;align-items:center;gap:5px;padding:16px 18px !important}
.tu-typ i{width:7px;height:7px;border-radius:50%;background:#8A93AD;animation:tuDot 1.2s ease-in-out infinite}
.tu-typ i:nth-child(2){animation-delay:.15s}.tu-typ i:nth-child(3){animation-delay:.3s}
@keyframes tuDot{0%,60%,100%{opacity:.35;transform:translateY(0)}30%{opacity:1;transform:translateY(-3px)}}
.tu-in{flex:1;min-width:0;border:0;outline:none;background:none;font-family:inherit;font-size:15px;color:#0B1433}
.tu-in::placeholder{color:#8A93AD}
.sc-cmp:focus-within{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.1)}
.tu-side{gap:6px}
.tu-code{margin:14px 0 0;padding:12px 14px;border-radius:12px;background:#0B1433;color:#DCE4FF;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12.5px;line-height:1.6;white-space:pre-wrap}
.tu-code b{color:#9DB8F7;font-weight:600}
.tu-lab{margin-top:20px}
.tu-sh{list-style:none;margin:8px 0 0;padding:0;display:flex;flex-direction:column;gap:9px}
.tu-sh li{display:flex;align-items:center;gap:9px;font-size:13.5px;color:#3A4566}
.tu-sh i{width:18px;height:18px;border-radius:999px;background:#E7F5EE;color:#0F6B45;display:flex;align-items:center;justify-content:center;flex-shrink:0}
@media (prefers-reduced-motion: reduce){.tu-typ i{animation:none}}
@media (max-width: 1080px){
.bk-pfs{grid-template-columns:repeat(2,minmax(0,1fr))}
}
@media (max-width: 760px){
.bk-tv{flex-wrap:wrap;padding:16px}
.bk-tva{width:100%;flex-direction:row-reverse;justify-content:space-between}
.bk-tva .ds-btn{flex:1;justify-content:space-between}
.bk-ok{align-items:flex-start;font-size:14px}
.bk-dl{padding:28px 18px 20px}
.bk-ft .ds-btn{justify-content:space-between}
.tv-roles{gap:6px}
.sg-l .tv-st{display:none}
.tu-tr li{grid-template-columns:minmax(0,1fr);gap:2px}
.sc-hd .hp-rb{white-space:nowrap}
.sc-hd > span:nth-child(2) > span{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sc-hd > span:nth-child(2){min-width:0}
.tu-chat{min-height:0}
}
'''

JS_STATE = "tv: p.tv || 'new', tvBusy: false, cn: { email: true, google: true, apple: false, truvault: p.tv === 'connected', metamask: false, wc: false }, showT: false, tdraft: '', typing: false, replies: 0, msgs: [{ f: 't', x: 'Hi Ada, I’m Tobi. I’ve read your conversation with your AI Coach, so no need to repeat anything. Let’s try another angle: if you had a customer list and a separate order list, what would you write for someone who hasn’t ordered yet?' }]"

TR = [['You', 'I don’t understand why we use a LEFT JOIN here.'], ['Coach', 'LEFT JOIN keeps every customer; INNER JOIN drops the ones with no orders.'], ['You', 'Show me visually.'], ['Coach', 'Shared a results table with a customer whose total is NULL.'], ['You', 'Give me an example.'], ['Coach', 'Worked example: a shop’s full customer list, including people who haven’t bought yet.'], ['You', 'I’m still confused.'], ['Coach', 'Suggested a tutor and prepared this handover.']]
CANNED = ['Exactly: you’d still write their name and leave the amount blank. That blank is the NULL you saw. A LEFT JOIN does the same: keep everyone from the first list, fill in what matches.', 'Try it: open the practice editor, swap LEFT JOIN for INNER JOIN and compare the row counts. I’ll stay here.', 'Great. Tell me what you find, or book a live session if you’d like to walk through it together.']

JS_VALS = r'''
      pBack: S.page === 'backpack', pSet: S.page === 'settings', pTut: S.page === 'tutor',
      navPack: S.page === 'backpack' ? 'ds-on' : '', navPackCur: S.page === 'backpack' ? 'page' : 'false',
      navSet: S.page === 'settings' ? 'ds-on' : '', navSetCur: S.page === 'settings' ? 'page' : 'false',
      navLearn: S.page === 'tutor' ? 'ds-on' : '', navLearnCur: S.page === 'tutor' ? 'page' : 'false',
      tvModal: S.tv === 'new' || S.tvBusy, tvBusy: S.tvBusy, tvIdle: !S.tvBusy, tvBand: S.tv === 'new' || S.tv === 'later', tvDone: S.tv === 'connected',
      tvCta: S.tvBusy ? 'Opening TruVault…' : (S.tv === 'new' ? 'Set up TruVault' : 'Connect TruVault'), tvBusyCls: S.tvBusy ? 'busy' : '',
      tvLater: function () { if (!S.tvBusy) self.setState({ tv: 'later' }); },
      tvConnect: function () { if (S.tvBusy) return; self.setState({ tvBusy: true }); clearTimeout(self._tvT); self._tvT = setTimeout(function () { var c = Object.assign({}, self.state.cn); c.truvault = true; self.setState({ tvBusy: false, tv: 'connected', cn: c }); }, 2600); },
      cn: (function () { var o = {}; [['email', 1], ['google', 0], ['apple', 0], ['truvault', 0], ['metamask', 0], ['wc', 0], ['sso', 2]].forEach(function (r) { var k = r[0], on = !!S.cn[k], lock = r[1] > 0;
        o[k] = { tag: on && k !== 'email', btn: !lock, lock: lock, label: k === 'email' ? 'Primary' : (k === 'sso' ? 'Via invite' : (on ? 'Disconnect' : 'Connect')), cls: '', aria: (on ? 'Disconnect ' : 'Connect ') + k,
          flip: function () { if (lock) return; var c = Object.assign({}, self.state.cn); c[k] = !on; self.setState({ cn: c }); } }; }); return o; })(),
      coachName: CN, showT: S.showT, tOpen: S.showT ? 'true' : 'false', tLabel: S.showT ? 'Hide your ' + CN + ' conversation' : 'View your ' + CN + ' conversation',
      toggleT: function () { self.setState({ showT: !S.showT }); },
      tr: TR.map(function (t) { return { who: t[0] === 'Coach' ? CN : t[0], text: t[1], cls: t[0] === 'Coach' ? 'nv' : '' }; }),
      msgs: S.msgs.map(function (m) { return { tutor: m.f === 't', cls: m.f === 't' ? '' : 'me', text: m.x }; }),
      typing: S.typing, tdraft: S.tdraft, onTDraft: function (e) { self.setState({ tdraft: e.target.value }); },
      send: function (e) { if (e && e.preventDefault) e.preventDefault(); var t = (self.state.tdraft || '').trim(); if (!t || self.state.typing) return;
        self.setState({ tdraft: '', typing: true, msgs: self.state.msgs.concat([{ f: 'm', x: t }]) }); clearTimeout(self._tuT);
        self._tuT = setTimeout(function () { var n = self.state.replies; self.setState({ typing: false, replies: n + 1, msgs: self.state.msgs.concat([{ f: 't', x: CANNED[Math.min(n, CANNED.length - 1)] }]) }); }, 1400); },'''
JS_VALS = JS_VALS.replace('CN', "(S.coach || 'Nova')")
JS_DATA = 'var TR = ' + json.dumps(TR, ensure_ascii=False) + ';\nvar CANNED = ' + json.dumps(CANNED, ensure_ascii=False) + ';\n'
