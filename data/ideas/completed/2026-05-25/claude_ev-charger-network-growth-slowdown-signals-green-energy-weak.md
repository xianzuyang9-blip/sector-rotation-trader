# Ev Charger Network Growth Slowdown Signals Green Energy Weakness

**Idea ID:** `ev-charger-network-growth-slowdown-signals-green-energy-weak`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Slowdown or plateau in EV charger installation pace signals weakening clean energy sector momentum and policy/subsidy concerns. Slower EV infrastructure build suggests reduced clean energy capital deployment and investor sentiment downturn in renewables.

## Universe
- XLE

## Data Sources
- OpenChargeMap EV charger location counts (total installed and operational) weekly snapshot

## Signal Logic
When weekly net new EV chargers installed falls below 5th percentile of trailing 12-week rolling average AND cumulative growth rate <2% month-over-month

## Entry / Exit
Entry: When weekly net new EV chargers installed falls below 5th percentile of trailing 12-week rolling average AND cumulative growth rate <2% month-over-month Exit: After 10 trading days or when installation rate rebounds above 25th percentile

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap EV charger location counts (total installed and operational) weekly snapshot via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: EV charger growth fluctuates seasonally and with policy shifts; slowdowns occur 2–3 times per year during funding cycles or subsidy transitions.

## Required Keys
- None
