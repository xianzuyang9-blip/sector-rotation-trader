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
- Public messaging still says:
  - `No checkout yet. Waitlist first, paid launch July 1.`

## Launch Decision

### 1. Decide what July 1 means
- [ ] Decide whether July 1 is:
  - a real paid launch
  - or a traction / readiness checkpoint
- [ ] If it is not a real paid launch, update public copy so the site does not imply otherwise

## Paid Surface Definition

### 2. Lock the free vs paid boundary
- [ ] Define exactly what stays free
- [ ] Define exactly what becomes paid
- [ ] Write one source-of-truth matrix for:
  - public page / endpoint
  - free or paid
  - current state
  - July 1 state

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

