# Google Trends Surge In Bankruptcy Search Terms Signals Consumer Debt Stress

**Idea ID:** `google-trends-surge-in-bankruptcy-search-terms-signals-consu`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in bankruptcy and debt-related searches correlate with consumer financial stress cycles; lead indicator for credit card delinquencies and loan defaults. Banks and financial institutions face rising default risk; credit card issuers and consumer lenders see margin compression.

## Universe
- XLF

## Data Sources
- Google Trends weekly search interest for 'bankruptcy filing' and 'debt consolidation near me'

## Signal Logic
When weekly Google Trends index for 'bankruptcy filing' or 'debt consolidation' exceeds 65 AND increases >15 points week-over-week from prior week

## Entry / Exit
Entry: When weekly Google Trends index for 'bankruptcy filing' or 'debt consolidation' exceeds 65 AND increases >15 points week-over-week from prior week Exit: After 14 trading days or when index falls below 50

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'bankruptcy filing' and 'debt consolidation near me' via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Consumer debt stress searches spike regularly during economic slowdowns and rate hikes; signals occur 2–4 times per year with high consistency.

## Required Keys
- None
