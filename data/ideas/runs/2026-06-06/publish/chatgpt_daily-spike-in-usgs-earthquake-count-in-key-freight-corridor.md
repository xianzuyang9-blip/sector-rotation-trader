# Daily Spike In Usgs Earthquake Count In Key Freight Corridor Signals Logistics Disruption

**Idea ID:** `daily-spike-in-usgs-earthquake-count-in-key-freight-corridor`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Higher-than-normal earthquake activity disrupts freight corridors causing short-term logistic bottlenecks. Industrial sector depends heavily on smooth freight logistics; disruptions hit earnings.

## Universe
- XLI

## Data Sources
- USGS earthquake activity daily counts

## Signal Logic
Enter short XLI if daily USGS earthquake count in California freight corridor rises above 3 std deviations from 30-day mean

## Entry / Exit
Entry: Enter short XLI if daily USGS earthquake count in California freight corridor rises above 3 std deviations from 30-day mean Exit: Exit after 7 trading days or earthquake counts normalize below 1 std deviation

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity daily counts via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seismic activity fluctuates regularly, causing intermittent short-term spikes.

## Required Keys
- None
