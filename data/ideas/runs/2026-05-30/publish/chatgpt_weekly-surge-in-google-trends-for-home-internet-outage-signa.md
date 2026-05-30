# Weekly Surge In Google Trends For Home Internet Outage Signals Consumer Tech Sector Stress

**Idea ID:** `weekly-surge-in-google-trends-for-home-internet-outage-signa`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising interest in internet outages signals consumer tech infrastructure issues impacting discretionary tech demand. Tech product disruptions reduce consumer spending enthusiasm in technology-related discretionary items.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'home internet outage'

## Signal Logic
If weekly search interest spikes more than 30% week-over-week

## Entry / Exit
Entry: If weekly search interest spikes more than 30% week-over-week Exit: Exit after 3 weeks or when interest falls below 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'home internet outage' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Internet outages are common and frequently searched, often creating weekly spikes.

## Required Keys
- None
