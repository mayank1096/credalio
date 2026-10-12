# build33: PATCHES live CR-SET in place with variants notif / privacy / lang / signin (= SET-004 / SET-005 / SET-006 / SET-008)
# and writes their wrappers. SET-007 = existing CR-HOME-SET. usage: python3 build33.py <dir>  (asserts if already patched)
import re, sys, os
P = sys.argv[1]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tipx import tip
def rd(f): return open(os.path.join(P, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(P, f), 'w', encoding='utf-8').write(s)
def ic(paths, w=20, sw=1.9):
    return f'<svg width="{w}" height="{w}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>'
CHEV = ic('<path d="m6 9 6 6 6-6"></path>', 16, 2.2)
BACK = ic('<path d="M19 12H5"></path><path d="m11 6-6 6 6 6"></path>', 16, 2.2)
ARR = ic('<path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path>', 18, 2.4)
OUT = []
s = rd('CR-SET.dc.html')
assert 'isNot' not in s, 'already patched'

# nav hooks (Notifications, Privacy, Language & region are the 4th-6th plain items)
items = list(re.finditer(r'<a href="#" class="se-n">', s))
assert len(items) == 4  # Profile, Notifications, Privacy, Language
for m, k in reversed(list(zip(items[1:], ['not', 'pri', 'lan']))):
    s = s[:m.start()] + f'<a href="#" class="se-n {{{{nv.{k}}}}}">' + s[m.end():]

def sw(on, lab):
    return f'<button type="button" class="hp-sw{" on" if on else ""}" role="switch" aria-checked="{"true" if on else "false"}" aria-label="{lab}"></button>'

# ---------- SET-004 notifications ----------
NM = [('Collaboration', 'Invitations, mentions, agreements', 1, 1, 0), ('Validation', 'Requests, meetings, decisions', 1, 1, 1),
      ('Learner activity', 'Enrolments and completions', 1, 0, 0), ('Discussions', 'New questions and replies', 1, 0, 0),
      ('Calendar', 'Upcoming sessions and changes', 1, 1, 0), ('Earnings & payouts', 'Earnings and payout status', 1, 1, 1),
      ('Credit Wallet', 'Funding and payments', 1, 1, 1), ('Creator updates', 'Product news and guides', 1, 0, 0)]
ALW = '<span class="nm-al">Always' + tip('Decisions, payments and payouts are always emailed.', 'r') + '</span>'
rows = ''.join(f'<div class="nm-r"><span class="nm-t"><b>{t}</b><span>{d}</span></span><span class="nm-c">{sw(a, t + " in the app")}</span>'
               f'<span class="nm-c">{ALW if lock else sw(e, t + " by email")}</span></div>' for t, d, a, e, lock in NM)
notif = ('<div class="se-ph"><div><h2>Notifications</h2></div></div>'
         '<div class="nm-h"><span></span><span>In the app</span><span>Email</span></div>' + rows +
         '<span class="hp-lab sa-lab">Message pop-ups</span>'
         '<div class="se-row"><div class="se-l"><b>Show new messages as pop-ups</b><span>Opens the conversation. Paused while you’re away.</span></div>' + sw(1, 'Message pop-ups') + '</div>'
         '<div class="se-row nm-last"><div class="se-l"><b>Show message preview</b><span>Turn off if you share your screen.</span></div>' + sw(1, 'Message preview') + '</div>')

# ---------- SET-005 privacy ----------
PR = [('Public creator profile', 'Learners can find and view your profile.', 1), ('Show location', 'Lagos, Nigeria on your public profile.', 1),
      ('Show when you’re online', 'Collaborators see if you’re online or away.', 1), ('Learner support requests', 'Enrolled learners can ask you for help.', 1),
      ('Help improve Credalio', 'Share anonymised usage data.', 0)]
priv = ('<div class="se-ph"><div><h2>Privacy</h2></div></div>'
        + ''.join(f'<div class="se-row"><div class="se-l"><b>{t}</b><span>{d}</span></div>{sw(on, t)}</div>' for t, d, on in PR)
        + '<span class="hp-lab sa-lab">Your data</span>'
        '<div class="sa-x"><div><b>Download my data</b><span>Your profile, learning experiences and activity, emailed as a file.</span></div><a href="#" class="hp-rb">Request</a></div>'
        '<a href="#" class="ds-link pv-pol">Privacy policy</a>')

# ---------- SET-006 language & region ----------
LG = [('Language', ['English', 'French', 'Yoruba', 'Hausa', 'Igbo'], ''),
      ('Time zone', ['WAT (UTC+1) · Lagos', 'GMT (UTC+0) · Accra', 'EAT (UTC+3) · Nairobi'], tip('Sets your Calendar, live sessions and office hours.')),
      ('Date format', ['12 Oct 2026', '12/10/2026', '2026-10-12'], ''), ('Time format', ['24-hour · 16:00', '12-hour · 4:00 PM'], '')]
def sel(opts, lab):
    return f'<div class="ob-sel lg-sel"><select class="ob-f" aria-label="{lab}">' + ''.join(f'<option>{o}</option>' for o in opts) + '</select>' + CHEV + '</div>'
lang = ('<div class="se-ph"><div><h2>Language &amp; region</h2></div></div>'
        + ''.join(f'<div class="se-row"><div class="se-l"><b class="lg-b">{t}{tp}</b></div>{sel(o, t)}</div>' for t, o, tp in LG)
        + '<div class="se-ft"><span class="lg-pv"><span class="hp-lab">Preview</span><span>Mon 12 Oct 2026 · 16:00 WAT</span></span>'
        f'<a href="#" class="ds-btn hp-btn"><span>Save changes</span><span class="ob-arrow">{ARR}</span></a></div>')

# ---------- SET-008 sign-in methods ----------
G = '<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path fill="#4285F4" d="M21.6 12.2c0-.7-.1-1.4-.2-2H12v3.8h5.4a4.6 4.6 0 0 1-2 3v2.5h3.2c1.9-1.7 3-4.3 3-7.3z"/><path fill="#34A853" d="M12 22c2.7 0 5-.9 6.6-2.4l-3.2-2.5c-.9.6-2 1-3.4 1-2.6 0-4.8-1.8-5.6-4.1H3.1v2.6A10 10 0 0 0 12 22z"/><path fill="#FBBC05" d="M6.4 14c-.2-.6-.3-1.3-.3-2s.1-1.4.3-2V7.4H3.1a10 10 0 0 0 0 9.2L6.4 14z"/><path fill="#EA4335" d="M12 5.9c1.5 0 2.8.5 3.8 1.5l2.8-2.8A10 10 0 0 0 3.1 7.4L6.4 10c.8-2.4 3-4.1 5.6-4.1z"/></svg>'
APPLE = '<svg width="19" height="19" viewBox="0 0 24 24" aria-hidden="true"><path fill="#0B1433" d="M16.4 12.6c0-2.4 2-3.6 2.1-3.7-1.1-1.7-2.9-1.9-3.5-1.9-1.5-.2-2.9.9-3.7.9-.8 0-1.9-.9-3.2-.8-1.6 0-3.1 1-4 2.4-1.7 3-.4 7.4 1.2 9.8.8 1.2 1.8 2.5 3 2.4 1.2 0 1.7-.8 3.1-.8 1.5 0 1.9.8 3.2.8 1.3 0 2.2-1.2 3-2.4.9-1.4 1.3-2.7 1.3-2.8 0 0-2.5-1-2.5-3.9zM14 5.5c.7-.8 1.1-1.9 1-3-1 0-2.1.7-2.8 1.5-.6.7-1.2 1.8-1 2.9 1.1.1 2.1-.6 2.8-1.4z"/></svg>'
MAIL = ic('<rect x="3" y="5" width="18" height="14" rx="2.5"></rect><path d="m4 7 8 6 8-6"></path>', 20, 1.9)
SG = [(MAIL, 'Email and password', 'ada.ononuju@example.com', True, 'Change password'), (G, 'Google', 'ada.ononuju@gmail.com', True, 'Disconnect'),
      (APPLE, 'Apple', 'Not connected', False, 'Connect')]
sign = ('<a href="CR-SET-001.dc.html" class="pg-back sg-back">' + BACK + 'Account &amp; sign-in</a>'
        '<div class="se-ph sg-ph"><div><h2 class="sg-h">Sign-in methods' + tip('You always keep at least one way to sign in.') + '</h2></div></div>'
        '<ul class="ss-l sg-l">' + ''.join(f'<li class="ss-r"><span class="ss-ic sg-ic">{i}</span><span class="ss-t"><b>{t}</b><span>{d}</span></span>'
        + ('<span class="st gr">Connected</span>' if on else '') + f'<a href="#" class="hp-rb">' + (f'<span class="sg-lg">{a}</span><span class="sg-sm">Change</span>' if a == 'Change password' else a) + '</a></li>' for i, t, d, on, a in SG) + '</ul>')

panels = ('<sc-if value="{{isNot}}" hint-placeholder-val="{{false}}">' + notif + '</sc-if>'
          '<sc-if value="{{isPri}}" hint-placeholder-val="{{false}}">' + priv + '</sc-if>'
          '<sc-if value="{{isLan}}" hint-placeholder-val="{{false}}">' + lang + '</sc-if>'
          '<sc-if value="{{isSig}}" hint-placeholder-val="{{false}}">' + sign + '</sc-if>')
assert s.count('</section></div><sc-if value="{{isDel}}"') == 1
s = s.replace('</section></div><sc-if value="{{isDel}}"', panels + '</section></div><sc-if value="{{isDel}}"', 1)

old_js = re.search(r"    const v = props\.variant.*?\} \};", s, flags=re.S).group(0)
new_js = """    const v = props.variant || 'account';
    const acc = v === 'account' || v === 'delete' || v === 'signin';
    const T = { account: 'Account and sign-in', delete: 'Account and sign-in', signin: 'Sign-in methods', security: 'Security', orgs: 'My organizations', notif: 'Notifications', privacy: 'Privacy', lang: 'Language and region' };
    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }),
      isAcc: v === 'account' || v === 'delete', isSec: v === 'security', isOrg: v === 'orgs', isDel: v === 'delete',
      isNot: v === 'notif', isPri: v === 'privacy', isLan: v === 'lang', isSig: v === 'signin',
      panel: T[v] || '',
      nv: { acc: acc ? 'on' : '', sec: v === 'security' ? 'on' : '', org: v === 'orgs' ? 'on' : '', not: v === 'notif' ? 'on' : '', pri: v === 'privacy' ? 'on' : '', lan: v === 'lang' ? 'on' : '' } };"""
s = s.replace(old_js, new_js, 1)

CSS = """
/* build33: notifications matrix, privacy, language, sign-in methods */
.nm-h{display:grid;grid-template-columns:minmax(0,1fr) 110px 110px;padding:16px 0 6px 0;font-size:12.5px;font-weight:500;color:#8A93AD}
.nm-h span{text-align:center}
.nm-r{display:grid;grid-template-columns:minmax(0,1fr) 110px 110px;align-items:center;padding:13px 0;border-bottom:1.5px solid #F0F2F8}
.nm-t{display:flex;flex-direction:column;gap:2px;min-width:0}.nm-t b{font-size:15px;font-weight:600}.nm-t span{font-size:13.5px;color:#5B6582}
.nm-c{display:flex;justify-content:center}
.nm-al{display:inline-flex;align-items:center;gap:4px;font-size:13px;font-weight:500;color:#5B6582}
.nm-last{border-bottom:0;padding-bottom:4px}
.se-row > .hp-sw{justify-self:end}
.pv-pol{display:inline-block;margin-top:22px;font-size:14px}
.lg-b{display:inline-flex;align-items:center;gap:6px}
.lg-sel{justify-self:end;width:280px}
.lg-sel select{width:100%;height:44px;box-sizing:border-box;padding:0 40px 0 14px;border-radius:12px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:inherit;font-size:14.5px;color:#0B1433;appearance:none;-webkit-appearance:none;outline:none}
.lg-pv{display:flex;flex-direction:column;gap:3px;font-size:15px;font-weight:500}
.pg-back{display:inline-flex;align-items:center;gap:8px;font-size:14px;font-weight:500;color:#4A5578;text-decoration:none}.pg-back:hover{color:#0B1433}
.sg-back{margin-top:24px}
.sg-ph{padding-top:12px}
.sg-h{display:flex;align-items:center;gap:8px}
.sg-l{margin-top:8px}
.sg-l .ss-r{padding:16px 0}
.sg-ic{background:#FFFFFF;border:1.5px solid #E6EAF3;color:#3A4566}
.sg-l .st{margin-right:4px}
.sg-sm{display:none}
@media (max-width: 960px){
.nm-h,.nm-r{grid-template-columns:minmax(0,1fr) 58px 58px}
.nm-h{font-size:11.5px;padding-top:14px}
.nm-h span:nth-child(2){font-size:0}.nm-h span:nth-child(2)::after{content:'App';font-size:11.5px}
.nm-t b{font-size:14.5px}.nm-t span{font-size:13px}
.nm-al{font-size:12px}
.se-row{grid-template-columns:minmax(0,1fr) auto}
.lg-sel{grid-column:1 / -1;width:100%}
.se-row:has(.lg-sel){gap:10px}
.sg-back{margin-top:16px}
.sg-l .st{display:none}
.sg-lg{display:none}.sg-sm{display:inline}
.sg-l .ss-t span{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sg-l .hp-rb{height:36px;padding:0 13px;font-size:13px}
}
"""
i = s.rfind('</style>', 0, s.find('</helmet>'))
s = s[:i] + CSS + s[i:]
m = 'Email and password · Google</span><a href="#" class="hp-rb">Manage</a>'
assert s.count(m) == 1
s = s.replace(m, m.replace('href="#"', 'href="CR-SET-008.dc.html"'))
wr('CR-SET.dc.html', s); OUT.append('CR-SET.dc.html')

# wrappers (same templates as build32)
wd, wm = rd('CR-SET-001.dc.html'), rd('CR-SET-001-Mobile.dc.html')
for n, var, hm in [('CR-SET-004', 'notif', 1180), ('CR-SET-005', 'privacy', 860), ('CR-SET-006', 'lang', 844), ('CR-SET-008', 'signin', 844)]:
    for tpl, suf in [(wd, ''), (wm, '-Mobile')]:
        t = tpl.replace('variant="account"', f'variant="{var}"').replace('CR-SET-001', n)
        if suf:
            t = re.sub(r'hint-size="390px,\d+px"', f'hint-size="390px,{hm}px"', t)
            t = re.sub(r'width: 390px; height: \d+px;', f'width: 390px; height: {hm}px;', t, count=1)
            t = re.sub(r'"\$preview":\{"width":390,"height":\d+\}', f'"$preview":{{"width":390,"height":{hm}}}', t)
        if not suf and n == 'CR-SET-004':
            t = t.replace('height: 820px;', 'height: 1000px;').replace('hint-size="1440px,820px"', 'hint-size="1440px,1000px"').replace('"height":820', '"height":1000')
        wr(n + suf + '.dc.html', t); OUT.append(n + suf + '.dc.html')
print('build33 ok'); print(' '.join(OUT))
