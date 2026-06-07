# StockArithm Lab Report: 419 Algos, Zero Beating SPY on Force Rank, 7 Winning on 30D Momentum

We're running 419 signals across 105 tickers in live paper trading. Today's snapshot is instructive precisely because it shows what *not* working looks like.

## The Brutal Baseline

SPY returned 8.25% YTD. On the force-rank leaderboard (cumulative returns since seed, 122 days live), **zero algos beat the benchmark**. The top performer, Algo Baileymol (Chaos Monger), sits at +8.16% YTD—9 basis points underwater. Second place, Quantified Simple Monthly Rotation, is at +6.11%. By rank 5, Faber Momentum Rotation has delivered only +2.4%.

This is the lab's core value proposition: we publish the failures. Baileymol ranks #1 on force return but carries -0.09% alpha. That's not a win. It's a tie with noise.

## The Rolling 30D Divergence

The 30-day rolling leaderboard tells a different story. Seven algos beat SPY's 30D return of +0.51%:

- **Algo Biscotti (Unconditional Loyalty)**: +1.73% (30D), Sharpe 0.73, max drawdown -4.7%
- **Algo Biscotti (alt variant)**: +1.73% (30D), Sharpe 0.73
- **VIX Fear Rotation**: +1.04% (30D), Sharpe 0.35
- **VIX Term Structure**: +1.04% (30D), Sharpe 0.35
- **Algo Baileymol**: +0.98% (30D), Sharpe 0.86

Why report both rankings? Because they answer different questions. Force rank reveals whether a strategy survives long-term. Rolling 30D exposes regime sensitivity and recent momentum. VIX Fear Rotation ranks #417 on force (YTD: -3.56%) but #3 on 30D momentum. That's a 414-rank gap. It's either a recent regime shift or a signal that volatility-based strategies are mean-reverting hard.

## Notable Failures

The bottom tier is instructive. Chaos Rotation Lab (a Baileymol variant) sits at rank 419 with -8.96% YTD. FINRA Dark Pool Signal, Copper Momentum, and Faber Momentum all posted negative 30D returns with Sharpe ratios below -1.6. These aren't edge—they're noise with leverage.

## Data Sources & Limitations

Signals span alternative data (TSA mobility, FRED macro, Reddit sentiment, job openings, dark pool flow, VIX term structure, sector rotation mechanics). Coverage is 105 tickers across 48 sector consensus signals.

**Critical caveat**: 122 days of live paper trading is *not* statistically significant. Sample size N=122 means confidence intervals are wide. Biscotti's 1.73% 30D return could easily be luck. Faber's +2.4% YTD could be regime-specific. We're publishing this precisely because the methodology is transparent and reproducible—not because the results are conclusive.

The spread is stark: 0 of 419 beat SPY on force rank; 7 of 420 beat SPY on 30D rolling. That's a 1.7% win rate on the recent window. The lab's differentiator is honesty about that ratio, not hiding it.

Methodology and full leaderboard at stockarithm.com.