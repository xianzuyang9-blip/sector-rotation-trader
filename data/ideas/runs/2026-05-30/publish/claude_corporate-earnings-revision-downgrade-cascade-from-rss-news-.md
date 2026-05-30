# Corporate Earnings Revision Downgrade Cascade From Rss News Volume Surge

**Idea ID:** `corporate-earnings-revision-downgrade-cascade-from-rss-news-`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When daily RSS count for 'earnings miss' + 'guidance cut' spikes >50% above 20-day average, market reprices growth expectations downward; XLK and XLI see early selling pressure within 2-4 days. Earnings revisions sentiment is a leading indicator; downgrades signal deteriorating corporate fundamentals.

## Universe
- XLK

## Data Sources
- RSS feed aggregator tracking earnings-miss and guidance-cut keywords from major financial news sources (Bloomberg, Reuters, CNBC) via rss_count adapter, daily frequency

## Signal Logic
If RSS count for earnings-miss/guidance-cut keywords rises >50% above 20-day MA on 2 consecutive days, short XLK

## Entry / Exit
Entry: If RSS count for earnings-miss/guidance-cut keywords rises >50% above 20-day MA on 2 consecutive days, short XLK Exit: Exit after 7 trading days or when RSS count falls below 120% of 20-day MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed aggregator tracking earnings-miss and guidance-cut keywords from major financial news sources (Bloomberg, Reuters, CNBC) via rss_count adapter, daily frequency via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Earnings seasons and ad-hoc guidance cuts generate recurring RSS surges; events fire multiple times per quarter.

## Required Keys
- None
