# Natural Gas Demand Spike From Cold Weather Google Trends Heating Searches

**Idea ID:** `natural-gas-demand-spike-from-cold-weather-google-trends-hea`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly heating-related search volume spikes >50% AND temperature forecasts show sustained cold (<32F for 5+ days), natural gas demand expectations rise sharply. Cold snaps drive natural gas demand; energy prices respond positively within 1-2 weeks, lifting energy sector equities.

## Universe
- XLE

## Data Sources
- Google Trends weekly search volume for 'heating costs' and 'natural gas prices' combined with Open-Meteo daily temperature data through google_trends + weather_series adapters

## Signal Logic
If weekly Google Trends 'heating costs' search volume rises >45% week-over-week AND 7-day average temperature forecast falls below 35F

## Entry / Exit
Entry: If weekly Google Trends 'heating costs' search volume rises >45% week-over-week AND 7-day average temperature forecast falls below 35F Exit: After 2 weeks or once weekly search volume drops >30%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'heating costs' and 'natural gas prices' combined with Open-Meteo daily temperature data through google_trends + weather_series adapters via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Winter weather volatility and cold snaps occur throughout Q4-Q1; search spikes are reliable and predictable monthly.

## Required Keys
- None
