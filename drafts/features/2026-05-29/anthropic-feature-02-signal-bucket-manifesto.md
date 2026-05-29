# Signal Bucket Manifesto
Status: Draft
Generated: 2026-05-29 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** Alt-Data Nerd sees signals classified as ALPHA/noise/unresolved but has no visibility into the criteria used or the hypothesis behind each bucket assignment. The lab is gatekeeping its own thinking.
- **Goal:** Let users read the operator's live reasoning for why an algo lands in each bucket, with permission to challenge or track how the classification evolves.
- **Metric:** Engagement with manifesto entries (reads, time-on-page); correlation between users who read manifestos and users who renew paid subscriptions.

## 2. User Stories

- As an Alt-Data Nerd, I want to read the operator's reasoning for why Biscotti is ALPHA and not unresolved, so I understand what separates a real signal from noise.
- As a Receipts Guy, I want to see when the operator changes a signal's bucket assignment and why, so I can track whether the lab is being honest about signal quality over time.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Each signal bucket (ALPHA, noise, unresolved) displays a short narrative statement (<300 words) written by operator explaining the evidence for that classification, updated whenever bucket assignment changes.
- **Requirement 2:** Manifesto statements include a 'last updated' timestamp and a one-sentence summary of what changed (e.g., 'Moved to ALPHA after 60 days stable above 55% win rate').
- **Requirement 3:** Paid subscribers can view the full history of manifesto edits for any signal, showing how reasoning evolved as new data arrived.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** This is not a blog. It is not marketing copy. It sounds like field notes from someone running a real experiment. Short, specific, honest. No 'leveraging' or 'unlocking.' If the operator is unsure, say so. Manifestos live on the algo detail page, inline with the force rank and PnL, not behind a separate tab.

## 5. Acceptance Criteria (AC)

- Every algo in a named bucket (ALPHA/noise/unresolved) displays a manifesto statement on its detail page.
- Manifesto edit history is queryable and timestamped; paid users can view the full chain.
- Manifesto updates trigger a data refresh but do not send notifications (users discover changes by visiting the page).

## 6. Out of Scope

- User comments or discussion on manifestos. This is operator voice only.
- AI-generated summaries of manifesto intent. The operator writes these by hand.
