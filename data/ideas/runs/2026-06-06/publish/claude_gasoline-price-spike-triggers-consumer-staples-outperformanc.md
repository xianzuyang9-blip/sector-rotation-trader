# Gasoline Price Spike Triggers Consumer Staples Outperformance

**Idea ID:** `gasoline-price-spike-triggers-consumer-staples-outperformanc`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sharp weekly spikes in gasoline prices above prior 4-week rolling average signal input cost inflation that rotates demand toward cheaper staples and away from discretionary goods. Staples outperform when consumers face rising transport/fuel costs and tighten discretionary spending.

## Universe
- XLP

## Data Sources
- FRED series GASDESW (weekly average gasoline prices) via fred_series adapter

## Signal Logic
When weekly gasoline price exceeds 4-week moving average by >8%, enter long XLP

## Entry / Exit
Entry: When weekly gasoline price exceeds 4-week moving average by >8%, enter long XLP Exit: Exit after 15 trading days or when gasoline price falls back within 3% of 4-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series GASDESW (weekly average gasoline prices) via fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Gasoline prices fluctuate weekly with supply shocks and demand cycles; 8% spikes occur 3-4 times per quarter.

## Required Keys
- None
