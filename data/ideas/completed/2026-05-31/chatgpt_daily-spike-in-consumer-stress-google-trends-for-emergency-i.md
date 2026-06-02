# Daily Spike In Consumer Stress Google Trends For Emergency Internet Outage

**Idea ID:** `daily-spike-in-consumer-stress-google-trends-for-emergency-i`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Internet outages trigger consumer stress and disrupt ecommerce and communications. Consumer discretionary and tech sectors suffer from sudden connectivity issues.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest for 'emergency internet outage'

## Signal Logic
If daily search interest rises 30% above prior 14-day average

## Entry / Exit
Entry: If daily search interest rises 30% above prior 14-day average Exit: When interest falls below 10% increase for 3 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'emergency internet outage' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Internet outages are frequent and produce noticeable local or regional spikes in search interest.

## Required Keys
- None
