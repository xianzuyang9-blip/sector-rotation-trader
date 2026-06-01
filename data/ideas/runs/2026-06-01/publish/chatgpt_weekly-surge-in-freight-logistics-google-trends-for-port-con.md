# Weekly Surge In Freight Logistics Google Trends For Port Congestion Signals Supply Chain Pressure

**Idea ID:** `weekly-surge-in-freight-logistics-google-trends-for-port-con`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased search interest in port congestion reflects supply chain bottlenecks impacting industrial production. Port congestion delays shipments, raising costs and reducing industrial output.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest for 'port congestion'

## Signal Logic
Enter short XLI if weekly search interest exceeds 25% above trailing 8-week average

## Entry / Exit
Entry: Enter short XLI if weekly search interest exceeds 25% above trailing 8-week average Exit: Exit after 4 weeks or when search interest drops below 10% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'port congestion' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Port congestion news and interest often spike during seasonal shipping peaks.

## Required Keys
- None
