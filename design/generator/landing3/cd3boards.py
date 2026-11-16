"""Landing batch 3: wrapper boards for the course-detail access states and the lesson preview, plus their canvas row.
Usage: python3 cd3boards.py <canvas3/project> [heights.json]"""
import json, sys, os
D = sys.argv[1]; H = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else {}
W = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>%s</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">
<style>body{margin:0}</style>
</helmet>
<div style="width: %s; height: %dpx; overflow: hidden; background: #FFFFFF">
<dc-import name="%s"%s hint-size="%s,%dpx"></dc-import>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":%d,"height":%d}}'>
class Component extends DCLogic {
  renderVals() { return {}; }
}
</script>
</body>
</html>
'''
B = [('CourseDetail-Short', 'CourseDetail', ' viewer="learner" access="short"', 'COURSES-002 Course Detail · Not enough DLP (120 DLP)'),
     ('CourseDetail-SubOnly', 'CourseDetail', ' viewer="learner" access="subonly"', 'COURSES-002 Course Detail · Subscription only (no Credits route)'),
     ('CourseDetail-Progress', 'CourseDetail', ' viewer="learner" access="progress"', 'COURSES-002 Course Detail · In progress (subscription access)'),
     ('CourseDetail-Owned', 'CourseDetail', ' viewer="learner" access="owned"', 'COURSES-002 Course Detail · Owned with Credits'),
     ('CourseDetail-Temp', 'CourseDetail', ' viewer="learner" access="temp"', 'COURSES-002 Course Detail · Temporary access (institution)'),
     ('CourseDetail-Done', 'CourseDetail', ' viewer="learner" access="done"', 'COURSES-002 Course Detail · Completed, revision period ended'),
     ('CourseDetail-Closed', 'CourseDetail', ' viewer="learner" access="closed"', 'COURSES-002 Course Detail · Closed to new learners'),
     ('LessonPreview', 'LessonPreview', '', 'COURSES-003 Lesson preview · Video lesson (free)'),
     ('LessonPreview-Reading', 'LessonPreview', ' kind="reading"', 'COURSES-003 Lesson preview · Reading lesson (free)')]
c = json.load(open(os.path.join(D, 'canvas.json')))
NEWK = ('CourseDetail-Short', 'CourseDetail-SubOnly', 'CourseDetail-Progress', 'CourseDetail-Owned', 'CourseDetail-Temp', 'CourseDetail-Done', 'CourseDetail-Closed', 'LessonPreview')
Y = max(v['y'] + v['h'] for k, v in c['boards'].items() if not k.startswith(NEWK) and v['x'] < 39000) + 700; x = 0
c['notes']['row-b29'] = {'x': 0, 'y': Y - 300, 'text': 'Batch 29 · Course detail: access states and the free lesson preview', 'kind': 'title1', 'maxW': 8000, 'page': 'main'}
for name, src, props, title in B:
    for suf, w, ws, hs in [('', 1440, '100%', '100%'), ('-Mobile', 390, '390px', '390px')]:
        k = name + suf + '.dc.html'; h = H.get(k, 3000 if src == 'CourseDetail' else 1100)
        if name == src and not suf:
            sp = os.path.join(D, k); t = open(sp).read()
            import re as _re
            t = _re.sub(r'"\$preview":\{"width":1440,"height":\d+\}', '"$preview":{"width":1440,"height":%d}' % h, t); open(sp, 'w').write(t)
        else:
            open(os.path.join(D, k), 'w').write(W % (title + (' · Mobile' if suf else ''), ws, h, src, props, hs, h, w, h))
        c['boards'][k] = {'x': x + (1520 if suf else 0), 'y': Y, 'w': w, 'h': h, 'title': title + (' · Mobile' if suf else ' · Desktop'), 'page': 'main', 'expand': 'fill', 'is_interactive': True}
        if k not in c['order']: c['order'].append(k)
    x += 2150
if 'row-b29' not in c.get('noteOrder', []): c.setdefault('noteOrder', []).append('row-b29')
open(os.path.join(D, 'canvas.json'), 'w').write(json.dumps(c, indent=2, ensure_ascii=False))
print('boards', len(B) * 2)
