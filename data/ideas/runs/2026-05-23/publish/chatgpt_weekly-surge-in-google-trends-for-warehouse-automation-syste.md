# Weekly Surge In Google Trends For Warehouse Automation System Failure Signals Short-term Xli Volatility

**Idea ID:** `weekly-surge-in-google-trends-for-warehouse-automation-syste`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Failures in warehouse automation systems indicate operational risk and potential supply chain delays. Industrial sector depends increasingly on automation efficiency.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest for 'warehouse automation system failure'

## Signal Logic
Enter short XLI if weekly searches rise 30% week-over-week

## Entry / Exit
Entry: Enter short XLI if weekly searches rise 30% week-over-week Exit: Exit after 3 weeks or when growth falls below 10%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'warehouse automation system failure' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Automation system failures in warehouses spike periodically tied to technology rollouts or outages.

## Required Keys
- None
