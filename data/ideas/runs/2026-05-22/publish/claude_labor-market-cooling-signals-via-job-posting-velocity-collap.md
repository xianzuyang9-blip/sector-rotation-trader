# Labor Market Cooling Signals Via Job Posting Velocity Collapse

**Idea ID:** `labor-market-cooling-signals-via-job-posting-velocity-collap`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When 4-week average of initial jobless claims rises >12% YoY, employers are cutting headcount faster than seasonal trends would predict, triggering rotation into defensive consumer staples. Consumer discretionary sector is sensitive to employment uncertainty; rising claims signal consumer spending risk.

## Universe
- XLY

## Data Sources
- FRED series ICSA (Initial Claims, weekly) smoothed 4-week average

## Signal Logic
If ICSA 4-week MA rises >12% YoY AND above its 52-week moving average, short XLY

## Entry / Exit
Entry: If ICSA 4-week MA rises >12% YoY AND above its 52-week moving average, short XLY Exit: After 14 trading days OR if ICSA 4-week MA falls back below 52-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series ICSA (Initial Claims, weekly) smoothed 4-week average via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Initial claims data releases weekly; threshold of 12% YoY triggers 3–5 times per year in normal labor cycles.

## Required Keys
- None
