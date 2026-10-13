# build51: Link 1 identity + credentials states. PATCHES live CR-KYC-001 (variant err = KYC-001e), CR-KYC-002 (variant photosx = KYC-002e),
# CR-CRED-002 (variants fix / certup / ref = CRED-001r / 002g / 002h). usage: python3 build51.py <dir>
import re, sys, os
P = sys.argv[1]
def rd(f): return open(os.path.join(P, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(P, f), 'w', encoding='utf-8').write(s); OUT.append(f)
OUT = []
def sub(s, a, b, n=1):
    assert s.count(a) >= 1, a[:80]; return s.replace(a, b, n)
def css(s, c):
    i = s.rfind('</style>', 0, s.find('</helmet>')); return s[:i] + c + s[i:]
INFO = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="M12 8v5"></path><path d="M12 16.2v.2"></path></svg>'
ERRCSS = '.kx-err{display:flex;align-items:center;gap:6px;margin:8px 0 0 0;font-size:13.5px;line-height:1.4;color:#B42318}.kx-err svg{flex-shrink:0}\n'
WRAP = rd('CR-KYC-002b.dc.html')
def boards(n, imp, var, title, mob_tpl, mh=844):
    d = WRAP.replace('<dc-import name="CR-KYC-002" variant="photos"', f'<dc-import name="{imp}" variant="{var}"')
    d = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', d); wr(n + '.dc.html', d)
    m = rd(mob_tpl).replace(f'<dc-import name="{imp}"', f'<dc-import name="{imp}" variant="{var}"', 1)
    assert f'variant="{var}"' in m
    m = re.sub(r'<title>.*?</title>', f'<title>{n} mobile preview</title>', m)
    m = re.sub(r'height: \d+px; overflow', f'height: {mh}px; overflow', m, count=1); m = re.sub(r'hint-size="390px,\d+px"', f'hint-size="390px,{mh}px"', m)
    m = re.sub(r'"\$preview":\{"width":390,"height":\d+\}', f'"$preview":{{"width":390,"height":{mh}}}', m); wr(n + '-Mobile.dc.html', m)
# ---- KYC-001e: consent not given ----
s = rd('CR-KYC-001.dc.html'); assert 'kx-err' not in s
s = sub(s, "constructor(props) { super(props); this.state = { ok: false }; }",
        "constructor(props) { super(props); this.state = { ok: false, err: ((props || {}).variant) === 'err' }; }")
s = sub(s, "return { ckCls: ok ? 'tk-on' : '', goCls: ok ? '' : 'lp-off',",
        "const err = this.state.err && !ok; return { showErr: err, ckCls: ok ? 'tk-on' : (err ? 'tk-bad' : ''), goCls: (ok || err) ? '' : 'lp-off',")
s = sub(s, "this.setState({ ok: !ok }); } }; }", "this.setState({ ok: !ok }); } }; }")
i = s.index('<label class="tk-check {{ckCls}}"'); j = s.index('</label>', i) + 8
s = s[:j] + '<sc-if value="{{showErr}}" hint-placeholder-val="{{false}}"><p class="kx-err" role="alert">' + INFO + 'Tick the box so Sumsub can check your ID.</p></sc-if>' + s[j:]
s = css(s, '\n/* build51 consent error */\n' + ERRCSS + '.tk-check.tk-bad .tk-box{border-color:#D92D20;box-shadow:0 0 0 3px rgba(217,45,32,.12)}\n.k1-card .kx-err{margin:-6px 0 4px 32px}\n')
wr('CR-KYC-001.dc.html', s)
boards('CR-KYC-001e', 'CR-KYC-001', 'err', 'Credalio · Verify your identity: consent needed', 'CR-KYC-001-Mobile.dc.html')
# ---- KYC-002e: back photo missing ----
s = rd('CR-KYC-002.dc.html'); assert 'kx-err' not in s
s = sub(s, "const step = v === 'review' ? 3 : (v === 'liveness' ? 2 : (v === 'photos' ? 1 : 0));",
        "const step = v === 'review' ? 3 : (v === 'liveness' ? 2 : ((v === 'photos' || v === 'photosx') ? 1 : 0));")
s = sub(s, "this.state = { step, doc: step > 0 ? 1 : -1, f: step > 0, b: step > 1, live: step > 2 };",
        "this.state = { step, doc: step > 0 ? 1 : -1, f: step > 0, b: step > 1, live: step > 2, perr: v === 'photosx' };")
s = sub(s, "const { step, doc, f, b, live } = this.state;", "const { step, doc, f, b, live, perr } = this.state; const bErr = perr && step === 1 && !b;")
s = sub(s, "bCls: b ? 'k2-upd' : '',", "bErr, bCls: b ? 'k2-upd' : (bErr ? 'k2-bad' : ''),")
s = sub(s, "</div>\n<div class=\"k2-qr\">", "</div>\n<sc-if value=\"{{bErr}}\" hint-placeholder-val=\"{{false}}\"><p class=\"kx-err\" role=\"alert\">" + INFO + "Add a photo of the back of your ID to continue.</p></sc-if>\n<div class=\"k2-qr\">")
s = css(s, '\n/* build51 photo error */\n' + ERRCSS + '.k2-up.k2-bad{border-color:#D92D20;border-style:dashed;background:#FFF8F7}\n.k2-up.k2-bad b{color:#B42318}\n')
wr('CR-KYC-002.dc.html', s)
boards('CR-KYC-002e', 'CR-KYC-002', 'photosx', 'Credalio · Verify your identity: photo missing', 'CR-KYC-002-Mobile.dc.html')
# ---- CRED-002: fix / certup / ref ----
s = rd('CR-CRED-002.dc.html'); assert 'tX' not in s
tA = re.search(r'<sc-if value="\{\{tA\}\}" hint-placeholder-val="\{\{false\}\}">.*?</sc-if>', s, re.S).group(0)
SEL = re.search(r'<div class="ob-sel"><select id="is" class="ob-f"><option selected>Amazon Web Services \(AWS\)</option></select>(<svg.*?</svg>)</div>', tA, re.S).group(1)
SEG = re.search(r'<div class="cr-seg" role="radiogroup".*?</div>', tA, re.S).group(0)
DONE = re.search(r'<button type="button" class="cr-up done">.*?</button>', s, re.S).group(0)
def sel(i, label, val): return f'<div class="cr-f s4"><label class="ob-lab" for="{i}">{label}</label><div class="ob-sel"><select id="{i}" class="ob-f"><option selected>{val}</option></select>{SEL}</div></div>'
def seg_upload():
    g = SEG.replace('aria-checked="{{idOn}}" class="cr-o {{idCls}}" onClick="{{toId}}"', 'aria-checked="false" class="cr-o"')
    g = g.replace('aria-checked="{{lkOn}}" class="cr-o {{lkCls}}" onClick="{{toLink}}"', 'aria-checked="false" class="cr-o"')
    g = g.replace('<button type="button" role="radio" aria-checked="false" class="cr-o"><svg', '<button type="button" role="radio" aria-checked="true" class="cr-o on"><svg', 1) if False else g
    k = g.rfind('aria-checked="false" class="cr-o"'); return g[:k] + 'aria-checked="true" class="cr-o on"' + g[k + len('aria-checked="false" class="cr-o"'):]
def upl(name, meta, cls='done', act='Replace'):
    u = re.sub(r'<b>[^<]*</b><span>[^<]*</span>', f'<b>{name}</b><span>{meta}</span>', DONE, count=1)
    u = u.replace('<em>Replace</em>', f'<em>{act}</em>').replace('class="cr-up done"', f'class="cr-up {cls}"')
    if cls == 'bad': u = re.sub(r'(<span class="cr-ri">)<svg.*?</svg>', lambda m: m.group(1) + INFO.replace('15', '18'), u, count=1, flags=re.S)
    return u
def inp(i, label, val, cls='s1 s1m', extra=''): return f'<div class="cr-f {cls}"><label class="ob-lab" for="{i}">{label}</label><input id="{i}" class="cr-in{extra}" value="{val}"></div>'
FIX = ('<sc-if value="{{tX}}" hint-placeholder-val="{{false}}"><div class="cr-form">' + sel('xi', 'Issuer', 'Google') + sel('xc', 'Certification', 'Google Data Analytics Certificate')
       + '<div class="cr-f s4"><span class="ob-lab">How should we verify it?</span>' + seg_upload() + '</div>'
       + '<div class="cr-f s4"><span class="ob-lab">Certificate</span>' + upl('google-certificate.jpg', 'Too blurry to read', 'bad', 'Replace') + '</div>'
       + inp('x1', 'Issue date', 'Aug 2021') + inp('x2', 'Expiry date <em>(optional)</em>', 'No expiry') + '</div></sc-if>')
CUP = ('<sc-if value="{{tG}}" hint-placeholder-val="{{false}}"><div class="cr-form">' + sel('gi', 'Issuer', 'Tableau (Salesforce)') + sel('gc', 'Certification', 'Tableau Desktop Specialist')
       + '<div class="cr-f s4"><span class="ob-lab">How should we verify it?</span>' + seg_upload() + '</div>'
       + '<div class="cr-f s4"><span class="ob-lab">Certificate</span>' + upl('tableau-certificate.pdf', 'PDF · 640 KB') + '</div>'
       + inp('g1', 'Issue date', 'Nov 2023') + inp('g2', 'Expiry date <em>(optional)</em>', 'No expiry') + '</div></sc-if>')
REF = ('<sc-if value="{{tR}}" hint-placeholder-val="{{false}}"><div class="cr-form">' + inp('rt', 'Job title', 'Senior Data Analyst', 's2') + inp('ro', 'Organization', 'Flutterwave', 's2')
       + inp('r1', 'From', 'Jan 2018') + inp('r2', 'To', 'Feb 2020')
       + '<div class="cr-f s4"><span class="ob-lab">How should we confirm it?</span><div class="cr-seg k2s" role="radiogroup" aria-label="How should we confirm it?">'
       + '<button type="button" role="radio" aria-checked="false" class="cr-o"><span>Upload a document</span><span class="cr-ok">' + re.search(r'<span class="cr-ok">(<svg.*?</svg>)</span>', SEG, re.S).group(1) + '</span></button>'
       + '<button type="button" role="radio" aria-checked="true" class="cr-o on"><span>Ask a referee</span><span class="cr-ok">' + re.search(r'<span class="cr-ok">(<svg.*?</svg>)</span>', SEG, re.S).group(1) + '</span></button></div></div>'
       + inp('rn', 'Referee name', 'Amaka Eze', 's2') + inp('rr', 'Their role', 'Head of Data, Flutterwave', 's2')
       + '<div class="cr-f s4"><label class="ob-lab" for="re">Referee email</label><input id="re" class="cr-in" value="amaka.eze@flutterwave.com"><p class="cr-hint">We send them one short email to confirm this role.</p></div></div></sc-if>')
i = s.index('<div class="cr-vm">'); s = s[:i] + FIX + '\n' + CUP + '\n' + REF + '\n' + s[i:]
s = sub(s, '<sc-if value="{{tF}}" hint-placeholder-val="{{false}}"><span class="lp-eb ob-in">Add a credential</span></sc-if>',
        '<sc-if value="{{eb}}" hint-placeholder-val="{{false}}"><span class="lp-eb ob-in">Add a credential</span></sc-if>')
s = sub(s, '"other": {"h1": "Your other evidence",',
        '"fix": {"h1": "Fix your Google certificate", "sub": "We couldn’t read your scan. Upload a clearer copy, or switch to the credential ID.", "ft": "Professional certification", "rev": "The Credalio team checks your new copy."}, '
        '"certup": {"h1": "Your certification", "sub": "Tell us the issuer and how we can check it.", "ft": "Professional certification", "rev": "The Credalio team checks your certificate."}, '
        '"ref": {"h1": "Your work experience", "sub": "Tell us about a role that shows your expertise.", "ft": "Work experience", "rev": "The Credalio team confirms the role with your referee."}, '
        '"other": {"h1": "Your other evidence",')
s = sub(s, "t0: !f, tF: f,", "t0: !f, tF: f, eb: f && t !== 'fix', tX: t === 'fix', tG: t === 'certup', tR: t === 'ref',")
s = sub(s, "backL: f ? 'Change type' : 'Your credentials',", "backL: (f && t !== 'fix') ? 'Change type' : 'Your credentials',")
s = sub(s, "back: () => { if (f) this.setState({ t: 'types' });", "back: () => { if (f && t !== 'fix') this.setState({ t: 'types' });")
s = sub(s, "goL: 'Submit',", "goL: t === 'fix' ? 'Resubmit' : 'Submit',")
s = css(s, '\n/* build51 credential states */\n.cr-up.bad{border-style:solid;border-color:#F0C774;background:#FFFBF2}\n.cr-up.bad .cr-ri{background:#FFF1D6;color:#8A5300}\n.cr-up.bad > span > span{color:#8A5300}\n.cr-up.bad em{margin-left:auto;font-style:normal;font-size:13px;font-weight:600;color:#1652F0}\n.cr-seg.k2s{grid-template-columns:repeat(2,minmax(0,1fr))}\n.cr-seg.k2s .cr-o:nth-child(2){grid-column:auto;order:0}\n')
wr('CR-CRED-002.dc.html', s)
for n, v, t in [('CR-CRED-001r', 'fix', 'Fix a credential'), ('CR-CRED-002g', 'certup', 'Certification by upload'), ('CR-CRED-002h', 'ref', 'Work experience with referee')]:
    boards(n, 'CR-CRED-002', v, 'Credalio · ' + t, 'CR-CRED-002-Mobile.dc.html', 1000)
print('build51 ok'); print(' '.join(OUT))
