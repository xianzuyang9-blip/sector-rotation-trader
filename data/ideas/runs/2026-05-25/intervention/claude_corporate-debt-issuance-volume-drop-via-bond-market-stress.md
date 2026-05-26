# Corporate Debt Issuance Volume Drop Via Bond Market Stress

**Idea ID:** `corporate-debt-issuance-volume-drop-via-bond-market-stress`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Spikes in corporate bond spreads combined with declining issuance signal credit stress; financial and industrial equities weaken within 3–7 days. Rising bond spreads reflect credit market dysfunction; financial institutions and investment-grade borrowers face funding pressure.

## Universe
- XLF

## Data Sources
- FRED series TERMCBCCALLNS (corporate bond spreads) daily through fred_series adapter, paired with volume proxies from financial news RSS

## Signal Logic
When daily corporate bond spread (TERMCBCCALLNS) exceeds 20-day moving average by >15 basis points AND spreads move >10 bps higher day-over-day

## Entry / Exit
Entry: When daily corporate bond spread (TERMCBCCALLNS) exceeds 20-day moving average by >15 basis points AND spreads move >10 bps higher day-over-day Exit: After 7 trading days or when spreads contract below 20-day MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series TERMCBCCALLNS (corporate bond spreads) daily through fred_series adapter, paired with volume proxies from financial news RSS via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Corporate bond spreads widen frequently during volatile macro periods; >15 bps spikes occur multiple times per quarter.

## Required Keys
- None
