# Daily Spike In Consumerstress Google Trends For Unemployment Benefits Application Signals Rising Labor Market Weakness

**Idea ID:** `daily-spike-in-consumerstress-google-trends-for-unemployment`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A jump in searches for unemployment benefits signals increasing job losses and labor market stress. Rising unemployment claims reduce consumer spending and pressure financial sector earnings.

## Universe
- XLF

## Data Sources
- Google Trends daily search interest

## Signal Logic
If daily Google Trends for 'unemployment benefits application' rises over 20% compared to 7-day average

## Entry / Exit
Entry: If daily Google Trends for 'unemployment benefits application' rises over 20% compared to 7-day average Exit: After 7 days or when trend falls below 10% increase

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
- Why It Should Fire Soon: Labor market stress indicators spike regularly with economic shifts.

## Required Keys
- None
