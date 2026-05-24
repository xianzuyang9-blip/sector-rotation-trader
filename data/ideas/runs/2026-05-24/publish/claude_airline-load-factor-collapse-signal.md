# Airline Load Factor Collapse Signal

**Idea ID:** `airline-load-factor-collapse-signal`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly airline load factor drops >2% from 4-week moving average, it signals demand collapse in leisure/business travel. Falling load factors indicate weak discretionary spending and business travel; consumer discretionary reprices.

## Universe
- XLY

## Data Sources
- BTS (Bureau of Transportation Statistics) weekly airline load factor and capacity utilization

## Signal Logic
If load factor drops >2% from 4-week MA AND XLY closes down >0.8%

## Entry / Exit
Entry: If load factor drops >2% from 4-week MA AND XLY closes down >0.8% Exit: After 8 trading days or when load factor recovers >1% toward MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use BTS (Bureau of Transportation Statistics) weekly airline load factor and capacity utilization via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seasonal travel demand varies weekly; threshold fires 1–2 times per month during normal cycles.

## Required Keys
- None
