# Weekly Surge In Google Trends For Overtime Jobs Signals Labor Market Tightness

**Idea ID:** `weekly-surge-in-google-trends-for-overtime-jobs-signals-labo`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sudden weekly increase in searches for overtime jobs indicates firms are struggling to fill shifts, signaling labor scarcity. Industrial companies benefit from strong labor demand as it signals robust production activity.

## Universe
- XLI

## Data Sources
- Google Trends weekly searches for 'overtime jobs'

## Signal Logic
Enter long XLI when weekly Google Trends for 'overtime jobs' rises 20%+ versus prior week

## Entry / Exit
Entry: Enter long XLI when weekly Google Trends for 'overtime jobs' rises 20%+ versus prior week Exit: Exit after 3 weeks or if trend falls below prior week's level

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly searches for 'overtime jobs' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor tightness signals frequently spike seasonally or with economic shifts, producing weekly jumps.

## Required Keys
- None
