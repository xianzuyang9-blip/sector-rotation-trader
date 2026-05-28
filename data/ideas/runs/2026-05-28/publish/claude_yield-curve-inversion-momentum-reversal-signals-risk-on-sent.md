# Yield Curve Inversion Momentum Reversal Signals Risk-on Sentiment Shift

**Idea ID:** `yield-curve-inversion-momentum-reversal-signals-risk-on-sent`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When yield curve moves from inverted territory (negative spread) back into positive territory by 10+ basis points over 5 trading days, it signals Fed pivot expectations and risk appetite restoration. Curve normalization from inversion signals lower recession risk and higher growth expectations; technology and growth stocks benefit from lower perceived discount rates.

## Universe
- XLK

## Data Sources
- FRED series T10Y2Y (10-year minus 2-year yield spread) daily via fred_series adapter

## Signal Logic
When T10Y2Y spread rises 10+ basis points in 5-day window and crosses zero moving from negative

## Entry / Exit
Entry: When T10Y2Y spread rises 10+ basis points in 5-day window and crosses zero moving from negative Exit: After 10 trading days or if spread inverts again by 5+ basis points

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series T10Y2Y (10-year minus 2-year yield spread) daily via fred_series adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Yield curve inversions and normalizations occur 2–3 times per year during policy uncertainty; 5-day swings of 10+ bps are common during Fed meeting cycles and inflation pivot narratives.

## Required Keys
- None
