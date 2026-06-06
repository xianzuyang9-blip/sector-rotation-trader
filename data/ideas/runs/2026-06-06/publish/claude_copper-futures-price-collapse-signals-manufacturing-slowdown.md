# Copper Futures Price Collapse Signals Manufacturing Slowdown

**Idea ID:** `copper-futures-price-collapse-signals-manufacturing-slowdown`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When copper prices drop >4% in a single trading day, it signals sudden demand collapse or recession fears in manufacturing-heavy sectors, triggering bearish rotation. Copper is a leading indicator of industrial demand; sharp declines precede capex cuts and manufacturing weakness.

## Universe
- XLI

## Data Sources
- Yahoo Finance daily copper futures prices via price_only adapter

## Signal Logic
If daily copper close < prior close × 0.96, short XLI and long XLU

## Entry / Exit
Entry: If daily copper close < prior close × 0.96, short XLI and long XLU Exit: Exit after 8 trading days or when copper rebounds above 2-day prior close

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily copper futures prices via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Copper futures are liquid and volatile; 4%+ daily swings occur 15-20 times per month.

## Required Keys
- None
