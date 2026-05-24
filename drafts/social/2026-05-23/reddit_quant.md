# StockArithm Lab Report: 339 Algos, 1 Winner, 111 Days In

We're running 339 signals across 105 tickers in live paper trading. Today's snapshot: **1 algo is beating SPY on force rank. 4 are beating it on rolling 30-day momentum.** That's the honest baseline.

## The Setup

Each signal ingests alternative data—FRED macroeconomic releases, TSA passenger flows, Reddit sentiment, job openings, VIX term structure, port container volume, freight rail carloads, FINRA dark pool activity, retail sales, copper prices. We rank them two ways:

1. **Force rank**: cumulative return since seed (111 days ago). Accounts for the full sample. SPY is up 9.44% YTD; we measure alpha against that.
2. **Rolling 30D momentum**: recent performance only. Sharpe ratio, max drawdown, and delta vs. SPY in the last month.

We publish both because they tell different stories. Force rank is your long-term signal quality. Rolling 30D catches regime shifts and recent edge decay.

## What's Working

**Quantified Simple Monthly Rotation** (simple_monthly) leads on both metrics:
- Force rank: +3.64% alpha, +13.09% YTD, $113,086 equity
- Rolling 30D: +13.09% return, Sharpe 5.46, +8.24% vs. SPY

That's the outlier. It's a standard momentum rotation strategy—no exotic data. It works. But it's *one algo out of 339*.

The rolling 30D leaderboard shows more diversity: **VIX Fear Rotation** (rank 337 on force, rank 2 on 30D) returned 6.14% in the last month with a 4.14 Sharpe. **VIX Term Structure** and **Retail Sales Momentum** also posted positive 30D deltas. These are "crazy" category signals—alternative-data driven. Some are catching recent momentum; others are noise.

## What's Failing

**335 of 339 algos are underperforming SPY on force rank.** The bottom tier:
- Copper Momentum: -11.24% alpha, -1.8% YTD
- Port Container Volume: -11.62% alpha, -2.18% YTD
- VIX Fear Rotation (force rank): -11.79% alpha, -2.35% YTD

Note the divergence: VIX Fear Rotation is rank 2 on rolling 30D but rank 337 on force. It was underwater for months, then caught a recent edge. That's a red flag for overfitting or regime-dependent signal decay.

## The Critique (We'll Say It First)

**Sample size:** 111 days is not statistically significant. A single algo beating SPY over 4 months could be luck. Sharpe ratios above 5 are suspicious—they suggest either genuine edge or data snooping. We're publishing the failures to let you audit the methodology.

**Survivorship bias:** We're not hiding dead signals. But we're also not running 10,000 backtests and showing you the 5 that worked.

**Sector consensus:** All five major sectors are BEARISH according to our algo consensus (Technology 29% bullish, Industrials 23%, Utilities 12%). That's a weak signal—it's not actionable, and it's not a prediction.

## Why This Matters

The point isn't that we've found alpha. The point is transparency. We run signals live, we publish losses, we show the spread. You can see which data sources fail (freight rail, dark pools, copper) and which occasionally work (VIX, retail sales, simple momentum). That's the differentiator.

Methodology and full leaderboard at **stockarithm.com**.