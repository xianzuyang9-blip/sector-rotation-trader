# Airline Seat Load Factor Compression Signals Travel Weakness

**Idea ID:** `airline-seat-load-factor-compression-signals-travel-weakness`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Falling load factors (more empty seats) precede airline margin compression and broader discretionary travel slowdown by 1–3 weeks. Airline weakness signals consumer travel confidence deterioration; hospitality and leisure stocks follow within 2 weeks.

## Universe
- XLY

## Data Sources
- BTS airline load factor (available seat miles vs. revenue passenger miles) weekly proxy via port/airline data feeds

## Signal Logic
When weekly aggregate US airline load factor falls >2.5 percentage points from prior month average AND closes below 80% capacity utilization

## Entry / Exit
Entry: When weekly aggregate US airline load factor falls >2.5 percentage points from prior month average AND closes below 80% capacity utilization Exit: After 7 trading days or when load factor rebounds above 82%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use BTS airline load factor (available seat miles vs. revenue passenger miles) weekly proxy via port/airline data feeds via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Airline load factors vary seasonally and cyclically; drops >2.5% occur multiple times per quarter during demand transitions.

## Required Keys
- None
