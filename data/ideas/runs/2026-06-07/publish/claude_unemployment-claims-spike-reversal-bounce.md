# Unemployment Claims Spike Reversal Bounce

**Idea ID:** `unemployment-claims-spike-reversal-bounce`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly jobless claims spike above the 4-week moving average by >15%, triggering panic, then reverse within 1-2 weeks as data normalizes or expectations reset. Consumer discretionary rallies on relief from labor shock fears; financial sector also benefits from recession-avoidance narrative.

## Universe
- XLY

## Data Sources
- FRED series ICSA (Initial Claims, Seasonally Adjusted) weekly

## Signal Logic
If ICSA > (4-week MA × 1.15) close above prior week close

## Entry / Exit
Entry: If ICSA > (4-week MA × 1.15) close above prior week close Exit: After 7 calendar days or when ICSA falls back below 1.10× 4-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series ICSA (Initial Claims, Seasonally Adjusted) weekly via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Claims spike >15% above 4-week MA occurs 3–5 times per year; reversal within 7–14 days is typical seasonal/statistical noise.

## Required Keys
- None
