# Weekly Google Trends Surge In Cold Storage Warehouse Rental Signals Food Supply Chain Tightness

**Idea ID:** `weekly-google-trends-surge-in-cold-storage-warehouse-rental-`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising interest in cold storage rentals suggests tightening food supply chain and inventory management issues. Consumer staples benefit from increased demand for food storage and logistics services.

## Universe
- XLP

## Data Sources
- Google Trends weekly search interest for 'cold storage warehouse rental'

## Signal Logic
If weekly search interest rises 25% above trailing 5-week average

## Entry / Exit
Entry: If weekly search interest rises 25% above trailing 5-week average Exit: After 4 weeks or decline below 10% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'cold storage warehouse rental' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Supply chain issues cause periodic spikes in cold storage rental interest.

## Required Keys
- None
