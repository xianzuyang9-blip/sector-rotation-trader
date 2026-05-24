# Labor Force Participation Gap Snap

**Idea ID:** `labor-force-participation-gap-snap`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Unexpected weekly jumps or drops in labor force participation signal worker re-entry or exit, shifting wage/employment narrative and equity rotation. Rising participation eases wage pressure and supports consumer credit; financial sector reprices rate expectations.

## Universe
- XLF

## Data Sources
- FRED series CIVPART (Civilian Labor Force Participation Rate) weekly

## Signal Logic
If weekly change in CIVPART exceeds ±0.15 percentage points from prior week

## Entry / Exit
Entry: If weekly change in CIVPART exceeds ±0.15 percentage points from prior week Exit: After 8 trading days or when weekly change normalizes within ±0.05 pp

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series CIVPART (Civilian Labor Force Participation Rate) weekly via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor participation reports generate weekly moves; seasonal patterns and migration shifts fire this 2–3 times monthly.

## Required Keys
- None
