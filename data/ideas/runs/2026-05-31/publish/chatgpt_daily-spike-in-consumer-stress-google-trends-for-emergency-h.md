# Daily Spike In Consumer Stress Google Trends For Emergency Hvac Repair

**Idea ID:** `daily-spike-in-consumer-stress-google-trends-for-emergency-h`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden HVAC repair emergencies reflect seasonal consumer stress and home maintenance urgency. Consumer discretionary and housing-related products see demand lift from urgent repairs.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest for 'emergency HVAC repair'

## Signal Logic
If daily search interest spikes 25% above 14-day average

## Entry / Exit
Entry: If daily search interest spikes 25% above 14-day average Exit: When interest returns to within 10% of average for 3 days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'emergency HVAC repair' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: HVAC emergencies are common, especially with weather changes, producing frequent search spikes.

## Required Keys
- None
