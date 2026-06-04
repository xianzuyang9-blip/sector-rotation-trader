# Weekly Google Trends Surge In Home Office Furniture Sale Signals Consumer Discretionary Bounce

**Idea ID:** `weekly-google-trends-surge-in-home-office-furniture-sale-sig`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising interest in home office furniture sales suggests increased consumer spending on discretionary goods. Consumer discretionary sector benefits from increased spending on home office setups.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'home office furniture sale'

## Signal Logic
If weekly search interest rises 20% above 4-week average

## Entry / Exit
Entry: If weekly search interest rises 20% above 4-week average Exit: After 5 weeks or decline of 10% from peak

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'home office furniture sale' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seasonal and promotional cycles regularly cause spikes in furniture-related searches.

## Required Keys
- None
