# Ev Charger Rollout Deceleration Signals Green Energy Capex Pullback

**Idea ID:** `ev-charger-rollout-deceleration-signals-green-energy-capex-p`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly growth in public EV charger installations declines sharply, it signals slowing green energy infrastructure investment and policy support; precedes energy transition slowdown. EV charger slowdown signals reduced government green energy policy execution and capital deployment; negative for renewable transition thesis.

## Universe
- XLE

## Data Sources
- OpenChargeMap API weekly charger count increments across North America

## Signal Logic
When weekly charger count growth rate falls below 0.5% and is below 52-week moving average of growth rate, enter short XLE

## Entry / Exit
Entry: When weekly charger count growth rate falls below 0.5% and is below 52-week moving average of growth rate, enter short XLE Exit: Exit after 8 trading days or when growth rate rebounds above 1%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap API weekly charger count increments across North America via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Charger deployment fluctuates with funding cycles and policy changes; growth rate dips occur 1–2 times per quarter.

## Required Keys
- None
