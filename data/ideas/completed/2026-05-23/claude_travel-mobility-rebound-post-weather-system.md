# Travel Mobility Rebound Post Weather System

**Idea ID:** `travel-mobility-rebound-post-weather-system`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
After severe weather (rain >1 inch or wind >35 mph) clears for 3+ consecutive days, consumer travel and hospitality demand rebounds as pent-up reservations release. XLY outperforms SPY by 1–2%. Travel and hospitality companies see immediate booking surges when weather uncertainty ends.

## Universe
- XLY

## Data Sources
- Open-Meteo daily weather data (precipitation, wind gust max) for major US metro centroids aggregated to national monthly index

## Signal Logic
If severe weather clears (no >0.5in rain or >30mph wind for 3 consecutive days) after 5+ prior days of disruption, buy

## Entry / Exit
Entry: If severe weather clears (no >0.5in rain or >30mph wind for 3 consecutive days) after 5+ prior days of disruption, buy Exit: After 7 trading days or if weather deteriorates again

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily weather data (precipitation, wind gust max) for major US metro centroids aggregated to national monthly index via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Severe weather systems occur regularly and clear within 5–10 day cycles multiple times per season.

## Required Keys
- None
