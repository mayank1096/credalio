# ctype1013: designer 2026-10-13 — ONB-002 "How will you create?" shows a ROLE-SPECIFIC illustration (the role picked on
# Main via sessionStorage crRole): same person in the centre, left = creating on their own, right = with an organization.
# learner / creator / validator images (designer), replaces the main scene + role fades on this screen. Mobile pan 0
# (centre person). usage: python3 ctype1013.py <dir>
import os, re, sys
IMG = {'learn': '/_blob/e068872cdedaf033aa3b84af3a149173', 'create': '/_blob/303efabd2ddabb7edfb4cda677ac03d8',
       'validate': '/_blob/9c4c8b4c538fc972644e2f47e62afe9c'}
p = os.path.join(sys.argv[1], 'CR-ONB-002.dc.html'); s = open(p, encoding='utf-8').read()
assert 'roleImg' not in s
i = s.find('<div class="ob-illus" aria-hidden="true"'); j = s.find('</div>', i); blk = s[i:j]
k = blk.find('<img '); ke = blk.find('>', k) + 1
img = '<img src="{{roleImg}}" alt="" style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; display: block; object-fit: cover; object-position: center bottom">'
nb = blk[:k] + img + '\n'
s = s[:i] + nb + s[j:]
a = "return { rl, rolePan: "
assert s.count(a) == 1
s = s.replace(a, "const imgs = %r;\n    return { roleImg: imgs[role] || imgs.create, rl, X % IMG)
s = re.sub(r"_pan: \{[^}]*\}\[role\], ", '', s, count=1)
open(p, 'w', encoding='utf-8').write(s); print('ok')
