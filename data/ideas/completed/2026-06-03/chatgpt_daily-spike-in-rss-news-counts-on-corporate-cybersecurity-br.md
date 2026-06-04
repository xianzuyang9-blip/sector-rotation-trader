# Daily Spike In Rss News Counts On Corporate Cybersecurity Breaches Signals Tech Sector Volatility

**Idea ID:** `daily-spike-in-rss-news-counts-on-corporate-cybersecurity-br`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased cybersecurity breach news coverage often triggers short-term price swings and risk aversion. Tech sector sensitivity to cyber risk leads to volatile price reactions on breach news spikes.

## Universe
- XLK

## Data Sources
- RSS news feed counts

## Signal Logic
If daily RSS counts on 'corporate cybersecurity breach' exceed 30% increase day-over-day

## Entry / Exit
Entry: If daily RSS counts on 'corporate cybersecurity breach' exceed 30% increase day-over-day Exit: Exit after 5 trading days or when counts revert below 10% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Cybersecurity incidents and related news spikes are frequent and often clustered in time.

## Required Keys
- None
