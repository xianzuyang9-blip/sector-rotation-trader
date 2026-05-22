# Financial Sector Repricing From Bank Deposit Outflow Alerts

**Idea ID:** `financial-sector-repricing-from-bank-deposit-outflow-alerts`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When WIMFSL (money market fund rates) spike >50 bps week-over-week AND RSS mentions of deposit flight spike >150% above baseline, it signals depositor unease, triggering brief weakness in regional bank stocks and financials rotation. Banks face NIM compression and credit risk when deposit flight accelerates; financial sector reprices downward before recovery.

## Universe
- XLF

## Data Sources
- FRED series WIMFSL (Weekly Insured Moneysaver Rate) + RSS count for 'bank run' + 'deposit flight' terms, weekly frequency

## Signal Logic
If WIMFSL spikes >50 bps WoW AND RSS deposit flight mentions exceed 150% of 4-week MA, short XLF

## Entry / Exit
Entry: If WIMFSL spikes >50 bps WoW AND RSS deposit flight mentions exceed 150% of 4-week MA, short XLF Exit: After 11 trading days OR if WIMFSL normalizes back toward prior week level

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series WIMFSL (Weekly Insured Moneysaver Rate) + RSS count for 'bank run' + 'deposit flight' terms, weekly frequency via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Money market rates and financial sector anxiety events occur 3–5 times per year; weekly data ensures timely signal detection.

## Required Keys
- None
