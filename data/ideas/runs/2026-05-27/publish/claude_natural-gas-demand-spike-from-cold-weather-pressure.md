# Natural Gas Demand Spike From Cold Weather Pressure

**Idea ID:** `natural-gas-demand-spike-from-cold-weather-pressure`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When daily average temperatures drop sharply below seasonal norms across major heating regions, natural gas demand surges within 2–5 days, driving spot price volatility and energy sector strength. Energy sector benefits from rising input costs and demand signals; integrated oil/gas companies see margin expansion.

## Universe
- XLE

## Data Sources
- Open-Meteo daily temperature data + EIA Natural Gas Spot Price from FRED (series: DHHNGSP)

## Signal Logic
If 7-day rolling average temperature drops >8°F below 30-year seasonal baseline AND EIA spot price rises >3% in 2 days

## Entry / Exit
Entry: If 7-day rolling average temperature drops >8°F below 30-year seasonal baseline AND EIA spot price rises >3% in 2 days Exit: After 10 trading days OR when temperature recovers within 3°F of baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily temperature data + EIA Natural Gas Spot Price from FRED (series: DHHNGSP) via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Winter/shoulder seasons produce temperature swings >8°F almost weekly in Northern Hemisphere; energy prices react predictably within 2–5 days.

## Required Keys
- None
