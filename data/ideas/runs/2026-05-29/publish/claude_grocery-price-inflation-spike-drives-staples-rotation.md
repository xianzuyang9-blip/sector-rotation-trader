# Grocery Price Inflation Spike Drives Staples Rotation

**Idea ID:** `grocery-price-inflation-spike-drives-staples-rotation`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Consumer searches for grocery pricing spike during periods of food inflation anxiety, preceding retail earnings misses and category rotation away from discretionary goods. Staples outperform when consumer stress on essentials forces budget reallocation away from discretionary purchases.

## Universe
- XLP

## Data Sources
- Google Trends weekly search volume for 'grocery prices near me' and 'food price inflation'

## Signal Logic
When weekly Google Trends search interest for grocery price queries exceeds 75th percentile of trailing 52-week distribution

## Entry / Exit
Entry: When weekly Google Trends search interest for grocery price queries exceeds 75th percentile of trailing 52-week distribution Exit: After 3 weeks or when search interest drops below 50th percentile

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'grocery prices near me' and 'food price inflation' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Food price concerns emerge weekly during inflationary cycles; search volume crosses thresholds multiple times per quarter.

## Required Keys
- None
