"""Push canvas rows down until no boards overlap (left area, x < 39000). Usage: python3 unoverlap.py <canvas3/project>"""
import json, sys, os
P = os.path.join(sys.argv[1], 'canvas.json'); c = json.load(open(P)); B = c['boards']; N = c['notes']
for it in range(40):
    rows = sorted(set(v['y'] for v in B.values() if v['x'] < 39000)); moved = False
    for i, y in enumerate(rows):
        a = [v for v in B.values() if v['y'] == y and v['x'] < 39000]; bot = max(v['y'] + v['h'] for v in a)
        for y2 in rows[i + 1:]:
            b = [v for v in B.values() if v['y'] == y2 and v['x'] < 39000]
            if y2 < bot + 500 and any(p['x'] < q['x'] + q['w'] and q['x'] < p['x'] + p['w'] for p in a for q in b):
                d = bot + 600 - y2
                for v in B.values():
                    if v['y'] >= y2 and v['x'] < 39000: v['y'] += d
                for v in N.values():
                    if v.get('y', 0) >= y2 - 300 and v.get('x', 0) < 39000: v['y'] += d
                moved = True; break
        if moved: break
    if not moved: break
ov = lambda a, b: a['x'] < b['x'] + b['w'] and b['x'] < a['x'] + a['w'] and a['y'] < b['y'] + b['h'] and b['y'] < a['y'] + a['h']
ks = list(B); print('overlaps', sum(1 for i, a in enumerate(ks) for b in ks[i + 1:] if ov(B[a], B[b])))
open(P, 'w').write(json.dumps(c, indent=2, ensure_ascii=False))
