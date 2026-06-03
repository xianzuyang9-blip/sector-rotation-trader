# Daily Spike In Google Trends For Car Repossession Signals Rising Consumer Financial Distress

**Idea ID:** `daily-spike-in-google-trends-for-car-repossession-signals-ri`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden increases in car repossession searches reflect rising financial distress impacting consumer discretionary demand. Discretionary spending contracts as consumers face repossession risk and cut back on non-essentials.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest

## Signal Logic
If daily Google Trends for 'car repossession' rises 30%+ over 7-day average

## Entry / Exit
Entry: If daily Google Trends for 'car repossession' rises 30%+ over 7-day average Exit: Exit after 10 calendar days or when volume falls below 15% above baseline

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
- Why It Should Fire Soon: Auto loan stress and economic slowdowns often trigger quick search interest spikes.

## Required Keys
- None
