# Weekly Jump In Politicalinsiderfiling Submissions For Consumer Discretionary Sector Signals Possible Insider Buying Opportunity

**Idea ID:** `weekly-jump-in-politicalinsiderfiling-submissions-for-consum`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sudden increase in insider buying filings in consumer discretionary stocks suggests confidence in near-term sector strength. Insiders typically buy when expecting positive company or sector performance.

## Universe
- XLY

## Data Sources
- Public insider trading filings weekly

## Signal Logic
If weekly insider buying filings in XLY constituents rise by over 25% WoW

## Entry / Exit
Entry: If weekly insider buying filings in XLY constituents rise by over 25% WoW Exit: After 4 weeks or if filings drop below 10% WoW change

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Public insider trading filings weekly via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Insider filings data updates weekly and insiders trade regularly enough to trigger signal.

## Required Keys
- None
