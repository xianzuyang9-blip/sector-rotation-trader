# Bucket Reclassifier
Status: Draft
Generated: 2026-05-22 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** Signals are classified as ALPHA / NOISE / UNRESOLVED, but these buckets are hand-assigned by the operator and users have no visibility into the reasoning. A signal's bucket can feel arbitrary.
- **Goal:** Let paid users see the operator's explicit criteria for each signal's bucket classification, including historical reclassifications. Show the thinking, not just the label.
- **Metric:** % of paid users who expand bucket-reasoning at least once per month. Paid conversion lift among Signal Hunters who view reclassifier data.

## 2. User Stories

- As a Signal Hunter, I want to understand why a signal is labeled NOISE instead of UNRESOLVED, so I can decide if I trust the operator's judgment enough to trade against it.
- As an Alt-Data Nerd, I want to see the history of when a signal's bucket changed and what triggered the reclassification, so I can track how the operator's thesis on a signal evolves.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Add a 'Bucket History' tab to each signal's detail page showing: current bucket, date assigned, operator reason (1-3 sentences), previous buckets with dates and reasons.
- **Requirement 2:** Bucket reasons must be operator-written and human-readable: e.g., 'ALPHA: >60% win rate, rolling Sharpe >1.2 for 90 days, trades 2-3x/week,' not auto-generated summaries.
- **Requirement 3:** Reclassifications logged with date, old bucket, new bucket, and reason. If a signal moves from NOISE to UNRESOLVED, that event is recorded and visible.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Bucket History is a compact timeline, not a narrative. Each entry is a small card: date | old → new | reason. Paid users see full history; free users see current bucket and reason only. The operator voice is clinical: 'This moved because X changed, not because I changed my mind.'

## 5. Acceptance Criteria (AC)

- Every signal with a bucket classification has a reason statement (free and paid visibility).
- Reclassification history is complete going back to signal launch (no backfilling required in first version, but all future changes are logged).
- Reason text is operator-authored; no auto-generated bucket explanations appear anywhere.

## 6. Out of Scope

- User comments or disagreement voting on bucket classifications (this is operator-final).
- Automated reclassification based on rolling metrics (all changes are operator-initiated).
