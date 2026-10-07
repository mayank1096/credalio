import sys
from PIL import Image
# side by side: web (left) vs figma (right), optional crop box x,y,w,h in css px
key=sys.argv[1]; out=sys.argv[2]
w=Image.open(f'out/{key}/_full.png').convert('RGB'); f=Image.open(f'cmp/{key}.png').convert('RGB')
f=f.resize((w.width//2,w.height//2)); w=w.resize((w.width//2,w.height//2))
if len(sys.argv)>3:
    x,y,cw,ch=map(int,sys.argv[3].split(',')); w=w.crop((x,y,x+cw,y+ch)); f=f.crop((x,y,x+cw,y+ch))
im=Image.new('RGB',(w.width*2+10,w.height),'red'); im.paste(w,(0,0)); im.paste(f,(w.width+10,0)); im.save(out)
