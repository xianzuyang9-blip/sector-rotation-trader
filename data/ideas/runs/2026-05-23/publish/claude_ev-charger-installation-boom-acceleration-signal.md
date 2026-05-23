# Ev Charger Installation Boom Acceleration Signal

**Idea ID:** `ev-charger-installation-boom-acceleration-signal`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
EV charger deployment accelerates during quarters when federal incentive deadlines approach or state rebate programs announce funding tranches. Weekly growth rate spikes above 3% correlate with infrastructure-driven utility and materials demand. Rising charger density signals sustained industrial construction spending and electrical equipment demand.

## Universe
- XLI

## Data Sources
- OpenChargeMap API daily charger count by region aggregated to US total

## Signal Logic
If 7-day EV charger count growth rate exceeds 2.5% and accelerates above prior week's rate

## Entry / Exit
Entry: If 7-day EV charger count growth rate exceeds 2.5% and accelerates above prior week's rate Exit: After 10 trading days or if growth rate drops below 1.5% for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap API daily charger count by region aggregated to US total via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal infrastructure spending cycles and grant disbursement schedules typically accelerate charger deployment 2–3 times per quarter.

## Required Keys
- None
