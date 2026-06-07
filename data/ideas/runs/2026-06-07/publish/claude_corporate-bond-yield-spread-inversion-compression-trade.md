# Corporate Bond Yield Spread Inversion Compression Trade

**Idea ID:** `corporate-bond-yield-spread-inversion-compression-trade`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
High-yield OAS widens >40 bps in a single week (credit panic), then compresses as credit sentiment recovers and yield buyers step in. Credit widening panics financials and leverage-exposed cyclicals; recompression rallies both.

## Universe
- XLF

## Data Sources
- FRED series BAMLH0A0HYM2 (ICE BofA High Yield OAS) weekly

## Signal Logic
If HY OAS widens >40 bps WoW, close above open

## Entry / Exit
Entry: If HY OAS widens >40 bps WoW, close above open Exit: After 10 trading days or when HY OAS tightens >15 bps from entry

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series BAMLH0A0HYM2 (ICE BofA High Yield OAS) weekly via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weekly HY OAS moves >40 bps occur 2–4 times per year; reversions within 5–10 days are typical risk-on behavior.

## Required Keys
- None
