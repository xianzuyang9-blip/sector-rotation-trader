# How to read the board

StockArithm runs 374 trading algorithms against live market data and ranks them in two ways. One ranking—**force rank**—measures how well each algorithm has performed over its entire history. The other—**rolling 30D**—measures only the last 30 days. They tell very different stories. Understanding the difference is the key to reading the board without getting fooled.

## What StockArithm is

StockArithm is a live leaderboard of quantitative trading strategies. Each algorithm trades a basket of stocks or sectors based on a specific rule set—momentum, mean reversion, macro signals, sentiment data, whatever. We run them all in parallel, track their returns and risk metrics, and publish the results daily. The system covers 105 tickers across 374 distinct algos, from simple rotation strategies to experimental models built on container port volume or liquor store foot traffic.

The point is not to tell you which algo to trade. It's to show you what actually works in real time, without the noise of backtests or marketing. Some algos beat the S&P 500. Most don't. Some blow up. That's the data.

## Force rank: the long view

Force rank is the primary leaderboard. It ranks each algorithm by its total return since inception, adjusted for volatility (Sharpe ratio). An algo that has been running for 114 days and returned 16% year-to-date ranks higher than one that returned 6% in the same period, all else equal.

As of May 26, 2026, **Quantified Simple Monthly Rotation** sits at force rank #1 with a 16.06% YTD return and a 5.89% alpha over the S&P 500 (which returned 10.17% YTD). It has beaten SPY. Only one algo out of 374 has done that.

Force rank is stable. It rewards consistency. An algo that has been grinding out steady gains for months will stay near the top. An algo that had one good week but is otherwise mediocre will stay near the bottom.

The problem: force rank is backward-looking. It tells you what worked, not what's working *now*.

## Rolling 30D: the recent view

Rolling 30D ranks algos by their return over the last 30 calendar days only. It ignores history. It's a snapshot of momentum.

On the same date, the top 5 rolling 30D performers are:

1. **Quantified Simple Monthly Rotation** — 16.06% (same as force rank #1)
2. **VIX Term Structure** — 6.60% (a "crazy" experimental algo)
3. **VIX Fear Rotation** — 6.08% (also experimental)
4. **Uber Mobility Index** — 5.60% (experimental)
5. **Retail Sales Momentum** — 5.22% (experimental)

Notice: only one of these is a "normal" algo. The rest are experimental models. And notice that VIX Fear Rotation ranks #372 on force rank but #3 on rolling 30D. That's a gap of 369 positions.

Rolling 30D is forward-looking. It catches hot hands. But it's also noisy. An algo can spike on a lucky two-week run and then crash.

## The divergence that matters

The biggest insight on the board is when force rank and rolling 30D disagree sharply. These divergences tell you something is changing.

**VIX Fear Rotation** is the clearest example today:
- Force rank: #372 (YTD: -1.17%)
- Rolling 30D rank: #3 (30D return: +6.08%)
- Rank gap: 369 positions

This algo has been a dud all year. But in the last month, it's been on fire. Why? The data doesn't say. Maybe the market regime shifted. Maybe it got lucky. But the divergence is real, and it's worth watching.

The opposite happens too. **Chaos Rotation Lab** ranks #374 on force rank (worst in the system, YTD: -6.08%) but #14 on rolling 30D (30D return: +0.18%). It's been terrible for months but just started working. Again: the divergence is the signal.

These three algos—VIX Fear Rotation, Chaos Rotation Lab, and Algo Biscotti—are flagged as "notable divergences" on the board. They're not the best performers. They're the ones where recent behavior contradicts the long-term record.

## Why the split matters

If you only look at force rank, you miss the fact that the market has changed. You might keep trading an algo that worked for six months but stopped working last week.

If you only look at rolling 30D, you chase performance. You'll jump into the hottest algo and get crushed when it reverts.

The real edge is in the gap. When an algo that has been failing suddenly works, or when a winner suddenly fails, that's when you need to ask why. Is it a regime shift? A data artifact? A real change in market structure?

StockArithm shows you both numbers. The board displays force rank as the primary sort, but rolling 30D metrics are there too. The divergences are highlighted. You have to read both.

## What to take away

The board is not a buy signal. It's a fact sheet. On May 26, 2026:

- 374 algos are running live.
- 1 is beating SPY on a force-rank basis.
- 5 are beating SPY on a rolling 30D basis.
- The best performer (Simple Monthly Rotation) is also the most consistent.
- The worst performers (Port Container Volume, Liquor Store Leading Indicator, VIX Fear Rotation) are all experimental models that have been underwater all year.
- But three of those worst performers have spiked in the last 30 days, creating a divergence worth monitoring.

Read force rank for what works. Read rolling 30D for what's working now. Read the gap between them for what's changing.

---

**Want to see the full board and track these divergences yourself?** Visit [stockarithm.com](https://www.stockarithm.com) to explore live rankings, sector consensus, and daily signals across all 374 algos.
