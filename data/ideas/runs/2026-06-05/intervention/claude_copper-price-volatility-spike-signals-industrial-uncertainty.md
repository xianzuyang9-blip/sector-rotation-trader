# Copper Price Volatility Spike Signals Industrial Uncertainty

**Idea ID:** `copper-price-volatility-spike-signals-industrial-uncertainty`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Daily COPX volatility (20-day rolling standard deviation) exceeds 3.5%, signaling economic uncertainty and manufacturing demand shock. Copper volatility spike reflects industrial capex uncertainty; manufactures and industrials pull in capex under uncertainty.

## Universe
- XLI

## Data Sources
- Yahoo Finance daily prices for COPX (copper miners ETF) via price_only adapter

## Signal Logic
If 20-day COPX volatility > 3.5%, short XLI and long XLU (safe haven)

## Entry / Exit
Entry: If 20-day COPX volatility > 3.5%, short XLI and long XLU (safe haven) Exit: After 11 trading days or when COPX volatility drops below 2.8%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for COPX (copper miners ETF) via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Copper volatility spikes 3-5 times quarterly on rate shocks and China growth data; 3.5% threshold fires 2-3 times per month.

## Required Keys
- None
