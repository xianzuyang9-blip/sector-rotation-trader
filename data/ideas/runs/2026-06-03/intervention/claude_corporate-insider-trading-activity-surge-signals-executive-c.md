# Corporate Insider Trading Activity Surge Signals Executive Confidence Shift

**Idea ID:** `corporate-insider-trading-activity-surge-signals-executive-c`
**Family:** `political_insider_filing`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly insider buy-to-sell ratio (by dollar volume) jumps >1.5x the 8-week moving average, executives are signaling confidence, often preceding 4-6 week rallies. Insider buying clusters often precede sector rotation; tech insiders' confidence is especially predictive of broad market risk-on sentiment.

## Universe
- XLK

## Data Sources
- SEC insider trading filings (Form 4) aggregate buy-to-sell ratio weekly through html_table adapter (public SEC Edgar data)

## Signal Logic
If weekly insider buy-to-sell ratio (tech sector) exceeds 8-week moving average by >40% AND exceeds 1.3x baseline

## Entry / Exit
Entry: If weekly insider buy-to-sell ratio (tech sector) exceeds 8-week moving average by >40% AND exceeds 1.3x baseline Exit: After 4 weeks or if ratio drops below 1.0x for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use SEC insider trading filings (Form 4) aggregate buy-to-sell ratio weekly through html_table adapter (public SEC Edgar data) via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Executive trading activity is continuous; clustering occurs monthly, especially around earnings seasons and earnings pre-announcement windows.

## Required Keys
- None
