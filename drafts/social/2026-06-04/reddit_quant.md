# StockArithm Lab Report: 121 Days In, 1 Algo Beating SPY (Force Rank)

We're running 403 live paper-trading signals across 105 tickers. Today's snapshot: **one algorithm is beating SPY on full-window force rank. Three are beating it on rolling 30-day momentum.** The rest are underwater. This is the point.

## The Leaderboard Reality

**Quantified Simple Monthly Rotation** leads force rank with +13.68% YTD vs. SPY's +11.12%—a 2.56% alpha over 121 days. It's also #1 on the 30-day rolling leaderboard with 9.49% return and a 2.94 Sharpe ratio. That's the win.

Below it: **Algo Baileymol (Chaos Monger)** at +8.16% YTD (-2.96% alpha), **Antonacci Dual Momentum Sector Rotation** at +7.38% YTD (-3.74% alpha), and 400 others trailing further. At the bottom, **Electricity Consumption** sits at -6.61% YTD, -17.74% alpha—the failure of the day.

The spread matters: 1 out of 403 force-ranked algos is winning. On rolling 30D, 3 out of 404 are beating SPY. That's 0.25% and 0.74% respectively. Not a portfolio. A diagnostic.

## Two Ranking Systems, Two Stories

We publish both force rank (full-window since seed) and rolling 30-day momentum because they answer different questions:

- **Force rank** shows which signals have compounded best over the entire live period. It's noisy at N=121 days—statistically insignificant by academic standards—but it's honest.
- **Rolling 30D** isolates recent regime fit. **VIX Fear Rotation** and **VIX Term Structure** rank #2 and #3 on 30D (3.86 Sharpe each) despite middling force ranks. **Job Posting Acceleration** (FRED labor data) ranks #4 on 30D but is underwater YTD. These divergences flag regime sensitivity.

## The Divergences

Three algos show sharp rank gaps: **Biscotti** variants and a **Google Trends freight/logistics signal** all rank 13–22 on rolling 30D but 388–398 on force rank. They've caught the last month. They lost the first four months. That's not edge; that's curve-fit to recent volatility.

## Data Sources & Caveats

Signals draw from FRED (retail sales, job postings, mortgage rates), TSA passenger data, Reddit sentiment, Google Trends, VIX term structure, FINRA dark pool volume, and sector ETF consensus. Sample size is 121 days. Correlation with SPY is high; alpha is thin. Drawdowns are real: **Electricity Consumption** peaked at -6.61% YTD. **Consumer Sentiment** is -2.29% YTD with a -4.6 Sharpe on 30D.

We're not claiming statistical significance. We're publishing the failures alongside the wins because that's the only way to audit alternative-data signals in real time.

**Methodology and full leaderboard at stockarithm.com.**