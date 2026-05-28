# Grocery Price Inflation Google Trends Spike Triggers Consumer Staples Rotation

**Idea ID:** `grocery-price-inflation-google-trends-spike-triggers-consume`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in consumer searches about rising grocery costs correlate with inflation anxiety and willingness to shift spending toward budget staples brands and away from discretionary categories. Consumer staples (especially discount retailers and budget food brands) outperform when inflation concerns spike and consumers trade down from discretionary spending.

## Universe
- XLP

## Data Sources
- Google Trends weekly search interest for 'grocery prices rising' and 'food cost increase'

## Signal Logic
When weekly Google Trends for 'grocery prices rising' exceeds 60-point threshold and rises 25+ points week-over-week

## Entry / Exit
Entry: When weekly Google Trends for 'grocery prices rising' exceeds 60-point threshold and rises 25+ points week-over-week Exit: After 3 weeks or when search interest falls below 40-point threshold for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'grocery prices rising' and 'food cost increase' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Grocery price concerns spike multiple times per year during supply chain disruptions and inflation cycles; search behavior is highly correlated with CPI announcements and seasonal demand surges.

## Required Keys
- None
