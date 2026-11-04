# Wow moments (designer pick, 2026-11-04). Shared snippets, one per moment, built on existing pieces:
#   1 certificate assembles  -> Certifications paper (ct-paper) + Credalio seal, on the Dashboard certification card
#   2 gold jar               -> checkout top-up (3D DLP coin, gold palette)
#   3 holographic record     -> Validation Record gold seal (cd-val)
#   4 TruVault lock          -> Backpack dialog (dl-*)
#   5 Nova -> tutor baton    -> Ask Tutor summary (sc-sum)
# Replays: elements carry data-wow; the page re-arms data-go when they scroll back into view (WOW_JS).
SEAL = '<path d="M56.5 9.0 Q64.2 6.3 68.8 13.0 Q77.0 12.8 79.3 20.7 Q87.2 23.0 87.0 31.2 Q93.7 35.8 91.0 43.5 Q96.0 50.0 91.0 56.5 Q93.7 64.2 87.0 68.8 Q87.2 77.0 79.3 79.3 Q77.0 87.2 68.8 87.0 Q64.2 93.7 56.5 91.0 Q50.0 96.0 43.5 91.0 Q35.8 93.7 31.2 87.0 Q23.0 87.2 20.7 79.3 Q12.8 77.0 13.0 68.8 Q6.3 64.2 9.0 56.5 Q4.0 50.0 9.0 43.5 Q6.3 35.8 13.0 31.2 Q12.8 23.0 20.7 20.7 Q23.0 12.8 31.2 13.0 Q35.8 6.3 43.5 9.0 Q50.0 4.0 56.5 9.0Z"'

# re-arm data-go on [data-wow] elements each time they come into view (works inside canvas artboards that stay mounted)
WOW_JS = r'''
  wowScan() {
    if (typeof IntersectionObserver !== 'function') return;
    var self = this;
    if (!this._wowIO) this._wowIO = new IntersectionObserver(function (es) { es.forEach(function (e) {
      var el = e.target;
      if (e.intersectionRatio >= 0.45 && !el.__seen) { el.__seen = true; el.removeAttribute('data-go'); void el.offsetWidth; el.setAttribute('data-go', '1'); }
      else if (e.intersectionRatio < 0.05) el.__seen = false;
    }); }, { threshold: [0, 0.05, 0.45] });
    var look = function () { var l = document.querySelectorAll('[data-wow]'); for (var i = 0; i < l.length; i++) if (!l[i].__wowObs) { l[i].__wowObs = true; self._wowIO.observe(l[i]); } };
    look(); if (!this._wowMo && typeof MutationObserver === 'function') { this._wowMo = new MutationObserver(look); this._wowMo.observe(document.body, { childList: true, subtree: true }); }
  }
  wowStop() { if (this._wowIO) this._wowIO.disconnect(); if (this._wowMo) this._wowMo.disconnect(); }
'''

# ---------- 1 · certificate assembles (Dashboard G) ----------
def cert_paper():
    def piece(cls, text, var):
        return '<span class="cpz %s"><span class="cpz-g" aria-hidden="true">%s</span><span class="cpz-s" style="--p: {{%s}}">%s</span></span>' % (cls, text, var, text)
    return ('<div class="cpw" data-wow="1" data-go="1">'
            '<div class="ct-paper cpp {{cpCls}}" role="img" aria-label="Your certificate, {{cpPct}}">'
            + piece('cpz-l', 'PROFESSIONAL CERTIFICATE', 'cp0') + piece('cpz-n', 'Data Analysis', 'cp1') + piece('cpz-i', 'Ada Ononuju · Northgate University', 'cp2') +
            '<span class="cps" aria-hidden="true"><span class="cps-g"></span><svg class="cps-s" viewBox="0 0 100 100">' + SEAL + ' fill="#1652F0"></path><path d="M33 51l11 11 23-24" fill="none" stroke="#FFFFFF" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"></path></svg><span class="cps-r"></span></span>'
            '</div>'
            '<div class="cpf"><span>{{cpPct}}</span><button type="button" class="ds-link cpb" onClick="{{cpPlay}}">{{cpPlayT}}</button></div>'
            '</div>')

CERT_CSS = r'''.cpw{flex-shrink:0;width:300px;display:flex;flex-direction:column;gap:10px}
.cpp{margin:0;height:156px;box-shadow:0 18px 40px -26px rgba(11,20,51,.35)}
.ct-paper{position:relative;border-radius:12px;background:linear-gradient(180deg,#FFFFFF,#F5F8FF);border:1px solid #E3E8F3;padding:20px 22px;box-sizing:border-box;display:flex;flex-direction:column;gap:6px;overflow:hidden}
.ct-paper::before{content:"";position:absolute;inset:7px;border:1px solid #DCE5FB;border-radius:7px;pointer-events:none}
.cpz{position:relative;display:block;width:max-content;max-width:100%}
.cpz-g{color:#E3E8F3}
.cpz-s{position:absolute;left:0;top:0;white-space:nowrap;clip-path:inset(0 calc(100% - var(--p)) 0 0);transition:clip-path 1s cubic-bezier(.3,.8,.3,1)}
.cpz-l{font-size:9.5px;font-weight:600;letter-spacing:1.8px}
.cpz-l .cpz-s{color:#8A93AD}
.cpz-n{font-size:21px;font-weight:600;letter-spacing:-.4px;line-height:1.15}
.cpz-n .cpz-s{color:#0B1433}
.cpz-i{margin-top:auto;font-size:12px}
.cpz-i .cpz-s{color:#5B6582}
.cpz-g,.cpz-s{white-space:nowrap}
.cpw[data-go] .cpz-s{animation:cpInk 1.1s cubic-bezier(.3,.8,.3,1) both}
.cpw[data-go] .cpz-n .cpz-s{animation-delay:.35s}
.cpw[data-go] .cpz-i .cpz-s{animation-delay:.7s}
@keyframes cpInk{from{clip-path:inset(0 100% 0 0)}}
.cps{position:absolute;right:16px;bottom:14px;width:52px;height:52px}
.cps-g{position:absolute;inset:2px;border-radius:50%;border:1.5px dashed #CBD3E6}
.cps-s{position:absolute;inset:0;width:100%;height:100%;opacity:0;transform:scale(1.8) rotate(-18deg);filter:drop-shadow(0 8px 12px rgba(22,82,240,.3))}
.cps-r{position:absolute;inset:-6px;border-radius:50%;border:2px solid #1652F0;opacity:0}
.cpp.full .cps-s{animation:cpStamp .55s cubic-bezier(.2,1.4,.4,1) 1.15s forwards}
.cpp.full .cps-r{animation:cpRing .7s ease-out 1.45s}
.cpp.full .cps-g{opacity:0;transition:opacity .2s 1.15s}
.cpp.full{animation:cpThud .35s ease 1.4s}
@keyframes cpStamp{0%{opacity:0;transform:scale(1.8) rotate(-18deg)}60%{opacity:1;transform:scale(.92) rotate(3deg)}100%{opacity:1;transform:scale(1) rotate(0)}}
@keyframes cpRing{from{opacity:.7;transform:scale(.8)}to{opacity:0;transform:scale(1.5)}}
@keyframes cpThud{40%{transform:translateY(2px) scale(.995)}}
.cpf{display:flex;align-items:center;justify-content:space-between;gap:12px;font-size:13px;font-weight:500;color:#3A4566}
.cpb{font-size:13.5px}
@media (prefers-reduced-motion: reduce){.cpw[data-go] .cpz-s,.cpp.full,.cpp.full .cps-s,.cpp.full .cps-r{animation:none}.cpp.full .cps-s{opacity:1;transform:none}}
@media (max-width: 960px){.cpw{width:100%}}
@media (max-width: 760px){.cpp{height:124px;padding:16px 18px}.cpz-n{font-size:18px}.cps{width:42px;height:42px}}
'''

# ---------- 2 · gold jar (checkout top-up for a course) ----------
JAR = ('<div class="jr" data-wow="1" data-go="1" role="img" aria-label="{{jrAria}}">'
       '<div class="jr-need {{jrOk}}" style="left: {{jrNeedL}}"><span class="jr-nl"><span class="jr-ck">' + '<svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg>' + '</span>{{jrNeedT}}</span></div>'
       '<div class="jr-tube"><span class="jr-base" style="width: {{jrBase}}"></span><span class="jr-add {{jrPour}}" style="left: {{jrBase}}; width: {{jrAdd}}"><i class="jr-wave"></i></span><span class="jr-glass"></span>'
       '<span class="jr-drops {{jrPour}}" style="left: calc({{jrEnd}} - 14px)" aria-hidden="true"><span class="dlp-c"></span><span class="dlp-c"></span><span class="dlp-c"></span></span>'
       '<sc-if value="{{jrSpill}}" hint-placeholder-val="{{ false }}"><span class="jr-spill {{jrPour}}" aria-hidden="true"><span class="dlp-c"></span><span class="dlp-c"></span><span class="dlp-c"></span><span class="dlp-c"></span></span></sc-if></div>'
       '<div class="jr-ax"><span>Now <b>{{jrNow}}</b></span><span>After top-up <b>{{jrAfter}} DLP</b></span></div>'
       '</div>')
JAR_CSS = r'''.jr{position:relative;margin:22px 0 4px;padding-top:30px}
.jr-tube{position:relative;height:44px;border-radius:999px;background:linear-gradient(180deg,#FBFCFF,#F1F4FB);box-shadow:inset 0 2px 6px rgba(11,20,51,.08),inset 0 0 0 1.5px #E3E8F3}
.jr-base,.jr-add{position:absolute;top:4px;bottom:4px;transition:width .9s cubic-bezier(.3,.8,.3,1),left .9s cubic-bezier(.3,.8,.3,1)}
.jr-base{left:4px;border-radius:999px 0 0 999px;background:linear-gradient(180deg,#E9C46A,#C8961E);box-shadow:inset 0 -3px 0 rgba(120,80,10,.18)}
.jr-add{border-radius:0 999px 999px 0;overflow:hidden;background:linear-gradient(180deg,#FFF1CF,#F4D98E 55%,#E9C46A);box-shadow:inset 0 -3px 0 rgba(120,80,10,.12)}
.jr-wave{position:absolute;inset:0;background:linear-gradient(100deg,transparent 30%,rgba(255,255,255,.75) 46%,transparent 62%);background-size:220% 100%;animation:jrShine 2.6s linear infinite}
@keyframes jrShine{from{background-position:120% 0}to{background-position:-120% 0}}
.jr-glass{position:absolute;left:14px;right:14px;top:7px;height:7px;border-radius:999px;background:linear-gradient(90deg,rgba(255,255,255,.85),rgba(255,255,255,.2));pointer-events:none}
.jr-need{position:absolute;top:0;bottom:22px;width:0;border-left:2px dashed #B97A10;transition:left .4s ease;z-index:2}
.jr-nl{position:absolute;bottom:calc(100% - 26px);left:-1px;transform:translateX(-50%);display:inline-flex;align-items:center;gap:6px;height:24px;padding:0 10px;border-radius:999px;background:#FFF4E0;color:#8A5A00;font-size:12px;font-weight:600;white-space:nowrap;transition:background .3s ease,color .3s ease}
.jr-ck{display:none;width:16px;height:16px;border-radius:999px;background:#0F6B45;color:#FFFFFF;align-items:center;justify-content:center}
.jr-need.ok{border-left-color:#0F6B45}
.jr-need.ok .jr-nl{background:#E7F5EE;color:#0F6B45}
.jr-need.ok .jr-ck{display:inline-flex;animation:jrPop .4s cubic-bezier(.2,1.6,.4,1) .7s both}
@keyframes jrPop{from{transform:scale(0)}}
.jr-ax{display:flex;justify-content:space-between;margin-top:10px;font-size:13px;color:#5B6582}
.jr-ax b{font-weight:600;color:#0B1433}
.jr-drops{position:absolute;top:-34px;width:28px;height:30px;pointer-events:none;transition:left .9s cubic-bezier(.3,.8,.3,1)}
.jr-drops .dlp-c,.jr-spill .dlp-c{position:absolute;left:4px;top:0;width:20px;height:20px;opacity:0}
.jr-drops.p500 .dlp-c{animation:jrDropA .8s cubic-bezier(.5,0,.8,.4) both}
.jr-drops.p1000 .dlp-c{animation:jrDropB .8s cubic-bezier(.5,0,.8,.4) both}
.jr-drops.p2500 .dlp-c{animation:jrDropC .8s cubic-bezier(.5,0,.8,.4) both}
.jr-drops .dlp-c:nth-child(2){animation-delay:.12s !important}.jr-drops .dlp-c:nth-child(3){animation-delay:.24s !important}
@keyframes jrDropA{0%{opacity:0;transform:translateY(-10px)}20%{opacity:1}100%{opacity:0;transform:translateY(46px) scale(.7)}}
@keyframes jrDropB{0%{opacity:0;transform:translateY(-10px)}20%{opacity:1}100%{opacity:0;transform:translateY(46px) scale(.7)}}
@keyframes jrDropC{0%{opacity:0;transform:translateY(-10px)}20%{opacity:1}100%{opacity:0;transform:translateY(46px) scale(.7)}}
.jr-spill{position:absolute;right:6px;top:-6px;width:30px;height:30px;pointer-events:none}
.jr-spill .dlp-c{left:5px;top:6px;animation:jrSpill 1.2s cubic-bezier(.2,.7,.3,1) .7s both}
.jr-spill .dlp-c:nth-child(2){--sx:26px;--sy:-34px;animation-delay:.78s}.jr-spill .dlp-c:nth-child(3){--sx:-14px;--sy:-42px;animation-delay:.86s}.jr-spill .dlp-c:nth-child(4){--sx:40px;--sy:-14px;animation-delay:.94s}
@keyframes jrSpill{0%{opacity:0;transform:translate(0,0) scale(.6)}30%{opacity:1}100%{opacity:0;transform:translate(var(--sx,10px),var(--sy,-30px)) rotate(200deg) scale(1)}}
.jr[data-go] .jr-base{animation:jrFill .9s cubic-bezier(.3,.8,.3,1) .1s both}
@keyframes jrFill{from{width:0}}
@media (prefers-reduced-motion: reduce){.jr-wave,.jr-drops .dlp-c,.jr-spill .dlp-c,.jr[data-go] .jr-base{animation:none}}
@media (max-width: 760px){.jr{margin-top:18px}.jr-tube{height:38px}.jr-nl{font-size:11.5px;height:22px;padding:0 8px}}
'''

# ---------- 3 · holographic record seal ----------
HOLO_CSS = r'''.rc-main .cd-val{position:relative;overflow:hidden;background:radial-gradient(120% 90% at 100% 0%,#FFFBF0 0%,#FFFFFF 46%),#FFFFFF;border-color:#EADFC2}
.rc-main .cd-val::before{content:"";position:absolute;inset:8px;border:1px solid #F1E6C9;border-radius:14px;pointer-events:none}
.rc-main .cd-val::after{content:"";position:absolute;inset:0;pointer-events:none;opacity:.5;background-image:repeating-radial-gradient(circle at 0 100%,transparent 0 13px,rgba(200,150,30,.07) 13px 14px),repeating-radial-gradient(circle at 100% 0,transparent 0 17px,rgba(22,82,240,.05) 17px 18px)}
.rc-main .cd-val > *{position:relative;z-index:1}
.rc-main .cd-chk{background:linear-gradient(180deg,#FFFAEB,#FFF3D6);box-shadow:inset 0 0 0 1px #F4E3B5}
.rc-main .cd-chk span{color:#6B5A33}
.hl{position:relative;width:76px;height:76px;align-self:start;perspective:500px}
.hl-in{position:absolute;inset:0;transform:rotateX(var(--ry,0deg)) rotateY(var(--rx,0deg));transform-style:preserve-3d;transition:transform .25s ease-out}
.hl .cd-seal{width:100%;height:100%;filter:drop-shadow(0 10px 16px rgba(168,122,18,.35))}
.hl-sh{position:absolute;inset:4%;border-radius:50%;pointer-events:none;mix-blend-mode:color-dodge;opacity:.85;-webkit-mask:radial-gradient(circle,#000 62%,transparent 63%);mask:radial-gradient(circle,#000 62%,transparent 63%);background:conic-gradient(from var(--ha,0deg) at var(--hx,30%) var(--hy,30%),rgba(255,120,200,.0),rgba(120,220,255,.75),rgba(255,255,160,.7),rgba(255,140,220,.65),rgba(120,255,200,.6),rgba(255,120,200,.0));animation:hlSpin 6s linear infinite}
.hl-gl{position:absolute;inset:4%;border-radius:50%;pointer-events:none;-webkit-mask:radial-gradient(circle,#000 62%,transparent 63%);mask:radial-gradient(circle,#000 62%,transparent 63%);background:linear-gradient(115deg,transparent 35%,rgba(255,255,255,.85) 48%,transparent 60%);background-size:260% 100%;animation:hlGlint 3.4s ease-in-out infinite}
@property --ha{syntax:'<angle>';inherits:false;initial-value:0deg}
@keyframes hlSpin{to{--ha:360deg}}
@keyframes hlGlint{0%,35%{background-position:130% 0}70%,100%{background-position:-60% 0}}
.hl-cap{display:inline-flex;align-items:center;gap:6px;margin-top:10px;font-size:12px;font-weight:500;color:#8A6A1E}
.hl-cap i{width:6px;height:6px;border-radius:50%;background:linear-gradient(135deg,#7FD6FF,#FF9AD5,#FFE27A)}
@media (prefers-reduced-motion: reduce){.hl-sh,.hl-gl{animation:none}}
@media (max-width: 760px){.hl{width:60px;height:60px}}
'''
HOLO_JS = r'''
  holoMove(e) {
    var el = document.querySelector('.rc-main .cd-val'), h = document.querySelector('.hl'); if (!el || !h) return;
    var r = el.getBoundingClientRect(), x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
    h.style.setProperty('--rx', ((x - .5) * 26).toFixed(1) + 'deg'); h.style.setProperty('--ry', ((.5 - y) * 26).toFixed(1) + 'deg'); h.style.setProperty('--hx', (x * 100).toFixed(0) + '%'); h.style.setProperty('--hy', (y * 100).toFixed(0) + '%');
  }
  holoOut() { var h = document.querySelector('.hl'); if (h) { h.style.setProperty('--rx', '0deg'); h.style.setProperty('--ry', '0deg'); } }
'''

# ---------- 4 · TruVault vault door (Backpack dialog) ----------
def _bolts():
    import math
    out = ''
    for k in range(12):
        a = k * 30
        out += '<rect x="-3" y="-66" width="6" height="11" rx="3" transform="rotate(%d)"></rect>' % a
    return out
def _rivets():
    out = ''
    for k in range(24):
        out += '<circle cx="0" cy="-47" r="1.3" transform="rotate(%g)"></circle>' % (k * 15)
    return out
VAULT = ('<div class="vt" aria-hidden="true"><div class="vt-st">'
         '<div class="vt-fr"><span class="vt-scr s1"></span><span class="vt-scr s2"></span><span class="vt-scr s3"></span><span class="vt-scr s4"></span>'
         '<span class="vt-hole"><span class="vt-in"></span></span>'
         '<span class="vt-card"><span class="lr-pf-i">CREDI</span><i></i><i></i></span>'
         '<div class="vt-door"><svg viewBox="-70 -70 140 140" width="140" height="140">'
         '<defs><radialGradient id="vdF" cx="38%" cy="32%" r="80%"><stop offset="0" stop-color="#2C3F86"></stop><stop offset=".55" stop-color="#16245E"></stop><stop offset="1" stop-color="#0B1433"></stop></radialGradient>'
         '<linearGradient id="vdR" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#C9D7FB"></stop><stop offset=".45" stop-color="#4C7DFF"></stop><stop offset="1" stop-color="#1B2A63"></stop></linearGradient>'
         '<linearGradient id="vdS" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".22"></stop><stop offset=".5" stop-color="#FFFFFF" stop-opacity="0"></stop></linearGradient></defs>'
         '<g class="vt-bolts" fill="#9DB8F7">' + _bolts() + '</g>'
         '<circle r="60" fill="url(#vdF)" stroke="url(#vdR)" stroke-width="3.5"></circle>'
         '<circle r="52" fill="none" stroke="rgba(157,184,247,.22)" stroke-width="1"></circle>'
         '<g fill="rgba(157,184,247,.55)">' + _rivets() + '</g>'
         '<circle r="40" fill="none" stroke="rgba(157,184,247,.14)" stroke-width="8"></circle>'
         '<g class="vt-dial"><g stroke="#C9D7FB" stroke-width="3.5" stroke-linecap="round"><path d="M0 0V-30M0 0 26 15M0 0-26 15"></path></g>'
         '<g fill="#C9D7FB"><circle cx="0" cy="-30" r="4.5"></circle><circle cx="26" cy="15" r="4.5"></circle><circle cx="-26" cy="15" r="4.5"></circle></g>'
         '<circle r="11" fill="#0B1433" stroke="url(#vdR)" stroke-width="2.5"></circle><circle r="4" fill="#4C7DFF"></circle></g>'
         '<ellipse cx="-14" cy="-30" rx="40" ry="20" fill="url(#vdS)" transform="rotate(-24)"></ellipse>'
         '</svg></div>'
         '<span class="vt-glow"></span></div>'
         '<span class="vt-ok">CKI</span>'
         '</div></div>')
VAULT_CSS = r'''.vt{position:relative;width:220px;height:178px;margin:2px auto 0}
.vt-st{position:absolute;inset:0;perspective:720px}
.vt-fr{position:absolute;left:24px;top:8px;width:172px;height:162px;border-radius:30px;background:linear-gradient(155deg,#22327A 0%,#0F1A45 55%,#0B1433 100%);box-shadow:0 26px 44px -20px rgba(11,20,51,.6),inset 0 1px 0 rgba(255,255,255,.12),inset 0 -2px 0 rgba(0,0,0,.35);transform-style:preserve-3d;animation:vtIn .45s cubic-bezier(.2,1.2,.4,1) both}
.vt-fr::before{content:"";position:absolute;inset:8px;border-radius:24px;border:1px solid rgba(157,184,247,.16)}
.vt-scr{position:absolute;width:7px;height:7px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#C9D7FB,#4C6BB8 70%);box-shadow:0 1px 0 rgba(0,0,0,.4)}
.vt-scr.s1{left:16px;top:16px}.vt-scr.s2{right:16px;top:16px}.vt-scr.s3{left:16px;bottom:16px}.vt-scr.s4{right:16px;bottom:16px}
.vt-hole{position:absolute;left:50%;top:50%;width:136px;height:136px;margin:-68px 0 0 -68px;border-radius:50%;background:#050A1C;box-shadow:inset 0 0 0 3px #0B1433,inset 0 10px 24px rgba(0,0,0,.8)}
.vt-in{position:absolute;inset:18px;border-radius:50%;background:radial-gradient(circle,rgba(76,125,255,.35),transparent 70%);animation:vtPulse 1.6s ease-in-out infinite}
.vt-card{position:absolute;left:-58px;top:52px;width:62px;height:44px;box-sizing:border-box;padding:6px;border-radius:10px;background:#FFFFFF;border:1.5px solid #DCE5FB;box-shadow:0 12px 22px -8px rgba(11,20,51,.45);display:grid;grid-template-columns:28px 1fr;grid-template-rows:1fr 1fr;column-gap:5px;align-items:center;z-index:2;animation:vtFly .75s cubic-bezier(.6,0,.3,1) .3s both}
.vt-card .lr-pf-i{grid-row:1 / span 2;width:28px;height:28px;border-radius:8px}
.vt-card .lr-pf-i svg{width:15px;height:15px}
.vt-card i{display:block;height:3px;border-radius:3px;background:#DCE5FB}
.vt-card i:last-child{width:70%}
.vt-door{position:absolute;left:16px;top:11px;width:140px;height:140px;z-index:3;transform-origin:0 50%;transform:rotateY(-108deg);animation:vtShut .55s cubic-bezier(.3,1.25,.5,1) 1s both;filter:drop-shadow(0 10px 14px rgba(0,0,0,.45))}
.vt-door svg{display:block}
.vt-dial{transform-box:fill-box;transform-origin:center;animation:vtSpin .7s cubic-bezier(.5,0,.3,1) 1.5s both}
.vt-bolts{transform-box:view-box;transform-origin:0 0;transform:scale(.86);animation:vtBolt .22s cubic-bezier(.4,1.6,.6,1) 2.15s both}
.vt-glow{position:absolute;left:50%;top:50%;width:150px;height:150px;margin:-75px 0 0 -75px;border-radius:50%;box-shadow:0 0 0 2px #4C7DFF,0 0 30px rgba(76,125,255,.7);opacity:0;z-index:4;pointer-events:none;animation:vtGlow .9s ease-out 2.2s both}
.vt-ok{position:absolute;right:16px;bottom:2px;width:32px;height:32px;border-radius:50%;background:#0F6B45;color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 4px #FFFFFF,0 8px 16px -6px rgba(15,107,69,.6);z-index:5;animation:vtOk .4s cubic-bezier(.2,1.6,.4,1) 2.35s both}
@keyframes vtIn{from{opacity:0;transform:translateY(10px) scale(.94)}}
@keyframes vtPulse{50%{opacity:.4}}
@keyframes vtFly{0%{transform:translate(0,0) rotate(-8deg)}50%{transform:translate(58px,-14px) rotate(3deg)}100%{transform:translate(112px,6px) scale(.35);opacity:0}}
@keyframes vtShut{from{transform:rotateY(-108deg)}to{transform:rotateY(0)}}
@keyframes vtSpin{from{transform:rotate(0)}to{transform:rotate(-240deg)}}
@keyframes vtBolt{to{transform:scale(1)}}
@keyframes vtGlow{0%{opacity:0;transform:scale(.9)}35%{opacity:1}100%{opacity:0;transform:scale(1.12)}}
@keyframes vtOk{from{opacity:0;transform:scale(0)}}
@media (prefers-reduced-motion: reduce){.vt-fr,.vt-in,.vt-card,.vt-door,.vt-dial,.vt-bolts,.vt-glow,.vt-ok{animation:none}.vt-card{opacity:0}.vt-door{transform:none}.vt-bolts{transform:none}}
'''

# ---------- 5 · Nova -> tutor baton (Ask Tutor) ----------
def baton(nova_av):
    return ('<div class="bt" data-wow="1" data-go="1" aria-hidden="true">' + nova_av +
            '<span class="bt-tr"><span class="bt-ln"></span><span class="bt-card"><i></i><i></i><i></i></span></span>'
            '<span class="av tu-av bt-to">TA</span></div>')
BATON_CSS = r'''.bt{display:flex;align-items:center;gap:10px;margin-bottom:12px}
.bt .nv-av{width:30px !important;height:30px !important;flex-shrink:0}
.bt-tr{position:relative;flex:1;height:30px;max-width:260px}
.bt-ln{position:absolute;left:0;right:0;top:50%;height:0;border-top:2px dashed #C9D7FB}
.bt[data-go] .bt-ln{background:none}
.bt-ln::after{content:"";position:absolute;left:0;top:-2px;height:2px;width:0;background:#1652F0;border-radius:2px}
.bt[data-go] .bt-ln::after{animation:btLine 1.5s cubic-bezier(.5,0,.3,1) .2s forwards}
.bt-card{position:absolute;left:0;top:50%;width:30px;height:22px;margin-top:-11px;border-radius:6px;background:#FFFFFF;border:1.5px solid #9DB8F7;box-shadow:0 0 0 4px rgba(22,82,240,.12),0 0 18px rgba(22,82,240,.45);display:flex;flex-direction:column;justify-content:center;gap:2px;padding:0 5px;box-sizing:border-box}
.bt-card i{display:block;height:2px;border-radius:2px;background:#9DB8F7}
.bt-card i:nth-child(2){width:70%}.bt-card i:nth-child(3){width:45%}
.bt[data-go] .bt-card{animation:btRun 1.5s cubic-bezier(.5,0,.3,1) .2s both}
.bt .bt-to{width:30px;height:30px;font-size:11px}
.bt[data-go] .bt-to{animation:btGet .6s ease 1.65s both}
.bt[data-go] .nv-av{animation:btGive .5s ease .1s both}
@keyframes btLine{to{width:100%}}
@keyframes btRun{0%{left:0;transform:scale(.6);opacity:0}12%{opacity:1;transform:scale(1)}85%{left:calc(100% - 30px);transform:scale(1)}100%{left:calc(100% - 30px);transform:scale(.4);opacity:0}}
@keyframes btGet{0%{box-shadow:0 0 0 0 rgba(22,82,240,.55)}100%{box-shadow:0 0 0 12px rgba(22,82,240,0)}}
@keyframes btGive{0%{box-shadow:0 0 0 0 rgba(22,82,240,.45)}100%{box-shadow:0 0 0 10px rgba(22,82,240,0)}}
.bt[data-go] .bt-done{animation:btDone .3s ease 1.7s both}
@media (prefers-reduced-motion: reduce){.bt[data-go] .bt-card,.bt[data-go] .bt-ln::after,.bt[data-go] .bt-to,.bt[data-go] .nv-av{animation:none}.bt-ln::after{width:100%}.bt-card{display:none}}
'''
