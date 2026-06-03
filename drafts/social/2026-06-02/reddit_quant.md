# StockArithm Lab Report: 118 Days In, 1 Algo Beating SPY (Force Rank)

We're running 374 live paper-trading signals across 105 tickers. Today's snapshot: **one algorithm is outperforming SPY on a full-window basis. Three are ahead on rolling 30-day momentum.** The rest are underwater. This is the point.

## The Leaderboard Split

**Force rank** (cumulative since seed, 118 days):
- **Quantified Simple Monthly Rotation** (+15.21% YTD, +3.87% alpha vs. SPY's +11.34%) sits alone at rank 1.
- Baileymol, DMSR, Faber, and Retail Sales Momentum all trail SPY by 3–6 percentage points.
- Electricity Consumption anchors the bottom at –7.25% YTD, –18.59% alpha.
- **Beat rate: 1 of 374 (0.27%).**

**Rolling 30-day momentum** (last 30 calendar days):
- Simple Monthly Rotation leads again: +13.53% (Sharpe 4.24), +7.89% delta to SPY's +5.64%.
- VIX Fear Rotation and VIX Term Structure both hit +8.3%, outpacing SPY by ~2.6 percentage points.
- Retail Sales Momentum and Job Posting Acceleration show positive 30D returns but negative SPY deltas.
- **Beat rate: 3 of 375 (0.80%).**

The divergence matters. Liquor Store Leading Indicator, Mortgage Rate Housing Proxy, and Consumer Sentiment are all negative on both windows—they're not mean-reverting; they're just wrong.

## Data Sources & Methodology Transparency

These signals ingest FRED macroeconomic data (retail sales, employment, mortgage rates), TSA passenger volumes, Reddit sentiment aggregates, Google Trends job-opening searches, VIX term structure, and sector price momentum. Each algo is a distinct hypothesis about market microstructure or macro regime.

**Critical limitation:** 118 days is not statistically significant. A single algo beating SPY over four months could be luck. We're publishing this anyway because the methodology—not the returns—is the product. We show losses as loudly as wins.

## Notable Divergences

Three algos show rank gaps worth flagging:

1. **Daily Rise In Freightlogistics Google Trends** (force rank 357, rolling 30D rank 15): Recent strength in labor-supply signals despite weak full-window performance.
2. **Price Momentum Reversion In Defensive Sectors** (force rank 28, rolling 30D rank 317): Worked early; has stalled hard in the last month.
3. **Google Trends Surge In Logistics Job Openings** (force rank 336, rolling 30D rank 48): Another labor-shortage proxy showing recent traction.

These divergences suggest regime shift—macro signals that worked in Q1 are failing now.

## Sector Consensus

All five major sectors are bearish by composite vote. Technology (XLK) shows the highest bullish percentage at 28% (13 of 46 algos), but that's still a 2:1 bearish lean. Consumer Defensive (XLP) is the most pessimistic at 15% bullish.

## What This Isn't

This is not a track record. It's a live laboratory. We're not claiming edge; we're documenting methodology and failure in public. The 0.27% beat rate on force rank is a humbling baseline. If you're reading this as a quant, you already know: sample size N=118 days, single-algo outperformance, and no statistical significance test. Ask the hard questions.

**Methodology and full leaderboard at stockarithm.com.**