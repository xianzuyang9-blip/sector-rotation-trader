# Daily Spike In Weather Series For Extreme Heat Days Signals Utility Sector Demand Surge

**Idea ID:** `daily-spike-in-weather-series-for-extreme-heat-days-signals-`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A spike in extreme heat days drives higher electricity demand for cooling, lifting utility sector revenues. Utilities benefit from increased power consumption during heat waves.

## Universe
- XLU

## Data Sources
- Open-Meteo daily temperature data for US major metro areas

## Signal Logic
Enter long XLU if number of daily hours above 95F rises 50%+ compared to 7-day average

## Entry / Exit
Entry: Enter long XLU if number of daily hours above 95F rises 50%+ compared to 7-day average Exit: Exit after 7 trading days or if heat hours normalize

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily temperature data for US major metro areas via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Heat waves occur frequently and create daily spikes in extreme heat hours.

## Required Keys
- None
