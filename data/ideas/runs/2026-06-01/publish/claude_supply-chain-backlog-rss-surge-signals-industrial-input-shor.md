# Supply Chain Backlog Rss Surge Signals Industrial Input Shortage

**Idea ID:** `supply-chain-backlog-rss-surge-signals-industrial-input-shor`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Supply chain disruptions (fab outages, port strikes, geopolitical shocks) trigger 100-300% daily spikes in logistics news. These precede production delays and industrial margin compression. Industrials face delayed input delivery and margin pressure; construction, automotive, electronics all affected.

## Universe
- XLI

## Data Sources
- RSS news feed counts (major outlets) tracking 'supply chain backlog' + 'semiconductor' OR 'chip' OR 'component' via rss_count adapter

## Signal Logic
If daily RSS count for 'supply chain backlog' OR 'chip shortage' exceeds prior 30-day average by 120% AND count > 40 articles

## Entry / Exit
Entry: If daily RSS count for 'supply chain backlog' OR 'chip shortage' exceeds prior 30-day average by 120% AND count > 40 articles Exit: After 4 weeks or once daily count falls to 70% of prior 30-day baseline for 7 days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts (major outlets) tracking 'supply chain backlog' + 'semiconductor' OR 'chip' OR 'component' via rss_count adapter via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Logistics disruptions spike 8-12 times per year; each generates 120%+ spike lasting 7-21 days.

## Required Keys
- None
