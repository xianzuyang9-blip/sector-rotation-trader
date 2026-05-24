# Credit Market Stress Corporate Spread Widening Alert

**Idea ID:** `credit-market-stress-corporate-spread-widening-alert`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When high-yield spreads widen >50 bps in a single week, it signals credit stress and forces risk-off rotation into financials and staples. Widening credit spreads force financial sector to re-mark loan books; spreads are a leading indicator of economic stress.

## Universe
- XLF

## Data Sources
- FRED series BAMLH0A0HYM2 (HY Corporate OAS) daily

## Signal Logic
If weekly OAS change >+50 bps AND XLF closes below 5-day MA

## Entry / Exit
Entry: If weekly OAS change >+50 bps AND XLF closes below 5-day MA Exit: After 9 trading days or when spreads compress >30 bps intra-period

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series BAMLH0A0HYM2 (HY Corporate OAS) daily via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Credit spreads move daily; weekly thresholds are hit 2–3 times per month during normal volatility.

## Required Keys
- None
