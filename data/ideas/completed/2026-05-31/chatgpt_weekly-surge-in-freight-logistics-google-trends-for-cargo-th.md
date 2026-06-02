# Weekly Surge In Freight Logistics Google Trends For Cargo Theft

**Idea ID:** `weekly-surge-in-freight-logistics-google-trends-for-cargo-th`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased cargo theft searches indicate rising supply chain risk and potential insurance claims. Industrial sector vulnerable to supply chain disruptions and logistics cost pressure.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest for 'cargo theft'

## Signal Logic
If weekly cargo theft search interest rises by 15% week-over-week

## Entry / Exit
Entry: If weekly cargo theft search interest rises by 15% week-over-week Exit: When search interest declines or stabilizes for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'cargo theft' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Cargo theft concerns fluctuate with geopolitical and seasonal patterns, causing multiple trend spikes per year.

## Required Keys
- None
