# Unemployment Claims Spike Triggers Defensive Rotation

**Idea ID:** `unemployment-claims-spike-triggers-defensive-rotation`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly jobless claims frequently spike 10-15% above 4-week moving average due to seasonal adjustments, weather, or regional shocks. This triggers flight-to-safety rotation out of cyclicals. Consumer discretionary underperforms when labor market stress signals weaken demand ahead.

## Universe
- XLY

## Data Sources
- FRED series ICSA (Initial Claims) weekly data via fred_series adapter

## Signal Logic
If ICSA rises 12% or more week-over-week AND exceeds its 4-week MA by more than 1 standard deviation

## Entry / Exit
Entry: If ICSA rises 12% or more week-over-week AND exceeds its 4-week MA by more than 1 standard deviation Exit: Exit after 3 weeks or when ICSA falls back below 4-week MA for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series ICSA (Initial Claims) weekly data via fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 120
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Claims data releases weekly; seasonal swings and weather disruptions cause 10%+ moves several times per quarter.

## Required Keys
- None
