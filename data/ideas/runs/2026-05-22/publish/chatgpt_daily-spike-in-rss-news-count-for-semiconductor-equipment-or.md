# Daily Spike In Rss News Count For Semiconductor Equipment Orders Signals Chip Sector Rebound

**Idea ID:** `daily-spike-in-rss-news-count-for-semiconductor-equipment-or`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A 40%+ daily jump in news stories about semiconductor equipment orders implies renewed capital expenditure. Higher equipment orders suggest improving chip demand and sector earnings prospects.

## Universe
- XLK

## Data Sources
- RSS news feed counts via rss_count adapter

## Signal Logic
Enter long XLK if daily RSS count for semiconductor equipment orders > 140% of 30-day average

## Entry / Exit
Entry: Enter long XLK if daily RSS count for semiconductor equipment orders > 140% of 30-day average Exit: Exit after 5 trading days or if counts drop below 120%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts via rss_count adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: News flow on chip orders spikes frequently around earnings and supply chain updates.

## Required Keys
- None
