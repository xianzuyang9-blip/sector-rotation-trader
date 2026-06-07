# Weekly Surge In Rss News Counts On Container Ship Delays Signals Freight Logistics Headwinds

**Idea ID:** `weekly-surge-in-rss-news-counts-on-container-ship-delays-sig`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased media coverage of container delays reflects supply chain disruptions and logistics stress. Shipping delays pressure industrial supply chains and logistics sector profitability.

## Universe
- XLI

## Data Sources
- RSS news feed counts filtered for 'container ship delay'

## Signal Logic
If weekly RSS count for container ship delays rises above 30% of 4-week average

## Entry / Exit
Entry: If weekly RSS count for container ship delays rises above 30% of 4-week average Exit: When weekly count drops below 10% above 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts filtered for 'container ship delay' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Shipping bottlenecks and news coverage spike frequently with port congestion cycles.

## Required Keys
- None
