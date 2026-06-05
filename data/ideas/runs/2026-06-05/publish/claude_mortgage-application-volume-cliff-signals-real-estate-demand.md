# Mortgage Application Volume Cliff Signals Real Estate Demand Shock

**Idea ID:** `mortgage-application-volume-cliff-signals-real-estate-demand`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly mortgage applications drop >15% week-over-week from recent 4-week average. This signals rapid demand destruction in housing and consumer confidence. Real estate demand implosion directly impacts REITs, construction, and home-building equity values.

## Universe
- XLRE

## Data Sources
- FRED series MMNRNJ (weekly mortgage applications)

## Signal Logic
If MMNRNJ < (4-week MA * 0.85), short XLRE

## Entry / Exit
Entry: If MMNRNJ < (4-week MA * 0.85), short XLRE Exit: Exit after 10 trading days or when MMNRNJ recovers above 4-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series MMNRNJ (weekly mortgage applications) via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Mortgage application volatility is high; 15% drops occur monthly in seasonal and rate-shock cycles.

## Required Keys
- None
