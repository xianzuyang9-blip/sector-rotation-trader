# Alt-Data Signal Explorer
Status: Draft
Generated: 2026-06-05 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Alt-Data Nerds want to explore and compare groups of signals built on similar alternative data sources to understand which data types hold promise or fail.
- **Goal:** Create a filter and grouping system on the leaderboard to segment signals by alt-data categories, showing their aggregate performance and failure rates.
- **Metric:** Increase time spent by Alt-Data Nerd users on grouped signal views by 25%.

## 2. User Stories

- As an Alt-Data Nerd, I want to see all signals using satellite imagery data grouped together with combined stats so I can assess that data’s overall usefulness.
- As an Alt-Data Nerd, I want to compare failure rates across alt-data categories to identify which data sources are noise.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Tag signals with alt-data categories based on their core input source.
- **Requirement 2:** Allow leaderboard grouping and filtering by these categories with aggregate stats (win rate, avg drawdown).
- **Requirement 3:** Show failure counts and days since last firing prominently in group summaries.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Use a rough grid layout with minimal styling, each group labeled with quirky category names like 'Satellite Dust' or 'Tweets & Whispers'.

## 5. Acceptance Criteria (AC)

- All alt-data tagged signals appear in their groups with correct aggregate metrics.
- Filtering and grouping controls are responsive and intuitive without onboarding.
- Failure stats are clearly visible and not hidden or softened.

## 6. Out of Scope

- No new alt-data ingestion pipelines in this release.
- No ranking or scoring of alt-data categories beyond raw aggregation.
