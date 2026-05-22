# Weekly Jump In Google Trends For Electric Vehicle Battery Replacement Signals Auto Tech Stress

**Idea ID:** `weekly-jump-in-google-trends-for-electric-vehicle-battery-re`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A 25%+ weekly increase in searches for EV battery replacement indicates rising consumer concerns about EV reliability. Rising EV repair concerns can pressure auto and discretionary sectors related to EV sales.

## Universe
- XLY

## Data Sources
- Google Trends weekly data via google_trends adapter

## Signal Logic
Enter short XLY if weekly EV battery replacement search interest > 125% prior week

## Entry / Exit
Entry: Enter short XLY if weekly EV battery replacement search interest > 125% prior week Exit: Exit after 4 weeks or interest falls below 110%

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
- Why It Should Fire Soon: EV battery concerns fluctuate with recalls, warranty news, and consumer reports.

## Required Keys
- None
