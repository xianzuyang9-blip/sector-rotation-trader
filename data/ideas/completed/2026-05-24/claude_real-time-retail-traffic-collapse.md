# Real-time Retail Traffic Collapse

**Idea ID:** `real-time-retail-traffic-collapse`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in combined search interest for store closures and retail layoff news precede consumer discretionary drawdowns. Rising search for closures and cuts signals consumer avoidance behavior and discretionary pullback.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'store closing near me' + 'retail job cuts' combined index

## Signal Logic
If combined index rises >25% week-over-week

## Entry / Exit
Entry: If combined index rises >25% week-over-week Exit: After 12 trading days or when index falls below prior week baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'store closing near me' + 'retail job cuts' combined index via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Retail news and store closure announcements spike weekly; threshold is loose enough to fire 3–4 times per month.

## Required Keys
- None
