# Ev Charger Installation Acceleration Signals Clean Energy Capex Surge

**Idea ID:** `ev-charger-installation-acceleration-signals-clean-energy-ca`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sustained acceleration in EV charger installation rates signal government stimulus pull-through and infrastructure investment acceleration, which precedes utility and energy transition index gains. Rapid EV charger deployment signals grid modernization spending and utility sector infrastructure capex cycles; benefits power generation and grid operators.

## Universe
- XLU

## Data Sources
- OpenChargeMap weekly charger count growth across North America through openchargemap adapter

## Signal Logic
If weekly EV charger count increase exceeds prior 6-week median by 35%, enter long position

## Entry / Exit
Entry: If weekly EV charger count increase exceeds prior 6-week median by 35%, enter long position Exit: Exit after 10 trading days or if weekly growth rate falls below 6-week median

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap weekly charger count growth across North America through openchargemap adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Charger installation is lumpy and grant-driven; acceleration waves appear 2-3 times quarterly as funding tranches deploy.

## Required Keys
- None
