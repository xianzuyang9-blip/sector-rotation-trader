# Political Insider Selling Surge Predicts Market Pullback

**Idea ID:** `political-insider-selling-surge-predicts-market-pullback`
**Family:** `political_insider_filing`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When insider sell volume exceeds buy volume by >4:1 ratio in a single week, company officers are rotating away from equity exposure, signaling private pessimism that precedes broad market weakness by 5–15 days. Technology insiders are most active traders; their selling surge often signals sector-wide confidence loss.

## Universe
- XLK

## Data Sources
- SEC Form 4 filings aggregated by insider transaction type (sell vs. buy) via html_table adapter, weekly count

## Signal Logic
If weekly Form 4 insider sell count to buy count ratio exceeds 4:1, short XLK

## Entry / Exit
Entry: If weekly Form 4 insider sell count to buy count ratio exceeds 4:1, short XLK Exit: After 10 trading days OR if sell-to-buy ratio drops below 2:1

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use SEC Form 4 filings aggregated by insider transaction type (sell vs. buy) via html_table adapter, weekly count via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Insider filing flow is constant; 4:1 ratios appear 4–8 times per quarter, especially around earnings seasons.

## Required Keys
- None
