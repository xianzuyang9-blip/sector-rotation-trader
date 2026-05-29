# Weekly Google Trends Surge For Mortgage Refinance Rates Rising

**Idea ID:** `weekly-google-trends-surge-for-mortgage-refinance-rates-risi`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing searches about rising mortgage refinance rates indicate tightening credit conditions affecting housing affordability. Consumer staples may face pressure as tighter credit reduces discretionary consumer spending.

## Universe
- XLP

## Data Sources
- Google Trends weekly search interest for 'mortgage refinance rates rising'

## Signal Logic
Enter short XLP when weekly search interest spikes by more than 25% versus prior week

## Entry / Exit
Entry: Enter short XLP when weekly search interest spikes by more than 25% versus prior week Exit: Exit after 3 weeks or when growth drops below 5%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'mortgage refinance rates rising' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Mortgage rate chatter intensifies several times a year with rate moves and economic data.

## Required Keys
- None
