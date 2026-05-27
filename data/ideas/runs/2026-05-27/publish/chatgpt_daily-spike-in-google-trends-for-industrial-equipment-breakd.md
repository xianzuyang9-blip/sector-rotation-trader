# Daily Spike In Google Trends For Industrial Equipment Breakdown Signals Supply Chain Disruption

**Idea ID:** `daily-spike-in-google-trends-for-industrial-equipment-breakd`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased search interest in equipment failures often signals upcoming logistics slowdowns and industrial sector stress. Industrial equipment problems can disrupt supply chains, weighing on industrial sector earnings.

## Universe
- XLI

## Data Sources
- Google Trends daily data for 'industrial equipment breakdown'

## Signal Logic
If daily Google Trends for 'industrial equipment breakdown' spikes 50% above 10-day average

## Entry / Exit
Entry: If daily Google Trends for 'industrial equipment breakdown' spikes 50% above 10-day average Exit: After 7 trading days or when the trend returns below 10-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily data for 'industrial equipment breakdown' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Industrial disruptions are common and often prompt search spikes.

## Required Keys
- None
