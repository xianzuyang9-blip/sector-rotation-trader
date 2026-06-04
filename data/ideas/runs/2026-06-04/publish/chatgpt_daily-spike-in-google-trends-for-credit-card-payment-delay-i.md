# Daily Spike In Google Trends For Credit Card Payment Delay Indicates Rising Consumer Financial Stress

**Idea ID:** `daily-spike-in-google-trends-for-credit-card-payment-delay-i`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increasing search interest signals consumer cash flow issues and potential credit stress. Financial sector is sensitive to rising consumer credit stress and loan default risk.

## Universe
- XLF

## Data Sources
- Google Trends daily search interest for 'credit card payment delay'

## Signal Logic
If daily search interest exceeds 30% above 10-day moving average

## Entry / Exit
Entry: If daily search interest exceeds 30% above 10-day moving average Exit: After 7 trading days or interest falls below 5-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'credit card payment delay' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Consumer financial stress fluctuates with economic conditions and often shows short-term spikes.

## Required Keys
- None
