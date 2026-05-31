# Commercial Real Estate Stress Spike From Earthquake Activity Signals Sector Rotation

**Idea ID:** `commercial-real-estate-stress-spike-from-earthquake-activity`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Cluster of 4.5+ magnitude earthquakes in commercial real estate regions (San Francisco, Dallas, Oklahoma City) triggers insurance claims, property reassessments, and cap rate compression fears. Earthquakes raise insurance costs and devalue commercial property; XLRE weighs heavily on REITs with West/South exposure.

## Universe
- XLRE

## Data Sources
- USGS Earthquake Activity API magnitude 4.5+ events in major commercial real estate hubs (CA, TX, OK) via earthquake_activity adapter

## Signal Logic
If 2+ earthquakes magnitude 4.5+ strike within 7 days in commercial real estate regions, short XLRE on day 2 after second event

## Entry / Exit
Entry: If 2+ earthquakes magnitude 4.5+ strike within 7 days in commercial real estate regions, short XLRE on day 2 after second event Exit: Exit after 9 trading days or if seismic activity ceases for 14 days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS Earthquake Activity API magnitude 4.5+ events in major commercial real estate hubs (CA, TX, OK) via earthquake_activity adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Earthquake activity is random but frequent; 30-day windows in seismic zones almost always capture multiple events.

## Required Keys
- None
