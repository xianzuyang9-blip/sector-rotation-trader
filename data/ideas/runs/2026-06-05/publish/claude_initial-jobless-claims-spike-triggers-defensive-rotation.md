# Initial Jobless Claims Spike Triggers Defensive Rotation

**Idea ID:** `initial-jobless-claims-spike-triggers-defensive-rotation`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly initial jobless claims rise >12% from prior week. Signals rapid labor market deterioration and recession risk. Job losses reduce consumer spending power; discretionary demand implodes while staples and healthcare remain sticky.

## Universe
- XLY

## Data Sources
- FRED series ICSA (weekly initial jobless claims)

## Signal Logic
If ICSA > (prior week * 1.12), short XLY and long XLP equally weighted

## Entry / Exit
Entry: If ICSA > (prior week * 1.12), short XLY and long XLP equally weighted Exit: After 14 trading days or when ICSA declines for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series ICSA (weekly initial jobless claims) via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Jobless claims spike weekly and exceed 12% thresholds 1-2 times monthly on seasonal and economic shocks.

## Required Keys
- None
