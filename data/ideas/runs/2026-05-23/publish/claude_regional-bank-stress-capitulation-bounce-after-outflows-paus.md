# Regional Bank Stress Capitulation Bounce After Outflows Pause

**Idea ID:** `regional-bank-stress-capitulation-bounce-after-outflows-paus`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When KRE volume spikes >150% above 20-day MA on down days but price holds above its 200-day MA, deposit flight panic is exhausting. KRE typically rebounds 2–3% over next 5 trading days as short-covering floods in. Regional banks bounce sharply after panic selling volume exhausts when fundamental support levels hold.

## Universe
- XLF

## Data Sources
- Yahoo Finance daily price for KRE (Regional Banking ETF) volume and price; calculate 5-day volume MA

## Signal Logic
If KRE volume exceeds 20-day MA by 150% on a down close AND KRE closes above 200-day MA

## Entry / Exit
Entry: If KRE volume exceeds 20-day MA by 150% on a down close AND KRE closes above 200-day MA Exit: After 5 trading days or if volume returns to normal and price rolls over below entry

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily price for KRE (Regional Banking ETF) volume and price; calculate 5-day volume MA via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Banking sector stress cycles create volume spikes 3–5 times per quarter during risk-off periods.

## Required Keys
- None
