# Hotel Occupancy Rate Weekly Collapse Snap

**Idea ID:** `hotel-occupancy-rate-weekly-collapse-snap`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Hotel occupancy rate (measured via alternative weekly hospitality data or event calendars) drops >12% WoW on weather/event cancellation, then snaps back as bookings normalize. Travel/leisure crash, then bounce on realization shock is temporary; consumer discretionary recovers.

## Universe
- XLY

## Data Sources
- FRED series HOUST1MUSA (1-Family House Starts, or proxy via hospitality leading indicators) weekly

## Signal Logic
If hotel occupancy proxy metric drops >12% WoW and closes above prior week midpoint

## Entry / Exit
Entry: If hotel occupancy proxy metric drops >12% WoW and closes above prior week midpoint Exit: After 7 trading days or when occupancy rebounds >6% from trough

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series HOUST1MUSA (1-Family House Starts, or proxy via hospitality leading indicators) weekly via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal hotel demand swings and weather events cause weekly volatility; 12%+ drops occur 3–5 times annually.

## Required Keys
- None
