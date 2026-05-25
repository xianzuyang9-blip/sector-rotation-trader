# Algo Changelog

This is the signal-board changelog for StockArithm.

It tracks changes to the algo inventory itself:

- added algos
- renamed algos
- retired algos
- metadata or display changes that affect how a signal appears on the public board

It is not the place for site copy, content-system, or workflow changes. Those belong in `PUBLIC_CHANGELOG.md`.

## Entry Rules

- Log batch additions when they materially change board size or coverage.
- Log renames that affect public display.
- Log retirements, graveyard moves, or major status changes.
- Log large metadata backfills when they change how the board is read.
- Do not log every nightly stat change.

## 2026-05-24

### Added
- Latest daily signal batch brought the public board to `344` live signals across `105` tickers.

### Metadata
- Backfilled plain-English descriptions for older signals so existing algo detail pages now explain the signal intent in readable language.

## 2026-05-20

### Hygiene
- Removed duplicate algo IDs from the force-rank and rolling-30D layers so every public row now maps to a unique signal identity.

### Renamed
- Duplicate visible names now use explicit `alt` suffixes instead of silently sharing the same public label.
- Example: duplicate Biscotti variants now render with distinct labels instead of appearing as the same signal twice.

## 2026-05-19

### Added
- Public board expanded to `292` generated signals across `105` tickers.

## 2026-05-18

### Added
- Public board held at `278` generated signals across `105` tickers while the rolling board continued to track `279` live rows.

## 2026-05-15

### Added
- Public board reached `278` generated signals across `105` tickers.

### Metadata
- Daily content and launch-copy layers were generated against the live board so the early launch surfaces reflected the actual signal population instead of stale placeholder numbers.

## Operating Format

Use this structure for future entries:

```text
## YYYY-MM-DD

### Added
- Signal family or batch summary.

### Renamed
- Old visible name -> new visible name.

### Retired
- Signal name and short reason.

### Metadata
- Public-facing description/status/family changes.
```
