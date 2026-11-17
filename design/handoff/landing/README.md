# Credalio · Landing, learners & pricing · design handoff for developers

The designs are reference mockups. Rebuild them in your own components; don't copy the markup wholesale.
Every value you need (colour, size, spacing, radius, shadow, motion) is in each screen's `<style>` block and inline styles.

## What's in this handoff

| File | What it is |
|---|---|
| `credalio-landing-developer-package.zip` | The code of every screen, all images, the fonts, design tokens, a screen index and this README. Runs offline. |
| `credalio-landing-screen-book.pdf` | Every screen on its own page, desktop and mobile side by side, in flow order, with a contents page |
| `credalio-landing-screenshots.zip` | Every board as an image, numbered in flow order |
| `credalio-landing-developer-guide.pdf` | A short introduction: what is built, how to find your way around, what to know before building |
| `assets/` · `tokens/` | The images and design tokens on their own |

Inside the developer package:

| Folder / file | What it is |
|---|---|
| `index.html` | Every screen in flow order, by section and group, with desktop and mobile links. Start here. |
| `screens/` | One responsive `.dc.html` file per screen, plus the small runtime that renders them (`support.js`, `vendor/`) |
| `assets/` | Every image used: logo, hero and footer art, illustrations, AI Coach characters, avatars, backgrounds |
| `fonts/` | Google Sans (variable, latin + latin-ext) and `google-sans.css` |
| `tokens/` | Colours, type, radius, shadows, sizes, breakpoints and motion (`design-tokens.css`, `design-tokens.json`) |
| `screens.csv` | Section, group, title, desktop / mobile board, source file, props, and the screens each one links to |

**To open it:** unzip, then in the folder run `python3 -m http.server 8000` and open http://localhost:8000.
Opening the files straight from disk with `file://` will not work: browsers block the scripts.

**Font licence:** Google Sans is served by Google Fonts (fonts.google.com). Check its licence before you ship it;
Google Sans Flex or Inter at the same weights are the closest swaps.

## What is covered

The public site and the learner side: landing page, discovery, course / path / certificate / program pages,
the journey builder, learner onboarding, the learner dashboard, checkout and pricing, and the pages for creators,
institutions and validation. **147 screens, each designed for desktop (1440) and mobile (390): 294 boards**, plus 3 shared sources.

| Section | Screens |
|---|---|
| Landing page, discovery and course pages | Landing page; Explore Learning (guest, signed in, filters, loading, no results, error); Courses; Course detail (guest, signed in, not enough DLP, subscription only, in progress, owned with Credits, temporary access, completed, closed) and the free lesson preview (video, reading); Career paths and path detail (+ compare, states); Certifications and certificate detail (eligibility: meets, evidence needed, not yet eligible; enrolled; certified; compare); Learning programs and program detail (application: draft, submitted, under review, accepted, waitlisted, payment pending, full, closed; enrolled; completed; compare; no cohorts match your schedule); listing states (loading, nothing published, no results, error) |
| Journey, onboarding and institution invite | Start your journey (goal, what you know, building, ready); your journey (guest, saved, step 1 started, returning); onboarding (welcome, account, inbox, verified, password, about you, personalise or explore, meet your AI Coach, how you like to learn, Nova builds, ready, progress saved); institution invite (code, invitation, create account, linked) |
| Learner dashboard | New learner, interests only, goal without a path, career path in progress, active journey, course-only, certification-first, learning program, returning learner, Ask Nova; season and usage (wallets, LAS breakdown, rewards calculating / ready, MFORGE not eligible, DLP usage); allowance shortfall (running low, used, course needs more DLP, zero DLP, low DLP in a lesson); Digital Backpack and TruVault; Ask Tutor |
| Checkout and pricing | Checkout from Pricing (Basic, Pro), Pro after onboarding (plan, payment, review), processing, done; from the allowance moment and the Data Analyst path; from your plan page; adding DLP without changing plan; payment didn't go through; Pricing page (plans, compare, Enterprise, top-ups, what DLP is, how DLP works) and its signed-in modes |
| Creators, institutions, validation, TruVault and Ask Tutor | For Creators; For Institutions; partner inquiry (form, missing details, sent); How Validation Works; Public Validation Record |

## How the files are organised

- **One responsive file per screen.** The mobile board only previews the same file at 390 wide. Never treat it as a separate design.
- **States are props of one source.** A small board file like `CourseDetail-Owned.dc.html` contains only
  `<dc-import name="CourseDetail" access="owned">`. The switch lives in the source's `renderVals()` / `<sc-if>` blocks.
  Build one component with a prop, not one component per board. Common props: `viewer` (guest | learner), `state`
  (loading | empty | noresults | error), `view`, `access`, `elig`, `app`, `step`, `mode`. `screens.csv` lists each board's props.
- **Shared sources:** `Dashboard.dc.html` (every learner dashboard board), `Checkout.dc.html` (every checkout board) and
  `Access.dc.html` (the allowance-shortfall boards) have no board of their own.
- **Screen codes** in the titles: EXP explore, PATH career paths, CERT certifications, PROG programs, JNY journey,
  ONB onboarding, INST institution invite, LRN learner dashboard, ACC allowance, CHK checkout, PRC pricing,
  CRE for creators, ENT for institutions / partner inquiry, TRST validation, TV TruVault.
- **Sample data:** names, prices, dates, counts and balances are realistic placeholders and are dynamic in the product.

## Links

- Cards, navigation, breadcrumbs and buttons that lead to another screen are real links (file names) and work in the prototype:
  Explore → listing → detail → checkout, and back.
- About 200 buttons and links are `href="#"` on purpose: they act on the page (Save, Share, Notify me, Download)
  or lead to pages outside this handoff (Log in, Privacy, Terms, the course player).
- Learner onboarding reuses the Journey screens in "onboarding" mode, so the same files appear in both flows.

## Foundations

Same as Links 1 and 2 (see `tokens/`). In short:

- **Type:** Google Sans 400 / 500 / 600. Headings and buttons 600; tags, chips and pills always 500.
- **Colour:** navy text `#0B1433`; one cobalt accent `#1652F0` (hover `#0E3BB8`); soft blues `#EAF0FF` / `#F5F8FF`;
  backgrounds white and `#F7F9FD`; borders `#E6EAF3` / `#D6DDEE`; success `#0F6B45`; error `#B42318`.
- **Status:** green = complete, cobalt = in progress, amber = action needed, grey = not started / declined / in review.
- **DLP vs Credits:** DLP is the learning allowance from a plan (gold 3D coin). Credits are the wallet, used to own
  learning for life and to pay certificate and program fees (cobalt "C" coin). They are separate and never converted.
  MFORGE uses the navy "M" token.
- **Shape:** pill buttons; the primary is a cobalt pill with a white circle arrow. Cards radius 16–22 with 1.5px borders.
- **Breakpoints:** 1300 (site nav collapses into a menu), 1080, 960 (filter column becomes a bottom sheet; dashboard
  sidebar becomes a drawer), 760. Touch targets ≥ 44px. Motion turns off under `prefers-reduced-motion`.

## Patterns to build once

| Pattern | Where | Notes |
|---|---|---|
| Site header and footer | every public page | 8-link nav with the current page highlighted; signed in, Log in / Create account become the DLP balance and avatar |
| Listing with filters | Explore, career paths, certifications, programs | filter column with counts per option, "More filters", chips with Clear all, sort, result count, compare (up to 3), pagination; bottom sheet on mobile |
| Listing states | the four listings | loading skeletons, nothing published, no results (with "Try instead" chips), couldn't load (retry) |
| Detail page | course, path, certificate, program | hero with validation tier, CEI and rating, Save / Share; section tabs; sticky access card on desktop, stacked on mobile |
| Access card | detail pages | DLP and Credits routes side by side; changes with the access / eligibility / application state |
| Focus flow | journey, onboarding, checkout | no site nav: logo, progress, close; sticky actions on mobile |
| Outcome page | checkout done, failed, verified, linked | emblem → status pill → heading → sub → card / next step → button → small links |
| AI Coach (Nova) | journey, dashboard | thinking state before every reply (spinning ring + status line), then the reply types in |
| Info tooltip | everywhere | navy bubble behind an ⓘ; explanations live here, not in extra paragraphs |

Animations only run in the prototype's Play mode.

## Open items (client to confirm)

- Prices, fees and hours are samples. One rule is applied everywhere: learning in DLP or Credits, certificate
  assessment fees and program fees in Credits. The learner dashboard's sample prices are not yet aligned with the listing pages.
- The lesson preview shows a video and a reading lesson; a practice lesson only appears as a locked row.
- Log in, Privacy, Terms and the course player are outside this handoff.
