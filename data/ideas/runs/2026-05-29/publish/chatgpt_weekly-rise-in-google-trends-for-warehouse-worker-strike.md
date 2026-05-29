# Weekly Rise In Google Trends For Warehouse Worker Strike

**Idea ID:** `weekly-rise-in-google-trends-for-warehouse-worker-strike`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing searches about warehouse strikes indicate labor unrest disrupting supply chains and inventory flows. Industrial sector suffers operational disruption and cost inflation from labor strikes.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest for 'warehouse worker strike'

## Signal Logic
Enter short XLI when weekly search interest rises more than 25% week-over-week

## Entry / Exit
Entry: Enter short XLI when weekly search interest rises more than 25% week-over-week Exit: Exit after 4 weeks or once weekly growth falls below 5%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'warehouse worker strike' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Warehouse labor issues are recurrent and generate search spikes multiple times per year.

## Required Keys
- None
