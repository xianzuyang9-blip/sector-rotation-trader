# Weekly Rise In Fred Series For Crude Oil Inventory Draw Signals Energy Supply Tightening

**Idea ID:** `weekly-rise-in-fred-series-for-crude-oil-inventory-draw-sign`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Inventory draws in crude oil indicate tightening supply and potential price increases. Energy sector benefits from rising oil prices driven by supply constraints.

## Universe
- XLE

## Data Sources
- FRED weekly crude oil inventory data

## Signal Logic
Enter long XLE if weekly crude oil inventory falls by more than 3% WoW

## Entry / Exit
Entry: Enter long XLE if weekly crude oil inventory falls by more than 3% WoW Exit: Exit after 4 weeks or if inventory stabilizes within 1% of baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly crude oil inventory data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Oil inventory fluctuations happen frequently with weekly EIA/FRED reporting.

## Required Keys
- None
