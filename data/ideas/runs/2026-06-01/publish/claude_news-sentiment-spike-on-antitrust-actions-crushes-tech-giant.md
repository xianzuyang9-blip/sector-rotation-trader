# News Sentiment Spike On Antitrust Actions Crushes Tech Giants

**Idea ID:** `news-sentiment-spike-on-antitrust-actions-crushes-tech-giant`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Major antitrust action announcements (DOJ, EU, FTC) trigger 200%+ daily spikes in regulatory news mentions. These often precede legislative/judicial developments that pressure mega-cap tech valuations. Tech megacaps face breakup risk and margin pressure from antitrust scrutiny; market reprices on headline volume.

## Universe
- XLK

## Data Sources
- RSS news feed counts (major outlets: Reuters, Bloomberg, CNBC) tracking 'antitrust' + 'technology' via rss_count adapter

## Signal Logic
If daily RSS count for 'antitrust + technology' exceeds prior 30-day average by 150% AND count > 50 articles

## Entry / Exit
Entry: If daily RSS count for 'antitrust + technology' exceeds prior 30-day average by 150% AND count > 50 articles Exit: After 3 weeks or once daily count falls below 80% of peak for 5 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts (major outlets: Reuters, Bloomberg, CNBC) tracking 'antitrust' + 'technology' via rss_count adapter via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Regulatory actions fire 6-10 times per year; each generates 150%+ spike lasting 5-10 days.

## Required Keys
- None
