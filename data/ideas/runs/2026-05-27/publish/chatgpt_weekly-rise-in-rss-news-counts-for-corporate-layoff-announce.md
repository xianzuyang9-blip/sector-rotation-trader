# Weekly Rise In Rss News Counts For Corporate Layoff Announcements Signals Labor Market Weakness

**Idea ID:** `weekly-rise-in-rss-news-counts-for-corporate-layoff-announce`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Growing news volume on layoffs signals weakening labor market and potential consumer spending reduction. Labor market stress typically depresses consumer discretionary stocks.

## Universe
- XLY

## Data Sources
- RSS news feed counts for corporate layoffs via rss_count adapter

## Signal Logic
If weekly RSS counts on layoffs increase 50% above 8-week average

## Entry / Exit
Entry: If weekly RSS counts on layoffs increase 50% above 8-week average Exit: After 4 weeks or when counts normalize

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts for corporate layoffs via rss_count adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Layoff announcements occur regularly and generate news volume spikes.

## Required Keys
- None
