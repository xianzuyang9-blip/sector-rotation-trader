# Failure Waterfall
Status: Draft
Generated: 2026-06-05 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Receipts Guy users want to see not just where signals succeed but the detailed sequence and scale of their failures over time.
- **Goal:** Provide a visual waterfall chart per signal showing each losing trade's impact on equity curve, making losses as transparent as wins.
- **Metric:** Increase average session duration on signal detail pages by 15%.

## 2. User Stories

- As a Receipts Guy, I want to see a waterfall of losses per trade so that I can verify the honesty of each signal's bad streaks.
- As a Receipts Guy, I want to distinguish between many small losses and few big losses to understand risk profiles.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Display a chronological waterfall chart for each signal showing individual trade P&L impacting total equity.
- **Requirement 2:** Include clear negative bars for losses and positive bars for wins without smoothing or aggregation.
- **Requirement 3:** Ensure the chart updates live with new trades and works offline with cached data.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Chart uses a rugged, hand-drawn style reminiscent of lab notebook sketches, with tooltip callouts naming each losing trade date and impact.

## 5. Acceptance Criteria (AC)

- Waterfall chart is visible on all paid subscriber signal detail pages on desktop and mobile.
- Loss bars are clearly red and labeled with date and P&L.
- Chart updates within 10 seconds of new trade data ingestion.

## 6. Out of Scope

- No smoothing or aggregation of losses into averages.
- No onboarding or tooltip explanations beyond basic trade info.
