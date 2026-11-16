"""Landing batch 7 (client review, "Also found"): Explore filters (shared + per learning type), loading / empty /
no-results / error states on the listings, and signed-in views for certificates and programs.
Patches the live sources in place:
  Explore, CareerPaths, Certifications, Programs  -> prop state = '' | loading | empty | noresults | error
  all six (+ CertDetail, ProgramDetail)           -> prop viewer = guest | learner (signed-in header: DLP balance + avatar)
  Explore                                         -> filter bar + panel (prop view = '' | filters)
  ProgramDetail                                   -> app states enrolled + done
Usage: python3 st7.py <canvas3/project>"""
import re, sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import kit
from kit import ck, ARROW
D = sys.argv[1]
def svg(d, w=18, sw=2):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (w, w, sw, d)
I_ERR = svg('<path d="M12 4 2.5 20h19z"></path><path d="M12 10v4M12 17v.2"></path>', 24, 2)
I_EMP = svg('<path d="M4 8l8-4 8 4v8l-8 4-8-4z"></path><path d="M4 8l8 4 8-4M12 12v8"></path>', 24, 1.9)
I_NO = svg('<circle cx="11" cy="11" r="7"></circle><path d="m20 20-3.5-3.5M8.5 11h5"></path>', 24, 2)
FILTI = svg('<path d="M4 6h16M7 12h10M10 18h4"></path>', 16, 2.2)
X = svg('<path d="M6 6l12 12M18 6 6 18"></path>', 13, 2.4)
C = open(os.path.join(D, 'Courses.dc.html')).read(); CST = C[C.find('<style>'):C.find('</style>')]
DLP = '\n'.join(re.findall(r'(?:^|\n)(\.dlp-c[^{]*\{[^}]*\})', CST)) + '\n' + '\n'.join(re.findall(r'@keyframes dlp\w+\{(?:[^{}]*\{[^}]*\})*\}', C))
HDR_CSS = ('.sx-dlp{height:36px;padding:0 12px 0 8px;border-radius:999px;background:#F5F8FF;border:1px solid #DCE5FB;display:flex;align-items:center;gap:8px;font-size:14px;font-weight:600;color:#0B1433;text-decoration:none;white-space:nowrap}\n'
           '.sx-av{width:40px;height:40px;border-radius:999px;background:#DCE5FB;color:#1652F0;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:600}\n'
           '.pav-h{position:relative !important;overflow:hidden !important}\n.pav{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;border-radius:inherit;display:block;pointer-events:none}\n'
           '@media (max-width: 520px){.sx-dlp b span{display:none}}\na.sx-av{text-decoration:none}\n')
HDR_OLD = re.compile(r'<a class="sx-link sx-login" href="#" style="font-weight: 600; color: #0B1433">Log in</a>\n<a class="(?:ds-btn sm np|sx-cta)" href="OnbWelcome.dc.html">Create account</a>')
HDR_NEW = ('<sc-if value="{{st7Guest}}" hint-placeholder-val="{{ true }}">\n<a class="sx-link sx-login" href="#" style="font-weight: 600; color: #0B1433">Log in</a>\n<a class="ds-btn sm np" href="OnbWelcome.dc.html">Create account</a>\n</sc-if>\n'
           '<sc-if value="{{st7Learner}}" hint-placeholder-val="{{ false }}">\n<a class="sx-dlp" href="Usage.dc.html" aria-label="1,460 DLP available. View usage"><span class="dlp-c"></span><b style="font-weight: 600">1,460<span style="font-weight: 500; color: #5B6582"> available</span></b></a>\n'
           '<a class="sx-av pav-h" href="Dashboard.dc.html" aria-label="Your account">AO<img class="pav" src="/_blob/9112077cc7e3c1c839edc7e609d87954" alt=""></a>\n</sc-if>')

def block(name):
    sk = ''.join('<div class="st7-sk"><i class="st7-b st7-b1"></i><i class="st7-b st7-b2"></i><i class="st7-b st7-b3"></i><i class="st7-b st7-b4"></i></div>' for _ in range(4))
    return ('<sc-if value="{{st7Loading}}" hint-placeholder-val="{{ false }}"><div class="st7 st7-load" aria-busy="true" aria-live="polite"><span class="st7-sr">Loading %s…</span>%s</div></sc-if>\n'
            '<sc-if value="{{st7Msg}}" hint-placeholder-val="{{ false }}"><div class="st7 st7-msg {{st7Cls}}" role="status"><span class="st7-i">'
            '<sc-if value="{{st7IsErr}}" hint-placeholder-val="{{ false }}">%s</sc-if><sc-if value="{{st7IsEmpty}}" hint-placeholder-val="{{ false }}">%s</sc-if><sc-if value="{{st7IsNo}}" hint-placeholder-val="{{ false }}">%s</sc-if></span>'
            '<b>{{st7T}}</b><span class="st7-d">{{st7D}}</span><div class="st7-a"><button class="ds-btn sm" type="button"><span>{{st7Cta}}</span><span class="ob-arrow">%s</span></button><a class="ds-link" href="{{st7AltHref}}">{{st7Alt}}</a></div>'
            '<sc-if value="{{st7HasSug}}" hint-placeholder-val="{{ false }}"><div class="st7-sug"><span>Try instead</span><sc-for list="{{st7Sug}}" as="g" hint-placeholder-count="3"><a class="ds-chip sm" href="{{g.h}}">{{g.t}}</a></sc-for></div></sc-if></div></sc-if>\n') % (
        name, sk, I_ERR, I_EMP, I_NO, ARROW)

ST_CSS = r'''
.st7{grid-column:1 / -1}
.st7-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.st7-load{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.st7-sk{display:flex;flex-direction:column;gap:12px;padding:22px;border-radius:20px;border:1.5px solid #EEF1F7;background:#FFFFFF}
.st7-b{display:block;height:14px;border-radius:8px;background:linear-gradient(90deg,#EEF1F7 0%,#F7F9FD 50%,#EEF1F7 100%);background-size:200% 100%;animation:st7Sh 1.4s ease-in-out infinite}
.st7-b1{width:44px;height:44px;border-radius:14px}
.st7-b2{width:70%;height:20px}
.st7-b3{width:90%}
.st7-b4{width:45%;margin-top:18px}
@keyframes st7Sh{0%{background-position:100% 0}100%{background-position:-100% 0}}
@media (prefers-reduced-motion: reduce){.st7-b{animation:none}}
.st7-msg{display:flex;flex-direction:column;align-items:center;text-align:center;gap:10px;padding:44px 28px;border-radius:22px;border:1.5px dashed #CBD7F5;background:#FAFBFF}
.st7-i{width:56px;height:56px;border-radius:50%;background:#EAF0FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.st7-err{background:#FFFBF2;border-color:#F0C774}
.st7-err .st7-i{background:#FFF1D6;color:#8A5A00}
.st7-msg > b{font-size:20px;font-weight:600;color:#0B1433}
.st7-d{max-width:480px;font-size:14.5px;line-height:1.55;color:#5B6582}
.st7-a{display:flex;align-items:center;justify-content:center;gap:20px;flex-wrap:wrap;margin-top:6px}
.st7-sug{display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:8px;margin-top:10px;font-size:13px;color:#8A93AD}
.st7-sug .ds-chip{text-decoration:none;color:#0B1433}
.cp4-main:has(.st7) .cp-grid,.cp4-main:has(.st7) .ct-grid,.cp4-main:has(.st7) .pg-list,.cp4-main:has(.st7) .cs-chips,.cp4-main:has(.st7) .cp4-ct{display:none}
.cp4-main:has(.st7) ~ .cp4-pg{display:none}
.cp4-lay:has(.st7) .cp4-pg,.cp4-lay:has(.pl6-none) .cp4-pg{display:none}
.ex-body:has(.st7) .ex7-n{display:none}
.pg-body:has(.st7) .pg-feat{display:none}
.ex-body:has(.st7) .ex-sec,.ex-body:has(.st7) .ex-note{display:none}
@media (max-width: 760px){.st7-load{grid-template-columns:minmax(0,1fr);gap:10px}.st7-sk:nth-child(n+3){display:none}.st7-msg{padding:32px 18px}.st7-a{flex-direction:column;align-items:stretch;gap:10px}.st7-a .ds-btn{justify-content:space-between}}
'''

PAGES = {
 'CareerPaths': dict(at='<div class="cp-grid">', name='career paths', lists=['paths'], none='none', count='countLabel',
    empty=('No career paths in Health yet', 'Creators are building the first ones. We can tell you when one is published.', 'Tell me when one is ready', 'See all career paths', 'CareerPaths.dc.html'),
    no=('No career paths match “astrophysics”', 'Try a role or a skill instead, or ask Nova to build a route around your goal.', 'Clear the search', 'Ask Nova', '#', [('Data Analyst', 'PathDetail.dc.html'), ('Product Designer', 'CareerPaths.dc.html'), ('Find my path', '#')]),
    err=('We couldn’t load career paths', 'Check your connection and try again. Your search and filters are kept.', 'Try again', 'Go to Explore learning', 'Explore.dc.html')),
 'Certifications': dict(at='<div class="ct-grid">', name='certifications', lists=['certs'], none='none', count='countLabel',
    empty=('No certifications in Health yet', 'Issuers are preparing the first ones. We can tell you when one opens for registration.', 'Tell me when one opens', 'See all certifications', 'Certifications.dc.html'),
    no=('No certifications match “astrophysics”', 'Try a skill or a role instead, or remove a filter. Nova can suggest what to prepare first.', 'Clear the search', 'Ask Nova', '#', [('Data Analysis', 'CertDetail.dc.html'), ('Project Management', 'Certifications.dc.html'), ('Security Operations', 'Certifications.dc.html')]),
    err=('We couldn’t load certifications', 'Check your connection and try again. Your search and filters are kept.', 'Try again', 'Go to Explore learning', 'Explore.dc.html')),
 'Programs': dict(at='<div class="pg-list">', name='programs', lists=['progs'], none='none', count='count',
    empty=('No programs are open right now', 'New cohorts are announced every few weeks. Self-paced learning is always available.', 'Tell me when one opens', 'Browse self-paced courses', 'Courses.dc.html'),
    no=('No programs match “astrophysics”', 'Try a field or a role instead, or remove a filter.', 'Clear the search', 'Ask Nova', '#', [('AI & Data Analytics', 'ProgramDetail.dc.html'), ('Product Design Cohort', 'Programs.dc.html'), ('Self-paced options', 'Courses.dc.html')]),
    err=('We couldn’t load programs', 'Check your connection and try again. Your filters are kept.', 'Try again', 'Go to Explore learning', 'Explore.dc.html')),
 'Explore': dict(at='<div class="ex-body">', after=True, name='learning', lists=['paths', 'courses', 'certs', 'progs'], none=None, count=None,
    empty=('Nothing published in this topic yet', 'Try another topic, or ask Nova to plan a route from what’s available.', 'Ask Nova', 'See all topics', 'Explore.dc.html'),
    no=('Nothing matches “astrophysics”', 'Try a role, a skill or a broader word. Nova can also plan a route from your goal.', 'Clear the search', 'Ask Nova', '#', [('Data analysis', 'Courses.dc.html'), ('Product design', 'Courses.dc.html'), ('Become a Data Analyst', 'PathDetail.dc.html')]),
    err=('We couldn’t load learning right now', 'Check your connection and try again. Your search is kept.', 'Try again', 'Browse courses', 'Courses.dc.html')),
}

# ---------------------------------------------------------------- Explore filters
EXF = r'''
<div class="ex7-fb">
<button class="ds-chip sm {{f7Cls}}" type="button" aria-expanded="{{f7Exp}}" onClick="{{f7Toggle}}">FILTI<span>Filters</span><sc-if value="{{f7Has}}" hint-placeholder-val="{{ false }}"><i>{{f7N}}</i></sc-if></button>
<sc-for list="{{f7Active}}" as="a" hint-placeholder-count="2"><button class="ds-chip sm on" type="button" onClick="{{a.drop}}" aria-label="Remove filter {{a.label}}">{{a.label}}X</button></sc-for>
<sc-if value="{{f7Has}}" hint-placeholder-val="{{ false }}"><button class="ds-link" type="button" onClick="{{f7Clear}}">Clear all</button></sc-if>
<span class="ex7-n">{{f7Count}}</span>
</div>
<sc-if value="{{f7Open}}" hint-placeholder-val="{{ false }}"><div class="ex7-fp" role="group" aria-label="Filters">
<sc-for list="{{f7Groups}}" as="g" hint-placeholder-count="5"><div class="ex7-g {{g.cls}}"><span class="cs-gl">{{g.label}}</span><div class="cs-cw"><sc-for list="{{g.opts}}" as="o" hint-placeholder-count="3"><button class="ds-chip sm {{o.cls}}" type="button" role="checkbox" aria-checked="{{o.on}}" onClick="{{o.pick}}">CK{{o.label}}<i>{{o.n}}</i></button></sc-for></div></div></sc-for>
<p class="ex7-note">{{f7Note}}</p>
</div></sc-if>
'''.replace('FILTI', FILTI).replace('X</button>', X + '</button>').replace('CK', ck(12))
EXF_CSS = r'''
.ex7-fb{display:flex;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:6px}
.ex7-fb .ds-chip i{font-style:normal;min-width:18px;height:18px;padding:0 5px;box-sizing:border-box;border-radius:999px;background:#1652F0;color:#FFFFFF;font-size:11px;display:inline-flex;align-items:center;justify-content:center}
.ex7-n{margin-left:auto;font-size:14px;color:#5B6582}
.ex7-fp{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:18px 24px;padding:20px 22px;border-radius:20px;border:1.5px solid #E6EAF3;background:#FFFFFF;box-shadow:0 22px 44px -36px rgba(11,20,51,.45);margin-bottom:10px}
.ex7-g{display:flex;flex-direction:column;gap:2px}
.ex7-g .cs-gl{display:flex;align-items:center;margin-bottom:10px;font-size:12px;font-weight:600;letter-spacing:.8px;color:#8A93AD}
.ex7-g .cs-cw{display:flex;flex-wrap:wrap;gap:6px}
.ex7-g .ds-chip i{font-style:normal;font-size:12px;color:#8A93AD}
.ex7-g.ex7-t{padding-left:22px;border-left:1.5px solid #EEF1F7}
.ex7-g.ex7-t .cs-gl{color:#1652F0}
.ex7-note{grid-column:1 / -1;margin:0;padding-top:12px;border-top:1px solid #EEF1F7;font-size:13px;color:#8A93AD}
@media (max-width: 1180px){.ex7-fp{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media (max-width: 760px){.ex7-fp{grid-template-columns:minmax(0,1fr);gap:16px;padding:16px}.ex7-g.ex7-t{padding-left:0;border-left:0;padding-top:16px;border-top:1px solid #EEF1F7}.ex7-n{flex-basis:100%;margin:2px 0 0}}
'''
EXF_JS = r'''
  f7(x, k) {
    var S = this.state, f = S.f7 || {}, self = this;
    var LV = { Foundation: 'Beginner', Professional: 'Intermediate' }, TN = { gold: 'Gold', silver: 'Silver', bronze: 'Bronze', rev: 'In review' };
    var v = this.f7v(x, k);
    return Object.keys(f).every(function (g) { var on = f[g] || []; return !on.length || on.some(function (o) { return (v[g] || []).indexOf(o) > -1; }); });
  }
  f7v(x, k) {
    var LV = { Foundation: 'Beginner', Professional: 'Intermediate' }, TN = { gold: 'Gold', silver: 'Silver', bronze: 'Bronze', rev: 'In review' };
    var GX = { 'Applied Project Leadership': ['Intermediate', 'Hybrid'], 'AI for Business Leaders': ['Advanced', 'In person'], 'Frontend Engineering Bootcamp': ['Beginner', 'Live online'], 'Clinical Data Program': ['Intermediate', 'Hybrid'] };
    if (k === 'p') { var mo = parseInt((x.time.split('–')[1] || x.time)); return { lvl: [x.lvl.split(' ')[0]], tier: [TN[TP_[x.t][2]]], acc: ['Subscription (DLP)', 'Own with Credits'], lang: ['English'], len: [mo <= 8 ? 'Up to 8 months' : 'Over 8 months'] }; }
    if (k === 'c') return { lvl: [x.lvl], tier: [TN[x.tier]], acc: x.free ? ['Free'] : (x.life > 0 ? ['Subscription (DLP)', 'Own with Credits'] : ['Subscription (DLP)']), lang: [x.t.indexOf('Introduction à') === 0 ? 'French' : 'English'], dur: [x.hrs < 5 ? 'Under 5 hrs' : (x.hrs <= 10 ? '5–10 hrs' : 'Over 10 hrs')] };
    if (k === 'ce') return { lvl: [LV[x.level] || x.level], tier: [TN[TC_[x.short][2]]], acc: ['Own with Credits'], lang: ['English'], fmt: ['Exam', 'Practical', 'Portfolio'].filter(function (f) { var s = x.format.toLowerCase(); return s.indexOf(f.toLowerCase()) > -1 || (f === 'Practical' && /case|lab|simulation|build/.test(s)); }) };
    var g = GX[x.t] || ['Intermediate', 'Live online'];
    return { lvl: [g[0]], tier: [TN[TG_[x.t][2]]], acc: ['Own with Credits'], lang: ['English'], pfmt: [g[1]] };
  }
'''
EXF_VALS = r'''
    var f7 = S.f7 || {}, tab = S.tab;
    var T7 = { courses: ['dur', 'Duration', ['Under 5 hrs', '5–10 hrs', 'Over 10 hrs'], 'c'], certs: ['fmt', 'Assessment', ['Exam', 'Practical', 'Portfolio'], 'ce'], paths: ['len', 'Length', ['Up to 8 months', 'Over 8 months'], 'p'], programs: ['pfmt', 'Format', ['Live online', 'In person', 'Hybrid'], 'g'] };
    var srcs = [['p', this.P, 'paths'], ['c', this.C, 'courses'], ['ce', this.CE, 'certs'], ['g', this.G, 'programs']].filter(function (s) { return tab === 'you' || tab === s[2]; });
    var base = function (x) { return (S.topic === 'All' || x.topic === S.topic) && (!S.q || (x.t + ' ' + (x.by || '') + ' ' + (x.d || '') + ' ' + x.topic).toLowerCase().indexOf(S.q.toLowerCase()) >= 0); };
    var cnt = function (g, o) { var n = 0; srcs.forEach(function (s) { s[1].forEach(function (x) { if (!base(x)) return; var v = self.f7v(x, s[0]); if ((v[g] || []).indexOf(o) < 0) return; var ff = Object.assign({}, f7); delete ff[g]; var ok = Object.keys(ff).every(function (k) { var on = ff[k] || []; return !on.length || on.some(function (q) { return (v[k] || []).indexOf(q) > -1; }); }); if (ok) n++; }); }); return n; };
    var tg = function (g, o) { var f = Object.assign({}, f7), l = (f[g] || []).slice(), i = l.indexOf(o); if (i > -1) l.splice(i, 1); else l.push(o); f[g] = l; self.setState({ f7: f }); };
    var G7 = [['lvl', 'Level', ['Beginner', 'Intermediate', 'Advanced'], ''], ['tier', 'Validation', ['Gold', 'Silver', 'Bronze'], ''], ['acc', 'Access', ['Free', 'Subscription (DLP)', 'Own with Credits'], ''], ['lang', 'Language', ['English', 'French'], '']];
    if (T7[tab]) G7.push([T7[tab][0], T7[tab][1], T7[tab][2], 'ex7-t']);
    var act = []; Object.keys(f7).forEach(function (g) { (f7[g] || []).forEach(function (o) { act.push({ label: o, drop: function () { tg(g, o); } }); }); });
    var shown = 0; srcs.forEach(function (s) { s[1].forEach(function (x) { if (base(x) && self.f7(x, s[0])) shown++; }); });
'''
EXF_RET = r'''
      f7Open: !!S.f7open, f7Exp: S.f7open ? 'true' : 'false', f7Cls: S.f7open || act.length ? 'on' : '', f7Toggle: function () { self.setState({ f7open: !S.f7open }); },
      f7Has: act.length > 0, f7N: act.length, f7Active: act, f7Clear: function () { self.setState({ f7: {} }); },
      f7Count: shown + (shown === 1 ? ' result' : ' results') + (tab === 'you' ? ' across all types' : ''),
      f7Note: T7[tab] ? 'Level, validation, access and language apply to every type. ' + T7[tab][1] + ' is only for ' + ({ courses: 'courses', certs: 'certifications', paths: 'career paths', programs: 'learning programs' })[tab] + '.' : 'Pick a type above for more filters, like course length or assessment format.',
      f7Groups: G7.map(function (g) { return { label: g[1].toUpperCase(), cls: g[3], opts: g[2].map(function (o) { var on = (f7[g[0]] || []).indexOf(o) > -1; return { label: o, n: cnt(g[0], o), on: on ? 'true' : 'false', cls: on ? 'on' : '', pick: function () { tg(g[0], o); } }; }) }; }),
'''

def wrapper_js(page, cfg):
    st = cfg.get('empty') is not None
    me = "this.props.viewer === 'learner'"
    if page == 'CertDetail': me += " || !!this.props.elig"
    if page == 'ProgramDetail': me += " || !!this.props.app"
    js = "  renderVals() {\n    var v = this._rv7(), st = this.props.state || '', me = %s;\n    v.st7Guest = !me; v.st7Learner = me;\n" % me
    if st:
        M = {'empty': cfg['empty'], 'noresults': cfg['no'], 'error': cfg['err']}
        js += "    var M = %s;\n" % json.dumps(M, ensure_ascii=False)
        js += ("    v.st7Loading = st === 'loading'; v.st7Msg = !!M[st]; var m = M[st];\n"
               "    v.st7IsErr = st === 'error'; v.st7IsEmpty = st === 'empty'; v.st7IsNo = st === 'noresults'; v.st7Cls = st === 'error' ? 'st7-err' : '';\n"
               "    if (m) { v.st7T = m[0]; v.st7D = m[1]; v.st7Cta = m[2]; v.st7Alt = m[3]; v.st7AltHref = m[4]; v.st7HasSug = !!m[5]; v.st7Sug = (m[5] || []).map(function (g) { return { t: g[0], h: g[1] }; }); }\n")
        if cfg.get('count'):
            js += "    if (st) v.%s = st === 'loading' ? 'Loading…' : (st === 'error' ? '' : '0 %s');\n" % (cfg['count'], cfg['name'])
        if cfg.get('none'):
            js += "    if (st) v.%s = false;\n" % cfg['none']
        if page == 'Explore':
            js += "    if (st === 'noresults') { v.q = 'astrophysics'; v.hasQ = false; }\n"
    js += "    return v;\n  }\n"
    return js

def patch(page, cfg):
    p = os.path.join(D, page + '.dc.html'); s = open(p).read()
    assert '_rv7' not in s, page + ' already patched'
    s, n = HDR_OLD.subn(HDR_NEW, s, count=1); assert n == 1, page + ' header'
    css = '' if '.sx-dlp{' in s else HDR_CSS
    if '.dlp-c{' not in s: css += DLP + '\n'
    if cfg.get('empty'):
        at = cfg['at']; assert s.count(at) == 1, (page, at)
        s = s.replace(at, (at + '\n' + block(cfg['name'])) if cfg.get('after') else (block(cfg['name']) + at), 1)
        css += ST_CSS
        if '.ds-chip{' not in s: css += '\n'.join(l.strip() for l in kit.KIT_CSS.split('\n') if re.match(r'\.ds-chip[.:{,\s]', l.strip())) + '\n'
    if page == 'Explore':
        s = s.replace('<div class="ex-body">', '<div class="ex-body">\n' + EXF, 1)
        css += EXF_CSS
        # filters apply to every list; the French course joins the course list
        a = "C('Leading Remote Teams', 'Leadership', 'Tom Hughes', 'Intermediate', 'silver', 84, '4.7', '460', 5, 600, 1200)"
        assert s.count(a) == 1; s = s.replace(a, a + ",\n      C('Introduction à l’analyse de données', 'Data', 'Élise Laurent', 'Beginner', 'gold', 90, '4.9', '410', 7, 600, 1200)")
        a = "var paths = this.P.filter(ok).slice(0, nP), courses = this.C.filter(ok).slice(0, S.tab === 'courses' ? 8 : nC), certs = this.CE.filter(ok).slice(0, nCe), progs = this.G.filter(ok).slice(0, nG);"
        assert s.count(a) == 1
        s = s.replace(a, "var paths = this.P.filter(function (x) { return ok(x) && self.f7(x, 'p'); }).slice(0, nP), courses = this.C.filter(function (x) { return ok(x) && self.f7(x, 'c'); }).slice(0, S.tab === 'courses' ? 8 : nC), certs = this.CE.filter(function (x) { return ok(x) && self.f7(x, 'ce'); }).slice(0, nCe), progs = this.G.filter(function (x) { return ok(x) && self.f7(x, 'g'); }).slice(0, nG);" + EXF_VALS)
        a = "      q: S.q, hasQ: !!S.q,"
        assert s.count(a) == 1; s = s.replace(a, EXF_RET + a)
        a = "this.state = { q: '', tab: 'you', topic: 'All', wish: {} };"
        assert s.count(a) == 1; s = s.replace(a, "var fv = props && props.view === 'filters';\n    this.state = { q: '', tab: fv ? 'courses' : 'you', topic: 'All', wish: {}, f7open: fv, f7: fv ? { lvl: ['Beginner'], acc: ['Own with Credits'] } : {} };")
        head = 'class Component extends DCLogic {'; i = s.index(head) + len(head); s = s[:i] + EXF_JS + s[i:]
    if page == 'ProgramDetail':
        a = '{"draft": ["blue",'
        assert s.count(a) == 1
        s = s.replace(a, '{"enrolled": ["green", "Enrolled", "You’re in the January cohort", "Week 5 of 12 · next live session Tue 18:00 GMT", "Continue learning", "#", "42%", "Open the cohort space", "cb"], '
                         '"done": ["green", "Completed", "You completed the program", "Completed 6 Apr 2027 · certificate in your Digital Backpack", "View certificate", "#", "", "Share your capstone", "ok"], "draft": ["blue",', 1)
        a = '{"draft": ["cb",'
        assert s.count(a) == 1
        s = s.replace(a, '{"enrolled": ["cb", "Enrolled · week 5 of 12", "Next live session Tue 18:00 GMT"], "done": ["ok", "Completed 6 Apr 2027", "Your certificate is in your Digital Backpack"], "draft": ["cb",', 1)
        s = s.replace('"options":["","draft","submitted","review","accepted","waitlisted","payment","full","closed"]', '"options":["","draft","submitted","review","accepted","waitlisted","payment","full","closed","enrolled","done"]', 1)
    # props + renderVals wrapper
    props = '"viewer":{"editor":"enum","options":["guest","learner"],"default":"guest"},'
    if cfg.get('empty'): props += '"state":{"editor":"enum","options":["","loading","empty","noresults","error"],"default":""},'
    if page == 'Explore': props += '"view":{"editor":"enum","options":["","filters"],"default":""},'
    s = s.replace('data-props=\'{', 'data-props=\'{' + props, 1)
    assert s.count('  renderVals() {') == 1, page
    s = s.replace('  renderVals() {', '  _rv7() {', 1)
    head = 'class Component extends DCLogic {'; i = s.index(head) + len(head)
    s = s[:i] + '\n' + wrapper_js(page, cfg) + s[i:]
    i = s.find('</style>'); s = s[:i] + css + s[i:]
    open(p, 'w').write(s); print('patched', page)

ONLY = sys.argv[2:]
for page, cfg in list(PAGES.items()) + [('CertDetail', {}), ('ProgramDetail', {})]:
    if not ONLY or page in ONLY: patch(page, cfg)
