# Why good signals fail in the wrong regime

A strategy that crushed it last month can crater this month. A signal that worked for three years can stop working overnight. This isn't randomness. It's regime mismatch—and it's the reason most backtests don't survive contact with real markets.

StockArithm is a live signal-ranking system that tracks 374 trading algorithms across 105 stocks, updating daily. We don't sell strategies or promise returns. We publish what actually happens when dozens of different signal types compete in real time. And what we're seeing right now is a textbook case of why regime matters more than signal quality.

## The setup: One winner, 373 also-rans

As of May 29, 2026, the Quantified Simple Monthly Rotation algorithm is the only strategy beating the S&P 500 year-to-date. It's up 12.42% while SPY is up 11.03%. That's a 1.39% alpha edge—real, measurable, and documented.

Everything else is underwater or barely treading water.

The second-ranked algo, Baileymol (a chaos-based rotation system), is down 2.87% relative to SPY. The Faber Momentum Rotation, a well-known tactical allocation framework, is down 4.89%. Retail Sales Momentum, Job Posting Acceleration, and a dozen other "smart" signals are all negative alpha.

At the bottom of the leaderboard, the Liquor Store Leading Indicator is down 13.17%. Consumer Sentiment is down 12.56%. FINRA Dark Pool Signal is down 12.83%.

These aren't all bad ideas. Some of them work in other regimes. But right now, in this market, they're failing.

## The divergence: Recent winners that are full-window losers

Here's where regime mismatch becomes visible.

Chaos Rotation Lab (a variant of Baileymol) ranks 374th overall—dead last—with a year-to-date return of -6.59%. But in the last 30 days, it's ranked 15th, returning +0.23% while SPY returned +6.31%. It's been working lately. It just hasn't worked for long enough to overcome its earlier losses.

Algo Biscotti (Unconditional Loyalty) shows the same pattern. Full-window force rank: 366th. Rolling 30-day rank: 11th. It's been one of the better performers in the last month, but the market regime that made it work didn't exist six months ago.

This is the regime mismatch in its purest form: a signal that is *currently correct* but was *historically wrong*. If you'd been running it all year, you'd be underwater. If you started it last month, you'd be beating the market.

## Why the simple monthly rotation is winning

The Quantified Simple Monthly Rotation doesn't rely on sentiment, dark pool flows, job postings, or liquor store traffic. It's a straightforward rebalancing system—the kind of thing that works when markets are mean-reverting and sector rotations are predictable.

In the current regime, that's exactly what's happening. Sectors are rotating. Momentum is fading. Simple rules are beating complex ones.

But this regime won't last forever. When volatility spikes, when correlations break down, when the market stops respecting historical patterns—the simple monthly rotation will fail. And one of the "crazy" signals that's currently losing will suddenly start winning.

The Liquor Store Leading Indicator isn't a bad idea because it's stupid. It's failing because the regime it was designed for (consumer stress, recession signals, flight to safety) isn't the current regime. When that regime returns, it might work again.

## What the data actually tells us

Out of 375 algorithms tracked over the last 30 days, only 4 are beating SPY. That's 1.1%. The median algorithm is down 7.8% relative to the market.

This isn't a sign that most strategies are broken. It's a sign that the current regime—steady growth, sector rotation, mean reversion—favors a very specific type of signal. Everything else is noise.

The moment the regime shifts—and it will—the leaderboard will reshuffle. Algorithms that are currently ranked 350th will move to the top 50. Algorithms that are winning now will crater.

This is why backtesting is dangerous. A strategy that shows 15% annual returns over a 10-year backtest might have worked in only 2 of those 10 years. The other 8 years, it was underwater. You just didn't notice because you were looking at the average.

## The takeaway: Regime awareness beats signal confidence

The best traders don't ask "Is this signal good?" They ask "Is this signal good *right now*?" They monitor regime shifts. They know when their edge is working and when it's not. They're willing to sit out when the regime doesn't match their signal.

StockArithm exists to make that visible. We show you which signals are working in the current regime, which ones are waiting for their regime to return, and which ones are diverging—working recently but failing historically, or vice versa.

You can't predict regime shifts. But you can see them happening in real time by watching what's winning and what's losing. The Liquor Store Leading Indicator isn't going to stay at the bottom forever. The Simple Monthly Rotation won't stay at the top forever. The market will change. The question is whether you'll notice when it does.

---

If you want to see the full leaderboard, the rolling 30-day rankings, and the regime divergences in real time, visit [stockarithm.com](https://www.stockarithm.com). We update daily. No hype. Just data.
