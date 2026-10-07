// In-page serializer: returns {root, caps:[{id,mode}], svgs}
(() => {
  const VW = innerWidth, VH = innerHeight;
  const caps = []; let capN = 0;
  const R = v => Math.round(v * 100) / 100;
  const px = v => parseFloat(v) || 0;
  const parseColor = s => {
    const m = s && s.match(/rgba?\(([^)]+)\)/); if (!m) return null;
    const p = m[1].split(/[ ,/]+/).filter(Boolean).map(Number);
    const a = p.length > 3 ? p[3] : 1; if (a === 0) return null;
    return [Math.round(p[0]), Math.round(p[1]), Math.round(p[2]), R(a)];
  };
  const splitTop = s => { const out = []; let d = 0, cur = ''; for (const ch of s) { if (ch === '(') d++; if (ch === ')') d--; if (ch === ',' && !d) { out.push(cur.trim()); cur = ''; } else cur += ch; } if (cur.trim()) out.push(cur.trim()); return out; };
  function linear(s, w, h) {
    const m = s.match(/^linear-gradient\((.*)\)$/); if (!m) return null;
    const parts = splitTop(m[1]); let ang = 180;
    if (/deg$/.test(parts[0])) { ang = parseFloat(parts.shift()); }
    else if (/^to /.test(parts[0])) { const t = parts.shift(); const map = { 'to top': 0, 'to right': 90, 'to bottom': 180, 'to left': 270, 'to top right': null, 'to right top': null, 'to bottom right': null, 'to right bottom': null, 'to bottom left': null, 'to left bottom': null, 'to top left': null, 'to left top': null };
      if (map[t] != null) ang = map[t]; else { const dx = /right/.test(t) ? 1 : -1, dy = /top/.test(t) ? -1 : 1; ang = Math.atan2(dx * h, -dy * w) * 180 / Math.PI; /* approx corner */ ang = (Math.atan2(dx / w, -dy / h) * 180 / Math.PI); } }
    const stops = []; for (let i = 0; i < parts.length; i++) {
      const cm = parts[i].match(/^(rgba?\([^)]*\))\s*(.*)$/); if (!cm) return null;
      const c = parseColor(cm[1]) || [0, 0, 0, 0]; const pos = cm[2].trim().split(/\s+/).filter(Boolean);
      if (pos.length === 0) stops.push([c, null]); else for (const p of pos) stops.push([c, /%$/.test(p) ? parseFloat(p) / 100 : (/px$/.test(p) ? null : null)]);
    }
    if (stops.length < 2) return null;
    if (stops[0][1] == null) stops[0][1] = 0; if (stops[stops.length - 1][1] == null) stops[stops.length - 1][1] = 1;
    for (let i = 1; i < stops.length - 1; i++) if (stops[i][1] == null) { let j = i; while (stops[j][1] == null) j++; const a = stops[i - 1][1], b = stops[j][1]; for (let k = i; k < j; k++) stops[k][1] = a + (b - a) * (k - i + 1) / (j - i + 1); }
    const t = ang * Math.PI / 180, sx = Math.sin(t), sy = -Math.cos(t);
    const L = Math.abs(w * sx) + Math.abs(h * sy);
    const p0 = [(w / 2 - sx * L / 2) / w, (h / 2 - sy * L / 2) / h], p1 = [(w / 2 + sx * L / 2) / w, (h / 2 + sy * L / 2) / h];
    return ['L', R(p0[0] * 1000) / 1000, R(p0[1] * 1000) / 1000, R(p1[0] * 1000) / 1000, R(p1[1] * 1000) / 1000, stops.map(s => [s[0][0], s[0][1], s[0][2], s[0][3] == null ? 1 : s[0][3], R(s[1])])];
  }
  function shadows(s) {
    if (!s || s === 'none') return [];
    return splitTop(s).map(x => {
      const c = parseColor(x); const rest = x.replace(/rgba?\([^)]*\)/, '').trim();
      const ins = /inset/.test(rest); const n = rest.replace('inset', '').trim().split(/\s+/).map(px);
      if (!c) return null; return [ins ? 1 : 0, n[0] || 0, n[1] || 0, n[2] || 0, n[3] || 0, c];
    }).filter(Boolean);
  }
  const isId = tr => tr === 'none' || /^matrix\(1, 0, 0, 1,/.test(tr);
  function pseudoActive(el, which) { const cs = getComputedStyle(el, which); return cs.content && cs.content !== 'none' && cs.content !== 'normal' && cs.display !== 'none'; }
  function needTreeRaster(el, cs) {
    if (['IMG', 'CANVAS', 'VIDEO', 'PICTURE'].includes(el.tagName)) return true;
    if (cs.filter !== 'none' || cs.webkitMaskImage !== 'none' && cs.webkitMaskImage || cs.maskImage && cs.maskImage !== 'none' || cs.clipPath !== 'none' || cs.mixBlendMode !== 'normal') return true;
    if (!isId(cs.transform)) return true;
    return false;
  }
  function needSelfRaster(el, cs) {
    const bi = cs.backgroundImage;
    if (bi && bi !== 'none') { const layers = splitTop(bi); if (layers.length > 1 || !/^linear-gradient/.test(layers[0])) return true; if (!linear(layers[0], 100, 100)) return true; }
    if (pseudoActive(el, '::before') || pseudoActive(el, '::after')) return true;
    const bc = [cs.borderTopColor, cs.borderRightColor, cs.borderBottomColor, cs.borderLeftColor];
    const bw = [cs.borderTopWidth, cs.borderRightWidth, cs.borderBottomWidth, cs.borderLeftWidth].map(px);
    const used = bc.filter((c, i) => bw[i] > 0); if (new Set(used).size > 1) return true;
    const bs = [cs.borderTopStyle, cs.borderRightStyle, cs.borderBottomStyle, cs.borderLeftStyle].filter((s, i) => bw[i] > 0);
    if (bs.some(s => !['solid', 'dashed', 'dotted'].includes(s))) return true;
    return false;
  }
  function visuals(el, cs, w, h) {
    const v = {}; const bg = parseColor(cs.backgroundColor); const fills = [];
    if (bg) fills.push(['S', ...bg]);
    const bi = cs.backgroundImage; if (bi && bi !== 'none') { const g = linear(splitTop(bi)[0], w, h); if (g) fills.push(g); }
    if (fills.length) v.bg = fills;
    const bw = [cs.borderTopWidth, cs.borderRightWidth, cs.borderBottomWidth, cs.borderLeftWidth].map(px);
    if (bw.some(x => x > 0)) { const i = bw.findIndex(x => x > 0); const c = parseColor([cs.borderTopColor, cs.borderRightColor, cs.borderBottomColor, cs.borderLeftColor][i]); const sty = [cs.borderTopStyle, cs.borderRightStyle, cs.borderBottomStyle, cs.borderLeftStyle][i]; if (c) v.st = [c, bw, sty === 'solid' ? 0 : (sty === 'dashed' ? 1 : 2)]; }
    const rad = [cs.borderTopLeftRadius, cs.borderTopRightRadius, cs.borderBottomRightRadius, cs.borderBottomLeftRadius].map(x => { if (/%/.test(x)) return Math.min(w, h) * parseFloat(x) / 100; return px(x); }).map(x => R(Math.min(x, Math.min(w, h) / 2)));
    if (rad.some(x => x > 0)) v.r = rad.every(x => x === rad[0]) ? rad[0] : rad;
    const sh = shadows(cs.boxShadow); if (sh.length) v.fx = sh;
    return v;
  }
  const hasVis = v => v.bg || v.st || v.fx;
  function capture(el, mode) { const id = 'c' + (capN++); el.setAttribute('data-cap', id); caps.push({ id, mode }); return id; }
  // ---------- text helpers ----------
  const inlineTags = new Set(['SPAN', 'B', 'STRONG', 'EM', 'I', 'A', 'SMALL', 'U', 'S', 'SUB', 'SUP', 'MARK', 'LABEL', 'BR', 'CODE', 'ABBR', 'TIME']);
  function isInlineText(el) {
    if (el.nodeType !== 1) return false; if (el.tagName === 'BR') return true;
    const cs = getComputedStyle(el); if (cs.display !== 'inline' && cs.display !== 'contents') return false;
    if (cs.display === 'none') return true;
    const r = el.getBoundingClientRect(); const v = visuals(el, cs, r.width, r.height);
    if (hasVis(v) || px(cs.paddingLeft) + px(cs.paddingRight) + px(cs.paddingTop) > 0 || needSelfRaster(el, cs) || needTreeRaster(el, cs)) return false;
    for (const c of el.children) if (!isInlineText(c)) return false; return true;
  }
  function styleOf(cs) {
    const c = parseColor(cs.color) || [0, 0, 0, 1];
    return { sz: R(px(cs.fontSize)), wt: +cs.fontWeight || 400, it: cs.fontStyle === 'italic' ? 1 : 0, c, dec: /underline/.test(cs.textDecorationLine) ? 1 : (/line-through/.test(cs.textDecorationLine) ? 2 : 0), ls: cs.letterSpacing === 'normal' ? 0 : R(px(cs.letterSpacing)), tt: cs.textTransform };
  }
  function textGroup(nodes, container) {
    // nodes: list of text nodes / inline-text elements (consecutive siblings)
    let chars = ''; const runs = []; let lastSpace = true;
    const ccs = getComputedStyle(container); const pre = /pre/.test(ccs.whiteSpace);
    function walk(n) {
      if (n.nodeType === 3) {
        const pcs = getComputedStyle(n.parentElement); if (pcs.display === 'none' || pcs.visibility === 'hidden') return;
        let t = n.nodeValue; if (!pre) t = t.replace(/[\s\n\r\t]+/g, ' '); if (!pre && lastSpace) t = t.replace(/^ /, '');
        if (!t) return; const st = styleOf(pcs);
        if (st.tt === 'uppercase') t = t.toUpperCase(); else if (st.tt === 'lowercase') t = t.toLowerCase(); else if (st.tt === 'capitalize') t = t.replace(/\b\w/g, m => m.toUpperCase());
        runs.push([chars.length, chars.length + t.length, st]); chars += t; lastSpace = / $/.test(t);
      } else if (n.nodeType === 1) {
        if (n.tagName === 'BR') { chars = chars.replace(/ $/, ''); chars += '\n'; lastSpace = true; return; }
        if (getComputedStyle(n).display === 'none') return; for (const c of n.childNodes) walk(c);
      }
    }
    nodes.forEach(walk);
    // trim trailing space
    while (chars.endsWith(' ')) { chars = chars.slice(0, -1); const r = runs[runs.length - 1]; if (r) r[1] = Math.min(r[1], chars.length); }
    if (!chars.trim()) return null;
    const range = document.createRange(); range.setStartBefore(nodes[0]); range.setEndAfter(nodes[nodes.length - 1]);
    const rects = [...range.getClientRects()].filter(r => r.width > 0 && r.height > 0);
    if (!rects.length) return null;
    let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity; const tops = new Set();
    for (const r of rects) { x0 = Math.min(x0, r.left); y0 = Math.min(y0, r.top); x1 = Math.max(x1, r.right); y1 = Math.max(y1, r.bottom); tops.add(Math.round(r.top / 4)); }
    // base style = longest run
    const cnt = {}; for (const r of runs) { const k = JSON.stringify(r[2]); cnt[k] = (cnt[k] || 0) + (r[1] - r[0]); }
    const baseK = Object.keys(cnt).sort((a, b) => cnt[b] - cnt[a])[0]; const base = JSON.parse(baseK);
    const lhRaw = ccs.lineHeight; const lh = lhRaw === 'normal' ? R(rects[0].height) : R(px(lhRaw));
    const ml = tops.size > 1 || chars.includes('\n');
    const lineH = lh || R(base.sz * 1.27);
    const firstH = rects[0].height; const yAdj = (lineH - firstH) / 2;
    const al = ccs.textAlign === 'center' ? 'C' : (ccs.textAlign === 'right' || ccs.textAlign === 'end' ? 'R' : (ccs.textAlign === 'justify' ? 'J' : 'L'));
    const nLines = ml ? Math.max(tops.size, chars.split('\n').length) : 1;
    let bx = x0, bw = x1 - x0;
    if (ml) { const cr = container.getBoundingClientRect(); bx = cr.left + px(ccs.paddingLeft) + px(ccs.borderLeftWidth); bw = cr.width - px(ccs.paddingLeft) - px(ccs.paddingRight) - px(ccs.borderLeftWidth) - px(ccs.borderRightWidth); if (bw < x1 - x0) { bx = x0; bw = x1 - x0; } }
    const T = { k: 'T', s: chars, f: base, lh, al, ml: ml ? 1 : 0, box: [bx, y0 - yAdj, bw, ml ? (y1 - y0) + 2 * yAdj : lineH] };
    const extra = runs.filter(r => JSON.stringify(r[2]) !== baseK).map(r => { const d = {}; for (const k in r[2]) if (JSON.stringify(r[2][k]) !== JSON.stringify(base[k])) d[k] = r[2][k]; return [r[0], r[1], d]; }).filter(r => r[1] > r[0]);
    if (extra.length) T.runs = extra;
    T.n = chars.slice(0, 40).replace(/\n/g, ' ');
    T.nw = nwOf(chars, base, T.runs);
    return T;
  }
  const __cv = document.createElement('canvas').getContext('2d');
  function nwOf(chars, base, runs) {
    const st = new Array(chars.length).fill(base);
    for (const [a, b, d] of (runs || [])) for (let i = a; i < b; i++) st[i] = Object.assign({}, base, d);
    let best = 0, cur = 0, i = 0;
    while (i < chars.length) {
      if (chars[i] === '\n') { best = Math.max(best, cur); cur = 0; i++; continue; }
      let j = i; while (j < chars.length && chars[j] !== '\n' && st[j] === st[i]) j++;
      const f = st[i]; __cv.font = `${f.it ? 'italic ' : ''}${f.wt} ${f.sz}px "Google Sans"`;
      cur += __cv.measureText(chars.slice(i, j)).width + (f.ls || 0) * (j - i); i = j;
    }
    return R(Math.max(best, cur));
  }
  function svgSer(el, cs) {
    if (el.querySelector('foreignObject,text,filter,image,mask,pattern,animate,animateTransform')) return null;
    const c = el.cloneNode(true); const src = [el, ...el.querySelectorAll('*')]; const dst = [c, ...c.querySelectorAll('*')];
    const shapes = new Set(['path', 'circle', 'rect', 'line', 'polyline', 'polygon', 'ellipse', 'g', 'svg']);
    for (let i = 0; i < src.length; i++) {
      const s = src[i], d = dst[i]; const tag = s.tagName.toLowerCase(); const st = getComputedStyle(s);
      if (st.display === 'none') { d.remove(); continue; }
      if (shapes.has(tag)) {
        if (st.strokeDasharray && st.strokeDasharray !== 'none' && st.strokeDashoffset && px(st.strokeDashoffset) !== 0) return null;
        const ps = (tag === 'svg') ? null : getComputedStyle(s.parentElement);
        const props = [['fill', 'fill'], ['stroke', 'stroke'], ['stroke-width', 'strokeWidth'], ['stroke-linecap', 'strokeLinecap'], ['stroke-linejoin', 'strokeLinejoin'], ['stroke-dasharray', 'strokeDasharray'], ['fill-opacity', 'fillOpacity'], ['stroke-opacity', 'strokeOpacity']];
        for (const [a, k] of props) d.removeAttribute(a);
        for (const [a, k] of props) { let v = st[k]; if (a === 'fill' && v.startsWith('url')) { v = s.getAttribute('fill') || 'none'; } if (a === 'stroke-width') v = v.replace('px', '');
          const pv = ps ? (k === 'strokeWidth' ? ps[k].replace('px', '') : ps[k]) : ({ fill: 'rgb(0, 0, 0)', stroke: 'none', 'stroke-width': '1', 'stroke-linecap': 'butt', 'stroke-linejoin': 'miter', 'stroke-dasharray': 'none', 'fill-opacity': '1', 'stroke-opacity': '1' })[a];
          if (a === 'stroke-dasharray' && s.getAttribute('pathLength')) { const pl = +s.getAttribute('pathLength'); const da = (st.strokeDasharray || 'none').split(/[ ,]+/).map(parseFloat); if (st.strokeDasharray === 'none' || da[0] >= pl - 0.01) continue; return null; }
          if (v !== pv) d.setAttribute(a, v); }
        if (+st.opacity !== 1) d.setAttribute('opacity', st.opacity);
      }
      d.removeAttribute('class'); d.removeAttribute('style'); for (const a of [...d.attributes]) if (/^(data-|aria-|role|focusable)/.test(a.name)) d.removeAttribute(a.name);
    }
    const r = el.getBoundingClientRect(); c.setAttribute('width', R(r.width)); c.setAttribute('height', R(r.height)); c.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
    if (!c.getAttribute('viewBox')) c.setAttribute('viewBox', `0 0 ${R(r.width)} ${R(r.height)}`);
    let s = c.outerHTML.replace(/currentColor/g, cs.color).replace(/\s+/g, ' ').replace(/> </g, '><');
    s = s.replace(/(\d+\.\d{2})\d+/g, '$1').replace(/rgb\((\d+), (\d+), (\d+)\)/g, (m, a, b, c) => '#' + [a, b, c].map(x => (+x).toString(16).padStart(2, '0')).join(''));
    if (s.length > 2500) return null;
    return s;
  }
  function nameOf(el) { const cl = (el.getAttribute('class') || '').split(/\s+/).filter(c => c && !/^(ob-in\d?|cp-pop|sc-|fx-in)/.test(c)); return cl[0] || el.tagName.toLowerCase(); }
  // ---------- main ----------
  function visit(el, pr) {
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity === 0) return null;
    if (cs.display === 'contents') { return { k: 'C', ch: kids(el, pr) }; }
    const r = el.getBoundingClientRect();
    if (r.width <= 1.01 && r.height <= 1.01 && cs.overflow === 'hidden') return null;
    if (r.right < 0 || r.bottom < 0 || r.left > VW || r.top > VH) return null;
    if (cs.clip && cs.clip !== 'auto' && /rect\(0/.test(cs.clip)) return null;
    const abs = cs.position === 'absolute' || cs.position === 'fixed';
    const tag = el.tagName;
    const zz = (cs.position !== 'static' && cs.zIndex !== 'auto') ? +cs.zIndex : 0; const oo = +cs.order || 0;
    if ((el instanceof SVGSVGElement) && needTreeRaster(el, cs)) return { k: 'I', n: nameOf(el), img: capture(el, 'tree'), box: [r.left, r.top, r.width, r.height], abs, bm: cs.mixBlendMode !== 'normal' ? cs.mixBlendMode : 0, z: zz, o2: oo };
    if (tag === 'svg' || tag === 'SVG' || el instanceof SVGSVGElement) {
      const s = svgSer(el, cs); if (s) return { k: 'S', n: nameOf(el) === 'svg' ? 'icon' : nameOf(el), box: [r.left, r.top, r.width, r.height], svg: s, abs, z: zz, o2: oo };
      return { k: 'I', n: 'graphic', img: capture(el, 'tree'), box: [r.left, r.top, r.width, r.height], abs, z: zz, o2: oo };
    }
    if (needTreeRaster(el, cs)) return { z: zz, o2: oo, k: 'I', n: tag === 'IMG' ? (el.getAttribute('alt') || nameOf(el)) : nameOf(el), img: capture(el, 'tree'), box: [r.left, r.top, r.width, r.height], abs, bm: cs.mixBlendMode !== 'normal' ? cs.mixBlendMode : (el.parentElement && getComputedStyle(el.parentElement).mixBlendMode !== 'normal' ? getComputedStyle(el.parentElement).mixBlendMode : 0) };
    const N = { k: 'F', n: nameOf(el), box: [r.left, r.top, r.width, r.height], abs, z: zz, o2: oo };
    if (needSelfRaster(el, cs)) { N.self = capture(el, 'self'); const v = visuals(el, cs, r.width, r.height); if (v.r) N.r = v.r; }
    else Object.assign(N, visuals(el, cs, r.width, r.height));
    if (+cs.opacity < 1) N.op = R(+cs.opacity);
    if (cs.overflow !== 'visible' || cs.overflowX !== 'visible') N.clip = 1;
    N.css = { disp: cs.display, dir: cs.flexDirection, jc: cs.justifyContent, ai: cs.alignItems, wrap: cs.flexWrap, pad: [cs.paddingTop, cs.paddingRight, cs.paddingBottom, cs.paddingLeft].map(px), bw: [cs.borderTopWidth, cs.borderRightWidth, cs.borderBottomWidth, cs.borderLeftWidth].map(px) };
    N.grow = +cs.flexGrow > 0 ? 1 : 0;
    N.ch = tag === 'SELECT' ? [] : kids(el, r);
    // form controls: placeholder / value text
    if ((tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') && !N.ch.length) {
      const val = tag === 'SELECT' ? ((el.options[el.selectedIndex] || {}).text || '') : (el.value || el.getAttribute('placeholder') || ''); if (val && el.type !== 'checkbox' && el.type !== 'radio') {
        const pcs = getComputedStyle(el, el.value ? null : '::placeholder'); const st = styleOf(el.value ? cs : pcs);
        const cx = r.left + px(cs.paddingLeft) + px(cs.borderLeftWidth); const ch = r.height; const cw = r.width - px(cs.paddingLeft) - px(cs.paddingRight) - px(cs.borderLeftWidth) - px(cs.borderRightWidth);
        if (tag === 'TEXTAREA') { const lh = cs.lineHeight === 'normal' ? R(st.sz * 1.27) : R(px(cs.lineHeight)); const top = r.top + px(cs.paddingTop) + px(cs.borderTopWidth);
          N.ch.push({ k: 'T', s: val, f: st, lh, al: 'L', ml: 1, box: [cx, top, cw, r.height - px(cs.paddingTop) - px(cs.paddingBottom) - px(cs.borderTopWidth) - px(cs.borderBottomWidth)], n: val.slice(0, 40), nw: nwOf(val, st) }); }
        else { const lh = R(st.sz * 1.27);
          N.ch.push({ k: 'T', s: val, f: st, lh, al: 'L', ml: 0, box: [cx, r.top + (ch - lh) / 2, cw, lh], n: val.slice(0, 40), nw: nwOf(val, st) }); }
      }
    }
    return N;
  }
  function kids(el, pr) {
    const out = []; let group = [];
    const flush = () => { if (group.length) { const t = textGroup(group, el); if (t) out.push(t); group = []; } };
    for (const n of el.childNodes) {
      if (n.nodeType === 3) { if (n.nodeValue.trim() || group.length) group.push(n); continue; }
      if (n.nodeType !== 1) continue;
      if (['SCRIPT', 'STYLE', 'TEMPLATE', 'LINK', 'META'].includes(n.tagName)) continue;
      if (inlineTags.has(n.tagName) && isInlineText(n)) { group.push(n); continue; }
      flush(); const c = visit(n, pr); if (c) { if (c.k === 'C') out.push(...c.ch); else out.push(c); }
    }
    flush();
    const ecs = getComputedStyle(el); const flex = /flex|grid/.test(ecs.display);
    out.forEach((c, i) => c._i = i);
    out.sort((a, b) => ((a.z || 0) - (b.z || 0)) || (flex ? ((a.o2 || 0) - (b.o2 || 0)) : 0) || (a._i - b._i));
    // text nodes inside flex/grid containers that are positioned absolutely? fine
    return out;
  }
  const body = document.body; const bcs = getComputedStyle(body);
  const root = { k: 'F', n: 'root', box: [0, 0, VW, VH], bg: [['S', ...(parseColor(bcs.backgroundColor) || parseColor(getComputedStyle(document.documentElement).backgroundColor) || [1, 1, 1, 1])]], clip: 1, ch: kids(body, null), css: { disp: 'block', pad: [0, 0, 0, 0], bw: [0, 0, 0, 0] } };
  return { root, caps };
})()
