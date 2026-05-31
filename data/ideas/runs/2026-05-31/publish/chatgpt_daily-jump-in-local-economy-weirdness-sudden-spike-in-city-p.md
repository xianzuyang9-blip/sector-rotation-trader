# Daily Jump In Local Economy Weirdness Sudden Spike In City Parking Violation Complaints

**Idea ID:** `daily-jump-in-local-economy-weirdness-sudden-spike-in-city-p`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Spike in parking complaints suggests urban mobility or enforcement changes impacting local retail foot traffic. Consumer discretionary retail sensitive to local mobility and parking availability.

## Universe
- XLY

## Data Sources
- City stable public tables on parking violation complaints

## Signal Logic
If daily complaints exceed 200% of 30-day average

## Entry / Exit
Entry: If daily complaints exceed 200% of 30-day average Exit: When complaints return below 120% of average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use City stable public tables on parking violation complaints via scrape (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Parking complaint surges are common due to policy or enforcement changes in cities.

## Required Keys
- None
