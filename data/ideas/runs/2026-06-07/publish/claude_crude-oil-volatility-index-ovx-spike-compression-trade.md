# Crude Oil Volatility Index Ovx Spike Compression Trade

**Idea ID:** `crude-oil-volatility-index-ovx-spike-compression-trade`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
OVX spikes >30% in a single day (supply shock panic or geopolitical spike), then compresses over 5–10 days as mean reversion and sentiment stabilizes. Energy volatility spike followed by mean reversion lifts crude and energy equities as panic fades.

## Universe
- XLE

## Data Sources
- Yahoo Finance daily prices for OVX (Crude Oil Volatility Index) via price_only adapter

## Signal Logic
If OVX > (20-day MA × 1.30) and closes above open

## Entry / Exit
Entry: If OVX > (20-day MA × 1.30) and closes above open Exit: After 7 trading days or when OVX falls >10% from spike close

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for OVX (Crude Oil Volatility Index) via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: OVX >30% spikes occur monthly or bi-weekly; reversions are predictable and occur within 3–7 days.

## Required Keys
- None
