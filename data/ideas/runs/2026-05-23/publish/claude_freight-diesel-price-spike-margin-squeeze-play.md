# Freight Diesel Price Spike Margin Squeeze Play

**Idea ID:** `freight-diesel-price-spike-margin-squeeze-play`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When diesel prices jump >5% in a single week without corresponding freight index rallies, trucking operator margins compress sharply. Historical data shows this triggers short-covering rallies in XRT as logistics costs suddenly normalize. Retailers benefit from lower expected logistics costs when fuel spikes temporarily stall demand, creating pricing relief.

## Universe
- XRT

## Data Sources
- FRED series GASDESW (Diesel Sales Price) weekly data

## Signal Logic
If weekly diesel price change exceeds +5% and XRT lags SPY by >1% over same week

## Entry / Exit
Entry: If weekly diesel price change exceeds +5% and XRT lags SPY by >1% over same week Exit: After 8 trading days or once diesel stabilizes and XRT catches up to SPY

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series GASDESW (Diesel Sales Price) weekly data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Fuel price volatility spikes multiple times per month due to weather, refinery outages, and OPEC signals.

## Required Keys
- None
