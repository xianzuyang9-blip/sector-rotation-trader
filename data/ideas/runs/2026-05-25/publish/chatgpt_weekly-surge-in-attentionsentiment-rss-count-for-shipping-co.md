# Weekly Surge In Attentionsentiment Rss Count For Shipping Container Backlog Signals Industrial Sector Headwind

**Idea ID:** `weekly-surge-in-attentionsentiment-rss-count-for-shipping-co`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising news mentions of shipping container backlog reflect growing supply chain delays impacting industrial production. Supply chain constraints reduce industrial output and profitability.

## Universe
- XLI

## Data Sources
- RSS feed counts weekly

## Signal Logic
If weekly RSS count for 'shipping container backlog' increases by 30% week-over-week

## Entry / Exit
Entry: If weekly RSS count for 'shipping container backlog' increases by 30% week-over-week Exit: After 4 weeks or when RSS count falls below 10% WoW change

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed counts weekly via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Container backlogs ebb and flow due to port congestion and demand fluctuations.

## Required Keys
- None
