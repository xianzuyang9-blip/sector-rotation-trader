# Daily Surge In Open Charge Map Ev Charger Counts Signals Accelerating Green Infrastructure Demand

**Idea ID:** `daily-surge-in-open-charge-map-ev-charger-counts-signals-acc`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rapid daily growth in EV charger installations points to accelerating clean energy infrastructure buildout. Communication services sector includes companies supporting EV infrastructure and tech services.

## Universe
- XLC

## Data Sources
- Open Charge Map daily EV charger count updates

## Signal Logic
Enter long XLC if daily EV charger count growth exceeds 5% vs 7-day average

## Entry / Exit
Entry: Enter long XLC if daily EV charger count growth exceeds 5% vs 7-day average Exit: Exit after 7 trading days or if growth rate falls below 2%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open Charge Map daily EV charger count updates via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: EV infrastructure installations show daily growth with seasonal and policy-driven bursts.

## Required Keys
- None
