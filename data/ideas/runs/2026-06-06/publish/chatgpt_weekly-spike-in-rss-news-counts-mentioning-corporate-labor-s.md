# Weekly Spike In Rss News Counts Mentioning Corporate Labor Strike Signals Broad Labor Unrest

**Idea ID:** `weekly-spike-in-rss-news-counts-mentioning-corporate-labor-s`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising news coverage of corporate labor strikes signals broad labor market tensions and wage pressure. Consumer discretionary sector is vulnerable to labor cost inflation and supply chain issues.

## Universe
- XLY

## Data Sources
- RSS news feed counts

## Signal Logic
Enter short XLY if weekly RSS news count mentioning 'corporate labor strike' rises by 40% WoW

## Entry / Exit
Entry: Enter short XLY if weekly RSS news count mentioning 'corporate labor strike' rises by 40% WoW Exit: Exit after 5 weeks or if news count returns to baseline

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
- Why It Should Fire Soon: Labor strikes frequently generate weekly news spikes.

## Required Keys
- None
