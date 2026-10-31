#!/usr/bin/env python3
"""Read recent Reddit posts from the public Arctic Shift archive and filter them locally by keywords.

Reddit itself blocks this environment; Arctic Shift (arctic-shift.photon-reddit.com) is a public, read-only
archive. Its full-text `query=` times out, so this script pulls listings (newest 100 posts per window) and
filters locally. Be gentle: it sleeps between requests.

Usage:
  python3 scripts/reddit_archive.py Landlord --since 2025-06-01 --windows 4 --grep "is there|tool|software|app" --max-chars 400
  python3 scripts/reddit_archive.py AgingParents,caregivers --since 2025-05-01 --windows 3 --grep "paperwork|medicare|bills"
Output per hit: date | permalink | score/comments | title, then selftext (truncated).
Permalink format: https://www.reddit.com/r/<sub>/comments/<id>/
"""
import argparse
import datetime as dt
import json
import re
import sys
import time
import urllib.parse
import urllib.request

API = "https://arctic-shift.photon-reddit.com/api/posts/search"
FIELDS = "id,title,selftext,created_utc,score,num_comments,subreddit"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "idea-research/1.0 (read-only)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def fetch_window(sub, after, before):
    params = {"subreddit": sub, "after": after, "before": before, "limit": "100", "sort": "desc", "fields": FIELDS}
    return get(API + "?" + urllib.parse.urlencode(params)).get("data") or []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("subs", help="comma-separated subreddit names without r/")
    ap.add_argument("--since", default="2025-05-01")
    ap.add_argument("--until", default="", help="YYYY-MM-DD, default today")
    ap.add_argument("--windows", type=int, default=3, help="number of 100-post pages to walk back per subreddit")
    ap.add_argument("--grep", default="", help="case-insensitive regex applied to title+selftext")
    ap.add_argument("--min-comments", type=int, default=0)
    ap.add_argument("--max-chars", type=int, default=500)
    a = ap.parse_args()
    until = a.until or dt.date.today().isoformat()
    rx = re.compile(a.grep, re.I) if a.grep else None
    for sub in [s.strip() for s in a.subs.split(",") if s.strip()]:
        before = until
        seen = 0
        for _ in range(a.windows):
            try:
                posts = fetch_window(sub, a.since, before)
            except Exception as e:  # noqa: BLE001
                print(f"# r/{sub}: request failed: {e}")
                break
            if not posts:
                break
            for p in posts:
                seen += 1
                text = (p.get("title") or "") + "\n" + (p.get("selftext") or "")
                if rx and not rx.search(text):
                    continue
                if (p.get("num_comments") or 0) < a.min_comments:
                    continue
                d = dt.datetime.fromtimestamp(p["created_utc"], dt.timezone.utc).date().isoformat()
                body = (p.get("selftext") or "").replace("\n", " ").strip()
                if a.max_chars and len(body) > a.max_chars:
                    body = body[: a.max_chars] + " [...]"
                print(f"--- {d} | https://www.reddit.com/r/{sub}/comments/{p['id']}/ | {p.get('score')} pts, {p.get('num_comments')} comments | {p.get('title')}")
                if body and body not in ("[removed]", "[deleted]"):
                    print(body)
            oldest = min(p["created_utc"] for p in posts)
            before = dt.datetime.fromtimestamp(oldest, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
            time.sleep(1.5)
        print(f"# r/{sub}: scanned {seen} posts since {a.since}")


if __name__ == "__main__":
    sys.exit(main())
