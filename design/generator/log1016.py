"""Log in + password reset (CR-LOG-001 / 002 / 003) for the Link 1 canvas.

Built from the LIVE onboarding files so the frame, fields and buttons match:
  CR-ONB-003c (form frame + campus scene), CR-ONB-003 (header, Google/Apple row),
  CR-ONB-003b (check-inbox illustration), CR-KYC-003 (outcome emblem + confetti).
Usage: python3 log1016.py <canvas/project dir>
Writes the 3 sources + 17 wrapper boards; canvas.json layout is done by log1016_canvas.py.
"""
import re, sys, os

P = sys.argv[1]
rd = lambda f: open(os.path.join(P, f)).read()
c3c, c3, c3b, kyc = rd('CR-ONB-003c.dc.html'), rd('CR-ONB-003.dc.html'), rd('CR-ONB-003b.dc.html'), rd('CR-KYC-003.dc.html')

css = lambda s: re.search(r'<style>(.*?)</style>', s, re.S).group(1).strip('\n')
BASE = css(c3c).split('\n')
def extra(src, keep):
    return [l for l in css(src).split('\n') if l not in BASE and keep(l)]

ROW_CSS = ['@media (max-width: 960px){.ob-hide-sm{display:none}.ob-row{flex-direction:column !important;align-items:stretch !important;width:100%}.ob-row > a{flex:none !important}}']
INBOX_CSS = ['@media (max-width: 960px){' + l + '}' if l.startswith('.ob-illus{') else l for l in extra(c3b, lambda l: 'ob-illus' in l or 'ob-link' in l)]
KO_CSS = [l for l in css(kyc).split('\n') if re.match(r'\.(ko-v|ko-a|ko-emb|ko-halo|ko-disc|ko-tick)\b', l) or l.startswith('@keyframes koDraw')]
CF_CSS = [l for l in css(kyc).split('\n') if l.startswith('.cf') or l.startswith('@keyframes cf') or '.cf{' in l]
# cfPath keyframes span several lines in the source; copy the whole block
m = re.search(r'@keyframes cfPath\{.*?\n100%[^\n]*\}\}', css(kyc), re.S)
CF_CSS = [l for l in CF_CSS if not l.startswith('@keyframes cfPath')] + [m.group(0)]

LG_CSS = r'''
.ob-link:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:3px}
.lg-labrow{display:flex;align-items:baseline;justify-content:space-between;gap:12px}
.lg-forgot{font-size:13px;font-weight:600;text-decoration:none;margin:0 2px 6px 0}
.lg-forgot:hover{text-decoration:underline}
.lg-go{width:100%;justify-content:space-between}
.lg-off{background:#C3CEEA !important;box-shadow:none !important;pointer-events:none;cursor:default}
.lg-off .ob-arrow{color:#8A9BC8 !important}
.lg-al{display:flex;align-items:flex-start;gap:10px;width:100%;box-sizing:border-box;padding:12px 14px;border-radius:14px;border:1.5px solid var(--ab);background:var(--abg);font-size:14px;line-height:1.5;color:#0B1433;text-align:left}
.lg-al svg{flex-shrink:0;margin-top:2px;color:var(--ai)}
.lg-al b{font-weight:600}
.lg-al a{font-weight:600}
.lg-red{--ab:#FBD5D1;--abg:#FEF4F3;--ai:#D92D20}
.lg-amb{--ab:#F4DFB0;--abg:#FFF8EA;--ai:#B26A00}
.lg-note{margin:16px 0 0 0;font-size:14px;line-height:1.6;color:#4A5578;text-align:center}
.lg-note a{font-weight:600}
.lg-glow{position:absolute;left:50%;top:-260px;width:1200px;height:600px;transform:translateX(-50%);background:radial-gradient(closest-side,rgba(var(--glow),.13),rgba(var(--glow),0));z-index:-1;pointer-events:none}
.lg-ok{--glow:15,107,69}
.lg-wait{--glow:214,140,20}
.ko-emb{margin-bottom:6px}
@media (max-width: 960px){.lg-glow{width:640px;top:-300px}.ob-main{padding-top:44px !important}.lg-note{margin-top:14px}}
'''.strip('\n').split('\n')

def head(title, extra_css):
    lines = BASE + extra_css
    seen, out = set(), []
    for l in lines:
        if l not in seen:
            seen.add(l); out.append(l)
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>%s</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">\n<style>\n%s\n</style>\n</helmet>\n') % (title, '\n'.join(out))

ROOT = re.search(r'<div class="ob-root"[^>]*>', c3c).group(0)
HDR = c3c[c3c.index('<header'):c3c.index('</header>') + 9]
HDR_JOIN = HDR.replace('<span></span>\n</header>',
    '<div style="display: flex; align-items: center; gap: 14px; font-size: 14px; color: #3A4566"><span class="ob-hide-sm">New to Credalio?</span> '
    '<a href="Main.dc.html" class="ob-ghost" style="display: flex; align-items: center; height: 44px; padding: 0 20px; border-radius: 999px; border: 1.5px solid #D6DDEE; background: #FFFFFF; color: #0B1433; font-weight: 600; text-decoration: none">Create account</a></div>\n</header>')
assert HDR_JOIN != HDR
BACK = re.search(r'<a href="[^"]*" class="ob-ghost ob-back".*?</a>', c3c, re.S).group(0)
def track(href):
    return ('<div class="ob-track" style="position: absolute; left: 0; top: 88px; width: 100%; height: 44px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; z-index: 3">\n'
            + re.sub(r'href="[^"]*"', 'href="%s"' % href, BACK, count=1) + '\n</div>\n')
SCENE = '<div class="ob-scene" aria-hidden="true"></div>\n'
ARROW = re.search(r'<span class="ob-arrow".*?</span>', c3c, re.S).group(0)
BTN_STYLE = re.search(r'<a href="CR-ONB-004.dc.html" class="ob-btn" style="([^"]*)"', c3c).group(1)
def btn(href, label, cls='', top='clamp(18px, 3vh, 26px)'):
    st = re.sub(r'margin-top: [^;]*;', 'margin-top: %s;' % top, BTN_STYLE)
    return '<a href="%s" class="ob-btn %s" style="%s">%s%s</a>' % (href, cls, st, label, ARROW)
SOCIAL = re.search(r'<div class="ob-row" style="width: 100%; display: flex; gap: 10px">.*?Continue with Apple</a></div>', c3, re.S).group(0)
OR = re.search(r'<div aria-hidden="true" style="width: 100%; margin: clamp\(14px, 2.6vh, 20px\) 0;.*?</div>', c3, re.S).group(0)
SHOW_BTN = re.search(r'<button type="button" class="ob-x".*?</button>', c3c, re.S).group(0)
ERR_ICON = re.search(r'<span class="ob-err" role="alert">(<svg.*?</svg>)', c3c, re.S).group(1)
H1 = '<h1 class="ob-h1 ob-in" style="margin: 0; font-size: clamp(36px, 6vh, 52px); line-height: 1.1; font-weight: 600; letter-spacing: -0.035em; color: #0B1433; text-align: center; width: max-content; max-width: calc(100vw - 48px)">%s</h1>'
SUB = '<p class="ob-in2" style="margin: 12px 0 0 0; max-width: 460px; font-size: 16px; line-height: 1.55; color: #4A5578; text-align: center">%s</p>'
def main(top, width, inner):
    return ('<main class="ob-main" style="position: absolute; z-index: 2; left: 0; top: %s; width: 100%%; display: flex; flex-direction: column; align-items: center">\n'
            '<div class="ob-col" style="width: min(%dpx, calc(100%% - 48px)); display: flex; flex-direction: column; align-items: center">\n%s\n</div>\n</main>\n') % (top, width, inner)
WAVE = re.search(r'<img class="ob-wave"[^>]*>', rd('CR-ONB-004.dc.html')).group(0)
WAVE_CSS = [l for l in css(rd('CR-ONB-004.dc.html')).split('\n') if 'obWave' in l or 'ob-wave' in l]
I_ALERT = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="M12 7.5v5.5"></path><path d="M12 16.4v.2"></path></svg>'
I_MAIL = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="3"></rect><path d="m4 7 8 6 8-6"></path></svg>'
I_LOCK = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4.5" y="10.5" width="15" height="10" rx="2.5"></rect><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3"></path></svg>'
def err(cond, text):
    return '<sc-if value="{{%s}}" hint-placeholder-val="{{false}}"><span class="ob-err" role="alert">%s%s</span></sc-if>' % (cond, ERR_ICON, text)
def script(js):
    return ('</div>\n</x-dc>\n<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":1440,"height":820}}\'>\n%s\n</script>\n</body>\n</html>\n') % js.strip('\n')

# ---------- CR-LOG-001 · Log in (variants invalid / wrong / unverified / locked) ----------
alerts = (
    '<sc-if value="{{isWrong}}" hint-placeholder-val="{{false}}"><div class="lg-al lg-red ob-in3" role="alert" style="margin-top: clamp(18px, 3vh, 24px)">%s<span>That email and password don’t match. Try again, or <a href="CR-LOG-002.dc.html">reset your password</a>.</span></div></sc-if>\n'
    '<sc-if value="{{isUnv}}" hint-placeholder-val="{{false}}"><div class="lg-al lg-amb ob-in3" role="status" style="margin-top: clamp(18px, 3vh, 24px)">%s<span><b>Confirm your email to log in.</b> We’ve sent a new link to {{email}}. <a href="#">Resend link</a></span></div></sc-if>\n'
    '<sc-if value="{{isLock}}" hint-placeholder-val="{{false}}"><div class="lg-al lg-amb ob-in3" role="alert" style="margin-top: clamp(18px, 3vh, 24px)">%s<span><b>Logging in is paused for 15 minutes</b> after too many attempts. You can <a href="CR-LOG-002.dc.html">reset your password</a> now.</span></div></sc-if>'
) % (I_ALERT, I_MAIL, I_LOCK)
form1 = (
    '<div class="ob-in3" style="margin-top: clamp(16px, 2.6vh, 22px); width: 100%%; display: flex; flex-direction: column; gap: 14px; text-align: left">\n'
    '<div><label for="lg-em" class="ob-lab">Email</label><input id="lg-em" class="ob-f {{eCls}}" type="email" value="{{email}}" onChange="{{onEmail}}" aria-invalid="{{eInv}}" autocomplete="email" placeholder="you@example.com">%s</div>\n'
    '<div><div class="lg-labrow"><label for="lg-pw" class="ob-lab">Password</label><a href="CR-LOG-002.dc.html" class="lg-forgot">Forgot password?</a></div>'
    '<div style="position: relative"><input id="lg-pw" class="ob-f {{pCls}}" type="{{pwType}}" value="{{pw}}" onChange="{{onPw}}" aria-invalid="{{pInv}}" autocomplete="current-password" placeholder="Your password" style="padding-right: 64px">%s</div>%s</div>\n'
    '</div>'
) % (err('eErr', 'Enter a full email, like name@example.com.'), SHOW_BTN, err('pErr', 'Enter your password.'))
inner1 = '\n'.join([H1 % ('Welcome back.' + WAVE), SUB % 'Log in to pick up where you left off.', alerts, form1,
                    btn('CR-DASH-NEW.dc.html', 'Log in', 'lg-go {{goCls}}" aria-disabled="{{goDis}}'), OR, SOCIAL.replace('CR-ONB-004.dc.html', 'CR-DASH-NEW.dc.html')])
log1 = (head('CR-LOG-001 · Log in', ROW_CSS + LG_CSS + WAVE_CSS) + ROOT + '\n' + SCENE + HDR_JOIN + '\n'
        + main('clamp(116px, 15vh, 150px)', 460, inner1) + script(r'''
class Component extends DCLogic {
  constructor(props) {
    super(props);
    const v = (props && props.variant) || 'form';
    const email = { invalid: 'ada.ononuju@', wrong: 'ada.ononuju@example.com', unverified: 'ada.ononuju@example.com', locked: 'ada.ononuju@example.com' }[v] || '';
    this.state = { v, email, pw: v === 'wrong' || v === 'locked' ? 'sunshine2024' : (v === 'unverified' ? 'Lagos#2026' : ''), show: false };
  }
  renderVals() {
    const { v, email, pw, show } = this.state;
    const eErr = v === 'invalid', pErr = v === 'invalid', both = v === 'wrong';
    return {
      email, pw, onEmail: (e) => this.setState({ email: e.target.value }), onPw: (e) => this.setState({ pw: e.target.value }),
      pwType: show ? 'text' : 'password', showLabel: show ? 'Hide' : 'Show', toggle: () => this.setState({ show: !show }),
      isWrong: v === 'wrong', isUnv: v === 'unverified', isLock: v === 'locked', eErr, pErr,
      eCls: eErr || both ? 'ob-bad' : '', pCls: pErr || both ? 'ob-bad' : '',
      eInv: eErr || both ? 'true' : 'false', pInv: pErr || both ? 'true' : 'false',
      goCls: v === 'locked' ? 'lg-off' : '', goDis: v === 'locked' ? 'true' : 'false'
    };
  }
}'''))

# ---------- CR-LOG-002 · Reset your password (variant sent) ----------
ask = '\n'.join([H1 % 'Forgot your password?', SUB % 'Enter your email and we’ll send you a link to choose a new one.',
    '<div class="ob-in3" style="margin-top: clamp(20px, 3.6vh, 32px); width: 100%; text-align: left"><label for="lg-em" class="ob-lab">Email</label>'
    '<input id="lg-em" class="ob-f" type="email" value="{{email}}" onChange="{{onEmail}}" autocomplete="email" placeholder="you@example.com"></div>',
    btn('CR-LOG-002b.dc.html', 'Send reset link', 'lg-go'),
    '<p class="lg-note">Remembered it? <a href="CR-LOG-001.dc.html" class="ob-link">Back to log in</a></p>'])
sent = '\n'.join([H1 % 'Check your inbox.',
    SUB.replace('max-width: 460px', 'max-width: 520px') % 'If there’s an account for <span style="color: #0B1433; font-weight: 600">{{email}}</span>, a link to reset your password is on its way.',
    btn('CR-LOG-003.dc.html', 'Open email', '', 'clamp(20px, 3.6vh, 30px)'),
    '<p class="lg-note">No email yet? Check spam or <a href="#" class="ob-link">resend the link</a>. <a href="CR-LOG-001.dc.html" class="ob-link">Back to log in</a></p>'])
inner2 = ('<sc-if value="{{ask}}" hint-placeholder-val="{{true}}">\n%s\n</sc-if>\n<sc-if value="{{sent}}" hint-placeholder-val="{{false}}">\n%s\n</sc-if>' % (ask, sent))
log2 = (head('CR-LOG-002 · Forgot your password', ROW_CSS + INBOX_CSS + LG_CSS) + ROOT + '\n'
        + SCENE
        + HDR_JOIN + '\n' + track('CR-LOG-001.dc.html')
        + main('clamp(140px, 19vh, 176px)', 460, inner2).replace('<div class="ob-col" style="width: min(460px', '<div class="ob-col" style="width: min({{colW}}px')
        + script(r'''
class Component extends DCLogic {
  constructor(props) { super(props); const sent = !!(props && props.variant === 'sent'); this.state = { sent, email: sent ? 'ada.ononuju@example.com' : '' }; }
  renderVals() {
    const { sent, email } = this.state;
    return { ask: !sent, sent, email, colW: sent ? 560 : 460, onEmail: (e) => this.setState({ email: e.target.value }) };
  }
}'''))

# ---------- CR-LOG-003 · Choose a new password (variants done / expired) ----------
m0 = c3c.index('<h1 class="ob-h1 ob-in"'); m1 = c3c.index('<a href="CR-ONB-004.dc.html" class="ob-btn"')
pwform = c3c[m0:m1]
pwform = pwform.replace('Choose a password.', 'Choose a new password.')
pwform = pwform.replace('Create a password to protect your account.', 'For <span style="color: #0B1433; font-weight: 600">ada.ononuju@example.com</span>. You’ll use it the next time you log in.')
pwform = pwform.replace('>Password</label>', '>New password</label>').replace('placeholder="Create a password"', 'placeholder="New password"').replace('>Confirm password</label>', '>Confirm new password</label>')
pwform = re.sub(r'<sc-if value="\{\{weak\}\}".*?</sc-if>', '', pwform, flags=re.S)
assert 'New password' in pwform and 'weak' not in pwform
cf = re.search(r'<span class="cf" aria-hidden="true">.*?</span></sc-if>', kyc, re.S).group(0)[:-len('</sc-if>')]
TICK = '<svg class="ko-tick" width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5" pathLength="1"></path></svg>'
CLOCK = '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="13" r="8"></circle><path d="M12 9v4l2.5 2"></path><path d="M9.5 2.5h5"></path></svg>'
H1o = H1.replace('font-size: clamp(36px, 6vh, 52px)', 'font-size: clamp(32px, 5.4vh, 46px)')
done = '\n'.join(['<div class="ko-emb ko-v ob-in" aria-hidden="true">' + cf + '<span class="ko-halo"></span><span class="ko-disc">' + TICK + '</span></div>',
    H1o % 'Password updated.', SUB % 'You’re all set. Log in with your new password to pick up where you left off.',
    btn('CR-LOG-001.dc.html', 'Log in', '', 'clamp(20px, 3.6vh, 30px)')])
expired = '\n'.join(['<div class="ko-emb ko-a ob-in" aria-hidden="true"><span class="ko-halo"></span><span class="ko-disc">' + CLOCK + '</span></div>',
    H1o % 'This link has expired.', SUB % 'Reset links only work for a short time. Ask for a new one and use it straight away.',
    btn('CR-LOG-002.dc.html', 'Send a new link', '', 'clamp(20px, 3.6vh, 30px)'),
    '<p class="lg-note"><a href="CR-LOG-001.dc.html" class="ob-link">Back to log in</a></p>'])
inner3 = ('<sc-if value="{{isForm}}" hint-placeholder-val="{{true}}">\n%s%s\n</sc-if>\n<sc-if value="{{isDone}}" hint-placeholder-val="{{false}}">\n%s\n</sc-if>\n<sc-if value="{{isExp}}" hint-placeholder-val="{{false}}">\n%s\n</sc-if>'
          % (pwform, btn('CR-LOG-003b.dc.html', 'Save password', 'lg-go'), done, expired))
log3 = (head('CR-LOG-003 · Choose a new password', LG_CSS + KO_CSS + CF_CSS) + ROOT.replace('class="ob-root"', 'class="ob-root {{glow}}"') + '\n'
        + '<div class="lg-glow" aria-hidden="true"></div>\n' + SCENE + HDR + '\n'
        + '<sc-if value="{{isForm}}" hint-placeholder-val="{{true}}">' + track('CR-LOG-002b.dc.html').strip('\n') + '</sc-if>\n'
        + main('{{top}}', 460, inner3) + script(r'''
class Component extends DCLogic {
  constructor(props) { super(props); this.v = (props && props.variant) || 'form'; this.state = { pw: '', pw2: '', show: false }; }
  renderVals() {
    const { pw, pw2, show } = this.state, v = this.v;
    const r = [pw.length >= 8, /\d/.test(pw), /[^A-Za-z0-9]/.test(pw)];
    const n = r.filter(Boolean).length;
    const segC = n === 3 ? '#0F6B45' : '#1652F0';
    const rule = (ok) => ({ c: ok ? '#0F6B45' : '#5B6582', bg: ok ? '#0F6B45' : '#D6DDEE' });
    const match = pw2.length === 0 ? '' : (pw2 === pw ? 'Passwords match.' : 'These don’t match yet.');
    return {
      isForm: v === 'form', isDone: v === 'done', isExp: v === 'expired',
      glow: v === 'done' ? 'lg-ok' : (v === 'expired' ? 'lg-wait' : ''), top: v === 'form' ? 'clamp(140px, 19vh, 176px)' : 'clamp(150px, 22vh, 200px)',
      pw, pw2, pwType: show ? 'text' : 'password', showLabel: show ? 'Hide' : 'Show',
      onPw: (e) => this.setState({ pw: e.target.value }), onPw2: (e) => this.setState({ pw2: e.target.value }),
      toggle: () => this.setState({ show: !show }),
      s1: n >= 1 ? segC : '#E6EAF3', s2: n >= 2 ? segC : '#E6EAF3', s3: n >= 3 ? segC : '#E6EAF3',
      r1: rule(r[0]), r2: rule(r[1]), r3: rule(r[2]),
      matchText: match, pwCls: '', matchColor: pw2 === pw ? '#0F6B45' : '#5B6582'
    };
  }
}'''))

def wrap(name, src, variant, title, mobile):
    hint = '390px,844px' if mobile else '1440px,820px'
    var = ' variant="%s"' % variant if variant else ''
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>%s</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n'
            '<dc-import name="%s"%s hint-size="%s"></dc-import>\n</x-dc>\n</body>\n</html>\n') % (title, src, var, hint)

BOARDS = [  # board, source, variant, title
    ('CR-LOG-001', 'CR-LOG-001', None, 'Log in'),
    ('CR-LOG-001a', 'CR-LOG-001', 'invalid', 'Check your details'),
    ('CR-LOG-001b', 'CR-LOG-001', 'wrong', 'Wrong email or password'),
    ('CR-LOG-001c', 'CR-LOG-001', 'unverified', 'Email not confirmed'),
    ('CR-LOG-001d', 'CR-LOG-001', 'locked', 'Too many attempts'),
    ('CR-LOG-002', 'CR-LOG-002', None, 'Forgot your password'),
    ('CR-LOG-002b', 'CR-LOG-002', 'sent', 'Reset link sent'),
    ('CR-LOG-003', 'CR-LOG-003', None, 'Choose a new password'),
    ('CR-LOG-003b', 'CR-LOG-003', 'done', 'Password updated'),
    ('CR-LOG-003c', 'CR-LOG-003', 'expired', 'Reset link expired'),
]
if __name__ == '__main__':
    out = {'CR-LOG-001.dc.html': log1, 'CR-LOG-002.dc.html': log2, 'CR-LOG-003.dc.html': log3}
    for b, src, var, t in BOARDS:
        if b != src:
            out[b + '.dc.html'] = wrap(b, src, var, '%s · %s' % (b, t), False)
        out[b + '-Mobile.dc.html'] = wrap(b, src, var, '%s · %s · Mobile' % (b, t), True)
    for f, s in out.items():
        open(os.path.join(P, f), 'w').write(s)
    print(len(out), 'files')
