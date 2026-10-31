#!/usr/bin/env python3
"""Search Hacker News via the public Algolia API and print exact text with URLs and dates.

Read-only research helper. Usage examples:
  python3 scripts/hn_search.py "is there a tool" --tags comment --since 2025-05-01 --n 20
  python3 scripts/hn_search.py "Ask HN: what tool do you wish existed" --tags ask_hn --since 2025-01-01
  python3 scripts/hn_search.py "I would pay for" --tags comment --since 2025-06-01 --by-date
  python3 scripts/hn_search.py --story 41234567          # print a story and its top-level comments

Output per hit: date | permalink | story title | text (HTML stripped, truncated with --max-chars).
"""
import argparse
import datetime as dt
import html
import json
import re
import sys
import urllib.parse
import urllib.request

API = "https://hn.algolia.com/api/v1"


def strip_html(s):
    if not s:
        return ""
    s = re.sub(r"<p>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s).strip()


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "idea-research/1.0 (read-only)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def search(query, tags, since, until, n, by_date, page):
    endpoint = "search_by_date" if by_date else "search"
    params = {"query": query, "hitsPerPage": str(n), "page": str(page)}
    if tags:
        params["tags"] = tags
    filters = []
    if since:
        ts = int(dt.datetime.strptime(since, "%Y-%m-%d").replace(tzinfo=dt.timezone.utc).timestamp())
        filters.append(f"created_at_i>{ts}")
    if until:
        ts = int(dt.datetime.strptime(until, "%Y-%m-%d").replace(tzinfo=dt.timezone.utc).timestamp())
        filters.append(f"created_at_i<{ts}")
    if filters:
        params["numericFilters"] = ",".join(filters)
    url = f"{API}/{endpoint}?" + urllib.parse.urlencode(params)
    return get(url)


def print_hit(h, max_chars):
    oid = h.get("objectID")
    date = (h.get("created_at") or "")[:10]
    title = h.get("title") or h.get("story_title") or ""
    text = strip_html(h.get("comment_text") or h.get("story_text") or "")
    if max_chars and len(text) > max_chars:
        text = text[:max_chars] + " [...]"
    pts = h.get("points")
    ncom = h.get("num_comments")
    meta = []
    if pts is not None:
        meta.append(f"{pts} pts")
    if ncom is not None:
        meta.append(f"{ncom} comments")
    print(f"--- {date} | https://news.ycombinator.com/item?id={oid} | {title} {('(' + ', '.join(meta) + ')') if meta else ''}")
    if text:
        print(text)


def print_story(story_id, max_chars, limit):
    d = get(f"{API}/items/{story_id}")
    print(f"=== {d.get('created_at','')[:10]} | https://news.ycombinator.com/item?id={story_id} | {d.get('title')} ({d.get('points')} pts)")
    if d.get("text"):
        print(strip_html(d["text"])[:max_chars or None])
    kids = d.get("children") or []
    for c in kids[:limit]:
        t = strip_html(c.get("text"))
        if not t:
            continue
        if max_chars and len(t) > max_chars:
            t = t[:max_chars] + " [...]"
        print(f"--- {c.get('created_at','')[:10]} | https://news.ycombinator.com/item?id={c.get('id')} | by {c.get('author')}")
        print(t)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="?", default="")
    ap.add_argument("--tags", default="", help="comment | story | ask_hn | show_hn | combos like 'comment,ask_hn' is AND")
    ap.add_argument("--since", default="", help="YYYY-MM-DD")
    ap.add_argument("--until", default="", help="YYYY-MM-DD")
    ap.add_argument("--n", type=int, default=20)
    ap.add_argument("--page", type=int, default=0)
    ap.add_argument("--by-date", action="store_true")
    ap.add_argument("--max-chars", type=int, default=600)
    ap.add_argument("--story", default="", help="print a story with its top-level comments")
    ap.add_argument("--limit", type=int, default=60, help="max top-level comments for --story")
    a = ap.parse_args()
    if a.story:
        print_story(a.story, a.max_chars, a.limit)
        return
    d = search(a.query, a.tags, a.since, a.until, a.n, a.by_date, a.page)
    print(f"# nbHits={d.get('nbHits')} query={a.query!r} tags={a.tags!r} since={a.since!r}")
    for h in d.get("hits", []):
        print_hit(h, a.max_chars)


if __name__ == "__main__":
    sys.exit(main())
