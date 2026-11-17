# Credalio · Link 4 · Course Studio · design handoff for developers

The designs are reference mockups. Rebuild them in your own components; don't copy the markup wholesale.
Every value you need (colour, size, spacing, radius, shadow, motion) is in each screen's `<style>` block and inline styles.

## What's in this handoff

| File | What it is |
|---|---|
| `credalio-link4-developer-package.zip` | The code of every screen, all images, the fonts, design tokens, a screen index and this README. Runs offline. |
| `credalio-link4-screen-book.pdf` | Every screen on its own page, desktop and mobile side by side, in flow order, with a contents page. Long pages are split into parts. |
| `credalio-link4-screenshots.zip` | Every board as a full-length image, numbered in flow order |
| `credalio-link4-developer-guide.pdf` | A short introduction: what is built, how to find your way around, what to know before building |
| `assets/` · `tokens/` | The images and design tokens on their own |

Inside the developer package:

| Folder / file | What it is |
|---|---|
| `index.html` | Every screen in flow order, by section and group, with desktop and mobile links. Start here. |
| `screens/` | One responsive `.dc.html` file per screen, plus the small runtime that renders them (`support.js`, `vendor/`) |
| `assets/` | Every image used: logo, Nova, avatars, the sign-in illustration, the Nova card background |
| `fonts/` | Google Sans (variable, latin + latin-ext) and `google-sans.css` |
| `tokens/` | Colours, type, radius, shadows, sizes, breakpoints and motion (`design-tokens.css`, `design-tokens.json`) |
| `screens.csv` | Section, group, title, desktop / mobile board, source file, props, and the screens each one links to |

**To open it:** unzip, then in the folder run `python3 -m http.server 8000` and open http://localhost:8000.
Opening the files straight from disk with `file://` will not work: browsers block the scripts.

**Font licence:** Google Sans is served by Google Fonts (fonts.google.com). Check its licence before you ship it;
Google Sans Flex or Inter at the same weights are the closest swaps.

## What is covered

Link 4 is the **Course Studio** (creating a course from the first idea to publication) and **Manage Published Course**
(everything after it goes live), plus collaboration on both sides.
**242 screens, each designed for desktop (1440) and mobile (390): 484 boards**, plus 19 shared sources.

| Section | Screens |
|---|---|
| Course setup & course design | Create new → Delivery (from Create new or from Nova) → Setup review → How you'll create it → Studio welcome; Studio home; basics, audience, career & skills, outcomes, skills map, evidence, assessment & award, effort, design summary |
| Curriculum Builder & editors | Builder (team, solo, open for collaboration, invited co-creator); add / move / delete items and chapters; editors for video, text, live class, assessment, applied learning |
| Build tools, course views, access & pricing | Resource library, completion rules, team & assignments, my work, team chat; DLP & effort, assessments, practice & projects, delivery, learner experience, learner support; access model, maintenance, pricing |
| Prepare & submit | Course review, marketplace and learner previews, intelligence profile, Nova review, readiness checks, issues; submit for validation (intake, declaration, readiness, scope, quote, payment) |
| Validation, decision & publish | Awaiting assignment, validators assigned, workspace, requests, evidence, meeting, findings; improvements required, revision, resubmission, passed; final pricing, revenue, listing, course is live |
| Manage Published Course | Hub, publishing & visibility (and its states), unpublish; pricing & access; updates & versions; learner access; validation history; archive & removal; insights & engagement; course credits & visibility |
| Collaboration (course) | Collaboration centre, invite, roles & permissions, review, manage collaborators, remove; open collaboration setup, applications, offers, opportunity management |
| Collaboration (creator) | My invitations, invitation details and outcomes, shared courses; opportunities, apply, my applications |
| Launch · Creio & messages | Full validation report, subscription-only pricing, publish confirmation, share; Creio running low / none left / estimate before a large action, account menu, message pop-ups |

**Not in this handoff (still to come):** CR-STU-023 Assessment Type, CR-STU-020B Curriculum Readiness (solo and team)
and CR-COL-001-SOLO (collaboration centre, solo empty state). These four boards follow separately.

## How the files are organised

- **One responsive file per screen.** The mobile board only previews the same file at 390 wide. Never treat it as a separate design.
- **States are props of one source.** A small board file like `MGT-002C.dc.html` contains only
  `<dc-import name="Manage" page="c">`. The switch lives in the source's `renderVals()` / `<sc-if>` blocks.
  Build one component with a prop, not one component per board. `screens.csv` lists each board's props.
  The 19 shared sources (Setup, Studio, Builder, Editor, Course, Prepare, Submit, Preview, Validate, Publish, Manage,
  Manage2, Manage3, Unpublish, Learner, Collab, Collab2, Collab3, Collab4) are listed at the end of `index.html`.
- **Names:** `CR-<AREA>-<NNN>`. Areas: STU Course Studio, COURSE-MGT (shown as MGT) Manage Published Course,
  COL course collaboration, INV invitations, OPP opportunities and applications, NAV shared courses,
  CREDITS course credits, LEARN-CREATORS learner course page, STU-AI Creio, STU-MSG messages. A letter or word after the
  number is a state (for example `MGT-002C` hidden, `COL-004-PENDING`).
- **Copy:** the client's copy is used word for word, with "AI Tokens" renamed Creio throughout.
- **Sample data:** names, prices, dates and counts are realistic placeholders and are dynamic in the product.

## Links

- Buttons that lead to another screen are real links (file names) and work in the prototype.
- Many buttons are `href="#"` on purpose: they act on the page (Save, Export, Send, Upload, Download)
  or lead to places outside this handoff (Link 1 and Link 2 screens such as the creator dashboard, wallet and settings).

## Foundations

Same as Links 1 and 2 (see `tokens/`). In short:

- **Type:** Google Sans 400 / 500 / 600. Headings and buttons 600; tags, chips and pills always 500.
- **Colour:** navy text `#0B1433`; one cobalt accent `#1652F0` (hover `#0E3BB8`); soft blues `#EAF0FF` / `#F5F8FF`;
  app background `#F7F9FD`; borders `#E6EAF3` / `#D6DDEE`; success `#0F6B45`; error `#B42318`.
- **Status:** green = complete, cobalt = in progress, amber = action needed, grey = not started / declined / in review.
- **Creio vs Credits:** Creio (AI usage) is always gold with the gold coin. Credits (wallet) always use the cobalt "C" coin.
- **Shape:** pill buttons; the primary is a cobalt pill with a white circle arrow. Cards radius 16–22 with 1.5px borders.
- **Breakpoints:** 1080, 960 (sidebar becomes a drawer), 760. Touch targets ≥ 44px. Motion turns off under `prefers-reduced-motion`.

## Patterns to build once

| Pattern | Where | Notes |
|---|---|---|
| Course Studio shell | course design, builder, tools, prepare | sidebar with the course and its sections, sticky top bar with the Creio pill; drawer under 960 |
| Creator shell | Manage Published Course, collaboration | the creator dashboard sidebar with Create / Work / Insights / Economy / Creator / Account |
| Focus flow | setup, submit, publish, unpublish, open collaboration | slim bar with close, title and step progress; sticky actions on mobile |
| Outcome page | submitted, paid, passed, live, accepted, sent | emblem → status pill → heading → sub → card / next step → button → small links |
| Drawer / dialog | learner detail, collaborator detail, confirms | right drawer on desktop, bottom sheet on mobile |
| Nova | design, builder, review | Nova cards use the profile gradient; a thinking state runs before every reply |
| Info tooltip | everywhere | navy bubble behind an ⓘ; explanations live here, not in extra paragraphs |

Animations only run in the prototype's Play mode.

## Open items

- The four boards listed above, still to come.
- Prices, fees, revenue shares and dates are samples for the client to confirm.
