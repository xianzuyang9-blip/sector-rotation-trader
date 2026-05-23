# Consumer Stress Spike In Google Trends For Urgent Daycare Availability Signals Xly Weakness

**Idea ID:** `consumer-stress-spike-in-google-trends-for-urgent-daycare-av`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising urgent daycare searches reflect parental stress and can reduce discretionary spending. Consumer discretionary spending contracts when household stress rises.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'urgent daycare availability'

## Signal Logic
Enter short XLY if weekly 'urgent daycare availability' searches increase by 20% over prior week

## Entry / Exit
Entry: Enter short XLY if weekly 'urgent daycare availability' searches increase by 20% over prior week Exit: Exit after 4 weeks or when searches decline below 10% growth week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'urgent daycare availability' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Daycare availability stress regularly spikes seasonally and during economic pressure periods.

## Required Keys
- None
