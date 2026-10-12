# ori_m.py: Link 1 orientation lessons (ORI-Mn-*) from the LIVE player files.
# lesson(): template LIVE CR-ORI-003 (lesson page: rail, eyebrow, H1, lead, optional note, figure, Ask Nova, Prev/Next bar)
# check():  template LIVE CR-ORI-004 (two questions); one source CR-ORI-Mn-K, variants none / right / wrong (= K1 / K2 / K3)
import re, os
ICO = {
 'book': '<path d="M2.5 5.5C5 4 8.5 4 12 6c3.5-2 7-2 9.5-.5V19c-2.5-1.5-6-1.5-9.5.5-3.5-2-7-2-9.5-.5z"></path><path d="M12 6v13.5"></path>',
 'shield': '<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"></path><path d="m9 12 2 2 4-4"></path>',
 'cap': '<path d="M2 9.5 12 5l10 4.5-10 4.5z"></path><path d="M6 11.5v4.5c3.5 2.5 8.5 2.5 12 0v-4.5"></path>',
 'pen': '<path d="M12 20h9"></path><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"></path>',
 'rocket': '<path d="M5 15c-1.5 1.5-2 4-2 6 2 0 4.5-.5 6-2"></path><path d="M9 15 6.5 12.5C8 7 12.5 3.5 20.5 3.5c0 8-3.5 12.5-9 14z"></path><circle cx="15" cy="9" r="1.6"></circle>',
 'info': '<circle cx="12" cy="12" r="9"></circle><path d="M12 11v5"></path><path d="M12 7.6v.2"></path>',
 'play': '<path d="M8 5.5v13l11-6.5z" fill="currentColor"></path>',
}
def svg(k, w=20, sw=1.9): return f'<svg width="{w}" height="{w}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICO[k]}</svg>'
CHK = '<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg>'
LESSON_CSS = """
/* lesson breathing room (designer: too stuffed vertically) */
@media (min-width: 961px){
.ls-top .lp-p{margin-top:20px}
.ls-top + .ls-roles,.ls-top + .vc2,.ls-top + .ls-cmp,.ls-top + .ls-vid{margin-top:40px}
.ls-roles li{padding:20px}
.ls-roles{gap:16px}
.lp-main .lp-ask{margin-top:40px}
}
/* rail breathing room (designer: too stuffed vertically) */
.lp-rail{width:264px}
.lp-rl{margin-bottom:20px}
.lp-o{min-height:68px}
.lp-ot{gap:4px}
.lp-ol::before{top:22px;bottom:22px}
/* ori_m lesson blocks */
@media (min-width: 961px){.vc3{grid-template-columns:minmax(0,1fr) 36px minmax(0,1fr) 36px minmax(0,1fr)}}
.ls-gk{padding:16px 18px;border-radius:18px;background:#F5F8FF;border:1.5px solid #E6EAF3;display:flex;flex-direction:column;gap:4px}
.ls-gk i{width:28px;height:28px;border-radius:9px;background:#FFFFFF;color:#1652F0;display:flex;align-items:center;justify-content:center;margin-bottom:6px}
.ls-gk b{font-size:14px;font-weight:600}.ls-gk span{font-size:13.5px;line-height:1.5;color:#4A5578}
.ls-vid{position:relative;margin:24px 0 0 0;border-radius:22px;overflow:hidden;aspect-ratio:10/3;background:#F7F9FD url(/_blob/35f92c519316f253dc620c3c4b2d859c) center 70% / 104% auto no-repeat;border:1.5px solid #E6EAF3}
.ls-vid::after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(255,255,255,0) 40%,rgba(11,20,51,.10))}
.ls-play{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);z-index:1;width:64px;height:64px;border-radius:50%;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 10px rgba(22,82,240,.14),0 14px 30px rgba(22,82,240,.30)}
.ls-cap{position:absolute;left:16px;bottom:14px;z-index:1;display:inline-flex;align-items:center;height:32px;padding:0 12px;border-radius:999px;background:#FFFFFF;color:#0B1433;font-size:13px;font-weight:500;box-shadow:0 4px 14px rgba(11,20,51,.10)}
.ls-roles{list-style:none;margin:12px 0 0 0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.ls-roles li{display:grid;grid-template-columns:40px minmax(0,1fr);column-gap:12px;row-gap:1px;align-items:center;padding:14px 16px;border-radius:16px;background:#FFFFFF;border:1.5px solid #E6EAF3}
.ls-roles li .vc-i{grid-row:span 2;margin:0}
.ls-roles b{font-size:15px;font-weight:600;align-self:end}.ls-roles span:last-child{font-size:13px;line-height:1.4;color:#5B6582;align-self:start}
@media (max-width: 960px){
.ls-vid{aspect-ratio:16/10;margin-top:20px;border-radius:18px;background-size:190% auto}
.ls-play{width:56px;height:56px}
.ls-roles{grid-template-columns:minmax(0,1fr);gap:8px}
.ls-roles li{padding:12px 14px;grid-template-columns:36px minmax(0,1fr)}
.ls-roles li .vc-i{width:36px;height:36px}
.ls-gk{order:2}
}
"""
def _head(s, mod, mname, steps, cur, tn):
    s = re.sub(r'<span class="lp-t2">Module \d+ · [^<]*</span>', f'<span class="lp-t2">Module {mod} · {mname}</span>', s, count=1)
    segs = ''.join(f'<span class="lp-seg lp-seg-{"done" if i < cur else ("cur" if i == cur else "todo")}"></span>' for i in range(len(steps)))
    s = re.sub(r'<div class="lp-segs" aria-hidden="true">.*?</div>', f'<div class="lp-segs" aria-hidden="true">{segs}</div>', s, count=1, flags=re.S)
    return re.sub(r'<span class="lp-tn">[^<]*</span>', f'<span class="lp-tn">{tn}</span>', s, count=1)
def _foot(s, prev_href, prev_label, n, total, next_href, next_label, dyn=False):
    a0 = s.index('<footer class="lp-bar">'); a1 = s.index('</footer>', a0)
    f = s[a0:a1]
    f = re.sub(r'<a href="[^"]*" class="lp-prev">', f'<a href="{prev_href}" class="lp-prev">', f, count=1)
    f = re.sub(r'<span class="lp-hide-sm">[^<]*</span>', f'<span class="lp-hide-sm">{prev_label}</span>', f, count=1)
    f = re.sub(r'<span class="lp-stepn">[^<]*</span>', f'<span class="lp-stepn">Step {n} of {total}</span>', f, count=1)
    f = re.sub(r'(<a href=")[^"]*(" class="ds-btn lp-next)', rf'\g<1>{next_href}\g<2>', f, count=1)
    if not dyn: f = re.sub(r'(class="ds-btn lp-next[^"]*"[^>]*><span>)[^<]*(</span>)', rf'\g<1>{next_label}\g<2>', f, count=1)
    return s[:a0] + f + s[a1:]
SCENE_CSS = """
/* campus scene filler at the bottom (designer 2026-10-12) */
.lp-root{position:relative;isolation:isolate}
.lp-scene ~ .lp-body{background-color:transparent !important}
.lp-scene{position:absolute;left:0;right:0;bottom:0;height:min(44vh,38vw);background:url(/_blob/6acc9dd1cd600c17d2fd6381a3069aaa) 50% 100% / cover no-repeat;z-index:-1;pointer-events:none}
@media (max-width: 960px){.lp-scene{height:220px;background-size:250% auto;background-position:52% 100%}}
"""
def add_scene(s):
    if 'lp-scene' in s: return s
    s = s.replace('<div class="lp-root">', '<div class="lp-root"><div class="lp-scene" aria-hidden="true"></div>', 1)
    i = s.rfind('</style>', 0, s.find('</helmet>')); return s[:i] + SCENE_CSS + s[i:]
def lesson(tpl, mod, mname, steps, cur, mins, h1, lead, note, figure, prev, nxt, title, scene=False):
    s = _head(tpl, mod, mname, steps, cur, f'Step {cur + 1} of {len(steps)}')
    rows = ''
    for i, (t, k) in enumerate(steps):
        st = 'done' if i < cur else ('cur' if i == cur else 'todo')
        rows += f'<li class="lp-o lp-o-{st}"><span class="lp-om">{CHK if st == "done" else ""}</span><span class="lp-ot"><b>{t}</b><span>{k}</span></span></li>'
    s = re.sub(r'<aside class="lp-rail" aria-label="Module steps">.*?</aside>', f'<aside class="lp-rail" aria-label="Module steps"><span class="lp-rl">Module {mod} · {mname}</span><ol class="lp-ol">{rows}</ol></aside>', s, count=1, flags=re.S)
    m0 = s.index('<main class="lp-main">') + len('<main class="lp-main">'); m1 = s.index('<a href="#" class="lp-ask', m0)
    top = (f'<div class="ls-top"><div><span class="lp-eb ob-in">About {mins} min read</span>'
           f'<h1 class="lp-h1 ob-in">{h1}</h1><p class="lp-p ob-in2">{lead}</p></div>' + (note or '') + '</div>')
    s = s[:m0] + top + figure + s[m1:]
    s = _foot(s, prev[0], prev[1], cur + 1, len(steps), nxt[0], nxt[1])
    i = s.rfind('</style>', 0, s.find('</helmet>')); s = s[:i] + LESSON_CSS + s[i:]
    if scene: s = add_scene(s)
    return re.sub(r'<title>.*?</title>', f'<title>{title}</title>', s)
def note(head, text, icon='info'):
    return f'<aside class="ls-gk ob-in3"><i>{svg(icon, 16, 2.2)}</i><b>{head}</b><span>{text}</span></aside>'
def flow(nodes, hub=1):
    out = '<figure class="vc2 vc3 ob-in3" aria-label="How it works">'
    for i, (ic, b, t) in enumerate(nodes):
        if i: out += '<span class="vc2-l" aria-hidden="true"></span>'
        out += f'<div class="vc2-n{" vc2-hub" if i == hub else ""}"><span class="vc-i">{svg(ic)}</span><b>{b}</b><span>{t}</span></div>'
    return out + '</figure>'
def video(caption):
    return f'<figure class="ls-vid ob-in3" aria-label="{caption}"><span class="ls-play">{svg("play", 24, 0)}</span><figcaption class="ls-cap">{caption}</figcaption></figure>'
def roles(items):
    return '<ul class="ls-roles ob-in3">' + ''.join(f'<li><span class="vc-i">{svg(ic)}</span><b>{b}</b><span>{t}</span></li>' for ic, b, t in items) + '</ul>'
def check(tpl, mod, mname, steps, Q, prev, done_href, title):
    n = len(steps)
    s = _head(tpl, mod, mname, steps, n - 1, f'Step {n} of {n}')
    q = ',\n      '.join("[" + ", ".join(repr(x) if not isinstance(x, list) else "[" + ", ".join(repr(y) for y in x) + "]" for x in qq) + "]" for qq in Q)
    s = re.sub(r'const Q = \[.*?\n    \];', 'const Q = [\n      ' + q + '\n    ];', s, count=1, flags=re.S)
    s = s.replace("constructor(props) { super(props); this.state = { a: [1, -1] }; }",
                  "constructor(props) { super(props); const v = (props && props.variant) || 'none'; this.state = { a: v === 'right' ? [" + str(Q[0][3]) + ", " + str(Q[1][3]) + "] : (v === 'wrong' ? [" + str((Q[0][3] + 1) % len(Q[0][2])) + ", -1] : [-1, -1]) }; }", 1)
    assert "props.variant" in s
    s = re.sub(r'<p class="lp-meta ob-in2">[^<]*</p>', '', s, count=1)
    s = _foot(s, prev[0], prev[1], n, n, done_href, '', dyn=True)
    s = add_scene(s)
    return re.sub(r'<title>.*?</title>', f'<title>{title}</title>', s)

# ---------- module overview (template LIVE CR-ORI-M1-00) / module complete (template LIVE CR-ORI-006) / compare figure ----------
ICO.update({
 'target': '<circle cx="12" cy="12" r="8.5"></circle><circle cx="12" cy="12" r="4.5"></circle><circle cx="12" cy="12" r="1" fill="currentColor"></circle>',
 'check': '<circle cx="12" cy="12" r="9"></circle><path d="m8 12.5 3 3 5-6"></path>',
 'doc': '<path d="M7 3h7l5 5v13H7z"></path><path d="M14 3v5h5"></path><path d="M10 13h6M10 17h4"></path>',
 'x': '<path d="M7 7l10 10M17 7 7 17"></path>',
})
TICK14 = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg>'
def overview(tpl, mod, mname, steps, mins, desc, hi, takeaways, start_href, title):
    s = _head(tpl, mod, mname, steps, 0, f'{len(steps)} steps')
    s = re.sub(r'<span class="lp-eb ob-in">Module \d+ of 7</span>', f'<span class="lp-eb ob-in">Module {mod} of 7</span>', s, count=1)
    s = re.sub(r'<h1 class="lp-h1 ob-in">[^<]*</h1>', f'<h1 class="lp-h1 ob-in">{mname}</h1>', s, count=1)
    s = re.sub(r'<p class="mo-desc ob-in2">[^<]*</p>', f'<p class="mo-desc ob-in2">{desc}</p>', s, count=1)
    s = re.sub(r'About \d+ minutes</span>', f'About {mins} minutes</span>', s, count=1)
    s = re.sub(r'<span class="mo-hi-b">[^<]*</span>', f'<span class="mo-hi-b">{hi}</span>', s, count=1)
    s = re.sub(r'<a href="[^"]*" class="ds-btn mo-go mo-go-new', f'<a href="{start_href}" class="ds-btn mo-go mo-go-new', s, count=1)
    l0 = s.index('<ol class="mo-list">'); l1 = s.index('</ol>', l0) + 5
    nx = re.search(r'<li class="mo-r mo-next">.*?</li>', s[l0:l1], re.S).group(0); td = re.search(r'<li class="mo-r mo-todo">.*?</li>', s[l0:l1], re.S).group(0)
    def li(t, k, tpl_li, old):
        return re.sub(r'<b>[^<]*</b><span>[^<]*</span>', f'<b>{t}</b><span>{k}</span>', tpl_li, count=1)
    s = s[:l0] + '<ol class="mo-list">' + ''.join(li(t, k, nx if i == 0 else td, None) for i, (t, k) in enumerate(steps)) + '</ol>' + s[l1:]
    u0 = s.index('<ul class="mo-ll">'); u1 = s.index('</ul>', u0) + 5
    tick = re.search(r'<li>(<svg.*?</svg>)', s[u0:u1], re.S).group(1)
    s = s[:u0] + '<ul class="mo-ll">' + ''.join(f'<li>{tick}<span>{t}</span></li>' for t in takeaways) + '</ul>' + s[u1:]
    return re.sub(r'<title>.*?</title>', f'<title>{title}</title>', s)
def done(tpl, mod, mname, nsteps, sub, learned, duties, next_href, title):
    s = re.sub(r'<span class="lp-t2">Module \d+ · [^<]*</span>', f'<span class="lp-t2">Module {mod} · {mname}</span>', tpl, count=1)
    s = re.sub(r'<div class="lp-segs" aria-hidden="true">.*?</div>', '<div class="lp-segs" aria-hidden="true">' + '<span class="lp-seg lp-seg-done"></span>' * nsteps + '</div>', s, count=1, flags=re.S)
    s = re.sub(r'<span class="lp-tn">[^<]*</span>', f'<span class="lp-tn">{nsteps} steps</span>', s, count=1)
    s = re.sub(r'>Module \d+ complete</span>', f'>Module {mod} complete</span>', s, count=1)
    s = re.sub(r'<h1 class="lp-h1 dn-h ob-in2">[^<]*</h1>', f'<h1 class="lp-h1 dn-h ob-in2">{mname}</h1>', s, count=1)
    s = re.sub(r'<p class="dn-sub ob-in2">[^<]*</p>', f'<p class="dn-sub ob-in2">{sub}</p>', s, count=1)
    dd = re.search(r'<span class="dn-n dn-d">(<svg.*?</svg>)</span>', s, re.S).group(1)
    path = ''.join(f'<span class="dn-n dn-d{" dn-just" if i == mod else ""}">{dd}</span>' if i <= mod else f'<span class="dn-n ">{i}</span>' for i in range(1, 8))
    s = re.sub(r'<div class="dn-path ob-in3" aria-label="[^"]*">.*?</div>', f'<div class="dn-path ob-in3" aria-label="{mod} of 7 modules complete">{path}</div>', s, count=1, flags=re.S)
    s = re.sub(r'<ul class="dn-l">.*?</ul>', '<ul class="dn-l">' + ''.join(f'<li>{TICK14}<span>{t}</span></li>' for t in learned) + '</ul>', s, count=1, flags=re.S)
    s = re.sub(r'<ul class="dn-l dn-l2">.*?</ul>', '<ul class="dn-l dn-l2">' + ''.join(f'<li><span class="dn-dot"></span><span>{t}</span></li>' for t in duties) + '</ul>', s, count=1, flags=re.S)
    s = re.sub(r'<a href="[^"]*" class="ds-btn dn-go">', f'<a href="{next_href}" class="ds-btn dn-go">', s, count=1)
    return re.sub(r'<title>.*?</title>', f'<title>{title}</title>', s)
COMPARE_CSS = """
/* ori_m compare */
.ls-cmp{margin:28px 0 0 0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.ls-cmp > div{display:flex;flex-direction:column;gap:10px;padding:20px;border-radius:18px;border:1.5px solid #E6EAF3;background:#FFFFFF}
.ls-cmp .cmp-h{display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:500;color:#5B6582}
.ls-cmp .cmp-h i{width:24px;height:24px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:#F1F3F8;color:#8A93AD}
.ls-cmp .cmp-ok{border-color:#BFE3CF;background:#F3FBF6}
.ls-cmp .cmp-ok .cmp-h{color:#0F6B45}.ls-cmp .cmp-ok .cmp-h i{background:#0F6B45;color:#FFFFFF}
.ls-cmp p{margin:0;font-size:16px;line-height:1.55;color:#1F2A4D}
.ls-cmp .cmp-no p{color:#5B6582}
@media (max-width: 960px){.ls-cmp{grid-template-columns:minmax(0,1fr);gap:10px;margin-top:20px}.ls-cmp > div{padding:16px}.ls-cmp p{font-size:15px}}
"""
def compare(weak, strong):
    return ('<figure class="ls-cmp ob-in3" aria-label="Weak and strong example">'
            f'<div class="cmp-no"><span class="cmp-h"><i>{svg("x", 13, 2.6)}</i>Weak</span><p>{weak}</p></div>'
            f'<div class="cmp-ok"><span class="cmp-h"><i>{svg("check", 14, 2.2)}</i>Strong</span><p>{strong}</p></div></figure>')
def with_css(s, css):
    i = s.rfind('</style>', 0, s.find('</helmet>')); return s[:i] + css + s[i:]
