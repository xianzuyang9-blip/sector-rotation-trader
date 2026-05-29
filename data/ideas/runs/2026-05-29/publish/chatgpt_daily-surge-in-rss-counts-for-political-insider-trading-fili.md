# Daily Surge In Rss Counts For Political Insider Trading Filings

**Idea ID:** `daily-surge-in-rss-counts-for-political-insider-trading-fili`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased filings by political insiders often precede sector rotation or risk repricing based on anticipated policy moves. Financial sector is sensitive to political insider activity hinting at regulatory or policy risk.

## Universe
- XLF

## Data Sources
- RSS news counts of political insider trading filings

## Signal Logic
Enter short XLF when daily RSS count of insider filings rises 40% above 10-day average

## Entry / Exit
Entry: Enter short XLF when daily RSS count of insider filings rises 40% above 10-day average Exit: Exit after 10 trading days or when counts normalize

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news counts of political insider trading filings via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Political insider filings have regular bursts tied to quarterly disclosures and political events.

## Required Keys
- None
