# Railway Deploy Checklist

## Purpose

This is the operator checklist for deploying the premium backend to Railway without guessing.

The goal is not "container starts."
The goal is "checkout, unlock, entitlement, and premium pages work end to end."

## 1. Service Setup

- [ ] Create a Railway service from this repo
- [ ] Set the Docker source to `backend/Dockerfile`
- [ ] Confirm Railway exposes `PORT`
- [ ] Confirm the service boots with:
  - `uvicorn backend.stockarithm_api:app --host 0.0.0.0 --port $PORT`

## 2. Required Env Vars

- [ ] `APP_ENV=prod`
- [ ] `STRIPE_SECRET_KEY=...`
- [ ] `STRIPE_WEBHOOK_SECRET=...`
- [ ] `JWT_SECRET=...`
- [ ] `APP_URL=https://stockarithm.com/app.html`
- [ ] `CORS_ORIGINS=https://stockarithm.com`
- [ ] `COOKIE_DOMAIN=.stockarithm.com`
- [ ] `COOKIE_SECURE=true`
- [ ] `PUBLIC_ARTIFACT_DIR=/app/docs/data/public`
- [ ] `PRIVATE_ARTIFACT_DIR=/app/private_artifacts`
- [ ] `ENTITLEMENTS_PATH=/app/data/premium/entitlements.json`
- [ ] `PROCESSED_EVENTS_PATH=/app/data/premium/stripe_events.json`

## 3. Domain / Routing

- [ ] Attach custom domain:
  - `api.stockarithm.com`
- [ ] Point DNS to Railway target
- [ ] Confirm HTTPS is active

## 4. Artifact Assumptions

- [ ] Confirm `private_artifacts/daily_report_detailed.html` exists in the deploy context or mounted storage
- [ ] Confirm `private_artifacts/daily_report_detailed.json` exists in the deploy context or mounted storage
- [ ] Confirm public artifacts are readable at:
  - `/app/docs/data/public`
- [ ] Decide whether Railway filesystem persistence is acceptable for July 1

## 5. Health Checks

- [ ] `GET /health` returns `200`
- [ ] `GET /api/me/status` returns free state when no cookie is present
- [ ] `GET /api/premium/leaderboard` returns `403/401` when no entitlement is present

## 6. Stripe Wiring

- [ ] Create Stripe webhook endpoint:
  - `https://api.stockarithm.com/webhook`
- [ ] Subscribe webhook to:
  - `checkout.session.completed`
  - `customer.subscription.updated`
  - `customer.subscription.deleted`
  - `invoice.paid`
- [ ] Confirm webhook signing secret matches Railway env var

## 7. End-to-End Paid Path

- [ ] Trigger a real Stripe test checkout
- [ ] Confirm success redirects to:
  - `/unlock?session_id=...`
- [ ] Confirm `/unlock` redirects to:
  - `https://stockarithm.com/app.html`
- [ ] Confirm the signed cookie is set on `.stockarithm.com`
- [ ] Confirm `GET /api/me/status` returns:
  - `authenticated=true`
  - `entitled=true`
- [ ] Confirm `docs/app.html` loads:
  - premium leaderboard
  - detailed daily report
- [ ] Confirm `GET /api/premium/download/daily_report_detailed` succeeds

## 8. Negative Tests

- [ ] Confirm no-cookie browser is denied premium endpoints
- [ ] Confirm invalid/expired cookie is denied
- [ ] Cancel the Stripe subscription in test mode
- [ ] Confirm webhook processes cancellation
- [ ] Confirm entitlement is removed
- [ ] Confirm premium app stops loading member content after cancel

## 9. Launch Readiness Call

Paid launch is only real if all are true:

- [ ] checkout completes
- [ ] unlock works
- [ ] cookie is set correctly
- [ ] premium app loads real member content
- [ ] webhook updates entitlement correctly
- [ ] cancellation removes access correctly
- [ ] no required env vars are missing
