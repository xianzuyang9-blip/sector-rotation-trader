# Copper Price Collapse Signals Industrial Recession Fear

**Idea ID:** `copper-price-collapse-signals-industrial-recession-fear`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Copper is recession canary; drop more than 3% in one week signals weakening demand and industrial slowdown. Industrials and materials follow within days. Copper demand correlates tightly with manufacturing and construction; collapse presages XLI weakness as machinery, equipment orders slow.

## Universe
- XLI

## Data Sources
- Yahoo Finance daily prices for DBB (Commodities ETF tracking copper) via price_only adapter

## Signal Logic
If DBB falls more than 3% over 5 trading days, short XLI at close on day 5

## Entry / Exit
Entry: If DBB falls more than 3% over 5 trading days, short XLI at close on day 5 Exit: Exit after 7 trading days or if DBB closes above entry-day close

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for DBB (Commodities ETF tracking copper) via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Commodity volatility ensures 3% 5-day drops occur 2-3 times per quarter; 30-day window catches at least one.

## Required Keys
- None
