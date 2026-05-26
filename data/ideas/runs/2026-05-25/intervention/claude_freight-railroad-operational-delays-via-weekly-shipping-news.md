# Freight Railroad Operational Delays Via Weekly Shipping News Volume

**Idea ID:** `freight-railroad-operational-delays-via-weekly-shipping-news`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in railroad delay and operational issue reporting correlate with freight bottlenecks and logistics stress, which historically precedes industrial sector weakness. Industrial companies depend on reliable rail transport; delays signal supply chain friction and near-term margin pressure.

## Universe
- XLI

## Data Sources
- RSS feed counts from railway industry news sources (Progressive Railroading, Railway Age)

## Signal Logic
When weekly RSS count for 'railroad delay' or 'rail congestion' exceeds 90th percentile of trailing 12-week average by >40%

## Entry / Exit
Entry: When weekly RSS count for 'railroad delay' or 'rail congestion' exceeds 90th percentile of trailing 12-week average by >40% Exit: After 10 trading days or when RSS count returns to median

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed counts from railway industry news sources (Progressive Railroading, Railway Age) via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Railroad operational issues are frequent and seasonal; logistics disruptions occur multiple times per quarter, making this a reliable monthly signal.

## Required Keys
- None
