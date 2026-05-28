# Ev Charger Installation Pace Acceleration Signals Green Energy Capex Surge Bullish Xle Rotation

**Idea ID:** `ev-charger-installation-pace-acceleration-signals-green-ener`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly increases in EV charger count of 5%+ signal accelerating government EV infrastructure spending and private utility capex buildout, supporting energy transition capex demand. Utilities and energy infrastructure firms benefit from EV charging buildout contracts; legacy energy transition investments create sustained revenue growth in the energy sector.

## Universe
- XLE

## Data Sources
- OpenChargeMap charger count by region, updated weekly via openchargemap adapter

## Signal Logic
When weekly EV charger count increases 5%+ from 4-week average and 52-week trend is positive

## Entry / Exit
Entry: When weekly EV charger count increases 5%+ from 4-week average and 52-week trend is positive Exit: After 4 weeks or when charger growth rate drops below 2% for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap charger count by region, updated weekly via openchargemap adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: EV charging infrastructure expands in waves tied to federal spending cycles and regional utility programs; 5%+ weekly surges occur 3–5 times annually, especially around legislative action windows.

## Required Keys
- None
