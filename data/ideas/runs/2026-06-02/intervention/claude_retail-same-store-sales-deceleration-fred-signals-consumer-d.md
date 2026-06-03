# Retail Same-store Sales Deceleration Fred Signals Consumer Discretionary Slowdown

**Idea ID:** `retail-same-store-sales-deceleration-fred-signals-consumer-d`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When retail sales growth decelerates sharply relative to prior 4 weeks and falls below prior-year growth, it signals consumer discretionary weakness and inventory correction. Retail sales slowdown precedes earnings misses and margin compression in discretionary retailers and restaurants.

## Universe
- XLY

## Data Sources
- FRED series: Retail Sales (RSXFS) and Retail Trade Employment (RETA) weekly/monthly changes

## Signal Logic
When RSXFS monthly change drops below 1% AND is below prior month by >0.5 percentage points, enter short XLY

## Entry / Exit
Entry: When RSXFS monthly change drops below 1% AND is below prior month by >0.5 percentage points, enter short XLY Exit: Exit after 8 trading days or when monthly change exceeds 1.5% for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series: Retail Sales (RSXFS) and Retail Trade Employment (RETA) weekly/monthly changes via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: FRED retail data is released monthly; deceleration triggers occur 2–4 times per year during normal market cycles.

## Required Keys
- None
