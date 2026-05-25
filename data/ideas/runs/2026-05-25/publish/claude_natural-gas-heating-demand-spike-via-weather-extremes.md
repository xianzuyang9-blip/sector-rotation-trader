# Natural Gas Heating Demand Spike Via Weather Extremes

**Idea ID:** `natural-gas-heating-demand-spike-via-weather-extremes`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Sudden cold snaps drive heating demand spikes, raising natural gas input pressure and energy sector volatility within 7–14 days. Energy producers benefit from sustained demand spikes; natural gas futures and integrated energy stocks rally on weather-driven input scarcity.

## Universe
- XLE

## Data Sources
- Open-Meteo daily temperature anomalies (heating degree days) for US bulk weighted by population

## Signal Logic
When 5-day rolling average heating degree days exceeds 95th percentile threshold AND daily low temperature drops >8°F from prior week average

## Entry / Exit
Entry: When 5-day rolling average heating degree days exceeds 95th percentile threshold AND daily low temperature drops >8°F from prior week average Exit: After 7 trading days or when heating degree days return below 60th percentile

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily temperature anomalies (heating degree days) for US bulk weighted by population via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weather extremes are frequent October–March; cold snaps occur multiple times per winter, triggering frequent signals.

## Required Keys
- None
