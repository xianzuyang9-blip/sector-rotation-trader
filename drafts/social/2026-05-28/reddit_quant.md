# StockArithm Lab Report: 374 Algos, 1 Beating SPY on Force Rank

We're running 374 signals across 105 tickers in live paper trading. One is ahead of SPY on full-window cumulative return. Four beat SPY in the rolling 30-day window. The rest are underwater or treading water. This is the report.

## The Setup

StockArithm publishes two ranking systems because they answer different questions:

**Force rank** (full-window since seed, ~116 days): cumulative alpha. Tells you which signals have actually compounded value over the entire live period. Only *Quantified Simple Monthly Rotation* is positive here—up 6.38% alpha while SPY returned 10.76%, for a net -4.38% underperformance. That's still the best in the cohort.

**Rolling 30-day momentum**: recent performance and risk-adjusted returns (Sharpe, max drawdown). Captures regime shifts and signal decay. Four algos beat SPY in this window: *Simple Monthly* (17.1% vs. SPY's 6.0%), *VIX Fear Rotation* (8.5%), *VIX Term Structure* (8.5%), and *Retail Sales Momentum* (7.2%).

The spread matters. Of 374 force-ranked algos, 373 are losing to SPY. Of 375 rolling 30D algos, 371 are losing. This is not a lab producing consistent alpha. It's a lab publishing consistent failure.

## Data Sources & Methodology

Signals draw from FRED (retail sales, job postings), TSA (travel volume), Reddit sentiment, FINRA dark pool data, port container volume, liquor store transactions, insider trading filings, and VIX term structure. Each algo is a hypothesis about market microstructure or macro regime. Most are wrong.

The bottom performers illustrate the point: *FINRA Dark Pool Signal* (-11.67% alpha), *Port Container Volume* (-11.7%), and *Liquor Store Leading Indicator* (-11.86%) are all "crazy" category signals—alternative data bets that failed to predict equity returns. They're ranked 370–372 out of 374. They're still published.

## The Honest Critique

116 days is not statistically significant. N=116 observations cannot distinguish signal from noise at conventional confidence levels. The single winner (*Simple Monthly*) may be luck. The four 30D winners may be mean reversion or regime-specific. We're not claiming edge; we're showing methodology.

Notable divergence: *Chaos Rotation Lab* ranks 374 on force (down 6.26% YTD) but 16 on rolling 30D (up 0.8% last month). *Insider Trading Signals* ranks 12 on force but 365 on rolling 30D. These gaps expose the fragility of short-window performance and the danger of chasing recent winners.

Sector consensus is uniformly bearish: Technology (24% bullish), Consumer Defensive (19%), Utilities (18%). No sector shows conviction.

## Why This Matters

The differentiator is not returns—they're mediocre. It's transparency. We publish the failures alongside the wins. We name the data sources. We state the sample size limitation. We show both ranking systems so you can see where signals are decaying. We don't claim statistical significance we don't have.

If you're building a quant strategy, this is a live case study in how alternative data performs in real time, and how often it doesn't.

Methodology and full leaderboard at stockarithm.com.