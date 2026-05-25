I built StockArithm because I got tired of watching smart people defend bad signals with good stories.

Three years ago, I was running a small quant shop. We'd backtest something, it'd look clean, we'd paper trade it, and then—six months in—it'd crater. The postmortem was always the same: "The regime changed" or "We didn't account for X." But we never published the failures. We just moved on to the next idea.

That bothered me. Not because I'm noble. Because I realized I couldn't tell the difference between a signal that was actually broken and one that was just unlucky in a small sample.

So I started building a public lab. The rule was simple: every signal gets ranked. Every failure stays visible. No cherry-picking. No narrative cleanup.

Today, 344 signals are running live. One is beating SPY. That's it.

The winner—"Quantified Simple Monthly Rotation"—is up 13.09% YTD versus SPY's 9.44%. It's been running 112 days. It has a 30-day Sharpe of 5.46 and a max drawdown of 3.5%. Those are real numbers. But 112 days is not a career. It's a data point.

The other 343 signals are losing. Some by a little (Faber Momentum at -1.17% alpha). Some by a lot (Copper Momentum at -11.24% alpha). A few are "crazy" signals—things like Port Container Volume or VIX Fear Rotation—that I built to test whether alternative data could work. Most of them don't.

Here's what matters for this subreddit: the sample size problem is *visible*. You can see that VIX Fear Rotation ranks #2 on the rolling 30-day board but #342 on the full-window force rank. That's not a bug. That's a feature. It tells you something real about regime dependence and overfitting risk.

The lab exists because I needed to answer a specific question: can I build a system that tells me which signals are actually working versus which ones are just lucky? The answer so far is: barely. One winner out of 344 is not a system. It's a lottery ticket.

But it's an *honest* lottery ticket. Every algo is ranked the same way. Every failure is public. The board updates daily. You can see the divergences—signals that crush the last 30 days but tank over the full window. You can see the sector consensus (currently bearish across all major sectors). You can see the equity curves.

I'm not selling anything. I'm not claiming edge. I'm publishing the work because the quant community needs more public failure data, not less. Most of what gets published is the one signal that worked. This is the 344 that didn't, plus the one that did.

If you want to dig into the methodology, the full board is public. If you want to build on top of it, the data is there. If you want to tell me why 343 of these are garbage, I'm listening.

That's why StockArithm exists.
