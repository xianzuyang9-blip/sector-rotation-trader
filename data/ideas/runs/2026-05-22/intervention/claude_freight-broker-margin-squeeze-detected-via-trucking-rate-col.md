# Freight Broker Margin Squeeze Detected Via Trucking Rate Collapse

**Idea ID:** `freight-broker-margin-squeeze-detected-via-trucking-rate-col`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When trucking freight rates fall sharply week-over-week, logistics companies face margin compression and often announce guidance cuts within days, triggering sector rotation. Industrial sector includes transport and logistics operators whose profitability is directly tied to freight rate spreads.

## Universe
- XLI

## Data Sources
- FRED series TRUCKFRT (Trucking Services Index) weekly frequency

## Signal Logic
If TRUCKFRT weekly value drops >3% from prior week AND 10-week moving average is still positive, short XLI

## Entry / Exit
Entry: If TRUCKFRT weekly value drops >3% from prior week AND 10-week moving average is still positive, short XLI Exit: After 10 trading days OR if TRUCKFRT rebounds >2% over 2 weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series TRUCKFRT (Trucking Services Index) weekly frequency via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weekly FRED data refreshes reliably; freight rate volatility produces 3%+ swings multiple times per quarter, especially around demand shocks.

## Required Keys
- None
