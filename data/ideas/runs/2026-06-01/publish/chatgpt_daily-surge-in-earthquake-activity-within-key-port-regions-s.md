# Daily Surge In Earthquake Activity Within Key Port Regions Signals Freight Logistics Risk And Industrial Caution

**Idea ID:** `daily-surge-in-earthquake-activity-within-key-port-regions-s`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising earthquake activity near ports can disrupt shipping and logistics, pressuring industrial supply chains. Port disruptions due to natural disasters impact industrial production and logistics.

## Universe
- XLI

## Data Sources
- USGS earthquake activity daily counts near major US ports

## Signal Logic
Enter short XLI if daily earthquake counts near ports exceed 2x the 14-day average

## Entry / Exit
Entry: Enter short XLI if daily earthquake counts near ports exceed 2x the 14-day average Exit: Exit after 7 days or when earthquake activity normalizes below 1.2x average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity daily counts near major US ports via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seismic activity near ports fluctuates and can spike due to aftershocks or regional events.

## Required Keys
- None
