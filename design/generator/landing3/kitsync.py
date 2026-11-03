"""Sync kit.py into Landing-canvas pages.

For every page given: rules in the page's first <style> whose (media, selector) also exists in KIT_CSS get the kit's
current body; kit rules (and the keyframes they use) that the page's markup needs but lacks are added. Page-only
rules are left alone. Run after any kit change, then audit + cleancss.

Usage: python3 kitsync.py <page.dc.html> [...]
"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import KIT_CSS

def parse(css):
    """-> list of items: ('rule', media, sel, body) | ('kf', name, text) | ('raw', text)"""
    out, i, n = [], 0, len(css)
    def rules(block, media):
        res = []
        for m in re.finditer(r'([^{}]+)\{([^{}]*)\}', block):
            res.append(('rule', media, m.group(1).strip(), m.group(2)))
        return res
    while i < n:
        while i < n and css[i] in ' \n\t': i += 1
        if i >= n: break
        j = css.find('{', i)
        if j < 0: out.append(('raw', css[i:])); break
        head = css[i:j].strip()
        if head.startswith('@media') or head.startswith('@keyframes') or head.startswith('@supports'):
            d, k = 0, j
            while k < n:
                if css[k] == '{': d += 1
                elif css[k] == '}':
                    d -= 1
                    if d == 0: break
                k += 1
            inner = css[j + 1:k]
            if head.startswith('@keyframes'):
                out.append(('kf', head.split()[1], css[i:k + 1]))
            elif '@' in inner:
                out.append(('raw', css[i:k + 1]))
            else:
                out.extend(rules(inner, head))
            i = k + 1
        else:
            k = css.find('}', j)
            out.append(('rule', '', head, css[j + 1:k])); i = k + 1
    return out

def emit(items):
    lines, cur = [], None
    for it in items:
        media = it[1] if it[0] == 'rule' else ''
        if media != cur:
            if cur: lines.append('}')
            if media: lines.append(media + '{')
            cur = media
        if it[0] == 'rule': lines.append('%s{%s}' % (it[2], it[3]))
        elif it[0] == 'kf': lines.append(it[2])
        else: lines.append(it[1])
    if cur: lines.append('}')
    return '\n'.join(lines)

def classes(sel):
    sel = re.sub(r'::?[a-z-]+(\([^)]*\))?', ' ', sel)
    return set(re.findall(r'\.(-?[A-Za-z_][\w-]*)', sel))

KIT = parse(KIT_CSS)
KR = {(it[1], it[2]): it[3] for it in KIT if it[0] == 'rule'}
KF = {it[1]: it[2] for it in KIT if it[0] == 'kf'}

def sync(path):
    s = open(path, encoding='utf-8').read()
    m = re.search(r'(<style[^>]*>)(.*?)(</style>)', s, re.S)
    css = m.group(2)
    rest = s[:m.start()] + s[m.end():]
    words = set(re.findall(r'[A-Za-z_][\w-]*', re.sub(r'<style[^>]*>.*?</style>', ' ', rest, flags=re.S)))
    items = parse(css)
    have = set()
    changed = 0
    for x, it in enumerate(items):
        if it[0] == 'rule' and (it[1], it[2]) in KR:
            have.add((it[1], it[2]))
            if it[3] != KR[(it[1], it[2])]:
                items[x] = ('rule', it[1], it[2], KR[(it[1], it[2])]); changed += 1
    used_kit = [k for k in have]
    adds = []
    for it in KIT:
        if it[0] != 'rule': continue
        key = (it[1], it[2])
        if key in have: continue
        cls = classes(it[2])
        if not cls or not cls <= words: continue
        if not any(c.startswith(('ds-', 'ob-', 'tip', 'ko-', 'cf', 'nv-', 'nova', 'dlp')) for c in cls): continue
        if not any(classes(k[1]) & cls for k in used_kit) and not any(c in words for c in cls if c.startswith(('ds-', 'tip', 'ko-', 'nv-', 'nova', 'dlp', 'cf'))):
            continue
        adds.append(it); have.add(key)
    kfs = {it[1] for it in items if it[0] == 'kf'}
    allb = ' '.join(it[3] for it in items if it[0] == 'rule') + ' '.join(a[3] for a in adds)
    for name, txt in KF.items():
        if name not in kfs and re.search(r'\b%s\b' % re.escape(name), allb):
            adds.append(('kf', name, txt))
    if adds:
        top = [a for a in adds if a[0] == 'kf' or a[1] == '']
        med = [a for a in adds if a[0] == 'rule' and a[1]]
        pos = 1 if items and items[0][0] == 'rule' and items[0][2] == 'body' else 0
        items[pos:pos] = top
        for a in med:
            idx = max([x for x, it in enumerate(items) if it[0] == 'rule' and it[1] == a[1]] or [-1])
            if idx >= 0: items.insert(idx + 1, a)
            else: items.append(a)
    new = emit(items)
    if new != css:
        s = s[:m.start(2)] + '\n' + new + '\n' + s[m.end(2):]
        open(path, 'w', encoding='utf-8').write(s)
    print(os.path.basename(path), 'updated', changed, 'added', len(adds))

if __name__ == '__main__':
    for p in sys.argv[1:]: sync(p)
