# StockArithm Lab Report: 332 Signals Running, Only 4 Beating SPY

We're running 332 algorithmic signals across 105 tickers in our public paper-trading lab. Today's snapshot: **only 4 of them are beating SPY year-to-date**. That's the reality of testing alternative-data rotation strategies at scale.

## What's Working (Barely)

**Quantified Simple Monthly Rotation** is the only signal beating SPY meaningfully. It's up 13.09% YTD versus SPY's 9.44%—a 3.64% alpha. Over the last 30 days, it returned 13.09% while SPY returned 4.84%, with a Sharpe ratio of 5.36. That's the outlier. The other three beating SPY are marginal.

The rest? Baileymol (Chaos Monger) is down 0.8% relative to SPY. Faber Momentum Rotation is -1.17%. Antonacci Dual Momentum Sector Rotation is -2.55%. These aren't tiny misses—they're real underperformance.

## The Failures Are Public

This is what makes the lab different. We publish the losses.

**Copper Momentum** is down 11.24% relative to SPY. **Port Container Volume** is -11.62%. **VIX Fear Rotation** is -11.79% YTD. These signals measure real economic data—freight tonnage, port activity, volatility structure—but they're not working right now. We show that openly.

## The Divergence Worth Watching

Some signals are hot in the last 30 days but ice-cold for the year. **VIX Fear Rotation** ranks #2 over the past month (5.4% return, Sharpe 3.4) but sits at force rank 330 overall (down 2.35% YTD). That's a 328-rank gap. It suggests recent momentum in volatility-based rotation that hasn't held up historically.

Opposite story: **FINRA Dark Pool Signal** ranks #10 overall but dropped to #296 in the last 30 days. Full-window strength, recent weakness.

## Sector Consensus: Bearish Across the Board

Our 40 signals covering sector rotation are overwhelmingly bearish. Technology (XLK) shows only 28% bullish signals. Basic Materials (XLB) is 24%. Energy (XLE) is 14%. No sector is getting majority bullish votes.

## The Bottom Line

332 signals. 4 beating the market. The lab runs them all publicly because the failures teach you as much as the wins. Some measure economic data (tonnage, container volume, retail sales). Some measure market structure (dark pools, VIX term structure). Most aren't working.

Everything is public at stockarithm.com.