# Daily Jump In Google Trends For Diy Home Repair Signals Consumer Discretionary Caution

**Idea ID:** `daily-jump-in-google-trends-for-diy-home-repair-signals-cons`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising DIY home repair searches reflect consumers delaying professional services, indicating tightening budgets and stress. Increased DIY searches signal consumer cost-cutting and reduced discretionary spending on services.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest for 'DIY home repair'

## Signal Logic
Enter short XLY if daily search interest jumps more than 20% vs 7-day moving average

## Entry / Exit
Entry: Enter short XLY if daily search interest jumps more than 20% vs 7-day moving average Exit: Exit after 7 days or when search interest falls below 10% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'DIY home repair' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Consumer stress indicators with DIY spikes occur frequently during economic uncertainty.

## Required Keys
- None
