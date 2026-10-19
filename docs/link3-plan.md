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
