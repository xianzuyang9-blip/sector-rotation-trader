# One data source and what it really measures

StockArithm is a live testing ground for trading algorithms. We run 385 different strategies—some based on classic momentum theory, others on alternative data sources like job postings, retail sales, and consumer sentiment—and rank them by real returns. The goal is simple: find out which signals actually work, and which ones sound good but fail in practice.

This post is about one of those alternative data sources, why it matters, and what the evidence actually shows when you test it at scale.

## Why alternative data sounds so promising

The appeal is obvious. If you can find a data source that moves before the market does, you've found an edge. Traditional stock prices and volume are already baked into thousands of algorithms. But what if you could trade on job postings before earnings season? Or liquor store foot traffic before consumer spending reports? Or dark pool activity before institutional moves?

The logic is sound: real economic activity leaves traces. Those traces appear in alternative data before they show up in official statistics or stock prices. If you can read those traces, you can get ahead of the crowd.

The problem is that "sounds promising" and "actually works" are different things. Most alternative data sources fail when tested rigorously over time. And the ones that do work often work for reasons nobody expected.

## The case study: Retail Sales Momentum

Let's look at one concrete example from our current leaderboard: **Retail Sales Momentum**.

This algorithm trades based on real-time or near-real-time retail sales data—the idea being that consumer spending accelerates or decelerates before it shows up in official reports, and before the market fully prices it in. It's a reasonable hypothesis. Consumer spending drives GDP. If you can see it moving early, you should be able to trade on it.

Here's what the data shows:

**Full-window performance (119 days):**
- Return: +5.56% YTD
- vs. SPY: +11.49% YTD
- Alpha: -5.92%
- Rank: 5th out of 385 algorithms

**Last 30 days:**
- Return: +4.96%
- vs. SPY: +5.79%
- Alpha: -0.83%
- Sharpe ratio: 2.68
- Rank: 4th out of 386 rolling algorithms

So Retail Sales Momentum is doing okay recently—top 5 in the last month—but it's underperforming the market over the full window. It's not a disaster. It's not a winner either.

## The contrast: What actually beats the market

Now compare that to the algorithm that *is* winning: **Quantified Simple Monthly Rotation**.

This strategy doesn't use alternative data at all. It's a straightforward monthly rebalance across a basket of assets, based on momentum and trend. No dark pools. No consumer sentiment surveys. No proprietary data feeds.

**Full-window performance (119 days):**
- Return: +16.65% YTD
- vs. SPY: +11.49% YTD
- Alpha: +5.16%
- Rank: 1st out of 385 algorithms

**Last 30 days:**
- Return: +14.83%
- vs. SPY: +5.79%
- Alpha: +9.04%
- Sharpe ratio: 4.62
- Rank: 1st out of 386 rolling algorithms

The winner is boring. It's a rotation strategy. It doesn't require expensive data subscriptions or machine learning pipelines. It just rebalances monthly based on what's already moving.

## The failure mode: When alternative data breaks

But here's where it gets interesting. Some alternative data sources don't just underperform—they catastrophically fail.

Look at **Liquor Store Leading Indicator**:

- Return: -3.14% YTD
- vs. SPY: +11.49% YTD
- Alpha: -14.63%
- Rank: 383rd out of 385 algorithms
- Last 30 days: -2.64% (vs. SPY +5.79%)

The logic was: liquor store foot traffic correlates with consumer confidence and discretionary spending. If you can track it, you can predict consumer behavior. It sounds plausible. It's also completely wrong in this market.

Or **Consumer Sentiment**:

- Return: -2.41% YTD
- vs. SPY: +11.49% YTD
- Alpha: -13.90%
- Rank: 381st out of 385 algorithms
- Last 30 days: -2.41% (Sharpe: -4.79)

Consumer sentiment surveys are a standard economic indicator. The University of Michigan publishes them monthly. Surely they contain signal about future market moves? The data says no. Not in this window. Not at this scale.

## What this actually tells us

Three lessons emerge from testing 385 algorithms, including dozens built on alternative data:

**First: Alternative data is not inherently better.** It's just different. The fact that it's expensive, proprietary, or novel doesn't make it predictive. Liquor store traffic and dark pool volume are real data. They just don't predict stock returns in the way the hypothesis suggested.

**Second: The simplest strategies often win.** Monthly rotation based on momentum has beaten 384 other strategies, including ones with access to job postings, mortgage rates, electricity consumption, and FINRA dark pool signals. This doesn't mean alternative data is useless forever. It means that in this market, in this window, the edge came from something much older: trend-following.

**Third: Failure is informative.** When Liquor Store Leading Indicator ranks 383rd, that's not noise. It's a signal that the hypothesis was wrong. The market doesn't care about liquor store foot traffic the way the algorithm designer thought it would. That's valuable to know. It saves you from deploying real capital on a broken idea.

## What you should take away

If you're evaluating alternative data sources for trading, don't ask: "Does this sound like it should work?" Ask: "Does it actually work when tested against real returns over time, at scale, against other strategies?"

StockArithm exists to answer that question. We test the hypotheses. We rank the results. We show you the winners and the failures side by side, with no hype.

Right now, the evidence says that simple momentum rotation is beating alternative data sources. That could change. Markets shift. New data sources emerge. But the only way to know is to test, measure, and update.

If you want to see the full leaderboard—all 385 algorithms, ranked by real returns, updated daily—visit **stockarithm.com**. You'll see which strategies are actually working, which ones are failing, and which alternative data sources are worth your attention.
