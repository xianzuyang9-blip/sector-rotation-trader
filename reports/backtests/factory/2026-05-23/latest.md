# Professional Backtest V1

- Run date: 2026-05-23
- Window: 2024-01-01 to 2026-05-23
- Slippage: 5.0 bps per trade
- Method: signal after close, execute next trading day open, long/cash only, SPY benchmark.

## Counts

- INSUFFICIENT_ACTIVITY: 1
- LIVE_ONLY_NON_PRICE: 4

## Results

| Algo | Family | Status | Alpha vs SPY | Trades | Reason |
| --- | --- | --- | ---: | ---: | --- |
| Daily Surge In Google Trends For Home Heating Oil Shortage Signals Energy Sector Stress | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Ev Charger Installation Boom Acceleration Signal | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.openchargemap |
| Healthcare Utilization Surge From Seasonal Illness Wave | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Travel Mobility Rebound Post Weather System | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.weather_series |
| Utilities Volatility Spike Long Hedge Trade | crazy | INSUFFICIENT_ACTIVITY | -62.1 | 0 | Backtest completed |

This is experimental research, not investment advice. Past performance does not predict future results.
