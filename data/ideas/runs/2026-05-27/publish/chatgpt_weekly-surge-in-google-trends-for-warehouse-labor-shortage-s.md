# Weekly Surge In Google Trends For Warehouse Labor Shortage Signals Rising Labor Pressure

**Idea ID:** `weekly-surge-in-google-trends-for-warehouse-labor-shortage-s`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Growing search interest in warehouse labor shortages reveals tightening labor markets impacting supply chains. Labor shortages increase costs and can delay production, pressuring industrial stocks.

## Universe
- XLI

## Data Sources
- Google Trends weekly data for 'warehouse labor shortage'

## Signal Logic
If weekly Google Trends for 'warehouse labor shortage' rises 50% above prior 8-week average

## Entry / Exit
Entry: If weekly Google Trends for 'warehouse labor shortage' rises 50% above prior 8-week average Exit: After 4 weeks or when trend falls below 8-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data for 'warehouse labor shortage' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor issues in warehouses are recurrent and generate periodic search interest spikes.

## Required Keys
- None
