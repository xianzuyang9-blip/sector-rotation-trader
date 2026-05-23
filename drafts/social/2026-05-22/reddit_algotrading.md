# Lab Report: 332 Signals, 1 Winner (Force Rank), 4 Winners (Last 30 Days)

We're running 332 algorithmic signals across 105 tickers. Today's snapshot: **99.7% are underperforming SPY on a full-window force-rank basis.** One signal is beating the benchmark. That's the actual state of the lab.

## The Pipeline

Each signal generates a daily position or rotation call. We measure two things:

1. **Force Rank** — cumulative alpha since inception (110 days for most signals). This is the long-term scoreboard.
2. **Rolling 30D** — last 30 calendar days of returns, Sharpe ratio, max drawdown, and delta vs. SPY. This catches regime shifts and recent edge.

SPY returned **9.44% YTD** and **4.84% in the last 30 days**. That's the bar.

## The Failure Rate (Lead with This)

**Force rank:** 1 of 332 signals beat SPY. That's **0.3% win rate** on the full window.

- **Quantified Simple Monthly Rotation** (simple_monthly): +13.09% YTD, +3.64% alpha. Equity: $113,085.93.
- Everyone else: negative alpha. Baileymol at -0.8%, Faber at -1.17%, DMSR at -2.55%.
- Bottom dwellers (Copper Momentum, Port Container Volume, VIX Fear Rotation): -11% to -12% alpha.

**Rolling 30D:** 4 of 333 signals beat SPY in the last month.

- simple_monthly: +13.09% (Sharpe 5.36, max DD -3.5%)
- VIX Fear Rotation: +5.40% (Sharpe 3.40, max DD -2.5%)
- Uber Mobility Index: +5.28% (Sharpe 3.18, max DD -2.5%)
- VIX Term Structure: +5.26% (Sharpe 3.23, max DD -2.5%)

Three of those four are "crazy" category signals (alternative data / exotic). One is a standard rotation.

## The Divergence Problem

This is where it gets interesting. **VIX Fear Rotation ranks #330 on force rank (YTD: -2.35%) but #2 on rolling 30D (+5.40%).** That's a 328-rank gap. Same with VIX Term Structure: force rank #322, rolling 30D rank #4.

Inverse case: **FINRA Dark Pool Signal** is force rank #10 but rolling 30D rank #296. It's been solid YTD (+0.27%) but flatlined the last month (-0.07%).

This matters. A signal that's been wrong for 110 days but right for 30 days is not the same as a signal that's been consistently right. We publish both rankings because they answer different questions: *Is this signal actually working?* vs. *Is this signal working right now?*

## Sector Consensus (All Bearish)

Across 40 signals covering Technology (XLK), only 28% are bullish. Basic Materials (XLB): 24% bullish. Energy (XLE): 14% bullish. The lab is tilted bearish across the board.

## What We're Not Claiming

- No alpha is "statistically significant" at 110 days.
- One winner out of 332 could be luck.
- The 30D winners might revert tomorrow.
- Alternative data (Uber Mobility, VIX signals, Retail Sales Momentum) is noisier than standard factors, and the rolling 30D leaderboard proves it.

## Invitation

If you see a methodological flaw in how we're measuring force rank vs. rolling 30D, or if you think a signal is gaming the system, call it out. The lab publishes failures publicly because that's the only way to know if the edge is real.

Full leaderboard at stockarithm.com — all signals public, failures included.