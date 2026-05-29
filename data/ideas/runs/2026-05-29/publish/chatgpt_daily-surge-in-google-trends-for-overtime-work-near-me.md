# Daily Surge In Google Trends For Overtime Work Near Me

**Idea ID:** `daily-surge-in-google-trends-for-overtime-work-near-me`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Spikes in overtime work searches suggest labor shortages and rising wage pressure in certain sectors. Industrial companies may face margin pressure from increased labor costs and capacity constraints.

## Universe
- XLI

## Data Sources
- Google Trends daily search interest for 'overtime work near me'

## Signal Logic
Enter short XLI when daily search interest rises more than 25% vs 7-day average

## Entry / Exit
Entry: Enter short XLI when daily search interest rises more than 25% vs 7-day average Exit: Exit after 5 trading days or when spike falls below 10%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'overtime work near me' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor market tightness and overtime demand often produce frequent search spikes.

## Required Keys
- None
