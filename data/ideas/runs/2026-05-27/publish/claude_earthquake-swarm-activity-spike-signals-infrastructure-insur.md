# Earthquake Swarm Activity Spike Signals Infrastructure Insurance Sector Volatility

**Idea ID:** `earthquake-swarm-activity-spike-signals-infrastructure-insur`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When earthquake swarm activity (5+ magnitude >3.0 events within 7 days in a single region) occurs, insurance claim expectations rise and infrastructure repair demand spikes; regional economic disruption signals follow within 1–3 days. Infrastructure repair, engineering services, and heavy equipment demand increase; construction sector benefits from disaster-driven capital deployment.

## Universe
- XLI

## Data Sources
- USGS Earthquake API daily magnitude >3.0 event counts from seismic networks

## Signal Logic
7-day rolling count of magnitude >3.0 earthquakes in any USGS region exceeds 5 events AND closest prior 30-day window had <4 events

## Entry / Exit
Entry: 7-day rolling count of magnitude >3.0 earthquakes in any USGS region exceeds 5 events AND closest prior 30-day window had <4 events Exit: After 20 trading days OR seismic activity returns to <2 events per 7-day window

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS Earthquake API daily magnitude >3.0 event counts from seismic networks via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Known seismic zones (California, Pacific Northwest, Taiwan) experience swarm activity 3–4 times per quarter; aftershock sequences trigger this signal regularly.

## Required Keys
- None
