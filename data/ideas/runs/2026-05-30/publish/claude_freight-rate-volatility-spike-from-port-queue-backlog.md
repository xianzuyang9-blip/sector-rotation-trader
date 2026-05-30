# Freight Rate Volatility Spike From Port Queue Backlog

**Idea ID:** `freight-rate-volatility-spike-from-port-queue-backlog`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly container volumes spike 20%+ above 12-week average (indicating congestion), freight rates and logistics demand jump within 3-5 days as shippers rush to secure capacity. Industrials and shipping companies see margin expansion and demand surge when freight congestion drives rate hikes.

## Universe
- XLI

## Data Sources
- Port container volume data from existing port_container_volume adapter (major US ports: LA, Long Beach, New York, Savannah) tracking weekly volumes

## Signal Logic
If aggregate US port TEU volume jumps >20% above 12-week average, enter long XLI

## Entry / Exit
Entry: If aggregate US port TEU volume jumps >20% above 12-week average, enter long XLI Exit: Exit after 10 trading days or when volume normalizes below 110% of 12-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Port container volume data from existing port_container_volume adapter (major US ports: LA, Long Beach, New York, Savannah) tracking weekly volumes via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Port congestion is seasonal and episodic; volume spikes fire several times per quarter, especially post-holiday and pre-tariff rush periods.

## Required Keys
- None
