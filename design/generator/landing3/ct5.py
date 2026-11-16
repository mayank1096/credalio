"""Landing batch 5 (client review, Certifications listing): real filters, sort, result count, compare,
pagination, cards with entry requirements and what you'll demonstrate, and "How professional certification works".
Patches the live Certifications.dc.html in place (hero, card design and Nova band kept).
Prop view = '' | compare. Usage: python3 ct5.py <canvas3/project>"""
import re, sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import kit
from kit import ck, ARROW, tip
D = sys.argv[1]; P = os.path.join(D, 'Certifications.dc.html'); s = open(P).read()
assert 'ct5-' not in s, 'already patched'
FILT = open(os.path.join(HERE, 'csfilt.css')).read()
def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:90], s.count(a)); s = s.replace(a, b)
def svg(d, w=18, sw=2):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (w, w, sw, d)
CHEV = svg('<path d="m6 9 6 6 6-6"></path>', 14, 2.2)
FILTI = svg('<path d="M4 6h16M7 12h10M10 18h4"></path>', 16, 2.2)
X = svg('<path d="M6 6l12 12M18 6 6 18"></path>', 13, 2.4)

def grp(key, label, multi=True, t=''):
    return ('<div class="cs-grp" role="%s" aria-label="%s"><span class="cs-gl">%s%s</span><div class="cs-cw"><sc-for list="{{f_%s}}" as="f" hint-placeholder-count="3">'
            '<button class="ds-chip sm {{f.cls}}" type="button" role="%s" aria-checked="{{f.on}}" onClick="{{f.pick}}">%s{{f.label}}<i>{{f.n}}</i></button></sc-for></div></div>') % (
        'group' if multi else 'radiogroup', label, label.upper(), tip(t) if t else '', key, 'checkbox' if multi else 'radio', ck(12))
ASIDE = ('<div class="cs-sheetbg {{sheetBg}}" onClick="{{closeSheet}}"></div>\n<aside class="cs-side {{sideCls}}" aria-label="Filters">'
         '<div class="cs-sh"><b>Filters</b><span style="display: flex; align-items: center; gap: 14px"><button class="ds-link {{clearCls}}" type="button" onClick="{{clearAll}}">Clear all</button>'
         '<button class="ds-link cs-sheetx" type="button" onClick="{{closeSheet}}" style="display: none; color: #0B1433">Done</button></span></div>'
         + grp('lvl', 'Professional level', True, 'Foundation is for newcomers to the field. Professional and above expect some experience.')
         + grp('exp', 'Experience needed', True, 'Whether the issuer requires work experience before you register, or only recommends it.')
         + grp('fmt', 'Assessment format')
         + grp('dur', 'Preparation time')
         + grp('iss', 'Issuer')
         + grp('tier', 'Validation tier')
         + grp('fee', 'Assessment fee', True, 'The fee is in Credits and separate from preparation learning, which uses DLP.')
         + '<button class="ds-btn cs-go2" type="button" onClick="{{closeSheet}}"><span>{{showLabel}}</span><span class="ob-arrow">%s</span></button></aside>') % ARROW
TOP = ('<div class="cs-bar"><div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap; min-width: 0">'
       '<button class="ds-chip cs-fbtn" type="button" onClick="{{openSheet}}">%sFilters<sc-if value="{{hasFilters}}" hint-placeholder-val="{{ false }}"><i>{{nFilters}}</i></sc-if></button>'
       '<span class="cs-count" aria-live="polite">{{countLabel}}</span></div>'
       '<span class="cs-sortw"><span>Sort</span><span class="cs-selw"><label for="ct5-sort" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Sort certifications</label>'
       '<select id="ct5-sort" class="cs-sel" onChange="{{onSort}}"><sc-for list="{{sorts}}" as="o" hint-placeholder-count="4"><option value="{{o.v}}" selected="{{o.sel}}">{{o.v}}</option></sc-for></select>%s</span></span></div>\n'
       '<sc-if value="{{hasFilters}}" hint-placeholder-val="{{ false }}"><div class="cs-chips" aria-label="Active filters"><sc-for list="{{active}}" as="a" hint-placeholder-count="2">'
       '<button class="ds-chip sm on" type="button" onClick="{{a.drop}}" aria-label="Remove filter {{a.label}}">{{a.label}}%s</button></sc-for></div></sc-if>\n'
       '<sc-if value="{{cmpOpen}}" hint-placeholder-val="{{ false }}"><section class="cp4-ct" aria-labelledby="ct5-cth"><div class="cp4-cth"><h2 id="ct5-cth">Compare certifications</h2>'
       '<button class="ds-link" type="button" onClick="{{closeCmp}}">Close</button></div><div class="cp4-tw"><table><thead><tr><th scope="col"></th><sc-for list="{{cmpCols}}" as="c" hint-placeholder-count="2"><th scope="col">{{c.t}}</th></sc-for></tr></thead>'
       '<tbody><sc-for list="{{cmpRows}}" as="r" hint-placeholder-count="8"><tr><th scope="row">{{r.k}}</th><sc-for list="{{r.v}}" as="v" hint-placeholder-count="2"><td>{{v}}</td></sc-for></tr></sc-for></tbody></table></div>'
       '<p class="cp4-cn">Fees and requirements come from each issuer’s published rules.</p></section></sc-if>\n') % (FILTI, CHEV, X)
PAGER = ('<nav class="cp4-pg" aria-label="Pagination"><span>{{pageLabel}}</span><div><button class="cp4-pn on" type="button" aria-current="page">1</button><button class="cp4-pn" type="button">2</button>'
         '<button class="cp4-pn" type="button">3</button><button class="cp4-pn" type="button">4</button><button class="ds-ghost sm" type="button">Next</button></div></nav>\n')
CMPBAR = ('<sc-if value="{{cmpBar}}" hint-placeholder-val="{{ false }}"><div class="cp4-bar" role="region" aria-label="Compare"><span><b>{{cmpN}}</b> {{cmpHint}}</span>'
          '<span class="cp4-ba"><button class="ds-link" type="button" onClick="{{clearCmp}}">Clear</button><button class="ds-btn sm {{cmpDis}}" type="button" onClick="{{openCmp}}"><span>Compare</span><span class="ob-arrow">%s</span></button></span></div></sc-if>\n') % ARROW
HOW = [('Explore', 'Find a certification that matches the role or skill you want to prove.'), ('Check eligibility', 'Three questions tell you if you can register, or what to do first.'),
       ('Demonstrate', 'Prepare if you need to, then pass the exam, practical work and review.'), ('Get certified', 'Your credential goes to your Digital Backpack with a link anyone can check.')]
AFTER = ('<section class="cp4-how" aria-labelledby="ct5-hh"><h2 id="ct5-hh" class="cp4-h2">How professional certification works</h2>'
         '<p class="cp4-hs">You earn a certification by showing you meet a published standard, not by finishing courses. Each one is issued by the creator or institution named on it.</p>'
         '<ol class="cp4-steps ct5-steps">%s</ol></section>\n') % ''.join('<li><span class="cp4-sn">%d</span><b>%s</b><span>%s</span></li>' % (i + 1, t, d) for i, (t, d) in enumerate(HOW))

# hero chips: fields stay; body becomes filters + results
body = s[s.index('<div class="ct-body">'):s.index('<section class="ct-ai nova-card"')]
grid = body[body.index('<div class="ct-grid">'):]
bar = body[body.index('<div class="ct-bar">'):body.index('<div class="ct-grid">')]
grid = grid.replace('<sc-for list="{{certs}}" as="c" hint-placeholder-count="6">', '<sc-for list="{{certs}}" as="c" hint-placeholder-count="6"><div class="cp4-cw">')
grid = grid.replace('<span class="mx">', '<span class="ct5-dem"><em>You’ll demonstrate</em>{{c.dem}}</span>\n<span class="ct5-dem"><em>Entry</em>{{c.entry}}<span class="ds-tag {{c.expCls}}">{{c.expTag}}</span></span>\n<span class="mx">', 1)
grid = re.sub(r'(<span class="ds-link">View →</span></span>\n</div>\n</a>)', r'\1<button class="cp4-cmp {{c.cmpCls}}" type="button" aria-pressed="{{c.cmpOn}}" onClick="{{c.cmp}}"><span class="cp4-box">' + ck(11).replace('\\', '\\\\') + '</span>Compare</button></div>', grid, count=1)
grid = grid.replace('No certifications match yet. Try another field, or ask Nova.', 'No certifications match these filters. Try removing one, or ask Nova what to prepare first.')
grid = grid.rstrip()
assert grid.endswith('</div>'); grid = grid[:-6].rstrip()
NEW = ('<div class="ct-body">\n' + bar + '<div class="cp4-lay">\n' + ASIDE + '\n<div class="cp4-main">\n' + TOP + grid + '\n</div>\n' + PAGER + '</div>\n</div>\n' + CMPBAR + AFTER)
s = s.replace(body, NEW, 1)

# ---------------------------------------------------------------- JS
X5 = {'Data Analysis': ('Recommended', 'Data Foundations, or an equivalent', 'Clean data, write SQL, analyse and present findings', 'Exam + case study', 3.5),
      'Product Design': ('Recommended', 'UX and Product Design Foundations, or a portfolio', 'Research, design and test a product feature', 'Portfolio + practical', 4.5),
      'Security Operations': ('Required', '1 year in IT or networking', 'Detect, triage and respond to live incidents', 'Practical lab + exam', 5),
      'Project Management': ('None', 'Open to anyone', 'Plan, run and close a project with risks managed', 'Exam + practical', 3),
      'Applied AI Practitioner': ('Recommended', 'Prompt Engineering for Professionals', 'Build and evaluate an AI workflow', 'Practical + oral review', 2.5),
      'Financial Analysis': ('Required', '6 months in finance or accounting', 'Build a model, value a business and report on it', 'Exam + practical', 3.5)}
G = [('lvl', ['Foundation', 'Professional', 'Advanced'], 'level'), ('exp', ['None', 'Recommended', 'Required'], 'exp'), ('fmt', ['Exam', 'Practical', 'Portfolio'], 'fmt'),
     ('dur', ['Up to 3 months', '3–4 months', 'Over 4 months'], 'dur'), ('iss', ['Institutions', 'Independent creators'], 'type'), ('tier', ['Gold', 'Silver', 'In review'], 'tier'),
     ('fee', ['Under 150 Credits', '150–200 Credits', 'Over 200 Credits'], 'fee')]
JS = r'''  renderVals() {
    var self = this, S = this.state, q = S.q.trim().toLowerCase(), X5 = X5_;
    var TN = { gold: 'Gold', silver: 'Silver', bronze: 'Bronze', rev: 'In review' };
    var val = function (c, k) {
      var x = X5[c.short], t = TC_[c.short], fee = parseInt(t[4]);
      if (k === 'level') return [c.level]; if (k === 'exp') return [x[0]]; if (k === 'type') return [c.type === 'Institutions' ? 'Institutions' : 'Independent creators'];
      if (k === 'fmt') return ['Exam', 'Practical', 'Portfolio'].filter(function (f) { return x[3].toLowerCase().indexOf(f.toLowerCase()) > -1 || (f === 'Practical' && /case|lab/.test(x[3])); });
      if (k === 'dur') return [x[4] <= 3 ? 'Up to 3 months' : (x[4] <= 4 ? '3–4 months' : 'Over 4 months')]; if (k === 'tier') return [TN[t[2]]];
      if (k === 'fee') return [fee < 150 ? 'Under 150 Credits' : (fee <= 200 ? '150–200 Credits' : 'Over 200 Credits')];
      return [];
    };
    var match = function (c, skip) {
      if (S.field !== 'All' && c.field !== S.field) return false;
      if (q && (c.t + ' ' + c.skills.join(' ') + ' ' + c.issuer).toLowerCase().indexOf(q) < 0) return false;
      for (var i = 0; i < self.G.length; i++) { var g = self.G[i]; if (g[0] === skip) continue; var on = S.f[g[0]] || []; if (on.length && !on.some(function (o) { return val(c, g[2]).indexOf(o) > -1; })) return false; }
      return true;
    };
    var list = this.L.filter(function (c) { return match(c); });
    var srt = { 'Shortest preparation': function (a, b) { return X5[a.short][4] - X5[b.short][4]; }, 'Lowest fee': function (a, b) { return parseInt(TC_[a.short][4]) - parseInt(TC_[b.short][4]); },
      'Highest rated': function (a, b) { return parseFloat(TC_[b.short][0]) - parseFloat(TC_[a.short][0]); } };
    if (srt[S.sort]) list = list.slice().sort(srt[S.sort]);
    var toggle = function (key, o) { var f = Object.assign({}, S.f), l = (f[key] || []).slice(), i = l.indexOf(o); if (i > -1) l.splice(i, 1); else l.push(o); f[key] = l; self.setState({ f: f }); };
    var v = {};
    this.G.forEach(function (g) { var key = g[0]; v['f_' + key] = g[1].map(function (o) { var on = (S.f[key] || []).indexOf(o) > -1; return { label: o, n: self.L.filter(function (c) { return match(c, key) && val(c, g[2]).indexOf(o) > -1; }).length, on: on ? 'true' : 'false', cls: on ? 'on' : '', pick: function () { toggle(key, o); } }; }); });
    var active = []; Object.keys(S.f).forEach(function (k) { (S.f[k] || []).forEach(function (o) { active.push({ label: o, drop: function () { toggle(k, o); } }); }); });
    var cmp = S.cmp, cols = this.L.filter(function (c) { return cmp.indexOf(c.short) > -1; });
    var row = function (k, fn) { return { k: k, v: cols.map(fn) }; };
    var EXPC = { None: 'green', Recommended: 'line', Required: 'amber' };
    return Object.assign(v, {
      q: S.q, onQ: function (e) { self.setState({ q: e.target.value }); }, onSubmit: function (e) { e.preventDefault(); },
      fields: ['All', 'Data', 'Design', 'Cybersecurity', 'Business', 'AI', 'Finance'].map(function (f) { var on = S.field === f; return { label: f === 'All' ? 'All fields' : f, on: on ? 'true' : 'false', cls: on ? 'on' : '', pick: function () { self.setState({ field: f }); } }; }),
      certs: list.map(function (c) { var t = TC_[c.short], x = X5[c.short], on = cmp.indexOf(c.short) > -1; return { rating: t[0], reviews: t[1], tierLabel: TIER_[t[2]][0], tierDot: TIER_[t[2]][1], cei: t[3], fee: t[4], tagA: c.ok ? 'blue' : 'line', tagB: 'line',
        short: c.short, issuer: c.issuer, level: c.level, time: c.time, format: c.format, pre: c.pre, ok: c.ok, rev: !c.ok, dem: x[2], entry: x[1], expTag: x[0] === 'None' ? 'No experience needed' : 'Experience ' + x[0].toLowerCase(), expCls: EXPC[x[0]],
        cmpOn: on ? 'true' : 'false', cmpCls: on ? 'on' : '', cmp: function () { var l = cmp.slice(), i = l.indexOf(c.short); if (i > -1) l.splice(i, 1); else if (l.length < 3) l.push(c.short); self.setState({ cmp: l, cmpOpen: S.cmpOpen && l.length > 1 }); } }; }),
      none: list.length === 0,
      countLabel: list.length + (list.length === 1 ? ' certification' : ' certifications'), pageLabel: list.length ? 'Showing 1–' + list.length + ' of ' + (list.length === self.L.length ? 24 : list.length) + ' certifications' : '',
      sorts: ['Recommended', 'Shortest preparation', 'Lowest fee', 'Highest rated'].map(function (o) { return { v: o, sel: S.sort === o }; }), onSort: function (e) { self.setState({ sort: e.target.value }); },
      hasFilters: active.length > 0, nFilters: active.length, active: active, clearCls: active.length ? '' : 'off', clearAll: function () { self.setState({ f: {} }); },
      sideCls: S.sheet ? 'cs-side-open' : '', sheetBg: S.sheet ? 'cs-sheetbg-on' : '', openSheet: function () { self.setState({ sheet: true }); }, closeSheet: function () { self.setState({ sheet: false }); },
      showLabel: 'Show ' + list.length + (list.length === 1 ? ' certification' : ' certifications'),
      cmpBar: cmp.length > 0 && !S.cmpOpen, cmpN: cmp.length + ' of 3', cmpHint: cmp.length < 2 ? 'selected · pick one more' : 'selected', cmpDis: cmp.length < 2 ? 'cd-dis' : '',
      clearCmp: function () { self.setState({ cmp: [], cmpOpen: false }); }, openCmp: function () { if (cmp.length > 1) self.setState({ cmpOpen: true }); }, closeCmp: function () { self.setState({ cmpOpen: false }); },
      cmpOpen: S.cmpOpen && cols.length > 1, cmpCols: cols.map(function (c) { return { t: c.short }; }),
      cmpRows: [row('Issuer', function (c) { return c.issuer; }), row('Level', function (c) { return c.level; }), row('Experience', function (c) { return X5[c.short][0]; }), row('Entry', function (c) { return X5[c.short][1]; }),
        row('You’ll demonstrate', function (c) { return X5[c.short][2]; }), row('Assessment', function (c) { return X5[c.short][3]; }), row('Preparation', function (c) { return c.time; }),
        row('Assessment fee', function (c) { return TC_[c.short][4] + ' Credits'; }), row('Validation', function (c) { return TIER_[TC_[c.short][2]][0] + ' · CEI ' + TC_[c.short][3]; })]
    });
  }
}
'''.replace('X5_', json.dumps(X5, ensure_ascii=False))
i = s.index('  renderVals() {'); j = s.index('</script>', i)
s = s[:i] + JS + s[j:]
rep("this.state = { q: '', field: 'All' };", "var cv = props && props.view === 'compare';\n    this.state = { q: '', field: 'All', f: {}, sort: 'Recommended', sheet: false, cmp: cv ? ['Data Analysis', 'Financial Analysis'] : [], cmpOpen: cv };\n    this.G = " + json.dumps(G, ensure_ascii=False) + ";")
rep('"$preview":', '"view":{"editor":"enum","options":["","compare"],"default":""},"$preview":')

CP = open(os.path.join(D, 'CareerPaths.dc.html')).read()
cp4 = [r for r in re.findall(r'(?:^|\n)(\.cp4-[^{]*\{[^}]*\})', CP[CP.find('<style>'):CP.find('</style>')])]
need = [l.strip() for l in kit.KIT_CSS.split('\n') if re.match(r'\.(ds-tag\.(green|amber)|ds-ghost)[.:{,\s]', l.strip())]
CSS = FILT + '\n'.join(need) + '\n' + '\n'.join(r for r in cp4 if not r.startswith(('.cp4-q', '.cp4-fit', '.cp4-dest', '.cp4-dhw', '.cp4-dg', '.cp4-d', '.cp4-cw:has', '.cp4-cw .cp-top'))) + r'''
.ds-btn.cd-dis{background:#3A4566;color:#B5BDD3;box-shadow:none;pointer-events:none}
.cp4-main .ct-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
.ct-body .ct-bar{margin-bottom:8px}
.ct5-dem{display:flex;flex-wrap:wrap;align-items:center;gap:4px 8px;font-size:13px;line-height:1.45;color:#0B1433}
.ct5-dem em{flex-basis:100%;font-style:normal;font-size:11.5px;font-weight:500;color:#8A93AD}
.ct5-dem .ds-tag{height:22px;font-size:11.5px;padding:0 8px}
.ct5-steps{grid-template-columns:repeat(4,minmax(0,1fr))}
.cp4-cw .cp4-cmp{top:18px;right:18px}
@media (max-width: 1180px){.cp4-main .ct-grid{grid-template-columns:minmax(0,1fr)}.ct5-steps{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width: 960px){.cp4-main .ct-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width: 760px){.cp4-main .ct-grid{grid-template-columns:minmax(0,1fr)}.ct5-steps{grid-template-columns:minmax(0,1fr)}.cp4-cw .cp4-cmp{top:14px;right:14px}}
@media (max-width: 760px){.cp4-lay{grid-template-columns:minmax(0,1fr)}}
'''
i = s.find('</style>'); s = s[:i] + CSS + s[i:]
open(P, 'w').write(s); print('patched Certifications')
