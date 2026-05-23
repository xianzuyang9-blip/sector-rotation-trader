# Utilities Volatility Spike Long Hedge Trade

**Idea ID:** `utilities-volatility-spike-long-hedge-trade`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When XLU's 20-day rolling correlation to VIX drops below 0.1 (near zero or negative) while broad market volatility spikes, utilities have decoupled as safe havens. This regime reversal historically completes within 5–7 days. Utilities act as volatility hedges; negative VIX correlation signals markets are pricing safe-haven demand.

## Universe
- XLU

## Data Sources
- Yahoo Finance daily prices for XLU and VIX through price_only adapter; calculate 20-day rolling correlation

## Signal Logic
If 20-day XLU-VIX correlation falls below 0.05 and VIX closes >18, buy XLU at close

## Entry / Exit
Entry: If 20-day XLU-VIX correlation falls below 0.05 and VIX closes >18, buy XLU at close Exit: After 7 trading days or once correlation normalizes above 0.15

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for XLU and VIX through price_only adapter; calculate 20-day rolling correlation via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: VIX spikes above 18 occur 2–4 times per quarter, creating windows for this correlation signal to fire.

## Required Keys
- None
