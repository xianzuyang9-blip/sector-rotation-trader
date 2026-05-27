# Freight Rate Compression Signal From Weekly Load Matching Data

**Idea ID:** `freight-rate-compression-signal-from-weekly-load-matching-da`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When spot trucking rates fall >5% weekly and load-to-truck ratio dips below 0.85, freight pricing weakness signals logistics cost relief for manufacturers and retailers. Industrial and manufacturing sectors see margin expansion from lower freight input costs; transportation suppliers face headwinds but overall manufacturing profit improves.

## Universe
- XLI

## Data Sources
- Cass Freight Index Weekly Spot Trucking Rate Index (public HTML tables from cass.com or via FRED TRUCKD series proxy)

## Signal Logic
Cass Trucking Rate Index drops >5% week-over-week AND 4-week moving average of rate falls below prior 12-week mean

## Entry / Exit
Entry: Cass Trucking Rate Index drops >5% week-over-week AND 4-week moving average of rate falls below prior 12-week mean Exit: After 15 trading days OR rates rise back above 12-week mean

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Cass Freight Index Weekly Spot Trucking Rate Index (public HTML tables from cass.com or via FRED TRUCKD series proxy) via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Spot trucking rates fluctuate >5% almost every 2–3 weeks; mean reversion trades fire frequently in logistics data.

## Required Keys
- None
