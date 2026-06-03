I've been running 385 signals in live paper trading for four months. One is beating SPY. The rest are not. Here's what I learned about why—and why I'm publishing the full leaderboard including every failure.

**The Winner: Simple Monthly Rotation**

"Quantified Simple Monthly Rotation" returned 16.65% YTD while SPY returned 11.49%. That's 5.16% alpha over 119 days. In the last 30 days alone, it returned 14.83% versus SPY's 5.79%. The signal is mechanical: rank sectors by one-month momentum, hold the top three, rebalance monthly. No machine learning. No alternative data. No complexity.

Why does it work? Because it's measuring something real—recent relative strength—and acting on it without lag. The Sharpe ratio over 30 days is 4.62. Maximum drawdown in that window: 4%.

**The Failures: What I Expected to Work**

I built signals around alternative data sources I thought would predict returns:

- **Retail Sales Momentum**: -5.92% alpha. Ranked 5th overall but only because it's new (118 days running). The logic was sound—consumer spending should lead equity returns. It doesn't, at least not this way.
- **FINRA Dark Pool Signal**: -14.19% alpha. Dark pool volume as a contrarian indicator. Ranked 382nd. I was wrong about what it measures.
- **Liquor Store Leading Indicator**: -14.63% alpha. Ranked 383rd. The idea: discretionary spending at liquor stores predicts consumer health. It predicts nothing useful here.
- **Electricity Consumption**: -18.23% alpha. Ranked dead last (385th). I thought grid load would correlate with economic activity. It correlates with weather.

**The Divergence That Matters**

Three signals are ranked in the bottom 20 overall but top 20 in the last 30 days. "Algo Biscotti" is ranked 380th force-rank but 16th in rolling 30-day performance. This gap tells you something: recent market conditions favor a strategy that failed over the full window. That's not alpha. That's regime change. It's also why I publish both metrics.

**Why Visible Losses Matter**

Most backtests hide failures. They cherry-pick data windows, optimize parameters, and report only the winners. I'm doing the opposite: every signal runs live, every loss is public, and the leaderboard updates daily. 

When you see "Liquor Store Leading Indicator" ranked 383rd, you're seeing real money that would have been lost if I'd trusted the hypothesis. That's more useful than a 95% Sharpe ratio on a curated dataset.

**What This Means for You**

If you're building signals, test them live and publish the failures. If you're evaluating someone else's signals, ask for the full leaderboard, not just the winners. And if a signal sounds clever—dark pools, consumer sentiment, alternative data—be skeptical. The one that's working is the simplest one: momentum.
