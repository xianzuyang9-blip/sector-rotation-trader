# Daily Spike In Google Trends For Food Delivery Delays Signals Consumer Staples Disruption

**Idea ID:** `daily-spike-in-google-trends-for-food-delivery-delays-signal`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising searches for food delivery delays reveal logistical stress impacting consumer staples availability. Delivery delays can reduce sales and margins in consumer staples companies reliant on just-in-time inventory.

## Universe
- XLP

## Data Sources
- Google Trends daily search interest for 'food delivery delays'

## Signal Logic
Enter short XLP if daily search interest jumps 20% above 7-day average

## Entry / Exit
Entry: Enter short XLP if daily search interest jumps 20% above 7-day average Exit: Exit after 7 trading days or if interest falls below 5% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'food delivery delays' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Food delivery disruptions are common and sensitive to weather, labor, and supply chain factors.

## Required Keys
- None
