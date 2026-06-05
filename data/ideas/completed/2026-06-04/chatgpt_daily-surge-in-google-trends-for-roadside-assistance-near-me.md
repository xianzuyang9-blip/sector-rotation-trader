# Daily Surge In Google Trends For Roadside Assistance Near Me Indicates Consumer Auto Stress

**Idea ID:** `daily-surge-in-google-trends-for-roadside-assistance-near-me`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden search spikes imply rising car trouble and consumer auto-related stress. Increased demand for auto services supports discretionary auto repair and service companies.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest for 'roadside assistance near me'

## Signal Logic
If daily search interest exceeds 30% above 7-day average

## Entry / Exit
Entry: If daily search interest exceeds 30% above 7-day average Exit: After 7 days or interest falls below 5-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'roadside assistance near me' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Auto troubles and roadside assistance needs cause frequent short-term spikes.

## Required Keys
- None
