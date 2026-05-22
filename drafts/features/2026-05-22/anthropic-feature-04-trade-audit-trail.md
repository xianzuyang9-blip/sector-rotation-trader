# Trade Audit Trail
Status: Draft
Generated: 2026-05-22 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** Paid users can see trade history, but they can't easily verify that a signal is actually executing as described or spot accidental trades / logic gaps. Trust but verify is hard.
- **Goal:** Give users a per-signal trade log with entry/exit logic flagged, slippage recorded, and any anomalies (e.g., trade at unusual time, gap-filled entry) highlighted. No handholding — just show the work.
- **Metric:** % of paid users who view Trade Audit Trail at least once per month. Time spent on audit trail view. Support questions about signal execution logic.

## 2. User Stories

- As a Receipts Guy, I want to see the exact entry and exit logic for every trade (why the signal fired, what triggered the close), so I can verify the operator is doing what they claim.
- As a Signal Hunter, I want to spot any unusual trade execution (gap fills, slippage spikes, trades outside market hours) so I know if a signal's returns are real or inflated by luck.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Add 'Trade Audit' tab to signal detail showing a dense log: date | time | side | price | quantity | entry logic | exit logic | slippage | anomaly flags. One row per trade.
- **Requirement 2:** Entry/exit logic is a human-readable snippet (e.g., 'LONG: receipt sentiment >75th, RSI <30,' 'EXIT: close above 20D MA') pulled from the signal code comments or operator annotation.
- **Requirement 3:** Anomaly detection: flag trades executed outside 9:30-16:00 ET, gap fills, slippage >1%, order fills at limit price. No interpretation — just the fact.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Audit trail is a scrollable table, sortable by date/slippage/anomalies. Dense, technical, no smoothing. Anomaly flags are small red badges; hovering shows the deviation in basis points. Free users don't see this view. The operator voice: 'Here is what happened. Judge for yourself.'

## 5. Acceptance Criteria (AC)

- Trade Audit logs all fills for a signal with correct entry/exit logic and slippage calculation (no null values).
- Anomaly flags are accurate: gap fills detected if entry price is >0.5% away from previous close, slippage calculated as entry price vs VWAP at entry time.
- Entry/exit logic is readable without opening the signal code (operator provides plain-English annotations if code is too complex).

## 6. Out of Scope

- Automated trade-by-trade performance attribution or 'why this trade won' explanations.
- User-initiated trade adjustments or backtesting scenarios based on audit data.
