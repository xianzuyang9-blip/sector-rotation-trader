# Electricity Demand Surge From Extreme Heat Signals Energy Sector Strength

**Idea ID:** `electricity-demand-surge-from-extreme-heat-signals-energy-se`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly electricity demand spikes >10% above rolling 12-week average AND heat index exceeds 95°F for 3+ consecutive days, energy stocks surge as peak pricing and margin expansion material. Peak electricity demand during heat waves drives higher wholesale prices and utility margins; energy sector benefits.

## Universe
- XLE

## Data Sources
- EIA electricity demand data (series: EMRATIO) weekly via eia_electricity adapter combined with Open-Meteo daily heat stress index

## Signal Logic
If EIA electricity demand >10% above 12-week average AND regional heat index >95°F for 3+ days, enter long XLE

## Entry / Exit
Entry: If EIA electricity demand >10% above 12-week average AND regional heat index >95°F for 3+ days, enter long XLE Exit: Exit after 10 trading days or when demand normalizes below 105% of 12-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use EIA electricity demand data (series: EMRATIO) weekly via eia_electricity adapter combined with Open-Meteo daily heat stress index via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Heat waves are seasonal; summer months (June-Sept) produce multiple 3+ day heat stress events per year.

## Required Keys
- None
