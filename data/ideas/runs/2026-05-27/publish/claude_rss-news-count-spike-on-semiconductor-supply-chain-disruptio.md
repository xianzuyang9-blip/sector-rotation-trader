# Rss News Count Spike On Semiconductor Supply Chain Disruptions Signals Xlk Volatility

**Idea ID:** `rss-news-count-spike-on-semiconductor-supply-chain-disruptio`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When daily RSS news count on semiconductor supply chain issues rises >150% from 20-day baseline, market is pricing in equipment delays and fab utilization risk; tech sector reprices within 1–3 days. Supply chain disruption headlines force semiconductor equipment makers and fabless designers to revise guidance; sentiment turns bearish immediately.

## Universe
- XLK

## Data Sources
- RSS feed aggregation (Feedly/RSS Monkey) counting daily mentions of 'semiconductor supply chain disruption' or 'chip fab outage'

## Signal Logic
Daily RSS count >150% of 20-day rolling average AND closes above prior day count

## Entry / Exit
Entry: Daily RSS count >150% of 20-day rolling average AND closes above prior day count Exit: After 8 trading days OR RSS count falls back below 120% of rolling average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed aggregation (Feedly/RSS Monkey) counting daily mentions of 'semiconductor supply chain disruption' or 'chip fab outage' via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Fab maintenance windows, geopolitical tensions, and trade policy changes trigger supply chain news spikes 2–3 times per month; sentiment shifts are immediate and measurable.

## Required Keys
- None
