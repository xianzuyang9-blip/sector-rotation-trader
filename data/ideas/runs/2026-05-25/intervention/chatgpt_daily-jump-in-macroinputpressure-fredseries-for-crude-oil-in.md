# Daily Jump In Macroinputpressure Fredseries For Crude Oil Inventory Change Signals Energy Sector Momentum

**Idea ID:** `daily-jump-in-macroinputpressure-fredseries-for-crude-oil-in`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A sharp drop in crude oil inventories signals tightening supply and potential energy sector price strength. Lower inventories support crude oil price gains benefiting energy stocks.

## Universe
- XLE

## Data Sources
- FRED crude oil inventory weekly data

## Signal Logic
If daily change in crude oil inventory is a decline exceeding 2% compared to prior week

## Entry / Exit
Entry: If daily change in crude oil inventory is a decline exceeding 2% compared to prior week Exit: After 7 trading days or if inventory change reverses to positive

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED crude oil inventory weekly data via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Oil inventory levels fluctuate weekly with regular reporting cycles.

## Required Keys
- None
