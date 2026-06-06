# Gasoline Price Spike Triggers Consumer Staples Rotation

**Idea ID:** `gasoline-price-spike-triggers-consumer-staples-rotation`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly gasoline prices spike above 52-week moving average by >8%, signaling input cost pressure. Consumer staples stocks outperform discretionary on fuel shock. Staples are defensive and less price-sensitive; discretionary gets crushed on fuel/transport cost fears.

## Universe
- XLP

## Data Sources
- FRED series GASREGCOVW (weekly gasoline prices)

## Signal Logic
If GASREGCOVW > (52-week MA + 8%), buy XLP and short XLY equally weighted

## Entry / Exit
Entry: If GASREGCOVW > (52-week MA + 8%), buy XLP and short XLY equally weighted Exit: Exit when GASREGCOVW drops below 52-week MA or after 15 trading days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series GASREGCOVW (weekly gasoline prices) via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Gasoline prices move weekly and spike above MA thresholds 3-4 times per quarter; highly observable in commodity markets.

## Required Keys
- None
