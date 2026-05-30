# Labor Market Weakness Reflected In Adp Employment Miss

**Idea ID:** `labor-market-weakness-reflected-in-adp-employment-miss`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When ADP employment growth drops >100k below prior month or 2-month average, market reprices Fed rate-cut expectations, creating bullish rotation into XLV and defensive sectors within 2-5 days. Weaker labor data signals lower-for-longer rates, benefiting defensive healthcare valuations over cyclicals.

## Universe
- XLV

## Data Sources
- FRED ADP Employment data (series: EMPSAPCOMP) published monthly, historical daily interpolation via price_only adapter on SPY volatility around release dates

## Signal Logic
If latest ADP print is >100k below 2-month average, enter long XLV and short XLY equally weighted

## Entry / Exit
Entry: If latest ADP print is >100k below 2-month average, enter long XLV and short XLY equally weighted Exit: Exit after 7 trading days or when next major labor report (NFP) is released

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED ADP Employment data (series: EMPSAPCOMP) published monthly, historical daily interpolation via price_only adapter on SPY volatility around release dates via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: ADP reports monthly; misses occur 3-4 times per year on average, and market reacts within days.

## Required Keys
- None
