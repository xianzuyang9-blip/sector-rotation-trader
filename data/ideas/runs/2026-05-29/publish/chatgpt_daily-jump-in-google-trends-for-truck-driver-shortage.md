# Daily Jump In Google Trends For Truck Driver Shortage

**Idea ID:** `daily-jump-in-google-trends-for-truck-driver-shortage`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Spikes in searches about truck driver shortages indicate tightening supply in freight labor affecting logistics. Logistics and industrial companies face higher costs and delays when driver shortages intensify.

## Universe
- XLI

## Data Sources
- Google Trends daily search interest for 'truck driver shortage'

## Signal Logic
Enter short XLI when daily search interest spikes more than 25% compared to 7-day average

## Entry / Exit
Entry: Enter short XLI when daily search interest spikes more than 25% compared to 7-day average Exit: Exit when search interest falls below 10% increase for 3 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'truck driver shortage' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor shortages in trucking frequently generate media and search spikes in volatile conditions.

## Required Keys
- None
