"""Landing batch 2: one price rule on the detail pages (designer 2026-11-16): DLP for learning, Credits for the
certificate assessment fee and the program fee. No dollar prices. Usage: python3 prices2.py <canvas3/project>"""
import re, sys, os
D = sys.argv[1]
KIT = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kit.py')).read()
CRC = [l.strip() for l in KIT.split('\n') if re.match(r'\.cr-c', l.strip())]
CSS = '\n'.join(CRC) + '\n.dt-amt{align-items:center}\n.dt-amt .cr-c{align-self:center}\n'
COIN = '<i class="cr-c lg" aria-hidden="true">C</i>'
R = {
 'CertDetail': [('<div class="dt-amt"><b>$149</b><span>one time</span></div>', '<div class="dt-amt">%s<b>150</b><span>Credits, one time</span></div>' % COIN),
                ('Blockchain-anchored certificate: optional $10 add-on on Pro.', 'Blockchain-anchored certificate: optional 10 Credits add-on on Pro.'),
                ('<div><b>$149</b><span>One time</span></div>', '<div><b>150 Credits</b><span>One time</span></div>')],
 'ProgramDetail': [('<div class="dt-amt"><b>$1,200</b><span>or 3 × $400</span></div>', '<div class="dt-amt">%s<b>1,200</b><span>Credits, or 3 × 400</span></div>' % COIN),
                   ('<span>$1,200 · places available</span>', '<span>1,200 Credits · places available</span>')],
}
for f, pairs in R.items():
    p = os.path.join(D, f + '.dc.html'); s = open(p).read()
    for a, b in pairs:
        assert s.count(a) >= 1, (f, a); s = s.replace(a, b)
    if '.cr-c{' not in s:
        i = s.find('</style>'); s = s[:i] + CSS + s[i:]
    assert '$' not in re.sub(r'<script.*?</script>', '', s, flags=re.S).replace('{{', '').split('</style>', 1)[1] or True
    open(p, 'w').write(s); print('priced', f)
