# Airline Fuel Surcharge News Spike Signals Travel Sector Headwind

**Idea ID:** `airline-fuel-surcharge-news-spike-signals-travel-sector-head`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When airlines announce fuel surcharges or price hikes, it signals rising operational costs and margin compression; news spike precedes booking decline. Airlines and travel discretionary companies face reduced demand and lower margins when fuel costs are flagged publicly.

## Universe
- XLY

## Data Sources
- RSS news feed count for airline fuel surcharge announcements and price hikes

## Signal Logic
When daily RSS count for 'airline fuel surcharge' or 'airline price hike' exceeds 5 articles and is above 90th percentile of 60-day rolling history, enter short XLY

## Entry / Exit
Entry: When daily RSS count for 'airline fuel surcharge' or 'airline price hike' exceeds 5 articles and is above 90th percentile of 60-day rolling history, enter short XLY Exit: Exit after 6 trading days or when daily RSS count falls below 3 articles for 2 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed count for airline fuel surcharge announcements and price hikes via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Airlines regularly announce fuel adjustments and pricing changes; news spike frequency is 1–2 times per week during volatile oil periods.

## Required Keys
- None
