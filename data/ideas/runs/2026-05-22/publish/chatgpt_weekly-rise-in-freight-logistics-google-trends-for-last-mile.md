# Weekly Rise In Freight Logistics Google Trends For Last Mile Delivery Delay Signals Rising Shipping Friction

**Idea ID:** `weekly-rise-in-freight-logistics-google-trends-for-last-mile`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A 20%+ increase in weekly search interest for last-mile delivery delays signals growing logistics bottlenecks. Last-mile delivery issues increase costs and delay shipments, hurting industrial supply chains.

## Universe
- XLI

## Data Sources
- Google Trends weekly data via google_trends adapter

## Signal Logic
Enter short XLI if weekly search interest > 120% prior week

## Entry / Exit
Entry: Enter short XLI if weekly search interest > 120% prior week Exit: Exit after 3 weeks or if interest falls below 110%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Delivery delays surge regularly with labor strikes, weather, or demand spikes.

## Required Keys
- None
