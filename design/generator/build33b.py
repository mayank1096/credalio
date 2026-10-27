# build33b: CR-AI-001 Copilot panel (CP-001/002) = LIVE CR-DASH-NEW with Nova's side panel open (mobile: full-height sheet).
# usage: python3 build33b.py <dir>   (only writes CR-AI-001*.dc.html)
import re, sys, os
P = sys.argv[1]
def rd(f): return open(os.path.join(P, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(P, f), 'w', encoding='utf-8').write(s)
def ic(paths, w=20, sw=1.9):
    return f'<svg width="{w}" height="{w}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>'
def nova(px):
    return (f'<span class="cp-av" aria-hidden="true" style="width: {px}px; height: {px}px"><img src="/_blob/b8f0756720795e1bd3b02e9c2655cb25" alt="" '
            'style="position: absolute; left: -87.50%; top: -57.81%; width: 294.06%; max-width: none; height: auto; mix-blend-mode: multiply"></span>')
X = ic('<path d="M7 7l10 10M17 7 7 17"></path>', 18, 2.2)
HIST = ic('<path d="M3 12a9 9 0 1 0 3-6.7L3 8"></path><path d="M3 3v5h5"></path><path d="M12 7v5l3 2"></path>', 18, 2)
SEND = ic('<path d="M12 19V5"></path><path d="m5 12 7-7 7 7"></path>', 18, 2.4)
PIN = ic('<rect x="3" y="4" width="18" height="16" rx="3"></rect><path d="M3 9h18"></path>', 14, 2)

s = rd('CR-DASH-NEW.dc.html')
CHIPS = ['Draft a course from my idea', 'Help me pick a format', 'What happens before publishing?']
panel = ('<div class="cp-ov" aria-hidden="true"></div>'
         '<aside class="cp" role="dialog" aria-label="Nova, your Copilot"><div class="cp-fx" aria-hidden="true"></div>'
         '<header class="cp-h">' + nova(40) + '<span class="cp-n"><b>Nova</b><span>Your Copilot</span></span>'
         '<button type="button" class="cp-ib" aria-label="Past conversations">' + HIST + '</button>'
         '<a href="CR-DASH-NEW.dc.html" class="cp-ib" aria-label="Close">' + X + '</a></header>'
         '<div class="cp-b"><span class="cp-ctx">' + PIN + 'Looking at your Dashboard</span>'
         '<div class="cp-m">' + nova(28) + '<div class="cp-bub"><p>Hi Ada. Tell me your idea in a sentence and I’ll sketch a first draft for you to shape.</p>'
         '<p>Not sure which format fits? I can help you choose.</p></div></div></div>'
         '<footer class="cp-f"><div class="cp-ch">' + ''.join(f'<button type="button">{c}</button>' for c in CHIPS) + '</div>'
         '<label class="cp-in"><span class="sr-only">Ask Nova</span><input placeholder="Ask Nova anything…"><button type="button" class="cp-go" aria-label="Send">' + SEND + '</button></label>'
         '<span class="cp-cost"><i aria-hidden="true"></i>About 150 Creio per reply</span></footer></aside>')
assert s.count('</x-dc>') == 1
s = s.replace('</x-dc>', panel + '\n</x-dc>', 1)
CSS = """
/* CR-AI-001 Copilot panel */
.cp-ov{position:fixed;inset:0;z-index:30;background:rgba(11,20,51,.18)}
.cp{position:fixed;z-index:31;top:0;right:0;bottom:0;width:420px;max-width:100vw;box-sizing:border-box;display:flex;flex-direction:column;background:#FFFFFF;border-left:1.5px solid #E6EAF3;box-shadow:-24px 0 64px rgba(11,20,51,.14);overflow:hidden;font-family:'Google Sans','Google Sans Text','Helvetica Neue',system-ui,sans-serif;color:#0B1433}
.cp-fx{position:absolute;left:0;right:0;top:0;height:180px;pointer-events:none;background:linear-gradient(90deg,rgba(22,82,240,0) 0%,rgba(22,82,240,.16) 18%,rgba(140,175,255,.26) 34%,rgba(22,82,240,0) 50%,rgba(22,82,240,.16) 68%,rgba(140,175,255,.26) 84%,rgba(22,82,240,0) 100%);background-size:200% 100%;-webkit-mask-image:linear-gradient(180deg,#000 0%,rgba(0,0,0,.5) 45%,transparent 100%);mask-image:linear-gradient(180deg,#000 0%,rgba(0,0,0,.5) 45%,transparent 100%);animation:fxFlow 10s linear infinite}
@keyframes fxFlow{from{background-position:0% 0}to{background-position:200% 0}}
@media (prefers-reduced-motion: reduce){.cp-fx{animation:none}}
.cp-h{position:relative;display:flex;align-items:center;gap:12px;padding:20px 16px 16px 22px}
.cp-av{position:relative;display:block;flex-shrink:0;border-radius:50%;overflow:hidden;background:#EAF0FF}
.cp-n{flex-grow:1;display:flex;flex-direction:column;gap:1px}.cp-n b{font-size:17px;font-weight:600}.cp-n span{font-size:13px;color:#5B6582}
.cp-ib{width:40px;height:40px;border-radius:50%;border:0;background:transparent;color:#4A5578;display:flex;align-items:center;justify-content:center;cursor:pointer}
.cp-ib:hover{background:rgba(11,20,51,.06)}
.cp-b{position:relative;flex-grow:1;display:flex;flex-direction:column;justify-content:flex-end;gap:18px;padding:0 22px 20px 22px;overflow-y:auto}
.cp-ctx{align-self:center;display:inline-flex;align-items:center;gap:6px;height:28px;padding:0 12px;border-radius:999px;background:#F1F3F8;color:#5B6582;font-size:12.5px;font-weight:500}
.cp-m{display:flex;align-items:flex-end;gap:10px}
.cp-bub{padding:14px 16px;border-radius:18px 18px 18px 6px;background:#F5F8FF;border:1.5px solid #E1E9FF}
.cp-bub p{margin:0;font-size:14.5px;line-height:1.55}.cp-bub p + p{margin-top:8px}
.cp-f{position:relative;padding:14px 22px 18px 22px;border-top:1.5px solid #F0F2F8;display:flex;flex-direction:column;gap:12px}
.cp-ch{display:flex;gap:8px;overflow-x:auto;margin:0 -22px;padding:0 22px;scrollbar-width:none}.cp-ch::-webkit-scrollbar{display:none}
.cp-ch button{flex-shrink:0;height:36px;padding:0 14px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:inherit;font-size:13.5px;font-weight:500;color:#0B1433;cursor:pointer;white-space:nowrap}
.cp-ch button:hover{border-color:#1652F0;background:#F5F8FF}
.cp-in{display:flex;align-items:center;gap:8px;height:52px;padding:0 6px 0 18px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF}
.cp-in:focus-within{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.cp-in input{flex-grow:1;min-width:0;border:0;outline:none;font-family:inherit;font-size:15px;color:#0B1433;background:transparent}
.cp-go{width:40px;height:40px;flex-shrink:0;border-radius:50%;border:0;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center;cursor:pointer}
.cp-cost{display:inline-flex;align-items:center;gap:7px;align-self:center;font-size:12.5px;color:#6B4E16}
.cp-cost i{width:14px;height:14px;border-radius:50%;background:linear-gradient(135deg,#FFE9A3,#F6C343 45%,#D08A12)}
@media (max-width: 960px){
.cp-ov{display:none}
.cp{width:100%;border-left:0;box-shadow:none}
.cp-h{padding:14px 10px 12px 16px}
.cp-b{padding:0 16px 18px 16px}
.cp-f{padding:12px 16px 16px 16px}
.cp-ch{margin:0 -16px;padding:0 16px}
}
"""
i = s.rfind('</style>', 0, s.find('</helmet>'))
s = s[:i] + CSS + s[i:]
s = re.sub(r'<title>.*?</title>', '<title>Credalio · Nova, your Copilot</title>', s, count=1)
wr('CR-AI-001.dc.html', s)
wm = rd('CR-SET-008-Mobile.dc.html').replace('<dc-import name="CR-SET" variant="signin"', '<dc-import name="CR-AI-001"').replace('CR-SET-008', 'CR-AI-001')
assert 'name="CR-AI-001"' in wm
wr('CR-AI-001-Mobile.dc.html', wm)
print('build33b ok'); print('CR-AI-001.dc.html CR-AI-001-Mobile.dc.html')
