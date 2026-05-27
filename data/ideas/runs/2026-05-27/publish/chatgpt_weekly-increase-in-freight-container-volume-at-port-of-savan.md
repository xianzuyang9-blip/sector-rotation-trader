# Weekly Increase In Freight Container Volume At Port Of Savannah Signals Industrial Sector Strength

**Idea ID:** `weekly-increase-in-freight-container-volume-at-port-of-savan`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising container throughput signals increased trade activity and industrial output ahead of earnings. Higher freight volume correlates with stronger industrial demand and manufacturing growth.

## Universe
- XLI

## Data Sources
- Port container volume data from Port of Savannah via port_container_volume adapter

## Signal Logic
If weekly container volume increases by 5% or more vs prior 4-week average

## Entry / Exit
Entry: If weekly container volume increases by 5% or more vs prior 4-week average Exit: After 4 weeks or when volume falls below 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Port container volume data from Port of Savannah via port_container_volume adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Freight volume has consistent weekly variability tied to economic activity.

## Required Keys
- None
