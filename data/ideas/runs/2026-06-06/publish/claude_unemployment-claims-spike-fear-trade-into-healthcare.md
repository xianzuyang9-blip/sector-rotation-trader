# Unemployment Claims Spike Fear Trade Into Healthcare

**Idea ID:** `unemployment-claims-spike-fear-trade-into-healthcare`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly jobless claims spikes above 3-week moving average trigger flight-to-safety rotation into defensive healthcare stocks as investors price recession risk. Healthcare is defensive and non-cyclical; demand spikes during labor market deterioration.

## Universe
- XLV

## Data Sources
- FRED series ICSA (initial claims weekly) via fred_series adapter

## Signal Logic
When weekly initial claims exceed 3-week MA by >12%, enter long XLV and short XLY

## Entry / Exit
Entry: When weekly initial claims exceed 3-week MA by >12%, enter long XLV and short XLY Exit: Exit after 10 trading days or when claims fall back within 5% of 3-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series ICSA (initial claims weekly) via fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weekly claims data is volatile and noisy; 12% spikes above rolling mean occur 2-3 times per quarter.

## Required Keys
- None
