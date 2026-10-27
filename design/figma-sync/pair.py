import sys
from PIL import Image
keys=sys.argv[2:]; out=sys.argv[1]; ims=[]
for k in keys:
    w=Image.open(f'out/{k}/_full.png').convert('RGB'); w=w.resize((w.width//2,w.height//2))
    f=Image.open(f'cmp/{k}.png').convert('RGB').resize(w.size)
    ims+= [w,f]
W=sum(i.width+8 for i in ims); H=max(i.height for i in ims)
c=Image.new('RGB',(W,H),'red'); x=0
for i in ims: c.paste(i,(x,0)); x+=i.width+8
c.save(out)
