# Receipts Export (CSV + Trade Log)
Status: Draft
Generated: 2026-06-05 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** Receipts Guy wants to pull the full audit trail — every trade, every loss, every signal that misfired — into his own tools to verify the lab isn't cherry-picking or hiding results. Currently, he can only see summaries on the UI.
- **Goal:** Give subscribers a one-click export of complete trade history (date, algo, entry, exit, P&L, signal rationale) so they can audit the lab independently and feed data into their own analysis.
- **Metric:** % of paid users who export at least once per quarter; average rows per export (proxy for depth of audit engagement).

## 2. User Stories

- As the Receipts Guy, I want to download every trade from every algo as a CSV so I can load it into my own notebook and verify the numbers match the leaderboard.
- As the Alt-Data Nerd, I want the export to include the signal input (e.g., 'Receipt count was +15%') so I can see the raw reason each trade fired and spot patterns the lab might have missed.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Export includes: Algo Name, Trade Date, Entry Price, Exit Price, P&L ($), P&L (%), Signal Input (if logged), Trade Status (Closed/Open). No rows omitted; losses and cancelled trades are included.
- **Requirement 2:** CSV generation is server-side; exports are timestamped and available for 30 days in subscriber account. No limit on download frequency.
- **Requirement 3:** Export respects subscription tier: free users get a summary (weekly aggregate); paid users get full trade-by-trade detail.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Button lives on the leaderboard header or algo detail page. Label: 'Export Receipts.' Click → dialog → download immediately (no email, no wizard). Filename: 'stockarithm_[algo-name]_[date].csv'. No onboarding; if a user wants receipts, they know what they want.

## 5. Acceptance Criteria (AC)

- Export includes trades with P&L = $0 and cancelled trades; no silent filtering.
- CSV is UTF-8 encoded and opens correctly in Excel, Google Sheets, and pandas without data loss or encoding errors.
- A user who exports the same algo twice on the same day gets identical CSVs (idempotent); export is based on settlement time, not request time.

## 6. Out of Scope

- Real-time streaming or API access; CSV export is the interface.
- Custom column selection or filtered exports; we give you everything or nothing so no one can claim we gave them a curated view.
