# build52: CRED-002x (CR-CRED-002 variant miss), POL-000 (CR-POL-001 variant none), COL-002a / 002d (CR-COL-002 variants ask / decline),
# COL-002x (CR-COL-004 variant declined: grey standard outcome, no confetti). PATCHES live files. usage: python3 build52.py <dir>
import re, sys, os
P = sys.argv[1]
def rd(f): return open(os.path.join(P, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(P, f), 'w', encoding='utf-8').write(s); OUT.append(f)
OUT = []
def sub(s, a, b, n=1):
    assert s.count(a) >= 1, a[:90]; return s.replace(a, b, n)
def css(s, c):
    i = s.rfind('</style>', 0, s.find('</helmet>')); return s[:i] + c + s[i:]
INFO = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="M12 8v5"></path><path d="M12 16.2v.2"></path></svg>'
ERRCSS = '.kx-err{display:flex;align-items:center;gap:6px;margin:8px 0 0 0;font-size:13.5px;line-height:1.4;color:#B42318}.kx-err svg{flex-shrink:0}\n'
WRAP = rd('CR-KYC-002b.dc.html')
def boards(n, imp, var, title, mob_tpl, mh=844):
    d = WRAP.replace('<dc-import name="CR-KYC-002" variant="photos"', f'<dc-import name="{imp}" variant="{var}"')
    d = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', d); wr(n + '.dc.html', d)
    m = rd(mob_tpl); m = re.sub(f'<dc-import name="{imp}"( variant="[^"]*")?', f'<dc-import name="{imp}" variant="{var}"', m, count=1)
    m = re.sub(r'<title>.*?</title>', f'<title>{n} mobile preview</title>', m)
    m = re.sub(r'height: \d+px; overflow', f'height: {mh}px; overflow', m, count=1); m = re.sub(r'hint-size="390px,\d+px"', f'hint-size="390px,{mh}px"', m)
    m = re.sub(r'"\$preview":\{"width":390,"height":\d+\}', f'"$preview":{{"width":390,"height":{mh}}}', m); wr(n + '-Mobile.dc.html', m)
# ---- CRED-002x: missing required fields (degree form) ----
s = rd('CR-CRED-002.dc.html'); assert 'tE' not in s
tD = re.search(r'<sc-if value="\{\{tD\}\}" hint-placeholder-val="\{\{false\}\}">.*?</sc-if>', s, re.S).group(0)
tE = tD.replace('{{tD}}', '{{tE}}').replace('id="q"', 'id="eq"').replace('for="q"', 'for="eq"').replace('id="fs"', 'id="efs"').replace('for="fs"', 'for="efs"')
tE = tE.replace('id="in"', 'id="ein"').replace('for="in"', 'for="ein"').replace('id="co"', 'id="eco"').replace('for="co"', 'for="eco"').replace('id="yr"', 'id="eyr"').replace('for="yr"', 'for="eyr"')
tE = sub(tE, '<input id="eq" class="cr-in" value="MSc Data Science">', '<input id="eq" class="cr-in cr-bad" value="" placeholder="e.g. MSc Data Science" aria-invalid="true"><p class="kx-err">' + INFO + 'Add the name of your qualification.</p>')
tE = re.sub(r'<button type="button" class="cr-up done">(<span class="cr-ri">)<svg.*?</svg>(</span>)<span><b>msc-certificate\.pdf</b><span>PDF · 1\.2 MB</span></span><em>Replace</em></button>',
            lambda m: '<button type="button" class="cr-up cr-upbad">' + m.group(1) + INFO.replace('15', '18') + m.group(2) + '<span><b>Add your certificate</b><span>PDF, JPG or PNG · up to 10 MB</span></span></button><p class="kx-err">' + INFO + 'We need your certificate to check this.</p>', tE, count=1, flags=re.S)
assert 'cr-upbad' in tE
i = s.index('<div class="cr-vm">'); s = s[:i] + tE + '\n' + s[i:]
s = sub(s, '"fix": {', '"miss": {"h1": "Your degree or diploma", "sub": "Add it as it appears on your certificate.", "ft": "Degree or diploma", "rev": "The Credalio team checks your document. We may contact you or the issuer if something needs confirming."}, "fix": {')
s = sub(s, "t0: !f, tF: f,", "t0: !f, tF: f, tE: t === 'miss',")
s = css(s, '\n/* build52 missing fields */\n' + ERRCSS + '.cr-in.cr-bad{border-color:#D92D20;box-shadow:0 0 0 3px rgba(217,45,32,.10)}\n.cr-up.cr-upbad{border-style:dashed;border-color:#D92D20;background:#FFF8F7}\n.cr-up.cr-upbad .cr-ri{background:#FDECEA;color:#B42318}\n.cr-up.cr-upbad b{color:#B42318}\n')
wr('CR-CRED-002.dc.html', s)
boards('CR-CRED-002x', 'CR-CRED-002', 'miss', 'Credalio · Add a credential: missing details', 'CR-CRED-002-Mobile.dc.html', 1000)
# ---- POL-000: none accepted ----
s = rd('CR-POL-001.dc.html'); assert 'props.variant' not in s
s = sub(s, "constructor(props) { super(props); this.state = { acc: { terms: true, ip: true }, open: 'ai' }; }",
        "constructor(props) { super(props); const none = ((props || {}).variant) === 'none'; this.state = none ? { acc: {}, open: 'terms' } : { acc: { terms: true, ip: true }, open: 'ai' }; }")
wr('CR-POL-001.dc.html', s)
boards('CR-POL-000', 'CR-POL-001', 'none', 'Credalio · Creator policies', 'CR-POL-001-Mobile.dc.html', 900)
# ---- COL-002a / 002d ----
s = rd('CR-COL-002.dc.html')
s = sub(s, "ask: false, dec: false, sent: false, declined: false }; }", "ask: v === 'ask', dec: v === 'decline', sent: false, declined: false }; }")
s = sub(s, "const S = this.state, v = S.v, out = {};", "const S = this.state, v = (S.v === 'ask' || S.v === 'decline') ? 'review' : S.v, out = {};")
s = sub(s, '<button type="button" class="ds-ghost cl-sm cl-red" onClick="{{confirmDecline}}">Decline invitation</button>',
        '<a href="CR-COL-002x.dc.html" class="ds-ghost cl-sm cl-red" onClick="{{confirmDecline}}">Decline invitation</a>')
wr('CR-COL-002.dc.html', s)
boards('CR-COL-002a', 'CR-COL-002', 'ask', 'Credalio · Invitation: ask a question', 'CR-COL-002-Mobile.dc.html', 1300)
boards('CR-COL-002d', 'CR-COL-002', 'decline', 'Credalio · Invitation: decline', 'CR-COL-002-Mobile.dc.html', 1300)
# ---- COL-002x: declined outcome (COL-004 variant declined) ----
s = rd('CR-COL-004.dc.html'); assert "'declined'" not in s
X = '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 7l10 10M17 7 7 17"></path></svg>'
s = re.sub(r'(<sc-if value="\{\{v\}\}" hint-placeholder-val="\{\{false\}\}"><svg.*?</svg></sc-if>\n)(</span></div>)', lambda m: m.group(1) + '<sc-if value="{{f}}" hint-placeholder-val="{{false}}">' + X + '</sc-if>\n' + m.group(2), s, count=1, flags=re.S)
assert '{{f}}' in s
s = sub(s, "this.v = 'verified';", "this.v = ((props || {}).variant) === 'declined' ? 'declined' : 'verified';")
s = sub(s, "const T = ['ko-v', 'Joined', 'You’re now a collaborator', 'Chapter 3 is waiting in Assigned to me, and the team knows you’ve joined.'];",
        "const T = v === 'declined' ? ['ko-f', 'Declined', 'You declined the invitation', 'We’ve let Dr. Bola Ade know.'] : ['ko-v', 'Joined', 'You’re now a collaborator', 'Chapter 3 is waiting in Assigned to me, and the team knows you’ve joined.'];")
s = sub(s, "r: v === 'review', v: v === 'verified' };", "r: v === 'review', v: v === 'verified', f: v === 'declined', l1: v === 'declined' ? 'Notifications' : 'Assigned to me', l1h: v === 'declined' ? 'CR-NOT-001.dc.html' : '#' };")
s = sub(s, '<div class="ko-links ob-in4"><a href="#">Assigned to me</a>', '<div class="ko-links ob-in4"><a href="{{l1h}}">{{l1}}</a>')
wr('CR-COL-004.dc.html', s)
boards('CR-COL-002x', 'CR-COL-004', 'declined', 'Credalio · Invitation declined', 'CR-COL-004-Mobile.dc.html', 844)
print('build52 ok'); print(' '.join(OUT))
