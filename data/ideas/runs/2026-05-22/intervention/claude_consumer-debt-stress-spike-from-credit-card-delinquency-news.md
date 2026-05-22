# Consumer Debt Stress Spike From Credit Card Delinquency News Surge

**Idea ID:** `consumer-debt-stress-spike-from-credit-card-delinquency-news`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When daily RSS news mentions of consumer debt stress terms spike >120% above 30-day average, it signals mainstream media focus on household fragility, predicting flight to safety and defensive sector outperformance. Consumer discretionary spending faces headwinds when media highlights rising debt stress; rotation into staples and health care follows within days.

## Universe
- XLY

## Data Sources
- RSS news feed count for terms 'credit card delinquency' + 'loan default' + 'debt burden' via rss_count adapter, daily

## Signal Logic
If daily RSS count for debt stress terms exceeds 30-day MA by >120%, short XLY immediately

## Entry / Exit
Entry: If daily RSS count for debt stress terms exceeds 30-day MA by >120%, short XLY immediately Exit: After 8 trading days OR if RSS count reverts to <110% of 30-day MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed count for terms 'credit card delinquency' + 'loan default' + 'debt burden' via rss_count adapter, daily via scrape (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Consumer financial stress news clusters occur 6–10 times per year; daily RSS feeds capture spikes in real time.

## Required Keys
- None
