# Food Price Inflation Rss Spike Signals Consumer Staples Pricing Power

**Idea ID:** `food-price-inflation-rss-spike-signals-consumer-staples-pric`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Daily spikes in food inflation/grocery price news signal successful producer cost pass-through and staples margin expansion. Consumer staples stocks rally on pricing power. Food price inflation articles correlate with staples companies raising prices successfully; margins expand and valuations re-rate higher.

## Universe
- XLP

## Data Sources
- RSS news feed count for 'grocery price increase' and 'food inflation' via rss_count adapter

## Signal Logic
If daily RSS count for food/grocery price increase spikes >50% from 5-day average, long XLP on next open

## Entry / Exit
Entry: If daily RSS count for food/grocery price increase spikes >50% from 5-day average, long XLP on next open Exit: Exit after 10 trading days or if RSS count falls below 1.2x baseline for two days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed count for 'grocery price increase' and 'food inflation' via rss_count adapter via scrape (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Food inflation news cycles occur constantly; 50% RSS spikes on staples pricing hit multiple times per month reliably.

## Required Keys
- None
