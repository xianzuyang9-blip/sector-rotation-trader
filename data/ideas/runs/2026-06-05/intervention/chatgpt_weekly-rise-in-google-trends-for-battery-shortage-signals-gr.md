# Weekly Rise In Google Trends For Battery Shortage Signals Green Energy Supply Chain Stress

**Idea ID:** `weekly-rise-in-google-trends-for-battery-shortage-signals-gr`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Spikes in battery shortage searches reflect supply chain constraints in green energy sectors. Energy sector, especially renewables, faces input cost and supply risks, pressuring prices.

## Universe
- XLE

## Data Sources
- Google Trends weekly search interest for 'battery shortage'

## Signal Logic
Enter short XLE when weekly search interest rises 25% week-over-week

## Entry / Exit
Entry: Enter short XLE when weekly search interest rises 25% week-over-week Exit: Exit after 5 weeks or when growth drops below 10%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'battery shortage' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Supply chain concerns and shortages produce regular attention spikes, triggering frequent signals.

## Required Keys
- None
