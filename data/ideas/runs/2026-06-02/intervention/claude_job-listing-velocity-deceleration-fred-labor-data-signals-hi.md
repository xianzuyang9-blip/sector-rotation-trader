# Job Listing Velocity Deceleration Fred Labor Data Signals Hiring Cooldown

**Idea ID:** `job-listing-velocity-deceleration-fred-labor-data-signals-hi`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When job opening counts decline sharply relative to payroll growth, it signals slowing demand for new hires and rising recession risk; precedes earnings miss. Hiring slowdown foreshadows consumer discretionary weakness as unemployment risk rises and wage growth cools.

## Universe
- XLY

## Data Sources
- FRED series: Total Nonfarm Payroll (PAYEMS) and Job Openings (JTTS) weekly/monthly changes

## Signal Logic
When JTTS falls more than 3% week-over-week and is below its 52-week moving average, enter short XLY

## Entry / Exit
Entry: When JTTS falls more than 3% week-over-week and is below its 52-week moving average, enter short XLY Exit: Exit after 7 trading days or when JTTS rebounds above prior week level

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series: Total Nonfarm Payroll (PAYEMS) and Job Openings (JTTS) weekly/monthly changes via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: FRED labor data is released weekly; job opening drops of 3%+ occur several times per quarter in normal market cycles.

## Required Keys
- None
