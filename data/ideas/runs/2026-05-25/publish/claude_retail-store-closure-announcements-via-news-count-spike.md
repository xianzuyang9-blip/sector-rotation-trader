# Retail Store Closure Announcements Via News Count Spike

**Idea ID:** `retail-store-closure-announcements-via-news-count-spike`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Clusters of retail closure announcements signal sector distress and consumer spending pullback, weak forward guidance for retail landlords and suppliers. Real estate investors (REITs) and landlords suffer from vacancies; retail space values decline as closures accelerate.

## Universe
- XLRE

## Data Sources
- RSS feed counts from retail trade publications (RetailDive, Chain Store Age) for 'store closure' and 'retail consolidation'

## Signal Logic
When weekly RSS count for 'store closure' OR 'retail consolidation' exceeds 75th percentile of trailing 12-week average AND is >8 articles per week

## Entry / Exit
Entry: When weekly RSS count for 'store closure' OR 'retail consolidation' exceeds 75th percentile of trailing 12-week average AND is >8 articles per week Exit: After 14 trading days or when article count returns to median

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed counts from retail trade publications (RetailDive, Chain Store Age) for 'store closure' and 'retail consolidation' via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Retail consolidation is ongoing; closure announcements occur frequently (especially post-earnings), generating signals multiple times per quarter.

## Required Keys
- None
