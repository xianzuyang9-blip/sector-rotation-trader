# Weekly Google Trends Surge For Home Moving Services Searches

**Idea ID:** `weekly-google-trends-surge-for-home-moving-services-searches`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising interest in moving services often indicates increased household mobility and real estate activity. Higher household moves boost real estate demand and related services, supporting XLRE ETFs.

## Universe
- XLRE

## Data Sources
- Google Trends weekly search interest for 'home moving services'

## Signal Logic
Enter long XLRE when weekly search interest rises more than 15% week-over-week

## Entry / Exit
Entry: Enter long XLRE when weekly search interest rises more than 15% week-over-week Exit: Exit after 4 weeks or when weekly growth falls below 5%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'home moving services' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Household moving interest fluctuates seasonally and due to economic conditions, with multiple surges yearly.

## Required Keys
- None
