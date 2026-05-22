# Signal Decay Curves
Status: Draft
Generated: 2026-05-22 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Users struggle to see how signals degrade or improve over time, obscuring which weird ideas remain alive or are fading into noise.
- **Goal:** Make it obvious how each algo’s edge evolves with days running, emphasizing failures as much as successes.
- **Metric:** Increase time spent viewing individual algo performance curves by 20%.

## 2. User Stories

- As a Signal Hunter, I want to see how an algo’s ranking changes across different time windows, so I can judge if a signal is genuinely holding up or just lucky short-term.
- As an Alt-Data Nerd, I want to observe the decay pattern of a signal’s edge, so I can identify slow-building or fast-failing ideas without guesswork.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Display an interactive graph per algo showing rolling rank over multiple time frames (7, 30, 90 days).
- **Requirement 2:** Show explicit markers for best and worst performance points with dates.
- **Requirement 3:** Handle algos with intermittent trades or no trades in a period by showing gaps or flat lines clearly.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** The graph uses a stark, no-frills style with red/green shading for losses/wins; hover states show exact ranks and dates. No smoothing—raw data only.

## 5. Acceptance Criteria (AC)

- Graphs render correctly on desktop and mobile with responsive scaling.
- Users can toggle between different time windows easily without page reload.
- Missing or sparse data is clearly indicated, not hidden or interpolated.

## 6. Out of Scope

- Predictive ranking or future performance estimates.
- Automated summaries or signal quality scores.
