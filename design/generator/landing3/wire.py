"""Landing batch 2: wire cards, 'View all' links and breadcrumbs so Explore → listing → detail clicks through.
Patches live sources in place. Usage: python3 wire.py <canvas3/project>"""
import re, sys, os

def sub1(s, old, new, n=1):
    assert old in s, old[:80]
    return s.replace(old, new, n)

def view_all(s):
    # the four "View all" links on Explore, in section order: paths, courses, certs, programs
    it = iter(['CareerPaths.dc.html', 'Courses.dc.html', 'Certifications.dc.html', 'Programs.dc.html'])
    return re.sub(r'<a class="ds-link" href="#">View all</a>', lambda m: '<a class="ds-link" href="%s">View all</a>' % next(it), s)

R = {
    'Explore': [('<a class="cp-card {{p.cls}}" href="#"', '<a class="cp-card {{p.cls}}" href="PathDetail.dc.html"'),
                ('<a class="ct-card" href="#"', '<a class="ct-card" href="CertDetail.dc.html"'),
                ('<a class="pg-row" href="#"', '<a class="pg-row" href="ProgramDetail.dc.html"')],
    'CareerPaths': [('<a class="cp-card {{p.cls}}" href="#"', '<a class="cp-card {{p.cls}}" href="PathDetail.dc.html"')],
    'Certifications': [('<a class="ct-card" href="#"', '<a class="ct-card" href="CertDetail.dc.html"')],
    'Programs': [('<a class="pg-feat aur" href="#"', '<a class="pg-feat aur" href="ProgramDetail.dc.html"'), ('<a class="pg-row" href="#"', '<a class="pg-row" href="ProgramDetail.dc.html"')],
    'Courses': [('<nav class="cs-crumb" aria-label="Breadcrumb"><a href="#">', '<nav class="cs-crumb" aria-label="Breadcrumb"><a href="Explore.dc.html">')],
    'CourseDetail': [('<nav class="cd-crumb" aria-label="Breadcrumb"><a href="#">Explore learning</a><span aria-hidden="true">/</span><a href="#">Courses</a>',
                      '<nav class="cd-crumb" aria-label="Breadcrumb"><a href="Explore.dc.html">Explore learning</a><span aria-hidden="true">/</span><a href="Courses.dc.html">Courses</a>'),
                     ('<a class="cd-path aur" href="#"', '<a class="cd-path aur" href="PathDetail.dc.html"')],
    'PathDetail': [('<nav class="pd-crumb" aria-label="Breadcrumb"><a href="#">', '<nav class="pd-crumb" aria-label="Breadcrumb"><a href="CareerPaths.dc.html">')],
    'CertDetail': [('<nav class="dt-crumb" aria-label="Breadcrumb"><a href="#">', '<nav class="dt-crumb" aria-label="Breadcrumb"><a href="Certifications.dc.html">')],
    'ProgramDetail': [('<nav class="dt-crumb" aria-label="Breadcrumb"><a href="#">', '<nav class="dt-crumb" aria-label="Breadcrumb"><a href="Programs.dc.html">')],
}
GC = ['CourseDetail.dc.html', 'CertDetail.dc.html', 'CareerPaths.dc.html', 'Programs.dc.html']

def patch(page, s):
    for a, b in R.get(page, []):
        if a in s: s = s.replace(a, b)
    if page == 'Explore': s = view_all(s)
    # every course card (a link or a button-wrapped card) opens Course detail
    s = re.sub(r'<a class="cs-card([^"]*)" href="#"', r'<a class="cs-card\1" href="CourseDetail.dc.html"', s)
    if page == 'Landing':
        it = iter(GC)
        s = re.sub(r'<a class="(gc-card[^"]*)" href="#"', lambda m: '<a class="%s" href="%s"' % (m.group(1), next(it)), s)
        s = s.replace('<a class="ds-btn mk-link" href="#"', '<a class="ds-btn mk-link" href="Explore.dc.html"')
    return s

if __name__ == '__main__':
    d = sys.argv[1]
    for f in sorted(os.listdir(d)):
        if not f.endswith('.dc.html') or '-' in f: continue
        p = os.path.join(d, f); s = open(p).read(); t = patch(f[:-8], s)
        if t != s: open(p, 'w').write(t); print('wired', f)
