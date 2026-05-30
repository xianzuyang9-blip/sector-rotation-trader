# Google Trends Surge In Recession Fear Drives Defensive Rotation

**Idea ID:** `google-trends-surge-in-recession-fear-drives-defensive-rotat`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly Google Trends for recession-related searches spike >30% above rolling 8-week average, consumer sentiment deteriorates and equity allocators rotate from XLY to XLP/XLV within 3-7 days. Rising recession anxiety triggers flight-to-safety; consumer discretionary underperforms as allocation shifts to staples and healthcare.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for terms: 'recession outlook', 'economic slowdown', 'job cuts news' via google_trends adapter

## Signal Logic
If Google Trends composite score for recession-fear keywords jumps >30% above 8-week rolling average, short XLY and long XLP equally

## Entry / Exit
Entry: If Google Trends composite score for recession-fear keywords jumps >30% above 8-week rolling average, short XLY and long XLP equally Exit: Exit after 10 trading days or when Trends score reverts below 120% of rolling average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for terms: 'recession outlook', 'economic slowdown', 'job cuts news' via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Recession anxiety spikes episodically; market uncertainty triggers multiple Trends surges per quarter.

## Required Keys
- None
