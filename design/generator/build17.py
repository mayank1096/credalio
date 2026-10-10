# build17: Studio pages on the CR-DASH-NEW shell — CR-NOT-001 (Notification Centre), CR-HOME-EXP (My learning experiences),
# CR-HOME-NEW (Create new), CR-HOME-SET (Settings · AI preferences). The bell dropdown is CR-DASH-ST variant "bell" (build16).
# Built from the LIVE CR-DASH-NEW so logo / Creio / client copy carry over. Only writes its own files.
# usage: python3 build17.py <canvas project dir>
import re, sys, os
P = sys.argv[1]
rd = lambda f: open(os.path.join(P, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(P, f), 'w', encoding='utf-8').write(s)
def ic(paths, w=20, sw=1.9):
    return f'<svg width="{w}" height="{w}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>'
ARR = ic('<path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path>', 18, 2.4)
CHK = ic('<path d="m5 12.5 4.5 4.5L19 7.5"></path>', 13, 3)
CHEV = ic('<path d="m6 9 6 6 6-6"></path>', 16, 2.2)
PLUS = ic('<path d="M12 5v14M5 12h14"></path>', 18, 2.4)
I = {
 'val': '<path d="M12 3v18M5 21h14M6 7h12"></path><path d="m6 7-3 7a3 3 0 0 0 6 0zM18 7l-3 7a3 3 0 0 0 6 0z"></path>',
 'col': '<circle cx="9" cy="8" r="3.5"></circle><path d="M2.5 20a6.5 6.5 0 0 1 13 0"></path><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14.5a6.5 6.5 0 0 1 3.5 5.5"></path>',
 'at': '<circle cx="12" cy="12" r="4"></circle><path d="M16 8v5a3 3 0 0 0 6 0v-1a10 10 0 1 0-4 8"></path>',
 'sup': '<circle cx="12" cy="12" r="9"></circle><circle cx="12" cy="12" r="3.5"></circle><path d="m5.6 5.6 3.9 3.9M14.5 14.5l3.9 3.9M18.4 5.6l-3.9 3.9M9.5 14.5l-3.9 3.9"></path>',
 'chat': '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"></path>',
 'cal': '<rect x="3" y="5" width="18" height="16" rx="2"></rect><path d="M3 10h18M8 3v4M16 3v4"></path>',
 'card': '<rect x="3" y="6" width="18" height="14" rx="3"></rect><path d="M3 10h18M16 15h2"></path>',
 'doc': '<rect x="5" y="3" width="14" height="18" rx="2.5"></rect><path d="M9 8h6M9 12h6M9 16h3"></path>',
 'ok': '<circle cx="12" cy="12" r="9"></circle><path d="m8.5 12 2.5 2.5 4.5-5"></path>',
 'ai': '<path d="M12 3l1.9 5.6L19.5 10.5l-5.6 1.9L12 18l-1.9-5.6L4.5 10.5l5.6-1.9z"></path>',
 'coin': '<circle cx="12" cy="12" r="9"></circle><path d="M15 9.5c-.5-1-1.6-1.5-3-1.5-1.7 0-3 .9-3 2s1.3 1.7 3 2 3 .9 3 2-1.3 2-3 2c-1.4 0-2.5-.5-3-1.5M12 6v2M12 16v2"></path>',
 'star': '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"></path>',
 'book': '<path d="M4 19.5V5a2 2 0 0 1 2-2h14v18H6.5A2.5 2.5 0 0 1 4 18.5"></path><path d="M8 7h8"></path>',
 'cert': '<circle cx="12" cy="9" r="5"></circle><path d="m8.5 13.2-1.5 7.8 5-2.6 5 2.6-1.5-7.8"></path>',
 'path': '<circle cx="6" cy="18" r="2.5"></circle><circle cx="18" cy="6" r="2.5"></circle><path d="M8.5 18H15a3 3 0 0 0 0-6H9a3 3 0 0 1 0-6h6.5"></path>',
 'prog': '<rect x="3" y="5" width="18" height="16" rx="2"></rect><path d="M3 10h18M8 3v4M16 3v4M8 14h3M8 17h6"></path>',
 'set': '<circle cx="12" cy="12" r="3"></circle><path d="M12 2.5v2.2M12 19.3v2.2M4.6 4.6l1.6 1.6M17.8 17.8l1.6 1.6M2.5 12h2.2M19.3 12h2.2M4.6 19.4l1.6-1.6M17.8 6.2l1.6-1.6"></path>',
 'user': '<circle cx="12" cy="8" r="4"></circle><path d="M4 21a8 8 0 0 1 16 0"></path>',
 'lock': '<rect x="5" y="11" width="14" height="10" rx="2.5"></rect><path d="M8 11V8a4 4 0 0 1 8 0v3"></path>',
 'bell': '<path d="M18 16V11a6 6 0 1 0-12 0v5l-2 2h16z"></path><path d="M10 21h4"></path>',
 'eye': '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"></path><circle cx="12" cy="12" r="3"></circle>',
 'globe': '<circle cx="12" cy="12" r="9"></circle><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"></path>',
 'org': '<path d="M3 21h18M5 21V8l7-4 7 4v13M9 21v-6h6v6"></path>',
}

dsh = rd('CR-DASH-NEW.dc.html')
NOVA = re.search(r'<span aria-hidden="true" style="[^"]*"><img src="/_blob/b8f0756720795e1bd3b02e9c2655cb25" alt="" style="[^"]*"></span>', dsh).group(0)
NOVA40 = NOVA.replace('width: 26px; height: 26px;', 'width: 40px; height: 40px;')
CH = {  # Copilot heads (same crop as Nova head) — blobs from CLAUDE.md
 'Nova': '/_blob/b8f0756720795e1bd3b02e9c2655cb25', 'Maya': '/_blob/0539eaee91dd97c09ad321718b4b2947',
 'Alex': '/_blob/180b8d793cf8025b7bf4a7efeb6da0a2', 'Sage': '/_blob/e77858d41b6ddf496fcf2ad82ab9d64a'}
from cpx import head as _hc
def head(n, sz=34):
    t = NOVA.replace('width: 26px; height: 26px;', f'width: {sz}px; height: {sz}px;').replace(CH['Nova'], CH[n])
    a = _hc(n)
    return re.sub(r'left: [-\d.]+%; top: [-\d.]+%; width: [\d.]+%', f"left: {a['l']}; top: {a['t']}; width: {a['w']}", t)

def page(name, active_label, main, script_vals, css, title, state='{ nav: false }'):
    s = dsh
    s = s.replace('class="ds-item ds-on" aria-current="page"', 'class="ds-item"', 1)
    if active_label:
        m = re.search(r'<a href="[^"]*" class="ds-item"><svg(?:(?!</a>).)*?<span style="flex-grow: 1; min-width: 0">' + re.escape(active_label) + '</span>', s, re.S)
        s = s[:m.start()] + m.group(0).replace('class="ds-item"', 'class="ds-item ds-on" aria-current="page"', 1) + s[m.end():]
    # sidebar + bell links
    for lab, url in [('My learning experiences', 'CR-HOME-EXP.dc.html'), ('Create new', 'CR-HOME-NEW.dc.html'), ('Settings', 'CR-HOME-SET.dc.html')]:
        k = s.index('min-width: 0">' + lab + '</span>')
        a = s.rindex('<a href="', 0, k) + 9
        s = s[:a] + url + s[s.index('"', a):]
    s = s.replace('<a href="#" class="ds-icon-btn" aria-label="Notifications', '<a href="CR-NOT-001.dc.html" class="ds-icon-btn" aria-label="Notifications', 1)
    a0, a1 = s.index('<main class="ds-main">'), s.index('</main>') + 7
    s = s[:a0] + main + s[a1:]
    script = ("<script type=\"text/x-dc\" data-dc-script data-props='{\"$preview\":{\"width\":1440,\"height\":820}}'>\nclass Component extends DCLogic {\n"
              f"  constructor(props) {{ super(props); this.state = {state}; }}\n  renderVals() {{\n    const S = this.state;\n{script_vals}\n  }}\n}}\n</script>")
    s = s[:s.index('<script type="text/x-dc"')] + script + '\n</body>\n</html>\n'
    s = s.replace('</style>', BASE_CSS + css + '</style>', 1)
    s = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', s)
    wr(name + '.dc.html', s)

BASE_CSS = '''
/* build17 shared */
.hp{max-width:1240px}
.hp-head{display:flex;align-items:flex-end;justify-content:space-between;gap:20px;padding:22px 0 18px 0}
.hp-sub{margin:6px 0 0 0;font-size:15px;color:#4A5578}
.hp-lab{display:block;font-size:12.5px;font-weight:500;color:#8A93AD}
.hp-btn{height:48px;font-size:15px;padding:0 5px 0 20px;flex-shrink:0}
.hp-btn .ob-arrow{width:38px;height:38px}
.hp-rb{display:inline-flex;align-items:center;height:38px;padding:0 15px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;font-size:13.5px;font-weight:600;text-decoration:none;flex-shrink:0;font-family:inherit;cursor:pointer;white-space:nowrap}
.hp-tabs{display:flex;gap:8px;overflow-x:auto;scrollbar-width:none}
.hp-tab{display:inline-flex;align-items:center;gap:6px;height:38px;padding:0 15px;border-radius:999px;border:1.5px solid #E6EAF3;background:#FFFFFF;color:#3A4566;font-family:inherit;font-size:14px;font-weight:500;cursor:pointer;white-space:nowrap;flex-shrink:0}
.hp-tab em{font-style:normal;color:#8A93AD}
.hp-tab.on{background:#EAF0FF;border-color:#1652F0;color:#0E3BB8}.hp-tab.on em{color:#0E3BB8}
.hp-sw{position:relative;width:44px;height:26px;flex-shrink:0;border-radius:999px;border:0;background:#CBD3E6;cursor:pointer;transition:background .2s ease}
.hp-sw::after{content:'';position:absolute;top:3px;left:3px;width:20px;height:20px;border-radius:50%;background:#FFFFFF;box-shadow:0 1px 3px rgba(11,20,51,.2);transition:left .2s ease}
.hp-sw.on{background:#1652F0}.hp-sw.on::after{left:21px}
.hp-ic{width:40px;height:40px;flex-shrink:0;border-radius:12px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.hp-ic.am{background:#FFF1CF;color:#8A5300}.hp-ic.gr{background:#E7F5EE;color:#0F6B45}.hp-ic.gy{background:#F1F3F8;color:#5B6582}.hp-ic.gd{background:#FFF6DC;color:#8A6400}
@media (max-width: 960px){
.hp-head{flex-direction:column;align-items:stretch;gap:12px;padding:20px 0 14px 0}
.hp-head .hp-btn{width:100%;justify-content:space-between}
.hp-tabs{margin:0 -16px;padding:0 16px}
}
'''

# ======================= CR-NOT-001 · Notification Centre =======================
# (id, cat, group, icon, tone, title, context, when, action, unread)
NOTS = [
 ('n1', 'Validation', 'Today', 'val', 'am', 'Clarification requested for Data Analysis with SQL', 'Case VAL-00928 · Chapter 4 → Lesson 3', '10 min ago', 'Review', 1),
 ('ai1', 'AI', 'Today', 'coin', 'gd', 'Your Creio balance is getting low', '20,000 Creio left. Add more to keep working with Nova.', '1 h ago', 'Add Creio', 1),
 ('n2', 'Collaboration', 'Today', 'col', '', 'Dr. Bola Ade invited you to co-create Financial Modelling Basics', 'Role: Co-Creator', '1 h ago', 'Review', 1),
 ('n11', 'Learner support', 'Today', 'sup', '', 'Mary sent you a private support message', 'Data Analysis with SQL · Lesson 4.2', '1 h ago', 'Open', 0),
 ('n3', 'Creation', 'Today', 'at', '', 'John mentioned you on Lesson 2.4', '“@Ada can you check the join example?”', '2 h ago', 'Open', 0),
 ('n4', 'Discussions', 'Today', 'chat', '', 'New question in Data Analysis with SQL, Chapter 4', '“Why does my GROUP BY return duplicates?”', '3 h ago', 'Open', 0),
 ('n6', 'Economy', 'Yesterday', 'card', 'gr', 'Validation payment successful', '1,250 Credits · Data Analysis with SQL', 'Yesterday', 'View', 0),
 ('n7', 'Collaboration', 'Yesterday', 'doc', 'am', 'Mary hasn’t confirmed her contributor declaration', 'Data Analysis with SQL · Assessments', 'Yesterday', 'Review', 0),
 ('n8', 'Account', 'Earlier', 'ok', 'gr', 'Creator Orientation complete', 'Your readiness is now 80%', '2 days ago', 'Open', 0),
 ('n9', 'Economy', 'Earlier', 'coin', 'gr', '$420 moved to available earnings', 'September marketplace earnings', '3 days ago', 'View', 0),
 ('n10', 'Validation', 'Earlier', 'star', 'gr', 'Advanced SQL for Analysts is Silver validated', 'Case VAL-00811', '1 week ago', 'Open', 0),
]
CATS = ['All', 'Validation', 'Collaboration', 'Creation', 'Discussions', 'Learner support', 'Economy', 'AI', 'Account']
import json
NOT_JS = 'const N = ' + json.dumps([list(x) for x in NOTS], ensure_ascii=False) + ';'
ICONS_JS = ''
NIC = sorted({x[3] for x in NOTS})
ICON_IFS = ''.join(f'<sc-if value="{{{{r.i_{k}}}}}" hint-placeholder-val="{{{{false}}}}">{ic(I[k], 20)}</sc-if>' for k in NIC)
main_not = '''<main class="ds-main hp">
<div class="hp-head ob-in"><div><h1 class="ds-h1">Notifications</h1><p class="hp-sub">{{unreadTxt}}</p></div>
<div class="nt-acts"><label class="nt-un"><button type="button" class="hp-sw {{unCls}}" role="switch" aria-checked="{{unAria}}" onClick="{{toggleUnread}}" aria-label="Unread only"></button><span>Unread only</span></label><button type="button" class="hp-rb" onClick="{{markAll}}">Mark all as read</button></div></div>
<div class="hp-tabs ob-in2" role="tablist" aria-label="Categories"><sc-for list="{{cats}}" as="c" hint-placeholder-count="9"><button type="button" role="tab" aria-selected="{{c.sel}}" class="hp-tab {{c.cls}}" onClick="{{c.pick}}">{{c.t}}</button></sc-for></div>
<sc-for list="{{groups}}" as="g" hint-placeholder-count="3"><section class="nt-g ob-in3" aria-label="{{g.t}}"><span class="hp-lab">{{g.t}}</span><ul class="ds-card nt-l"><sc-for list="{{g.rows}}" as="r" hint-placeholder-count="4">
<li class="nt-r {{r.cls}}"><span class="hp-ic {{r.tone}}">''' + ICON_IFS + '''</span><span class="nt-t"><b>{{r.t}}</b><span>{{r.ctx}}</span></span><span class="nt-m"><span>{{r.cat}}</span><span>{{r.when}}</span></span><a href="#" class="hp-rb" onClick="{{r.open}}">{{r.cta}}</a><i class="nt-dot" aria-label="Unread"></i></li>
</sc-for></ul></section></sc-for>
<sc-if value="{{empty}}" hint-placeholder-val="{{false}}"><div class="ds-card nt-empty"><b>You’re all caught up</b><span>Nothing unread in this category.</span></div></sc-if>
<a href="CR-HOME-SET.dc.html" class="ds-link nt-pref">Notification settings</a>
</main>'''
js_not = f'''    {NOT_JS}
    {ICONS_JS}
    const read = (r) => !r[9] || S.read[r[0]];
    const vis = N.filter((r) => (S.cat === 'All' || r[1] === S.cat) && (!S.unread || !read(r)));
    const groups = ['Today', 'Yesterday', 'Earlier'].map((g) => ({{ t: g, rows: vis.filter((r) => r[2] === g).map((r) => ({{
      ['i_' + r[3]]: true, tone: r[4], t: r[5], ctx: r[6], cat: r[1], when: r[7], cta: r[8], cls: read(r) ? '' : 'un',
      open: () => this.setState({{ read: Object.assign({{}}, S.read, {{ [r[0]]: true }}) }}) }})) }})).filter((g) => g.rows.length);
    const n = N.filter((r) => !read(r)).length;
    return {{ navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({{ nav: !S.nav }}),
      unreadTxt: n ? n + ' unread' : 'You’re all caught up', groups, empty: !groups.length,
      cats: {json.dumps(CATS)}.map((c) => ({{ t: c, cls: S.cat === c ? 'on' : '', sel: S.cat === c ? 'true' : 'false', pick: () => this.setState({{ cat: c }}) }})),
      unCls: S.unread ? 'on' : '', unAria: S.unread ? 'true' : 'false', toggleUnread: () => this.setState({{ unread: !S.unread }}),
      markAll: () => {{ const r = {{}}; N.forEach((x) => {{ r[x[0]] = true; }}); this.setState({{ read: r }}); }} }};'''
css_not = '''
.nt-acts{display:flex;align-items:center;gap:16px}
.nt-un{display:inline-flex;align-items:center;gap:10px;font-size:14px;color:#3A4566;cursor:pointer}
.nt-g{margin-top:22px}
.nt-l{list-style:none;margin:10px 0 0 0;padding:4px 20px}
.nt-r{position:relative;display:grid;grid-template-columns:40px minmax(0,1fr) 150px 112px;align-items:center;column-gap:16px;padding:14px 0;border-top:1.5px solid #F0F2F8}
.nt-r:first-child{border-top:0}
.nt-t{display:flex;flex-direction:column;gap:3px;min-width:0}
.nt-t b{font-size:15px;font-weight:500;color:#3A4566}
.nt-r.un .nt-t b{font-weight:600;color:#0B1433}
.nt-t > span{font-size:13.5px;color:#5B6582;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.nt-m{display:flex;flex-direction:column;gap:2px;font-size:13px;color:#5B6582}
.nt-m > span:first-child{font-weight:500;color:#3A4566}
.nt-r .hp-rb{justify-self:end}
.nt-dot{display:none;position:absolute;left:-12px;top:50%;width:7px;height:7px;margin-top:-3.5px;border-radius:50%;background:#1652F0}
.nt-r.un .nt-dot{display:block}
.nt-empty{margin-top:22px;padding:28px;display:flex;flex-direction:column;align-items:center;gap:4px;font-size:14px;color:#5B6582}.nt-empty b{font-size:16px;color:#0B1433}
.nt-pref{margin:20px 0 0 4px;font-size:14px}
@media (max-width: 960px){
.hp-head .nt-acts{justify-content:space-between}
.nt-l{padding:2px 14px}
.nt-r{grid-template-columns:36px minmax(0,1fr);column-gap:12px;align-items:start;padding:13px 0}
.nt-r .hp-ic{width:36px;height:36px;border-radius:11px;grid-row:span 2}
.nt-m{grid-column:2;flex-direction:row;margin-top:4px;font-size:12.5px}
.nt-m > span:first-child{display:none}
.nt-r .hp-rb{position:absolute;inset:0;height:auto;opacity:0;font-size:0}
.nt-dot{top:31px}
.nt-t b{font-size:14.5px}
.nt-t > span{white-space:normal;display:-webkit-box;-webkit-line-clamp:1;-webkit-box-orient:vertical}
.nt-dot{left:-9px}
}
'''
page('CR-NOT-001', None, main_not, js_not, css_not, 'Credalio · Notifications', "{ nav: false, cat: 'All', unread: false, read: {} }")

# ======================= CR-HOME-EXP · My learning experiences =======================
EXP = [
 ('Data Analysis with SQL', 'Course', 'book', 'Published', 'gr', 'Gold validated · 1,240 learners', '', 'Updated 2 days ago'),
 ('Advanced SQL for Analysts', 'Course', 'book', 'Published', 'gr', 'Silver validated · 512 learners', '', 'Updated last week'),
 ('Certified Data Analyst', 'Professional Certification', 'cert', 'Published', 'gr', '138 candidates', '', 'Updated 3 weeks ago'),
 ('Applied AI Program', 'Learning Program', 'prog', 'Published', 'gr', 'Cohort A running · week 9 of 12', '', 'Updated yesterday'),
 ('Data Analyst Career Path', 'Career Path', 'path', 'In validation', 'cb', 'Case VAL-01102 · evidence requested', 'att', 'Updated today'),
 ('Python for Analysts', 'Course', 'book', 'Draft', 'gy', '', '42', 'Edited yesterday'),
 ('Dashboards that Drive Decisions', 'Course', 'book', 'Draft', 'gy', '', '15', 'Edited 2 weeks ago'),
]
TABS = [('All', 7), ('Published', 4), ('Drafts', 2), ('In validation', 1), ('Needs action', 1)]
rows = ''
for t, ty, icn, st, tone, meta, prog, upd in EXP:
    filt = {'Published': 'pub', 'Draft': 'drf', 'In validation': 'val'}[st] + (' att' if prog == 'att' else '')
    mid = (f'<span class="ex-pg"><span class="ex-bar"><span style="width: {prog}%"></span></span>{prog}% built</span>' if prog and prog != 'att'
           else f'<span class="ex-mt{" amb" if prog == "att" else ""}">{meta}</span>')
    act = 'Respond' if prog == 'att' else ('Resume' if st == 'Draft' else 'Open')
    rows += (f'<li class="ex-r" data-f="{filt}"><span class="ex-cv">{ic(I[icn], 20)}</span><span class="ex-t"><b>{t}</b><span>{ty}</span></span>'
             f'<span class="ex-st"><span class="ex-pill {tone}">{st}</span></span>{mid}<span class="ex-up">{upd}</span><a href="#" class="hp-rb">{act}</a></li>')
main_exp = ('<main class="ds-main hp">\n<div class="hp-head ob-in"><div><h1 class="ds-h1">My learning experiences</h1><p class="hp-sub">4 published · 1 in validation · 2 drafts</p></div>'
            '<a href="CR-HOME-NEW.dc.html" class="ds-btn hp-btn"><span>Create new</span><span class="ob-arrow">' + PLUS + '</span></a></div>'
            '<div class="ex-bar2 ob-in2"><div class="hp-tabs" role="tablist" aria-label="Filter"><sc-for list="{{tabs}}" as="c" hint-placeholder-count="5"><button type="button" role="tab" aria-selected="{{c.sel}}" class="hp-tab {{c.cls}}" onClick="{{c.pick}}">{{c.t}} <em>{{c.n}}</em></button></sc-for></div>'
            '<label class="ex-s">' + ic('<circle cx="11" cy="11" r="7"></circle><path d="m20 20-3.5-3.5"></path>', 18, 1.9) + '<span class="sr-only">Search</span><input placeholder="Search your learning experiences"></label></div>'
            '<div class="ds-card ex-card ob-in3 {{fCls}}"><div class="ex-h"><span>Learning experience</span><span>Status</span><span>Progress</span><span>Last change</span><span></span></div><ul class="ex-l">' + rows + '</ul></div>\n</main>')
js_exp = '''    const T = ''' + json.dumps([list(x) for x in TABS]) + ''';
    const key = { 'All': '', 'Published': 'f-pub', 'Drafts': 'f-drf', 'In validation': 'f-val', 'Needs action': 'f-att' };
    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }), fCls: key[S.tab],
      tabs: T.map((x) => ({ t: x[0], n: x[1], cls: S.tab === x[0] ? 'on' : '', sel: S.tab === x[0] ? 'true' : 'false', pick: () => this.setState({ tab: x[0] }) })) };'''
css_exp = '''
.ex-bar2{display:flex;align-items:center;justify-content:space-between;gap:16px}
.ex-s{display:flex;align-items:center;gap:10px;width:300px;height:42px;padding:0 16px;box-sizing:border-box;border-radius:999px;border:1.5px solid #E6EAF3;background:#FFFFFF;color:#8A93AD}
.ex-s input{border:0;outline:none;font-family:inherit;font-size:14px;color:#0B1433;width:100%;background:none}
.ex-card{margin-top:16px;padding:6px 22px}
.ex-h,.ex-r{display:grid;grid-template-columns:44px minmax(0,2fr) 130px minmax(0,1.6fr) 150px 100px;align-items:center;column-gap:16px}
.ex-h{padding:12px 0 10px 0;font-size:12.5px;color:#8A93AD;border-bottom:1.5px solid #F0F2F8}
.ex-l{list-style:none;margin:0;padding:0}
.ex-r{padding:14px 0;border-top:1.5px solid #F0F2F8}
.ex-r:first-child{border-top:0}
.ex-h > span:first-child{grid-column:1 / 3}
.ex-cv{width:44px;height:44px;border-radius:13px;background:linear-gradient(135deg,#1652F0,#6E96FF);color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.ex-t{display:flex;flex-direction:column;gap:2px;min-width:0}
.ex-t b{font-size:15.5px;font-weight:600}.ex-t > span{font-size:13px;color:#5B6582}
.ex-pill{display:inline-flex;align-items:center;height:28px;padding:0 11px;border-radius:999px;font-size:12.5px;font-weight:500;white-space:nowrap}
.ex-pill.gr{background:#E7F5EE;color:#0F6B45}.ex-pill.cb{background:#EAF0FF;color:#0E3BB8}.ex-pill.gy{background:#F1F3F8;color:#4A5578}
.ex-mt{font-size:13.5px;color:#3A4566}.ex-mt.amb{color:#8A5300;font-weight:500}
.ex-pg{display:flex;align-items:center;gap:10px;font-size:13.5px;color:#3A4566}
.ex-bar{display:block;width:120px;height:6px;border-radius:6px;background:#E6EAF3;overflow:hidden}.ex-bar span{display:block;height:100%;background:#1652F0;border-radius:6px}
.ex-up{font-size:13px;color:#5B6582}
.ex-r .hp-rb{justify-self:end}
.f-pub .ex-r:not([data-f^="pub"]),.f-drf .ex-r:not([data-f^="drf"]),.f-val .ex-r:not([data-f^="val"]),.f-att .ex-r:not([data-f*="att"]){display:none}
@media (max-width: 1180px){.ex-up,.ex-h > span:nth-child(4){display:none}.ex-r,.ex-h{grid-template-columns:44px minmax(0,1.4fr) 130px minmax(0,1fr) 100px}}
@media (max-width: 960px){
.ex-bar2{flex-direction:column;align-items:stretch;gap:12px}
.ex-s{width:100%}
.ex-card{padding:2px 14px}
.ex-h{display:none}
.ex-r{grid-template-columns:40px minmax(0,1fr) auto;row-gap:6px;column-gap:12px;padding:14px 0}
.ex-cv{width:40px;height:40px;border-radius:12px;grid-row:span 2}
.ex-st{display:none}
.ex-r > .ex-mt,.ex-r > .ex-pg{grid-column:2 / 3;grid-row:2}
.ex-r .hp-rb{grid-column:3;grid-row:1 / span 2;height:34px;padding:0 13px;font-size:13px}
.ex-t b{font-size:15px}
.ex-pg .ex-bar{width:80px}
}
'''
page('CR-HOME-EXP', 'My learning experiences', main_exp, js_exp, css_exp, 'Credalio · My learning experiences', "{ nav: false, tab: 'All' }")

# ======================= CR-HOME-NEW · Create new =======================
FMTS = [('book', 'Course', 'Build a structured learning experience around a subject or skill.', 'One topic, learned step by step', '2 to 10 hours'),
        ('cert', 'Professional Certification', 'Assess and verify professional competencies.', 'Proving someone can do the job', 'Exam + practical'),
        ('path', 'Career Path', 'Create a structured journey toward a career outcome.', 'Getting someone into a role', 'Several courses'),
        ('prog', 'Learning Program', 'Deliver coordinated learning over a structured period.', 'A group learning together', 'Weeks, with cohorts')]
fmt_cards = ''.join(
    f'<a href="CR-CREATE-001.dc.html" class="nw-f"><span class="nw-fi">{ic(I[i], 22)}</span><b>{t}</b><span class="nw-fd">{d}</span>'
    f'<span class="nw-fm"><span><em>Best for</em>{best}</span><span><em>Typical size</em>{size}</span></span><span class="nw-go">Choose {ARR}</span></a>' for i, t, d, best, size in FMTS)
main_new = ('<main class="ds-main hp">\n<div class="hp-head ob-in"><div><h1 class="ds-h1">Create something new</h1><p class="hp-sub">Start from an idea, or pick a format if you already know what you’re making.</p></div></div>'
            '<section class="ds-card nw-c ob-in2" aria-label="Start from an idea"><label for="nw-i" class="sr-only">Describe your idea</label>'
            '<textarea id="nw-i" rows="2" placeholder="Describe an idea. For example: Python for analysts who already know SQL."></textarea>'
            f'<div class="nw-cf"><span class="nw-h">{NOVA}Not sure which format fits? Nova picks one from your idea.</span><a href="CR-CREATE-002A.dc.html" class="ds-btn hp-btn"><span>Start with Nova</span><span class="ob-arrow">{ARR}</span></a></div></section>'
            '<div class="nw-or ob-in3"><span class="hp-lab">Or choose a format</span></div><div class="nw-g ob-in3">' + fmt_cards + '</div>'
            '\n</main>')
js_new = "    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }) };"
css_new = '''
.nw-c{padding:18px 20px 16px 22px;border-color:#CBD7F5;box-shadow:0 18px 44px rgba(22,82,240,.08)}
.nw-c textarea{width:100%;box-sizing:border-box;border:0;outline:none;resize:none;font-family:inherit;font-size:17px;line-height:1.5;color:#0B1433;background:none;min-height:56px}
.nw-c textarea::placeholder{color:#8A93AD}
.nw-cf{margin-top:8px;display:flex;align-items:center;justify-content:space-between;gap:16px}
.nw-h{display:flex;align-items:center;gap:10px;font-size:14px;color:#5B6582}
.nw-or{margin-top:28px}
.nw-g{margin-top:12px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}
.nw-f{display:flex;flex-direction:column;padding:20px;border-radius:20px;background:#FFFFFF;border:1.5px solid #E6EAF3;text-decoration:none;color:#0B1433;transition:border-color .2s ease,box-shadow .2s ease,transform .2s ease}
.nw-f:hover{border-color:#CBD7F5;box-shadow:0 14px 34px rgba(22,82,240,.08);transform:translateY(-2px)}
.nw-fi{width:46px;height:46px;border-radius:14px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.nw-f b{margin-top:14px;font-size:17px;font-weight:600}
.nw-fd{margin-top:6px;font-size:14px;line-height:1.5;color:#4A5578;flex-grow:1}
.nw-fm{margin-top:16px;padding-top:14px;border-top:1.5px solid #F0F2F8;display:flex;flex-direction:column;gap:8px;font-size:13.5px;color:#0B1433}
.nw-fm em{display:block;font-style:normal;font-size:12px;color:#8A93AD}
.nw-go{margin-top:16px;display:inline-flex;align-items:center;gap:6px;font-size:14.5px;font-weight:600;color:#1652F0}
.nw-n{margin-top:18px;display:flex;align-items:center;gap:14px;padding:16px 20px;border-radius:20px;border:1.5px solid #E1E9FF;background:#F5F8FF url(/_blob/d268046654a4206d2a726e62005bcc59) center / cover no-repeat}
.nw-nt{flex-grow:1;display:flex;flex-direction:column;gap:2px}
.nw-nt b{font-size:15px;font-weight:600}.nw-nt > span:last-child{font-size:13.5px;color:#3A4566}
.nw-n .hp-rb{background:#FFFFFF}
@media (max-width: 1180px){.nw-g{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width: 960px){
.nw-c{padding:14px 16px}
.nw-c textarea{font-size:15.5px}
.nw-cf{flex-direction:column;align-items:stretch;gap:12px}
.nw-cf .hp-btn{width:100%;justify-content:space-between}
.nw-or{margin-top:22px}
.nw-g{grid-template-columns:minmax(0,1fr);gap:10px}
.nw-f{display:grid;grid-template-columns:40px minmax(0,1fr) 18px;column-gap:14px;align-items:center;padding:14px 16px;border-radius:16px}
.nw-fi{width:40px;height:40px;border-radius:12px;grid-row:span 2}
.nw-f b{margin-top:0;font-size:15.5px}
.nw-fd{margin-top:2px;font-size:13.5px;grid-column:2}
.nw-fm{display:none}
.nw-go{grid-column:3;grid-row:1 / span 2;margin-top:0;font-size:0;gap:0}
}
'''
page('CR-HOME-NEW', 'Create new', main_new, js_new, css_new, 'Credalio · Create new')

# ======================= CR-HOME-SET · Settings · AI preferences =======================
SNAV = [('user', 'Profile'), ('lock', 'Account & sign-in'), ('bell', 'Notifications'), ('eye', 'Privacy'), ('globe', 'Language & region'), ('ai', 'AI preferences'), ('org', 'My organizations')]
snav = ''.join(f'<a href="#" class="se-n{" on" if t == "AI preferences" else ""}"{" aria-current=page" if t == "AI preferences" else ""}>{ic(I[i], 18)}<span>{t}</span></a>' for i, t in SNAV)
names = ''.join(f'<button type="button" role="radio" aria-checked="{{{{n{k}.sel}}}}" class="se-c {{{{n{k}.cls}}}}" onClick="{{{{n{k}.pick}}}}">{head(k, 30)}<span>{k}</span></button>' for k in CH)
STY = {'Concise': 'Outcomes 2 and 4 aren’t measurable. Try “Write a query that…”. Fix?',
       'Collaborative': 'Happy to. Who’s the main audience, analysts or managers? Outcome 2 reads differently for each.',
       'Detailed': 'Two outcomes use verbs validators can’t observe (“understand”, “know”). Here’s how I’d rewrite each, and why it helps.'}
PVH = ''.join('<sc-if value="{{p' + k + '}}" hint-placeholder-val="{{' + ('true' if k == 'Nova' else 'false') + '}}">' + head(k, 34) + '</sc-if>' for k in CH)
main_set = ('<main class="ds-main hp">\n<div class="hp-head ob-in"><div><h1 class="ds-h1">Settings</h1></div></div>'
            '<div class="se ob-in2"><nav class="se-nav" aria-label="Settings">' + snav + '</nav>'
            '<section class="ds-card se-p" aria-labelledby="se-h"><div class="se-ph"><div><h2 id="se-h">AI preferences</h2><p>How your Copilot works with you. Changing these keeps your history.</p></div></div>'
            '<div class="se-row se-top"><div class="se-l"><b>Your Copilot</b><span>Pick a name, or type your own.</span></div><div class="se-v">'
            '<div class="se-cs" role="radiogroup" aria-label="Copilot name">' + names + '</div>'
            '<label class="se-in"><span class="sr-only">Copilot name</span><input placeholder="Or type your own" value="{{cpName}}" onChange="{{onName}}"></label></div></div>'
            '<div class="se-row se-top"><div class="se-l"><b>Response style</b><span>How {{cpName}} talks to you.</span></div><div class="se-v">'
            '<div class="se-seg" role="radiogroup" aria-label="Response style"><sc-for list="{{styles}}" as="c" hint-placeholder-count="3"><button type="button" role="radio" aria-checked="{{c.sel}}" class="se-s {{c.cls}}" onClick="{{c.pick}}">{{c.t}}</button></sc-for></div>'
            '<div class="se-pv"><span class="se-pa">' + PVH + f'</span><span><span class="hp-lab">{{{{cpName}}}} · preview</span><span class="se-pt">{{{{sample}}}}</span></span></div></div></div>'
            '<div class="se-row"><div class="se-l"><b>Proactive suggestions</b><span>{{cpName}} points out gaps while you work.</span></div><button type="button" class="hp-sw {{proCls}}" role="switch" aria-checked="{{proAria}}" aria-label="Proactive suggestions" onClick="{{togglePro}}"></button></div>'
            '<div class="se-row"><div class="se-l"><b>Low Creio alerts</b><span>In the app and by email.</span></div><div class="se-v se-inl"><div class="ob-sel se-sel"><select class="ob-f" aria-label="Alert level"><option>Below 20,000 Creio</option><option>Below 10,000 Creio</option><option>Below 5,000 Creio</option></select>' + CHEV + '</div>'
            '<button type="button" class="hp-sw {{lowCls}}" role="switch" aria-checked="{{lowAria}}" aria-label="Low Creio alerts" onClick="{{toggleLow}}"></button></div></div>'
            '<div class="se-ft"><span class="se-cr"><span class="se-coin" aria-hidden="true"></span><span><b>20,000 Creio</b> left</span><a href="#" class="ds-link">See usage</a></span>'
            f'<a href="#" class="ds-btn hp-btn"><span>Save changes</span><span class="ob-arrow">{ARR}</span></a></div></section></div>\n</main>')
js_set = '''    const STY = ''' + json.dumps(STY, ensure_ascii=False) + ''';
    const IMG = ''' + json.dumps(CH) + ''';
    const out = { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }),
      cpName: S.name, onName: (e) => this.setState({ name: e.target.value }), 
      styles: Object.keys(STY).map((k) => ({ t: k, cls: S.style === k ? 'on' : '', sel: S.style === k ? 'true' : 'false', pick: () => this.setState({ style: k }) })),
      sample: STY[S.style],
      proCls: S.pro ? 'on' : '', proAria: S.pro ? 'true' : 'false', togglePro: () => this.setState({ pro: !S.pro }),
      lowCls: S.low ? 'on' : '', lowAria: S.low ? 'true' : 'false', toggleLow: () => this.setState({ low: !S.low }) };
    Object.keys(IMG).forEach((k) => { out['p' + k] = (IMG[S.name] ? S.name : 'Nova') === k; out['n' + k] = { cls: S.name === k ? 'on' : '', sel: S.name === k ? 'true' : 'false', pick: () => this.setState({ name: k }) }; });
    return out;'''
css_set = '''
.se{display:grid;grid-template-columns:240px minmax(0,1fr);gap:24px;align-items:start}
.se-nav{position:sticky;top:96px;display:flex;flex-direction:column;gap:2px}
.se-n{display:flex;align-items:center;gap:12px;height:44px;padding:0 14px;border-radius:12px;color:#3A4566;font-size:14.5px;font-weight:500;text-decoration:none}
.se-n svg{color:#5B6582}
.se-n.on{background:#EAF0FF;color:#0E3BB8;font-weight:600}.se-n.on svg{color:#1652F0}
.se-p{padding:6px 28px 22px 28px}
.se-ph{padding:20px 0 18px 0;border-bottom:1.5px solid #F0F2F8}
.se-ph h2{margin:0;font-size:20px;font-weight:600;letter-spacing:-0.01em}
.se-ph p{margin:4px 0 0 0;font-size:14px;color:#5B6582}
.se-row{display:grid;grid-template-columns:minmax(0,260px) minmax(0,1fr);gap:24px;align-items:center;padding:20px 0;border-bottom:1.5px solid #F0F2F8}
.se-row > .hp-sw{justify-self:end}
.se-top{align-items:start}
.se-l{display:flex;flex-direction:column;gap:3px}
.se-l b{font-size:15px;font-weight:600}.se-l span{font-size:13.5px;color:#5B6582;line-height:1.45}
.se-v{display:flex;flex-direction:column;gap:12px;min-width:0}
.se-inl{flex-direction:row;align-items:center;justify-content:flex-end;gap:16px}
.se-cs{display:flex;flex-wrap:wrap;gap:8px}
.se-c{display:inline-flex;align-items:center;gap:9px;height:44px;padding:0 16px 0 6px;border-radius:14px;border:1.5px solid #E6EAF3;background:#FFFFFF;font-family:inherit;font-size:14.5px;font-weight:500;color:#0B1433;cursor:pointer}
.se-c.on{background:#EAF0FF;border-color:#1652F0;color:#0E3BB8}
.se-in input{width:100%;max-width:320px;height:44px;box-sizing:border-box;padding:0 14px;border-radius:12px;border:1.5px solid #D6DDEE;font-family:inherit;font-size:15px;color:#0B1433;outline:none}
.se-seg{display:inline-flex;padding:4px;gap:4px;border-radius:14px;background:#F1F3F8;align-self:flex-start}
.se-s{height:38px;padding:0 16px;border-radius:11px;border:0;background:none;font-family:inherit;font-size:14px;font-weight:500;color:#3A4566;cursor:pointer}
.se-s.on{background:#FFFFFF;color:#0E3BB8;box-shadow:0 1px 3px rgba(11,20,51,.1)}
.se-pv{display:flex;align-items:flex-start;gap:12px;padding:14px 16px;border-radius:16px;border:1.5px solid #E1E9FF;background:#F5F8FF url(/_blob/d268046654a4206d2a726e62005bcc59) center / cover no-repeat}
.se-pv > span:last-child{display:flex;flex-direction:column;gap:3px}
.se-pt{font-size:14.5px;line-height:1.5;color:#0B1433}
.se-sel{width:220px}
.se-sel select{width:100%;height:44px;box-sizing:border-box;padding:0 40px 0 14px;border-radius:12px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:inherit;font-size:14.5px;color:#0B1433;appearance:none;-webkit-appearance:none;outline:none}
.ob-sel{position:relative}.ob-sel svg{position:absolute;right:14px;top:50%;transform:translateY(-50%);pointer-events:none;color:#5B6582}
.se-pa{display:flex;flex-shrink:0}
.se-ft{display:flex;align-items:center;justify-content:space-between;gap:16px;padding-top:20px}
.se-cr{display:flex;align-items:center;gap:10px;flex-wrap:wrap;font-size:14px;color:#3A4566}
.se-cr b{font-weight:600;color:#4A3300}
.se-coin{width:26px;height:26px;flex-shrink:0;border-radius:50%;background:linear-gradient(135deg,#FFE9A3,#F6C343 45%,#D08A12);box-shadow:inset 0 0 0 3px rgba(255,241,194,.6)}
@media (max-width: 960px){
.se{grid-template-columns:minmax(0,1fr);gap:14px}
.se-nav{position:static;flex-direction:row;overflow-x:auto;margin:0 -16px;padding:0 16px;gap:6px;scrollbar-width:none}
.se-n{flex-shrink:0;height:40px;border:1.5px solid #E6EAF3;background:#FFFFFF;border-radius:999px;font-size:14px}
.se-n.on{border-color:#1652F0}
.se-p{padding:2px 16px 18px 16px}
.se-ph{padding:16px 0 14px 0}
.se-row{grid-template-columns:minmax(0,1fr) auto;gap:14px;padding:16px 0}
.se-top{grid-template-columns:minmax(0,1fr)}
.se-inl{grid-column:1 / -1;justify-content:space-between}
.se-sel{flex-grow:1;width:auto}
.se-cs{flex-wrap:nowrap;overflow-x:auto;margin:0 -16px;padding:0 16px;scrollbar-width:none}
.se-c{flex-shrink:0}
.se-in input{max-width:none}
.se-seg{align-self:stretch;display:flex}.se-s{flex:1 1 0;padding:0 6px}
.se-ft{flex-direction:column;align-items:stretch}
.se-ft .hp-btn{width:100%;justify-content:space-between}
}
'''
page('CR-HOME-SET', 'Settings', main_set, js_set, css_set, 'Credalio · Settings · AI preferences', "{ nav: false, name: 'Nova', style: 'Collaborative', pro: true, low: true }")

# ---------- mobile wrappers ----------
wm = rd('CR-CRED-002c-Mobile.dc.html')
for n, h in [('CR-NOT-001', 1200), ('CR-HOME-EXP', 1100), ('CR-HOME-NEW', 1100), ('CR-HOME-SET', 1300)]:
    t = wm.replace('<dc-import name="CR-CRED-002" variant="badge"', f'<dc-import name="{n}"')
    t = re.sub(r'hint-size="[^"]*"', f'hint-size="390px,{h}px"', t)
    t = re.sub(r'width: \d+px; height: \d+px;', f'width: 390px; height: {h}px;', t, count=1)
    t = re.sub(r'"\$preview":\{"width":\d+,"height":\d+\}', f'"$preview":{{"width":390,"height":{h}}}', t)
    t = re.sub(r'<title>.*?</title>', f'<title>{n} mobile preview</title>', t)
    wr(n + '-Mobile.dc.html', t)
print('ok')

# ======================= CR-NOT-bell · bell dropdown over the dashboard =======================
b = dsh
bs = b.index('<a href="#" class="ds-icon-btn" aria-label="Notifications')
be = b.index('</a>', bs) + 4
bell = b[bs:be].replace('href="#" class="ds-icon-btn"', 'href="CR-NOT-001.dc.html" class="ds-icon-btn nb-on" aria-expanded="true"', 1).replace('Notifications, 1 new', 'Notifications, 3 new')
items = ''
for r in NOTS[:5]:
    items += (f'<li class="nb-r{" un" if r[9] else ""}"><a href="CR-NOT-001.dc.html"><span class="hp-ic {r[4]}">{ic(I[r[3]], 18)}</span>'
              f'<span class="nb-t"><b>{r[5]}</b><span>{r[7]}</span></span>{"<i class=nb-dot aria-label=Unread></i>" if r[9] else ""}</a></li>')
pop = ('<div class="nb-w">' + bell + '<section class="nb-p" role="dialog" aria-label="Notifications"><div class="nb-h"><b>Notifications</b><span class="nb-n">3 new</span><a href="#" class="ds-link">Mark all as read</a></div>'
       '<ul class="nb-l">' + items + '</ul><a href="CR-NOT-001.dc.html" class="nb-all">See all notifications</a></section></div>')
b = b[:bs] + pop + b[be:]
b = b.replace('<main class="ds-main">', '<div class="nb-scrim" aria-hidden="true"></div><main class="ds-main">', 1)
b = b.replace('</style>', BASE_CSS + '''
/* build17 bell */
.nb-w{position:relative}
.ds-icon-btn.nb-on{background:#EAF0FF;border-color:#CBD7F5;color:#1652F0}
.nb-p{position:absolute;right:-8px;top:calc(100% + 12px);z-index:30;width:420px;box-sizing:border-box;padding:6px 0 8px 0;border-radius:20px;background:#FFFFFF;border:1.5px solid #E6EAF3;box-shadow:0 24px 60px rgba(11,20,51,.16)}
.nb-h{display:flex;align-items:center;gap:10px;padding:14px 20px 10px 20px}
.nb-h b{font-size:17px;font-weight:600}
.nb-n{display:inline-flex;align-items:center;height:24px;padding:0 9px;border-radius:999px;background:#EAF0FF;color:#0E3BB8;font-size:12.5px;font-weight:500}
.nb-h .ds-link{margin-left:auto;font-size:13.5px}
.nb-l{list-style:none;margin:0;padding:0 8px}
.nb-r a{position:relative;display:flex;align-items:flex-start;gap:12px;padding:10px 12px;border-radius:14px;text-decoration:none;color:#0B1433}
.nb-r a:hover{background:#F5F8FF}
.nb-r .hp-ic{width:36px;height:36px;border-radius:11px}
.nb-t{display:flex;flex-direction:column;gap:2px;min-width:0;padding-right:14px}
.nb-t b{font-size:14px;font-weight:500;color:#3A4566;line-height:1.4;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.nb-r.un .nb-t b{font-weight:600;color:#0B1433}
.nb-t span{font-size:12.5px;color:#5B6582}
.nb-dot{position:absolute;right:12px;top:18px;width:8px;height:8px;border-radius:50%;background:#1652F0}
.nb-all{display:flex;align-items:center;justify-content:center;height:44px;margin:6px 16px 4px 16px;border-radius:999px;border:1.5px solid #D6DDEE;color:#0B1433;font-size:14px;font-weight:600;text-decoration:none}
.nb-scrim{position:fixed;inset:0;z-index:9;background:rgba(11,20,51,.06);pointer-events:none}
@media (max-width: 960px){
.nb-w{position:static}
.nb-p{position:fixed;left:8px;right:8px;top:68px;width:auto;border-radius:20px}
.nb-scrim{background:rgba(11,20,51,.28)}
}
</style>''', 1)
b = re.sub(r'<title>.*?</title>', '<title>Credalio · Notifications (bell)</title>', b)
wr('CR-NOT-bell.dc.html', b)
t = wm.replace('<dc-import name="CR-CRED-002" variant="badge"', '<dc-import name="CR-NOT-bell"')
t = re.sub(r'<title>.*?</title>', '<title>CR-NOT-bell mobile preview</title>', t)
wr('CR-NOT-bell-Mobile.dc.html', t)
print('bell ok')
