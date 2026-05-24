# Utility Demand Spike From Weather Extremes

**Idea ID:** `utility-demand-spike-from-weather-extremes`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When daily temperature deviation exceeds 10°F from normal AND EIA electricity demand rises >5% day-over-day, utilities face margin compression or expansion. Extreme weather boosts utility revenues short-term but signals long-term grid stress; equity reprices dividend safety.

## Universe
- XLU

## Data Sources
- Open-Meteo daily temperature anomaly (degree-days relative to 30-year normal) + EIA daily electricity demand

## Signal Logic
If temp anomaly >10°F AND electricity demand >5% DoD spike

## Entry / Exit
Entry: If temp anomaly >10°F AND electricity demand >5% DoD spike Exit: After 6 trading days or when both conditions reverse

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily temperature anomaly (degree-days relative to 30-year normal) + EIA daily electricity demand via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seasonal weather swings and demand spikes occur weekly; combined trigger fires 1–2 times per week on average.

## Required Keys
- None
