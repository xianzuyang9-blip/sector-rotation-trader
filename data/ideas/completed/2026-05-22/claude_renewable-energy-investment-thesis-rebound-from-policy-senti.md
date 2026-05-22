# Renewable Energy Investment Thesis Rebound From Policy Sentiment Surge

**Idea ID:** `renewable-energy-investment-thesis-rebound-from-policy-senti`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When combined Google Trends volume for renewable energy policy/jobs terms spikes >40% above 52-week baseline, institutional investors anticipate policy tailwinds, triggering brief bullish rotation into clean energy and utilities. Utilities and renewable energy companies benefit from policy momentum signaled by rising public interest in clean energy topics.

## Universe
- XLU

## Data Sources
- Google Trends weekly search volume for terms 'renewable energy jobs' + 'solar tax credit' + 'wind energy news', via google_trends adapter

## Signal Logic
If Google Trends combined volume for renewable terms exceeds 52-week MA by >40%, buy XLU

## Entry / Exit
Entry: If Google Trends combined volume for renewable terms exceeds 52-week MA by >40%, buy XLU Exit: After 9 trading days OR if Google Trends volume falls below 52-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for terms 'renewable energy jobs' + 'solar tax credit' + 'wind energy news', via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Google Trends for renewable energy topics spike 5–7 times per year around policy announcements, earnings, and seasonal events.

## Required Keys
- None
