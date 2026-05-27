# Lab Report: 374 Signals, 1 Beating SPY on Force Rank — Here's What That Means

We're running 374 algorithmic signals across 105 tickers. Today's snapshot: **373 are underwater vs. SPY on the full-window force rank. One is not.**

This is the post where we lead with failure, because that's the only honest way to run a public lab.

## The Pipeline

Each signal gets two scorecards:

1. **Force Rank** — cumulative return from day 1 (114 days for most signals). This is your "did this idea actually work?" metric.
2. **Rolling 30D** — last 30 calendar days. This catches regime shifts and recent momentum that force rank might bury.

We measure edge as alpha: signal return minus SPY return. SPY is up 10.17% over the window. Most of our signals are not.

## The Failure Rate (Lead with This)

- **Force rank:** 1 of 374 beating SPY (0.27%)
- **Rolling 30D:** 5 of 375 beating SPY (1.3%)

The gap matters. It tells us something is happening *right now* that wasn't happening before. More on that below.

### Top Force Rank (The Lonely Winner)

**Quantified Simple Monthly Rotation** (+5.89% alpha, +16.06% YTD)
- 114 days live
- Equity: $116,063.69
- Sharpe (30D): 6.53

Everything else is negative alpha. **Faber Momentum Rotation** is second at -1.82%. **Algo Baileymol** (Chaos Monger) is third at -2.01%. The bottom three are all "crazy" category signals (alternative data experiments): Port Container Volume, Liquor Store Leading Indicator, and VIX Fear Rotation, all down 11%+ vs. SPY.

## The Divergence: Why Rolling 30D Matters

Here's where it gets interesting. **VIX Fear Rotation** ranks 372nd on force rank (down 11.34% YTD) but **3rd on rolling 30D** (up 6.08% in the last month, +1.13% vs. SPY).

Same story for **Chaos Rotation Lab** (Baileymol-crazy): force rank 374, rolling 30D rank 14.

This isn't noise. These signals are either:
- Recovering from a bad regime
- Overfitting to recent data
- Actually capturing something the market just started pricing in

We don't know which. That's why we publish both.

## Sector Consensus (All Bearish)

Our 42 signals covering Technology (XLK) are 33% bullish. Everything else is worse: Basic Materials 19%, Consumer Defensive 16%, Industrials 13%, Utilities 12%. The composite label across all sectors: **BEARISH**.

This is not a prediction. It's a vote count. 

## What We're Not Saying

- No "this is the bottom" or "buy the dip"
- No claims about why one signal works and 373 don't
- No promises that rolling 30D winners will stay winners

## What We're Asking

If you're running algos or building signals, what would make you trust a leaderboard like this? What's missing? Why does force rank vs. rolling 30D matter to you — or does it?

Full leaderboard at stockarithm.com — all signals public, failures included.