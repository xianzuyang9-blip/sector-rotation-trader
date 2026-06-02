# Cybersecurity Budget Squeeze Google Trends Signals Tech Services Headwind

**Idea ID:** `cybersecurity-budget-squeeze-google-trends-signals-tech-serv`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When searches for enterprise cybersecurity budget and cost concerns spike, it signals CIO cost pressure and deferred IT spending; negative for tech services vendors. Tech services and software companies face reduced enterprise spending when IT budgets come under pressure.

## Universe
- XLK

## Data Sources
- Google Trends weekly search interest for 'enterprise cybersecurity cost' and 'IT security budget'

## Signal Logic
When Google Trends search volume for 'cybersecurity budget' or 'IT security cost' exceeds 75th percentile of 52-week rolling history, enter short XLK

## Entry / Exit
Entry: When Google Trends search volume for 'cybersecurity budget' or 'IT security cost' exceeds 75th percentile of 52-week rolling history, enter short XLK Exit: Exit after 6 trading days or when search volume falls below 55th percentile

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'enterprise cybersecurity cost' and 'IT security budget' via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Budget constraint discussions spike quarterly during earnings season and fiscal planning windows; 2–3 triggers per quarter expected.

## Required Keys
- None
