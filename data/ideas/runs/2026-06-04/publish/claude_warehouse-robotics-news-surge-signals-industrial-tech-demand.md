# Warehouse Robotics News Surge Signals Industrial Tech Demand Inflection

**Idea ID:** `warehouse-robotics-news-surge-signals-industrial-tech-demand`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Surges in warehouse automation news often coincide with labor shortage announcements and capex acceleration announcements from major logistics firms, signaling near-term industrial tech demand. Warehouse automation news spikes drive technology and industrial equipment valuations higher as investors recognize capex cycles and supply chain modernization acceleration.

## Universe
- XLK

## Data Sources
- RSS news feed count spike for 'warehouse robotics' and 'warehouse automation investment' from industry and tech news through rss_count adapter

## Signal Logic
If weekly RSS count for warehouse robotics news exceeds prior 6-week average by 55%, enter long position

## Entry / Exit
Entry: If weekly RSS count for warehouse robotics news exceeds prior 6-week average by 55%, enter long position Exit: Exit after 10 trading days or if RSS count falls below 6-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed count spike for 'warehouse robotics' and 'warehouse automation investment' from industry and tech news through rss_count adapter via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Automation investment announcements cluster during earnings season and labor reports; fires 2-3 times per quarter as companies announce capex plans.

## Required Keys
- None
