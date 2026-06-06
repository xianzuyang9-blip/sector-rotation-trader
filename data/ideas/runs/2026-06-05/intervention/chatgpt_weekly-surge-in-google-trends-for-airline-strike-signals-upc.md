# Weekly Surge In Google Trends For Airline Strike Signals Upcoming Travel Mobility Disruptions

**Idea ID:** `weekly-surge-in-google-trends-for-airline-strike-signals-upc`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased searches on airline strikes indicate potential travel disruptions and reduced airline earnings. Consumer discretionary travel and leisure spending falls amid airline labor disputes.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'airline strike'

## Signal Logic
Enter short XLY when weekly search interest rises 40% week-over-week

## Entry / Exit
Entry: Enter short XLY when weekly search interest rises 40% week-over-week Exit: Exit after 4 weeks or when interest declines below 10% growth

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'airline strike' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor disputes in travel sectors occur repeatedly with news cycles causing frequent search spikes.

## Required Keys
- None
