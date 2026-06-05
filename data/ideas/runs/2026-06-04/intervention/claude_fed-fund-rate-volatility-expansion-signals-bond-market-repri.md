# Fed Fund Rate Volatility Expansion Signals Bond Market Repricing

**Idea ID:** `fed-fund-rate-volatility-expansion-signals-bond-market-repri`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Rapid expansions in Fed funds rate volatility (realized vol spike) often precede sharp bond yield moves and flight-to-safety rotations in equity markets. Fed rate volatility increases cost of capital and disrupts borrowing conditions; discretionary sectors face compression as duration risk reprices sharply.

## Universe
- XLY

## Data Sources
- FRED effective federal funds rate (FEDFUNDS) daily close and 20-day realized volatility through fred_series adapter

## Signal Logic
If 20-day realized volatility of FEDFUNDS rises 30% above prior 60-day median, enter short position in XLY

## Entry / Exit
Entry: If 20-day realized volatility of FEDFUNDS rises 30% above prior 60-day median, enter short position in XLY Exit: Exit after 6 trading days or if volatility returns to 60-day median

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED effective federal funds rate (FEDFUNDS) daily close and 20-day realized volatility through fred_series adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Fed funds volatility spikes frequently during policy uncertainty and inflation data releases; fires 1-2 times per week consistently.

## Required Keys
- None
