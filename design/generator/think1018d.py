"""Designer 2026-10-18: in canvas Play every artboard stays mounted, so ONB-006 / ONB-007 had already finished thinking
by the time you arrive from the previous screen. Now the intro (thinking -> greeting) restarts each time the artboard
comes into view (IntersectionObserver; falls back to starting on mount). Usage: python3 think1018d.py <canvas/project dir>"""
import os, sys
P = sys.argv[1]
def rep(s, old, new, n=1):
    assert s.count(old) == n, (old[:90], s.count(old)); return s.replace(old, new)
WATCH = '''  watch(start) {
    if (typeof IntersectionObserver !== 'function') { start(); return; }
    let shown = false;
    this.io = new IntersectionObserver((es) => {
      const r = es[es.length - 1].intersectionRatio;
      if (r >= 0.5 && !shown) { shown = true; start(); } else if (r < 0.05) shown = false;
    }, { threshold: [0, 0.05, 0.5] });
    this.io.observe(document.querySelector('.ob-root') || document.documentElement);
  }
'''
f = os.path.join(P, 'CR-ONB-006.dc.html'); s = open(f).read(); assert 'watch(' not in s
s = rep(s, "    this.greet(5200, 1700);\n  }\n", "    this.watch(() => this.setState({ sel: 'Nova', picked: false, asked: false }, () => this.greet(5200, 1700)));\n  }\n" + WATCH)
s = rep(s, "componentWillUnmount() { clearInterval(this.ts);", "componentWillUnmount() { if (this.io) this.io.disconnect(); clearInterval(this.ts);")
open(f, 'w').write(s)
f = os.path.join(P, 'CR-ONB-007.dc.html'); s = open(f).read(); assert 'watch(' not in s
s = rep(s, "    this.think();\n  }\n", "    this.watch(() => this.think());\n  }\n" + WATCH)
s = rep(s, "  componentWillUnmount() { clearTimeout(this.t0);", "  componentWillUnmount() { if (this.io) this.io.disconnect(); clearTimeout(this.t0);")
open(f, 'w').write(s)
print('ok')
