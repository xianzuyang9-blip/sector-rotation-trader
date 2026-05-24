# Weekly Surge In Political Insider Filings For Buy Transactions Signals Confidence In Financial Sector

**Idea ID:** `weekly-surge-in-political-insider-filings-for-buy-transactio`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased insider buying activity in financial sector stocks often precedes positive sector performance due to informed optimism. Political insiders buying shares suggest confidence in upcoming sector fundamentals.

## Universe
- XLF

## Data Sources
- Political insider trading filings

## Signal Logic
If weekly buy filings in financial sector rise 25% above 8-week average

## Entry / Exit
Entry: If weekly buy filings in financial sector rise 25% above 8-week average Exit: After 6 weeks or if filings drop below baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Political insider trading filings via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Insider buying activity fluctuates regularly with earnings and policy cycles.

## Required Keys
- None
