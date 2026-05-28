# Weekly Surge In Google Trends For Last-mile Delivery Delay Complaints Signals E-commerce Stress

**Idea ID:** `weekly-surge-in-google-trends-for-last-mile-delivery-delay-c`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Consumers increasingly complain about last-mile delivery delays, indicating e-commerce stress and potential order cancellations. Rising delivery complaints foreshadow weakening consumer discretionary spending in e-commerce reliant sectors.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'last mile delivery delay'

## Signal Logic
If weekly Google Trends interest for 'last mile delivery delay' rises more than 25% WoW

## Entry / Exit
Entry: If weekly Google Trends interest for 'last mile delivery delay' rises more than 25% WoW Exit: When interest drops below 10% WoW increase for two consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'last mile delivery delay' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Delivery delays frequently spike seasonally or due to macro shocks, causing weekly search interest jumps.

## Required Keys
- None
