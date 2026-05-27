# Weekly Google Trends Spike For Food Delivery Delay Complaints Signals Consumer Service Stress

**Idea ID:** `weekly-google-trends-spike-for-food-delivery-delay-complaint`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased complaints about food delivery delays often reflect logistical and consumer stress impacting discretionary spending. Service delays hurt consumer sentiment and reduce demand for discretionary services.

## Universe
- XLY

## Data Sources
- Google Trends weekly data for 'food delivery delay complaints'

## Signal Logic
If weekly Google Trends for 'food delivery delay complaints' rises 50% above prior 8-week average

## Entry / Exit
Entry: If weekly Google Trends for 'food delivery delay complaints' rises 50% above prior 8-week average Exit: After 3 weeks or when trend falls below average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data for 'food delivery delay complaints' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Food delivery complaints spike regularly due to operational hiccups.

## Required Keys
- None
