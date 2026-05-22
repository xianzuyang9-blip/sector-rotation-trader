# Travel Sentiment Surge From Airline Load Factor Rebound Signals Discretionary Recovery

**Idea ID:** `travel-sentiment-surge-from-airline-load-factor-rebound-sign`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When airline load factors jump >2 percentage points week-over-week (e.g., 82% to 84.5%), it signals unexpected travel demand surge, triggering hospitality and leisure spending expectations. Airlines are leading indicator for leisure travel; rising load factors predict hotel, restaurant, and entertainment spending booms.

## Universe
- XLY

## Data Sources
- BTS airline load factor (weekly average) via bts_airline_load_factor adapter

## Signal Logic
If BTS load factor jumps >2 percentage points WoW AND closes above 52-week MA, buy XLY

## Entry / Exit
Entry: If BTS load factor jumps >2 percentage points WoW AND closes above 52-week MA, buy XLY Exit: After 7 trading days OR if load factor drops >1.5 percentage points in following week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use BTS airline load factor (weekly average) via bts_airline_load_factor adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weekly BTS data shows 2+ percentage point swings 4–6 times per year, especially around holidays and seasonal travel peaks.

## Required Keys
- None
