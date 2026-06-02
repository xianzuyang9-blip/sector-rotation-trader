# Container Port Backlog Rss Surge Signals Industrial Demand Weakness

**Idea ID:** `container-port-backlog-rss-surge-signals-industrial-demand-w`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When news about port congestion and container backlogs spike, it signals reduced import velocity and weak industrial demand; counterintuitive to old supply-chain headlines. Port backlog reduction signals lower demand for goods and industrial equipment; negative for industrial cyclicals.

## Universe
- XLI

## Data Sources
- RSS news feed count for 'port congestion', 'container backlog', and 'shipping delay' announcements

## Signal Logic
When daily RSS article count for 'container backlog' or 'port congestion' exceeds 4 articles and is above 85th percentile of 30-day rolling history, enter short XLI

## Entry / Exit
Entry: When daily RSS article count for 'container backlog' or 'port congestion' exceeds 4 articles and is above 85th percentile of 30-day rolling history, enter short XLI Exit: Exit after 5 trading days or when article count falls below 2 for 2 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed count for 'port congestion', 'container backlog', and 'shipping delay' announcements via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Port and logistics news spikes 2–4 times per week during seasonal demand swings and geopolitical disruptions.

## Required Keys
- None
