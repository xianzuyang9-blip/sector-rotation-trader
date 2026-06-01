# Hotel Occupancy Rate Collapse Signals Travel Recession

**Idea ID:** `hotel-occupancy-rate-collapse-signals-travel-recession`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Hotel occupancy drops sharply during economic slowdowns, pandemics, or post-holiday periods. A 3%+ drop from prior week signals near-term travel demand weakness. Hospitality and leisure discretionary spending decline when occupancy crashes.

## Universe
- XLY

## Data Sources
- FRED series HOUST2 (Hotel Occupancy Rate) via fred_series adapter

## Signal Logic
If occupancy rate falls 3% or more week-over-week AND drops below its 12-week MA

## Entry / Exit
Entry: If occupancy rate falls 3% or more week-over-week AND drops below its 12-week MA Exit: After 3 weeks or once occupancy rises for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series HOUST2 (Hotel Occupancy Rate) via fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seasonal dips and economic noise cause 3%+ weekly swings 8-10 times per year.

## Required Keys
- None
