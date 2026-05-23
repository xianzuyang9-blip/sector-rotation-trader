# Tech News Surge Contrarian Fade After Earnings

**Idea ID:** `tech-news-surge-contrarian-fade-after-earnings`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When RSS mention counts for negative tech earnings language spike >200% above baseline after earnings season, sentiment is oversold. Contrarian fade into XLK often triggers a 3–5 day bounce within 2 weeks. Extreme negative sentiment often marks temporary capitulation in growth-heavy tech sectors.

## Universe
- XLK

## Data Sources
- RSS feed count aggregator (Feedburner or native RSS feed) tracking top 10 tech news sources daily mention volume for 'software earnings miss' or 'cloud growth slowdown'

## Signal Logic
If daily RSS mention count for 'software earnings miss' or 'cloud slowdown' exceeds prior 30-day average by 150% and XLK is down >2% intraday

## Entry / Exit
Entry: If daily RSS mention count for 'software earnings miss' or 'cloud slowdown' exceeds prior 30-day average by 150% and XLK is down >2% intraday Exit: After 5 trading days or once mention count reverts to 50% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed count aggregator (Feedburner or native RSS feed) tracking top 10 tech news sources daily mention volume for 'software earnings miss' or 'cloud growth slowdown' via scrape (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Tech earnings season and related sentiment spikes occur quarterly and trigger intra-quarter momentum swings.

## Required Keys
- None
