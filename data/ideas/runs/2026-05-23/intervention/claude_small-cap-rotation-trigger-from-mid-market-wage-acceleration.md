# Small-cap Rotation Trigger From Mid-market Wage Acceleration

**Idea ID:** `small-cap-rotation-trigger-from-mid-market-wage-acceleration`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When monthly wage growth in mid-market sectors accelerates >0.5% MoM, small-cap stocks rally as markets price in strong consumer spending and lower recession risk. IWM typically outperforms SPY by 1–2% over next 10 days. Wage acceleration in lower-income brackets drives consumer discretionary spending disproportionately.

## Universe
- XLY

## Data Sources
- FRED series MMNRNJ (Average Hourly Earnings for all employees, mid-market sector proxy) weekly data

## Signal Logic
If monthly MoM wage growth exceeds 0.5% and IWM closes above its 50-day MA

## Entry / Exit
Entry: If monthly MoM wage growth exceeds 0.5% and IWM closes above its 50-day MA Exit: After 8 trading days or once wage growth decelerates below 0.3% MoM

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series MMNRNJ (Average Hourly Earnings for all employees, mid-market sector proxy) weekly data via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Monthly wage data releases occur monthly; 0.5%+ acceleration happens 2–3 times per year.

## Required Keys
- None
