# Weekly Rise In Political Insider Filings For Insider Selling In Financial Sector Signals Bearish Xlf

**Idea ID:** `weekly-rise-in-political-insider-filings-for-insider-selling`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased insider selling by political insiders in financial firms often precedes sector weakness. Political insiders may have advanced knowledge of regulatory or economic headwinds affecting banks.

## Universe
- XLF

## Data Sources
- Political insider filings aggregated weekly for financial sector stocks

## Signal Logic
Enter short XLF if weekly insider selling count rises 30% above trailing 8-week average

## Entry / Exit
Entry: Enter short XLF if weekly insider selling count rises 30% above trailing 8-week average Exit: Exit after 4 weeks or if insider selling count drops below 15% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Political insider filings aggregated weekly for financial sector stocks via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Insider selling activity by political figures fluctuates regularly and is reported weekly.

## Required Keys
- None
