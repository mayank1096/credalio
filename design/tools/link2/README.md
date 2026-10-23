# Link 2 delivery build (run from design/)
1. `python3 tools/package_link2.py <support.js> <vendor dir> <fonts dir> <blobmap.json>` → handoff/link2/credalio-link2-developer-package.zip (+ handoff/build/rows.json)
   blobmap.json maps each canvas image id to a file in illustrations/ (match by sha256 from the canvas asset listing).
2. Unzip the package to a scratch folder; `node pkgcheck.js <pkg dir>` (offline check: errors, missing files).
3. `node shots.js <pkg dir> rows.json <out>/credalio-link2-screenshots` → numbered full-page JPGs + shots.json; zip them.
4. `python3 book.py <dir with shots/>` → shots/book.html; `node pdf.js <shots dir> book.html <out.pdf> l` → screen book.
5. guide.html (copy into the shots dir with the wordmark + font) → `node pdf.js <dir> guide.html <out.pdf> p`.
6. Check: no "claude|anthropic" in the folder, the unzipped zips or the PDFs.
