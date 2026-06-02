# Weather Extreme Heat Spike Google Trends Signals Utility Demand Surge

**Idea ID:** `weather-extreme-heat-spike-google-trends-signals-utility-dem`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When daily maximum temperatures exceed historical highs for the date AND Google Trends search interest for AC repair spikes, it signals peak utility demand and grid stress. Extreme heat drives peak electricity demand, higher wholesale prices, and margin expansion for utilities.

## Universe
- XLU

## Data Sources
- Open-Meteo API daily maximum temperature combined with Google Trends searches for 'air conditioning repair' and 'cooling center'

## Signal Logic
When daily max temperature exceeds 92°F AND Google Trends 'air conditioning repair' volume exceeds 75th percentile of 30-day history, enter long XLU

## Entry / Exit
Entry: When daily max temperature exceeds 92°F AND Google Trends 'air conditioning repair' volume exceeds 75th percentile of 30-day history, enter long XLU Exit: Exit after 5 trading days or when temperatures fall below 85°F for 2 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo API daily maximum temperature combined with Google Trends searches for 'air conditioning repair' and 'cooling center' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Heat waves and AC repair search spikes occur multiple times during summer months; daily trigger potential is high.

## Required Keys
- None
