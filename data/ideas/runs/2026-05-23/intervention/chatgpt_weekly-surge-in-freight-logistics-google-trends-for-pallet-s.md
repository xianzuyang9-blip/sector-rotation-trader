# Weekly Surge In Freight Logistics Google Trends For Pallet Shortage Signals Industrial Supply Chain Stress

**Idea ID:** `weekly-surge-in-freight-logistics-google-trends-for-pallet-s`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising searches for pallet shortages indicate supply chain bottlenecks that can pressure industrial production and shipping sectors. Industrial sector is sensitive to logistics bottlenecks reducing throughput and margins.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest for 'pallet shortage'

## Signal Logic
Enter short XLI if weekly 'pallet shortage' Google Trends rises more than 15% week-over-week

## Entry / Exit
Entry: Enter short XLI if weekly 'pallet shortage' Google Trends rises more than 15% week-over-week Exit: Exit after 3 weeks or when trend drops below 5% growth week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'pallet shortage' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Supply chain stress signals from Google Trends for pallets are common and spike multiple times per year.

## Required Keys
- None
