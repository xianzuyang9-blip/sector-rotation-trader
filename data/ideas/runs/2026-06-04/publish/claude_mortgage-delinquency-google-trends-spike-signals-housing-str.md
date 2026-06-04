# Mortgage Delinquency Google Trends Spike Signals Housing Stress Rotation

**Idea ID:** `mortgage-delinquency-google-trends-spike-signals-housing-str`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in mortgage-related distress searches often precede housing market weakness and financial sector credit stress, indicating consumer payment difficulty. Financial sector credit quality deteriorates when housing distress spreads; mortgage-backed securities and bank loan portfolios face pressure.

## Universe
- XLF

## Data Sources
- Google Trends weekly search interest for 'mortgage forbearance' and 'late mortgage payment' through google_trends adapter

## Signal Logic
If weekly Google Trends index for mortgage delinquency searches rises 40% or more from prior week, enter short position

## Entry / Exit
Entry: If weekly Google Trends index for mortgage delinquency searches rises 40% or more from prior week, enter short position Exit: Exit after 10 trading days or if search volume returns to baseline (prior 4-week median)

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'mortgage forbearance' and 'late mortgage payment' through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Housing stress and payment anxiety searches spike during economic downturns and rate hikes; historically fires 2-3 times per quarter.

## Required Keys
- None
