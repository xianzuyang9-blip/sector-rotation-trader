# Weekly Spike In Rss News Counts On Port Labor Strikes Signals Freight Logistics Disruption

**Idea ID:** `weekly-spike-in-rss-news-counts-on-port-labor-strikes-signal`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased media coverage of port labor strikes correlates with short-term shipping delays and inventory bottlenecks. Industrial and transportation sectors face rising costs and shipment delays during labor unrest.

## Universe
- XLI

## Data Sources
- RSS news feed counts

## Signal Logic
If weekly RSS news counts on 'port labor strike' increase by 50%+ versus prior week

## Entry / Exit
Entry: If weekly RSS news counts on 'port labor strike' increase by 50%+ versus prior week Exit: Exit after 4 weeks or when counts drop below 20% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor strike news coverage frequently flares during contract negotiation periods and supply chain stress.

## Required Keys
- None
