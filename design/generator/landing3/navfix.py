"""Landing batch 2 (client review): one shared nav + footer across the public pages.
Patches the live sources in place (never rebuilds them): 8 nav links, all wired, active state per page,
a working mobile menu (details/summary, no JS), logo to Landing, footers with every link wired.
Usage: python3 navfix.py <canvas3/project>
"""
import re, sys, os

LINKS = [('Explore learning', 'Explore.dc.html'), ('Courses', 'Courses.dc.html'), ('Career paths', 'CareerPaths.dc.html'),
         ('Certifications', 'Certifications.dc.html'), ('Learning programs', 'Programs.dc.html'), ('Pricing', 'Pricing.dc.html'),
         ('For creators', 'Creators.dc.html'), ('For institutions', 'Institutions.dc.html')]
ACTIVE = {'Explore': 'Explore learning', 'Access': 'Explore learning', 'Courses': 'Courses', 'CourseDetail': 'Courses',
          'CareerPaths': 'Career paths', 'PathDetail': 'Career paths', 'Certifications': 'Certifications', 'CertDetail': 'Certifications',
          'Programs': 'Learning programs', 'ProgramDetail': 'Learning programs', 'Pricing': 'Pricing', 'Creators': 'For creators',
          'Institutions': 'For institutions', 'Partner': 'For institutions'}
MENU_I = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"></path></svg>'
CLOSE_I = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"></path></svg>'

def links(cls, active):
    return '\n'.join('<a class="%s%s" href="%s"%s>%s</a>' % (cls, ' %s-on' % cls if l == active else '', h, ' aria-current="page"' if l == active else '', l) for l, h in LINKS)

def drawer(active, menu_cls):
    return ('<details class="sx-dd"><summary class="%s" aria-label="Open menu"><span class="sx-dd-o">%s</span><span class="sx-dd-x">%s</span></summary>'
            '<nav class="sx-dn" aria-label="Menu">%s<span class="sx-dn-sep"></span><a class="sx-dl" href="#">Log in</a><a class="ds-btn sx-dn-cta" href="OnbWelcome.dc.html"><span>Create account</span></a></nav></details>') % (
        menu_cls, MENU_I, CLOSE_I, ''.join('<a class="sx-dl%s" href="%s"%s>%s</a>' % (' sx-dl-on' if l == active else '', h, ' aria-current="page"' if l == active else '', l) for l, h in LINKS))

DCSS = ('@media (min-width: 1301px){.sx-links{gap:2px}.sx-links .sx-link{padding:0 10px;font-size:14.5px}.lh-links .lh-link{padding:0 10px !important;font-size:14.5px !important}}\n'
        '.sx-dd{position:relative;display:none}\n.sx-dd > summary{list-style:none;cursor:pointer}\n.sx-dd > summary::-webkit-details-marker{display:none}\n'
        '.sx-dd .sx-dd-x{display:none}\n.sx-dd[open] .sx-dd-o{display:none}\n.sx-dd[open] .sx-dd-x{display:flex}\n.sx-dd-o,.sx-dd-x{align-items:center;justify-content:center}\n.sx-dd-o{display:flex}\n'
        '.sx-dn{position:fixed;right:16px;top:68px;z-index:60;max-height:calc(100vh - 84px);overflow:auto;width:min(320px,calc(100vw - 32px));box-sizing:border-box;padding:10px;border-radius:20px;background:#FFFFFF;border:1.5px solid #E6EAF3;box-shadow:0 24px 60px -20px rgba(11,20,51,.28);display:flex;flex-direction:column;gap:2px}\n'
        '.sx-dl{display:flex;align-items:center;min-height:46px;padding:0 14px;border-radius:12px;font-size:15.5px;font-weight:500;color:#0B1433;text-decoration:none}\n'
        '.sx-dl:hover{background:#F5F8FF}\n.sx-dl-on{background:#EAF0FF;color:#0E3BB8}\n.sx-dn-sep{height:1.5px;background:#EEF1F7;margin:6px 4px}\n.sx-dn-cta{margin-top:6px;justify-content:center}\n'
        '@media (max-width: 1300px){.sx-links{display:none}.sx-menu{display:flex}.lh-links{display:none !important}.lh-menu{display:flex !important}.sx-dd{display:block}}\n')

SFOOT = ('<nav aria-label="Footer"><a href="Courses.dc.html">Courses</a><a href="CareerPaths.dc.html">Career Paths</a><a href="Certifications.dc.html">Certifications</a>'
         '<a href="Programs.dc.html">Learning Programs</a><a href="Pricing.dc.html">Pricing</a><a href="Creators.dc.html">For Creators</a><a href="Institutions.dc.html">For Institutions</a>'
         '<a href="Validation.dc.html">How validation works</a><a href="#">Privacy</a><a href="#">Terms</a></nav>')
FT_LEARN = ('<nav class="ft-col" aria-label="Learn"><span class="ft-h">Learn</span><a class="ft-a" href="Explore.dc.html">Explore learning</a><a class="ft-a" href="Courses.dc.html">Courses</a>'
            '<a class="ft-a" href="Certifications.dc.html">Professional Certifications</a><a class="ft-a" href="CareerPaths.dc.html">Career Paths</a><a class="ft-a" href="Programs.dc.html">Learning Programs</a>'
            '<a class="ft-a" href="Validation.dc.html">How validation works</a></nav>')

def patch(name, s):
    page = name[:-8]
    act = ACTIVE.get(page, '')
    # sx header
    s = re.sub(r'<nav class="sx-links" aria-label="Main">.*?</nav>', lambda m: '<nav class="sx-links" aria-label="Main">\n%s\n</nav>' % links('sx-link', act), s, flags=re.S)
    s = re.sub(r'<button class="sx-menu" type="button" aria-label="Open menu">.*?</button>', lambda m: drawer(act, 'sx-menu'), s, flags=re.S)
    s = s.replace('<a class="sx-logo" href="#"', '<a class="sx-logo" href="Landing.dc.html"')
    # Landing header (inline-styled lh-links)
    def lh(m):
        out = m.group(0)
        for l, h in LINKS:
            out = re.sub(r'(<a class="lh-link" href=")[^"]*(" style="[^"]*">%s</a>)' % re.escape(l), r'\g<1>%s\2' % h, out)
        st = re.search(r'<a class="lh-link" href="[^"]*" (style="[^"]*")>', out).group(1)
        for prev, (l, h) in [('Explore learning', LINKS[1]), ('Certifications', LINKS[4])]:
            if '>%s</a>' % l not in out:
                out = out.replace('>%s</a>' % prev, '>%s</a>\n<a class="lh-link" href="%s" %s>%s</a>' % (prev, h, st, l), 1)
        return out
    s = re.sub(r'<nav class="lh-links" aria-label="Main".*?</nav>', lh, s, flags=re.S)
    s = re.sub(r'<button class="lh-menu" type="button" aria-label="Open menu" (style="[^"]*")>.*?</button>',
               lambda m: drawer('', 'lh-menu" %s' % m.group(1)).replace('class="lh-menu" style', 'class="lh-menu" style', 1), s, flags=re.S)
    s = s.replace('<a href="#" aria-label="Credalio home"', '<a href="Landing.dc.html" aria-label="Credalio home"')
    # footers
    s = re.sub(r'<nav aria-label="Footer">.*?</nav>', SFOOT, s, flags=re.S)
    s = re.sub(r'<nav class="ft-col" aria-label="Learn">.*?</nav>', FT_LEARN, s, flags=re.S)
    s = s.replace('<a class="ft-a" href="#">Become a Validator</a>', '<a class="ft-a" href="Validation.dc.html">Become a Validator</a>')
    s = s.replace('<a class="ft-a" href="#">Pricing</a>', '<a class="ft-a" href="Pricing.dc.html">Pricing</a>')
    if 'sx-dd' in s and '.sx-dd{' not in s:
        i = s.index('</style>'); s = s[:i] + DCSS + s[i:]
    return s

if __name__ == '__main__':
    d = sys.argv[1]
    for f in sorted(os.listdir(d)):
        if not f.endswith('.dc.html'): continue
        p = os.path.join(d, f); s = open(p).read(); t = patch(f, s)
        if t != s: open(p, 'w').write(t); print('patched', f)
