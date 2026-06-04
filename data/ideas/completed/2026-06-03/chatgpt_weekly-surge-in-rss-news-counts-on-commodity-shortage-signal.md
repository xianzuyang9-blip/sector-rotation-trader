# Weekly Surge In Rss News Counts On Commodity Shortage Signals Industrial Sector Headwinds

**Idea ID:** `weekly-surge-in-rss-news-counts-on-commodity-shortage-signal`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising news coverage on commodity shortages signals supply chain disruptions and cost pressures for industrial firms. Commodity scarcity increases input costs and delays production, pressuring industrial sector earnings.

## Universe
- XLI

## Data Sources
- RSS news feed counts

## Signal Logic
If weekly RSS counts on 'commodity shortage' rise 40%+ week-over-week

## Entry / Exit
Entry: If weekly RSS counts on 'commodity shortage' rise 40%+ week-over-week Exit: Exit after 3 weeks or when counts drop below 15% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Commodity shortages often flare during seasonal supply chain stresses and geopolitical events.

## Required Keys
- None
