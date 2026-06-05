# Rolling P&L vs SPY Comparison Chart
Status: Draft
Generated: 2026-06-05 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** Alt-Data Nerd and Signal Hunter want to see whether a signal is actually outperforming SPY over different windows (7D, 30D, 90D), not just the all-time leaderboard. An algo might be top-10 lifetime but underwater for 3 weeks — that divergence is invisible on the current leaderboard.
- **Goal:** Show rolling P&L (algo vs SPY) across fixed windows so users can spot when signals are actually holding up in real time and when they're lagging the market.
- **Metric:** % of subscribers who view the rolling comparison; average time spent on comparison view; signal hunter insights captured in comments/notes on algos with clear rolling underperformance.

## 2. User Stories

- As a Signal Hunter, I want to see how each algo performed vs SPY over the last 7, 30, and 90 days, so I can spot signals that are holding up in the current market vs ones that rode an old trend.
- As the Alt-Data Nerd, I want a small chart showing rolling P&L divergence, so I can see when a signal stopped working and whether it's recovering or just dead.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Algo detail page includes a small multi-window chart: 7D, 30D, 90D rolling P&L (algo line) overlaid on SPY P&L (gray reference line). Both measured in % return from window start.
- **Requirement 2:** Chart updates daily at market close; if an algo has <7 days of live trading, that window shows 'Insufficient Data' instead of a line.
- **Requirement 3:** Y-axis is percentage return; X-axis is calendar days within the selected window. No smoothing; every data point is a settlement close.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Chart is read-only and embedded inline on the algo detail page, below the force rank and trade list. Clicking the window buttons (7D / 30D / 90D) redraws the chart; no transition animation. Keep it dull: algo line in dark gray, SPY reference in light gray. Tooltip on hover shows date and P&L % for both lines.

## 5. Acceptance Criteria (AC)

- An algo that is +15% in 30D but -5% vs SPY (SPY was +20%) shows this clearly; both numbers are visible without clicking or hovering.
- Rolling windows are aligned to calendar days, not trading days; a 7D window is exactly 7 calendar days from today back, even if that includes weekends.
- If SPY data is missing (market closed), the rolling window is recalculated to the last available close; the chart does not have gaps or NaN values.

## 6. Out of Scope

- Customizable windows (users cannot set their own 15D or 45D windows); 7D/30D/90D are fixed.
- Predictive extrapolation or trend lines; we show what happened, not what will happen next.
