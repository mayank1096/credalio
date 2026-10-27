# cl1012c: cleanup of the last 10 Link 1 screens (designer 2026-10-12). Patches live files in <dir>.
import re, sys, os
P = sys.argv[1]
def rd(f): return open(os.path.join(P, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(P, f), 'w', encoding='utf-8').write(s)
def sub1(s, a, b):
    assert s.count(a) == 1, (s.count(a), a[:80]); return s.replace(a, b, 1)
# ORI-001 start: stats repeat the subtitle ("Seven" modules) and module 1's line repeats its steps
s = rd('CR-ORI-001.dc.html')
i = s.index('<sc-if value="{{isStart}}"'); j = s.index('</sc-if>', i)
b = s[i:j]
b = re.sub(r'<dl class="or-stats">.*?</dl>', '', b, flags=re.S)
b = re.sub(r'<p class="or-desc">[^<]*</p>', '', b)
s = s[:i] + b + s[j:]
# ORI-001 done: the rail already says all 7 are done, so no Done pill per row and no extra line
i = s.index('<sc-if value="{{isDone}}"'); j = s.index('</sc-if>', i)
b = s[i:j]
b = re.sub(r'<span class="st-pill" style="background: #E7F5EE; color: #0F6B45">.*?Done</span>', '', b, flags=re.S)
b = sub1(b, '<span class="or-ns">Orientation counts toward your readiness.</span>', '')
s = s[:i] + b + s[j:]
wr('CR-ORI-001.dc.html', s)
# M1-00: lessons + check are listed in Steps right below
s = rd('CR-ORI-M1-00.dc.html')
s = re.sub(r'<span>(<svg(?:(?!</svg>).)*</svg>)2 lessons</span>', '', s, count=1, flags=re.S)
s = re.sub(r'<span>(<svg(?:(?!</svg>).)*</svg>)Quick check</span>', '', s, count=1, flags=re.S)
assert '2 lessons</span>' not in s and 'Quick check</span>' not in s
wr('CR-ORI-M1-00.dc.html', s)
# Lessons: step count is already in the top bar, the rail and the bottom bar
for f in ['CR-ORI-M1-L1.dc.html', 'CR-ORI-M1-L2.dc.html']:
    s = rd(f); s = re.sub(r'(<span class="lp-eb ob-in">)Step \d+ of \d+ · about (\d+) min read', r'\1About \2 min read', s, count=1)
    assert 'About ' in s; wr(f, s)
s = rd('CR-ORI-M1-L2.dc.html'); s = sub1(s, ' Three stages, always in this order.', ''); wr('CR-ORI-M1-L2.dc.html', s)
# Check: the H1 already says "Two quick questions"
s = rd('CR-ORI-M1-K.dc.html'); s = re.sub(r'<p class="lp-meta ob-in2">[^<]*</p>', '', s, count=1); wr('CR-ORI-M1-K.dc.html', s)
print('cl1012c ok')
