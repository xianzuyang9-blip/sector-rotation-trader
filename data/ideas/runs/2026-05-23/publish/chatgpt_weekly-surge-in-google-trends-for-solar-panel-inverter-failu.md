# Weekly Surge In Google Trends For Solar Panel Inverter Failure Signals Bearish Xle

**Idea ID:** `weekly-surge-in-google-trends-for-solar-panel-inverter-failu`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Technical failures in solar equipment indicate stress on renewable energy inputs and potential slowdowns. Energy sector exposure to renewable tech suffers from equipment reliability issues.

## Universe
- XLE

## Data Sources
- Google Trends weekly search interest for 'solar panel inverter failure'

## Signal Logic
Enter short XLE if weekly searches rise by 25% week-over-week

## Entry / Exit
Entry: Enter short XLE if weekly searches rise by 25% week-over-week Exit: Exit after 3 weeks or when growth falls below 10%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'solar panel inverter failure' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Solar panel failure concerns spike seasonally and after weather events.

## Required Keys
- None
