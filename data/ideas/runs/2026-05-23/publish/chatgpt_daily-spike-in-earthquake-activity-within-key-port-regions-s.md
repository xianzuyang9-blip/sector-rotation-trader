# Daily Spike In Earthquake Activity Within Key Port Regions Signals Potential Short-term Xli Disruption

**Idea ID:** `daily-spike-in-earthquake-activity-within-key-port-regions-s`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased seismic activity near ports can disrupt freight logistics and industrial supply chains. Industrial sector is sensitive to shipping and logistics interruptions.

## Universe
- XLI

## Data Sources
- USGS daily earthquake activity near major ports

## Signal Logic
Enter short XLI if daily earthquake count near ports rises 50% above 30-day average

## Entry / Exit
Entry: Enter short XLI if daily earthquake count near ports rises 50% above 30-day average Exit: Exit after 5 days or when earthquake activity normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS daily earthquake activity near major ports via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seismic activity near ports fluctuates and periodically spikes impacting logistics.

## Required Keys
- None
