# Gasoline Price Spike Triggers Consumer Discretionary Rotation

**Idea ID:** `gasoline-price-spike-triggers-consumer-discretionary-rotatio`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sharp week-over-week gasoline price jumps above 5 cents compress consumer disposable income and trigger defensive sector rotation. Consumer spending slows measurably within 2-3 weeks. Consumer discretionary spending directly correlates with gas affordability; spike signals demand compression for retail, restaurants, travel.

## Universe
- XLY

## Data Sources
- FRED series GASREGCOVW (Weekly U.S. Regular Gasoline Prices) via fred_series adapter

## Signal Logic
If weekly gasoline price rises more than 5 cents from prior week close, short XLY on open of next trading day

## Entry / Exit
Entry: If weekly gasoline price rises more than 5 cents from prior week close, short XLY on open of next trading day Exit: Exit after 10 trading days or if gasoline price falls 3 cents from entry week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series GASREGCOVW (Weekly U.S. Regular Gasoline Prices) via fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: FRED gasoline data updates weekly and volatile price moves of 5+ cents occur several times per quarter, easily hitting within 30 days.

## Required Keys
- None
