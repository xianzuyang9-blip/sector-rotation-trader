# Lumber Price Rebound Signals Housing Demand Resurgence

**Idea ID:** `lumber-price-rebound-signals-housing-demand-resurgence`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Weekly lumber prices rise >8% from prior week, signaling construction material demand acceleration and housing momentum. Lumber spikes signal homebuilding activity and construction starts; REITs and home builders rally.

## Universe
- XLRE

## Data Sources
- FRED series DCOILWTICO (use as proxy for commodity cycle) and Yahoo Finance daily prices for LVL (lumber spot prices via commodity tracker)

## Signal Logic
If LVL > (prior week close * 1.08), long XLRE

## Entry / Exit
Entry: If LVL > (prior week close * 1.08), long XLRE Exit: After 9 trading days or when LVL drops below 5-day MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series DCOILWTICO (use as proxy for commodity cycle) and Yahoo Finance daily prices for LVL (lumber spot prices via commodity tracker) via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Lumber prices spike weekly on weather, demand, and supply shocks; 8% moves occur 2-3 times monthly seasonally.

## Required Keys
- None
