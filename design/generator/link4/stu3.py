"""Link 4 · Batch 3: course set-up pages. Client copy word for word.

Course.dc.html (prop page) → CR-STU-026 resources, 027 completion rules, 028 team & assignments (+ my assigned work, + solo my work),
031 DLP & effort, course assessments, practice & projects, delivery & schedule, learner experience, learner support,
032 access model, 033 maintenance burden, 034 pricing (+ update required), 035 summary.
CR-STU-030 Team Chat is a Builder overlay (stu2.py).
"""
import json
from l4kit import *
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
P('res', 'res', 'Build', page_head('Build', 'Course Resource Library', 'Upload once, attach anywhere: to the whole course, a chapter, or a single learning item. Each attachment controls download, requirement and when learners see it.',
    '<a class="ds-ghost sm" href="#">%s<span>Upload</span></a><a class="ds-ghost sm" href="#">%s<span>Add link</span></a>' % (ic('upload', 16, 2), ic('plus', 16, 2.2))) +
  '''<section class="ds-card flt ob-in2"><div class="flt-l"><span class="fl-l">Level</span>%s</div>%s</section>
<div class="wn ob-in2">%s<span>1 resource needs rights or source information: <b>retail-dataset.zip</b>.</span></div>
<div class="rcs ob-in3">%s</div>''' % (
      C.seg(['All levels', 'Course', 'Chapter', 'Item'], 0),
      chips(['All (8)', 'Documents (3)', 'Templates (1)', 'Datasets (2)', 'Downloads (0)', 'Links (1)', 'References (1)', 'Source materials (0)'], {0}, group='rcat'),
      ic('warn', 16, 2), ''.join(res_card(r) for r in RES)) +
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
    return '<nav class="pts ob-in2" aria-label="Team views"><a href="STU-028.dc.html" class="pt%s">Team progress</a><a href="STU-029.dc.html" class="pt%s">My assigned work</a></nav>' % (
        ' on' if cur == 0 else '', ' on' if cur == 1 else '')
HIST = [('Tue 14:30', 'Ada removed John from “Aggregations and GROUP BY” · authorship and activity history kept'), ('Mon 09:05', 'Ada made John Chapter 2 lead'),
        ('Mon 09:02', 'Ada assigned John to Chapter 2 “SQL Foundations”')]
P('team', 'team', 'Build', page_head('Build', 'Team & Assignments', TEAM_SUB) + team_tabs(0) +
  '<div class="pcs ob-in2">%s</div>' % ''.join(person(*x) for x in PEOPLE) +
  card('Course-level assignment', chips(['Ada', 'John', 'ABC Institute'], {0}), sub='People assigned to the whole course (for example, reviewing every chapter).', cls='ob-in3') +
  '<section class="ds-card fc ob-in3">%s</section>' % asg_table() +
  card('Assignment history', '<ul class="hs">%s</ul>' % ''.join('<li><em>%s</em><span>%s</span></li>' % x for x in HIST), t='Changing an assignment never erases authorship or activity history.') +
  acts('STU-031.dc.html'))

MYW = [('inter', 'SELECT Statements', 'Chapter 2 · Interactive', 'Needs review', 'Oct 3'), ('text', 'INNER vs LEFT JOIN', 'Chapter 3 · Text / Article', 'In progress', 'Oct 4'),
       ('practice', 'Your First Queries', 'Chapter 2 · Practice Activity', 'Not started', 'Oct 5'), ('practice', 'Practice Joins', 'Chapter 3 · Practice Activity', 'Not started', 'Oct 6'),
       ('quiz', 'Final Exam', 'Chapter 5 · Exam', 'Not started', 'Oct 7')]
P('mywork', 'team', 'Build', page_head('Build', 'My Assigned Work', TEAM_SUB) + team_tabs(1) +
  '<div class="mw-bar ob-in2">%s<div class="bn mw-v">%s<p><b>Viewing as Dr. John Adeyemi · Co-Creator</b></p></div></div>' % (
      C.seg(['All curriculum', 'My assigned work', 'Needs review', 'Completed'], 1), av(M1, 'J', 32)) +
  '<section class="ds-card mw ob-in3">%s</section>' % ''.join(
      '<div class="mw-r">%s<div class="mw-b"><b>%s</b><span>%s · %s</span></div>%s<span class="mw-d">Due %s</span><a class="ds-ghost xs" href="#">Open</a></div>' % (
          iti(k, 17), t, m, s, tag(s, STATUS_C[s]), d) for k, t, m, s, d in MYW))

P('mysolo', 'team', 'Build', page_head('Build', 'My Work', 'Your plan for this course: what is done, what is in progress and what is due. You are the only creator, so every lesson is yours. If you invite co-creators later, assignments appear here.') +
  '<div class="pcs one ob-in2">%s</div>' % person((ME, 'A'), 'Ada', 'You · Owner', 16, 7, 'SELECT Statements · due Oct 3', '16 lessons · 7 complete') +
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
<div class="ob-in3" style="margin-top: 16px">%s</div>
<div class="g2 ob-in4">%s%s</div>
<section class="ds-card fc ex ob-in4"><div class="fc-h"><div><h2>Estimated DLP is not DLP consumed</h2></div></div><div class="ex-g">
<div><span class="pg-e">Estimated course DLP · 795 DLP</span><p>Calculated here, in Creator Studio, from each item’s duration, reading time or expected effort. It’s the starting point for DLP Access at publication.</p></div>
<div><span class="pg-e">DLP consumed by learners</span><p>Decided on the learner side by the access and use policy [TO CONFIRM]. It can differ from the estimate, for example when optional items are skipped.</p></div></div>
<a class="ds-link" href="#">See how it’s used in DLP Access%s</a></section>''' % (
      tip('Runs continuously as you build. The exact calculation follows Credalio’s DLP policy [TO CONFIRM]. This estimate sets the permitted price range; it isn’t your price.'),
      ''.join('<i style="flex: %d; background: %s" title="%s"></i>' % (d, SEGC[i], n) for i, (n, t, d) in enumerate(EST)),
      ''.join('<span><i style="background: %s"></i><b>%s</b><em>%s · %d DLP</em></span>' % (SEGC[i], n, t, d) for i, (n, t, d) in enumerate(EST)), coin(),
      nova_sg('Your curriculum currently adds up to 8h 5m, but you planned about 26 hours in Course Design. Either the curriculum is still growing, or the plan needs updating.'),
      card('By chapter', bars(BYCH, 300)), card('By type of learning', bars(BYTY, 200)), ic('arrowr', 15, 2.2)) +
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
    return ('<section class="ds-card fc pr%s"><div class="pr-h">%s<div><b>%s</b><span>%s</span></div>%s</div><div class="fg fg2">%s%s%s%s</div><div class="pr-pl"><span class="pr-plt"><b>Becomes Proof of Learning?</b><span>Shown in the learner’s achievement record once passed.</span></span>%s</div></section>' % (
        ' warn' if warn else '', iti(k, 18), t, m, ('<span class="it-warn">%s<span>Still to set: outcome</span></span>' % ic('warn', 13, 2.2)) if warn else '',
        field('What will the learner produce?', '<input class="ds-in" value="%s" aria-label="What will the learner produce">' % prod),
        field('How is it evaluated?', '<input class="ds-in" value="%s" aria-label="How is it evaluated">' % ev),
        field('What skill does it demonstrate?', selx(SKL, sk, 'Skill demonstrated')), field('What outcome does it prove?', selx(OUT, oc, 'Outcome proved')),
        C.seg(['Yes', 'No'], pol)))
P('practice', 'alla', 'Build', page_head('Build', 'Practice & Projects', 'For each piece of practical work: what learners produce, which skill it demonstrates, which outcome it proves, how it’s evaluated, and whether it becomes Proof of Learning.') +
  '<div class="ob-in2">%s</div><div class="chips addp ob-in3">%s</div>' % (''.join(pra_card(p) for p in PRA), ''.join(
      '<button type="button" class="ds-chip add">%s<span>%s</span></button>' % (ic('plus', 14, 2.2), x) for x in ['Practical exercise', 'Project', 'Case study', 'Simulation', 'Portfolio work'])) +
  acts('STU-DEL.dc.html'))

# ---------------------------------------------------------------- Delivery & Schedule
P('deliv', 'deliv', 'Experience', page_head('Experience', 'Delivery & Schedule', 'Configure live sessions for your hybrid course.') +
  card('Scheduling model', '<div class="fg">%s<div class="fg fg3">%s%s%s</div></div>' % (
      C.seg(['Cohort', 'Recurring availability'], 0),
      field('Capacity per session', '<input class="ds-in" value="25" aria-label="Capacity per session">'),
      field('Time zone', '<input class="ds-in" value="WAT (UTC+1)" aria-label="Time zone">'),
      field('Instructor', '<input class="ds-in" value="Ada Ononuju" aria-label="Instructor">')), cls='ob-in2') +
  card('Live sessions', '<div class="ls">%s<div class="ls-t"><b>Analysis Clinic</b><span>Thursdays · 6:00 PM</span></div>%s</div><button type="button" class="ch-add" style="width: 100%%">%s<span>Add live session</span></button>' % (
      '<span class="ls-d"><em>THU</em><b>6:00</b></span>', tag('60 min', 'line'), ic('plus', 16, 2.2)), cls='ob-in3') +
  card('Policies', '<div class="fg">%s%s%s</div>' % (
      field('Attendance requirement', C.seg(['Required', 'Recommended', 'Optional'], 1)),
      field('Recording policy', C.seg(['Recorded for enrolled learners', 'Not recorded'], 0)),
      field('Office hours', C.seg(['Weekly', 'Fortnightly', 'None'], 0))), cls='ob-in3') +
  '<div class="ob-in4" style="margin-top: 16px">%s</div>' % nova_sg('Detected split: <b>88 % self-paced · 12 % instructor-led</b>. Saved to your course profile.<span class="spl"><span class="spl-b"><i style="width: 88%"></i></span></span>') +
  acts('STU-LX.dc.html'))

# ---------------------------------------------------------------- Learner Experience
P('lx', 'lx', 'Experience', page_head('Experience', 'Learner Experience', 'How learners move through the course, and what counts as completing it.') +
  card('Course navigation', '<div class="opt2">%s%s</div>' % (C.opt('<span class="o-t"><b>Sequential</b></span>', True, 'nav'), C.opt('<span class="o-t"><b>Flexible</b></span>', False, 'nav')), cls='ob-in2') +
  card('Completion requirements', '<div class="fg">%s%s%s</div>' % (
      chips(['Complete all lessons', 'Pass assessments', 'Submit final project'], {0, 1}, cls=''),
      field('Minimum score', '<span class="pct-w"><input class="ds-in pct" type="number" value="70" aria-label="Minimum score"><em>%</em></span>'),
      field('Minimum score applies to', C.seg(['Each assessment', 'Final exam only', 'Overall average'], 0), 'Assessment requirements for completion')), cls='ob-in3') +
  acts('STU-SUP.dc.html'))

# ---------------------------------------------------------------- Learner Support
def sup(t, tagt, d, on, k):
    kk = C.new(on)
    return '<button type="button" class="sp {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}"><span class="sp-t"><b>%s</b>%s<span>%s</span></span><span class="tg-s"><i></i></span></button>' % (
        kk, kk, kk, t, tag(tagt, 'green' if tagt == 'ENABLED' else ''), d)
FLOW = ['Learner question', 'AI Coach', 'Tutor', 'Answered · logged in Manage']
P('support', 'lx', 'Experience', page_head('Experience', 'Learner Support', 'How can learners get help? These settings connect to the course chat, tutor escalation and Manage → Learner Questions.') +
  '<section class="ds-card flw ob-in2"><ol>%s</ol></section>' % ''.join('<li><span class="flw-d">%d</span><b>%s</b></li>' % (i + 1, x) for i, x in enumerate(FLOW)) +
  '<div class="sps ob-in3">%s</div>' % ''.join([
      sup('AI Coach', 'ENABLED', 'Answers learner questions 24/7 using your course content. It cites the lesson it drew from.', True, 1),
      sup('Ask Tutor', 'ENABLED', 'Learners send a question to a human tutor from any lesson.', True, 2),
      sup('AI → Tutor escalation', 'ENABLED', 'When the AI Coach can’t resolve a question, it hands over to a tutor with the conversation attached.', True, 3),
      sup('Course Discussion', 'ENABLED', 'Public Q&A between learners and creators, separate from private support.', True, 4),
      sup('Office Hours', 'OPTIONAL', 'Scheduled live drop-in sessions with the creator team.', False, 5)]) +
  card('Tutor requests', '<div class="fg fg3">%s%s%s</div>' % (
      field('Who answers', selx(['Lead Creator', 'All co-creators', 'Assigned instructors'], 'All co-creators', 'Who answers tutor requests')),
      field('Response target', selx(['Within 24 hours', 'Within 48 hours', 'Within 72 hours'], 'Within 24 hours', 'Response target')),
      field('Office hours', selx(['Off', 'Weekly', 'Fortnightly'], 'Off', 'Office hours frequency'))), cls='ob-in4') +
  acts('STU-032.dc.html'))

# ---------------------------------------------------------------- CR-STU-032 Course Access Model
PROC = ['Credalio measures', 'Credalio derives', 'you review and select', 'validation confirms', 'you publish']
P('access', 'price', 'Experience', page_head('Experience', 'Course Access Model', 'How should learners access this course? This decides which pricing fields appear next.') +
  '<div class="am ob-in2">%s%s</div>' % (
      C.opt('<span class="am-v">%s</span><span class="o-t"><b>Subscription Only</b><span>Learners access this course using DLP from their Credalio subscription.</span><span class="am-f">%s</span></span>' % (
          coin(True), tag('DLP price from a permitted range', 'line')), False, 'am', 'amc'),
      C.opt('<span class="am-v">%s%s</span><span class="o-t"><b>Subscription + Marketplace</b><span>Learners can access it through their subscription, or buy lifetime course access with Marketplace Credits.</span><span class="am-f">%s%s%s</span></span>' % (
          coin(True), credit(True), tag('DLP price', 'line'), tag('Credit price', 'line'), tag('Maintenance burden', 'line')), True, 'am', 'amc')) +
  '<section class="ds-card flw ob-in3"><ol>%s</ol><p class="flw-n">You won’t type a price anywhere: you choose from ranges Credalio generates.</p></section>' % ''.join(
      '<li><span class="flw-d">%d</span><b>%s</b></li>' % (i + 1, x) for i, x in enumerate(PROC)) +
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
def rng(vals, sel, unit, coin_html):
    return '<div class="rg"><span class="rg-l"></span>%s</div>' % ''.join(
        '<button type="button" class="rg-p%s" aria-pressed="%s">%s<b>%s</b></button>' % (' on' if v == sel else '', 'true' if v == sel else 'false', coin_html, v) for v in vals)
def pricing(update):
    s_dlp, s_cr = ('700', '150') if update else (None, None)
    banner = ''
    if update:
        banner = ('<div class="bn bn-amb ob-in2"><span class="bn-i amb">%s</span><p><b>Pricing update required</b> Your course’s learning structure has changed significantly since pricing was selected. Previous DLP range: 500–700 DLP · Updated range: <b class="in">700–900 DLP</b>. Your price hasn’t been changed.</p>'
                  '<div class="bn-a"><a class="ds-ghost sm" href="#">Review Pricing</a></div></div>') % ic('warn', 18, 2)
    why = ('<details class="why"%s><summary>%s<span>Why this range?</span></summary><div class="why-b"><span class="fl-l">Based on:</span><ul>%s</ul><p>Credalio doesn’t publish its internal coefficients. <a class="ds-link sm" href="#">Learn about Credalio Pricing [link TO CONFIRM]</a></p></div></details>' % (
        '' if update else ' open', ic('down', 15, 2.2), ''.join('<li>%s</li>' % w for w in WHY)))
    return (page_head('Experience', 'Course Pricing', 'Choose your price from the range Credalio permits for this course. Pricing is provisional now and confirmed before publication.') + banner +
            '''<div class="g2 pg2 ob-in3">
<section class="ds-card fc"><div class="fc-h"><div><span class="pg-e">Subscription access</span><h2>Calculated course DLP: 795 DLP</h2></div></div>
<span class="rg-t">Credalio DLP range: <b>700–900 DLP</b></span>%s<p class="rg-s">Selected: <b>%s</b></p></section>
<section class="ds-card fc"><div class="fc-h"><div><span class="pg-e">Lifetime marketplace access</span><h2><a class="mbl" href="STU-033.dc.html">Maintenance burden: Medium %s</a></h2></div></div>
<span class="rg-t">Allowed Marketplace range: <b>130–210 Credits</b></span>%s<p class="rg-s">Selected: <b>%s</b>%s</p>%s</section>
</div>
<div class="wn info ob-in4">%s<span><b>DLP estimate ≠ creator price.</b> Calculated DLP is Credalio’s assessment of learning consumption. The permitted range comes from it, and you choose your price within that range.</span></div>''' % (
                rng(['700', '800', '900'], s_dlp, 'DLP', coin()), (s_dlp + ' DLP') if s_dlp else 'Not selected', ic('chev', 14, 2.2),
                rng(['130', '150', '170', '190', '210'], s_cr, 'Credits', credit()), (s_cr + ' Credits') if s_cr else 'Not selected',
                tip('Marketplace Credits purchase lifetime access to this course under Credalio’s marketplace terms.'), why, ic('info', 16, 2) if 'info' in EXTRA else ICON('<circle cx="12" cy="12" r="9"></circle><path d="M12 11v5"></path><path d="M12 7.6v.2"></path>', 16, 2)) +
            acts('STU-035.dc.html', 'Continue to summary'))
P('pricing', 'price', 'Experience', pricing(False))
P('pricingupd', 'price', 'Experience', pricing(True))

# ---------------------------------------------------------------- CR-STU-035 Access & Pricing Summary
P('psum', 'price', 'Experience', page_head('Experience', 'Access & Pricing Summary', 'What learners will be offered, pending validation.') +
  '''<section class="ds-card ps ob-in2">
<div class="ps-r"><span>Course access</span><b>Subscription + Marketplace</b></div>
<div class="ps-g"><div class="ps-c"><span>Subscription</span><b>%s800 DLP</b></div><div class="ps-c"><span>Lifetime access</span><b>%s170 Credits</b></div></div>
<div class="ps-r"><span>Maintenance burden</span><b>Medium · confirmed</b></div>
<div class="ps-r"><span>Pricing status</span>%s</div>
<p class="ps-n">Pricing status: Provisional. Final permitted pricing will be confirmed before publication.</p>
</section>''' % (coin(True), credit(True), tag('Provisional', 'amber')) +
  '<div class="ds-acts sb sv"><span class="sv-s"><a class="ds-ghost sm" href="STU-032.dc.html">Edit Access</a><a class="ds-ghost sm" href="STU-034.dc.html">Edit Pricing</a></span><span class="sv-r">%s</span></div>' % btn('Continue', '#'))

COURSE_CSS = stu2.EDITOR_CSS + r'''.it-i.sm{width:34px;height:34px;border-radius:10px}
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
.rcs{margin-top:16px;display:flex;flex-direction:column;gap:12px}
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
.mw-bar{margin-top:16px;display:flex;flex-wrap:wrap;align-items:center;gap:12px}
.mw-v{margin:0;flex:1;padding:8px 14px;background:#F5F8FF;border-color:#DCE5FB}
.mw-v p b{display:inline}
.mw{margin-top:16px;padding:6px 10px}
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
.am{margin-top:22px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.ds-opt.amc{flex-direction:column;align-items:flex-start;gap:16px;padding:24px;border-radius:20px}
.amc .ds-opt-ck{position:absolute;top:22px;right:22px;margin:0}
.am-v{display:flex;gap:8px}
.am-f{margin-top:10px;display:flex;flex-wrap:wrap;gap:6px}
.amc .o-t b{font-size:18px}
.amc .o-t > span{font-size:14px}
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
.pg2{align-items:stretch}
.rg-t{display:block;font-size:14px;color:#3A4566}
.rg-t b{font-weight:600;color:#0B1433}
.rg{position:relative;margin-top:18px;display:flex;justify-content:space-between;gap:8px}
.rg-l{position:absolute;left:24px;right:24px;top:50%;height:3px;margin-top:-1.5px;border-radius:3px;background:linear-gradient(90deg,#9DB8F7,#1652F0)}
.rg-p{position:relative;z-index:1;display:inline-flex;align-items:center;gap:6px;height:44px;padding:0 14px 0 8px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;font-family:inherit;font-size:14.5px;cursor:pointer}
.rg-p b{font-weight:600}
.rg-p:hover{border-color:#1652F0}
.rg-p.on{background:#1652F0;border-color:#1652F0;color:#FFFFFF;box-shadow:0 10px 22px -10px rgba(22,82,240,.7)}
.rg-s{margin:16px 0 0 0;display:flex;align-items:center;font-size:14px;color:#5B6582}
.rg-s b{margin-left:4px;font-weight:600;color:#0B1433}
.mbl{display:inline-flex;align-items:center;gap:4px;color:#0B1433;text-decoration:none}
.mbl:hover{color:#1652F0}
.why{margin-top:16px;border-top:1.5px solid #F0F2F8;padding-top:12px}
.why summary{display:inline-flex;align-items:center;gap:6px;cursor:pointer;font-size:14px;font-weight:600;color:#1652F0;list-style:none}
.why summary::-webkit-details-marker{display:none}
.why[open] summary svg{transform:rotate(180deg)}
.why-b{margin-top:10px;font-size:13.5px;color:#3A4566}
.why-b ul{margin:6px 0 0 0;padding-left:18px;display:flex;flex-direction:column;gap:3px}
.why-b p{margin:10px 0 0 0;font-size:13px;color:#5B6582}
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
.am{grid-template-columns:minmax(0,1fr)}
.kn{grid-template-columns:minmax(0,1fr)}
.mq{flex-direction:column;align-items:stretch;gap:10px}
.mb{grid-template-columns:minmax(0,1fr);gap:12px}
.rg{flex-wrap:wrap;justify-content:flex-start}
.rg-l{display:none}
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
