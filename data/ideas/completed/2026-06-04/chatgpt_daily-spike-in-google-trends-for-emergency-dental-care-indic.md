# Daily Spike In Google Trends For Emergency Dental Care Indicates Healthcare Consumer Stress

**Idea ID:** `daily-spike-in-google-trends-for-emergency-dental-care-indic`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden increases in emergency dental care searches reflect urgent healthcare needs and consumer stress. Higher urgent care demand boosts healthcare sector revenues and service utilization.

## Universe
- XLV

## Data Sources
- Google Trends daily search interest for 'emergency dental care'

## Signal Logic
If daily search interest is 20% above 7-day average

## Entry / Exit
Entry: If daily search interest is 20% above 7-day average Exit: After 10 days or when interest reverts below 5-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'emergency dental care' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Healthcare consumer stress is a persistent factor with frequent short-term spikes.

## Required Keys
- None
