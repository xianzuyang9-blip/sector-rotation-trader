# Ism Manufacturing Weakness Print Bounce-back Signal

**Idea ID:** `ism-manufacturing-weakness-print-bounce-back-signal`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
ISM Manufacturing index drops >3 points month-over-month (contraction signal), triggering bearish reaction, then bounces as investors realize it's cyclical noise or data was front-loaded. Industrials and materials sell off on ISM miss, then rally hard on expected reversion within earnings cycle.

## Universe
- XLI

## Data Sources
- FRED series MMNRNJ (ISM Manufacturing Index, monthly release)

## Signal Logic
Day after ISM release, if index drops >3 pts MoM and close > open

## Entry / Exit
Entry: Day after ISM release, if index drops >3 pts MoM and close > open Exit: After 5 trading days or when XLI outperforms SPY by >1% over 2 days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series MMNRNJ (ISM Manufacturing Index, monthly release) via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: ISM swings >3 pts occur 4–6 times annually; post-release bounce-backs within 3–7 days are highly consistent.

## Required Keys
- None
