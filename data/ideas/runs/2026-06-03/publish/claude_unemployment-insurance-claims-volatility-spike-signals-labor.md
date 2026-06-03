# Unemployment Insurance Claims Volatility Spike Signals Labor Slack Tightening

**Idea ID:** `unemployment-insurance-claims-volatility-spike-signals-labor`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly jobless claims drop >15% in a single week after trending elevated, it signals rapid labor market tightening and wage pressure building. Sharp claims drops foreshadow wage inflation and potential Fed tightening; financial sector reprices rate expectations upward.

## Universe
- XLF

## Data Sources
- FRED Initial Jobless Claims (ICSA) weekly series through fred_series adapter

## Signal Logic
If weekly initial claims fall >12% from prior week AND claims level is below the 8-week moving average

## Entry / Exit
Entry: If weekly initial claims fall >12% from prior week AND claims level is below the 8-week moving average Exit: After 2 weeks or once claims rise >8% in a single week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED Initial Jobless Claims (ICSA) weekly series through fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weekly claims data is noisy and volatile; large single-week moves occur multiple times per year, especially around seasonal adjustments and weather events.

## Required Keys
- None
