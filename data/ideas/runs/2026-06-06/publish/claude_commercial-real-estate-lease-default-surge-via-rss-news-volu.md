# Commercial Real Estate Lease Default Surge Via Rss News Volume

**Idea ID:** `commercial-real-estate-lease-default-surge-via-rss-news-volu`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Spikes in news mentions of commercial lease defaults or office vacancy above weekly rolling baseline signal distress in the CRE sector, triggering REIT volatility. Default surge news triggers REIT selloffs as dividend safety is questioned and refinancing risk rises.

## Universe
- XLRE

## Data Sources
- RSS feeds (CRE news, REIT blogs, commercial real estate site feeds) via rss_count adapter tracking mentions of 'lease termination', 'commercial property default', 'office vacancy'

## Signal Logic
When daily CRE default mention count > 8-week MA × 1.25, short XLRE and long XLU

## Entry / Exit
Entry: When daily CRE default mention count > 8-week MA × 1.25, short XLRE and long XLU Exit: Exit after 9 trading days or when mention count falls below 8-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feeds (CRE news, REIT blogs, commercial real estate site feeds) via rss_count adapter tracking mentions of 'lease termination', 'commercial property default', 'office vacancy' via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: CRE stress news is recurrent; mention spikes occur monthly in volatile markets.

## Required Keys
- None
