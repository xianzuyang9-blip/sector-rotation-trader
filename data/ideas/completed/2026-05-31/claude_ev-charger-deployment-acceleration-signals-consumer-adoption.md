# Ev Charger Deployment Acceleration Signals Consumer Adoption Surge

**Idea ID:** `ev-charger-deployment-acceleration-signals-consumer-adoption`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Rapid week-over-week growth in public EV chargers (>3% per week) signals accelerating consumer adoption, supporting EVs and green tech stocks. EV charger expansion supports semiconductor demand (power electronics, controllers), software platforms, and charging network tech.

## Universe
- XLK

## Data Sources
- OpenChargeMap API weekly charger count growth rates via openchargemap adapter

## Signal Logic
If weekly OpenChargeMap global charger count grows >3% from prior week, long XLK on next Tuesday open

## Entry / Exit
Entry: If weekly OpenChargeMap global charger count grows >3% from prior week, long XLK on next Tuesday open Exit: Exit after 12 trading days or if growth rate falls below 1% for two consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap API weekly charger count growth rates via openchargemap adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: EV charger networks expand steadily; 3%+ weekly growth occurs frequently enough to fire multiple times per quarter.

## Required Keys
- None
