# Daily Spike In Earthquake Activity Near Key Manufacturing Hubs Signals Short-term Supply Disruption

**Idea ID:** `daily-spike-in-earthquake-activity-near-key-manufacturing-hu`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased local seismic activity can disrupt manufacturing operations and supply chains temporarily. Earthquake disruptions impair industrial output and can depress industrial sector stocks.

## Universe
- XLI

## Data Sources
- USGS earthquake activity daily data near major manufacturing regions

## Signal Logic
If daily earthquake count in defined manufacturing zone exceeds 3 standard deviations above 30-day average

## Entry / Exit
Entry: If daily earthquake count in defined manufacturing zone exceeds 3 standard deviations above 30-day average Exit: After 7 trading days or when earthquake activity normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity daily data near major manufacturing regions via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Moderate seismic events occur frequently in active zones and are measurable daily.

## Required Keys
- None
