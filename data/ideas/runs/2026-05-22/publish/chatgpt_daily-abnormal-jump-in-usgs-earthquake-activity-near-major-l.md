# Daily Abnormal Jump In Usgs Earthquake Activity Near Major Logistics Hubs Signals Freight Disruption Risk

**Idea ID:** `daily-abnormal-jump-in-usgs-earthquake-activity-near-major-l`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A 50%+ daily increase in earthquake events magnitude 3+ near major ports/warehouses suggests potential logistic interruptions. Earthquake disruptions increase logistics costs and delay industrial shipments.

## Universe
- XLI

## Data Sources
- USGS earthquake daily activity via earthquake_activity adapter

## Signal Logic
Enter short XLI if daily earthquake count near hubs > 150% of 30-day average

## Entry / Exit
Entry: Enter short XLI if daily earthquake count near hubs > 150% of 30-day average Exit: Exit after 5 days or if counts revert below 120%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake daily activity via earthquake_activity adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seismic activity near logistics hubs is regularly recorded and can spike unexpectedly.

## Required Keys
- None
