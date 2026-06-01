# Daily Jump In Google Trends For Emergency Car Repair Signals Consumer Discretionary Stress Lift

**Idea ID:** `daily-jump-in-google-trends-for-emergency-car-repair-signals`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising emergency car repair searches indicate unexpected consumer expenses, lifting auto service demand. Higher emergency car repair demand benefits auto service and parts companies within consumer discretionary.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest for 'emergency car repair'

## Signal Logic
Enter long XLY if daily search interest jumps 25% above 7-day average

## Entry / Exit
Entry: Enter long XLY if daily search interest jumps 25% above 7-day average Exit: Exit after 10 trading days or if interest falls below 10% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'emergency car repair' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Emergency car repairs spike often with weather or seasonal vehicle issues.

## Required Keys
- None
