# Signal Divergence Flags
Status: Draft
Generated: 2026-06-05 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Signal Hunters struggle to quickly spot algos whose short-term rolling ranks diverge sharply from their overall force rank, which can indicate emerging or fading edges.
- **Goal:** Surface honest divergence flags for signals showing meaningful rank shifts, helping users catch interesting signal behavior without smoothing it over.
- **Metric:** Increase click-through rate on flagged signals on the leaderboard by 20%.

## 2. User Stories

- As a Signal Hunter, I want a clear visual marker when a signal’s 30-day rolling rank sharply differs from its all-time rank so I can investigate unusual momentum.
- As a Signal Hunter, I want to filter leaderboard signals by divergence strength to focus on interesting anomalies.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Calculate rank divergence as the absolute difference between overall force rank and rolling 30-day rank.
- **Requirement 2:** Display a colored flag icon next to signals with divergence above a configurable threshold.
- **Requirement 3:** Allow sorting and filtering leaderboard by divergence flags.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Flags appear as hand-drawn warning triangles with a subtle flicker animation to draw the eye without being obnoxious.

## 5. Acceptance Criteria (AC)

- Divergence flags appear only on signals exceeding threshold difference.
- Filtering leaderboard by flagged signals updates results instantly.
- Feature works identically on desktop and mobile.

## 6. Out of Scope

- No predictive claims about divergence significance.
- No automatic alerts or notifications.
