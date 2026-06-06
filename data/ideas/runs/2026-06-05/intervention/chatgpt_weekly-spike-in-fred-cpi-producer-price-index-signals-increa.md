# Weekly Spike In Fred Cpi Producer Price Index Signals Increasing Input Cost Pressure For Industrials

**Idea ID:** `weekly-spike-in-fred-cpi-producer-price-index-signals-increa`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising producer price inflation increases input costs for industrial companies, pressuring margins. Industrial sector earnings pressured by rising raw material and production costs.

## Universe
- XLI

## Data Sources
- FRED weekly PPI index

## Signal Logic
Enter short XLI when weekly PPI increases by more than 0.3% week-over-week

## Entry / Exit
Entry: Enter short XLI when weekly PPI increases by more than 0.3% week-over-week Exit: Exit after 6 weeks or when PPI growth slows below 0.1%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly PPI index via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: PPI data fluctuates steadily with inflation trends, creating frequent relevant signals.

## Required Keys
- None
