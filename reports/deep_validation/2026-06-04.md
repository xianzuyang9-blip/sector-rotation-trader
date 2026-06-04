# Deep Validation Report - 2026-06-04

## Definitions
- force_rank: Full-window/since-seed rank from data/rank_history.csv. Use for long-term trust, promotion, demotion, and kill review.
- rolling_30d: Recent trailing 30-day return rank from docs/leaderboards/rolling_30d.json. Use for tactical spotlight and recent momentum.
- sector_consensus: Precomputed sector verdicts from docs/signals/index.json. Use for current directional sector context.

## System State
- Force-ranked algos: 403 rows (403 unique algo_ids)
- Force-ranked beating SPY: 1 of 403 rows
- Rolling 30D algos: 404 rows (404 unique algo_ids)
- Rolling 30D beating SPY: 3 of 404 rows
- Signals generated: 403
- Tickers covered: 105
- Sectors computed: 11

## Data Hygiene
- Force-rank duplicate rows: 0
- Rolling 30D duplicate rows: 0
- Rolling-only algo_ids with no force-rank row: 1

## Force Rank
Full-window/since-seed rank; not the same as recent 30D performance.

### Top 10
| Rank | Algo | Type | Return | Alpha vs SPY | Rank Change |
| --- | --- | --- | --- | --- | --- |
| 1 | Quantified Simple Monthly Rotation | normal | +13.68% | +2.56% | +0 |
| 2 | Algo Baileymol (Chaos Monger) | normal | +8.16% | -2.96% | +0 |
| 3 | Antonacci Dual Momentum Sector Rotation | normal | +7.38% | -3.74% | +0 |
| 4 | Faber Momentum Rotation | normal | +5.49% | -5.63% | +0 |
| 5 | Retail Sales Momentum | crazy | +4.50% | -6.62% | +0 |
| 6 | Job Posting Acceleration | crazy | +3.21% | -7.91% | +0 |
| 7 | Uber Mobility Index | crazy | +2.43% | -8.69% | +1 |
| 8 | Housing Permit Velocity | crazy | +2.22% | -8.90% | +1 |
| 9 | VIX Term Structure | crazy | +1.87% | -9.25% | -2 |
| 10 | High Yield Spread Regime | crazy | +1.18% | -9.95% | +123 |

### Bottom 5
| Rank | Algo | Type | Return | Alpha vs SPY | Rank Change |
| --- | --- | --- | --- | --- | --- |
| 399 | Consumer Sentiment | crazy | -2.29% | -13.41% | -18 |
| 400 | FINRA Dark Pool Signal | crazy | -2.57% | -13.70% | -18 |
| 401 | Liquor Store Leading Indicator | crazy | -2.99% | -14.11% | -18 |
| 402 | Chaos Rotation Lab | crazy | -6.23% | -17.35% | -18 |
| 403 | Electricity Consumption | crazy | -6.61% | -17.74% | -18 |

## Rolling 30D
Trailing 30-day return rank; useful for recent momentum and tactical spotlight.
SPY 30D: +4.60%

| Rank | Algo | Category | 30D Return | 30D vs SPY |
| --- | --- | --- | --- | --- |
| 1 | Quantified Simple Monthly Rotation | standard | +9.49% | +4.88% |
| 2 | VIX Fear Rotation | crazy | +6.55% | +1.95% |
| 3 | VIX Term Structure | crazy | +6.53% | +1.93% |
| 4 | Job Posting Acceleration | crazy | +3.23% | -1.37% |
| 5 | Retail Sales Momentum | crazy | +2.97% | -1.63% |
| 6 | Antonacci Dual Momentum Sector Rotation | standard | +2.70% | -1.91% |
| 7 | NRWise Acceleration | standard | +2.24% | -2.36% |
| 8 | Housing Permit Velocity | crazy | +1.69% | -2.91% |
| 9 | High Yield Spread Regime | crazy | +1.18% | -3.43% |
| 10 | Freight Rail Carloads | crazy | +0.99% | -3.61% |

## Sector Consensus
- Top Bullish: XLK, XLU, XLI
- Top Bearish: XLC, XLV, XLRE

| ETF | Sector | Composite | Label | Bullish % |
| --- | --- | --- | --- | --- |
| XLK | Technology | 14 of 49 | BEARISH | 29% |
| XLU | Utilities | 12 of 57 | BEARISH | 21% |
| XLI | Industrials | 13 of 70 | BEARISH | 19% |
| XLP | Consumer Defensive | 9 of 55 | BEARISH | 16% |
| XLY | Consumer Cyclical | 13 of 85 | BEARISH | 15% |
| XLB | Basic Materials | 7 of 51 | BEARISH | 14% |
| XLE | Energy | 5 of 51 | BEARISH | 10% |
| XLF | Financial Services | 4 of 52 | BEARISH | 8% |
| XLC | Communication Services | 2 of 47 | BEARISH | 4% |
| XLV | Healthcare | 1 of 53 | BEARISH | 2% |
| XLRE | Real Estate | 1 of 47 | BEARISH | 2% |

## Content Facts
- Signal of day: Quantified Simple Monthly Rotation (Ranked #1 on rolling 30D leaderboard)
- Call of day: XLK BEARISH (Highest bullish percentage in precomputed sector consensus)
- Failure of day: Electricity Consumption (Lowest full-window force rank)

## Notable Divergences
- Algo Biscotti (Unconditional Loyalty): force rank #398, rolling 30D rank #14. Strong recent 30D rank despite weaker full-window force rank.
- Algo Biscotti (Unconditional Loyalty) (alt): force rank #395, rolling 30D rank #13. Strong recent 30D rank despite weaker full-window force rank.
- Daily Rise In Freightlogistics Google Trends For Truck Driver Shortage Signals Industrial Sector Labor Supply Constraint: force rank #388, rolling 30D rank #22. Strong recent 30D rank despite weaker full-window force rank.
- Lumber Momentum: force rank #379, rolling 30D rank #18. Strong recent 30D rank despite weaker full-window force rank.
- Grocery Price Inflation Google Trends Spike Signals Consumer Staples Demand: force rank #342, rolling 30D rank #27. Strong recent 30D rank despite weaker full-window force rank.

