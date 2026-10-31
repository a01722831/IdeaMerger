# Sources

Every source used or attempted, with access status. Track files list their exact queries; this file is the cross-track register.

## Access test (2026-10-31)
| Source | Method | Status | Notes |
|---|---|---|---|
| WebSearch tool | search | works | Returns titles, URLs and a model summary; summaries are not exact quotes |
| Hacker News | Algolia API via `scripts/hn_search.py` | works | Exact comment text, dates, permalinks. Primary source for exact quotes |
| Apple App Store reviews | iTunes RSS JSON via `scripts/app_reviews.py` | works | Most recent ~500 reviews per app, exact text and dates |
| Stack Exchange | api.stackexchange.com | works | Exact text; good for money, workplace, freelancing, law, expatriates, softwarerecs |
| Discourse forums | `/search.json` | works | Tested community.n8n.io, forum.obsidian.md |
| Lobsters | JSON | works | |
| Google News | RSS search | works | Useful for shutdowns, regulation news |
| YC company directory | WebFetch / curl | works (thin, JS-rendered) | Use WebSearch `site:ycombinator.com/companies` for content |
| BetaList, Uneed, Microlaunch | curl 200 | works | |
| Capterra, Chrome Web Store | curl 200 | works (partial, JS-heavy) | |
| BiggerPockets forums, Shopify Community | curl 200 | works | |
| Reddit | curl and WebFetch | BLOCKED (403; mirrors 429/503) | Use WebSearch with site filter; quote titles only, marked (title) |
| Product Hunt | curl | BLOCKED (403) | Use WebSearch and roundups |
| G2 | curl | BLOCKED (403) | Use WebSearch snippets, Capterra, app stores |
| Trustpilot | curl | BLOCKED (403) | |
| Upwork, Fiverr | curl | BLOCKED (403) | Use WebSearch, category pages via search, roundups |
| Indie Hackers | curl | BLOCKED (403) | |
| Peerlist, There's An AI For That | curl | BLOCKED (403) | |
| Bluesky public API | curl | BLOCKED (403) | |
| web.archive.org | curl | BLOCKED (connection reset) | |
| ContractorTalk, DuckDuckGo HTML | curl 202 | challenge page | |

## Sources added by research tracks
Each track file has a "Method" and "Blocked sources" section. The main thread merges notable additions here after each wave.
