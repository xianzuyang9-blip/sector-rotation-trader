# Earthquake Swarm Activity Triggers Insurance And Reinsurance Demand Spike

**Idea ID:** `earthquake-swarm-activity-triggers-insurance-and-reinsurance`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Clusters of earthquakes (3+ magnitude 3.0+ events in 7 days) trigger insurance broker phone calls, quote requests, and reinsurance repricing expectations, creating brief bullish waves in financial sector. Insurance and reinsurance companies see revenue acceleration and pricing power improvements during seismic event clusters.

## Universe
- XLF

## Data Sources
- USGS earthquake activity API (daily magnitude 3.0+) via earthquake_activity adapter

## Signal Logic
If USGS logs 3+ magnitude 3.0+ earthquakes within any rolling 7-day window in a seismically active region (CA, NV, OR, WA), buy XLF

## Entry / Exit
Entry: If USGS logs 3+ magnitude 3.0+ earthquakes within any rolling 7-day window in a seismically active region (CA, NV, OR, WA), buy XLF Exit: After 8 trading days OR if earthquake activity ceases for 7+ consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity API (daily magnitude 3.0+) via earthquake_activity adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Earthquake swarms occur 4–6 times annually in high-activity zones; daily USGS data ensures timely detection.

## Required Keys
- None
