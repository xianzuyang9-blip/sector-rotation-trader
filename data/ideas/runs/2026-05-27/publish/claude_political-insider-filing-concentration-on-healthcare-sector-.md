# Political Insider Filing Concentration On Healthcare Sector Signals Regulatory Shift

**Idea ID:** `political-insider-filing-concentration-on-healthcare-sector-`
**Family:** `political_insider_filing`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When healthcare sector insider filings surge >300% on 5-day rolling basis and majority are net SELLS (not buys), congressional committee activity on drug pricing or reimbursement is often imminent; sector volatility follows within 5–10 days. Insider selling in healthcare sector signals anticipation of adverse regulatory action or margin pressure from pricing reform proposals.

## Universe
- XLV

## Data Sources
- SEC Form 4 insider trading filings (daily scrape) filtered by healthcare sector filers; cross-reference with House/Senate committee membership

## Signal Logic
5-day rolling healthcare sector Form 4 count >3x prior 30-day daily average AND net sell % >60%

## Entry / Exit
Entry: 5-day rolling healthcare sector Form 4 count >3x prior 30-day daily average AND net sell % >60% Exit: After 15 trading days OR healthcare insider buying returns to >40% of filings

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use SEC Form 4 insider trading filings (daily scrape) filtered by healthcare sector filers; cross-reference with House/Senate committee membership via scrape (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Congress healthcare committee hearings/votes occur 2–3 times per month; insider selling spikes precede legislative announcements by 3–7 days.

## Required Keys
- None
