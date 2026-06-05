# Utility Sector Relative Strength Reversal After Volatility Crush

**Idea ID:** `utility-sector-relative-strength-reversal-after-volatility-c`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When XLU volatility compresses sharply below its 90-day median while underperforming broad market, defensive rotation often triggers mean-reversion buying in utilities as risk appetite stabilizes. Utility sectors are defensive hedges; after volatility crush cycles, utilities often outperform as investors rebuild hedges and reduce equity risk.

## Universe
- XLU

## Data Sources
- Yahoo Finance daily prices for XLU, XLY, and SPY through price_only adapter; compute 30-day realized volatility

## Signal Logic
If 20-day realized volatility of XLU falls 25% below 90-day median AND XLU underperforms SPY by 2% over 5 trading days, enter long position

## Entry / Exit
Entry: If 20-day realized volatility of XLU falls 25% below 90-day median AND XLU underperforms SPY by 2% over 5 trading days, enter long position Exit: Exit after 8 trading days or if XLU volatility re-expands above 90-day median

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for XLU, XLY, and SPY through price_only adapter; compute 30-day realized volatility via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Volatility cycles in utilities are frequent and driven by interest rate expectations; signal fires 2-3 times per quarter.

## Required Keys
- None
