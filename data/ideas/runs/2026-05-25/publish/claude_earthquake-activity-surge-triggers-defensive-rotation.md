# Earthquake Activity Surge Triggers Defensive Rotation

**Idea ID:** `earthquake-activity-surge-triggers-defensive-rotation`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Clusters of moderate seismic events in populated regions drive risk-off sentiment and brief rotation to defensive sectors within 2–5 trading days. Earthquake fears trigger temporary flight to safety; discretionary spending appetite declines as consumer confidence dips.

## Universe
- XLY

## Data Sources
- USGS earthquake activity API (magnitude ≥4.5 in continental US) daily count and regional clustering

## Signal Logic
When 3-day rolling count of magnitude ≥4.5 earthquakes in CA or PNW ≥3 events AND event occurs within 500km of metro area (pop >1M)

## Entry / Exit
Entry: When 3-day rolling count of magnitude ≥4.5 earthquakes in CA or PNW ≥3 events AND event occurs within 500km of metro area (pop >1M) Exit: After 5 trading days or when S&P 500 VIX falls below prior 10-day mean

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity API (magnitude ≥4.5 in continental US) daily count and regional clustering via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seismic activity is natural and frequent; California and Oregon experience moderate earthquakes multiple times per month on average.

## Required Keys
- None
