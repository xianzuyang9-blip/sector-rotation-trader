# Ev Charging Network Expansion Acceleration Signals Green Capex Boom

**Idea ID:** `ev-charging-network-expansion-acceleration-signals-green-cap`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly new charger installations exceed 3% growth week-over-week for 2+ weeks, it signals acceleration in renewable infrastructure spending and positive capex sentiment. EV charging buildout requires industrial equipment, materials, and electrical infrastructure; acceleration signals strong green capex demand.

## Universe
- XLI

## Data Sources
- OpenChargeMap weekly active EV charger counts (public data, updated daily) through openchargemap adapter

## Signal Logic
If weekly net new EV charger additions exceed the 12-week rolling average by >25% AND the growth rate is >2.5% week-over-week

## Entry / Exit
Entry: If weekly net new EV charger additions exceed the 12-week rolling average by >25% AND the growth rate is >2.5% week-over-week Exit: After 4 weeks or if weekly growth rate drops below 1% for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap weekly active EV charger counts (public data, updated daily) through openchargemap adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Charger network expansion is continuous; weekly volatility in growth rates crosses thresholds monthly due to funding cycles and deployment timelines.

## Required Keys
- None
