# Canvas → Figma sync

Converts each canvas board (rendered DOM) into an editable Figma frame: auto-layout where the CSS layout maps cleanly, colour variables bound, text in Google Sans Flex, icons as vectors, images uploaded as PNG.

1. `extract.js <renderDir> <outDir> board.dc.html:WxH ...` — Playwright render, serialise the DOM (`ser.js`), capture image/complex-paint layers.
2. `plan.py` — runs `post.py` (layout inference, image trimming) and `gen.py` (one `use_figma` script per frame, `builder.js` runtime) for every board in `boards.txt`.
3. Run each `out/<board>/job_*.js` with `use_figma`, then upload `out/<board>/img/*.png` to the nodes tagged with shared plugin data `crd/img` (`up.py`).

Re-running a job replaces the frame of the same name.
