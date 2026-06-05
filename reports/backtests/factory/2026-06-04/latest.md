# Professional Backtest V1

- Run date: 2026-06-04
- Window: 2024-01-01 to 2026-06-04
- Slippage: 5.0 bps per trade
- Method: signal after close, execute next trading day open, long/cash only, SPY benchmark.

## Counts

- INSUFFICIENT_ACTIVITY: 1
- LIVE_ONLY_NON_PRICE: 15

## Results

| Algo | Family | Status | Alpha vs SPY | Trades | Reason |
| --- | --- | --- | ---: | ---: | --- |
| Daily Jump In Google Trends For Job Market Reskilling Courses Indicates Labor Market Shift | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Daily Spike In Google Trends For Credit Card Payment Delay Indicates Rising Consumer Financial Stress | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Daily Spike In Google Trends For Emergency Dental Care Indicates Healthcare Consumer Stress | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Daily Surge In Google Trends For Emergency Plumbing Services Signals Home Repair Stress | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Daily Surge In Google Trends For Roadside Assistance Near Me Indicates Consumer Auto Stress | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Ev Charger Installation Acceleration Signals Clean Energy Capex Surge | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.openchargemap |
| Healthcare Cost Search Spike Signals Staples Defensive Rotation | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Port Congestion News Spike Signals Logistics Headwind Reversal Trade | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.rss_count |
| Used Car Price Rally Google Trends Signals Discretionary Demand Rebound | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Utility Sector Relative Strength Reversal After Volatility Crush | crazy | INSUFFICIENT_ACTIVITY | -63.97 | 0 | Backtest completed |
| Warehouse Robotics News Surge Signals Industrial Tech Demand Inflection | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.rss_count |
| Weekly Google Trends Surge In Cold Storage Warehouse Rental Signals Food Supply Chain Tightness | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Google Trends Surge In Electric Truck Orders Signals Industrial Ev Demand Growth | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Google Trends Surge In Home Office Furniture Sale Signals Consumer Discretionary Bounce | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Surge In Google Trends For Last-minute Vacation Rentals Signals Travel Bounce | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Surge In Rss Counts For Port Congestion News Signals Industrial Headwinds | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.rss_count |

This is experimental research, not investment advice. Past performance does not predict future results.
