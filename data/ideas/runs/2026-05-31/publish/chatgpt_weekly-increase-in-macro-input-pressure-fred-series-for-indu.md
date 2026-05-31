# Weekly Increase In Macro Input Pressure Fred Series For Industrial Natural Gas Prices

**Idea ID:** `weekly-increase-in-macro-input-pressure-fred-series-for-indu`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Higher natural gas prices increase input costs for industrial production, pressuring margins. Industrial sector margins compress as energy input costs rise.

## Universe
- XLI

## Data Sources
- FRED weekly industrial natural gas price index

## Signal Logic
If weekly natural gas price increases by more than 5%

## Entry / Exit
Entry: If weekly natural gas price increases by more than 5% Exit: When prices fall back or increase less than 1% for 2 weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly industrial natural gas price index via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Natural gas price volatility frequently triggers cost pressure signals for industrials.

## Required Keys
- None
