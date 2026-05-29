# Cloud Outage Spike News Drives Cybersecurity Sentiment Surge

**Idea ID:** `cloud-outage-spike-news-drives-cybersecurity-sentiment-surge`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Major cloud infrastructure outages generate 50%+ spike in relevant news mentions, triggering investor focus on cybersecurity and infrastructure resilience investments. Cloud failures drive enterprise IT budgets toward redundancy, security, and managed service providers.

## Universe
- XLK

## Data Sources
- RSS news feed count aggregation for 'cloud outage' and 'AWS outage' from major tech news sources (daily scrape)

## Signal Logic
When daily RSS mention count for 'cloud outage' spikes 50%+ above 20-day moving average

## Entry / Exit
Entry: When daily RSS mention count for 'cloud outage' spikes 50%+ above 20-day moving average Exit: After 5 trading days or when mention count falls 30% below spike peak

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed count aggregation for 'cloud outage' and 'AWS outage' from major tech news sources (daily scrape) via scrape (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Cloud outages occur irregularly but frequently; 1–2 major incidents with 50%+ news spikes occur per quarter.

## Required Keys
- None
