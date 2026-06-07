# Daily Spike In Earthquake Activity Near Critical Ports Signals Short-term Freight Logistics Disruption

**Idea ID:** `daily-spike-in-earthquake-activity-near-critical-ports-signa`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased seismic activity near major ports can cause temporary disruption in freight logistics. Port disruptions impact industrial supply chains and logistics throughput negatively.

## Universe
- XLI

## Data Sources
- USGS earthquake activity daily data

## Signal Logic
If daily earthquake count near top 5 US ports rises 50% above 30-day average

## Entry / Exit
Entry: If daily earthquake count near top 5 US ports rises 50% above 30-day average Exit: When quake counts return below 10% above 30-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity daily data via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Earthquake activity near ports fluctuates regularly causing intermittent logistics risks.

## Required Keys
- None
