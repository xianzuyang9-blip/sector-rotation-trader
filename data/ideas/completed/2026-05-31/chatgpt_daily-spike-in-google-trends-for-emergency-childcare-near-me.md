# Daily Spike In Google Trends For Emergency Childcare Near Me

**Idea ID:** `daily-spike-in-google-trends-for-emergency-childcare-near-me`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden childcare emergencies signal rising family stress and short-term labor participation disruption. Consumer discretionary sensitive to labor supply shocks and consumer stress.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest for 'emergency childcare near me'

## Signal Logic
If daily search volume spikes above 20% of 30-day average

## Entry / Exit
Entry: If daily search volume spikes above 20% of 30-day average Exit: When daily search volume drops below 10% above 30-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'emergency childcare near me' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Childcare emergencies are frequent and seasonal, producing multiple spikes annually.

## Required Keys
- None
