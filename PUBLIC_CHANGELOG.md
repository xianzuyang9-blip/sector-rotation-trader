# Public Changelog

This is the public-facing product changelog for StockArithm.

It is intentionally selective. It records meaningful product, methodology, data-hygiene, and ops changes that affect what a reader sees or how the lab should be interpreted.

It is not a raw git log.

For signal inventory changes, see `ALGO_CHANGELOG.md`.

For the full engineering log, see `CHANGELOG.md`.

## Entry Rules

- Log user-visible product changes.
- Log methodology changes that affect interpretation.
- Log data-hygiene changes that change trust in the board.
- Log ops changes only when they materially affect public reliability.
- Do not log every daily run.
- Do not log routine content generation.

## 2026-05-25

### Data Hygiene
- Hardened the Reddit content bundle generator so Reddit bodies can no longer collapse into placeholder output like `BODY`.
- Added validation to keep the Reddit first comment short and operational instead of accidentally duplicating the whole post.

### Content
- Tightened the Substack content gate so long-form pieces have to read like self-contained essays instead of thin summaries.
- Added bounded retry logic to the content generator so weak drafts get rewritten before they are committed.

## 2026-05-24

### Transparency
- Backfilled plain-English descriptions across existing algo pages so a non-quant reader can understand what each signal is trying to do.

### Product
- Added the first schedule-driven `marketing/content/` bundle flow for X, Reddit, Medium, Substack, and Substack Notes.
- Added hook QA for X hooks and Reddit title candidates so weak summary hooks do not win by default.

## 2026-05-23

### Product
- Added a hidden-but-public `angel-algo` page for direct access to a private set of algo links without wiring it into the main navigation.

### Site
- Fixed the footer link treatment so `Biscotti` remains the visible footer link and `R&B AlgoLabs` stays in the powered-by attribution.

## 2026-05-20

### Data Hygiene
- Eliminated duplicate algo IDs in the ranking and rolling-30D pipelines.
- Made duplicate display names explicit with `alt` labeling instead of silently reusing the same visible name.
- Updated deep validation reporting to surface unique algo counts and rolling-only population differences clearly.

### Ops
- Disabled the old Google Drive push path in this repo and simplified the overnight workflow to the report path only.

## 2026-05-15

### Brand
- Added the first StockArithm logo asset so the product had a consistent visual mark across site and launch surfaces.

### Content
- Added the initial StockArithm content architecture docs and operating guide so long-form content, channel derivatives, and public-facing copy all had an explicit contract instead of ad hoc prompts.
