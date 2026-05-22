# Biscotti’s Failures Gallery
Status: Draft
Generated: 2026-05-22 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Losses and failed signals tend to be buried or sanitized elsewhere; users want a focused space to confront and learn from the worst performers.
- **Goal:** Provide a dedicated, brutally honest view of the lab’s worst algos, making failure as visible and informative as success.
- **Metric:** Boost engagement with bottom-ranked algos by 30%.

## 2. User Stories

- As a Receipts Guy, I want a no-BS gallery of the worst-performing algos, so I can verify the lab isn’t hiding bad bets.
- As a Signal Hunter, I want to study failure modes of algos, so I can avoid noise and understand what dead signals look like live.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Create a leaderboard subset filtered to the bottom 20% of algos by force rank.
- **Requirement 2:** Show detailed stats including max drawdown, days since last trade, and loss streaks.
- **Requirement 3:** Include operator notes or rough hypotheses on why each algo is tanking, preserving the personal voice.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Use a grim, stripped-back design with bold red highlights for losses; the tone is candid, almost like a lab notebook’s ‘failures’ section with handwritten-style operator comments.

## 5. Acceptance Criteria (AC)

- Users can easily switch between full leaderboard and failures gallery.
- All failure data is displayed without any positive spin or hiding.
- Operator notes are visible and editable by the operator only.

## 6. Out of Scope

- Automatically removing or archiving dead algos.
- Filtering failures by user preference or severity.
