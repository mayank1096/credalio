# Credalio · Link 2 · Creator Studio · design handoff for developers

The designs are reference mockups. Rebuild them in your own components; don't copy the markup wholesale.
Every value you need (colour, size, spacing, radius, shadow, motion) is in each screen's `<style>` block and inline styles.

## What's in this handoff

| File | What it is |
|---|---|
| `credalio-link2-developer-package.zip` | The code of every screen, all images, the fonts, design tokens, a screen index and this README. Runs offline. |
| `credalio-link2-screen-book.pdf` | Every screen on its own page, desktop and mobile side by side, in flow order, with a contents page |
| `credalio-link2-screenshots.zip` | Every board as an image, numbered in flow order |
| `credalio-link2-developer-guide.pdf` | A three-page introduction: what is built, how to find your way around, what to know before building |
| `assets/` · `tokens/` | The images and design tokens on their own |

Inside the developer package:

| Folder / file | What it is |
|---|---|
| `index.html` | Every screen in flow order, by section, with desktop and mobile links. Start here. |
| `screens/` | One responsive `.dc.html` file per screen, plus the small runtime that renders them (`support.js`, `vendor/`) |
| `assets/` | Every image used: logo, illustrations, Copilot characters, payout provider logos, backgrounds |
| `fonts/` | Google Sans (variable, latin + latin-ext) and `google-sans.css` |
| `tokens/` | Colours, type, radius, shadows, sizes, breakpoints and motion (`design-tokens.css`, `design-tokens.json`) |
| `screens.csv` | Title, desktop / mobile board, source file, variant, and the screens each one links to |

**To open it:** unzip, then in the folder run `python3 -m http.server 8000` and open http://localhost:8000.
Opening the files straight from disk with `file://` will not work: browsers block the scripts.

**Font licence:** Google Sans is served by Google Fonts (fonts.google.com). Check its licence before you ship it;
Google Sans Flex or Inter at the same weights are the closest swaps.

## What is covered

Link 2 is the **Creator Studio**: everything a creator uses after their first course is live.
**124 screens, each designed for desktop (1440) and mobile (390): 248 boards**, plus 24 shared sources.

| Section | Screens |
|---|---|
| Credit Wallet | Wallet, add Credits (amount, payment method, review), processing, failed, Credits added, transactions |
| Payments & revalidation | Validation quote, balance check (short, enough, back from funding), confirm, paid; revalidation (what changed, quote) |
| Earnings & payouts | Earnings (payout on its way, below minimum, no method); payout method (PayPal, Payoneer, Tipalti, U.S. direct deposit) with connect, pending, connected, error and action states; payout status (processing, paid, failed, returned, action required); payout history |
| Course overview & discussions | Course overview; discussions list, unanswered, thread, answering, from a notification |
| Calendar & availability | Month, week, day, agenda, event detail; weekly availability; days off; presence and visibility |
| Learner support, learners & analytics | Support inbox and conversation; learners and learner detail; analytics overview, course, certification, career path, programme, compare (courses, cohorts), export |
| Creator profile & organizations | Profile, expertise, credentials, public preview, public profile; My organizations (coming soon) |
| Settings | Account, deactivate, delete, security, notifications, privacy, language, AI preferences (and saved state), sign-in methods |
| Nova panel, search & help | Copilot panel (default, expanded, apply changes, past conversations); search results and no results; help, article, contact (and errors), request sent, my requests, conversation |
| Nova & Creio | Nova overview (new creator, standard), Creio history, buy Creio (packages, custom, below minimum, review), Creio added |
| Creio · topping up | Not enough Credits → add Credits from Nova → back to the purchase |
| Creio · usage & alerts | Usage, top-bar popover, low, almost out, used up, not enough for an action, estimate before running |
| Account menu | Menu (several roles, one role), switching to the Validator workspace |
| Message pop-ups | Pop-ups, quick reply, reply sent, many messages, preview hidden, pop-up settings |

**Not in this handoff (agreed with the client):** programme cohorts, cohort overview, enrolment and roster
(the 53 boards below the "do not design" note), and the retired manual payout request.

## How the files are organised

- **One responsive file per screen.** The mobile board only previews the same file at 390 wide. Never treat it as a separate design.
- **States are variants of one source.** A small board file like `CR-PAYO-001m.dc.html` contains only
  `<dc-import name="CR-PAYO-OUT" variant="tipalti">`. The switch lives in the source's `renderVals()` / `<sc-if>` blocks.
  Build one component with a prop, not one component per board. The 24 shared sources are listed at the end of `index.html`.
- **Names:** `CR-<AREA>-<NNN><letter>`. Areas: WAL wallet, PAY payment, REVAL revalidation, EARN earnings, PAYO payouts,
  COURSE-OV course overview, DISC discussions, CAL calendar, SUP learner support, LRN learners, ANA analytics, PROF profile,
  ORG organizations, SET / HOME-SET settings, AI Nova panel, SEARCH search, HELP help, NOVA Nova, CREIO Creio,
  PM account menu, MSG message pop-ups. A trailing letter is a state (for example `f` failed, `p` paid / pending, `e` error).
- **Sample data:** names, amounts, dates and counts are realistic placeholders. Balances, Creio, counts and dates are dynamic in the product.

## Links

- Buttons that lead to another screen are real links (file names) and work in the prototype.
- About 70 buttons are `href="#"` on purpose: they act on the page (Save, Download, Export, Join call, Decline, Apply changes)
  and have no screen of their own.
- Some links point to **Link 1 screens** (My Creations, Create, Assigned to me, Validation Centre, Creator Centre,
  Readiness, Notifications, identity, credentials, orientation, policies, Log in). Those files are in the Link 1 package.

## Foundations

Same as Link 1 (see `tokens/`). In short:

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
| Studio shell | every dashboard page | 264px sidebar, sticky top bar (search, Creio pill, help, bell, avatar); drawer under 960 |
| Focus flow | add Credits, payments, payout method, buy Creio | slim bar with close and title; left column (title, balance, steps, "What happens next"); right card; sticky actions on mobile |
| Outcome page | processing, failed, paid, connected, pending | emblem → status pill → heading → sub → card / next step → button → small links |
| Status track | pending payouts, processing payment | horizontal cobalt track; done = solid, current = dashed and moving |
| Printing receipt | payment success screens | receipt prints down (about 2 s), "Paid" stamp, then confetti; replays when the screen comes into view |
| Info tooltip | everywhere | navy bubble behind an ⓘ; explanations live here, not in extra paragraphs |
| Nova panel | Copilot | slides over any page; expands wide; Creio cost shown under the input |
| Message pop-ups | dashboard | stacked bottom-right on desktop; one card plus a "N new messages" bar on mobile |

Animations only run in the prototype's Play mode.

## Open items (client to confirm)

- Whether the MFORGE payment option stays.
- Waiting times (test deposit 1–2 business days, Payoneer / Tipalti 1–3), Tipalti "lower FX fees", validation decision time,
  and Creio bundle prices (25,000 = 25 Credits, 100,000 = 80, 250,000 = 175).
- Card fee on receipts is shown at 1.5% (sample).
