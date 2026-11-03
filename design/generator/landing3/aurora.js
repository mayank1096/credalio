auroraMount(el) {
    var cv = document.createElement('canvas');
    cv.className = 'aur-c';
    cv.setAttribute('aria-hidden', 'true');
    el.insertBefore(cv, el.firstChild);
    el.__aurC = cv;
    var gl = cv.getContext('webgl', { premultipliedAlpha: false, antialias: false });
    if (!gl) { el.classList.add('aur-off'); return function () {}; }
    var vs = 'attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';
    var fs = [
      'precision highp float;uniform vec2 R;uniform float T;uniform vec3 A;uniform vec3 B;uniform vec3 C;uniform vec3 G0;uniform vec3 G1;',
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
      'gl_FragColor=vec4(base*(1.-clamp(br*.5,0.,1.)*.35)+glow,1.);}'
    ].join('');
    var mk = function (t, s) { var o = gl.createShader(t); gl.shaderSource(o, s); gl.compileShader(o); return o; };
    var pr = gl.createProgram();
    gl.attachShader(pr, mk(gl.VERTEX_SHADER, vs)); gl.attachShader(pr, mk(gl.FRAGMENT_SHADER, fs)); gl.linkProgram(pr);
    if (!gl.getProgramParameter(pr, gl.LINK_STATUS)) { el.classList.add('aur-off'); return function () {}; }
    gl.useProgram(pr);
    var bf = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, bf);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 1, -1, -1, 1, 1, 1]), gl.STATIC_DRAW);
    var lp = gl.getAttribLocation(pr, 'p'); gl.enableVertexAttribArray(lp); gl.vertexAttribPointer(lp, 2, gl.FLOAT, false, 0, 0);
    var u = function (n) { return gl.getUniformLocation(pr, n); };
    var hex = function (h) { return [parseInt(h.substr(1, 2), 16) / 255, parseInt(h.substr(3, 2), 16) / 255, parseInt(h.substr(5, 2), 16) / 255]; };
    gl.uniform3fv(u('A'), hex('#0E3BB8')); gl.uniform3fv(u('B'), hex('#2E63FF')); gl.uniform3fv(u('C'), hex('#9DB8F7'));
    gl.uniform3fv(u('G0'), hex('#050A20')); gl.uniform3fv(u('G1'), hex('#0B1A4D'));
    var uR = u('R'), uT = u('T'), raf = 0, on = true, t0 = performance.now(), seed = Math.random() * 40;
    var still = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var draw = function () {
      var r = Math.min(window.devicePixelRatio || 1, 1.5), w = Math.max(1, Math.round(el.clientWidth * r)), h = Math.max(1, Math.round(el.clientHeight * r));
      if (cv.width !== w || cv.height !== h) { cv.width = w; cv.height = h; gl.viewport(0, 0, w, h); }
      gl.uniform2f(uR, w, h); gl.uniform1f(uT, seed + (still ? 0 : (performance.now() - t0) / 1000));
      gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
    };
    var loop = function () { draw(); if (on && !still) raf = requestAnimationFrame(loop); };
    var io = window.IntersectionObserver ? new IntersectionObserver(function (e) {
      var vis = e[0].isIntersecting; if (vis && !on) { on = true; loop(); } else if (!vis) { on = false; cancelAnimationFrame(raf); }
    }) : null;
    if (io) io.observe(el);
    loop();
    return function () { on = false; cancelAnimationFrame(raf); if (io) io.disconnect(); };
  }
