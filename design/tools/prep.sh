# prep.sh <srcdir> <rootdir>
rm -rf "$2"; mkdir -p "$2"; B=/tmp/claude-0/-home-user-credalio/ac3a299a-59c2-576d-8df6-3f8bf66b6d40/scratchpad/clean/base
ln -s $B/_blob "$2/_blob"; ln -s $B/vendor "$2/vendor"; cp $B/support.js "$2/"
for f in "$1"/*.dc.html; do sed 's#<script src="\(\./\)\?support.js#<script src="./vendor/react.js"></script><script src="./vendor/react-dom.js"></script>&#' "$f" > "$2/$(basename "$f")"; done
