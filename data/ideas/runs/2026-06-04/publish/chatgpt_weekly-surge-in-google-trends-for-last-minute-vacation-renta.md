# Weekly Surge In Google Trends For Last-minute Vacation Rentals Signals Travel Bounce

**Idea ID:** `weekly-surge-in-google-trends-for-last-minute-vacation-renta`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sudden rise in last-minute vacation rental searches indicates an imminent travel demand surge. Increased travel demand benefits discretionary travel and leisure stocks.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'last minute vacation rentals'

## Signal Logic
If the 3-week moving average of search interest rises by more than 15% compared to prior 3 weeks

## Entry / Exit
Entry: If the 3-week moving average of search interest rises by more than 15% compared to prior 3 weeks Exit: After 4 weeks or when trend reverses by 10%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'last minute vacation rentals' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly Google Trends data routinely shows spikes in travel-related last-minute booking interest.

## Required Keys
- None
