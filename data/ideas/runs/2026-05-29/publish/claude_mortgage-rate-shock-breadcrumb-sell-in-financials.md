# Mortgage Rate Shock Breadcrumb Sell In Financials

**Idea ID:** `mortgage-rate-shock-breadcrumb-sell-in-financials`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Daily jumps in mortgage rates exceeding 25 basis points signal Fed shock or risk-off repricing, compressing mortgage origination demand and bank net interest margin expectations. Rapid rate increases hurt mortgage banking revenues and weigh on bank equity multiples due to margin compression fears.

## Universe
- XLF

## Data Sources
- FRED series MORTGAGE30US (30-year mortgage rate) daily data

## Signal Logic
When MORTGAGE30US rises 25+ basis points in a single day and closes above 20-day moving average

## Entry / Exit
Entry: When MORTGAGE30US rises 25+ basis points in a single day and closes above 20-day moving average Exit: After 5 trading days or if rate falls 15+ basis points

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series MORTGAGE30US (30-year mortgage rate) daily data via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Mortgage rate volatility spikes 1–2 times per month during Fed communication cycles and economic data surprises.

## Required Keys
- None
