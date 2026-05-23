# Healthcare Utilization Surge From Seasonal Illness Wave

**Idea ID:** `healthcare-utilization-surge-from-seasonal-illness-wave`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When Google Trends volume for urgent care and walk-in clinic searches spikes >50% above baseline (typically Oct–Mar and Jul–Aug), healthcare utilization demand surges. XLV outperforms SPY by 0.5–1.5% over next 10 days. Acute care utilization directly drives revenue for urgent care operators and hospital systems.

## Universe
- XLV

## Data Sources
- Google Trends weekly search volume for 'urgent care near me' and 'walk-in clinic' aggregated national index

## Signal Logic
If weekly Google Trends index for urgent care/walk-in clinic exceeds prior 13-week average by >40%

## Entry / Exit
Entry: If weekly Google Trends index for urgent care/walk-in clinic exceeds prior 13-week average by >40% Exit: After 8 trading days or if trend volume reverts to baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'urgent care near me' and 'walk-in clinic' aggregated national index via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal illness waves peak 4–5 times per year and last 2–3 weeks each, creating recurring signals.

## Required Keys
- None
