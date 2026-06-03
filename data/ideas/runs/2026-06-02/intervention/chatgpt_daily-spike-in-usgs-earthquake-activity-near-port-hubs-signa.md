# Daily Spike In Usgs Earthquake Activity Near Port Hubs Signals Freight Disruption Risk

**Idea ID:** `daily-spike-in-usgs-earthquake-activity-near-port-hubs-signa`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
An increase in earthquake frequency or magnitude near port hubs raises short-term risk of freight delays or rerouting. Industrial and logistics sectors face operational disruption and cost pressure from port delays.

## Universe
- XLI

## Data Sources
- USGS daily earthquake activity near major US ports

## Signal Logic
Enter short XLI if daily count of magnitude 3+ earthquakes near key ports rises by 50%+ vs 7-day average

## Entry / Exit
Entry: Enter short XLI if daily count of magnitude 3+ earthquakes near key ports rises by 50%+ vs 7-day average Exit: Exit after 5 trading days or if quake activity normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS daily earthquake activity near major US ports via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Earthquake activity near ports can cluster episodically causing daily spikes in risk perception.

## Required Keys
- None
