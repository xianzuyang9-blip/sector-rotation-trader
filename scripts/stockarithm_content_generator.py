#!/usr/bin/env python3
"""
stockarithm_content_generator.py

Generate dispatcher-ready StockArithm marketing bundles from:
- marketing_schedule.csv
- reports/deep_validation/latest.json (or a dated report)

Output shape:
  marketing/content/YYYY-MM-DD-slug/
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

Usage:
    python scripts/stockarithm_content_generator.py
    python scripts/stockarithm_content_generator.py --date 2026-05-23
    python scripts/stockarithm_content_generator.py --dry-run
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from datetime import date
from pathlib import Path

try:
    import anthropic
except ModuleNotFoundError:  # pragma: no cover - handled at runtime
    anthropic = None

MODEL = os.getenv("ANTHROPIC_MODEL") or "claude-haiku-4-5-20251001"
REPORTS_DIR = Path("reports/deep_validation")
SCHEDULE_FILE = Path("marketing_schedule.csv")
OUTPUT_ROOT = Path("marketing/content")
BRAND = "StockArithm"
DEFAULT_TIME = "09:30"
DEFAULT_TZ = "America/New_York"


def _slugify(value):
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-")


def _load_report(run_date):
    dated = REPORTS_DIR / f"{run_date}.json"
    latest = REPORTS_DIR / "latest.json"
    for path in (dated, latest):
        if path.exists():
            try:
                return json.loads(path.read_text())
            except Exception:
                continue
    return {}


def _build_facts_block(report):
    cf = report.get("content_facts", {})
    ss = report.get("system_state", {})
    fr = report.get("force_rank", {})
    r30 = report.get("rolling_30d", {})
    sc = report.get("sector_consensus", {})

    facts = {
        "report_date": report.get("report_date"),
        "generated_at": report.get("generated_at"),
        "system_state": {
            "total_force_ranked": ss.get("total_force_ranked"),
            "beating_spy_force_rank": ss.get("beating_spy_force_rank"),
            "rolling_30d_algos": ss.get("rolling_30d_algos"),
            "rolling_30d_beating_spy": ss.get("rolling_30d_beating_spy"),
            "signals_generated": ss.get("signals_generated"),
            "tickers_covered": ss.get("tickers_covered"),
        },
        "top_force_ranked": (fr.get("top_10") or [])[:5],
        "bottom_force_ranked": (fr.get("bottom_5") or [])[:3],
        "top_rolling_30d": (r30.get("top_10") or [])[:5],
        "bottom_rolling_30d": (r30.get("bottom_5") or [])[:3],
        "spy_ret_30d": r30.get("spy_ret_30d"),
        "signal_of_day": cf.get("signal_of_day"),
        "failure_of_day": cf.get("failure_of_day"),
        "call_of_day": cf.get("call_of_day"),
        "notable_divergences": (cf.get("notable_divergences") or [])[:3],
        "sector_consensus": (sc.get("sectors_ranked") or [])[:5],
    }
    return json.dumps(facts, indent=2)


def _load_schedule_row(run_date):
    if not SCHEDULE_FILE.exists():
        return None

    with SCHEDULE_FILE.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        matches = []
        for row in reader:
            if row.get("date") != run_date:
                continue
            status = (row.get("status") or "").strip().lower()
            if status not in {"scheduled", "ready"}:
                continue
            matches.append(row)

    if not matches:
        return None
    if len(matches) > 1:
        raise RuntimeError(f"multiple schedule rows found for {run_date}")
    return matches[0]


def _split_list(value):
    if not value:
        return []
    parts = re.split(r"[;,]", value)
    return [part.strip() for part in parts if part.strip()]


def _top_force_item(report):
    force_rank = report.get("force_rank") or {}
    top_10 = force_rank.get("top_10") or []
    return top_10[0] if top_10 else {}


def _top_rolling_item(report):
    rolling = report.get("rolling_30d") or {}
    top_10 = rolling.get("top_10") or []
    return top_10[0] if top_10 else {}


def _count_value(report, key):
    system_state = report.get("system_state") or {}
    value = system_state.get(key)
    return int(value) if isinstance(value, (int, float)) else 0


def _pluralize(count, singular, plural=None):
    if count == 1:
        return singular
    return plural or f"{singular}s"


def _hook_quality_score(text, channel_key):
    score = 0
    cleaned = re.sub(r"\s+", " ", text.strip())
    lower = cleaned.lower()
    length = len(cleaned)

    if not cleaned:
        return -999

    # Core qualities
    if any(word in lower for word in ("why", "what", "how", "wrong", "still", "fail", "losing", "visible", "public", "beating", "but", "yet")):
        score += 4
    if re.search(r"\d", cleaned):
        score += 3
    if "spy" in lower:
        score += 2
    if "stockarithm" in lower:
        score += 1 if channel_key in {"x", "substack_note"} else 0

    # Length / fit
    if channel_key == "x":
        if length <= 280:
            score += 5
        if length <= 140:
            score += 3
        if 40 <= length <= 120:
            score += 2
        if length < 25:
            score -= 2
    else:
        if 30 <= length <= 120:
            score += 2
        if length > 180:
            score -= 1

    # Penalize soft or internal-language hooks
    if lower.startswith(("we ", "here's ", "here is ", "this post", "daily update", "summary", "report", "launch", "product")):
        score -= 4
    if any(word in lower for word in ("proprietary", "seamless", "game-changing", "cutting-edge", "synergy", "solution")):
        score -= 6
    if any(word in lower for word in ("taxonomy", "ledger", "pipeline", "backtest", "notebook")) and channel_key in {"x", "reddit"}:
        score -= 2

    return score


def _select_best_hook(candidates, channel_key):
    ranked = sorted(
        [c for c in candidates if c],
        key=lambda item: (-_hook_quality_score(item, channel_key), len(item), item.lower()),
    )
    if not ranked:
        return ""
    return ranked[0]


def _render_reddit_title_options(channel_key, report, row):
    candidates = _reddit_title_candidates(channel_key, report, row)
    ranked = sorted(
        [c for c in candidates if c],
        key=lambda item: (-_hook_quality_score(item, "reddit"), len(item), item.lower()),
    )
    return ranked[:5]


def _x_hook_candidates(report, row):
    top_force = _top_force_item(report)
    top_name = top_force.get("name") or "the top signal"
    beat_spy = _count_value(report, "beating_spy_force_rank")
    total = _count_value(report, "total_force_ranked")
    losers = max(total - beat_spy, 0)
    title = row.get("title") or "StockArithm"
    verb = "is" if beat_spy == 1 else "are"
    return [
        f"{beat_spy} of {total} signals {verb} beating SPY. The losers stay visible.",
        f"{top_name} is still #1, but the board is the real story.",
        f"The point of StockArithm is not a polished backtest. It is a public board.",
        f"{title}: the premise matters less than what the board keeps showing.",
        f"{losers} signals are not beating SPY. That is the part worth reading.",
    ]


def _substack_note_candidates(report, row):
    top_force = _top_force_item(report)
    top_name = top_force.get("name") or "the top signal"
    total = _count_value(report, "total_force_ranked")
    beat_spy = _count_value(report, "beating_spy_force_rank")
    winner_word = _pluralize(beat_spy, "winner")
    return [
        f"One public board, {beat_spy} {winner_word}, {total - beat_spy} losers. That is the point.",
        f"{top_name} is still the cleanest winner, but the board is the better story.",
        f"StockArithm exists to keep the failures visible, not hide them.",
        f"The interesting part is not the winner; it is how the full board behaves.",
    ]


def _reddit_title_candidates(channel_key, report, row):
    top_force = _top_force_item(report)
    top_name = top_force.get("name") or "the top signal"
    beat_spy = _count_value(report, "beating_spy_force_rank")
    total = _count_value(report, "total_force_ranked")
    failure_count = max(total - beat_spy, 0)
    title = row.get("title") or "StockArithm"
    winner_word = _pluralize(beat_spy, "winner")
    verb = "is" if beat_spy == 1 else "are"

    shared = [
        f"{beat_spy} of {total} signals {verb} beating SPY. Here is the full public board.",
        f"I built a public sector-rotation lab and kept every failure visible.",
        f"The label can be wrong and the signal can still work.",
    ]

    if channel_key == "reddit_algotrading":
        return shared + [
            f"{top_name} is #1, but the more interesting number is {failure_count} losing signals.",
            "How I keep a public paper-trading board honest when most ideas fail",
        ]
    if channel_key == "reddit_investing":
        return shared + [
            f"{title} — a public paper-trading lab for alternative data signals",
            "Why I think visible losses matter more than pretty backtests",
        ]
    if channel_key == "reddit_stocks":
        return shared + [
            f"One winner, a lot of losers, and a public board I can’t hide",
            f"{beat_spy} {winner_word} out of {total} signals. That is the whole story.",
        ]
    if channel_key == "reddit_quant":
        return shared + [
            f"{total} paper-traded signals, {beat_spy} above SPY, and the sample size is still small",
            "What a public sector-rotation lab can and cannot tell you",
        ]
    if channel_key == "reddit_security_analysis":
        return shared + [
            f"Why a public alternative-data sector lab is really a thesis test",
            "How visible failures change the way I think about signal quality",
        ]
    return shared


def _parse_reddit_bundle(text):
    body = _extract_named_section(text, "body", ["first comment"])
    first_comment = _extract_named_section(text, "first comment", [])
    if body and first_comment:
        return _normalize_reddit_sections(body, first_comment)

    # Fallback: accept a simple two-paragraph structure if the model omits markers.
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    if len(paragraphs) >= 2:
        body = paragraphs[0]
        first_comment = "\n\n".join(paragraphs[1:]).strip()
        return _normalize_reddit_sections(body, first_comment)

    # Final fallback: keep the body and synthesize a short first comment so the
    # bundle can still be generated and committed.
    return _normalize_reddit_sections(
        text.strip(),
        "Full write-up in the first comment once the draft is posted.",
    )


def _is_named_heading(line, name):
    normalized = re.sub(r"^[#>\-\s]+", "", line.strip())
    normalized = normalized.rstrip(":").strip().lower()
    return normalized == name.lower()


def _extract_named_section(text, section_name, next_sections):
    lines = text.splitlines()
    start = None
    for idx, line in enumerate(lines):
        if _is_named_heading(line, section_name):
            start = idx + 1
            break
    if start is None:
        return ""

    end = len(lines)
    for idx in range(start, len(lines)):
        if any(_is_named_heading(lines[idx], section) for section in next_sections):
            end = idx
            break
    return "\n".join(lines[start:end]).strip()


def _strip_leading_reddit_heading(text):
    lines = text.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    if lines and _is_named_heading(lines[0], "body"):
        lines = lines[1:]
    if lines and _is_named_heading(lines[0], "first comment"):
        lines = lines[1:]
    return "\n".join(lines).strip()


def _word_count(text):
    return len(re.findall(r"\b[\w'-]+\b", text))


def _normalize_reddit_sections(body, first_comment):
    body = _strip_leading_reddit_heading(body)
    first_comment = _strip_leading_reddit_heading(first_comment)

    body_words = _word_count(body)
    first_comment_words = _word_count(first_comment)

    # If the model dumped the real post into FIRST COMMENT and left BODY empty,
    # recover the post instead of committing a garbage bundle.
    if body_words < 40 and first_comment_words >= 120:
        body = first_comment
        first_comment = "Linking the full write-up in the first comment after posting."

    # Keep first comments short and operational rather than duplicating the post.
    if first_comment_words > 120:
        first_comment = "Linking the full write-up in the first comment after posting."

    return body.strip(), first_comment.strip()


def _channel_prompt(channel_key, schedule_row, selected_hook=None, title_options=None):
    title = schedule_row["title"]
    theme = schedule_row["theme"]
    notes = schedule_row.get("notes") or ""

    shared = """\
Hard rules:
- Use ONLY facts present in the JSON data block and schedule row. Do not invent metrics, returns, or causes.
- StockArithm is the brand. Never write "Stockarithm".
- stockarithm.com is the URL. Use it only if it fits the channel.
- Show wins and failures honestly. No hype. No investment advice.
- Keep the tone human, specific, and evidence-based.
"""

    if channel_key == "x":
        return f"""\
You are writing a single X post for StockArithm.

{shared}

Context:
- title: {title}
- theme: {theme}
- notes: {notes}

Selected hook: {selected_hook or "n/a"}

Write one tweet only, under 280 characters, with one sharp observation and a light CTA. If possible, open with the selected hook or a very close variant that preserves the same tension. Hint toward the longer Substack piece, but do not force a URL.
Return plain text only.
"""

    if channel_key == "medium":
        return f"""\
You are writing a Medium article for StockArithm.

{shared}

Context:
- title: {title}
- theme: {theme}
- notes: {notes}

Selected hook: {selected_hook or "n/a"}

Write a polished, readable Medium article with a clear title on the first line, 3-5 short sections, and a practical closing. Keep it honest and useful, not marketing copy. This should act as a teaser / discovery surface for the canonical Substack article.
Length: 700-1100 words.
Return markdown only.
"""

    if channel_key == "substack":
        return f"""\
You are writing a Substack post for StockArithm.

{shared}

Context:
- title: {title}
- theme: {theme}
- notes: {notes}

Selected hook: {selected_hook or "n/a"}

Write the canonical long-form post. Put the title on the first line, then the body.

This draft must be a complete essay, not a summary fragment.
It must stand on its own for a reader who has never seen StockArithm before.

Required content:
- explain what StockArithm is in plain English;
- explain why it exists or why the question matters;
- explain what the current evidence says;
- include at least one concrete example, contrast, or failure mode;
- explain what the reader should take away;
- end with a short CTA that links back to https://www.stockarithm.com.

Structure guidance:
- use 3-6 short sections with headings;
- make the first section immediately orient the reader;
- keep the writing like a real analyst's field note, not a teaser or a memo;
- do not assume prior knowledge of the repo, dashboard, or internal workflow.

Length: 900-1300 words.
Return markdown only.
"""

    if channel_key == "substack_note":
        return f"""\
You are writing a Substack Note for StockArithm.

{shared}

Context:
- title: {title}
- theme: {theme}
- notes: {notes}

Selected hook: {selected_hook or "n/a"}

Write a short note: 2-4 sentences, sharp and readable, ending with a real question when possible. Keep it discovery-oriented, not salesy. It should support the canonical Substack article, not replace it.
Return plain text only.
"""

    reddit_prompts = {
        "reddit_algotrading": (
            "r/algotrading",
            "engineers, quant hobbyists, algo traders. Highly skeptical. Lead with methodology and failure rate.",
            400,
        ),
        "reddit_investing": (
            "r/investing",
            "general retail investors. More accessible than r/algotrading. Lead with what the signals measure and how they performed.",
            300,
        ),
        "reddit_stocks": (
            "r/stocks",
            "casual retail stock traders. Numbers first, short, direct, zero jargon.",
            200,
        ),
        "reddit_quant": (
            "r/quant",
            "quants, statisticians, finance academics. Be explicit about sample size limits and methodology.",
            450,
        ),
        "reddit_security_analysis": (
            "r/SecurityAnalysis",
            "fundamental analysts and macro-focused readers. Frame the post around sector-rotation rationale and economic logic.",
            350,
        ),
    }
    if channel_key in reddit_prompts:
        subreddit, audience, length = reddit_prompts[channel_key]
        return f"""\
You are writing a Reddit post for {subreddit} for StockArithm.

{shared}

Audience: {audience}

Context:
- title: {title}
- theme: {theme}
- notes: {notes}
- selected title option: {selected_hook or "n/a"}
- title candidates:
{title_options or "n/a"}

Write a post tailored to the subreddit. Output exactly these sections:

BODY:
...

FIRST COMMENT:
...

Rules:
- Do not use markdown heading markers like "# BODY" or "## FIRST COMMENT". Use the plain labels exactly once.
- The BODY must be native-value and link-free.
- The BODY must contain the actual post, not a placeholder heading.
- Do not include any URLs in the BODY.
- Do not include stockarithm.com or substack.com in the BODY.
- The FIRST COMMENT must be short: 1-2 sentences only. It is not the post body.
- The FIRST COMMENT can hold the link placeholder for the later manual post or the actual outbound link text.
- The selected title should be the hook QA winner from the title candidates above.
Length: {length} to 550 words depending on the subreddit.
Return markdown/plain text only.
"""

    raise KeyError(channel_key)


CHANNEL_ORDER = [
    "x",
    "medium",
    "substack",
    "substack_note",
    "reddit_algotrading",
    "reddit_investing",
    "reddit_stocks",
    "reddit_quant",
    "reddit_security_analysis",
]


def _build_meta(run_date, row, bundle_dir, report, hook_qa=None):
    reddit_targets = _split_list(row.get("reddit_targets"))
    channels = _split_list(row.get("channels"))

    channel_meta = {}
    if "x" in channels:
        channel_meta["x"] = {"status": "ready", "file": "x.md", "link_policy": "substack_cta"}
    if "medium" in channels:
        channel_meta["medium"] = {"status": "ready", "file": "medium.md", "link_policy": "substack_teaser"}
    if "substack" in channels:
        channel_meta["substack"] = {
            "status": "ready",
            "file": "substack.md",
            "link_policy": "site_cta",
            "canonical_url": "https://www.stockarithm.com",
        }
    if "substack_note" in channels:
        channel_meta["substack_note"] = {"status": "ready", "file": "substack_note.md", "link_policy": "hook"}
    if "reddit" in channels and reddit_targets:
        channel_meta["reddit"] = {
            "status": "ready",
            "link_policy": "no_links_in_body",
            "subreddits": [
                {
                    "name": target,
                    "status": "ready",
                    "file": f"reddit_{target}.md",
                    "titles_file": f"reddit_{target}_titles.md",
                    "first_comment_file": f"reddit_{target}_first_comment.txt",
                }
                for target in reddit_targets
            ],
        }

    meta = {
        "post_id": f"{run_date}-{row['slug']}",
        "product": "stockarithm",
        "scheduled_date": run_date,
        "scheduled_time": row.get("scheduled_time") or DEFAULT_TIME,
        "timezone": row.get("timezone") or DEFAULT_TZ,
        "status": "ready",
        "title": row.get("title"),
        "slug": row.get("slug"),
        "theme": row.get("theme"),
        "source_report": str((REPORTS_DIR / f"{run_date}.json") if (REPORTS_DIR / f"{run_date}.json").exists() else REPORTS_DIR / "latest.json"),
        "bundle_path": str(bundle_dir),
        "channels": channel_meta,
    }
    if hook_qa:
        meta["hook_qa"] = hook_qa
    return meta


def _lint_draft(text, channel_key):
    if re.search(r"\{[^}]+\}", text):
        raise ValueError(f"{channel_key}: unresolved placeholder found")
    if "Stockarithm" in text:
        raise ValueError(f"{channel_key}: stale brand casing Stockarithm found")
    if channel_key == "x" and len(text) > 280:
        raise ValueError(f"{channel_key}: X draft exceeds 280 characters")
    if channel_key == "substack" and "stockarithm.com" not in text.lower():
        raise ValueError(f"{channel_key}: missing stockarithm.com URL")
    if channel_key == "substack":
        words = re.findall(r"\b[\w'-]+\b", text)
        if len(words) < 850:
            raise ValueError(f"{channel_key}: draft too short to qualify as a full essay")
        heading_count = len(re.findall(r"(?m)^##\s+\S", text))
        if heading_count < 3:
            raise ValueError(f"{channel_key}: draft needs at least 3 markdown section headings")
        lower = text.lower()
        concept_hits = 0
        if "stockarithm" in lower:
            concept_hits += 1
        if any(token in lower for token in ("sector rotation", "signal", "signals", "spy")):
            concept_hits += 1
        if any(token in lower for token in ("because", "matters", "exists", "failure", "loser", "winner", "evidence")):
            concept_hits += 1
        if concept_hits < 3:
            raise ValueError(f"{channel_key}: draft missing premise/context coverage")
        if any(phrase in lower for phrase in ("summary", "tl;dr", "note to self", "quick update")):
            raise ValueError(f"{channel_key}: draft reads like a summary fragment")
    if channel_key.startswith("reddit_"):
        cleaned = re.sub(r"^[#>\-\s]+", "", text.strip(), flags=re.MULTILINE).strip().lower()
        if cleaned in {"body", "first comment"} or len(text.strip()) < 80:
            raise ValueError(f"{channel_key}: Reddit body is too thin to publish")
        if re.search(r"https?://|www\.", text, re.IGNORECASE):
            raise ValueError(f"{channel_key}: Reddit body must not contain URLs")
        if "stockarithm.com" in text.lower():
            raise ValueError(f"{channel_key}: Reddit body must not contain stockarithm.com")


def _lint_reddit_first_comment(text, channel_key):
    words = _word_count(text)
    if words < 4:
        raise ValueError(f"{channel_key}: Reddit first comment is too thin")
    if words > 40:
        raise ValueError(f"{channel_key}: Reddit first comment is too long and is duplicating the post")


def _request_draft(client, prompt, user_message, channel_key):
    max_tokens = {
        "x": 256,
        "medium": 1400,
        "substack": 2600,
        "substack_note": 512,
        "reddit_algotrading": 1100,
        "reddit_investing": 900,
        "reddit_stocks": 700,
        "reddit_quant": 1300,
        "reddit_security_analysis": 1100,
    }[channel_key]

    message = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        temperature=0,
        system=prompt,
        messages=[{"role": "user", "content": user_message}],
    )
    return message.content[0].text.strip()


def _write_channel(client, channel_key, run_date, facts_block, row, bundle_dir, selected_hook=None, title_options=None):
    prompt = _channel_prompt(channel_key, row, selected_hook=selected_hook, title_options=title_options)
    base_user_message = (
        f"Schedule row for {run_date}:\n"
        f"{json.dumps(row, indent=2, sort_keys=True)}\n\n"
        f"Locked facts:\n```json\n{facts_block}\n```\n\n"
        f"Write the draft for {channel_key} now."
    )

    attempts = 3 if channel_key in {"substack", "medium"} or channel_key.startswith("reddit_") else 2
    draft = ""
    body = ""
    first_comment = ""
    last_error = None
    feedback = ""
    for _ in range(attempts):
        user_message = base_user_message + feedback
        draft = _request_draft(client, prompt, user_message, channel_key)
        try:
            if channel_key.startswith("reddit_"):
                body, first_comment = _parse_reddit_bundle(draft)
                _lint_draft(body, channel_key)
                _lint_reddit_first_comment(first_comment, channel_key)
            else:
                _lint_draft(draft, channel_key)
            last_error = None
            break
        except ValueError as exc:
            last_error = exc
            feedback = (
                "\n\nThe previous draft failed validation.\n"
                f"Failure: {exc}\n"
                "Rewrite from scratch and satisfy the failing requirement exactly.\n"
                "Do not summarize the prior draft. Produce a full replacement.\n"
            )
    if last_error is not None:
        raise last_error

    if channel_key.startswith("reddit_"):
        body_path = bundle_dir / f"{channel_key}.md"
        titles_path = bundle_dir / f"{channel_key}_titles.md"
        comment_path = bundle_dir / f"{channel_key}_first_comment.txt"
        body_path.write_text(body + "\n", encoding="utf-8")
        titles_path.write_text((title_options or "") + "\n", encoding="utf-8")
        comment_path.write_text(first_comment + "\n", encoding="utf-8")
        print(f"[stockarithm-content] wrote {body_path}")
        print(f"[stockarithm-content] wrote {titles_path}")
        print(f"[stockarithm-content] wrote {comment_path}")
        return

    filename = {
        "x": "x.md",
        "medium": "medium.md",
        "substack": "substack.md",
        "substack_note": "substack_note.md",
    }[channel_key]
    out_path = bundle_dir / filename
    out_path.write_text(draft + "\n", encoding="utf-8")
    print(f"[stockarithm-content] wrote {out_path}")


def generate(run_date, dry_run=False):
    row = _load_schedule_row(run_date)
    if not row:
        print(f"[stockarithm-content] no scheduled bundle for {run_date}")
        return

    report = _load_report(run_date)
    if not report:
        print(f"[stockarithm-content] no deep validation report found for {run_date}", file=sys.stderr)
        sys.exit(1)

    facts_block = _build_facts_block(report)
    bundle_dir = OUTPUT_ROOT / f"{run_date}-{row['slug']}"
    bundle_dir.mkdir(parents=True, exist_ok=True)

    x_candidates = _x_hook_candidates(report, row)
    x_hook = _select_best_hook(x_candidates, "x")
    note_candidates = _substack_note_candidates(report, row)
    note_hook = _select_best_hook(note_candidates, "substack_note")
    reddit_title_options = {}
    for target in _split_list(row.get("reddit_targets")):
        channel_key = f"reddit_{target}"
        reddit_title_options[target] = _render_reddit_title_options(channel_key, report, row)

    hook_qa = {
        "x": {"selected": x_hook, "candidates": x_candidates},
        "substack_note": {"selected": note_hook, "candidates": note_candidates},
        "reddit_titles": reddit_title_options,
    }

    meta = _build_meta(run_date, row, bundle_dir, report, hook_qa=hook_qa)

    if dry_run:
        print(f"[stockarithm-content] dry-run for {run_date}")
        print(json.dumps(meta, indent=2, sort_keys=True))
        channels = _split_list(row.get("channels"))
        if "reddit" in channels:
            for target in _split_list(row.get("reddit_targets")):
                print(f"  would write: {bundle_dir / f'reddit_{target}.md'}")
                print(f"  would write: {bundle_dir / f'reddit_{target}_titles.md'}")
                print(f"  would write: {bundle_dir / f'reddit_{target}_first_comment.txt'}")
        for key in ("x", "medium", "substack", "substack_note"):
            if key in channels:
                print(f"  would write: {bundle_dir / f'{key}.md'}")
        print(f"  selected x hook: {x_hook}")
        print(f"  selected substack note hook: {note_hook}")
        return

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("[stockarithm-content] ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)
    if anthropic is None:
        print("[stockarithm-content] anthropic module not installed", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    channels = _split_list(row.get("channels"))

    for channel_key in CHANNEL_ORDER:
        if channel_key.startswith("reddit_"):
            if "reddit" not in channels:
                continue
            target = channel_key.replace("reddit_", "")
            if target not in _split_list(row.get("reddit_targets")):
                continue
            title_options = reddit_title_options.get(target, [])
            selected_title = title_options[0] if title_options else ""
            _write_channel(
                client,
                channel_key,
                run_date,
                facts_block,
                row,
                bundle_dir,
                selected_hook=selected_title,
                title_options="\n".join(f"{idx + 1}. {title}" for idx, title in enumerate(title_options)),
            )
        else:
            if channel_key not in channels:
                continue
            selected_hook = x_hook if channel_key in {"x", "medium"} else note_hook if channel_key == "substack_note" else None
            _write_channel(
                client,
                channel_key,
                run_date,
                facts_block,
                row,
                bundle_dir,
                selected_hook=selected_hook,
            )

    (bundle_dir / "meta.json").write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"[stockarithm-content] wrote {bundle_dir / 'meta.json'}")


def main():
    parser = argparse.ArgumentParser(description="Generate dispatcher-ready StockArithm marketing bundles")
    parser.add_argument("--date", default=None, help="YYYY-MM-DD (default: today)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    run_date = args.date or date.today().isoformat()
    generate(run_date, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
