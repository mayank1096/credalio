# confetti.py: shared success confetti (designer 2026-10-13: "all success screens should have confetti", "should not stuck anywhere",
# "motion is not natural"). Real-confetti physics in CSS, one burst from the green tick:
#   i = flight path: fast burst outward that slows to a peak, then a drag-limited fall, fading at the end (per-piece speed);
#   b = side-to-side sway while falling;  s = the paper piece itself, flipping in 3D at its own rate.
# Nothing stays on screen. Plays in Play mode / live only. Insert CONF inside the emblem (position:relative), add CSS once.
import random
_r = random.Random(11)
COL = ['#1652F0', '#6E96FF', '#AFC1F5', '#F6C343', '#0F6B45', '#3BB273', '#1652F0', '#F6C343']
def _pieces(n=34):
    out = []
    while len(out) < n:
        x = _r.uniform(-320, 320); y = _r.uniform(-150, -10)
        if abs(x) < 60: continue
        k = _r.random()
        w, h, br = (7, 7, '50%') if k < .22 else ((5, 12, '1.5px') if k < .6 else (8, 10, '1.5px'))
        out.append('<i style="--x:%d;--y:%d;--f:%d;--d:%.2fs;--dl:%.2fs;--sw:%dpx;--sd:%.2fs;--fd:%.2fs;--rx:%.2f;--r:%ddeg">'
                   '<b><s style="width:%dpx;height:%dpx;border-radius:%s;background:%s"></s></b></i>' % (
                   x, y, _r.uniform(380, 480), _r.uniform(2.6, 3.8), _r.uniform(.18, .5), _r.uniform(6, 16), _r.uniform(.45, .9),
                   _r.uniform(.55, 1.3), _r.uniform(-1, 1), _r.randint(-80, 80), w, h, br, _r.choice(COL)))
    return out
CONF = '<span class="cf" aria-hidden="true">' + ''.join(_pieces()) + '</span>'
CSS = """
/* confetti.py success burst */
.cf{position:absolute;left:50%;top:50%;width:0;height:0;pointer-events:none;z-index:0;--k:1}
.cf i{position:absolute;left:0;top:0;display:block;opacity:0;animation:cfPath var(--d) var(--dl) both}
.cf b{display:block;animation:cfSway var(--sd) ease-in-out infinite alternate}
.cf s{display:block;transform:rotate(var(--r));animation:cfFlip var(--fd) linear infinite}
@keyframes cfPath{
0%{opacity:0;transform:translate(-50%,-50%);animation-timing-function:cubic-bezier(.1,.7,.25,1)}
5%{opacity:1}
24%{transform:translate(calc(var(--x) * var(--k) * 1px - 50%),calc(var(--y) * 1px - 50%));animation-timing-function:cubic-bezier(.42,.08,.7,.92)}
86%{opacity:1}
100%{opacity:0;transform:translate(calc(var(--x) * var(--k) * 1.22px - 50%),calc((var(--y) + var(--f)) * 1px))}}
@keyframes cfSway{from{transform:translateX(calc(var(--sw) * -1)) rotate(-12deg)}to{transform:translateX(var(--sw)) rotate(12deg)}}
@keyframes cfFlip{from{transform:rotate(var(--r)) rotate3d(var(--rx),1,0,0deg)}to{transform:rotate(var(--r)) rotate3d(var(--rx),1,0,360deg)}}
@media (max-width: 960px){.cf{--k:.56}}
@media (prefers-reduced-motion: reduce){.cf{display:none}}
"""
def add_css(s):
    if '/* confetti.py success burst */' in s: return s
    i = s.rfind('</style>', 0, s.find('</helmet>')); return s[:i] + CSS + s[i:]
