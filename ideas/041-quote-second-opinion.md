---
id: "041"
slug: quote-second-opinion
name: Quote Second Opinion
one_liner: "Upload contractor quotes and house details; get a scope-matched comparison, red flags, a fair local range and questions to ask."
target_user: "Homeowners comparing roofing, HVAC, electrical or foundation bids over $5,000"
form_factor: "web app"
lens: "Remix"
frontier: false
competition: "CROWDED"
confidence: "MED"
status: "killed"
signals: [GAP-33, GAP-34, GAP-35, GAP-36, GAP-37, GAP-38]
scores:
  pain: 3
  evidence: 4
  ai_leverage: 4
  whitespace: 1
  novelty: 1
  why_now: 3
  solo_feasibility: 4
  distribution: 2
  wtp_economics: 2
  scale_defensibility: 1
total: 51.6
price_hypothesis: "$19 per comparison; $39 for HVAC with a sizing check"
model_cost_per_user_month: "$0.36 per comparison"
gross_margin: "91%"
mvp_weeks: 4
deep_dive: false
red_team: false
---

# Quote Second Opinion

> **Main-thread review, 2026-10-31: KILLED.** CROWDED. At least 11 named AI quote checkers (several free), free crowd advice on Reddit and the general assistants themselves cover quote comparison; an HVAC-sizing-only wedge would need its own test. The file is kept as a record of the competition check.

## 1. One-liner
Upload contractor quotes and house details; get a scope-matched comparison, red flags, a fair local range and questions to ask.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | Bids differ 2x to 4x on $10,000 to $85,000 jobs, but a buyer faces it once every few years and a free crowd helps |
| Evidence quality | 2 | 4 | 6 recent signals, 4 strong, one explicit request for a paid third party; the same threads show free help |
| AI leverage | 2 | 4 | Normalizing messy PDFs into one scope matrix is model work, and assistants do it natively |
| Whitespace | 2 | 1 | CROWDED: at least a dozen AI quote checkers, several free |
| Novelty of insight | 1 | 1 | "Compare scopes, not prices" is the pitch of every tool in the table |
| Why now | 1 | 3 | PDF reading became reliable in 2024 to 2025; the field filled up since |
| Solo feasibility | 2 | 4 | About 4 weeks; credible local price ranges are the weak point |
| Distribution | 2 | 2 | Search is crowded and Reddit communities distrust promotion; ads for home-services terms are costly [ASSUMPTION] |
| Willingness to pay and unit economics | 2 | 2 | Rivals charge $0 to $29 per report; margin is fine but the price ceiling is low |
| Scale and defensibility | 2 | 1 | Feature-sized; ChatGPT, Claude and Gemini do it with a pasted PDF |
| **Total** | | **51.6** | |

Confidence: MED. FRONTIER: no.

## 3. The problem
- Who: homeowners facing a roof, HVAC, electrical or foundation job who collect two to eight bids and cannot tell whether the scopes match.
- Frequency and cost: spreads of $11,000 to $23,000 for "what looks like the same product" (GAP-33), $21,000 to $85,000 for wiring (GAP-34), $9,000 to $28,200 for 3-ton systems in a sibling thread of GAP-35.
- Workaround: ask Reddit (free), get more bids, paste PDFs into an assistant, or pay an AI checker $0 to $29.

## 4. Evidence
Six independent signals, all 2026-10, four strong.
- **GAP-33** (strong, 2026-10-16, r/Roofing, 94 comments): "full tear off on a 1,600 sq ft ranch in southwest Ohio, architectural shingle, three quotes and they came back at $11k, $16k and $23k for what looks like the same product."
- **GAP-34** (strong, 2026-10-17, r/HomeImprovement, 49 comments): "I've gotten three bids for the work so far, and they are ridiculously disparate." Bids of $21k, $44k and $85k; top replies say compare apples to apples.
- **GAP-35** (strong, 2026-10-27, r/hvacadvice, 81 comments, post title): "Do HVAC companies do manual J load calculations. I’ve had 4 quotes and non have done that." Sizing cannot be checked.
- **GAP-36** (strong, 2026-10-22, r/solar): "I’m curious if there is some sort of third party I can hire/contact that could help me compare and make a decision?" Explicit ask. The top reply says "Don't pay anybody to compare them. Just post the numbers here", which is the free competitor.
- **GAP-37** (medium, 2026-10-22): "every place ive gotten quotes from has tried to sell me "their" version of a drainage system for 20,000-30,000$, which is basically half the value of the home."
- **GAP-38** (medium, 2026-10-22, 22 comments): "I shouldn’t have to get a bunch of bids to make sure I’m not getting fleeced. Just wastes everyone’s time."

## 5. The product
- Finished outcome: one page that lines up every bid by scope, shows what is missing or inflated, and gives questions to send to each contractor.
- Core AI loop: upload bid PDFs or photos plus house facts (age, size, climate, photos of equipment, panel or roof) -> model extracts line items and normalizes scope (equipment, permit, ductwork, electrical, disposal, warranty, financing fees) -> scope matrix with gaps and upsells -> sizing sanity check from house facts, shown as a range with its uncertainty -> fair range built from the user's own bids plus cited public cost guides [UNVERIFIED sources] -> email drafts asking for missing items (for example a load calculation) and a negotiation script.
- Interaction: web upload, report page, shareable link for a spouse or the contractor.
- Day in the life: Tom has three HVAC bids ($9,400, $14,800, $21,200). The report shows only one lists a permit, none includes a load calculation, and the largest unit sits well above the estimated range for his house. He sends the drafted email asking each firm for its load calculation and permit plan.
- Liability line: comparison and questions, not an engineering opinion. It states that ranges are estimates, never says a contractor is overcharging or fraudulent (neutral wording such as "20% above the median of your other bids"), makes no code or safety rulings, and links to state license lookups. No lead selling to contractors, to avoid a conflict of interest.

## 6. Why the LLM is load-bearing
Bids are unstructured PDFs with different line items, abbreviations and bundled prices. The model maps them to one scope list and writes the questions. This is also exactly what a general assistant does when given the files, which is the problem.

## 7. The insight
The homeowner's problem is comparing different scopes, not prices. That insight is now table stakes. The only claim left is that verifiable checks (is a load calculation included, does the unit size fit the house, do model numbers match a certified efficiency listing [UNVERIFIED terms]) beat price opinions, and are best shown for HVAC.

## 8. Why now, and why this does not exist yet
Reliable PDF reading arrived in 2024 to 2025 and at least a dozen small tools launched on it. It exists. What does not yet exist is an HVAC-specific verifier: my search found no dedicated tool that checks homeowner HVAC quotes against a load estimate (Manual J tools I saw serve contractors).

## 9. Inspiration and derivation
Parents: Carfax and Kayak (vehicle history and price comparison), the dozen quote checkers below, the free Reddit crowd. Changed: user (homeowner, not the contractor), core job (verification and questions, not a price score), channel (help-in-thread, not search), business model (per report).

## 10. Competition check
Queries run (2026-10-31): (1) web "AI contractor quote checker upload estimate is my quote fair roofing HVAC remodel compare bids homeowners"; (2) Product Hunt via search, "contractor quote estimate compare homeowner overcharged" restricted to producthunt.com (only a contractor-side proposal tool); (3) web "CheckMyBid RenoCanvas Bidcompareai contractor bid comparison price per report"; (4) web "HVAC quote analyzer AI homeowner upload quotes Manual J load calculation sizing check tool"; (5) YC directory mirror https://yc-oss.github.io/api/companies/all.json with `homeowners|roofing|HVAC|solar|remodel|contractor quote|renovation` from 2022 and `quote|bid|estimate` near `compare|check|review` (Remi, Upfront, Handyman.ai, HomeBreeze; no checker); (6) App Store `--find "contractor quote estimate compare"` (only contractor-side estimate makers such as Joist and Hover); (7) page titles of readmybid.com, renocanvas.com, checkmybid.com; (8) the earlier gap-fill track notes.

| Product | What it does | Price | Difference |
|---|---|---|---|
| [ReadMyBid](https://readmybid.com/) ([Indie Hackers](https://www.indiehackers.com/product/readmybid)) | Roofing quote check for missing or excluded details, questions to ask, compare 2 to 3 quotes | Free beta (earlier note) | Roofing only |
| [CheckMyBid](https://www.checkmybid.com/) | Compare all bids side by side with completeness scores, red flags per contractor, AI recommendation (search summary; page text did not load for me) | $19 single, $29 three-quote ([UNVERIFIED], earlier note) | Roof, HVAC, remodels |
| [Is My Quote Fair](https://build-folio.com/is-my-quote-fair/) | Quote fairness check | Not checked | Generic |
| [RenoCanvas](https://www.renocanvas.com/) | "Extract quotes, compare bids, track budgets" for renovations | "Plans from $79" (an earlier press mention said $9.99 per comparison) | Project-management bundle |
| [BidCompare AI by GreatBuildz](https://bidcompare.greatbuildz.com/) ([article](https://resident.com/tech-and-gear/2025/08/15/thwarting-home-renovation-regret-pioneering-ai-tool-transforms-bid-comparison)) | Line-by-line spreadsheet and red-flag summary | Free | Run by a contractor-matching service, so a lead-gen funnel |
| [Ripoff.pro](https://peerpush.com/p/ripoffpro), [QuoteCheck](https://www.techtic.com/our-work/quotecheck-ai-quote-analysis-vendor-marketplace/), [QuotesBuster](https://hunted.space/product/quotesbuster), [Reno Shield](https://www.hunted.space/product/reno-shield), [RemodelerIQ](https://betalist.com/startups/remodeleriq), [Quoterly](https://peerpush.com/p/quoterly) | Fairness scores, local-rate checks, overpriced-line flags, negotiation scripts (vendor claims) | Not checked | Small launches, no validated benchmarks seen |
| [Sia Policy white-glove solar review](https://siapolicy.ai/white-glove-solar.html) | Paid solar quote review (named in the GAP-36 thread) | Not checked | Solar only |
| Free crowd and assistants | Reddit threads; ChatGPT, Claude, Gemini with a pasted PDF | Free | The real incumbent |
| [Remi](https://www.ycombinator.com/companies/remi) (YC Winter 2022), [Upfront](https://www.ycombinator.com/companies/upfront) (Winter 2023, inactive) | Roofing estimates and matching; "a personal assistant for every homeowner" | n/a | Adjacent; Upfront shows consumer homeowner assistants struggle |

Classification: CROWDED (at least 11 named AI checkers plus free substitutes). Platform risk: very high; assistants do the core comparison natively and Angi-type marketplaces or Remi could add it. A sharper wedge exists only for HVAC verification (load estimate, equipment fit, permit and scope gaps).

## 11. Business model
- Payer: the homeowner, one time. Anchors: CheckMyBid $19 to $29 (unverified), RenoCanvas from $79, BidCompare AI and ReadMyBid free. Hypothesis: $19 per comparison, $39 for HVAC with the sizing check.
- Model cost per comparison [ESTIMATE], prices from `research/LANDSCAPE.md`: read 18 pages on Haiku 5.5, 27,000 in + 4,000 out = $0.0027 + $0.002 = $0.0047; normalize on Sonnet 5.5, 30,000 in + 4,000 out = $0.06 + $0.04 = $0.10; red flags and questions, 12,000 in + 2,500 out = $0.024 + $0.025 = $0.049; 10 price searches at $10 per 1,000 = $0.10; 15 chat turns with 20,000 cached tokens at $0.10/1M, 500 new in, 400 out = $0.002 + $0.001 + $0.004 = $0.007 each, $0.105. Total about $0.36.
- Margin: payment fee 2.9% + $0.30 = $0.85; support allowance $0.50 [ASSUMPTION]; ($19 - 0.36 - 0.85 - 0.50) / $19 = 91%.

## 12. Market size
[ESTIMATE] About 85M owner-occupied US homes [UNVERIFIED, from memory] x 5% a year that collect multiple bids for a major job [ASSUMPTION] = 4.25M; 3% buy a checker = 127k x $19 = $2.4M. A 10% share of that is about $0.24M. Small, and shared with free tools.

## 13. Go-to-market
- First 100 customers: deliver free summaries inside threads like GAP-33 to GAP-35 on r/Roofing, r/hvacadvice and r/HomeImprovement (read each subreddit's rules first), gate the full report at $19; inspector and realtor referrals [UNVERIFIED]; long-tail search such as "4 HVAC quotes no manual J". Split: 60 threads, 20 search, 20 referrals.
- Growth loop: shareable report links and an anonymized local benchmark that improves with every uploaded bid.

## 14. Moat and scale path
The only compounding asset is an anonymized local bid database (scope and price by trade and ZIP) that sharpens ranges; it needs volume that a $19 product may never reach. Scale: HOAs and property managers who buy bids repeatedly (a B2B twist), other trades.

## 15. Solo feasibility
- MVP, 4 weeks: upload, extraction and scope matrix (weeks 1-2), HVAC sizing range with stated uncertainty and email drafts (3), payments and PDF report (4).
- Running cost before revenue about $40 a month. Hardest risk: credible local prices without licensed cost data. Mitigate with relative comparison across the user's own bids and cited sources, and never present a guessed number as fact.

## 16. Pre-mortem
1. Crowded and free: a dozen checkers, two free ones, Reddit and assistants squeeze price to near zero and ads are expensive.
2. Trust: one visibly wrong price range or an accusation against a contractor ends the brand and invites a defamation complaint.
3. One-time purchase and a thin HVAC niche: no retention, small revenue.

## 17. Cheapest validation test
2 weeks, under $100. Review 30 real HVAC quote threads (similar to GAP-35) by hand with a prototype, offering a free summary and a $19 full report. Also run a blind test of 10 real quotes against ChatGPT with 5 HVAC professionals as raters. Pass: at least 8 of 30 pay $19 and raters prefer our report on at least 7 of 10 quotes. Otherwise kill.

## 18. Open questions
- Recommendation: kill as a general quote checker. The only candidate is HVAC verification, and only if the test above passes.
- Is there a repeat-buyer version (HOAs, property managers) with real retention?
- Which free public cost sources can be cited legitimately for ranges?
- Do model-number checks against certified efficiency listings carry usable terms? [UNVERIFIED]
