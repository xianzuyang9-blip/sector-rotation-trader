# Unemployment Claims Surprise Beat Mean Reversion

**Idea ID:** `unemployment-claims-surprise-beat-mean-reversion`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When initial jobless claims beat consensus expectations by >10k and fall below their 4-week moving average, risk appetite snaps back into defensives before rotating to cyclicals over the following 2–3 weeks. Stronger labor markets remove recession hedges and rotate capital into consumer discretionary.

## Universe
- XLY

## Data Sources
- FRED series ICSA (Initial Claims) weekly data published Thursdays

## Signal Logic
If weekly initial claims beat prior consensus by >10k AND fall below 4-week MA, buy at close

## Entry / Exit
Entry: If weekly initial claims beat prior consensus by >10k AND fall below 4-week MA, buy at close Exit: After 6 trading days or once claims move above 4-week MA again

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series ICSA (Initial Claims) weekly data published Thursdays via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly claims releases create data surprises roughly 3–4 times per month that can exceed beat thresholds.

## Required Keys
- None
