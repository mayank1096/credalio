"""Fold the less-used filter groups under a 'More filters' disclosure so listing pages stay compact.
Usage: python3 chk8b.py <canvas3/project>"""
import os, sys
D = sys.argv[1]
CSS = ('.cs-more>summary{list-style:none;cursor:pointer;display:flex;align-items:center;justify-content:space-between;min-height:48px;font-size:14px;font-weight:600;color:#1652F0;border-bottom:1px solid #EEF1F7}\n'
       '.cs-more>summary::-webkit-details-marker{display:none}\n'
       '.cs-more>summary svg{transition:transform .2s ease}\n'
       '.cs-more[open]>summary svg{transform:rotate(180deg)}\n'
       '.cs-more>summary:hover{color:#0E3BB8}\n')
CHEV = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"></path></svg>'
G = '<div class="cs-grp" role="%s" aria-label="%s">'

def grp(s, label):
    for role in ('group', 'radiogroup'):
        i = s.find(G % (role, label))
        if i > -1: return i
    raise AssertionError(label)

def grp_end(s, i):
    # a group is <div class="cs-grp" ...> ... </sc-for></div></div>
    return s.index('</sc-for></div></div>', i) + len('</sc-for></div></div>')

def fold(name, first, n):
    p = os.path.join(D, name); s = open(p, encoding='utf-8').read()
    assert 'cs-more' not in s, 'already patched'
    a = grp(s, first); b = s.index('<button class="ds-btn cs-go2"', a)
    s = s[:a] + '<details class="cs-more"><summary>More filters (%d)%s</summary>' % (n, CHEV) + s[a:b] + '</details>' + s[b:]
    s = s.replace('</style>', CSS + '</style>', 1)
    open(p, 'w', encoding='utf-8').write(s)

# Programs: move Duration after Start, then fold from Duration
p = os.path.join(D, 'Programs.dc.html'); s = open(p, encoding='utf-8').read()
a = grp(s, 'Duration'); b = grp_end(s, a); dur = s[a:b]; s = s[:a] + s[b:]
a = grp(s, 'Start'); b = grp_end(s, a); s = s[:b] + dur + s[b:]
open(p, 'w', encoding='utf-8').write(s)
fold('Programs.dc.html', 'Duration', 8)
fold('Certifications.dc.html', 'Issuer', 4)
fold('CareerPaths.dc.html', 'Skills you’ll build', 4)
print('ok')
