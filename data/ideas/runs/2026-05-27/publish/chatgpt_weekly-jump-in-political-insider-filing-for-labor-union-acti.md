# Weekly Jump In Political Insider Filing For Labor Union Activity Predicts Labor-related Stock Volatility

**Idea ID:** `weekly-jump-in-political-insider-filing-for-labor-union-acti`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Spike in insider filings mentioning labor unions can foreshadow labor disputes or contract negotiations impacting company costs. Labor unrest risks increase operational costs, pressuring financial and industrial stocks.

## Universe
- XLF

## Data Sources
- Political insider filings related to labor unions via public SEC filings

## Signal Logic
If weekly insider filings referencing unions rise more than 40% vs prior 8-week average

## Entry / Exit
Entry: If weekly insider filings referencing unions rise more than 40% vs prior 8-week average Exit: After 4 weeks or when filings normalize below 8-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Political insider filings related to labor unions via public SEC filings via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor filings are periodic and often cluster around contract cycles.

## Required Keys
- None
