import sys
start=int(sys.argv[1]); ids=sys.argv[2].split(',')
S=[l.split()[1] for l in open('slots.txt')][start:start+len(ids)]
open('ub.txt','w').write(''.join(f'{k} https://mcp.figma.com/mcp/upload/{u}/submit?scaleMode=FILL\n' for k,u in zip(S,ids)))
