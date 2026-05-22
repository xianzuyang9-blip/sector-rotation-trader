# Daily Spike In Local Building Permits Filings Signals Regional Economic Acceleration

**Idea ID:** `daily-spike-in-local-building-permits-filings-signals-region`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A 20%+ daily increase in building permit filings in key metro areas suggests upcoming construction growth. Higher permits indicate future real estate development and construction activity.

## Universe
- XLRE

## Data Sources
- Stable public building permit tables via html_table adapter

## Signal Logic
Enter long XLRE if daily building permits increase > 120% over 7-day average

## Entry / Exit
Entry: Enter long XLRE if daily building permits increase > 120% over 7-day average Exit: Exit after 10 trading days or drop below 110% average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Stable public building permit tables via html_table adapter via scrape (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Building permit data updates frequently and reflects real-time construction demand shifts.

## Required Keys
- None
