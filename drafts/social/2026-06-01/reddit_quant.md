# StockArithm Lab Report: 118 Days Live, 1 Algo Beating SPY (Force Rank)

We're publishing today's paper-trading results across 374 signals covering 105 tickers. The headline is stark: **only 1 algorithm is beating SPY on full-window force rank**. On rolling 30-day momentum, 3 are ahead. This is not a marketing problem. This is the actual state of the lab.

## The Numbers

**Force Rank (full window, 118 days):**
- Quantified Simple Monthly Rotation: +15.21% YTD, +3.87% alpha vs. SPY's +11.34%
- Baileymol (Chaos Monger): +8.16% YTD, -3.17% alpha
- Antonacci Dual Momentum Sector Rotation: +6.49% YTD, -4.85% alpha
- 371 of 374 algos are underwater relative to the benchmark

**Rolling 30-Day (last 30 trading days):**
- Simple Monthly Rotation: +13.53%, Sharpe 4.24, +7.89% delta to SPY
- VIX Fear Rotation: +8.29%, Sharpe 4.90, +2.64% delta
- VIX Term Structure: +8.27%, Sharpe 4.90, +2.62% delta
- SPY returned +5.64% in the same window

The divergence matters. Some algos (e.g., Daily Rise In Freightlogistics Google Trends) rank 357th force but 15th rolling 30D—a 342-rank gap. Others show the inverse: strong full-window, weak recent. This suggests regime sensitivity and the danger of overfitting to recent momentum.

## Data Sources & Methodology

Signals draw from FRED (economic data), TSA (travel), Reddit sentiment, job openings (Google Trends), VIX term structure, retail sales, mortgage rates, consumer sentiment, and price momentum across sectors. Each algo generates a daily signal; we rank by cumulative return (force rank) and 30-day rolling return separately. Both are reported because they answer different questions: *What has worked?* vs. *What is working now?*

## The Honest Critique

**Sample size:** 118 days is not statistically significant. A single lucky sector rotation or mean-reversion bounce can dominate the leaderboard. Sharpe ratios above 4.0 are suspicious at this horizon—they suggest either genuine edge or overfitting to a narrow regime.

**Survivorship bias:** We're showing failures (Electricity Consumption at -7.25% YTD, Liquor Store Leading Indicator at -3.56%), but only algos that made it into the lab. Dead signals aren't here.

**Sector consensus is bearish across the board:** Technology (28% bullish), Consumer Cyclical (23%), Utilities (21%). When consensus is this one-sided, it's worth noting—not as a signal, but as context for why mean-reversion algos may be struggling.

**The real test:** Can Simple Monthly Rotation sustain +3.87% alpha over 12+ months? Or does it revert? We'll know in 6 months. Until then, this is a data point, not a thesis.

## What We're Not Saying

No investment advice. No price predictions. No claims of edge. The point is the methodology and the public failure rate. 99.7% of algos are losing to SPY. That's the differentiator—we show it.

Methodology and full leaderboard at stockarithm.com.