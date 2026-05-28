# Crude Oil Volatility Spike Above 25 Vix Equivalent Signals Energy Sector Risk-off Trade

**Idea ID:** `crude-oil-volatility-spike-above-25-vix-equivalent-signals-e`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When crude oil 20-day realized volatility exceeds 25% annualized (equivalent to VIX spike), it signals geopolitical risk or supply shock; energy equities typically underperform during volatility spikes. Oil price volatility creates margin compression uncertainty for energy producers; equities sell off during high-volatility periods as derivatives hedging costs rise and demand destruction concerns emerge.

## Universe
- XLE

## Data Sources
- Yahoo Finance daily prices for USO (crude oil ETF) and CL=F futures via price_only adapter; calculate 20-day realized volatility

## Signal Logic
When 20-day realized volatility on USO/crude exceeds 25% and closes above prior day close

## Entry / Exit
Entry: When 20-day realized volatility on USO/crude exceeds 25% and closes above prior day close Exit: After 3 trading days or when volatility drops below 20% for 1 trading day

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for USO (crude oil ETF) and CL=F futures via price_only adapter; calculate 20-day realized volatility via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Crude oil volatility exceeds 25% spikes 4–6 times per year during supply disruptions, geopolitical escalations, and demand shocks; daily triggers average 2–3 per month.

## Required Keys
- None
