# Weekly Rise In Fred Series Initial Jobless Claims Signals Rising Labor Market Stress

**Idea ID:** `weekly-rise-in-fred-series-initial-jobless-claims-signals-ri`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An increase in initial jobless claims signals growing labor market weakness and potential economic slowdown. Financial sector is sensitive to economic cycles and rising claims often forecast lower credit demand and defaults.

## Universe
- XLF

## Data Sources
- FRED weekly Initial Jobless Claims

## Signal Logic
Enter short XLF if weekly claims rise 5%+ vs previous week

## Entry / Exit
Entry: Enter short XLF if weekly claims rise 5%+ vs previous week Exit: Exit after 4 weeks or if claims decline below entry week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly Initial Jobless Claims via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Jobless claims fluctuate weekly due to economic and seasonal factors, frequently triggering signals.

## Required Keys
- None
