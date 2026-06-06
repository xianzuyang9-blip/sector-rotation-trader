# Weekly Spike In Google Trends For Construction Labor Shortage Signals Industrial And Materials Sector Tightness

**Idea ID:** `weekly-spike-in-google-trends-for-construction-labor-shortag`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising construction labor shortage searches indicate tight labor markets boosting wages and input costs. Materials sector margins pressured by rising labor costs and project delays.

## Universe
- XLB

## Data Sources
- Google Trends weekly search interest for 'construction labor shortage'

## Signal Logic
Enter short XLB when weekly search interest increases 20% week-over-week

## Entry / Exit
Entry: Enter short XLB when weekly search interest increases 20% week-over-week Exit: Exit after 4 weeks or when weekly growth falls below 5%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'construction labor shortage' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor shortages in construction are cyclical and topical, producing frequent search interest spikes.

## Required Keys
- None
