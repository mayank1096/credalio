"""Link 4 · Batch 2: Curriculum Builder + learning-item editors. Client copy is used word for word.

Builder.dc.html (props state: team | solo | open | co ; overlay: '' | add | mvl | mvc | del | delc)
    CR-STU-020 (+ SOLO / OPEN / CO-CREATOR), CR-STU-021 add item, move lesson, move chapter, delete item, delete chapter
Editor.dc.html  (props kind: video | text | live | assess | project ; overlay: '' | del)
    CR-STU-022A video, 022B text (+ delete), 022D live class, 024 assessment, 025 applied learning
"""
import json
from l4kit import *
from rail import *
from kit import coin

J = (M1, 'J')
A = (ME, 'A')
ABC = (None, 'AB')
WHO = {'A': 'Ada', 'J': 'John', 'AB': 'ABC Institute'}

ITEM_IC = {'video': 'play', 'text': 'file', 'quiz': 'quiz', 'inter': 'target', 'practice': 'edit', 'live': 'live', 'assign': 'project',
           'project': 'project', 'pdf': 'file'}
ITEM_IC2 = dict(ITEM_IC, assign='assigned', project='rocket')
EXTRA['rocket'] = '<path d="M5 15c-1.5 1.5-2 4-2 6 2 0 4.5-.5 6-2"></path><path d="M9 15 15 9"></path><path d="M14.5 3.5C18 3 21 6 20.5 9.5L15 15l-6-6z"></path><path d="m9 9-4 1-2 3 4 1M15 15l-1 4-3 2-1-4"></path>'
EXTRA['assigned'] = I['assigned']
EXTRA['up'] = '<path d="m6 15 6-6 6 6"></path>'
EXTRA['move'] = '<path d="M5 9 2 12l3 3M9 5l3-3 3 3M15 19l-3 3-3-3M19 9l3 3-3 3M2 12h20M12 2v20"></path>'
EXTRA['trash'] = '<path d="M4 7h16M10 11v6M14 11v6M6 7l1 13h10l1-13M9 7V4h6v3"></path>'
EXTRA['eye'] = '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"></path><circle cx="12" cy="12" r="3"></circle>'
EXTRA['clip'] = '<path d="M21 11.5 12.5 20a5 5 0 0 1-7-7L14 4.5a3.5 3.5 0 0 1 5 5L10.5 18a2 2 0 0 1-3-3L15 7.5"></path>'
EXTRA['copy'] = '<rect x="8" y="8" width="12" height="12" rx="2"></rect><path d="M16 8V6a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h2"></path>'
EXTRA['more'] = '<circle cx="5" cy="12" r="1.3"></circle><circle cx="12" cy="12" r="1.3"></circle><circle cx="19" cy="12" r="1.3"></circle>'
EXTRA['audio'] = '<path d="M3 14v-2a9 9 0 0 1 18 0v2"></path><rect x="3" y="14" width="4" height="7" rx="2"></rect><rect x="17" y="14" width="4" height="7" rx="2"></rect>'
EXTRA['slides'] = '<rect x="3" y="4" width="18" height="12" rx="2"></rect><path d="M12 16v4M8 20h8"></path>'
EXTRA['link'] = '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"></path><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"></path>'
EXTRA['download'] = '<path d="M12 4v11M7 10l5 5 5-5"></path><path d="M4 19h16"></path>'
EXTRA['bold'] = '<path d="M7 5h6a3.5 3.5 0 0 1 0 7H7zM7 12h7a3.5 3.5 0 0 1 0 7H7z"></path>'
EXTRA['table'] = '<rect x="3" y="4" width="18" height="16" rx="2"></rect><path d="M3 10h18M3 15h18M9 4v16"></path>'
EXTRA['code'] = '<path d="m8 8-4 4 4 4M16 8l4 4-4 4M14 5l-4 14"></path>'
EXTRA['bulb'] = '<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-4 10.5c.7.7 1 1.5 1 2.5h6c0-1 .3-1.8 1-2.5A6 6 0 0 0 12 3z"></path>'
EXTRA['cap'] = '<rect x="3" y="5" width="18" height="14" rx="2"></rect><path d="M10 10.5a2 2 0 1 0 0 3M16 10.5a2 2 0 1 0 0 3"></path>'

def ppl(codes, size=24):
    return stack([{'A': A, 'J': J, 'AB': ABC}[c] for c in codes], size)

def names(codes):
    return ' + '.join(WHO[c] for c in codes)

# (kind, title, type, tier, dur, dlp, complete, required, who, comments, href_edit, edit_label)
CH = [
    ('Introduction to Data Analysis', '3 items', '40m', '60', 'Complete all required items', ['A', 'J'], [
        ('video', 'What is Data Analysis?', 'Video', 'Intermediate', '12 min', '20 DLP', 'Complete: Watch ≥ 70%', True, ['A'], 0, '#', 'Edit'),
        ('text', 'The Analytics Workflow', 'Text + PDF', None, '18 min', '25 DLP', 'Complete: Reach the end', True, ['A'], 0, '#', 'Edit'),
        ('quiz', 'Knowledge Check', 'Knowledge Check · 5 questions', None, '10 min', '15 DLP', 'Complete: Submit', True, ['A'], 0, '#', 'Edit assessment')],
     ['Data Analysis Handbook.pdf', 'Course Worksheet.xlsx']),
    ('SQL Foundations', '4 items', '1h 23m', '135', 'Complete 3 of 4 required', ['J'], [
        ('video', 'Databases and Tables', 'Video', 'Beginner', '16 min', '25 DLP', 'Complete: Watch ≥ 70%', True, ['J'], 0, '#', 'Edit'),
        ('inter', 'SELECT Statements', 'Interactive', 'Intermediate', '22 min', '35 DLP', None, True, ['J'], 0, '#', 'Edit'),
        ('practice', 'Your First Queries', 'Practice Activity', 'Advanced', '30 min', '50 DLP', 'Complete: Submit', True, ['J'], 0, '#', 'Edit'),
        ('quiz', 'Quiz 1', 'Quiz · 10 questions', None, '15 min', '25 DLP', 'Complete: Achieve ≥ 70%', True, ['A'], 0, 'STU-024.dc.html', 'Edit assessment')], []),
    ('Joining Tables', '3 items', '58m', '90', 'Complete all required items', ['J', 'A'], [
        ('video', 'Joining Tables with SQL', 'Video', 'Intermediate', '18 min', '30 DLP', 'Complete: Watch ≥ 70%', True, ['J'], 0, 'STU-022A.dc.html', 'Edit'),
        ('text', 'INNER vs LEFT JOIN', 'Text / Article', None, '15 min', '20 DLP', 'Complete: Reach the end', True, ['A', 'J'], 2, 'STU-022B.dc.html', 'Edit'),
        ('practice', 'Practice Joins', 'Practice Activity', 'Beginner', '25 min', '40 DLP', 'Complete: Submit', True, ['J'], 1, '#', 'Edit')],
     ['SQL Joins Cheat Sheet.pdf', 'Practice Dataset.csv']),
    ('Analysing Business Data', '3 items', '2h 5m', '210', 'Complete all required items', ['A', 'AB'], [
        ('video', 'Aggregations and GROUP BY', 'Video', 'Intermediate', '20 min', '35 DLP', 'Complete: Watch ≥ 70%', True, ['A'], 0, '#', 'Edit'),
        ('live', 'Analysis Clinic', 'Live Class', 'Advanced', '60 min', '100 DLP', 'Complete: Attend ≥ 70%', False, ['AB'], 0, 'STU-022D.dc.html', 'Edit'),
        ('assign', 'Sales Analysis', 'Assignment', 'Intermediate', '45 min', '75 DLP', 'Complete: Receive a passing evaluation', True, ['A'], 0, '#', 'Edit')], []),
    ('Communicating Findings', '3 items', '2h 59m', '300', 'Complete all required items', ['A'], [
        ('video', 'Storytelling with Data', 'Video', 'Beginner', '14 min', '25 DLP', 'Complete: Watch ≥ 70%', True, ['A'], 0, '#', 'Edit'),
        ('project', 'Final Project', 'Project', 'Intermediate', '120 min', '200 DLP', 'Complete: Pass the rubric', True, ['A'], 0, 'STU-025.dc.html', 'Edit'),
        ('quiz', 'Final Exam', 'Exam · 20 questions', None, '45 min', '75 DLP', 'Complete: Pass', True, ['A', 'J'], 0, '#', 'Edit assessment')], []),
]

def ibtn(icon, label, href='#', cls=''):
    return '<a class="ib%s" href="%s" aria-label="%s">%s</a>' % ((' ' + cls) if cls else '', href, label, ic(icon, 16, 2))

def item_row(ci, ii, it, mode):
    kind, title, typ, tier, dur, dlp, comp, req, who, com, href, elabel = it
    meta = [typ] + ([tier] if tier else []) + [dur, dlp]
    m = ' · '.join(meta)
    c = ('<span class="it-warn">%s<span>No completion rule</span></span>' % ic('warn', 13, 2.2)) if comp is None else '<span>%s</span>' % comp
    team = mode in ('team', 'open', 'co')
    right = tag('REQUIRED' if req else 'OPTIONAL', 'blue' if req else '')
    if team:
        right += ppl(who, 26)
    if mode == 'co':
        right += ('<a class="ds-ghost xs" href="%s">Edit</a>' % href) if 'J' in who else '<span class="it-lock">%s<span>View only</span></span>' % ic('lock', 13, 2)
    else:
        mv = 'STU-020-MVL.dc.html' if (ci, ii) == (0, 0) else '#'
        dl = 'STU-020-DEL.dc.html' if (ci, ii) == (2, 1) else '#'
        right += ('<span class="it-act"><span class="ud">%s%s</span><a class="ds-ghost xs" href="%s">%s</a>%s%s</span>' %
                  (ibtn('up', 'Move up'), ibtn('down', 'Move down'), href, elabel, ibtn('move', 'Move', mv), ibtn('trash', 'Delete', dl, 'del')))
    cm = ('<span class="it-cm">%s%d</span>' % (ic('chat', 12, 2), com)) if com and team else ''
    return ('<div class="it"><span class="it-i k-%s">%s</span><div class="it-b"><div class="it-t"><span class="it-n">%d.</span><b>%s</b>%s</div>'
            '<div class="it-m"><span>%s</span><i></i>%s</div></div><div class="it-r">%s</div></div>') % (
        kind, ic(ITEM_IC2[kind], 17), ii + 1, title, cm, m, c, right)

def chapter(ci, ch, mode):
    title, n, dur, dlp, rule, who, items, res = ch
    team = mode in ('team', 'open', 'co')
    assign = ''
    if team:
        assign = '<span class="ch-as"><em>Assigned:</em>%s<span>%s</span>%s</span>' % (ppl(who, 22), names(who), '' if mode == 'co' else '<a class="ds-link sm" href="#">+ Assign</a>')
    if mode == 'co':
        tools = '<a class="ds-link sm" href="#">Edit</a><a class="ds-link sm" href="#">Add Resources</a>'
    else:
        mvc = 'STU-020-MVC.dc.html' if ci == 0 else '#'
        delc = 'STU-020-DELC.dc.html' if ci == 1 else '#'
        tools = ('<a class="ds-link sm" href="#">Edit</a><a class="ds-link sm" href="#">Add Resources</a><a class="ds-link sm" href="#">Duplicate</a>'
                 '<span class="ud">%s%s</span><a class="ds-link sm" href="%s">Move…</a><button type="button" class="nv-chip xs">%s<span>Suggest</span></button>'
                 '<a class="ds-link sm del" href="%s">Delete chapter</a>') % (ibtn('up', 'Move chapter up'), ibtn('down', 'Move chapter down'), mvc, SPARK, delc)
    rows = ''.join(item_row(ci, ii, it, mode) for ii, it in enumerate(items))
    resh = ''
    if res:
        resh = '<div class="ch-res"><span class="ch-rl">Chapter resources</span>%s</div>' % ''.join('<a class="rs-f" href="#">%s<span>%s</span></a>' % (ic('clip', 14, 2), r) for r in res)
    add = '' if mode == 'co' else '<a class="ch-add" href="%s">%s<span>Add Learning Item</span></a>' % ('STU-021.dc.html' if ci == 1 else '#', ic('plus', 16, 2.2))
    return ('<section class="ds-card ch"><header class="ch-h"><div class="ch-hl"><span class="ch-k">Chapter %d</span><h2>%s</h2>'
            '<div class="ch-m"><span>%s</span><i></i><span>%s</span><i></i><span>%s DLP</span><i></i><span>%s</span></div></div>%s</header>'
            '<div class="ch-tools">%s</div><div class="ch-items">%s</div>%s%s</section>') % (ci + 1, title, n, dur, dlp, rule, assign, tools, rows, resh, add)

def stat(v, l):
    return '<span class="cs-s"><b>%s</b><em>%s</em></span>' % (v, l)

def builder(mode):
    head_btns = '<a class="ds-ghost sm" href="#">%s<span>Preview</span></a>' % ic('eye', 16, 2)
    if mode in ('team', 'open', 'co'):
        head_btns += '<a class="ds-ghost sm" href="STU-030.dc.html">%s<span>Team Chat</span></a>' % ic('chat', 16, 2)
    if mode != 'co':
        head_btns += '<a class="ds-ghost sm" href="#">%s<span>Add Chapter</span></a>' % ic('plus', 16, 2.2)
    head_btns += nchip('Review')
    quick = [('check', 'Completion rules', 'STU-027.dc.html'), ('clip', 'Resource library', 'STU-026.dc.html'), ('users', 'Team & assignments', 'STU-028.dc.html') if mode != 'solo' else ('assigned', 'My work', 'STU-028-SOLO.dc.html'), ('analytics', 'DLP & effort', 'STU-031.dc.html')]
    banner = ''
    if mode == 'open':
        banner = ('<div class="bn bn-open ob-in2"><span class="bn-i">%s</span><p><b>Open for collaboration · live</b> Looking for: SQL reviewer (Content Contributor) · 3 applications waiting. Only you can accept applicants.</p>'
                  '<div class="bn-a"><a class="ds-ghost sm" href="#">Review applications</a><a class="ds-link sm" href="#">Manage opportunity</a></div></div>') % ic('globe', 18)
    if mode == 'co':
        banner = ('<div class="bn ob-in2">%s<p><b>You are viewing as a Co-Creator · Dr. John Adeyemi</b> You can edit the lessons assigned to you. Only the owner (Ada) can add or remove chapters, move lessons, change assignments or publish.</p></div>') % av(M1, 'J', 36)
    cons = ('<section class="ds-card rx cs2 ob-in2"><span class="rx-k">Course consumption</span><b class="cs2-t">5 chapters · 16 learning items</b>'
            '<div class="cs2-r">%s<span class="cs2-h"><b>31%%</b><em>Course Health</em></span></div>'
            '<div class="cs2-st">%s%s</div><nav class="cs2-q" aria-label="Curriculum tools">%s</nav></section>') % (
        ring(31, 76, 11),
        stat('8h 5m', 'Estimated learning time'), stat('795 DLP', 'Estimated DLP' + tip('Calculated by Credalio from each item’s duration, reading time or expected effort. This is the estimate, not what learners consume under the access policy. Formula per DLP policy [TO CONFIRM].', 'r')),
        ''.join('<a class="cs-ql" href="%s">%s<span>%s</span>%s</a>' % (h, ic(i, 15, 2), l, ic('chev', 14, 2)) for i, l, h in quick))
    nova = ('<section class="rn nova-card ob-in3"><header class="rn-h">%s<span><b>Nova</b><em>Creator Copilot · %s</em></span><span class="rn-c">2</span></header>'
            '<div class="rn-s"><p>“SELECT Statements” is marked required, but no completion rule has been configured.</p><button type="button" class="ds-ghost xs">Set Completion Rule</button></div>'
            '<div class="rn-s"><p>Outcome 4 requires learners to “Understand SQL”, but the curriculum has no practice or assessment for it.</p><button type="button" class="ds-ghost xs">Add Practice</button></div>'
            '<footer><b>Nova</b> proposes. You approve every change.</footer></section>') % (nova_av(), COURSE)
    main = '%s<div class="chs ob-in3">%s</div>%s' % (banner, ''.join(chapter(ci, ch, mode) for ci, ch in enumerate(CH)),
                                                   ('' if mode == 'co' else '<a class="ch-add big" href="#">%s<span>Add Chapter</span></a>' % ic('plus', 18, 2.2)))
    return (page_head('Build', 'Curriculum Builder', 'The learner journey, chapter by chapter. Add any learning item (content, assessments, practice, live classes) and Credalio estimates its learning time and DLP as you go.', head_btns) +
            '<div class="wk bw"><div class="wk-m">%s</div>%s<aside class="wk-r">%s%s</aside></div>' % (
                main, acts('#').replace('class="ds-acts sb sv"', 'class="ds-acts sb sv wk-a"'), cons, nova))

# ---------- overlays (builder)
B = Toggles()
ADD_GROUPS = [('Teach', [('play', 'Video', 'Upload a video'), ('file', 'Text / Article', 'Written lesson'), ('file', 'PDF / Document', 'Upload a document'),
                         ('audio', 'Audio', 'Upload audio'), ('slides', 'Presentation', 'Slides'), ('live', 'Live Class', 'Scheduled session')]),
              ('Check understanding', [('quiz', 'Assessment', 'Knowledge check, quiz or exam')]),
              ('Apply', [('edit', 'Practice Activity', 'Guided hands-on work'), ('assigned', 'Assignment', 'Submitted work'), ('rocket', 'Project', 'Larger applied work')]),
              ('Engage', [('chat', 'Discussion', 'Prompted conversation')]),
              ('Support', [('link', 'External Resource', 'Link to outside content'), ('download', 'Downloadable Resource', 'File learners keep')])]
OV_ADD = '''<div class="ov-scrim"></div>
<aside class="dr" role="dialog" aria-modal="true" aria-label="Add to Chapter 2">
<header class="dr-h"><div><span class="pg-e">Add to Chapter 2</span><h2>What would you like to add?</h2></div><a class="ds-x" href="STU-020.dc.html" aria-label="Close">%s</a></header>
<div class="dr-b">%s</div>
</aside>''' % (ic('x', 18, 2.2), ''.join('<div class="ag"><span class="ag-l">%s</span><div class="ag-g">%s</div></div>' % (g, ''.join(
    '<a class="at" href="%s"><span class="at-i">%s</span><b>%s</b><span>%s</span></a>' % ('STU-024.dc.html' if l == 'Assessment' else '#', ic(i, 18), l, d) for i, l, d in its)) for g, its in ADD_GROUPS))

def dlg(title, body, primary, cancel='STU-020.dc.html', danger=False, icon=''):
    pb = ('<a class="ds-btn danger" href="%s"><span>%s</span></a>' % (cancel, primary)) if danger else btn(primary, cancel)
    return '''<div class="ov-scrim"></div>
<div class="dl" role="dialog" aria-modal="true" aria-label="%s">
<header class="dl-h">%s<h2>%s</h2><a class="ds-x sm" href="%s" aria-label="Close">%s</a></header>
<div class="dl-b">%s</div>
<footer class="dl-f"><a class="ds-ghost" href="%s">Cancel</a>%s</footer>
</div>''' % (title.replace('“', '').replace('”', ''), ('<span class="dl-i%s">%s</span>' % (' danger' if danger else '', icon)) if icon else '', title, cancel, ic('x', 16, 2.2), body, cancel, pb)

CHAPS = ['Ch 1 · Introduction to Data Analysis', 'Ch 2 · SQL Foundations', 'Ch 3 · Joining Tables', 'Ch 4 · Analysing Business Data', 'Ch 5 · Communicating Findings']
POS = ['1 (first)', '2', '3', '4', '5 (last)']
OV_MVL = dlg('Move “What is Data Analysis?”',
             '<span class="dl-l">Move to chapter</span><div class="rl">%s</div><span class="dl-l">Position in that chapter</span>%s<p class="dl-n">%s<span>It moves to Chapter 2, position 2. Chapter times and DLP update. Completion rules and comments move with it. Assignments stay with the lesson.</span></p>' % (
                 ''.join(B.opt('<span class="o-t"><b>%s</b></span>' % c, i == 1, 'mvl', 'sm') for i, c in enumerate(CHAPS)), B.seg(POS, 1), ic('info', 15, 2) if 'info' in EXTRA else ''),
             'Move lesson', icon=ic('move', 18, 2))
OV_MVC = dlg('Move Chapter 1 · Introduction to Data Analysis',
             '<span class="dl-l">Move to position</span>%s<p class="dl-n"><span>Chapter 1 becomes Chapter 3. Its lessons, DLP and assignments move with it.</span></p>' % B.seg(POS, 2),
             'Move chapter', icon=ic('move', 18, 2))
OV_DEL = dlg('Delete “INNER vs LEFT JOIN”?',
             '<ul class="dl-ul"><li>Removes it from Chapter 3 (−15 min, −20 estimated DLP)</li><li>Assigned to Ada + John. They’ll see the change in Team Chat.</li></ul>',
             'Delete learning item', danger=True, icon=ic('trash', 18, 2))
OV_DELC = dlg('Delete Chapter 2 · SQL Foundations?',
              '<ul class="dl-ul"><li>4 learning items · 1h 23m · 135 estimated DLP</li><li>Assigned to John</li></ul><div class="rl">%s%s</div><span class="dl-l">Move the items to</span>%s<p class="dl-n"><span>Only the Lead Creator can delete a chapter [TO CONFIRM]. Collaborators can delete items assigned to them.</span></p>' % (
                  B.opt('<span class="o-t"><b>Delete the chapter and its 4 items</b></span>', False, 'delc', 'sm'),
                  B.opt('<span class="o-t"><b>Move the items to another chapter first</b></span>', True, 'delc', 'sm'),
                  sel('Chapter 1 · Introduction to Data Analysis', 'Move the items to')),
              'Move items & delete chapter', danger=True, icon=ic('trash', 18, 2))
CHAT = [((M1, 'J'), 'John', 'Mon 10:12', 'I’ve finished Chapter 3. Can you review the practical exercise?', False),
        ((ME, 'A'), 'Ada', 'Mon 10:40', 'Yes. I think we should connect it to Outcome 4.', True),
        ((None, 'AB'), 'ABC Institute', 'Mon 14:05', 'We can run the Analysis Clinic live on Thursdays.', False)]
OV_CHAT = '''<a class="cp-ov" href="STU-020.dc.html" aria-label="Close Team Chat"></a>
<aside class="cp" role="dialog" aria-label="Course Team">
<header class="cp-h"><span class="cp-tv">%s</span><span class="cp-n"><b>Course Team</b><span>Linked to Course ID CRS-00284 · not a general chat</span></span>
<a class="cp-tb cp-x1" href="STU-020.dc.html" aria-label="Close">%s</a></header>
<div class="cp-r"><span class="cp-mem">%s<span>Ada · John · ABC Institute</span></span><div class="cp-seg" role="tablist" aria-label="Copilot panel"><button type="button" role="tab" aria-selected="false">Nova</button><button type="button" role="tab" class="on" aria-selected="true">Team</button></div></div>
<div class="cp-b">%s</div>
<footer class="cp-f"><div class="cp-in"><label class="sr-only" for="tm-msg">Message the course team</label><input id="tm-msg" placeholder="Message the team, @mention someone"><button type="button" class="cp-send">Send</button></div></footer>
</aside>''' % (ic('chat', 20, 2), ic('x', 16, 2.4), ppl(['A', 'J', 'AB'], 24),
               ''.join('<div class="tm%s">%s<div class="tm-b"><span class="tm-h"><b>%s</b> · %s</span><div class="cp-m%s">%s</div></div></div>' % (
                   ' me' if me else '', av(p[0], p[1], 30), n, w, ' cp-me' if me else '', t) for p, n, w, t, me in CHAT))
OVS = {'add': OV_ADD, 'mvl': OV_MVL, 'mvc': OV_MVC, 'del': OV_DEL, 'delc': OV_DELC, 'chat': OV_CHAT}

MODES = ['team', 'solo', 'open', 'co']
BUILDER_BODY = '''<div class="ds-root">
%s
<div style="min-width: 0; display: flex; flex-direction: column">
<sc-if value="{{m_solo}}" hint-placeholder-val="{{ false }}">%s</sc-if>
<sc-if value="{{teamTop}}" hint-placeholder-val="{{ true }}">%s</sc-if>
<main class="ds-main">
%s
</main>
</div>
</div>
%s''' % (sidebar('cb'), topbar(solo=True, phase='Build'), topbar(phase='Build'),
         '\n'.join('<sc-if value="{{m_%s}}" hint-placeholder-val="{{ %s }}">%s</sc-if>' % (m, 'true' if m == 'team' else 'false', builder(m)) for m in MODES),
         '\n'.join('<sc-if value="{{o_%s}}" hint-placeholder-val="{{ false }}">%s</sc-if>' % (k, v) for k, v in OVS.items()))

BUILDER_JS = B.js() + '''class Component extends DCLogic {
  renderVals() {
    var m = this.props.state || 'team', o = this.props.overlay || '';
    var v = togVals(this), self = this;
    %s.forEach(function (k) { v['m_'.concat(k)] = k === m; });
    %s.forEach(function (k) { v['o_'.concat(k)] = k === o; });
    v.teamTop = m !== 'solo';
    v.navCls = this.state.nav ? 'ds-open' : '';
    v.toggleNav = function () { self.setState({ nav: !self.state.nav }); };
    return v;
  }
}''' % (json.dumps(MODES), json.dumps(list(OVS)))

BUILDER_CSS = r'''.ds-ghost.sm{height:40px;padding:0 16px;font-size:14px;gap:7px}
.ds-ghost.xs{height:32px;padding:0 12px;font-size:13px;border-width:1.5px}
.ds-link.sm{font-size:13.5px}
.ds-link.del,.ds-link.del:hover{color:#B42318}
.nv-chip.xs{height:30px;padding:0 11px;font-size:12.5px}
.pg-hr{flex-wrap:wrap;justify-content:flex-end}
.cs{margin-top:22px;padding:20px 24px;display:grid;grid-template-columns:auto minmax(0,1fr);align-items:center;gap:16px 32px}
.cs-l b{display:block;font-size:19px;font-weight:600;letter-spacing:-0.01em}
.cs-st{display:flex;justify-content:flex-end;gap:10px}
.cs-s{display:flex;flex-direction:column;gap:2px;min-width:140px;padding:12px 16px;border-radius:14px;background:#F7F9FD}
.cs-s b{font-size:21px;font-weight:600;letter-spacing:-0.02em}
.cs-s em{display:flex;align-items:center;font-style:normal;font-size:12.5px;color:#5B6582}
.cs-q{grid-column:1 / -1;display:flex;flex-wrap:wrap;gap:8px;padding-top:16px;border-top:1.5px solid #F0F2F8}
.cs-ql{display:inline-flex;align-items:center;gap:8px;height:36px;padding:0 14px;border-radius:999px;background:#F5F8FF;color:#0E3BB8;font-size:13.5px;font-weight:500;text-decoration:none}
.cs-ql:hover{background:#EAF0FF}
.bn{margin-top:14px;display:flex;align-items:center;gap:14px;padding:14px 16px;border-radius:16px;background:#FFFFFF;border:1.5px solid #E6EAF3}
.bn p{margin:0;flex:1;min-width:0;font-size:14px;line-height:1.5;color:#3A4566}
.bn p b{display:block;color:#0B1433;font-weight:600}
.bn-open{background:linear-gradient(120deg,#F2F6FF,#E8EFFF);border-color:#C9D7FA}
.bn-i{width:40px;height:40px;flex-shrink:0;border-radius:12px;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.bn-a{display:flex;align-items:center;gap:16px;flex-shrink:0}
.nv-st{margin-top:14px;display:flex;flex-direction:column;gap:10px}
.chs{margin-top:22px;display:flex;flex-direction:column;gap:16px}
.ch{padding:22px 24px 18px 24px}
.ch-h{display:flex;align-items:flex-start;justify-content:space-between;gap:20px}
.ch-k{display:block;font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:#1652F0}
.ch-h h2{margin:4px 0 0 0;font-size:20px;font-weight:600;letter-spacing:-0.015em}
.ch-m{margin-top:6px;display:flex;flex-wrap:wrap;align-items:center;gap:6px 8px;font-size:13.5px;color:#5B6582}
.ch-m i,.it-m i{width:3px;height:3px;border-radius:50%;background:#AEB6CC}
.ch-as{display:inline-flex;align-items:center;gap:8px;flex-shrink:0;padding:6px 8px 6px 12px;border-radius:999px;background:#F7F9FD;font-size:13px;color:#3A4566}
.ch-as em{font-style:normal;color:#8A93AD}
.ch-as .avs .av + .av{margin-left:-6px}
.ch-tools{margin:14px 0 6px 0;display:flex;flex-wrap:wrap;align-items:center;gap:6px 18px;padding-bottom:14px;border-bottom:1.5px solid #F0F2F8}
.ud{display:inline-flex;gap:2px}
.ib{width:30px;height:30px;padding:0;border:0;border-radius:9px;background:none;display:inline-flex;align-items:center;justify-content:center;color:#5B6582;text-decoration:none;cursor:pointer}
.ib:hover{background:#F1F3F8;color:#0B1433}
.ib.del:hover{background:#FDECEA;color:#B42318}
.ch-items{display:flex;flex-direction:column}
.it{display:flex;align-items:center;gap:14px;padding:12px 6px;border-radius:14px}
.it + .it{box-shadow:0 -1.5px 0 #F0F2F8}
.it:hover{background:#F9FAFD}
.it-i{width:40px;height:40px;flex-shrink:0;border-radius:12px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.it-b{flex:1;min-width:0}
.it-t{display:flex;align-items:center;gap:8px}
.it-n{font-size:14px;color:#8A93AD;font-weight:500}
.it-t b{font-size:15px;font-weight:600}
.it-cm{display:inline-flex;align-items:center;gap:4px;height:22px;padding:0 8px;border-radius:999px;background:#EAF0FF;color:#0E3BB8;font-size:12px;font-weight:500}
.it-m{margin-top:4px;display:flex;flex-wrap:wrap;align-items:center;gap:4px 8px;font-size:13px;color:#5B6582}
.it-warn{display:inline-flex;align-items:center;gap:5px;color:#8A5A00;font-weight:500}
.it-warn svg{color:#B76E00}
.it-r{display:flex;align-items:center;gap:10px;flex-shrink:0}
.it-r .avs .av + .av{margin-left:-6px}
.it-act{display:inline-flex;align-items:center;gap:4px}
.it-act .ds-ghost{margin:0 4px;min-width:64px;justify-content:center}
.it-lock{display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 12px;border-radius:999px;background:#F1F3F8;color:#5B6582;font-size:13px;font-weight:500}
.ch-res{margin-top:6px;padding:12px 6px 4px 6px;display:flex;flex-wrap:wrap;align-items:center;gap:8px;border-top:1.5px solid #F0F2F8}
.ch-rl{font-size:12px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;color:#8A93AD;margin-right:4px}
.rs-f{display:inline-flex;align-items:center;gap:7px;height:32px;padding:0 12px;border-radius:999px;border:1.5px solid #E6EAF3;color:#0B1433;font-size:13px;font-weight:500;text-decoration:none}
.rs-f svg{color:#5B6582}
.ch-add{margin-top:10px;display:flex;align-items:center;justify-content:center;gap:8px;height:46px;border-radius:14px;border:1.5px dashed #C9D2E6;color:#1652F0;font-size:14px;font-weight:600;text-decoration:none;transition:background .2s ease,border-color .2s ease}
.ch-add:hover{background:#F5F8FF;border-color:#1652F0}
.ch-add.big{margin-top:16px;height:60px;border-radius:18px;background:#FFFFFF}
.ov-scrim{position:fixed;inset:0;z-index:1000;background:rgba(11,20,51,.38)}
.dr{position:fixed;z-index:1001;top:0;right:0;bottom:0;width:560px;max-width:100vw;box-sizing:border-box;background:#FFFFFF;display:flex;flex-direction:column;box-shadow:-24px 0 64px rgba(11,20,51,.18);font-family:'Google Sans','Google Sans Text','Helvetica Neue',system-ui,sans-serif;color:#0B1433}
.dr-h{display:flex;align-items:flex-start;justify-content:space-between;gap:16px;padding:26px 28px 18px 28px;border-bottom:1.5px solid #EEF1F7}
.dr-h h2{margin:0;font-size:22px;font-weight:600;letter-spacing:-0.02em}
.dr-b{flex:1;overflow-y:auto;padding:8px 28px 28px 28px}
.ag{margin-top:18px}
.ag-l{display:block;margin-bottom:10px;font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:#8A93AD}
.ag-g{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.at{display:flex;flex-direction:column;gap:4px;padding:14px;border-radius:14px;border:1.5px solid #E6EAF3;color:#0B1433;text-decoration:none;transition:border-color .2s ease,box-shadow .2s ease}
.at:hover{border-color:#1652F0;box-shadow:0 10px 24px -14px rgba(22,82,240,.5)}
.at-i{width:36px;height:36px;margin-bottom:6px;border-radius:11px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.at b{font-size:14px;font-weight:600}
.at span{font-size:12.5px;line-height:1.4;color:#5B6582}
.dl{position:fixed;z-index:1001;left:50%;top:50%;transform:translate(-50%,-50%);width:540px;max-width:calc(100vw - 32px);max-height:calc(100vh - 48px);overflow-y:auto;box-sizing:border-box;border-radius:24px;background:#FFFFFF;box-shadow:0 40px 90px -30px rgba(11,20,51,.5);font-family:'Google Sans','Google Sans Text','Helvetica Neue',system-ui,sans-serif;color:#0B1433}
.dl-h{position:relative;display:flex;flex-direction:column;align-items:center;gap:14px;padding:28px 56px 0 56px;text-align:center}
.dl-h > .ds-x{position:absolute;top:14px;right:14px}
.dl-h h2{margin:0;font-size:20px;line-height:1.3;font-weight:600;letter-spacing:-0.015em}
.dl-i{width:44px;height:44px;flex-shrink:0;border-radius:14px;background:#EAF0FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.dl-i.danger{background:#FDECEA;color:#B42318}
.ds-x.sm{width:36px;height:36px;border-color:transparent;color:#5B6582}
.dl-b{padding:16px 24px 4px 24px;display:flex;flex-direction:column;gap:10px}
.dl-l{margin-top:6px;font-size:13.5px;font-weight:600}
.dl-n{margin:8px 0 0 0;display:flex;gap:8px;padding:12px 14px;border-radius:12px;background:#F7F9FD;font-size:13.5px;line-height:1.5;color:#3A4566}
.dl-ul{margin:0;padding:0 0 0 18px;display:flex;flex-direction:column;gap:6px;font-size:14.5px;line-height:1.5;color:#3A4566}
.dl-f{display:flex;justify-content:center;gap:10px;padding:20px 24px 24px 24px}
.rl{display:flex;flex-direction:column;gap:8px}
.ds-opt.sm{padding:12px 14px;border-radius:12px}
.ds-opt.sm .o-t b{font-size:14px;font-weight:500}
.ds-btn.danger{background:#B42318;padding:0 24px;box-shadow:0 10px 24px rgba(180,35,24,.24)}
.ds-btn.danger:hover{background:#912018}
.o-t{display:flex;flex-direction:column;gap:3px;min-width:0}
.o-t b{font-size:15px;font-weight:600}
.cp-ov{position:fixed;left:0;right:0;top:72px;bottom:0;z-index:1000;background:linear-gradient(90deg,rgba(247,249,253,0) 0%,rgba(11,20,51,.10) 100%)}
.cp{position:fixed;z-index:1001;top:72px;right:0;bottom:0;width:440px;max-width:100vw;box-sizing:border-box;display:flex;flex-direction:column;background:#FFFFFF;border-left:1.5px solid #E6EAF3;box-shadow:-24px 0 64px rgba(11,20,51,.12);font-family:'Google Sans','Google Sans Text','Helvetica Neue',system-ui,sans-serif;color:#0B1433}
.cp-h{display:flex;align-items:center;gap:12px;padding:16px 16px 14px 20px;border-bottom:1.5px solid #F0F2F8}
.cp-tv{width:46px;height:46px;flex-shrink:0;border-radius:50%;background:#EAF0FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.cp-n{flex-grow:1;display:flex;flex-direction:column;gap:1px;min-width:0}
.cp-n b{font-size:18px;font-weight:600}
.cp-n span{font-size:13px;color:#5B6582}
.cp-tb{height:38px;padding:0 14px;border-radius:10px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;font-family:inherit;font-size:14px;font-weight:600;cursor:pointer;text-decoration:none}
.cp-tb:hover{border-color:#1652F0}
.cp-x1{width:38px;padding:0;display:flex;align-items:center;justify-content:center;box-sizing:border-box}
.cp-r{display:flex;align-items:center;gap:10px;padding:12px 16px 12px 20px;border-bottom:1.5px solid #F0F2F8}
.cp-mem{flex:1;min-width:0;display:inline-flex;align-items:center;gap:8px;font-size:13px;color:#3A4566}
.cp-mem .avs .av + .av{margin-left:-6px}
.cp-seg{display:flex;gap:4px;flex-shrink:0}
.cp-seg button{height:34px;padding:0 14px;border-radius:999px;border:0;background:#F1F3F8;color:#3A4566;font-family:inherit;font-size:14px;font-weight:600;cursor:pointer}
.cp-seg button.on{background:#0B1433;color:#FFFFFF}
.cp-b{flex-grow:1;overflow-y:auto;display:flex;flex-direction:column;gap:16px;padding:18px 20px}
.cp-m{max-width:88%;padding:12px 16px;border-radius:14px;background:#F1F4FB;font-size:14.5px;line-height:1.55;align-self:flex-start}
.cp-me{align-self:flex-end;background:#E3EBFF}
.tm{display:flex;gap:10px;align-items:flex-start}
.tm.me{flex-direction:row-reverse}
.tm-b{flex:1;min-width:0;display:flex;flex-direction:column;gap:5px}
.tm.me .tm-b{align-items:flex-end}
.tm-h{font-size:12.5px;color:#5B6582}
.tm-h b{color:#0B1433;font-weight:600}
.tm .cp-m{max-width:100%}
.cp-f{padding:12px 20px 14px 20px;border-top:1.5px solid #F0F2F8}
.cp-in{display:flex;gap:8px}
.cp-in input{flex-grow:1;min-width:0;height:46px;box-sizing:border-box;padding:0 14px;border-radius:12px;border:1.5px solid #D6DDEE;font-family:inherit;font-size:14.5px;color:#0B1433;outline:none}
.cp-in input:focus{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.cp-send{height:46px;padding:0 20px;border-radius:12px;border:0;background:#1652F0;color:#FFFFFF;font-family:inherit;font-size:14.5px;font-weight:600;cursor:pointer}
@media (max-width: 1180px){.cs{grid-template-columns:minmax(0,1fr)}.cs-st{justify-content:flex-start}}
@media (max-width: 960px){
.pg-h{gap:18px}
.pg-hr{justify-content:flex-start;flex-wrap:nowrap;overflow-x:auto;width:calc(100% + 32px);box-sizing:border-box;margin:0 -16px;padding:2px 16px 6px 16px;gap:8px;scrollbar-width:none}
.pg-hr::-webkit-scrollbar,.nv-st::-webkit-scrollbar,.ch-tools::-webkit-scrollbar{display:none}
.pg-hr > *{flex-shrink:0}
.cs{margin-top:22px;padding:20px 18px;gap:18px}
.cs-l b{font-size:18px;margin-top:2px}
.nv-st{flex-direction:row;overflow-x:auto;scroll-snap-type:x mandatory;margin:22px -16px 0 -16px;padding:0 16px 6px 16px;gap:10px;scrollbar-width:none}
.nv-st .nv-sg{flex:0 0 84%;box-sizing:border-box;scroll-snap-align:start;align-content:flex-start}
.chs{margin-top:28px;gap:20px}
.ch-h{gap:14px}
.ch-m{margin-top:8px}
.ch-tools{flex-wrap:nowrap;overflow-x:auto;margin:16px -14px 6px -14px;padding:0 14px 16px 14px;gap:20px;scrollbar-width:none}
.ch-tools > *{flex-shrink:0}
.it + .it{box-shadow:0 -1.5px 0 #F0F2F8}
.cs-st{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
.cs-s{min-width:0;padding:10px 12px}
.cs-s b{font-size:16px}
.cs-s em{font-size:11.5px}
.cs-q{flex-wrap:nowrap;overflow-x:auto;margin:0 -16px;padding:14px 16px 0 16px;scrollbar-width:none}
.cs-ql{flex-shrink:0}
.bn{flex-wrap:wrap}
.bn-a{width:100%}
.ch{padding:20px 14px 16px 14px;border-radius:18px}
.ch-h{flex-direction:column;gap:10px}
.ch-h h2{font-size:17px}
.ch-tools{gap:4px 14px}
.ch-tools .nv-chip,.ch-tools .ud{display:none}
.it{flex-wrap:wrap;gap:12px;padding:16px 2px}
.it-i{width:36px;height:36px}
.it-r{width:100%;padding-left:48px;box-sizing:border-box;flex-wrap:wrap}
.it-act .ud{display:none}
.dr{width:100vw;top:auto;max-height:88vh;border-radius:22px 22px 0 0}
.dr-h{padding:20px 18px 14px 18px}
.dr-b{padding:4px 18px 24px 18px}
.ag-g{grid-template-columns:repeat(2,minmax(0,1fr))}
.dl{top:auto;bottom:0;left:0;transform:none;width:100vw;max-width:100vw;border-radius:22px 22px 0 0}
.dl-f{flex-direction:column-reverse}
.dl-f .ds-btn{position:relative;width:100%;justify-content:center}
.dl-f .ds-btn .ob-arrow{position:absolute;right:5px;top:50%;margin:0;transform:translateY(-50%)}
.dl .ds-seg button{padding:0 6px;font-size:12px}
.cp-ov{display:none}
.cp{top:0;width:100%;border-left:0;box-shadow:none}
.cp-h{padding:12px 12px 12px 16px}
.cp-r{padding:10px 12px 10px 16px}
.cp-b{padding:16px}
.cp-f{padding:10px 16px 14px 16px}
}
'''

BUILDER_CSS += WK_CSS + r'''.bw{margin-top:22px}
.bw .wk-m{gap:0}
.bw .bn{margin:0 0 16px 0}
.bw .chs{margin-top:0;position:relative;padding-left:56px;counter-reset:chn}
.bw .chs::before{content:'';position:absolute;left:19px;top:30px;bottom:40px;width:2px;border-radius:2px;background:linear-gradient(180deg,#1652F0,#AFC1F5)}
.bw .ch{position:relative;counter-increment:chn}
.bw .ch::before{content:counter(chn);position:absolute;left:-56px;top:20px;width:40px;height:40px;border-radius:50%;background:#1652F0;color:#FFFFFF;font-size:15px;font-weight:600;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 6px #F7F9FD,0 10px 20px -10px rgba(22,82,240,.8)}
.bw .ch::after{content:'';position:absolute;left:-16px;top:39px;width:16px;height:2px;background:#AFC1F5}
.bw .ch:hover::before{animation:chNode .6s ease}
@keyframes chNode{50%{transform:scale(1.12)}}
.bw .ch-add.big{margin-left:56px}
.bw .ch-k{display:none}
.bw .ch-h h2{margin-top:0}
.ch-tools .ud{margin-left:auto}
.it-r .ds-tag{height:22px;padding:0 8px;font-size:11px;letter-spacing:.03em}
.cs2-t{display:block;font-size:17px;font-weight:600;letter-spacing:-0.01em;line-height:1.3}
.cs2-r{margin-top:16px;display:flex;align-items:center;gap:14px}
.cs2-h{display:flex;flex-direction:column;gap:2px}
.cs2-h b{font-size:24px;font-weight:600;letter-spacing:-0.02em}
.cs2-h em{font-style:normal;font-size:12.5px;color:#5B6582}
.cs2-st{margin-top:14px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.cs2 .cs-s{min-width:0;padding:10px 12px}
.cs2 .cs-s b{font-size:17px}
.cs2 .cs-s em{font-size:12px}
.cs2-q{margin:14px -8px -8px -8px;padding-top:8px;border-top:1.5px solid #F0F2F8;display:flex;flex-direction:column}
.cs2 .cs-ql{height:42px;padding:0 10px;border-radius:12px;background:none;color:#0B1433}
.cs2 .cs-ql span{flex:1}
.cs2 .cs-ql svg{color:#1652F0}
.cs2 .cs-ql svg:last-child{color:#AEB6CC}
.cs2 .cs-ql:hover{background:#F5F8FF}
.rn-h > .rn-c{margin-left:auto;flex-direction:row;min-width:22px;height:22px;padding:0 6px;box-sizing:border-box;border-radius:999px;background:#1652F0;color:#FFFFFF;font-size:12px;font-weight:600;align-items:center;justify-content:center}
.rn-s{margin-top:12px;padding:12px;border-radius:14px;background:rgba(255,255,255,.82);border:1px solid #E1E8FA}
.rn-s + .rn-s{margin-top:8px}
.rn-s p{margin:0 0 10px 0;font-size:13.5px;line-height:1.5;color:#0B1433}
@media (max-width: 960px){
.bw{margin-top:18px}
.bw .cs2{order:0}
.bw .wk-m > .bn{order:-1;margin:0}
.bw .wk-r > .rn{order:1}
.bw .chs{padding-left:0;margin-top:4px}
.bw .chs::before{left:21px;top:48px;bottom:60px;z-index:0}
.bw .ch::before{left:14px;top:20px;width:30px;height:30px;font-size:13px;box-shadow:0 8px 16px -10px rgba(22,82,240,.8)}
.bw .ch-hl{padding-left:42px;min-height:30px}
.bw .ch-h h2{line-height:30px}
.bw .ch::after{display:none}
.bw .ch-add.big{margin-left:0}
.bw .it{display:grid;grid-template-columns:36px minmax(0,1fr);column-gap:12px;row-gap:8px;align-items:start;padding:14px 2px}
.bw .it-i{grid-row:1 / span 2}
.bw .it-t b{font-size:14.5px}
.bw .it-m{font-size:12.5px;gap:2px 6px}
.bw .it-r{grid-column:2;width:auto;padding:0;flex-wrap:nowrap;gap:8px}
.bw .it-act{margin-left:auto}
.bw .it .ud,.bw .it .ib{display:none}
.bw .it-act .ds-ghost{margin:0;min-width:0}
.cs2-r{margin-top:12px}
.cs2-q{flex-direction:row;overflow-x:auto;margin:14px -16px 0 -16px;padding:14px 16px 0 16px;gap:8px;scrollbar-width:none}
.cs2-q::-webkit-scrollbar{display:none}
.cs2 .cs-ql{flex-shrink:0;height:38px;border-radius:999px;background:#F5F8FF;color:#0E3BB8;padding:0 14px}
.cs2 .cs-ql svg:last-child{display:none}
.rn-s{padding:12px}
}
'''

write('Builder.dc.html', doc('Curriculum Builder · shared source', kit.KIT_CSS + '\n' + dash.DASH_CSS + BASE_CSS + CW_CSS + BUILDER_CSS, BUILDER_BODY, BUILDER_JS))

# ======================================================================= EDITORS
E = Toggles()
LOS4 = ['LO1', 'LO2', 'LO3', 'LO4']
SK4 = ['SQL', 'Data Analysis', 'Data Cleaning', 'Relational Databases']
LIB = ['Data Analysis Handbook.pdf', 'Course Worksheet.xlsx', 'SQL Joins Cheat Sheet.pdf', 'Practice Dataset.csv', 'Exercise Instructions.pdf',
       'retail-dataset.zip', 'PostgreSQL documentation', 'The Data Warehouse Toolkit (Kimball & Ross)']

def card(title, body, cls='', right='', t=''):
    return '<section class="ds-card ec%s"><div class="ec-h"><h2>%s%s</h2>%s</div>%s</section>' % ((' ' + cls) if cls else '', title, tip(t) if t else '', right, body)

def dlp_card(n, lt, src, prov=False, extra=''):
    return ('<section class="ds-card dlpc"><div class="dlpc-h"><span class="pg-e">Estimated DLP</span>%s</div><div class="dlpc-n">%s<b>%s</b><span>DLP</span></div>'
            '<div class="dlpc-r"><span>Estimated learning time</span><b>%s</b></div><p class="dlpc-s">%s%s</p>%s</section>') % (
        tag('PROVISIONAL', 'amber') if prov else '', coin(True), n, lt, src, tip('Recalculated automatically when this item or its tier changes.', 'r'), extra)

def tier_card(noun, idx, label='Content tier', note=None):
    return card(label + ' *', '<p class="ec-p">%s</p>%s%s<p class="lockl">%s<span>DLP Complexity Weight: 1.15× [TO CONFIRM]</span>%s</p>' % (
        'Select the difficulty tier of this %s. It feeds the DLP estimate above.' % noun if note is None else note,
        E.seg(['Beginner', 'Intermediate', 'Advanced', 'Expert'], idx), '' if note is None else '',
        ic('lock', 13, 2), tip('Read-only. Assigned by Credalio pricing rules for the selected tier. Final DLP remains subject to content analysis and validation.', 'r')), 'side')

def chips(items, on, cls='sm'):
    return '<div class="chips">%s</div>' % ''.join(E.chip(x, i in on, cls=cls) for i, x in enumerate(items))

def settings(req=None, assigned=None, los=(), sks=(), comp=None, comp_on=0, comp_note=''):
    h = ''
    if req is not None:
        h += card('Requirement', E.seg(['Required', 'Optional'], 0 if req else 1), 'side')
    if assigned is not None:
        h += card('Assigned', chips(['Ada', 'John', 'ABC Institute'], assigned), 'side', t='Assignment is work, not ownership.')
    h += card('Mapped outcomes', chips(LOS4, los), 'side')
    h += card('Mapped skills', chips(SK4, sks), 'side', t='Feeds the Learning Intelligence Profile.')
    if comp:
        h += card('When it counts as complete', '<div class="rl">%s</div><p class="ec-p">%s</p>' % (
            ''.join(E.opt('<span class="o-t"><b>%s</b></span>' % c, i == comp_on, 'cp', 'sm') for i, c in enumerate(comp)), comp_note), 'side')
    return h

def resources(attached=None):
    a = ('<div class="ra"><span class="ra-i">%s</span><span class="ra-t"><b>%s</b><span>%s</span></span><a class="ds-link sm" href="#">Detach</a></div>' % (ic('clip', 16, 2), attached[0], attached[1])) if attached else '<p class="ec-p">No resources attached.</p>'
    return card('Resources', a + '<div class="rat"><span class="sr-only">Attach from library</span><label class="sel"><span class="sr-only">Attach from library</span><select class="ds-in"><option>Choose a library file…</option>%s</select>%s</label><button type="button" class="ds-ghost">Attach</button></div>' % (
        ''.join('<option>%s</option>' % l for l in LIB), ic('down', 16, 2)), t='From the one Course Resource Library. The same file can be attached anywhere.',
        right='<span class="ec-sub">Attach from library</span>')

def comments(thread=()):
    t = ''.join('<div class="cm"><span class="cm-a">%s</span><div class="cm-b"><div class="cm-h"><b>%s</b><span>· %s</span><button type="button" class="ds-link sm">%s</button></div><p>%s</p></div></div>' % (
        av(*p, size=30), n, w, act, txt) for p, n, w, act, txt in thread)
    return card('Comments', t + '<div class="cmp"><textarea class="ds-in" placeholder="Comment on this item, @mention someone" aria-label="Comment"></textarea><div class="cmp-f"><span class="chips"><span class="ds-tag line">@ John</span><span class="ds-tag line">@ ABC</span></span><button type="button" class="ds-ghost sm">Post comment</button></div></div>')

def details(title, desc='', ph='Short description learners see before they start'):
    return card('Details', '<div class="fg">%s%s</div>' % (
        field('Title', '<input class="ds-in" value="%s" aria-label="Title">' % title),
        field('Description', '<textarea class="ds-in sm" placeholder="%s" aria-label="Description">%s</textarea>' % (ph, desc))))

def facts(dlp, lt, src, who=None, req=None, prov=False):
    '''Key facts strip in the editor header (moved up from the side DLP card).'''
    h = '<span class="ef-c ef-dl"><em>Estimated DLP%s</em><b>%s%s</b>%s</span><span class="ef-c"><em>Estimated learning time</em><b>%s</b></span>' % (
        tip(src + '. Recalculated automatically when this item or its tier changes.', 'dn r'), coin(), dlp, tag('PROVISIONAL', 'amber') if prov else '', lt)
    if who:
        h += '<span class="ef-c"><em>Assigned</em><span class="ef-w">%s<b>%s</b></span></span>' % (ppl(who, 26), names(who))
    if req is not None:
        h += '<span class="ef-c"><em>Requirement</em>%s</span>' % tag('Required' if req else 'Optional', 'blue' if req else '')
    return '<div class="eh-f">%s</div>' % h

def ehead(crumbs, kind_label, icon, title, meta, chips_='', facts_=''):
    bc = '<nav class="bc" aria-label="Breadcrumb"><a href="STU-020.dc.html">%s<span>Curriculum</span></a>%s</nav>' % (ICON(I['back'], 15, 2), ''.join('<span aria-hidden="true">›</span><span>%s</span>' % c for c in crumbs))
    return ('%s<header class="eh ob-in"><span class="eh-i">%s</span><div class="eh-t"><span class="pg-e">%s</span><h1 class="ds-h1">%s</h1><p class="ds-sub">%s</p>%s</div>%s</header>' %
            (bc, ic(icon, 22), kind_label, title, meta, chips_, facts_))

def eacts():
    return '<div class="ds-acts sb sv"><span class="sv-s"><a class="ds-link del" href="{{delHref}}">%s<span>Delete</span></a></span><span class="sv-r"><a class="ds-ghost sm" href="#">Save Draft</a>%s</span></div>' % (ic('trash', 15, 2), btn('Save & Continue', 'STU-020.dc.html'))

def layout(head, main, side):
    return '%s<div class="ed ob-in2"><div class="ed-m">%s</div><aside class="ed-s">%s</aside></div>%s' % (head, main, side, eacts())

ED = {}
# ---------- video
MARK_ = [('0:00', 'Why joins matter', 0), ('6:00', 'INNER JOIN, step by step', 32.8), ('13:00', 'LEFT JOIN and missing rows', 71)]
ED['video'] = layout(
    ehead(['Chapter 3', 'Joining Tables with SQL', 'Video'], 'Video', 'play', 'Joining Tables with SQL', 'Chapter 3 · Joining Tables', facts_=facts('30', '18m', '18 min video, detected from joining-tables.mp4', ['J'], True)),
    details('Joining Tables with SQL', 'How INNER and LEFT joins combine two tables, with a worked example on customers and orders.') +
    card('Video file', '<div class="vf"><span class="vf-th">%s</span><span class="vf-t"><b>%s joining-tables.mp4</b><span>Duration detected: 18 min</span></span><a class="ds-link sm" href="#">Replace</a></div>'
         '<div class="va">%s</div>%s' % (
             '<span class="vz-play"></span>', '<span class="okc">%s</span>' % ck(10),
             ''.join('<span class="va-c"><em>%s</em><b class="%s">%s</b></span>' % (l, k, v) for l, v, k in [
                 ('Duration', '18:18', ''), ('Processing', 'Complete', 'g'), ('Transcript', 'Available', 'g'), ('Captions', 'Missing', 'a'),
                 ('Estimated learning time', '18 min', ''), ('Estimated DLP contribution', '30 DLP', '')]),
             field('Or hosted source', '<input class="ds-in" placeholder="Approved hosted video link, if supported [TO CONFIRM providers]" aria-label="Or hosted source">')),
         t='') +
    card('Transcript & captions', '<div class="tr"><span class="tr-i">%s</span><span class="tr-t"><b>Transcript</b><span>Generated from the audio, then reviewed</span></span>%s</div>'
         '<div class="tr"><span class="tr-i a">%s</span><span class="tr-t"><b>Captions</b><span>Required for validation on video</span></span>%s</div>' % (
             ic('file', 16), tag('Available', 'green'), ic('cap', 16), tag('Missing', 'amber'))) +
    card('Chapter markers', '<div class="mk"><div class="mk-bar">%s</div><div class="mk-l">%s</div></div>' % (
        ''.join('<i style="left: %s%%"></i>' % p for _, _, p in MARK_), ''.join('<span><b>%s</b>%s</span>' % (t, l) for t, l, _ in MARK_))) +
    resources(('SQL Joins Cheat Sheet.pdf', 'Downloadable · Optional · During lesson')) + comments(),
    nova_sg('I can draft an outline, and I’ll flag long stretches of content with no check.', cls='side-nv') +
    tier_card('video', 1) + settings(True, {1}, {1}, {0, 3}, ['Open the lesson', 'Watch ≥ 70% (recommended)', 'Watch ≥ 90%', 'Watch to the end'], 1,
                                      'Recommended: 70% minimum viewing. You choose within Credalio policy.'))

# ---------- text
TOOLS = [('H2', None), ('B', 'bold'), ('Image', 'image'), ('Table', 'table'), ('Code', 'code'), ('Embed', 'play'), ('Example', 'bulb')]
TXT_THREAD = [((ME, 'A'), 'Ada', 'Tue 09:14', 'Resolve', '@John can you add another example here?'),
              ((M1, 'J'), 'John', 'Tue 11:02', 'Resolve', 'On it. Adding a three-table join.'),
              ((ME, 'A'), 'Ada', 'Tue 11:30', 'Reopen', 'Great, thanks.')]
ED['text'] = layout(
    ehead(['Chapter 3', 'INNER vs LEFT JOIN', 'Text / Article'], 'Text / Article', 'file', 'INNER vs LEFT JOIN', 'Chapter 3 · Joining Tables', facts_=facts('20', '15m', '3,400 words at 230 a minute · about 15 min', ['A', 'J'], True)),
    details('INNER vs LEFT JOIN') +
    card('Lesson text', '<div class="rt"><div class="rt-tb">%s</div><div class="rt-a" aria-label="Lesson text"><p>When you join two tables you choose which rows survive. An INNER JOIN keeps only rows that match in both tables; a LEFT JOIN keeps every row from the left table and fills the gaps with NULL.</p><h3>Worked example: customers and orders</h3><ol><li>Start with the customers table (who) and the orders table (what they bought).</li><li>INNER JOIN on customer_id returns only customers who have ordered.</li><li>LEFT JOIN returns every customer, with NULL where there is no order.</li></ol></div><div class="rt-f">3,400 words · about 15 min of reading · 20 estimated DLP</div></div>' % (
        ''.join('<button type="button" class="rt-b" aria-label="%s">%s</button>' % (l, ic(i, 15, 2) + ('<span>%s</span>' % l if l not in ('B',) else '') if i else '<b>%s</b>' % l) for l, i in TOOLS)),
        right=nchip('Draft an outline')) +
    resources() + comments(TXT_THREAD),
    nova_sg('I can draft an outline, and I’ll flag long stretches of content with no check.', cls='side-nv') +
    tier_card('text lesson', 1) + settings(True, {0, 1}, {1}, {0, 3}, ['Reach the end (recommended)', 'Mark as complete', 'Minimum active time'], 0,
                                            'Counts toward chapter and course completion when required.'))

# ---------- live class
ED['live'] = layout(
    ehead(['Chapter 4', 'Analysis Clinic', 'Live Class'], 'Live Class', 'live', 'Analysis Clinic', 'Chapter 4 · Analysing Business Data', facts_=facts('100', '1h', '60 min scheduled', ['AB'], False)),
    details('Analysis Clinic') +
    card('Schedule', '<div class="fg"><div class="fg fg3">%s%s%s</div>%s%s</div>' % (
        field('Date', '<input class="ds-in" value="Thu 16 Oct" placeholder="e.g. Thu 16 Oct" aria-label="Date">'),
        field('Start time', '<input class="ds-in" value="6:00 PM" placeholder="e.g. 6:00 PM" aria-label="Start time">'),
        field('Time zone', '<label class="sel"><span class="sr-only">Time zone</span><select class="ds-in"><option>WAT (UTC+1)</option><option>GMT (UTC+0)</option><option>EAT (UTC+3)</option></select>%s</label>' % ic('down', 16, 2)),
        field('Duration', E.seg(['30m', '45m', '1h', '1h 30m', '2h'], 2)), field('Repeats', E.seg(['One-off', 'Weekly', 'Every 2 weeks'], 0)))) +
    card('Delivery', '<div class="fg"><div class="fg fg2">%s%s</div>%s%s</div>' % (
        field('Instructor', chips(['Ada', 'John', 'ABC Institute'], {2})), field('Capacity', '<input class="ds-in" value="25" aria-label="Capacity">'),
        field('Where it happens%s' % tip('External platforms depend on integrations [TO CONFIRM].'), '<div class="opt2">%s</div>' % ''.join(
            E.opt('<span class="o-t"><b>%s</b></span>' % w, i == 0, 'where', 'sm') for i, w in enumerate(['Credalio Live', 'Zoom link', 'Microsoft Teams link', 'In person']))),
        field('Agenda', '<textarea class="ds-in sm" aria-label="Agenda">Bring a question from your own data. We work through two learner examples live.</textarea>'))) +
    card('Attendance & recording', '<div class="fg">%s%s</div>' % (
        field('Counts as attended when learners are present for at least', E.seg(['50% of the session', '70% of the session', '80% of the session', '90% of the session'], 1)),
        field('Recording', '<div class="opt3">%s</div>' % ''.join(E.opt('<span class="o-t"><b>%s</b></span>' % r, i == 0, 'rec', 'sm') for i, r in enumerate(['Recorded for enrolled learners', 'Recorded for attendees only', 'Not recorded']))))) +
    resources() + comments(),
    nova_sg('Attendance sets when a live class counts as complete.', cls='side-nv') +
    tier_card('live class', 2) + settings(False, {2}, {2}, {1}, ['Attend ≥ 50%', 'Attend ≥ 70% (recommended)', 'Attend ≥ 80%', 'Attend ≥ 90%'], 1,
                                           'Matches the attendance threshold set for this class.'))

# ---------- assessment
QTYPES = ['Multiple choice (single)', 'Multiple choice (multiple)', 'True / False', 'Short answer', 'Fill in the blank', 'Matching', 'Ordering / sequence', 'Long answer / essay', 'File submission']
QS = [(2, 'Write a query that returns all customers based in Lagos.', 'Short answer', '3 points'),
      (3, 'SELECT DISTINCT removes duplicate rows from a result. True or false?', 'True / False', '1 point'),
      (4, 'Match each clause to what it does: WHERE, ORDER BY, LIMIT.', 'Matching', '2 points')]
READY = [('ok', '10 of 10 saved questions valid'), ('ok', 'Question types counted: 6 single choice, 2 short answer, 1 true/false, 1 matching'),
         ('ok', 'Tier selected: Intermediate'), ('ok', 'Scoring configured (13 points, pass 70%)'), ('w', 'Estimated effort 15 min is from the time limit; confirm after review')]
def tog(label, on, sub=''):
    k = E.new(on)
    return '<button type="button" class="tg {{c%s}}" aria-pressed="{{a%s}}" onClick="{{x%s}}"><span class="tg-t"><b>%s</b>%s</span><span class="tg-s"><i></i></span></button>' % (
        k, k, k, label, ('<span>%s</span>' % sub) if sub else '')
Q1 = '''<div class="q q-open">
<div class="q-h"><span class="q-n">1</span><b>Which clause filters rows before they are grouped?</b><span class="q-m">%s%s<span>1 point</span></span><span class="q-a"><button type="button" class="ds-ghost xs">Done</button><button type="button" class="ib" aria-label="Remove question">%s</button></span></div>
<div class="q-b">
%s
<span class="fl-l">Options · tick the correct answer</span>
<div class="qo">%s</div>
<div class="fg fg2">%s%s</div>
<div class="fg fg2">%s%s</div>
%s
</div>
</div>''' % (tag('Multiple choice (single)', 'line'), tag('LO1', 'blue'), ic('x', 15, 2),
             field('Question', '<input class="ds-in" value="Which clause filters rows before they are grouped?" aria-label="Question">'),
             ''.join('<label class="qo-r%s"><span class="qo-c">%s</span><input class="ds-in" value="%s" aria-label="Option %d"></label>' % (' ok' if i == 0 else '', ck(11) if i == 0 else '', o, i + 1) for i, o in enumerate(['WHERE', 'HAVING', 'GROUP BY', 'ORDER BY'])),
             field('Points', '<input class="ds-in" value="1" aria-label="Points">'), field('Difficulty', E.seg(['Easy', 'Medium', 'Hard'], 0)),
             field('Mapped outcome', '<label class="sel"><span class="sr-only">Mapped outcome</span><select class="ds-in"><option>LO1 · Write SQL queries to retriev</option><option>LO2 · Combine multiple relational</option><option>LO3 · Analyse business datasets an</option><option>LO4 · Understand SQL</option></select>%s</label>' % ic('down', 16, 2)),
             field('Mapped skill', '<label class="sel"><span class="sr-only">Mapped skill</span><select class="ds-in"><option>SQL</option><option>No skill</option><option>Data Analysis</option><option>Data Cleaning</option><option>Relational Databases</option></select>%s</label>' % ic('down', 16, 2)),
             field('Explanation shown to learners', '<input class="ds-in" value="WHERE filters rows before grouping; HAVING filters groups after." placeholder="Why the answer is right" aria-label="Explanation shown to learners">'))
ED['assess'] = layout(
    ehead(['Chapter 2', 'Quiz 1', 'Assessment', 'Quiz', 'Questions'], 'Assessment', 'quiz', 'Quiz 1', 'Chapter 2 · Quiz 1 · 10 questions',
          '<div class="eh-c">%s%s%s%s%s</div>' % (tag('Type: Quiz', 'line'), tag('Questions: 10', 'line'), tag('Estimated time: 15 min', 'line'), tag('Required', 'blue'), tag('Mapped outcomes: 1', 'line'))),
    card('Assessment type', '%s<p class="ec-p">A scored assessment of a lesson, chapter or set of concepts: passing score, attempts, feedback, optional time limit, outcome mapping.</p>' % E.seg(['Knowledge Check', 'Quiz', 'Exam'], 1)) +
    card('A · Assessment basics', '<div class="fg">%s%s%s%s</div>' % (
        field('Title', '<input class="ds-in" value="Quiz 1" aria-label="Title">'),
        field('Description', '<textarea class="ds-in sm" aria-label="Description">Check understanding of filtering and grouping before moving to joins.</textarea>'),
        field('Subtype', E.seg(['Knowledge Check', 'Quiz', 'Exam'], 1), "Exams must be scored under Credalio's exam policy."),
        field('Linked learning outcomes', chips(LOS4, {0})))) +
    card('D · Question Builder', Q1 + ''.join('<div class="q"><div class="q-h"><span class="q-n">%d</span><b>%s</b><span class="q-m">%s%s<span>%s</span></span><span class="q-a"><button type="button" class="ds-ghost xs">Edit</button><button type="button" class="ib" aria-label="Remove question">%s</button></span></div></div>' % (
        n, t, tag(ty, 'line'), tag('LO1', 'blue'), p, ic('x', 15, 2)) for n, t, ty, p in QS) +
        '<button type="button" class="q-more">+ 6 more questions</button>'
        '<div class="qa"><span class="fl-l">Add question</span><div class="chips">%s</div><p class="ec-p"><b>Later:</b> Code response · Numeric answer · AI-evaluated response, once assessment policy supports them</p></div>'
        '<div class="qg">%s<span>Nova drafts; you review and approve every question.</span></div>' % (
            ''.join('<button type="button" class="ds-chip sm">%s<span>%s</span></button>' % (ic('plus', 13, 2.4), q) for q in QTYPES), nchip('Generate draft questions')),
        right='<span class="ec-sub">10 questions · 13 points</span>') +
    card('E · Delivery settings', '<div class="fg"><div class="fg fg2">%s%s</div>%s<div class="tgs">%s%s%s%s%s</div>%s</div>' % (
        field('Attempts', '<label class="sel"><span class="sr-only">Attempts</span><select class="ds-in"><option>2</option><option>1</option><option>3</option><option>5</option><option>Unlimited</option></select>%s</label>' % ic('down', 16, 2)),
        field('Time limit', '<label class="sel"><span class="sr-only">Time limit</span><select class="ds-in"><option>15 minutes</option><option>No limit</option><option>30 minutes</option><option>45 minutes</option><option>60 minutes</option><option>90 minutes</option></select>%s</label>' % ic('down', 16, 2)),
        field('Feedback', E.seg(['Immediately', 'After submission', 'After final attempt', 'After passing'], 1)),
        tog('Randomise question order', True), tog('Randomise answer order', True), tog('Show explanations', True),
        tog('Draw from a question bank', False, 'Each attempt draws a different set'), tog('Required for course completion', True),
        field('Completion', '%s<span class="fl-h" style="margin-top: 6px">Required · Pass ≥ 70%%</span>' % E.seg(['Submit assessment', 'Pass assessment'], 1)))) +
    '',
    ('<section class="ds-card dlpc"><div class="dlpc-h"><span class="pg-e">F · DLP readiness</span>%s</div><div class="dlpc-n">%s<b>25</b><span>DLP</span></div>'
     '<div class="dlpc-r"><span>Estimated learning time</span><b>15m</b></div><p class="dlpc-s">10 questions · about 15 min%s</p><ul class="rd">%s</ul>'
     '<p class="ec-p">DLP is calculated from saved, valid questions, never from a typed question count.%s</p></section>') % (
        tag('PROVISIONAL', 'amber'), coin(True), tip('Recalculated automatically when this item or its tier changes.', 'r'),
        ''.join('<li class="%s"><span>%s</span>%s</li>' % (k, ck(10) if k == 'ok' else '!', t) for k, t in READY),
        tip('The approved value on the live version is kept until a new version is activated. Not ready states: add the required questions, answers and scoring before DLP can be calculated.', 'r')) +
    nova_sg('I can draft questions. You review and approve each one before it’s added.', nchip('Generate draft questions'), cls='side-nv') +
    card('B · Assessment difficulty *', '<div class="tq">%s</div>'
         '<div class="qd2"><span class="qd2-l">Question-level difficulty <em>(supported for this subtype)</em></span><span class="qd2-b" aria-hidden="true"><i class="e" style="flex: 4"></i><i class="m" style="flex: 5"></i><i class="h" style="flex: 1"></i></span>'
         '<span class="qd2-k"><span class="e"><i></i>4 Easy</span><span class="m"><i></i>5 Medium</span><span class="h"><i></i>1 Hard</span><span class="n">0 not set</span></span></div>'
         '<p class="lockl">%s<span>DLP Complexity Weight: 1.15× [TO CONFIRM]</span>%s</p>' % (
             ''.join(E.opt('<span class="o-t"><b>%s</b></span><span class="tq-d" aria-hidden="true">%s</span>' % (t, ''.join('<i class="%s"></i>' % ('on' if j <= i else '') for j in range(4))), i == 1, 'tier', 'sm tq-o') for i, t in enumerate(['Beginner', 'Intermediate', 'Advanced', 'Expert'])),
             ic('lock', 13, 2),
             tip('Read-only. Assigned by Credalio pricing rules for the selected tier. Final DLP remains subject to content analysis and validation.', 'r')), 'side',
         t='Overall tier of this assessment. It feeds the DLP estimate. Question-level difficulty is separate and set on each question in D.') +
    card('C · Scoring configuration', '<div class="fg">%s%s%s</div><p class="ec-p">Total points: 13 · set on each question in D%s</p>' % (
        field('Will this activity carry points?', '<div class="opt2">%s%s</div>' % (E.opt('<span class="o-t"><b>Yes · Scored</b></span>', True, 'sc', 'sm'), E.opt('<span class="o-t"><b>No · Practice / self-check</b></span>', False, 'sc', 'sm'))),
        field('Point allocation', E.seg(['Points per question', 'Total score'], 0)),
        field('Passing score (%)', '<input class="ds-in pct" value="70" aria-label="Passing score (%)">'),
        tip('Unscored knowledge checks are never blocked for missing points. Changing points alone does not change DLP.')), 'side') +
    settings(None, None, {0}, {0}, ['Submit', 'Achieve ≥ 70% (recommended)'], 1, 'Uses this quiz’s passing score.') + resources() + comments())

# ---------- applied learning (project)
RUB = [('Query correctness', '40'), ('Analysis quality', '30'), ('Communication of findings', '30')]
ED['project'] = layout(
    ehead(['Chapter 5', 'Final Project', 'Project'], 'Project', 'rocket', 'Final Project', 'Chapter 5 · Communicating Findings', facts_=facts('200', '2h', 'Creator estimate of 2h, adjusted by Credalio as learners complete it', ['A'], True)),
    details('Final Project') +
    card('Instructions for learners', '<div class="fg">%s%s</div>' % (
        '<textarea class="ds-in" aria-label="Instructions for learners">Choose a business question, prepare the data, analyse it with SQL and present your findings in a 5-minute recorded presentation.</textarea>',
        field('Expected effort', E.seg(['15m', '30m', '45m', '1h', '2h', '4h', '8h'], 4), 'Creator estimate. Credalio adjusts it as learners complete the activity.'))) +
    card('Submission & evidence', '<div class="fg">%s%s%s%s</div>' % (
        field('Learners submit', chips(['File upload', 'Link', 'Text response', 'SQL / code file'], {0, 3})),
        field('Deliverable: what the learner produces', '<input class="ds-in" value="SQL file, results and a recorded presentation" placeholder="e.g. SQL file + analysis report" aria-label="Deliverable: what the learner produces">'),
        field('Evidence that proves the outcome', '<input class="ds-in" placeholder="e.g. SQL file and a one-page write-up" aria-label="Evidence that proves the outcome">'),
        '<div class="tgs">%s</div>' % tog('Becomes Proof of Learning', True, 'Shown on the learner’s record once passed'))) +
    card('Evaluation & feedback', '<div class="fg">%s%s%s</div>' % (
        field('Feedback to learners', chips(['Written feedback', 'Rubric scores only', 'Feedback conversation'], {0})),
        field('Evaluation method', '<div class="opt3">%s</div>' % ''.join(E.opt('<span class="o-t"><b>%s</b></span>' % m, i == 1, 'ev', 'sm') for i, m in enumerate(['Auto-checked', 'Tutor-marked with rubric', 'Peer review + tutor']))),
        '<div class="rb"><div class="rb-r rb-hd"><span>Rubric criterion</span><span>Weight (%%)</span><span></span></div>%s<button type="button" class="ds-link sm rb-add">+ Add criterion</button><p class="rb-ok">%s<span>Weights total 100%%</span></p></div>' % (
            ''.join('<div class="rb-r"><input class="ds-in" value="%s" aria-label="Criterion %d"><input class="ds-in" value="%s" aria-label="Weight %d"><button type="button" class="ib" aria-label="Remove criterion %d">%s</button></div>' % (c, i + 1, w, i + 1, i + 1, ic('x', 15, 2)) for i, (c, w) in enumerate(RUB)), ck(12)))) +
    resources(('retail-dataset.zip', 'Downloadable · Required · Before lesson')) + comments(),
    nova_sg('Practice that maps to an outcome gives validators evidence.', cls='side-nv') +
    tier_card('applied learning activity', 1) + settings(True, {0}, {2}, {0, 1}, ['Submit', 'Pass the rubric (recommended)'], 1,
                                                          'Counts toward chapter and course completion when required.'))

OV_EDEL = dlg('Delete “INNER vs LEFT JOIN”?',
              '<ul class="dl-ul"><li>Removes it from Chapter 3 (−15 min, −20 estimated DLP)</li><li>Assigned to Ada + John. They’ll see the change in Team Chat.</li></ul>',
              'Delete learning item', cancel='STU-022B.dc.html', danger=True, icon=ic('trash', 18, 2))

KINDS = ['video', 'text', 'live', 'assess', 'project']
EDITOR_BODY = '''<div class="ds-root">
%s
<div style="min-width: 0; display: flex; flex-direction: column">
%s
<main class="ds-main ed-main">
%s
</main>
</div>
</div>
<sc-if value="{{o_del}}" hint-placeholder-val="{{ false }}">%s</sc-if>''' % (
    sidebar('cb'), topbar(phase='Build'), '\n'.join('<sc-if value="{{k_%s}}" hint-placeholder-val="{{ %s }}">%s</sc-if>' % (k, 'true' if k == 'video' else 'false', ED[k]) for k in KINDS), OV_EDEL)

EDITOR_JS = E.js() + '''class Component extends DCLogic {
  renderVals() {
    var k = this.props.kind || 'video';
    var v = togVals(this), self = this;
    %s.forEach(function (x) { v['k_'.concat(x)] = x === k; });
    v.o_del = this.props.overlay === 'del';
    v.delHref = k === 'text' ? 'STU-022B-DEL.dc.html' : '#';
    v.navCls = this.state.nav ? 'ds-open' : '';
    v.toggleNav = function () { self.setState({ nav: !self.state.nav }); };
    return v;
  }
}''' % json.dumps(KINDS)

EDITOR_CSS = BUILDER_CSS + r'''.ed-main{max-width:1240px}
.bc{display:flex;flex-wrap:wrap;align-items:center;gap:8px;font-size:13.5px;color:#5B6582;margin-bottom:16px}
.bc a{display:inline-flex;align-items:center;gap:6px;color:#3A4566;font-weight:500;text-decoration:none}
.bc a:hover{color:#1652F0}
.bc span[aria-hidden]{color:#AEB6CC}
.eh{display:flex;align-items:flex-start;gap:16px}
.eh-t{flex:1}
.eh-f{flex-shrink:0;align-self:center;display:flex;align-items:stretch;padding:6px;border-radius:18px;background:#FFFFFF;border:1.5px solid #E6EAF3;box-shadow:0 1px 2px rgba(11,20,51,.03)}
.ef-c{display:flex;flex-direction:column;justify-content:center;gap:6px;padding:10px 18px;min-width:96px}
.ef-c + .ef-c{border-left:1.5px solid #F0F2F8}
.ef-c em{display:flex;align-items:center;font-style:normal;font-size:12px;color:#5B6582;white-space:nowrap}
.ef-c b{display:flex;align-items:center;gap:8px;font-size:20px;font-weight:600;letter-spacing:-0.02em;white-space:nowrap}
.ef-c.ef-dl{border-radius:13px;background:linear-gradient(160deg,#FFFDF6,#FFF6DC);margin-right:4px}
.ef-c.ef-dl + .ef-c{border-left:0}
.ef-c.ef-dl .ds-tag{align-self:flex-start;height:22px;font-size:11px}
.ef-c .ds-tag{align-self:flex-start}
.ef-w{display:flex;align-items:center;gap:8px}
.ef-w b{font-size:14px;font-weight:600;letter-spacing:0}
.ef-w .avs .av + .av{margin-left:-6px}
.eh-i{width:52px;height:52px;flex-shrink:0;border-radius:16px;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 12px 24px -12px rgba(22,82,240,.7)}
.eh-t{min-width:0}
.eh-t .pg-e{margin-bottom:4px}
.eh-c{margin-top:12px;display:flex;flex-wrap:wrap;gap:6px}
.ed{margin-top:22px;display:grid;grid-template-columns:minmax(0,1fr) 360px;gap:16px;align-items:start}
.ed-m,.ed-s{display:flex;flex-direction:column;gap:16px;min-width:0}
.ed-s{position:sticky;top:88px}
.ec{padding:22px 24px 24px 24px}
.ec.side{padding:18px 20px 20px 20px}
.ec-h{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:16px}
.ec-h h2{margin:0;display:flex;align-items:center;font-size:16px;font-weight:600;letter-spacing:-0.01em}
.ec.side .ec-h{margin-bottom:12px}
.ec.side .ec-h h2{font-size:14.5px}
.ec-sub{font-size:13px;color:#5B6582}
.ec-p{margin:10px 0 0 0;font-size:13px;line-height:1.5;color:#5B6582}
.ec-p:first-child{margin-top:0}
.ec-p b{font-weight:600;color:#3A4566}
textarea.ds-in.sm{min-height:76px}
.dlpc{padding:18px 20px 20px 20px;background:linear-gradient(160deg,#FFFFFF 40%,#FFF8E6);border-color:#F4E2B0}
.dlpc-h{display:flex;align-items:center;justify-content:space-between}
.dlpc-h .pg-e{margin:0;color:#8A5A00}
.dlpc-n{margin-top:10px;display:flex;align-items:center;gap:10px}
.dlpc-n b{font-size:38px;font-weight:600;letter-spacing:-0.03em;line-height:1}
.dlpc-n > span:last-child{font-size:15px;font-weight:500;color:#5B6582;align-self:flex-end;margin-bottom:4px}
.dlpc-r{margin-top:14px;display:flex;justify-content:space-between;padding-top:12px;border-top:1.5px solid #F4E9C8;font-size:13.5px;color:#3A4566}
.dlpc-r b{font-weight:600}
.dlpc-s{margin:6px 0 0 0;display:flex;align-items:center;font-size:12.5px;color:#5B6582}
.lockl{margin:12px 0 0 0;display:flex;align-items:center;gap:6px;font-size:12.5px;color:#5B6582}
.lockl svg{color:#8A93AD}
.side-nv{padding:12px 14px;flex-wrap:wrap}
.side-nv p{flex:1 1 calc(100% - 44px)}
.side-nv .nv-sg-a{width:100%;padding-left:42px;box-sizing:border-box}
.side-nv p{font-size:13.5px}
.ed-s .ds-seg button{padding:0 8px;font-size:13px}
.vf{display:flex;align-items:center;gap:14px;padding:10px 16px 10px 10px;border-radius:14px;border:1.5px solid #E6EAF3}
.vf-th{position:relative;width:88px;height:54px;flex-shrink:0;border-radius:10px;background:linear-gradient(140deg,#1652F0,#0B1433)}
.vz-play{position:absolute;left:50%;top:50%;width:24px;height:24px;margin:-12px 0 0 -12px;border-radius:50%;background:#FFFFFF}
.vz-play::after{content:'';position:absolute;left:9px;top:6px;border-left:8px solid #1652F0;border-top:6px solid transparent;border-bottom:6px solid transparent}
.vf-t{flex:1;min-width:0;display:flex;flex-direction:column;gap:3px}
.vf-t b{display:flex;align-items:center;gap:8px;font-size:15px;font-weight:600}
.vf-t span{font-size:13px;color:#5B6582}
.okc{width:18px;height:18px;border-radius:50%;background:#0F6B45;color:#FFFFFF;display:inline-flex;align-items:center;justify-content:center}
.va{margin:16px 0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
.va-c{display:flex;flex-direction:column;gap:3px;padding:12px 14px;border-radius:12px;background:#F7F9FD}
.va-c em{font-style:normal;font-size:12px;color:#5B6582}
.va-c b{font-size:16px;font-weight:600}
.va-c b.g{color:#0F6B45}
.va-c b.a{color:#8A5A00}
.tr{display:flex;align-items:center;gap:14px;padding:12px 0}
.tr + .tr{border-top:1.5px solid #F0F2F8}
.tr-i{width:38px;height:38px;flex-shrink:0;border-radius:11px;background:#E7F5EE;color:#0F6B45;display:flex;align-items:center;justify-content:center}
.tr-i.a{background:#FFF4E0;color:#8A5A00}
.tr-t{flex:1;display:flex;flex-direction:column;gap:2px}
.tr-t b{font-size:14.5px;font-weight:600}
.tr-t span{font-size:13px;color:#5B6582}
.mk-bar{position:relative;height:8px;margin:8px 4px 18px 4px;border-radius:8px;background:linear-gradient(90deg,#1652F0,#5C86FF)}
.mk-bar i{position:absolute;top:50%;width:14px;height:14px;margin:-7px 0 0 -7px;border-radius:50%;background:#FFFFFF;border:3px solid #1652F0;box-sizing:border-box}
.mk-l{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.mk-l span{display:flex;flex-direction:column;gap:2px;font-size:13.5px;color:#3A4566}
.mk-l b{font-size:13px;font-weight:600;color:#1652F0}
.rt{border:1.5px solid #E6EAF3;border-radius:14px;overflow:hidden}
.rt-tb{display:flex;flex-wrap:wrap;gap:2px;padding:6px;border-bottom:1.5px solid #EEF1F7;background:#F9FAFD}
.rt-b{display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 10px;border:0;border-radius:8px;background:transparent;color:#3A4566;font-family:inherit;font-size:13px;font-weight:500;cursor:pointer}
.rt-b:hover{background:#FFFFFF;color:#0B1433}
.rt-b b{font-size:13px;font-weight:600}
.rt-a{padding:18px 20px;font-size:15px;line-height:1.65;color:#0B1433}
.rt-a p{margin:0}
.rt-a h3{margin:18px 0 8px 0;font-size:17px;font-weight:600}
.rt-a ol{margin:0;padding-left:20px}
.rt-f{padding:10px 20px;border-top:1.5px solid #EEF1F7;font-size:12.5px;color:#5B6582;background:#F9FAFD}
.ra{display:flex;align-items:center;gap:12px;padding:10px 14px 10px 10px;border-radius:12px;background:#F7F9FD}
.ra-i{width:36px;height:36px;flex-shrink:0;border-radius:10px;background:#FFFFFF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.ra-t{flex:1;min-width:0;display:flex;flex-direction:column;gap:2px}
.ra-t b{font-size:14px;font-weight:600}
.ra-t span{font-size:12.5px;color:#5B6582}
.rat{margin-top:12px;display:flex;gap:10px}
.rat .sel{flex:1}
.rat .ds-ghost{height:48px}
.cm{display:flex;gap:12px;padding:10px 0}
.cm + .cm{border-top:1.5px solid #F0F2F8}
.cm-b{flex:1;min-width:0}
.cm-h{display:flex;align-items:center;gap:6px;font-size:13px;color:#5B6582}
.cm-h b{font-size:14px;font-weight:600;color:#0B1433}
.cm-h .ds-link{margin-left:auto;border:0;background:none;font-family:inherit;cursor:pointer;font-size:13px}
.cm-b p{margin:4px 0 0 0;font-size:14.5px;line-height:1.5}
.cmp{margin-top:10px}
.cmp textarea{min-height:64px}
.cmp-f{margin-top:10px;display:flex;align-items:center;justify-content:space-between;gap:10px}
.q{border:1.5px solid #E6EAF3;border-radius:14px}
.q + .q{margin-top:8px}
.q-h{display:flex;align-items:center;gap:12px;padding:12px 12px 12px 14px}
.q-n{width:28px;height:28px;flex-shrink:0;border-radius:50%;background:#F1F3F8;color:#3A4566;font-size:13px;font-weight:600;display:flex;align-items:center;justify-content:center}
.q-open{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.08)}
.q-open .q-n{background:#1652F0;color:#FFFFFF}
.q-h b{flex:1;min-width:0;font-size:14.5px;font-weight:600}
.q-m{display:flex;align-items:center;gap:6px;flex-shrink:0;font-size:12.5px;color:#5B6582}
.q-a{display:flex;align-items:center;gap:4px;flex-shrink:0}
.q-b{display:flex;flex-direction:column;gap:14px;padding:4px 16px 18px 16px;border-top:1.5px solid #EEF1F7;padding-top:16px}
.qo{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;margin-top:-6px}
.qo-r{position:relative;display:block}
.qo-r .ds-in{padding-left:46px}
.qo-c{position:absolute;left:12px;top:50%;width:22px;height:22px;margin-top:-11px;box-sizing:border-box;border-radius:50%;border:1.5px solid #CBD3E6;display:flex;align-items:center;justify-content:center;color:#FFFFFF}
.qo-r.ok .qo-c{background:#0F6B45;border-color:#0F6B45}
.qo-r.ok .ds-in{border-color:#A7D7BF;background:#F4FBF7}
.q-more{margin-top:8px;width:100%;height:42px;border-radius:12px;border:1.5px dashed #C9D2E6;background:none;color:#3A4566;font-family:inherit;font-size:13.5px;font-weight:500;cursor:pointer}
.qa{margin-top:18px;padding-top:16px;border-top:1.5px solid #F0F2F8;display:flex;flex-direction:column;gap:10px}
.qg{margin-top:14px;display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:14px;background:#F5F8FF;font-size:13px;color:#3A4566}
.pct{max-width:140px}
.tgs{display:flex;flex-direction:column}
.ed-s .opt2{grid-template-columns:minmax(0,1fr) !important;display:grid;gap:6px}
.ed-s .ds-seg button{padding:0 8px;font-size:12.5px}
@media (min-width: 961px){.ed-m .tgs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));column-gap:24px}.ed-m .tgs .tg:last-child:nth-child(odd){grid-column:1 / -1}}
.tg{display:flex;align-items:center;gap:14px;width:100%;padding:12px 0;border:0;border-bottom:1.5px solid #F0F2F8;background:none;font-family:inherit;text-align:left;cursor:pointer;color:#0B1433}
.tg:last-child{border-bottom:0}
.tg-t{flex:1;display:flex;flex-direction:column;gap:2px}
.tg-t b{font-size:14.5px;font-weight:500}
.tg-t span{font-size:12.5px;color:#5B6582}
.tg-s{position:relative;width:44px;height:26px;flex-shrink:0;border-radius:999px;background:#D6DDEE;transition:background .2s ease}
.tg-s i{position:absolute;left:3px;top:3px;width:20px;height:20px;border-radius:50%;background:#FFFFFF;box-shadow:0 1px 3px rgba(11,20,51,.2);transition:transform .2s ease}
.tg.on .tg-s{background:#1652F0}
.tg.on .tg-s i{transform:translateX(18px)}
.tg:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:2px}
.rd{list-style:none;margin:14px 0 0 0;padding:12px 0 0 0;border-top:1.5px solid #F4E9C8;display:flex;flex-direction:column;gap:8px}
.rd li{display:flex;gap:9px;font-size:13px;line-height:1.45;color:#3A4566}
.rd li > span{width:18px;height:18px;flex-shrink:0;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700}
.rd li.ok > span{background:#E7F5EE;color:#0F6B45}
.rd li.w > span{background:#FFF4E0;color:#8A5A00}
.tq{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:6px}
.ds-opt.tq-o{flex-direction:column;align-items:flex-start;gap:6px;padding:10px 12px;min-height:0}
.ds-opt.tq-o .ds-opt-ck{display:none}
.ds-opt.tq-o .o-t b{font-size:13px}
.tq-d{display:flex;gap:3px}
.tq-d i{width:12px;height:4px;border-radius:3px;background:#E1E7F4}
.tq-d i.on{background:#AFC1F5}
.ds-opt.tq-o.on .tq-d i.on{background:#1652F0}
.qd2{margin-top:14px;padding-top:12px;border-top:1.5px solid #F0F2F8;display:flex;flex-direction:column;gap:8px}
.qd2-l{font-size:12.5px;font-weight:500;color:#3A4566}
.qd2-l em{font-style:normal;color:#8A93AD;font-weight:400}
.qd2-b{display:flex;gap:2px;height:8px;border-radius:5px;overflow:hidden}
.qd2-b i{transform-origin:left;animation:bdG .8s cubic-bezier(.2,.8,.2,1) both}
.qd2-b .e{background:#34C38F}.qd2-b .m{background:#F4B860;animation-delay:.15s}.qd2-b .h{background:#E5675B;animation-delay:.3s}
.qd2-k{display:flex;flex-wrap:wrap;gap:4px 12px;font-size:12px;color:#3A4566}
.qd2-k > span{display:inline-flex;align-items:center;gap:5px}
.qd2-k i{width:8px;height:8px;border-radius:2px}
.qd2-k .e i{background:#34C38F}.qd2-k .m i{background:#F4B860}.qd2-k .h i{background:#E5675B}
.qd2-k .n{color:#8A93AD}
.qd{margin-top:12px;display:flex;flex-direction:column;gap:2px;padding:10px 12px;border-radius:12px;background:#F7F9FD;font-size:12.5px;color:#5B6582}
.qd b{font-size:13.5px;font-weight:600;color:#0B1433}
.rb{margin-top:4px}
.rb-r{display:grid;grid-template-columns:minmax(0,1fr) 120px 36px;gap:10px;align-items:center;padding:6px 0}
.rb-hd{font-size:12.5px;font-weight:500;color:#8A93AD;padding-bottom:2px}
.rb-add{margin-top:6px;border:0;background:none;font-family:inherit;cursor:pointer;padding:0}
.rb-ok{margin:10px 0 0 0;display:inline-flex;align-items:center;gap:6px;font-size:13px;font-weight:500;color:#0F6B45}
.opt2,.opt3{display:grid;gap:10px}
.opt2{grid-template-columns:repeat(2,minmax(0,1fr))}
.opt3{grid-template-columns:repeat(3,minmax(0,1fr))}
.ds-x.sm:hover{border-color:#D6DDEE;color:#0B1433}
@media (max-width: 1180px){.ed{grid-template-columns:minmax(0,1fr) 320px}}
@media (max-width: 960px){
.bc{margin-bottom:10px;font-size:12.5px}
.eh-i{width:44px;height:44px;border-radius:14px}
.eh{flex-wrap:wrap}
.eh-t{flex-basis:calc(100% - 60px)}
.eh-f{width:100%;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:4px;padding:4px}
.ef-c{padding:10px 12px;min-width:0}
.ef-c + .ef-c{border-left:0}
.ef-c.ef-dl{margin:0}
.ef-c b{font-size:17px}
.ed{grid-template-columns:minmax(0,1fr);margin-top:16px}
.ed-s{position:static;gap:0;border-radius:20px;border:1.5px solid #E6EAF3;background:#FFFFFF;overflow:hidden}
.ed-s > .ds-card{border:0;border-radius:0;box-shadow:none;margin:0}
.ed-s > .ds-card + .ds-card{border-top:1.5px solid #F0F2F8}
.ed-s > .nv-sg{border:0;border-radius:0}
.ed-s > .ec.side{padding:16px 16px 18px 16px}
.ec{padding:18px 16px 20px 16px}
.va{grid-template-columns:repeat(2,minmax(0,1fr))}
.mk-l{grid-template-columns:minmax(0,1fr)}
.qo{grid-template-columns:minmax(0,1fr)}
.q-h{flex-wrap:wrap}
.q-m{order:3;width:100%;padding-left:40px;flex-wrap:wrap}
.opt2,.opt3{grid-template-columns:minmax(0,1fr)}
.ds-seg{flex-wrap:wrap;border-radius:16px}
.rb-r{grid-template-columns:minmax(0,1fr) 72px 36px}
.sv-s{display:flex !important;order:2;justify-content:center}
}
'''

write('Editor.dc.html', doc('Learning item editors · shared source', kit.KIT_CSS + '\n' + dash.DASH_CSS + BASE_CSS + CW_CSS + EDITOR_CSS, EDITOR_BODY, EDITOR_JS))

BOARDS = [
    ('STU-020', 'Builder', {'state': 'team'}, 'CR-STU-020 · Curriculum Builder: team'),
    ('STU-020-SOLO', 'Builder', {'state': 'solo'}, 'CR-STU-020 · Curriculum Builder: solo'),
    ('STU-020-OPEN', 'Builder', {'state': 'open'}, 'CR-STU-020 · Curriculum Builder: open for collaboration'),
    ('STU-020-CO', 'Builder', {'state': 'co'}, 'CR-STU-020 · Curriculum Builder: invited co-creator view'),
    ('STU-021', 'Builder', {'state': 'team', 'overlay': 'add'}, 'CR-STU-021 · Add learning item'),
    ('STU-020-MVL', 'Builder', {'state': 'team', 'overlay': 'mvl'}, 'CR-STU-020 · Move lesson'),
    ('STU-020-MVC', 'Builder', {'state': 'team', 'overlay': 'mvc'}, 'CR-STU-020 · Move chapter'),
    ('STU-020-DEL', 'Builder', {'state': 'team', 'overlay': 'del'}, 'CR-STU-020 · Delete a learning item'),
    ('STU-020-DELC', 'Builder', {'state': 'team', 'overlay': 'delc'}, 'CR-STU-020 · Delete a chapter'),
    ('STU-030', 'Builder', {'state': 'team', 'overlay': 'chat'}, 'CR-STU-030 · Course Team Chat'),
    ('STU-022A', 'Editor', {'kind': 'video'}, 'CR-STU-022A · Video editor'),
    ('STU-022B', 'Editor', {'kind': 'text'}, 'CR-STU-022B · Text editor'),
    ('STU-022B-DEL', 'Editor', {'kind': 'text', 'overlay': 'del'}, 'CR-STU-022B · Delete from inside the editor'),
    ('STU-022D', 'Editor', {'kind': 'live'}, 'CR-STU-022D · Live class editor'),
    ('STU-024', 'Editor', {'kind': 'assess'}, 'CR-STU-024 · Assessment editor'),
    ('STU-025', 'Editor', {'kind': 'project'}, 'CR-STU-025 · Applied learning editor'),
]
OVERLAY = {'STU-030', 'STU-021', 'STU-020-MVL', 'STU-020-MVC', 'STU-020-DEL', 'STU-020-DELC', 'STU-022B-DEL'}

if __name__ == '__main__':
    import sys
    H = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else {}
    for code, src, props, title in BOARDS:
        hd, hm = H.get(code, (900, 844))
        write(code + '.dc.html', wrapper(title + ' · Desktop', src, props, 1440, hd))
        write(code + '-Mobile.dc.html', wrapper(title + ' · Mobile', src, props, 390, hm))
    print('ok', len(BOARDS), 'boards; toggles', B.n, E.n)
