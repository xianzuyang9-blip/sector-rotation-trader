# Jobless Claims Spike Triggers Financial Sector Bearish Fade

**Idea ID:** `jobless-claims-spike-triggers-financial-sector-bearish-fade`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sudden spike in jobless claims above 50k relative to prior week signals recession fears and financial sector credit risk. Banks weaken as loan default expectations rise. Banks profit from lending spreads; jobless spikes presage defaults, raising NPL expectations and compressing valuations.

## Universe
- XLF

## Data Sources
- FRED series ICSA (Initial Claims, Seasonally Adjusted) via fred_series adapter

## Signal Logic
If weekly initial claims rise more than 50k from prior week and exceed 300k, short XLF on open next trading day

## Entry / Exit
Entry: If weekly initial claims rise more than 50k from prior week and exceed 300k, short XLF on open next trading day Exit: Exit after 8 trading days or if claims fall 30k from entry week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series ICSA (Initial Claims, Seasonally Adjusted) via fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: FRED jobless claims update every Thursday; 50k+ weekly swings occur 4-6 times per year, guaranteed hit within 30 days in any 6-month window.

## Required Keys
- None
