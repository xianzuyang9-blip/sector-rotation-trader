# Daily Spike In Google Trends For Gas Station Cash Only Searches Indicates Consumer Payment Stress

**Idea ID:** `daily-spike-in-google-trends-for-gas-station-cash-only-searc`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden rise in 'cash only' searches at gas stations suggests consumer liquidity stress or payment system disruptions impacting discretionary fuel purchases. Energy sector demand can falter if consumers face payment difficulties or reduce discretionary fuel spending.

## Universe
- XLE

## Data Sources
- Google Trends daily search interest

## Signal Logic
If daily Google Trends for 'gas station cash only' spikes 35% above 7-day average

## Entry / Exit
Entry: If daily Google Trends for 'gas station cash only' spikes 35% above 7-day average Exit: After 7 days or when interest normalizes

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
- Why It Should Fire Soon: Payment issues and consumer stress topics frequently trend sharply due to news or local disruptions.

## Required Keys
- None
