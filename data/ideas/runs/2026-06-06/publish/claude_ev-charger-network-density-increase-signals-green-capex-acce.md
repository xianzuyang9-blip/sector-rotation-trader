# Ev Charger Network Density Increase Signals Green Capex Acceleration

**Idea ID:** `ev-charger-network-density-increase-signals-green-capex-acce`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When weekly average EV charger installations exceed prior 12-week rolling mean by >8%, it signals government incentive acceleration or private capex surge supporting EV adoption. Charger expansion indicates semiconductor and software demand from EV infrastructure buildout.

## Universe
- XLK

## Data Sources
- OpenChargeMap API daily charger station counts by region via openchargemap adapter

## Signal Logic
When 7-day average new chargers > 12-week MA × 1.08, enter long XLK

## Entry / Exit
Entry: When 7-day average new chargers > 12-week MA × 1.08, enter long XLK Exit: Exit after 12 trading days or when charger installation rate falls below 12-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap API daily charger station counts by region via openchargemap adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Charger deployments cluster around policy rollouts; 8%+ spikes occur 1-2 times per quarter.

## Required Keys
- None
