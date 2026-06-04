# Weekly Spike In Fred Series For Industrial Electricity Consumption Growth Signals Manufacturing Strength

**Idea ID:** `weekly-spike-in-fred-series-for-industrial-electricity-consu`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising industrial electricity consumption indicates increased manufacturing activity and economic strength. Manufacturing growth translates into higher industrial sector earnings.

## Universe
- XLI

## Data Sources
- FRED weekly industrial electricity consumption index

## Signal Logic
If weekly consumption growth rate exceeds 1.5% compared to prior week

## Entry / Exit
Entry: If weekly consumption growth rate exceeds 1.5% compared to prior week Exit: After 3 weeks or drop below 0.5% growth

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly industrial electricity consumption index via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Industrial electricity data regularly reflects current manufacturing activity shifts.

## Required Keys
- None
