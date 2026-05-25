# Daily Spike In Laborjobs Google Trends For Temporary Job Openings Signals Labor Market Tightening And Industrial Strength

**Idea ID:** `daily-spike-in-laborjobs-google-trends-for-temporary-job-ope`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A rise in temporary job openings search interest suggests strong labor demand, often signaling industrial sector growth. Increasing temporary hiring indicates business optimism and production ramp-up.

## Universe
- XLI

## Data Sources
- Google Trends daily search interest

## Signal Logic
If daily Google Trends for 'temporary job openings' increases by more than 15% compared to 7-day average

## Entry / Exit
Entry: If daily Google Trends for 'temporary job openings' increases by more than 15% compared to 7-day average Exit: After 7 days or if trend falls below 5% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor demand search interest spikes often with economic cycles and hiring trends.

## Required Keys
- None
