# Core Pce Inflation Acceleration Crushes Growth Stocks

**Idea ID:** `core-pce-inflation-acceleration-crushes-growth-stocks`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Monthly PCE releases create sharp repricing when inflation surprises above trend. Weekly sampling of FRED data detects momentum shifts 1-2 weeks before major policy reaction. Tech and growth stocks crater on inflation surprises as Fed tightening prospects increase.

## Universe
- XLK

## Data Sources
- FRED series PCEPILFE (Core PCE Inflation) via fred_series adapter

## Signal Logic
If week-over-week PCE momentum (proxied by consecutive daily/weekly FRED updates) accelerates 0.15% or more from prior week AND exceeds 2.5% annualized

## Entry / Exit
Entry: If week-over-week PCE momentum (proxied by consecutive daily/weekly FRED updates) accelerates 0.15% or more from prior week AND exceeds 2.5% annualized Exit: After 4 weeks or once momentum decelerates for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series PCEPILFE (Core PCE Inflation) via fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Monthly PCE prints create momentum swings; each print (12 per year) has 40% odds of surprise above trend.

## Required Keys
- None
