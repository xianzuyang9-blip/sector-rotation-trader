# Daily Spike In Google Trends For Emergency Childcare Searches Signals Working Parent Stress

**Idea ID:** `daily-spike-in-google-trends-for-emergency-childcare-searche`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden rises in emergency childcare searches indicate working parent stress that can impact labor participation and discretionary spending. Consumer discretionary sectors may be pressured by reduced consumer time and income flexibility.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest

## Signal Logic
If daily search interest for 'emergency childcare' increases by 30% over previous day

## Entry / Exit
Entry: If daily search interest for 'emergency childcare' increases by 30% over previous day Exit: After 7 days or when interest falls below 7-day average

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
- Why It Should Fire Soon: Childcare issues frequently spike due to sudden school closures or illness trends.

## Required Keys
- None
