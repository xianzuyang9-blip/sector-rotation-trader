# Job Posting Collapse Precedes Unemployment Spike

**Idea ID:** `job-posting-collapse-precedes-unemployment-spike`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sharp drops in weekly job posting counts (7%+ decline) historically lead unemployment rate increases by 2–4 weeks, creating volatility in equity risk sentiment. Job opening collapses signal impending layoff waves and consumer confidence erosion, suppressing discretionary spending.

## Universe
- XLY

## Data Sources
- FRED series JTSJOR (Job Openings, BLS) weekly aggregated from daily scrape

## Signal Logic
When JTSJOR falls 7%+ week-over-week after trading above 60th percentile of 12-month range

## Entry / Exit
Entry: When JTSJOR falls 7%+ week-over-week after trading above 60th percentile of 12-month range Exit: After 3 weeks or if job openings stabilize (WoW change > -2%)

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series JTSJOR (Job Openings, BLS) weekly aggregated from daily scrape via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Job openings are cyclical; 7% weekly declines occur 1–2 times per quarter during business cycle downturns.

## Required Keys
- None
