"""Link 4 · Batch 3: course set-up pages. Client copy word for word.

Course.dc.html (prop page) → CR-STU-026 resources, 027 completion rules, 028 team & assignments (+ my assigned work, + solo my work),
031 DLP & effort, course assessments, practice & projects, delivery & schedule, learner experience, learner support,
032 access model, 033 maintenance burden, 034 pricing (+ update required), 035 summary.
CR-STU-030 Team Chat is a Builder overlay (stu2.py).
"""
import json
from l4kit import *
from rail import ring, nova_rail
from kit import coin, credit
import stu2
from stu2 import ppl, ITEM_IC2, EXTRA, ibtn

C = Toggles()
PAGES = []
def P(key, nav, phase, html, solo=False):
    PAGES.append((key, nav, phase, solo, html))

def chips(items, on, cls='sm', group=None):
    return '<div class="chips">%s</div>' % ''.join(C.chip(x, i in on, group, cls) for i, x in enumerate(items))
def selx(options, cur, label):
    o = ''.join('<option%s>%s</option>' % (' selected' if x == cur else '', x) for x in options)
    return '<label class="sel"><span class="sr-only">%s</span><select class="ds-in">%s</select>%s</label>' % (label, o, ic('down', 16, 2))
def card(title, body, cls='', right='', t='', sub=''):
    return '<section class="ds-card fc%s"><div class="fc-h"><div><h2>%s%s</h2>%s</div>%s</div>%s</section>' % (
        (' ' + cls) if cls else '', title, tip(t) if t else '', ('<p>%s</p>' % sub) if sub else '', right, body)
def back_btn(note=''):
    return '<div class="ds-acts sb sv"><span class="sv-s">%s</span><span class="sv-r">%s</span></div>' % (note, btn('Back to Curriculum', 'STU-020.dc.html'))
def wk(main, actions, rail):
    return '<div class="wk"><div class="wk-m">%s</div>%s<aside class="wk-r">%s</aside></div>' % (main, actions.replace('class="ds-acts sb sv"', 'class="ds-acts sb sv wk-a"'), rail)
def tiles(items):
    return '<div class="st4">%s</div>' % ''.join('<span class="st-t%s"><b>%s</b><em>%s</em></span>' % ((' ' + k) if k else '', v, l) for v, l, k in items)

ICO = {'🎥': 'video', '📖': 'text', '📝': 'quiz', '✨': 'inter', '🛠': 'practice', '🔴': 'live', '📋': 'assign', '🚀': 'project'}
def iti(kind, size=16):
    return '<span class="it-i sm k-%s">%s</span>' % (kind, ic(ITEM_IC2[kind], size))

# ---------------------------------------------------------------- CR-STU-026 Course Resource Library
RES = [
    ('file', 'Data Analysis Handbook.pdf', 'Documents', '1 place', '', [('Chapter', 'Chapter 1 · Introduction to Data Analysis', 0, 1, 'Always')]),
    ('table', 'Course Worksheet.xlsx', 'Templates', '1 place', '', [('Chapter', 'Chapter 1 · Introduction to Data Analysis', 0, 1, 'Always')]),
    ('file', 'SQL Joins Cheat Sheet.pdf', 'Documents', '2 places', '', [('Chapter', 'Chapter 3 · Joining Tables', 0, 1, 'Always'), ('Item', 'Joining Tables with SQL (Ch 3)', 0, 1, 'During lesson')]),
    ('table', 'Practice Dataset.csv', 'Datasets', '2 places', '', [('Chapter', 'Chapter 3 · Joining Tables', 0, 1, 'Always'), ('Item', 'Practice Joins (Ch 3)', 0, 0, 'Before lesson')]),
    ('file', 'Exercise Instructions.pdf', 'Documents', '1 place', '', [('Item', 'Practice Joins (Ch 3)', 0, 0, 'Before lesson')]),
    ('download', 'retail-dataset.zip', 'Datasets', '1 place', '', [('Item', 'Final Project (Ch 5)', 0, 0, 'Before lesson')]),
    ('link', 'PostgreSQL documentation', 'Links', '1 place', 'postgresql.org/docs', [('Course', 'Whole course', 1, 1, 'Always')]),
    ('course', 'The Data Warehouse Toolkit (Kimball & Ross)', 'References', '1 place', '', [('Course', 'Whole course', 1, 1, 'Always')]),
]
RIGHTS = ['Select rights', 'Created by me', 'Licensed (third-party)', 'Open licence', 'Public domain', 'Cited reference', 'External link']
VIS = ['Always', 'Before lesson', 'During lesson', 'After completion']
TARGETS = ['Choose where…', 'Whole course'] + ['Chapter %d · %s' % (i + 1, c[0]) for i, c in enumerate(stu2.CH)] + \
    ['%s (Ch %d)' % (it[1], i + 1) for i, c in enumerate(stu2.CH) for it in c[6]]
def res_card(r):
    icon, name, cat, used, src, att = r
    warn = name == 'retail-dataset.zip'
    rows = ''.join('<div class="at-r"><span class="at-l">%s<b>%s</b></span>%s%s%s<a class="ds-link sm" href="#">Detach</a></div>' % (
        tag(lv.upper(), 'line'), tgt, C.seg(['Download', 'View only'], dl), C.seg(['Required', 'Optional'], rq), selx(VIS, vis, 'Visibility')) for lv, tgt, dl, rq, vis in att)
    return ('<section class="ds-card rc%s"><header class="rc-h"><span class="rc-i">%s</span><span class="rc-t"><b>%s</b><span>%s · used in %s · v 1</span></span>%s<button type="button" class="ds-ghost sm">Upload new version</button></header>'
            '<div class="fg fg3">%s%s%s</div><div class="at">%s</div><div class="rc-f"><span class="fl-l">Attach to</span>%s<button type="button" class="ds-ghost sm">Attach</button></div></section>') % (
        ' warn' if warn else '', ic(icon, 18), name, cat, used, tag('Needs rights', 'amber') if warn else '',
        field('Description', '<input class="ds-in" placeholder="Description learners see" aria-label="Description">'),
        field('Source or licence', '<input class="ds-in"%s placeholder="Source (optional)" aria-label="Source or licence">' % ((' value="%s"' % src) if src else '')),
        field('Rights', selx(RIGHTS, 'Select rights', 'Rights for ' + name)), rows, selx(TARGETS, 'Choose where…', 'Attach to'))
def res_row(r, on=False):
    icon, name, cat, used, src, att = r
    warn = name == 'retail-dataset.zip'
    a = ''.join('<span class="rr-a">%s<span>%s</span><em>%s · %s · %s</em></span>' % (
        tag(lv.upper(), 'line'), tgt, ['Download', 'View only'][dl], ['Required', 'Optional'][rq], vis) for lv, tgt, dl, rq, vis in att)
    return ('<a class="rr%s%s" href="#"%s><span class="rc-i">%s</span><span class="rr-b"><span class="rr-t"><b>%s</b>%s</span><span class="rr-m">%s · used in %s · v 1%s</span><span class="rr-as">%s</span></span><span class="rr-go">%s</span></a>') % (
        ' on' if on else '', ' warn' if warn else '', ' aria-current="true"' if on else '', ic(icon, 18), name, tag('Needs rights', 'amber') if warn else '', cat, used, (' · ' + src) if src else '', a, ic('chev', 16, 2))
P('res', 'res', 'Build', page_head('Build', 'Course Resource Library', 'Upload once, attach anywhere: to the whole course, a chapter, or a single learning item. Each attachment controls download, requirement and when learners see it.',
    '<a class="ds-ghost sm" href="#">%s<span>Upload</span></a><a class="ds-ghost sm" href="#">%s<span>Add link</span></a>' % (ic('upload', 16, 2), ic('plus', 16, 2.2))) +
  '''<section class="ds-card flt ob-in2"><div class="flt-l"><span class="fl-l">Level</span>%s</div>%s</section>
<div class="wn ob-in2">%s<span>1 resource needs rights or source information: <b>retail-dataset.zip</b>.</span></div>
<div class="rlw ob-in3"><div class="ds-card rl-l">%s</div><div class="rl-d">%s</div></div>''' % (
      C.seg(['All levels', 'Course', 'Chapter', 'Item'], 0),
      chips(['All (8)', 'Documents (3)', 'Templates (1)', 'Datasets (2)', 'Downloads (0)', 'Links (1)', 'References (1)', 'Source materials (0)'], {0}, group='rcat'),
      ic('warn', 16, 2), ''.join(res_row(r, i == 0) for i, r in enumerate(RES)), res_card(RES[0])) +
  acts('STU-027.dc.html', note='Downloadable, required and visibility are set per attachment, so the same dataset can be optional in a lesson but required in a project.%s' % tip('Validators review rights for anything you didn’t create.')))

# ---------------------------------------------------------------- CR-STU-027 Completion Rules
RULES = {
    'video': ['Choose a rule…', 'Open the lesson', 'Watch ≥ 70%', 'Watch ≥ 90%', 'Watch to the end'],
    'text': ['Choose a rule…', 'Reach the end', 'Mark as complete', 'Minimum active time'],
    'inter': ['Choose a rule…', 'Complete the activity', 'Open'],
    'practice': ['Choose a rule…', 'Submit', 'Mark as complete'],
    'live': ['Choose a rule…', 'Attend ≥ 50%', 'Attend ≥ 70%', 'Attend ≥ 80%', 'Attend ≥ 90%'],
    'assign': ['Choose a rule…', 'Submit', 'Receive a passing evaluation'],
    'project': ['Choose a rule…', 'Submit', 'Pass the rubric'],
}
def rule_opts(it):
    kind, title, typ = it[0], it[1], it[2]
    if kind == 'quiz':
        if typ.startswith('Quiz'): return ['Choose a rule…', 'Submit', 'Achieve ≥ 70%']
        if typ.startswith('Exam'): return ['Choose a rule…', 'Pass']
        return ['Choose a rule…', 'Submit']
    return RULES[kind]
def cr_item(it):
    kind, title, typ, tier, dur, dlp, comp, req = it[:8]
    opts = rule_opts(it)
    cur = comp.replace('Complete: ', '') if comp else 'Choose a rule…'
    short = typ.split(' · ')[0]
    meta = ('<span class="it-warn">%s<span>Required item with no completion rule</span></span>' % ic('warn', 13, 2.2)) if comp is None else '<span>%s · recommended: %s</span>' % (short, cur)
    return ('<div class="cr%s">%s<div class="cr-b"><b>%s</b><div class="it-m">%s</div></div>%s%s</div>' %
            (' warn' if comp is None else '', iti(kind), title, meta, C.seg(['Required', 'Optional'], 0 if req else 1), selx(opts, cur, 'Completion rule for ' + title)))
def cr_chapter(ci, ch):
    nofm = ci == 1
    return ('<section class="ds-card fc crc"><div class="crc-h"><div><span class="ch-k">Chapter %d</span><h2>%s</h2></div><div class="crc-w"><span class="fl-l">Chapter complete when</span>%s%s</div></div>%s</section>' % (
        ci + 1, ch[0], C.seg(['All required items', 'N of M required'], 1 if nofm else 0),
        selx(['1 of 4', '2 of 4', '3 of 4', '4 of 4'], '3 of 4', 'Number of required items') if nofm else '', ''.join(cr_item(it) for it in ch[6])))
REQS = [(True, 'Complete all required lessons', '8 lessons'), (True, 'Pass all required assessments', '3 assessments'),
        (True, 'Submit required project', '4 projects and activities'), (False, 'Attend required live sessions', '0 live sessions')]
P('comp', 'comp', 'Build', page_head('Build', 'Completion Rules', 'When each learning item counts as complete, and what finishes a chapter. The Course Completion Engine uses these to calculate learner progress.') +
  '<div class="ob-in2">%s</div>' % tiles([('15', 'Required items', ''), ('1', 'Optional items', ''), ('1', 'Required items without a rule', 'amber')]) +
  '''<section class="ds-card fc ccr ob-in2"><div class="fc-h"><div><h2>Course completion requirements%s</h2></div></div><div class="ccr-g">%s</div></section>
<div class="ob-in3">%s</div>''' % (
      tip('These requirements determine when Credalio marks the learner’s course as Complete. They connect to certificates, the Learning Achievement Score and verified completion. Optional items never block progress.'),
      ''.join('<div class="ccr-r%s"><span class="ccr-i">%s</span><b>%s</b><span>%s</span></div>' % ('' if on else ' off', ck(12) if on else '—', t, d) for on, t, d in REQS),
      ''.join(cr_chapter(ci, ch) for ci, ch in enumerate(stu2.CH))) +
  back_btn('Rules are kept deliberately simple for now: “complete all required items” or “complete N of M required”.%s' % tip('Recommended defaults, such as 70% viewing for video, are suggestions within Credalio policy, not forced.')))

# ---------------------------------------------------------------- CR-STU-028 Team & Assignments (+ my work)
STATUS_C = {'Complete': 'green', 'In progress': 'blue', 'Needs review': 'amber', 'Not started': ''}
ST_OPTS = ['Not started', 'In progress', 'Needs review', 'Complete']
# (chapter lead options, lead) + items (assigned set, status, due)
ASG = [
    (['No lead', 'Ada', 'John'], 'Ada', [({'Ada'}, 'Complete', '✓'), ({'Ada'}, 'Complete', '✓'), ({'Ada'}, 'Complete', '✓')]),
    (['No lead', 'John'], 'John', [({'John'}, 'Complete', '✓'), ({'John'}, 'Needs review', 'Oct 3'), ({'John'}, 'Not started', 'Oct 5'), ({'Ada'}, 'In progress', 'Oct 6')]),
    (['No lead', 'John', 'Ada'], 'John', [({'John'}, 'Complete', '✓'), ({'Ada', 'John'}, 'In progress', 'Oct 4'), ({'John'}, 'Not started', 'Oct 6')]),
    (['No lead', 'Ada', 'ABC Institute'], 'Ada', [({'Ada'}, 'Complete', '✓'), ({'ABC'}, 'Not started', 'Oct 16'), ({'Ada'}, 'Not started', 'Oct 9')]),
    (['No lead', 'Ada'], 'Ada', [({'Ada'}, 'Complete', '✓'), ({'Ada'}, 'In progress', 'Oct 12'), ({'Ada', 'John'}, 'Not started', 'Oct 7')]),
]
def st_sel(cur, label):
    return '<span class="sts %s">%s</span>' % (STATUS_C[cur], selx(ST_OPTS, cur, label))
def asg_table(solo=False):
    h = '<div class="tb%s"><div class="tb-r tb-hd"><span>Learning item</span>%s<span>Status</span><span>Due</span></div>' % (' solo' if solo else '', '' if solo else '<span>Assigned</span>')
    for ci, ch in enumerate(stu2.CH):
        lopts, lead, rows = ASG[ci]
        h += '<div class="tb-g"><b>Chapter %d · %s</b>%s</div>' % (ci + 1, ch[0], '' if solo else '<span class="tb-lead"><span>Chapter lead</span>%s</span>' % selx(lopts, lead, 'Chapter lead'))
        for ii, it in enumerate(ch[6]):
            who, st, due = rows[ii]
            extra = ''
            if not solo and it[0] == 'live':
                extra = '<span class="tb-ins"><span>Instructor</span>%s</span>' % selx(['Ada', 'John', 'ABC Institute'], 'ABC Institute', 'Instructor')
            asg = '' if solo else '<span class="tb-a">%s%s</span>' % (''.join(C.chip(n, n in who, cls='xs') for n in ['Ada', 'John', 'ABC']), extra)
            h += '<div class="tb-r"><span class="tb-it"><em>%d</em>%s<b>%s</b></span>%s%s<span class="tb-d%s">%s</span></div>' % (
                ci + 1, iti(it[0], 15), it[1], asg, st_sel(st, 'Status'), ' ok' if due == '✓' else '', due)
    return h + '</div>'
PEOPLE = [((ME, 'A'), 'Ada', 'Owner / Lead Creator', 10, 5, 'INNER vs LEFT JOIN · due Oct 4'), ((M1, 'J'), 'John', 'Co-Creator', 7, 2, 'SELECT Statements · due Oct 3'),
          ((None, 'AB'), 'ABC Institute', 'Content Contributor', 1, 0, 'Analysis Clinic · due Oct 16')]
def person(p, n, role, a, c, nxt, label=None):
    return ('<div class="ds-card pc">%s<div class="pc-b"><b>%s</b><span>%s</span></div><div class="pc-p"><span>%s</span><span class="ef-pb"><i style="width: %d%%"></i></span></div><p class="pc-n">Next: %s</p></div>' % (
        av(p[0], p[1], 44), n, role, label or '%d assigned · %d complete' % (a, c), int(100 * c / a) if a else 0, nxt))
TEAM_SUB = 'Who is building what. Assign at chapter or item level. Assignment is work, not ownership: ownership, permissions, assignment and revenue share stay separate.'
def team_tabs(cur):
    t = [('STU-028.dc.html', 'users', 'Team progress'), ('STU-029.dc.html', 'assigned', 'My assigned work')]
    return '<nav class="utabs ob-in2" aria-label="Team views">%s</nav>' % ''.join(
        '<a href="%s" class="ut%s"%s>%s<span>%s</span></a>' % (h, ' on' if k == cur else '', ' aria-current="page"' if k == cur else '', ic(i, 16, 2), l) for k, (h, i, l) in enumerate(t))
HIST = [('Tue 14:30', 'Ada removed John from “Aggregations and GROUP BY” · authorship and activity history kept'), ('Mon 09:05', 'Ada made John Chapter 2 lead'),
        ('Mon 09:02', 'Ada assigned John to Chapter 2 “SQL Foundations”')]
P('team', 'team', 'Build', page_head('Build', 'Team & Assignments', TEAM_SUB) + team_tabs(0) +
  '<div class="pcs ob-in2">%s</div>' % ''.join(person(*x) for x in PEOPLE) +
  wk('<section class="ds-card fc ob-in3">%s</section>' % asg_table(), acts('STU-031.dc.html'),
     card('Course-level assignment', chips(['Ada', 'John', 'ABC Institute'], {0}), sub='People assigned to the whole course (for example, reviewing every chapter).', cls='rx ob-in3') +
     card('Assignment history', '<ul class="hs">%s</ul>' % ''.join('<li><em>%s</em><span>%s</span></li>' % x for x in HIST), t='Changing an assignment never erases authorship or activity history.', cls='rx ob-in4')))

MYW = [('inter', 'SELECT Statements', 'Chapter 2 · Interactive', 'Needs review', 'Oct 3'), ('text', 'INNER vs LEFT JOIN', 'Chapter 3 · Text / Article', 'In progress', 'Oct 4'),
       ('practice', 'Your First Queries', 'Chapter 2 · Practice Activity', 'Not started', 'Oct 5'), ('practice', 'Practice Joins', 'Chapter 3 · Practice Activity', 'Not started', 'Oct 6'),
       ('quiz', 'Final Exam', 'Chapter 5 · Exam', 'Not started', 'Oct 7')]
def my_summary(who='Ada'):
    cnt = {k: 0 for k in ST_OPTS}
    for _, _, rows in ASG:
        for w, st, _ in rows:
            if who == 'Ada' or who in w:
                cnt[st] += 1
    tot = sum(cnt.values())
    order = ['Complete', 'In progress', 'Needs review', 'Not started']
    bar = ''.join('<i class="%s" style="flex: %d"></i>' % (STATUS_C[k] or 'grey', cnt[k]) for k in order)
    cells = ''.join('<span class="ms-c %s"><i></i><b>%d</b><em>%s</em></span>' % (STATUS_C[k] or 'grey', cnt[k], k) for k in order)
    return ('<section class="ds-card ms ob-in2"><div class="ms-me">%s<span><b>%s</b><em>%s</em></span></div>'
            '<div class="ms-rg">%s<span><b>%d</b><em>of %d</em></span></div>'
            '<div class="ms-st"><span class="ms-l">%s</span><span class="ms-bar">%s</span><div class="ms-cs">%s</div></div>'
            '<a class="ms-nx" href="#"><span class="ms-l">Next</span><b>SELECT Statements</b><em>due Oct 3</em><span class="ms-go">%s</span></a></section>') % (
        av(ME, 'A', 52) if who == 'Ada' else av(M1, 'J', 52), who, 'You · Owner' if who == 'Ada' else 'Co-Creator',
        ring(round(100 * cnt['Complete'] / tot), 92, 11), cnt['Complete'], tot,
        ('%d lessons · %d complete' if who == 'Ada' else '%d assigned · %d complete') % (tot, cnt['Complete']), bar, cells, ic('arrowr', 16, 2.2))

P('mywork', 'team', 'Build', page_head('Build', 'My Assigned Work', TEAM_SUB) + team_tabs(1) + my_summary('John') +
  '<section class="ds-card mw ob-in3"><header class="mw-h"><span class="mw-who"><b>Viewing as Dr. John Adeyemi</b></span>%s</header>%s</section>' % (
      chips(['All curriculum', 'My assigned work', 'Needs review', 'Completed'], {1}, group='mwf'), ''.join(
      '<div class="mw-r">%s<div class="mw-b"><b>%s</b><span>%s · %s</span></div>%s<span class="mw-d">Due %s</span><a class="ds-ghost xs" href="#">Open</a></div>' % (
          iti(k, 17), t, m, s, tag(s, STATUS_C[s]), d) for k, t, m, s, d in MYW)))

P('mysolo', 'team', 'Build', page_head('Build', 'My Work', 'Your plan for this course: what is done, what is in progress and what is due. You are the only creator, so every lesson is yours. If you invite co-creators later, assignments appear here.') +
  my_summary() +
  '<section class="ds-card fc ob-in3">%s</section>' % asg_table(True) + acts('STU-031.dc.html'), solo=True)

# ---------------------------------------------------------------- CR-STU-031 DLP & Learning Effort
EST = [('Structured learning', '2h 15m', 215), ('Practice', '1h 40m', 165), ('Assessment', '1h 10m', 115), ('Projects', '2h', 200), ('Live', '1h', 100)]
BYCH = [('Chapter 1 · Introduction to Data Analysis', '40m', 60), ('Chapter 2 · SQL Foundations', '1h 23m', 135), ('Chapter 3 · Joining Tables', '58m', 90),
        ('Chapter 4 · Analysing Business Data', '2h 5m', 210), ('Chapter 5 · Communicating Findings', '2h 59m', 300)]
BYTY = [('Project', '2h', 200), ('Video', '1h 20m', 135), ('Live Class', '1h', 100), ('Practice Activity', '55m', 90), ('Assignment', '45m', 75), ('Exam', '45m', 75),
        ('Interactive', '22m', 35), ('Text + PDF', '18m', 25), ('Quiz', '15m', 25), ('Text / Article', '15m', 20), ('Knowledge Check', '10m', 15)]
SEGC = ['#1652F0', '#5C86FF', '#9DB8F7', '#0B1433', '#C9D7FA']
def bars(rows, mx):
    return '<div class="bl">%s</div>' % ''.join('<div class="bl-r"><span class="bl-n">%s</span><span class="bl-b"><i style="width: %d%%"></i></span><span class="bl-v"><b>%s</b>%d DLP</span></div>' % (
        n, max(3, round(100 * d / mx)), t, d) for n, t, d in rows)
P('dlp', 'dlpe', 'Build', page_head('Build', 'DLP & Learning Effort', 'System-calculated learning time and estimated DLP across the whole curriculum, compared with the effort you intended in Course Design.') +
  '<div class="ob-in2">%s</div>' % tiles([('8h 5m', 'Calculated learning time', ''), ('795 DLP', 'Estimated DLP', ''), ('26h', 'Intended in Course Design (018)', ''), ('31%', 'Built so far vs intended', '')]) +
  '''<section class="ds-card fc ob-in3"><div class="fc-h"><div><h2>Current course estimate%s</h2></div></div>
<div class="sb4">%s</div><div class="lg5">%s</div>
<div class="tot"><span>Estimated learning effort</span><b>8h 5m</b><b class="tot-d">%s ~ 795 DLP</b></div></section>
<div class="g2 dl2 ob-in3"><div class="dl2-l">%s%s</div>%s</div>
<section class="ds-card fc ex ob-in4"><div class="fc-h"><div><h2>Estimated DLP is not DLP consumed</h2></div></div><div class="ex-g">
<div><span class="pg-e">Estimated course DLP · 795 DLP</span><p>Calculated here, in Creator Studio, from each item’s duration, reading time or expected effort. It’s the starting point for DLP Access at publication.</p></div>
<div><span class="pg-e">DLP consumed by learners</span><p>Decided on the learner side by the access and use policy [TO CONFIRM]. It can differ from the estimate, for example when optional items are skipped.</p></div></div>
<a class="ds-link" href="#">See how it’s used in DLP Access%s</a></section>''' % (
      tip('Runs continuously as you build. The exact calculation follows Credalio’s DLP policy [TO CONFIRM]. This estimate sets the permitted price range; it isn’t your price.'),
      ''.join('<i style="flex: %d; background: %s" title="%s"></i>' % (d, SEGC[i], n) for i, (n, t, d) in enumerate(EST)),
      ''.join('<span><i style="background: %s"></i><b>%s</b><em>%s · %d DLP</em></span>' % (SEGC[i], n, t, d) for i, (n, t, d) in enumerate(EST)), coin(),
      card('By chapter', bars(BYCH, 300)), nova_sg('Your curriculum currently adds up to 8h 5m, but you planned about 26 hours in Course Design. Either the curriculum is still growing, or the plan needs updating.'),
      card('By type of learning', bars(BYTY, 200)), ic('arrowr', 15, 2.2)) +
  back_btn())

# ---------------------------------------------------------------- Course Assessments (management view)
ASM = [('Knowledge Check', 'Knowledge Check', '1', '5', 'Yes', '—'), ('Quiz 1', 'Quiz', '2', '10', 'Yes', '70%'), ('Final Exam', 'Exam', '5', '20', 'Yes', '75%')]
COV = [('Knowledge Check', 'Knowledge Check', '5', [1, 0, 0, 0]), ('Quiz 1', 'Quiz', '10', [1, 0, 0, 0]), ('Final Exam', 'Exam', '20', [1, 1, 0, 0]),
       ('Final Project', 'Project', '—', [0, 1, 1, 0]), ('Your First Queries', 'Practice', '—', [1, 0, 0, 0])]
P('assess', 'alla', 'Build', page_head('Build · Management view', 'Course Assessments', 'Every assessment already created in the curriculum, in one place. You don’t build assessments here: add them as learning items in the Curriculum. Clicking one takes you back to its place there.') +
  '''<section class="ds-card tbl ob-in2"><div class="tbl-r tbl-hd"><span>Assessment</span><span>Type</span><span>Chapter</span><span>Questions</span><span>Required</span><span>Pass</span><span></span></div>%s</section>
<section class="ds-card fc ob-in3"><div class="fc-h"><div><h2>Outcome coverage</h2></div></div>
<div class="cv"><div class="cv-r cv-hd"><span>Assessment</span><span>Type</span><span>Questions</span><span>LO1</span><span>LO2</span><span>LO3</span><span>LO4</span><span></span></div>%s</div>
<div class="wn">%s<span>LO4 has no assessment evidence yet.</span></div></section>''' % (
      ''.join('<div class="tbl-r">%s<span>%s</span><span>%s</span><span>%s</span><span>%s</span><span>%s</span><a class="ds-link sm" href="STU-020.dc.html">Show in Curriculum%s</a></div>' % (
          '<span class="tbl-n">%s<b>%s</b></span>' % (iti('quiz', 15), a), t, c, q, r, p, ic('arrowr', 14, 2.2)) for a, t, c, q, r, p in ASM),
      ''.join('<div class="cv-r"><b>%s</b><span>%s</span><span>%s</span>%s<a class="ds-link sm" href="#">Edit</a></div>' % (
          a, t, q, ''.join('<span class="cv-c%s">%s</span>' % (' on' if v else '', ck(11) if v else '') for v in cells)) for a, t, q, cells in COV),
      ic('warn', 16, 2)) + back_btn())

# ---------------------------------------------------------------- Practice & Projects
SKL = ['Select skill', 'SQL', 'Data Analysis', 'Data Cleaning', 'Relational Databases']
OUT = ['Select outcome', 'LO1 · Write SQL queries to retrieve and filter structu', 'LO2 · Combine multiple relational tables using joins.', 'LO3 · Analyse business datasets and communicate findin', 'LO4 · Understand SQL']
PRA = [('practice', 'Your First Queries', 'Practical exercise · Chapter 2', '5 working SELECT queries', 'Auto-checked results', 'SQL', OUT[1], 1),
       ('assign', 'Sales Analysis', 'Case study · Chapter 4', 'A written analysis of 3 sales questions', 'Tutor-marked against a rubric', 'Data Analysis', OUT[3], 0),
       ('project', 'Final Project', 'Project · Chapter 5', 'SQL analysis + 5-minute presentation', 'Rubric: data, analysis, communication', 'Data Analysis', OUT[0], 0)]
def pra_card(p):
    k, t, m, prod, ev, sk, oc, pol = p
    warn = oc == 'Select outcome'
    return ('<section class="ds-card fc pr%s"><div class="pr-h">%s<div><b>%s</b><span>%s</span>%s</div><div class="pr-pl"><span class="pr-plt"><b>Becomes Proof of Learning?</b>%s</span>%s</div></div><div class="fg fg2">%s%s%s%s</div></section>' % (
        ' warn' if warn else '', iti(k, 18), t, m, ('<span class="it-warn">%s<span>Still to set: outcome</span></span>' % ic('warn', 13, 2.2)) if warn else '',
        tip('Shown in the learner’s achievement record once passed.', 'r'), C.seg(['Yes', 'No'], pol),
        field('What will the learner produce?', '<input class="ds-in" value="%s" aria-label="What will the learner produce">' % prod),
        field('How is it evaluated?', '<input class="ds-in" value="%s" aria-label="How is it evaluated">' % ev),
        field('What skill does it demonstrate?', selx(SKL, sk, 'Skill demonstrated')), field('What outcome does it prove?', selx(OUT, oc, 'Outcome proved'))))
P('practice', 'alla', 'Build', page_head('Build', 'Practice & Projects', 'For each piece of practical work: what learners produce, which skill it demonstrates, which outcome it proves, how it’s evaluated, and whether it becomes Proof of Learning.') +
  '<div class="ob-in2">%s</div><div class="chips addp ob-in3">%s</div>' % (''.join(pra_card(p) for p in PRA), ''.join(
      '<button type="button" class="ds-chip add">%s<span>%s</span></button>' % (ic('plus', 14, 2.2), x) for x in ['Practical exercise', 'Project', 'Case study', 'Simulation', 'Portfolio work'])) +
  acts('STU-DEL.dc.html'))

# ---------------------------------------------------------------- Delivery & Schedule
P('deliv', 'deliv', 'Experience', page_head('Experience', 'Delivery & Schedule', 'Configure live sessions for your hybrid course.') + wk(
  card('Scheduling model', '<div class="fg">%s<div class="fg fg3">%s%s%s</div></div>' % (
      C.seg(['Cohort', 'Recurring availability'], 0),
      field('Capacity per session', '<input class="ds-in" value="25" aria-label="Capacity per session">'),
      field('Time zone', '<input class="ds-in" value="WAT (UTC+1)" aria-label="Time zone">'),
      field('Instructor', '<input class="ds-in" value="Ada Ononuju" aria-label="Instructor">')), cls='sch ob-in2') +
  card('Live sessions', '<div class="ls">%s<div class="ls-t"><b>Analysis Clinic</b><span>Thursdays · 6:00 PM</span></div>%s</div><button type="button" class="ch-add" style="width: 100%%">%s<span>Add live session</span></button>' % (
      '<span class="ls-d"><em>THU</em><b>6:00</b></span>', tag('60 min', 'line'), ic('plus', 16, 2.2)), cls='ob-in3') +
  card('Policies', '<div class="pol">%s%s%s</div>' % (
      field('Attendance requirement', C.seg(['Required', 'Recommended', 'Optional'], 1)),
      field('Recording policy', C.seg(['Recorded for enrolled learners', 'Not recorded'], 0)),
      field('Office hours', C.seg(['Weekly', 'Fortnightly', 'None'], 0))), cls='ob-in3'),
  acts('STU-LX.dc.html'),
  nova_rail('Detected split: <b>88 % self-paced · 12 % instructor-led</b>. Saved to your course profile.',
            '<span class="spr">%s<span class="spr-l"><span><i></i><b>88 %%</b><em>self-paced</em></span><span><i class="n"></i><b>12 %%</b><em>instructor-led</em></span></span></span>' % ring(88, 96, 13, track='#0B1433'))))

# ---------------------------------------------------------------- Learner Experience
P('lx', 'lx', 'Experience', page_head('Experience', 'Learner Experience', 'How learners move through the course, and what counts as completing it.') +
  wk(card('Course navigation', '<div class="opt2 nvo">%s%s</div>' % (
      C.opt('<span class="nvz seq" aria-hidden="true"><i class="d"></i><i></i><i></i><i></i></span><span class="o-t"><b>Sequential</b></span>', True, 'nav'),
      C.opt('<span class="nvz flx" aria-hidden="true"><i class="d"></i><i></i><i></i><i></i></span><span class="o-t"><b>Flexible</b></span>', False, 'nav')), cls='ob-in2') +
  card('Completion requirements', '<div class="fg lxc">%s<div class="lxs">%s%s</div></div>' % (
      chips(['Complete all lessons', 'Pass assessments', 'Submit final project'], {0, 1}, cls=''),
      field('Minimum score', '<span class="pct-w"><input class="ds-in pct" type="number" value="70" aria-label="Minimum score"><em>%</em></span>'),
      field('Minimum score applies to', C.seg(['Each assessment', 'Final exam only', 'Overall average'], 0), 'Assessment requirements for completion')), cls='ob-in3'),
  acts('STU-SUP.dc.html'),
  '<section class="ds-card rx lxp ob-in3"><span class="rx-k">Course navigation · Sequential</span><ol>%s</ol></section>' % ''.join(
      '<li class="%s" style="--i: %d"><span class="lxp-d">%s</span><span><em>Chapter %d</em><b>%s</b></span></li>' % (
          ['dn', 'on', 'lk', 'lk', 'lk'][i], i, [ck(11), str(i + 1), ic('lock', 12, 2), ic('lock', 12, 2), ic('lock', 12, 2)][i], i + 1, c[0]) for i, c in enumerate(stu2.CH))))

# ---------------------------------------------------------------- Learner Support
def sup(t, tagt, d, on, k):
    kk = C.new(on)
    return '<button type="button" class="sp {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}"><span class="sp-t"><b>%s</b>%s<span>%s</span></span><span class="tg-s"><i></i></span></button>' % (
        kk, kk, kk, t, tag(tagt, 'green' if tagt == 'ENABLED' else ''), d)
FLOW = ['Learner question', 'AI Coach', 'Tutor', 'Answered · logged in Manage']
P('support', 'lx', 'Experience', page_head('Experience', 'Learner Support', 'How can learners get help? These settings connect to the course chat, tutor escalation and Manage → Learner Questions.') +
  wk('<section class="ds-card sps lst ob-in2">%s</section>' % ''.join([
      sup('AI Coach', 'ENABLED', 'Answers learner questions 24/7 using your course content. It cites the lesson it drew from.', True, 1),
      sup('Ask Tutor', 'ENABLED', 'Learners send a question to a human tutor from any lesson.', True, 2),
      sup('AI → Tutor escalation', 'ENABLED', 'When the AI Coach can’t resolve a question, it hands over to a tutor with the conversation attached.', True, 3),
      sup('Course Discussion', 'ENABLED', 'Public Q&A between learners and creators, separate from private support.', True, 4),
      sup('Office Hours', 'OPTIONAL', 'Scheduled live drop-in sessions with the creator team.', False, 5)]) +
  card('Tutor requests', '<div class="fg fg3">%s%s%s</div>' % (
      field('Who answers', selx(['Lead Creator', 'All co-creators', 'Assigned instructors'], 'All co-creators', 'Who answers tutor requests')),
      field('Response target', selx(['Within 24 hours', 'Within 48 hours', 'Within 72 hours'], 'Within 24 hours', 'Response target')),
      field('Office hours', selx(['Off', 'Weekly', 'Fortnightly'], 'Off', 'Office hours frequency'))), cls='ob-in4'),
  acts('STU-032.dc.html'),
  '<section class="ds-card rx flw v ob-in3"><ol>%s</ol></section>' % ''.join('<li style="--i: %d"><span class="flw-d">%d</span><b>%s</b></li>' % (i, i + 1, x) for i, x in enumerate(FLOW))))

# ---------------------------------------------------------------- CR-STU-032 Course Access Model
PROC = ['Credalio measures', 'Credalio derives', 'you review and select', 'validation confirms', 'you publish']
COVER = '<span class="ax-cv"><i>SQL</i><b></b><b class="s"></b></span>'
def ax_vis(both):
    sub = '<span class="ax-p gold">%s<b>DLP</b><em>Subscription</em></span>' % coin()
    life = '<span class="ax-p blue">%s<b>Credits</b><em>Lifetime</em></span>' % credit()
    if both:
        return '<span class="ax-v two">%s%s<svg class="ax-l" viewBox="0 0 120 120" preserveAspectRatio="none" aria-hidden="true"><path d="M0 30 C60 30 60 60 120 60"></path><path d="M0 90 C60 90 60 60 120 60"></path></svg>%s</span>' % (sub, life, COVER)
    return '<span class="ax-v">%s<svg class="ax-l" viewBox="0 0 120 120" preserveAspectRatio="none" aria-hidden="true"><path d="M0 60 L120 60"></path></svg>%s</span>' % (sub, COVER)
def ax_card(both, title, desc, fields, on):
    inner = ('<span class="ax-vz" aria-hidden="true">%s</span><span class="ax-t"><b>%s</b><span>%s</span></span>'
             '<span class="ax-f">%s</span>') % (ax_vis(both), title, desc, ''.join('<span>%s%s</span>' % (ic_, f) for ic_, f in fields))
    return C.opt(inner, on, 'am', 'amc')
ACT = [('c', 'Credalio measures'), ('c', 'Credalio derives'), ('y', 'you review and select'), ('c', 'validation confirms'), ('y', 'you publish')]
P('access', 'price', 'Experience', page_head('Experience', 'Course Access Model', 'How should learners access this course? This decides which pricing fields appear next.') +
  '<div class="am ob-in2">%s%s</div>' % (
      ax_card(False, 'Subscription Only', 'Learners access this course using DLP from their Credalio subscription.', [(coin(), 'DLP price from a permitted range')], False),
      ax_card(True, 'Subscription + Marketplace', 'Learners can access it through their subscription, or buy lifetime course access with Marketplace Credits.',
              [(coin(), 'DLP price'), (credit(), 'Credit price'), (ic('settings', 14, 2), 'Maintenance burden')], True)) +
  '<section class="ds-card ax-pr ob-in3"><ol>%s</ol><p>%s<span>You won’t type a price anywhere: you choose from ranges Credalio generates.</span></p></section>' % (
      ''.join('<li class="%s"><span class="ax-d">%s</span><b>%s</b></li>' % (k, av(ME, 'AO', 34) if k == 'y' else '<i class="ax-m"></i>', x) for k, x in ACT), ic('lock', 15, 2)) +
  acts('STU-033.dc.html', 'Continue to Maintenance Burden'))

# ---------------------------------------------------------------- CR-STU-033 Maintenance Burden
KNOWN = ['Topic: SQL and data analysis, in Technology · Data & Analytics', 'The course links to PostgreSQL documentation and uses SQL tooling',
         '2 datasets in the Resource Library', '3 assessments and 1 project that reference specific data and tools']
QS = [('How often is this subject likely to need material updates?', ['Rarely', 'Every year or two', 'Several times a year'], 1),
      ('Does the course depend on external software or platforms?', ['No', 'Yes, stable tools', 'Yes, fast-changing tools'], 2),
      ('Could changes in regulation or professional standards affect the content?', ['No', 'Possibly', 'Yes'], 0),
      ('Do assessments or resources need regular updating?', ['No', 'Occasionally', 'Regularly'], 1)]
P('maint', 'price', 'Experience', page_head('Experience', 'Maintenance Burden', 'How much ongoing upkeep this course needs. Credalio assesses it from what it already knows and a few guided questions. It feeds Marketplace Credit pricing.') +
  card('What Credalio already knows', '<ul class="kn">%s</ul>' % ''.join('<li><span>%s</span>%s</li>' % (ck(11), k) for k in KNOWN), cls='ob-in2') +
  '<section class="ds-card fc ob-in3">%s</section>' % ''.join('<div class="mq"><b>%s</b>%s</div>' % (q, C.seg(o, s)) for q, o, s in QS) +
  '''<section class="ds-card mb ob-in4"><div class="mb-g"><span class="pg-e">Maintenance burden</span><div class="mb-m"><i class="on"></i><i class="on"></i><i></i></div><b>Medium</b>%s</div>
<p>This course relies on software and tools that may change, and is expected to need periodic content and resource updates.</p>
<div class="mb-a"><button type="button" class="ds-ghost sm">%s<span>Confirm</span></button><a class="ds-link sm" href="#">Request review</a></div></section>''' % (tag('Not confirmed yet', 'amber'), ck(13)) +
  acts('STU-034.dc.html', 'Continue to Course Pricing'))

# ---------------------------------------------------------------- CR-STU-034 Course Pricing (+ update required)
WHY = ['Learning effort (8h 5m calculated)', 'Course structure', 'Assessment and practice requirements', 'Maintenance requirements (Medium)', 'Course characteristics', 'Other applicable marketplace factors']
def stops(vals, sel, coin_html, calc=None):
    lo, hi = int(vals[0]), int(vals[-1])
    mk = ''
    if calc is not None:
        mk = '<span class="pc-calc" style="left: %.1f%%"><i></i><em>%s</em></span>' % (100.0 * (calc - lo) / (hi - lo), 'Calculated %d' % calc)
    return ('<div class="pc-band"><span class="pc-tr"><i></i></span>%s</div><div class="pc-stops" style="--n: %d" role="group">%s</div>' % (
        mk, len(vals), ''.join('<button type="button" class="pc-stop%s" aria-pressed="%s">%s<b>%s</b></button>' % (
            ' on' if v == sel else '', 'true' if v == sel else 'false', coin_html, v) for v in vals)))
def pcard(kind, eyebrow, title, rng_label, rng_val, vals, sel, unit, calc=None, extra='', title_tip=''):
    coin_html = coin() if kind == 'gold' else credit()
    big = coin(True) if kind == 'gold' else credit(True)
    selv = ('<b>%s</b><em>%s</em>' % (sel, unit)) if sel else '<b class="no">Not selected</b>'
    return ('<section class="ds-card pcd %s"><header class="pc-h"><span class="pc-i">%s</span><div><span class="pg-e">%s</span><h2>%s</h2></div>'
            '<div class="pc-sel"><span>Selected%s</span><div>%s</div></div></header>'
            '<div class="pc-r"><span>%s</span><b>%s</b></div>%s%s</section>') % (
        kind, big, eyebrow, title, title_tip, selv, rng_label, rng_val, stops(vals, sel, coin_html, calc), extra)
def pricing(update):
    s_dlp, s_cr = ('700', '150') if update else (None, None)
    banner = ''
    if update:
        banner = ('<div class="bn bn-amb ob-in2"><span class="bn-i amb">%s</span><p><b>Pricing update required</b> Your course’s learning structure has changed significantly since pricing was selected. Previous DLP range: 500–700 DLP · Updated range: <b class="in">700–900 DLP</b>. Your price hasn’t been changed.</p>'
                  '<div class="bn-a"><a class="ds-ghost sm" href="#">Review Pricing</a></div></div>') % ic('warn', 18, 2)
    why = ('<details class="ds-card why"%s><summary><span class="why-i">%s</span><b>Why this range?</b>%s</summary><div class="why-b"><span class="fl-l">Based on:</span><ul>%s</ul><p>Credalio doesn’t publish its internal coefficients.</p><a class="ds-link sm" href="#">Learn about Credalio Pricing [link TO CONFIRM]</a></div></details>' % (
        '' if update else ' open', ic('bulb', 18, 2), ic('down', 15, 2.2), ''.join('<li>%s%s</li>' % (ck(10), w) for w in WHY)))
    note = '<section class="ds-card pn"><span class="pn-eq"><b>DLP estimate</b><i>≠</i><b>creator price</b></span><p>Calculated DLP is Credalio’s assessment of learning consumption. The permitted range comes from it, and you choose your price within that range.</p></section>'
    return (page_head('Experience', 'Course Pricing', 'Choose your price from the range Credalio permits for this course. Pricing is provisional now and confirmed before publication.') + banner +
            '<div class="pr-g ob-in3"><div class="pr-main">%s%s</div><aside class="pr-side">%s%s</aside></div>' % (
                pcard('gold', 'Subscription access', 'Calculated course DLP: 795 DLP', 'Credalio DLP range:', '700–900 DLP', ['700', '800', '900'], s_dlp, 'DLP', calc=795),
                pcard('blue', 'Lifetime marketplace access', '<a class="mbl" href="STU-033.dc.html">Maintenance burden: Medium %s</a>' % ic('chev', 14, 2.2),
                      'Allowed Marketplace range:', '130–210 Credits', ['130', '150', '170', '190', '210'], s_cr, 'Credits',
                      title_tip=tip('Marketplace Credits purchase lifetime access to this course under Credalio’s marketplace terms.', 'r')),
                why, note) +
            acts('STU-035.dc.html', 'Continue to summary'))
P('pricing', 'price', 'Experience', pricing(False))
P('pricingupd', 'price', 'Experience', pricing(True))

# ---------------------------------------------------------------- CR-STU-035 Access & Pricing Summary
P('psum', 'price', 'Experience', page_head('Experience', 'Access & Pricing Summary', 'What learners will be offered, pending validation.') +
  '''<section class="ds-card ps ps2 ob-in2">
<div class="ps-r"><span>Course access</span><b>Subscription + Marketplace</b></div>
<div class="ps-g"><div class="ps-c"><span>Subscription</span><b>%s800 DLP</b></div><div class="ps-c"><span>Lifetime access</span><b>%s170 Credits</b></div></div>
<div class="ps-r"><span>Maintenance burden</span><b>Medium · confirmed</b></div>
<div class="ps-r"><span>Pricing status</span>%s</div>
<p class="ps-n">Pricing status: Provisional. Final permitted pricing will be confirmed before publication.</p>
</section>''' % (coin(True), credit(True), tag('Provisional', 'amber')) +
  '<div class="ds-acts sb sv"><span class="sv-s"><a class="ds-ghost sm" href="STU-032.dc.html">Edit Access</a><a class="ds-ghost sm" href="STU-034.dc.html">Edit Pricing</a></span><span class="sv-r">%s</span></div>' % btn('Continue', '#'))

COURSE_CSS = stu2.EDITOR_CSS + r'''.ms{margin-top:22px;padding:22px 24px;display:grid;grid-template-columns:auto auto minmax(0,1fr) 230px;align-items:center;gap:28px}
.ms-me{display:flex;align-items:center;gap:14px;padding-right:28px;border-right:1.5px solid #F0F2F8}
.ms-me > span,.ms-rg > span{display:flex;flex-direction:column;gap:2px}
.ms-me b{font-size:17px;font-weight:600}
.ms-me em,.ms-rg em{font-style:normal;font-size:13px;color:#5B6582}
.ms-rg{position:relative;width:92px;height:92px}
.ms-rg > span{position:absolute;inset:0;align-items:center;justify-content:center}
.ms-rg b{font-size:26px;font-weight:600;letter-spacing:-0.02em;line-height:1}
.ms-st{display:flex;flex-direction:column;gap:10px;min-width:0}
.ms-l{font-size:12.5px;font-weight:500;color:#8A93AD}
.ms-bar{display:flex;gap:3px;height:8px}
.ms-bar i{border-radius:6px;transform-origin:left center;animation:ldGrow .9s cubic-bezier(.2,.8,.2,1) .2s both}
.ms-bar i.green,.ms-c.green i{background:#0F6B45}
.ms-bar i.blue,.ms-c.blue i{background:#1652F0}
.ms-bar i.amber,.ms-c.amber i{background:#E0A030}
.ms-bar i.grey,.ms-c.grey i{background:#CBD3E6}
.ms-cs{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px}
.ms-c{display:grid;grid-template-columns:8px auto;align-items:center;column-gap:8px;row-gap:1px}
.ms-c i{width:8px;height:8px;border-radius:50%}
.ms-c b{font-size:18px;font-weight:600}
.ms-c em{grid-column:2;font-style:normal;font-size:12.5px;color:#5B6582;white-space:nowrap}
.ms-nx{position:relative;align-self:stretch;display:flex;flex-direction:column;justify-content:center;gap:3px;padding:14px 48px 14px 18px;border-radius:16px;background:#F5F8FF;color:#0B1433;text-decoration:none;transition:background .2s ease}
.ms-nx:hover{background:#EAF0FF}
.ms-nx b{font-size:15.5px;font-weight:600}
.ms-nx em{font-style:normal;font-size:13px;color:#8A5A00;font-weight:500}
.ms-go{position:absolute;right:14px;top:50%;margin-top:-16px;width:32px;height:32px;border-radius:50%;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center;transition:transform .2s ease}
.ms-nx:hover .ms-go{transform:translateX(3px)}
@media (max-width: 1280px){.ms{grid-template-columns:auto auto minmax(0,1fr);}.ms-nx{grid-column:1 / -1}}
@media (max-width: 960px){
.ms{margin-top:18px;padding:18px 16px;grid-template-columns:minmax(0,1fr) auto;gap:16px}
.ms-me{padding-right:0;border-right:0}
.ms-rg,.ms-rg svg{width:72px;height:72px}
.ms-rg b{font-size:20px}
.ms-st{grid-column:1 / -1}
.ms-cs{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.ms-nx{grid-column:1 / -1;padding:12px 48px 12px 14px}
}
.it-i.sm{width:34px;height:34px;border-radius:10px}
.ds-seg button{white-space:nowrap}
button.ch-add{background:none;font-family:inherit;cursor:pointer}
.nv-sg p .spl{margin:10px 0 0 0}
.flt{margin-top:22px;padding:14px 18px;display:flex;flex-wrap:wrap;align-items:center;gap:12px 20px}
.flt-l{display:flex;align-items:center;gap:10px}
.flt .ds-seg button{padding:0 12px}
.wn{margin-top:14px;display:flex;align-items:center;gap:10px;padding:12px 16px;border-radius:14px;background:#FFF8EA;border:1.5px solid #F4DDAA;font-size:14px;color:#3A4566}
.wn svg{flex-shrink:0;color:#B76E00}
.wn b{font-weight:600;color:#0B1433}
.wn.info{background:#F5F8FF;border-color:#DCE5FB}
.wn.info svg{color:#1652F0}
.rlw{margin-top:16px;display:grid;grid-template-columns:minmax(0,1fr) 430px;gap:16px;align-items:start}
.rl-l{padding:8px}
.rr{position:relative;display:flex;align-items:flex-start;gap:14px;padding:14px 12px;border-radius:14px;color:#0B1433;text-decoration:none;transition:background .2s ease}
.rr + .rr{box-shadow:0 -1.5px 0 #F0F2F8}
.rr:hover{background:#F7F9FD}
.rr.on{background:#F5F8FF;box-shadow:inset 0 0 0 1.5px #1652F0}
.rr.on + .rr{box-shadow:none}
.rr.on .rc-i{background:#1652F0;color:#FFFFFF}
.rr.warn .rc-i{background:#FFF4E0;color:#B76E00}
.rr-b{flex:1;min-width:0;display:flex;flex-direction:column;gap:3px}
.rr-t{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.rr-t b{font-size:15px;font-weight:600}
.rr-t .ds-tag{height:22px;font-size:11.5px}
.rr-m{font-size:13px;color:#5B6582}
.rr-as{margin-top:6px;display:flex;flex-direction:column;gap:4px}
.rr-a{display:flex;align-items:center;gap:8px;min-width:0;font-size:13px;color:#3A4566}
.rr-a .ds-tag{height:20px;padding:0 7px;font-size:10.5px;flex-shrink:0}
.rr-a > span:not(.ds-tag){font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0}
.rr-a em{font-style:normal;color:#8A93AD;white-space:nowrap;flex-shrink:0}
.rr-go{align-self:center;color:#AEB6CC;display:flex}
.rr.on .rr-go{color:#1652F0}
.rl-d{position:sticky;top:92px}
.rl-d .rc{padding:20px;border-color:#C9D7FA;box-shadow:0 24px 40px -32px rgba(22,82,240,.55)}
.rl-d .rc-h{flex-wrap:wrap;row-gap:12px}
.rl-d .rc-h .ds-ghost{width:100%;justify-content:center}
.rl-d .fg3{grid-template-columns:minmax(0,1fr);gap:14px}
.rl-d .at-r{grid-template-columns:minmax(0,1fr) auto;gap:10px}
.rl-d .at-l{grid-column:1 / -1}
.rl-d .at-r .ds-seg{width:100%;box-sizing:border-box}
.rl-d .at-r .sel{grid-column:1}
.rl-d .rc-f{grid-template-columns:minmax(0,1fr) auto}
.rl-d .rc-f .fl-l{grid-column:1 / -1}
.rc{padding:18px 20px}
.rc.warn{border-color:#F4DDAA}
.rc-h{display:flex;align-items:center;gap:14px;margin-bottom:14px}
.rc-i{width:40px;height:40px;flex-shrink:0;border-radius:12px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.rc-t{flex:1;min-width:0;display:flex;flex-direction:column;gap:2px}
.rc-t b{font-size:15.5px;font-weight:600}
.rc-t span{font-size:13px;color:#5B6582}
.at{margin-top:14px;display:flex;flex-direction:column;gap:8px}
.at-r{display:grid;grid-template-columns:minmax(0,1fr) auto auto 180px auto;align-items:center;gap:12px;padding:10px 12px;border-radius:12px;background:#F7F9FD}
.at-l{display:flex;align-items:center;gap:10px;min-width:0}
.at-l b{font-size:14px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.at-r .ds-seg{background:#EBEEF5}
.at-r .ds-seg button{height:32px;font-size:12.5px;padding:0 10px}
.at-r .ds-in{height:40px;font-size:13.5px}
.rc-f{margin-top:12px;display:grid;grid-template-columns:auto minmax(0,1fr) auto;align-items:center;gap:12px}
.rc-f .ds-in{height:40px;font-size:13.5px}
.st4{margin-top:22px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.st4:has(> :nth-child(3):last-child){grid-template-columns:repeat(3,minmax(0,1fr))}
.st-t{display:flex;flex-direction:column;gap:4px;padding:16px 18px;border-radius:18px;background:#FFFFFF;border:1.5px solid #E6EAF3}
.st-t b{font-size:24px;font-weight:600;letter-spacing:-0.02em}
.st-t em{font-style:normal;font-size:13px;color:#5B6582}
.st-t.amber{background:#FFF8EA;border-color:#F4DDAA}
.st-t.amber b{color:#8A5A00}
.ccr{border-color:#BFE3CF;background:linear-gradient(160deg,#FFFFFF 50%,#F2FAF5)}
.ccr-g{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}
.ccr-r{display:flex;flex-direction:column;gap:4px;padding:14px;border-radius:14px;background:#FFFFFF;border:1.5px solid #E1F0E7}
.ccr-i{width:24px;height:24px;margin-bottom:4px;border-radius:50%;background:#0F6B45;color:#FFFFFF;display:flex;align-items:center;justify-content:center;font-weight:600}
.ccr-r.off .ccr-i{background:#F1F3F8;color:#8A93AD}
.ccr-r b{font-size:14px;font-weight:600;line-height:1.35}
.ccr-r > span:last-child{font-size:13px;color:#5B6582}
.crc{margin-top:16px;padding:20px 22px}
.crc-h{display:flex;align-items:flex-end;justify-content:space-between;gap:20px;padding-bottom:14px;border-bottom:1.5px solid #F0F2F8}
.crc-h h2{margin:4px 0 0 0;font-size:18px;font-weight:600}
.crc-w{display:flex;align-items:center;gap:10px}
.crc-w .ds-in{height:40px;width:110px}
.cr{display:grid;grid-template-columns:34px minmax(0,1fr) auto 230px;align-items:center;gap:14px;padding:12px 0;border-bottom:1.5px solid #F0F2F8}
.cr:last-child{border-bottom:0;padding-bottom:0}
.cr-b b{font-size:14.5px;font-weight:600}
.cr .ds-in{height:42px;font-size:14px}
.cr.warn .ds-in{border-color:#E8B54A;background:#FFFCF5}
.pcs{margin-top:20px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.pcs.one{grid-template-columns:minmax(0,420px)}
.pc{padding:18px;display:grid;grid-template-columns:44px minmax(0,1fr);gap:4px 12px;align-items:center}
.pc-b{display:flex;flex-direction:column;gap:2px;min-width:0}
.pc-b b{font-size:15.5px;font-weight:600}
.pc-b span{font-size:13px;color:#5B6582}
.pc-p{grid-column:1 / -1;margin-top:12px;display:flex;flex-direction:column;gap:8px;font-size:13.5px;font-weight:500}
.pc-n{grid-column:1 / -1;margin:6px 0 0 0;font-size:13px;color:#5B6582}
.ef-pb{display:block;height:8px;border-radius:8px;background:#EAF0FF;overflow:hidden}
.ef-pb i{display:block;height:100%;border-radius:8px;background:#1652F0}
.tb{display:flex;flex-direction:column}
.tb-r{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1.3fr) 168px 70px;align-items:center;gap:12px;padding:10px 0;border-bottom:1.5px solid #F0F2F8}
.tb.solo .tb-r{grid-template-columns:minmax(0,1fr) 180px 80px}
.tb-hd{padding-top:0;font-size:12.5px;font-weight:500;color:#8A93AD}
.tb-g{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-top:14px;padding:10px 14px;border-radius:12px;background:#F7F9FD}
.tb-g:first-of-type{margin-top:4px}
.tb-g b{font-size:14px;font-weight:600}
.tb-lead,.tb-ins{display:inline-flex;align-items:center;gap:8px;font-size:12.5px;color:#5B6582}
.tb-lead .ds-in,.tb-ins .ds-in{height:34px;font-size:13px;padding-right:34px}
.tb-lead .sel svg,.tb-ins .sel svg{right:10px}
.tb-it{display:flex;align-items:center;gap:10px;min-width:0}
.tb-it em{width:18px;flex-shrink:0;font-style:normal;font-size:12.5px;color:#8A93AD}
.tb-it .it-i{width:30px;height:30px;border-radius:9px}
.tb-it b{font-size:14px;font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tb-a{display:flex;flex-wrap:wrap;align-items:center;gap:6px}
.ds-chip.xs{height:30px;padding:0 11px;font-size:12.5px;gap:5px}
.sts .ds-in{height:36px;font-size:13px;padding-left:28px;border-radius:999px}
.sts{position:relative;display:block}
.sts::before{content:'';position:absolute;z-index:1;left:12px;top:50%;width:8px;height:8px;margin-top:-4px;border-radius:50%;background:#8A93AD;pointer-events:none}
.sts.green::before{background:#0F6B45}
.sts.blue::before{background:#1652F0}
.sts.amber::before{background:#B76E00}
.sts.green .ds-in{background:#F2FAF5;border-color:#BFE3CF}
.sts.amber .ds-in{background:#FFF8EA;border-color:#F4DDAA}
.tb-d{font-size:13.5px;color:#3A4566;font-weight:500}
.tb-d.ok{color:#0F6B45}
.hs{list-style:none;margin:0;padding:0;display:flex;flex-direction:column}
.hs li{display:grid;grid-template-columns:100px minmax(0,1fr);gap:12px;padding:10px 0;border-bottom:1.5px solid #F0F2F8;font-size:14px}
.hs li:last-child{border-bottom:0}
.hs em{font-style:normal;color:#8A93AD;font-size:13px}
.utabs{margin-top:20px;display:flex;gap:28px;border-bottom:1.5px solid #E6EAF3}
.ut{display:inline-flex;align-items:center;gap:8px;height:46px;margin-bottom:-1.5px;border-bottom:2.5px solid transparent;color:#5B6582;font-size:14.5px;font-weight:500;text-decoration:none;white-space:nowrap}
.ut:hover{color:#0B1433}
.ut.on{color:#0B1433;font-weight:600;border-bottom-color:#1652F0}
.ut.on svg{color:#1652F0}
.mw-h{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:12px 8px 14px 8px;border-bottom:1.5px solid #F0F2F8;margin-bottom:4px}
.mw-who{display:flex;align-items:center;gap:12px}
.mw-who > span{display:flex;flex-direction:column;gap:1px}
.mw-who b{font-size:14.5px;font-weight:600}
.mw-who em{font-style:normal;font-size:12.5px;color:#5B6582}
.mw{margin-top:20px;padding:10px 14px 8px 14px}
.mw-r{display:flex;align-items:center;gap:14px;padding:12px 8px}
.mw-r + .mw-r{border-top:1.5px solid #F0F2F8}
.mw-b{flex:1;min-width:0;display:flex;flex-direction:column;gap:2px}
.mw-b b{font-size:15px;font-weight:600}
.mw-b span{font-size:13px;color:#5B6582}
.mw-d{width:90px;font-size:13.5px;font-weight:500;color:#3A4566}
.sb4{display:flex;height:16px;border-radius:999px;overflow:hidden;gap:3px}
.sb4 i{display:block;height:100%}
.lg5{margin-top:16px;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px}
.lg5 span{display:flex;flex-direction:column;gap:3px;font-size:13px}
.lg5 i{width:12px;height:12px;border-radius:4px;margin-bottom:4px}
.lg5 b{font-weight:600}
.lg5 em{font-style:normal;color:#5B6582}
.tot{margin-top:18px;padding-top:16px;border-top:1.5px solid #F0F2F8;display:flex;align-items:center;gap:16px;font-size:14px;color:#3A4566}
.tot > span{flex:1}
.tot b{font-size:18px;font-weight:600;color:#0B1433}
.tot-d{display:inline-flex;align-items:center;gap:8px}
.g2{margin-top:16px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.g2 > .fc{margin-top:0}
.bl{display:flex;flex-direction:column;gap:10px}
.bl-r{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr) 110px;align-items:center;gap:12px;font-size:13.5px}
.bl-n{color:#3A4566;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.bl-b{height:8px;border-radius:8px;background:#F1F3F8;overflow:hidden}
.bl-b i{display:block;height:100%;border-radius:8px;background:linear-gradient(90deg,#1652F0,#5C86FF)}
.bl-v{display:flex;justify-content:flex-end;gap:8px;color:#5B6582}
.bl-v b{font-weight:600;color:#0B1433}
.ex-g{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;margin-bottom:16px}
.ex-g p{margin:6px 0 0 0;font-size:14px;line-height:1.55;color:#3A4566}
.tbl{margin-top:22px;padding:6px 20px}
.tbl-r{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(0,1fr) 80px 90px 90px 70px 170px;align-items:center;gap:12px;padding:12px 0;border-bottom:1.5px solid #F0F2F8;font-size:14px}
.tbl-r:last-child{border-bottom:0}
.tbl-hd{font-size:12.5px;font-weight:500;color:#8A93AD}
.tbl-n{display:flex;align-items:center;gap:10px}
.tbl-n b{font-weight:600}
.cv{display:flex;flex-direction:column}
.cv-r{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,1fr) 90px repeat(4,56px) 60px;align-items:center;gap:10px;padding:10px 0;border-bottom:1.5px solid #F0F2F8;font-size:14px}
.cv-hd{font-size:12.5px;font-weight:500;color:#8A93AD;text-align:left}
.cv-r b{font-weight:600}
.cv-c{width:30px;height:30px;border-radius:9px;border:1.5px dashed #CBD3E6;display:flex;align-items:center;justify-content:center;color:#FFFFFF}
.cv-c.on{border:0;background:#1652F0}
.pr{margin-top:16px}
.pr.warn{border-color:#F4DDAA}
.pr-h{display:flex;align-items:center;gap:12px;margin-bottom:18px}
.pr-h div{flex:1;display:flex;flex-direction:column;gap:2px}
.pr-h b{font-size:16px;font-weight:600}
.pr-h span{font-size:13px;color:#5B6582}
.pr-pl{margin-top:18px;padding-top:16px;border-top:1.5px solid #F0F2F8;display:flex;align-items:center;justify-content:space-between;gap:16px}
.pr-plt{display:flex;flex-direction:column;gap:2px}
.pr-plt b{font-size:14.5px;font-weight:600}
.pr-plt span{font-size:13px;color:#5B6582}
.addp{margin-top:16px}
.ls{display:flex;align-items:center;gap:14px;padding:12px;border-radius:14px;background:#F7F9FD;margin-bottom:6px}
.ls-d{width:52px;height:52px;flex-shrink:0;border-radius:14px;background:#1652F0;color:#FFFFFF;display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1.1}
.ls-d em{font-style:normal;font-size:10.5px;font-weight:600;letter-spacing:.06em;opacity:.8}
.ls-d b{font-size:15px;font-weight:600}
.ls-t{flex:1;display:flex;flex-direction:column;gap:2px}
.ls-t b{font-size:15px;font-weight:600}
.ls-t span{font-size:13px;color:#5B6582}
.spl{display:block;margin-bottom:8px}
.spl-b{display:block;height:8px;border-radius:8px;background:#0B1433;overflow:hidden}
.spl-b i{display:block;height:100%;background:linear-gradient(90deg,#1652F0,#5C86FF)}
.pct-w{position:relative;display:inline-block;width:140px}
.pct-w em{position:absolute;right:14px;top:50%;transform:translateY(-50%);font-style:normal;color:#5B6582}
.flw{margin-top:22px;padding:22px 24px}
.flw ol{list-style:none;margin:0;padding:0;display:flex;position:relative}
.flw ol::before{content:'';position:absolute;left:16px;right:16px;top:15px;height:3px;border-radius:3px;background:linear-gradient(90deg,#1652F0,#9DB8F7)}
.flw li{flex:1 1 0;min-width:0;display:flex;flex-direction:column;align-items:center;gap:10px;text-align:center;position:relative}
.flw li:first-child{align-items:flex-start;text-align:left}
.flw li:last-child{align-items:flex-end;text-align:right}
.flw-d{position:relative;z-index:1;width:32px;height:32px;border-radius:50%;background:#1652F0;color:#FFFFFF;font-size:13px;font-weight:600;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 4px #FFFFFF}
.flw li b{font-size:14px;font-weight:600;padding:0 4px}
.flw-n{margin:16px 0 0 0;padding-top:14px;border-top:1.5px solid #F0F2F8;font-size:14px;color:#3A4566}
.sps{margin-top:16px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.sp{display:flex;align-items:flex-start;gap:16px;padding:18px 18px 18px 20px;border-radius:18px;border:1.5px solid #E6EAF3;background:#FFFFFF;font-family:inherit;text-align:left;cursor:pointer;color:#0B1433}
.sp.on{border-color:#C9D7FA}
.sp-t{flex:1;display:flex;flex-direction:column;align-items:flex-start;gap:6px}
.sp-t b{font-size:15.5px;font-weight:600}
.sp-t > span:last-child{font-size:13.5px;line-height:1.5;color:#5B6582}
.sp .tg-s{margin-top:2px}
.sp.on .tg-s{background:#1652F0}
.sp.on .tg-s i{transform:translateX(18px)}
.am{margin-top:22px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.ds-opt.amc{flex-direction:column;align-items:stretch;gap:0;padding:10px 10px 20px 10px;border-radius:22px;transition:border-color .2s ease,box-shadow .2s ease,transform .2s ease}
.ds-opt.amc:hover{transform:translateY(-2px);box-shadow:0 18px 40px -22px rgba(22,82,240,.35)}
.ds-opt.amc.on{background:#FFFFFF;box-shadow:0 0 0 4px rgba(22,82,240,.12),0 22px 44px -24px rgba(22,82,240,.45)}
.amc .ds-opt-ck{position:absolute;top:22px;right:22px;margin:0;z-index:2}
.ax-vz{display:block;height:150px;border-radius:15px;background:linear-gradient(160deg,#F5F8FF,#EDF2FF);position:relative;overflow:hidden}
.amc.on .ax-vz{background:linear-gradient(160deg,#EAF0FF,#DCE6FF)}
.ax-v{position:absolute;inset:0;display:grid;grid-template-columns:auto minmax(30px,1fr) auto;grid-template-rows:1fr;align-items:center;padding:0 40px}
.ax-v.two{grid-template-rows:1fr 1fr;padding:20px 40px}
.ax-v .ax-p{grid-column:1}
.ax-v .ax-l{grid-column:2;grid-row:1 / -1;width:100%;height:100%}
.ax-v .ax-cv{grid-column:3;grid-row:1 / -1}
.ax-l{fill:none;stroke:#1652F0;stroke-width:2.5;stroke-dasharray:4 5;vector-effect:non-scaling-stroke;opacity:.6}
.ax-p{justify-self:start;display:inline-flex;align-items:center;gap:8px;height:40px;padding:0 14px 0 8px;border-radius:999px;background:#FFFFFF;box-shadow:0 8px 18px -10px rgba(11,20,51,.35);white-space:nowrap}
.ax-p b{font-size:14px;font-weight:600}
.ax-p em{font-style:normal;font-size:12px;color:#5B6582}
.ax-p.gold{background:linear-gradient(135deg,#FFFAEB,#FFF1CF);border:1.5px solid #F4D98E}
.ax-p.gold b{color:#4A3300}
.ax-p.gold em{color:#6B4E16}
.ax-p.blue{border:1.5px solid #C9D7FA}
.ax-p.blue b{color:#0E3BB8}
.ax-cv{display:flex;flex-direction:column;gap:6px;width:92px;padding:8px;border-radius:14px;background:#FFFFFF;box-shadow:0 14px 28px -14px rgba(11,20,51,.45)}
.ax-cv i{display:flex;align-items:center;justify-content:center;height:44px;border-radius:9px;background:linear-gradient(140deg,#1652F0,#0B1433);color:#FFFFFF;font-style:normal;font-size:11px;font-weight:600}
.ax-cv b{height:5px;border-radius:5px;background:#E1E7F3}
.ax-cv b.s{width:60%}
.ax-t{display:flex;flex-direction:column;gap:6px;padding:18px 12px 0 12px}
.ax-t b{font-size:18px;font-weight:600;letter-spacing:-0.01em}
.ax-t span{font-size:14px;line-height:1.5;color:#4A5578}
.ax-f{margin:14px 12px 0 12px;padding-top:14px;border-top:1.5px solid #EEF1F7;display:flex;flex-wrap:wrap;gap:8px}
.ax-f > span{display:inline-flex;align-items:center;gap:7px;height:32px;padding:0 12px 0 6px;border-radius:999px;background:#F7F9FD;font-size:13px;font-weight:500;color:#3A4566}
.ax-f > span > svg{width:22px;height:22px;padding:4px;box-sizing:border-box;border-radius:50%;background:#EAF0FF;color:#1652F0}
.amc.on .ax-f > span{background:#F2F6FF}
.ax-pr{margin-top:16px;padding:24px 28px}
.ax-pr ol{list-style:none;margin:0;padding:0;display:flex;position:relative;justify-content:space-between}
.ax-pr ol::before{content:'';position:absolute;left:17px;right:17px;top:17px;height:2px;background:repeating-linear-gradient(90deg,#9DB8F7 0 6px,transparent 6px 11px)}
.ax-pr li{position:relative;z-index:1;flex:1 1 0;display:flex;flex-direction:column;align-items:center;gap:10px;text-align:center}
.ax-pr li:first-child{align-items:flex-start;text-align:left}
.ax-pr li:last-child{align-items:flex-end;text-align:right}
.ax-d{width:34px;height:34px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:#FFFFFF;box-shadow:0 0 0 4px #FFFFFF}
.ax-m{width:34px;height:34px;border-radius:50%;background:#0B1433 url(/_blob/6d26bb5dab742fc7a27cff4144cfd663) center / 18px no-repeat;display:block}
.ax-pr li.y .av{box-shadow:0 0 0 2.5px #1652F0}
.ax-pr li b{font-size:14px;font-weight:600}
.ax-pr li.y b{color:#1652F0}
.ax-pr p{margin:20px 0 0 0;padding-top:16px;border-top:1.5px solid #F0F2F8;display:flex;align-items:center;gap:8px;font-size:14px;color:#3A4566}
.ax-pr p svg{color:#1652F0;flex-shrink:0}
.pr-g{margin-top:22px;display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:16px;align-items:start}
.pr-main,.pr-side{display:flex;flex-direction:column;gap:16px;min-width:0}
.pr-side{position:sticky;top:88px}
.pcd{padding:24px 26px 26px 26px;position:relative;overflow:hidden}
.pcd::before{content:'';position:absolute;left:0;right:0;top:0;height:4px}
.pcd.gold::before{background:linear-gradient(90deg,#F6C343,#D08A12)}
.pcd.blue::before{background:linear-gradient(90deg,#5C86FF,#1652F0)}
.pc-h{display:flex;align-items:center;gap:16px}
.pc-i{width:56px;height:56px;flex-shrink:0;border-radius:16px;display:flex;align-items:center;justify-content:center}
.pcd.gold .pc-i{background:linear-gradient(140deg,#FFFAEB,#FFF1CF)}
.pcd.blue .pc-i{background:#EAF0FF}
.pc-h .pg-e{margin-bottom:4px}
.pcd.gold .pc-h .pg-e{color:#8A5A00}
.pc-h h2{margin:0;font-size:19px;font-weight:600;letter-spacing:-0.01em}
.pc-sel{margin-left:auto;display:flex;flex-direction:column;align-items:flex-end;gap:4px;text-align:right}
.pc-sel > span{display:flex;align-items:center;font-size:12.5px;color:#5B6582}
.pc-sel > div{display:flex;align-items:baseline;gap:6px}
.pc-sel b{font-size:30px;font-weight:600;letter-spacing:-0.03em;line-height:1}
.pc-sel b.no{font-size:16px;font-weight:500;color:#8A93AD;letter-spacing:0}
.pc-sel em{font-style:normal;font-size:14px;color:#5B6582}
.pc-r{margin-top:22px;display:flex;align-items:center;gap:8px;font-size:14px;color:#3A4566}
.pc-r b{font-weight:600;color:#0B1433}
.pc-band{position:relative;margin:16px 0 0 0;height:30px}
.pc-tr{position:absolute;left:0;right:0;top:12px;height:8px;border-radius:8px;overflow:hidden}
.pcd.gold .pc-tr{background:linear-gradient(90deg,#FFF1CF,#F6C343)}
.pcd.blue .pc-tr{background:linear-gradient(90deg,#DCE6FF,#5C86FF)}
.pc-calc{position:absolute;top:0;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center}
.pc-calc i{width:4px;height:32px;border-radius:4px;background:#0B1433;box-shadow:0 0 0 3px #FFFFFF}
.pc-calc em{position:absolute;top:-24px;white-space:nowrap;font-style:normal;font-size:12px;font-weight:600;color:#0B1433;background:#FFFFFF;padding:2px 8px;border-radius:999px;box-shadow:0 2px 8px rgba(11,20,51,.12)}
.pcd.gold .pc-band{margin-top:36px}
.pc-stops{margin-top:12px;display:grid;grid-template-columns:repeat(var(--n),minmax(0,1fr));gap:8px}
.pc-stop{display:flex;align-items:center;justify-content:center;gap:8px;padding:12px 6px;border-radius:14px;border:1.5px solid #E6EAF3;background:#FFFFFF;color:#0B1433;font-family:inherit;cursor:pointer;transition:border-color .2s ease,box-shadow .2s ease,transform .2s ease}
.pc-stop b{font-size:17px;font-weight:600}
.pc-stop:hover{border-color:#9DB8F7}
.pcd.gold .pc-stop.on{border-color:#D08A12;background:linear-gradient(160deg,#FFFAEB,#FFF1CF);box-shadow:0 0 0 4px rgba(214,150,30,.16);transform:translateY(-2px)}
.pcd.blue .pc-stop.on{border-color:#1652F0;background:#F2F6FF;box-shadow:0 0 0 4px rgba(22,82,240,.12);transform:translateY(-2px)}
.pc-stop:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:2px}
.mbl{display:inline-flex;align-items:center;gap:4px;color:#0B1433;text-decoration:none}
.mbl:hover{color:#1652F0}
.why{padding:0;overflow:hidden}
.why summary{display:flex;align-items:center;gap:12px;padding:18px 20px;cursor:pointer;list-style:none}
.why summary::-webkit-details-marker{display:none}
.why summary b{flex:1;font-size:15.5px;font-weight:600}
.why summary > svg{color:#5B6582;transition:transform .2s ease}
.why[open] summary > svg{transform:rotate(180deg)}
.why-i{width:36px;height:36px;border-radius:11px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.why-b{padding:0 20px 20px 20px;font-size:13.5px;color:#3A4566}
.why-b ul{list-style:none;margin:8px 0 0 0;padding:0;display:flex;flex-direction:column;gap:8px}
.why-b li{display:flex;align-items:center;gap:9px}
.why-b li svg{flex-shrink:0;width:18px;height:18px;padding:4px;box-sizing:border-box;border-radius:50%;background:#EAF0FF;color:#1652F0}
.why-b p{margin:14px 0 6px 0;padding-top:12px;border-top:1.5px solid #F0F2F8;font-size:13px;color:#5B6582}
.pn{padding:18px 20px;background:linear-gradient(160deg,#0B1433,#102A7A);border:0;color:#FFFFFF}
.pn-eq{display:flex;align-items:center;gap:10px;font-size:15px}
.pn-eq b{font-weight:600}
.pn-eq i{font-style:normal;font-size:22px;color:#9DB8F7}
.pn p{margin:10px 0 0 0;font-size:13.5px;line-height:1.55;color:rgba(255,255,255,.75)}
.kn{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.kn li{display:flex;gap:10px;align-items:flex-start;padding:12px 14px;border-radius:12px;background:#F7F9FD;font-size:14px;line-height:1.45}
.kn li span{width:20px;height:20px;flex-shrink:0;border-radius:50%;background:#E7F5EE;color:#0F6B45;display:flex;align-items:center;justify-content:center}
.mq{display:flex;align-items:center;justify-content:space-between;gap:20px;padding:14px 0;border-bottom:1.5px solid #F0F2F8}
.mq:first-child{padding-top:0}
.mq:last-child{border-bottom:0;padding-bottom:0}
.mq b{font-size:14.5px;font-weight:500;max-width:380px}
.mq .ds-seg{flex-shrink:0}
.mb{margin-top:16px;padding:22px 24px;display:grid;grid-template-columns:auto minmax(0,1fr) auto;align-items:center;gap:24px;background:linear-gradient(120deg,#F2F6FF,#FFFFFF 70%);border-color:#DCE5FB}
.mb-g{display:grid;grid-template-columns:auto auto;align-items:center;gap:6px 12px}
.mb-g .pg-e{grid-column:1 / -1;margin:0}
.mb-g b{font-size:24px;font-weight:600;letter-spacing:-0.02em}
.mb-g .ds-tag{grid-column:1 / -1;justify-self:start}
.mb-m{display:none}
.mb p{margin:0;font-size:14px;line-height:1.55;color:#3A4566}
.mb-a{display:flex;align-items:center;gap:14px}
.bn-amb{background:#FFF8EA;border-color:#F4DDAA}
.bn-i.amb{background:#B76E00}
.bn p b.in{display:inline}
.mbl{display:inline-flex;align-items:center;gap:4px;color:#0B1433;text-decoration:none}
.mbl:hover{color:#1652F0}
.ps{margin-top:22px;padding:6px 24px 20px 24px;max-width:760px}
.ps-r{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:16px 0;border-bottom:1.5px solid #F0F2F8;font-size:14.5px}
.ps-r span{color:#5B6582}
.ps-r b{font-weight:600}
.ps-g{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;padding:16px 0;border-bottom:1.5px solid #F0F2F8}
.ps-c{display:flex;flex-direction:column;gap:8px;padding:16px;border-radius:16px;background:#F7F9FD}
.ps-c span{font-size:13px;color:#5B6582}
.ps-c b{display:flex;align-items:center;gap:10px;font-size:24px;font-weight:600;letter-spacing:-0.02em}
.ps-n{margin:14px 0 0 0;font-size:13.5px;color:#5B6582}
.sv-s .ds-ghost{margin-right:8px}
@media (max-width: 1180px){.at-r{grid-template-columns:minmax(0,1fr) auto auto;}.at-r .sel{grid-column:1 / 3}.ccr-g{grid-template-columns:repeat(2,minmax(0,1fr))}.tbl-r{grid-template-columns:minmax(0,1.6fr) minmax(0,1fr) 70px 80px 80px 60px 150px}}
@media (max-width: 960px){
.am{grid-template-columns:minmax(0,1fr)}
.ax-vz{height:120px}
.ax-v,.ax-v.two{padding:14px 22px}
.ax-pr ol{flex-direction:column;align-items:stretch;gap:10px}
.ax-pr ol::before{left:17px;right:auto;top:18px;bottom:18px;width:2px;height:auto;background:repeating-linear-gradient(180deg,#9DB8F7 0 6px,transparent 6px 11px)}
.ax-pr li,.ax-pr li:first-child,.ax-pr li:last-child{flex-direction:row;align-items:center;text-align:left}
.ax-pr{padding:18px 16px}
.pr-g{grid-template-columns:minmax(0,1fr)}
.pr-side{position:static}
.pcd{padding:20px 16px}
.pc-h{flex-wrap:wrap}
.pc-sel{margin-left:0;text-align:left;align-items:flex-start;width:100%}
.pc-stops{gap:4px}
.pc-stop{padding:10px 2px;gap:4px}
.pc-stop b{font-size:14px}
.pc-stop .cr-c,.pc-stop .dlp-c{display:none}
.utabs{overflow-x:auto}
.mw-h{flex-direction:column;align-items:stretch}
.mw-h .chips{flex-wrap:nowrap;overflow-x:auto;margin:0 -14px;padding:0 14px 2px 14px;scrollbar-width:none}
.mw-h .ds-chip{flex-shrink:0}
.flt{padding:12px 14px}
.flt-l{width:100%;overflow-x:auto}
.flt .chips{flex-wrap:nowrap;overflow-x:auto;margin:0 -14px;padding:0 14px;scrollbar-width:none}
.flt .chips .ds-chip{flex-shrink:0}
.rc{padding:16px 14px}
.rc-h{flex-wrap:wrap}
.rc-h .ds-ghost{width:100%}
.at-r{grid-template-columns:minmax(0,1fr);gap:8px}
.at-r .sel{grid-column:auto}
.at-r .ds-seg{width:100%}
.rc-f{grid-template-columns:minmax(0,1fr)}
.st4{grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.st4:has(> :nth-child(3):last-child){grid-template-columns:repeat(3,minmax(0,1fr))}
.st-t{padding:12px}
.st-t b{font-size:19px}
.st-t em{font-size:12px}
.ccr-g{grid-template-columns:minmax(0,1fr)}
.ccr-r{flex-direction:row;align-items:center;gap:10px}
.ccr-i{margin:0}
.ccr-r b{flex:1}
.crc{padding:16px 14px}
.crc-h{flex-direction:column;align-items:stretch;gap:10px}
.crc-w{flex-wrap:wrap}
.cr{grid-template-columns:34px minmax(0,1fr);gap:8px 12px}
.cr .ds-seg,.cr .sel{grid-column:1 / -1}
.pcs{grid-template-columns:minmax(0,1fr)}
.tb-r,.tb.solo .tb-r{grid-template-columns:minmax(0,1fr) auto;gap:8px}
.tb-hd{display:none}
.tb-a{grid-column:1 / -1;order:3}
.tb-r .sts{grid-column:1;order:4}
.tb-d{order:2;text-align:right}
.tb.solo .tb-r{grid-template-columns:minmax(0,1fr) 148px;row-gap:2px;padding:12px 0}
.tb.solo .tb-r .sts{grid-column:2;grid-row:1;order:0}
.tb.solo .tb-it{grid-row:1 / span 2}
.tb.solo .tb-d{grid-column:2;grid-row:2;order:0;padding-right:4px;font-size:12px}
.tb.solo .tb-it b{white-space:normal}
.tb-g{flex-direction:column;align-items:flex-start}
.mw-r{flex-wrap:wrap}
.mw-b{flex-basis:calc(100% - 50px)}
.mw-r .ds-tag{margin-left:48px}
.lg5{grid-template-columns:repeat(2,minmax(0,1fr))}
.tot{flex-wrap:wrap}
.g2,.ex-g{grid-template-columns:minmax(0,1fr)}
.bl-r{grid-template-columns:minmax(0,1fr) 100px;}
.bl-b{grid-column:1 / -1;order:3}
.tbl{padding:4px 14px;overflow-x:auto}
.tbl-r{min-width:640px}
.cv{overflow-x:auto}
.cv-r{min-width:560px}
.pr-pl{flex-direction:column;align-items:stretch}
.flw{padding:18px 16px}
.flw ol{flex-direction:column;gap:0}
.flw ol::before{left:15px;right:auto;top:16px;bottom:16px;width:3px;height:auto;background:linear-gradient(180deg,#1652F0,#9DB8F7)}
.flw li,.flw li:first-child,.flw li:last-child{flex-direction:row;align-items:center;text-align:left;min-height:48px}
.sps{grid-template-columns:minmax(0,1fr)}
.kn{grid-template-columns:minmax(0,1fr)}
.mq{flex-direction:column;align-items:stretch;gap:10px}
.mb{grid-template-columns:minmax(0,1fr);gap:12px}
.ps{padding:4px 16px 16px 16px}
.ps-g{grid-template-columns:minmax(0,1fr)}
.sv-s .ds-ghost{width:100%;margin:0 0 6px 0}
.sv-s{flex-direction:column;width:100%}
}
'''

def body():
    blocks = '\n'.join('<sc-if value="{{p_%s}}" hint-placeholder-val="{{ %s }}">\n%s\n</sc-if>' % (k, 'true' if k == 'res' else 'false', h) for k, _, _, _, h in PAGES)
    navs = '\n'.join('<sc-if value="{{n_%s}}" hint-placeholder-val="{{ %s }}">%s</sc-if>' % (n, 'true' if n == 'res' else 'false', sidebar(n)) for n in sorted(set(p[1] for p in PAGES)))
    tops = '\n'.join('<sc-if value="{{t_%s}}" hint-placeholder-val="{{ %s }}">%s</sc-if>' % (k, 'true' if k == 'Build' else 'false', topbar(phase=ph, solo=solo))
                     for k, ph, solo in [('Build', 'Build', False), ('BuildSolo', 'Build', True), ('Experience', 'Experience', False)])
    return '''<div class="ds-root">
%s
<div style="min-width: 0; display: flex; flex-direction: column">
%s
<main class="ds-main">
%s
</main>
</div>
</div>''' % (navs, tops, blocks)

JS = C.js() + '''var PG = %s;
class Component extends DCLogic {
  renderVals() {
    var pg = this.props.page || 'res', info = PG[pg] || PG.res;
    var v = togVals(this), self = this;
    Object.keys(PG).forEach(function (k) { v['p_'.concat(k)] = k === pg; });
    %s.forEach(function (n) { v['n_'.concat(n)] = n === info[0]; });
    v.t_Build = info[1] === 'Build' && !info[2]; v.t_BuildSolo = info[1] === 'Build' && info[2]; v.t_Experience = info[1] === 'Experience';
    v.navCls = this.state.nav ? 'ds-open' : '';
    v.toggleNav = function () { self.setState({ nav: !self.state.nav }); };
    return v;
  }
}''' % (json.dumps({k: [n, ph, solo] for k, n, ph, solo, _ in PAGES}), json.dumps(sorted(set(p[1] for p in PAGES))))

COURSE_CSS += r'''.mb-g .mb-m{display:flex;align-items:flex-end;gap:4px;height:28px}
.mb-m i{width:8px;border-radius:3px;background:#E1E7F4;transform-origin:bottom;animation:mbUp .7s cubic-bezier(.2,.8,.2,1) both}
.mb-m i:nth-child(1){height:10px;animation-delay:.2s}
.mb-m i:nth-child(2){height:18px;animation-delay:.32s}
.mb-m i:nth-child(3){height:26px;animation-delay:.44s}
.mb-m i.on{background:linear-gradient(180deg,#5C86FF,#1652F0)}
@keyframes mbUp{from{transform:scaleY(0)}}
.ds-main > .sv:has(.sv-s:empty){width:max-content;margin-left:auto;padding-left:14px}
.wk > .wk-r .fc{margin:0}
.wk-r .fc.rx{padding:20px}
.wk-r .fc.rx .fc-h{margin-bottom:14px}
.wk-r .fc.rx .fc-h h2{font-size:16px}
.wk-m > .fc:first-child{margin-top:0}
.wk-r .hs li{grid-template-columns:minmax(0,1fr);gap:2px}
.mw-who b{font-size:14px}
.dl2{align-items:start}
.dl2-l{display:flex;flex-direction:column;gap:16px;min-width:0}
.dl2-l > .fc{margin:0}
.pr-h{align-items:flex-start;margin-bottom:20px}
.pr-h > div:not(.pr-pl){gap:3px}
.pr-h .it-warn{margin-top:4px;font-size:13px}
.pr-h .pr-pl{flex:0 0 auto;margin:0;padding:0;border:0;flex-direction:row;align-items:center;gap:12px}
.pr-h .ds-seg{flex:none;flex-direction:row;gap:4px}
.pr-h .pr-plt{flex:none;flex-direction:row;align-items:center;gap:0}
@media (min-width: 961px){.wk .tb-r{grid-template-columns:minmax(0,1fr) 200px 142px 48px;gap:10px}.wk .tb-a .ds-chip.xs{padding:0 10px}}
.sps.lst .sp-t{justify-items:start}
.pr-plt{flex-direction:row;align-items:center}
.pr-plt b{font-size:13.5px;font-weight:500;color:#3A4566}
.sch .ds-seg{width:max-content}
.pol{display:flex;flex-direction:column}
.pol .fl{display:grid;grid-template-columns:200px auto;align-items:center;justify-content:start;gap:16px;padding:12px 0;border-top:1.5px solid #F0F2F8}
.pol .fl:first-child{border-top:0;padding-top:0}
.pol .fl:last-child{padding-bottom:0}
.pol .ds-seg{width:max-content}
.spr{display:flex;align-items:center;gap:16px;margin-top:4px}
.spr-l{display:flex;flex-direction:column;gap:10px}
.spr-l > span{display:grid;grid-template-columns:10px auto;align-items:center;column-gap:8px}
.spr-l i{width:10px;height:10px;border-radius:50%;background:#1652F0}
.spr-l i.n{background:#0B1433}
.spr-l b{font-size:18px;font-weight:600;letter-spacing:-0.01em}
.spr-l em{grid-column:2;font-style:normal;font-size:12.5px;color:#5B6582}
.nvo .ds-opt{flex-direction:column;align-items:flex-start;gap:14px;padding:18px}
.nvo .ds-opt-ck{position:absolute;top:16px;right:16px}
.nvz{position:relative;display:flex;align-items:center;gap:22px;height:44px;padding:0 4px}
.nvz i{position:relative;z-index:1;width:16px;height:16px;box-sizing:border-box;border-radius:50%;border:2px solid #9DB8F7;background:#FFFFFF}
.nvz i.d{border-color:#1652F0;background:#1652F0}
.nvz.seq::before{content:'';position:absolute;left:12px;right:12px;top:50%;height:2px;margin-top:-1px;background:linear-gradient(90deg,#1652F0,#CBD3E6)}
.nvz.seq i:not(.d){border-color:#CBD3E6;background:#F1F3F8}
.nvz.flx{display:grid;grid-template-columns:repeat(2,16px);gap:10px 26px;height:44px;align-content:center}
.nvz.flx i:nth-child(2){transform:translateX(10px)}
.nvz.flx i:nth-child(3){transform:translateX(-6px)}
.ds-opt:hover .nvz.flx i{animation:nvFloat 2.4s ease-in-out infinite}
.ds-opt:hover .nvz.flx i:nth-child(2n){animation-delay:-1.2s}
@keyframes nvFloat{50%{translate:0 -3px}}
.lxc{gap:20px}
.lxs{display:grid;grid-template-columns:auto minmax(0,1fr);gap:24px;align-items:end}
.lxp ol{list-style:none;margin:0;padding:0;position:relative;display:flex;flex-direction:column;gap:6px}
.lxp ol::before{content:'';position:absolute;left:13px;top:16px;bottom:16px;width:2px;background:linear-gradient(180deg,#1652F0 25%,#E6EAF3 25%)}
.lxp li{position:relative;display:flex;align-items:center;gap:12px;padding:6px 0;animation:lxIn .5s ease both;animation-delay:calc(var(--i) * 90ms + 200ms)}
@keyframes lxIn{from{opacity:0;transform:translateY(6px)}}
.lxp-d{position:relative;z-index:1;width:28px;height:28px;flex-shrink:0;box-sizing:border-box;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;background:#F1F3F8;color:#8A93AD;box-shadow:0 0 0 4px #FFFFFF}
.lxp li.dn .lxp-d{background:#E7F5EE;color:#0F6B45}
.lxp li.on .lxp-d{background:#1652F0;color:#FFFFFF;box-shadow:0 0 0 4px #FFFFFF,0 0 0 7px rgba(22,82,240,.16)}
.lxp li > span:last-child{display:flex;flex-direction:column;gap:1px;min-width:0}
.lxp em{font-style:normal;font-size:11.5px;color:#8A93AD}
.lxp b{font-size:13.5px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lxp li.lk b{color:#8A93AD;font-weight:500}
.sps.lst{margin:0;padding:6px 20px;display:flex;flex-direction:column;gap:0}
.sps.lst .sp{border:0;border-radius:0;padding:16px 0;background:none;align-items:center}
.sps.lst .sp + .sp{border-top:1.5px solid #F0F2F8}
.sps.lst .sp-t{display:grid;grid-template-columns:auto auto;justify-content:start;align-items:center;column-gap:10px;row-gap:3px}
.sps.lst .sp-t > span:last-child{grid-column:1 / -1}
.sps.lst .sp-t .ds-tag{height:20px;padding:0 7px;font-size:10.5px}
.sps.lst .sp-t b{font-size:15px}
.wk-m > .fc{margin-top:0}
.flw.v{padding:20px 18px}
.flw.v ol{flex-direction:column;gap:6px}
.flw.v ol::before{left:15px;right:auto;top:16px;bottom:16px;width:3px;height:auto;background:linear-gradient(180deg,#1652F0,#9DB8F7)}
.flw.v li,.flw.v li:first-child,.flw.v li:last-child{flex-direction:row;align-items:center;text-align:left;min-height:48px;animation:lxIn .5s ease both;animation-delay:calc(var(--i) * 120ms + 200ms)}
.flw.v li b{font-size:14px}
.ps2{max-width:none;display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);grid-template-areas:"a m" "g p" "g n";column-gap:40px;align-items:start;padding:8px 28px 24px 28px}
.ps2 > :nth-child(1){grid-area:a}
.ps2 > :nth-child(2){grid-area:g;border-bottom:0;padding-bottom:0}
.ps2 > :nth-child(3){grid-area:m}
.ps2 > :nth-child(4){grid-area:p}
.ps2 > :nth-child(5){grid-area:n;margin-top:14px;padding:12px 14px;border-radius:12px;background:#FFF8EA;color:#6B4A00}
.ps2 .ps-c{padding:20px;gap:12px;border:1.5px solid #E6EAF3;background:linear-gradient(160deg,#FFFFFF,#F5F8FF)}
.ps2 .ps-c:first-child{background:linear-gradient(160deg,#FFFFFF,#FFF8E6);border-color:#F4E2B0}
.ps2 .ps-c b{font-size:28px}
@media (max-width: 960px){
.ds-main > .sv:has(.sv-s:empty){width:auto;margin-left:-16px;padding-left:16px}
.rlw{grid-template-columns:minmax(0,1fr);gap:14px}
.rl-l{padding:4px}
.rr{padding:12px 10px;gap:12px}
.rr .rc-i{width:36px;height:36px}
.rr-a{flex-wrap:wrap;row-gap:2px}
.rr-a em{flex-basis:100%;padding-left:0}
.rl-d{position:static}
.rl-d .rc{padding:16px 14px}
.pcs{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;margin:18px -16px 0 -16px;padding:2px 16px 6px 16px;gap:10px;scrollbar-width:none}
.pcs::-webkit-scrollbar{display:none}
.pcs > .pc{flex:0 0 82%;scroll-snap-align:start;box-sizing:border-box}
.pcs.one > .pc{flex-basis:100%}
.tb:not(.solo) .tb-r{grid-template-columns:minmax(0,1fr) 140px;row-gap:8px;padding:12px 0}
.tb:not(.solo) .tb-a{grid-column:1;grid-row:2;order:0}
.tb:not(.solo) .tb-r .sts{grid-column:2;grid-row:2;order:0}
.tb:not(.solo) .tb-d{grid-column:2;grid-row:1;order:0;justify-self:end;align-self:center}
.tb:not(.solo) .tb-it{grid-column:1 / -1;grid-row:1;padding-right:52px}
.tb:not(.solo) .tb-it b{white-space:normal}
.rr-a > span:not(.ds-tag){flex:1 1 0}
.rl-d .at-r{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}
.rl-d .at-r .ds-seg{grid-column:auto}
.rl-d .at-r .ds-seg button{padding:0 6px;font-size:12px}
.tb-a .ds-chip.xs{height:30px;padding:0 9px;font-size:12px}
.mw-r{display:grid;grid-template-columns:36px minmax(0,1fr) auto;align-items:center;gap:6px 12px}
.mw-r > .it-i{grid-row:1 / span 2}
.mw-b{grid-column:2 / -1}
.mw-r .ds-tag{margin-left:0;grid-column:2;justify-self:start}
.mw-d{display:none}
.mw-r .ds-ghost{grid-column:3;grid-row:2}
.cr{grid-template-columns:34px minmax(0,1fr) minmax(0,1fr);gap:10px 10px}
.cr-b{grid-column:2 / -1}
.cr .ds-seg{grid-column:1 / 3;width:100%;box-sizing:border-box}
.cr .ds-seg button{padding:0 8px}
.cr .sel{grid-column:3}
.cr .ds-in{height:40px;font-size:13px;padding-left:12px}
.bl-r{grid-template-columns:minmax(0,1fr) auto;row-gap:6px}
.bl-n{white-space:normal}
.bl-v{white-space:nowrap}
.tbl{overflow:visible;padding:4px 16px}
.tbl-r{min-width:0;display:flex;flex-wrap:wrap;align-items:center;gap:4px 14px;padding:14px 0}
.tbl-r.tbl-hd{display:none}
.tbl-r > .tbl-n{flex-basis:100%;margin-bottom:2px}
.tbl-r > span:not(.tbl-n){font-size:12.5px;color:#3A4566}
.tbl-r > span:nth-child(3)::before{content:'Chapter ';color:#8A93AD}
.tbl-r > span:nth-child(4)::before{content:'Questions ';color:#8A93AD}
.tbl-r > span:nth-child(5)::before{content:'Required ';color:#8A93AD}
.tbl-r > span:nth-child(6)::before{content:'Pass ';color:#8A93AD}
.tbl-r > a{flex-basis:100%;margin-top:6px;padding-left:40px}
.tbl-n .it-i{margin-right:2px}
.cv{overflow:visible}
.cv-r.cv-hd{display:none}
.cv-r{min-width:0;display:flex;flex-wrap:wrap;align-items:center;gap:6px 6px;padding:14px 0}
.cv-r > b{flex:1 1 calc(100% - 60px)}
.cv-r > a{order:1}
.cv-r > span:nth-child(2){order:2;flex-basis:100%;font-size:12.5px;color:#5B6582;margin-top:-4px}
.cv-r > span:nth-child(3){display:none}
.cv-r > .cv-c{order:3;width:auto;height:30px;padding:0 10px 0 8px;gap:5px;border-radius:999px;font-size:12px;font-weight:500;color:#5B6582}
.cv-r > .cv-c.on{color:#FFFFFF}
.cv-r > .cv-c:nth-child(4)::after{content:'LO1'}
.cv-r > .cv-c:nth-child(5)::after{content:'LO2'}
.cv-r > .cv-c:nth-child(6)::after{content:'LO3'}
.cv-r > .cv-c:nth-child(7)::after{content:'LO4'}
.pr-h{flex-wrap:wrap}
.pr-h > div:not(.pr-pl){flex-basis:calc(100% - 50px)}
.pr-h .pr-pl{width:100%;justify-content:space-between;padding:12px 0 0 0;border-top:1.5px solid #F0F2F8;margin-top:4px}
.addp{flex-wrap:nowrap;overflow-x:auto;margin-left:-16px;margin-right:-16px;padding:0 16px;scrollbar-width:none}
.addp::-webkit-scrollbar{display:none}
.addp .ds-chip{flex-shrink:0}
.sch .fg3{grid-template-columns:repeat(2,minmax(0,1fr))}
.sch .fg3 > .fl:last-child{grid-column:1 / -1}
.pol .fl{grid-template-columns:minmax(0,1fr);gap:8px}
.pol .ds-seg{width:100%;box-sizing:border-box;flex-wrap:wrap}
.lxs{grid-template-columns:minmax(0,1fr);gap:18px}
.nvo{grid-template-columns:repeat(2,minmax(0,1fr))}
.sps.lst{padding:2px 16px}
.sps.lst .sp{padding:14px 0;gap:12px}
.sps.lst .sp-t > span:last-child{font-size:13px}
.wk-r > .flw.v{order:0}
.nvz{gap:12px}
.ps2 .ps-c b{font-size:18px}
.ps2{display:block;padding:4px 16px 16px 16px}
.ps2 .ps-g{grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.ps2 .ps-c{padding:14px 12px}
.sv-s:not(:empty){display:flex}
.ds-acts.sv > .sv-s:has(.ds-ghost){display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;width:100%;order:2}
.sv-s .ds-ghost{justify-content:center}
}
'''

write('Course.dc.html', doc('Course set-up · shared source', kit.KIT_CSS + '\n' + dash.DASH_CSS + BASE_CSS + CW_CSS + COURSE_CSS, body(), JS))

BOARDS = [
    ('STU-026', 'Course', {'page': 'res'}, 'CR-STU-026 · Course Resource Library'),
    ('STU-027', 'Course', {'page': 'comp'}, 'CR-STU-027 · Completion Rules'),
    ('STU-028', 'Course', {'page': 'team'}, 'CR-STU-028 · Team & Assignments'),
    ('STU-029', 'Course', {'page': 'mywork'}, 'CR-STU-029 · My Assigned Work'),
    ('STU-028-SOLO', 'Course', {'page': 'mysolo'}, 'CR-STU-028 · My Work: solo'),
    ('STU-031', 'Course', {'page': 'dlp'}, 'CR-STU-031 · DLP & Learning Effort'),
    ('STU-ASM', 'Course', {'page': 'assess'}, 'Course Assessments (management view)'),
    ('STU-PRA', 'Course', {'page': 'practice'}, 'Practice & Projects (management view)'),
    ('STU-DEL', 'Course', {'page': 'deliv'}, 'Delivery & Schedule (hybrid)'),
    ('STU-LX', 'Course', {'page': 'lx'}, 'Learner Experience'),
    ('STU-SUP', 'Course', {'page': 'support'}, 'Learner Support'),
    ('STU-032', 'Course', {'page': 'access'}, 'CR-STU-032 · Course Access Model'),
    ('STU-033', 'Course', {'page': 'maint'}, 'CR-STU-033 · Maintenance Burden'),
    ('STU-034', 'Course', {'page': 'pricing'}, 'CR-STU-034 · Course Pricing'),
    ('STU-034b', 'Course', {'page': 'pricingupd'}, 'CR-STU-034 · Pricing update required'),
    ('STU-035', 'Course', {'page': 'psum'}, 'CR-STU-035 · Access & Pricing Summary'),
]

if __name__ == '__main__':
    import sys
    H = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else {}
    for code, src, props, title in BOARDS:
        hd, hm = H.get(code, (900, 844))
        write(code + '.dc.html', wrapper(title + ' · Desktop', src, props, 1440, hd))
        write(code + '-Mobile.dc.html', wrapper(title + ' · Mobile', src, props, 390, hm))
    print('ok', len(BOARDS), 'boards; toggles', C.n)
