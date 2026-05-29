# Alt-Data Nerd’s Signal Tag Explorer
Status: Draft
Generated: 2026-05-29 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Alt-Data Nerds want to explore signals by weird, real-world data categories but current buckets are too broad.
- **Goal:** Enable browsing and filtering the leaderboard by detailed alt-data tags (e.g., satellite imagery, social chatter, weather patterns).
- **Metric:** Increase time spent exploring signal categories by 20%.

## 2. User Stories

- As an Alt-Data Nerd, I want to filter signals by specific alternative data sources to track which data types hold up.
- As a Signal Hunter, I want to discover signals in new data buckets I didn’t know existed to expand my idea pool.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Implement a multi-select tag filter panel on leaderboard with tags derived from signal metadata.
- **Requirement 2:** Tags include clear, honest labels and no marketing fluff, e.g., 'Twitter mood', 'Cargo ship GPS', 'Electricity usage'.
- **Requirement 3:** Leaderboard updates instantly to show signals matching selected tags, including those with multiple tags.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Tags styled as rough-edged badges with muted colors; no hierarchical nesting; filter panel collapsible but visible by default for paying users.

## 5. Acceptance Criteria (AC)

- Filtering by one or more tags updates leaderboard correctly.
- Tags reflect actual signal metadata without generic labels.
- Feature works seamlessly on mobile and desktop.

## 6. Out of Scope

- No tag creation or user tagging.
- No AI-generated tag suggestions.
