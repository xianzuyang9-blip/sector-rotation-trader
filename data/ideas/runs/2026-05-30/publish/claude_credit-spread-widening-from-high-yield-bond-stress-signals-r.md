# Credit Spread Widening From High-yield Bond Stress Signals Recession Risk

**Idea ID:** `credit-spread-widening-from-high-yield-bond-stress-signals-r`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When daily HY OAS widens >50 bps above 60-day moving average and closes above it, credit stress spikes signal equity risk-off; cyclical sectors (XLI, XLY) underperform XLV. Credit stress signals deteriorating corporate health and recession fears; industrials and discretionary suffer first.

## Universe
- XLI

## Data Sources
- FRED high-yield OAS spread (series: BAMLH0A0HYM2) daily data via price_only adapter tracking relative widening vs 60-day average

## Signal Logic
If BAMLH0A0HYM2 spreads >50 bps above 60-day MA and holds for 2 consecutive days, short XLI and long XLV

## Entry / Exit
Entry: If BAMLH0A0HYM2 spreads >50 bps above 60-day MA and holds for 2 consecutive days, short XLI and long XLV Exit: Exit after 7 trading days or when spreads contract back below 130% of 60-day MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED high-yield OAS spread (series: BAMLH0A0HYM2) daily data via price_only adapter tracking relative widening vs 60-day average via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: HY spreads widen episodically; events fire multiple times per quarter during volatility spikes.

## Required Keys
- None
