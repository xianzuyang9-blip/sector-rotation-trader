# Force Rank Divergence View
Status: Draft
Generated: 2026-05-29 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** Signal Hunter can't quickly spot algos that are ranking differently across timeframes (e.g., all-time rank #45 but 30D rank #1). This honest divergence is interesting but buried in individual algo pages.
- **Goal:** Surface algos where recent performance contradicts historical ranking, making it obvious which signals are heating up or cooling down.
- **Metric:** % of paid subscribers who visit the divergence view at least weekly; time-to-insight for identifying trend reversals in signal performance.

## 2. User Stories

- As a Signal Hunter, I want to see which algos rank high in the last 30 days but low all-time, so I can spot signals that are lately working.
- As a Receipts Guy, I want to see which formerly strong algos have cratered in the last month, so I know which ones stopped holding up.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Divergence view lists algos sorted by (30D rank minus all-time rank) with raw rank numbers shown side-by-side and signed delta highlighted (e.g., +34 or -28).
- **Requirement 2:** Each row includes current PnL, days running, and force rank bucket (ALPHA/noise/unresolved) to provide context for divergence interpretation.
- **Requirement 3:** View respects all signal filtering (bucket, asset class, status) already available on main leaderboard.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** This is a second-order sort of the leaderboard data. No new data collection required. The view should feel like a different lens on the same lab notebook, not a separate feature. Show the math plainly: if an algo is rank 45 all-time and rank 3 in 30D, the delta is +42. No smoothing or narrative wrapping.

## 5. Acceptance Criteria (AC)

- Divergence view renders in <2s for full leaderboard on paid user session.
- Clicking an algo name navigates to its detail page with same context state preserved.
- View correctly handles algos with <30 days of running history (shows 'N/A' for 30D rank, not zero or error).

## 6. Out of Scope

- Predictive alerts ('this algo is trending up'). This is a passive view, not a notification system.
- Custom time windows. 30D divergence is the only lens for this version.
