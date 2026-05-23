# Energy Commodity Input Cost Relief Trade

**Idea ID:** `energy-commodity-input-cost-relief-trade`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When WTI crude falls >5% in a single week and closes below its 20-day MA, energy-intensive consumer staples and materials benefit from input cost relief. XLP outperforms SPY within 5 days as margin expansion expectations rise. Lower energy costs directly expand margins for staples and logistics, improving pricing power.

## Universe
- XLP

## Data Sources
- FRED series DCOILWTICO (WTI Crude Oil Price) daily data

## Signal Logic
If weekly WTI decline exceeds 5% AND WTI closes below 20-day MA, buy XLP at close

## Entry / Exit
Entry: If weekly WTI decline exceeds 5% AND WTI closes below 20-day MA, buy XLP at close Exit: After 7 trading days or if WTI bounces back above 20-day MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series DCOILWTICO (WTI Crude Oil Price) daily data via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Oil price weekly volatility >5% occurs multiple times per month, creating frequent entry opportunities.

## Required Keys
- None
