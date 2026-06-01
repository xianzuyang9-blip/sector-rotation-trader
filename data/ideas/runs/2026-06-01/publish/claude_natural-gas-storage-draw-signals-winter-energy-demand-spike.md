# Natural Gas Storage Draw Signals Winter Energy Demand Spike

**Idea ID:** `natural-gas-storage-draw-signals-winter-energy-demand-spike`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Winter draws from storage exceed forecasts when temperatures drop unexpectedly. A 5%+ week-over-week storage decline signals heating demand surge and energy cost inflation. Energy sector profits from demand spikes and price rises during storage draw cycles.

## Universe
- XLE

## Data Sources
- FRED series DHHNGSP (Weekly Natural Gas Storage, US) via fred_series adapter

## Signal Logic
If weekly storage draw exceeds 5% of current inventory AND draw exceeds prior year draw by 20%+ for same week

## Entry / Exit
Entry: If weekly storage draw exceeds 5% of current inventory AND draw exceeds prior year draw by 20%+ for same week Exit: After 4 weeks or once storage levels stabilize within historical 5-year range

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series DHHNGSP (Weekly Natural Gas Storage, US) via fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 60
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Winter months (Nov-Mar) see 5%+ weekly draws 8-12 times per season due to temperature volatility.

## Required Keys
- None
