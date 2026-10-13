# build53: last Link 1 states. PATCHES live CR-COL-002 (variant consentall = COL-003d: all 6 ticked, Accept and join on) and
# CR-DEC-001 (variant leaddone = DEC-004f: both lead statements ticked + name typed, Sign and submit on). usage: python3 build53.py <dir>
import re, sys, os
P = sys.argv[1]
def rd(f): return open(os.path.join(P, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(P, f), 'w', encoding='utf-8').write(s); OUT.append(f)
OUT = []
def sub(s, a, b, n=1):
    assert s.count(a) >= 1, a[:90]; return s.replace(a, b, n)
WRAP = rd('CR-KYC-002b.dc.html')
def boards(n, imp, var, title, mob_tpl, mh):
    d = WRAP.replace('<dc-import name="CR-KYC-002" variant="photos"', f'<dc-import name="{imp}" variant="{var}"')
    d = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', d); wr(n + '.dc.html', d)
    m = rd(mob_tpl); m = re.sub(f'<dc-import name="{imp}"( variant="[^"]*")?', f'<dc-import name="{imp}" variant="{var}"', m, count=1)
    m = re.sub(r'<title>.*?</title>', f'<title>{n} mobile preview</title>', m)
    m = re.sub(r'height: \d+px; overflow', f'height: {mh}px; overflow', m, count=1); m = re.sub(r'hint-size="390px,\d+px"', f'hint-size="390px,{mh}px"', m)
    m = re.sub(r'"\$preview":\{"width":390,"height":\d+\}', f'"$preview":{{"width":390,"height":{mh}}}', m); wr(n + '-Mobile.dc.html', m)
s = rd('CR-COL-002.dc.html'); assert 'consentall' not in s
s = sub(s, "this.state = { v, cons: v === 'consent' ? { 0: 1, 1: 1, 2: 1 } : {},",
        "this.state = { v: v === 'consentall' ? 'consent' : v, cons: v === 'consentall' ? { 0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1 } : (v === 'consent' ? { 0: 1, 1: 1, 2: 1 } : {}),")
wr('CR-COL-002.dc.html', s)
boards('CR-COL-003d', 'CR-COL-002', 'consentall', 'Credalio · Invitation: ready to join', 'CR-COL-003-Mobile.dc.html', 1250)
s = rd('CR-DEC-001.dc.html'); assert 'leaddone' not in s
s = sub(s, "const v = (props && props.variant) || 'request'; this.state = { v, ck: v === 'declare' ? { 0: 1, 1: 1 } : {}, lk: {}, name: '', rem: false }; }",
        "const v0 = (props && props.variant) || 'request', done = v0 === 'leaddone', v = done ? 'lead' : v0; this.state = { v, ck: v === 'declare' ? { 0: 1, 1: 1 } : {}, lk: done ? { 0: 1, 1: 1 } : {}, name: done ? 'Ada Ononuju' : '', rem: false }; }")
wr('CR-DEC-001.dc.html', s)
boards('CR-DEC-004f', 'CR-DEC-001', 'leaddone', 'Credalio · Submit for validation: signed', 'CR-DEC-004-Mobile.dc.html', 900)
print('build53 ok'); print(' '.join(OUT))
