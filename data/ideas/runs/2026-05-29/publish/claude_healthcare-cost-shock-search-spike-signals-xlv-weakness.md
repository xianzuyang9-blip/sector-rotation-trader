# Healthcare Cost Shock Search Spike Signals Xlv Weakness

**Idea ID:** `healthcare-cost-shock-search-spike-signals-xlv-weakness`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in searches for healthcare cost burden and payment plan alternatives signal consumer financial distress tied to medical expenses, pressuring healthcare stocks as demand for care declines. Rising healthcare cost anxiety precedes declining elective procedure volumes and patient delinquencies in medical billing.

## Universe
- XLV

## Data Sources
- Google Trends weekly search volume for 'high deductible insurance' and 'medical bill payment plans'

## Signal Logic
When weekly Google Trends interest for healthcare cost/payment plan searches exceeds 80th percentile of 52-week distribution

## Entry / Exit
Entry: When weekly Google Trends interest for healthcare cost/payment plan searches exceeds 80th percentile of 52-week distribution Exit: After 3 weeks or when search interest drops below 40th percentile

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'high deductible insurance' and 'medical bill payment plans' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Healthcare cost concerns spike during open enrollment and billing cycle peaks; 80th percentile breaches occur 2–3 times per year.

## Required Keys
- None
