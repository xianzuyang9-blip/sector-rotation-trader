# Weekly Rise In Google Trends For Corporate Bond Downgrade Signals Credit Stress Rotation

**Idea ID:** `weekly-rise-in-google-trends-for-corporate-bond-downgrade-si`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing searches for bond downgrades signal rising credit risk concerns, pressuring financial and industrial sectors. Credit stress lowers financial sector valuations and can ripple to broader cyclical sectors.

## Universe
- XLF

## Data Sources
- Google Trends weekly search interest for 'corporate bond downgrade'

## Signal Logic
If weekly search interest rises more than 20% week-over-week

## Entry / Exit
Entry: If weekly search interest rises more than 20% week-over-week Exit: Exit after 4 weeks or when interest normalizes below 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'corporate bond downgrade' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Bond downgrade news cycles and credit worries recur often in volatile markets.

## Required Keys
- None
