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

**4. NEW: cohort enrolment, COH-ENR-001…010** (18 boards incl. states). NOT designed.

**5. NEW: cohort operations, COH-OPS-001/002** (18 boards incl. states). NOT designed.

**6. NEW: programmes** (PRG-LE-001, PRG-MGT-001/002 + 13 states, PRG-FLOW). NOT designed.

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
