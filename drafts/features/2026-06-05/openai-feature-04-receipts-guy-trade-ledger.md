# Receipts Guy Trade Ledger
Status: Draft
Generated: 2026-06-05 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Receipts Guy users want raw, unfiltered trade logs for each signal that show every trade’s exact timestamp, price, and outcome to verify no cherry-picking.
- **Goal:** Provide a public trade ledger per signal with full transparency on all live trades, including losing trades and no-trade periods.
- **Metric:** Increase number of trade ledger views by Receipts Guy users by 30%.

## 2. User Stories

- As a Receipts Guy, I want to download or view a full trade ledger per signal so I can audit its real-world performance without filters.
- As a Receipts Guy, I want to see explicit no-trade days called out so I know when signals went silent.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Expose a paginated trade ledger table per signal with date/time, action, price, P&L, and trade notes.
- **Requirement 2:** Show explicit markers for days with zero trades.
- **Requirement 3:** Allow CSV export of the trade ledger for offline analysis.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Ledger uses monospace font and a utilitarian table style with no decoration, emphasizing raw data over prettiness.

## 5. Acceptance Criteria (AC)

- Trade ledger loads fully on desktop and mobile browsers with pagination.
- CSV export matches on-screen data exactly with all trades and no-trade days.
- No hiding or smoothing of losing trades or silent periods.

## 6. Out of Scope

- No summary stats or visualizations in the ledger view.
- No trade editing or deletion by users.
