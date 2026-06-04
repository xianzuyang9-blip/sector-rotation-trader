# Weekly Surge In Google Trends For Home Heating Oil Price Signals Energy Sector Inflation

**Idea ID:** `weekly-surge-in-google-trends-for-home-heating-oil-price-sig`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising consumer interest in heating oil prices reflects increasing energy costs feeding into inflationary pressure. Energy sector benefits from rising input prices driving revenue and margin expansion.

## Universe
- XLE

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly Google Trends for 'home heating oil price' rises 20%+ week-over-week

## Entry / Exit
Entry: If weekly Google Trends for 'home heating oil price' rises 20%+ week-over-week Exit: Exit after 4 weeks or when trend drops below 10% growth

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Energy cost concerns fluctuate seasonally and with geopolitical developments.

## Required Keys
- None
