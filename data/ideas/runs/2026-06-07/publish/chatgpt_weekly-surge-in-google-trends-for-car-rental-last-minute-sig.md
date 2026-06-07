# Weekly Surge In Google Trends For Car Rental Last Minute Signals Travel Demand Spike

**Idea ID:** `weekly-surge-in-google-trends-for-car-rental-last-minute-sig`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sudden rise in last-minute car rental searches suggests imminent travel plans and mobility demand. Increased travel mobility boosts discretionary spending and travel-related services.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly Google Trends for 'car rental last minute' rises 20% week-over-week

## Entry / Exit
Entry: If weekly Google Trends for 'car rental last minute' rises 20% week-over-week Exit: Once trend falls below 10% increase week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Travel demand fluctuates frequently with seasonal and event-driven spikes.

## Required Keys
- None
