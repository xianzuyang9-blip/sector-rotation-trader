# Force Rank Divergence View
Status: Draft
Generated: 2026-06-05 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** Signal Hunter can't quickly spot algos that are force-ranked low but performing well on rolling windows — the interesting contradictions get buried in a flat list. The 45th-ranked algo that's #1 over 30 days is invisible.
- **Goal:** Surface honest divergence between lifetime force rank and rolling-window performance so users can spot signals that might be turning around or were penalized early unfairly.
- **Metric:** % of Signal Hunters who click into at least one divergence card per session; time-to-insight on which algos are bucking the lifetime rank.

## 2. User Stories

- As a Signal Hunter, I want to see which algos rank differently on 7D/30D/90D windows vs lifetime, so I can catch signals that are actually holding up despite poor early runs.
- As the Receipts Guy, I want the leaderboard to show both the long view and the rolling view side-by-side, so I can verify that nothing is being hidden and contradictions are real.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Add a toggle or optional column to leaderboard showing [Force Rank Lifetime] vs [30D Rolling Rank] with delta highlighted only when >10 positions apart.
- **Requirement 2:** On algo detail page, render a small sparkline showing rank movement across 7D, 30D, 90D, and lifetime buckets without smoothing or narrative overlay.
- **Requirement 3:** Divergence calculation must include failed signals (0 trades, drawdown >30%) so users see when an algo dropped to #45 lifetime but has fired cleanly for 3 weeks straight.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** No explanatory text. No 'why' narrative. Just the numbers side by side. If a user knows what a signal lab is, they will read the divergence immediately. Keep column headers short: 'Rank (All-Time)' and 'Rank (30D)'. Sparklines are read-only; clicking opens the detail view.

## 5. Acceptance Criteria (AC)

- Divergence data updates in real-time as new trades settle; old trades do not retroactively change historical rank buckets.
- Algos with <7 days of live trading show 'Unresolved' in rolling windows, not a rank, so no false confidence.
- A algo that is force-ranked #1 overall but has 0 trades in the last 30 days shows rank divergence accurately (e.g., 'Rank 1' vs 'No Data (30D)').

## 6. Out of Scope

- Predictive ranking or 'trending' badges; we show what happened, not what will happen.
- Customizable rank windows; 7D/30D/90D are fixed to avoid analysis paralysis.
