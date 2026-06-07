# Daily Jump In Rss News Counts On Corporate Cybersecurity Breaches Signals Tech Sector Volatility

**Idea ID:** `daily-jump-in-rss-news-counts-on-corporate-cybersecurity-bre`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden increase in cybersecurity breach news causes heightened risk perception in tech sector stocks. Cybersecurity issues undermine tech sector confidence and can trigger selloffs.

## Universe
- XLK

## Data Sources
- RSS news feed counts filtered for 'corporate cybersecurity breach'

## Signal Logic
If daily RSS count on cybersecurity breaches rises 50% above 7-day average

## Entry / Exit
Entry: If daily RSS count on cybersecurity breaches rises 50% above 7-day average Exit: After 5 trading days or once count drops below 20% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts filtered for 'corporate cybersecurity breach' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Cybersecurity incidents and news spike frequently as breaches are regularly disclosed.

## Required Keys
- None
