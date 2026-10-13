# confetti.py: shared success confetti (designer 2026-10-13 "all success screens should have confetti").
# A burst of pieces from the green tick that falls away and disappears (designer 2026-10-13 "confetti should not stuck anywhere");
# nothing stays on screen. Plays in Play mode / live only. Insert CONF inside the emblem (position:relative), add CSS once.
import random
_r = random.Random(7)
COL = ['#1652F0', '#6E96FF', '#AFC1F5', '#F6C343', '#0F6B45', '#3BB273', '#1652F0', '#F6C343']
def _pieces(n=32):
    out = []
    while len(out) < n:
        x = _r.uniform(-310, 310); y = _r.uniform(-74, 30)
        if abs(x) < 74 and y > -62: continue          # keep the tick itself clear
        if abs(x) < 150 and y > 10: continue           # keep the pill / H1 under the tick clear
        k = _r.random()
        w, h, br = (7, 7, '50%') if k < .3 else ((4, 15, '2px') if k < .55 else (7, 11, '2px'))
        out.append(f'<i style="--x:{x:.0f};--y:{y:.0f};--r:{_r.randint(-70, 70)}deg;width:{w}px;height:{h}px;border-radius:{br};background:{_r.choice(COL)};animation-delay:{_r.uniform(.25, .55):.2f}s"></i>')
    return out
CONF = '<span class="cf" aria-hidden="true">' + ''.join(_pieces()) + '</span>'
CSS = """
/* confetti.py success burst */
.cf{position:absolute;left:50%;top:50%;width:0;height:0;pointer-events:none;z-index:0;--k:1}
.cf i{position:absolute;left:0;top:0;display:block;opacity:0;animation:cfFall 2.8s cubic-bezier(.2,.7,.4,1) both}
@keyframes cfFall{
0%{opacity:0;transform:translate(-50%,-50%) scale(.3) rotate(0)}
8%{opacity:1}
22%{opacity:1;transform:translate(calc(var(--x) * var(--k) * 1px - 50%),calc(var(--y) * 1px - 50%)) rotate(var(--r))}
75%{opacity:.9}
100%{opacity:0;transform:translate(calc(var(--x) * var(--k) * 1.12px - 50%),calc(var(--y) * 1px + 340px)) rotate(calc(var(--r) + 260deg))}}
@media (max-width: 960px){.cf{--k:.56}}
@media (prefers-reduced-motion: reduce){.cf{display:none}}
"""
def add_css(s):
    if '/* confetti.py success burst */' in s: return s
    i = s.rfind('</style>', 0, s.find('</helmet>')); return s[:i] + CSS + s[i:]
