# Hotel Occupancy Rate Drop Signals Travel Sector Weakness Rotation

**Idea ID:** `hotel-occupancy-rate-drop-signals-travel-sector-weakness-rot`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sharp weekly declines in U.S. hotel occupancy rates signal weakening business and leisure travel demand, indicating consumer pullback on discretionary travel spending. Hotels, airlines, and cruise operators (consumer discretionary) underperform when occupancy drops, signaling demand destruction in travel and hospitality verticals.

## Universe
- XLY

## Data Sources
- STR Global hotel occupancy rates published weekly via public html_table scrape from hospitality research indices

## Signal Logic
When weekly occupancy rate drops 5+ percentage points from 4-week average and falls below seasonal median for that week

## Entry / Exit
Entry: When weekly occupancy rate drops 5+ percentage points from 4-week average and falls below seasonal median for that week Exit: After 2 weeks or when occupancy recovers to 4-week average + 2 points

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use STR Global hotel occupancy rates published weekly via public html_table scrape from hospitality research indices via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Hotel occupancy swings 3–8% week-to-week due to seasonal variation, economic shocks, and competitor pricing; triggers occur 2–3 times per quarter.

## Required Keys
- None
