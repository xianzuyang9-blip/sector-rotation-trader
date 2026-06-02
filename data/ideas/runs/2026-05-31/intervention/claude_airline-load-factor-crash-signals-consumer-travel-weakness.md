# Airline Load Factor Crash Signals Consumer Travel Weakness

**Idea ID:** `airline-load-factor-crash-signals-consumer-travel-weakness`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sharp drops in airline load factors (>2 percentage points week-over-week) signal traveler demand collapse. Consumer discretionary and hospitality stocks weaken. Lower load factors presage leisure travel decline; hotels, restaurants, attractions, and retail near airports face demand compression.

## Universe
- XLY

## Data Sources
- BTS airline load factor weekly proxy data via bts_airline_load_factor adapter

## Signal Logic
If weekly BTS load factor falls >2 percentage points from prior week, short XLY on next open

## Entry / Exit
Entry: If weekly BTS load factor falls >2 percentage points from prior week, short XLY on next open Exit: Exit after 9 trading days or if load factor recovers 1.5 points from entry week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use BTS airline load factor weekly proxy data via bts_airline_load_factor adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Airline demand is volatile; seasonal demand swings ensure 2+ point drops occur multiple times per quarter.

## Required Keys
- None
