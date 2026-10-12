# build32: CR-SET (Settings · one source, variants account / delete / security / orgs = SET-001 / SET-002d / SET-003 / ORG-SOON)
# + patches LIVE CR-PUB in place with variant "public" (= PROF-002: public header instead of the Studio shell).
# usage: python3 build32.py <dir>   (run in a scratch copy; build17 re-runs on import — copy back only the files listed at the end)
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build17 as B
from tipx import tip, TIP_CSS
P, rd, wr, ic, I, ARR = B.P, B.rd, B.wr, B.ic, B.I, B.ARR
SHIELD = '<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"></path>'
LAPTOP = '<rect x="4" y="5" width="16" height="11" rx="2"></rect><path d="M2 19h20"></path>'
PHONE = '<rect x="7" y="3" width="10" height="18" rx="2.5"></rect><path d="M11 18h2"></path>'
X = ic('<path d="M7 7l10 10M17 7 7 17"></path>', 18, 2.2)
OUT = []

wd, wm = rd('CR-DASH-S03.dc.html'), rd('CR-CRED-002c-Mobile.dc.html')
def mob(t, h):
    t = re.sub(r'hint-size="[^"]*"', f'hint-size="390px,{h}px"', t)
    t = re.sub(r'width: \d+px; height: \d+px;', f'width: 390px; height: {h}px;', t, count=1)
    return re.sub(r'"\$preview":\{"width":\d+,"height":\d+\}', f'"$preview":{{"width":390,"height":{h}}}', t)
def wrap(src, items):
    for n, var, hm in items:
        imp = f'<dc-import name="{src}"' + (f' variant="{var}"' if var else '')
        if n != src:
            t = wd.replace('<dc-import name="CR-DASH-ST" variant="s03"', imp)
            wr(n + '.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} preview</title>', t)); OUT.append(n + '.dc.html')
        t = mob(wm.replace('<dc-import name="CR-CRED-002" variant="badge"', imp), hm)
        wr(n + '-Mobile.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} mobile preview</title>', t)); OUT.append(n + '-Mobile.dc.html')
def props_patch(name):
    s = rd(name + '.dc.html').replace('constructor(props) { super(props);', 'constructor(props) { super(props); this.props0 = props;', 1)
    s = s.replace('    const S = this.state;\n', '    const S = this.state, props = this.props0 || {};\n', 1)
    wr(name + '.dc.html', s)

# ======================= CR-SET · Settings =======================
NAV = [('user', 'Profile', ''), ('lock', 'Account & sign-in', 'acc'), ('sec', 'Security', 'sec'), ('bell', 'Notifications', ''), ('eye', 'Privacy', ''),
       ('globe', 'Language & region', ''), ('ai', 'AI preferences', ''), ('org', 'My organizations', 'org')]
def nav():
    out = ''
    for i, t, k in NAV:
        p = SHIELD if i == 'sec' else I[i]
        cls = f' {{{{nv.{k}}}}}' if k else ''
        href = 'CR-HOME-SET.dc.html' if t == 'AI preferences' else '#'
        out += f'<a href="{href}" class="se-n{cls}">{ic(p, 18)}<span>{t}</span></a>'
    return out
def row(lab, val, act, extra='', cls=''):
    return (f'<div class="sa-r{cls}"><span class="sa-k">{lab}</span><span class="sa-v">{val}{extra}</span>'
            + (f'<a href="#" class="hp-rb">{act}</a>' if act else '') + '</div>')
VER = '<span class="st gr sa-st">Verified</span>'

acc = ('<div class="se-ph"><div><h2>Account &amp; sign-in</h2></div></div>'
       + row('Name', 'Ada Ononuju', 'Edit')
       + row('Email', 'ada.ononuju@example.com', 'Change', VER)
       + row('Phone', '+234 803 ••• 0000', 'Change')
       + row('Sign-in methods', 'Email and password · Google', 'Manage')
       + '<span class="hp-lab sa-lab">Leaving Credalio</span>'
       '<div class="sa-x"><div><b>Deactivate account</b><span>Hides your profile and pauses new enrolments. Come back any time.</span></div><a href="#" class="hp-rb">Deactivate</a></div>'
       '<div class="sa-x"><div><b>Delete account</b><span>Permanent. A few responsibilities are settled first.</span></div><a href="CR-SET-002d.dc.html" class="sa-del">Delete</a></div>')

SESS = [(LAPTOP, 'Chrome on macOS', 'Lagos, Nigeria · Active now', None), (PHONE, 'Credalio app on iPhone', 'Lagos, Nigeria · 2 hours ago', 'Sign out'),
        (LAPTOP, 'Firefox on Windows', 'Abuja, Nigeria · 5 days ago', 'Sign out')]
sess = ''.join(f'<li class="ss-r"><span class="ss-ic">{ic(d, 20)}</span><span class="ss-t"><b>{t}</b><span>{w}</span></span>'
               + (f'<a href="#" class="hp-rb">{a}</a>' if a else '<span class="st gr">This device</span>') + '</li>' for d, t, w, a in SESS)
sec = ('<div class="se-ph"><div><h2>Security</h2></div></div>'
       + row('Password', 'Changed 3 months ago', 'Change')
       + row('Two-step verification', '<span class="sa-on"><i></i>On</span><span class="sa-sub">Authenticator app</span>', 'Manage')
       + row('Recovery codes', '8 of 10 left' + tip('Each code signs you in once if you lose your phone. Keep them somewhere safe.'), 'View')
       + '<div class="ss-h"><span class="hp-lab">Where you’re signed in</span><a href="#" class="ds-link">Sign out everywhere else</a></div>'
       '<ul class="ss-l">' + sess + '</ul>')

orgs = ('<div class="og"><span class="so-ic">' + ic(I['org'], 28, 1.7) + '</span><span class="so-pill">Coming soon</span>'
        '<h2>Organizations are coming soon</h2>'
        '<p>Connect the institutions you work with, see your role in each, and handle invitations and agreements in one place.</p>'
        '<div class="og-r"><span class="hp-ic">' + ic(I['bell'], 20) + '</span><span class="so-t"><b>Invitations reach you as notifications</b><span>Until then, accept one to join an organization’s course.</span></span>'
        '<a href="CR-NOT-001.dc.html" class="hp-rb">View</a></div></div>')

DEL = [('book', '4 published learning experiences', 'Stay open to enrolled learners until their access ends.'),
       ('coin', '$1,410.00 in earnings', 'Paid out first. Pending earnings are paid when they clear.'),
       ('col', '1,214 active learners', 'Keep access to what they enrolled in.'),
       ('org', 'Roles at ABC Institute', 'ABC Institute is told, so it can reassign them.'),
       ('val', 'Validation records', 'Kept for audit. Your name stays on past records.')]
dlist = ''.join(f'<li><span class="hp-ic">{ic(I[i], 19)}</span><span class="so-t"><b>{t}</b><span>{d}</span></span></li>' for i, t, d in DEL)
dlg = ('<sc-if value="{{isDel}}" hint-placeholder-val="{{false}}"><div class="dl-ov" aria-hidden="false"></div>'
       '<div class="dl" role="dialog" aria-modal="true" aria-labelledby="dl-h"><a href="CR-SET-001.dc.html" class="dl-x" aria-label="Close">' + X + '</a>'
       '<h2 id="dl-h">Before your account can be deleted</h2><p>These are settled first, so nobody loses what they rely on.</p>'
       '<ul class="dl-l">' + dlist + '</ul>'
       '<div class="dl-ft"><a href="#" class="hp-rb dl-alt">Deactivate instead</a><a href="#" class="dl-go">Request deletion</a></div>'
       '<span class="dl-n">Nothing is removed until everything above is settled.</span></div></sc-if>')

main_set = ('<main class="ds-main hp">\n<div class="hp-head ob-in"><div><h1 class="ds-h1">Settings</h1></div></div>'
            '<div class="se ob-in2"><nav class="se-nav" aria-label="Settings">' + nav() + '</nav>'
            '<section class="ds-card se-p" aria-label="{{panel}}">'
            '<sc-if value="{{isAcc}}" hint-placeholder-val="{{true}}">' + acc + '</sc-if>'
            '<sc-if value="{{isSec}}" hint-placeholder-val="{{false}}">' + sec + '</sc-if>'
            '<sc-if value="{{isOrg}}" hint-placeholder-val="{{false}}">' + orgs + '</sc-if>'
            '</section></div>' + dlg + '\n</main>')
js_set = """    const v = props.variant || 'account';
    const acc = v === 'account' || v === 'delete';
    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }),
      isAcc: acc, isSec: v === 'security', isOrg: v === 'orgs', isDel: v === 'delete',
      panel: acc ? 'Account and sign-in' : (v === 'security' ? 'Security' : 'My organizations'),
      nv: { acc: acc ? 'on' : '', sec: v === 'security' ? 'on' : '', org: v === 'orgs' ? 'on' : '' } };"""
css_set = B.css_set + TIP_CSS + """
.st{display:inline-flex;align-items:center;gap:6px;height:26px;padding:0 11px;border-radius:999px;font-size:12.5px;font-weight:500;white-space:nowrap}
.st.gr{background:#E7F5EE;color:#0F6B45}
.se-p{padding:6px 32px 28px 32px}
.se-ph{padding:22px 0 14px 0}
.sa-r{display:grid;grid-template-columns:200px minmax(0,1fr) auto;align-items:center;gap:24px;min-height:44px;padding:16px 0;border-bottom:1.5px solid #F0F2F8}
.sa-k{font-size:14px;color:#5B6582}
.sa-v{display:flex;align-items:center;flex-wrap:wrap;gap:4px 12px;font-size:15px;font-weight:500;color:#0B1433;min-width:0}
.sa-v .tip{margin-left:-4px}
.sa-sub{font-size:13.5px;font-weight:400;color:#5B6582}
.sa-on{display:inline-flex;align-items:center;gap:8px;color:#0F6B45}.sa-on i{width:8px;height:8px;border-radius:50%;background:#0F6B45}
.sa-lab{display:block;margin-top:34px}
.sa-x{display:flex;align-items:center;justify-content:space-between;gap:24px;padding:16px 0;border-bottom:1.5px solid #F0F2F8}
.sa-x:last-child{border-bottom:0;padding-bottom:4px}
.sa-x > div{display:flex;flex-direction:column;gap:3px}.sa-x b{font-size:15px;font-weight:600}.sa-x div span{font-size:13.5px;color:#5B6582}
.sa-del{display:inline-flex;align-items:center;height:40px;padding:0 16px;border-radius:999px;color:#B42318;font-size:14px;font-weight:600;text-decoration:none}
.sa-del:hover{background:#FDECEA}
.ss-h{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-top:34px}
.ss-h .ds-link{font-size:14px}
.ss-l{list-style:none;margin:10px 0 0 0;padding:0}
.ss-r{display:flex;align-items:center;gap:16px;padding:14px 0;border-bottom:1.5px solid #F0F2F8}
.ss-r:last-child{border-bottom:0;padding-bottom:0}
.ss-ic{width:42px;height:42px;flex-shrink:0;border-radius:12px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.ss-t{flex-grow:1;display:flex;flex-direction:column;gap:2px;min-width:0}.ss-t b{font-size:15px;font-weight:600}.ss-t span{font-size:13.5px;color:#5B6582}
.og{display:flex;flex-direction:column;align-items:center;text-align:center;padding:64px 24px 40px 24px;max-width:560px;margin:0 auto}
.so-ic{width:60px;height:60px;border-radius:18px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.so-pill{margin-top:22px;display:inline-flex;align-items:center;height:28px;padding:0 12px;border-radius:999px;background:#F1F3F8;color:#4A5578;font-size:12.5px;font-weight:500}
.og h2{margin:12px 0 0 0;font-size:24px;line-height:1.2;font-weight:600;letter-spacing:-0.02em}
.og p{margin:10px 0 0 0;font-size:15.5px;line-height:1.6;color:#3A4566}
.og-r{margin-top:32px;width:100%;box-sizing:border-box;display:flex;align-items:center;gap:14px;padding:14px 14px 14px 16px;border-radius:16px;border:1.5px solid #E6EAF3;text-align:left}
.so-t{flex-grow:1;display:flex;flex-direction:column;gap:2px;min-width:0}.so-t b{font-size:15px;font-weight:600}.so-t span{font-size:13.5px;color:#5B6582}
.dl-ov{position:fixed;inset:0;z-index:40;background:rgba(11,20,51,.42)}
.dl{position:fixed;z-index:41;left:50%;top:50%;transform:translate(-50%,-50%);width:min(560px,calc(100vw - 32px));box-sizing:border-box;padding:32px 32px 24px 32px;border-radius:24px;background:#FFFFFF;box-shadow:0 30px 80px rgba(11,20,51,.28)}
.dl-x{position:absolute;right:18px;top:18px;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#5B6582}
.dl-x:hover{background:#F1F3F8}
.dl h2{margin:0;padding-right:40px;font-size:22px;font-weight:600;letter-spacing:-0.02em}
.dl > p{margin:8px 0 0 0;font-size:14.5px;line-height:1.5;color:#4A5578}
.dl-l{list-style:none;margin:22px 0 0 0;padding:0;display:flex;flex-direction:column;gap:16px}
.dl-l li{display:flex;align-items:flex-start;gap:14px}
.dl-l .hp-ic{flex-shrink:0}
.dl-ft{margin-top:28px;display:flex;justify-content:flex-end;gap:10px}
.dl-go{display:inline-flex;align-items:center;height:44px;padding:0 22px;border-radius:999px;background:#B42318;color:#FFFFFF;font-size:15px;font-weight:600;text-decoration:none}
.dl-go:hover{background:#912018}
.dl-alt{height:44px;padding:0 20px;font-size:15px}
.dl-n{display:block;margin-top:14px;text-align:right;font-size:12.5px;color:#8A93AD}
@media (max-width: 960px){
.se-p{padding:2px 18px 22px 18px}
.se-ph{padding:18px 0 8px 0}
.sa-r{grid-template-columns:minmax(0,1fr) auto;gap:4px 14px;padding:14px 0}
.sa-k{grid-column:1;font-size:13px}
.sa-v{grid-column:1;grid-row:2;font-size:14.5px}
.sa-r .hp-rb{grid-column:2;grid-row:1 / span 2;height:36px;padding:0 14px;font-size:13.5px}
.sa-lab{margin-top:30px}
.sa-x{gap:14px}
.sa-x .hp-rb{height:36px;padding:0 14px;font-size:13.5px}
.sa-del{height:36px;padding:0 10px;font-size:13.5px}
.ss-h{margin-top:30px;flex-wrap:wrap;gap:6px}
.ss-r{gap:12px}.ss-ic{width:38px;height:38px}
.ss-r .hp-rb{height:36px;padding:0 13px;font-size:13px}
.og{padding:36px 4px 12px 4px}
.so-ic{width:52px;height:52px;border-radius:16px}
.og h2{font-size:21px}.og p{font-size:14.5px}
.og-r{margin-top:26px;padding:12px}
.og-r .hp-rb{height:34px;padding:0 13px;font-size:13px}
.dl{left:0;right:0;top:auto;bottom:0;transform:none;width:100%;padding:28px 18px 22px 18px;border-radius:24px 24px 0 0}
.dl h2{font-size:20px}
.dl-l{gap:14px}
.dl-ft{flex-direction:column-reverse;gap:8px}
.dl-go,.dl-alt{justify-content:center;width:100%;box-sizing:border-box}
.dl-n{text-align:center}
}
"""
B.page('CR-SET', 'Settings', main_set, js_set, css_set, 'Credalio · Settings', "{ nav: false }")
props_patch('CR-SET')
OUT.append('CR-SET.dc.html')
wrap('CR-SET', [('CR-SET-001', 'account', 960), ('CR-SET-002d', 'delete', 844), ('CR-SET-003', 'security', 1000), ('CR-ORG-SOON', 'orgs', 844)])

# ======================= CR-PUB · variant public (PROF-002) — patch LIVE file =======================
s = rd('CR-PUB.dc.html')
assert 'isPub' not in s, 'CR-PUB already patched'
pubh = ('<sc-if value="{{isPub}}" hint-placeholder-val="{{false}}"><header class="pu-top"><a href="#" class="pu-lg"><span class="lg-word" role="img" aria-label="Credalio"></span></a>'
        '<span style="flex-grow: 1"></span><a href="#" class="pu-ex">Explore</a><a href="#" class="hp-rb">Log in</a></header></sc-if>\n')
s = s.replace('<main class="ds-main hp">', pubh + '<main class="ds-main hp">', 1)
assert s.count('<div class="ds-root">') == 1
s = s.replace('<div class="ds-root">', '<div class="ds-root {{pubCls}}">', 1)
s = s.replace("isPrev: v === 'preview' };", "isPrev: v === 'preview', isPub: v === 'public', pubCls: v === 'public' ? 'pu' : '' };", 1)
assert "isPub: v === 'public'" in s
PUBCSS = """
/* PROF-002: public page = no Studio shell */
.ds-root.pu{grid-template-columns:minmax(0,1fr)}
.pu .ds-side,.pu .ds-scrim,.pu .ds-top{display:none !important}
.pu .ds-main{max-width:1180px;margin:0 auto;padding-top:28px}
.pu-top{position:sticky;top:0;z-index:10;height:72px;box-sizing:border-box;padding:0 clamp(20px,3vw,40px);display:flex;align-items:center;gap:10px;background:rgba(255,255,255,.9);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1.5px solid #EEF1F7}
.pu-ex{height:40px;padding:0 14px;display:inline-flex;align-items:center;border-radius:999px;font-size:14.5px;font-weight:500;color:#3A4566;text-decoration:none}
.pu-ex:hover{background:#F1F3F8}
@media (max-width: 960px){.pu-top{height:60px;padding:0 16px}.pu .ds-main{padding-top:30px}.pu-ex{display:none}}
"""
i = s.rfind('</style>', 0, s.find('</helmet>'))
s = s[:i] + PUBCSS + s[i:]
wr('CR-PUB.dc.html', s); OUT.append('CR-PUB.dc.html')
wrap('CR-PUB', [('CR-PROF-002', 'public', 1220)])
print('build32 ok'); print(' '.join(OUT))
