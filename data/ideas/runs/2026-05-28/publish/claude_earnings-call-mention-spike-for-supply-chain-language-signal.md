# Earnings Call Mention Spike For Supply Chain Language Signals Industrial Headwind Bearish Rotation

**Idea ID:** `earnings-call-mention-spike-for-supply-chain-language-signal`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Daily RSS article count spikes on supply chain disruption mention in earnings coverage signal executives warning of margin pressure and delivery delays, triggering bearish industrial rotation. Supply chain warnings in earnings erode profit expectations for manufacturers and logistics firms; industrial sector underperforms as guidance revisions turn negative.

## Universe
- XLI

## Data Sources
- RSS feed count for earnings-related articles mentioning 'supply chain disruption' or 'logistics bottleneck' via rss_count adapter

## Signal Logic
When daily RSS count for 'supply chain disruption earnings' exceeds 50-article threshold and is 30% above 20-day average

## Entry / Exit
Entry: When daily RSS count for 'supply chain disruption earnings' exceeds 50-article threshold and is 30% above 20-day average Exit: After 5 trading days or when RSS count drops below 30 articles for 2 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed count for earnings-related articles mentioning 'supply chain disruption' or 'logistics bottleneck' via rss_count adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Earnings seasons (Q1, Q2, Q3, Q4) each trigger 2–4 supply chain warning spikes; off-season surprises add 1–2 monthly occurrences, averaging 3–4 total per month.

## Required Keys
- None
