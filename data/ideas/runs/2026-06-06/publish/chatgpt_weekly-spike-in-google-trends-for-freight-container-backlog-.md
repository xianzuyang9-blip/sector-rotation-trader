# Weekly Spike In Google Trends For Freight Container Backlog Signals Industrial Logistics Stress

**Idea ID:** `weekly-spike-in-google-trends-for-freight-container-backlog-`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising interest in freight container backlog indicates worsening supply chain congestion. Industrial sector earnings pressured by logistics bottlenecks and delayed shipments.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter short XLI if weekly Google Trends for 'freight container backlog' rises > 25% WoW

## Entry / Exit
Entry: Enter short XLI if weekly Google Trends for 'freight container backlog' rises > 25% WoW Exit: Exit after 5 weeks or if trend normalizes below 10% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Supply chain issues are persistent and news cycles drive weekly search interest.

## Required Keys
- None
