# Signal Decay Visualizer
Status: Draft
Generated: 2026-05-29 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Users struggle to understand how signal performance changes over time, especially distinguishing fresh signals from stale ones.
- **Goal:** Enable users to instantly see the freshness and decay patterns of each signal's trades over the last 90 days.
- **Metric:** Increase average session time on leaderboard by 10%.

## 2. User Stories

- As a Signal Hunter, I want to see how recent trades affect a signal’s current rank so that I can assess if it’s still relevant.
- As an Alt-Data Nerd, I want to identify signals that had early promise but have decayed, so I can track unresolved or dead signals honestly.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Add a mini heatmap or sparkline next to each signal on the leaderboard showing trade win/loss intensity over recent days.
- **Requirement 2:** Show gaps or zero activity periods explicitly to highlight inactivity or signal dormancy.
- **Requirement 3:** Update visualizations in real-time with live data feed without requiring page reload.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Use muted red and green shades with a linear timeline; no smoothing to preserve honest jaggedness; tooltip on hover reveals exact daily P/L and trade count.

## 5. Acceptance Criteria (AC)

- Heatmap/sparkline loads correctly on desktop and mobile views.
- Visual clearly distinguishes no-activity days from loss days.
- Tooltip data matches backend trade logs accurately.

## 6. Out of Scope

- No predictive trend lines or smoothing algorithms.
- No signal ranking adjustments based on decay.
