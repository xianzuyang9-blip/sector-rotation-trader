# Weekly Surge In Google Trends For Freight Truck Driver Shortage Signals Logistics Sector Tightness

**Idea ID:** `weekly-surge-in-google-trends-for-freight-truck-driver-short`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising search interest in driver shortages highlights capacity constraints and pricing power in logistics. Logistics companies can raise prices amid capacity shortages, boosting revenues.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest for 'freight truck driver shortage'

## Signal Logic
Enter long XLI when weekly search interest surges 25% week-over-week

## Entry / Exit
Entry: Enter long XLI when weekly search interest surges 25% week-over-week Exit: Exit after 5 weeks or when weekly growth falls below 10%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'freight truck driver shortage' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Logistics capacity and labor shortages are frequent and topical, causing multiple search interest surges annually.

## Required Keys
- None
