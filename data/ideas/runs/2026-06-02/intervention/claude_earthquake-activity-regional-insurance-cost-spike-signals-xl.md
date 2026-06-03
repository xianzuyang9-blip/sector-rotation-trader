# Earthquake Activity Regional Insurance Cost Spike Signals Xlv Hospital Demand

**Idea ID:** `earthquake-activity-regional-insurance-cost-spike-signals-xl`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When seismic activity spikes in populated regions and insurance-related news follows, it signals increased hospital demand and healthcare capex; precedes injury and treatment volume surge. Earthquake aftermath drives emergency room visits, orthopedic procedures, and mental health services; bullish for healthcare providers.

## Universe
- XLV

## Data Sources
- USGS Earthquake Activity API daily magnitude ≥4.0 events combined with RSS news for 'earthquake insurance cost'

## Signal Logic
When USGS reports ≥2 magnitude-4+ earthquakes in North America within 7 days AND 'earthquake insurance' RSS count exceeds 3 articles, enter long XLV

## Entry / Exit
Entry: When USGS reports ≥2 magnitude-4+ earthquakes in North America within 7 days AND 'earthquake insurance' RSS count exceeds 3 articles, enter long XLV Exit: Exit after 6 trading days or when magnitude-4+ event frequency returns to baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS Earthquake Activity API daily magnitude ≥4.0 events combined with RSS news for 'earthquake insurance cost' via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Regional earthquake clusters occur several times per quarter; news follow-through is reliable when magnitude >4.0.

## Required Keys
- None
