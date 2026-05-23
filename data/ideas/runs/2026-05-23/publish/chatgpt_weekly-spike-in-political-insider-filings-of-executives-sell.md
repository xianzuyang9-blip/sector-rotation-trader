# Weekly Spike In Political Insider Filings Of Executives Selling Xlf Stocks Signals Financial Sector Caution

**Idea ID:** `weekly-spike-in-political-insider-filings-of-executives-sell`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased insider selling in financial sector stocks often precedes sector-wide risk aversion. Executives sell shares when anticipating sector headwinds.

## Universe
- XLF

## Data Sources
- Political insider filings weekly aggregated data

## Signal Logic
Enter short XLF if weekly insider selling volume spikes 30% above 12-week average

## Entry / Exit
Entry: Enter short XLF if weekly insider selling volume spikes 30% above 12-week average Exit: Exit after 4 weeks or when insider selling normalizes below 10% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Political insider filings weekly aggregated data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Insider selling surges in financials regularly appear during market uncertainty.

## Required Keys
- None
