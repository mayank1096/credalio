# Link 4 delivery build (run from design/)
1. `python3 tools/link4/package_link4.py <support.js> <vendor dir> <fonts dir> <blobmap.json>` → handoff/link4/credalio-link4-developer-package.zip (+ handoff/build/rows.json). Sections group the canvas rows by batch; groups = the rows.
   blobmap.json maps each canvas image id to a file in illustrations/ (match by sha256 from the canvas asset listing).
2. Unzip the package; `node tools/link4/pkgcheck.js <pkg dir>` (offline: errors, missing files).
3. `node tools/link4/shots.js <pkg dir> rows.json <out>/credalio-link4-screenshots` → numbered full-page JPGs + shots.json.
   Scrolls each page first (scroll reveals), captures in pieces (long mobile pages stay 2x) and replaces the landing's pinned
   story track with one frame per stage (stitch.py). A re-run resumes: existing JPGs are skipped. Re-encode at quality 70 before zipping.
4. `python3 tools/link4/book.py <dir with shots/>` → shots/book.html (long pages split into parts);
   `node tools/link4/pdf.js <shots dir> book.html <out.pdf> l` → screen book.
5. guide.html (+ wordmark + GoogleSans-latin.woff2) → `node tools/link4/pdf.js <dir> guide.html <out.pdf> p`.
6. `python3 tools/link4/pdfmeta.py <pdf> "<title>"` on both PDFs (title, no browser user agent).
7. Check: no AI tool or vendor names in the folder, the unzipped zips or the PDFs.
