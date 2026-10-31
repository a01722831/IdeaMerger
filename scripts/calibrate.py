#!/usr/bin/env python3
"""Apply main-thread calibration changes to idea files: YAML scores, the section 2 table, totals, and a calibration note.

Usage: python3 scripts/calibrate.py changes.json
changes.json: {"008": {"pain": [3, "reason"], "whitespace": [2, "reason"]}, ...}
"""
import glob, json, re, sys

WEIGHTS = {"pain": 3, "evidence": 2, "ai_leverage": 2, "whitespace": 2, "novelty": 1, "why_now": 1,
           "solo_feasibility": 2, "distribution": 2, "wtp_economics": 2, "scale_defensibility": 2}
LABEL = {"pain": "Pain severity and frequency", "evidence": "Evidence quality", "ai_leverage": "AI leverage",
         "whitespace": "Whitespace", "novelty": "Novelty of insight", "why_now": "Why now",
         "solo_feasibility": "Solo feasibility", "distribution": "Distribution",
         "wtp_economics": "Willingness to pay and unit economics", "scale_defensibility": "Scale and defensibility"}


def main():
    changes = json.load(open(sys.argv[1]))
    for num, ch in changes.items():
        path = glob.glob(f"ideas/{num}-*.md")[0]
        t = open(path).read()
        notes = []
        for crit, (new, why) in ch.items():
            m = re.search(rf"(?m)^(\s+{crit}:\s*)(\d)", t)
            old = int(m.group(2))
            t = t[:m.start(2)] + str(new) + t[m.end(2):]
            # table row: | Label | weight | score | why |
            rx = re.compile(rf"(?m)^\|\s*{re.escape(LABEL[crit])}\s*\|\s*(\d)\s*\|\s*(\d)\s*\|(.*)\|\s*$")
            mm = rx.search(t)
            if mm:
                row = f"| {LABEL[crit]} | {mm.group(1)} | {new} | {mm.group(3).strip()} Calibrated {old} to {new}: {why} |"
                t = t[:mm.start()] + row + t[mm.end():]
            notes.append(f"{LABEL[crit].lower()} {old} to {new} ({why})")
        scores = {k: int(re.search(rf"(?m)^\s+{k}:\s*(\d)", t).group(1)) for k in WEIGHTS}
        total = round(sum(WEIGHTS[k] * v for k, v in scores.items()) / 95 * 100, 1)
        t = re.sub(r"(?m)^total:.*$", f"total: {total}", t, count=1)
        t = re.sub(r"(?m)^\|\s*\*\*Total\*\*\s*\|\s*\|\s*\*\*[\d.]+\*\*\s*\|", f"| **Total** | | **{total}** |", t, count=1)
        note = "Calibration (main researcher, 2026-10-31): " + "; ".join(notes) + "."
        t = re.sub(r"(?m)^(Confidence: [^\n]*\n)", lambda m: m.group(1) + "\n" + note + "\n", t, count=1)
        open(path, "w").write(t)
        print(num, "->", total)


if __name__ == "__main__":
    main()
