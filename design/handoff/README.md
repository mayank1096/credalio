# Credalio · design handoff for developers

The designs are reference mockups. Rebuild them in your own components; don't copy the markup wholesale.
Every value you need (colour, size, spacing, radius, shadow, motion) is in each screen's `<style>` block and inline styles.

## What's in this package

| Folder / file | What it is |
|---|---|
| `index.html` | List of every Link 1 screen in flow order, with desktop and mobile links |
| `screens/` | The code of every screen (one responsive `.dc.html` file per screen) plus the small runtime that renders them (`support.js`, `vendor/`). Runs fully offline. |
| `assets/` | Every image used (logo, illustrations, Copilot characters, backgrounds) |
| `fonts/` | Google Sans (variable, latin + latin-ext) and `google-sans.css` |
| `tokens/` | Design tokens: colours, type, radius, shadows, sizes, breakpoints, motion (`design-tokens.css` as CSS variables, `design-tokens.json` for any build tool) |
| `screens.csv` | Screen index: title, desktop / mobile board, source file, variant, and the screens each one links to |

**To open it:** unzip, then in the folder run `python3 -m http.server 8000` and open http://localhost:8000.
(Opening the files straight from disk with `file://` will not work: browsers block the scripts.)

**Font licence:** Google Sans is served by Google Fonts (fonts.google.com). Check its licence there before you ship it in the product;
if it can't be used, Google Sans Flex or Inter at the same weights are the closest swaps.

## Where the screens are

This handoff covers **Link 1 (phase 1)**: creator onboarding → first dashboard → readiness (identity, credentials, policies) →
Creator Orientation (7 modules) → collaboration and declarations → validation centre.

Canvas: Credalio · Link 1 (link shared with this handoff) · local copy `design/canvas/project/`.

Page 1 shows a desktop board (1440 wide) and a mobile board (390 wide) side by side, in flow order, under section notes.
Press Play in the canvas to click through. Animations only run in Play mode.

## How the files are organised

- **One responsive file per screen.** `CR-ONB-004.dc.html` is the whole screen; it adapts by media query.
  `CR-ONB-004-Mobile.dc.html` is only a 390-wide preview that imports it. Never treat the mobile board as a separate design.
- **States are variants of one source.** A small board file like `CR-KYC-004.dc.html` contains only
  `<dc-import name="CR-KYC-003" variant="verified">`. The variant switch lives in the source's `renderVals()` / `<sc-if>` blocks.
  Build one component with a prop; don't build one component per board.
- **Shared sources** sit on page 2, titled "… · shared source". They are not screens in the flow;
  the boards around them import them with a variant (e.g. `CR-ORI-M3-K` = Module 3 check with variants none / right / wrong).
- **IDs:** `CR-<AREA>-<NNN><letter>`. AREA = ONB onboarding, DASH dashboard, RDY readiness, KYC identity, CRED credentials,
  POL policies, ORI orientation, CTR Creator Centre, CREATE start creating, NOT notifications, HOME home pages,
  COL collaboration, ASG assigned to me, DEC declarations, VAL validation.
  A trailing letter is a state: `e` error, `d` done/declined, `x` declined/missing, `s` short/sent, `v` verified, `p` proactive/pending.
- **Sample data:** names, amounts, dates and counts are realistic placeholders. Copilot name, Creio balance, readiness % and counts,
  orientation progress and dates, and attempts left are all dynamic in the product.
- **`href="#"`** marks an action that is designed but not wired to another board. Real links between boards are file names.
  Everything that leads to a phase 2 screen (wallet, earnings, discussions, calendar, analytics, help, course studio) is `#` on purpose.
- **Role picker (ONB-001):** all four cards are selectable; only Creator (→ ONB-002) and Organization (→ "coming soon") continue in phase 1.

## Foundations

**Type:** Google Sans (400 / 500 / 600). Headings and buttons 600, tags/chips/pills always 500, never bold.
H1 onboarding `clamp(34px, 5.4vh, 46px)`; dashboard H1 28–32 desktop, 24 mobile; body 15–17.5, mobile 14–16.

**Colour**

| Role | Value |
|---|---|
| Text (navy) | `#0B1433` |
| Secondary text | `#3A4566` · `#4A5578` · `#5B6582`; faded labels `#8A93AD` |
| Accent (cobalt) / hover | `#1652F0` / `#0E3BB8` |
| Soft blues | `#EAF0FF` · `#F5F8FF`; app background `#F7F9FD` |
| Borders | `#E6EAF3` · `#D6DDEE` · `#CBD3E6` |
| Success | `#0F6B45` (soft `#E7F5EE`) |
| Error | border `#D92D20`, text `#B42318` |
| Creio (AI usage, always gold) | bg `#FFF1CF → #FFFAEB`, border `#F4D98E`, text brown `#4A3300` |

Status colours: green = complete, cobalt = in progress, amber = action needed, grey = not started / declined / in review.

**Shape:** buttons are pills; the primary button is a cobalt pill with a white circle arrow. Cards radius 16–22, 1.5px borders.
Selected options are a soft blue fill + cobalt border + check (radius 14). They must never look like the primary button.

**Breakpoints:** desktop ≥ 1081; tablet ≤ 1080 (grids collapse); mobile ≤ 960 (dashboard sidebar becomes a drawer) and ≤ 760 (onboarding stacks).
Touch targets ≥ 44px. Onboarding screens must not scroll at 1440×820 or 1280×720 (layout uses `vh` / `clamp`). Dashboard pages may scroll.
Every animation is switched off under `prefers-reduced-motion`.

## Patterns to build once

| Pattern | Where to look | Notes |
|---|---|---|
| Onboarding frame | `CR-ONB-003.dc.html` | logo, Log in, 5-step dashed tracker, centred content, illustration at the bottom |
| Role picker + route animation | `Main.dc.html` (ONB-001), `CR-ONB-002.dc.html` | per option: cobalt trail draws in (`cd-draw`), white streak (`cd-comet`), pulsing end dot (`cd-pulse`), breathing orb under the walker (`cd-orb`). Paths are SVG in a 2172×724 viewBox over the image. |
| Dashboard shell | `CR-DASH-NEW.dc.html` | 264px sidebar, sticky top bar (search, gold Creio pill, help, bell, avatar), content `#F7F9FD` |
| Focus / task shell | `CR-KYC-001.dc.html`, `CR-CRED-002.dc.html` | no sidebar; close, task count, trust pill; sticky bottom actions on mobile |
| Learning player | `CR-ORI-003.dc.html` | top segments, left step rail, 720 reading column, fixed Previous / Next bar |
| Outcome page (all success / pending / action / failed screens) | `CR-KYC-003.dc.html` (`ko-*`) | emblem → status pill → H1 → sub → card(s) → CTA → small links; success adds confetti |
| Info tooltip | any `.tip` | navy bubble on hover/focus next to a ⓘ; replaces explanatory paragraphs |
| Nova card / band | any element with the `profile-bg` image | Nova suggestions always use this gradient background |
| Field error | `CR-ONB-003e` | red border + one error line under the field (replaces the helper text) |

## Images

All images in use are in `assets/` (the canvases reference the same files as `/_blob/<id>`):

| File | Used for |
|---|---|
| `credalio-wordmark.png`, `credalio-mark.png` | logo (mark only on narrow screens) |
| `main-scene-v6.webp` | ONB-001 role scene (and orientation video posters) |
| `ctype-creator-v4.webp` | ONB-002 "How will you create?" scene |
| `create-account.webp`, `check-inbox-v2.webp`, `email-confirmed.webp`, `coming-soon.webp` | ONB-003, 003b, 003v, 002S |
| `campus-bg.webp` | soft background scene on forms, tasks, orientation checks |
| `copilot-nova/maya/alex/sage.webp` | Copilot characters (heads are CSS crops of these) |
| `profile-bg.webp` | Nova cards, profile banners |
| `wave.webp` | animated waving hand (Noto animated emoji, CC BY 4.0) |

Icons are inline SVG line icons (24 grid, 1.9–2.4 stroke, round caps). Swap them for your icon set at the same size and weight.
