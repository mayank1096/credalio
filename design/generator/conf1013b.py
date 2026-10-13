# conf1013b: swap the static confetti CSS for the fall-away version (designer "confetti should not stuck anywhere"). usage: python3 conf1013b.py <dir>
import sys, os, importlib.util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from confetti import CSS as NEW
OLD = sys.argv[2] if len(sys.argv) > 2 else None
spec = importlib.util.spec_from_file_location('cold', OLD); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
P = sys.argv[1]; out = []
for f in sorted(os.listdir(P)):
    if not f.endswith('.dc.html'): continue
    p = os.path.join(P, f); s = open(p, encoding='utf-8').read()
    if m.CSS in s:
        open(p, 'w', encoding='utf-8').write(s.replace(m.CSS, NEW, 1)); out.append(f)
print('conf1013b', len(out)); print(' '.join(out))
