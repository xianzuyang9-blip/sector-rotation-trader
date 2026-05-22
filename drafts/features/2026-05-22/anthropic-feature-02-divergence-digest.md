# Divergence Digest
Status: Draft
Generated: 2026-05-22 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** An algo can be force-ranked #50 but rolling 30D rank #1 — this honest divergence is invisible on the main leaderboard and looks like noise to a user scanning once a week.
- **Goal:** Surface and explain signals that are outperforming their all-time rank over the last 30 days. Let users see which weird ideas are quietly starting to hold up.
- **Metric:** % of paid users who read at least one Divergence Digest entry per week. CTR on divergence signals back to their detail page. Time spent on detail pages for divergence signals.

## 2. User Stories

- As a Signal Hunter, I want to see which underrated signals are suddenly performing well in the last 30 days, so I can spot ideas that are working despite low historical rank.
- As an Alt-Data Nerd, I want a weekly curated list of interesting rank divergences (good and bad), so I can track which experiments are trending up or down without manually comparing ranks.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Generate a weekly (Friday EOD) report showing the top 5 signals with largest positive divergence: all-time rank minus 30D rank. Include negative divergence (top signals losing steam) as a separate section.
- **Requirement 2:** For each divergence signal: show all-time rank, 30D rank, days in lab, current rolling Sharpe, and a one-line operator observation (e.g., 'Picked up late-day sentiment shift,' 'Correlated to rate chatter, but holding').
- **Requirement 3:** Digest is email + accessible in a pinned section on the leaderboard (free users see headline only; paid users get full detail). Operator voice in each observation.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Email format is plain text, no gradients, no CTA buttons. Subject line: '[Stockarithm] This week's quiet wins (and losses).' On-site digest appears as a collapsible card above the leaderboard with a timestamp. Clicking an entry jumps to the signal detail page.

## 5. Acceptance Criteria (AC)

- Digest generates every Friday at 17:00 UTC with accurate rank calculations and no stale data.
- Each divergence entry includes a hand-written operator note; if no note exists, the entry is excluded from that week's digest.
- Negative divergence (top signals failing) appears with equal prominence to positive divergence — no cherry-picking wins.

## 6. Out of Scope

- Automated divergence explanations or 'why this happened' predictions (only operator notes).
- User-customizable divergence thresholds or filters in the first version (static: all-time vs 30D only).
