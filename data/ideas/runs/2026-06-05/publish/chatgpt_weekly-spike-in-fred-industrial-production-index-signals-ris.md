# Weekly Spike In Fred Industrial Production Index Signals Rising Industrial Sector Demand Momentum

**Idea ID:** `weekly-spike-in-fred-industrial-production-index-signals-ris`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sharp increase in industrial production often presages stronger earnings and sector momentum. Industrial sector benefits from rising output and economic activity.

## Universe
- XLI

## Data Sources
- FRED weekly industrial production index

## Signal Logic
Enter long XLI when weekly industrial production increases by more than 0.5% week-over-week

## Entry / Exit
Entry: Enter long XLI when weekly industrial production increases by more than 0.5% week-over-week Exit: Exit after 6 weeks or once growth slows below 0.2%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly industrial production index via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Industrial production data shows regular fluctuations tied to economic cycles, providing multiple signals yearly.

## Required Keys
- None
