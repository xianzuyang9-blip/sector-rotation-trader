# Mortgage Rate Spike Affordability Panic Fade

**Idea ID:** `mortgage-rate-spike-affordability-panic-fade`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
30-year mortgage rates jump >25 bps in a single day (Fed move or risk-off shock), triggering panic in housing-sensitive sectors, then fade as sentiment stabilizes. Real estate panics on rate shock, then recovers as investors realize medium-term fundamentals intact; REITs snap back.

## Universe
- XLRE

## Data Sources
- FRED series MORTGAGE30US (30-Year Fixed Mortgage Rate) daily

## Signal Logic
If MORTGAGE30US rises >25 bps in one day, close above open

## Entry / Exit
Entry: If MORTGAGE30US rises >25 bps in one day, close above open Exit: After 5 trading days or when mortgage rate falls back >10 bps from entry

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series MORTGAGE30US (30-Year Fixed Mortgage Rate) daily via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Daily mortgage rate moves >25 bps occur 6–10 times per year; reversions within 3–7 days are common.

## Required Keys
- None
