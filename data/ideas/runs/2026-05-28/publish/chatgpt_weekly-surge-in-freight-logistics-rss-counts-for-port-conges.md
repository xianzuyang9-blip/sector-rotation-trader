# Weekly Surge In Freight Logistics Rss Counts For Port Congestion Mentions Signals Supply Chain Stress

**Idea ID:** `weekly-surge-in-freight-logistics-rss-counts-for-port-conges`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising news mentions of port congestion point to supply chain bottlenecks impacting industrial and consumer goods flow. Port congestion delays shipments, increasing costs and slowing industrial production cycles.

## Universe
- XLI

## Data Sources
- RSS news feed counts for 'port congestion' keyword

## Signal Logic
If weekly RSS count for 'port congestion' rises more than 30% WoW

## Entry / Exit
Entry: If weekly RSS count for 'port congestion' rises more than 30% WoW Exit: When counts revert to baseline levels for two consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts for 'port congestion' keyword via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Supply chain news surges regularly due to weather, labor, or regulatory delays affecting ports.

## Required Keys
- None
