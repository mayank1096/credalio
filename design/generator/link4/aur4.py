"""Aurora dark cards for Link 4: the shared animated Aurora (landing3/aurora.js) replaces the flat navy gradient.

Post-step run by layout.py after every source is written. For each source it adds class "aur" to the dark
boxes listed in DARK, the Aurora CSS (only for classes present), the Aurora methods on the Component and a
componentDidMount call. The original gradient stays underneath as the fallback when WebGL is missing.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'landing3'))
from kit import AURORA_JS  # noqa: E402

DARK = ['oph', 'opv-c', 'lc-hero', 'pn', 'cpv-h', 'lv-hero', 'hm-next', 'pv-cv', 'lv-cv', 'lc2-cv', 'lc-bv', 'lpv', 'sh8-cv']
GLOW = ['oph', 'opv-c', 'lc-hero', 'cpv-h', 'lv-hero']  # their old ::after glow sits on top of the aurora
BASE = ('.aur{position:relative;isolation:isolate;overflow:hidden}\n'
        '.aur > .aur-c{position:absolute;inset:0;width:100%;height:100%;z-index:-1;pointer-events:none;border-radius:inherit}\n')


def patch(s):
    used = []
    def cls(m):
        names = m.group(1).split()
        if 'aur' not in names and any(n in DARK for n in names):
            used.extend(n for n in names if n in DARK)
            return 'class="%s aur"' % m.group(1)
        return m.group(0)
    s = re.sub(r'class="([^"{}]*)"', cls, s)
    # the large course-cover preview (Basics / Publish), not the small cover icons
    s, n = re.subn(r'(class="[^"]*\bcv2\b[^"]*">.{0,300}?class=")cov-i"', r'\1cov-i aur"', s, flags=re.S)
    if n:
        used.append('cov-i')
    if not used:
        return s
    css = BASE + ''.join('.%s.aur::after{display:none}\n' % g for g in GLOW if g in used)
    i = s.rindex('</style>')
    s = s[:i] + css + s[i:]
    head = 'class Component extends DCLogic {'
    i = s.index(head) + len(head)
    s = s[:i] + '\n' + AURORA_JS + '\n' + s[i:]
    if 'componentDidMount() {' in s:
        s = s.replace('componentDidMount() {', 'componentDidMount() { this.aurScan();', 1)
    else:
        j = s.index(head) + len(head)
        s = s[:j] + '\n  componentDidMount() { this.aurScan(); }' + s[j:]
    return s


def run(out):
    for f in sorted(os.listdir(out)):
        if not f.endswith('.dc.html') or '-' in f:
            continue
        p = os.path.join(out, f)
        s = open(p).read()
        if 'aurScan' in s:
            continue
        t = patch(s)
        if t != s:
            open(p, 'w').write(t)


if __name__ == '__main__':
    run(sys.argv[1])
