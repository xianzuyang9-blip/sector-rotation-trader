# StockArithm Content Mechanism

## The Goal

**Primary:** Build trust and analyst credibility by publishing public, testable market ideas with visible winners and losers.

**Secondary:** Create qualified traffic and returning readers who understand the lab, the process, and the limits.

**Tertiary:** Earn downstream product pull when a signal, explanation, or pattern is strong enough to matter.

## The Home Base

**The repo is the source of truth.**

StockArithm content should be generated from validated artifacts and not from memory, vibes, or post-hoc storytelling.

Everything else feeds from that.

## The Content Loop

```text
validated facts
  -> content generator
  -> per-channel drafts
  -> review / copy / publish
  -> feedback
  -> improved rules
```

The content system is a formatting layer, not a trading layer.

It does not invent metrics.
It does not change the lab.
It does not hide failures.

## Operating Rule

If it is not in the validated facts package, it does not exist.

That means:

- no invented returns;
- no invented reasons;
- no invented certainty;
- no pretending a short sample is proof.

The content layer can interpret, but it cannot fabricate.

## The Output Contract

For any post date and slug, emit a dispatcher-ready bundle:

```text
marketing/content/{YYYY-MM-DD}-{slug}/
  meta.json
  x.md
  medium.md
  substack.md
  substack_note.md
  reddit_algotrading.md
  reddit_algotrading_titles.md
  reddit_algotrading_first_comment.txt
  reddit_investing.md
  reddit_investing_titles.md
  reddit_investing_first_comment.txt
  reddit_stocks.md
  reddit_stocks_titles.md
  reddit_stocks_first_comment.txt
  reddit_quant.md
  reddit_quant_titles.md
  reddit_quant_first_comment.txt
  reddit_security_analysis.md
  reddit_security_analysis_titles.md
  reddit_security_analysis_first_comment.txt
```

If a channel is not used for a given post, the file can be omitted or marked `skip` in `meta.json`, but the schema should stay stable.

## Status File

Each bundle should include a `meta.json` that tells the dispatcher:

- what the post is;
- when it should run;
- which channels are ready;
- which Reddit targets are included;
- which files to post.

The dispatcher should own posting and write-back status.
The generator should own preparation.

## Hook QA Layer

The hook QA layer exists to keep weak openings and weak Reddit titles out of the bundle by default.

It applies most directly to:

- `x.md`
- `substack_note.md`
- `reddit_*_titles.md`

The generator should:

- create a few candidate hooks from the schedule row and validated facts;
- score the candidates deterministically;
- select the strongest hook that still matches the channel;
- write the selected hook into `meta.json` for inspection.

The scoring should reward:

- curiosity;
- tension;
- contradiction when the facts support it;
- short, specific phrasing;
- numbers when they strengthen the hook.

The scoring should penalize:

- soft summary language;
- internal taxonomy language;
- generic marketing phrasing;
- hooks that are too literal to create curiosity.

## Channel Roles

| Channel | Purpose | Role |
|---------|---------|------|
| X | Short hook and reach | Fast, sharp, direct. Tease the longer Substack piece. |
| Medium | Secondary funnel | Optional broader reach and teaser surface. |
| Substack | Home base | Full long-form article, self-contained premise validation, and canonical CTA to `https://www.stockarithm.com`. |
| Substack Note | Discovery | Short teaser or question. |
| Reddit | Community discussion | Targeted, subreddit-specific version with no links in the body. First comment can carry the outbound link manually. |

## What The Generator Should Do

The generator should:

- read the validated facts;
- choose the right theme or angle;
- write channel-specific drafts;
- write the `meta.json`;
- keep the output folder self-contained;
- leave posting to the dispatcher.

Channel-specific link rules:

- `substack.md` is the canonical long-form article and should link back to `https://www.stockarithm.com`.
- `substack.md` must be self-contained: it needs its own context, premise, and explanation of why the reader should care.
- `substack.md` must not depend on prior knowledge of StockArithm, the dashboard, or the internal repo structure.
- If the draft is only a thin summary of the schedule row or the leaderboard, the generator should treat it as incomplete.
- `reddit_*.md` bodies must be link-free and native to the subreddit.
- `reddit_*_first_comment.txt` exists for the manual outbound link after posting.
- `x.md` should be short and controversial enough to push the reader to the longer piece.
- `medium.md` should act as a teaser/discovery surface, not a second canonical home.

Substack quality gate:

- The generator should only consider a Substack draft complete if it can stand alone as an essay.
- The article should answer: what StockArithm is, why it exists, what the evidence says, and why it matters.
- If the output reads like a post-it note for the operator, it should fail the content gate.

## What The Generator Should Not Do

The generator should not:

- post directly;
- guess channel credentials;
- invent facts;
- create a new schema per repo;
- force the operator to copy/paste between systems.

## Success Condition

The system is working if:

- the draft bundle can be picked up by the dispatcher without hand editing;
- the copy feels native to the target channel;
- the content stays honest when the signal is ugly;
- the operator can scale across multiple products without living on social media.

## Final Rule

The content system exists to turn validated truth into channel-ready drafts, not to become another job.

If the output is not dispatcher-ready, it is not done.
