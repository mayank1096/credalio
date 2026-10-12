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
def lesson(tpl, mod, mname, steps, cur, mins, h1, lead, note, figure, prev, nxt, title):
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
    return re.sub(r'<title>.*?</title>', f'<title>{title}</title>', s)
