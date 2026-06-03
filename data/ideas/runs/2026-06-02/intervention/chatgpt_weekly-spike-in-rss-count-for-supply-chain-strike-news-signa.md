# Weekly Spike In Rss Count For Supply Chain Strike News Signals Short-term Disruption Risk

**Idea ID:** `weekly-spike-in-rss-count-for-supply-chain-strike-news-signa`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A spike in news about supply chain strikes locally or regionally signals imminent disruptions to manufacturing and distribution. Industrial sector faces margin pressure and operational headwinds from strike-driven supply delays.

## Universe
- XLI

## Data Sources
- RSS feed news count for 'supply chain strike'

## Signal Logic
Enter short XLI if weekly RSS count for 'supply chain strike' doubles versus prior week

## Entry / Exit
Entry: Enter short XLI if weekly RSS count for 'supply chain strike' doubles versus prior week Exit: Exit after 3 weeks or if news counts revert below baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed news count for 'supply chain strike' via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor disputes and strikes flare up episodically, often captured in weekly news volume surges.

## Required Keys
- None
