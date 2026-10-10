# Credalio — project rules (read before every change)

## Who / what
- Designer directs, Claude builds everything. Keep chat replies SHORT.
- Deliverable: developer-ready Figma (later). For now we design screens on the canvas:
  https://claude.ai/artifact/Xq1VzSNgkrxnjsEeHbpAZq (local copy: `design/canvas/project/`).
- Client reference (content source, ~98% correct): `reference/project/` (snapshot), screen list: `screens.md`.
- Order agreed: design a few screens to settle the look → then design system → then Figma.

## Goal (never lose this)
- DESIGN, DON'T COPY (designer, 2026-10-04): the client reference is a CONTENT source only. For every screen think as a world-class product designer: understand the job of the screen and invent the clearest, most efficient, unique layout. Never reuse the client's layout.
- Clean, modern, world-class UI/UX. Simple, premium, calm, youthful, intelligent.
- Theme: "the feeling of becoming". Copy reads like a story, never a forceful/compliance onboarding.
- Best possible copywriting: warm, short, human, honest. Introduce concepts only when needed.

## Approved direction (CR-ONB-001 "Who will you become next?")
- White background, Google Sans, navy #0B1433 text, cobalt #1652F0 single accent (hover #0E3BB8).
- Soft blues #EAF0FF / #F5F8FF; secondary text #3A4566 #4A5578 #5B6582; borders #E6EAF3 #D6DDEE #CBD3E6; success #0F6B45.
- Pill buttons; primary = cobalt pill with white circle arrow. Cards radius 16–18, 1.5px borders, soft blue ring when selected.
- Illustration "One Line, Four Futures" (designer v2 2026-10-10: `design/illustrations/main-scene-v2.webp`, blob `/_blob/877e6d93c070677634b4956192180989`, 2000×667, same layout as v1 so all path/fade overlays still align; old v1 blob `/_blob/bad84659fa9f24b3a7efb7e88696e531` must not be used — older generators still reference it). The glowing cobalt line = the AI guide; reuse it as the progress/path motif.
- The "Your Copilot lights the way" pill was REMOVED by the designer. Don't bring it back.

## Onboarding layout (approved 2026-10-02)
- Every onboarding step uses the CR-ONB-001 layout: header (logo left, Log in right), dashed 5-step tracker centred under it ("Step 1 of 5 · Your account"), centred content, illustration at the bottom.
- NO left side panel. Illustration on EVERY screen (desktop bottom; mobile under the tracker, panned to hero + Creator). Creator path lit. NO text tags/chips on the illustration (removed by designer).
- 003c password, 005 your field, 005b topics: no main illustration; instead the designer's soft campus scene (2026-10-10, `design/illustrations/campus-bg.webp`, blob `/_blob/6acc9dd1cd600c17d2fd6381a3069aaa`) as a bottom layer `.ob-scene` behind content (root `isolation:isolate`, z -1; mobile 240px tall, 250% size). 006 + 007 Copilot: Nova character, no scene.
- 004 H1 uses the animated waving hand (Noto animated emoji, CC BY 4.0, `design/illustrations/wave.webp`, blob `/_blob/e0846c8b6889064bed3e0b948cd9888a`).
- Copilot characters (designer, 2026-10-06; replaces old copilot-avatars sprite): `design/illustrations/copilot-{nova,maya,alex,sage}.webp` (941×1672 each), blobs Nova `/_blob/b8f0756720795e1bd3b02e9c2655cb25`, Maya `/_blob/0539eaee91dd97c09ad321718b4b2947`, Alex `/_blob/180b8d793cf8025b7bf4a7efeb6da0a2`, Sage `/_blob/e77858d41b6ddf496fcf2ad82ab9d64a`. Crops in `design/generator/cpx.py` (stage + head). 006 swaps figure by name + head avatars in chips; 007 shows Nova; NOVA_AV (dashboard/chat/008) = Nova head; DASH hero desktop shows Nova standing.
- 005b profile card bg = designer image `design/illustrations/profile-bg.webp` (blob `/_blob/d268046654a4206d2a726e62005bcc59`). Nova (006/007) has NO blue floor line.
- Tags, chips and pills use MEDIUM weight (500), never bold. Bold (600) is for buttons, headings and key values only.
- Selected chips/options must never look like the primary button: soft blue fill + cobalt border + check, radius 14 (buttons are solid cobalt pills).
- Some steps have their OWN illustration (designer-supplied, in `design/illustrations/`): 003 create-account, 003v email-confirmed (+ confetti), 002S coming-soon. Others use the main scene.
- Shared frame generator: `design/generator/gen2.py` (+ build2.py / build3.py per batch; copy to scratchpad to run).

## Creator Studio (dashboard) shell (2026-10-04)
- Generator `design/generator/dash.py` (SHELL/WRAP/NOVA_AV/icons) + `build8.py`/`build8b.py` (v2 designs; build7 = superseded v1). Sidebar 264px white (sentence-case group labels, line icons, active = soft blue), sticky top bar (search, Nova token pill, help, bell, avatar), content bg #F7F9FD, white cards r20.
- Mobile ≤960: sidebar becomes drawer (hamburger), search hidden. Dashboard pages MAY scroll (no-scroll rule is onboarding only).
- Nova avatar = head crop of the Nova character (NOVA_AV). No emojis, no screen-ID eyebrows, no rainbow colours.
- MOBILE = efficiency first: smaller type (H1 24, body 14–15), compact rows, no tall decorative blocks, primary CTA visible without scrolling where possible, secondary info collapsible (toggle) or hidden; horizontal-scroll chip rows.
- The AI usage unit is "Creio" (client 2026-10-10; never "AI Tokens"/"AI balance"). Creio always shown GOLD (incl. top-bar pill: coin + "20K Creio") (coin, #FFF1CF→#FFFAEB bg, #F4D98E border, brown text). 008 = "Ada, you’re a Creator." reveal (no step tracker); profile card hangs on a lanyard and sways (pendulum).
- Creation flows (002A/002Ab) use FOCUS MODE (no sidebar): slim top bar (close, title, progress, gold tokens). Chat = centred column, messages bottom-anchored, composer docked at bottom with suggestion chips; blueprint as right pane (mobile: bottom sheet). Review = the course rendered as a real page with per-part icon tools + sticky review rail (mobile: fixed bottom bar). Generator `build9.py`.
- Variant screens use one source + prop (e.g. 002Ab = `dc-import CR-CREATE-002A variant="proposal"`).

## Designer feedback log (ALWAYS apply to every new screen)
- Never copy the client layout; rethink each screen's job and make it efficient, unique and clean.
- Mobile: no card-inside-card heroes (content runs edge to edge on the page bg), breathing room under bars/trackers (≥28px), full-width primary buttons, compact type, one primary CTA per view (no duplicate CTAs), swipeable chip/pill rows instead of wrapped 2-line boxes, collapsible lists (accordion) for secondary content.
- Mobile space under the top bar: dashboard pages ds-main padding-top 12px; focus/player/task screens ≥30–40px. Never let content stick to the bar.
- Desktop: use space well (no needless line breaks, no half-empty rows); one clear primary action per screen.
- Tags/chips/pills/status pills = weight 500. Selected ≠ primary button. Tokens always gold. No emojis, no screen-ID eyebrows, no rainbow colours (status: green complete, cobalt in progress/review, amber action required, grey not started).
- Characters: use the designer's Copilot images (Nova etc.), never the old main-scene crops for people. Chat-like screens: messages bottom-anchored, composer at the bottom; a soft blue gradient flowing sideways across the top (fxFlow) is the "Nova is here" ambient motif.
- Small labels/eyebrows above headings (section labels, "Next for you", "Question 1 of 2") use faded #8A93AD (or cobalt) so they never match the sub-heading colour.
- Any Nova card/band (suggestions, help, "Ask Nova") ALWAYS uses the profile-bg gradient background (`/_blob/d268046654a4206d2a726e62005bcc59`, `.nova-card`).
- Top ambient glow (radial fade under the bar) is status-coloured: green = success, amber/brown = error/action needed, cobalt = normal/in progress, grey = declined.
- Cobalt line/path = progress motif (readiness gates, orientation journey, setup route).
- Orientation flow (ORI-002…007) = LEARNING PLAYER in focus mode (`design/generator/build11.py` PLAYER): slim top bar (close, module, step segments), left step outline (desktop), reading column 720, fixed bottom bar (Previous / Next). Checks give instant feedback (green correct / amber not quite), Next stays disabled until all correct.
- Readiness TASKS (KYC, credentials, policies…) = focus-mode TASK shell (`build12.py` TASK): close → readiness, "Readiness · task n of 5", green "Secure · encrypted" pill. KYC SDK screens = one source CR-KYC-002 (variant photos / liveness) with a left tips column + our-styled Sumsub panel (stepper Document → Photos → Liveness → Submit); mobile: panel full-bleed, sticky Back/Continue bar.
- Readiness/Orientation/Creator Centre/002B generator: `design/generator/build10.py` (RDY-001s = `dc-import CR-RDY-001 variant="new"`).
- KYC outcomes: `build13.py` — CR-KYC-003 one source, variants review / verified / action / failed (= 003 / 004 / 005 / 006); KYC-002d = CR-KYC-002 variant "review". build13 only writes its own files.
- Credentials task (CRED-001…002c): `build14.py` — focus-mode TASK shell ("task 2 of 5"), left side + right panel; CR-CRED-002 one source, variants types / degree / aws / badge (= 002 / 002a / 002b / 002c). build14 only writes its own files.
- CRED-002d/e/f + CRED-003/003b: `build15.py` — PATCHES live CR-CRED-002 in place (adds variants lic / work / other = 002d / 002e / 002f; asserts if already patched) and writes CR-CRED-003 (copied from CR-KYC-003; variants verified / review = 003 / 003b) + wrappers. Canvas edited AFTER build15 (2026-10-10 cleanup: form header row removed, duplicate hints removed, footer note wraps, 003 badge/003b subtitle removed) — do not re-run.
- Client update 2026-10-08 (edited in canvas files directly, NOT in gen2): ONB-001 roles = Learner / Creator / Validator / Organisation (4th = set up an organisation); ONB-002 = 2 options Independently / Join an institution (+ "join later from My Organisations"); 002S = institution coming soon.
- Client copy v2 (2026-10-08, from client artifact SnCSyjk7mfZGdvxmL1dtxw) applied by string replace directly in canvas files (NOT in generators). Re-running gen2/build8/build9/build10/build11/build12/build13/build14 would revert copy.
- Client feedback 2026-10-10 (applied via `design/generator/fb1010.py`, copy only): unit = Creio; row buttons inside a titled row stay short (Start, Resume, Review, Set up, Fix now), standalone buttons specific ("Fix my credentials"); ONB card "Organization", 002 options sentence case; timelines hedged with "usually"; IDENTITY pages say "Powered by Sumsub" (neutral grey pill, no lock, no security claims) while CREDENTIALS pages keep "Secure · encrypted"; reviewer = "Credalio team" (never "Trust team"); avoid "teach/teacher" in creator copy (profile label "Topics"); Readiness Nova card label "Nova suggests"; spelling follows the client ("Organization"). Sample data: the unreadable credential is the GOOGLE certificate everywhere (MSc is verified); identity verified card holds name, country and ONE date. Dynamic in build: Copilot name, Creio balance + per-draft estimate, readiness % and counts, orientation progress/time/dates, attempts left.
- LOGO (2026-10-07): new Credalio wordmark (`design/illustrations/credalio-wordmark.png`, mark-only `credalio-mark.png`, blue #1E4497) was swapped into the canvas files by a regex post-process, NOT in the older generators. If you re-run gen2/build8/build10 etc., re-apply the logo swap (classes `lg-word` / `lg-mark`).

## Hard layout rules
- Desktop must NOT scroll on onboarding screens: must fit 1440×820 and 1280×720 (viewport-based layout, clamp/vh).
- Fully responsive: breakpoints ~1080 and ~760/860; mobile = stacked layout, 44px+ touch targets.
- One responsive source file per screen; preview boards (laptop/mobile) only `dc-import` it — never duplicate designs.
- Animations only play in canvas Play mode (editor disables them) — not a bug.
- Always re-read live canvas files before editing (designer edits in place); sync them into the repo.

## Figma (started 2026-10-03)
- File: https://www.figma.com/design/bUBmVNm3WWd5eCl5JxX2sz (Team1, Pro). Pages: Cover, Foundations, Components, Onboarding · Desktop, Onboarding · Mobile.
- Font in Figma: Google Sans Flex (closest available to Google Sans).
- Variables: Primitives / Color (semantic, Light) / Spacing / Radius; 16 text styles; 4 effect styles. Components use variables + styles.
- In Figma ALWAYS set clipsContent=false on inner frames/auto-layouts/components (only screen roots + illustration crops clip) — otherwise shadows get cropped.
- Figma can't render WebP image fills: always upload PNG. State ledger: `design/figma-state.json`.
- Screens are generated from the canvas with `design/figma-sync/` (DOM → auto-layout frames, colour variables bound, images as PNG). Re-sync a screen after canvas edits by re-running its job (replaces the frame by name). Pages: Onboarding · Desktop/Mobile, Creator Studio, Readiness & Centre, Orientation, Identity (KYC), Credentials. Builder source is stored in the file (root sharedPluginData crd/builder) so jobs only send data; combine jobs with `design/figma-sync/comb.py`.

## Workflow
- 25 screens/day plan in chat history; track progress in `screens.md`.
- Commit + push to branch `claude/gallant-meitner-290f6y` after each change.
