# Daily Spike In Rss Counts For Corporate Layoff Announcements Signals Consumer Discretionary Headwind

**Idea ID:** `daily-spike-in-rss-counts-for-corporate-layoff-announcements`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising news of corporate layoffs signals weakening economic sentiment and potential reduction in consumer discretionary spending. Discretionary sector often reacts negatively to labor market deterioration and income uncertainty.

## Universe
- XLY

## Data Sources
- RSS/news feed counts

## Signal Logic
If daily RSS counts for 'corporate layoffs' rise 40% above 14-day average

## Entry / Exit
Entry: If daily RSS counts for 'corporate layoffs' rise 40% above 14-day average Exit: After 10 days or when counts fall below baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS/news feed counts via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Layoff news surges frequently in economic weak patches or sector-specific slowdowns.

## Required Keys
- None
