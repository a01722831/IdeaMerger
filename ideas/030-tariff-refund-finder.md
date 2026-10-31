---
id: "030"
slug: tariff-refund-finder
name: Tariff Refund Finder
one_liner: "Small importers upload duty documents; AI finds IEEPA refunds, picks the filing route per entry, and builds the files."
target_user: "US small importers of record (Amazon, Etsy and Shopify sellers who import inventory) with unclaimed IEEPA duties and no broker attention"
form_factor: "web app"
lens: "Forcing function"
frontier: false
competition: "CROWDED"
confidence: "MED"
status: "developed"
signals: [FORCE-04, FORCE-05, FORCE-06, FORCE-01, GAP-28, GAP-29, GAP-30, GAP-31, GAP-32, HN-15, PRO-213, PRO-214]
scores:
  pain: 3
  evidence: 4
  ai_leverage: 3
  whitespace: 1
  novelty: 2
  why_now: 4
  solo_feasibility: 3
  distribution: 2
  wtp_economics: 3
  scale_defensibility: 1
total: 51.6
price_hypothesis: "$249 flat per claim file (up to 100 entries), no percentage fee; protest packet add-on $49 each"
model_cost_per_user_month: "$3.90 one-time per claim file, about $0.25/month tracking"
gross_margin: "95%"
mvp_weeks: 5
deep_dive: false
red_team: false
---

# Tariff Refund Finder

## 1. One-liner
Small importers upload duty documents; AI finds IEEPA refunds, picks the filing route per entry, and builds the files.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | Real money ($14k, $7,500, thousands of entries) but a one-off event, and carriers now pass refunds through for the entries they imported. |
| Evidence quality | 2 | 4 | Ten on-target signals dated 2026-02 to 2026-10, with dollar amounts (GAP-30, PRO-213) and broker-side confirmation (GAP-31, GAP-32); no explicit "I would pay" quote. |
| AI leverage | 2 | 3 | Parsing carrier and broker documents and drafting packets is model work; date-window routing and the CAPE CSV are deterministic. |
| Whitespace | 2 | 1 | Brokers at 5% or flat fees, a YC S26 company that audits past entries (Tarifflo), carrier pass-through programs, free estimators and many explainers. |
| Novelty of insight | 1 | 2 | The long tail of small claims is real, but brokers, Tarifflo and logistics firms have all noticed it. |
| Why now | 1 | 4 | The Supreme Court ruling (2026-02-20) and CBP's CAPE (2026-04-20) created the market, but it is decaying by the day. |
| Solo feasibility | 2 | 3 | Parsing, routing and file builders fit in about 5 weeks; filing itself needs the importer's ACE access or a licensed broker. |
| Distribution | 2 | 2 | High-intent searches, but law firms, forwarders and Zonos own them; seller subreddits are the only open door. |
| Willingness to pay and unit economics | 2 | 3 | Clear payer with money at stake and fee anchors (5% to 30%), 95% margin, but a tiny one-time pool and a customs-broker licensing limit on success fees. |
| Scale and defensibility | 2 | 1 | Time-boxed, no lock-in, and the useful ongoing part (duty accuracy) belongs to Zonos, Avalara, Tarifflo and carriers. |
| **Total** | | **51.6** | |

Confidence: MED. FRONTIER: no.

## 3. The problem
- Who: US importers of record that paid IEEPA tariffs between 2025-02-04 and 2026-02-24 (eligibility window per a manufacturer's refund page) and have not claimed: small Amazon, Etsy and Shopify sellers, and small brands that import by air or sea.
- How often: once. Each customs entry has its own clock that runs from its liquidation date; CBP's CAPE tab takes entries that are unliquidated or liquidated within 80 days, and a protest must be filed within 180 days of liquidation, though whether protests work for IEEPA duties "is not fully settled" (Ayar Law, 2026-10-22).
- What it costs: lost refunds (one seller reports "$14k", GAP-30), unexplained duty billing ($7,500, PRO-213), or fees of 5% to 30% for help.
- Workaround today: wait for the carrier, hire a customs broker (hard for small clients, HN-15), pay a refund-recovery firm, or guess at ACE reports (GAP-31).

## 4. Evidence
Twelve cited signals (full rows in `research/SIGNALS.md`); the most telling:
- GAP-28 (strong, 2026-10-07): "I'm specifically trying to determine what happened to the refunds because FedEx is not providing me with sufficient information." Shows: a seller with about 90 US shipments and no visibility. https://www.reddit.com/r/CustomsBroker/comments/1wzyawo/
- GAP-29 (medium, 2026-09-08; same thread as FORCE-06): "They've only processed one IEEPA refund and I have no visibility into the rest. They won't tell me which shipments they've actually filed claims on." Shows: carrier-held refunds are opaque. https://www.reddit.com/r/AmazonSeller/comments/1wau2k7/
- GAP-30 (medium, 2026-08-04): "Are we out of luck here and only the big guys are getting their money back or what?" Replies explain that only the importer of record on Form 7501 can claim, and one seller reports "got back $14k". https://www.reddit.com/r/AmazonSeller/comments/1vfayn3/
- GAP-31 (medium, 2026-09-11): "How does anyone keep record using various ACE reports to determine what’s paid and to whom (various brokers), what’s in process and what’s being denied for various reasons (duplicate, flagged for recon, etc)." Shows: brokers lack a status view. https://www.reddit.com/r/CustomsBroker/comments/1wdot88/
- GAP-32 (medium, 2026-10-29): "I have filed many protests this year for IEEPA when the items were past the CAPE limits but within the protest period and not a single one has been approved yet. They all are suspended after filing and just sit there." Shows: the fallback route is stuck. https://www.reddit.com/r/CustomsBroker/comments/1xiph25/
- PRO-213 (strong, 2026-03-09): "We recently noticed that in the last three bills we’ve accumulated over $7,500 in charges under a new category called “Shipping Duties and Import Taxes.”" Shows: duty-accuracy pain for CUSMA-eligible goods. https://www.reddit.com/r/shopify/comments/1rpa9m6/
- PRO-214 (strong, 2026-04-06): "I think my best bets lie in chapter 39 or 96, but I’m struggling to find a specific code that fits what I’m shipping." Shows: the recurring HS-code chore for micro-sellers. https://www.reddit.com/r/EtsySellers/comments/1sdy03k/
- HN-15 (medium, 2026-02-20): "Drawback claims (assuming this is the correct thing to use) are quite difficult to do. Requires a customs broker." https://news.ycombinator.com/item?id=47090340
- Facts: FORCE-04 (Supreme Court: IEEPA gives no tariff power, 2026-02-20), FORCE-05 (CAPE refund requests as CSV uploads, Phase 1 live 2026-04-20), FORCE-06 (DHL-as-importer seller with no visibility), FORCE-01 (de minimis suspended indefinitely, so every sub-$800 import needs entry).
- New evidence (not in SIGNALS.md): none first-person. The deadline rule comes from a law-firm page read by fetch: "The IEEPA refund window runs on every individual customs entry, not on a single fixed date." https://ayarlaw.com/tariff-refund-resources/ieepa-tariff-refund-deadline (2026-10-22).

## 5. The product
- Outcome: tell me, entry by entry, who can claim what, by when, through which route, and hand me the file.
- Core AI loop: input (FedEx/UPS/DHL duty invoices, broker statements, ACE entry summary exports, Form 7501 PDFs, marketplace duty reports) -> extraction of entry numbers, importer-of-record line, entry and liquidation dates, HTS lines and IEEPA Chapter 99 lines, duties paid -> routing per entry: claim now through CAPE, protest candidate (81 to 180 days after liquidation), held by carrier or supplier (draft the status request), or outside every window -> output: refund estimate, CAPE CSV of entry numbers for the importer to upload, protest packet drafts for a broker, carrier claim letters, status tracker with refund IDs -> feedback: user marks paid, in process or denied, which tunes the router.
- Interaction model: web upload, an eligibility checker that answers "am I the importer of record?" in minutes, then an entry table with a deadline countdown.
- Form factor: web app. The user files through their own ACE account or hands the packet to a licensed broker; the product does not file.
- Day in the life: an Amazon seller who imports six shipments a year under her own importer number uploads an ACE export and two forwarder statements. The tool shows 41 entries and $38,200 of IEEPA duty: 29 ready for CAPE, 9 protest candidates, 3 outside all windows. She uploads the CSV, then logs refund IDs as they arrive.

## 6. Why the LLM is load-bearing
- Carrier invoices, broker statements and 7501s arrive as inconsistent PDFs; reading them into entries and spotting who is named importer of record is the hard part.
- Explaining a route and drafting protest and carrier letters in the right register needs language.
- Without the model it is a CSV builder and a calculator, which free estimators already are (GingerControl's IEEPA estimator).

## 7. The insight
For small importers the blocker is not the filing but knowing which entries are theirs, which route applies and what is already in motion, because carriers, forwarders and brokers each hold part of the picture. Honest note: the carriers' own pass-through programs and brokers' status work are closing exactly this gap for the segment that did not import in its own name.

## 8. Why now, and why this does not exist yet
- Why now: the Supreme Court held IEEPA tariffs unlawful (2026-02-20, FORCE-04); CAPE opened 2026-04-20 (FORCE-05); Phase 3 for finally liquidated entries began 2026-10-06 for court plaintiffs and a class of non-suing importers was certified on 2026-10-08 (Ayar Law); the government appeal is pending.
- It does exist in parts: see section 10.
- Time limits: as of 2026-10-31, entries liquidated before 2026-08-12 are outside the 80-day CAPE window, and before 2026-05-04 are outside the 180-day protest period [ESTIMATE: today minus 80 and 180 days]. If standard liquidation takes about 314 days after entry [UNVERIFIED], entries from before about 2025-06-24 are already past protest, and the last entries (2026-02-24) liquidate around 2027-01 and age out of CAPE around 2027-03. The addressable demand therefore runs roughly four to five more months, shrinking from the old end.

## 9. Inspiration and derivation
- Parents: customs brokers' CAPE services, Tarifflo (audit of past entries), Flexport and Zonos explainers, free estimators, claims-buyer funds, FBA reimbursement recovery services (25% fee, PRO-216).
- Changed: target user (the small importer of record, not the broker), business model (flat fee per file, no percentage), interaction model (route per entry with deadlines). The first two already exist among cheaper rivals.

## 10. Competition check
Queries run (2026-10-31):
1. Web: "IEEPA tariff refund CAPE deadline protest 180 days liquidation importers who has not filed November 2026"
2. Web: "tariff refund service small business IEEPA refund claim help startup fee percentage of refund Zonos Tarifflo Gaia Dynamics"
3. Product Hunt: "site:producthunt.com IEEPA tariff refund" (no Product Hunt pages; one similarly named "Tariflo" listing surfaced elsewhere)
4. YC: "site:ycombinator.com/companies tariff customs HS code classification AI duties" (surfaced Tarifflo via a mirror, not a YC page)
5. Carriers: "UPS FedEx DHL IEEPA tariff refund shippers importer of record carrier refund program how to claim customers"
6. Company check: "Tarifflo Y Combinator S26 tariff classification customs entries recover overpaid duties"
7. Classification vendors: "Gaia Dynamics HS code classification AI Zonos Classify pricing per classification small ecommerce sellers"
8. Store: "Shopify app store duties taxes IEEPA tariff refund app merchants importer of record Zonos Global-e Managed Markets refund" (no Shopify refund app found)
Read: the [Ayar Law deadline page](https://ayarlaw.com/tariff-refund-resources/ieepa-tariff-refund-deadline), dated 2026-10-22.

Findings:
- [Tarifflo](https://yespress.io/tarifflo-yc-s26.md) (YC S26, per a third-party mirror; official site tarifflo.com not read): classifies products under the HTS, files entries through CBP's broker interface, and "audits past import entries to recover overpaid duties"; CEO is a licensed customs broker; funding listed at about $520K ([Caplight](https://www.caplight.com/company/tarifflo)); a $1.3M recovery for one importer is a company claim. The closest direct competitor, though aimed at brokers and importers with volume.
- Fee-based help: a customs firm's agreement takes 5% of each refund with a $500 minimum and a $20,000 cap ([agreement PDF](https://files.constantcontact.com/1f332db5401/cadad9cd-0aef-44fc-aab1-a30b11d6a5ec.pdf), search summary); [Freight Right](https://www.freightright.com/solution/ieepa-tariff-refund) offers a one-time service fee with free estimates; a trade article reports some providers charged up to 30% ([Dairy Reporter](https://www.dairyreporter.com/Article/2026/05/14/tariff-refunds-what-brands-need-to-know/), search summary); [VAT IT](https://vatit.com/blog/us-ieepa-tariff-refund-how-to-claim/) sells recovery.
- Free aids: [GingerControl guide and refund estimator](https://www.gingercontrol.com/blog/ieepa-tariff-refund-guide); a free referral resource run by the Liberty Justice Center (search summary, link not captured); Kelley Drye's tracker; explainers from [Zonos](https://zonos.com/ieepa-tariff-refunds-cape), [FlavorCloud](https://flavorcloud.com/blog/ieepa-tariff-refunds-and-cape-declarations-what-importers-need-to-know-in-2026), [Swap](https://help.swap-commerce.com/en/articles/16071778-the-swap-guide-to-ieepa-tariff-refunds), [ShipMonk](https://www.shipmonk.com/resources/content-hub/ieepa-tariff-refund-guide-2026) and [Inventory Hero](https://www.inventoryhero.ai/blog/how-to-get-trump-tariff-refund). Zonos says that in typical cross-border e-commerce the carrier's brokerage is importer of record, so merchants lack standing (search summary).
- Carrier programs ([Supply Chain Dive on FedEx, UPS, DHL](https://supplychaindive.com/news/fedex-ups-and-dhl-detail-tariff-refund-approach-for-customers/818057/); [FedEx to send refunds from August](https://supplychaindive.com/news/fedex-to-send-tariff-refunds-to-customers-starting-in-august/823677)): FedEx files declarations where it was broker and has a refund status portal; UPS says it will retrieve and pass through refunds; DHL credits accounts and says 30 to 90 days after it is paid (search summaries, spring 2026). GAP-28 and GAP-29 show the portals leave gaps.
- Classification and duty accuracy: [Zonos Classify](https://zonos.com/zonos-classify-hs-codes) (1,000 free classifications; a garbled page lists $500 and $1,000 monthly tiers; free with Landed Cost per a search summary), [Gaia Dynamics](https://www.gaiadynamics.ai/blog/6-best-hs-code-lookup-tools-for-importers-and-exporters) (tiered, free basic to enterprise), [Avalara AI classification](https://www.sharedserviceslink.com/news/avalara-announces-new-ai-based-tariff-code-classification-solution), Federation (claims first place on an HS-code benchmark).

Classification: CROWDED for the refund job, and time-limited. The only unserved sliver (a multi-source status view and route picker for small importers of record) is small, and carriers' portals plus free estimators cover much of it.

Platform risk: high and mixed. CBP can simplify CAPE or widen eligibility; FedEx, UPS and DHL already run pass-through and status portals; Amazon, Shopify, Etsy and ShipStation or ShipMonk publish guides and could add duty reports; Tarifflo and brokers can serve the long tail. A reversal of the refund ruling on appeal would end the market. Caps Whitespace at 1 and Scale at 1.

## 11. Business model
- Payer: the small importer of record; secondarily a broker that refers small clients.
- Price hypothesis: $249 per claim file (up to 100 entries), protest packet add-on $49, no percentage of refund. Anchors: 5% with a $500 minimum (so $500 or more per claim), up to 30% at some providers, flat-fee brokers. $249 is about 5% of a $5,000 refund [ASSUMPTION: median small claim]. A percentage fee for preparing or filing for others may count as customs business needing a broker license [UNVERIFIED]; this is why the price is flat and the importer files.
- Model cost per claim file [ESTIMATE] (Haiku 5.5 $0.10 in / $0.50 out; Sonnet 5.5 $2.00 / $10.00; OCR about $4 per 1,000 pages, UNVERIFIED; from `research/LANDSCAPE.md` section 6):
  - 300 duty invoices on Haiku 5.5, 2,500 in + 600 out: 300 x (2,500 x $0.10 + 600 x $0.50) / 1M = 300 x $0.00055 = $0.165.
  - OCR of 600 pages: 600 x $4 / 1,000 = $2.40.
  - Entry reasoning for 60 entries on Sonnet 5.5, 6,000 in + 800 out: 60 x (6,000 x $2 + 800 x $10) / 1M = 60 x $0.02 = $1.20.
  - Five packets and letters on Sonnet 5.5, 3,000 in + 1,500 out: 5 x $0.021 = $0.105.
  - Total $3.87, about $3.90 once; tracking after that about $0.25/month [ASSUMPTION].
- Gross margin: ($249 - $3.87 - card fee $7.52) / $249 = 95.4%.

## 12. Market size
- [ASSUMPTION, no verified count] 250,000 US importers of record with IEEPA entries; 60% in the long tail (under $50K of duty) = 150,000; 30% with unclaimed, still-open entries and no broker working them = 45,000; 5% buy a self-serve tool = 2,250 x $249 = $0.56M, one time. Even at 15% it is $1.7M.
- Carrier-IOR sellers are mostly not buyers (the carrier files), which is why the pool is small. The press figure of about $166B in refunds ("Businesses line up for $166B", April 2026) shows the pool is large in dollars, not in small buyers.

## 13. Go-to-market
- First 100 customers (must happen between 2026-11 and about 2027-03): (1) 50 from a free "am I the importer of record, and which route applies?" checker plus helpful answers in r/AmazonSeller, r/CustomsBroker, r/EtsySellers and r/shopify threads like GAP-28 to GAP-30; (2) 30 from 5 to 10 customs brokers who refer small clients they do not want to serve; (3) 20 from seller newsletters and Amazon and Etsy seller forums.
- Growth loop: the checker's result page is shareable; brokers send small clients to it.
- Seasonality is the opposite of a loop: demand falls every month.

## 14. Moat and scale path
- None for the refund job. Candidates: a clean entry database per customer, then monitoring.
- Scale path: ongoing duty accuracy (HS codes, USMCA/CUSMA eligibility as in PRO-213, de minimis end, FORCE-01), which meets Zonos, Avalara, Gaia Dynamics, Federation and Tarifflo head on. That is a different, crowded product.

## 15. Solo feasibility
- MVP (5 weeks): document ingestion and entry parser; IOR detection; date-window router; IEEPA line finder; CAPE CSV builder; protest and carrier letter drafts; entry table with countdowns; Stripe.
- Running cost before revenue: about $60/month (hosting $20, database $15, OCR and model tests $15, domain and email $10) [ESTIMATE].
- Hardest technical risk: rule drift and legal accuracy. CAPE phases, formats and eligibility have changed several times in six months, protest availability is unsettled, and a wrong file harms the user. Needs a clear "not legal advice, not a broker" frame and a broker review lane.

## 16. Pre-mortem
1. The window and the market shrink faster than the build and sale cycle, or the appeal reverses refunds.
2. Most small sellers were not importers of record, so the carriers handle them and the paying pool is a few thousand.
3. Licensing and liability: percentage fees and filing for others need a customs broker license, and a wrong claim or missed deadline is blamed on the product.

## 17. Cheapest validation test
- Concierge: reply publicly with a free checker offer in 10 recent seller threads (r/AmazonSeller, r/CustomsBroker, r/EtsySellers) and run 10 volunteers' documents by hand with Claude.
- Cost: about $20 of model spend and 12 hours; duration 2 weeks.
- Pass: at least 6 of 10 are the importer of record on at least one open-window entry worth $1,000 or more, and at least 3 pay $249 within 7 days for the filled CAPE CSV. Fail: most turn out to be carrier- or supplier-IOR with nothing to file, or fewer than 2 pay.

## 18. Open questions
- Recommendation: do not build as a company. If built at all, treat it as a 6-month, low-cost burst product, and only if the concierge test passes.
- How many small sellers are the named importer on Form 7501 (line 22 per GAP-30 replies) with open entries?
- Does a flat-fee file-preparation tool avoid customs-broker licensing? Needs a customs-law opinion.
- What happens to non-litigant importers after the 2026-10-08 class certification and the pending appeal?
