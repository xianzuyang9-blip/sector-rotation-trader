# StockArithm Lab Report: 344 Algos, 1 Beating SPY (Force Rank), 4 in Rolling 30D

We're 112 days into live paper trading across 344 signals covering 105 tickers. The headline is brutal: only **1 algo is beating SPY on full-window force rank**. On the rolling 30-day leaderboard, **4 are ahead**. Both numbers matter, and both are statistically fragile.

## The Setup

Each signal is seeded at $100k. We track two ranking systems because they answer different questions:

1. **Force rank** (full window since seed): cumulative alpha from day 1. Answers: "Which signals have structural edge?"
2. **Rolling 30D**: recent momentum. Answers: "What's working *now*?" Sharpe ratios included.

SPY returned 9.44% over the measurement window. YTD, 13.09%.

## What's Winning

**Quantified Simple Monthly Rotation** (simple_monthly) leads both leaderboards:
- Force rank: +3.64% alpha, $113,086 equity
- Rolling 30D: +13.09% return, 5.46 Sharpe, +8.24% delta vs. SPY

This is a standard rotation algo. It works. But N=112 days. One quarter of data. The confidence interval is wide.

The rolling 30D top 4 include three "crazy" category signals (VIX Fear Rotation, VIX Term Structure, Retail Sales Momentum) that are underwater on force rank but hot recently. VIX Fear Rotation sits at force rank 342 (−2.35% YTD) yet ranks #2 in the last month (+6.14%). This is the divergence problem: mean reversion or regime shift? Unknown.

## What's Failing

**343 of 344 algos are underperforming SPY on force rank.** The bottom tier:
- Copper Momentum: −11.24% alpha, −1.8% YTD
- Port Container Volume: −11.62% alpha, −2.18% YTD
- VIX Fear Rotation (force rank): −11.79% alpha, −2.35% YTD

These are alternative-data signals (FRED commodity flows, TSA mobility, port logistics, FINRA dark pool volume, Reddit sentiment). The lab publishes them anyway. Transparency includes failure.

## The Honest Critique

**Sample size is the killer.** 112 days is 22 weeks. Sharpe ratios look clean (5.46 for the leader), but that's noise-fitting territory. A single tail event reshuffles the board. The 340-rank gap between VIX Fear Rotation's force rank (342) and rolling 30D rank (2) screams regime dependence, not signal quality.

**Sector consensus is uniformly bearish.** All five top sectors (Materials, Tech, Consumer Defensive, Industrials, Energy) show <26% bullish signals. This is crowded positioning. When consensus is this tight, edge is either nonexistent or about to reprrice hard.

**The "crazy" category (alternative data) is 3 of top 5 rolling 30D but 340+ of bottom force ranks.** That's not edge—that's overfitting to recent market structure.

## What We're Watching

- Does simple_monthly's alpha persist past 6 months?
- Do the VIX signals revert to their force-rank levels, or is this a regime shift?
- Will the bearish sector consensus trigger a reversal that favors the underperformers?

This is a lab. The point is methodology and public failure. We're not claiming edge. We're showing the work.

**Methodology and full leaderboard at stockarithm.com.**