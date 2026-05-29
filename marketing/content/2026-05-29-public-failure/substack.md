# Why the failures stay visible

StockArithm is a live ranking system that tests 374 trading algorithms against real market data. Every day, we measure which ones beat the S&P 500 and which ones don't. We publish the results—wins and losses—without filtering or spin. The system exists because most trading research hides its failures. Backtests show only the strategies that worked. Live leaderboards are rare, and when they exist, they often disappear when the numbers turn ugly.

This matters because failure is the only honest teacher in markets. If you can't see what doesn't work, you can't learn what might. And if a system only shows you the winners, you're not looking at evidence—you're looking at marketing.

## The math of failure

Right now, 374 algorithms are running live. Of those, only 4 are beating the S&P 500 year-to-date. That's 1%. The other 370 are underperforming.

SPY returned 10.76% so far this year. The median algorithm in our system is down or barely flat. Some are down 6%, 11%, even 17%. These aren't theoretical losses. They're real equity curves, updated daily, visible to anyone who looks.

The temptation—the industry standard, really—is to stop publishing the moment the numbers get bad. Rename the strategy. Adjust the parameters. Wait for a better window. Relaunch with a new track record. Repeat.

We don't do that. The failures stay visible because they're the data.

## A concrete case: the chaos rotation lab

One algorithm in our system is called "Chaos Rotation Lab." It's ranked 374th overall—dead last on our force-ranked leaderboard. Year-to-date, it's down 6.26%. Over the past 30 days, it's returned 0.8% while SPY returned 6%. It's underperforming by 5.2 percentage points in a single month.

By any reasonable standard, this algorithm has failed.

But here's where it gets interesting: in the last 30 days alone, Chaos Rotation Lab ranked 16th out of 375 algorithms. It was in the top 5% of recent performers. Yet its full-window ranking is 374th. The gap between its long-term record and its recent performance is 358 positions.

This divergence is a failure, but not the kind you'd expect. It's not a failure of the algorithm to work—it's a failure of the algorithm to work *consistently*. It got lucky recently. Or the market changed. Or both. The point is: you can't see this pattern if you only publish the winners or if you hide the full history.

When we show Chaos Rotation Lab's entire track record alongside its recent spike, we're showing you what *actually happened*. Not what we wish had happened. Not what the algorithm's designer claims it should do. What it did.

## Why this matters for you

If you're building a trading system, testing a hypothesis, or evaluating someone else's strategy, you need to see the failures. Not because failure is fun—it isn't. But because:

1. **Failure reveals regime dependence.** An algorithm that works in one market environment and fails in another is telling you something about what it actually does. Chaos Rotation Lab's recent strength and long-term weakness suggests it's sensitive to market conditions. That's useful information.

2. **Failure exposes overfitting.** If a strategy looks great on paper but collapses in live trading, the backtest was probably too tight. Seeing both the backtest and the live result is how you learn to be skeptical.

3. **Failure is the only honest comparison.** When you can see all 374 algorithms ranked side by side—the winners and the losers—you can actually evaluate what works. You're not comparing a strategy to a cherry-picked benchmark. You're comparing it to everything else.

4. **Failure teaches humility.** Markets are harder than they look. Of 374 algorithms tested here, only 4 beat the index. That's not because the other 370 are stupid. It's because beating the market is genuinely difficult. Seeing that in real time is worth more than a thousand blog posts about risk management.

## What the data says today

As of May 29, 2026:

- **Quantified Simple Monthly Rotation** is ranked #1 overall and #1 in the last 30 days. It's up 17.14% year-to-date, beating SPY by 6.38 percentage points. It's the only algorithm in the top 5 that's actually beating the index.

- **Faber Momentum Rotation** is ranked #2 overall but is down 2.56% relative to SPY. It's up 8.2% year-to-date, but that's 2.56 points behind the market.

- **Retail Sales Momentum** is ranked #4 overall but #4 in the last 30 days. It's returned 7.14% year-to-date, underperforming by 3.29 points.

- **Port Container Volume** and **Liquor Store Leading Indicator** are ranked 371st and 372nd. Both are down roughly 1% year-to-date. Both are "crazy" category algorithms—meaning they're based on unconventional signals. Both are failing.

The pattern is clear: most strategies underperform. A few don't. The ones that do tend to be simpler and more mechanical. The ones that don't tend to rely on exotic data or complex logic.

But you can only see that pattern if the failures are visible.

## The takeaway

StockArithm exists to answer a simple question: *What actually works?* Not what sounds good. Not what worked in the past. What works right now, measured against the market, with nothing hidden.

That means publishing the failures. It means keeping Chaos Rotation Lab on the leaderboard even though it's ranked 374th. It means showing you that 370 out of 374 algorithms are underperforming. It means being honest about what the data says, even when the data is ugly.

If you're serious about trading or investing, you need to see the full picture. Not the highlight reel. The full picture includes the failures, the divergences, the algorithms that looked good last month and terrible this month. That's where the real learning happens.

---

**Want to see the live leaderboard?** Visit [stockarithm.com](https://www.stockarithm.com) to track all 374 algorithms in real time. No filters. No spin. Just the data.
