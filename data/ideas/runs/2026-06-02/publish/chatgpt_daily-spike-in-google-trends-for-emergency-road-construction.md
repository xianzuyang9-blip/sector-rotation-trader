# Daily Spike In Google Trends For Emergency Road Construction Signals Local Infrastructure Strain

**Idea ID:** `daily-spike-in-google-trends-for-emergency-road-construction`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden daily increases in searches suggest unexpected infrastructure repairs causing local traffic and transport disruptions. Industrial and transport sectors face delays and increased costs from local infrastructure issues.

## Universe
- XLI

## Data Sources
- Google Trends daily search interest for 'emergency road construction'

## Signal Logic
Enter short XLI if daily search interest rises 30%+ vs 7-day average

## Entry / Exit
Entry: Enter short XLI if daily search interest rises 30%+ vs 7-day average Exit: Exit after 7 trading days or if search interest falls below baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'emergency road construction' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Infrastructure issues and emergency road works are common and trigger frequent daily search spikes.

## Required Keys
- None
