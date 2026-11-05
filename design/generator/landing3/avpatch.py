"""Put the designer's people photos into every person avatar (initials circles) on Landing-canvas pages.

Photos (240px crops, design/illustrations/avatars/, uploaded to the canvas):
  av-f1 laughing, dark hair  · av-f2 light-brown hair  · av-m1 beard, glasses  · av-m2 curly hair, glasses
Initials stay in the markup as the fallback; the photo sits on top (.pav). Organisation initials (NU, MU, NA, CU …) and
validator role badges keep their initials. Idempotent: run after any generator and after kitsync.

Usage: python3 avpatch.py <page.dc.html> [...]
"""
import re, sys

F1 = '/_blob/84f08b38fbe9b11d8aa477ac10398bfe'
F2 = '/_blob/9112077cc7e3c1c839edc7e609d87954'
M1 = '/_blob/6940b199369f0ef8a87915557d16027b'
M2 = '/_blob/54e6db3b8b5f0875ac9ee0cfd0aef3d2'

# people by initials (fictional personas); AO = Ada Ononuju (the learner) except where it means Amara Okafor (creator)
PEOPLE = {'AO': F2, 'DR': M1, 'TA': M2, 'TH': M2, 'TR': M1, 'PN': F1, 'GA': F2, 'ML': F1, 'HC': F2, 'LF': F2, 'PS': F1,
          'LO': F2, 'MR': F1, 'SA': F2, 'SM': F1, 'KB': M1, 'JM': M2, 'SL': F2, 'AK': M2, 'MS': F1, 'PL': M1, 'SR': M1,
          'JL': M2, 'ME': F1, 'MO': F1, 'KA': M1, 'IN': F2, 'DA': M2,
          'DM': M2, 'TB': M1, 'RP': M2, 'NB': F1, 'LK': F2, 'JC': M1, 'DK': M2}
CREATOR_AO = F1                      # Amara Okafor
CREATOR_CLS = {'cd-av', 'cd-cav', 'cs-cav', 'ci-av'}
PERSON_CLS = {'sx-av', 'cd-av', 'cd-cav', 'cd-rav', 'cs-cav', 'ci-av', 'lr-av', 'lr-gv-you', 'av', 'jy-me', 'jp-me',
              'bp-av', 'pd2-av'}

CSS = ('.pav{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;border-radius:inherit;display:block;pointer-events:none}\n'
       '.pav-h{position:relative !important;overflow:hidden !important}\n')
JS = ('var AVP = ' + str({k: v for k, v in PEOPLE.items() if k != 'AO'}).replace("'", '"') + ';\n'
      'AVP.AO = "' + CREATOR_AO + '";\nfunction PIC(i) { return AVP[i] || ""; }\n')

def img(src): return '<img class="pav" src="%s" alt="">' % src

def patch(s):
    if 'class="pav"' in s or 'function PIC(' in s:
        return s, 0
    n = 0
    # 1 · static initials in person-avatar elements
    def rep(m):
        nonlocal n
        tag, attrs, cls, ini = m.group(1), m.group(2), m.group(3), m.group(4)
        first = cls.split()[0]
        if first not in PERSON_CLS or ini not in PEOPLE: return m.group(0)
        src = CREATOR_AO if (ini == 'AO' and first in CREATOR_CLS) else PEOPLE[ini]
        n += 1
        attrs2 = attrs.replace('class="%s' % cls, 'class="%s pav-h' % cls, 1)
        return '<%s%s>%s%s' % (tag, attrs2, ini, img(src))
    s = re.sub(r'<(span|a|div|i|b)(\s[^>]*class="([^"]*)"[^>]*)>([A-Z]{2})(?=<)', rep, s)
    # 1b · class-less spans inside the program cohort stack
    def stack(m):
        nonlocal n
        inner = m.group(2)
        def one(k):
            nonlocal n
            ini = k.group(2)
            if ini not in PEOPLE: return k.group(0)
            n += 1
            return '<span%s class="pav-h">%s%s</span>' % (k.group(1), ini, img(PEOPLE[ini]))
        return m.group(1) + re.sub(r'<span((?:\s+style="[^"]*")?)>([A-Z]{2})</span>', one, inner)
    s = re.sub(r'(<span class="pd2-avs"[^>]*>)(.*?</span></span>)', stack, s, flags=re.S)
    # 2 · data-driven avatars: {{x.ini}} gets {{x.pic}}
    def tpl(m):
        nonlocal n
        v = m.group(1); n += 1
        return '{{%s.ini}}<sc-if value="{{%s.pic}}" hint-placeholder-val="{{ false }}">%s</sc-if>' % (v, v, img('{{%s.pic}}' % v))
    s = re.sub(r'\{\{([a-z]+(?:\.[a-z]+)?)\.ini\}\}(?=</span>)', tpl, s)
    # avatar containers that hold a data-driven photo need the holder class
    s = re.sub(r'class="(cs-cav|bp-av)"(?=[^>]*>\{\{[a-z.]+\.ini\}\})', r'class="\1 pav-h"', s)
    # JS: every `ini: EXPR` also exposes `pic: PIC(EXPR)`
    out, i = [], 0
    for m in re.finditer(r'\bini: ', s):
        if m.start() < i: continue
        j = m.end(); d = 0; k = j
        while k < len(s):
            ch = s[k]
            if ch in '([{': d += 1
            elif ch in ')]}':
                if d == 0: break
                d -= 1
            elif ch == ',' and d == 0: break
            elif ch in '\'"':
                q = ch; k += 1
                while s[k] != q: k += 2 if s[k] == '\\' else 1
            k += 1
        expr = s[j:k]
        out.append(s[i:k] + ', pic: PIC(%s)' % expr); i = k
    if out:
        s = ''.join(out) + s[i:]
        s = s.replace('<script type="text/x-dc" data-dc-script', '<script type="text/x-dc" data-dc-script', 1)
        m = re.search(r'(<script type="text/x-dc" data-dc-script[^>]*>)', s)
        s = s[:m.end()] + '\n' + JS + s[m.end():]
    if n or out:
        k = s.index('</style>'); s = s[:k] + CSS + s[k:]
    return s, n + len(out)

if __name__ == '__main__':
    for f in sys.argv[1:]:
        s = open(f).read(); t, n = patch(s)
        if t != s: open(f, 'w').write(t)
        print(f, n)
