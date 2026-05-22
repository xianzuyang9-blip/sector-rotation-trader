# Utility Sector Rate Hike Anxiety From Weather-driven Demand Spike

**Idea ID:** `utility-sector-rate-hike-anxiety-from-weather-driven-demand-`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When daily average temperature deviation from seasonal norm exceeds +8°F AND EIA daily electricity demand reaches 90%+ of recent capacity, utility companies see margin pressure from capped rates, triggering brief defensive demand. Utilities are defensive when rate hike pressure is evident; high demand periods force regulators and investors to acknowledge margin stress, driving safe-haven rotation into utilities.

## Universe
- XLU

## Data Sources
- Open-Meteo daily temperature data (US national area-weighted) + EIA electricity demand via eia_electricity adapter

## Signal Logic
If temperature deviation >+8°F AND EIA demand >90% capacity AND XLU closes above 20-day SMA, buy XLU

## Entry / Exit
Entry: If temperature deviation >+8°F AND EIA demand >90% capacity AND XLU closes above 20-day SMA, buy XLU Exit: After 6 trading days OR if temperature normalizes AND demand falls below 80% capacity

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily temperature data (US national area-weighted) + EIA electricity demand via eia_electricity adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Daily weather and EIA data update constantly; extreme temperatures and demand spikes occur 8–12 times per year in US regions.

## Required Keys
- None
