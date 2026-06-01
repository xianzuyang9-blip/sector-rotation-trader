# Weekly Spike In Google Trends For Retail Theft Increase Signals Consumer Discretionary Risk

**Idea ID:** `weekly-spike-in-google-trends-for-retail-theft-increase-sign`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising interest in retail theft increases signals rising shrinkage costs and operational risk for retailers. Higher theft rates pressure margins and profitability in consumer discretionary retail.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'retail theft increase'

## Signal Logic
Enter short XLY if weekly search interest jumps 30% above 8-week average

## Entry / Exit
Entry: Enter short XLY if weekly search interest jumps 30% above 8-week average Exit: Exit after 3 weeks or if interest falls below 15% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'retail theft increase' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Retail theft news and related searches spike frequently due to economic conditions or policy changes.

## Required Keys
- None
