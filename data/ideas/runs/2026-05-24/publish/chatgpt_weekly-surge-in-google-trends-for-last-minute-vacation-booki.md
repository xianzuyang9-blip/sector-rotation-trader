# Weekly Surge In Google Trends For Last Minute Vacation Bookings Signals Travel Demand Spike

**Idea ID:** `weekly-surge-in-google-trends-for-last-minute-vacation-booki`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A spike in last minute vacation booking searches usually precedes increased travel activity and discretionary spending on travel-related services. Travel sector ETFs benefit from last-minute booking surges which often translate to higher revenues for airlines, hotels, and leisure companies.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly Google Trends interest for 'last minute vacation' increases by 20% week-over-week

## Entry / Exit
Entry: If weekly Google Trends interest for 'last minute vacation' increases by 20% week-over-week Exit: After 4 weeks or if interest drops below previous baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seasonal shifts and travel promotions regularly cause weekly last-minute booking interest spikes.

## Required Keys
- None
