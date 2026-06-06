# Airline Load Factor Contraction Signals Travel Demand Collapse

**Idea ID:** `airline-load-factor-contraction-signals-travel-demand-collap`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When month-over-month airline load factor declines >2 percentage points, it indicates collapsing travel demand and recession pressure on discretionary consumer spending. Falling load factors precede hospitality, entertainment, and discretionary revenue declines.

## Universe
- XLY

## Data Sources
- BTS monthly airline load factor and available seat miles via bts_airline_load_factor adapter

## Signal Logic
When LF(current month) < LF(prior month) - 2.0pp, short XLY and long XLP

## Entry / Exit
Entry: When LF(current month) < LF(prior month) - 2.0pp, short XLY and long XLP Exit: Exit after 15 trading days or when LF stabilizes above prior month level

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use BTS monthly airline load factor and available seat miles via bts_airline_load_factor adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Airline load factor swings 1-3pp monthly; 2pp+ declines occur 3-4 times per year.

## Required Keys
- None
