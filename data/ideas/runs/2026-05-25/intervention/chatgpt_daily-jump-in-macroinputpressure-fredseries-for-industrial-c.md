# Daily Jump In Macroinputpressure Fredseries For Industrial Commodity Price Index Signals Inflationary Pressure On Materials Sector

**Idea ID:** `daily-jump-in-macroinputpressure-fredseries-for-industrial-c`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A rising industrial commodity price index signals increasing input costs pressuring materials companies. Higher input prices compress margins in materials sector unless passed to customers.

## Universe
- XLB

## Data Sources
- FRED industrial commodity price index

## Signal Logic
If daily industrial commodity price index rises by more than 1.5% compared to prior day

## Entry / Exit
Entry: If daily industrial commodity price index rises by more than 1.5% compared to prior day Exit: After 5 trading days or if index falls below 0.5% daily change

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED industrial commodity price index via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Commodity prices show daily volatility due to global demand and supply shocks.

## Required Keys
- None
