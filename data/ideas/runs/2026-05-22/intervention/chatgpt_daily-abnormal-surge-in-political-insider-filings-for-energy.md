# Daily Abnormal Surge In Political Insider Filings For Energy Sector Execs

**Idea ID:** `daily-abnormal-surge-in-political-insider-filings-for-energy`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A 50%+ daily increase in insider sell filings by energy sector executives may indicate negative near-term sentiment. Insider selling often signals executives' concerns about upcoming sector headwinds.

## Universe
- XLE

## Data Sources
- Public filings scrape via political_insider_filing adapter

## Signal Logic
Enter short XLE if daily insider sell filings exceed 150% of 30-day average

## Entry / Exit
Entry: Enter short XLE if daily insider sell filings exceed 150% of 30-day average Exit: Exit after 7 trading days or filings normalize below 120%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Public filings scrape via political_insider_filing adapter via scrape (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Insider filings data updates daily and can spike on sector-specific news or regulatory concerns.

## Required Keys
- None
