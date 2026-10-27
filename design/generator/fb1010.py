# Client feedback 2026-10-10: Creio, row buttons, Sumsub wording, Credalio team, teach->topics,
# sentence case, hedged timelines, consistent sample data. Applied directly to canvas files (copy only).
import re, sys, os, glob
P = sys.argv[1]
R = {
 '*': [('AI Tokens', 'Creio')],
 'CR-ONB-002.dc.html': [('Create Independently', 'Create independently'), ('With an Organization', 'With an organization')],
 'CR-ONB-005b.dc.html': [('>Teaches <span', '>Topics <span'), ('SQL teacher', 'SQL trainer'), ('what you will teach', 'your topics')],
 'CR-RDY-001.dc.html': [('class="rd-cta">Resume Orientation', 'class="rd-cta">Resume'), ('<span class="rd-nl">Your next step', '<span class="rd-nl">Nova suggests'),
                        ('Your MSc certificate scan', 'Your Google certificate scan'), ('It’s reviewed within a business day', 'It’s usually reviewed within a business day')],
 'CR-KYC-003.dc.html': [('Your MSc certificate scan', 'Your Google certificate scan'),
                        ('Ada Ononuju · Nigeria · verified by Sumsub on 1 Oct 2026. Your identity badge', 'Verified by Sumsub. Your identity badge')],
 'CR-ORI-007.dc.html': [('Your MSc certificate scan', 'Your Google certificate scan')],
 'CR-CRED-001.dc.html': [('class="ds-ghost">Fix</a>', 'class="ds-ghost">Fix now</a>')],
 'CR-CRED-002.dc.html': [('Reviewed by the Credalio Trust team', 'Reviewed by the Credalio team'), ("'Reviewed in 1 to 3 days'", "'Usually reviewed in 1 to 3 days'"),
                         ("lab('Organisation'", "lab('Organization'"), ('>Organisation</label>', '>Organization</label>')],
 'CR-CRED-003.dc.html': [('Thanks, your credential is with our Trust team', 'Thanks, your credential is with the Credalio team'), ('<b>Our Trust team reviews it', '<b>The Credalio team reviews it')],
 'CR-KYC-002.dc.html': [('Powered by Sumsub · secure and encrypted', 'Powered by Sumsub')],
}
SEC = re.compile(r'<span class="tk-sec"><svg.*?</svg><span>Secure · encrypted</span></span>', re.S)
SUM = '<span class="tk-sec tk-sum"><span>Powered by Sumsub</span></span>'
SUMCSS = '\n.tk-sec.tk-sum{background:#F1F3F8;color:#4A5578;padding:0 13px}\n@media (max-width: 960px){.tk-sec.tk-sum{width:auto;padding:0 12px;font-size:12px;height:30px}.tk-sec.tk-sum span{display:inline}}\n'
ch = {}
for f in sorted(glob.glob(os.path.join(P, '*.dc.html'))):
    n = os.path.basename(f); s = o = open(f, encoding='utf-8').read()
    for a, b in R['*'] + R.get(n, []):
        if a in s: s = s.replace(a, b)
        elif n in R and (a, b) in R[n]: print('MISSING', n, a)
    if n.startswith('CR-KYC-00') and not n.endswith('-Mobile.dc.html') and SEC.search(s):
        s = SEC.sub(SUM, s); s = s.replace('</style>', SUMCSS + '</style>', 1)
    if s != o: open(f, 'w', encoding='utf-8').write(s); ch[n] = 1
print(sorted(ch))
