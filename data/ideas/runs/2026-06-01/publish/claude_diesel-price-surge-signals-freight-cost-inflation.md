# Diesel Price Surge Signals Freight Cost Inflation

**Idea ID:** `diesel-price-surge-signals-freight-cost-inflation`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Diesel prices move sharply on crude swings, supply disruptions, and refinery outages. A 5%+ weekly jump signals margin compression across logistics and manufacturing. Industrials and transportation companies face immediate margin pressure when fuel costs spike.

## Universe
- XLI

## Data Sources
- FRED series GASDESW (Weekly U.S. Diesel Prices) via fred_series adapter

## Signal Logic
If GASDESW rises 5% or more week-over-week and closes above its 8-week high

## Entry / Exit
Entry: If GASDESW rises 5% or more week-over-week and closes above its 8-week high Exit: After 4 weeks or once GASDESW closes below its 8-week MA for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series GASDESW (Weekly U.S. Diesel Prices) via fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 60
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Crude volatility ensures diesel prices spike 5%+ multiple times per quarter; refinery maintenance also triggers moves.

## Required Keys
- None
