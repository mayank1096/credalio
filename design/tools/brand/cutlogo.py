# cutlogo.py <page.svg> <out.svg> <x0> <y0> <x1> <y1> [pad]: keeps the filled paths whose box lies inside the region
# (page coordinates from pdftocairo -svg), drops text glyphs and backgrounds, and crops the viewBox to the logo.
import re, sys
src, out = sys.argv[1:3]; X0, Y0, X1, Y1 = map(float, sys.argv[3:7]); pad = float(sys.argv[7]) if len(sys.argv) > 7 else 0
s = open(src).read(); body = s[s.index('</defs>') + 7:]
keep = []; bx = [1e9, 1e9, -1e9, -1e9]
for m in re.finditer(r'<path ([^>]*?)/>', body):
    a = m.group(1); d = re.search(r' d="([^"]*)"', a).group(1)
    nums = list(map(float, re.findall(r'-?[\d.]+', d))); xs, ys = nums[0::2], nums[1::2]
    if not xs: continue
    if min(xs) >= X0 and max(xs) <= X1 and min(ys) >= Y0 and max(ys) <= Y1:
        fill = re.search(r'fill="([^"]*)"', a).group(1)
        keep.append('<path fill-rule="nonzero" fill="%s" d="%s"/>' % (fill, d))
        bx = [min(bx[0], min(xs)), min(bx[1], min(ys)), max(bx[2], max(xs)), max(bx[3], max(ys))]
x, y, w, h = bx[0] - pad, bx[1] - pad, bx[2] - bx[0] + 2 * pad, bx[3] - bx[1] + 2 * pad
open(out, 'w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%.2f %.2f %.2f %.2f" width="%.0f" height="%.0f">%s</svg>\n' % (x, y, w, h, w, h, ''.join(keep)))
print(out, len(keep), 'paths', '%.0fx%.0f' % (w, h))
