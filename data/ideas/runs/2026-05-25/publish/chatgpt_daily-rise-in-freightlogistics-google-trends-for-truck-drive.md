# Daily Rise In Freightlogistics Google Trends For Truck Driver Shortage Signals Industrial Sector Labor Supply Constraint

**Idea ID:** `daily-rise-in-freightlogistics-google-trends-for-truck-drive`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increasing search interest in truck driver shortage indicates labor supply constraints likely to hurt logistics and industrial throughput. Driver shortages can delay deliveries and increase costs in industrial supply chains.

## Universe
- XLI

## Data Sources
- Google Trends daily search interest

## Signal Logic
If daily Google Trends for 'truck driver shortage' rises 15% above 7-day average

## Entry / Exit
Entry: If daily Google Trends for 'truck driver shortage' rises 15% above 7-day average Exit: After 5 days or when trend drops below 5% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor shortages in trucking frequently spike with economic and regulatory changes.

## Required Keys
- None
