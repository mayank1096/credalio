"""Landing batch 4 (client review, Career paths listing): search, real filters, sort, result count, pagination,
compare, richer cards (who it's for, starting point), "How career paths work" and browse by career destination.
Patches the live CareerPaths.dc.html in place (hero art, nav, footer, card design kept).
Prop view = '' | compare (two paths picked, comparison open). Usage: python3 cp4.py <canvas3/project>"""
import re, sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from kit import ck, ARROW, tip
D = sys.argv[1]; P = os.path.join(D, 'CareerPaths.dc.html'); s = open(P).read()
assert 'cp4-lay' not in s, 'already patched'
FILT = open('/tmp/claude-0/-home-user-credalio/5129fafc-9b09-5b10-ba39-f1d832483495/scratchpad/csfilt.css').read() if os.path.exists('/tmp/claude-0/-home-user-credalio/5129fafc-9b09-5b10-ba39-f1d832483495/scratchpad/csfilt.css') else ''
def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:90], s.count(a)); s = s.replace(a, b)
def svg(d, w=18, sw=2):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (w, w, sw, d)
SEARCH = svg('<circle cx="11" cy="11" r="7"></circle><path d="m20 20-3.5-3.5"></path>', 18, 2)
CHEV = svg('<path d="m6 9 6 6 6-6"></path>', 14, 2.2)
FILTI = svg('<path d="M4 6h16M7 12h10M10 18h4"></path>', 16, 2.2)
X = svg('<path d="M6 6l12 12M18 6 6 18"></path>', 13, 2.4)

# ---------------------------------------------------------------- hero: search
rep('<div class="cp-areas" role="group" aria-label="Area">',
    '<form class="ds-ask cp4-q" role="search" onSubmit="{{onSubmit}}">%s<label for="cp4-q" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Search career paths</label>'
    '<input id="cp4-q" type="search" placeholder="Search roles, skills or industries" value="{{q}}" onInput="{{onQ}}" autocomplete="off"><button class="ds-btn sm" type="submit"><span>Search</span><span class="ob-arrow">%s</span></button></form>\n'
    '<div class="cp-areas" role="group" aria-label="Area">' % (SEARCH, ARROW))

# ---------------------------------------------------------------- body: filters + results
def grp(key, label, multi=True, t=''):
    return ('<div class="cs-grp" role="%s" aria-label="%s"><span class="cs-gl">%s%s</span><div class="cs-cw"><sc-for list="{{f_%s}}" as="f" hint-placeholder-count="3">'
            '<button class="ds-chip sm {{f.cls}}" type="button" role="%s" aria-checked="{{f.on}}" onClick="{{f.pick}}">%s{{f.label}}<i>{{f.n}}</i></button></sc-for></div></div>') % (
        'group' if multi else 'radiogroup', label, label.upper(), tip(t) if t else '', key, 'checkbox' if multi else 'radio', ck(12))
ASIDE = ('<div class="cs-sheetbg {{sheetBg}}" onClick="{{closeSheet}}"></div>\n<aside class="cs-side {{sideCls}}" aria-label="Filters">'
         '<div class="cs-sh"><b>Filters</b><span style="display: flex; align-items: center; gap: 14px"><button class="ds-link {{clearCls}}" type="button" onClick="{{clearAll}}">Clear all</button>'
         '<button class="ds-link cs-sheetx" type="button" onClick="{{closeSheet}}" style="display: none; color: #0B1433">Done</button></span></div>'
         + grp('for', 'Designed for', True, 'Who the creator built it for. Not the same as entry level.')
         + grp('lvl', 'Entry level', True, 'How much you need to know on day one.')
         + grp('dur', 'Duration')
         + grp('start', 'Starting skills', True, 'Skills you already have.')
         + grp('skill', 'Skills you’ll build')
         + grp('tier', 'Validation tier')
         + grp('acc', 'Access', True, 'Use DLP from your plan course by course, buy courses with Credits, or own the whole path with a package.')
         + grp('by', 'Creator or institution', False)
         + '<button class="ds-btn cs-go2" type="button" onClick="{{closeSheet}}"><span>{{showLabel}}</span><span class="ob-arrow">%s</span></button></aside>') % ARROW

CARD_EXTRA = ('<span class="cp4-fit"><span><em>For</em>{{p.forTxt}}</span><span><em>Start with</em>{{p.start}}</span></span>\n')
COMPARE_BTN = '<button class="cp4-cmp {{p.cmpCls}}" type="button" aria-pressed="{{p.cmpOn}}" onClick="{{p.cmp}}"><span class="cp4-box">%s</span>Compare</button>' % ck(11)

RES_TOP = ('<div class="cs-bar"><div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap; min-width: 0">'
           '<button class="ds-chip cs-fbtn" type="button" onClick="{{openSheet}}">%sFilters<sc-if value="{{hasFilters}}" hint-placeholder-val="{{ false }}"><i>{{nFilters}}</i></sc-if></button>'
           '<span class="cs-count" aria-live="polite">{{countLabel}}</span></div>'
           '<span class="cs-sortw"><span>Sort</span><span class="cs-selw"><label for="cp4-sort" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Sort career paths</label>'
           '<select id="cp4-sort" class="cs-sel" onChange="{{onSort}}"><sc-for list="{{sorts}}" as="o" hint-placeholder-count="4"><option value="{{o.v}}" selected="{{o.sel}}">{{o.v}}</option></sc-for></select>%s</span></span></div>\n'
           '<sc-if value="{{hasFilters}}" hint-placeholder-val="{{ false }}"><div class="cs-chips" aria-label="Active filters"><sc-for list="{{active}}" as="a" hint-placeholder-count="2">'
           '<button class="ds-chip sm on" type="button" onClick="{{a.drop}}" aria-label="Remove filter {{a.label}}">{{a.label}}%s</button></sc-for></div></sc-if>\n') % (FILTI, CHEV, X)

CMP_TABLE = ('<sc-if value="{{cmpOpen}}" hint-placeholder-val="{{ false }}"><section class="cp4-ct" aria-labelledby="cp4-cth"><div class="cp4-cth"><h2 id="cp4-cth">Compare career paths</h2>'
             '<button class="ds-link" type="button" onClick="{{closeCmp}}">Close</button></div><div class="cp4-tw"><table><thead><tr><th scope="col"></th><sc-for list="{{cmpCols}}" as="c" hint-placeholder-count="2"><th scope="col">{{c.t}}</th></sc-for></tr></thead>'
             '<tbody><sc-for list="{{cmpRows}}" as="r" hint-placeholder-count="8"><tr><th scope="row">{{r.k}}</th><sc-for list="{{r.v}}" as="v" hint-placeholder-count="2"><td>{{v}}</td></sc-for></tr></sc-for></tbody></table></div>'
             '<p class="cp4-cn">Career paths build relevant skills. They don’t guarantee a job.</p></section></sc-if>\n')

PAGER = ('<nav class="cp4-pg" aria-label="Pagination"><span>{{pageLabel}}</span><div><button class="cp4-pn on" type="button" aria-current="page">1</button><button class="cp4-pn" type="button">2</button>'
         '<button class="cp4-pn" type="button">3</button><button class="ds-ghost sm" type="button">Next</button></div></nav>\n')

CMPBAR = ('<sc-if value="{{cmpBar}}" hint-placeholder-val="{{ false }}"><div class="cp4-bar" role="region" aria-label="Compare"><span><b>{{cmpN}}</b> {{cmpHint}}</span>'
          '<span class="cp4-ba"><button class="ds-link" type="button" onClick="{{clearCmp}}">Clear</button><button class="ds-btn sm {{cmpDis}}" type="button" onClick="{{openCmp}}"><span>Compare paths</span><span class="ob-arrow">%s</span></button></span></div></sc-if>\n') % ARROW

HOW = [('Choose a destination', 'Pick the role you want to work toward, at the level you’re starting from.'), ('Follow the route', 'Courses, practice and projects in a set order, with checkpoints along the way.'),
       ('Show what you can do', 'Build portfolio evidence and, if you want, take the professional certification.')]
DEST = [('Data Analyst', 'Data &amp; AI', 2), ('Product Designer', 'Design', 1), ('AI Engineer', 'Data &amp; AI', 1), ('Cybersecurity Analyst', 'Security', 1), ('Project Manager', 'Business', 1), ('Frontend Developer', 'Technology', 1)]
AFTER = ('<section class="cp4-how" aria-labelledby="cp4-hh"><h2 id="cp4-hh" class="cp4-h2">How career paths work</h2><p class="cp4-hs">A career path isn’t a bundle of courses. It’s an ordered route to a role, with projects and checkpoints that show what you can do.</p>'
         '<ol class="cp4-steps">%s</ol></section>\n'
         '<section class="cp4-dest" aria-labelledby="cp4-dh"><div class="cp4-dhw"><h2 id="cp4-dh" class="cp4-h2">Browse by career destination</h2><span class="cs-count">Only roles with a published path are shown</span></div>'
         '<div class="cp4-dg"><sc-for list="{{dests}}" as="d" hint-placeholder-count="6"><button class="cp4-d {{d.cls}}" type="button" onClick="{{d.pick}}"><b>{{d.t}}</b><span>{{d.area}} · {{d.n}}</span></button></sc-for></div></section>\n') % (
    ''.join('<li><span class="cp4-sn">%d</span><b>%s</b><span>%s</span></li>' % (i + 1, t, d) for i, (t, d) in enumerate(HOW)))

old_body = s[s.index('<div class="cp-body">'):s.index('<section class="cp-ai nova-card"')]
grid = old_body[old_body.index('<div class="cp-grid">'):]
grid = grid.replace('<sc-for list="{{paths}}" as="p" hint-placeholder-count="6">', '<sc-for list="{{paths}}" as="p" hint-placeholder-count="6"><div class="cp4-cw">')
grid = grid.replace('<span class="cp-foot">', CARD_EXTRA + '<span class="cp-foot">', 1)
grid = re.sub(r'(<span class="cp-foot">.*?</span></span>\n</a>)', r'\1' + COMPARE_BTN.replace('\\', '\\\\') + '</div>', grid, count=1, flags=re.S)
grid = grid.replace('No paths in this area yet. Nova can still build you a route.', 'No career paths match these filters. Try removing one, or ask Nova to build you a route.')
NEWBODY = ('<div class="cp-body">\n<div class="cp4-lay">\n' + ASIDE + '\n<div class="cp4-main">\n' + RES_TOP + CMP_TABLE + grid.rstrip()[:-6].rstrip() + '\n</div>\n' + PAGER + '</div>\n</div>\n' + CMPBAR + AFTER)
s = s.replace(old_body, NEWBODY, 1)

# ---------------------------------------------------------------- JS
PATHS = [
 dict(t='Data Analyst', area='Data & AI', entry='Beginner', lvl='Beginner → Job-ready', time='6–8 months', mo=7, courses=8, proj='4 projects', skills=['SQL', 'Excel', 'Power BI', 'Statistics'], ico=0, fr=['Complete beginners', 'Career switchers'], start='Basic spreadsheet use', starts=['Computer basics', 'Spreadsheets'], acc=['Subscription', 'Credits per course', 'Path package'], by='Amara Okafor'),
 dict(t='Product Designer', area='Design', entry='Beginner', lvl='Beginner → Job-ready', time='7–9 months', mo=8, courses=7, proj='4 projects', skills=['Figma', 'User research', 'Prototyping', 'Design systems'], ico=1, fr=['Career switchers'], start='No design tools needed', starts=['Computer basics'], acc=['Subscription', 'Credits per course', 'Path package'], by='Lena Fischer'),
 dict(t='AI Engineer', area='Data & AI', entry='Intermediate', lvl='Intermediate → Job-ready', time='8–10 months', mo=9, courses=8, proj='4 projects', skills=['Python', 'Machine learning', 'LLM apps', 'Evaluation'], ico=2, fr=['Upskilling professionals'], start='Some Python', starts=['Some coding'], acc=['Subscription', 'Path package'], by='Northgate University'),
 dict(t='Cybersecurity Analyst', area='Security', entry='Beginner', lvl='Beginner → Job-ready', time='8–10 months', mo=9, courses=7, proj='3 simulations', skills=['Networking', 'Linux', 'SIEM', 'Incident response'], ico=3, fr=['Complete beginners', 'Career switchers'], start='Basic computer use', starts=['Computer basics'], acc=['Subscription', 'Credits per course'], by='Westbridge Institute'),
 dict(t='Project Manager', area='Business', entry='Beginner', lvl='Beginner → Job-ready', time='5–7 months', mo=6, courses=6, proj='3 projects', skills=['Planning', 'Agile', 'Risk', 'Stakeholders'], ico=4, fr=['Upskilling professionals', 'Career switchers'], start='Some workplace experience', starts=['Workplace experience'], acc=['Subscription', 'Credits per course', 'Path package'], by='Westbridge Institute'),
 dict(t='Frontend Developer', area='Technology', entry='Beginner', lvl='Beginner → Job-ready', time='8–10 months', mo=9, courses=8, proj='4 projects', skills=['HTML & CSS', 'JavaScript', 'React', 'Testing'], ico=5, fr=['Complete beginners', 'Career switchers'], start='Basic computer use', starts=['Computer basics'], acc=['Subscription', 'Credits per course'], by='Mia Lopez')]
G = [('for', ['Complete beginners', 'Career switchers', 'Upskilling professionals'], 'fr'), ('lvl', ['Beginner', 'Intermediate', 'Advanced'], 'entry'), ('dur', ['Under 6 months', '6–8 months', 'Over 8 months'], 'dur'),
     ('start', ['Computer basics', 'Spreadsheets', 'Some coding', 'Workplace experience'], 'starts'), ('skill', ['SQL', 'Python', 'Figma', 'Networking', 'Agile', 'JavaScript'], 'skills'),
     ('tier', ['Gold', 'Silver', 'Bronze'], 'tier'), ('acc', ['Subscription', 'Credits per course', 'Path package'], 'acc'), ('by', ['Anyone', 'Independent creators', 'Northgate University', 'Westbridge Institute'], 'by')]
JS = r'''  constructor(props) {
    super(props);
    var cmp = props && props.view === 'compare';
    this.state = { area: 'All', q: '', f: {}, by: 'Anyone', sort: 'Recommended', sheet: false, cmp: cmp ? ['Data Analyst', 'Project Manager'] : [], cmpOpen: cmp };
    this.P = PATHS_;
    this.G = GROUPS_;
  }
  renderVals() {
    var self = this, S = this.state, P = this.P;
    var areas = ['All', 'Data & AI', 'Design', 'Technology', 'Business', 'Security'];
    var TIERN = { gold: 'Gold', silver: 'Silver', bronze: 'Bronze' };
    var val = function (p, k) {
      if (k === 'fr') return p.fr; if (k === 'entry') return [p.entry]; if (k === 'starts') return p.starts; if (k === 'skills') return p.skills; if (k === 'acc') return p.acc;
      if (k === 'tier') return [TIERN[TP_[p.t][2]]]; if (k === 'dur') return [p.mo < 6 ? 'Under 6 months' : (p.mo <= 8 ? '6–8 months' : 'Over 8 months')];
      if (k === 'by') return [p.by === 'Northgate University' || p.by === 'Westbridge Institute' ? p.by : 'Independent creators'];
      return [];
    };
    var match = function (p, skip) {
      if (S.area !== 'All' && p.area !== S.area) return false;
      var q = S.q.trim().toLowerCase(); if (q && (p.t + ' ' + p.skills.join(' ') + ' ' + p.area).toLowerCase().indexOf(q) < 0) return false;
      for (var i = 0; i < self.G.length; i++) { var g = self.G[i], key = g[0]; if (key === skip) continue;
        if (key === 'by') { if (S.by !== 'Anyone' && val(p, 'by')[0] !== S.by) return false; continue; }
        var on = S.f[key] || []; if (on.length && !on.some(function (o) { return val(p, g[2]).indexOf(o) > -1; })) return false; }
      return true;
    };
    var list = P.filter(function (p) { return match(p); });
    var order = { 'Shortest first': function (a, b) { return a.mo - b.mo; }, 'Lowest DLP': function (a, b) { return parseInt(TP_[a.t][4].replace(',', '')) - parseInt(TP_[b.t][4].replace(',', '')); }, 'Highest rated': function (a, b) { return parseFloat(TP_[b.t][0]) - parseFloat(TP_[a.t][0]); } };
    if (order[S.sort]) list = list.slice().sort(order[S.sort]);
    var toggle = function (key, o) { var f = Object.assign({}, S.f), l = (f[key] || []).slice(), i = l.indexOf(o); if (i > -1) l.splice(i, 1); else l.push(o); f[key] = l; self.setState({ f: f }); };
    var v = {};
    this.G.forEach(function (g) {
      var key = g[0];
      v['f_' + key] = g[1].map(function (o) {
        var on = key === 'by' ? S.by === o : (S.f[key] || []).indexOf(o) > -1;
        var n = key === 'by' && o === 'Anyone' ? '' : P.filter(function (p) { return match(p, key) && (key === 'by' ? val(p, 'by')[0] === o : val(p, g[2]).indexOf(o) > -1); }).length;
        return { label: o, n: n, on: on ? 'true' : 'false', cls: on ? 'on' : '', pick: function () { if (key === 'by') self.setState({ by: o }); else toggle(key, o); } };
      });
    });
    var active = [];
    Object.keys(S.f).forEach(function (k) { (S.f[k] || []).forEach(function (o) { active.push({ label: o, drop: function () { toggle(k, o); } }); }); });
    if (S.by !== 'Anyone') active.push({ label: S.by, drop: function () { self.setState({ by: 'Anyone' }); } });
    var nF = active.length;
    var cmp = S.cmp;
    var cols = P.filter(function (p) { return cmp.indexOf(p.t) > -1; });
    var row = function (k, fn) { return { k: k, v: cols.map(fn) }; };
    return Object.assign(v, {
      areas: areas.map(function (a) { var on = S.area === a; return { label: a === 'All' ? 'All paths' : a, n: a === 'All' ? P.length : P.filter(function (p) { return p.area === a; }).length, on: on ? 'true' : 'false', cls: on ? 'on' : '', pick: function () { self.setState({ area: a }); } }; }),
      q: S.q, onQ: function (e) { self.setState({ q: e.target.value }); }, onSubmit: function (e) { e.preventDefault(); },
      paths: list.map(function (p, k) {
        var feat = S.area === 'All' && !nF && !S.q && S.sort === 'Recommended' && k === 0, t = TP_[p.t], on = cmp.indexOf(p.t) > -1;
        var o = { rating: t[0], reviews: t[1], tierLabel: TIER_[t[2]][0], tierDot: TIER_[t[2]][1], cei: t[3], dlp: t[4], cr: t[5], tagA: feat ? 'glass' : 'blue', tagB: feat ? 'glass' : 'line',
          t: p.t, lvl: p.lvl, time: p.time, courses: p.courses, proj: p.proj, skills: p.skills.slice(0, 3), feat: feat, cls: feat ? 'cp-feat aur' : '', tag: feat ? 'glass' : '', icoBg: '#EAF0FF', icoFg: '#1652F0',
          forTxt: p.fr.join(', '), start: p.start, aria: p.courses + ' courses, ' + p.proj + ', a professional certification and a portfolio',
          cmpOn: on ? 'true' : 'false', cmpCls: on ? 'on' : '', cmp: function () { var l = cmp.slice(), i = l.indexOf(p.t); if (i > -1) l.splice(i, 1); else if (l.length < 3) l.push(p.t); self.setState({ cmp: l, cmpOpen: S.cmpOpen && l.length > 1 }); } };
        for (var i = 0; i < 6; i++) o['i' + i] = p.ico === i ? 'inline' : 'none';
        return o;
      }),
      none: list.length === 0,
      countLabel: list.length + (list.length === 1 ? ' career path' : ' career paths'),
      pageLabel: list.length ? 'Showing 1–' + list.length + ' of ' + (list.length === P.length ? 18 : list.length) + ' career paths' : '',
      sorts: ['Recommended', 'Shortest first', 'Lowest DLP', 'Highest rated'].map(function (o) { return { v: o, sel: S.sort === o }; }),
      onSort: function (e) { self.setState({ sort: e.target.value }); },
      hasFilters: nF > 0, nFilters: nF, active: active, clearCls: nF ? '' : 'off',
      clearAll: function () { self.setState({ f: {}, by: 'Anyone' }); },
      sideCls: S.sheet ? 'cs-side-open' : '', sheetBg: S.sheet ? 'cs-sheetbg-on' : '',
      openSheet: function () { self.setState({ sheet: true }); }, closeSheet: function () { self.setState({ sheet: false }); },
      showLabel: 'Show ' + list.length + (list.length === 1 ? ' path' : ' paths'),
      cmpBar: cmp.length > 0 && !S.cmpOpen, cmpN: cmp.length + ' of 3', cmpHint: cmp.length < 2 ? 'selected · pick one more to compare' : 'selected', cmpDis: cmp.length < 2 ? 'cd-dis' : '',
      clearCmp: function () { self.setState({ cmp: [], cmpOpen: false }); }, openCmp: function () { if (cmp.length > 1) self.setState({ cmpOpen: true }); }, closeCmp: function () { self.setState({ cmpOpen: false }); },
      cmpOpen: S.cmpOpen && cols.length > 1, cmpCols: cols.map(function (p) { return { t: p.t }; }),
      cmpRows: [row('Time', function (p) { return p.time; }), row('Entry level', function (p) { return p.entry; }), row('Start with', function (p) { return p.start; }), row('Designed for', function (p) { return p.fr.join(', '); }),
        row('Route', function (p) { return p.courses + ' courses · ' + p.proj; }), row('Learning', function (p) { return TP_[p.t][4] + ' DLP'; }), row('Own the path', function (p) { return p.acc.indexOf('Path package') > -1 ? TP_[p.t][5] + ' Credits' : 'Not offered'; }),
        row('Validation', function (p) { return TIER_[TP_[p.t][2]][0] + ' · CEI ' + TP_[p.t][3]; }), row('Rating', function (p) { return '★ ' + TP_[p.t][0] + ' (' + TP_[p.t][1] + ')'; })],
      dests: DESTS_.map(function (d) { var on = S.q === d[0]; return { t: d[0], area: d[1], n: d[2] + (d[2] === 1 ? ' path' : ' paths'), cls: on ? 'on' : '', pick: function () { self.setState({ q: d[0], area: 'All' }); } }; })
    });
  }
}
'''.replace('PATHS_', json.dumps(PATHS, ensure_ascii=False)).replace('GROUPS_', json.dumps(G, ensure_ascii=False)).replace('DESTS_', json.dumps([(t, a.replace('&amp;', '&'), n) for t, a, n in DEST], ensure_ascii=False))
i = s.index('  constructor(props) {'); j = s.index('</script>', i)
s = s[:i] + JS + s[j:]
rep('"$preview":', '"view":{"editor":"enum","options":["","compare"],"default":""},"$preview":')

KITX = '\n'.join(l.strip() for l in __import__('kit').KIT_CSS.split('\n') if re.match(r'\.(tip|ds-ghost)[.:{,\s-]', l.strip()))
CSS = FILT + KITX + r'''
@media (max-width: 760px){.tip-b{display:none;width:min(250px,calc(100vw - 48px))}.tip:hover .tip-b,.tip:focus .tip-b{display:block}}
.cp4-d b{font-size:15.5px;font-weight:600;color:#0B1433}
.cp4-d span{font-size:13px;color:#5B6582}
.cp4-q{width:min(640px,100%);margin-top:6px}
.cp4-lay{display:grid;grid-template-columns:250px minmax(0,1fr);gap:40px;align-items:start}
.cp4-main{min-width:0;display:flex;flex-direction:column;gap:20px}
.cp4-main .cp-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
.cp4-main .cs-bar{margin-bottom:0}
.cp4-cw{position:relative;display:flex;flex-direction:column}
.cp4-cw > .cp-card{flex:1}
.cp4-fit{display:flex;flex-direction:column;gap:4px;font-size:13px;color:#3A4566}
.cp4-fit em{font-style:normal;color:#8A93AD;margin-right:6px}
.cp-feat .cp4-fit{color:rgba(255,255,255,.85)}
.cp-feat .cp4-fit em{color:rgba(255,255,255,.55)}
.cp4-cmp{position:absolute;top:22px;right:22px;z-index:2;display:inline-flex;align-items:center;gap:7px;height:32px;padding:0 12px 0 8px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:inherit;font-size:12.5px;font-weight:500;color:#3A4566;cursor:pointer}
.cp4-cmp:hover{border-color:#1652F0}
.cp4-box{width:16px;height:16px;border-radius:5px;border:1.5px solid #CBD3E6;display:flex;align-items:center;justify-content:center;color:#FFFFFF;box-sizing:border-box}
.cp4-box .ck{display:none}
.cp4-cmp.on{border-color:#1652F0;background:#EAF0FF;color:#0E3BB8}
.cp4-cmp.on .cp4-box{background:#1652F0;border-color:#1652F0}
.cp4-cmp.on .cp4-box .ck{display:block}
.cp4-cw:has(.cp-feat) .cp4-cmp{background:rgba(255,255,255,.14);border-color:rgba(255,255,255,.3);color:#FFFFFF}
.cp4-cw .cp-top .ds-tag{margin-right:110px}
.cp4-pg{display:flex;align-items:center;justify-content:space-between;gap:16px;padding-top:4px;font-size:14px;color:#5B6582}
.cp4-pg > div{display:flex;align-items:center;gap:6px}
.cp4-pn{width:40px;height:40px;border-radius:12px;border:1.5px solid #E6EAF3;background:#FFFFFF;font-family:inherit;font-size:14px;font-weight:500;color:#3A4566;cursor:pointer}
.cp4-pn.on{background:#0B1433;border-color:#0B1433;color:#FFFFFF}
.cp4-pg .ds-ghost{height:40px}
.cp4-bar{position:sticky;bottom:20px;z-index:20;align-self:center;display:flex;align-items:center;gap:24px;padding:10px 10px 10px 22px;border-radius:999px;background:#0B1433;color:#FFFFFF;font-size:14px;box-shadow:0 24px 50px -20px rgba(11,20,51,.6)}
.cp4-bar b{font-weight:600}
.cp4-ba{display:flex;align-items:center;gap:14px}
.cp4-ba .ds-link{color:rgba(255,255,255,.75)}
.ds-btn.cd-dis{background:#3A4566;color:#B5BDD3;box-shadow:none;pointer-events:none}
.cp4-ct{border:1.5px solid #DCE5FB;border-radius:22px;padding:22px 24px;background:linear-gradient(180deg,#F5F8FF,#FFFFFF)}
.cp4-cth{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.cp4-cth h2{margin:0;font-size:20px;font-weight:600;letter-spacing:-.3px}
.cp4-tw{overflow-x:auto}
.cp4-ct table{width:100%;border-collapse:collapse;font-size:14px}
.cp4-ct th,.cp4-ct td{text-align:left;padding:12px 14px;border-top:1px solid #E6EAF3;vertical-align:top}
.cp4-ct thead th{border-top:none;font-size:16px;font-weight:600;color:#0B1433}
.cp4-ct tbody th{width:150px;font-weight:500;color:#8A93AD;font-size:13px}
.cp4-ct td{color:#0B1433}
.cp4-cn{margin:12px 0 0;font-size:12.5px;color:#8A93AD}
.cp4-h2{margin:0;font-size:28px;line-height:1.15;font-weight:600;letter-spacing:-.7px;color:#0B1433}
.cp4-how{display:flex;flex-direction:column;gap:10px;padding-top:24px}
.cp4-hs{margin:0;max-width:640px;font-size:16px;line-height:1.55;color:#4A5578}
.cp4-steps{margin:14px 0 0;padding:0;list-style:none;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;position:relative}
.cp4-steps li{display:flex;flex-direction:column;gap:6px;padding:22px;border-radius:20px;border:1.5px solid #E6EAF3;background:#FFFFFF}
.cp4-sn{width:34px;height:34px;border-radius:50%;background:#1652F0;color:#FFFFFF;font-size:14px;font-weight:600;display:flex;align-items:center;justify-content:center;margin-bottom:8px}
.cp4-steps b{font-size:17px;font-weight:600}
.cp4-steps li > span:last-child{font-size:14px;line-height:1.5;color:#5B6582}
.cp4-dest{display:flex;flex-direction:column;gap:16px}
.cp4-dhw{display:flex;align-items:baseline;justify-content:space-between;gap:16px;flex-wrap:wrap}
.cp4-dg{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:12px}
.cp4-d{display:flex;flex-direction:column;align-items:flex-start;gap:4px;padding:18px;border-radius:18px;border:1.5px solid #E6EAF3;background:#FFFFFF;font-family:inherit;text-align:left;cursor:pointer;transition:border-color .2s ease,transform .3s ease}
.cp4-d:hover{border-color:#9DB8F7;transform:translateY(-2px)}
.cp4-d.on{border-color:#1652F0;background:#EAF0FF}
.cp4-d b{font-size:15px;font-weight:600;color:#0B1433}
.cp4-d span{font-size:12.5px;color:#5B6582}
@media (max-width: 1180px){.cp4-dg{grid-template-columns:repeat(3,minmax(0,1fr))}.cp4-main .cp-grid{grid-template-columns:minmax(0,1fr)}}
@media (max-width: 960px){.cp4-lay{grid-template-columns:minmax(0,1fr)}.cp4-main .cp-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width: 760px){
.cp4-q{margin-top:2px}
.cp4-q .ds-btn span:first-child{display:none}
.cp4-main .cp-grid{grid-template-columns:minmax(0,1fr)}
.cp4-cmp{top:18px;right:18px}
.cp4-pg{flex-direction:column;align-items:stretch;gap:12px;text-align:center}
.cp4-pg > div{justify-content:center}
.cp4-bar{bottom:12px;gap:12px;padding:8px 8px 8px 16px;font-size:13px}
.cp4-ba .ds-link{display:none}
.cp4-ct{padding:18px 14px;margin:0 -4px}
.cp4-ct tbody th{width:96px}
.cp4-h2{font-size:22px;letter-spacing:-.4px}
.cp4-hs{font-size:15px}
.cp4-steps{grid-template-columns:minmax(0,1fr);gap:10px}
.cp4-steps li{display:grid;grid-template-columns:34px minmax(0,1fr);column-gap:14px;padding:16px}
.cp4-sn{grid-row:span 2;margin:0}
.cp4-dg{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.cp4-d{padding:14px}
}
'''
i = s.find('</style>'); s = s[:i] + CSS + s[i:]
open(P, 'w').write(s); print('patched CareerPaths')
