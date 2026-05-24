# Weekly Rise In Google Trends For Unemployment Benefits Searches Signals Labor Market Stress

**Idea ID:** `weekly-rise-in-google-trends-for-unemployment-benefits-searc`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing searches for unemployment benefits indicate rising labor market stress and potential softening in employment conditions. Financial sector ETFs often react negatively to deteriorating labor conditions due to credit risk and economic slowdown concerns.

## Universe
- XLF

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly search interest for 'unemployment benefits' rises by 15% week-over-week

## Entry / Exit
Entry: If weekly search interest for 'unemployment benefits' rises by 15% week-over-week Exit: After 6 weeks or when search interest reverts below baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor market news and seasonal layoffs frequently cause weekly search spikes.

## Required Keys
- None
