# Grocery Price Inflation Google Trends Spike Signals Consumer Staples Demand

**Idea ID:** `grocery-price-inflation-google-trends-spike-signals-consumer`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When consumers search for grocery price information more intensely, it signals heightened awareness of food cost pressure and willingness to trade down or shift purchasing patterns. Staples companies benefit from flight-to-safety during inflation anxiety; discount retailers outperform premium brands.

## Universe
- XLP

## Data Sources
- Google Trends weekly search interest for 'grocery prices' and 'food inflation'

## Signal Logic
When Google Trends search volume for 'grocery prices' exceeds 70th percentile of 52-week rolling history, enter long XLP

## Entry / Exit
Entry: When Google Trends search volume for 'grocery prices' exceeds 70th percentile of 52-week rolling history, enter long XLP Exit: Exit after 8 trading days or when search volume falls below 50th percentile

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'grocery prices' and 'food inflation' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Grocery price discussions spike weekly during inflationary periods and seasonal food cost transitions; Google Trends data is real-time and fires multiple times per month.

## Required Keys
- None
