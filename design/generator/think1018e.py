"""Designer 2026-10-18: Nova chat (CR-CREATE-002A / 002Ab) gets the same thinking visual as ONB-006 / 007:
the thinking row sits in a bubble with the moving cobalt gradient border + glow, Nova's avatar pulses, and on arrival Nova
thinks first ("Getting to know your field…") before asking question 1 (replays each time the screen comes into view).
Usage: python3 think1018e.py <canvas/project dir>"""
import os, sys
P = sys.argv[1]; f = os.path.join(P, 'CR-CREATE-002A.dc.html'); s = open(f).read()
def rep(s, old, new, n=1):
    assert s.count(old) == n, (old[:90], s.count(old)); return s.replace(old, new)
assert 'nv-bub' not in s
CSS = r'''@keyframes nvBorder{from{background-position:0 0,0% 0}to{background-position:0 0,300% 0}}
@keyframes nvRing{0%,100%{box-shadow:0 0 0 0 rgba(22,82,240,.35)}50%{box-shadow:0 0 0 7px rgba(22,82,240,0)}}
.nv-bub{display:inline-flex;align-self:flex-start;padding:10px 16px 10px 12px;border-radius:18px 18px 18px 6px;border:1.5px solid transparent;background:linear-gradient(#F5F8FF,#F5F8FF) padding-box,linear-gradient(90deg,#1652F0,#C9D8FF,#6E96FF,#DCE5FB,#1652F0) border-box;background-size:100% 100%,300% 100%;box-shadow:0 0 0 5px rgba(22,82,240,.07),0 12px 30px rgba(22,82,240,.13);animation:nvBorder 2.2s linear infinite}
.nv-ava{animation:nvRing 1.6s ease-out infinite}
@media (prefers-reduced-motion: reduce){.nv-bub,.nv-ava{animation:none}}'''
s = rep(s, '</style>', CSS + '\n</style>')
s = rep(s, '<div class="fx-msg fx-nova" style="display: {{m.dd}}"><span aria-hidden="true" style="',
           '<div class="fx-msg fx-nova" style="display: {{m.dd}}"><span class="nv-ava" aria-hidden="true" style="')
s = rep(s, '<span class="nv-think" role="status"><span class="nv-orb" aria-hidden="true"><i></i></span><span class="nv-tt">{{m.think}}</span></span>',
           '<span class="nv-bub"><span class="nv-think" role="status"><span class="nv-orb" aria-hidden="true"><i></i></span><span class="nv-tt">{{m.think}}</span></span></span>')
# intro: think before question 1, replayed whenever the screen comes into view
s = rep(s, "  componentWillUnmount() { clearTimeout(this.t); clearInterval(this.ts); }",
'''  componentDidMount() {
    if (this.state.phase !== 'chat' || this.state.answers.length) return;
    const start = () => {
      clearTimeout(this.ti); clearInterval(this.ts);
      this.setState({ intro: true, step: 0 });
      this.ts = setInterval(() => this.setState({ step: Math.min((this.state.step || 0) + 1, 2) }), 1300);
      this.ti = setTimeout(() => { clearInterval(this.ts); this.setState({ intro: false }); }, 4000);
    };
    if (typeof IntersectionObserver !== 'function') { start(); return; }
    let shown = false;
    this.io = new IntersectionObserver((es) => {
      const r = es[es.length - 1].intersectionRatio;
      if (r >= 0.5 && !shown) { shown = true; if (!this.state.answers.length) start(); } else if (r < 0.05) shown = false;
    }, { threshold: [0, 0.05, 0.5] });
    this.io.observe(document.querySelector('.fx-msgs') || document.documentElement);
  }
  componentWillUnmount() { if (this.io) this.io.disconnect(); clearTimeout(this.t); clearTimeout(this.ti); clearInterval(this.ts); }''')
s = rep(s, "    if (typing) msgs.push({ text: '', nd: 'none', md: 'none', dd: 'flex', qd: 'none', ql: '', edit: () => {} });",
           "    const intro = this.state.intro && n === 0 && phase === 'chat';\n    if (typing || intro) msgs.push({ text: '', nd: 'none', md: 'none', dd: 'flex', qd: 'none', ql: '', edit: () => {} });")
s = rep(s, "    msgs.forEach((m) => { m.think = ['Reading your answer…', 'Thinking it through…', 'Writing…'][this.state.step || 0]; });",
           "    msgs.forEach((m) => { m.think = (intro ? ['Getting to know your field…', 'Planning a few questions…', 'Writing the first one…'] : ['Reading your answer…', 'Thinking it through…', 'Writing…'])[this.state.step || 0]; });")
s = rep(s, "chips: (n < 5 && !typing) ?", "chips: (n < 5 && !typing && !intro) ?")
open(f, 'w').write(s); print('ok')
