# Why One Signal Beats SPY While 384 Fail: What Retail Sales Data Actually Tells You

Out of 385 trading signals we track, exactly one is beating SPY right now. The other 384 are visible on our leaderboard—and most are losing money. This isn't a story about finding the winner. It's about understanding why so many alternative data sources fail, and what that tells us about how markets actually work.

## The Winner: Simplicity Over Complexity

The signal winning today is called **Quantified Simple Monthly Rotation**. It's up 16.65% year-to-date while SPY sits at 11.49%. Over the last 30 days, it's returned 14.83% versus SPY's 5.79%—a 9.04 percentage point edge.

Here's the thing: it's not using exotic alternative data. It's not scraping dark pool flows or analyzing satellite imagery. It's a straightforward monthly rotation strategy that rebalances based on momentum across a basket of assets. It's been running for 119 days. It works.

The second-ranked signal, "Algo Baileymol," is down 3.33% against SPY's 11.49%. The third, "Antonacci Dual Momentum Sector Rotation," is down 4.08%. By rank 385—a signal called "Electricity Consumption"—we're looking at -18.23% alpha and a -6.74% year-to-date return.

## The Losers: What Alternative Data Gets Wrong

This is where it gets interesting. We track 385 signals across 105 tickers. Many of them rely on alternative data sources—the kind that promise edge through unconventional information. Let's look at three that are currently failing hardest:

**Liquor Store Leading Indicator** (rank 383): -14.63% alpha, -3.14% YTD. The logic is intuitive—consumer spending at liquor stores might signal economic health. But it's down 2.64% over the last 30 days while SPY gained 5.79%. The signal is noisy. Consumer behavior at a single retail category doesn't predict broad market moves reliably.

**FINRA Dark Pool Signal** (rank 382): -14.19% alpha, -2.7% YTD. Dark pool volume is real data. Institutional order flow matters. But predicting market direction from it? The signal has been running 109 days and is consistently underperforming. It's possible dark pool data is already priced in by the time retail traders see it.

**Consumer Sentiment** (rank 381): -13.9% alpha, -2.41% YTD. This one is particularly telling. Consumer sentiment surveys are published regularly. They're legitimate economic indicators. Yet as a trading signal, they're among the worst performers in our system. Sentiment moves slowly. Markets move fast. The lag kills the edge.

## The Gap Between Logic and Returns

Here's what these failures reveal: **intuitive logic doesn't equal market edge.**

A liquor store indicator *should* work if consumer spending predicts economic cycles. Dark pool data *should* matter if institutional order flow drives prices. Consumer sentiment *should* be useful if it reflects future spending.

But "should" and "does" are different things in markets.

The winners tend to be simpler. They're based on price momentum, sector rotation, and rebalancing rules—mechanical signals that don't require the data source to be predictive. They just need to capture existing market structure.

The losers often rely on alternative data that's either:
- **Too slow**: Sentiment surveys and economic reports lag price discovery.
- **Too noisy**: Retail behavior at one store type doesn't generalize.
- **Already priced in**: By the time alternative data reaches traders, smart money has already moved.

## What This Means for Your Research

If you're evaluating alternative data sources for trading, don't ask "Is this data real?" Ask instead:

1. **Is it faster than price?** If the market already knows it, you're late.
2. **Does it generalize?** One data point from one source rarely predicts broad market moves.
3. **Can you act on it mechanically?** The best signals don't require interpretation. They're rules.

The Quantified Simple Monthly Rotation doesn't need satellite imagery or dark pool access. It just needs a calendar and a price feed. That's not sexy. But it's beating 384 other signals, including ones built on more exotic data.

---

**The full analysis—including sector consensus, notable divergences, and deeper dives into why specific alternative data sources fail—is available on our Substack.** We update these rankings daily and track which signals survive market regimes. If you're building a quant strategy or evaluating data vendors, the patterns here matter.
