# Ev Charger Network Saturation Spillover Demand Signal

**Idea ID:** `ev-charger-network-saturation-spillover-demand-signal`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When DC fast charger capacity reaches 90%+ utilization (inferred from count flattening + demand reports), EV adoption accelerates but infrastructure stress rises, triggering demand for battery tech and materials stocks. Battery materials (lithium, cobalt) and industrial metals see demand surge when charging infrastructure becomes constrained, signaling EV adoption acceleration.

## Universe
- XLB

## Data Sources
- Open Charge Map API (weekly count of Level 3 DC fast chargers in top 10 metro areas)

## Signal Logic
If weekly DC fast charger count growth falls below 0.5% YoY AND prior 4 weeks averaged >1% growth, buy XLB

## Entry / Exit
Entry: If weekly DC fast charger count growth falls below 0.5% YoY AND prior 4 weeks averaged >1% growth, buy XLB Exit: After 12 trading days OR if charger count growth rebounds above 1.5% over 2 weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open Charge Map API (weekly count of Level 3 DC fast chargers in top 10 metro areas) via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: EV charger networks grow steadily but with 2–4 week plateaus per quarter as infrastructure deployment waves hit local saturation.

## Required Keys
- None
