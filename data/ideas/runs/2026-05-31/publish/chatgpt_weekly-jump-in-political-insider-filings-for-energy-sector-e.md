# Weekly Jump In Political Insider Filings For Energy Sector Executives

**Idea ID:** `weekly-jump-in-political-insider-filings-for-energy-sector-e`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased insider sales or buys by energy executives often precede sector moves related to policy shifts or commodity price changes. Executives trade based on non-public information anticipating sector moves.

## Universe
- XLE

## Data Sources
- SEC insider filing database for energy sector executives

## Signal Logic
If total insider buy filings exceed total sells by 30% in a week

## Entry / Exit
Entry: If total insider buy filings exceed total sells by 30% in a week Exit: After 3 weeks or when insider activity normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use SEC insider filing database for energy sector executives via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly insider filing data regularly shows clusters of activity during earnings or policy announcement seasons.

## Required Keys
- None
