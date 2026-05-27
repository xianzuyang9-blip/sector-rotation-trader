# Airline Load Factor Weakness From Bts Data Signals Travel Demand Fade

**Idea ID:** `airline-load-factor-weakness-from-bts-data-signals-travel-de`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When airline load factors decline >3 percentage points week-over-week (e.g., 82% → 79%), demand for leisure/business travel is softening; airlines cut capacity and fares within 1–2 weeks, signaling consumer discretionary stress. Collapsing airline load factors are leading indicator of consumer travel spending pullback; signals weakness in hotels, car rentals, restaurants.

## Universe
- XLY

## Data Sources
- BTS Airline Load Factor (% seats filled) weekly, via BTS public data portal or FRED proxy

## Signal Logic
Airline load factor drops >3 percentage points week-over-week AND 2-week rolling average falls below 78%

## Entry / Exit
Entry: Airline load factor drops >3 percentage points week-over-week AND 2-week rolling average falls below 78% Exit: After 12 trading days OR load factor recovers >2 points above entry level

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use BTS Airline Load Factor (% seats filled) weekly, via BTS public data portal or FRED proxy via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal demand swings post-holiday and pre-summer produce >3 point drops monthly; recession/economic shock scenarios fire this signal weekly.

## Required Keys
- None
