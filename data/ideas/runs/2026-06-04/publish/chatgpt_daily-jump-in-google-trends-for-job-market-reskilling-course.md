# Daily Jump In Google Trends For Job Market Reskilling Courses Indicates Labor Market Shift

**Idea ID:** `daily-jump-in-google-trends-for-job-market-reskilling-course`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Spikes in job reskilling searches suggest workers anticipating layoffs or sector shifts, increasing labor market uncertainty. Labor market stress often pressures financial sector through credit risk and loan performance concerns.

## Universe
- XLF

## Data Sources
- Google Trends daily search interest for 'reskilling courses' and 'online job training'

## Signal Logic
If daily search interest jumps 20% above 10-day moving average

## Entry / Exit
Entry: If daily search interest jumps 20% above 10-day moving average Exit: After 10 trading days or when daily interest drops below 5-day moving average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'reskilling courses' and 'online job training' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor market shifts and reskilling trends are common near economic inflection points.

## Required Keys
- None
