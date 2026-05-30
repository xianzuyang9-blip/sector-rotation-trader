# Ev Charger Network Rollout Acceleration Signals Clean Energy Tailwind

**Idea ID:** `ev-charger-network-rollout-acceleration-signals-clean-energy`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly charger deployment accelerates >15% above 12-week average (signaling investment phase), clean energy and EV-linked equities (XLK, XLI) outperform as infrastructure demand becomes tangible. Infrastructure buildout boosts industrial/materials demand; signals policy tailwinds for clean energy transition.

## Universe
- XLI

## Data Sources
- OpenChargeMap API weekly charger count snapshots across major US metro areas (density metric: chargers per 1000 EVs)

## Signal Logic
If aggregate US charger count grows >15% week-over-week above 12-week average, enter long XLI

## Entry / Exit
Entry: If aggregate US charger count grows >15% week-over-week above 12-week average, enter long XLI Exit: Exit after 14 trading days or when growth rate falls below 105% of 12-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap API weekly charger count snapshots across major US metro areas (density metric: chargers per 1000 EVs) via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Charger deployment follows predictable quarterly government funding cycles; multiple acceleration phases per year.

## Required Keys
- None
