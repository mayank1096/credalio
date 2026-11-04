"""Shared Credalio UI kit for the Landing canvas (canvas3).

Every value is copied from Links 1 and 2 (dash.py ds-*, tipx.py, confetti.py, the CR-KYC-003 ko-* outcome,
think1018.py nv-think, the Nova head crop from cpx.py) so the three links share one set of elements.
Pages get KIT_CSS once at the top of their <style>, and their markup uses only these classes for
buttons, links, chips, tags, option cards, inputs, ask bars, close buttons, mobile bars, tooltips,
outcome emblems, confetti, Nova avatar / card / thinking state and the gold coin.

Usage: from kit import KIT_CSS, btn, ghost, tip, info, conf, emblem, nova_av, think, coin, ck
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
import confetti as _cf

NOVA = '/_blob/398ca91d2832bb0ab6b0af61319676f4'
NOVA_BG = '/_blob/0b29db2e4cd6f4a89dc7ba8f12e59c8d'

ARROW = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg>'
INFO = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="M12 11v5"></path><path d="M12 7.6v.2"></path></svg>'
def ck(sz=14, sw=3):
    return '<svg class="ck" width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg>' % (sz, sz, sw)
CLOSE = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"></path></svg>'

KIT_CSS = r'''.ds-card{background:#FFFFFF;border:1.5px solid #E6EAF3;border-radius:20px;box-shadow:0 1px 2px rgba(11,20,51,.03)}
.ds-btn{display:inline-flex;align-items:center;gap:14px;height:52px;padding:0 6px 0 24px;box-sizing:border-box;border-radius:999px;background:#1652F0;color:#FFFFFF;font-family:inherit;font-size:15.5px;font-weight:600;text-decoration:none;white-space:nowrap;border:0;cursor:pointer;box-shadow:0 1px 0 rgba(255,255,255,.25) inset,0 10px 24px rgba(22,82,240,.24);transition:background .2s ease,transform .2s ease}
.ds-btn:hover{background:#0E3BB8;color:#FFFFFF;transform:translateY(-1px)}
.ds-btn .ob-arrow{width:40px;height:40px;border-radius:50%;background:#FFFFFF;color:#1652F0;display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:transform .3s cubic-bezier(.3,1.4,.5,1)}
.ds-btn:hover .ob-arrow{transform:translateX(3px)}
.ds-btn.sm{height:44px;padding:0 5px 0 18px;font-size:14.5px;gap:10px}
.ds-btn.sm .ob-arrow{width:34px;height:34px}
.ds-btn.np{padding:0 22px}
.ds-ghost{display:inline-flex;align-items:center;justify-content:center;gap:8px;height:48px;padding:0 20px;box-sizing:border-box;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;font-family:inherit;font-size:15px;font-weight:600;text-decoration:none;white-space:nowrap;cursor:pointer;transition:border-color .2s ease,background .2s ease}
.ds-ghost:hover{border-color:#1652F0;background:#F5F8FF;color:#0B1433}
.ds-ghost.sm{height:44px;padding:0 18px;font-size:14.5px}
.ds-ghost.dk{background:rgba(255,255,255,.1);border-color:rgba(255,255,255,.32);color:#FFFFFF}
.ds-ghost.dk:hover{background:rgba(255,255,255,.18);border-color:#FFFFFF}
.ds-link{display:inline-flex;align-items:center;gap:6px;color:#1652F0;font-family:inherit;font-weight:600;font-size:14.5px;text-decoration:none;background:none;border:0;padding:0;cursor:pointer;white-space:nowrap}
.ds-link:hover{color:#0E3BB8}
.ds-btn.wh{background:#FFFFFF;color:#0B1433;box-shadow:0 10px 24px rgba(11,20,51,.24)}
.ds-btn.wh .ob-arrow{background:#1652F0;color:#FFFFFF}
.ds-btn.wh:hover{background:#EAF0FF;color:#0B1433}
.ds-ghost.on{background:#EAF0FF;border-color:#1652F0;color:#0E3BB8}
.ds-link.off{opacity:.45;pointer-events:none}
.ds-tag.solid{background:#1652F0;color:#FFFFFF}
.ds-tag .tip{margin-left:0}
.ds-in.err{border-color:#D92D20}
.ds-in.err:focus{box-shadow:0 0 0 4px rgba(217,45,32,.12)}
.ds-chip{display:inline-flex;align-items:center;justify-content:center;gap:7px;height:40px;padding:0 16px;box-sizing:border-box;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;font-family:inherit;font-size:14px;font-weight:500;cursor:pointer;white-space:nowrap;flex-shrink:0;transition:border-color .2s ease,background .2s ease}
.ds-chip:hover{border-color:#1652F0;background:#F5F8FF}
.ds-chip .ck{display:none}
.ds-chip.on{background:#EAF0FF;border-color:#1652F0;color:#0E3BB8}
.ds-chip.on .ck{display:block}
.ds-chip.sm{height:34px;padding:0 13px;font-size:13px}
.ds-chip i{font-style:normal;font-size:12px;color:#8A93AD}
.ds-tag{display:inline-flex;align-items:center;gap:6px;height:26px;padding:0 10px;box-sizing:border-box;border-radius:999px;font-size:12px;font-weight:500;line-height:1;white-space:nowrap;background:#F1F3F8;color:#3A4566}
.ds-tag.blue{background:#EAF0FF;color:#0E3BB8}
.ds-tag.green{background:#E7F5EE;color:#0F6B45}
.ds-tag.amber{background:#FFF4E0;color:#8A5A00}
.ds-tag.line{background:#FFFFFF;box-shadow:inset 0 0 0 1px #E6EAF3}
.ds-tag.glass{background:rgba(255,255,255,.14);color:#FFFFFF;box-shadow:inset 0 0 0 1px rgba(255,255,255,.18)}
.ds-tag.lg{height:30px;padding:0 12px;font-size:13px}
.ds-opt{position:relative;display:flex;align-items:center;gap:14px;width:100%;box-sizing:border-box;padding:16px 18px;border-radius:14px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;font-family:inherit;text-align:left;cursor:pointer;transition:border-color .2s ease,background .2s ease}
.ds-opt:hover{border-color:#9DB8F7}
.ds-opt.on{background:#EAF0FF;border-color:#1652F0}
.ds-opt-ck{width:22px;height:22px;border-radius:999px;border:1.5px solid #CBD3E6;background:#FFFFFF;box-sizing:border-box;flex-shrink:0;margin-left:auto;display:flex;align-items:center;justify-content:center;color:#FFFFFF}
.ds-opt-ck .ck{display:none}
.ds-opt.on .ds-opt-ck{background:#1652F0;border-color:#1652F0}
.ds-opt.on .ds-opt-ck .ck{display:block}
.ds-in{height:48px;width:100%;box-sizing:border-box;padding:0 14px;border-radius:12px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:inherit;font-size:15px;color:#0B1433;outline:none;transition:border-color .2s ease,box-shadow .2s ease}
.ds-in.lg{height:56px;padding:0 18px;border-radius:14px;font-size:17px}
.ds-in::placeholder{color:#8A93AD}
.ds-in:focus{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.ds-ask{display:flex;align-items:center;gap:10px;height:60px;box-sizing:border-box;padding:6px 6px 6px 22px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;box-shadow:0 20px 40px -30px rgba(11,20,51,.5);transition:border-color .2s ease,box-shadow .2s ease}
.ds-ask:focus-within{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.ds-ask input{flex:1;min-width:0;height:100%;border:none;outline:none;background:transparent;font-family:inherit;font-size:16px;color:#0B1433}
.ds-ask input::placeholder{color:#8A93AD}
.ds-ask .ds-btn{flex-shrink:0}
.ds-ask.sm{height:50px;padding:4px 4px 4px 16px}
.ds-ask.sm input{font-size:14px}
.ds-send{width:40px;height:40px;border-radius:999px;border:none;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center;cursor:pointer;flex-shrink:0;transition:background .2s ease}
.ds-send:hover{background:#0E3BB8}
.ds-x{width:44px;height:44px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;display:flex;align-items:center;justify-content:center;cursor:pointer;flex-shrink:0;text-decoration:none;transition:border-color .2s ease}
.ds-x:hover{border-color:#1652F0}
.ds-acts{display:flex;align-items:center;justify-content:flex-end;gap:20px;margin-top:32px}
.ds-acts.c{justify-content:center}
.ds-acts.sb{justify-content:space-between}
.ds-mbar{display:none}
.ko-v.am{--k:#B97A10;--kb:#FFF4E0}
.ko-v.cb{--k:#1652F0;--kb:#EAF0FF}
.al-opts{display:grid;grid-template-columns:repeat(var(--n,3),minmax(0,1fr));gap:14px}
.al-o{position:relative;display:flex;flex-direction:column;gap:6px;padding:20px 20px 18px;border-radius:18px;background:#FFFFFF;border:1.5px solid #E6EAF3;text-align:left;box-sizing:border-box}
.al-o.rec{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.08),0 20px 40px -30px rgba(22,82,240,.5)}
.al-o > .ds-tag{position:absolute;top:-12px;left:18px}
.al-o b{font-size:16px;font-weight:600;letter-spacing:-.1px}
.al-o p{margin:0;font-size:14px;line-height:1.5;color:#4A5578}
.al-o-a{margin-top:auto;padding-top:14px}
.cr-c,.mf-c{display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;align-self:center;width:18px;height:18px;border-radius:50%;color:#FFFFFF;font-style:normal;font-size:10.5px;font-weight:700;line-height:1;box-shadow:inset 0 -1.5px 0 rgba(0,0,0,.18),inset 0 1px 0 rgba(255,255,255,.35)}
.cr-c{background:#1652F0}
.mf-c{background:#0B1433}
.cr-c.lg,.mf-c.lg{width:26px;height:26px;font-size:13px}
.ds-seg{display:flex;gap:4px;padding:4px;border-radius:999px;background:#F1F3F8}
.ds-seg button{flex:1;display:inline-flex;align-items:center;justify-content:center;gap:6px;height:38px;padding:0 14px;border:0;border-radius:999px;background:transparent;font-family:inherit;font-size:14px;font-weight:500;color:#3A4566;cursor:pointer;transition:background .2s ease,color .2s ease}
.ds-seg button.on{background:#FFFFFF;color:#0B1433;box-shadow:0 1px 2px rgba(11,20,51,.08),0 6px 14px -8px rgba(11,20,51,.25)}
.ds-seg button i{font-style:normal;min-width:20px;height:20px;padding:0 6px;box-sizing:border-box;border-radius:999px;background:#1652F0;color:#FFFFFF;font-size:11.5px;font-weight:600;display:inline-flex;align-items:center;justify-content:center}
.ds-seg button:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:2px}
.ds-btn:focus-visible,.ds-ghost:focus-visible,.ds-link:focus-visible,.ds-chip:focus-visible,.ds-opt:focus-visible,.ds-x:focus-visible,.ds-send:focus-visible,.tip:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:2px}
.tip{position:relative;display:inline-flex;align-items:center;vertical-align:-2px;margin-left:6px;color:#8A93AD;cursor:default;outline:none}
.tip:hover,.tip:focus{color:#1652F0}
.tip-b{position:absolute;bottom:calc(100% + 10px);left:-12px;width:250px;padding:12px 14px;border-radius:12px;background:#0B1433;color:#FFFFFF;font-size:13px;font-weight:400;line-height:1.45;letter-spacing:0;text-align:left;white-space:normal;box-shadow:0 14px 34px rgba(11,20,51,.22);opacity:0;visibility:hidden;transform:translateY(4px);transition:opacity .15s ease,transform .15s ease;z-index:30;pointer-events:none}
.tip-b.r{left:auto;right:-12px}
.tip-b.dn{bottom:auto;top:calc(100% + 10px)}
.tip:hover .tip-b,.tip:focus .tip-b{opacity:1;visibility:visible;transform:none}
.ko-v{--k:#0F6B45;--kb:#E7F5EE}
.ko-emb{position:relative;width:84px;height:84px;display:flex;align-items:center;justify-content:center}
.ko-halo{position:absolute;inset:0;border-radius:50%;background:var(--kb);z-index:1}
.ko-disc{position:relative;z-index:1;width:58px;height:58px;border-radius:50%;background:var(--k);color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 12px 28px rgba(11,20,51,.16)}
.ko-tick path{stroke-dasharray:1;stroke-dashoffset:1;animation:koDraw .6s ease .3s forwards}
@keyframes koDraw{to{stroke-dashoffset:0}}
.ko-pill{margin-top:14px;display:inline-flex;align-items:center;height:30px;padding:0 13px;border-radius:999px;background:var(--kb);color:var(--k);font-size:13px;font-weight:500}
.cf{position:absolute;left:50%;top:50%;width:0;height:0;pointer-events:none;z-index:0;--k:1}
.cf i{position:absolute;left:0;top:0;display:block;opacity:0;animation:cfPath var(--d) var(--dl) both}
.cf b{display:block;animation:cfSway var(--sd) ease-in-out infinite alternate}
.cf s{display:block;transform:rotate(var(--r));animation:cfFlip var(--fd) linear infinite}
@keyframes cfPath{0%{opacity:0;transform:translate(-50%,-50%);animation-timing-function:cubic-bezier(.1,.7,.25,1)}5%{opacity:1}24%{transform:translate(calc(var(--x) * var(--k) * 1px - 50%),calc(var(--y) * 1px - 50%));animation-timing-function:cubic-bezier(.42,.08,.7,.92)}86%{opacity:1}100%{opacity:0;transform:translate(calc(var(--x) * var(--k) * 1.22px - 50%),calc((var(--y) + var(--f)) * 1px))}}
@keyframes cfSway{from{transform:translateX(calc(var(--sw) * -1)) rotate(-12deg)}to{transform:translateX(var(--sw)) rotate(12deg)}}
@keyframes cfFlip{from{transform:rotate(var(--r)) rotate3d(var(--rx),1,0,0deg)}to{transform:rotate(var(--r)) rotate3d(var(--rx),1,0,360deg)}}
.nova-card{background:#FFFFFF url(NOVABG) center / cover no-repeat}
.nv-av{position:relative;flex-shrink:0;width:36px;height:36px;border-radius:50%;overflow:hidden;background:#EAF0FF;display:block}
.nv-av img{position:absolute;left:-87.5%;top:-57.81%;width:294.06%;max-width:none;height:auto;mix-blend-mode:multiply}
.nv-av.lg{width:56px;height:56px;box-shadow:0 0 0 3px #FFFFFF,0 0 0 4.5px #D6DDEE}
.nv-av.sm{width:28px;height:28px}
@keyframes nvSpin{to{transform:rotate(360deg)}}
@keyframes nvPulse{0%,100%{transform:scale(.65);opacity:.65}50%{transform:scale(1);opacity:1}}
@keyframes nvShim{from{background-position:100% 0}to{background-position:-100% 0}}
.nv-think{display:inline-flex;align-items:center;gap:10px;min-height:24px}
.nv-orb{position:relative;width:22px;height:22px;flex-shrink:0;display:flex;align-items:center;justify-content:center}
.nv-orb::before{content:'';position:absolute;inset:0;border-radius:50%;background:conic-gradient(from 0deg,#1652F0,#6E96FF,#DCE5FB,#1652F0);-webkit-mask:radial-gradient(circle,transparent 6.5px,#000 7.5px);mask:radial-gradient(circle,transparent 6.5px,#000 7.5px);animation:nvSpin 1.1s linear infinite}
.nv-orb i{width:7px;height:7px;border-radius:50%;background:#1652F0;animation:nvPulse 1.1s ease-in-out infinite}
.nv-tt{font-size:15px;font-weight:400;line-height:1.4;background:linear-gradient(90deg,#5B6582 0%,#5B6582 35%,#1652F0 50%,#5B6582 65%,#5B6582 100%);background-size:200% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:nvShim 1.6s linear infinite}
COINCSS
@media (max-width: 960px){
.ds-chip{height:36px;font-size:13.5px;padding:0 14px}
.ds-chip.sm{height:32px;font-size:12.5px;padding:0 12px}
.ds-btn{height:48px;font-size:15px}
.ds-btn .ob-arrow{width:36px;height:36px}
.ds-btn.sm{height:42px;font-size:14px}
.ds-btn.sm .ob-arrow{width:32px;height:32px}
.ds-ghost{height:44px;font-size:14.5px}
.cf{--k:.56}
}
@media (max-width: 760px){
.al-opts{grid-template-columns:minmax(0,1fr);gap:10px}
.al-o.rec{margin:12px 0 6px}
.al-o .ds-btn{width:100%;justify-content:space-between}
.al-o:not(.rec){display:grid;grid-template-columns:minmax(0,1fr) auto;column-gap:14px;row-gap:3px;padding:14px 16px}
.al-o:not(.rec) b{grid-column:1;grid-row:1;font-size:15px}
.al-o:not(.rec) p{grid-column:1 / -1;grid-row:2;font-size:13.5px}
.al-o:not(.rec) .al-o-a{grid-column:2;grid-row:1;padding-top:0;margin-top:0}
.ds-btn.sm.np{padding:0 16px}
.tip-b{display:none;width:min(250px,calc(100vw - 48px))}
.tip:hover .tip-b,.tip:focus .tip-b{display:block}
.ds-x{width:40px;height:40px}
.ds-ask{height:54px;padding:5px 5px 5px 18px}
.ds-ask input{font-size:15px}
.ds-acts,.ds-mbar{display:flex;flex-direction:column-reverse;align-items:stretch;gap:4px;position:sticky;bottom:0;z-index:20;margin:28px -20px 0;padding:12px 16px;background:#FFFFFF;border-top:1.5px solid #EEF1F7}
.ds-acts .ds-btn,.ds-mbar .ds-btn{width:100%;justify-content:space-between}
.ds-acts .ds-link,.ds-mbar .ds-link{justify-content:center;min-height:40px}
.ko-emb{width:72px;height:72px}
.ko-disc{width:48px;height:48px}
.ko-disc svg{width:24px;height:24px}
}
@media (prefers-reduced-motion: reduce){.cf{display:none}.ko-tick path{animation:none;stroke-dashoffset:0}.nv-orb::before,.nv-orb i,.nv-tt{animation:none}.nv-tt{color:#5B6582}}'''
KIT_CSS = KIT_CSS.replace('NOVABG', NOVA_BG).replace('COINCSS', open(os.path.join(HERE, 'coin.css')).read().strip())

def btn(label, href='#', cls='', extra='', tag='a'):
    """Primary pill with the white arrow circle (one per screen)."""
    h = (' href="%s"' % href) if tag == 'a' else ' type="button"'
    return '<%s class="ds-btn%s"%s%s><span>%s</span><span class="ob-arrow">%s</span></%s>' % (tag, (' ' + cls) if cls else '', h, (' ' + extra) if extra else '', label, ARROW, tag)
def ghost(label, href='#', cls='', extra=''):
    return '<a class="ds-ghost%s" href="%s"%s>%s</a>' % ((' ' + cls) if cls else '', href, (' ' + extra) if extra else '', label)
def tip(text, cls=''):
    """ⓘ info tooltip (tipx.py)."""
    return '<span class="tip" tabindex="0" aria-label="More info">%s<span class="tip-b%s" role="tooltip">%s</span></span>' % (INFO, (' ' + cls) if cls else '', text)
def conf():
    return _cf.CONF
def emblem(confetti=True):
    """Green success emblem (ko-*), confetti bursts from it."""
    tick = '<svg class="ko-tick" width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5" pathLength="1"></path></svg>'
    return '<div class="ko-emb ko-v" aria-hidden="true">%s<span class="ko-halo"></span><span class="ko-disc">%s</span></div>' % (conf() if confetti else '', tick)
def nova_av(cls=''):
    return '<span class="nv-av%s" aria-hidden="true"><img src="%s" alt=""></span>' % ((' ' + cls) if cls else '', NOVA)
def think(text):
    return '<span class="nv-think" role="status"><span class="nv-orb" aria-hidden="true"><i></i></span><span class="nv-tt">%s</span></span>' % text
def credit(lg=False):
    """Marketplace Credits: cobalt C coin (never gold)."""
    return '<i class="cr-c%s" aria-hidden="true">C</i>' % (' lg' if lg else '')
def mforge(lg=False):
    return '<i class="mf-c%s" aria-hidden="true">M</i>' % (' lg' if lg else '')
def opts():
    """Allowance options (upgrade / add DLP / wait for refresh). Data: opts [{t,d,cta,href,rec,plain,cls}], optN."""
    return ('<div class="al-opts" style="--n: {{optN}}"><sc-for list="{{opts}}" as="o" hint-placeholder-count="3"><div class="al-o {{o.cls}}">'
            '<sc-if value="{{o.rec}}" hint-placeholder-val="{{ false }}"><span class="ds-tag solid">Recommended</span></sc-if><b>{{o.t}}</b><p>{{o.d}}</p><div class="al-o-a">'
            '<sc-if value="{{o.rec}}" hint-placeholder-val="{{ false }}">' + btn('{{o.cta}}', '{{o.href}}', 'sm') + '</sc-if>'
            '<sc-if value="{{o.plain}}" hint-placeholder-val="{{ true }}"><a class="ds-link" href="{{o.href}}">{{o.cta}}</a></sc-if></div></div></sc-for></div>')
def coin(lg=False):
    return '<span class="dlp-c%s" aria-hidden="true"></span>' % (' dlp-lg' if lg else '')

WAVE = '/_blob/3d4d999db1912d0cb0084365c58434d3'
AUR_CSS = '.aur{position:relative;isolation:isolate;overflow:hidden;background:#0B1433}\n.aur > .aur-c{position:absolute;inset:0;width:100%;height:100%;z-index:-1;pointer-events:none;border-radius:inherit}\n.aur-off{background:#0B1433 url(' + WAVE + ') center / cover no-repeat}\n.aur.aur-lt,.aur-off-lt{background:linear-gradient(160deg,#F6F9FF,#E4ECFF)}'
AURORA_JS = open(os.path.join(HERE, 'aurora.js')).read().rstrip() + """
  aurScan() {
    var self = this, q = 0;
    var go = function () { q = 0; document.querySelectorAll('.aur').forEach(function (el) { if (!el.__aurC || el.__aurC.parentNode !== el) { if (el.__aur) el.__aur(); el.__aur = self.auroraMount(el); } }); };
    go();
    if (!this._aurMo && window.MutationObserver) { this._aurMo = new MutationObserver(function () { if (!q) q = requestAnimationFrame(go); }); this._aurMo.observe(document.body, { childList: true, subtree: true }); }
  }"""
