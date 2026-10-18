# Credalio · project rules (read before every change)

## How we work
- The designer directs and Claude builds. Keep chat replies SHORT; if the designer says "tldr", the reply was too long.
- Give complete, honest answers up front, including what is missing or not done. Never say "enough" without listing what is not covered.
- Commit and push after each change (`git push -u origin <current branch>`).
- Start each session by reading `docs/link3-plan.md`, which says what's done and what's next. Update it at the end of each batch.
- Full build log (every generator, blob id, past decision, by topic): see `docs/history.md` for how to open it. Grep it for details; never read it whole.

## Project
- **Link 1 (phase 1) is DELIVERED** (2026-10-14).
  - Canvas: https://claude.ai/artifact/Xq1VzSNgkrxnjsEeHbpAZq (local copy `design/canvas/project/`).
  - Handoff: `design/handoff/` (README, tokens, assets, developer package zip, screenshots zip, screen book PDF, developer guide PDF).
  - Don't change Link 1 unless the designer asks.
  - 2026-10-16: Log in + password reset added at the top of page p1 (CR-LOG-001 a–d, 002 b, 003 b–c; `design/generator/log1016.py` + `log1016_canvas.py`); onboarding "Log in" buttons → CR-LOG-001. The handoff zips/PDFs predate this.
  - 2026-10-16: sign-up + log-in illustration = `design/illustrations/auth-scene.webp` (blob `/_blob/2f4b6a89779043fb2ec851f8050aa46a`) as the bottom `.ob-scene` on ONB-003 (+003e/003d), ONB-003c (+003ce) and every CR-LOG page (`auth1016.py`); 003b inbox and 003v confirmed keep their own. "Welcome back." has the waving hand.
  - 2026-10-17: CR-ONB-001L / 001V (Learning / Validation coming soon, client WTusAd9o3fJn711spDqBsJ) = `dc-import CR-ONB-002S variant=learn|validate` (002S is now one source; all three use the same coming-soon illustration, designer 2026-10-17); ONB-001 Continue: Learner → 001L, Validator → 001V (`soon1017.py`).
- **Link 3 is NEXT** (designer 2026-10-14; the old Link 2 is dropped).
  - Client Link 3 prototype: https://claude.ai/artifact/Mg8o83iNa9x4ov1FxivdEW
  - Our Studio canvas (most Studio screens already designed): https://claude.ai/artifact/CzyHQrVg4MbHzgqsSeZwY9 (local copy `design/canvas2/project/`).
  - Plan: `docs/link3-plan.md`.
  - **Scope:** skip anything below the client's "DO NOT DESIGN ANYTHING BELOW THIS NOTE" (all PRG/COH cohort screens) and the "DO NOT DESIGN THIS ROW" retired payouts. Mapping: `docs/link3-map.md`.
- **Client reference** (content source only, about 98% correct): `reference/project/`. Screen list: `screens.md`.
- **Artifact file limit:** 512 files per canvas version. Check the count before adding boards.

## Goal (never lose this)
- DESIGN, DON'T COPY. The client prototype is a content source only. For every screen, work out its job and invent the clearest, most efficient layout. Never reuse the client's layout.
- Clean, modern, world-class: simple, premium, calm, youthful, intelligent. Theme: "the feeling of becoming".
- Copy is warm, short, human and honest, and reads like a story. Introduce concepts only when needed. UK spelling (Centre, licence), but "Organization" with a z. Avoid "teach/teacher" in creator copy.

## Look
- **Colour:** white background; Google Sans 400/500/600; navy `#0B1433` text; one cobalt accent `#1652F0` (hover `#0E3BB8`).
  - Soft blues `#EAF0FF` / `#F5F8FF`; app background `#F7F9FD`.
  - Secondary text `#3A4566` / `#4A5578` / `#5B6582`; faded labels `#8A93AD`.
  - Borders `#E6EAF3` / `#D6DDEE` / `#CBD3E6`.
  - Success `#0F6B45` (soft `#E7F5EE`); error border `#D92D20`, error text `#B42318`.
- **Weights:** tags, chips and pills always 500, never bold. 600 is only for buttons, headings and key values.
- **Buttons:** pills; the primary is a cobalt pill with a white circle arrow. One primary action per screen.
- **Cards:** radius 16–22 with 1.5px borders.
- **Selected options:** soft blue fill + cobalt border + check, radius 14. They must never look like the primary button.
- **Status colours:** green = complete, cobalt = in progress, amber = action needed, grey = not started / declined / in review. No rainbow colours and no emojis.
- **No screen-ID eyebrows.** Small labels above headings use `#8A93AD` (or cobalt).
- **Creio** (the AI usage unit, never "AI Tokens") is always GOLD: coin, `#FFF1CF→#FFFAEB` background, `#F4D98E` border, brown text. **Credits** (the wallet) are not Creio: cobalt "C" coin.
- **Nova** (the Copilot) cards and bands always use the profile-bg gradient (`/_blob/d268046654a4206d2a726e62005bcc59`, `.nova-card`). Characters come from the designer's images: Nova, Maya, Alex, Sage (blob ids in history).
- **Explanations** go in an info tooltip (`design/generator/tipx.py`: navy bubble, ⓘ), not in extra paragraphs. Never repeat what the H1 already says.
- **Top ambient glow** is status-coloured (green success, amber action, cobalt normal, grey declined / in review).
- **Cobalt line/path** is the progress motif.
- **Nova thinking state** (designer 2026-10-18): before every AI reply show `.nv-think` (spinning cobalt ring orb + shimmering status line that steps through what Nova is doing, ~2–3 s), then type the reply. Never a bare caret or three dots. Source: `design/generator/think1018.py` (ONB-006, ONB-007, CREATE-002A).
- **Outcome screens** (success, pending, action, failed) use the ONE standard `ko-*` layout from `CR-KYC-003`:
  - order: emblem → status pill → H1 → sub → card(s) / Next for you → CTA → small links
  - success screens add confetti (`confetti.py` / `conf1013c.py`)

## Layout
- **One responsive source file per screen.** Mobile/laptop boards only `dc-import` it.
- **States are variants** of one source (`dc-import name=… variant=…`, `renderVals()` / `<sc-if>`).
- **Breakpoints:** about 1080, 960 (sidebar becomes a drawer), 760/860. Touch targets ≥44px; small text links get an invisible 44px `::after` hit area on mobile.
- **Dashboard / Studio shell:** `design/generator/dash.py`.
  - 264px white sidebar and a sticky top bar (search, gold Creio pill, help, bell, avatar); content on `#F7F9FD` with white r20 cards.
  - Pages may scroll.
  - Header row: H1 left plus a slim strip right. One full-width focus card. No two-column split with small side cards.
- **Focus mode** (creation, tasks, flows) has no sidebar: slim bar with close, title and progress; sticky bottom actions on mobile.
- **Mobile is efficiency first:**
  - H1 24, body 14–15; compact rows; no card-inside-card heroes.
  - ≥28px under bars; full-width primary buttons; one CTA per view.
  - Swipeable chip rows; accordions for secondary content.
- **Desktop:** use the space well. No half-empty rows or needless line breaks.
- **Onboarding only:** no scroll at 1440×820 and 1280×720.
- **Animations** only run in canvas Play mode. That's not a bug.

## Canvas workflow
- **Always re-read the live canvas files before editing** (the designer edits in place) and sync them into the repo.
- **Publish** with the Artifact tool: `root=design/canvas2/project` (or `canvas/project`), `file_path=canvas.json`, plus a `files` list. A null value deletes a file. Image uploads return `/_blob/<id>` and the code references those ids, never base64.
- **Generators** live in `design/generator/` (see `docs/history.md` for which build script made what). Copy one to the scratchpad to run it. Many later copy edits were made directly in the canvas, so **never re-run an old build script over live files**; patch the live files instead.
- **After every batch:**
  - run `design/tools/audit.py` + `cleancss.py` (no unused CSS, no build comments or dates in code)
  - check that no page errors, broken images or broken links remain
  - link every new button to its destination (unwired = `href="#"`)
  - update `screens.md` and `docs/link3-plan.md`
- **Delivery tools** (reuse them for Link 3):
  - `design/tools/package.py`: offline developer package zip
  - `renderall.js` / `cmp.py` / `prep.sh`: render and pixel-compare
  - screen book + developer guide PDFs: HTML → Chromium `page.pdf`
