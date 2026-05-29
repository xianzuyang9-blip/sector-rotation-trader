# Bucket Divergence Flags
Status: Draft
Generated: 2026-05-29 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Users get confused when a signal’s force rank differs wildly from its rolling 30-day rank with no immediate explanation.
- **Goal:** Surface honest divergence flags explaining notable rank mismatches directly on the leaderboard.
- **Metric:** Reduce user support questions about rank discrepancies by 25%.

## 2. User Stories

- As an Alt-Data Nerd, I want to quickly grasp why a signal is simultaneously in the top 10 of one metric but bottom 10 of another.
- As a Signal Hunter, I want clear, no-BS notes on leaderboard about rank divergence to inform my decisions.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Add a subtle icon next to signals with >20 rank difference between force rank and rolling 30D rank.
- **Requirement 2:** On hover or tap, show a short note explaining the divergence (e.g., recent surge, recent drop, inactivity).
- **Requirement 3:** The divergence calculation updates in real time with leaderboard refresh.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Use a rough hand-drawn style warning icon to align with brand; keep notes brutally honest and concise; no sugarcoating.

## 5. Acceptance Criteria (AC)

- Icons appear only on signals meeting divergence threshold.
- Hover notes display correct explanation text.
- Feature works consistently on desktop and mobile.

## 6. Out of Scope

- No automatic rank smoothing or adjustment.
- No user-configurable divergence thresholds.
