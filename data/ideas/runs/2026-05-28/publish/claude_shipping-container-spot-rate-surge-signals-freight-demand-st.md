# Shipping Container Spot Rate Surge Signals Freight Demand Strength

**Idea ID:** `shipping-container-spot-rate-surge-signals-freight-demand-st`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly spikes in container shipping spot rates (Shanghai to Rotterdam) of 10%+ signal sudden surge in global trade demand and manufacturing activity, bullish for industrials and materials. Rising shipping rates signal strong export demand and manufacturing strength; industrials and capital equipment suppliers benefit from increased logistics costs passed through supply chains.

## Universe
- XLI

## Data Sources
- Drewry World Container Index weekly rates via html_table scrape from public shipping indices

## Signal Logic
When weekly spot rate rises 10%+ from 4-week MA and is above 52-week median

## Entry / Exit
Entry: When weekly spot rate rises 10%+ from 4-week MA and is above 52-week median Exit: After 3 weeks or when rate falls below entry price by 5%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Drewry World Container Index weekly rates via html_table scrape from public shipping indices via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Container rates fluctuate 5–15% weekly due to seasonal demand, port congestion, and trade cycles; volatility spikes occur monthly, especially around holiday shipping seasons.

## Required Keys
- None
