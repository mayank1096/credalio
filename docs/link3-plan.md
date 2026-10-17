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
