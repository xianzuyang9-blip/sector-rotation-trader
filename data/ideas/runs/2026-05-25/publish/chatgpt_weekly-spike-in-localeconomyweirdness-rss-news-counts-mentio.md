# Weekly Spike In Localeconomyweirdness Rss News Counts Mentioning Small Town Retail Closures Signals Consumer Discretionary Softness

**Idea ID:** `weekly-spike-in-localeconomyweirdness-rss-news-counts-mentio`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An increase in reports about small town retail closures signals localized consumer spending weakness. Retail closures reflect weakening demand in consumer discretionary markets.

## Universe
- XLY

## Data Sources
- RSS feed counts weekly

## Signal Logic
If weekly RSS count for 'small town retail closures' rises 30% WoW

## Entry / Exit
Entry: If weekly RSS count for 'small town retail closures' rises 30% WoW Exit: After 4 weeks or if count falls below 10% WoW change

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed counts weekly via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Retail closure news frequency varies with economic cycles and seasonal retail trends.

## Required Keys
- None
