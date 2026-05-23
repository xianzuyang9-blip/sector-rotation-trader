# StockArithm Lab Report: 110 Days In, 1 Algo Beating SPY (Force Rank)

We're running 332 live paper-trading signals across 105 tickers. After 110 days, here's what the data says—and what it doesn't.

## The Headline (With Caveats)

**Quantified Simple Monthly Rotation** is the only algo beating SPY on full-window force rank: +13.09% YTD vs. SPY's +9.44%, generating +3.64% alpha. It's also #1 on the rolling 30-day leaderboard with a 5.36 Sharpe ratio and +8.24% outperformance over the last month.

That's one winner out of 332. Let's be direct: **110 days is not statistically significant**. This is a single draw from a distribution we don't yet understand. The lab publishes it anyway because transparency beats silence.

## The Spread

On rolling 30-day momentum, 4 algos are beating SPY. On force rank (full window), 1 is. The gap matters: it tells us whether recent performance is mean-reverting or persistent. Right now, the data suggests recent winners may not sustain.

At the bottom: **Copper Momentum**, **Port Container Volume**, and **VIX Fear Rotation** are down 1.8% to -2.35% YTD, dragging -11.24% to -11.79% alpha against SPY. These are labeled "crazy" algos—signals built on alternative data (commodity flows, port activity, volatility term structure). Some work in 30-day windows. None are working over the full sample.

## Notable Divergences

**VIX Fear Rotation** ranks #330 force but #2 rolling 30D—a 328-rank gap. It returned +5.4% in the last month while down -2.35% YTD. This is the kind of regime-dependent behavior that screams "watch for reversion."

**FINRA Dark Pool Signal** inverts the pattern: #10 force rank, #296 rolling 30D. It's been steady but recently flat. The divergence flags potential structural breaks in the signal.

## Data Sources & Methodology

Signals draw from FRED macroeconomic data, TSA passenger flows, Reddit sentiment, job openings, freight indices, VIX term structure, dark pool volume, and sector rotation mechanics. Each algo is a distinct hypothesis about market microstructure or macro regime.

We report two rankings because they answer different questions:
- **Force rank**: Which signals have the longest track record of edge?
- **Rolling 30D**: Which are working *right now*?

Both are necessary. Neither is sufficient at N=110 days.

## What We're Not Saying

We're not claiming edge. We're not predicting returns. We're not recommending any of these signals for live capital. The lab is a methodology testbed, not a fund pitch.

What we *are* doing: publishing failures alongside wins, naming sample size limitations, and letting quants and statisticians audit the leaderboard in real time.

Sector consensus is heavily bearish across all five major sectors (Technology 28% bullish, Energy 14%). Whether that's signal or noise is your call to make.

---

**Methodology and full leaderboard at stockarithm.com.**