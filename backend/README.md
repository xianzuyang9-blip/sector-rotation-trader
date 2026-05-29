# Stockarithm Premium API

Small FastAPI/Railway backend for Stripe-backed premium access. Build and test this with Stripe test mode first; live mode is only an environment-variable swap later.

## Local Run

```bash
pip install -r backend/requirements.txt
uvicorn backend.stockarithm_api:app --reload --port 8080
```

## Docker Run

Build from the repo root so the backend can see `docs/data/public`, `private_artifacts`, and the current state files it still reads during staging.

```bash
docker build -f backend/Dockerfile -t stockarithm-premium .
docker run --rm -p 8080:8080 \
  -e APP_ENV=prod \
  -e STRIPE_SECRET_KEY=sk_test_... \
  -e STRIPE_WEBHOOK_SECRET=whsec_... \
  -e JWT_SECRET=replace-me \
  -e APP_URL=https://stockarithm.com/app.html \
  -e CORS_ORIGINS=https://stockarithm.com \
  stockarithm-premium
```

Railway can deploy this directly from `backend/Dockerfile`.

Use `backend/RAILWAY_DEPLOY_CHECKLIST.md` as the operator checklist before calling the deploy real.

## Required Env For Stripe Test Mode

```bash
APP_ENV=prod
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
JWT_SECRET=<random-long-secret>
APP_URL=https://stockarithm.com/app.html
CORS_ORIGINS=https://stockarithm.com,http://localhost:8000
```

Optional:

```bash
PRIVATE_ARTIFACT_DIR=private_artifacts
PUBLIC_ARTIFACT_DIR=docs/data/public
ENTITLEMENTS_PATH=data/premium/entitlements.json
PROCESSED_EVENTS_PATH=data/premium/stripe_events.json
COOKIE_DOMAIN=.stockarithm.com
COOKIE_SECURE=true
```

## Flow

1. Stripe Checkout completes in test mode.
2. Stripe calls `POST /webhook` with `checkout.session.completed`.
3. Backend stores the customer email as premium-entitled.
4. User lands on `/unlock?session_id=cs_test_...`.
5. Backend verifies the Checkout Session with Stripe, sets a signed HTTP-only cookie, and redirects to `APP_URL`.
6. `docs/app.html` or any premium frontend calls `/api/me/status` and premium endpoints with credentials included.

## Endpoints

- `GET /health`
- `GET /unlock?session_id=...`
- `POST /webhook`
- `GET /api/me/status`
- `GET /api/premium/leaderboard`
- `GET /api/premium/daily-report`
- `GET /api/premium/signal/{algo_id}`
- `GET /api/premium/ticker/{symbol}`
- `GET /api/premium/download/algo_performance`
- `GET /api/premium/download/signals_today`
- `GET /api/premium/download/trade_history`
- `GET /api/premium/download/daily_report_detailed`

## Notes

- Stripe is the source of truth for payment.
- The backend only stores entitlement state and signed sessions.
- Auth0 is intentionally not used: no passwords, teams, SSO, or account lifecycle needed for launch.
- `PRIVATE_ARTIFACT_DIR` is checked first; public artifacts are fallback only so the API can be tested before private publishing exists.
- In non-`dev` mode the backend now fails closed if `JWT_SECRET`, `STRIPE_SECRET_KEY`, or `STRIPE_WEBHOOK_SECRET` are missing.
- Do not bake private artifacts into the image as a long-term storage model. The container should read current artifacts from Railway storage or another mounted/persistent path.
