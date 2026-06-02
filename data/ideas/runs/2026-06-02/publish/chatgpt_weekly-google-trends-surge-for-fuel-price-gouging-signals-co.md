# Weekly Google Trends Surge For Fuel Price Gouging Signals Consumer Stress And Energy Sector Volatility

**Idea ID:** `weekly-google-trends-surge-for-fuel-price-gouging-signals-co`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing consumer concern about fuel pricing points to stress around energy costs and potential price volatility. Energy sector faces demand pressure and regulatory risk from consumer backlash on fuel prices.

## Universe
- XLE

## Data Sources
- Google Trends weekly searches for 'fuel price gouging'

## Signal Logic
Enter short XLE if weekly search interest rises 30%+ versus prior week

## Entry / Exit
Entry: Enter short XLE if weekly search interest rises 30%+ versus prior week Exit: Exit after 3 weeks or if searches fall below baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly searches for 'fuel price gouging' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Fuel pricing stress fluctuates with market and geopolitical events, triggering weekly search bursts.

## Required Keys
- None
