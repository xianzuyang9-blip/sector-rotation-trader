# Freight Rail Car Utilization Snap-down Rebound

**Idea ID:** `freight-rail-car-utilization-snap-down-rebound`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Rail equipment utilization drops >8% week-over-week (demand shock), then snaps back as supply chain re-normalizes or demand catches up. Industrials and transportation stocks bounce hard on recovery in goods movement; signals economic activity resumption.

## Universe
- XLI

## Data Sources
- FRED series RAILROADEQUIPMENT (Rail Equipment Utilization Index) weekly

## Signal Logic
If weekly rail utilization index drops >8% WoW and closes above prior week open

## Entry / Exit
Entry: If weekly rail utilization index drops >8% WoW and closes above prior week open Exit: After 10 trading days or when utilization rebounds >5% from entry low

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series RAILROADEQUIPMENT (Rail Equipment Utilization Index) weekly via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Rail utilization is cyclical and volatile; 8%+ drops occur 2–4 times annually with quick reversions within 7–14 days.

## Required Keys
- None
