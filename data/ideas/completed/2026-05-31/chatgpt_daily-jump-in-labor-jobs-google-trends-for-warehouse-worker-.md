# Daily Jump In Labor Jobs Google Trends For Warehouse Worker Shortage

**Idea ID:** `daily-jump-in-labor-jobs-google-trends-for-warehouse-worker-`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Growing warehouse labor scarcity signals rising wage pressure and supply chain bottlenecks. Industrial and logistics sectors face cost inflation and operational delays.

## Universe
- XLI

## Data Sources
- Google Trends daily search interest for 'warehouse worker shortage'

## Signal Logic
If daily search interest exceeds 25% above 30-day average

## Entry / Exit
Entry: If daily search interest exceeds 25% above 30-day average Exit: When interest drops below 10% increase for 3 days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'warehouse worker shortage' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor shortages are ongoing and produce frequent search spikes due to news and hiring cycles.

## Required Keys
- None
