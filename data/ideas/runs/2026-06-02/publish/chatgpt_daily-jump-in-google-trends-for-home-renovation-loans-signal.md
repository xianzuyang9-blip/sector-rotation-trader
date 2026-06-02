# Daily Jump In Google Trends For Home Renovation Loans Signals Consumer Stress Turning To Housing Sector Demand

**Idea ID:** `daily-jump-in-google-trends-for-home-renovation-loans-signal`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A sudden surge in searches for renovation loans suggests increased consumer stress but also potential lift in home improvement demand. Consumer discretionary sector, especially home improvement retailers, benefit from renewed renovation spending.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest for 'home renovation loans'

## Signal Logic
Enter long XLY if daily search interest jumps 30%+ versus 7-day average

## Entry / Exit
Entry: Enter long XLY if daily search interest jumps 30%+ versus 7-day average Exit: Exit after 10 trading days or if search interest falls below 7-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'home renovation loans' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Consumer stress related to housing finance fluctuates frequently, triggering daily search bursts.

## Required Keys
- None
