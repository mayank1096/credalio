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
