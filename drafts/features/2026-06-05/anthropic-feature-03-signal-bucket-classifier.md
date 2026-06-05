# Signal Bucket Classifier
Status: Draft
Generated: 2026-06-05 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** Signal Hunter lands on the leaderboard and sees 30 algos but has no framework for which bucket they belong in (ALPHA / noise / unresolved / dead). The lab knows this but doesn't expose it, forcing him to guess or read the blog.
- **Goal:** Surface the lab's internal classification of each algo (ALPHA, NOISE, UNRESOLVED, DEAD) so Signal Hunter can instantly understand what he is looking at and decide which signals to take seriously.
- **Metric:** % of paid users who filter or sort by bucket in first session; engagement depth on UNRESOLVED bucket (highest-value exploration for traders).

## 2. User Stories

- As a Signal Hunter, I want to see which algos the lab classifies as live ALPHA so I can ignore noise and focus on signals that are actually holding up.
- As the Alt-Data Nerd, I want to see the UNRESOLVED bucket and understand why they're still running, so I can follow the experiment and spot breakthroughs early.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Leaderboard includes a 'Bucket' column with values: ALPHA (force rank top 20, 60+ days, win rate >50%), NOISE (force rank >30, declining 90D performance), UNRESOLVED (20-60 days, unclear trend), DEAD (0 trades in 90 days).
- **Requirement 2:** Bucket classification is deterministic and recalculated daily; rules are published in a single page on the site (no AI, no black box).
- **Requirement 3:** Each bucket is a clickable filter on the leaderboard; clicking 'UNRESOLVED' shows only algos in that bucket, sorted by days-running ascending (newest first).

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Bucket colors are muted and functional, not emotional. ALPHA is not green-with-trophy; it is a quiet label. The rules page is boring and specific ('force rank top 20 AND 60+ days running AND win rate >50% across all trades'). No algorithm explanation beyond the rules.

## 5. Acceptance Criteria (AC)

- An algo that moves from UNRESOLVED to ALPHA shows the new bucket in the leaderboard immediately after the daily recalculation, with no announcement or toast.
- DEAD algos remain on the leaderboard (never hidden); their bucket is marked DEAD and they sort to the bottom by default.
- Bucket classification rules are deterministic; given the same input data, two independent systems produce identical bucket assignments for all algos.

## 6. Out of Scope

- User-custom buckets or tagging; the lab's classification is the only view.
- Narrative explanations ('This algo is ALPHA because it caught the Tesla short'); only the rules are published, not stories.
