# Freight Rail Car Utilization Collapse Signals Recession Freight Risk

**Idea ID:** `freight-rail-car-utilization-collapse-signals-recession-frei`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Rail car utilization drops >15% week-over-week during demand shocks, preceding broader industrial contraction by 2-3 weeks and signaling logistics stress. Rail freight is a leading indicator of industrial production and capital goods demand; sharp drops foreshadow equity weakness in industrials.

## Universe
- XLI

## Data Sources
- Association of American Railroads weekly freight car loadings through html_table adapter (public weekly AAR reports)

## Signal Logic
If weekly AAR rail car loadings fall >12% sequentially AND the 4-week moving average is below the 52-week median

## Entry / Exit
Entry: If weekly AAR rail car loadings fall >12% sequentially AND the 4-week moving average is below the 52-week median Exit: After 3 weeks or when loadings stabilize above prior week level for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Association of American Railroads weekly freight car loadings through html_table adapter (public weekly AAR reports) via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Economic cycles and inventory corrections occur multiple times per year; rail data is released weekly and is volatile enough to cross thresholds regularly.

## Required Keys
- None
