# Used Car Price Index Reversal Signals Consumer Credit Relief

**Idea ID:** `used-car-price-index-reversal-signals-consumer-credit-relief`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sharp drops in used car prices after sustained highs indicate cooling credit demand and easing transportation cost burden, typically bullish for discretionary spending. Lower used car prices reduce household debt service, freeing cash for discretionary consumption.

## Universe
- XLY

## Data Sources
- FRED series MMNRNJ (Manheim Used Vehicle Index) weekly data

## Signal Logic
When MMNRNJ drops 3%+ week-over-week after trading above 90th percentile of trailing 6-month range

## Entry / Exit
Entry: When MMNRNJ drops 3%+ week-over-week after trading above 90th percentile of trailing 6-month range Exit: After 4 weeks or if index reverses 2%+ to upside

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series MMNRNJ (Manheim Used Vehicle Index) weekly data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Used car market is volatile; 3% weekly swings occur 2–3 times per quarter, especially in seasonal transitions.

## Required Keys
- None
