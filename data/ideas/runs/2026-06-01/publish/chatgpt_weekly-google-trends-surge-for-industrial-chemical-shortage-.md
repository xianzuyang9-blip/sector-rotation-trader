# Weekly Google Trends Surge For Industrial Chemical Shortage Signals Basic Materials Supply Risk

**Idea ID:** `weekly-google-trends-surge-for-industrial-chemical-shortage-`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising interest in chemical shortages signals supply chain disruptions impacting basic materials production. Chemical supply constraints raise costs and reduce output in materials sector.

## Universe
- XLB

## Data Sources
- Google Trends weekly search interest for 'industrial chemical shortage'

## Signal Logic
Enter short XLB if weekly search interest exceeds 30% above 8-week average

## Entry / Exit
Entry: Enter short XLB if weekly search interest exceeds 30% above 8-week average Exit: Exit after 4 weeks or if interest drops below 15% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'industrial chemical shortage' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Chemical shortage concerns often surface cyclically due to production and shipping constraints.

## Required Keys
- None
