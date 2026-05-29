# Daily Surge In Google Trends For Emergency Auto Repair Near Me

**Idea ID:** `daily-surge-in-google-trends-for-emergency-auto-repair-near-`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sharp rise in emergency auto repair searches signals rising consumer stress and unexpected vehicle maintenance costs. Consumer discretionary spending may be squeezed by rising emergency vehicle costs.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest for 'emergency auto repair near me'

## Signal Logic
Enter short XLY when daily search interest rises more than 30% versus 7-day average

## Entry / Exit
Entry: Enter short XLY when daily search interest rises more than 30% versus 7-day average Exit: Exit after 5 trading days or once spike drops below 10%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'emergency auto repair near me' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Vehicle issues are common and generate frequent search spikes reflecting consumer budget stress.

## Required Keys
- None
