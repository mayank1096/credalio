# build39: onboarding error / edge states (Link 1). PATCHES live CR-ONB-003 (variants invalid / change = ONB-003e / ONB-003d),
# CR-ONB-003c (variant weak = ONB-003ce), CR-ONB-004 (variant err = ONB-004e), CR-ONB-005 (variant err = ONB-005e);
# writes desktop + mobile wrappers. Asserts if already patched. usage: python3 build39.py <dir>  (scratch copy; copy back printed files)
import re, sys, os
P = sys.argv[1]
def rd(f): return open(os.path.join(P, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(P, f), 'w', encoding='utf-8').write(s)
OUT = []
BANG = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<circle cx="12" cy="12" r="9"></circle><path d="M12 7.5v5.5"></path><path d="M12 16.4v.2"></path></svg>')
ERR_CSS = """
/* build39 field errors */
.ob-bad,.ob-bad:focus{border-color:#D92D20 !important;box-shadow:0 0 0 4px rgba(217,45,32,.08) !important}
.ob-err{display:flex;align-items:center;gap:6px;margin:8px 0 0 2px;font-size:13.5px;line-height:1.4;color:#B42318;text-align:left}
.ob-err svg{flex-shrink:0}
.ob-grid2 .ob-err{margin-top:6px;font-size:13px}
"""
def err(cond, text, extra=''):
    return f'<sc-if value="{{{{{cond}}}}}" hint-placeholder-val="{{{{false}}}}"><span class="ob-err" role="alert"{extra}>{BANG}{text}</span></sc-if>'
def add_css(s):
    i = s.index('</style>'); return s[:i] + ERR_CSS + s[i:]
def sub1(s, a, b):
    assert s.count(a) == 1, a[:80]; return s.replace(a, b, 1)
def set_rv(s, code):
    m = re.search(r'renderVals\(\) \{ return \{\}; \}', s)
    if m: return s[:m.start()] + 'renderVals() {\n    const v = (this.props && this.props.variant) || \'\';\n    ' + code + '\n  }' + s[m.end():]
    raise AssertionError('renderVals')
def wrap(src, n, var, hm):
    d = rd('CR-SET-001.dc.html').replace('<dc-import name="CR-SET" variant="account"', f'<dc-import name="{src}" variant="{var}"').replace('CR-SET-001', n)
    wr(n + '.dc.html', d); OUT.append(n + '.dc.html')
    m = rd(src + '-Mobile.dc.html').replace(f'<dc-import name="{src}"', f'<dc-import name="{src}" variant="{var}"').replace(f'{src} mobile', f'{n} mobile')
    m = re.sub(r'height: \d+px; overflow', f'height: {hm}px; overflow', m, count=1)
    m = re.sub(r'hint-size="390px,\d+px"', f'hint-size="390px,{hm}px"', m)
    m = re.sub(r'"\$preview":\{"width":390,"height":\d+\}', f'"$preview":{{"width":390,"height":{hm}}}', m)
    wr(n + '-Mobile.dc.html', m); OUT.append(n + '-Mobile.dc.html')

# ---------- CR-ONB-003 · invalid / change ----------
s = rd('CR-ONB-003.dc.html')
assert 'build39' not in s, 'CR-ONB-003 already patched'
s = add_css(s)
s = sub1(s, '>Let’s save your place.</h1>', '>{{h1}}</h1>')
s = sub1(s, '>Start turning what you know into learning others can use.</p>', '>{{sub}}</p>')
s = sub1(s, '<a href="CR-ONB-002.dc.html" class="ob-ghost ob-back"', '<a href="{{backHref}}" class="ob-ghost ob-back"')
s = sub1(s, '<input id="ob-email" class="ob-input" type="email"', '<input id="ob-email" class="ob-input {{emCls}}" type="email" value="{{em}}" aria-invalid="{{emInv}}"')
a = 'class="ob-btn" style="margin-top: 0; display: flex; align-items: center; gap: 16px; height: 56px; padding: 0 6px 0 28px; box-sizing: border-box; border-radius: 999px; background: #1652F0; color: #FFFFFF; font-size: 16px; font-weight: 600; letter-spacing: -0.005em; text-decoration: none; white-space: nowrap; box-shadow: 0 1px 0 rgba(255, 255, 255, 0.25) inset, 0 12px 28px rgba(22, 82, 240, 0.28)">Continue with Email<span'
s = sub1(s, a, a.replace('>Continue with Email<span', '>{{btn}}<span'))
# error line right under the email row; social + terms hidden when changing the email
i = s.index('<div aria-hidden="true" style="width: 100%; margin: clamp(14px, 2.6vh, 20px) 0;')
j = s.index('</p>', s.index('Privacy Policy</a>', i)) + 4
s = s[:i] + '<sc-if value="{{full}}" hint-placeholder-val="{{true}}">' + s[i:j] + '</sc-if>' + s[j:]
# error sits inside the row: under both on desktop (wraps), between field and button on mobile
a = 'placeholder="Your email address" style="flex-grow: 1; min-width: 0; height: 56px; box-sizing: border-box; padding: 0 22px; border-radius: 999px; border: 1.5px solid #D6DDEE; background: #FFFFFF; font-family: inherit; font-size: 16px; color: #0B1433; outline: none">'
s = sub1(s, a, a + err('bad', 'Enter a valid email address.'))
s = sub1(s, '<div class="ob-row ob-in3" style="margin-top: clamp(22px, 4vh, 36px); width: 100%; display: flex; align-items: center; gap: 10px">',
         '<div class="ob-row ob-in3" style="margin-top: clamp(22px, 4vh, 36px); width: 100%; display: flex; flex-wrap: wrap; align-items: center; gap: 10px">')
s = s.replace('/* build39 field errors */', '''/* build39 field errors */
.ob-row > .ob-err{order:3;flex-basis:100%;margin:0 0 0 22px}
@media (max-width: 960px){.ob-row > input{order:1}.ob-row > .ob-err{order:2;margin:-2px 0 4px 18px}.ob-row > a{order:3}.ob-sub{width:auto !important}}''', 1)
# subtitle is not a heading: it used the ob-h1 class and became 30px on mobile
s = sub1(s, '<p class="ob-in2 ob-h1" style="margin: 12px 0 0 0; width: max-content;', '<p class="ob-in2 ob-sub" style="margin: 12px 0 0 0; width: max-content;')
s = set_rv(s, """const ch = v === 'change', bad = v === 'invalid';
    return { h1: ch ? 'Change your email.' : 'Let’s save your place.',
      sub: ch ? 'We’ll send a new link to the right address. The old one stops working.' : 'Start turning what you know into learning others can use.',
      btn: ch ? 'Send new link' : 'Continue with Email', backHref: ch ? 'CR-ONB-003b.dc.html' : 'CR-ONB-002.dc.html',
      em: ch ? 'ada.ononuju@gmail.com' : (bad ? 'ada.ononuju@example' : ''), emCls: bad ? 'ob-bad' : '', emInv: bad ? 'true' : 'false', bad, full: !ch };""")
wr('CR-ONB-003.dc.html', s); OUT.append('CR-ONB-003.dc.html')
wrap('CR-ONB-003', 'CR-ONB-003e', 'invalid', 1010)
wrap('CR-ONB-003', 'CR-ONB-003d', 'change', 980)
# 003b "This isn't my email" now goes to the change screen
b = rd('CR-ONB-003b.dc.html')
b = sub1(b, '<a href="CR-ONB-003.dc.html" class="ob-link" style="font-weight: 600">This isn’t my email</a>', '<a href="CR-ONB-003d.dc.html" class="ob-link" style="font-weight: 600">This isn’t my email</a>')
wr('CR-ONB-003b.dc.html', b); OUT.append('CR-ONB-003b.dc.html')

# ---------- CR-ONB-003c · weak ----------
s = rd('CR-ONB-003c.dc.html')
assert 'build39' not in s, 'CR-ONB-003c already patched'
s = add_css(s)
s = sub1(s, '<input id="pw" class="ob-f" type="{{pwType}}"', '<input id="pw" class="ob-f {{pwCls}}" type="{{pwType}}"')
s = sub1(s, "constructor(props) { super(props); this.state = { pw: '', pw2: '', show: false }; }",
         "constructor(props) { super(props); this.weak = !!(props && props.variant === 'weak'); this.state = { pw: this.weak ? 'sunshine' : '', pw2: '', show: false }; }")
s = sub1(s, "const rule = (ok) => ({ c: ok ? '#0F6B45' : '#5B6582', bg: ok ? '#0F6B45' : '#D6DDEE' });",
         "const W = this.weak && n < 3;\n    const rule = (ok) => ({ c: ok ? '#0F6B45' : (W ? '#B42318' : '#5B6582'), bg: ok ? '#0F6B45' : (W ? '#D92D20' : '#D6DDEE') });")
s = sub1(s, "matchText: match,", "matchText: match, pwCls: W ? 'ob-bad' : '', weak: W,")
s = sub1(s, "const segC = n === 3 ? '#0F6B45' : '#1652F0';", "const segC = n === 3 ? '#0F6B45' : (this.weak ? '#D92D20' : '#1652F0');")
# error line after the rules row (rules already say what is missing, so the message stays short)
i = s.index('<div role="status"'); j = s.index('</div>', i) + 6
s = s[:j] + err('weak', 'Add a number and a symbol to make it stronger.') + s[j:]
wr('CR-ONB-003c.dc.html', s); OUT.append('CR-ONB-003c.dc.html')
wrap('CR-ONB-003c', 'CR-ONB-003ce', 'weak', 880)

# ---------- CR-ONB-004 · missing display name ----------
s = rd('CR-ONB-004.dc.html')
assert 'build39' not in s, 'CR-ONB-004 already patched'
s = add_css(s)
s = sub1(s, '<input id="fn" class="ob-f" type="text" placeholder="Ada"', '<input id="fn" class="ob-f" type="text" placeholder="Ada" value="{{fn}}"')
s = sub1(s, '<input id="ln" class="ob-f" type="text" placeholder="Ononuju"', '<input id="ln" class="ob-f" type="text" placeholder="Ononuju" value="{{ln}}"')
s = sub1(s, '<input id="dn" class="ob-f" type="text" placeholder="Ada O."><span class="ob-help">Learners will see this name.</span>',
         '<input id="dn" class="ob-f {{dnCls}}" type="text" placeholder="Ada O." aria-invalid="{{dnInv}}">'
         '<sc-if value="{{ok}}" hint-placeholder-val="{{true}}"><span class="ob-help">Learners will see this name.</span></sc-if>' + err('e', 'Add the name learners will see.'))
s = set_rv(s, "const e = v === 'err';\n    return { e, ok: !e, fn: e ? 'Ada' : '', ln: e ? 'Ononuju' : '', dnCls: e ? 'ob-bad' : '', dnInv: e ? 'true' : 'false' };")
wr('CR-ONB-004.dc.html', s); OUT.append('CR-ONB-004.dc.html')
wrap('CR-ONB-004', 'CR-ONB-004e', 'err', 1110)

# ---------- CR-ONB-005 · missing required fields ----------
s = rd('CR-ONB-005.dc.html')
assert 'build39' not in s, 'CR-ONB-005 already patched'
s = add_css(s)
s = sub1(s, '<select id="ind" class="ob-f"><option>Choose an industry</option><option selected>Technology</option>',
         '<select id="ind" class="ob-f {{indCls}}" aria-invalid="{{inv}}" value="{{indV}}"><option>Choose an industry</option><option>Technology</option>')
i = s.index('<select id="ind"'); j = s.index('</div></div>', i) + 6
s = s[:j] + err('e', 'Choose your industry.') + s[j:]
s = sub1(s, '<input id="dom" class="ob-f" type="text" placeholder="e.g. Data &amp; Analytics" value="Data &amp; Analytics">',
         '<input id="dom" class="ob-f {{domCls}}" type="text" placeholder="e.g. Data &amp; Analytics" value="{{dom}}" aria-invalid="{{inv}}">' + err('e', 'Add your main area of expertise.'))
s = sub1(s, "    return { exp };", "    const e = (this.props && this.props.variant) === 'err';\n    return { exp, e, ok: !e, inv: e ? 'true' : 'false', indCls: e ? 'ob-bad' : '', domCls: e ? 'ob-bad' : '', dom: e ? '' : 'Data & Analytics', indV: e ? 'Choose an industry' : 'Technology' };")
wr('CR-ONB-005.dc.html', s); OUT.append('CR-ONB-005.dc.html')
wrap('CR-ONB-005', 'CR-ONB-005e', 'err', 990)
print('build39 ok'); print(' '.join(OUT))
