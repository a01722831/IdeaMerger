#!/usr/bin/env python3
"""Regenerate ideas/INDEX.md and ideas/scoreboard.csv from idea front matter.

Usage:
  python3 scripts/build_index.py            # rebuild indexes, print warnings
  python3 scripts/build_index.py --fix      # also rewrite each file's `total:` to the computed value
  python3 scripts/build_index.py --check    # QA mode: template sections, signal IDs, placeholders

Idea files: ideas/NNN-slug.md with YAML front matter (see ideas/_TEMPLATE.md).
Total = sum(weight x score) / 95 x 100.
"""
import argparse
import csv
import glob
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDEAS = os.path.join(ROOT, "ideas")
SIGNALS_FILES = [os.path.join(ROOT, "research", "SIGNALS.md")] + sorted(
    glob.glob(os.path.join(ROOT, "research", "tracks", "*.md"))
) + sorted(glob.glob(os.path.join(ROOT, "research", "landscape", "*.md")))

WEIGHTS = {
    "pain": 3,
    "evidence": 2,
    "ai_leverage": 2,
    "whitespace": 2,
    "novelty": 1,
    "why_now": 1,
    "solo_feasibility": 2,
    "distribution": 2,
    "wtp_economics": 2,
    "scale_defensibility": 2,
}
LABELS = {
    "pain": "Pain",
    "evidence": "Evidence",
    "ai_leverage": "AI leverage",
    "whitespace": "Whitespace",
    "novelty": "Novelty",
    "why_now": "Why now",
    "solo_feasibility": "Solo feasibility",
    "distribution": "Distribution",
    "wtp_economics": "WTP & economics",
    "scale_defensibility": "Scale & defensibility",
}
SECTIONS = [
    "One-liner", "Scores", "The problem", "Evidence", "The product", "Why the LLM is load-bearing",
    "The insight", "Why now", "Inspiration and derivation", "Competition check", "Business model",
    "Market size", "Go-to-market", "Moat and scale path", "Solo feasibility", "Pre-mortem",
    "Cheapest validation test", "Open questions",
]
COMP = {"WHITESPACE", "ADJACENT ONLY", "WEAK DIRECT", "CROWDED"}
CONF = {"HIGH", "MED", "LOW"}
PLACEHOLDER_RE = re.compile(r"\bTODO\b|\bTBD\b|\bFIXME\b|\[placeholder\]|lorem ipsum|\.\.\. \|", re.I)
SIGNAL_ID_RE = re.compile(r"\b([A-Z][A-Z0-9]{1,6}-\d{1,3})\b")


def compute_total(scores):
    raw = sum(WEIGHTS[k] * float(scores.get(k, 0)) for k in WEIGHTS)
    return round(raw / 95 * 100, 1)


def load(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError("missing YAML front matter")
    fm = yaml.safe_load(m.group(1)) or {}
    return fm, m.group(2), text


def known_signal_ids():
    ids = set()
    for p in SIGNALS_FILES:
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8") as f:
            for line in f:
                if line.startswith("|"):
                    cells = [c.strip() for c in line.strip().strip("|").split("|")]
                    if cells and SIGNAL_ID_RE.fullmatch(cells[0] or ""):
                        ids.add(cells[0])
                    # merged rows may list aliases like "HN-03 (=RED-12)"
                    for alias in SIGNAL_ID_RE.findall(cells[0] if cells else ""):
                        ids.add(alias)
    return ids


def md_escape(s):
    return str(s).replace("|", "/").replace("\n", " ").strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--dry-run", action="store_true", help="validate only; do not write INDEX.md or scoreboard.csv")
    ap.add_argument("--only", default="", help="validate only files whose name contains this substring")
    a = ap.parse_args()

    files = sorted(glob.glob(os.path.join(IDEAS, "[0-9][0-9][0-9]-*.md")))
    if a.only:
        files = [f for f in files if a.only in os.path.basename(f)]
    rows, warnings = [], []
    sig_ids = known_signal_ids()

    for path in files:
        rel = os.path.relpath(path, ROOT)
        try:
            fm, body, text = load(path)
        except Exception as e:  # noqa: BLE001
            warnings.append(f"{rel}: {e}")
            continue
        scores = fm.get("scores") or {}
        missing = [k for k in WEIGHTS if k not in scores]
        if missing:
            warnings.append(f"{rel}: missing scores {missing}")
        bad = [k for k, v in scores.items() if k in WEIGHTS and not (isinstance(v, (int, float)) and 1 <= v <= 5)]
        if bad:
            warnings.append(f"{rel}: scores out of range {bad}")
        total = compute_total(scores)
        if fm.get("total") is None or abs(float(fm.get("total", 0)) - total) > 0.05:
            warnings.append(f"{rel}: front matter total {fm.get('total')} != computed {total}")
            if a.fix:
                text = re.sub(r"(?m)^total:.*$", f"total: {total}", text, count=1)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(text)
        if str(fm.get("competition", "")).upper() not in COMP:
            warnings.append(f"{rel}: competition '{fm.get('competition')}' not in {sorted(COMP)}")
        if str(fm.get("confidence", "")).upper() not in CONF:
            warnings.append(f"{rel}: confidence '{fm.get('confidence')}' not in {sorted(CONF)}")
        one = str(fm.get("one_liner", ""))
        if len(one.split()) > 20:
            warnings.append(f"{rel}: one_liner has {len(one.split())} words (max 20)")
        sigs = fm.get("signals") or []
        if len(sigs) < 3:
            warnings.append(f"{rel}: fewer than 3 signals in front matter")
        if sig_ids:
            unknown = [s for s in sigs if s not in sig_ids]
            if unknown:
                warnings.append(f"{rel}: signal IDs not found in research files: {unknown}")
        if a.check:
            for i, sec in enumerate(SECTIONS, 1):
                if not re.search(rf"(?m)^##\s+{i}\.\s+{re.escape(sec)}", body):
                    warnings.append(f"{rel}: missing or misnumbered section '## {i}. {sec}'")
            for ln, line in enumerate(body.splitlines(), 1):
                if PLACEHOLDER_RE.search(line):
                    warnings.append(f"{rel}:{ln}: placeholder-like text: {line.strip()[:80]}")
            if "10. Competition check" in body:
                comp_sec = body.split("10. Competition check", 1)[1].split("## 11.", 1)[0]
                if len(re.findall(r"https?://", comp_sec)) < 2:
                    warnings.append(f"{rel}: competition check has fewer than 2 links")
        row = {
            "id": str(fm.get("id", "")),
            "slug": fm.get("slug", ""),
            "name": fm.get("name", ""),
            "file": os.path.basename(path),
            "one_liner": one,
            "target_user": fm.get("target_user", ""),
            "form_factor": fm.get("form_factor", ""),
            "lens": fm.get("lens", ""),
            "frontier": bool(fm.get("frontier", False)),
            "competition": str(fm.get("competition", "")).upper(),
            "confidence": str(fm.get("confidence", "")).upper(),
            "status": fm.get("status", ""),
            "signals": ";".join(sigs),
            "price_hypothesis": fm.get("price_hypothesis", ""),
            "model_cost_per_user_month": fm.get("model_cost_per_user_month", ""),
            "gross_margin": fm.get("gross_margin", ""),
            "mvp_weeks": fm.get("mvp_weeks", ""),
            "deep_dive": bool(fm.get("deep_dive", False)),
            "red_team": bool(fm.get("red_team", False)),
            "total": total,
        }
        for k in WEIGHTS:
            row[k] = scores.get(k, "")
        rows.append(row)

    live = [r for r in rows if r["status"] != "killed"]
    dead = [r for r in rows if r["status"] == "killed"]
    live.sort(key=lambda r: (-r["total"], r["id"]))
    dead.sort(key=lambda r: (-r["total"], r["id"]))

    if a.dry_run or a.only:
        print(f"Validated {len(rows)} idea files (dry run, nothing written). Known signal IDs: {len(sig_ids)}.")
        for wmsg in warnings:
            print("WARN", wmsg)
        return 1 if warnings else 0

    # INDEX.md
    out = ["# Idea index", "",
           "Generated by `scripts/build_index.py` from each idea file's front matter. Do not edit by hand.", "",
           f"Ideas: {len(live)} live, {len(dead)} killed after development. Total = sum(weight x score) / 95 x 100. "
           "See `METHODOLOGY.md` for the rubric.", "",
           "| Rank | Idea | One-liner | Total | Confidence | Competition | FRONTIER | Lens | Form factor | Deep dive |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(live, 1):
        out.append(
            f"| {i} | [{md_escape(r['name'])}]({r['file']}) | {md_escape(r['one_liner'])} | {r['total']:.1f} | "
            f"{r['confidence']} | {r['competition']} | {'yes' if r['frontier'] else ''} | {md_escape(r['lens'])} | "
            f"{md_escape(r['form_factor'])} | {'yes' if r['deep_dive'] else ''} |"
        )
    if dead:
        out += ["", "## Killed after development", "",
                "| Idea | One-liner | Total | Competition |", "|---|---|---|---|"]
        for r in dead:
            out.append(f"| [{md_escape(r['name'])}]({r['file']}) | {md_escape(r['one_liner'])} | {r['total']:.1f} | {r['competition']} |")
    out += ["", "## Score columns", "",
            "| Rank | Idea | " + " | ".join(f"{LABELS[k]} (x{WEIGHTS[k]})" for k in WEIGHTS) + " | Total |",
            "|---|---|" + "---|" * (len(WEIGHTS) + 1)]
    for i, r in enumerate(live, 1):
        out.append(f"| {i} | [{md_escape(r['name'])}]({r['file']}) | " + " | ".join(str(r[k]) for k in WEIGHTS) + f" | {r['total']:.1f} |")
    with open(os.path.join(IDEAS, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")

    # scoreboard.csv
    fields = ["rank", "id", "name", "file", "total", "status", "confidence", "competition", "frontier", "lens",
              "form_factor", "target_user", "one_liner"] + list(WEIGHTS) + [
              "price_hypothesis", "model_cost_per_user_month", "gross_margin", "mvp_weeks", "deep_dive", "red_team",
              "signals", "slug"]
    with open(os.path.join(IDEAS, "scoreboard.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for i, r in enumerate(live + dead, 1):
            rr = dict(r)
            rr["rank"] = i if r in live else ""
            w.writerow({k: rr.get(k, "") for k in fields})

    print(f"Indexed {len(rows)} idea files ({len(live)} live, {len(dead)} killed). Known signal IDs: {len(sig_ids)}.")
    for wmsg in warnings:
        print("WARN", wmsg)
    return 1 if (a.check and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
