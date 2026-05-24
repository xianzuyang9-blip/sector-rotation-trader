# Daily Jump In Weather Series Temperature Volatility Signals Utility Demand Surges

**Idea ID:** `daily-jump-in-weather-series-temperature-volatility-signals-`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden temperature volatility causes spikes in electricity and gas demand for heating/cooling, impacting utilities sector performance. Utility companies benefit from demand spikes tied to sudden weather swings.

## Universe
- XLU

## Data Sources
- Open-Meteo daily weather temperature data

## Signal Logic
If daily temperature range (max-min) increases 30% above 14-day average

## Entry / Exit
Entry: If daily temperature range (max-min) increases 30% above 14-day average Exit: After 5 days or when volatility returns to normal

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily weather temperature data via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weather volatility frequently occurs especially during seasonal transitions.

## Required Keys
- None
