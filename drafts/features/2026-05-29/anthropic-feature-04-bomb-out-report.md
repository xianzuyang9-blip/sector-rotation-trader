# Bomb-Out Report
Status: Draft
Generated: 2026-05-29 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** Alt-Data Nerd wants to learn from dead signals but the leaderboard buries algos that stopped firing or were explicitly killed. Failure is valuable data, but it disappears from the active view.
- **Goal:** Create a scrollable archive of dead/killed algos with clear tags, final PnL, reason for shutdown, and date killed—so users can study what didn't work and why the lab killed it.
- **Metric:** Engagement with Bomb-Out Report (time spent, repeat visits); correlation between users who read it and users who submit novel signal ideas.

## 2. User Stories

- As an Alt-Data Nerd, I want to see every algo the lab has killed and why (e.g., 'No trades in 60 days,' 'Directional without edge,' 'Correlation drift'), so I know which failure modes to avoid.
- As a Signal Hunter, I want to read the post-mortem on three failed algos before investing time in my own signal idea, so I don't repeat someone else's dead hypothesis.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Bomb-Out Report lists all killed/inactive algos (status = 'inactive' or 'killed') with kill date, final PnL, days running, and operator-written reason tag (<20 words, e.g., 'No edge after regime change,' 'Win rate degraded below 50% over 90D').
- **Requirement 2:** Algos are sortable by kill date, final PnL, days running, or reason tag; free users see a summary view (last 5 killed, aggregate stats), paid users see full historical list.
- **Requirement 3:** Each dead algo links to its final detail page (last equity curve, final trades, force rank at time of kill) so users can inspect the wreckage.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** This is not a graveyard. It is a library of negative results. The tone is clinical: 'Baileymol v2 did not survive the 2024 vol spike. Final return -8%. Reason: Correlation drift in implied vol regime. Killed 2024-03-15.' No softening. No 'lessons learned' spin. Just the facts and the kill tag.

## 5. Acceptance Criteria (AC)

- Bomb-Out Report loads in <1s and renders 50+ historical dead algos without lag.
- Each dead algo displays kill date, final PnL, final win rate, days running, and kill reason tag on a single row.
- Clicking an algo name shows its full detail page frozen at the kill date (final trades, equity curve, final leaderboard rank).

## 6. Out of Scope

- User-submitted commentary on why algos failed. This is operator voice only.
- Predictive alerts based on kill patterns. The report is historical, not forward-looking.
