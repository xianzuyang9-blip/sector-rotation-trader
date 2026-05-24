# Weekly Increase In Fred Producer Price Index Input Prices Signals Rising Macro Input Pressure

**Idea ID:** `weekly-increase-in-fred-producer-price-index-input-prices-si`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising producer input prices suggest increasing cost pressures on manufacturers, potentially squeezing margins and signaling inflation risk. Materials sector faces margin pressure when input prices rise rapidly, hurting profitability.

## Universe
- XLB

## Data Sources
- FRED series PPI input prices

## Signal Logic
If weekly PPI input price index increases by more than 0.5% week-over-week

## Entry / Exit
Entry: If weekly PPI input price index increases by more than 0.5% week-over-week Exit: After 4 weeks or when index growth rate decelerates below 0.1%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series PPI input prices via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly PPI data regularly fluctuates with commodity price cycles and supply chain changes.

## Required Keys
- None
