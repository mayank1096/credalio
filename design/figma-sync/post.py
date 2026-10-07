#!/usr/bin/env python3
"""tree.json (+cap pngs) -> compact node tree + trimmed pngs.
usage: post.py <outdir/NAME>  -> writes NAME/c.json and NAME/img/*.png"""
import json, sys, os
from PIL import Image

D = sys.argv[1]
T = json.load(open(os.path.join(D, 'tree.json')))
W, H = T['w'], T['h']
caps = {c['id']: c for c in T['caps']}
os.makedirs(os.path.join(D, 'img'), exist_ok=True)
EPS = 1.5
GENERIC = {'div', 'span', 'b', 'p', 'li', 'ul', 'a', 'label', 'button', 'strong', 'em', 'section', 'header', 'main', 'nav', 'aside', 'footer', 'i', 'small', 'root'}

def trim(cid):
    c = caps.get(cid)
    p = os.path.join(D, cid + '.png')
    if not c or 'clip' not in c or not os.path.exists(p):
        return None
    im = Image.open(p).convert('RGBA')
    bb = im.getchannel('A').point(lambda a: 255 if a > 3 else 0).getbbox()
    if not bb:
        return None
    im.crop(bb).save(os.path.join(D, 'img', cid + '.png'), optimize=True)
    x, y = c['clip']
    return [x + bb[0] / 2, y + bb[1] / 2, (bb[2] - bb[0]) / 2, (bb[3] - bb[1]) / 2]

def hexc(c):
    s = '%02x%02x%02x' % tuple(int(v) for v in c[:3])
    a = c[3] if len(c) > 3 else 1
    return s if a >= 0.995 else s + '%02x' % round(a * 255)

def has_vis(n):
    return any(k in n for k in ('bg', 'st', 'fx', 'self')) or n.get('clip') or n.get('op')

def pad_of(n):
    css = n.get('css') or {}
    p = css.get('pad', [0, 0, 0, 0]); b = css.get('bw', [0, 0, 0, 0])
    return [p[i] + b[i] for i in range(4)]

def prep(n):
    """resolve images, drop empties, collapse wrappers. returns node or None"""
    k = n['k']
    if k == 'I':
        bx = trim(n['img'])
        if not bx: return None
        n['box'] = bx
        return n
    if k in ('T', 'S'):
        return n
    if n.get('self'):
        bx = trim(n['self'])
        if bx: n['selfbox'] = bx
        else: del n['self']
    ch = [c for c in (prep(c) for c in n.get('ch', [])) if c]
    n['ch'] = ch
    x, y, w, h = n['box']
    if not ch and not has_vis(n):
        return None
    if w < 0.5 and h < 0.5 and not ch:
        return None
    # collapse plain wrapper with single child
    if len(ch) == 1 and not has_vis(n) and sum(pad_of(n)) == 0 and n['n'] != 'root':
        c = ch[0]
        cb = c['box']
        same = all(abs(cb[i] - n['box'][i]) <= EPS for i in range(4))
        if c['k'] == 'T' or same:
            if n.get('abs'): c['abs'] = True
            if n.get('grow'): c['grow'] = 1
            if c['k'] == 'T' and same is False:
                # text inside a block wrapper: keep T but adopt wrapper box for multi-line width
                pass
            if c['k'] == 'F' and c['n'] in GENERIC and n['n'] not in GENERIC:
                c['n'] = n['n']
            c['_wrapbox'] = n['box']
            if c['k'] == 'T' and not c.get('ml') and n['box'][2] > c['box'][2] + 2:
                c['box'] = [n['box'][0], c['box'][1], n['box'][2], c['box'][3]]; c['fw'] = 1
            return c
    return n

def rel(box, o):
    return [round(box[0] - o[0], 1), round(box[1] - o[1], 1), round(box[2], 1), round(box[3], 1)]

def lay_box(c):
    """box used for layout checks (wrapper box if collapsed)"""
    return c.get('_wrapbox') or c['box']

def infer(n):
    ch = [c for c in n['ch'] if not c.get('abs')]
    if not ch: return None
    css = n.get('css') or {}
    disp = css.get('disp', 'block')
    x, y, w, h = n['box']
    p = pad_of(n)  # t r b l
    cands = []
    if 'flex' in disp:
        if css.get('wrap') == 'wrap' and len(ch) > 1:
            pass
        cands = ['H' if 'row' in (css.get('dir') or 'row') else 'V']
        if 'reverse' in (css.get('dir') or ''): return None
    else:
        cands = ['V', 'H'] if len(ch) > 1 else ['V']
    for d in cands:
        res = try_dir(n, ch, d, p, css)
        if res: return res
    return None

def try_dir(n, ch, d, p, css):
    x, y, w, h = n['box']
    if d == 'H':
        ms, ml, cs_, cl = 0, 2, 1, 3; size, csize = w, h; ps, pe, cps, cpe = p[3], p[1], p[0], p[2]; o, co = x, y
    else:
        ms, ml, cs_, cl = 1, 3, 0, 2; size, csize = h, w; ps, pe, cps, cpe = p[0], p[2], p[3], p[1]; o, co = y, x
    bs = [lay_box(c) for c in ch]
    starts = [b[ms] - o for b in bs]; ends = [b[ms] - o + b[ml] for b in bs]
    for i in range(1, len(bs)):
        if starts[i] < ends[i - 1] - 0.6: return None
    gaps = [starts[i] - ends[i - 1] for i in range(1, len(bs))]
    sb = False; gap = 0
    if gaps:
        if css.get('jc') == 'space-between' and d == ('H' if 'row' in (css.get('dir') or 'row') else 'V') and 'flex' in css.get('disp', ''): sb = True
        elif max(gaps) - min(gaps) <= EPS: gap = round(sum(gaps) / len(gaps))
        else: return None
    s0 = starts[0] - ps; e0 = size - pe - ends[-1]
    if sb:
        if abs(s0) > EPS or abs(e0) > EPS: return None
        pa = 'SB'
    elif abs(s0) <= EPS: pa = 'MIN'
    elif abs(s0 - e0) <= EPS: pa = 'CENTER'
    elif abs(e0) <= EPS: pa = 'MAX'
    elif s0 > 0 and e0 > 0 and len(ch) == 1:  # odd offset: absorb into padding
        pa = 'MIN'; ps = starts[0]
    else: return None
    avail = csize - cps - cpe
    opts = None; fills = []
    for b in bs:
        t = b[cs_] - co - cps; bt = csize - cpe - (b[cs_] - co + b[cl])
        s = set()
        if abs(t) <= EPS: s.add('MIN')
        if abs(t - bt) <= EPS: s.add('CENTER')
        if abs(bt) <= EPS: s.add('MAX')
        fills.append(abs(t) <= EPS and abs(bt) <= EPS and avail > 0)
        opts = s if opts is None else opts & s
        if not opts: break
    if not opts:
        if len(ch) == 1:
            b = bs[0]; t = b[cs_] - co - cps
            if t > 0: cps = cps + t; opts = {'MIN'}
            else: return None
        else: return None
    ca = 'MIN' if 'MIN' in opts else ('CENTER' if 'CENTER' in opts else 'MAX')
    if d == 'H': pad = [cps, pe, cpe, ps]
    else: pad = [ps, cpe, pe, cps]
    if any(v < -0.5 for v in pad): return None
    pad = [max(0, round(v)) for v in pad]
    return {'d': d, 'g': gap, 'p': pad, 'pa': pa, 'ca': ca, 'fills': fills, 'ch': ch}

def fills_of(n):
    out = []
    for f in n.get('bg', []):
        if f[0] == 'S': out.append(hexc(f[1:]))
        elif f[0] == 'L': out.append(['L', f[1], f[2], f[3], f[4], [[hexc(s[:4]), s[4]] for s in f[5]]])
    return out

def emit(n, origin, parent_al=None, idx=None):
    k = n['k']
    b = rel(n['box'], origin)
    pr = {}
    if n.get('abs') and parent_al: pr['a'] = 1
    if parent_al and idx is not None and not n.get('abs'):
        al = parent_al
        if al['fills'][idx] and k in ('F', 'I') or (al['fills'][idx] and k == 'T' and n.get('ml')): pr['fc'] = 1
        if n.get('grow') and k == 'F' and al['pa'] != 'SB': pr['fm'] = 1
    if k == 'T':
        f = n['f']
        t = {'s': n['s'], 'z': f['sz'], 'w': f['wt'], 'c': hexc(f['c'])}
        if f.get('it'): t['i'] = 1
        if f.get('dec'): t['d'] = f['dec']
        if f.get('ls'): t['ls'] = f['ls']
        if n.get('lh'): t['lh'] = n['lh']
        if n['al'] != 'L': t['al'] = n['al']
        if n.get('ml'): t['ml'] = 1
        if n.get('fw'): t['fw'] = 1
        if n.get('nw'): t['nw'] = n['nw']
        if n.get('runs'):
            rr = []
            for s, e, dd in n['runs']:
                x = {}
                if 'c' in dd: x['c'] = hexc(dd['c'])
                if 'wt' in dd: x['w'] = dd['wt']
                if 'sz' in dd: x['z'] = dd['sz']
                if 'it' in dd: x['i'] = dd['it']
                if 'dec' in dd: x['d'] = dd['dec']
                if x: rr.append([s, e, x])
            if rr: t['r'] = rr
        pr['t'] = t
        return ['T', n['n'], *b, pr]
    if k == 'S':
        pr['v'] = n['svg']
        return ['S', n['n'], *b, pr]
    if k == 'I':
        pr['i'] = n['img']
        if n.get('bm'): pr['bm'] = n['bm']
        return ['I', n['n'], *b, pr]
    # frame
    fl = fills_of(n)
    if fl: pr['b'] = fl
    if 'st' in n:
        c, bw, sty = n['st']
        pr['s'] = [hexc(c), bw if len(set(bw)) > 1 else bw[0], sty]
    if 'r' in n: pr['r'] = n['r']
    if 'fx' in n: pr['e'] = [[s[0], s[1], s[2], s[3], s[4], hexc(s[5])] for s in n['fx']]
    if n.get('op'): pr['o'] = n['op']
    if n.get('clip') and not (n['ch'] and all(c['k'] == 'T' for c in n['ch'])): pr['c'] = 1
    if n.get('self') and n.get('selfbox'):
        pr['si'] = [n['self'], *rel(n['selfbox'], n['box'])]
    al = infer(n)
    kids = []
    if al:
        pr['l'] = [al['d'], al['g'], al['p'], al['pa'], al['ca']]
        inflow = al['ch']
        for c in n['ch']:
            i = inflow.index(c) if c in inflow else None
            kids.append(emit(c, n['box'], al, i))
    else:
        for c in n['ch']:
            kids.append(emit(c, n['box']))
    return ['F', n['n'], *b, pr, kids]

root = prep(T['root'])
root['box'] = [0, 0, W, H]
out = emit(root, [0, 0])
json.dump(out, open(os.path.join(D, 'c.json'), 'w'), separators=(',', ':'), ensure_ascii=False)
print(D, len(json.dumps(out, separators=(',', ':'), ensure_ascii=False)))
