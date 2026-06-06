# Corporate Bond Spread Widening Signals Credit Stress Rotation

**Idea ID:** `corporate-bond-spread-widening-signals-credit-stress-rotatio`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When high-yield bond OAS widens >50bp in a single week above 4-week moving average, it signals deteriorating credit conditions and recession expectations. Widening credit spreads increase bank loss provisions and reduce lending capacity; financial sector underperforms.

## Universe
- XLF

## Data Sources
- FRED series BAMLH0A0HYM2 (HY OAS) and BAMLC0A1CMBBBEY (BBB OAS) via fred_series adapter

## Signal Logic
When weekly HY OAS increase > 50bp and close > 4-week MA + 25bp, short XLF and long XLV

## Entry / Exit
Entry: When weekly HY OAS increase > 50bp and close > 4-week MA + 25bp, short XLF and long XLV Exit: Exit after 11 trading days or when OAS tightens back below 4-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series BAMLH0A0HYM2 (HY OAS) and BAMLC0A1CMBBBEY (BBB OAS) via fred_series adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Credit spreads widen sharply 2-3 times per quarter during volatility episodes; 50bp+ moves are frequent.

## Required Keys
- None
