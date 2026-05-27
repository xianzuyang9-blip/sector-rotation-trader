# Wheat Corn Price Volatility Spike From Usda Crop Condition Weekly Reports

**Idea ID:** `wheat-corn-price-volatility-spike-from-usda-crop-condition-w`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When USDA crop condition ratings drop >5% week-over-week (indicating drought/pest pressure) or exceed -10% from prior year, commodity prices spike within 2–4 days and agricultural input inflation signals ripple through food supply chains. Consumer staples (food producers) face margin compression from rising agricultural input costs; pricing power is limited.

## Universe
- XLP

## Data Sources
- FRED Wheat Prices (PWHEAMTUSD) + Corn Prices (PMAIZMTUSD) daily, cross-referenced with USDA weekly crop progress reports (HTML scrape)

## Signal Logic
USDA crop condition rating falls >5 points week-over-week AND corn/wheat futures close >2% higher on news day

## Entry / Exit
Entry: USDA crop condition rating falls >5 points week-over-week AND corn/wheat futures close >2% higher on news day Exit: After 12 trading days OR crop conditions stabilize (improve >3 points) for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED Wheat Prices (PWHEAMTUSD) + Corn Prices (PMAIZMTUSD) daily, cross-referenced with USDA weekly crop progress reports (HTML scrape) via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Growing season (May–August) produces crop condition volatility nearly every week; 2–3 rating drops >5 points expected each summer.

## Required Keys
- None
