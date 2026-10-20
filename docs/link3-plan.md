# Link 3 · plan and progress

Update this file at the end of every batch: what was done, and what's next.

## Where things are
- **Client Link 3 prototype** (content source + which buttons link where): https://claude.ai/artifact/Mg8o83iNa9x4ov1FxivdEW
  - Made outside our org. Read it as data with the Artifact tool (`action: read`, `path: project/<file>`). It has about 199 files; `canvas.json` gives the layout and section order.
  - Its INVENTORY / ENR-FLOW / PRG-FLOW boards explain the flows.
  - Local copy (version 1791978988-4949, 183 project files): `reference/link3/project/`. Most CR/AI/PM/MSG boards are thin wrappers over one big `CreatorHome.dc.html` (page/variant attrs).
- **Our Studio canvas** (Link 3 screens we already designed): https://claude.ai/artifact/CzyHQrVg4MbHzgqsSeZwY9 (local copy `design/canvas2/project/`, about 207 files; limit 512)
- **Old Link 2 prototype:** GCDVk2taFowXLcEABysm7u. Superseded by Link 3; ignore it.
- **Shared with Link 1:** CR-DASH-ST and CR-VAL-WS exist in both canvases. Change one, change both.
- **Screen checklist:** `screens.md` (sections 11–24).

## What Link 3 contains (2026-10-14 file list)
**1. Studio pages (CR-*, about 100 boards).** Mostly ALREADY DESIGNED in canvas2:
- wallet, pay, revalidation
- payouts, earnings
- course overview, discussions, calendar
- support, learners, analytics
- profile, settings, help, search
- Nova panel

Check for new IDs we don't have:
- CR-EARN-001n
- CR-PAYO-001h…001p, 005f/005p/005r
- CR-PROF-001e
- CR-ANA-002path, CR-ANA-003c
- CR-SEARCH-EMPTY
- CR-HELP-003e

**2. Nova / Creio (AI-*, 21 boards).** Mostly already designed as CR-CREIO-* / CR-NOVA-*. New IDs to check:
- AI-001n
- AI-003e
- AI-010c
- AI-EST
- CP-EXP

**3. Account menu PM-001…003 and message pop-ups MSG-001…006.** NOT designed yet.

**4. Cohort enrolment, COH-ENR-001…010.** OUT OF SCOPE: below the client's "DO NOT DESIGN ANYTHING BELOW THIS NOTE".

**5. Cohort operations, COH-OPS-001/002.** OUT OF SCOPE (same note).

**6. Programmes** (PRG-*). OUT OF SCOPE (same note). Also out: retired PAYO-002/003/004 ("DO NOT DESIGN THIS ROW").

## Suggested order
1. **Map Link 3 against canvas2.** Produce one list of:
   - already done
   - done but changed in Link 3
   - new screens
   - unwired buttons

   Show it to the designer before building.
2. Build the missing screens section by section, in client order, in small batches (10–15 screens per session).
3. Wire the links to match the client prototype.
4. Delivery QA and handoff, the same way as Link 1:
   - audit + cleancss
   - click-sweep
   - package zip
   - screenshots
   - screen book PDF
   - developer guide PDF

## Log
- 2026-10-14: Link 1 delivered. Designer: work on LINK 3 next (the old Link 2 link is dropped).
- 2026-10-14: Context pulled. canvas2 live = repo (no drift, 207 files). Client Link 3 saved to `reference/link3/`. Client says 174 screens / 16 sections; PAYO-002/003/004 are RETIRED there. Next: step 1 (mapping list) for the designer.
- 2026-10-15: Step 1 mapping list written: `docs/link3-map.md` (92 done, copy/rule changes, ≈80 new, 639 unwired). Waiting on designer review + 4 questions.
- 2026-10-15: Designer: yes to all 4 questions; client note "DO NOT DESIGN ANYTHING BELOW THIS NOTE" excludes all PRG/COH screens. Scope now 29 new screens (PM 3, MSG 6, 20 missing states) + client copy/rule changes + SET-007/AI-012 copy + Gold wording in both canvases. Next: build in batches.
- 2026-10-15: Canvas re-laid out in client Link 3 order (`design/generator/relayout_l3.py`): 92 done in place, 29 "Not done yet" notes, 2 "In the Link 1 canvas" notes (SET-007, AI-012), sources last. Only Studio canvas from now on; Link 1 untouched.
- 2026-10-17: Batch 1 done (Earnings & payouts, 10 screens): EARN-001n, PAYO-001h/i/j/k/m/n, PAYO-005f/p/r as variants of CR-EARN (none), CR-PAYO (poconnect/ticonnect/acherr), CR-PAYO-OUT (ach/tipalti/action), CR-PAYST (failed/paid/returned). Wired: provider Continue → its own step, Tipalti submit → 001m, ACH save → 001k, 005a fix → 001n, Earnings › Payout history → 006. Payout timing now "by 13 Nov" (client: first 10 business days). Rendered 20 boards: 0 page errors. Render setup: runtime from the Link 1 developer package (blobs offline). Left: 19 screens (PM 3, MSG 6, ANA 2, PROF-001e, SEARCH-EMPTY, HELP-003e, CP-EXP, AI-001n/003e/010c/EST) + client copy/rule changes + SET-007/AI-012 copy.
- 2026-10-18: Batch 1 trims (repeated copy out, causes into tooltips) + pink strips under new boards ("NEW · batch N").
- 2026-10-18: Batch 2 done (6): ANA-002path (CR-ANX path), ANA-003c (CR-ANA-003 cohorts + Courses/Cohorts switch), PROF-001e (CR-PROF expertise + Expertise tab), CR-AI-001x = client CP-EXP (CR-AI-001 expanded, expand/collapse button, hidden on mobile), SEARCH-EMPTY (CR-SEARCH-002 empty), HELP-003e (CR-HELPT error). 0 page errors; base screens re-checked. Left: 13 (AI-001n, AI-003e, AI-010c, AI-EST, AI-012 + SET-007 copy, PM 3, MSG 6) + client copy/rule changes.
- 2026-10-18: Batch 2 trims (Field dup, Milestones row, cohort chips, search card, topic error).
- 2026-10-18: Batch 3 done (5 + AI prefs): CR-NOVA-001n (variant new), CR-CREIO-003e (CREIO-BUY customerr: red field, min 10,000, Continue off), CR-CREIO-010c (NOVA crit, "Almost out"), CR-CREIO-EST (CREIO-011b estimate: cobalt estimate card, Run full review / Not now). CR-HOME-SET copied from Link 1 into the Studio canvas (SET-007 slot) + CR-AI-012 wrapper; blobs remapped; Maya/Alex/Sage uploaded to canvas2: Maya 19a0a700c34e0a72a8932d0f4c591087, Alex 33f355562e77cd0a80abdae30e56b6fb, Sage eb873f1cde95f0d8f34eb7b2fc6fa88d. 0 page errors. Left: PM 3, MSG 6 + client copy/rule changes (Gold validated still on COURSE-OV/011b/etc.).
- 2026-10-18: Batch 3 trims.
- 2026-10-19: Batch 4 done (9): CR-PM (new source, `design/generator/b4_1019.py` from LIVE CR-CREIO-POP; variants menu / one / switch = PM-001/002/003: avatar menu with status Available/Away/Do not disturb, Switch role Creator/Validator(2)/Learner, profile/settings/help/sign-out links; switch = focus page "Opening your Validator workspace"), CR-MSG (new source; pops / reply / sent / many / hidden = MSG-001…005; desktop stack bottom-right, mobile shows the newest only + "+N more" bar; gear → MSG-006), MSG-006 = CR-SET variant notifpop (pop-up section on top, highlighted) + new "Quick reply" switch in the pop-up section (SET-004 too). ALL client slots now filled (no "Not done yet" notes left). 0 page errors. Next: client copy/rule changes (link3-map.md section B: Gold/Silver validated, AI Coach → AI Course Assistant, Credits rules, SV codes), then wiring (step 3) and delivery QA (step 4).
- 2026-10-19: Batch 4 trims (role-row subtitles, Validator badge, switch pill).
- 2026-10-19: Client copy changes done (Studio canvas only; Link 1 untouched): Gold validated → Validated, Silver → Validated with recommendations, "Validation tiers explained" → "How validation works" (DASH-ST, COURSE-OV, AI-001a, CREIO-011b, PUB, SEARCH-002, PAY, HELP); AI Coach → AI Course Assistant / assistant (LRN-002, SUP); quote line "Standard Course Validation · Tier 2" / "Standard Revalidation · Tier 2" with SV-001 / SV-007 rule in a tooltip (CR-PAY); Credits rules tooltip on the wallet balance (oldest first, 365 / 90-day expiry). Already done earlier: payout timing, Creio max 1,000,000. Bank transfer was already an option. Note: Link 1's own DASH-ST, HOME-EXP, NOT-001, ORI-M4-L3 still say Gold (designer: leave Link 1). Next: wiring (step 3), then delivery QA (step 4).
- 2026-10-19: Full check vs client (version 1791978988, unchanged): 123 client screens above the "DO NOT DESIGN" note (excl. Main, INVENTORY, CreatorHome and the 3 retired payout boards) = 123 of ours, each with desktop + mobile; client inventory (174) minus the 51 below the note = 123, all matched; nothing extra on our side; 0 "Not done yet" notes; all 246 boards render with 0 page errors.

### 2026-10-19 · Step 3 · buttons wired (canvas v1792441516-96ea)
- Sidebar, top bar (Help, avatar → CR-PM-001, Creio pill → CR-CREIO-TOP, bell → CR-NOT-001) and page links wired in 39 sources; `#` links 639 → 75.
- Page links: readiness strip → KYC/CRED/ORI/POL; Nova Close/Not now → COURSE-OV-001; course "Review" → REVAL-002; Help articles/contact/requests/tickets → HELP-002/003/005/006; Settings nav (HOME-SET + SET) → SET-001…006, HOME-SET, ORG-SOON; learner rows → LRN-002; payout rows → PAYO-005p; WAL-001 View all/Manage → WAL-007/003; DASH-ST as in Link 1 + Fix now → PAYO-001n, Open discussions/calendar → DISC/CAL.
- Left as `#` on purpose (in-place actions, no screen): Save changes, Download/Export/receipt, Join call, Propose, Decline, Apply changes, Change/Edit/Connect/Sign out in Settings, Change photo, Mark resolved, help categories, CREIO-USE rows, PUB cards, VAL-WS (Link 1).
- OPEN: ~430 links point at Link 1-only boards (CR-HOME-EXP/NEW, CREATE-*, ASG, VAL-MC, CTR, RDY, NOT, KYC, CRED, ORI, POL, COL, DEC, LOG). They don't exist in the Studio canvas, so they do nothing there; fine in the merged developer package.
- 246 boards render, 0 page errors; audit = 12 known false positives.

### 2026-10-19 · Redesign: outcome + quote components (designer: "bad use of space / cluttered")
- Steps (WAL-005, PAYO-001g/k/m): desktop = horizontal cobalt track (done solid, current dashed + flowing), no card; provider = pill chip above it. Mobile keeps the vertical list. "Won't be charged twice" → ⓘ tooltip on the sub.
- Funded / paid (WAL-006, PAY-002f/r, CREIO-006c, PAY-003s): balance card + Next-for-you merged into ONE ticket (gradient stub with big number + receipt | perforated edge | next step + CTA).
- Quote (PAY-001, REVAL-002): balance pill removed from all headers; balance now sits in the footer next to the CTA ("110 short" amber / "1,760 left after").
- REVAL-001: "stays live" line moved into the footer next to the CTA, with a green dot.

### 2026-10-20 · Payment-complete receipt (designer reference: printing receipt video)
- CR-WAL-OUT success variants (WAL-006, PAY-002f/r, CREIO-006c, PAY-003s): printer slot + receipt that prints down (stepped, 2.2 s), green "Paid" stamp with the Credalio mark lands at ~2.4 s, then confetti. Zigzag bottom edge (CSS mask). Final state is the static view (editor shows it printed).
- Desktop: text column (pill, H1, sub, Next for you, links) left, receipt right, both vertically centred. Mobile: receipt first, then text and CTA.
- Replaces the ticket card. Funded receipt lines: Credits + card fee 1.5% = total; paid receipt lines: validator fees + service fee.
- Also this session: payment methods = 4 tiles (WAL-FUND), softer total separators, PAY-002 panel centred, spacing scan of all 246 boards (`design/tools/overlap.js`).
- 2026-10-20: Add Credits illustration (designer) = `design/illustrations/add-credits.webp`, Studio blob `/_blob/c2da5637e0727865bb6e7d2c12f6825e`, as the `.tk-scene` bottom layer in CR-WAL-FUND (WAL-002/003/004, CREIO-006b). Mobile: scene sits after the content (order:99), not behind the sticky bar.
- 2026-10-20 review of the first 20 screens (WAL-001…PAYO/EARN): outcome screens vertically centred on desktop (WAL-OUT, PAYO-OUT); failed-payment duplicate note removed; WAL-004 fine print → ⓘ on Total; WAL-001 sub trimmed + "Nothing waiting to clear" removed; PAY-002b duplicate line removed; PAYO connect forms (001b/c/d): Cancel is a ghost pill beside the primary. Open: PAY/REVAL left column stays empty until the designer's laptop illustration file arrives.
- 2026-10-20 review of screens 21–40 (PAYO-001…006): PAYO-001g connected + 001n action needed rebuilt to the chip pattern (provider pill with Verified ⓘ + Change; one Next-for-you card; payout-waits line folded into the sub). Rest consistent, no change.
- 2026-10-20 review of screens 41–60 (COURSE-OV, DISC, CAL, SUP, LRN, ANA-001/004): only CAL-001a agenda changed (list + month side card like the day view, list no longer half width). Rest consistent.
- 2026-10-20 review of screens 61–80 (ANA-002…003c, PROF, ORG-SOON, SET-001…008, HOME-SET): only PROF-001c changed (same 'How learners see you' preview as the other tabs, with its verified credentials). Rest consistent.
- 2026-10-20 review of screens 81–100 (AI panel, SEARCH, HELP, NOVA, CREIO-002…004): HELP-003/003e contact form gets a 'Quick answers' side card (desktop only); HELP-004 and CREIO-005 outcome screens centred vertically on desktop like the other outcomes. Rest consistent.
- 2026-10-20 review of screens 101–123 (CREIO-005…EST, AI-012, PM, MSG): CREIO-006/006d status panels centred (matches PAY-002); PM-003 switch page centred vertically. Full 123-screen pass done.
- 2026-10-20 coin pass (designer: missing coins): gold Creio coin on Get more Creio packages, 'You'll get' and review '+100,000'; cobalt Credits coin on 'Wallet after'; gold coin on Nova '27,550 Creio used'. Rule: headline/selectable amounts carry their coin; line items and list rows keep the 'Cr' suffix only. Checker: design/tools/coins.js.
- 2026-10-20 coins in lists: cobalt Credits coin before every amount in WAL-001 Recent activity and WAL-007 Transactions (CSS ::before, 'Cr' suffix dropped); gold Creio coin in CREIO-USE list. Old pale outline Credits icon (.cr-ic) switched to the solid cobalt coin in PAY, WAL-001, WAL-FUND, CREIO-BUY.
- 2026-10-20: PM-003 'Opening your Validator workspace' illustration (designer) = design/illustrations/validator-switch.webp, Studio blob /_blob/cefeb2ed55579c524fd4ec636cb7cff1, bottom band .rs-scene (desktop cover min(48vh,33.5vw); mobile 250px, figure kept in view).
- 2026-10-20: sidebar/back-link label 'My learning experiences' → 'My Creations' (designer) in all 37 Studio sources. Link 1 canvas not changed. Generic 'learning experiences' copy (search placeholder, filters, body text) unchanged.
- 2026-10-20: pink 'NEW · batch' strips (31 notes) removed and header note shortened for the client review.
