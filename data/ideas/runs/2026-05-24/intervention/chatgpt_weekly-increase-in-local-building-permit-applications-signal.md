# Weekly Increase In Local Building Permit Applications Signals Construction Sector Lift

**Idea ID:** `weekly-increase-in-local-building-permit-applications-signal`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising building permits indicate increased construction activity expectations, benefiting construction materials and services sectors. Materials sector benefits from higher demand for construction inputs driven by new projects.

## Universe
- XLB

## Data Sources
- stable public html_table scraping of municipal building permits

## Signal Logic
If weekly building permits rise by more than 10% week-over-week

## Entry / Exit
Entry: If weekly building permits rise by more than 10% week-over-week Exit: After 6 weeks or if permits fall below baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use stable public html_table scraping of municipal building permits via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Monthly and weekly permit data consistently fluctuates with construction cycles and seasonality.

## Required Keys
- None
