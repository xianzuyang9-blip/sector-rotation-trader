# Labor Market Weakness Signal From Weekly Jobless Claims Momentum Fade

**Idea ID:** `labor-market-weakness-signal-from-weekly-jobless-claims-mome`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When 4-week moving average of jobless claims rises >8% from prior month's mean, labor demand is weakening; this precedes consumer spending weakness by 1–3 weeks. Consumer discretionary sector faces headwinds from rising unemployment; advertising and retail demand fade as hiring slows.

## Universe
- XLY

## Data Sources
- FRED Initial Jobless Claims (ICSA) weekly series

## Signal Logic
4-week MA of jobless claims rises >8% from 12-week baseline AND 2-week acceleration is >3%

## Entry / Exit
Entry: 4-week MA of jobless claims rises >8% from 12-week baseline AND 2-week acceleration is >3% Exit: After 15 trading days OR jobless claims fall back below 105% of 12-week baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED Initial Jobless Claims (ICSA) weekly series via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Jobless claims oscillate >8% on a 4-week basis 4–6 times per year; summer and winter layoff cycles are predictable.

## Required Keys
- None
