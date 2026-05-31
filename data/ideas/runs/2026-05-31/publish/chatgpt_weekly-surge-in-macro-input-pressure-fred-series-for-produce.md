# Weekly Surge In Macro Input Pressure Fred Series For Producer Price Index Of Metals

**Idea ID:** `weekly-surge-in-macro-input-pressure-fred-series-for-produce`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising producer prices for metals increase costs for materials-intensive industries. Materials sector margins pressured by higher input prices.

## Universe
- XLB

## Data Sources
- FRED weekly PPI metals index

## Signal Logic
If weekly PPI metals index rises more than 3% week-over-week

## Entry / Exit
Entry: If weekly PPI metals index rises more than 3% week-over-week Exit: When index growth slows below 1% for 2 weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly PPI metals index via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Commodity price volatility drives regular input cost pressure signals on a weekly basis.

## Required Keys
- None
