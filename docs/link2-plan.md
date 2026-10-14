# Link 2 (phase 2) · plan and progress

Update this file at the end of every batch: what was done, and what's next.

## Where things are
- **Our Studio canvas:** https://claude.ai/artifact/CzyHQrVg4MbHzgqsSeZwY9 (local copy `design/canvas2/project/`, about 207 files; limit 512)
- **Client Link 2 prototype:** artifact GCDVk2taFowXLcEABysm7u. It's the content source and shows which buttons link where.
- **Shared with Link 1:** CR-DASH-ST and CR-VAL-WS exist in both canvases. Change one, change both.
- **Screen checklist:** `screens.md` sections 11–24.

## Status (2026-10-14)
Most Link 2 screens were designed during Link 1 work:
- Wallet
- Payments and revalidation
- Earnings and payouts
- Course overview and discussions
- Calendar
- Support, learners and analytics
- Profile
- Settings
- Copilot panel
- Search and help
- Creio

See `docs/history.md` (build21…build38) for how each was built.

**Not designed yet:**
- [ ] `AI-EST`: large AI action, estimate before running (full course review)
- [ ] `PM-001`: account menu (status, profile, switch role, settings, sign out)
- [ ] `PM-002`: account menu, one role (no switcher)
- [ ] `PM-003`: switching role (Validator workspace opens)
- [ ] `MSG-001`: message pop-ups (learner, team, validator), each opening the exact message
- [ ] `MSG-002`: quick reply to a learner from the pop-up
- [ ] `MSG-003`: quick reply sent
- [ ] `MSG-004`: more than 3, collapsed into "+3 more · View all"
- [ ] `MSG-005`: preview hidden (screen-sharing setting)
- [ ] `MSG-006`: Settings › Notifications, pop-up preferences

## Suggested order
1. **Check the client's Link 2 prototype against canvas2:** find missing screens, missing states and unwired buttons. Report this to the designer before building.
2. Design the 10 missing screens above.
3. Wire the Link 2 links (same approach as Link 1, `design/generator/wire1014.py`).
4. Delivery QA and handoff, the same way as Link 1:
   - audit + cleancss
   - click-sweep
   - package zip
   - screenshots
   - screen book PDF
   - developer guide PDF

## Log
- 2026-10-14: plan created; Link 1 delivered.
