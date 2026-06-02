# Weekly Rise In Fred Series Producer Price Index Energy Inputs Signals Inflation Pressure On Energy Sector

**Idea ID:** `weekly-rise-in-fred-series-producer-price-index-energy-input`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A weekly rise in energy input prices signals rising input cost pressure that could squeeze margins but also lift energy prices. Energy sector revenues often rise with input cost inflation as prices pass through to consumers.

## Universe
- XLE

## Data Sources
- FRED weekly Producer Price Index for Energy Inputs

## Signal Logic
Enter long XLE if PPI Energy Inputs rises more than 1% week-over-week

## Entry / Exit
Entry: Enter long XLE if PPI Energy Inputs rises more than 1% week-over-week Exit: Exit after 4 weeks or if PPI falls below entry level

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly Producer Price Index for Energy Inputs via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Energy input cost inflation often moves in weekly bursts tied to commodity price shocks.

## Required Keys
- None
