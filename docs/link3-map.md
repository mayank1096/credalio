# Link 3 · mapping list (client vs our Studio canvas)

Client Link 3 (Mg8o83iNa9x4ov1FxivdEW, version 1791978988) vs our Studio canvas (CzyHQrVg4MbHzgqsSeZwY9).
Client inventory: 174 screens in 16 sections. Compared with the old Link 2 file we designed from (GCDVk2taFowXLcEABysm7u): **same 182 boards, nothing added or removed**, but the client rewrote the copy across the Studio pages (see B).

## A. Already done (92 screens, desktop + mobile)

| Client section | Client | Ours |
|---|---|---|
| Credit Wallet | WAL-001…007, 005f | same IDs (8) |
| Payments & revalidation | PAY-001, 002, 002b/f/r, 003, 003s, REVAL-001/002 | same IDs (9) |
| Earnings & payouts | EARN-001, 001b, PAYO-001, 001a–e, 001g, 001p, 005, 005a, 006 | same IDs (13) |
| Course overview & discussions | COURSE-OV-001, DISC-001, 001u, 002, 002b, 003 | same IDs (6) |
| Calendar | CAL-001, 001a/d/w, 002–005 | same IDs (8) |
| Support, learners, analytics | SUP-001/002, LRN-001/002, ANA-001, 002, 002c, 002p, 003, 004 | same IDs (10) |
| Profile + My Organizations | PROF-001, 001c, 001v, 002, ORG-SOON | same IDs (5) |
| Settings | SET-001, 002d, 003–006, 008 | same IDs (7) |
| Copilot, search, help | CR-AI-001, 001a, 003, SEARCH-002, HELP-001…006 | same IDs (10) |
| Creio overview & buy | AI-001, 002, 003, 003c, 004, 005 | NOVA-001, CREIO-002, 003, 003c, 004, 005 |
| Creio · not enough Credits | AI-006, 006b/c/d | CREIO-006, 006b/c/d |
| Creio · usage, low, empty, chip | AI-007, 010, 010b, 011, 011b, AI-TOP | CREIO-USE, 010, 010b, 011, 011b, TOP |

In the **Link 1 canvas** (CR-HOME-SET), not in the Studio canvas: SET-007 AI preferences, AI-012 Copilot preferences.

## B. Done, but changed by the client (copy and rules)

Applies to all Studio pages: sentence case, screen-ID eyebrows and `[TO CONFIRM]` placeholders removed, US spelling ("authorized", "organization").

| Change | Our screens affected |
|---|---|
| Metal tiers gone: "Gold validated / Silver" → "Validated" / "Approved with recommendations" | AI-001a, COURSE-OV-001, CREIO-011b, PAY, PUB, SEARCH-002, **DASH-ST (shared with Link 1)** |
| "AI Coach" → "AI Course Assistant"; learner button "Ask the Creator" | LRN-002, SUP |
| Credits rules now stated: 10 Credits = $1, oldest spent first, purchased expire after 365 days, promotional after 90 | WAL-001, WAL-007 (check), DASH-ST mentions expiry |
| Creio buy rules: minimum 10,000, rounded to 1,000, 0.8 Credits per 1,000 Creio, up to 1,000,000 at once | CREIO-BUY (has min + rate; add max) |
| Payouts automatic, sent within the first 10 business days of the month (no request) | EARN, PAYST (check wording) |
| Validation quote shows service code + tier: "Standard Course Validation (SV-001) · Tier 2 · 11 to 30 learning hours" | PAY |
| Revalidation: "Standard Revalidation (SV-007) · Tier 2 · up to 50% changed content"; bigger changes → Major Revalidation with a new quote | REVAL-001/002 |
| Payment options include MFORGE Wallet and bank transfer | WAL-FUND (has MFORGE; check bank transfer) |

Rules stay "design, don't copy": we keep our layouts and copy, but terms and rules should match the client.

## C. New screens to design (≈80)

**1. Enrolment & learner roster (27):**
- COH-OPS-002 roster states (9): active, completed, cancelled, upcoming, empty, error, loading, instructor view, Requests tab
- COH-ENR-001 learner drawer (3: default, DLP short, payment ok · confirmation failed)
- COH-ENR-002 invite (2: open cohort, closed → exception request)
- COH-ENR-003 request reviews (4: payment reconciliation, late exception, approve, offer next cohort)
- COH-ENR-004 waitlist, 005 seat offer, 006 withdraw, 007 transfer (3), 008 suspend, 009 audit history, 010 bulk actions

**2. Programme cohorts & cohort overview (24):**
- PRG-LE-001 My learning experiences (programme row), PRG-MGT-001 programme overview
- PRG-MGT-002 programme cohorts + 13 states (after publish, delete draft, cancel, archive, 3 empties, instructor, loading, error, validation expired, new version in validation)
- COH-OPS-001 cohort overview (9: active, upcoming, completed, cancelled, pending changes, instructor, loading, partial failure, unauthorized)

**3. Account menu (3):** PM-001, PM-002, PM-003

**4. Message pop-ups (6):** MSG-001…006

**5. Missing states of screens we have (20):**
- Earnings/payouts (10): EARN-001n no payout method · PAYO-001h Payoneer connect · 001i Tipalti open · 001j ACH error · 001k ACH test deposit pending · 001m Tipalti pending · 001n action required · PAYO-005f failed · 005p paid · 005r returned by bank
- Analytics (2): ANA-002path career path · ANA-003c compare cohorts
- PROF-001e Expertise tab · SEARCH-EMPTY no results · HELP-003e form error
- Creio (5): AI-001n new creator starting balance · AI-003e custom amount below minimum · AI-010c critical balance · AI-EST estimate before a large action · CP-EXP Copilot panel expanded

**Retired by the client, not needed:** PAYO-002/003/004 (manual payout request).

## D. Unwired buttons

639 `href="#"` across 37 Studio files (510 already linked). Most are the shared sidebar/top bar repeated on every page. Wire to match the client prototype in step 3.

## E. Questions for the designer

1. DASH-ST is shared with Link 1. Change "Gold validated" in both canvases?
2. SET-007 / AI-012 live in Link 1's CR-HOME-SET. Bring a copy into the Studio canvas so Link 3 is complete on its own?
3. Client placeholders still open: [REFUND POLICY], [POST-COHORT ACCESS PERIOD]. Show them as-is?
4. Add / edit / publish a cohort happen on the client's Learning Program Studio canvas (LP-STU-030/031/032, COH-PUB-001), which isn't in Link 3. Out of scope?

File budget: 207 now + ≈80 screens × 2 boards + ≈15 sources ≈ 380 of 512.
