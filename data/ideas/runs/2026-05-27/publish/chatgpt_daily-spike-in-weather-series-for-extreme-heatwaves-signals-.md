# Daily Spike In Weather Series For Extreme Heatwaves Signals Energy Demand Surge

**Idea ID:** `daily-spike-in-weather-series-for-extreme-heatwaves-signals-`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden extreme heat waves increase electricity demand for cooling, pressuring energy utilities. Heatwaves increase energy consumption, benefiting energy sector revenues.

## Universe
- XLE

## Data Sources
- Open-Meteo daily temperature data for US regions

## Signal Logic
If daily max temperature exceeds 95th percentile of 5-year daily max temps for region

## Entry / Exit
Entry: If daily max temperature exceeds 95th percentile of 5-year daily max temps for region Exit: After 7 days or when temperatures normalize

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily temperature data for US regions via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 60
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Heatwaves occur seasonally and generate measurable temperature spikes.

## Required Keys
- None
