# Daily Surge In Fred Weekly Initial Jobless Claims Signals Near-term Labor Market Stress

**Idea ID:** `daily-surge-in-fred-weekly-initial-jobless-claims-signals-ne`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sudden spike in jobless claims often indicates emerging labor market weakness affecting consumer and financial sectors. Financial sector negatively impacted by rising unemployment risk and reduced consumer credit demand.

## Universe
- XLF

## Data Sources
- FRED weekly initial jobless claims

## Signal Logic
Enter short XLF when weekly initial jobless claims rise more than 10% week-over-week

## Entry / Exit
Entry: Enter short XLF when weekly initial jobless claims rise more than 10% week-over-week Exit: Exit after 4 weeks or when claims decline consecutively for 2 weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly initial jobless claims via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 60
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weekly jobless claims regularly fluctuate with economic cycles and labor market shocks, triggering multiple signals yearly.

## Required Keys
- None
