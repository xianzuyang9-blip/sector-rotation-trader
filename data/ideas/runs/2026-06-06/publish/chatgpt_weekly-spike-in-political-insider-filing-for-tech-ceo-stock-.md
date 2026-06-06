# Weekly Spike In Political Insider Filing For Tech Ceo Stock Sales Signals Sector Caution

**Idea ID:** `weekly-spike-in-political-insider-filing-for-tech-ceo-stock-`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased insider sales by tech executives signal reduced confidence in near-term technology sector outlook. Tech sector tends to follow insider sentiment on stock sales.

## Universe
- XLK

## Data Sources
- Public political insider filings weekly counts

## Signal Logic
Enter short XLK if weekly insider filing count for tech CEO stock sales doubles WoW

## Entry / Exit
Entry: Enter short XLK if weekly insider filing count for tech CEO stock sales doubles WoW Exit: Exit after 4 weeks or if filings drop below baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Public political insider filings weekly counts via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Insider selling patterns often cluster before earnings or sector rotations.

## Required Keys
- None
