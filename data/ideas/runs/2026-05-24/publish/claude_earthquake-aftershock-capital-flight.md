# Earthquake Aftershock Capital Flight

**Idea ID:** `earthquake-aftershock-capital-flight`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Major earthquake clusters in resource-rich regions trigger short-term supply chain jitters and insurance repricing, creating XLB volatility. Seismic events disrupt mining/logistics in commodity regions; materials sector reprices production and insurance costs.

## Universe
- XLB

## Data Sources
- USGS earthquake activity (magnitude >4.5) daily feed + XLB (materials ETF) price correlation

## Signal Logic
If USGS reports 2+ quakes >4.5 magnitude in resource regions within 48 hours AND XLB closes down >1%

## Entry / Exit
Entry: If USGS reports 2+ quakes >4.5 magnitude in resource regions within 48 hours AND XLB closes down >1% Exit: After 7 trading days or when USGS activity returns to baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity (magnitude >4.5) daily feed + XLB (materials ETF) price correlation via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seismic clusters in active zones occur monthly; threshold captures regional supply shocks.

## Required Keys
- None
