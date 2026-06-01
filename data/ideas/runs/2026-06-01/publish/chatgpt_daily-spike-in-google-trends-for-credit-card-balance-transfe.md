# Daily Spike In Google Trends For Credit Card Balance Transfer Signals Consumer Financial Stress

**Idea ID:** `daily-spike-in-google-trends-for-credit-card-balance-transfe`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising searches for balance transfers indicate consumers struggling with credit card debt and seeking relief. Consumer financial stress often pressures banks and financials through increased delinquencies.

## Universe
- XLF

## Data Sources
- Google Trends daily search interest for 'credit card balance transfer'

## Signal Logic
Enter short XLF when daily search interest jumps 15% above 7-day average

## Entry / Exit
Entry: Enter short XLF when daily search interest jumps 15% above 7-day average Exit: Exit after 10 trading days or if interest falls below 5% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'credit card balance transfer' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Consumer credit stress indicators spike repeatedly during inflationary periods.

## Required Keys
- None
