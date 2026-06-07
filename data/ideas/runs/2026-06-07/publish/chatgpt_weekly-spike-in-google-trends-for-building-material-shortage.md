# Weekly Spike In Google Trends For Building Material Shortage Signals Construction Sector Input Stress

**Idea ID:** `weekly-spike-in-google-trends-for-building-material-shortage`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Growing consumer and industry concern about building material scarcity signals rising cost pressures. Material shortages raise costs and delay projects impacting basic materials sector.

## Universe
- XLB

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly Google Trends for 'building material shortage' rises 30% week-over-week

## Entry / Exit
Entry: If weekly Google Trends for 'building material shortage' rises 30% week-over-week Exit: When growth falls below 10%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Material shortages and supply chain issues are common and frequently reported.

## Required Keys
- None
