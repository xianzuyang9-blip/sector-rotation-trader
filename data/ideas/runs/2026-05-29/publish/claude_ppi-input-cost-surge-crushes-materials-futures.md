# Ppi Input Cost Surge Crushes Materials Futures

**Idea ID:** `ppi-input-cost-surge-crushes-materials-futures`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly PPI commodity surges exceeding 2% signal sudden input cost inflation, typically followed by 1–2 week margin compression in materials and basic industries. Raw material cost shocks compress margins in cyclical materials before prices can be passed through to customers.

## Universe
- XLB

## Data Sources
- FRED series PPIACO (PPI: All Commodities) weekly data

## Signal Logic
When PPIACO rises 2%+ week-over-week and closes above 30-day moving average

## Entry / Exit
Entry: When PPIACO rises 2%+ week-over-week and closes above 30-day moving average Exit: After 2 weeks or if PPI falls 1%+ week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series PPIACO (PPI: All Commodities) weekly data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: PPI volatility is high; 2% weekly swings occur 4–6 times per year, especially during supply shocks.

## Required Keys
- None
