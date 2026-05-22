# Signal Graveyard
Status: Draft
Generated: 2026-05-22 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** Users can't tell if a dead signal failed or just stopped running. Algos that haven't fired in 60+ days vanish from view, leaving the story incomplete.
- **Goal:** Show every signal that has been retired or gone silent for 60+ days with its final stats, last trade date, and reason for retirement (if known). Make failure visible and complete.
- **Metric:** Engagement with retired algos section. % of users who view at least one dead signal per month. Retention lift among Receipts Guys.

## 2. User Stories

- As a Receipts Guy, I want to see the full history of failed signals with their final P&L and retirement date, so I can understand what didn't work and why.
- As a Signal Hunter, I want to know which signals tested poorly enough to get shelved, so I don't waste time re-discovering the same dead idea.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Create a separate view accessible from the leaderboard that shows all algos force-ranked below #100 or inactive for 60+ days, sorted by retirement date descending.
- **Requirement 2:** For each dead signal: show final rank, total trades, net P&L, Sharpe, max drawdown, last trade date, and a one-line operator note on why it died (e.g., 'stopped working after rate hike,' 'data source unreliable').
- **Requirement 3:** Graveyard is public (free users see it) but full detail (trade history, daily equity curve) is paid-only. Dead signals stay named — never replaced with generic labels.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Graveyard is a tab on the leaderboard, not a separate page. Dark background. Signals listed as cards with strike-through rank. No inspirational copy. This is a failure museum. The operator voice is: 'This one died. Here's why.'

## 5. Acceptance Criteria (AC)

- All algos inactive for 60+ days appear in the Graveyard with final stats intact and no data loss.
- Paid users can click any dead signal to see full trade history and equity curve; free users see only name, final rank, and P&L summary.
- Operator note field is optional but required for any algo retired due to known failure (not just natural expiration).

## 6. Out of Scope

- Un-retiring signals or restarting dead algos (that is operator-only).
- Automated categorization of failure reasons (all notes are hand-written by the operator).
