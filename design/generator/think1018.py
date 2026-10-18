"""Designer 2026-10-18: a clear "Nova is thinking" state before every AI reply (replaces the three dots / bare caret wait).
Indicator = spinning cobalt ring orb + shimmering status line that steps through what Nova is doing (~2.4-2.9 s), then the reply types in.
Patches LIVE CR-ONB-006 (Meet your Copilot), CR-ONB-007 (+007p; How should Nova work) and CR-CREATE-002A (+002Ab; Nova chat + drafting).
Usage: python3 think1018.py <canvas/project dir>"""
import os, re, sys
P = sys.argv[1]
rd = lambda f: open(os.path.join(P, f)).read()
def wr(f, s): open(os.path.join(P, f), 'w').write(s)
def rep(s, old, new, n=1):
    assert s.count(old) == n, (old[:80], s.count(old)); return s.replace(old, new)

CSS = r'''@keyframes nvSpin{to{transform:rotate(360deg)}}
@keyframes nvPulse{0%,100%{transform:scale(.65);opacity:.65}50%{transform:scale(1);opacity:1}}
@keyframes nvShim{from{background-position:100% 0}to{background-position:-100% 0}}
.nv-think{display:inline-flex;align-items:center;gap:10px;min-height:24px}
.nv-orb{position:relative;width:22px;height:22px;flex-shrink:0;display:flex;align-items:center;justify-content:center}
.nv-orb::before{content:'';position:absolute;inset:0;border-radius:50%;background:conic-gradient(from 0deg,#1652F0,#6E96FF,#DCE5FB,#1652F0);-webkit-mask:radial-gradient(circle,transparent 6.5px,#000 7.5px);mask:radial-gradient(circle,transparent 6.5px,#000 7.5px);animation:nvSpin 1.1s linear infinite}
.nv-orb i{width:7px;height:7px;border-radius:50%;background:#1652F0;animation:nvPulse 1.1s ease-in-out infinite}
.nv-tt{font-size:15px;font-weight:500;line-height:1.4;background:linear-gradient(90deg,#5B6582 0%,#5B6582 35%,#1652F0 50%,#5B6582 65%,#5B6582 100%);background-size:200% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:nvShim 1.6s linear infinite}
@media (prefers-reduced-motion: reduce){.nv-orb::before,.nv-orb i,.nv-tt{animation:none}.nv-tt{color:#5B6582}}'''
def ui(text): return '<span class="nv-think" role="status"><span class="nv-orb" aria-hidden="true"><i></i></span><span class="nv-tt">%s</span></span>' % text
DOTS = '<sc-if value="{{waiting}}" hint-placeholder-val="{{false}}"><span style="display: inline-flex; gap: 5px; padding: 6px 0" aria-label="typing"><span class="cp-dot"></span><span class="cp-dot" style="animation-delay: .15s"></span><span class="cp-dot" style="animation-delay: .3s"></span></span></sc-if>'
def add_css(s): return rep(s, '</style>', CSS + '\n</style>')

# CR-ONB-006 · Meet your Copilot
s = rd('CR-ONB-006.dc.html'); assert 'nv-think' not in s
s = add_css(s)
s = rep(s, DOTS, '<sc-if value="{{waiting}}" hint-placeholder-val="{{false}}">' + ui('{{think}}') + '</sc-if>')
s = rep(s, "i: 0, phase: 'wait' };", "i: 0, phase: 'wait', step: 0 };")
s = rep(s, "    this.t0 = setTimeout(() => {\n      this.setState({ phase: 'typing' });",
           "    this.ts = setInterval(() => this.setState({ step: Math.min(this.state.step + 1, 2) }), 950);\n    this.t0 = setTimeout(() => {\n      clearInterval(this.ts);\n      this.setState({ phase: 'typing' });")
s = rep(s, "    }, 1300);\n  }", "    }, 2900);\n  }")
s = rep(s, "componentWillUnmount() { clearTimeout(this.t0);", "componentWillUnmount() { clearInterval(this.ts); clearTimeout(this.t0);")
s = rep(s, "      waiting: phase === 'wait',", "      think: this.name() + [' is reading your profile…', ' is getting to know Data Analysis…', ' is writing to you…'][this.state.step],\n      waiting: phase === 'wait',")
wr('CR-ONB-006.dc.html', s)

# CR-ONB-007 · How should Nova work with you? (re-thinks on every style change)
s = rd('CR-ONB-007.dc.html'); assert 'nv-think' not in s
s = add_css(s)
s = rep(s, DOTS, '<sc-if value="{{waiting}}" hint-placeholder-val="{{false}}">' + ui('{{think}}') + '</sc-if>')
s = rep(s, "i: 0, phase: 'wait' }; }", "i: 0, phase: 'wait', step: 0 }; }")
s = rep(s, "    this.t0 = setTimeout(() => this.type(), 1100);\n  }", "    this.think();\n  }")
s = rep(s, "  componentWillUnmount() { clearTimeout(this.t0); clearInterval(this.iv); }",
           "  componentWillUnmount() { clearTimeout(this.t0); clearInterval(this.iv); clearInterval(this.ts); }\n"
           "  think() {\n    clearTimeout(this.t0); clearInterval(this.iv); clearInterval(this.ts);\n    this.setState({ phase: 'wait', step: 0 });\n"
           "    this.ts = setInterval(() => this.setState({ step: Math.min(this.state.step + 1, 2) }), 800);\n"
           "    this.t0 = setTimeout(() => { clearInterval(this.ts); this.type(); }, 2400);\n  }")
s = rep(s, "else this.type(); });", "else this.think(); });")
s = rep(s, "waiting: phase === 'wait', typing: phase === 'typing' };",
           "think: ['Nova is reading your outcomes…', 'Nova is thinking it through…', 'Nova is writing in your style…'][this.state.step], waiting: phase === 'wait', typing: phase === 'typing' };")
wr('CR-ONB-007.dc.html', s)

# CR-CREATE-002A · Nova chat (after each answer) + drafting
s = rd('CR-CREATE-002A.dc.html'); assert 'nv-think' not in s
s = add_css(s)
s, n = re.subn(r'<span class="fx-dots" aria-label="Nova is typing">.*?</span></span>', ui('{{m.think}}'), s, flags=re.S); assert n == 1
s = rep(s, '<span class="fx-hint" style="margin: 0">Nova is drafting your course…</span>', ui('{{draftText}}'))
s = rep(s, "  componentWillUnmount() { clearTimeout(this.t); }", "  componentWillUnmount() { clearTimeout(this.t); clearInterval(this.ts); }")
s = rep(s, "    this.setState({ answers: [...this.state.answers, t], text: '', typing: true });\n    this.t = setTimeout(() => this.setState({ typing: false }), 700);",
           "    this.setState({ answers: [...this.state.answers, t], text: '', typing: true, step: 0 });\n"
           "    clearInterval(this.ts); this.ts = setInterval(() => this.setState({ step: Math.min((this.state.step || 0) + 1, 2) }), 700);\n"
           "    this.t = setTimeout(() => { clearInterval(this.ts); this.setState({ typing: false }); }, 2100);")
s = rep(s, "      draft: () => { this.setState({ phase: 'drafting' }); this.t = setTimeout(() => this.setState({ phase: 'proposal' }), 1600); },",
           "      draft: () => { this.setState({ phase: 'drafting', step: 0 }); clearInterval(this.ts); this.ts = setInterval(() => this.setState({ step: Math.min((this.state.step || 0) + 1, 2) }), 900); this.t = setTimeout(() => { clearInterval(this.ts); this.setState({ phase: 'proposal' }); }, 2700); },\n"
           "      draftText: ['Nova is reading your answers…', 'Nova is shaping the chapters…', 'Nova is writing your draft…'][this.state.step || 0],")
s = rep(s, "    return {\n", "    msgs.forEach((m) => { m.think = ['Reading your answer…', 'Thinking it through…', 'Writing…'][this.state.step || 0]; });\n    return {\n")
wr('CR-CREATE-002A.dc.html', s)
print('patched 006, 007, 002A')
