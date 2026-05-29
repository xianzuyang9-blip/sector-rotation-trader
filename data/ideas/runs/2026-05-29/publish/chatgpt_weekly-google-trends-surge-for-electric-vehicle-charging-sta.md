# Weekly Google Trends Surge For Electric Vehicle Charging Station Near Me

**Idea ID:** `weekly-google-trends-surge-for-electric-vehicle-charging-sta`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing interest in EV charging stations signals accelerating adoption of electric vehicles and supportive infrastructure. Communications and tech sectors benefit from infrastructure growth related to EV connectivity.

## Universe
- XLC

## Data Sources
- Google Trends weekly search interest for 'electric vehicle charging station near me'

## Signal Logic
Enter long XLC when weekly search interest rises more than 20% versus prior week

## Entry / Exit
Entry: Enter long XLC when weekly search interest rises more than 20% versus prior week Exit: Exit after 4 weeks or when growth drops below 5%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'electric vehicle charging station near me' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: EV infrastructure interest surges seasonally and with policy news multiple times per year.

## Required Keys
- None
