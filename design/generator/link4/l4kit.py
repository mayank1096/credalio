"""Link 4 (Course Studio) shared pieces: course-workspace shell, focus shell, toggles, helpers.

Reuses the Landing kit (kit.py: buttons, chips, options, inputs, tags, tooltips, Nova) and the Studio shell CSS
(dash.py DASH_CSS), so Link 4 screens look exactly like Links 1 and 2. Blob ids are remapped to this canvas's uploads.
"""
import os, sys, json, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'landing3'))
sys.path.insert(0, os.path.join(HERE, '..'))
import kit
from kit import btn, ghost, tip, nova_av, ck, ARROW, INFO
import dash
from dash import ICON, I, COIN

OUT = os.path.normpath(os.path.join(HERE, '..', '..', 'canvas4', 'project'))

# this canvas's uploads (same files as Links 1 to 3, new ids)
BLOBS = {
    '398ca91d2832bb0ab6b0af61319676f4': '7768558e9a167cb4198a0461f26bc891',  # Nova
    '0b29db2e4cd6f4a89dc7ba8f12e59c8d': '2201db898f778e583c1885b56e2d9c62',  # nova-card background
    '84f08b38fbe9b11d8aa477ac10398bfe': '167d6259769b54fee7a18d6801741d2f',  # av-f1
    '9112077cc7e3c1c839edc7e609d87954': '579b7da5420994a2a08f63fa37cbbf9f',  # av-f2
    '6940b199369f0ef8a87915557d16027b': 'cbfe3f2bbb89728d8777e425b59db736',  # av-m1
    '54e6db3b8b5f0875ac9ee0cfd0aef3d2': 'a4f450d2ae86bf787d69075bfb298fd4',  # av-m2
    '8acabcff7ece53343d63205e8b7321a2': '56bd922e46929406f00f4b18fe9b3244',  # wordmark
    'f81e36d31295a0d0737959589ec1abd4': '6d26bb5dab742fc7a27cff4144cfd663',  # mark
}
WORD = '/_blob/56bd922e46929406f00f4b18fe9b3244'
MARK = '/_blob/6d26bb5dab742fc7a27cff4144cfd663'
F1, F2 = '/_blob/167d6259769b54fee7a18d6801741d2f', '/_blob/579b7da5420994a2a08f63fa37cbbf9f'
M1, M2 = '/_blob/cbfe3f2bbb89728d8777e425b59db736', '/_blob/a4f450d2ae86bf787d69075bfb298fd4'
ME = F2  # Ada Ononuju, the creator

def fixblobs(s):
    for a, b in BLOBS.items():
        s = s.replace('/_blob/' + a, '/_blob/' + b)
    return s

def ic(name, size=18, sw=1.8):
    return ICON(EXTRA.get(name) or I[name], size, sw)

EXTRA = {
    'lock': '<rect x="5" y="10.5" width="14" height="10" rx="2.5"></rect><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"></path>',
    'home': '<path d="M4 10.5 12 4l8 6.5V19a1.5 1.5 0 0 1-1.5 1.5H15v-6H9v6H5.5A1.5 1.5 0 0 1 4 19z"></path>',
    'chat': '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"></path>',
    'users': '<circle cx="9" cy="8" r="3.5"></circle><path d="M2.5 20a6.5 6.5 0 0 1 13 0"></path><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14.5a6.5 6.5 0 0 1 3.5 5.5"></path>',
    'user': '<circle cx="12" cy="8" r="4"></circle><path d="M4 21a8 8 0 0 1 16 0"></path>',
    'globe': '<circle cx="12" cy="12" r="9"></circle><path d="M3 12h18M12 3c2.5 2.6 3.7 5.6 3.7 9s-1.2 6.4-3.7 9c-2.5-2.6-3.7-5.6-3.7-9S9.5 5.6 12 3z"></path>',
    'play': '<rect x="3" y="5" width="18" height="14" rx="3"></rect><path d="m10 9.5 5 2.5-5 2.5z" fill="currentColor"></path>',
    'live': '<circle cx="12" cy="12" r="2.5"></circle><path d="M7.8 7.8a6 6 0 0 0 0 8.4M16.2 7.8a6 6 0 0 1 0 8.4M5 5a10 10 0 0 0 0 14M19 5a10 10 0 0 1 0 14"></path>',
    'mix': '<rect x="3" y="4" width="8" height="7" rx="2"></rect><circle cx="17" cy="7.5" r="3.5"></circle><rect x="3" y="14" width="8" height="6" rx="2"></rect><path d="M14 14h6v6h-6z"></path>',
    'plus': '<path d="M12 5v14M5 12h14"></path>',
    'x': '<path d="M6 6l12 12M18 6 6 18"></path>',
    'upload': '<path d="M12 16V4M7 9l5-5 5 5"></path><path d="M4 16v3a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-3"></path>',
    'image': '<rect x="3" y="4" width="18" height="16" rx="3"></rect><circle cx="9" cy="10" r="2"></circle><path d="m21 16-5-5-9 9"></path>',
    'layers': '<path d="m12 3 9 5-9 5-9-5z"></path><path d="m3 13 9 5 9-5"></path>',
    'target': '<circle cx="12" cy="12" r="9"></circle><circle cx="12" cy="12" r="5"></circle><circle cx="12" cy="12" r="1.5"></circle>',
    'clock': '<circle cx="12" cy="12" r="9"></circle><path d="M12 7v5l3 2"></path>',
    'import': '<path d="M12 4v11M7 10l5 5 5-5"></path><path d="M4 19h16"></path>',
    'edit': '<path d="M4 20h4L19 9a2.8 2.8 0 0 0-4-4L4 16z"></path><path d="m13.5 6.5 4 4"></path>',
    'warn': '<path d="M12 3 2 20h20z"></path><path d="M12 10v4M12 17h.01"></path>',
    'file': '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"></path><path d="M14 3v5h5"></path>',
    'quiz': '<rect x="4" y="3" width="16" height="18" rx="2"></rect><path d="M8 8h8M8 12h5M8 16h3"></path>',
    'project': '<rect x="3" y="7" width="18" height="13" rx="2"></rect><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>',
    'badge': '<circle cx="12" cy="9" r="6"></circle><path d="m8.5 13.8-1.5 7.2 5-3 5 3-1.5-7.2"></path>',
    'cert2': '<rect x="3" y="4" width="18" height="13" rx="2"></rect><path d="M7 9h10M7 12h6"></path><path d="m14 17 1 4 2-1.2L19 21l1-4"></path>',
    'arrowr': '<path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path>',
    'chev': '<path d="m9 6 6 6-6 6"></path>',
    'down': '<path d="m6 9 6 6 6-6"></path>',
    'grip': '<circle cx="9" cy="7" r="1"></circle><circle cx="15" cy="7" r="1"></circle><circle cx="9" cy="12" r="1"></circle><circle cx="15" cy="12" r="1"></circle><circle cx="9" cy="17" r="1"></circle><circle cx="15" cy="17" r="1"></circle>',
}
SPARK = '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l1.9 6.1L20 10l-6.1 1.9L12 18l-1.9-6.1L4 10l6.1-1.9z"></path></svg>'

# ---------- toggles: chips, options and segments that work in Play ----------
class Toggles:
    def __init__(self):
        self.n = 0; self.d = {}; self.g = {}
    def new(self, on=False, group=None):
        self.n += 1; k = 't%d' % self.n
        self.d[k] = bool(on)
        if group: self.g[k] = group
        return k
    def chip(self, label, on=False, group=None, cls='', sub=''):
        k = self.new(on, group)
        s = (' <i>%s</i>' % sub) if sub else ''
        return '<button type="button" class="ds-chip%s {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}">%s<span>%s</span>%s</button>' % (
            (' ' + cls) if cls else '', k, k, k, ck(13), label, s)
    def seg(self, labels, on=0, group=None):
        group = group or 'g%d' % (self.n + 1)
        h = ''.join('<button type="button" class="{{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}">%s</button>' % ((lambda k: (k, k, k))(self.new(i == on, group)) + (l,)) for i, l in enumerate(labels))
        return '<div class="ds-seg">%s</div>' % h
    def opt(self, inner, on=False, group=None, cls=''):
        k = self.new(on, group)
        return '<button type="button" class="ds-opt%s {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}">%s<span class="ds-opt-ck">%s</span></button>' % (
            (' ' + cls) if cls else '', k, k, k, inner, ck(12))
    def js(self):
        return ('var T0 = %s, G = %s;\n' % (json.dumps(self.d), json.dumps(self.g)) +
                '''function togVals(self) {
  var t = self.state.t || T0, v = {};
  Object.keys(T0).forEach(function (k) {
    v['c'.concat(k)] = t[k] ? 'on' : ''; v['a'.concat(k)] = t[k] ? 'true' : 'false';
    v['x'.concat(k)] = function () {
      var n = Object.assign({}, t);
      if (G[k]) { Object.keys(G).forEach(function (j) { if (G[j] === G[k]) n[j] = false; }); n[k] = true; } else n[k] = !t[k];
      self.setState({ t: n });
    };
  });
  return v;
}
''')

# ---------- small pieces ----------
def av(src, ini, size=32, cls=''):
    if not src:  # organisation: initials badge, no photo
        return '<span class="av org%s" style="width: %dpx; height: %dpx">%s</span>' % ((' ' + cls) if cls else '', size, size, ini)
    return '<span class="av%s" style="width: %dpx; height: %dpx">%s<img src="%s" alt=""></span>' % ((' ' + cls) if cls else '', size, size, ini, src)

def stack(people, size=32):
    return '<span class="avs">%s</span>' % ''.join(av(s, i, size) for s, i in people)

def nova_sg(text, actions='', cls=''):
    """Nova suggestion strip (profile-bg gradient, as every Nova card)."""
    return ('<div class="nv-sg nova-card%s">%s<p><b>Nova</b> %s</p>%s</div>' %
            ((' ' + cls) if cls else '', nova_av('sm'), text, ('<div class="nv-sg-a">%s</div>' % actions) if actions else ''))

def nchip(label):
    """Nova action chip (small, sparkle)."""
    return '<button type="button" class="nv-chip">%s<span>%s</span></button>' % (SPARK, label)

def field(label, inner, hint='', tipt='', cls=''):
    t = tip(tipt) if tipt else ''
    h = ('<span class="fl-h">%s</span>' % hint) if hint else ''
    return '<div class="fl%s"><span class="fl-l">%s%s</span>%s%s</div>' % ((' ' + cls) if cls else '', label, t, h, inner)

def sel(value, label):
    return '<label class="sel"><span class="sr-only">%s</span><select class="ds-in"><option>%s</option></select>%s</label>' % (label, value, ic('down', 16, 2))

def tag(text, kind=''):
    return '<span class="ds-tag%s">%s</span>' % ((' ' + kind) if kind else '', text)

STATUS = {
    'ok': '<span class="st ok" aria-label="Done">%s</span>' % ck(11),
    'pr': '<span class="st pr" aria-label="In progress"></span>',
    'to': '<span class="st to" aria-label="Not started"></span>',
    'lk': '<span class="st lk" aria-label="Locked">%s</span>' % ICON(EXTRA['lock'], 13, 2),
}

# ---------- course workspace ----------
COURSE = 'Data Analysis with SQL'
# (label, href, status, key)
NAV = [
    ('Overview', [('Course Home', 'STU-009.dc.html', None, 'home')]),
    ('Design', [('Basics', 'STU-010.dc.html', 'ok', 'basics'), ('Audience & Prerequisites', 'STU-011.dc.html', 'ok', 'audience'),
                ('Career & Skills', 'STU-012.dc.html', 'pr', 'career'), ('Learning Outcomes', 'STU-014.dc.html', 'pr', 'outcomes'),
                ('Learning Design', 'STU-017.dc.html', None, 'design')]),
    ('Build', [('Curriculum', 'STU-020.dc.html', 'pr', 'curr'), ('Resources', '#', 'pr', 'res')]),
    ('Experience', [('Delivery & Schedule', '#', 'ok', 'deliv'), ('Learner Experience', '#', 'ok', 'lx'), ('Access & Pricing', '#', 'pr', 'price')]),
    ('Prepare', [('Course Review', '#', None, 'review'), ('Validation Readiness', '#', 'pr', 'ready')]),
    ('Validate · Gate', [('Validation', '#', 'lk', 'val')]),
    ('Publish · Gate', [('Publication', '#', 'lk', 'pub')]),
    ('Manage', [('Collaborators', '#', None, 'collab'), ('Course Settings', '#', None, 'settings')]),
]

SUBNAV = {'curr': [('Curriculum Builder', 'STU-020.dc.html', 'cb'), ('Completion Rules', '#', 'comp'), ('Team & Assignments', '#', 'team'),
                    ('DLP & Effort', '#', 'dlpe'), ('All Assessments', '#', 'alla')]}

def course_nav(active):
    h = ''
    for g, items in NAV:
        if g and g != 'Overview': h += '<span class="ds-glab">%s</span>' % g
        for label, href, st, key in items:
            sub = SUBNAV.get(key)
            open_ = bool(sub) and any(k == active for _, _, k in sub)
            on = key == active
            icon = ic('home', 18) if key == 'home' else ''
            if open_:
                h += '<a href="%s" class="cn-i cn-open">%s<span class="cn-t">%s</span>%s</a><div class="cn-sub">' % (href, ic('down', 15, 2.2), label, STATUS.get(st, '') if st else '')
                for sl, shref, sk in sub:
                    son = sk == active
                    h += '<a href="%s" class="cn-s%s"%s>%s</a>' % (shref, ' ds-on' if son else '', ' aria-current="page"' if son else '', sl)
                h += '</div>'
                continue
            h += '<a href="%s" class="cn-i%s"%s>%s<span class="cn-t">%s</span>%s</a>' % (
                href, ' ds-on' if on else '', ' aria-current="page"' if on else '', icon, label, STATUS.get(st, '') if st else '')
    return h

PHASES = [('Design', 'cur'), ('Build', 'pr'), ('Experience', 'pr'), ('Prepare', 'to'), ('Validate', 'lk'), ('Publish', 'lk')]
def phase_strip():
    out = ''
    for i, (p, s) in enumerate(PHASES):
        lk = ICON(EXTRA['lock'], 11, 2.2) if s == 'lk' else ''
        out += '<li class="ph-%s"><span class="ph-d">%s</span><span class="ph-l">%s</span></li>' % (s, lk, p)
    return '<ol class="ph" aria-label="Course phases: Design in progress">%s</ol>' % out

TEAM = [(ME, 'AO'), (M1, 'JA'), (None, 'AB')]

def topbar(nova_href='#', solo=False):
    return '''<header class="ds-top cw-top">
<button type="button" class="ds-icon-btn ds-menu" onClick="{{toggleNav}}" aria-label="Open course menu">%s</button>
<span class="cw-mt">%s</span>
%s
<span class="cw-sp"></span>
<a href="STU-009.dc.html" class="cw-hp ds-hide-sm"><span>Course Health</span><b>31%%</b></a>
%s
<a href="%s" class="cw-nova ds-hide-sm">%s<span>Nova</span></a>
<a href="#" class="ds-tok" aria-label="72,450 Creio">%s<span>72.4K</span></a>
<a href="#" class="cw-me" aria-label="Your account">%s</a>
</header>''' % (ic('menu', 20), COURSE, phase_strip(),
       '' if solo else '<a href="#" class="cw-team ds-hide-sm" aria-label="Team Chat">%s<span class="cw-chat">%s<span>Team Chat</span></span></a>' % (stack(TEAM, 30), ic('chat', 16, 2)),
       nova_href, nova_av('sm'), COIN('tp', 26), av(ME, 'AO', 40))

def sidebar(active):
    return '''<div class="ds-scrim {{navCls}}" onClick="{{toggleNav}}"></div>
<nav class="ds-side cw-side {{navCls}}" aria-label="Course">
<button type="button" class="ds-icon-btn ds-close" onClick="{{toggleNav}}" aria-label="Close menu">%s</button>
<a href="#" class="cw-back">%s<span>Dashboard</span></a>
<div class="cw-course">
<span class="cw-cv" aria-hidden="true">SQL</span>
<span class="cw-ct"><b>%s</b><span class="ds-tag">Draft</span></span>
</div>
<span class="cw-gap"></span>
%s
<div class="cw-lip"><span class="cw-lipl">Learning Intelligence Profile%s</span><b>9 <em>of 13 signals captured</em></b><span class="cw-hb"><i style="width: 69%%"></i></span></div>
</nav>''' % (ic('x', 18), ICON(I['back'], 16, 2), COURSE, course_nav(active), tip('Built quietly as you work. Next: career role, proficiency levels.'))

def acts(next_href, next_label='Save & continue', back_href=None, note=''):
    b = ('<a class="ds-link" href="%s">Back</a>' % back_href) if back_href else ''
    return ('<div class="ds-acts sb sv"><span class="sv-s">%s</span><span class="sv-r">%s%s</span></div>' %
            (note, b, btn(next_label, next_href)))

def page_head(eyebrow, h1, sub, right='', tabs=''):
    return ('<header class="pg-h ob-in"><div class="pg-hl"><span class="pg-e">%s</span><h1 class="ds-h1">%s</h1>%s</div>%s</header>%s' %
            (eyebrow, h1, ('<p class="ds-sub">%s</p>' % sub) if sub else '', ('<div class="pg-hr">%s</div>' % right) if right else '', tabs))

def subtabs(items, cur):
    """Steps inside one nav section (links to their boards)."""
    h = ''
    for i, (label, href) in enumerate(items):
        on = i == cur
        h += '<a href="%s" class="pt%s"%s><span class="pt-n">%d</span>%s</a>' % (href, ' on' if on else '', ' aria-current="step"' if on else '', i + 1, label)
    return '<nav class="pts ob-in2" aria-label="Steps in this section">%s</nav>' % h

def doc(title, css, body, js, preview=(1440, 900)):
    return '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>%s</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">
<style>
%s
</style>
</helmet>
%s
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":%d,"height":%d}}'>
%s
</script>
</body>
</html>
''' % (title, css, body, preview[0], preview[1], js)

def wrapper(title, target, props, w, h, bg='#F7F9FD'):
    p = ''.join(' %s="%s"' % kv for kv in props.items())
    return '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>%s</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">
<style>body{margin:0}</style>
</helmet>
<div style="width: 100%%; height: %dpx; overflow: hidden; background: %s">
<dc-import name="%s"%s hint-size="%s,%dpx"></dc-import>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":%d,"height":%d}}'>
class Component extends DCLogic {
  renderVals() { return {}; }
}
</script>
</body>
</html>
''' % (title, h, bg, target, p, '100%' if w > 600 else '%dpx' % w, h, w, h)

BASE_CSS = r'''body{margin:0;background:#F7F9FD}
a{color:#1652F0}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.lg-word{display:block;height:26px;aspect-ratio:292/56;background:url(WORD) left center/contain no-repeat}
.av{position:relative;flex-shrink:0;display:inline-flex;align-items:center;justify-content:center;border-radius:50%;overflow:hidden;background:#EAF0FF;color:#0E3BB8;font-size:11px;font-weight:600;box-sizing:border-box}
.av img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.av.org{background:#0B1433;color:#FFFFFF;font-size:10.5px;letter-spacing:.02em}
.avs{display:inline-flex;align-items:center}
.avs .av{box-shadow:0 0 0 2px #FFFFFF}
.avs .av + .av{margin-left:-8px}
.st{width:18px;height:18px;border-radius:50%;flex-shrink:0;box-sizing:border-box;display:inline-flex;align-items:center;justify-content:center}
.st.ok{background:#E7F5EE;color:#0F6B45}
.st.pr{border:2px solid #1652F0;background:conic-gradient(#1652F0 0 50%,#FFFFFF 50% 100%)}
.st.to{border:2px solid #CBD3E6}
.st.lk{color:#8A93AD}
.nv-sg{display:flex;align-items:center;gap:14px;padding:14px 16px 14px 14px;border-radius:16px;border:1.5px solid #DCE5FB}
.nv-sg p{margin:0;flex:1;min-width:0;font-size:14.5px;line-height:1.5;color:#3A4566}
.nv-sg p b{color:#0B1433;font-weight:600;margin-right:4px}
.nv-sg-a{display:flex;align-items:center;gap:10px;flex-shrink:0}
.nv-chip{display:inline-flex;align-items:center;gap:7px;height:36px;padding:0 14px;box-sizing:border-box;border-radius:999px;border:1.5px solid #CBD7F5;background:#FFFFFF;color:#0E3BB8;font-family:inherit;font-size:13.5px;font-weight:500;cursor:pointer;white-space:nowrap;transition:border-color .2s ease,background .2s ease}
.nv-chip svg{color:#1652F0}
.nv-chip:hover{border-color:#1652F0;background:#F5F8FF}
.nv-chip:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:2px}
.fl{display:flex;flex-direction:column;gap:8px;min-width:0}
.fl-l{display:flex;align-items:center;font-size:14px;font-weight:600;color:#0B1433}
.fl-h{margin-top:-4px;font-size:13px;line-height:1.45;color:#5B6582}
.sel{position:relative;display:block}
.sel select{appearance:none;-webkit-appearance:none;padding-right:40px;cursor:pointer}
.sel svg{position:absolute;right:14px;top:50%;transform:translateY(-50%);color:#5B6582;pointer-events:none}
textarea.ds-in{height:auto;min-height:110px;padding:12px 14px;line-height:1.55;resize:vertical}
.chips{display:flex;flex-wrap:wrap;gap:8px}
@media (max-width: 760px){
.nv-sg{flex-wrap:wrap;padding:14px}
.nv-sg p{flex-basis:calc(100% - 44px)}
.nv-sg-a{width:100%;padding-left:42px;box-sizing:border-box;flex-wrap:wrap}
}
'''.replace('WORD', WORD)

CW_CSS = r'''.ds-root{grid-template-columns:272px minmax(0,1fr)}
.cw-side{padding:18px 14px 28px 14px;gap:1px}
.cw-back{display:inline-flex;align-items:center;gap:8px;align-self:flex-start;height:36px;padding:0 12px 0 10px;border-radius:999px;color:#3A4566;font-size:13.5px;font-weight:500;text-decoration:none}
.cw-back:hover{background:#F5F8FF;color:#0B1433}
.cw-course{display:flex;align-items:center;gap:12px;margin:10px 6px 0 6px}
.cw-cv{width:44px;height:44px;flex-shrink:0;border-radius:12px;background:linear-gradient(140deg,#1652F0,#0B1433);color:#FFFFFF;font-size:12px;font-weight:600;letter-spacing:.04em;display:flex;align-items:center;justify-content:center}
.cw-ct{display:flex;flex-direction:column;min-width:0}
.cw-ct b{font-size:15px;font-weight:600;line-height:1.25;color:#0B1433}
.cw-ct span{margin-top:2px;font-size:12.5px;color:#5B6582}
.cw-health{margin:16px 6px 6px 6px;padding:12px 14px;border-radius:14px;background:#F7F9FD;display:grid;grid-template-columns:1fr auto;align-items:center;row-gap:8px}
.cw-hl{display:flex;align-items:center;font-size:12.5px;font-weight:500;color:#3A4566}
.cw-health b{font-size:14px;font-weight:600}
.cw-hb{grid-column:1 / -1;height:6px;border-radius:6px;background:#E6EAF3;overflow:hidden}
.cw-hb i{display:block;height:100%;border-radius:6px;background:#1652F0}
.cw-gap{height:8px;flex-shrink:0}
.cw-side .ds-glab{margin:12px 12px 3px 12px;font-size:11.5px}
.cn-i{display:flex;align-items:center;gap:10px;min-height:34px;padding:0 10px 0 12px;border-radius:11px;color:#3A4566;font-size:14px;font-weight:500;text-decoration:none;transition:background .2s ease,color .2s ease}
.cn-i svg{flex-shrink:0;color:#5B6582}
.cn-i:hover{background:#F5F8FF;color:#0B1433}
.cn-t{flex-grow:1;min-width:0}
.cn-open{color:#0B1433;font-weight:600}
.cn-open svg{margin-left:-4px;color:#1652F0}
.cn-sub{display:flex;flex-direction:column;gap:1px;margin:2px 0 4px 20px;padding-left:10px;border-left:2px solid #E6EAF3}
.cn-s{display:flex;align-items:center;min-height:32px;padding:0 10px;border-radius:10px;color:#3A4566;font-size:13.5px;font-weight:500;text-decoration:none}
.cn-s:hover{background:#F5F8FF;color:#0B1433}
.cn-s.ds-on{position:relative}
.cn-s.ds-on::before{content:'';position:absolute;left:-12px;top:6px;bottom:6px;width:2px;border-radius:2px;background:#1652F0}
.cn-i.ds-on .st.to{border-color:#9DB8F7}
.cw-top{gap:14px}
.cw-mt{display:none;font-size:15px;font-weight:600;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cw-sp{flex-grow:1}
.ph{list-style:none;margin:0;padding:0;display:flex;align-items:center}
.ph li{display:flex;align-items:center;gap:7px;font-size:13px;font-weight:500;color:#5B6582;white-space:nowrap}
.ph li + li::before{content:'';width:22px;height:2px;border-radius:2px;margin:0 8px 0 2px;background:#D6DDEE}
.ph-d{width:10px;height:10px;box-sizing:border-box;border-radius:50%;border:2px solid #CBD3E6;background:#FFFFFF;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0}
.ph-cur{color:#0B1433 !important;font-weight:600 !important}
.ph-cur .ph-d{width:12px;height:12px;border:0;background:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.16)}
.ph-pr .ph-d{border-color:#1652F0}
.ph-pr + li::before,.ph-cur + li::before{background:linear-gradient(90deg,#1652F0,#D6DDEE)}
.ph-lk{color:#8A93AD !important}
.ph-lk .ph-d{width:auto;height:auto;border:0;background:none;color:#8A93AD}
.cw-team{display:inline-flex;align-items:center;gap:8px;height:44px;padding:0 12px 0 7px;box-sizing:border-box;border-radius:999px;border:1.5px solid #E6EAF3;background:#FFFFFF;color:#3A4566;text-decoration:none}
.cw-team:hover{border-color:#AFC1F5}
.cw-chat{display:flex;align-items:center;gap:6px;color:#3A4566;font-size:13.5px;font-weight:500;white-space:nowrap}
.cw-hp{display:inline-flex;align-items:center;gap:8px;height:44px;padding:0 14px;box-sizing:border-box;border-radius:999px;background:#FFFFFF;border:1.5px solid #E6EAF3;color:#3A4566;font-size:13.5px;font-weight:500;text-decoration:none;white-space:nowrap}
.cw-hp b{color:#0B1433;font-weight:600}
.cw-hp:hover{border-color:#AFC1F5}
.cw-ct .ds-tag{align-self:flex-start;margin-top:5px;height:22px;font-size:11.5px}
.cw-lip{margin:18px 6px 0 6px;padding:12px 14px;border-radius:14px;background:#F7F9FD;display:flex;flex-direction:column;gap:6px}
.cw-lipl{display:flex;align-items:center;font-size:12.5px;font-weight:500;color:#3A4566}
.cw-lip b{font-size:15px;font-weight:600}
.cw-lip b em{font-style:normal;font-size:12.5px;font-weight:400;color:#5B6582}
.cw-hb{height:6px;border-radius:6px;background:#E6EAF3;overflow:hidden}
.cw-hb i{display:block;height:100%;border-radius:6px;background:#1652F0}
.cw-nova{display:inline-flex;align-items:center;gap:8px;height:44px;padding:0 16px 0 6px;box-sizing:border-box;border-radius:999px;border:1.5px solid #CBD7F5;background:#FFFFFF;color:#0E3BB8;font-size:14px;font-weight:600;text-decoration:none;white-space:nowrap}
.cw-nova:hover{border-color:#1652F0;background:#F5F8FF}
.cw-me{display:flex;border-radius:50%;text-decoration:none}
.ds-main{max-width:1180px;padding:20px clamp(20px,3vw,44px) 40px clamp(20px,3vw,44px)}
.pg-h{display:flex;align-items:flex-end;justify-content:space-between;gap:24px}
.pg-hl{min-width:0}
.pg-e{display:block;margin-bottom:8px;font-size:13px;font-weight:600;color:#1652F0}
.pg-hr{flex-shrink:0;display:flex;align-items:center;gap:10px}
.pts{display:flex;gap:6px;margin-top:22px;padding:5px;border-radius:999px;background:#EEF1F7;width:max-content;max-width:100%;box-sizing:border-box;overflow-x:auto;scrollbar-width:none}
.pts::-webkit-scrollbar{display:none}
.pt{display:inline-flex;align-items:center;gap:8px;height:36px;padding:0 16px 0 8px;border-radius:999px;color:#3A4566;font-size:14px;font-weight:500;text-decoration:none;white-space:nowrap}
.pt:hover{color:#0B1433}
.pt-n{width:22px;height:22px;border-radius:50%;background:#FFFFFF;color:#5B6582;font-size:12px;font-weight:600;display:flex;align-items:center;justify-content:center}
.pt.on{background:#FFFFFF;color:#0B1433;font-weight:600;box-shadow:0 1px 2px rgba(11,20,51,.08),0 6px 14px -8px rgba(11,20,51,.25)}
.pt.on .pt-n{background:#1652F0;color:#FFFFFF}
.fc{padding:28px 32px 30px 32px;margin-top:24px}
.fc + .fc{margin-top:16px}
.fc-h{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-bottom:22px}
.fc-h h2{margin:0;display:flex;align-items:center;font-size:18px;font-weight:600;letter-spacing:-0.01em}
.fc-h p{margin:4px 0 0 0;font-size:14px;line-height:1.5;color:#5B6582}
.fg{display:grid;gap:22px}
.fg2{grid-template-columns:repeat(2,minmax(0,1fr))}
.fg3{grid-template-columns:repeat(3,minmax(0,1fr))}
.sv{position:sticky;bottom:0;z-index:5;margin:24px 0 0 0;padding:14px 14px 14px 22px;border-radius:999px;background:rgba(255,255,255,.94);border:1.5px solid #E6EAF3;box-shadow:0 18px 40px -24px rgba(11,20,51,.35);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}
.sv-s{display:inline-flex;align-items:center;gap:8px;font-size:13.5px;color:#5B6582}
.sv-s svg{color:#0F6B45}
.sv-r{display:inline-flex;align-items:center;gap:20px}
@media (max-width: 1280px){.ph li + li::before{width:12px;margin:0 6px 0 0}.ph-l{font-size:12.5px}}
@media (max-width: 1560px){.cw-chat span{display:none}.cw-team{padding-right:10px}.ph li + li::before{width:14px;margin:0 6px 0 0}}
@media (max-width: 1180px){.cw-hp{display:none !important}.ds-root{grid-template-columns:248px minmax(0,1fr)}.ph-pr .ph-l,.ph-to .ph-l,.ph-lk .ph-l{display:none}}
@media (max-width: 960px){
.ds-root{grid-template-columns:minmax(0,1fr)}
.cw-mt{display:block;flex:1 1 auto}
.ph,.cw-sp{display:none}
.cw-me .av{width:36px !important;height:36px !important}
.ds-main{padding:16px 16px 0 16px}
.pg-h{flex-direction:column;align-items:flex-start;gap:14px}
.pg-e{margin-bottom:6px;font-size:12.5px}
.pts{margin-top:16px;width:auto}
.pt{height:34px;font-size:13.5px}
.fc{padding:20px 18px 22px 18px;margin-top:18px;border-radius:18px}
.fc-h{margin-bottom:16px;flex-wrap:wrap}
.fc-h h2{font-size:16.5px}
.fg2,.fg3{grid-template-columns:minmax(0,1fr)}
.fg{gap:18px}
.sv{margin:24px -16px 0 -16px;border-radius:0;border:0;border-top:1.5px solid #EEF1F7;padding:12px 16px 14px 16px;box-shadow:none}
.sv-s{display:none}
.sv-r{flex-direction:column-reverse;align-items:stretch;gap:4px;width:100%}
.sv-r .ds-btn{width:100%;justify-content:space-between}
.sv-r .ds-link{justify-content:center;min-height:40px}
}
'''

FOCUS_CSS = r'''.fx-root{min-height:100vh;display:flex;flex-direction:column;background:#FFFFFF;font-family:'Google Sans','Google Sans Text','Helvetica Neue',system-ui,sans-serif;color:#0B1433;position:relative;isolation:isolate}
.fx-root::before{content:'';position:absolute;z-index:-1;left:0;right:0;top:64px;height:340px;pointer-events:none;background:linear-gradient(180deg,#F2F6FF,rgba(242,246,255,0))}
.fx-top{height:64px;flex-shrink:0;box-sizing:border-box;display:flex;align-items:center;gap:16px;padding:0 20px;border-bottom:1.5px solid #EEF1F7;background:#FFFFFF;position:relative}
.fx-x{width:40px;height:40px;flex-shrink:0;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#3A4566;text-decoration:none}
.fx-x:hover{background:#F5F8FF;color:#0B1433}
.fx-title{display:flex;align-items:baseline;gap:8px;min-width:0}
.fx-t1{font-size:16px;font-weight:600;white-space:nowrap}
.fx-t2{font-size:14px;color:#5B6582;white-space:nowrap}
.fx-step{font-size:13.5px;color:#5B6582;white-space:nowrap}
.fx-bar{position:absolute;left:0;bottom:-1.5px;height:3px;border-radius:0 3px 3px 0;background:linear-gradient(90deg,#1652F0,#5C86FF);transition:width .6s ease}
.fx-main{flex-grow:1;display:flex;justify-content:center;align-items:center;padding:clamp(36px,6vh,64px) 24px 56px 24px}
.fx-col{width:min(1040px,100%);display:flex;flex-direction:column}
.fx-col.n{width:min(760px,100%)}
.fx-h1{margin:0;font-size:clamp(32px,4.6vh,42px);line-height:1.12;font-weight:600;letter-spacing:-0.035em}
.fx-sub{margin:12px 0 0 0;max-width:620px;font-size:16.5px;line-height:1.55;color:#4A5578}
.fx-back{display:inline-flex;align-items:center;gap:8px;align-self:flex-start;height:36px;margin:0 0 18px -10px;padding:0 14px 0 10px;border-radius:999px;color:#3A4566;font-size:14px;font-weight:500;text-decoration:none}
.fx-back:hover{background:#F5F8FF;color:#0B1433}
.fx-acts{margin-top:32px;display:flex;align-items:center;justify-content:flex-end;gap:20px}
@media (max-width: 960px){
.fx-top{height:56px;padding:0 12px 0 6px;gap:8px}
.fx-t2{display:none}
.fx-main{align-items:flex-start;padding:24px 16px 0 16px}
.fx-h1{font-size:26px}
.fx-sub{font-size:14.5px;margin-top:8px}
.fx-back{margin-bottom:10px}
.fx-acts{position:sticky;bottom:0;z-index:5;margin:28px -16px 0 -16px;padding:12px 16px 14px 16px;background:#FFFFFF;border-top:1.5px solid #EEF1F7;flex-direction:column-reverse;align-items:stretch;gap:4px}
.fx-acts .ds-btn{width:100%;justify-content:space-between}
.fx-acts .ds-link{justify-content:center;min-height:40px}
}
'''

def write(name, s):
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, name), 'w').write(fixblobs(s))
