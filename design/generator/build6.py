exec(open('build5.py').read())
def strip_illus(n):
    p=P+n; s=open(p).read()
    a=s.index('<div class="ob-illus"'); b=s.index('</div>\n</x-dc>',a)
    s=s[:a]+s[b:]
    s=s.replace('</style>','@media (max-width: 960px){.ob-main{padding-top:28px !important}}\n</style>',1)
    open(p,'w').write(s)
strip_illus('CR-ONB-003c.dc.html'); strip_illus('CR-ONB-005.dc.html'); strip_illus('CR-ONB-005b.dc.html')
# 004: waving hand
WAVE='/_blob/e0846c8b6889064bed3e0b948cd9888a'
p=P+'CR-ONB-004.dc.html'; s=open(p).read()
old='>Nice to meet you.</h1>'; assert old in s
s=s.replace(old,'>Nice to meet you<img class="ob-wave" src="'+WAVE+'" alt="" aria-hidden="true" style="display: inline-block; width: 1.08em; height: 1.08em; margin-left: 0.2em; vertical-align: -0.16em"></h1>')
css='''@keyframes obWaveIn{0%{opacity:0;transform:translateY(10px) scale(.4) rotate(-30deg)}60%{opacity:1;transform:translateY(-2px) scale(1.12) rotate(8deg)}100%{opacity:1;transform:none}}
.ob-wave{transform-origin:70% 85%;animation:obWaveIn .7s cubic-bezier(.3,1.4,.5,1) .35s both}
@media (prefers-reduced-motion: reduce){.ob-wave{animation:none}}
</style>'''
s=s.replace('</style>',css,1); open(p,'w').write(s)
print('build6 done')
