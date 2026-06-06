# Temperature Extreme Surge Drives Utility Demand

**Idea ID:** `temperature-extreme-surge-drives-utility-demand`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Daily maximum temperature exceeds 95F in >3 major US cities simultaneously. Signals extreme cooling demand and utility load spike. Utilities profit from peak demand events; higher loads → higher peak pricing and revenue capture.

## Universe
- XLU

## Data Sources
- Open-Meteo daily max temperature for major US cities (New York, Houston, Chicago, Phoenix)

## Signal Logic
If >3 major cities exceed 95F on same day, long XLU

## Entry / Exit
Entry: If >3 major cities exceed 95F on same day, long XLU Exit: After 7 trading days or when all cities drop below 90F for 2 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily max temperature for major US cities (New York, Houston, Chicago, Phoenix) via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Summer heat waves occur regularly; multi-city 95F+ days fire 3-5 times per summer season.

## Required Keys
- None
