# conf1013c: swap confetti markup + CSS (v2 fall-away -> v3 natural physics). usage: python3 conf1013c.py <dir> <old_confetti.py> <v2_confetti.py>
import sys, os, importlib.util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import confetti as N
def load(p):
    spec = importlib.util.spec_from_file_location(os.path.basename(p)[:-3], p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
OLD, V2 = load(sys.argv[2]), load(sys.argv[3])
P = sys.argv[1]; out = []
for f in sorted(os.listdir(P)):
    if not f.endswith('.dc.html'): continue
    p = os.path.join(P, f); s = open(p, encoding='utf-8').read()
    if OLD.CONF in s:
        assert V2.CSS in s, f
        s = s.replace(OLD.CONF, N.CONF, 1).replace(V2.CSS, N.CSS, 1); open(p, 'w', encoding='utf-8').write(s); out.append(f)
print('conf1013c', len(out)); print(' '.join(out))
