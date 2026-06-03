# Daily Spike In Google Trends For Emergency Plumber Signals Consumer Home Repair Stress

**Idea ID:** `daily-spike-in-google-trends-for-emergency-plumber-signals-c`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden spikes in urgent home repair search terms indicate rising consumer stress and potential discretionary spending shifts. Consumer staples and home improvement sectors often benefit from increased emergency repair demand.

## Universe
- XLP

## Data Sources
- Google Trends daily search interest

## Signal Logic
If daily search volume for 'emergency plumber' rises 25%+ above 7-day average

## Entry / Exit
Entry: If daily search volume for 'emergency plumber' rises 25%+ above 7-day average Exit: Exit after 10 calendar days or when volume normalizes below 10% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weather events and seasonal wear frequently cause plumbing emergencies triggering search spikes.

## Required Keys
- None
