# Ev Charger Buildout Pace Acceleration From Openchargemap Growth

**Idea ID:** `ev-charger-buildout-pace-acceleration-from-openchargemap-gro`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly net charger additions exceed 3-month rolling average by >20% (indicating infrastructure investment surge), EV adoption momentum signals bullish tech/industrial transition thesis. Accelerating charger deployment signals adoption of EV tech platforms, battery management systems, and digital infrastructure; semiconductor and software demand benefits.

## Universe
- XLK

## Data Sources
- OpenChargeMap public API charger count by region, weekly snapshots

## Signal Logic
Weekly charger additions >120% of 12-week rolling average AND 2-week cumulative additions >250 units

## Entry / Exit
Entry: Weekly charger additions >120% of 12-week rolling average AND 2-week cumulative additions >250 units Exit: After 20 trading days OR weekly additions fall back to 90% of rolling average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap public API charger count by region, weekly snapshots via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Infrastructure grants and regional EV mandates create periodic surges in charger deployment; spikes above rolling average occur 6–8 times per year.

## Required Keys
- None
