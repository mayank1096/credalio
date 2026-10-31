import re
s=open('design/canvas3/project/Landing.dc.html').read()
d=open('design/demo/landing/index.html').read()
M={'bbd33f9ce984750cfa6abea29b7528de':'hero-wide-1600','e6967fe2b7132bfebac7f5321a83e34a':'hero-wide-2800','130e1caa8d9077a42c20869730d8434e':'hero-1024','59cb50235121b8ea88ff562a72bc1e63':'hero-1536','41ff0a4f2d85266cb38bf7eb56bfd49e':'footer-1440','eb2e20d6cbd3a76832bd7baba973357a':'footer-2000','8d1041b4dd08fd7406351fcbbd98b97a':'learner-700'}
for k,v in M.items(): s=s.replace('/_blob/'+k,'img/%s.webp'%v)
s=s.replace('/_blob/8ef03b46dfef084b5a8501cb87efcad2','img/pricing-clouds.webp').replace('/_blob/6d413632692b3ddab8bd438b7e97a664','img/pricing-clouds-m.webp')
s=s.replace('/_blob/3d4d999db1912d0cb0084365c58434d3','img/dark-card-wave.webp')
s=s.replace('/_blob/8acabcff7ece53343d63205e8b7321a2','img/wordmark.png').replace('/_blob/f81e36d31295a0d0737959589ec1abd4','img/mark.png')
assert '_blob' not in s
av=lambda x:x.replace('.webp','.avif')
hp=re.search(r'<picture><source media="\(min-width: 761px\)" srcset="([^"]+)" sizes="100vw"><img class="lh-figure" src="[^"]+" srcset="([^"]+)" sizes="180vw"',s)
s=s.replace('<picture><source media="(min-width: 761px)" srcset="%s"'%hp.group(1),'<picture><source media="(min-width: 761px)" type="image/avif" srcset="%s" sizes="100vw"><source media="(min-width: 761px)" type="image/webp" srcset="%s"'%(av(hp.group(1)),hp.group(1)),1)
s=s.replace('<img class="lh-figure"','<source type="image/avif" srcset="%s" sizes="180vw"><img class="lh-figure"'%av(hp.group(2)),1)
fm=re.search(r'<img class="ft-img" src="[^"]+" srcset="([^"]+)" sizes="([^"]+)"[^>]*>',s)
s=s.replace(fm.group(0),'<picture><source type="image/avif" srcset="%s" sizes="%s">%s</picture>'%(av(fm.group(1)),fm.group(2),fm.group(0)))
lm=re.search(r'<img class="ac-learner"[^>]*>',s).group(0)
s=s.replace(lm,'<picture><source type="image/avif" srcset="img/learner-700.avif">%s</picture>'%lm)
head=d[d.index('<title>'):d.index('<script src="./support.js">')]
s=s.replace(s[s.index('<title>'):s.index('<script src="./support.js">')],head)
open('design/demo/landing/index.html','w').write(s)
