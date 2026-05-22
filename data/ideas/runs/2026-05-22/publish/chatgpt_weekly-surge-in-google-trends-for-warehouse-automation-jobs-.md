# Weekly Surge In Google Trends For Warehouse Automation Jobs Signals Industrial Tech Adoption

**Idea ID:** `weekly-surge-in-google-trends-for-warehouse-automation-jobs-`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A 25%+ weekly increase in searches for warehouse automation jobs reflects rising industrial tech adoption. Increased interest in automation jobs signals capex and productivity gains in industrials.

## Universe
- XLI

## Data Sources
- Google Trends weekly data via google_trends adapter

## Signal Logic
Enter long XLI if weekly search interest for automation jobs > 125% prior week

## Entry / Exit
Entry: Enter long XLI if weekly search interest for automation jobs > 125% prior week Exit: Exit after 4 weeks or if interest falls below 110%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Interest in automation jobs fluctuates with tech adoption cycles and labor market shifts.

## Required Keys
- None
