# Earthquake Swarm Aftershock Insurance Building Stock Volatility

**Idea ID:** `earthquake-swarm-aftershock-insurance-building-stock-volatil`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When a magnitude 5.0+ earthquake occurs or a swarm of 10+ events in 3 days triggers aftershock warnings, construction/materials stocks (XLB, XLRE) and insurance-linked instruments see demand spikes as repairs and building inspections accelerate. Materials demand rises from emergency repairs; construction and building materials experience near-term demand boost.

## Universe
- XLB

## Data Sources
- USGS earthquake_activity API tracking daily seismic events magnitude >3.5 in populated US zones (California, Pacific Northwest)

## Signal Logic
If USGS reports magnitude 5.0+ quake OR 10+ events magnitude >3.5 in 3-day window in California/PNW, enter long XLB

## Entry / Exit
Entry: If USGS reports magnitude 5.0+ quake OR 10+ events magnitude >3.5 in 3-day window in California/PNW, enter long XLB Exit: Exit after 10 trading days or when aftershock warning expires

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake_activity API tracking daily seismic events magnitude >3.5 in populated US zones (California, Pacific Northwest) via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: California and Pacific Northwest experience multiple notable seismic events per year; swarms fire several times annually.

## Required Keys
- None
