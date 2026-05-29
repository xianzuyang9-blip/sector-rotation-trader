# July 1 Paywall Checklist

## Purpose

This checklist is the technical inventory for deciding whether StockArithm can support a real paid launch on July 1.

The goal is not "some premium code exists."
The goal is "a user can pay, get access, keep access correctly, and understand what they bought."

## Current Read

- Backend exists: `backend/stockarithm_api.py`
- Premium app shell exists: `docs/app.html`
- Premium teaser page exists: `docs/premium.html`
- Stripe-backed entitlement flow exists in code, but is not yet proven end to end
- July 1 is a real paid launch
- Public messaging is now behind reality and still says:
  - `No checkout yet. Waitlist first, paid launch July 1.`

## Launch Decision

### 1. Decide what July 1 means
- [x] July 1 is a real paid launch
- [ ] Update public copy so the site reflects a real paid path, not a preview-only state

## Paid Surface Definition

### 2. Lock the free vs paid boundary
- [x] Define exactly what stays free
- [x] Define exactly what becomes paid
- [x] Write one source-of-truth matrix for:
  - public page / endpoint
  - free or paid
  - current state
  - July 1 state

#### Free vs Paid Matrix

| Surface / Asset | Free | Paid | Current State | July 1 State | Repo Path / Endpoint | Match Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Homepage | Yes | No | Public | Public | `docs/index.html`, `docs/landing.html` | Already matches | Front-door explanation and proof stay public. |
| Glossary | Yes | No | Public | Public | `docs/glossary.html` | Already matches | Needed for comprehension. |
| Public Changelog | Yes | No | Public | Public | `docs/public-changelog.html` | Already matches | Trust layer. |
| Algo Changelog | Yes | No | Public | Public | `docs/algo-changelog.html` | Already matches | Trust and lab evolution. |
| Blog / selected public posts | Yes | No | Public | Public | `docs/blog/` | Already matches | Top-of-funnel content. |
| Signal index | Yes | No | Public | Public | `docs/signals/index.html` | Already matches | Full inventory stays visible. |
| Public signal summary pages | Yes | No | Public | Public | `docs/signals/*.html` | Already matches | Plain-English summaries stay free. |
| Biscotti public page | Yes | No | Public | Public | `docs/biscotti.html` | Already matches | Flagship public proof page. |
| Public leaderboard | Yes | Partial | Public stripped version exists | Keep stripped teaser public | `docs/leaderboard.html` | Needs change | Must stay teaser-only and avoid leaking full paid depth. |
| Full leaderboard | No | Yes | Not yet wired behind paywall | Paid | `docs/app.html`, `/api/premium/leaderboard` | Missing | Paid member path needs real wiring. |
| Public daily report | Yes | Partial | Public report exists | Keep lighter proof version public | `docs/daily.html` | Needs change | Needs explicit public-vs-paid split. |
| Detailed daily report | No | Yes | Not yet split cleanly | Paid | `docs/daily.html`, `/api/premium/download/{kind}` or private artifact | Missing | Detailed version is not yet defined as a separate paid surface. |
| Full algo dashboards/pages | No | Yes | Public files exist today | Move behind paywall | `docs/normal/*/index.html`, `docs/crazy/*/index.html`, `/api/premium/signal/{algo_id}` | Needs change | Public files should stop being publicly published. |
| Biscotti full dashboard | No | Yes | Public Biscotti preview exists | Keep preview public, gate full dashboard depth | `docs/biscotti.html`, `docs/normal/biscotti/index.html` | Needs change | Keep preview page free; gate detailed dashboard. |
| Weekly notes | No | Yes | Content system exists; paid path not wired | Paid | `marketing/content/*/substack.md`, `substack_note.md` | Missing | Need delivery model and entitlement gating. |
| Premium summaries | No | Yes | Teased, not fully defined | Paid | `docs/premium.html`, premium artifacts TBD | Missing | Promise must be narrowed or implemented. |
| Downloadable premium artifacts | No | Yes | API stubs exist | Paid if ready; otherwise defer | `/api/premium/download/{kind}` | Partial | Endpoint exists in code; actual private artifacts and entitlement path not proven. |
| `/api/premium/leaderboard` | No | Yes | Code exists | Paid | `backend/stockarithm_api.py` | Partial | Needs deploy and end-to-end test. |
| `/api/premium/signal/{algo_id}` | No | Yes | Code exists | Paid | `backend/stockarithm_api.py` | Partial | Needs deploy and real private artifact source. |
| `/api/premium/ticker/{symbol}` | No | Yes | Code exists | Paid | `backend/stockarithm_api.py` | Partial | Needs deploy and end-to-end test. |
| `/api/premium/download/{kind}` | No | Yes | Code exists | Paid | `backend/stockarithm_api.py` | Partial | Needs actual private files and access test. |

### 3. Confirm premium promise matches real assets
- [ ] Verify the promised premium assets actually exist:
  - full leaderboard
  - full per-algo detail
  - full per-ticker detail
  - trade history
  - equity curves
  - premium summaries / notes
- [ ] Remove or soften any premium claim that is not real yet

## Checkout Flow

### 4. Verify the buy path
- [ ] Confirm where checkout sessions are created
- [ ] Confirm the checkout button / CTA is wired to a real Stripe flow
- [ ] Confirm success redirects into `/unlock?session_id=...`
- [ ] Confirm cancel / failure path is sane and does not leave the user in limbo

### 5. Verify `/unlock`
- [ ] Confirm `/unlock` accepts the Stripe session id
- [ ] Confirm it verifies payment completion correctly
- [ ] Confirm it sets the session cookie correctly
- [ ] Confirm it redirects the user to the correct app surface

## Entitlements

### 6. Verify entitlement lifecycle
- [ ] Test anonymous user
- [ ] Test newly paid user
- [ ] Test returning paid user with valid cookie
- [ ] Test expired / invalid cookie
- [ ] Test canceled subscription
- [ ] Test subscription update / renewal path

### 7. Review entitlement storage
- [ ] Confirm whether file-backed entitlements are acceptable for July 1
- [ ] If yes, document the operational risks and backup plan
- [ ] If no, move entitlement state to a more reliable persistent store

Files involved:
- `data/premium/entitlements.json`
- `data/premium/stripe_events.json`

## Webhooks

### 8. Verify Stripe webhook handling
- [ ] Confirm Railway receives Stripe webhook traffic
- [ ] Confirm signature verification works in the deployed environment
- [ ] Confirm these event types are tested:
  - `checkout.session.completed`
  - `customer.subscription.updated`
  - `customer.subscription.deleted`
  - `invoice.paid`
- [ ] Confirm duplicate event replay is safe

### 8a. Run the real paid-path test
- [ ] Create a real Stripe checkout session from the production premium CTA
- [ ] Complete checkout with a controlled test customer
- [ ] Confirm success redirects to `/unlock?session_id=...`
- [ ] Confirm `/unlock` sets the signed session cookie and redirects to `app.html`
- [ ] Confirm `GET /api/me/status` returns `authenticated=true` and `entitled=true`
- [ ] Confirm `GET /api/premium/leaderboard` loads in `docs/app.html`
- [ ] Confirm `GET /api/premium/daily-report` loads in `docs/app.html`
- [ ] Confirm `GET /api/premium/download/daily_report_detailed` succeeds for the entitled user
- [ ] Confirm the matching Stripe webhook events were received and recorded
- [ ] Confirm a browser without the cookie is denied correctly
- [ ] Cancel the subscription and confirm access is removed on the next entitlement check

## Premium API

### 9. Verify gated endpoints
- [ ] `/api/me/status`
- [ ] `/api/premium/leaderboard`
- [ ] `/api/premium/signal/{algo_id}`
- [ ] `/api/premium/ticker/{symbol}`
- [ ] `/api/premium/download/{kind}`

For each endpoint:
- [ ] anonymous user is denied correctly
- [ ] entitled user succeeds
- [ ] error state is understandable

## Premium UX

### 10. Harden the premium app shell
- [ ] Improve `docs/app.html` status states
- [ ] Make unauthenticated vs not-entitled states clearer
- [ ] Add clearer next actions after unlock
- [ ] Decide whether `docs/app.html` is enough for July 1 or needs a more complete member UI

### 11. Align public teaser copy
- [ ] Update `docs/premium.html` once the launch decision is real
- [ ] Remove stale copy like `No checkout yet` once checkout exists
- [ ] Keep the teaser honest if July 1 becomes a soft launch instead

## Ops / Deployment

### 12. Verify deployment environment
- [ ] Confirm Railway env vars are present:
  - `STRIPE_SECRET_KEY`
  - `STRIPE_WEBHOOK_SECRET`
  - `JWT_SECRET` / `PREMIUM_JWT_SECRET`
  - `COOKIE_DOMAIN`
  - `APP_URL`
  - `PUBLIC_ARTIFACT_DIR`
  - `PRIVATE_ARTIFACT_DIR`
- [ ] Confirm `api.stockarithm.com` is the correct production API host
- [ ] Confirm CORS and cookie settings work with the production site domain

### 13. Confirm support / recovery posture
- [ ] Decide how to manually grant or revoke access if Stripe or webhook processing misbehaves
- [ ] Decide how to inspect current entitlements quickly during launch week
- [ ] Write a small operator runbook for refund / cancel / support cases

## Go / No-Go

### 14. Paid launch can only be called real if all of these are true
- [ ] A user can pay successfully
- [ ] Access unlocks immediately
- [ ] Access persists correctly
- [ ] Canceled access is removed correctly
- [ ] Paid assets are actually worth gating
- [ ] Public copy accurately reflects the state of the system

## Recommendation

Current likely order of work:
1. define the paid surface matrix
2. verify the checkout creation + `/unlock` path
3. verify webhooks and entitlement persistence
4. test the gated endpoints end to end
5. reconcile `docs/premium.html` with reality
