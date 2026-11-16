"""Review check fixes (after batch 7): missing filters + cert levels + cohort dates.
Patches live files in canvas3/project. Usage: python3 chk8.py <canvas3/project>"""
import re, sys, os
D = sys.argv[1]

def rd(n): return open(os.path.join(D, n), encoding='utf-8').read()
def wr(n, s): open(os.path.join(D, n), 'w', encoding='utf-8').write(s)
def rep(s, a, b, n=1):
    c = s.count(a)
    assert c == n, (a[:80], c)
    return s.replace(a, b)

def grp_tpl(s, label):
    """Copy an existing plain filter group (no tooltip) as a template."""
    m = re.search(r'<div class="cs-grp" role="group" aria-label="' + re.escape(label) + r'"><span class="cs-gl">[^<]*</span><div class="cs-cw"><sc-for list="\{\{f_[a-z]+\}\}".*?</sc-for></div></div>', s)
    assert m, label
    return m.group(0), m.start(), m.end()

def mk(tpl, label, key):
    t = re.sub(r'aria-label="[^"]*"', 'aria-label="%s"' % label, tpl, count=1)
    t = re.sub(r'<span class="cs-gl">[^<]*</span>', '<span class="cs-gl">%s</span>' % label.upper(), t, count=1)
    return re.sub(r'\{\{f_[a-z]+\}\}', '{{f_%s}}' % key, t, count=1)

def grp_start(s, label):
    i = s.index('<div class="cs-grp" role="group" aria-label="%s">' % label)
    return i

# ---------- Career paths: Industry ----------
s = rd('CareerPaths.dc.html')
assert '"ind"' not in s, 'already patched'
tpl, a, b = grp_tpl(s, 'Duration')
s = s[:a] + mk(tpl, 'Industry', 'ind') + s[a:]
s = rep(s, '["dur", ["Under 6 months", "6–8 months", "Over 8 months"], "dur"]',
        '["ind", ["Technology", "Finance", "Retail", "Healthcare", "Public sector"], "ind"], ["dur", ["Under 6 months", "6–8 months", "Over 8 months"], "dur"]')
s = rep(s, "      if (k === 'by') return [p.by === 'Northgate University'",
        "      if (k === 'ind') return ({ 'Data Analyst': ['Retail', 'Finance', 'Healthcare', 'Technology'], 'Product Designer': ['Technology', 'Retail'], 'AI Engineer': ['Technology', 'Finance'], 'Cybersecurity Analyst': ['Finance', 'Public sector', 'Technology'], 'Project Manager': ['Public sector', 'Technology'], 'Frontend Developer': ['Technology', 'Retail'] })[p.t] || [];\n"
        "      if (k === 'by') return [p.by === 'Northgate University'")
wr('CareerPaths.dc.html', s)

# ---------- Certifications: levels, Industry, Access ----------
LVL = {'Data Analysis': 'Intermediate', 'Product Design': 'Intermediate', 'Security Operations': 'Advanced',
       'Applied AI Practitioner': 'Intermediate', 'Financial Analysis': 'Advanced'}
s = rd('Certifications.dc.html')
s = rep(s, '["lvl", ["Foundation", "Professional", "Advanced"], "level"]',
        '["lvl", ["Foundation", "Intermediate", "Advanced", "Expert"], "level"], ["ind", ["Technology", "Finance", "Retail", "Healthcare", "Public sector"], "ind"]')
s = rep(s, '["fee", ["Under 150 Credits", "150–200 Credits", "Over 200 Credits"], "fee"]',
        '["fee", ["Under 150 Credits", "150–200 Credits", "Over 200 Credits"], "fee"], ["acc", ["Prepare with DLP", "Prepare with Credits", "Employer can pay"], "acc"]')
for short, lv in LVL.items():
    s = re.sub(r"(R\('[^']*', '%s', '[^']*', '[^']*', '[^']*', )'Professional'" % re.escape(short), r"\1'%s'" % lv, s, count=1)
assert "'Professional', '" not in re.sub(r"'Professional Cert[^']*'", '', s), 'level left'
s = rep(s, "      if (k === 'fee') return",
        "      if (k === 'ind') return ({ 'Data Analysis': ['Retail', 'Finance', 'Healthcare', 'Technology'], 'Product Design': ['Technology', 'Retail'], 'Security Operations': ['Finance', 'Public sector', 'Technology'], 'Project Management': ['Public sector', 'Technology'], 'Applied AI Practitioner': ['Technology'], 'Financial Analysis': ['Finance'] })[c.short] || [];\n"
        "      if (k === 'acc') return ['Prepare with DLP', 'Prepare with Credits'].concat(c.type === 'Institutions' ? ['Employer can pay'] : []);\n"
        "      if (k === 'fee') return")
s = rep(s, 'Foundation is for newcomers to the field. Professional and above expect some experience.',
        'Foundation is for newcomers to the field. Intermediate and above expect some experience.')
tpl, a, b = grp_tpl(s, 'Assessment format')
s = s[:a] + mk(tpl, 'Industry', 'ind') + s[a:]
i = s.index('<button class="ds-btn cs-go2"')
s = s[:i] + mk(tpl, 'Access', 'acc') + s[i:]
wr('Certifications.dc.html', s)

s = rd('Explore.dc.html')
for short, lv in LVL.items():
    s = re.sub(r"(short: '%s',[^}]*?level: )'Professional'" % re.escape(short), r"\1'%s'" % lv, s, count=1)
# Explore: shared Skills filter
s = rep(s, "['lang', 'Language', ['English', 'French'], '']];",
        "['lang', 'Language', ['English', 'French'], ''], ['sk', 'Skills', ['Data analysis', 'AI', 'Design', 'Leadership', 'Security', 'Software'], '']];")
s = rep(s, '  f7v(x, k) {\n', '  f7v(x, k) {\n    var r = this._f7v8(x, k), h = (x.t + \' \' + (x.skills || []).join(\' \') + \' \' + (x.topic || x.area || \'\')).toLowerCase();\n'
        "    r.sk = [['Data analysis', /data|sql|analy|statist|power bi|excel/], ['AI', /\\bai\\b|machine|llm|prompt/], ['Design', /design|ux|figma/], ['Leadership', /lead|manag|project/], ['Security', /secur|cyber/], ['Software', /python|javascript|frontend|software|react|cloud/]].filter(function (p) { return p[1].test(h); }).map(function (p) { return p[0]; });\n"
        '    return r;\n  }\n  _f7v8(x, k) {\n')
s = rep(s, 'Level, validation, access and language apply to every type.', 'Level, validation, access, language and skills apply to every type.')
wr('Explore.dc.html', s)

s = rd('CertDetail.dc.html')
s = rep(s, '<span class="ds-tag line lg">Professional</span>', '<span class="ds-tag line lg">Intermediate</span>')
wr('CertDetail.dc.html', s)
s = rd('Dashboard.dc.html')
s = rep(s, 'Northgate University<span class="cs-dot"></span>Professional<span class="cs-dot"></span>About 30 hrs',
        'Northgate University<span class="cs-dot"></span>Intermediate<span class="cs-dot"></span>About 30 hrs')
wr('Dashboard.dc.html', s)

# ---------- Programs: skills, roles, duration, session days, time zone ----------
s = rd('Programs.dc.html')
s = rep(s, '["time", ["Daytime", "Evenings", "Weekends", "No fixed times"], 5]',
        '["day", ["Weekdays", "Weekends", "Flexible"], "day"], ["time", ["Daytime", "Evenings", "Weekends", "No fixed times"], 5], ["tz", ["GMT (UK)", "CET (Europe)", "Any time zone"], "tz"]')
s = rep(s, '["eff", ["Up to 5 hrs a week", "6–10 hrs a week", "Over 10 hrs a week"], "eff"]',
        '["eff", ["Up to 5 hrs a week", "6–10 hrs a week", "Over 10 hrs a week"], "eff"], ["len", ["Up to 8 weeks", "9–12 weeks", "Over 12 weeks"], "len"]')
s = rep(s, '["dom", ["Data & AI", "Technology", "Business", "Design", "Health"], 0]',
        '["dom", ["Data & AI", "Technology", "Business", "Design", "Health"], 0], ["sk", ["Data analysis", "AI tools", "Leadership", "Web development", "UX design", "Security"], "sk"], ["role", ["Data analyst", "Product designer", "Software developer", "Manager or leader", "Security analyst"], "role"]')
X8 = ('{"Applied Project Leadership": [["Leadership"], ["Manager or leader"], ["Weekdays"], ["GMT (UK)"]], '
      '"AI & Data Analytics Accelerator": [["Data analysis", "AI tools"], ["Data analyst"], ["Weekdays", "Weekends"], ["GMT (UK)"]], '
      '"Frontend Engineering Bootcamp": [["Web development"], ["Software developer"], ["Weekdays"], ["CET (Europe)"]], '
      '"Product Design Cohort": [["UX design"], ["Product designer"], ["Weekdays"], ["GMT (UK)"]], '
      '"AI for Business Leaders": [["AI tools", "Leadership"], ["Manager or leader"], ["Weekdays"], ["GMT (UK)"]], '
      '"Clinical Data Program": [["Data analysis"], ["Data analyst"], ["Weekends"], ["GMT (UK)"]], '
      '"Executive Leadership in the AI Era": [["Leadership", "AI tools"], ["Manager or leader"], ["Weekdays"], ["GMT (UK)"]], '
      '"Cloud & Security Pathway": [["Security"], ["Security analyst", "Software developer"], ["Flexible"], ["Any time zone"]]}')
s = rep(s, "    var val = function (p, k) { var x = X6[p.t];",
        "    var X8 = " + X8 + ";\n"
        "    var val = function (p, k) { var x = X6[p.t], y = X8[p.t];"
        " if (k === 'sk') return y[0]; if (k === 'role') return y[1]; if (k === 'day') return y[2]; if (k === 'tz') return y[3];"
        " if (k === 'len') { var w = parseInt(p.len); return [!/week/.test(p.len) ? 'Over 12 weeks' : (w <= 8 ? 'Up to 8 weeks' : (w <= 12 ? '9–12 weeks' : 'Over 12 weeks'))]; }")
tpl, a, b = grp_tpl(s, 'Delivery format')
st = grp_start(s, 'Session time')
s = s[:st] + mk(tpl, 'Session days', 'day') + s[st:]
tpl, a, b = grp_tpl(s, 'Delivery format')
s = s[:a] + mk(tpl, 'Time zone', 'tz') + s[a:]
tpl, a, b = grp_tpl(s, 'Start')
s = s[:a] + mk(tpl, 'Duration', 'len') + s[a:]
tpl, a, b = grp_tpl(s, 'Designed for')
s = s[:a] + mk(tpl, 'Skills', 'sk') + mk(tpl, 'Roles', 'role') + s[a:]
wr('Programs.dc.html', s)

# ---------- Program detail: cohort dates + places left ----------
s = rd('ProgramDetail.dc.html')
s = rep(s, '"12 Jan – 6 Apr · Tue 18:00 GMT", "Places available"', '"18 Jan – 12 Apr · Tue 18:00 GMT", "9 places left"')
s = rep(s, '"12 Apr – 5 Jul · Tue 18:00 GMT", "Applications open"', '"12 Apr – 5 Jul · Tue 18:00 GMT", "Open · 40 places"')
s = rep(s, 'Completed 6 Apr 2027', 'Completed 12 Apr 2027', 2)
wr('ProgramDetail.dc.html', s)
print('ok')
