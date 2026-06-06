# Weekly Rise In Rss News Counts Mentioning Warehouse Labor Strike Signals Industrial Disruption

**Idea ID:** `weekly-rise-in-rss-news-counts-mentioning-warehouse-labor-st`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased news coverage of warehouse labor strikes indicates imminent supply chain delays and cost pressures. Industrial sector earnings vulnerable to labor unrest and supply chain interruptions.

## Universe
- XLI

## Data Sources
- RSS news feed counts

## Signal Logic
Enter short XLI if weekly RSS news count for 'warehouse labor strike' rises by 50% WoW

## Entry / Exit
Entry: Enter short XLI if weekly RSS news count for 'warehouse labor strike' rises by 50% WoW Exit: Exit after 4 weeks or if news count drops below baseline

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
- Why It Should Fire Soon: Labor disputes often flare quickly and get weekly media spikes.

## Required Keys
- None
