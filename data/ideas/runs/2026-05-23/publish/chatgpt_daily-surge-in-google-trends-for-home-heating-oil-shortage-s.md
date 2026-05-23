# Daily Surge In Google Trends For Home Heating Oil Shortage Signals Energy Sector Stress

**Idea ID:** `daily-surge-in-google-trends-for-home-heating-oil-shortage-s`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising searches indicate heating fuel supply pressures, often signaling upstream energy cost inflation. Energy sector benefits from supply shortages driving prices higher.

## Universe
- XLE

## Data Sources
- Google Trends daily search interest for 'home heating oil shortage'

## Signal Logic
Enter long XLE if daily searches rise 20% day-over-day

## Entry / Exit
Entry: Enter long XLE if daily searches rise 20% day-over-day Exit: Exit after 7 days or when daily growth falls below 5%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'home heating oil shortage' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Heating oil shortages and supply concerns are seasonal and often spike before winter.

## Required Keys
- None
