"""Designer 2026-10-18 follow-up ("I can't see where Nova is thinking"): make the thinking state unmistakable and reviewable on the canvas.
- While thinking: Nova's figure gets a breathing cobalt aura, the reply bubble gets a moving cobalt gradient border + soft glow,
  the status line is bigger (16px) and lasts longer (~3.6 s).
- New frozen boards CR-ONB-006t / CR-ONB-007t (+ Mobile) = variant "thinking" (no timers), so the state shows without Play mode.
Run after think1018.py. Usage: python3 think1018b.py <canvas/project dir>"""
import json, os, sys
P = sys.argv[1]
rd = lambda f: open(os.path.join(P, f)).read()
def wr(f, s): open(os.path.join(P, f), 'w').write(s)
def rep(s, old, new, n=1):
    assert s.count(old) == n, (old[:90], s.count(old)); return s.replace(old, new)

CSS = r'''@keyframes nvAura{0%,100%{opacity:.55;transform:translate(-50%,-50%) scale(.92)}50%{opacity:1;transform:translate(-50%,-50%) scale(1.04)}}
@keyframes nvBorder{from{background-position:0 0,0% 0}to{background-position:0 0,300% 0}}
.nv-aura{position:absolute;left:50%;top:42%;width:118%;aspect-ratio:1;border-radius:50%;background:radial-gradient(closest-side,rgba(22,82,240,.24),rgba(110,150,255,.12) 55%,rgba(22,82,240,0));transform:translate(-50%,-50%);animation:nvAura 1.8s ease-in-out infinite;pointer-events:none}
.nv-bub{border-color:transparent !important;background:linear-gradient(#F5F8FF,#F5F8FF) padding-box,linear-gradient(90deg,#1652F0,#C9D8FF,#6E96FF,#DCE5FB,#1652F0) border-box !important;background-size:100% 100%,300% 100% !important;box-shadow:0 0 0 5px rgba(22,82,240,.07),0 14px 34px rgba(22,82,240,.14);animation:nvBorder 2.2s linear infinite,cpPop .45s ease both !important}
.nv-think .nv-tt{font-size:16px}
.nv-think .nv-orb{width:26px;height:26px}
@media (prefers-reduced-motion: reduce){.nv-aura,.nv-bub{animation:none !important}}'''

for f, h, frozen in [('CR-ONB-006.dc.html', 'min-height: 52px', "    if (this.props && this.props.variant === 'thinking') { this.setState({ step: 1 }); return; }\n"),
                     ('CR-ONB-007.dc.html', 'min-height: 104px', "    if (this.props && this.props.variant === 'thinking') { this.setState({ step: 1 }); return; }\n")]:
    s = rd(f); assert 'nv-aura' not in s
    s = rep(s, '</style>', CSS + '\n</style>')
    s = rep(s, '<div style="position: relative; align-self: start">',
            '<div style="position: relative; align-self: start"><sc-if value="{{waiting}}" hint-placeholder-val="{{false}}"><span class="nv-aura" aria-hidden="true"></span></sc-if>')
    s = rep(s, '<div class="cp-pop" style="max-width: 560px; padding: 16px 18px; border-radius: 20px 20px 20px 6px; background: #F5F8FF; border: 1.5px solid #E6EAF3; font-size: 16px; line-height: 1.55; color: #0B1433; %s; box-sizing: border-box">' % h,
            '<div class="cp-pop {{bubCls}}" style="max-width: 560px; padding: 16px 18px; border-radius: 20px 20px 20px 6px; background: #F5F8FF; border: 1.5px solid #E6EAF3; font-size: 16px; line-height: 1.55; color: #0B1433; %s; box-sizing: border-box">' % h)
    s = rep(s, "waiting: phase === 'wait'", "bubCls: phase === 'wait' ? 'nv-bub' : '', waiting: phase === 'wait'")
    if f == 'CR-ONB-006.dc.html':
        s = rep(s, "    if (reduce) { this.setState({ phase: 'done', i: 9999 }); return; }\n", frozen + "    if (reduce) { this.setState({ phase: 'done', i: 9999 }); return; }\n")
        s = rep(s, "Math.min(this.state.step + 1, 2) }), 950);", "Math.min(this.state.step + 1, 2) }), 1200);")
        s = rep(s, "    }, 2900);\n  }", "    }, 3600);\n  }")
    else:
        s = rep(s, "    this.reduce = typeof matchMedia", frozen + "    this.reduce = typeof matchMedia")
        s = rep(s, "Math.min(this.state.step + 1, 2) }), 800);", "Math.min(this.state.step + 1, 2) }), 1100);")
        s = rep(s, "this.type(); }, 2400);", "this.type(); }, 3300);")
    wr(f, s)

def wrap(title, src, hint):
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>%s</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n'
            '<dc-import name="%s" variant="thinking" hint-size="%s"></dc-import>\n</x-dc>\n</body>\n</html>\n') % (title, src, hint)
cj = os.path.join(P, 'canvas.json'); d = json.load(open(cj)); B = d['boards']
assert 'CR-ONB-006t.dc.html' not in B
for src, t in [('CR-ONB-006', 'Meet your Copilot · Nova thinking'), ('CR-ONB-007', 'How should Nova help · Nova thinking')]:
    b = src + 't'; mh = B[src + '-Mobile.dc.html']['h']
    wr(b + '.dc.html', wrap('%s · %s' % (b, t), src, '1440px,820px'))
    wr(b + '-Mobile.dc.html', wrap('%s · %s · Mobile' % (b, t), src, '390px,%dpx' % mh))
    Y = B[src + '.dc.html']['y']; X = B[src + '.dc.html']['x'] + 2070
    for k, v in B.items():
        if v.get('page', 'p1') == 'p1' and v['y'] == Y and v['x'] >= X: v['x'] += 2070
    for n in d['notes'].values():
        if n.get('page') == 'p1' and Y < n['y'] < Y + 1300 and n['x'] >= X: n['x'] += 2070
    B[b + '.dc.html'] = {'x': X, 'y': Y, 'w': 1440, 'h': 820, 'is_interactive': True, 'page': 'p1', 'title': '%s · %s · Desktop' % (b, t)}
    B[b + '-Mobile.dc.html'] = {'x': X + 1520, 'y': Y, 'w': 390, 'h': mh, 'is_interactive': True, 'page': 'p1', 'title': '%s · Mobile' % b}
    d['notes']['new-' + b] = {'text': 'NEW · Nova thinking state · ' + b, 'x': X, 'y': Y + 1010, 'w': 1910, 'fill': 'red', 'page': 'p1'}
    o = [k for k in d['order'] if not k.startswith(b + '.') and not k.startswith(b + '-')]
    i = o.index(src + '-Mobile.dc.html') + 1
    d['order'] = o[:i] + [b + '.dc.html', b + '-Mobile.dc.html'] + o[i:]
Y = B['CR-ONB-006.dc.html']['y']
row = sorted((v['x'], v['x'] + v['w'], k) for k, v in B.items() if v.get('page', 'p1') == 'p1' and v['y'] == Y)
for a, c in zip(row, row[1:]): assert a[1] <= c[0], (a, c)
json.dump(d, open(cj, 'w'), ensure_ascii=False, indent=2, sort_keys=True)
print('ok')
