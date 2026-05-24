# Commodity Input Price Shock Cascade

**Idea ID:** `commodity-input-price-shock-cascade`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly PPI intermediate goods rise >1% WoW, it signals input cost compression upstream and forces energy/basic materials repricing. Input price spikes push energy/materials sector margins higher short-term and reprices commodity hedges.

## Universe
- XLE

## Data Sources
- FRED series MMNRNJ (Producer Price Index: Intermediate Materials) weekly

## Signal Logic
If weekly PPI change >+1.0% AND XLE closes above 5-day MA

## Entry / Exit
Entry: If weekly PPI change >+1.0% AND XLE closes above 5-day MA Exit: After 10 trading days or when PPI reverts >0.5% in opposite direction

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series MMNRNJ (Producer Price Index: Intermediate Materials) weekly via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Commodity shocks and PPI volatility spike weekly; threshold is accessible 2–3 times per month.

## Required Keys
- None
