"""Shared work-area layout: main column + right rail (Nova card, context cards, section flow, rings)."""
from l4kit import *

def nova_rail(msg, chips_html='', cls=''):
    """Nova Copilot card for the right rail (client copy: per-page Copilot line + actions)."""
    return ('<section class="rn nova-card%s"><header class="rn-h">%s<span><b>Nova</b><em>Creator Copilot · %s</em></span></header>'
            '<p>%s</p>%s<footer><b>Nova</b> proposes. You approve every change.</footer></section>') % (
        (' ' + cls) if cls else '', nova_av(), COURSE, msg, ('<div class="rn-a">%s</div>' % chips_html) if chips_html else '')

def flow(items, cur):
    """Steps of a multi-page section (desktop rail)."""
    return '<nav class="ds-card rf" aria-label="Pages in this section"><ol>%s</ol></nav>' % ''.join(
        '<li class="%s"><a href="%s"><span class="rf-d">%s</span><span>%s</span></a></li>' % (
            'on' if i == cur else ('dn' if i < cur else ''), h, ck(10) if i < cur else i + 1, l) for i, (l, h) in enumerate(items))
def ring(pct, size=132, stroke=10, cls='', track='#EAF0FF', color='#1652F0', grad=None):
    c = 2 * 3.14159 * 50
    d = c * pct / 100.0
    g = ''
    col = color
    if grad:
        g = '<defs><linearGradient id="%s" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="%s"></stop><stop offset="1" stop-color="%s"></stop></linearGradient></defs>' % grad
        col = 'url(#%s)' % grad[0]
    return ('<svg class="rg%s" viewBox="0 0 120 120" width="%d" height="%d" aria-hidden="true">%s<circle cx="60" cy="60" r="50" fill="none" stroke="%s" stroke-width="%d"></circle>'
            '<circle class="rg-a" cx="60" cy="60" r="50" fill="none" stroke="%s" stroke-width="%d" stroke-linecap="round" stroke-dasharray="%.1f 400" style="--d: %.1f" transform="rotate(-90 60 60)"></circle></svg>') % (
        (' ' + cls) if cls else '', size, size, g, track, stroke, col, stroke, d, d)

WK_CSS = r'''.wk{margin-top:24px;display:grid;grid-template-columns:minmax(0,1fr) 312px;grid-template-rows:auto 1fr;grid-template-areas:"m r" "a r";column-gap:24px;align-items:start}
.hm-next + .wk{margin-top:16px}
.wk-m{grid-area:m;min-width:0;display:flex;flex-direction:column;gap:16px}
.wk-m > .fc,.wk-m > .fc + .fc,.wk-m > .hm-list,.wk-m > .hm-det{margin-top:0}
.wk-a{grid-area:a;align-self:start}
.wk-a:not(:has(.sv-s:not(:empty))){justify-self:end;padding-left:14px}
.wk-r .hm-det{padding:18px 14px 14px 14px;margin:0}
.wk-r .hm-det .rx-k{margin:0 4px 12px 4px}
.wk-r .hm-dg{grid-template-columns:repeat(2,minmax(0,1fr));gap:6px;padding:0}
.wk-r .hm-dg span{padding:10px 12px}
.wk-r .hm-dg b{font-size:17px}
.wk-r .hm-dg em{font-size:12px}
.fl-f .cnt{align-self:center;margin:0}
.cv2 .cov{display:grid;grid-template-columns:minmax(0,1fr) auto;align-items:center;height:auto;padding:6px 14px 10px 6px;row-gap:10px;column-gap:10px}
.cv2 .cov-i{grid-column:1 / -1;width:auto;height:96px;border-radius:9px;font-size:24px;letter-spacing:-0.02em;background:radial-gradient(circle at 85% 20%,rgba(92,134,255,.7),rgba(92,134,255,0) 55%),linear-gradient(140deg,#1652F0,#0B1433)}
.cv2 .cov-t{padding-left:8px}
.ce-r{display:grid;grid-template-columns:40px minmax(0,1fr) 196px 128px;gap:14px;padding:14px 0}
.ce-r > .ds-ghost,.ce-r > .ce-x{justify-self:end}
.sk-r{grid-template-columns:minmax(0,1fr) 148px 148px minmax(0,1fr) 36px}
.sk-r .ds-in{padding-left:12px;font-size:14.5px}
textarea.ds-in.lo-in{field-sizing:content}
.mx{min-width:0}
.mx-r{grid-template-columns:minmax(190px,1.7fr) repeat(var(--n),minmax(0,1fr))}
.mx-hd span:first-child{text-align:left}
.mx-o .ds-tag{height:auto;min-height:26px;padding:4px 10px;white-space:normal;line-height:1.35}
.wk-m .hm-r{min-height:76px}
.wk-r{grid-area:r;min-width:0;position:sticky;top:92px;display:flex;flex-direction:column;gap:14px}
.wk-m .hm-dg{grid-template-columns:repeat(4,minmax(0,1fr))}
.rn{position:relative;overflow:hidden;isolation:isolate;padding:18px 18px 14px 18px;border-radius:20px;border:1.5px solid #DCE5FB}
.rn::after{content:'';position:absolute;z-index:-1;top:0;bottom:0;left:-60%;width:40%;background:linear-gradient(100deg,rgba(255,255,255,0),rgba(255,255,255,.75),rgba(255,255,255,0));transform:skewX(-18deg);animation:rnSheen 7s ease-in-out 1.2s infinite}
@keyframes rnSheen{0%{left:-60%}22%{left:130%}100%{left:130%}}
.rn-h{display:flex;align-items:center;gap:10px}
.rn-h .nv-av{animation:rnAura 3.2s ease-in-out infinite}
@keyframes rnAura{0%,100%{box-shadow:0 0 0 0 rgba(22,82,240,0)}50%{box-shadow:0 0 0 5px rgba(22,82,240,.12)}}
.rn-h > span{display:flex;flex-direction:column;min-width:0}
.rn-h b{font-size:14.5px;font-weight:600}
.rn-h em{font-style:normal;font-size:12px;color:#5B6582;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.rn p{margin:12px 0 0 0;font-size:14px;line-height:1.55;color:#0B1433}
.rn-a{margin-top:14px;display:flex;flex-wrap:wrap;align-items:center;gap:8px}
.rn-a .ds-chip{height:34px;padding:0 12px;font-size:13px;gap:5px}
.rn-a .ds-link{border:0;background:none;font-family:inherit;cursor:pointer;font-size:13.5px;padding:0 6px}
.rn footer{margin-top:14px;padding-top:12px;border-top:1px solid rgba(11,20,51,.07);font-size:12px;color:#5B6582}
.rn footer b{font-weight:600;color:#3A4566}
.ds-btn.sm{height:36px;padding:0 16px;font-size:13.5px}
.ds-btn.wh2{background:#0B1433;color:#FFFFFF;box-shadow:none}
.ds-btn.wh2:hover{background:#1B2550;color:#FFFFFF}
.rx{padding:18px;border-radius:20px}
.rx-k{display:flex;align-items:center;margin-bottom:12px;font-size:12.5px;font-weight:500;color:#8A93AD}
.rx-p{margin:12px 0 0 0;font-size:13px;line-height:1.5;color:#5B6582}
.cr-rx{background:linear-gradient(160deg,#FFF1CF,#FFFAEB);border-color:#F4D98E}
.cr-n{display:flex;align-items:center;gap:12px}
.cr-n b{font-size:26px;font-weight:600;letter-spacing:-0.02em;color:#5A3B00}
.cr-n span{margin-top:6px;font-size:13.5px;font-weight:500;color:#7A5300}
.cr-rx p{margin:8px 0 0 0;font-size:13.5px;color:#6B4A00}
.cr-a{margin-top:14px;display:flex;align-items:center;gap:6px}
.cr-a .ds-ghost{background:#FFFFFF;border-color:#F0D08A;color:#5A3B00}
.cr-a .ds-link{color:#7A5300;padding:0 10px;font-size:13.5px}
.pv-c{display:block;border-radius:16px;border:1.5px solid #E6EAF3;overflow:hidden;background:#FFFFFF;box-shadow:0 18px 30px -26px rgba(11,20,51,.5);transition:transform .3s ease}
.pv:hover .pv-c{transform:translateY(-3px)}
.pv-cv{position:relative;display:block;height:112px;overflow:hidden;background:radial-gradient(circle at 85% 20%,rgba(92,134,255,.75),rgba(92,134,255,0) 55%),linear-gradient(140deg,#1652F0,#0B1433)}
.pv-cv i{position:absolute;left:16px;bottom:10px;font-style:normal;font-size:30px;font-weight:600;letter-spacing:-0.03em;color:#FFFFFF}
.pv-cv em{position:absolute;right:16px;height:6px;border-radius:6px;background:rgba(255,255,255,.22)}
.pv-cv em:nth-of-type(1){top:20px;width:84px}
.pv-cv em:nth-of-type(2){top:34px;width:56px;background:rgba(255,255,255,.4)}
.pv-cv em:nth-of-type(3){top:48px;width:70px}
.pv-tg{display:flex;gap:6px;padding:12px 14px 0 14px}
.pv-tg .ds-tag{height:24px;font-size:11.5px}
.pv-c b{display:block;padding:8px 14px 0 14px;font-size:15px;font-weight:600}
.pv-c p{margin:4px 0 0 0;padding:0 14px;font-size:13px;line-height:1.5;color:#5B6582}
.pv-sk{display:flex;flex-wrap:wrap;gap:6px;padding:12px 14px 14px 14px}
.pv-sk i{font-style:normal;font-size:12px;font-weight:500;padding:4px 9px;border-radius:999px;background:#F5F8FF;color:#0E3BB8}
.lp{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:12px}
.lp li{display:flex;align-items:center;gap:12px}
.lp li > span:last-child{display:flex;flex-direction:column;gap:1px}
.lp-i{width:24px;height:24px;flex-shrink:0;border-radius:50%;background:#E7F5EE;color:#0F6B45;display:flex;align-items:center;justify-content:center}
.lp b{font-size:14px;font-weight:600}
.lp em{font-style:normal;font-size:12.5px;color:#5B6582}
.rm{padding:0;overflow:hidden;background:radial-gradient(circle at 50% 50%,#F5F8FF,#FFFFFF 70%)}
.rm-v{position:relative;display:block;height:216px}
.rm-o{position:absolute;left:50%;top:50%;width:150px;height:150px;margin:-76.5px 0 0 -76.5px;border-radius:50%;border:1.5px dashed #BBCBF3;animation:rmSpin 46s linear infinite}
.rm-o.b{width:236px;height:236px;margin:-119.5px 0 0 -119.5px;border-color:#E1E7F4;animation-direction:reverse;animation-duration:70s}
@keyframes rmSpin{to{transform:rotate(360deg)}}
.rm-c{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);display:flex;flex-direction:column;align-items:center;gap:2px;padding:12px 18px;border-radius:18px;background:linear-gradient(150deg,#1652F0,#0E3BB8);color:#FFFFFF;box-shadow:0 16px 30px -14px rgba(22,82,240,.7);white-space:nowrap}
.rm-c svg{margin-bottom:4px;opacity:.85}
.rm-c b{font-size:14.5px;font-weight:600}
.rm-c em{font-style:normal;font-size:11.5px;color:rgba(255,255,255,.75)}
.rm-s{position:absolute;padding:6px 11px;border-radius:999px;background:#FFFFFF;border:1.5px solid #D6DDEE;box-shadow:0 8px 18px -12px rgba(11,20,51,.35);white-space:nowrap;animation:rmFloat 5s ease-in-out infinite}
.rm-s b{font-size:12.5px;font-weight:500;color:#0B1433}
.rm-s.s1{left:16px;top:20px}
.rm-s.s2{right:14px;bottom:20px;animation-delay:-2.5s}
@keyframes rmFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-5px)}}
.ld{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:7px}
.ld li{display:grid;grid-template-columns:88px minmax(0,1fr);align-items:center;gap:10px;font-size:12.5px;font-weight:500;color:#3A4566}
.ld li span{order:-1}
.ld li i{display:block;height:10px;border-radius:6px;width:calc(20% + var(--i) * 20%);background:linear-gradient(90deg,#AFC1F5,#1652F0);opacity:calc(.45 + var(--i) * .14);transform-origin:left center;animation:ldGrow .9s cubic-bezier(.2,.8,.2,1) both;animation-delay:calc(var(--i) * 110ms + 200ms)}
@keyframes ldGrow{from{transform:scaleX(0)}}
.cvl{list-style:none;margin:0;padding:0;display:flex;flex-direction:column}
.cvl li{display:grid;grid-template-columns:minmax(0,1fr) auto;align-items:center;gap:3px 10px;padding:11px 0;border-top:1.5px solid #F0F2F8}
.cvl li:first-child{border-top:0;padding-top:0}
.cvl-h{display:flex;flex-direction:column;gap:1px;min-width:0}
.cvl-h b{font-size:14px;font-weight:600}
.cvl-h em{font-style:normal;font-size:12px;color:#5B6582}
.cvl li.amb .cvl-h em{color:#8A5A00}
.cvl-b{display:flex;gap:3px}
.cvl-b i{width:14px;height:6px;border-radius:3px;background:#E6EAF3}
.cvl-b i.on{background:#1652F0;animation:cvOn .5s ease both}
.cvl-b i.on:nth-child(2){animation-delay:.12s}
@keyframes cvOn{from{background:#E6EAF3}}
.cvl-d{grid-column:1 / -1;font-size:12.5px;color:#3A4566}
.inf{display:flex;flex-direction:column;align-items:flex-start;gap:12px}
.inf-i{width:38px;height:38px;border-radius:12px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.inf p{margin:0;font-size:13.5px;line-height:1.55;color:#3A4566}
.inf .ds-link,.lip2 .ds-link{display:inline-flex;align-items:center;gap:6px;font-size:13.5px}
.ls-n{display:block;font-size:30px;font-weight:600;letter-spacing:-0.025em;line-height:1.1}
.ls-r,.lip-r{display:flex;align-items:center;gap:14px}
.ls-r{margin-top:16px;padding-top:16px;border-top:1.5px solid #F0F2F8}
.ls-r > span,.lip-r > span{display:flex;flex-direction:column;gap:2px}
.ls-r b,.lip-r b{font-size:20px;font-weight:600;letter-spacing:-0.01em}
.ls-r em,.lip-r em{font-style:normal;font-size:12.5px;color:#5B6582}
.lip-r{margin-bottom:16px}
.wk-r .sg{gap:6px}
.wk-r .sg-i{height:28px;padding:0 10px 0 8px;gap:6px;font-size:12px}
.rg-a{animation:rgDraw 1.4s cubic-bezier(.2,.8,.2,1) .25s both}
@keyframes rgDraw{from{stroke-dasharray:0 400}}
.rf{padding:8px}
.rf ol{list-style:none;margin:0;padding:0}
.rf li{position:relative}
.rf li + li::before{content:'';position:absolute;left:20.25px;top:-11px;width:1.5px;height:22px;background:#D6DDEE}
.rf li.dn + li::before{background:#1652F0}
.rf a{position:relative;display:flex;align-items:center;gap:10px;min-height:44px;padding:0 10px;border-radius:12px;color:#3A4566;font-size:13.5px;font-weight:500;text-decoration:none}
.rf a:hover{background:#F7F9FD;color:#0B1433}
.rf-d{position:relative;z-index:1;width:22px;height:22px;flex-shrink:0;box-sizing:border-box;border-radius:50%;border:1.5px solid #CBD3E6;background:#FFFFFF;color:#5B6582;font-size:11.5px;font-weight:600;display:flex;align-items:center;justify-content:center}
.rf li.dn .rf-d{border-color:#E7F5EE;background:#E7F5EE;color:#0F6B45}
.rf li.on a{background:#F5F8FF;color:#0B1433;font-weight:600}
.rf li.on .rf-d{border-color:#1652F0;background:#1652F0;color:#FFFFFF;box-shadow:0 0 0 4px rgba(22,82,240,.14)}
.mst{display:none}
.qs{display:flex;flex-direction:column}
.qz{display:grid;grid-template-columns:32px minmax(0,1fr);gap:16px;padding:18px 0;border-top:1.5px solid #F0F2F8}
.qz:first-child{border-top:0;padding-top:2px}
.qz:last-child{padding-bottom:0}
.qz-n{width:32px;height:32px;border-radius:50%;background:#EAF0FF;color:#0E3BB8;font-size:13px;font-weight:600;display:flex;align-items:center;justify-content:center}
.qz-b{display:grid;grid-template-columns:minmax(0,1fr) auto;align-items:center;gap:12px 20px;min-width:0}
.qz-b > b{font-size:15px;font-weight:600;line-height:1.4}
.qz-b > .ds-seg{grid-row:1;grid-column:2}
.qz-b > .fl-sub,.qz-b > .chips{grid-column:1 / -1;margin:0}
.qz-b > .fl-sub{margin-bottom:-4px}
.cv2{grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr)}
.fg2.keep{grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}
.pq-q .ds-seg{width:100%;box-sizing:border-box}
.pq-q .ds-seg button{padding:0 10px}
.ce-m{display:flex;flex-direction:column;align-items:flex-start;gap:6px;min-width:0}
.ce-m .ce-s{font-size:12.5px;line-height:1.4;align-items:flex-start}
.ce-m .ce-s svg{margin-top:1px}
.ce-m .ce-s svg{flex-shrink:0}
.opt3.v .ds-opt{align-items:flex-start}
.lo{position:relative;gap:14px}
.lo-r{position:relative;grid-template-columns:36px minmax(0,1fr);gap:14px}
.lo-r:not(:last-child)::before{content:'';position:absolute;left:17px;top:38px;bottom:-16px;width:2px;border-radius:2px;background:linear-gradient(180deg,#1652F0,#AFC1F5)}
.lo-r:has(+ .lo-r.warn)::before{background:linear-gradient(180deg,#AFC1F5,#F4DDAA)}
.lo-n{position:relative;z-index:1;margin-top:2px;box-shadow:0 0 0 5px #FFFFFF}
.lo-r:not(.warn) .lo-n{background:#1652F0;color:#FFFFFF}
.lo-b{min-width:0;padding:12px 12px 14px 16px;border-radius:16px;border:1.5px solid #E6EAF3;background:#FFFFFF;transition:border-color .2s ease,box-shadow .2s ease}
.lo-b:focus-within{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.1)}
.lo-r.warn .lo-b{border-color:#F4DDAA;background:#FFFCF5}
.lo-h{display:flex;align-items:center;justify-content:space-between;gap:10px;margin:-4px -4px 2px 0}
.lo-h .lo-k{margin:0}
textarea.ds-in.lo-in{min-height:0;padding:0;border:0;border-radius:0;background:transparent;box-shadow:none;font-size:15.5px;line-height:1.5;resize:none}
textarea.ds-in.lo-in:focus{outline:none;box-shadow:none}
.lo-r.warn .lo-in{color:#8A5A00}
.lo-w{margin-top:12px;background:#FFFFFF}
.lo-f{margin-top:18px;margin-left:50px;display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.ev-r.warn .ev-o em{color:#8A5A00}
.ch-c.ok{animation:chPop .5s cubic-bezier(.2,.9,.3,1.4) both;animation-delay:calc(var(--i) * 130ms + 300ms)}
@keyframes chPop{from{transform:scale(.3);opacity:0}}
.wk-r .ch-r{grid-template-columns:42px repeat(4,minmax(0,1fr))}
.wk-r .ch-r:not(.ch-hd)::before{left:calc(37px + 12.5%);right:calc(12.5% - 5px)}
.wk-r .ch-hd{font-size:11px}
.wk-r .ch-o{font-size:13px}
.wk-r .ch-c{width:26px;height:26px}
.wk-r .ch-c.no i{width:22px;height:22px}
.ds-opt.awc{padding:20px 20px 20px 18px;gap:18px}
.aw-v{width:64px;height:64px;flex-shrink:0;border-radius:18px;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden}
.aw-v.cert{background:linear-gradient(150deg,#EAF0FF,#F7F9FD);color:#1652F0;box-shadow:inset 0 0 0 1.5px #D6E1FB}
.aw-v.badge{background:linear-gradient(150deg,#1652F0,#0B1433);color:#FFFFFF}
.aw-v::after{content:'';position:absolute;top:-20%;bottom:-20%;left:-80%;width:50%;background:linear-gradient(100deg,rgba(255,255,255,0),rgba(255,255,255,.55),rgba(255,255,255,0));transform:skewX(-18deg);animation:rnSheen 6s ease-in-out 2s infinite}
.ef-d{display:flex;flex-direction:column;gap:6px}
.ef-b{display:block;width:100%;max-width:150px;height:6px;border-radius:6px;background:#E7F5EE;overflow:hidden}
.ef-b i{display:block;height:100%;border-radius:6px;background:#0F6B45;transform-origin:left center;animation:ldGrow 1.1s cubic-bezier(.2,.8,.2,1) .3s both}
.sm-r{position:relative}
.sm-r.ok .st,.sm-r.pr .st{margin-left:0}
.hm-tt{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.hm-tt .ds-tag{height:24px;font-size:12px}
@media (prefers-reduced-motion: reduce){.rn::after,.rn-h .nv-av,.rm-o,.rm-s,.ld li i,.rg-a,.ch-c.ok,.aw-v::after,.ef-b i,.cvl-b i.on{animation:none}}
@media (max-width: 1180px){.wk{grid-template-columns:minmax(0,1fr) 280px;column-gap:20px}.fg2.keep{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width: 960px){
.wk{display:flex;flex-direction:column;align-items:stretch;gap:16px;margin-top:20px}
.hm-next + .wk{margin-top:16px}
.wk-m{display:contents}
.wk-r{display:contents}
.wk-m > *{order:2}
.wk-r > .rn{order:1}
.wk-r > .rx{order:3}
.wk-a{order:4;align-self:stretch}
.sk-r{grid-template-columns:repeat(2,minmax(0,1fr))}
.tkw{grid-column:1 / -1}
.wk-r > .pv{display:none}
.wk-r > .rf,.wk-r > .rm{display:none}
.rn{padding:16px 16px 12px 16px;border-radius:18px}
.rn p{margin-top:10px;font-size:14px}
.rn-a{margin-top:12px;flex-wrap:nowrap;overflow-x:auto;margin-right:-16px;padding-right:16px;scrollbar-width:none}
.rn-a::-webkit-scrollbar{display:none}
.rn-a > *{flex-shrink:0}
.rn footer{display:none}
.rx{padding:18px 16px;border-radius:18px}
.mst{display:flex;gap:8px;overflow-x:auto;margin:16px -16px 0 -16px;padding:2px 16px;scrollbar-width:none;scroll-snap-type:x proximity}
.mst::-webkit-scrollbar{display:none}
.mst-i{flex-shrink:0;scroll-snap-align:start;display:inline-flex;align-items:center;gap:8px;height:40px;padding:0 14px 0 10px;box-sizing:border-box;border-radius:999px;background:#FFFFFF;border:1.5px solid #E6EAF3;color:#3A4566;font-size:13.5px;font-weight:500;text-decoration:none;white-space:nowrap}
.mst-i.on{border-color:#1652F0;background:#F5F8FF;color:#0B1433}
.mst-i .st{width:16px;height:16px}
.wk-m .hm-dg{grid-template-columns:repeat(2,minmax(0,1fr))}
.cv2{grid-template-columns:minmax(0,1fr)}
.fg2.keep{grid-template-columns:repeat(2,minmax(0,1fr));gap:14px 10px}
.qz{grid-template-columns:minmax(0,1fr);gap:10px;padding:18px 0}
.qz-n{width:26px;height:26px;font-size:12px}
.qz-b{grid-template-columns:minmax(0,1fr);gap:12px}
.qz-b > .ds-seg{grid-row:auto;grid-column:1}
.qz-b .chips{flex-wrap:nowrap;overflow-x:auto;margin-right:-18px;padding-right:18px;scrollbar-width:none}
.qz-b .chips::-webkit-scrollbar{display:none}
.qz-b .chips .ds-chip{flex-shrink:0}
.ce-r{display:grid;grid-template-columns:40px minmax(0,1fr) auto;align-items:start;gap:8px 12px;padding:16px 0}
.ce-r > .ds-ghost,.ce-r > .ce-x{grid-row:1;grid-column:3;margin:0}
.ce-r > .ce-x{min-height:40px}
.ce-t{flex:none}
.ce-t b{font-size:14.5px}
.fl .ds-seg:has(> button:nth-child(4)){display:grid;grid-template-columns:repeat(2,minmax(0,1fr));border-radius:18px}
.fl .ds-seg:has(> button:nth-child(4)) button{border-radius:14px}
.mx-r{gap:6px}
.mx-c{height:34px;padding:0 11px;font-size:12.5px}
.ce-m{grid-column:2 / -1;grid-row:2;margin:0;flex-direction:row;flex-wrap:wrap;align-items:center;gap:6px 10px}
.ce-m .ce-s{margin-left:0;flex-basis:auto}
.wk-a:not(:has(.sv-s:not(:empty))){justify-self:stretch;padding-left:16px}
.lo-r:not(:last-child)::before{left:13px;top:30px}
.lo-r{grid-template-columns:28px minmax(0,1fr);gap:10px}
.lo-n{display:flex;width:28px;height:28px;font-size:12.5px;box-shadow:0 0 0 4px #FFFFFF}
.lo-b{padding:10px 8px 12px 14px;border-radius:14px}
textarea.ds-in.lo-in{font-size:15px}
.lo-w{flex-direction:column;align-items:flex-start;gap:10px}
.lo-w p{flex-basis:auto}
.lo-w .ds-ghost{margin-left:0}
.lo-f{margin-left:38px}
.ds-opt.awc{padding:16px;gap:14px}
.aw-v{width:52px;height:52px;border-radius:15px}
.ef-b{max-width:none}
}
'''
