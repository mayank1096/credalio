# stitch.py <meta.json> <out.jpg>: joins the page pieces; if the page has a pinned story, its track is replaced by the story frames.
import json, sys
from PIL import Image
m = json.load(open(sys.argv[1])); k = m['dpr']
parts = [Image.open(c).convert('RGB') for c in m['chunks']]
W = parts[0].width; page = Image.new('RGB', (W, sum(p.height for p in parts)), '#FFFFFF'); y = 0
for p in parts: page.paste(p, (0, y)); y += p.height
if m['story']:
    t, h = m['story']['top'] * k, m['story']['h'] * k
    frames = [Image.open(f).convert('RGB') for f in m['frames']]
    fh = sum(f.height for f in frames)
    out = Image.new('RGB', (W, page.height - h + fh), '#FFFFFF')
    out.paste(page.crop((0, 0, W, t)), (0, 0)); y = t
    for f in frames: out.paste(f, (0, y)); y += f.height
    out.paste(page.crop((0, t + h, W, page.height)), (0, y)); page = out
page.save(sys.argv[2], quality=84)
