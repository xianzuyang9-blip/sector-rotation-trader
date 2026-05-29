# Commercial Vehicle Freight Tonnage Collapse Signals Recession Risk

**Idea ID:** `commercial-vehicle-freight-tonnage-collapse-signals-recessio`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sudden 4%+ week-over-week declines in commercial freight activity index forecasts GDP misses and consumer demand weakness 2–3 weeks ahead. Freight collapses precede industrial earnings downgrades and signal deteriorating demand across manufacturing and logistics.

## Universe
- XLI

## Data Sources
- FRED series TOTALSA (Total Vehicle Miles, seasonally adjusted) weekly data

## Signal Logic
When TOTALSA (trucking proxy) drops 4%+ week-over-week and closes below 20-day moving average

## Entry / Exit
Entry: When TOTALSA (trucking proxy) drops 4%+ week-over-week and closes below 20-day moving average Exit: After 4 weeks or if tonnage rebounds 2%+ week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series TOTALSA (Total Vehicle Miles, seasonally adjusted) weekly data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Freight activity is volatile and seasonal; 4% weekly swings occur during demand shocks 3–4 times per year.

## Required Keys
- None
