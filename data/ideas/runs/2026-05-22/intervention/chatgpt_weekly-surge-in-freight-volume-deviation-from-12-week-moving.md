# Weekly Surge In Freight Volume Deviation From 12-week Moving Average

**Idea ID:** `weekly-surge-in-freight-volume-deviation-from-12-week-moving`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Freight volume rises more than 10% above its 12-week moving average, indicating sudden demand spikes in industrial activity. Increased freight volumes often precede industrial sector strength due to higher shipping and manufacturing demand.

## Universe
- XLI

## Data Sources
- Port container volume weekly data via port_container_volume adapter

## Signal Logic
Enter long XLI if weekly freight volume > 110% of 12-week MA

## Entry / Exit
Entry: Enter long XLI if weekly freight volume > 110% of 12-week MA Exit: Exit after 3 weeks or if volume falls below 105% of 12-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Port container volume weekly data via port_container_volume adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly freight volumes fluctuate seasonally and can spike due to demand surges or supply chain disruptions.

## Required Keys
- None
