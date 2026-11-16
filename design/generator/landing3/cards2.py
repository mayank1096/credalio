"""Landing batch 2 (client review): matching cards across learning types + one price rule (DLP or Credits)
+ sample-data fixes. Patches live sources in place. Usage: python3 cards2.py <canvas3/project> <kit.py dir>"""
import re, sys, os
D = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
KIT = open(os.path.join(HERE, 'kit.py')).read()
COURSES = open(os.path.join(D, 'Courses.dc.html')).read()

def rd(f): return open(os.path.join(D, f + '.dc.html')).read()
def wr(f, s): open(os.path.join(D, f + '.dc.html'), 'w').write(s)
def rep(s, a, b, n=1):
    assert s.count(a) >= (1 if n == 'all' else n), (a[:90], s.count(a))
    return s.replace(a, b) if n == 'all' else s.replace(a, b, n)

# ---------------------------------------------------------------- shared CSS (kit values; added only where missing)
def kit_rules(sel_rx):
    return [l.strip() for l in KIT.split('\n') if re.match(sel_rx, l.strip())]
DLP = [r.strip() for r in re.findall(r'(?:^|\n)(\.dlp-c[^{]*\{[^}]*\})', COURSES[COURSES.find('<style'):COURSES.find('</style>')])]
KF = re.findall(r'@keyframes dlp\w+\{(?:[^{}]*\{[^}]*\})*\}', COURSES)
BASE = (kit_rules(r'\.ds-tag(\{|\.blue\{|\.line\{|\.glass\{)') + kit_rules(r'\.cr-c') + DLP + KF)
MX = '''.mx{display:flex;flex-wrap:wrap;align-items:center;gap:6px 8px}
.mx-r{display:inline-flex;align-items:center;gap:4px;font-size:13px;color:#5B6582;margin-right:2px}
.mx-r b{font-weight:600;color:#0B1433}
.mx-s{color:#E3A008}
.mx-d{width:7px;height:7px;border-radius:50%;flex-shrink:0;font-style:normal}
.mx-p{display:inline-flex;align-items:center;flex-wrap:wrap;gap:6px;font-size:13px;color:#5B6582;min-width:0}
.mx-p b{font-size:15px;font-weight:600;color:#0B1433;white-space:nowrap}
.mx-p em{font-style:normal;white-space:nowrap}
.mx-p .cr-c,.mx-life .cr-c{width:16px;height:16px;font-size:9.5px}
.mx-life{display:inline-flex;align-items:center;gap:6px;font-size:13px;color:#5B6582}
.cp-feat .mx-r,.cp-feat .mx-p,.cp-feat .mx-p em{color:rgba(255,255,255,.72)}
.cp-feat .mx-r b,.cp-feat .mx-p b{color:#FFFFFF}
.cp-foot{justify-content:space-between}
.ct-fmt{font-size:13px;color:#5B6582;margin-top:-6px}
.pg-row{grid-template-columns:72px minmax(0,1fr) 170px 170px 40px}
.pg-rx{margin-top:8px}
@media (max-width: 760px){.pg-row{grid-template-columns:56px minmax(0,1fr) auto;row-gap:10px}.pg-date{grid-row:1 / span 2;align-self:start}.pg-row > span:nth-child(2){grid-column:2 / -1}.pg-row > .mx-p{grid-column:2;grid-row:2;margin:0}.pg-row > .pg-stat{grid-column:3;grid-row:2;margin:0;justify-self:end}.pg-rx{margin-top:6px}.pg-rx .ds-tag + .ds-tag{display:none}}
'''
def add_css(s):
    st = s[s.find('<style'):s.find('</style>')]
    have = set(re.findall(r'(?:^|\n|\})\s*([^{}@\n]+)\{', st))
    need = [r for r in BASE if r.split('{')[0].strip() not in have and r not in st]
    i = s.find('</style>')
    return s[:i] + '\n'.join(need) + '\n' + MX + s[i:]

TIER = "{ gold: ['Gold Validated', '#C8961E'], silver: ['Silver Validated', '#8E9BB0'], bronze: ['Bronze Validated', '#A8683A'], rev: ['Validation in review', '#8A93AD'] }"
MXROW = ('<span class="mx"><span class="mx-r"><span class="mx-s" aria-hidden="true">★</span><b>{{X.rating}}</b><span>({{X.reviews}})</span></span>'
         '<span class="ds-tag {{X.tagA}}"><i class="mx-d" style="background: {{X.tierDot}}"></i>{{X.tierLabel}}</span><span class="ds-tag {{X.tagB}}">CEI {{X.cei}}</span></span>')
def mxrow(v): return MXROW.replace('X.', v + '.')
JSV = ("rating: t[0], reviews: t[1], tierLabel: TIER_[t[2]][0], tierDot: TIER_[t[2]][1], cei: t[3]")

# trust + price data (sample; one unit rule: DLP for learning, Credits for lifetime access, assessment and program fees)
PATHS = {'Data Analyst': ['4.8', '2.4k', 'gold', 92, '3,800', '7,600'], 'Product Designer': ['4.7', '1.1k', 'silver', 87, '3,400', '6,800'],
         'AI Engineer': ['4.8', '980', 'gold', 90, '4,600', '9,200'], 'Cybersecurity Analyst': ['4.6', '760', 'silver', 85, '4,200', '8,400'],
         'Project Manager': ['4.6', '640', 'bronze', 80, '2,600', '5,200'], 'Frontend Developer': ['4.7', '1.3k', 'silver', 86, '3,900', '7,800']}
CERTS = {'Data Analysis': ['4.8', '860', 'gold', 93, '150'], 'Product Design': ['4.7', '410', 'silver', 88, '180'], 'Security Operations': ['4.8', '520', 'gold', 91, '220'],
         'Project Management': ['4.6', '690', 'silver', 84, '120'], 'Applied AI Practitioner': ['4.6', '48', 'rev', 89, '160'], 'Financial Analysis': ['4.7', '330', 'silver', 87, '200']}
PROGS = {'Applied Project Leadership': ['4.7', '210', 'silver', 86, '900'], 'AI & Data Analytics Accelerator': ['4.9', '340', 'gold', 94, '1,200'],
         'Frontend Engineering Bootcamp': ['4.7', '520', 'silver', 85, '1,600'], 'Product Design Cohort': ['4.8', '180', 'gold', 88, '950'],
         'AI for Business Leaders': ['4.6', '160', 'silver', 90, '1,100'], 'Clinical Data Program': ['4.8', '95', 'gold', 92, '1,800'],
         'Executive Leadership in the AI Era': ['4.6', '140', 'silver', 89, '1,100'], 'Cloud & Security Pathway': ['4.5', '230', 'bronze', 81, '700']}
import json
def js_data(name, d): return 'var %s = %s;\nvar TIER_ = %s;\n' % (name, json.dumps(d, ensure_ascii=False), TIER)

def path_cards(s):
    s = rep(s, '<span class="cp-foot"><span class="ds-link">Explore path →</span></span>',
            mxrow('p') + '\n<span class="cp-foot"><span class="mx-p"><span class="dlp-c" aria-hidden="true"></span><b>{{p.dlp}} DLP</b><em>or {{p.cr}} Credits</em></span><span class="ds-link">Explore path →</span></span>', 'all')
    s = re.sub(r"(var v = \{ t: p\.t, )", r"var t = TP_[p.t];\n        \1" + JSV + ", dlp: t[4], cr: t[5], tagA: feat ? 'glass' : 'blue', tagB: feat ? 'glass' : 'line', ", s)
    return s

def cert_cards(s):
    s = rep(s, '<span class="ct-foot"><span>{{c.format}}</span><span class="ds-link">View →</span></span>',
            '<span class="ct-fmt">{{c.format}}</span>\n' + mxrow('c') + '\n<span class="ct-foot"><span class="mx-p"><i class="cr-c" aria-hidden="true">C</i><b>{{c.fee}} Credits</b><em>assessment</em></span><span class="ds-link">View →</span></span>', 'all')
    return s

def prog_rows(s):
    s = rep(s, '<span class="pg-rm" style="display: block">{{p.meta}}<span class="pg-by"> · {{p.by}}</span></span></span>',
            '<span class="pg-rm" style="display: block">{{p.meta}}<span class="pg-by"> · {{p.by}}</span></span>' + mxrow('p').replace('class="mx"', 'class="mx pg-rx"') + '</span>\n<span class="mx-p"><i class="cr-c" aria-hidden="true">C</i><b>{{p.fee}} Credits</b></span>', 'all')
    return s

def course_life(s):
    s = re.sub(r'<sc-if value="\{\{c\.hasLife\}\}" hint-placeholder-val="\{\{ false \}\}"><span class="tip" tabindex="0" onClick="\{\{c\.stop\}\}" aria-label="More info">.*?</span></span></sc-if></b></span>',
               '</b></span>\n<sc-if value="{{c.hasLife}}" hint-placeholder-val="{{ false }}"><span class="mx-life"><i class="cr-c" aria-hidden="true">C</i>or {{c.lifeV}} Credits for lifetime access</span></sc-if>', s, flags=re.S)
    s = s.replace("lifeTip: 'Or keep it for life: ' + c.life.toLocaleString('en-GB') + ' credits, one-off.'", "lifeV: c.life.toLocaleString('en-GB')")
    return s

def cert_js(s):
    s, n = re.subn(r"(certs: \w+\.map\(function \(c\) \{ )return \{ short: c\.short,", r"\1var t = TC_[c.short]; return { " + JSV + ", fee: t[4], tagA: c.ok ? 'blue' : 'line', tagB: 'line', short: c.short,", s)
    assert n == 1; return s
def prog_js(s):
    s, n = re.subn(r"return \{ t: p\.t, meta: self\.NAMES\[p\.type\]", "var t = TG_[p.t]; return { " + JSV + ", fee: t[4], tagA: 'blue', tagB: 'line', t: p.t, meta: self.NAMES[p.type]", s)
    assert n == 1; return s
def inject_js(s, block):
    k = s.index('class Component extends DCLogic {')
    return s[:k] + block + s[k:]

# ---------------------------------------------------------------- pages
s = rd('CareerPaths'); s = path_cards(s); s = inject_js(s, js_data('TP_', PATHS)); s = add_css(s); wr('CareerPaths', s)

s = rd('Certifications'); s = cert_cards(s)
s = cert_js(s)
s = inject_js(s, js_data('TC_', CERTS)); s = add_css(s); wr('Certifications', s)

s = rd('Programs'); s = prog_rows(s)
s = prog_js(s)
s = rep(s, '<span><b>12 weeks</b></span><span>Northgate University</span></div>', '<span><b>12 weeks</b></span><span>Northgate University</span><span><b>1,200</b> Credits</span></div>')
s = inject_js(s, js_data('TG_', PROGS)); s = add_css(s); wr('Programs', s)

s = rd('Explore'); s = path_cards(s); s = cert_cards(s); s = prog_rows(s); s = course_life(s); s = cert_js(s); s = prog_js(s)
# Explore's certificate sample data matches the Certifications listing (duration + format)
for short, time, fmt in [('Data Analysis', '3–4 months', 'Timed exam + case study'), ('Product Design', '4–5 months', 'Portfolio review + design challenge'),
                         ('Security Operations', '4–6 months', 'Simulation lab + exam'), ('Financial Analysis', '3–4 months', 'Timed exam + modelling case')]:
    s = re.sub(r"(short: '%s', [^}]*?time: ')[^']*(', format: ')[^']*'" % re.escape(short), r"\g<1>%s\g<2>%s'" % (time, fmt), s)
s = inject_js(s, js_data('TP_', PATHS) + 'var TC_ = %s;\nvar TG_ = %s;\n' % (json.dumps(CERTS, ensure_ascii=False), json.dumps(PROGS, ensure_ascii=False)))
s = add_css(s); wr('Explore', s)

s = rd('Courses'); s = course_life(s); s = add_css(s); wr('Courses', s)

# Statistics Essentials is 10 hrs everywhere (path + certificate); certificate total follows
s = rd('CertDetail'); s = rep(s, 'Statistics Essentials<span>8 hrs</span>', 'Statistics Essentials<span>10 hrs</span>'); s = rep(s, '36 hrs', '38 hrs')
wr('CertDetail', s)
print('ok')
