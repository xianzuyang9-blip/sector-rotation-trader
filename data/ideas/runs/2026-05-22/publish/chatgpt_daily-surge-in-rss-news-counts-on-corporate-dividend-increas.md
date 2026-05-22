# Daily Surge In Rss News Counts On Corporate Dividend Increases Signals Financial Sector Strength

**Idea ID:** `daily-surge-in-rss-news-counts-on-corporate-dividend-increas`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A 30%+ daily increase in news stories on dividend raises signals financial sector confidence and capital return. Dividend increases reflect strong earnings and cash flow in financial stocks.

## Universe
- XLF

## Data Sources
- RSS news feed counts via rss_count adapter

## Signal Logic
Enter long XLF if daily RSS dividend increase stories > 130% of 30-day average

## Entry / Exit
Entry: Enter long XLF if daily RSS dividend increase stories > 130% of 30-day average Exit: Exit after 5 trading days or if counts drop below 115%

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
- Why It Should Fire Soon: Dividend news flow is frequent and spikes with quarterly earnings cycles.

## Required Keys
- None
