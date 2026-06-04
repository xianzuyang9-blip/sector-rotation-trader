# Weekly Surge In Google Trends For Job Quitting Signals Labor Market Churn Stress

**Idea ID:** `weekly-surge-in-google-trends-for-job-quitting-signals-labor`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising interest in quitting jobs signals increased labor market churn and potential wage inflation pressure. Financial sector may face credit risk pressure as labor churn raises consumer financial stress.

## Universe
- XLF

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly Google Trends for 'job quitting' rises 20%+ week-over-week

## Entry / Exit
Entry: If weekly Google Trends for 'job quitting' rises 20%+ week-over-week Exit: Exit after 4 weeks or when trend drops below 10% growth week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor market conditions change frequently near earnings and economic data releases.

## Required Keys
- None
