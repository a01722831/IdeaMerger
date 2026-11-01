# Report: startup discovery for a solo, AI-native founder

Prepared 2026-10-31 to 2026-11-01. Everything here is backed by files in this repo; every pain claim traces to a signal with a URL, a date and an exact quote in [research/SIGNALS.md](research/SIGNALS.md).

## 1. Executive summary
Being finalized after the second red-team pass (sections 1, 6, 8 and 10 depend on final scores).

## 2. How to navigate the repo
| If you want | Read |
|---|---|
| The ranked list with scores | [ideas/INDEX.md](ideas/INDEX.md) (generated) or [ideas/scoreboard.csv](ideas/scoreboard.csv) |
| One idea in depth | `ideas/NNN-slug.md`: 18 template sections; the top 12 add a `## Deep dive` (competitor table with prices, bottom-up sizing, unit economics, first 100 customers, a one-week validation test under $50, a paste-ready build brief) and a `## Red team` (skeptical-investor critique, the response, score changes) |
| Why an idea was killed | The review note at the top of each killed idea file, and the status column in [ideas/POOL.md](ideas/POOL.md) |
| The evidence | [research/SIGNALS.md](research/SIGNALS.md) (571 distinct signals by theme) and the raw tracks in `research/tracks/` |
| The market context | [research/LANDSCAPE.md](research/LANDSCAPE.md) (red zones, capability unlocks, model price table, traps) |
| The raw critiques | [research/RED_TEAM_A.md](research/RED_TEAM_A.md) and [research/RED_TEAM_B.md](research/RED_TEAM_B.md) |
| How scoring works | [METHODOLOGY.md](METHODOLOGY.md) |
| What happened, in order | [ops/PROGRESS.md](ops/PROGRESS.md) |

## 3. Method
**Pipeline.** Landscape scan, then ten pain-mining tracks, then 216 seeds from nine lenses plus wild ideas, screened against red zones and kill criteria, then 41 full idea files with a competition check of at least four differently worded searches each, then calibration, deep dives and red team on the top 12. Research subagents did the mining, drafting and deep dives; the main researcher did ideation, screening, review, kills, calibration and synthesis.

**Sources and counts.**
| Step | Output |
|---|---|
| Landscape | 95 recent AI products (Product Hunt via mirrors, YC W25 to F26 batch counts, BetaList, Uneed, Microlaunch, Futurepedia); model price tables from official pages read 2026-10-31; 20 investor theses; YC's Winter 2027 Requests for Startups; 26 dead or absorbed AI products |
| Pain mining | 586 raw signals in 10 tracks (Hacker News 38, founder communities 39, three professions batches 116, incumbent reviews 51, service-to-software 63, life admin 55, second-order AI 60, forcing functions 56, underserved users 51, gap-fill 46, plus 11 from the landscape), consolidated to **571 distinct signals, 130 strong**, in 62 themes |
| Ideation | **216 seeds**: Pain-first 31, Newly possible 24, Remix 22, Transplant 16, Service-to-software 25, Second-order AI 23, Interaction shift 16, Forcing function 20, Underserved users 27, Wild 12 |
| Screening | 109 killed at screening (reason recorded), 63 merged into stronger seeds, 41 developed, 3 queued for a second wave (not run) |
| Development | **41 full idea files**; **24 killed after their competition check** (all CROWDED), **17 live** |
| Top 12 | Deep dives and red-team critiques with responses and score changes |

**Evidence rules.** Every pain claim has a URL, a date when visible and an exact quote of two sentences or fewer; quotes were machine-checked against the fetched text in every track. Estimates are tagged [ESTIMATE] with the math, assumptions [ASSUMPTION], unverifiable claims [UNVERIFIED].

**What was blocked.** Reddit refuses direct reads from this environment; exact Reddit text came from the public Arctic Shift archive (newest posts per subreddit, so older threads are underrepresented). Product Hunt, G2, Trustpilot, Upwork, Fiverr, Indie Hackers, Peerlist and There's An AI For That returned 403; Product Hunt was read through mirrors (hunted.space, aitoolly), Upwork and Fiverr through public category pages, press and Freelancer.com listings. Paywalled news (FT, Bloomberg, 404 Media) was used for headlines only. Full register: [research/SOURCES.md](research/SOURCES.md).

## 4. Landscape
Full synthesis: [research/LANDSCAPE.md](research/LANDSCAPE.md).
- **The big assistants absorbed the horizontal layer in 2026.** ChatGPT Work, Claude Cowork and Claude Duet, Gemini tasks, Copilot Vision and Autopilot browse, act, remember, make documents, see the screen and run proactively. OpenAI retired its own Atlas browser and Sora. Generic agents, screen overlays, memory layers and document generators are red zones.
- **Incumbents shipped their own AI.** Intuit's Accounting Agent, Jobber's voice quotes, ServiceTitan's Atlas, Vagaro's Fill My Books, AppFolio's Realm-X, Stripe Smart Disputes and Greenhouse Voice AI each erased a startup wedge this project tested (section 5).
- **Small models are cheap and voice is a commodity.** Claude Haiku 5.5 and GPT-6 Luna cost $0.10 / $0.50 per million tokens, so a typical 3,000-in, 500-out call costs about $0.00055; realtime voice is about $0.05 a minute. Model cost is rarely the constraint for the ideas below; trust, liability and distribution are.
- **Investor consensus is crowded.** "Sell outcomes, not tools" in insurance, accounting, healthcare revenue cycle and legal is the most crowded thesis and mostly enterprise-sold. YC's newest requests moved to bottlenecks: credentials, government paperwork, the aging population, proving you are human, compliance.
- **HeyClicky set the interaction bar and showed the risk.** AI by the cursor that sees the screen on a hotkey and talks you through tasks won distribution, was cloned six times and absorbed by labs within months. The defensible version ties that interaction to a narrow job, domain data or a system the labs ignore.
- **Rules changed in 2025 and 2026.** The end of de minimis, the IEEPA tariff refunds, CPSC eFiling, EU packaging and GPSR rules, the European Accessibility Act, Medicaid work requirements from 2027 and FMCSA's Motus migration all create document-heavy work. Six expected forcing functions were vacated, stayed or delayed (FinCEN real-estate rule, CMMC Phase II, EU AI Act high-risk dates, Colorado AI Act, the H-1B fee, a student-visa rule), so deadlines need checking before building on them.

## 5. Opportunity themes
**What the competition checks taught.** 24 of 41 developed ideas died as CROWDED, and the pattern is clear. Generic small-business back office is saturated in late 2026: bookkeeping catch-up and review, receipt capture, chargebacks, booking-gap filling, voice estimates for trades, wholesale order entry, maintenance dispatch, change orders, restaurant invoices, COI issuance, applicant screening, AI governance for MSPs, accessibility fixes and remediation, product-compliance documents, tariff refunds and payment-fraud checks all have funded entrants or incumbents' own AI features. Consumer medical-bill fighting and AI quote checking are crowded too.

**Where whitespace survived.** The live ideas share three traits: (1) a long-lived case file rather than a one-shot answer, (2) a counterparty institution (a Medicaid agency, an insurer, a broker, a court, a funder, an agency portal) that is slow or adversarial, and (3) an incumbent that is a human service priced in thousands of dollars or a percentage, not software. The main cost in these markets is trust, liability lines and distribution, not model spend.

| Theme | Live ideas | Could merge into |
|---|---|---|
| Families carrying institutional paperwork | 006 Medicaid Ready, 007 Parent Mail Desk, 037 Retirement Desk, 008 Paper Trail, 002 Shoebox | One "family admin case file" company that starts with the sharpest wedge (Medicaid long-term care) and adds parent mail, retirement transitions and agency notices as modules |
| Claims against insurers and disasters | 039 Contents Claim Builder | Pairs with the family case file for households, or with public adjusters as a B2B engine |
| Money owed to small operators | 001 Haul Paid, 032 Authority Guard | An owner-operator back office (getting paid plus keeping authority alive) |
| Public benefits under new rules | 027 Benefits Portal Pilot | Could share infrastructure with the family case file (document vault, deadline engine) |
| Funded nonprofits | 005 Grant Ledger | Stands alone |
| Verification in the AI era | 018 Viva Voce, 025 Cite Check | A "proof of understanding" suite for education and publishing |
| Workers and chat-first sellers | 034 Wage Check, 033 Chat-to-Ledger | Stand alone; both lack a proven payer |
| Interaction-shift guides | 036 Do It With Me, 028 Legacy App Buddy, 010 Closeout Copilot | Share a screen-guidance engine, but each faces platform risk |

## 6. Picks by goal
Being finalized after the second red-team pass.

## 7. Wildcards
Unconventional seeds worth a second look even though they were not advanced (full list in [ideas/POOL.md](ideas/POOL.md)):
- **Casework Copilot (W01):** prepares a congressional casework request when the IRS, SSA, VA or USCIS stalls; folded into Paper Trail as an escalation channel, and possibly the most distinctive feature that idea has.
- **Regulatory Twin (W02):** a live model of every rule that applies to one micro-business; too broad for a solo MVP, but the right long-term shape for compliance products.
- **Viva Voce (018)** is the live idea closest to a wildcard: oral defenses of student work at class scale, only affordable since realtime voice became a commodity.
- **Wave 2, not run (S226 to S228):** long-term-care insurance claims for families, court accountings for family guardians and special-needs trustees, and workers' comp premium-audit defense for small contractors. They sit squarely in the whitespace pattern above and are the first thing to test in an EXTEND pass.

## 8. Full ranked table
Being finalized after the second red-team pass. The current generated ranking is always in [ideas/INDEX.md](ideas/INDEX.md).

## 9. Limitations and blind spots
- **Scores are judgment, not measurement.** The rubric is applied consistently and recalibrated side by side, but a 60 versus a 58 is not a meaningful difference. Confidence is MED or LOW for every live idea; none has a paying customer yet.
- **Willingness to pay is the weakest evidence everywhere.** Pain signals are strong; explicit payment signals are rare. Every top idea's first test is a payment test for that reason.
- **Coverage gaps.** Reddit evidence skews to the newest posts per subreddit (archive limits). Product Hunt, G2, Upwork and Fiverr were read indirectly. Professions with little online voice (funeral homes, churches, small farms, dental labs) produced no usable evidence, which says more about where people post than about their pain. The research is US-heavy, with some EU, Latin American and Indian signals.
- **Competition checks age fast.** Several competitors launched weeks before this research (OweRight on 2026-10-23, Greenhouse Voice AI in September 2026, many AI apps in 2026). Re-run the searches in each idea's section 10 before building.
- **Legal lines are not legal advice.** Several ideas sit near unauthorized practice of law, public adjusting, debt collection, CMS marketing rules or Circular 230. The files flag each line and how the product stays clear of it; a short consult with a practitioner in the launch state is part of each validation plan.
- **Platform risk is high across the board.** Frontier labs and vertical incumbents shipped features in 2026 that killed many seeds; the same can happen to live ideas. Each file has a platform-risk paragraph.
- **Second wave not run.** Three seeds in the strongest whitespace pattern (S226 to S228) were queued but not developed because of usage limits.

## 10. Suggested decision process
Being finalized after the second red-team pass.
