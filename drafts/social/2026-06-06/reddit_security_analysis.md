# StockArithm's 122-Day Test: When Sector Rotation Signals Underperform the Broad Market

Over the past four months, StockArithm has been running 419 distinct sector rotation algorithms—each built on a different economic leading indicator thesis—in live paper trading. The results offer a sobering lesson in signal validation: **zero algorithms are beating SPY on a force-ranked basis**, and the median performer is trailing the broad market by 3–6 percentage points year-to-date.

This is exactly the kind of failure the lab publishes openly.

## The Thesis Under Test

The core premise is sound: economic leading indicators—TSA checkpoint counts, initial jobless claims, the misery index, copper momentum, dark pool activity, even liquor store traffic—should predict sector rotation before price action confirms it. If housing starts spike, industrials should lead. If the yield curve flattens, utilities should outperform. These are not exotic ideas; they're standard macro playbooks.

Yet across 122 days of live execution, the algos built on these signals have collectively underperformed. Algo Baileymol (Chaos Monger), the top force-ranked performer, returned 8.16% YTD against SPY's 8.25%—a -9 basis point alpha. The second-ranked Quantified Simple Monthly Rotation sits at 6.11% YTD. By the fifth-ranked slot, Faber Momentum Rotation has delivered only 2.4%.

## The Divergence Problem

What's instructive is the *divergence* between long-window and recent performance. Faber Momentum Rotation ranks 5th on force (full-window), but 416th on the rolling 30-day leaderboard, with a -2.08% return in the last month. Conversely, VIX Fear Rotation ranks 417th on force but 3rd on the 30-day window, returning +1.04% recently despite -3.56% YTD.

This suggests the leading indicators are *timing-dependent*. A signal that worked in February may have stopped working in May. The economic regime shifted—perhaps inflation expectations changed, or Fed policy signaling altered sector flows—and the algos didn't adapt fast enough.

## What's Working (Barely)

Algo Biscotti (Unconditional Loyalty) leads the 30-day rankings with +1.73% return and a 0.73 Sharpe ratio, outperforming SPY by 122 basis points in the last month. This suggests that *some* rotation logic is capturing recent market microstructure, even if the full-window thesis has lagged.

The sector consensus from the lab's 48 precomputed signals is uniformly bearish: Utilities (XLU) shows the highest bullish conviction at just 25%, while Technology (XLK) and Basic Materials (XLB) sit at 19%. This alignment across bearish calls is notable—it suggests the leading indicators are *agreeing* on direction, even if that direction hasn't yet translated to outperformance.

## The Lesson

StockArithm's transparency here is the differentiator. Most quant shops hide underperforming models. This lab publishes them. The question for fundamental analysts isn't whether these signals are perfect—they're not—but whether the *economic rationale* remains sound and whether the recent 30-day divergence signals a regime reset worth monitoring.

Full signal methodology and sector consensus at stockarithm.com.