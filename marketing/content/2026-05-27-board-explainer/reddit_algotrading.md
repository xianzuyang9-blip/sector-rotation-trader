We run 374 signals live. One beats SPY on force rank. The other 373 don't. Here's what that split actually means, and why the board layout matters more than the headline.

**Force Rank vs. Rolling 30D: The Difference**

Force rank is cumulative. It measures total return from inception (114 days for most signals here) against SPY over the same window. It's your "did this idea work overall?" metric. Simple Monthly Rotation is +16.06% YTD. SPY is +10.17%. That's a 5.89% alpha edge. One signal. 373 failures.

Rolling 30D is a different animal. It's a 30-day lookback window that resets daily. It answers "what's working right now?" not "what worked on average?" This matters because a signal can be underwater for months and then catch fire in the last month. Or vice versa.

Look at VIX Fear Rotation: force rank 372 (dead last), rolling 30D rank 3 (top tier). It's down -1.17% YTD but returned +6.08% in the last 30 days. That's a rank gap of 369 positions. Same signal, two completely different stories depending on your time horizon.

**Why This Matters for Your Backtest**

If you're building a meta-strategy that picks from this board, you need to decide: are you optimizing for persistence or recency? Force rank rewards consistency. Rolling 30D rewards momentum. They're not the same thing.

Chaos Rotation Lab sits at force rank 374 (worst) but rolling 30D rank 14 (decent). It's -6.08% YTD but +0.18% in the last month. If you weighted only recent performance, you'd pick it. If you weighted full-window, you'd skip it entirely.

**The Honest Part**

373 signals are losing to SPY on a full-window basis. That's not a bug—it's the point. We keep them visible because:

1. Failure teaches faster than success.
2. A signal that's broken for 100 days and then works for 14 is still a signal.
3. The board is public. No cherry-picking.

The one winner (Simple Monthly Rotation) is boring: sector rotation, monthly rebalance, 114 days of data. It's not exotic. It's not a proprietary indicator. It's a textbook idea that happened to work in this market window.

The 373 losers include container volume, liquor store traffic, and VIX term structure. Some are "crazy" (labeled as such). Some are standard momentum or mean-reversion. The label doesn't predict the outcome.

**How to Read This**

If you're paper-trading or backtesting: check both metrics. Force rank tells you what's durable. Rolling 30D tells you what's hot. The gap between them is where the real signal lives.
