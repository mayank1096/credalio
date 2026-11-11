"""Build project/canvas.json for the Link 4 canvas from the batch board lists and measured heights.

Usage: python3 layout.py heights.json [more.json …]   ({code: [desktop_h, mobile_h]}, merged)
Each row: title note, then desktop + mobile pairs left to right. Shared sources sit in the last row.
"""
import json, os, sys
from l4kit import OUT
import stu1, stu2, stu3, stu4, stu5, stu6, stu7, stu8, stu10, stu11, stu12, stu13

PAIR, GAP, ROWGAP = 1440 + 80 + 390, 160, 420
H = {}
for f in sys.argv[1:]:
    H.update(json.load(open(f)))
T = {c: t for c, _, _, t in stu1.BOARDS + stu2.BOARDS + stu3.BOARDS + stu4.BOARDS + stu5.BOARDS + stu6.BOARDS + stu7.BOARDS + stu8.BOARDS + stu10.BOARDS + stu11.BOARDS + stu12.BOARDS + stu13.BOARDS}

ROWS = [
    ('b1-setup', 'Batch 1 · Course setup: learning experience, delivery type, setup review, how you’ll create it, Studio welcome', ['STU-001', 'STU-002', 'STU-003', 'STU-004', 'STU-008']),
    ('b1-design-a', 'Batch 1 · Course design: Studio home, basics, audience, career & skills', ['STU-009', 'STU-010', 'STU-011', 'STU-012', 'STU-012b', 'STU-013']),
    ('b1-design-b', 'Batch 1 · Course design: outcomes, skills map, evidence, assessment & award, effort, summary', ['STU-014', 'STU-015', 'STU-016', 'STU-017', 'STU-018', 'STU-019']),
    ('b2-builder', 'Batch 2 · Curriculum Builder: team, solo, open for collaboration, invited co-creator', ['STU-020', 'STU-020-SOLO', 'STU-020-OPEN', 'STU-020-CO']),
    ('b2-actions', 'Batch 2 · Builder actions: add learning item, move lesson, move chapter, delete item, delete chapter', ['STU-021', 'STU-020-MVL', 'STU-020-MVC', 'STU-020-DEL', 'STU-020-DELC']),
    ('b2-editors', 'Batch 2 · Learning item editors: video, text (+ delete), live class, assessment, applied learning', ['STU-022A', 'STU-022B', 'STU-022B-DEL', 'STU-022D', 'STU-024', 'STU-025']),
    ('b3-build', 'Batch 3 · Build tools: resource library, completion rules, team & assignments, my work, team chat', ['STU-026', 'STU-027', 'STU-028', 'STU-029', 'STU-028-SOLO', 'STU-030']),
    ('b3-views', 'Batch 3 · DLP & effort, course assessments, practice & projects, delivery, learner experience, learner support', ['STU-031', 'STU-ASM', 'STU-PRA', 'STU-DEL', 'STU-LX', 'STU-SUP']),
    ('b3-pricing', 'Batch 3 · Access & pricing: access model, maintenance burden, pricing, pricing update required, summary', ['STU-032', 'STU-033', 'STU-034', 'STU-034b', 'STU-035']),
    ('b4-review', 'Batch 4 · Prepare: course review, marketplace preview, learner preview pages, intelligence profile', ['STU-040', 'STU-040M', 'STU-PRV', 'STU-PRV-L', 'STU-041']),
    ('b4-ready', 'Batch 4 · Prepare: Nova course review, readiness checks, issues to resolve', ['STU-042', 'STU-043', 'STU-044']),
    ('b4-submit', 'Batch 4 · Submit for validation: intake, declaration, creator readiness, scope, quote, payment (short / enough), submitted', ['STU-045', 'STU-046', 'STU-047', 'STU-048', 'STU-049', 'STU-050', 'STU-051', 'STU-052']),
    ('b5-validate', 'Batch 5 · Validation: awaiting assignment, validators assigned, workspace overview, requests, evidence, meeting, findings', ['STU-053', 'STU-054', 'STU-055', 'STU-055A', 'STU-055B', 'STU-055C', 'STU-055D']),
    ('b5-decision', 'Batch 5 · Decision: improvements required, course revision, resubmission, passed validation', ['STU-056', 'STU-057', 'STU-058', 'STU-059']),
    ('b5-publish', 'Batch 5 · Publish: final pricing (within / outside range), revenue confirmation, marketplace listing, course is live', ['STU-060', 'STU-060b', 'STU-061', 'STU-062', 'STU-065']),
    ('b6-hub', 'Batch 6 · Manage Published Course: hub, Publishing & Visibility, Manage Availability (step 2 / step 3), paused, hidden', ['MGT-001', 'MGT-002', 'MGT-002-EDIT', 'MGT-002-REVIEW', 'MGT-002B', 'MGT-002C']),
    ('b6-states', 'Batch 6 · Publishing states: unpublished, restricted, organization approval, save error, restriction notice', ['MGT-002D', 'MGT-002E', 'MGT-002F', 'MGT-002G', 'MGT-002-NOTICE']),
    ('b6-unpub', 'Batch 6 · Unpublish: impact, reason & transition, confirm, unpublished, requires review · Downstream: course overview, My Creations, learner My Learning', ['MGT-003A', 'MGT-003B', 'MGT-003C', 'MGT-003D', 'MGT-003E', 'MGT-DS-OV', 'MGT-DS-CR', 'MGT-DS-ML']),
    ('b7-pricing', 'Batch 7 · Pricing & Access: overview, edit (step 1), review (step 2), updated, pending approval, invalid change, pricing history', ['MGT-004', 'MGT-004-D', 'MGT-004-E', 'MGT-004-G', 'MGT-004-F', 'MGT-004-H', 'MGT-004-I']),
    ('b7-versions', 'Batch 7 · Course Updates & Versions: with draft, no draft, create update, compare, readiness, under validation, changes requested, activate, history', ['MGT-005', 'MGT-005-NONE', 'MGT-005-CREATE', 'MGT-005-COMPARE', 'MGT-005-READY', 'MGT-005-VALIDATE', 'MGT-005-CHANGES', 'MGT-005-ACTIVATE', 'MGT-005-HISTORY']),
    ('b7-learners', 'Batch 7 · Learner Access & Enrollment: dashboard, empty, learner detail drawer, version assignments, access impact, unpublished', ['MGT-006', 'MGT-006-EMPTY', 'MGT-006-DETAIL', 'MGT-006-ASSIGN', 'MGT-006-IMPACT', 'MGT-006-UNPUB']),
    ('b8-validation', 'Batch 8 · Validation History: overview, record details, case history, findings, version relationship, required actions', ['MGT-007', 'MGT-007A', 'MGT-007B', 'MGT-007C', 'MGT-007D', 'MGT-007E-REV', 'MGT-007E-CHG']),
    ('b8-archive', 'Batch 8 · Archive & Removal: home, impact, confirm, archived, archived course, restore, removal request, removal status, restricted', ['MGT-008', 'MGT-008A', 'MGT-008B', 'MGT-008C', 'MGT-008D', 'MGT-008E', 'MGT-008F', 'MGT-008G', 'MGT-008H']),
    ('b8-insights', 'Batch 8 · Insights & Engagement: hub, learning performance, assessments, content health, reviews, questions & support, discussion', ['MGT-009', 'MGT-009A', 'MGT-009B', 'MGT-009C', 'MGT-009D', 'MGT-009E', 'MGT-009F']),
    ('b9-credits', 'Batch 9 · Course Credits & Visibility: credits manager, ask to credit, learner course page with 2 and 5 creators, creators panel', ['CREDITS', 'CREDITS-ASK', 'LEARN-CREATORS-2', 'LEARN-CREATORS-5', 'LEARN-CREATORS-PANEL']),
    ('b10-invite', 'Batch 10 · Collaboration: collaboration centre, invite (+ allocation error), roles & permissions (invitation, role changed, accepted, offer), review, sent', ['COL-001', 'COL-002', 'COL-002-ERR', 'COL-002B', 'COL-002B-ROLE', 'COL-002B-EDIT', 'COL-002B-OFFER', 'COL-003', 'COL-003-SENT']),
    ('b10-manage', 'Batch 10 · Manage collaborators: active, pending, past, activity, collaborator detail, withdraw invitation · Remove: impact, reason, executed, sent to review', ['COL-004', 'COL-004-PENDING', 'COL-004-PAST', 'COL-004-ACTIVITY', 'COL-004-DETAIL', 'COL-004-WITHDRAW', 'COL-005A', 'COL-005B', 'COL-005C', 'COL-005C-REVIEW']),
    ('b11-setup', 'Batch 11 · Open collaboration: opportunity, expertise, qualifications, revenue, review & publish, published, preview as creator', ['COL-006A', 'COL-006B', 'COL-006C', 'COL-006D', 'COL-006E', 'COL-006F', 'COL-007']),
    ('b11-apps', 'Batch 11 · Applications: all, new, shortlisted, offered, declined, applicant detail, clarification (request, sent, reply), decline, withdraw offer, offer withdrawn', ['COL-008', 'COL-008-NEW', 'COL-008-SHORTLISTED', 'COL-008-OFFERED', 'COL-008-DECLINED', 'COL-008-DETAIL', 'COL-008-CLARIFY', 'COL-008-CLARIFY-SENT', 'COL-008-CLARIFY-REPLY', 'COL-008-DECLINE-APP', 'COL-008-WITHDRAW-OFFER', 'COL-008-OFFER-WITHDRAWN']),
    ('b11-manage', 'Batch 11 · Make an offer · Opportunity management: open, no applications, paused, filled, closed, withdraw', ['COL-009', 'COL-010', 'COL-010-EMPTY', 'COL-010-PAUSED', 'COL-010-FILLED', 'COL-010-CLOSED', 'COL-010-WITHDRAW']),
    ('b12-invites', 'Batch 12 · My Invitations: pending, accepted, declined, all, empty · details (pending, expired, withdrawn) · accept · decline · Shared Courses', ['INV-001', 'INV-001-ACCEPTED', 'INV-001-DECLINED', 'INV-001-ALL', 'INV-001-EMPTY', 'INV-002', 'INV-002-EXPIRED', 'INV-002-WITHDRAWN', 'INV-003', 'INV-004', 'NAV-002']),
    ('b12-outcomes', 'Batch 12 · Invitation outcomes: accepted, activation pending, declined, expired, withdrawn, already responded, superseded', ['INV-005A', 'INV-005B', 'INV-005C', 'INV-005D', 'INV-005E', 'INV-005F', 'INV-005G']),
    ('b13-opps', 'Batch 13 · Opportunities, details (eligible / not eligible), apply, update Creator Profile, submitted for verification', ['OPP-001', 'OPP-002', 'OPP-002-INELIGIBLE', 'OPP-003', 'OPP-005', 'OPP-005-SUBMITTED']),
    ('b13-apps', 'Batch 13 · My Applications: pending, under review, shortlisted, offer received, accepted, declined, withdrawn, withdraw, reply to clarification', ['OPP-004', 'OPP-004-REVIEW', 'OPP-004-SHORTLISTED', 'OPP-004-OFFER', 'OPP-004-ACCEPTED', 'OPP-004-DECLINED', 'OPP-004-WITHDRAWN', 'OPP-004-WITHDRAW', 'OPP-004-CLARIFY']),
    ('b14-launch', 'Batch 14 · Launch: full validation report, subscription-only pricing, publish confirmation, share & promote, first learner state', ['STU-RPT', 'STU-SUB', 'STU-064', 'STU-066', 'STU-067']),
]
SOURCES = [('Setup.dc.html', 'Course setup · shared source'), ('Studio.dc.html', 'Course Studio · shared source'),
           ('Builder.dc.html', 'Curriculum Builder · shared source'), ('Editor.dc.html', 'Learning item editors · shared source'),
           ('Course.dc.html', 'Course set-up · shared source'), ('Prepare.dc.html', 'Prepare · shared source'),
           ('Submit.dc.html', 'Submit for validation · shared source'), ('Preview.dc.html', 'Creator Preview · shared source'),
           ('Validate.dc.html', 'Validate · shared source'), ('Publish.dc.html', 'Publish · shared source'),
           ('Manage.dc.html', 'Manage Published Course · shared source'), ('Unpublish.dc.html', 'Unpublish · shared source'), ('Learner.dc.html', 'Learner app · shared source'),
           ('Manage2.dc.html', 'Manage Published Course (pricing, versions, learners) · shared source'),
           ('Manage3.dc.html', 'Manage Published Course (validation, archive, insights) · shared source'),
           ('Collab.dc.html', 'Course collaboration (invite, permissions, manage, remove) · shared source'),
           ('Collab2.dc.html', 'Open collaboration (setup, applications, offers, manage opportunity) · shared source'),
           ('Collab3.dc.html', 'Collaboration, creator side (my invitations, shared courses) · shared source'),
           ('Collab4.dc.html', 'Collaboration, creator side (opportunities, applications, creator profile) · shared source')]

boards, order, notes = {}, [], {}
y = 300
for nid, text, codes in ROWS:
    notes[nid] = {'kind': 'title1', 'maxW': min(8000, len(codes) * (PAIR + GAP) - GAP), 'text': text, 'w': 240, 'x': 0, 'y': y - 300}
    notes[nid + '-new'] = {'x': 0, 'y': y - 150, 'text': 'NEW · batch %s' % nid[1:].split('-')[0], 'w': 260, 'fill': 'pink'}
    if nid == 'b2-builder':
        notes['b2-missing'] = {'x': 300, 'y': y - 150, 'text': 'Not built yet: CR-STU-023 Assessment Type and CR-STU-020B Curriculum Readiness (solo + team). The client file refuses to open these three boards, so their content is missing.', 'w': 1100, 'fill': 'red'}
    if nid == 'b10-invite':
        notes['b10-missing'] = {'x': 300, 'y': y - 150, 'text': 'Not built yet: CR-COL-001-SOLO (collaboration centre, solo empty state). The client file refuses to open this board.', 'w': 900, 'fill': 'yellow'}
    if nid == 'b1-setup':
        notes['b1-format'] = {'x': 300, 'y': y - 150, 'text': 'CR-STU-001 uses the same format-card design as Link 1 Create new (CR-HOME-NEW): one design for the format picker.', 'w': 900, 'fill': 'blue'}
    x, mh = 0, 0
    for c in codes:
        hd, hm = H[c]
        for name, w, h, sx in [(c + '.dc.html', 1440, hd, x), (c + '-Mobile.dc.html', 390, hm, x + 1520)]:
            boards[name] = {'x': sx, 'y': y, 'w': w, 'h': h, 'title': T[c] + (' · Desktop' if w > 600 else ' · Mobile'),
                            'page': 'main', 'is_interactive': True, 'expand': 'fill'}
            order.append(name)
        mh = max(mh, hd, hm)
        x += PAIR + GAP
    y += mh + ROWGAP
notes['sources'] = {'kind': 'title1', 'maxW': 3200, 'text': 'Shared sources (code the boards above import, not screens)', 'w': 240, 'x': 0, 'y': y - 300}
x = 0
for name, title in SOURCES:
    boards[name] = {'x': x, 'y': y, 'w': 1440, 'h': 900, 'title': title, 'page': 'main', 'is_interactive': True, 'expand': 'fill'}
    order.append(name); x += 1440 + GAP

p = os.path.join(OUT, 'canvas.json')
old = json.load(open(p)) if os.path.exists(p) else {}
c = {'v': 3, 'createdOnFiles': old.get('createdOnFiles', {'v': 1, 'at': '2026-11-08T06:00:00Z'}), 'title': 'Credalio · Link 4 · Course Studio',
     'launch': {'view': 'canvas'}, 'pages': [{'id': 'main', 'name': 'Course Studio'}], 'boards': boards, 'order': order,
     'notes': notes, 'noteOrder': list(notes), 'designSystems': []}
if 'attachments' in old: c['attachments'] = old['attachments']
json.dump(c, open(p, 'w'), ensure_ascii=False, indent=2)
import aur4
aur4.run(OUT)
print(len(boards), 'boards')
