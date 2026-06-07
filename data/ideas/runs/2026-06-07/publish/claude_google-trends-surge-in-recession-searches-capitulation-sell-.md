# Google Trends Surge In Recession Searches Capitulation Sell Signal

**Idea ID:** `google-trends-surge-in-recession-searches-capitulation-sell-`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly search volume for 'recession' spikes >100% (fear capitulation), which historically marks sentiment bottoms before 1–3 week rally. Peak fear/recession angst often coincides with market bottoms; discretionary recovers fastest on sentiment relief.

## Universe
- XLY

## Data Sources
- Google Trends weekly search volume for keyword 'recession' via google_trends adapter

## Signal Logic
If 'recession' search volume > 2× prior 4-week average, close above open

## Entry / Exit
Entry: If 'recession' search volume > 2× prior 4-week average, close above open Exit: After 10 trading days or when 'recession' volume falls back to <1.5× 4-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for keyword 'recession' via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Recession search spikes occur 3–5 times per year during volatility; most reverse within 5–14 days.

## Required Keys
- None
