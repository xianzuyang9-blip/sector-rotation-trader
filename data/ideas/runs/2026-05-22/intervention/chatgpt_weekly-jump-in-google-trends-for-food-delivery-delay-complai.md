# Weekly Jump In Google Trends For Food Delivery Delay Complaints Signals Consumer Frustration

**Idea ID:** `weekly-jump-in-google-trends-for-food-delivery-delay-complai`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A 20%+ weekly surge in search interest for food delivery delays reflects rising consumer dissatisfaction. Delivery delays hurt consumer staples demand and brand loyalty, pressuring sector performance.

## Universe
- XLP

## Data Sources
- Google Trends weekly data via google_trends adapter

## Signal Logic
Enter short XLP if weekly search interest for food delivery delays rises > 120% of prior week

## Entry / Exit
Entry: Enter short XLP if weekly search interest for food delivery delays rises > 120% of prior week Exit: Exit after 4 weeks or if interest falls below 110%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Food delivery frustration searches spike regularly with service disruptions and labor strikes.

## Required Keys
- None
