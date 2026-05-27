# Google Trends Surge In Pest Control Service Searches Signals Consumer Stress Healthcare Sector Demand

**Idea ID:** `google-trends-surge-in-pest-control-service-searches-signals`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in pest control search interest indicate reactive household maintenance spending during stress periods or seasonal pest surges; correlates with consumer financial pressure and home repair urgency. Rising pest control searches indicate unplanned household spending and deferred discretionary purchases; signals consumer budget pressure reducing retail/dining spending.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for keyword 'pest control service near me'

## Signal Logic
Weekly Google Trends index for 'pest control service' rises >35% from 8-week rolling average

## Entry / Exit
Entry: Weekly Google Trends index for 'pest control service' rises >35% from 8-week rolling average Exit: After 10 trading days OR index falls back below 115% of 8-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for keyword 'pest control service near me' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal pest waves and weather-driven infestations trigger search spikes spring/summer; summer 2025 will see multiple >35% spikes.

## Required Keys
- None
