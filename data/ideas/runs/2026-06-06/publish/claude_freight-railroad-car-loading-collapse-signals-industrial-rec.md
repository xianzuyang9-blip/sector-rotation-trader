# Freight Railroad Car Loading Collapse Signals Industrial Recession

**Idea ID:** `freight-railroad-car-loading-collapse-signals-industrial-rec`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly railroad carloads decline >5% from prior 8-week average, it signals collapsing industrial shipping demand and forward recession risk. Industrial production, construction, and materials demand all correlate with freight volume; sharp declines precede earnings misses.

## Universe
- XLI

## Data Sources
- FRED series RAILCARLD (railroad carloads weekly) via fred_series adapter

## Signal Logic
When weekly carloads < (8-week MA × 0.95), short XLI and long defensive XLU

## Entry / Exit
Entry: When weekly carloads < (8-week MA × 0.95), short XLI and long defensive XLU Exit: Exit after 12 trading days or when carloads rebound above 8-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series RAILCARLD (railroad carloads weekly) via fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Carload data is weekly and volatile; 5%+ drops from rolling mean occur 1-2 times per quarter.

## Required Keys
- None
