# Daily Spike In Fred Series For Initial Jobless Claims Signals Consumer Discretionary Stress

**Idea ID:** `daily-spike-in-fred-series-for-initial-jobless-claims-signal`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sudden rise in initial jobless claims signals deteriorating labor market conditions, pressuring consumer discretionary spending. Higher unemployment claims correlate with weaker consumer demand for discretionary goods.

## Universe
- XLY

## Data Sources
- FRED weekly initial jobless claims

## Signal Logic
If weekly initial jobless claims rise more than 10% week-over-week

## Entry / Exit
Entry: If weekly initial jobless claims rise more than 10% week-over-week Exit: Exit after 3 weeks or when claims fall below 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly initial jobless claims via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 60
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Initial claims data updates weekly and often spikes with economic weakness.

## Required Keys
- None
