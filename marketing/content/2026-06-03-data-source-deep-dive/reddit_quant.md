We ran 385 signals across 105 tickers. One is beating SPY. Here's what we learned about alternative data and why most of it fails.

The winner: Quantified Simple Monthly Rotation. It's up 16.65% YTD versus SPY's 11.49%. Over 119 days, it generated 5.16% alpha. On the 30-day rolling window, it returned 14.83% while SPY returned 5.79%—a 9.04 percentage point delta. Sharpe of 4.62 over 30 days. That's the signal. That's the data.

The rest: 384 signals underperformed. Some used alternative data sources—retail sales momentum, job posting acceleration, VIX term structure, consumer sentiment, FINRA dark pool signals, liquor store foot traffic, electricity consumption. All ranked below the simple monthly rotation. Most are negative alpha.

What this tells you about alternative data:

**Sample size is the hard constraint.** We have 119 days of live paper-traded results. That's not enough to distinguish signal from noise for most strategies. The rolling 30-day leaderboard shows three signals beating SPY in that window. Over the full period, one. Extend the lookback and the ranking will shift again. This is not a statement about which signal is "best"—it's a statement about statistical power.

**The data source doesn't guarantee the signal works.** Consumer Sentiment (rank 381, -13.9% alpha) and FINRA Dark Pool Signal (rank 382, -14.19% alpha) are both "alternative" in the sense that they're not price or volume. They're also both failing. Job Posting Acceleration (rank 5 on 30-day, -1.54% delta to SPY) looks better recently but is still underwater YTD. The label "alternative data" doesn't predict performance. The execution does.

**Regime matters more than you'd expect.** Algo Biscotti ranks 380 on force (full-window) but 16 on rolling 30-day—a 364-rank gap. Lumber Momentum: 375 force rank, 17 rolling rank. These aren't errors. They're evidence that recent market conditions favor certain strategies while penalizing others. A signal that works in one regime can be worthless in the next.

**The leaderboard is honest about failure.** Electricity Consumption is ranked 385. It's down 6.74% YTD. We're showing it. No filtering, no survivorship bias, no post-hoc narrative about why it "should" have worked.

The sector consensus is uniformly bearish (Industrials 25% bullish, Technology 23%, Utilities 21%). That's not a prediction. That's what the 385 signals are voting.

If you're building quant systems, the lesson isn't "use alternative data." It's "measure everything, hold the sample size constant, and be willing to kill signals that don't work." The one signal beating SPY isn't beating it because of exotic data. It's beating it because the logic is simple and the execution is clean.
