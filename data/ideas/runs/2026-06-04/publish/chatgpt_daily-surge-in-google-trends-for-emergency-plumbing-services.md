# Daily Surge In Google Trends For Emergency Plumbing Services Signals Home Repair Stress

**Idea ID:** `daily-surge-in-google-trends-for-emergency-plumbing-services`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden spikes in emergency plumbing searches indicate rising consumer home stress and urgent repair needs. Increased home repair demand benefits consumer staples and home improvement retailers.

## Universe
- XLP

## Data Sources
- Google Trends daily search interest for 'emergency plumber near me'

## Signal Logic
If daily search interest is 25% above 7-day moving average

## Entry / Exit
Entry: If daily search interest is 25% above 7-day moving average Exit: After 7 days or when interest falls below 5-day moving average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'emergency plumber near me' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Home emergencies frequently cause short-term spikes in local search interest.

## Required Keys
- None
