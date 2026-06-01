# Earthquake Activity Surge Triggers Insurance Sector Repricing

**Idea ID:** `earthquake-activity-surge-triggers-insurance-sector-repricin`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Multi-week seismic swarms (3+ magnitude 5.0+ earthquakes in 7 days) are rare but signal stress release or volcanic activity. Insurance and reinsurance markets reprice loss exposure sharply. Insurance/reinsurance companies face reserve raises and premium compression on seismic event clusters.

## Universe
- XLF

## Data Sources
- USGS Earthquake API (magnitude 4.5+ events) via earthquake_activity adapter

## Signal Logic
If 3 or more magnitude 5.0+ earthquakes occur within 7 days in a single geographic cluster AND previous 30 days had 1 or fewer

## Entry / Exit
Entry: If 3 or more magnitude 5.0+ earthquakes occur within 7 days in a single geographic cluster AND previous 30 days had 1 or fewer Exit: After 5 trading days or once seismic activity normalizes to historical baseline for 14 days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS Earthquake API (magnitude 4.5+ events) via earthquake_activity adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seismic swarms cluster 2-4 times per year on average; each swarm lasts 7-14 days and triggers repricing.

## Required Keys
- None
