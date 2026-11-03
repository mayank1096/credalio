"""Learner onboarding: how you like to learn (goal and starting point reuse the Journey screens in onboarding mode) built on the OnbChoice shell
(the Link 1 onboarding layout) plus kit chips, inputs, tooltip and the Nova avatar.
Usage: python3 onbgen.py <canvas3/project dir>"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from kit import KIT_CSS, ck, tip, nova_av
P = sys.argv[1]
SH = open(os.path.join(P, 'OnbChoice.dc.html')).read()
ON = '<span style="height: 4px; border-radius: 4px; background: #1652F0"></span>'
DOT = '<span style="height: 4px; border-radius: 4px; background: #E6EAF3"></span>'
I = {
    'video': '<rect x="3" y="5" width="18" height="14" rx="3"></rect><path d="M10 9.5v5l4.5-2.5z"></path>',
    'book': '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"></path><path d="M4 5v16"></path>',
    'tool': '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"></path>',
    'ear': '<path d="M3 14v-2a9 9 0 0 1 18 0v2"></path><rect x="3" y="14" width="4" height="6" rx="2"></rect><rect x="17" y="14" width="4" height="6" rx="2"></rect>',
    'users': '<circle cx="9" cy="8" r="3.2"></circle><path d="M3 20a6 6 0 0 1 12 0"></path><path d="M16 4.5a3 3 0 0 1 0 6"></path><path d="M18 14.5a5 5 0 0 1 3 4.5"></path>',
    'teach': '<path d="M3 5h18v11H3z"></path><path d="M8 20h8"></path><path d="M12 16v4"></path><path d="M7 10h6"></path>',
    'seed': '<path d="M12 21v-8"></path><path d="M12 13c0-4 3-7 8-7 0 4-3 7-8 7z"></path><path d="M12 15c0-3-2.5-5-6-5 0 3 2.5 5 6 5z"></path>',
    'steps': '<path d="M4 20h4v-4h4v-4h4V8h4"></path>',
    'swap': '<path d="M7 7h11l-3-3"></path><path d="M17 17H6l3 3"></path>',
    'brief': '<rect x="3" y="7" width="18" height="13" rx="2"></rect><path d="M9 7V4h6v3"></path>',
}
def ic(k, sz=22):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (sz, sz, I[k])
CKW = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="opacity: {{o.ck}}"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg>'
def card_loop(list_name, role, minh=84, desc=True, cnt=6, keys=()):
    d = '<span style="font-size: 13.5px; line-height: 1.4; color: #4A5578">{{o.desc}}</span>' if desc else ''
    head = ('<sc-for list="{{%s}}" as="o" hint-placeholder-count="%d"><button type="button" class="cd-card" role="%s" onClick="{{o.pick}}" aria-checked="{{o.pressed}}" style="display: flex; align-items: center; gap: 14px; padding: 14px 16px; min-height: %dpx; border-radius: 18px; border: 1.5px solid {{o.border}}; background: {{o.bg}}; box-shadow: {{o.shadow}}; cursor: pointer; text-align: left; font-family: inherit; transition: all .25s ease">') % (list_name, cnt, role, minh)
    icon = ''
    if keys:
        icon = ('<div style="width: 44px; height: 44px; flex-shrink: 0; border-radius: 13px; background: {{o.iconBg}}; color: {{o.iconFg}}; display: flex; align-items: center; justify-content: center; transition: all .25s ease">'
                + ''.join(ic(k).replace('<svg ', '<svg style="display: {{o.d_' + k + '}}" ', 1) for k in keys) + '</div>')
    text = '<div style="display: flex; flex-direction: column; gap: 3px; flex-grow: 1; min-width: 0"><span style="font-size: 16px; font-weight: 600; color: #0B1433; letter-spacing: -0.01em">{{o.title}}</span>' + d + '</div>'
    mark = '<div style="width: 22px; height: 22px; flex-shrink: 0; border-radius: {{o.rad}}; border: 1.5px solid {{o.radioBorder}}; background: {{o.radioBg}}; display: flex; align-items: center; justify-content: center; transition: all .25s ease">' + CKW + '</div></button></sc-for>'
    return head + icon + text + mark
CARD_JS = '''  card(on, multi) {
    return { pressed: on ? 'true' : 'false', border: on ? '#1652F0' : '#E6EAF3', bg: on ? '#F5F8FF' : '#FFFFFF',
      shadow: on ? '0 0 0 4px rgba(22, 82, 240, 0.12), 0 12px 28px rgba(22, 82, 240, 0.16)' : '0 1px 2px rgba(11, 20, 51, 0.04)',
      iconBg: on ? '#1652F0' : '#EAF0FF', iconFg: on ? '#FFFFFF' : '#1652F0', radioBorder: on ? '#1652F0' : '#CBD3E6', radioBg: on ? '#1652F0' : '#FFFFFF', ck: on ? 1 : 0, rad: multi ? '7px' : '50%' };
  }
'''
CHIP = '<button type="button" class="ds-chip {{c.cls}}" aria-pressed="{{c.on}}" onClick="{{c.pick}}">' + ck(13) + '{{c.label}}</button>'
def chips(lst, cnt=5, extra=''):
    return '<div class="ob-chips"%s><sc-for list="{{%s}}" as="c" hint-placeholder-count="%d">%s</sc-for></div>' % (extra, lst, cnt, CHIP)
NOVA = '<div class="ob-nova ob-in">' + nova_av('sm') + '<span><b>Nova</b> · your AI Coach</span></div>'
PAGE_CSS = '''.ob-nova{display:inline-flex;align-items:center;gap:8px;margin-bottom:14px;font-size:13.5px;color:#5B6582}
.ob-nova b{font-weight:600;color:#0B1433}
.ob-q{width:100%;margin-top:clamp(18px,3vh,26px);display:flex;flex-direction:column;gap:10px;text-align:left}
.ob-ql{display:flex;align-items:center;justify-content:space-between;gap:12px;font-size:15px;font-weight:600;color:#0B1433}
.ob-ql em{font-style:normal;font-size:13px;font-weight:500;color:#8A93AD}
.ob-chips{display:flex;flex-wrap:wrap;gap:8px}
.ob-skip{margin-top:12px;min-height:40px}
.ob-err{font-size:13px;color:#B42318}
.ob-cards3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;width:100%}
.ob-cards2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;width:100%}
.ob-cv{display:inline-flex;align-items:center;gap:6px;font-size:14px;color:#3A4566}
@media (max-width: 960px){.ob-cards3{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width: 760px){.ob-cards3,.ob-cards2{grid-template-columns:minmax(0,1fr);gap:10px}.ob-q{margin-top:20px}.ob-chips{flex-wrap:nowrap;overflow-x:auto;margin:0 -20px;padding:0 20px 2px;scrollbar-width:none}.ob-chips::-webkit-scrollbar{display:none}.ob-wrap .ob-chips{flex-wrap:wrap;overflow:visible;margin:0;padding:0}}
'''
def build(name, title, back, step, h1, sub, body, cta_label, cta_href, skip, script, colw=780):
    s = SH
    s = re.sub(r'<title>[^<]*</title>', '<title>%s</title>' % title, s)
    s = s.replace('href="OnbAbout.dc.html" class="ob-ghost ob-back"', 'href="%s" class="ob-ghost ob-back"' % back, 1)
    s = s.replace('Step 3 of 4: Personalise', 'Step %d of 4: %s' % step).replace('Step 3 of 4 · <span style="color: #0B1433; font-weight: 600">Personalise', 'Step %d of 4 · <span style="color: #0B1433; font-weight: 600">%s' % step)
    s = s.replace(ON * 3 + DOT, ON * step[0] + DOT * (4 - step[0]))
    s = s.replace('min(780px, calc(100% - 48px))', 'min(%dpx, calc(100%% - 48px))' % colw)
    i = s.index('<h1 class="ob-h1'); j = s.index('>', i) + 1; k = s.index('</h1>', j)
    s = s[:i] + NOVA + '\n' + s[i:j] + h1 + s[k:]
    s = s.replace('Personalising takes about two minutes, and you can skip any question.', sub)
    i = s.index('<div class="ob-grid2 ob-in3"'); j = s.index('<a href="{{ctaHref}}" class="ob-btn"')
    s = s[:i] + body + '\n' + s[j:]
    s = s.replace('<a href="{{ctaHref}}" class="ob-btn"', '<a href="%s" onClick="{{onCta}}" class="ob-btn"' % cta_href, 1).replace('{{ctaLabel}}', cta_label, 1)
    k = s.index('</a>', s.index('class="ob-btn"')) + 4
    if skip: s = s[:k] + '\n<a class="ds-link ob-skip" href="%s">Skip for now</a>' % skip + s[k:]
    s = s.replace('<div class="ob-scene" aria-hidden="true"></div>\n', '')
    s = re.sub(r'\.ob-scene\{[^}]*\}\n?', '', s); s = re.sub(r'@media \(max-width: 760px\)\{\.ob-scene\{[^}]*\}\}\n?', '', s)
    i = s.index('<style>') + len('<style>') if '<style>' in s else s.index('<style')
    i = s.index('>', s.index('<style')) + 1
    s = s[:i] + '\n' + KIT_CSS + '\n' + PAGE_CSS + s[i:]
    a = s.index('class Component extends DCLogic {'); b = s.index('</script>', a)
    s = s[:a] + script + '\n' + s[b:]
    open(os.path.join(P, name + '.dc.html'), 'w').write(s)
    print(name, len(s))

# 2 · How you learn
pref_body = '<div class="ob-q ob-in3" role="group" aria-label="How you like to learn"><div class="ob-cards3">' + card_loop('prefs', 'checkbox', 92, True, 6, ('video', 'book', 'tool', 'ear', 'users', 'teach')) + '</div></div>'
icons = {k: ic(k) for k in I}
pref_js = '''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { sel: { do: 1, watch: 1 } }; }
''' + CARD_JS + '''  renderVals() {
    const S = this.state, K = ['video', 'book', 'tool', 'ear', 'users', 'teach'], D = (k) => { const o = {}; K.forEach((x) => { o['d_' + x] = x === k ? 'block' : 'none'; }); return o; };
    const data = [['watch', 'Watch', 'Video lessons and demonstrations.', 'video'], ['read', 'Read', 'Articles, guides and written lessons.', 'book'], ['do', 'Learn by doing', 'Projects, exercises and practical work.', 'tool'],
      ['listen', 'Listen', 'Audio lessons and explanations.', 'ear'], ['others', 'Learn with others', 'Cohorts, discussions and group work.', 'users'], ['mentor', 'With a mentor', 'Live sessions, tutoring and guidance.', 'teach']];
    return { prefs: data.map(([k, t, d, i]) => { const on = !!S.sel[k]; return Object.assign(this.card(on, true), D(i), { title: t, desc: d, pick: () => { const n = Object.assign({}, S.sel); if (on) delete n[k]; else n[k] = 1; this.setState({ sel: n }); } }); }),
      onCta: () => {} };
  }
}'''
build('OnbPrefs', 'ONB-007 How you like to learn', 'OnbGoal.dc.html', (3, 'Personalise'), 'How do you like to learn?',
      'Choose as many as you like. Nova uses this to recommend what fits you.', pref_body, 'Continue', 'OnbStart.dc.html', 'OnbStart.dc.html', pref_js, 900)

