# Natural Gas Heating Demand Spike During Cold Snaps

**Idea ID:** `natural-gas-heating-demand-spike-during-cold-snaps`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When daily temperatures drop 15+ degrees below rolling 30-day average in winter months, natural gas futures spike sharply within 1-3 days, creating a predictable short-term commodity demand signal. Energy sector benefits from heating demand spikes and elevated commodity input costs that lift valuations.

## Universe
- XLE

## Data Sources
- Open-Meteo daily temperature data for major US heating zones combined with FRED natural gas spot prices (series: DHHNGSP)

## Signal Logic
If daily temperature drops >15°F below 30-day rolling average AND FRED DHHNGSP rises >5% in one week, enter long XLE

## Entry / Exit
Entry: If daily temperature drops >15°F below 30-day rolling average AND FRED DHHNGSP rises >5% in one week, enter long XLE Exit: Exit after 7 trading days or when temperature recovers within 10°F of rolling average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily temperature data for major US heating zones combined with FRED natural gas spot prices (series: DHHNGSP) via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Winter heating season runs through March; cold snaps occur multiple times per winter and reliably trigger gas price spikes within days.

## Required Keys
- None
