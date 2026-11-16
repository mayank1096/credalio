"""Landing batch 6 (client review, Learning programs listing): real filters (domain, designed for, entry level,
delivery format, start month, weekly effort, session time, enrolment status, access), sort, result count, compare,
pagination, schedule on every row, and the "no cohorts match your schedule" state.
Patches the live Programs.dc.html in place. Prop view = '' | compare | noschedule. Usage: python3 pl6.py <canvas3/project>"""
import re, sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import kit
from kit import ck, ARROW, tip
D = sys.argv[1]; P = os.path.join(D, 'Programs.dc.html'); s = open(P).read()
assert 'pl6-' not in s, 'already patched'
FILT = open(os.path.join(HERE, 'csfilt.css')).read()
def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:90], s.count(a)); s = s.replace(a, b)
def svg(d, w=18, sw=2):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (w, w, sw, d)
CHEV = svg('<path d="m6 9 6 6 6-6"></path>', 14, 2.2)
FILTI = svg('<path d="M4 6h16M7 12h10M10 18h4"></path>', 16, 2.2)
X = svg('<path d="M6 6l12 12M18 6 6 18"></path>', 13, 2.4)
CAL = svg('<rect x="3" y="5" width="18" height="16" rx="3"></rect><path d="M3 10h18M8 3v4M16 3v4"></path>', 22, 1.9)
CLOCK = svg('<circle cx="12" cy="12" r="9"></circle><path d="M12 7v5l3 2"></path>', 13, 2)

def grp(key, label, t=''):
    return ('<div class="cs-grp" role="group" aria-label="%s"><span class="cs-gl">%s%s</span><div class="cs-cw"><sc-for list="{{f_%s}}" as="f" hint-placeholder-count="3">'
            '<button class="ds-chip sm {{f.cls}}" type="button" role="checkbox" aria-checked="{{f.on}}" onClick="{{f.pick}}">%s{{f.label}}<i>{{f.n}}</i></button></sc-for></div></div>') % (
        label, label.upper(), tip(t) if t else '', key, ck(12))
ASIDE = ('<div class="cs-sheetbg {{sheetBg}}" onClick="{{closeSheet}}"></div>\n<aside class="cs-side {{sideCls}}" aria-label="Filters">'
         '<div class="cs-sh"><b>Filters</b><span style="display: flex; align-items: center; gap: 14px"><button class="ds-link {{clearCls}}" type="button" onClick="{{clearAll}}">Clear all</button>'
         '<button class="ds-link cs-sheetx" type="button" onClick="{{closeSheet}}" style="display: none; color: #0B1433">Done</button></span></div>'
         + grp('time', 'Session time', 'Times are in GMT. Signed in, they show in your own time zone.') + grp('fmt', 'Delivery format') + grp('eff', 'Weekly effort') + grp('start', 'Start')
         + grp('dom', 'Domain') + grp('for', 'Designed for') + grp('lvl', 'Entry level') + grp('st', 'Enrolment') + grp('acc', 'Access', 'Pay with Credits, or use DLP from a Pro plan where the provider allows it.')
         + '<button class="ds-btn cs-go2" type="button" onClick="{{closeSheet}}"><span>{{showLabel}}</span><span class="ob-arrow">%s</span></button></aside>') % ARROW
TOP = ('<div class="cs-bar"><div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap; min-width: 0">'
       '<button class="ds-chip cs-fbtn" type="button" onClick="{{openSheet}}">%sFilters<sc-if value="{{hasFilters}}" hint-placeholder-val="{{ false }}"><i>{{nFilters}}</i></sc-if></button>'
       '<span class="cs-count" aria-live="polite">{{count}}</span></div>'
       '<span class="cs-sortw"><span>Sort</span><span class="cs-selw"><label for="pl6-sort" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Sort programs</label>'
       '<select id="pl6-sort" class="cs-sel" onChange="{{onSort}}"><sc-for list="{{sorts}}" as="o" hint-placeholder-count="4"><option value="{{o.v}}" selected="{{o.sel}}">{{o.v}}</option></sc-for></select>%s</span></span></div>\n'
       '<sc-if value="{{hasFilters}}" hint-placeholder-val="{{ false }}"><div class="cs-chips" aria-label="Active filters"><sc-for list="{{active}}" as="a" hint-placeholder-count="2">'
       '<button class="ds-chip sm on" type="button" onClick="{{a.drop}}" aria-label="Remove filter {{a.label}}">{{a.label}}%s</button></sc-for></div></sc-if>\n'
       '<sc-if value="{{cmpOpen}}" hint-placeholder-val="{{ false }}"><section class="cp4-ct" aria-labelledby="pl6-cth"><div class="cp4-cth"><h2 id="pl6-cth">Compare programs</h2>'
       '<button class="ds-link" type="button" onClick="{{closeCmp}}">Close</button></div><div class="cp4-tw"><table><thead><tr><th scope="col"></th><sc-for list="{{cmpCols}}" as="c" hint-placeholder-count="2"><th scope="col">{{c.t}}</th></sc-for></tr></thead>'
       '<tbody><sc-for list="{{cmpRows}}" as="r" hint-placeholder-count="9"><tr><th scope="row">{{r.k}}</th><sc-for list="{{r.v}}" as="v" hint-placeholder-count="2"><td>{{v}}</td></sc-for></tr></sc-for></tbody></table></div>'
       '<p class="cp4-cn">Times are in GMT. Places and dates come from each provider’s live cohort records.</p></section></sc-if>\n') % (FILTI, CHEV, X)
NOSCHED = ('<sc-if value="{{none}}" hint-placeholder-val="{{ false }}"><div class="pl6-none"><span class="pl6-ni" aria-hidden="true">%s</span><b>No cohorts match your schedule</b>'
           '<span>Nothing runs at the times you picked. Try a wider time, or learn at your own pace and join live sessions later.</span>'
           '<div class="pl6-na"><button class="ds-ghost sm" type="button" onClick="{{clearSched}}">Clear schedule filters</button><a class="ds-link" href="#">Tell me when a cohort opens →</a></div>'
           '<div class="pl6-alt"><span class="pl6-k">At your own pace instead</span><a class="pl6-ar" href="ProgramDetail.dc.html"><b>Cloud &amp; Security Pathway</b><span>Self-paced program · 5 courses · start any time</span></a>'
           '<a class="pl6-ar" href="CareerPaths.dc.html"><b>Data Analyst career path</b><span>Self-paced · 6–8 months · fits any week</span></a></div></div></sc-if>\n') % CAL
PAGER = ('<nav class="cp4-pg" aria-label="Pagination"><span>{{pageLabel}}</span><div><button class="cp4-pn on" type="button" aria-current="page">1</button><button class="cp4-pn" type="button">2</button>'
         '<button class="ds-ghost sm" type="button">Next</button></div></nav>\n')
CMPBAR = ('<sc-if value="{{cmpBar}}" hint-placeholder-val="{{ false }}"><div class="cp4-bar" role="region" aria-label="Compare"><span><b>{{cmpN}}</b> {{cmpHint}}</span>'
          '<span class="cp4-ba"><button class="ds-link" type="button" onClick="{{clearCmp}}">Clear</button><button class="ds-btn sm {{cmpDis}}" type="button" onClick="{{openCmp}}"><span>Compare</span><span class="ob-arrow">%s</span></button></span></div></sc-if>\n') % ARROW

body = s[s.index('<div class="pg-body">'):s.index('<section class="pg-ai nova-card"')]
feat = body[body.index('<sc-if value="{{showFeat}}"'):body.index('<div class="pg-sh">')]
lst = body[body.index('<div class="pg-list">'):]
lst = lst.replace('<sc-for list="{{progs}}" as="p" hint-placeholder-count="8">', '<sc-for list="{{progs}}" as="p" hint-placeholder-count="8"><div class="pl6-rw">')
lst = lst.replace('<span class="pg-rm" style="display: block">{{p.meta}}<span class="pg-by"> · {{p.by}}</span></span>',
                  '<span class="pg-rm" style="display: block">{{p.meta}}<span class="pg-by"> · {{p.by}}</span></span><span class="pl6-sch">%s{{p.sched}}</span>' % CLOCK)
lst = re.sub(r'(<span class="pg-go" aria-hidden="true">.*?</span>\n</a>)', r'\1<button class="pl6-cmp {{p.cmpCls}}" type="button" aria-pressed="{{p.cmpOn}}" onClick="{{p.cmp}}"><span class="cp4-box">' + ck(11).replace('\\', '\\\\') + '</span>Compare</button></div>', lst, count=1, flags=re.S)
lst = lst.replace('<sc-if value="{{none}}" hint-placeholder-val="{{ false }}"><div class="pg-empty">No programs of this type are open right now.</div></sc-if>', NOSCHED)
lst = lst.rstrip(); assert lst.endswith('</div>'); lst = lst[:-6].rstrip()
NEW = ('<div class="pg-body">\n' + feat + '<div class="cp4-lay">\n' + ASIDE + '\n<div class="cp4-main">\n' + TOP + lst + '\n</div>\n' + PAGER + '</div>\n</div>\n' + CMPBAR)
s = s.replace(body, NEW, 1)
rep('<div class="pg-sh">', '<div class="pg-sh" hidden>') if '<div class="pg-sh">' in s else None

# ---------------------------------------------------------------- JS
X6 = {'Applied Project Leadership': ['Business', ['Working professionals'], 'Intermediate', 'Hybrid', 'Wed 18:00–20:00 GMT', 'Evenings', 5, 'January', 'Applications open'],
      'AI & Data Analytics Accelerator': ['Data & AI', ['Career switchers', 'Working professionals', 'Recent graduates'], 'Intermediate', 'Live online', 'Tue 18:00–19:30 GMT', 'Evenings', 6, 'January', 'Places available'],
      'Frontend Engineering Bootcamp': ['Technology', ['Career switchers', 'Recent graduates'], 'Beginner', 'Live online', 'Mon–Thu 19:00–21:00 CET', 'Evenings', 15, 'January', 'Places available'],
      'Product Design Cohort': ['Design', ['Career switchers'], 'Beginner', 'Live online', 'Wed 17:00–18:30 GMT', 'Evenings', 6, 'January', 'Places available'],
      'AI for Business Leaders': ['Data & AI', ['Working professionals'], 'Advanced', 'In person', 'Fri 09:30–12:30 · London', 'Daytime', 4, 'February', 'Waitlist open'],
      'Clinical Data Program': ['Health', ['Working professionals'], 'Intermediate', 'Hybrid', 'Sat 10:00–12:00 GMT', 'Weekends', 5, 'February', 'Applications open'],
      'Executive Leadership in the AI Era': ['Business', ['Working professionals'], 'Advanced', 'In person', 'Thu 09:00–12:00 · Manchester', 'Daytime', 4, 'February', 'Waitlist open'],
      'Cloud & Security Pathway': ['Technology', ['Career switchers', 'Recent graduates'], 'Beginner', 'Self-paced', 'No fixed times', 'No fixed times', 4, 'Any time', 'Start any time']}
ACC = {'Applied Project Leadership': ['Credits'], 'AI & Data Analytics Accelerator': ['Credits', 'DLP (Pro)'], 'Frontend Engineering Bootcamp': ['Credits'], 'Product Design Cohort': ['Credits', 'DLP (Pro)'],
       'AI for Business Leaders': ['Credits'], 'Clinical Data Program': ['Credits'], 'Executive Leadership in the AI Era': ['Credits'], 'Cloud & Security Pathway': ['Credits', 'DLP (Pro)']}
G = [('time', ['Daytime', 'Evenings', 'Weekends', 'No fixed times'], 5), ('fmt', ['Live online', 'In person', 'Hybrid', 'Self-paced'], 3), ('eff', ['Up to 5 hrs a week', '6–10 hrs a week', 'Over 10 hrs a week'], 'eff'),
     ('start', ['January', 'February', 'Any time'], 7), ('dom', ['Data & AI', 'Technology', 'Business', 'Design', 'Health'], 0), ('for', ['Career switchers', 'Working professionals', 'Recent graduates'], 1),
     ('lvl', ['Beginner', 'Intermediate', 'Advanced'], 2), ('st', ['Places available', 'Applications open', 'Waitlist open', 'Start any time'], 8), ('acc', ['Credits', 'DLP (Pro)'], 'acc')]
JS = r'''  renderVals() {
    var self = this, S = this.state, X6 = X6_, AC = ACC_;
    var val = function (p, k) { var x = X6[p.t]; if (k === 'eff') return [x[6] <= 5 ? 'Up to 5 hrs a week' : (x[6] <= 10 ? '6–10 hrs a week' : 'Over 10 hrs a week')]; if (k === 'acc') return AC[p.t]; var v = x[k]; return Array.isArray(v) ? v : [v]; };
    var match = function (p, skip) {
      if (S.type !== 'All' && p.type !== S.type) return false;
      for (var i = 0; i < self.G.length; i++) { var g = self.G[i]; if (g[0] === skip) continue; var on = S.f[g[0]] || []; if (on.length && !on.some(function (o) { return val(p, g[2]).indexOf(o) > -1; })) return false; }
      return true;
    };
    var nF = Object.keys(S.f).reduce(function (n, k) { return n + (S.f[k] || []).length; }, 0);
    var showFeat = (S.type === 'All' || S.type === 'Accelerator') && !nF;
    var list = this.L.filter(function (p) { return match(p) && !(showFeat && p.t === 'AI & Data Analytics Accelerator'); });
    var srt = { 'Starting soonest': function (a, b) { return (a.d ? parseInt(a.d) + (a.m === 'FEB' ? 31 : 0) : 99) - (b.d ? parseInt(b.d) + (b.m === 'FEB' ? 31 : 0) : 99); }, 'Lowest fee': function (a, b) { return parseInt(TG_[a.t][4].replace(',', '')) - parseInt(TG_[b.t][4].replace(',', '')); },
      'Least time a week': function (a, b) { return X6[a.t][6] - X6[b.t][6]; } };
    if (srt[S.sort]) list = list.slice().sort(srt[S.sort]);
    var toggle = function (key, o) { var f = Object.assign({}, S.f), l = (f[key] || []).slice(), i = l.indexOf(o); if (i > -1) l.splice(i, 1); else l.push(o); f[key] = l; self.setState({ f: f }); };
    var v = {};
    this.G.forEach(function (g) { var key = g[0]; v['f_' + key] = g[1].map(function (o) { var on = (S.f[key] || []).indexOf(o) > -1; return { label: o, n: self.L.filter(function (p) { return match(p, key) && val(p, g[2]).indexOf(o) > -1; }).length, on: on ? 'true' : 'false', cls: on ? 'on' : '', pick: function () { toggle(key, o); } }; }); });
    var active = []; Object.keys(S.f).forEach(function (k) { (S.f[k] || []).forEach(function (o) { active.push({ label: o, drop: function () { toggle(k, o); } }); }); });
    var cmp = S.cmp, cols = this.L.filter(function (p) { return cmp.indexOf(p.t) > -1; });
    var row = function (k, fn) { return { k: k, v: cols.map(fn) }; };
    var total = list.length + (showFeat ? 1 : 0);
    return Object.assign(v, {
      types: ['All', 'Cohort', 'Bootcamp', 'Accelerator', 'Institution', 'Executive', 'Self-paced'].map(function (t) { var on = S.type === t; return { label: t === 'All' ? 'All programs' : t, on: on ? 'true' : 'false', cls: on ? 'on' : '', pick: function () { self.setState({ type: t }); } }; }),
      showFeat: showFeat, listTitle: showFeat ? 'More upcoming programs' : 'Upcoming programs',
      count: total + (total === 1 ? ' program' : ' programs'), pageLabel: total ? 'Showing 1–' + total + ' of ' + (total === self.L.length ? 14 : total) + ' programs' : '',
      progs: list.map(function (p) { var st = self.ST[p.st], t = TG_[p.t], x = X6[p.t], on = cmp.indexOf(p.t) > -1; return { rating: t[0], reviews: t[1], tierLabel: TIER_[t[2]][0], tierDot: TIER_[t[2]][1], cei: t[3], fee: t[4], tagA: 'blue', tagB: 'line', t: p.t, meta: self.NAMES[p.type] + ' · ' + p.len + ' · ' + x[2], by: p.by,
        sched: x[3] + ' · ' + x[4] + (x[6] ? ' · ' + x[6] + ' hrs a week' : ''), d: p.d || 'Any', m: p.m || 'TIME', dcls: p.d ? '' : 'pg-any', when: p.d ? 'Starts ' + p.d + ' ' + p.m : 'Start any time', status: st[0], sc: st[1],
        cmpOn: on ? 'true' : 'false', cmpCls: on ? 'on' : '', cmp: function () { var l = cmp.slice(), i = l.indexOf(p.t); if (i > -1) l.splice(i, 1); else if (l.length < 3) l.push(p.t); self.setState({ cmp: l, cmpOpen: S.cmpOpen && l.length > 1 }); } }; }),
      none: list.length === 0 && !showFeat,
      clearSched: function () { var f = Object.assign({}, S.f); delete f.time; delete f.fmt; delete f.start; self.setState({ f: f }); },
      sorts: ['Recommended', 'Starting soonest', 'Lowest fee', 'Least time a week'].map(function (o) { return { v: o, sel: S.sort === o }; }), onSort: function (e) { self.setState({ sort: e.target.value }); },
      hasFilters: nF > 0, nFilters: nF, active: active, clearCls: nF ? '' : 'off', clearAll: function () { self.setState({ f: {} }); },
      sideCls: S.sheet ? 'cs-side-open' : '', sheetBg: S.sheet ? 'cs-sheetbg-on' : '', openSheet: function () { self.setState({ sheet: true }); }, closeSheet: function () { self.setState({ sheet: false }); },
      showLabel: 'Show ' + total + (total === 1 ? ' program' : ' programs'),
      cmpBar: cmp.length > 0 && !S.cmpOpen, cmpN: cmp.length + ' of 3', cmpHint: cmp.length < 2 ? 'selected · pick one more' : 'selected', cmpDis: cmp.length < 2 ? 'cd-dis' : '',
      clearCmp: function () { self.setState({ cmp: [], cmpOpen: false }); }, openCmp: function () { if (cmp.length > 1) self.setState({ cmpOpen: true }); }, closeCmp: function () { self.setState({ cmpOpen: false }); },
      cmpOpen: S.cmpOpen && cols.length > 1, cmpCols: cols.map(function (p) { return { t: p.t }; }),
      cmpRows: [row('Provider', function (p) { return p.by; }), row('Format', function (p) { return X6[p.t][3]; }), row('When', function (p) { return X6[p.t][4]; }), row('Length', function (p) { return p.len; }),
        row('Each week', function (p) { return X6[p.t][6] + ' hrs'; }), row('Entry level', function (p) { return X6[p.t][2]; }), row('Starts', function (p) { return p.d ? p.d + ' ' + p.m.charAt(0) + p.m.slice(1).toLowerCase() : 'Any time'; }),
        row('Fee', function (p) { return TG_[p.t][4] + ' Credits' + (AC[p.t].length > 1 ? ' or DLP on Pro' : ''); }), row('Status', function (p) { return self.ST[p.st][0]; })],
      onSubmit: function (e) { e.preventDefault(); }
    });
  }
}
'''.replace('X6_', json.dumps(X6, ensure_ascii=False)).replace('ACC_', json.dumps(ACC, ensure_ascii=False))
i = s.index('  renderVals() {'); j = s.index('</script>', i)
s = s[:i] + JS + s[j:]
rep("this.state = { type: 'All' };", "var vw = (props && props.view) || '';\n    this.state = { type: 'All', f: vw === 'noschedule' ? { time: ['Weekends'], fmt: ['Live online'] } : {}, sort: 'Recommended', sheet: false, cmp: vw === 'compare' ? ['Applied Project Leadership', 'Product Design Cohort'] : [], cmpOpen: vw === 'compare' };\n    this.G = " + json.dumps(G, ensure_ascii=False) + ";")
rep('"$preview":', '"view":{"editor":"enum","options":["","compare","noschedule"],"default":""},"$preview":')

CP = open(os.path.join(D, 'CareerPaths.dc.html')).read()
cp4 = re.findall(r'(?:^|\n)(\.cp4-[^{]*\{[^}]*\})', CP[CP.find('<style>'):CP.find('</style>')])
need = [l.strip() for l in kit.KIT_CSS.split('\n') if re.match(r'\.(ds-ghost|tip)[.:{,\s-]', l.strip())]
CSS = FILT + '\n'.join(need) + '\n@media (max-width: 760px){.tip-b{display:none;width:min(250px,calc(100vw - 48px))}.tip:hover .tip-b,.tip:focus .tip-b{display:block}}\n' + '\n'.join(
    r for r in cp4 if r.startswith(('.cp4-lay', '.cp4-main{', '.cp4-pg', '.cp4-pn', '.cp4-bar', '.cp4-b', '.cp4-ct', '.cp4-cth', '.cp4-tw', '.cp4-cn'))) + r'''
.ds-btn.cd-dis{background:#3A4566;color:#B5BDD3;box-shadow:none;pointer-events:none}
.ds-link{display:inline-flex;align-items:center;gap:6px;color:#1652F0;font-family:inherit;font-weight:600;font-size:14.5px;text-decoration:none;background:none;border:0;padding:0;cursor:pointer;white-space:nowrap}
.ds-link:hover{color:#0E3BB8}
.ds-link.off{color:#B5BDD3;pointer-events:none}
.cp4-main:has(.pl6-none) ~ .cp4-pg{display:none}
.cp4-ba .ds-link{color:rgba(255,255,255,.75)}
@media (max-width: 960px){.cp4-lay{grid-template-columns:minmax(0,1fr)}}
@media (max-width: 760px){.cp4-main .pg-row{grid-template-columns:56px minmax(0,1fr) auto;row-gap:10px}.cp4-main .pg-row > .mx-p{grid-column:2;grid-row:2}.cp4-main .pg-row > .pg-stat{grid-column:3;grid-row:2;justify-self:end}.cp4-pg{flex-direction:column;align-items:stretch;gap:12px;text-align:center}.cp4-pg > div{justify-content:center}.cp4-bar{bottom:12px;gap:12px;padding:8px 8px 8px 16px;font-size:13px}.cp4-ba .ds-link{display:none}.cp4-ct{padding:18px 14px;margin:0 -4px}.cp4-ct tbody th{width:96px}}
.pg-body > .cp4-lay{margin-top:8px}
.pl6-rw{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:10px;align-items:center}
.pl6-sch{display:flex;align-items:center;gap:6px;margin-top:6px;font-size:13px;color:#0E3BB8}
.pl6-cmp{display:inline-flex;align-items:center;gap:7px;height:34px;padding:0 12px 0 8px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:inherit;font-size:12.5px;font-weight:500;color:#3A4566;cursor:pointer}
.pl6-cmp:hover{border-color:#1652F0}
.cp4-box{width:16px;height:16px;border-radius:5px;border:1.5px solid #CBD3E6;display:flex;align-items:center;justify-content:center;color:#FFFFFF;box-sizing:border-box}
.cp4-box .ck{display:none}
.pl6-cmp.on{border-color:#1652F0;background:#EAF0FF;color:#0E3BB8}
.pl6-cmp.on .cp4-box{background:#1652F0;border-color:#1652F0}
.pl6-cmp.on .cp4-box .ck{display:block}
.cp4-main .pg-row{grid-template-columns:64px minmax(0,1fr) 130px 150px 36px;gap:18px}
.pl6-none{display:flex;flex-direction:column;align-items:center;text-align:center;gap:10px;padding:36px 28px;border-radius:22px;border:1.5px dashed #CBD7F5;background:#FAFBFF}
.pl6-ni{width:52px;height:52px;border-radius:50%;background:#EAF0FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.pl6-none > b{font-size:20px;font-weight:600;color:#0B1433}
.pl6-none > span:not(.pl6-ni){max-width:460px;font-size:14.5px;line-height:1.55;color:#5B6582}
.pl6-na{display:flex;align-items:center;gap:20px;flex-wrap:wrap;justify-content:center;margin-top:4px}
.pl6-alt{align-self:stretch;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-top:14px;text-align:left}
.pl6-k{grid-column:1 / -1;font-size:12px;font-weight:500;color:#8A93AD}
.pl6-ar{display:flex;flex-direction:column;gap:3px;padding:14px 16px;border-radius:16px;border:1.5px solid #E6EAF3;background:#FFFFFF;text-decoration:none}
.pl6-ar:hover{border-color:#9DB8F7}
.pl6-ar b{font-size:15px;font-weight:600;color:#0B1433}
.pl6-ar span{font-size:13px;color:#5B6582}
@media (max-width: 1180px){.cp4-main .pg-row{grid-template-columns:56px minmax(0,1fr) auto;row-gap:10px}.cp4-main .pg-row > .mx-p{grid-column:2;grid-row:2}.cp4-main .pg-row > .pg-stat{grid-column:3;grid-row:1}.cp4-main .pg-go{display:none}}
@media (max-width: 760px){.pl6-rw{grid-template-columns:minmax(0,1fr);gap:6px}.pl6-cmp{justify-self:end}.cp4-main .pg-row > .pg-stat{grid-column:3;grid-row:2}.pl6-alt{grid-template-columns:minmax(0,1fr)}.pl6-none{padding:28px 18px}}
'''
i = s.find('</style>'); s = s[:i] + CSS + s[i:]
open(P, 'w').write(s); print('patched Programs')
