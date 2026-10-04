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
- Illustration "One Line, Four Futures" (asset `/_blob/bad84659fa9f24b3a7efb7e88696e531`, 2172×724). The glowing cobalt line = the AI guide; reuse it as the progress/path motif.
- The "Your Copilot lights the way" pill was REMOVED by the designer. Don't bring it back.

## Onboarding layout (approved 2026-10-02)
- Every onboarding step uses the CR-ONB-001 layout: header (logo left, Log in right), dashed 5-step tracker centred under it ("Step 1 of 5 · Your account"), centred content, illustration at the bottom.
- NO left side panel. Illustration on EVERY screen (desktop bottom; mobile under the tracker, panned to hero + Creator). Creator path lit. NO text tags/chips on the illustration (removed by designer).
- NO illustration (designer removed): 003c password, 005 your field, 005b what you teach, 006 + 007 Copilot (Nova character instead).
- 004 H1 uses the animated waving hand (Noto animated emoji, CC BY 4.0, `design/illustrations/wave.webp`, blob `/_blob/e0846c8b6889064bed3e0b948cd9888a`).
- 005b profile card bg = designer image `design/illustrations/profile-bg.webp` (blob `/_blob/d268046654a4206d2a726e62005bcc59`). Nova (006/007) has NO blue floor line.
- Selected chips/options must never look like the primary button: soft blue fill + cobalt border + check, radius 14 (buttons are solid cobalt pills).
- Some steps have their OWN illustration (designer-supplied, in `design/illustrations/`): 003 create-account, 003v email-confirmed (+ confetti), 002S coming-soon. Others use the main scene.
- Shared frame generator: `design/generator/gen2.py` (+ build2.py / build3.py per batch; copy to scratchpad to run).

## Creator Studio (dashboard) shell (2026-10-04)
- Generator `design/generator/dash.py` (SHELL/WRAP/NOVA_AV/icons) + `build8.py`/`build8b.py` (v2 designs; build7 = superseded v1). Sidebar 264px white (sentence-case group labels, line icons, active = soft blue), sticky top bar (search, Nova token pill, help, bell, avatar), content bg #F7F9FD, white cards r20.
- Mobile ≤960: sidebar becomes drawer (hamburger), search hidden. Dashboard pages MAY scroll (no-scroll rule is onboarding only).
- Nova avatar = head crop of the Nova character (NOVA_AV). No emojis, no screen-ID eyebrows, no rainbow colours.
- MOBILE = efficiency first: smaller type (H1 24, body 14–15), compact rows, no tall decorative blocks, primary CTA visible without scrolling where possible, secondary info collapsible (toggle) or hidden; horizontal-scroll chip rows.
- AI Tokens are always shown GOLD (incl. top-bar pill: coin + "20K AI Tokens") (coin, #FFF1CF→#FFFAEB bg, #F4D98E border, brown text). 008 = "Ada, you’re a Creator." reveal (no step tracker); profile card hangs on a lanyard and sways (pendulum).
- Variant screens use one source + prop (e.g. 002Ab = `dc-import CR-CREATE-002A variant="proposal"`).

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

## Workflow
- 25 screens/day plan in chat history; track progress in `screens.md`.
- Commit + push to branch `claude/gallant-meitner-290f6y` after each change.
