# Utility Demand Surge From Heat Wave Google Trends Signals Energy Sector Strength

**Idea ID:** `utility-demand-surge-from-heat-wave-google-trends-signals-en`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in heat wave and HVAC repair searches correlate with residential/commercial electricity demand surges. Utilities and energy stocks rally on margin expansion expectations. Utilities profit from peak demand periods; heat wave signals higher volumes and better pricing power in generation and transmission.

## Universe
- XLU

## Data Sources
- Google Trends weekly search volume for 'heat wave forecast' and 'ac repair near me' via google_trends adapter

## Signal Logic
If weekly combined search volume for heat wave and ac repair doubles from 4-week average, long XLU on next Monday open

## Entry / Exit
Entry: If weekly combined search volume for heat wave and ac repair doubles from 4-week average, long XLU on next Monday open Exit: Exit after 10 trading days or if search volume falls below 1.5x the 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'heat wave forecast' and 'ac repair near me' via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal heat waves and cold snaps occur predictably; summer/winter 30-day windows guarantee at least one spike.

## Required Keys
- None
