# New project · Link 4 + Landing link (started 2026-10-27)

Read this, then `CLAUDE.md` (rules and look), before any work. Everything in CLAUDE.md "Goal", "Look" and "Layout" applies here unchanged:
same brand, same shell, same patterns as Links 1 and 2. DESIGN, DON'T COPY: the client files are a content source only.

## The two client links

| Our name | Client file | What it is |
|---|---|---|
| **Link 4** | https://claude.ai/artifact/3RdUuYV5KDmaKATNxvRqyJ | Course Studio (building one course) + Manage Published Course |
| **Landing link** | https://claude.ai/artifact/W174uLihc1ZtqgMRojf3M2 | Public landing page, discovery, pricing and checkout, learner onboarding and dashboard, creators, validators |

Saved copies of their canvas.json: `reference/link4/client-canvas.json`, `reference/landing/client-canvas.json`.
Client instructions for Link 4: `reference/link4/client-instructions.pdf` (summary below).

## Scope (counted 2026-10-26, board by board)

**Link 4: 245 screens** (client file has 264 boards)

| Client page | Boards | Not screens | Design |
|---|---|---|---|
| Course Studio | 183 | 9 (inventory, start here, play-through, architecture CR-STU-000, 3 flow maps CR-FLOW-*, CourseStudio component, CB-021b "no longer in flow") | 174 |
| Manage Published Course | 71 | 0 | 71 |
| Solo creator flow | 10 | **all: reference only, do NOT design** | 0 |

**Landing link: 196 screens** (client file has 213 boards)

| Client page | Boards | Not screens | Design |
|---|---|---|---|
| Landing, learners & pricing | 110 | 8 ("press Play" components + *-000 architecture pages) | 102 |
| Creators | 48 | 4 | 44 (revised version of our Link 1 creator journey + dashboard: reuse what fits) |
| Validators | 55 | 5 | 50 |

"Press Play" component boards (Checkout, Dashboard, Engine, Journey, Onboarding, CreatorDash, CreatorOnb, ValOnb, ValQual, ValDash, SVE)
and *-000 architecture pages are references for flow and rules, not screens.

**Total: 441 screens, about 880 boards with mobile.** Every screen gets desktop (1440) + mobile (390), as before.

## Client instructions (Link 4), in short

- **Solo creator flow page:** not designed. It is a reference for a "single creator" state of the course flow. Client will clarify more as we go.
- **Course Studio entry:** CR-STU-004 "How will you create this course?" with three cards: Create Solo → Curriculum Builder; Create with Co-Creators → CR-COL-002; Open to Collaboration → CR-COL-006. Replaces the old screen.
- **Course workspace left nav:** Overview, Design, Build, Experience, Prepare, Validate and Publish (both gated), then Manage with Collaborators and Course Settings.
- **Curriculum Builder (CR-STU-020):** separate boards for solo, team, open and co-creator states, incl. add a lesson straight into the editor, DLP rules, move lesson / chapter.
- **Message pop-ups and AI token rows** sit on the same page, each its own board. "AI Tokens" are **Creio** in our design (gold, never "AI Tokens").
- **Collaboration (course level, in Course Studio under Manage › Collaborators):**
  - Invite by name: CR-STU-004 Co-Creators → CR-COL-002 invite (+ error) → CR-COL-002B roles & permissions (optional; role-changed variant) → CR-COL-003 review → CR-COL-003-SENT (Continue building course) → CR-COL-004 manage (Active, Pending, Past, Activity, member detail, withdraw, resend) → CR-COL-005A–C remove.
  - Open collaboration (lead creator): CR-STU-004 Open → CR-COL-006A–E five setup steps → CR-COL-007 preview → CR-COL-006F published → CR-COL-010 manage opportunity (open, empty, paused, filled, closed, withdraw confirm) → CR-COL-008 applications (All, New, Shortlisted, Offered, Declined + applicant detail) → branches: clarification (CLARIFY, SENT, REPLY), decline, withdraw offer (confirm + success) → CR-COL-009 make an offer (+ CR-COL-002B-OFFER permissions).
  - On CR-COL-002 and every CR-COL-006 step: blue "do this later" banner with Continue building course. Roles & permissions also reachable from Make an offer and collaborator detail (Edit permissions).
- **Collaboration (creator level, in Creator Studio under Collaboration):** Invitations CR-INV-001–005 (tabs, details, accept, decline, every outcome, withdrawn); Opportunities CR-OPP-001–003 (list, details, apply); My Applications CR-OPP-004 (7 tabs: Pending, Under Review, Shortlisted, Offer Received, Accepted, Declined, Withdrawn; withdraw confirm; reply to clarification); Shared Courses CR-NAV-002.
- **Manage Published Course:** hub CR-COURSE-MGT-001 with eight cards: Publishing & Visibility, Pricing & Access, Course Updates & Versions, Learner Access & Enrollment, Validation History, Archive & Removal, Insights & Engagement (009, 009A–F), Course Credits & Visibility (new).
- **Multiple creators on the learner Course Overview:** CR-LEARN-CREATORS-2 (lead + 1, byline avatars, "Meet the creators" cards with contributions), -5 (3 names + "2 others", 4 cards, View all), -PANEL (all credited), CR-COURSE-CREDITS (lead controls who is shown), -ASK (ask a contributor to be credited).
  Credit rules: lead and co-creators shown by default; contributors and reviewers only if they agree; pending invites, applicants and revenue shares never shown.
- **Creator Preview** screens (amber CREATOR PREVIEW tag) simulate the learner view; the real learner app is designed separately.

## Overlap with what we already designed

- Link 1 (`design/canvas/`): collaboration COL-001–004 (old version), Nova chat, readiness, creator journey and dashboard. Link 4's collaboration flow is new and larger: design it fresh in our style, reuse components.
- Link 2 (`design/canvas2/`): Creio (top-bar chip, low / not enough / estimate), message pop-ups, account menu, Studio shell. Reuse these sources for Link 4's AI-token and pop-up boards.

## Before every new section
- Re-read the "Designer's rule for every new section" in CLAUDE.md: client files are dummy content layout only; design from scratch, $24K-website quality.

## How we work (same as before)

- New canvas(es) for each link. **512 files per canvas** limit: Link 4 (~490 boards) and Landing (~392) each need their own canvas; split a link across two canvases if it passes ~480.
- Work in batches of ~20–30 screens in client order; after each batch: render check (0 page errors), overlap scan (`design/tools/overlap.js`), coin check (`design/tools/coins.js`), board heights fit content, audit + cleancss, publish, commit, push, log in this file.
- Mark each batch's new boards with a pink strip note on the canvas (remove before client delivery).
- Never mention Claude / Anthropic in anything delivered (see CLAUDE.md).
- Quoted to the client: $7,500, about 3–4 weeks (not yet confirmed).
- **Order (designer 2026-10-27): Landing link FIRST, then Link 4.** Start with the landing page section in client order.

## Log

- 2026-10-27: project set up; references saved; nothing designed yet.
- 2026-10-28: Landing canvas created: https://claude.ai/artifact/J3znQsAEUEHQEJNruQgjFm (local `design/canvas3/project/`). Hero v1 (Main + Main-Mobile): pill nav, eyebrow, "Who will you become next?" with path tile, goal search bar + Try chips, illustration area reserved (dashed placeholder). Logo blobs copied from Link 1: wordmark `/_blob/8acabcff7ece53343d63205e8b7321a2`, mark `/_blob/f81e36d31295a0d0737959589ec1abd4`.
- 2026-10-28: hero edits from comments (no icon tile, wider nav, one-line sub, no Try chips, no note line); planet illustration as hero background: `design/illustrations/landing-planet.webp` (+ source .png) = `/_blob/195737ec1e847c0d182e13d12b6cc269`, overlaps content via `margin-top: calc(40px - 45.3%)` (mobile: 160% wide, centred).
- 2026-10-28: Hero-B (copy, fits viewport 820, plain header) and Hero-C: floating figure `design/illustrations/landing-float.webp` = `/_blob/edace6a66615ca20dfb081994323901a` with 8 career cards on a CSS 3D ring around the head (back ring behind the image, front ring above it, backface trick), click a card to fill the search.
- 2026-10-28: Hero-C desktop art = "many paths" `design/illustrations/landing-paths.webp` (checkerboard removed from the supplied image; source kept as landing-paths-source.webp) = `/_blob/296390fb43ef166647144a765490d140`; sized with container units so head clears the search bar and the centre dot stays in view; SVG light pulses run from the centre dot along the 4 paths; 6 orbit cards. Mobile keeps landing-float.
- 2026-10-29: Polish pass on sections 3–4: Coach mobile drops the stage card (no card-in-card), chat reads left/right with the learner avatar on her own bubble, height fixed across all 7 tabs (no layout jump), roomier header/tabs rhythm; Grow mobile coach pill on one line ("Not sure which? Ask your AI Coach"), more header space. Boards: Hero-C 3850, Hero-C-Mobile 3852, Coach-Mobile 1104.
- 2026-10-29: Hero-C art replaced with the designer's redrawn version `design/illustrations/landing-paths-2.webp` = `/_blob/c8358d40470e2f7e32e8a358d911397a` (fake checkerboard removed; source kept as landing-paths-2-source.webp); light-signal paths and centre mark re-traced to its dots (centre 760,888). Coach girl = thinking pose `landing-learner-think.webp` = `/_blob/29a268dcb297a1c04f59e9ee20e60886` (white cut out, bottom faded; source kept), 340px desktop, mobile avatar 35% 4% / 330%.
- 2026-10-29: Section 5 · Trusted learning (`Validated.dc.html`, boards Validated 1440×1040 + Validated-Mobile 390×1744, joined into Hero-C after Coach; Hero-C 4905, Hero-C-Mobile 5609). Concept: a real course card under live review. Three validator notes (subject / learning design / assessment) each light their part of the card (cobalt scan box + connector wire), card status walks Not yet validated → Review in progress → Credalio Validated, scalloped Credalio seal stamps on; status legend on the left follows along. ~12.8s auto loop, notes clickable, restarts when scrolled into view.
- 2026-10-29: Landing page combined into ONE board pair: `Landing.dc.html` (1440×4905, all 5 sections inline; each section's logic is a Part class inside one Component: HeroPart, EnginePart (+ momentVals), GrowPart, CoachPart, TrustPart; holes namespaced hero./eng./grow./coach./tv.) + `Landing-Mobile.dc.html` (390×5643). Removed boards/files: Hero-C(+Mobile), Engine-Field(+Mobile), Moment, Grow(+Mobile), Coach(+Mobile), Validated(+Mobile) (in git history). Hero-B concept board kept. Edit sections inside Landing.dc.html from now on.
- 2026-10-29: Section 5 redesigned (designer: old one cluttered). New concept = the seal being built: three thin rings (subject matter, learning design, assessment, curved labels) draw one by one around the Credalio mark, each with a reviewer bead (PN/JO/LM) riding the tip; when all close the scalloped seal stamps on with 'CREDALIO · VALIDATED' ring text and a green check. Left: H2, one sentence, 3 status pills that follow the loop, 'How validation works'. One caption line under the seal. Classes tv2-*, TrustPart in Landing.dc.html. Boards: Landing 4734, Landing-Mobile 4866.
- 2026-10-29: Designer rejected the seal-rings version ('ai slop'). Three static concept boards for Trusted learning added below the landing (row y 7760): Trust-A Quality label (nutrition-label style, signatures), Trust-B Course passport (3 ink stamps), Trust-C Two courses, one choice. Waiting for the pick; then build it into Landing.dc.html (desktop + mobile, animated) and delete the concept boards.
- 2026-10-29: Section 5 = motion piece in the section-2 dot language (designer picked 'motion piece like section 2'): 'quality filter'. Canvas lattice of dot lanes flows left→right (top→bottom on mobile) through three light sheets (01 Subject matter, 02 Learning design, 03 Assessment); ~20% per gate fall away grey, survivors tighten and turn cobalt, then pour into a dotted Credalio seal (scalloped ring + inner ring + check) that gently turns. Status pills sit in the flow (Not yet validated / Review in progress / Credalio Validated). Classes tq-*, TrustPart in Landing.dc.html; pauses when offscreen. Concept boards Trust-A/B/C removed. Boards: Landing 4802, Landing-Mobile 5067.
- 2026-10-30: Designer rejected the dot-flow version too. Section 5 rebuilt as an exploded 3D view of a course (CSS 3D, isometric): three real UI layers (Content: lesson + SQL; Learning design: Outcome → Lessons → Practice → Project; Assessment: quiz + pass mark) separate, a cobalt scan passes through each in turn with a green check, layers close and the Credalio seal stamps onto the card. Left: 3 steps that light up in sync + 'How validation works'; one status pill on the stage (Not yet validated → Review in progress → Credalio Validated); caption under. ~14s loop, restarts when in view. Classes tx-*, TrustPart. Boards: Landing 4750, Landing-Mobile 4983.
- 2026-10-30: Section 5 polish (designer: idea good, execution jittery/heavy, stamp dipped under the card): removed the constant 3D rocking (static camera), static badges (no spinning inside 3D), floor shadow without blur filter, layers will-change + 1px borders + soft shadow, slower easeInOut 1.4s, lighter content (light code block, tinted bars). Seal is now a child of the top layer at translateZ(3px), lands 90→3px with a no-overshoot ease-out after the layers have closed, plus a soft shadow; verified it never goes below the card.
- 2026-10-30: Footer added at the end of Landing.dc.html (designer's reference layout): brand + tagline, Learn / Create / Company columns (client content), 'Stay in the loop' newsletter pill input, full-bleed illustration strip (.ft-art, 360px, fades in from white), bottom bar over the art (socials, © 2026 magnummeta, Privacy/Terms/Cookies). Illustration is a STAND-IN (landing-paths-2) until the designer's GPT footer image arrives. Boards: Landing 5375, Landing-Mobile 6016.
- 2026-10-30: Footer illustration applied: `design/illustrations/landing-footer.webp` = `/_blob/bb8793dfe09d0f2ad470cd1807e01cf3` (designer's GPT image, top white cropped; source kept as landing-footer-source.webp). Full-width (min 1440px, centred; 820px on mobile showing the bridge), fades in from white; links sit above it (z-index). Boards: Landing 5541, Landing-Mobile 6086.
- 2026-10-30: Footer illustration swapped to the 3D Credalio logo version: `design/illustrations/landing-footer-logo.webp` = `/_blob/ee51c2bda2bb389fdd58792d3ed8dd32` (source kept; previous landscape landing-footer.webp kept as an alternative). Mobile image 620px so the whole logo shows; legal links get a white pill on desktop; mobile bottom bar sits below the art. Boards: Landing 5467, Landing-Mobile 6024.
- 2026-10-30: Hero orbit: 12 career cards on desktop (new between each: Architect, Chef, Pilot, Marketer, Accountant, Electrician), 6 on mobile (alternate ones hidden as before); cards spaced by width so gaps are even (desktop r 372, mobile r 140). Mobile cards smaller: 30px tall, 22px icon tile, 10px text. Cobalt = Software engineer, navy = Cybersecurity analyst.
- 2026-10-30: Client demo bundle (outside the canvas): `design/demo/landing/` (index.html = Landing.dc.html with blob paths → img/, runtime support.js, 5 images) + `design/demo/credalio-landing-demo.zip`. Works on any static host (needs http, not file://). Tested 1440 + 390: all sections render, scroll-driven Become Engine works, 0 errors, 0 broken images. Not hosted yet: repo is private and no hosting credentials in this session. Rebuild after landing changes: same sed swap of blob ids.
- 2026-10-30: Hero roles now all learnable online: Data scientist, Cloud engineer, UX designer, Content writer, Software engineer, AI engineer, Business analyst, Digital marketer, Product manager, Accountant, Cybersecurity analyst, Graphic designer (desktop orbit r 404). Canvas height fix: root min-height:100vh removed; when the viewport is taller than 1300px (canvas board) the Become Engine scroll track collapses to its sticky section, so the board is exactly the page. Measured: Landing 5413, Landing-Mobile 6012. Demo bundle rebuilt.
- 2026-10-30: Footer image replaced (designer's new 3D logo version) = `/_blob/e6a562c2cab8141c15be39c5c34e4fe7` (landing-footer-logo.webp overwritten; source kept). Measured boards: Landing 5381, Landing-Mobile 5998. Demo bundle rebuilt.
- 2026-10-30: Client demo LIVE: https://mayank1096.github.io/credalio/ (GitHub Pages from the demo-only `gh-pages` branch; repo made public by the designer). Tested desktop + mobile: full page renders, 0 errors, 0 broken images. To update: rebuild design/demo/landing, copy into the gh-pages worktree, commit, push gh-pages.
- 2026-10-30: Hero fits short laptop screens (MacBook 13 ~1440×680): hero height clamp(560px, 100svh-32px, 860px) (was min 720), card orbit scales with the illustration (--os = stage height/820, desktop only, set in HeroPart.componentDidMount). Canvas board heights unchanged. Demo + gh-pages updated.
- 2026-10-30: Hero on short desktop screens (max-height 860px): illustration lifted so the glowing C sits ~100px above the fold (clears the macOS Dock) — stage bottom offset 112px, height formula uses 480px for the text block. Taller screens and canvas unchanged. Demo + gh-pages updated.
- 2026-10-30: Reverted the short-screen lift (designer disliked it); hero back to v70 behaviour. Plan: designer makes a WIDER desktop-only hero image (~21:9, less height) in GPT; mobile keeps landing-paths-2.
