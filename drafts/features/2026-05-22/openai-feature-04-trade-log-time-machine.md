# Trade Log Time Machine
Status: Draft
Generated: 2026-05-22 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Users want to trace a signal’s history trade-by-trade but current logs are hard to navigate and don’t emphasize losses as lessons.
- **Goal:** Create an easy-to-use, timeline-style trade log per algo that highlights wins and losses equally, letting users ‘scroll back in time’ through messy real trading.
- **Metric:** Increase per-algo trade log views by 40%.

## 2. User Stories

- As a Receipts Guy, I want a detailed, honest trade timeline for each signal, so I can see the full receipts of every bet made.
- As a Signal Hunter, I want to analyze patterns in wins and losses over time within a signal’s trades, so I can spot recurring failure modes or streaks.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Display trades in chronological order with clear profit/loss coloring and amount.
- **Requirement 2:** Allow users to zoom in/out on time ranges and quickly jump to earliest or latest trades.
- **Requirement 3:** Support notes or operator commentary attached to specific trades.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** A vertical timeline with no nonsense: losses in red, wins in green, neutral or break-even in gray; no smoothing or aggregation. Operator notes appear as sticky flags on timeline points.

## 5. Acceptance Criteria (AC)

- Timeline loads trade data correctly across devices.
- Users can navigate through trades without lag or confusion.
- Operator notes are editable and saved reliably.

## 6. Out of Scope

- Trade prediction or signals about future trade outcomes.
- Aggregated trade statistics or summary dashboards.
