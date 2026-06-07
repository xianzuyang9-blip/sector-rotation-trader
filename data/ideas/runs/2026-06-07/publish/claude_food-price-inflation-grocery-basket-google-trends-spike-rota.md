# Food Price Inflation Grocery Basket Google Trends Spike Rotation Signal

**Idea ID:** `food-price-inflation-grocery-basket-google-trends-spike-rota`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly search volume for grocery/food price concerns spikes >80% (consumer pain point), triggering rotation from discretionary to staples and health. Food inflation anxiety signals consumer margin pressure; discretionary spending retrenches; staples and healthcare become defensive rotations.

## Universe
- XLY

## Data Sources
- Google Trends weekly search volume for keywords 'grocery prices' or 'food inflation' via google_trends adapter

## Signal Logic
If 'grocery prices' search > 1.8× prior 4-week MA, short XLY, close above open

## Entry / Exit
Entry: If 'grocery prices' search > 1.8× prior 4-week MA, short XLY, close above open Exit: After 8 trading days or when search volume falls back to <1.4× MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for keywords 'grocery prices' or 'food inflation' via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Food inflation concerns spike 2–4 times per year; rotations persist 5–10 days before mean reversion.

## Required Keys
- None
