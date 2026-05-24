# Freight Rate Volatility Crush Signal

**Idea ID:** `freight-rate-volatility-crush-signal`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Truck tonnage index spikes or drops sharply week-over-week, signaling logistics capacity stress or demand collapse that precedes industrial sector moves. Sharp tonnage drops indicate manufacturing/logistics stress; spikes show demand surge that can lead to overheating.

## Universe
- XLI

## Data Sources
- FRED series TRUCKD (Truck Tonnage Index) weekly data

## Signal Logic
If TRUCKD weekly change exceeds ±3% from 4-week moving average

## Entry / Exit
Entry: If TRUCKD weekly change exceeds ±3% from 4-week moving average Exit: Close position after 10 trading days or when weekly change reverts within ±1.5% of MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series TRUCKD (Truck Tonnage Index) weekly data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weekly tonnage data is volatile with supply chain micro-shocks firing multiple times per month.

## Required Keys
- None
