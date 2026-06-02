# Daily Spike In Google Trends For Food Delivery Driver Shortage Signals Discretionary Sector Disruption

**Idea ID:** `daily-spike-in-google-trends-for-food-delivery-driver-shorta`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Spiking searches reflect delivery labor shortages, causing delays and service disruptions impacting consumer discretionary demand. Consumer discretionary companies reliant on delivery face operational challenges and revenue risk.

## Universe
- XLY

## Data Sources
- Google Trends daily searches for 'food delivery driver shortage'

## Signal Logic
Enter short XLY if daily search interest rises 30%+ versus 7-day average

## Entry / Exit
Entry: Enter short XLY if daily search interest rises 30%+ versus 7-day average Exit: Exit after 7 trading days or if interest falls below baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily searches for 'food delivery driver shortage' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor shortages and delivery issues are frequent and reflected in daily search volume surges.

## Required Keys
- None
