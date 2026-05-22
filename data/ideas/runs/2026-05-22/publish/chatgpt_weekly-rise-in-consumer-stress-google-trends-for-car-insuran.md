# Weekly Rise In Consumer Stress Google Trends For Car Insurance Claims Signals Auto Sector Pressure

**Idea ID:** `weekly-rise-in-consumer-stress-google-trends-for-car-insuran`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An increase of 15%+ in weekly search interest for car insurance claims indicates rising consumer auto incidents and stress. Higher claims may pressure auto insurers and reduce consumer discretionary auto spending.

## Universe
- XLY

## Data Sources
- Google Trends weekly data via google_trends adapter

## Signal Logic
Enter short XLY if weekly search interest for 'car insurance claims' rises above 115% of prior week

## Entry / Exit
Entry: Enter short XLY if weekly search interest for 'car insurance claims' rises above 115% of prior week Exit: Exit after 4 weeks or when interest falls below 105%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Insurance claims and related search interest tend to fluctuate with seasonal accident rates and weather.

## Required Keys
- None
