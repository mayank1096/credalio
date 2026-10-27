"""Designer 2026-10-18: picking Nova / Maya / Alex / Sage on CR-ONB-006 must feel alive.
Each pick: the new character rises and un-blurs in, Nova's thinking state runs (aura, glowing bubble, "<name> is stepping in… / saying hello…"),
then a fresh greeting types in with the new name. Name chips and Continue stay visible after the first greeting.
Run after think1018b.py. Usage: python3 think1018c.py <canvas/project dir>"""
import os, sys
P = sys.argv[1]; f = os.path.join(P, 'CR-ONB-006.dc.html'); s = open(f).read()
def rep(s, old, new, n=1):
    assert s.count(old) == n, (old[:90], s.count(old)); return s.replace(old, new)
assert 'greet(' not in s
s = rep(s, 'mix-blend-mode: multiply; opacity: {{a.op}}; transition: opacity .45s ease">',
        'mix-blend-mode: multiply; opacity: {{a.op}}; transform: {{a.tf}}; filter: {{a.fl}}; transition: opacity .5s ease, transform .7s cubic-bezier(.2,.8,.2,1), filter .5s ease">')
old_mount = s[s.index('  componentDidMount() {'):s.index('  componentWillUnmount()')]
s = s.replace(old_mount, '''  componentDidMount() {
    this.reduce = typeof matchMedia === 'function' && matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (this.props && this.props.variant === 'thinking') { this.setState({ step: 1 }); return; }
    if (this.reduce) { this.setState({ phase: 'done', i: 9999, asked: true }); return; }
    this.greet(3600, 1200);
  }
  greet(wait, every) {
    clearInterval(this.ts); clearTimeout(this.t0); clearTimeout(this.t1); clearInterval(this.iv);
    this.setState({ phase: 'wait', step: 0, i: 0 });
    this.ts = setInterval(() => this.setState({ step: Math.min(this.state.step + 1, 2) }), every);
    this.t0 = setTimeout(() => {
      clearInterval(this.ts);
      this.setState({ phase: 'typing' });
      this.iv = setInterval(() => {
        const full = this.full();
        if (this.state.i >= full.length) { clearInterval(this.iv); this.t1 = setTimeout(() => this.setState({ phase: 'done', asked: true }), 350); return; }
        this.setState({ i: this.state.i + 2 });
      }, 24);
    }, wait);
  }
  pick(label) {
    if (label === this.state.sel) return;
    this.setState({ sel: label, picked: true }, () => { if (this.reduce) this.setState({ phase: 'done', i: 9999 }); else this.greet(1800, 700); });
  }
''')
s = rep(s, "phase: 'wait', step: 0 }; }", "phase: 'wait', step: 0, asked: false, picked: false }; }")
s = rep(s, "      think: this.name() + [' is reading your profile…', ' is getting to know Data Analysis…', ' is writing to you…'][this.state.step],",
           "      think: this.name() + (this.state.picked ? [' is stepping in…', ' is getting ready…', ' is saying hello…'] : [' is reading your profile…', ' is getting to know Data Analysis…', ' is writing to you…'])[this.state.step],")
s = rep(s, "askShown: phase === 'done',", "askShown: this.state.asked || phase === 'done',")
s = rep(s, "op: sel === label ? '1' : '0' }))", "op: sel === label ? '1' : '0', tf: sel === label ? 'none' : 'translateY(14px) scale(.96)', fl: sel === label ? 'none' : 'blur(6px)' }))")
s = rep(s, "pick: () => this.setState({ sel: label }),", "pick: () => this.pick(label),")
open(f, 'w').write(s); print('ok')
# Designer 2026-10-18 follow-up (applied in place): thinking lasts longer (006: 5.2 s first / 3.3 s per pick; 007: 4.8 s;
# 002A: 3.3 s per answer, 4.2 s drafting) and the status line is regular weight (400), not medium.
