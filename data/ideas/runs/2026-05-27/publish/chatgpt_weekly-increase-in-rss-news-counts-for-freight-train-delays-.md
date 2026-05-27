# Weekly Increase In Rss News Counts For Freight Train Delays Signals Logistic Sector Pressure

**Idea ID:** `weekly-increase-in-rss-news-counts-for-freight-train-delays-`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
More news coverage on freight train delays signals worsening logistics bottlenecks affecting industrial production. Logistics delays increase costs and disrupt supply chains, pressuring industrial stocks.

## Universe
- XLI

## Data Sources
- RSS news feed counts for freight train delays using rss_count adapter

## Signal Logic
If weekly RSS counts for 'freight train delays' increase by 40% vs prior 6-week average

## Entry / Exit
Entry: If weekly RSS counts for 'freight train delays' increase by 40% vs prior 6-week average Exit: After 3 weeks or when counts return below average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts for freight train delays using rss_count adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Logistics news coverage is frequent and sensitive to operational conditions.

## Required Keys
- None
