# Ev Charger Installation Acceleration Trend Momentum Shift

**Idea ID:** `ev-charger-installation-acceleration-trend-momentum-shift`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly EV charger installation count jumps >25% WoW (grant round release, policy push, or regional buildout), signaling green tech demand inflection. EV charging buildout signals tech/infrastructure play; semiconductor and electronics demand benefits.

## Universe
- XLK

## Data Sources
- OpenChargeMap network growth (new charger installations per week) via openchargemap adapter

## Signal Logic
If weekly new charger count > 1.25× prior 4-week MA, close above open

## Entry / Exit
Entry: If weekly new charger count > 1.25× prior 4-week MA, close above open Exit: After 10 trading days or when charger growth rate normalizes back to <1.1× MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap network growth (new charger installations per week) via openchargemap adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: EV charger installations are accelerating; 25%+ surges occur 2–3 times per quarter; momentum holds 7–14 days.

## Required Keys
- None
