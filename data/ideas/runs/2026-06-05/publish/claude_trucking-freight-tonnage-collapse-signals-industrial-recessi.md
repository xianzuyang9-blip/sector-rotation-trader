# Trucking Freight Tonnage Collapse Signals Industrial Recession

**Idea ID:** `trucking-freight-tonnage-collapse-signals-industrial-recessi`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly trucking tonnage drops >7% from prior month average. Indicates demand contraction in goods movement and industrial activity. Freight collapse signals manufacturing slowdown, inventory destocking, and capex pullback.

## Universe
- XLI

## Data Sources
- FRED series TOTALSA (weekly total tonnage indexed)

## Signal Logic
If TOTALSA < (prior 4-week MA * 0.93), short XLI and long defensive XLP

## Entry / Exit
Entry: If TOTALSA < (prior 4-week MA * 0.93), short XLI and long defensive XLP Exit: After 12 trading days or when TOTALSA recovers above 3-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series TOTALSA (weekly total tonnage indexed) via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Freight tonnage is volatile and seasonal; 7% swings occur 4-6 times annually in normal cycles.

## Required Keys
- None
