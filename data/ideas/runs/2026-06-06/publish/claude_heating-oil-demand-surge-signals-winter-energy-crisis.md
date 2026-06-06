# Heating Oil Demand Surge Signals Winter Energy Crisis

**Idea ID:** `heating-oil-demand-surge-signals-winter-energy-crisis`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly heating oil prices spike >10% above 6-week moving average during winter months (Nov–Mar), signaling supply constraints or demand surge from cold snap. Energy sector benefits from price spikes driven by heating demand and supply tightness.

## Universe
- XLE

## Data Sources
- FRED series DHHNGSP (heating oil prices weekly) via fred_series adapter

## Signal Logic
During Q4–Q1, if heating oil price > 6-week MA × 1.10, enter long XLE

## Entry / Exit
Entry: During Q4–Q1, if heating oil price > 6-week MA × 1.10, enter long XLE Exit: Exit after 14 trading days or when price falls below 6-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series DHHNGSP (heating oil prices weekly) via fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Winter heating oil spikes are predictable; 10%+ moves occur 2-3 times per winter season.

## Required Keys
- None
