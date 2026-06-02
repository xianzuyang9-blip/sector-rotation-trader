# Freight Volume Collapse From Port Container Backlog Signals Industrial Slowdown

**Idea ID:** `freight-volume-collapse-from-port-container-backlog-signals-`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sudden drop in container volumes week-over-week (-5%) signals export weakness and manufacturing slowdown. Industrial and materials sectors face demand headwinds. Container volume is leading indicator of trade activity; collapse signals demand destruction for machinery, equipment, and materials.

## Universe
- XLI

## Data Sources
- Port container volume weekly data (Los Angeles, Long Beach, New York) via port_container_volume adapter

## Signal Logic
If total weekly container volume (avg 3 major ports) falls >5% from prior week, short XLI on next open

## Entry / Exit
Entry: If total weekly container volume (avg 3 major ports) falls >5% from prior week, short XLI on next open Exit: Exit after 8 trading days or if volume recovers 3% from entry week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Port container volume weekly data (Los Angeles, Long Beach, New York) via port_container_volume adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Port data updates weekly; seasonal and cyclical volume swings guarantee 5% drops several times per year.

## Required Keys
- None
