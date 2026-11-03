auroraMount(el) {
    var host = window;
    try { if (window.top && window.top.document) host = window.top; } catch (e) { host = window; }
    var R = host.__credAurora;
    if (!R) {
      R = host.__credAurora = { items: [], raf: 0, last: 0, cur: 0 };
      var gc = host.document.createElement('canvas');
      var gl = gc.getContext('webgl', { premultipliedAlpha: false, antialias: false, preserveDrawingBuffer: true, powerPreference: 'low-power' });
      R.gl = gl; R.gc = gc;
      if (gl) {
        var vs = 'attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';
        var fs = [
          'precision mediump float;uniform vec2 R;uniform float T;uniform float L;uniform vec3 A;uniform vec3 B;uniform vec3 C;uniform vec3 G0;uniform vec3 G1;',
          'float hp(float s,float k,float b){return fract(sin(s*k)*b)*6.2831853;}',
          'float h3(vec3 p){return fract(sin(dot(p,vec3(127.1,311.7,74.7)))*43758.5453);}',
          'float vn(vec3 p){vec3 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);',
          'float a=mix(mix(h3(i),h3(i+vec3(1,0,0)),f.x),mix(h3(i+vec3(0,1,0)),h3(i+vec3(1,1,0)),f.x),f.y);',
          'float b=mix(mix(h3(i+vec3(0,0,1)),h3(i+vec3(1,0,1)),f.x),mix(h3(i+vec3(0,1,1)),h3(i+vec3(1,1,1)),f.x),f.y);',
          'return mix(a,b,f.z)*2.-1.;}',
          'void main(){vec2 uv=gl_FragCoord.xy/R;float asp=R.x/max(R.y,1.);',
          'float wav=.6,ray=.25,H=1.1,ins=1.12,bal=mix(2.5,.4,.5),cx=.62,cy=.18;',
          'float ws=0.,tot=0.;',
          'for(int i=0;i<4;i++){float fi=float(i);',
          'float to=fi==0.?0.:fi==1.?3.1:fi==2.?6.7:9.4;float w=fi==0.?1.:fi==1.?.65:fi==2.?.45:.3;',
          'float ts=T*.06+to;float ls=fi*31.7;float wx=(uv.x-cx)*asp*2.;',
          'float arc=.15*sin(wx*.7+ts*.4+hp(ls,12.9,4758.5))+.08*sin(wx*1.6+ts*.65+hp(ls,78.2,2847.1))+.04*sin(wx*2.9+ts*.3+hp(ls,41.6,1593.7));',
          'float nw=vn(vec3(wx*.5,ts*.25,ls*.1));float py=cy+arc*wav+nw*.14*wav;',
          'float rays=pow(sin((wx+nw*2.5)*mix(6.,20.,ray)*.15+ts*.1+hp(ls,53.7,3847.2))*.5+.5,1.5);',
          'float lh=H*mix(.4,1.,rays);float d=uv.y-py;float top=lh*(rays*.4+.6);',
          'float env=smoothstep(-.04,.015,d)*(1.-smoothstep(0.,top,d));',
          'float ct=clamp(d/(top+.001),0.,1.);float sb=mix(.4,1.,nw*.5+.5);float cd=ct-.2;float cb=exp(cd*cd*-6.)*.3+1.;',
          'float al=env*rays*sb*cb*w;ws+=ct*al;tot+=al;}',
          'float av=pow(ws/(tot+.001),bal);vec3 col=mix(mix(A,B,smoothstep(0.,.2,av)),C,smoothstep(.4,.85,av));',
          'float br=tot*ins;vec3 glow=clamp(col*br,0.,1.);',
          'vec3 base=mix(G0,G1,smoothstep(0.,1.,uv.y*.7+(1.-uv.x)*.3));',
          'gl_FragColor=L>.5?vec4(mix(base,col,clamp(br*.42,0.,.62)),1.):vec4(base*(1.-clamp(br*.5,0.,1.)*.35)+glow,1.);}'
        ].join('');
        var mk = function (t, s) { var o = gl.createShader(t); gl.shaderSource(o, s); gl.compileShader(o); return o; };
        var pr = gl.createProgram();
        gl.attachShader(pr, mk(gl.VERTEX_SHADER, vs)); gl.attachShader(pr, mk(gl.FRAGMENT_SHADER, fs)); gl.linkProgram(pr);
        if (!gl.getProgramParameter(pr, gl.LINK_STATUS)) { R.gl = null; } else {
          gl.useProgram(pr);
          var bf = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, bf);
          gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 1, -1, -1, 1, 1, 1]), gl.STATIC_DRAW);
          var lp = gl.getAttribLocation(pr, 'p'); gl.enableVertexAttribArray(lp); gl.vertexAttribPointer(lp, 2, gl.FLOAT, false, 0, 0);
          var u = function (n) { return gl.getUniformLocation(pr, n); };
          var hex = function (h) { return [parseInt(h.substr(1, 2), 16) / 255, parseInt(h.substr(3, 2), 16) / 255, parseInt(h.substr(5, 2), 16) / 255]; };
          R.pal = { dark: [hex('#0E3BB8'), hex('#2E63FF'), hex('#9DB8F7'), hex('#050A20'), hex('#0B1A4D'), 0], light: [hex('#B9CCFF'), hex('#7FA4FF'), hex('#4F80FF'), hex('#F6F9FF'), hex('#E4ECFF'), 1] };
          R.u = { A: u('A'), B: u('B'), C: u('C'), G0: u('G0'), G1: u('G1'), L: u('L') };
          R.uR = u('R'); R.uT = u('T');
        }
      }
      R.still = !!(host.matchMedia && host.matchMedia('(prefers-reduced-motion: reduce)').matches);
      R.t0 = host.performance.now();
      R.paint = function (it, now) {
        var g = R.gl, w = it.cv.width, h = it.cv.height;
        if (R.gc.width !== w || R.gc.height !== h) { R.gc.width = w; R.gc.height = h; }
        var pl = R.pal[it.light ? 'light' : 'dark']; g.uniform3fv(R.u.A, pl[0]); g.uniform3fv(R.u.B, pl[1]); g.uniform3fv(R.u.C, pl[2]); g.uniform3fv(R.u.G0, pl[3]); g.uniform3fv(R.u.G1, pl[4]); g.uniform1f(R.u.L, pl[5]);
        g.viewport(0, 0, w, h); g.uniform2f(R.uR, w, h); g.uniform1f(R.uT, it.seed + (R.still ? 0 : (now - R.t0) / 1000));
        g.drawArrays(g.TRIANGLE_STRIP, 0, 4);
        it.ctx.drawImage(R.gc, 0, 0);
      };
      R.size = function (it) {
        var cw = it.el.clientWidth, ch = it.el.clientHeight;
        if (!cw || !ch) return false;
        var s = Math.min(0.4, 320 / cw), w = Math.max(16, Math.round(cw * s)), h = Math.max(16, Math.round(ch * s));
        if (it.cv.width !== w || it.cv.height !== h) { it.cv.width = w; it.cv.height = h; it.fresh = true; }
        return true;
      };
      R.tick = function (now) {
        R.raf = 0;
        if (now - R.last > 33) {
          R.last = now;
          R.items = R.items.filter(function (it) { return it.el.isConnected; });
          var n = R.items.length, st = host.performance.now();
          for (var k = 0; k < n; k++) {
            var it = R.items[(R.cur + k) % n];
            if ((it.vis || it.fresh) && R.size(it)) { R.paint(it, now); it.fresh = false; }
            if (host.performance.now() - st > 6) { R.cur = (R.cur + k + 1) % n; break; }
          }
        }
        if (!R.still && R.items.some(function (it) { return it.vis; })) R.raf = host.requestAnimationFrame(R.tick);
      };
      R.wake = function () { if (!R.raf) R.raf = host.requestAnimationFrame(R.tick); };
    }
    if (!R.gl) { el.classList.add(el.classList.contains('aur-lt') ? 'aur-off-lt' : 'aur-off'); return function () {}; }
    var cv = el.ownerDocument.createElement('canvas');
    cv.className = 'aur-c';
    cv.setAttribute('aria-hidden', 'true');
    el.insertBefore(cv, el.firstChild);
    el.__aurC = cv;
    var it = { el: el, cv: cv, ctx: cv.getContext('2d'), seed: Math.random() * 40, vis: true, fresh: true, light: el.classList.contains('aur-lt') };
    R.items.push(it);
    var view = el.ownerDocument.defaultView || window;
    var io = view.IntersectionObserver ? new view.IntersectionObserver(function (e) { it.vis = e[0].isIntersecting; if (it.vis) R.wake(); }) : null;
    if (io) io.observe(el);
    R.wake();
    return function () { if (io) io.disconnect(); R.items = R.items.filter(function (x) { return x !== it; }); };
  }
