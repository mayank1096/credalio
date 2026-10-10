# build15: CRED-002d/e/f (licence / work / other evidence) as new variants of CR-CRED-002,
# and CR-CRED-003 outcome (variants verified = 003, review = 003b), modelled on CR-KYC-003.
# Patches the live canvas CR-CRED-002 in place (keeps client copy + later fixes); only writes its own new files.
# usage: python3 build15.py <canvas project dir>
import re, sys, os, json
P = sys.argv[1]
rd = lambda f: open(os.path.join(P, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(P, f), 'w', encoding='utf-8').write(s)

s = rd('CR-CRED-002.dc.html')
assert '{{tL}}' not in s, 'already patched'

# ---------- snippets reused from the existing file ----------
i = s.index('<ul class="cr-types">'); j = s.index('</ul>', i)
TI = [x.replace('width="22" height="22"', 'width="20" height="20"') for x in re.findall(r'<span class="cr-ri">(<svg.*?</svg>)</span>', s[i:j], flags=re.S)]
CHEV = re.search(r'<div class="ob-sel"><select[^>]*>.*?</select>(<svg.*?</svg>)</div>', s, flags=re.S).group(1)
LINK = re.search(r'<div class="cr-ico">(<svg.*?</svg>)', s, flags=re.S).group(1)
OK = re.search(r'<span class="cr-ok">(<svg.*?</svg>)</span>', s, flags=re.S).group(1)
UPD = re.search(r'<button type="button" class="cr-up done"><span class="cr-ri">(<svg.*?</svg>)</span>', s, flags=re.S).group(1)
UPE = re.search(r'<button type="button" class="cr-up"><span class="cr-ri">(<svg.*?</svg>)</span>', s, flags=re.S).group(1)

def lab(t, fid=''):
    t = t.replace('(optional)', '<em>(optional)</em>')
    return f'<label class="ob-lab" for="{fid}">{t}</label>' if fid else f'<span class="ob-lab">{t}</span>'
def IN(label, val, sp, fid, hint='', mono=False):
    h = f'<p class="cr-hint">{hint}</p>' if hint else ''
    return f'<div class="cr-f {sp}">{lab(label, fid)}<input id="{fid}" class="cr-in{" mono" if mono else ""}" value="{val}">{h}</div>'
def SEL(label, val, sp, fid):
    return f'<div class="cr-f {sp}">{lab(label, fid)}<div class="ob-sel"><select id="{fid}" class="ob-f"><option selected>{val}</option></select>{CHEV}</div></div>'
def LNK(label, val, sp, fid, hint=''):
    h = f'<p class="cr-hint">{hint}</p>' if hint else ''
    return f'<div class="cr-f {sp}">{lab(label, fid)}<div class="cr-ico">{LINK}<input id="{fid}" class="cr-in" value="{val}"></div>{h}</div>'
def TA(label, val, sp, fid, hint=''):
    h = f'<p class="cr-hint">{hint}</p>' if hint else ''
    return f'<div class="cr-f {sp}">{lab(label, fid)}<textarea id="{fid}" class="cr-in cr-ta" rows="3">{val}</textarea>{h}</div>'
def UP(label, done, name, meta, sp='s4'):
    if done:
        return f'<div class="cr-f {sp}">{lab(label)}<button type="button" class="cr-up done"><span class="cr-ri">{UPD}</span><span><b>{name}</b><span>{meta}</span></span><em>Replace</em></button></div>'
    return f'<div class="cr-f {sp}">{lab(label)}<button type="button" class="cr-up"><span class="cr-ri">{UPE}</span><span><b>{name}</b><span>{meta}</span></span></button></div>'
def SEG(label, opts, on):
    b = ''.join(f'<button type="button" role="radio" aria-checked="{"true" if o == on else "false"}" class="cr-o{" on" if o == on else ""}"><span>{o}</span><span class="cr-ok">{OK}</span></button>' for o in opts)
    return f'<div class="cr-f s4">{lab(label)}<div class="cr-seg k4" role="radiogroup" aria-label="{label}">{b}</div></div>'

LIC = (SEL('Professional body', 'Nigeria Computer Society (NCS)', 's4', 'lb')
       + SEL('Membership grade', 'Member (MNCS)', 's2', 'lg') + IN('Membership number', 'NCS/M/04217', 's2', 'ln', mono=True)
       + LNK('Public register link (optional)', 'ncs.org.ng/members/verify', 's2', 'lr', 'If your body has an online register, the review is quicker.')
       + IN('Member since', '2019', 's1 s1m', 'l1') + IN('Valid until (optional)', 'Dec 2026', 's1 s1m', 'l2')
       + UP('Proof of membership', True, 'ncs-membership.pdf', 'PDF · 840 KB'))
WORK = (IN('Job title', 'Lead Data Scientist', 's2', 'wt') + IN('Organisation', 'Paystack', 's2', 'wo')
        + IN('From', 'Mar 2020', 's1 s1m', 'w1') + IN('To', 'Present', 's1 s1m', 'w2')
        + IN('Referee email (optional)', 'tunde.bello@paystack.com', 's2', 'wr', 'We only contact them if something needs confirming.')
        + TA('What did you do?', 'Led a team of four building fraud models that screen 40 million payments a month.', 's4', 'wd')
        + UP('Proof of role', True, 'reference-letter.pdf', 'PDF · 320 KB'))
OTHER = (SEG('What kind of evidence?', ['Portfolio', 'Publication', 'Talk', 'Award'], 'Publication')
         + IN('Title', 'Forecasting market demand with satellite data', 's4', 'ot')
         + LNK('Link', 'doi.org/10.1016/j.dss.2024.11402', 's2', 'ol', 'A DOI, article page or portfolio link.')
         + IN('Year', '2024', 's1 s1m', 'oy') + SEL('Your role', 'Lead author', 's1 s1m', 'or')
         + UP('File (optional)', False, 'Add a file', 'PDF, JPG or PNG · up to 10 MB'))

blk = lambda v, body: f'<sc-if value="{{{{{v}}}}}" hint-placeholder-val="{{{{false}}}}"><div class="cr-form">{body}</div></sc-if>'
anchor = '\n<div class="cr-vm">'
assert s.count(anchor) == 1
s = s.replace(anchor, '\n' + blk('tL', LIC) + '\n' + blk('tW', WORK) + '\n' + blk('tO', OTHER) + anchor)

# form header icon per type
old_ic = re.search(r'<div class="cr-fh"><span class="cr-ri">.*?</span><b>', s, flags=re.S).group(0)
ic = ''.join(f'<sc-if value="{{{{{v}}}}}" hint-placeholder-val="{{{{false}}}}">{TI[k]}</sc-if>' for v, k in [('tD', 0), ('tC', 1), ('tL', 2), ('tW', 3), ('tO', 4)])
s = s.replace(old_ic, f'<div class="cr-fh"><span class="cr-ri">{ic}</span><b>')

# "Reviewed by the Credalio Trust team" box: all manual types, text per type
REV_OLD = '<sc-if value="{{tD}}" hint-placeholder-val="{{false}}"><div class="cr-v"><span class="cr-vi">'
assert s.count(REV_OLD) == 2
s = s.replace(REV_OLD, '<sc-if value="{{tM}}" hint-placeholder-val="{{false}}"><div class="cr-v"><span class="cr-vi">')
s = s.replace('<span>A reviewer checks your document. We may contact you or the issuer if something needs confirming.</span>', '<span>{{revTxt}}</span>')

# logic
s = s.replace("tD: t === 'degree', tA:", "tD: t === 'degree', tL: t === 'lic', tW: t === 'work', tO: t === 'other', tM: !cert && f, tA:")
s = s.replace("h1: !f ? 'Add a credential' : (t === 'degree' ? 'Your degree or diploma' : 'Your certification'),",
              "h1: !f ? 'Add a credential' : M.h1,")
s = s.replace("sub: !f ? 'Choose what you’re adding. The form changes to ask only for what that type needs.' : (t === 'degree' ? 'Add it as it appears on your certificate.' : 'Tell us the issuer and how we can check it.'),",
              "sub: !f ? 'Choose what you’re adding. The form changes to ask only for what that type needs.' : M.sub, revTxt: M.rev || '',")
s = s.replace("fTitle: t === 'degree' ? 'Degree or diploma' : 'Professional certification',", "fTitle: M.ft || '',")
s = s.replace("p_lic: () => {}, p_work: () => {}, p_other: () => {}", "p_lic: go('lic'), p_work: go('work'), p_other: go('other')")
CERT = {'h1': 'Your certification', 'sub': 'Tell us the issuer and how we can check it.', 'ft': 'Professional certification'}
MAP = {
  'degree': {'h1': 'Your degree or diploma', 'sub': 'Add it as it appears on your certificate.', 'ft': 'Degree or diploma',
             'rev': 'A reviewer checks your document. We may contact you or the issuer if something needs confirming.'},
  'aws': CERT, 'badge': CERT,
  'lic': {'h1': 'Your licence or membership', 'sub': 'Add it as it appears on your membership certificate.', 'ft': 'Licence or membership',
          'rev': 'A reviewer checks your proof, and the body’s public register where there is one.'},
  'work': {'h1': 'Your work experience', 'sub': 'Tell us about a role that shows your expertise.', 'ft': 'Work experience',
           'rev': 'A reviewer checks your proof of role. Your referee is only contacted if something needs confirming.'},
  'other': {'h1': 'Your other evidence', 'sub': 'Share work that shows what you know.', 'ft': 'Other evidence',
            'rev': 'A reviewer looks at your work and how it supports your expertise.'},
}
s = s.replace("    const go = (x) => () => this.setState({ t: x });",
              "    const go = (x) => () => this.setState({ t: x });\n    const M = (" + json.dumps(MAP, ensure_ascii=False) + ")[t] || {};")
for k in ['tL: t', 'M.h1', 'M.sub', 'M.ft', "go('lic')", 'const M =']:
    assert k in s, k

CSS = '''
/* build15: textarea + 4-up evidence chips */
.cr-ta{height:auto;min-height:76px;padding:12px 16px;line-height:1.45;resize:none;display:block}
.cr-seg.k4 .cr-o:nth-child(2){grid-column:auto;order:0}
@media (min-width: 961px){.cr-seg.k4{grid-template-columns:repeat(4,minmax(0,1fr))}}
.cr-seg.k4 .cr-o{justify-content:center}
.cr-seg.k4 .cr-o .cr-ok{margin-left:0}
'''
s = s.replace('</style>', CSS + '</style>', 1)
wr('CR-CRED-002.dc.html', s)

# ---------- variant wrappers 002d/e/f ----------
wd = rd('CR-CRED-002c.dc.html'); wm = rd('CR-CRED-002c-Mobile.dc.html')
for n, v, title in [('CR-CRED-002d', 'lic', 'licence or membership'), ('CR-CRED-002e', 'work', 'work experience'), ('CR-CRED-002f', 'other', 'other evidence')]:
    wr(n + '.dc.html', wd.replace('variant="badge"', f'variant="{v}"').replace('certification by badge link', title))
    wr(n + '-Mobile.dc.html', wm.replace('variant="badge"', f'variant="{v}"').replace('CR-CRED-002c', n))

# ---------- CR-CRED-003 outcome (from CR-KYC-003) ----------
k = rd('CR-KYC-003.dc.html')
body_a = k.index('<sc-if value="{{a}}" hint-placeholder-val="{{false}}">\n<section'); body_end = k.index('<div class="ko-links')
k = k[:body_a] + k[body_end:]
k = k.replace('<span class="lp-t1">Verify your identity</span><span class="lp-t2">Readiness · task 1 of 5</span>',
              '<span class="lp-t1">Credentials &amp; expertise</span><span class="lp-t2">Readiness · task 2 of 5</span>')
# disc icons: drop action / failed
k = re.sub(r'<sc-if value="\{\{a\}\}" hint-placeholder-val="\{\{false\}\}"><svg.*?</svg></sc-if>\n', '', k, flags=re.S)
k = re.sub(r'<sc-if value="\{\{f\}\}" hint-placeholder-val="\{\{false\}\}"><svg.*?</svg></sc-if>\n', '', k, flags=re.S)
# review path
k = k.replace('<b>Submitted to Sumsub</b><span>Today, 10:42</span>', '<b>Submitted</b><span>Today, 10:42</span>')
k = k.replace('<b>Sumsub checks your ID</b><span>Usually a few minutes, at most one business day</span>',
              '<b>Our Trust team reviews it</b><span>Usually 1 to 3 business days</span>')
# verified card: credential instead of identity
CAP = TI[1].replace('width="20" height="20"', 'width="22" height="22"')
k = re.sub(r'<span class="ko-ii"><svg.*?</svg></span>', '<span class="ko-ii">' + CAP + '</span>', k, count=1, flags=re.S)
k = k.replace('<b>Ada Ononuju</b><span>National ID card · Nigeria · verified 7 October 2026</span>',
              '<b>AWS Certified Data Engineer – Associate</b><span>Amazon Web Services · checked online · 10 October 2026</span>')
k = k.replace('aria-label="Verified identity"', 'aria-label="Verified credential"')
k = k.replace('<b>40%</b><em>+20%</em>', '<b>60%</b><em>+20%</em>')
# next task: Orientation
ORI = TI[0].replace('width="20" height="20"', 'width="22" height="22"')
k = re.sub(r'<span class="ko-ni"><svg.*?</svg></span>', '<span class="ko-ni">' + ORI + '</span>', k, flags=re.S)
k = k.replace('<b>Credentials &amp; expertise</b><span>Your MSc certificate scan is unreadable. Upload a clearer copy.</span>',
              '<b>Creator Orientation</b><span>3 of 7 modules done. Pick up at The validation case.</span>')
k = k.replace('<span>Fix my credentials</span>', '<span>Resume Orientation</span>')
k = k.replace('<a href="CR-RDY-001.dc.html">View readiness</a>', '<a href="CR-CRED-001.dc.html">Your credentials</a>')
k = k.replace("this.v = (props || {}).variant || 'review';", "this.v = (props || {}).variant || 'verified';")
k = re.sub(r"const T = \{.*?\}\[v\];", """const T = {
      review: ['ko-r', 'In review', 'Thanks, your credential is with our Trust team', 'We’ll let you know when it’s checked. Carry on with Orientation meanwhile.'],
      verified: ['ko-v', 'Verified', 'Credential verified', 'Amazon Web Services confirmed your certification. It now shows on your Creator Profile.']
    }[v];""", k, flags=re.S)
k = k.replace(", a: v === 'action', f: v === 'failed' }", ' }')
k = k.replace('<title>', '<title>').replace(re.search(r'<title>.*?</title>', k).group(0), '<title>Credalio · Credential outcome</title>')
for bad in ['Sumsub', '{{a}}', '{{f}}', 'Fix my credentials']:
    assert bad not in k, bad
wr('CR-CRED-003.dc.html', k)

kw = rd('CR-KYC-004.dc.html'); km = rd('CR-KYC-004-Mobile.dc.html') if os.path.exists(os.path.join(P, 'CR-KYC-004-Mobile.dc.html')) else None
for n, v, t in [('CR-CRED-003', 'verified', 'Credential verified'), ('CR-CRED-003b', 'review', 'Credential in review')]:
    if n != 'CR-CRED-003':
        wr(n + '.dc.html', re.sub(r'<dc-import name="CR-KYC-003" variant="\w+"', f'<dc-import name="CR-CRED-003" variant="{v}"', kw).replace(re.search(r'<title>.*?</title>', kw).group(0), f'<title>Credalio · {t}</title>'))
    wr(n + '-Mobile.dc.html', re.sub(r'<dc-import name="CR-KYC-003" variant="\w+"', f'<dc-import name="CR-CRED-003" variant="{v}"', km).replace(re.search(r'<title>.*?</title>', km).group(0), f'<title>{n} mobile preview</title>'))
print('ok')
