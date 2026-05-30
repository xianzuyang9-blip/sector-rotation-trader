# Daily Spike In Google Trends For Solar Panel Repair Signals Renewable Energy Sector Bounce

**Idea ID:** `daily-spike-in-google-trends-for-solar-panel-repair-signals-`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Growing search interest in solar panel repair signals rising adoption and maintenance demand in renewable energy sector. Maintenance demand supports renewable energy firms and related energy technology providers.

## Universe
- XLE

## Data Sources
- Google Trends daily search interest for 'solar panel repair'

## Signal Logic
If daily searches increase more than 25% compared to 7-day average

## Entry / Exit
Entry: If daily searches increase more than 25% compared to 7-day average Exit: Exit after 5 trading days or when searches revert below 7-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'solar panel repair' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Solar tech issues and maintenance searches spike with weather and seasonal changes.

## Required Keys
- None
