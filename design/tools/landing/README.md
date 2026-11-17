# Landing delivery build (run from design/)
1. `python3 tools/landing/package_landing.py <support.js> <vendor dir> <fonts dir> <blobmap.json>` → handoff/landing/credalio-landing-developer-package.zip (+ handoff/build/rows.json). Sections = the 5 canvas columns, groups = the rows.
   blobmap.json maps each canvas image id to a file in illustrations/ (match by sha256 from the canvas asset listing).
2. Unzip the package; `node tools/landing/pkgcheck.js <pkg dir>` (offline: errors, missing files).
3. `node tools/landing/shots.js <pkg dir> rows.json <out>/credalio-landing-screenshots` → numbered full-page JPGs + shots.json.
   Scrolls each page first (scroll reveals), captures in pieces (long mobile pages stay 2x) and replaces the landing's pinned
   story track with one frame per stage (stitch.py). A re-run resumes: existing JPGs are skipped. Re-encode at quality 70 before zipping.
4. `python3 tools/landing/book.py <dir with shots/>` → shots/book.html (long pages split into parts);
   `node tools/landing/pdf.js <shots dir> book.html <out.pdf> l` → screen book.
5. guide.html (+ wordmark + GoogleSans-latin.woff2) → `node tools/landing/pdf.js <dir> guide.html <out.pdf> p`.
6. `python3 tools/landing/pdfmeta.py <pdf> "<title>"` on both PDFs (title, no browser user agent).
7. Check: no AI tool or vendor names in the folder, the unzipped zips or the PDFs.
