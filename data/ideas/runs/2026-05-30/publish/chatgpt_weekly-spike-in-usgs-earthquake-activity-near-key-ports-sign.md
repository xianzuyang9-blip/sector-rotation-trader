# Weekly Spike In Usgs Earthquake Activity Near Key Ports Signals Supply Chain Risk In Industrials

**Idea ID:** `weekly-spike-in-usgs-earthquake-activity-near-key-ports-sign`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An increase in seismic activity near ports can disrupt shipping and logistics operations, causing supply chain interruptions. Supply chain disruptions reduce industrial efficiency and can depress industrial sector performance.

## Universe
- XLI

## Data Sources
- USGS earthquake activity near major US ports

## Signal Logic
If weekly earthquake count in 50km radius around major ports rises by 50% week-over-week

## Entry / Exit
Entry: If weekly earthquake count in 50km radius around major ports rises by 50% week-over-week Exit: Exit after 3 weeks or when earthquake activity normalizes below 2-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity near major US ports via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Earthquake activity near ports fluctuates seasonally and sporadically, often triggering short-term alerts.

## Required Keys
- None
