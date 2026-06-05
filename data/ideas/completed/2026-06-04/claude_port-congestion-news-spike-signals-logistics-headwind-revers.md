# Port Congestion News Spike Signals Logistics Headwind Reversal Trade

**Idea ID:** `port-congestion-news-spike-signals-logistics-headwind-revers`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in port congestion news often precede rapid clearance periods as supply chains self-correct, creating short-duration bullish trades in logistics and transport sectors. Port congestion news peaks often mark inflection points where volumes clear; transport operators and industrial suppliers see demand recovery.

## Universe
- XLI

## Data Sources
- RSS news feed count for 'port congestion' and 'container backlog' from shipping and logistics news through rss_count adapter

## Signal Logic
If weekly RSS count for port congestion news exceeds prior 8-week average by 60% and prior week count was 30% higher, enter long position

## Entry / Exit
Entry: If weekly RSS count for port congestion news exceeds prior 8-week average by 60% and prior week count was 30% higher, enter long position Exit: Exit after 7 trading days or if RSS count falls below 8-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed count for 'port congestion' and 'container backlog' from shipping and logistics news through rss_count adapter via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Port news cycles are volatile and weather-dependent; seasonal shipping peaks and disruptions trigger signal fires 2-3 times per quarter.

## Required Keys
- None
