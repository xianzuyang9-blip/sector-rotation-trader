# Hospital Admission Rates Spike Signals Healthcare Spending Urgency

**Idea ID:** `hospital-admission-rates-spike-signals-healthcare-spending-u`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly hospital admissions rise >9% from prior week average. Indicates acute health events or epidemic pressure driving urgent healthcare demand. Healthcare spending spikes with admission urgency; hospitals, pharma, and insurers benefit from elevated utilization.

## Universe
- XLV

## Data Sources
- FRED series HOSPNSA (weekly hospital admissions)

## Signal Logic
If HOSPNSA > (4-week MA * 1.09), long XLV

## Entry / Exit
Entry: If HOSPNSA > (4-week MA * 1.09), long XLV Exit: After 10 trading days or when HOSPNSA drops below 4-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series HOSPNSA (weekly hospital admissions) via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Hospital admissions spike seasonally and on disease outbreaks; 9% jumps occur monthly in flu/RSV seasons.

## Required Keys
- None
