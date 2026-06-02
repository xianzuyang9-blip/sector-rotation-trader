# Weekly Surge In Attention Sentiment Rss News Counts For Semiconductor Export Restrictions

**Idea ID:** `weekly-surge-in-attention-sentiment-rss-news-counts-for-semi`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased news volume on export restrictions signals supply chain risks and trade tensions. Semiconductor sector vulnerable to trade policy shocks.

## Universe
- XLK

## Data Sources
- RSS news feed counts for 'semiconductor export restrictions'

## Signal Logic
If weekly news count rises 40% above 6-week moving average

## Entry / Exit
Entry: If weekly news count rises 40% above 6-week moving average Exit: When news count normalizes below 20% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts for 'semiconductor export restrictions' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Trade tensions and export restrictions news emerge frequently and cause attention spikes.

## Required Keys
- None
