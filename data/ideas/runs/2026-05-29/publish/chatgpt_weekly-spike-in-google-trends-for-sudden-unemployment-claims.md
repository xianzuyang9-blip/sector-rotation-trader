# Weekly Spike In Google Trends For Sudden Unemployment Claims Searches

**Idea ID:** `weekly-spike-in-google-trends-for-sudden-unemployment-claims`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A rapid increase in searches for unemployment claims suggests rising labor market stress, often preceding cautious consumer and business spending. Rising labor stress tends to reduce discretionary spending, hurting consumer discretionary stocks.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'unemployment claims'

## Signal Logic
Enter short XLY when weekly search interest rises by more than 20% week-over-week

## Entry / Exit
Entry: Enter short XLY when weekly search interest rises by more than 20% week-over-week Exit: Exit once search interest declines below 10% week-over-week increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'unemployment claims' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly Google Trends data frequently show at least 20% week-over-week rises amid labor market shifts.

## Required Keys
- None
