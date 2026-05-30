# Airline Load Factor Compression Signals Travel Demand Weakness

**Idea ID:** `airline-load-factor-compression-signals-travel-demand-weakne`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When aggregate US airline load factor drops >3 percentage points below 13-week average (indicating lower-than-expected travel demand), XLY travel/leisure stocks see selling pressure within 3-5 days. Falling load factors signal weakening consumer travel demand, impacting discretionary spending outlook.

## Universe
- XLY

## Data Sources
- BTS airline load factor data weekly via bts_airline_load_factor adapter tracking major US carriers

## Signal Logic
If BTS aggregate load factor drops >3 ppts below 13-week rolling average, short XLY

## Entry / Exit
Entry: If BTS aggregate load factor drops >3 ppts below 13-week rolling average, short XLY Exit: Exit after 10 trading days or when load factor rebounds above 101% of 13-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use BTS airline load factor data weekly via bts_airline_load_factor adapter tracking major US carriers via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Airline data is published weekly; demand shocks trigger load factor drops multiple times per quarter seasonally.

## Required Keys
- None
