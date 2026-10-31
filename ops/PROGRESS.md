# PROGRESS: checklist and running log

Read this after every compaction together with `MISSION.md`. Update before each long step.

Branch: `claude/practical-rubin-cchd5o`. Started: 2026-10-31 (UTC).

## Phase checklist

### Phase 0: setup
- [x] 0.1 MISSION.md (brief verbatim)
- [x] 0.2 CLAUDE.md (standing orders)
- [x] 0.3 ops/PROGRESS.md (this file)
- [x] 0.4 ops/RESEARCH_BRIEF.md for subagents
- [x] 0.5 METHODOLOGY.md (rubric + kill criteria)
- [x] 0.6 research/SOURCES.md + skeleton (README.md, REPORT.md, ideas/INDEX.md, ideas/POOL.md, research/SIGNALS.md, research/LANDSCAPE.md, scripts/build_index.py)
- [x] 0.7 Tool test: one WebSearch, one WebFetch, one curl
- [x] 0.8 Commit and push

### Phase 1: landscape -> research/LANDSCAPE.md
- [x] 1.1 Subagent A: AI launches (PH, YC, BetaList, Uneed, Microlaunch, Peerlist, directories), 30+ products -> research/landscape/launches.md
- [x] 1.2 Subagent B: capability unlocks + current API prices -> research/landscape/capabilities.md
- [x] 1.3 Subagent C: theses (YC RFS, VC theses) + graveyard -> research/landscape/theses-graveyard.md
- [x] 1.4 Synthesize research/LANDSCAPE.md (red zones, unlocks, timing, price table, traps)
- [x] 1.5 Commit and push

### Phase 2: pain mining -> research/tracks/*.md, then research/SIGNALS.md
- [x] T1 Hacker News (38 signals) (Ask HN wishes, frustrations, would-pay; Show HN AI comments) -> tracks/01-hn.md
- [x] T2 Reddit founder/SaaS communities (39 signals) -> tracks/02-reddit-founders.md
- [x] T3a Professions batch A (35 signals) -> tracks/03a-professions.md
- [x] T3b Professions batch B (36 signals) -> tracks/03b-professions.md
- [x] T3c Professions batch C (45 signals) -> tracks/03c-professions.md
- [x] T4 Reviews of incumbent software (51 signals) -> tracks/04-reviews.md
- [x] T5 Service-to-software (63 signals, 48 with prices) -> tracks/05-service-to-software.md
- [x] T6 Consumer life admin (55 signals) -> tracks/06-life-admin.md
- [x] T7 Second-order AI effects (60 signals) -> tracks/07-second-order-ai.md
- [x] T8 Forcing functions (56 signals; 14 live, 6 dropped) -> tracks/08-forcing-functions.md
- [x] T9 Underserved users (51 signals) -> tracks/09-underserved.md
- [ ] 2.x Consolidate research/SIGNALS.md (150+ distinct, grouped by theme, dupes merged)
- [ ] 2.y Commit and push after each wave

### Phase 3: ideation and screening -> ideas/POOL.md
- [x] 3.1 Capability x persona grid (in POOL.md)
- [x] 3.2 200+ seeds, >=15 per lens (9 lenses) + 10 wild
- [x] 3.3 Screen: red zones, kill criteria, merges, status per seed
- [x] 3.4 Advance ~50 (38 concept notes written; gap-fill batch G pending) with 3-5 line concept notes
- [ ] 3.5 Commit and push

### Phase 4: development -> ideas/NNN-slug.md
- [x] 4.1 scripts/build_index.py working (plus --dry-run/--only for agents)
- [ ] 4.2 Subagent batches of 5-8 ideas (competition check >=4 queries each, classification, draft file)
- [ ] 4.3 Review every draft, kill/re-scope CROWDED, sharpen, own final scores
- [ ] 4.4 40+ full idea files; rebuild index after every batch; commit and push per batch

### Phase 5: calibration, deep dives, red team
- [ ] 5.1 Calibration pass across all ideas
- [ ] 5.2 Deep dives top 12 (competitor table w/ pricing, bottom-up sizing, unit economics w/ real prices, first 100 customers, <$50 1-week validation test w/ threshold, paste-ready build brief)
- [ ] 5.3 Red team subagent on top ideas; record critique + response; adjust scores
- [ ] 5.4 Commit and push

### Phase 6: synthesis
- [ ] 6.1 REPORT.md (10 sections)
- [ ] 6.2 README.md (intro, top 10 table, links)
- [ ] 6.3 Commit and push

### Phase 7: QA and finish
- [ ] 7.1 Template compliance, real signal IDs, INDEX/scoreboard match, no placeholders/TODOs, URLs from research
- [ ] 7.2 Mark done here, commit and push
- [ ] 7.3 Reply in chat with top 10 and where to start reading

## Definition of done (mirror of MISSION.md)
- [ ] MISSION.md, CLAUDE.md, METHODOLOGY.md, ops/PROGRESS.md, ops/RESEARCH_BRIEF.md exist
- [x] LANDSCAPE.md and SOURCES.md complete (SOURCES.md keeps growing)
- [ ] All 9 pain tracks covered
- [ ] SIGNALS.md has 150+ sourced signals
- [ ] POOL.md has 200+ seeds, each with a status
- [ ] 40+ full idea files, each with a recorded competition check
- [ ] Calibration done
- [ ] Top 12 have deep dives, red-team critiques and build briefs
- [ ] REPORT.md, README.md, INDEX.md and scoreboard.csv complete and consistent
- [ ] QA passed
- [ ] Everything committed and pushed

## Subagent task budget (target 25-30 total)
| Wave | Tasks | Count |
|---|---|---|
| Landscape | launches, capabilities, theses/graveyard | 3 |
| Pain wave 1 | T1 HN, T2 Reddit, T3a, T3b | 4 |
| Pain wave 2 | T3c, T4 reviews, T5 service, T6 life admin | 4 |
| Pain wave 3 | T7 second-order, T8 forcing, T9 underserved | 3 |
| Development | ~7 batches of 6-8 ideas | 7 |
| Deep dives | 3 batches of 4 | 3 |
| Red team | 1-2 | 2 |
| Total | | ~26 |

## Running log
- 2026-10-31 12:34 UTC: Session start. Repo had only Init.txt ("Start here.."). Kept it (harmless). Branch exists locally and on origin.
- 2026-10-31: Decision: landscape subagents write to research/landscape/*.md (one file each), main thread synthesizes research/LANDSCAPE.md. Keeps the "two subagents never write the same file" rule.
- 2026-10-31: Decision: subagents for pain mining use model "sonnet" (mid-tier) per brief. Development drafting also uses sonnet to save budget; main thread (this one) reviews and owns scores.

- 2026-10-31 12:50: Tool test done. WebSearch OK; WebFetch OK on most sites; curl OK for HN Algolia, Apple RSS reviews, Stack Exchange API, Discourse search.json. BLOCKED: Reddit (curl+WebFetch 403, mirrors 429/503), Product Hunt, G2, Trustpilot, Upwork, Fiverr, Indie Hackers, Peerlist, TAAFT, Bluesky API, web.archive.org. Network is not broadly restricted; lean on HN/StackExchange/app reviews for exact quotes and WebSearch for Reddit/PH (titles only).
- 2026-10-31: Wrote scripts/hn_search.py and scripts/app_reviews.py so subagents get exact text cheaply.
- 2026-10-31 12:55: Phase 0 committed and pushed. Launching Phase 1 (3 landscape subagents, model sonnet).
- 2026-10-31 13:20: Landscape C (theses/graveyard) done: 20 theses, YC W27 RFS, 26 graveyard cases. Subagent overran fetch budget slightly (11 vs 10).
- 2026-10-31 13:20: Decision: rolling waves. Keep max 4 subagents running at once; started T1 HN and T2 Reddit/founders while landscape A and B finish.
- 2026-10-31 14:05: Phase 1 done. LANDSCAPE.md synthesized from launches.md (95 products, YC batch stats, HeyClicky calibration), capabilities.md (9 unlocks, native features, price tables), theses-graveyard.md. Added 18 red zones. Started T3b. Note: subagents run 20-40 min each and use 250-500k tokens; keep prompts tight.
- 2026-10-31 14:25: T1 HN done (38 signals; 13 strong). Started T3c.
- 2026-10-31 14:45: T2 done (39 signals, exact Reddit text via Arctic Shift public archive). Wrote scripts/reddit_archive.py and added it to RESEARCH_BRIEF.md. Started T4 reviews.
- 2026-10-31 15:05: T3a done (35) and T3b done (36). Both ran well past the soft API-call cap (read-only public endpoints; acceptable). T3a flagged that some late-2026 Reddit/BiggerPockets posts look like founders' research-seeding posts and excluded them. Started T5 service-to-software and T6 life admin.
- 2026-10-31 15:20: Wrote scripts/merge_signals.py (parses track tables) and scripts/signal_themes.py (24 themes + duplicate merges, main-thread judgment). Interim SIGNALS.md built: 153 distinct. Rebuild after each track lands.
- 2026-10-31 15:40: T4 done (51; loudest theme: incumbents' bolted-on AI backfiring). Added themes incl. incumbent-ai. Started T7.
- 2026-10-31 16:00: T3c done (45). Started T8 forcing functions. Running: T5, T6, T7, T8. T9 next.
- 2026-10-31 16:20: T7 done (60). Split AI themes into ai-slop, ai-verify, ai-fakes, agent-oversight, ai-cost, scams, ai-education, shadow-ai. Started T9 (last pain track). T5/T6 files are on disk but agents not yet reported back.
- 2026-10-31 16:40: T5 (63) and T6 (55) done and themed; new themes freelance-market, data-conversion, accessibility-remediation, translation, household-records, immigration, family-records. Running: T8, T9.
- 2026-10-31 17:00: Launched T10 gap-fill (prefix GAP-) to test 9 candidate areas with thin evidence (contents claims, deposits, estate cleanouts, cargo claims, rental scams, tariff refunds, contractor quotes, inspectors, vendor payment fraud). Drafted POOL.md (159 seeds, 31 developed). Decision: kills based on known incumbents say 'not re-searched' when not verified in this project.
- 2026-10-31 17:30: T8 and T9 done and themed. Pool now has forcing-function and underserved lenses plus 12 wild seeds. Waiting on T10 gap-fill to resolve 9 pending seeds.
- 2026-10-31 17:50: Concept notes for 38 advanced seeds written in POOL.md with idea numbers 001-038 and batches A-F (G = gap-fill outcomes). Re-opened S020 Food Cost Buddy for a competition check (restaurants otherwise unrepresented). Added build_index.py --dry-run/--only so drafting agents can validate without writing INDEX.
- 2026-10-31 18:00: Wrote ops/DEV_BRIEF.md (shared drafting instructions). Launched development batches A (7 back-office ideas), B (7 field/freight), C (6 families/health), model sonnet. T10 gap-fill still running. Remaining: D (6), E (5), F (7), G (gap-fill outcomes).

## Counts
- Signals: 540 raw / 525 distinct (116 strong) after T1-T9 + LAND; T10 gap-fill pending
- Seeds: 213 (201 S + 12 W); developed 38 (+ up to 9 pending T10)
- Idea files: 0
- Deep dives: 0

## Blocked sources
(see research/SOURCES.md for the full list)
