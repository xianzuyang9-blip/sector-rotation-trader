# Daily Spike In Earthquake Activity In Major Port Regions

**Idea ID:** `daily-spike-in-earthquake-activity-in-major-port-regions`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased earthquake activity near ports signals potential logistics disruptions and inventory bottlenecks. Industrial and logistics sectors face short-term disruptions from port closures or damage.

## Universe
- XLI

## Data Sources
- USGS daily earthquake activity near major port cities

## Signal Logic
Enter short XLI on daily earthquake count increase of 2+ events near major ports compared to 14-day average

## Entry / Exit
Entry: Enter short XLI on daily earthquake count increase of 2+ events near major ports compared to 14-day average Exit: Exit after 7 trading days or when earthquake activity normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS daily earthquake activity near major port cities via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Port-adjacent earthquake clusters occur sporadically but roughly monthly on average.

## Required Keys
- None
