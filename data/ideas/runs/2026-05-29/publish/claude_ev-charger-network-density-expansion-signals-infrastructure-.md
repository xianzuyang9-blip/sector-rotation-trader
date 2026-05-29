# Ev Charger Network Density Expansion Signals Infrastructure Thesis

**Idea ID:** `ev-charger-network-density-expansion-signals-infrastructure-`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Monthly charger network expansion exceeding 5% signals accelerating EV adoption and infrastructure investment, bullish for utilities and green energy stocks. Charger network growth correlates with utility capex deployment and renewable grid demand, supporting long-term power demand.

## Universe
- XLU

## Data Sources
- OpenChargeMap API (monthly EV charger count by state/region)

## Signal Logic
When monthly EV charger count growth exceeds 5% month-over-month and exceeds 12-month average growth rate by 2%+

## Entry / Exit
Entry: When monthly EV charger count growth exceeds 5% month-over-month and exceeds 12-month average growth rate by 2%+ Exit: After 4 weeks or if growth drops below 2% month-over-month

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap API (monthly EV charger count by state/region) via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Charger expansion is steady; 5%+ monthly growth triggers 3–4 times per year during policy/subsidy rollouts.

## Required Keys
- None
