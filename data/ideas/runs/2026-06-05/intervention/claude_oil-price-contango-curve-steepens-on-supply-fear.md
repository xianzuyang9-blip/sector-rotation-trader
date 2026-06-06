# Oil Price Contango Curve Steepens On Supply Fear

**Idea ID:** `oil-price-contango-curve-steepens-on-supply-fear`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Oil futures curve steepens (front-month to 3-month spread widens >$2.50 per barrel) in single day. Signals supply tightness fear and storage building. Energy companies benefit from supply-constrained environments and higher futures expectations.

## Universe
- XLE

## Data Sources
- Yahoo Finance daily prices for USO (crude oil ETF) and price_only adapter for historical volatility and roll spread

## Signal Logic
If USO front-3mo spread > prior 20-day MA + $2.50, long XLE

## Entry / Exit
Entry: If USO front-3mo spread > prior 20-day MA + $2.50, long XLE Exit: After 8 trading days or when spread contracts below prior 5-day MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for USO (crude oil ETF) and price_only adapter for historical volatility and roll spread via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Oil futures curve steepens 1-2 times weekly on supply shocks; $2.50 spreads occur in 2-3 week windows multiple times per quarter.

## Required Keys
- None
