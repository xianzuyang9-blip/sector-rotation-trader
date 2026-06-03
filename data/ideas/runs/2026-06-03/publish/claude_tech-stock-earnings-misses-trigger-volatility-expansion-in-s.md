# Tech Stock Earnings Misses Trigger Volatility Expansion In Semiconductor Holdings

**Idea ID:** `tech-stock-earnings-misses-trigger-volatility-expansion-in-s`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When daily RSS news counts for tech/chip earnings misses jump >200% above baseline, implied volatility in semiconductor stocks expands within 1 trading day. Earnings misses trigger rotation away from growth tech; IV expansion creates hedging demand and volatility premium.

## Universe
- XLK

## Data Sources
- RSS/news feed counts for 'semiconductor earnings miss' and 'chip stock guidance cut' through rss_count adapter

## Signal Logic
If daily RSS news count for 'earnings miss' + 'chip' OR 'semiconductor' exceeds 3-month rolling average by >150% AND closing IV rank is <70%

## Entry / Exit
Entry: If daily RSS news count for 'earnings miss' + 'chip' OR 'semiconductor' exceeds 3-month rolling average by >150% AND closing IV rank is <70% Exit: After 5 trading days or once IV rank rises above 75%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS/news feed counts for 'semiconductor earnings miss' and 'chip stock guidance cut' through rss_count adapter via scrape (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Earnings seasons occur quarterly; off-season earnings surprises happen weekly; daily RSS volatility ensures frequent trigger crossings.

## Required Keys
- None
