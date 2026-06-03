# Gasoline Price Spike Triggers Commuter Stress Google Trends

**Idea ID:** `gasoline-price-spike-triggers-commuter-stress-google-trends`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When retail gasoline prices jump >10% week-over-week, consumer search volume for gas price comparisons and budget fuel options spikes within 3-5 days, signaling discretionary spending compression. Sharp fuel cost shocks reduce discretionary purchasing power and trigger rotation away from consumer discretionary toward staples.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'gas prices near me' and 'cheap gas' through google_trends adapter

## Signal Logic
If weekly Google Trends 'gas prices near me' search volume rises >40% week-over-week AND gasoline futures are up >8% in the same week

## Entry / Exit
Entry: If weekly Google Trends 'gas prices near me' search volume rises >40% week-over-week AND gasoline futures are up >8% in the same week Exit: After 2 weeks or if gas price volatility drops below 3% weekly change

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'gas prices near me' and 'cheap gas' through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal fuel price volatility and refinery disruptions occur multiple times per year, triggering search spikes consistently.

## Required Keys
- None
