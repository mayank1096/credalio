# cl1013g: cleanup of the last 15 Link 1 screens (designer "remove unnecessary stuff, tooltips"). usage: python3 cl1013g.py <dir>
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tipx
P = sys.argv[1]; OUT = []
def rd(f): return open(os.path.join(P, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(P, f), 'w', encoding='utf-8').write(s); OUT.append(f)
def sub(s, a, b, n=1):
    assert s.count(a) >= 1, a[:90]; return s.replace(a, b, n)
def css(s, c):
    i = s.rfind('</style>', 0, s.find('</helmet>')); return s[:i] + c + s[i:]
TC = '\n/* cl1013g tooltips */' + tipx.TIP_CSS
# COL-002: duplicate chips, consent intro + reply note -> tooltips
s = rd('CR-COL-002.dc.html'); assert 'cl1013g' not in s
s = sub(s, '<div class="cl-meta"><span>Course</span><span>Draft · build phase</span><span>ABC Institute</span></div>', '<div class="cl-meta"><span>Draft · build phase</span></div>')
s = sub(s, '<h2 id="cl-ch2" class="cl-ph">Before you join</h2><p class="cl-pp">Confirm how you’re taking part. This isn’t the validation declaration; that comes later, for your own work.</p>',
        '<h2 id="cl-ch2" class="cl-ph">Before you join' + tipx.tip('This isn’t the validation declaration. That comes later, for your own work.') + '</h2>')
s = sub(s, '<label for="cl-q" class="cl-lab">Your question to Dr. Bola Ade</label>', '<label for="cl-q" class="cl-lab">Your question to Dr. Bola Ade' + tipx.tip('The reply appears with this invitation.') + '</label>')
s = sub(s, '<span>The reply appears with this invitation.</span>', '<span></span>')
wr('CR-COL-002.dc.html', css(s, TC))
# DEC-001: duplicate "Course" chips, "Next" cell repeats the step tracker
s = rd('CR-DEC-001.dc.html'); assert 'cl1013g' not in s
s = s.replace('<div class="cl-meta"><span>Course</span>', '<div class="cl-meta">')
s = sub(s, '<span class="cl-sv"><em>Next</em><b>Quote → payment → case opens</b></span>', '')
wr('CR-DEC-001.dc.html', css(s, '\n/* cl1013g */\n'))
# CRED-002: date fields on one line each half, shorter fix intro
s = rd('CR-CRED-002.dc.html'); assert 'cl1013g' not in s
for i in ['x1', 'x2', 'g1', 'g2']:
    s = sub(s, f'<div class="cr-f s1 s1m"><label class="ob-lab" for="{i}">', f'<div class="cr-f s2 s1m"><label class="ob-lab" for="{i}">')
s = sub(s, '"sub": "We couldn’t read your scan. Upload a clearer copy, or switch to the credential ID."', '"sub": "Upload a clearer copy, or use the credential ID instead."')
wr('CR-CRED-002.dc.html', css(s, '\n/* cl1013g */\n'))
# KYC-001: Sumsub line repeats the partner header
s = rd('CR-KYC-001.dc.html'); assert 'cl1013g' not in s
s, n = re.subn(r'<p class="k1-priv"><svg.*?</svg><span>Sumsub handles your ID check\.</span></p>', '', s, count=1, flags=re.S); assert n
wr('CR-KYC-001.dc.html', css(s, '\n/* cl1013g */\n'))
# KYC-002: "Step n of 4" repeats the stepper
s = rd('CR-KYC-002.dc.html'); assert 'cl1013g' not in s
s = sub(s, '<span class="lp-eb">Step {{stepN}} of 4</span>', '')
wr('CR-KYC-002.dc.html', css(s, '\n/* cl1013g */\n'))
# POL-001: second sentence -> tooltip
s = rd('CR-POL-001.dc.html'); assert 'cl1013g' not in s
s = sub(s, '<p class="pl-sub">Open each policy, read the key points, and accept it. You can read the full text at any time from Creator Centre.</p>',
        '<p class="pl-sub">Read the key points of each policy and accept it.' + tipx.tip('You can read the full text any time in Creator Centre.') + '</p>')
wr('CR-POL-001.dc.html', css(s, TC))
print('cl1013g ok'); print(' '.join(OUT))
