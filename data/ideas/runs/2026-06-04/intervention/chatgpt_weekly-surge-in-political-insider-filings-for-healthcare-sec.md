# Weekly Surge In Political Insider Filings For Healthcare Sector Executives Buying Stock

**Idea ID:** `weekly-surge-in-political-insider-filings-for-healthcare-sec`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased insider buying suggests confidence in healthcare sector fundamentals or upcoming policy tailwinds. Insider buying often precedes positive sector performance driven by fundamentals or regulation.

## Universe
- XLV

## Data Sources
- Political insider filing counts for healthcare sector executives purchasing stock

## Signal Logic
If weekly insider purchase filings exceed 150% of 12-week average

## Entry / Exit
Entry: If weekly insider purchase filings exceed 150% of 12-week average Exit: After 6 weeks or filings drop below 90% of average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Political insider filing counts for healthcare sector executives purchasing stock via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Insider filing data is released regularly and insider buying surges are common before sector rallies.

## Required Keys
- None
