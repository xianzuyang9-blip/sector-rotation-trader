# Ev Charging Network Saturation Surge

**Idea ID:** `ev-charging-network-saturation-surge`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Rapid week-over-week growth in charger deployments (>8%) signals infrastructure investment confidence and tech sector repricing. EV charging expansion signals tech/software/grid optimization demand; XLK reprices green tech secular growth.

## Universe
- XLK

## Data Sources
- OpenChargeMap EV charger counts (weekly snapshot) by region + XLK technology ETF price

## Signal Logic
If charger count growth >8% WoW and XLK closes above 5-day MA

## Entry / Exit
Entry: If charger count growth >8% WoW and XLK closes above 5-day MA Exit: After 10 trading days or when growth rate falls below 5%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap EV charger counts (weekly snapshot) by region + XLK technology ETF price via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Regional charger rollouts occur weekly with seasonal acceleration; threshold fires 2–3 times per month.

## Required Keys
- None
