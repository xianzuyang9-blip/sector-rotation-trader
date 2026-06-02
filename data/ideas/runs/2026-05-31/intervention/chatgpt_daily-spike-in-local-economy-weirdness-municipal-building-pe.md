# Daily Spike In Local Economy Weirdness Municipal Building Permit Complaints

**Idea ID:** `daily-spike-in-local-economy-weirdness-municipal-building-pe`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden increases in permit complaints signal local construction delays and economic friction. Real estate development slows amid rising bureaucratic or compliance hurdles.

## Universe
- XLRE

## Data Sources
- City stable public tables on building permit complaints

## Signal Logic
If daily complaint counts exceed 150% of 30-day average

## Entry / Exit
Entry: If daily complaint counts exceed 150% of 30-day average Exit: When complaint counts return to below 110% of average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use City stable public tables on building permit complaints via scrape (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Local complaints surge often due to weather or policy changes, creating repeatable signals.

## Required Keys
- None
