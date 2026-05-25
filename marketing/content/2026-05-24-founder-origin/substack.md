# Why StockArithm exists

I built StockArithm because I got tired of watching smart people lose money to ideas that sounded good but didn't work.

Not because they were stupid. Because they had no way to know.

## The problem I kept running into

For years, I watched traders and investors operate on conviction. Someone reads a paper on momentum rotation. Another person discovers a correlation between copper prices and equity returns. A third notices that VIX term structure seems to predict market moves. All of these ideas have logic. Some have academic backing. Many have worked in the past.

But here's what I never saw: a systematic way to test whether they actually work *right now*, across a real portfolio, against a real benchmark, with honest accounting for when they fail.

Instead, I saw:
- Backtests that looked great because they were optimized on the exact data they were tested against.
- Strategies that worked for three years and then stopped, with no warning.
- Traders who believed in their edge so much they didn't notice it had evaporated.
- A lot of money moving based on plausible stories rather than evidence.

The worst part? There was no central place to see the graveyard. No dashboard showing which ideas were actually beating the market and which ones were just noise dressed up as insight.

## What StockArithm actually does

StockArithm is a live laboratory. It runs 344 different trading algorithms—some based on published academic research, some on market folklore, some on pure experimentation—and ranks them in real time against each other and against the S&P 500.

Every algorithm gets the same $100,000 starting capital. Every one is measured the same way: did it beat SPY? By how much? How much did it lose on its worst day? What's the Sharpe ratio?

No cherry-picking. No survivorship bias. No story that makes it sound better than it is.

As of today, May 24, 2026, we're tracking 105 different stock tickers across those 344 algorithms. In the last 30 days, only 4 of them beat the S&P 500. SPY returned 4.84% in that window. The best algorithm—Quantified Simple Monthly Rotation—returned 13.09% year-to-date and is up 3.64% relative to the market.

But here's the honest part: the worst algorithm is down 6.02% year-to-date. Some of the "crazy" category strategies—the experimental ones—are losing 11% or more while the market is up.

## Why this matters

The financial industry has a massive incentive to make things sound complicated. Complexity sells. It justifies fees. It makes people feel like they're getting something special.

But the evidence keeps showing the same thing: most active strategies underperform simple benchmarks. Most traders underperform buy-and-hold. Most "edge" is just luck with a good story attached.

That doesn't mean all strategies fail. It means you need to *measure* them honestly, *compare* them fairly, and *update* your beliefs when the data changes.

Right now, our data shows that simple monthly rotation is working. VIX-based strategies are having a good month. Copper momentum is getting crushed. Port container volume is getting crushed worse. The FINRA Dark Pool Signal is ranked #10 overall but #342 in the last 30 days—a massive divergence that suggests it worked in the past but isn't working now.

That's the kind of information that matters. Not because it tells you what to do, but because it tells you what's actually happening versus what you *think* is happening.

## A concrete example of why this exists

Take the Faber Momentum Rotation strategy. It's ranked #3 overall with 112 days of live trading. Year-to-date, it's up 8.27%. That sounds good.

But in the last 30 days, it's returned 4.26% while SPY returned 4.84%. It's underperforming. The algorithm that looked solid over a longer window is lagging right now.

Without a system like this, you'd either:
1. Keep believing in it because it worked before, and miss the fact that it's stopped working.
2. Abandon it because of one bad month, and miss the fact that it's still solid long-term.

With real-time ranking and honest measurement, you can see both truths at once. You can ask: is this a temporary drawdown or a regime change? The data doesn't answer that for you, but it gives you the right question to ask.

## What you should take away

StockArithm exists because the gap between "plausible idea" and "profitable strategy" is wider than most people think. And that gap is invisible unless you measure it.

We're not here to tell you which strategy to use. We're here to show you which ones are actually working, which ones have stopped, and which ones never worked at all. We're here to replace conviction with evidence.

Some strategies will beat the market. Most won't. The ones that do will eventually stop. That's not a failure of the system—it's how markets work. But you can't navigate that reality without seeing it clearly.

If you want to watch this in real time, see which algorithms are beating SPY this month, and understand why some strategies work while others fail, come see what we're building.

**[Visit StockArithm](https://www.stockarithm.com)** to see the live leaderboard, track algorithm performance, and test your own ideas against the data.
