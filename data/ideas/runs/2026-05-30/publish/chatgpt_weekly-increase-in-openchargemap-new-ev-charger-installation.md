# Weekly Increase In Openchargemap New Ev Charger Installations Signals Consumer Tech Infrastructure Growth

**Idea ID:** `weekly-increase-in-openchargemap-new-ev-charger-installation`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A rising rate of new EV charger installations signals accelerating EV adoption and infrastructure buildout. EV infrastructure growth boosts consumer discretionary and technology sectors tied to EV ecosystem.

## Universe
- XLC

## Data Sources
- OpenChargeMap weekly new EV charger counts

## Signal Logic
If weekly new charger counts increase more than 15% week-over-week

## Entry / Exit
Entry: If weekly new charger counts increase more than 15% week-over-week Exit: Exit after 4 weeks or when new installations fall below 4-week moving average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap weekly new EV charger counts via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: EV charger installation rates fluctuate with government incentives and corporate deployments.

## Required Keys
- None
