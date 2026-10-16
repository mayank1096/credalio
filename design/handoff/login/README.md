# Credalio · Log in and password reset (Link 1 addition)

This package adds **10 screens** to the Link 1 handoff. Everything else (foundations, tokens, patterns) is the same as the main Link 1 package and its README.

**To open it:** unzip, then in the folder run `python3 -m http.server 8000` and open http://localhost:8000.
Opening the files straight from disk with `file://` won't work, because browsers block the scripts.

## Screens

There are 3 source files. Each state is a variant of its source; build one component per source with a `variant` prop.

| Board | What it shows | Source · variant |
|---|---|---|
| CR-LOG-001 | Log in | `CR-LOG-001` (default) |
| CR-LOG-001a | Check your details: field errors (incomplete email, empty password) | `CR-LOG-001` · `invalid` |
| CR-LOG-001b | Wrong email or password: red message above the form, both fields marked | `CR-LOG-001` · `wrong` |
| CR-LOG-001c | Email not confirmed: amber message with "Resend link" | `CR-LOG-001` · `unverified` |
| CR-LOG-001d | Too many attempts: amber message, Log in disabled for 15 minutes | `CR-LOG-001` · `locked` |
| CR-LOG-002 | Forgot your password: email + "Send reset link" | `CR-LOG-002` (default) |
| CR-LOG-002b | Reset link sent: "Check your inbox" | `CR-LOG-002` · `sent` |
| CR-LOG-003 | Choose a new password: same strength check as sign-up (8+ characters, a number, a symbol) | `CR-LOG-003` (default) |
| CR-LOG-003b | Password updated: success, green tick and confetti | `CR-LOG-003` · `done` |
| CR-LOG-003c | Reset link expired: amber, "Send a new link" | `CR-LOG-003` · `expired` |

`CR-LOG-001-Mobile` and the other `-Mobile` files are 390-wide previews of the same responsive file. They are not separate designs.

## Flow

- **Log in** goes to the first dashboard (`CR-DASH-NEW`). Google and Apple do the same.
- **"Create account"** (top right) goes to sign-up (`Main`, "Begin your journey").
- **Forgot password?** (and the links inside the error messages) go to `CR-LOG-002`.
- **Send reset link** goes to `CR-LOG-002b`. **Open email** stands in for the link in the email and goes to `CR-LOG-003`.
- **Save password** goes to `CR-LOG-003b`, then **Log in** goes back to `CR-LOG-001`.
- An expired link shows `CR-LOG-003c`; **Send a new link** goes back to `CR-LOG-002`.
- The "Log in" button on the sign-up screens (ONB-001, 002, 002S, 003) now opens `CR-LOG-001`.

Links to screens outside this package (dashboard, sign-up) point to the main Link 1 package. "Resend link" is `#` (an action, not a screen).

## Notes for the build

- **Errors:**
  - Field errors use the same red border + one error line under the field as sign-up (`.ob-bad`, `.ob-err`).
  - Form-level messages (`.lg-al`) sit between the subtitle and the fields: red for a wrong email or password, amber for anything the person has to act on (confirm email, wait or reset).
- **Locked:** the Log in button is disabled (`aria-disabled="true"`, `.lg-off`). Show the real remaining time if the backend gives it.
- **Reset link sent:** never confirm whether an account exists ("If there's an account for …").
- **Outcome screens** (003b, 003c) use the standard outcome emblem: a green tick for success, an amber clock for expired. The top glow uses the same status colour. The confetti only plays in success states.
- **Images used:** `auth-scene.webp` (the scene along the bottom of every log-in and sign-up page; on short laptop screens a soft white glow behind the form keeps the figures from clashing with it), `wave.webp` (animated waving hand on "Welcome back."), plus the logo.
