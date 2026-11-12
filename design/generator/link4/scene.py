"""Minimal people-scene illustration (Link 1 auth-scene, uploaded to this canvas) along the empty bottom of the short
success screens. Post-step run by layout.py: adds the .ko-scene layer to the listed pages and its CSS to their sources.
"""
import os, re

BLOB = '/_blob/7aeeb145ff0fc4be2a74ed8f5683de98'
# source: (pages, left offset of the content column on desktop)
PAGES = {
    'Collab': (['sent', 'rm-done', 'rm-review'], 264), 'Collab2': (['a-sent', 'a-wdn'], 264), 'Collab3': (['o-a'], 264), 'Collab4': (['sub'], 264),
    'Manage2': (['p-done'], 264), 'Manage3': (['a-done'], 264),
    'Unpublish': (['done'], 0), 'Publish': (['live'], 0),
}
CSS = ('main:has(.ko-scene),.tk-root:has(.ko-scene){isolation:isolate}\n'
       '.ko-scene{position:fixed;left:%dpx;right:0;bottom:0;z-index:-1;height:min(34vh,280px);background:url(' + BLOB + ') 50%% 100%% / cover no-repeat;'
       'mix-blend-mode:multiply;pointer-events:none;-webkit-mask-image:linear-gradient(180deg,transparent,#000 30%%);mask-image:linear-gradient(180deg,transparent,#000 30%%);animation:obIn .8s ease .3s both}\n'
       '@media (max-width: 960px){.ko-scene{left:0;height:180px}}\n')
TAG = '<div class="ko-scene" aria-hidden="true"></div>'


def run(out):
    for src, (pages, left) in PAGES.items():
        p = os.path.join(out, src + '.dc.html')
        s = open(p).read()
        n = 0
        for pg in pages:
            key = pg.replace('-', '_')
            m = re.search(r'<sc-if value="\{\{[ps]_%s\}\}"[^>]*>' % re.escape(key), s)
            if not m:
                continue
            nxt = re.search(r'<sc-if value="\{\{[ps]_', s[m.end():])
            block = s[m.end():m.end() + (nxt.start() if nxt else len(s))]
            if 'ko-scene' in block:
                continue
            s = s[:m.end()] + TAG + s[m.end():]
            n += 1
        if n and '.ko-scene{' not in s:
            i = s.rindex('</style>')
            s = s[:i] + CSS % left + s[i:]
        if n:
            open(p, 'w').write(s)
