# Weekly Spike In Rss News Counts Mentioning Corporate Bond Downgrade Signals Financial Stress

**Idea ID:** `weekly-spike-in-rss-news-counts-mentioning-corporate-bond-do`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing news coverage on corporate bond downgrades signals rising credit stress and risk aversion. Financial sector valuation and credit risk worsen as downgrade news intensifies.

## Universe
- XLF

## Data Sources
- RSS news feed counts

## Signal Logic
If weekly RSS news counts on 'corporate bond downgrade' rise 50%+ week-over-week

## Entry / Exit
Entry: If weekly RSS news counts on 'corporate bond downgrade' rise 50%+ week-over-week Exit: Exit after 4 weeks or when counts drop below 20% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Credit rating agencies periodically announce downgrades, driving clustered news spikes.

## Required Keys
- None
