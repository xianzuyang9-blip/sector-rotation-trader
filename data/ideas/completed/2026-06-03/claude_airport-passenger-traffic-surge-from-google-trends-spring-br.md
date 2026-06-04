# Airport Passenger Traffic Surge From Google Trends Spring Break Bookings

**Idea ID:** `airport-passenger-traffic-surge-from-google-trends-spring-br`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
In February-March, spikes in spring break travel searches lead actual bookings by 1-2 weeks, signaling near-term surge in travel/hospitality demand. Spring break booking surges drive revenue for airlines, hotels, and restaurants; positive sentiment on discretionary spending.

## Universe
- XLY

## Data Sources
- Google Trends weekly search volume for 'cheap flights spring break' and 'hotels spring break' through google_trends adapter

## Signal Logic
If weekly Google Trends 'spring break' related travel searches rise >60% year-over-year in Feb-Mar AND search volume crosses above prior year peak

## Entry / Exit
Entry: If weekly Google Trends 'spring break' related travel searches rise >60% year-over-year in Feb-Mar AND search volume crosses above prior year peak Exit: After 3 weeks or once searches drop below 50-day moving average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'cheap flights spring break' and 'hotels spring break' through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Spring break is seasonal and predictable; surges occur annually in Feb-Mar, making this signal reliable within the 30-day window.

## Required Keys
- None
