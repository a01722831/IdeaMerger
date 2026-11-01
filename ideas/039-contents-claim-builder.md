---
id: "039"
slug: contents-claim-builder
name: Contents Claim Builder
one_liner: "Rebuilds an insurer-ready contents inventory from old photos, emails and card exports after a fire or flood."
target_user: "Households after fire, flood or wildfire, and licensed public adjusters"
form_factor: "web app"
lens: "Newly possible"
frontier: false
competition: "WEAK DIRECT"
confidence: "MED"
status: "developed"
signals: [GAP-01, GAP-02, GAP-03, GAP-04, GAP-05, GAP-06, GAP-07]
scores:
  pain: 4
  evidence: 4
  ai_leverage: 4
  whitespace: 2
  novelty: 3
  why_now: 3
  solo_feasibility: 3
  distribution: 3
  wtp_economics: 2
  scale_defensibility: 2
total: 61.1
price_hypothesis: "$249 flat per claim for households; $149/month per licensed public adjuster"
model_cost_per_user_month: "$4.80 per claim (about $1.60 per active month)"
gross_margin: "91%"
mvp_weeks: 8
deep_dive: true
red_team: true
---

# Contents Claim Builder

## 1. One-liner
Rebuilds an insurer-ready contents inventory from old photos, emails and card exports after a fire or flood.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 4 | 3,000+ item lists, 12.5% to 15% adjuster fees, months of delay; episodic and event-driven |
| Evidence quality | 2 | 4 | 7 recent signals, 4 strong, money named (fees, policy limits); no one says they paid for a tool like this |
| AI leverage | 2 | 4 | Vision plus receipt extraction plus matching is the whole job; manual entry is the alternative |
| Whitespace | 2 | 2 | WEAK DIRECT bordering CROWDED: ProofList, Loti (free), room-scan apps, a Claude skill, InventoryQuant |
| Novelty of insight | 1 | 3 | Rebuild from email and card history and track depreciation holdbacks; photo-to-inventory itself is not new |
| Why now | 1 | 3 | Cheap batch vision, the 2025 LA fires; California's 60% advance rule changes timing |
| Solo feasibility | 2 | 3 | 8 weeks; pricing credibility, carrier formats and state licensing review are the hard parts |
| Distribution | 2 | 3 | Survivor communities and public adjusters; demand is spiky around disasters |
| Willingness to pay and unit economics | 2 | 2 | Families pay adjusters 12.5% to 15%, so $249 is easy to justify; free rivals cap price Red team: 3 to 2, red team: free and cheap inventory tools cap the household price; valuable services are license-gated |
| Scale and defensibility | 2 | 2 | Episodic, regulated, a free adjuster-owned tool exists; insurers can offer their own |
| **Total** | | **61.1** | |

Confidence: MED. FRONTIER: no.

Red-team adjustment (main researcher, 2026-11-01): willingness to pay and unit economics 3 to 2 (red team: free and cheap inventory tools cap the household price; valuable services are license-gated).

## 3. The problem
- Who: households after a fire, flood or storm that must give the insurer an item-by-item list of everything lost, and the public adjusters who build those lists for a fee.
- Frequency and cost: one household list ran past 3,000 items (GAP-02); a full spreadsheet "way over our policy limit" finally forced a payout (GAP-01); adjusters take 12.5% to 15% (GAP-04, GAP-05); insurers want a notarized proof of loss (GAP-06).
- Workaround: spreadsheets, memory walks, a public adjuster, or free templates and apps.

## 4. Evidence
Seven independent signals, 2025-09 to 2026-10.
- **GAP-01** (strong, 2025-09-05, r/Altadena, 11 comments): "Then I did the whole inventory and submitted it (I like using spreadsheets). It was way over our policy limit." The inventory was the lever.
- **GAP-02** (strong, 2026-06-09, r/Altadena): "Feels like the only thing that could come from reviewing a 3000+ item list in 7-10 days is a full denial" A total-loss owner still fighting 17 months after the fire.
- **GAP-04** (strong, 2026-05-28, r/HomeInsurance, 25 comments): "The PA is already taking 12.5% of the total settlement, and with even more money being cut out, I honestly don’t understand the role of the appraiser because it just feels like a second round of public adjuster services."
- **GAP-05** (strong, 2026-10-16, r/Altadena, 35 comments): "My neighbors turned their nose up at using a public adjuster because “15% is too much” and we got so much more money than them without any of the work." Willingness to pay for the paperwork job.
- **GAP-03** (medium, 2026-05-06, r/HomeInsurance, 30 comments): "My insurance agent keeps telling me I should have a documented home inventory in case of a claim, but I have no idea where to start."
- **GAP-06** (medium, 2026-06-09, r/Altadena): "They're basically asking for a notarized affidavit that my house burned down, along with everything in it."
- **GAP-07** (medium, 2025-10-10, California Department of Insurance): "It is inhumane to require survivors to list destroyed items before receiving benefits." (fetch summary). The 2025 law (SB 495, effective January 2026) makes insurers pay 60% of contents limits, capped at $350,000, after a declared-emergency total loss with no detailed inventory for at least 100 days. It narrows the California total-loss case, not partial losses or other states.

## 5. The product
- Finished outcome: a room-by-room inventory in the insurer's spreadsheet, each line tied to evidence, plus a draft proof of loss, and later a tracker for the depreciation holdback owed after replacement.
- Core AI loop: family uploads a photo and video export, forwards or exports order emails (Amazon and retailer history), and uploads card or bank statements -> vision model finds items and rooms in old family photos -> extractor reads receipts and statements -> matcher joins photo, purchase and price, dedupes, and tags evidence (documented, photographed, purchase record only, owner recall) -> replacement prices from current listings for the top items, with source links -> the model asks the family short questions by text about gaps -> export to the carrier template and a draft proof of loss for the insured's own review, signature and notarization -> after payout, tracks replacement purchases against held-back depreciation.
- Interaction: guided web flow on phone or laptop; text-message questions; a share link for a public adjuster.
- Day in the life: Mai exports 4,100 photos, forwards two years of receipts and uploads three card statements. In an hour she sees 1,420 items by room: 38% with a receipt, 41% visible in photos only, the rest marked "recall". She answers 60 short questions, downloads the carrier's spreadsheet and a draft proof of loss, and signs it herself.
- Liability line: preparation and organization only. It does not negotiate with or contact the insurer, advise on coverage, limits, valuation disputes or settlement, or file the claim, and never charges a share of the recovery. Some states define public adjusting to include preparing claim documents for pay [UNVERIFIED], so the household product is self-serve software at a flat fee with a state-by-state legal review before launch (gate states if needed); licensed public adjusters use it under their own license. Every line shows its evidence level, recalled items are labeled and sworn by the insured, and values cite sources; no auto-inflation.

## 6. Why the LLM is load-bearing
Items sit half-visible in cluttered family photos and receipts arrive in dozens of email formats; matching them and writing the claim narrative is language and vision work. Without the model a family types 3,000 lines by hand.

## 7. The insight
The inventory already exists, scattered across a family's camera roll and inbox; vision models can now rebuild it, a job that used to take weeks of grief work or a 15% fee. Honest correction: photo-to-inventory is a commodity (see section 10). The open parts are order-history and card-statement evidence, insurer-format output, and tracking the depreciation holdback.

## 8. Why now, and why this does not exist yet
Batch vision pricing of $0.05 per million input tokens makes thousands of photos cost cents, and the January 2025 Los Angeles fires produced thousands of unresolved claims (GAP-02) and a wave of tools. It partly exists: ProofList says it was built after the Eaton and Palisades fires. The holdback tracker and email/card reconstruction I did not find elsewhere.

## 9. Inspiration and derivation
Parents: ProofList and Loti (photo inventories), pre-loss home inventory apps (HomeZada, Everspruce), public adjusters (service), InventoryQuant (adjuster-side contents processing). Changed: input (email and card history on top of photos), core job (the full claim packet and holdback, not storage), business model (flat fee instead of a percentage), channel (survivor communities and adjuster white-label).

## 10. Competition check
Queries run (2026-10-31): (1) web "AI tool builds contents inventory for homeowners insurance claim after fire from photos receipts proof of loss spreadsheet"; (2) Product Hunt via search, "home inventory insurance claim contents list" restricted to producthunt.com (no relevant product); (3) YC directory mirror https://yc-oss.github.io/api/companies/all.json with `home inventory|contents claim|policyholder|public adjuster|wildfire|property claims|insurance claims` from 2021 (InventoryQuant plus carrier-side claims AI); (4) App Store `--find "home inventory insurance claim"` plus iTunes lookups; (5) fetches of proof-list.com and loti.com/toolbox; (6) the earlier gap-fill track notes on pre-loss apps.

| Product | What it does | Price | Difference |
|---|---|---|---|
| [ProofList](https://proof-list.com/) | Photos to itemized loss schedule with values and comparable links, Excel export; "Trusted by families, public adjusters, and estate professionals"; built after the 2025 fires | 25 photos free; 50 for $59, 150 for $149, 300 for $279, unlimited $499 | Closest. Photos only; no email or card history, no proof of loss, no holdback tracking seen |
| [Loti Toolbox](https://loti.com/toolbox) | Free tools built "alongside our in house public adjusters": inventory from photos and catalog, receipts to spreadsheet, damage report | Free | Lead generation for an adjuster firm, so price pressure is zero |
| [AI Home Inventory: Room Scan](https://apps.apple.com/us/app/ai-home-inventory-room-scan/id6811415009), [ClaimsReady](https://apps.apple.com/us/app/claimsready-home-inventory/id6758244506) (iOS, 2026, 0 ratings) | Room photos to items with replacement ranges, PDF export | Free listing | New, tiny, pre-loss focus |
| [HomeZada](https://www.homezada.com/homeowners/home-inventory/), [Everspruce](https://apps.apple.com/us/app/everspruce-home-inventory/id1393940808) (479 ratings), [Home Contents](https://apps.apple.com/us/app/home-contents/id420151922) (1,463 ratings), Katalogger, Stowly, HomeTracer ([thread](https://www.reddit.com/r/HomeInsurance/comments/1t4xbs4/)) | Pre-loss inventories | Free to paid | Need the owner to document before the loss |
| [Cowork Home Inventory](https://www.onewave-ai.com/resources/claude-skills/cowork-home-inventory) (Claude skill) | A folder of photos and receipts becomes an inventory file and a gap list | Free | Shows the platform can do the core natively |
| [InventoryQuant](https://www.ycombinator.com/companies/inventoryquant) (YC Winter 2026, 1 person) | Automates contents processing for public adjusters, restoration firms and insurers | Not found | B2B, adjuster side; could add a consumer flow |
| Carrier-side claims AI: [Cozmo AI](https://www.ycombinator.com/companies/cozmo-ai), [Stream](https://www.ycombinator.com/companies/stream), [Basepilot](https://www.ycombinator.com/companies/basepilot) | Automate insurers' claim handling | Enterprise | Sell to insurers; may also offer policyholder tools |
| Public adjusters | Run the claim for a share | 12.5% to 15% (GAP-04, GAP-05) | The paid incumbent and the anchor |

Classification: WEAK DIRECT (borderline CROWDED on photo-to-inventory). Platform risk: a free Claude skill does the core already, and an insurer or carrier vendor could hand every policyholder an AI inventory within 12 months; scale capped at 2, whitespace at 3 (scored 2).

## 11. Business model
- Payer: the household, once per claim; public adjusters monthly. Anchors: ProofList $279 for 300 photos and $499 unlimited; adjusters 12.5% to 15%, which on a $200,000 contents settlement is $25,000 to $30,000 [ASSUMPTION, illustrative]. Hypothesis: $249 flat; adjuster mode $149 a month.
- Model cost per claim [ESTIMATE], 3,000 items, prices from `research/LANDSCAPE.md` (Haiku 5.5 batch $0.05 in / $0.25 out): 600 photos x 1,500 tokens = 900,000 in x $0.05/1M = $0.045 plus 180,000 out x $0.25/1M = $0.045; 3,000 emails x 800 = 2.4M in = $0.12 plus 160,000 out = $0.04; statements 150,000 in = $0.0075; price lookups for the top 300 items at $10 per 1,000 searches = $3.00 (the biggest line; the rest from a cached category table); merge and dedupe on Sonnet 5.5, 6 calls x ($0.10 + $0.05) = $0.90; spreadsheet and proof-of-loss draft $0.12; 50 Q&A turns at $0.01 = $0.50. Total about $4.80, or $1.60 per active month over about 3 months.
- Margin: payment fee $7.52; support allowance $10 [ASSUMPTION]; ($249 - 4.78 - 7.52 - 10) / $249 = 91%.

## 12. Market size
[ESTIMATE] Assume 300,000 US contents claims a year need an itemized list [ASSUMPTION, unsourced]; 25% are large enough (over about $25,000 of contents) to pay = 75,000; 3% penetration = 2,250 x $249 = $0.56M. Adjuster channel: 20,000 licensed adjusters [ASSUMPTION] x $1,788 = $35.8M; 3% = 600 x $1,788 = $1.07M. About $1.6M a year, with sharp spikes after disasters.

## 13. Go-to-market
- First 100 customers: help in the communities that produced the evidence (r/Altadena, r/HomeInsurance), a free first 50 items to match ProofList's 25-photo trial, a free evidence checklist and template, outreach to public adjusters for adjuster mode, and partner conversations with a policyholder nonprofit such as United Policyholders [UNVERIFIED willingness]. Split: 50 communities, 30 adjusters, 20 SEO ("contents inventory spreadsheet", "proof of loss").
- Growth loop: survivor groups swap what worked; each claim yields an evidence-linked packet adjusters like, and neighbors from the same event ask for it. Spin up an event page within days of each wildfire or hurricane.

## 14. Moat and scale path
Carrier template library, a sourced price database, an evidence graph and adjuster relationships. Scale: theft and water claims, renters, estate inventories, small-business contents. Moderate; ProofList and InventoryQuant can converge on the same features.

## 15. Solo feasibility
- MVP, 8 weeks: upload pipeline for zipped photos, PDFs, CSV and forwarded email, with item detection tested on 30 sample homes (weeks 1-2); receipt matching and dedupe (3-4); sourced pricing (5); three carrier templates plus a generic one and the proof-of-loss draft (6); holdback tracker (7); state legal review, payments, launch (8).
- Running cost before revenue about $80 a month (hosting and photo storage $40, model testing $30, domain and misc $10).
- Hardest risk: credible item identification and prices that adjusters accept, then regulatory exposure. Gmail OAuth for restricted scopes needs a security assessment [UNVERIFIED], so start with forwarding and exports.

## 16. Pre-mortem
1. Commodity and free: ProofList at $59 to $499, Loti free, a Claude skill; price power exists only if email, card history, proof of loss and holdbacks beat them.
2. Regulation: claim-document preparation for pay may need an adjuster license in some states; one cease-and-desist could end the household product.
3. Spiky, shrinking demand: disasters are lumpy and California's 60% advance (GAP-07) reduces urgency for total losses.

## 17. Cheapest validation test
3 weeks, under $100 plus about 40 hours. Concierge for 5 survivors from r/Altadena and r/HomeInsurance and 2 public adjusters: reconstruct inventories from their photos plus order history and card exports, and compare against ProofList's free 25-photo run on the same photos. Pass: at least 3 of 5 households and 1 adjuster pay or commit ($249 or $149 a month), and order history adds at least 30% more evidenced items than photos alone [ASSUMPTION threshold]. Fail otherwise.

## 18. Open questions
- Which states treat paid claim-document preparation as public adjusting? Get counsel's list before any consumer sale.
- Do carriers accept AI-built inventories, and which templates do adjusters use most?
- Is holdback tracking real value, and how is replacement proven?
- Adjuster-first (safe harbor, InventoryQuant overlap) or household-first?

## Deep dive

### Competitor table
| Competitor | Link | What it does | Price (as published, with date read) | Funding or traction (sourced) | Gap this idea exploits |
|---|---|---|---|---|---|
| ProofList | [site](https://proof-list.com/), [Trustpilot](https://www.trustpilot.com/review/proof-list.com) | Photos to an itemized loss schedule with values and comparable links, Excel export; built after the 2025 fires | 25 photos free; 50 for $59, 150 for $149, 300 for $279, unlimited $499 (section 10, read 2026-10-31) | "Trusted by families, public adjusters, and estate professionals" (its own site); funding not published | Photos only; no email or card history, proof of loss or holdback tracking seen |
| Loti Toolbox | [loti.com/toolbox](https://loti.com/toolbox) | Free tools built "alongside our in house public adjusters": inventory from photos, receipts to spreadsheet, damage report | Free | Lead generation for an adjuster firm; funding not seen | Feeds a firm that takes a percentage; this product is flat-fee |
| Bevel (Bevelmade) | [ABC7, Sept 2025](https://abc7news.com/post/artificial-intelligence-driven-inventory-tool-bevelmade-serves-solution-california-wildfire-victims-document-belongings/17882452/), [NBC Los Angeles](https://www.nbclosangeles.com/news/local/bevel-new-app-helps-document-belongings-disaster-palisades-fire/3800554/) | Free AI inventory from photos or video, built after a co-founder's parents lost their Palisades home; value estimates; also pre-disaster | Free account (search summary) | Local TV coverage; funding not seen | Photos and video only; no order or card evidence, proof of loss or holdbacks |
| ClaimLedger AI | [vendor page](https://claimledgerai-app-production-u6z3ua.laravel.cloud/how-it-works) | Inventory by room, brand, age and replacement value; policy extraction and claim tracking (vendor claims) | Not seen | Not seen [UNVERIFIED] | "Claim tracking" may overlap the holdback tracker; email and card reconstruction not described |
| HomeZada, Room Scan, ClaimsReady, Everspruce and other pre-loss apps | [HomeZada](https://www.homezada.com/homeowners/home-inventory/), [Coverager](https://coverager.com/homezada-launches-home-inventory-video-recognition-ai/), [Room Scan](https://apps.apple.com/us/app/ai-home-inventory-room-scan/id6811415009), [ClaimsReady](https://apps.apple.com/us/app/claimsready-home-inventory/id6758244506), [Everspruce](https://apps.apple.com/us/app/everspruce-home-inventory/id1393940808) | Pre-loss inventories; HomeZada added video item recognition (title only); Room Scan and ClaimsReady are new iOS apps | Free to paid (section 10) | Everspruce 479 ratings, Home Contents 1,463; Room Scan and ClaimsReady 0 ratings (section 10) | Need the owner to document before the loss |
| Cowork Home Inventory (Claude skill) | [onewave-ai](https://www.onewave-ai.com/resources/claude-skills/cowork-home-inventory) | A folder of photos and receipts becomes an inventory file and a gap list | Free | n/a | No carrier templates, state gate or evidence levels; shows the platform does the core natively |
| InventoryQuant; Cozmo AI, Stream, Basepilot | [InventoryQuant](https://www.ycombinator.com/companies/inventoryquant), [Cozmo AI](https://www.ycombinator.com/companies/cozmo-ai) | Contents processing for adjusters, restoration firms and insurers; claims automation for insurers | Not found / enterprise | InventoryQuant: YC Winter 2026, 1 person (section 10) | B2B; could add a consumer flow |
| United Policyholders | [uphelp.org](https://uphelp.org/theres-help-for-dealing-with-insurance/) | Nonprofit guidance; notes adjusters often ask for receipts although many were lost in fires (search summary) | Free | Nonprofit | Guidance, not a tool; possible partner [UNVERIFIED willingness] |
| Public adjusters | [NAPIA](https://napia.com/what-is-a-public-adjuster) | Run the claim; NAPIA says an adjuster "will prepare your claim, including all estimates, inventories and other factual information" (search summary) | 12.5% to 15% of the settlement (GAP-04, GAP-05) | Licensed state by state | Price and control; but only they may prepare and negotiate claims (see the licensing line) |

### Market sizing (bottom-up)
- Cited base ([Triple-I via III](https://www.iii.org/fact-statistic/facts-statistics-homeowners-and-renters-insurance), read 2026-10-31): fire and lightning claims run at 0.23 per 100 house-years (2019 to 2023 weighted average) with average severity $88,170; "About one in 425 insured homes has a property damage claim related to fire and lightning"; 47% of homeowners say they prepared an inventory (2023 Triple-I/Munich Re survey).
- Insured homes are not on that page: [ASSUMPTION] 70M. 70,000,000 x 0.0023 = 161,000 fire and lightning claims a year. Households that need a long list and would pay: 20% of fire claims have a large contents loss [ASSUMPTION] = 32,200, plus 40,000 catastrophe households a year (wildfire, hurricane, flood, tornado) [ASSUMPTION, spiky] = 72,200.

| Case | Households and adoption | Household revenue ($249) | Adjusters (20,000 [ASSUMPTION, section 12]) | Adjuster revenue ($149 x 12 = $1,788) | Total a year |
|---|---|---|---|---|---|
| Conservative | 72,200 x 2% = 1,444 | $0.36M | 20,000 x 25% with regular fire work x 5% = 250 | $0.45M | $0.81M |
| Optimistic | 72,200 x 6% = 4,332 | $1.08M | 20,000 x 50% x 10% = 1,000 | $1.79M | $2.87M |

- Downside check: removing the 47% who say they have an inventory cuts conservative households to 72,200 x 53% x 2% = 765 ($0.19M).
- Revenue at 100, 1,000 and 10,000 customers: households (one-time $249) $24,900, $249,000 and $2,490,000 (10,000 is 14% of 72,200); adjusters ($149 a month) $178,800, $1,788,000 and $17,880,000 a year (10,000 exceeds the 5,000 to 10,000 contents-active adjusters assumed, so it is not reachable).

### Unit economics
Per household claim over about 3 months. Prices from `research/LANDSCAPE.md` section 6.

| Line | Volume | Tokens | Model and price per 1M | Arithmetic [ESTIMATE] | Cost |
|---|---|---|---|---|---|
| Photo item detection | 600 photos | 1,500 in, 300 out each (900,000 / 180,000) | Haiku 5.5 batch, $0.05 / $0.25 | $0.045 + $0.045 | $0.09 |
| Order emails | 3,000 | 800 in, about 53 out each (2.4M / 160,000) | Haiku 5.5 batch | $0.12 + $0.04 | $0.16 |
| Card statements | 1 set | 150,000 in, 30,000 out | Haiku 5.5 batch | $0.0075 + $0.0075 | $0.02 |
| Replacement price lookups | 300 items | web search | $10 per 1,000 | 300 x $0.01 | $3.00 |
| Merge and dedupe | 6 | 50,000 in, 5,000 out | Sonnet 5.5, $2 / $10 | 6 x ($0.10 + $0.05) | $0.90 |
| Spreadsheet and evidence appendix | 1 | | | section 11 | $0.12 |
| Q&A | 50 | 3,000 in, 500 out | Sonnet 5.5 | 50 x $0.011 | $0.55 |
| Total | | | | 0.09 + 0.16 + 0.02 + 3.00 + 0.90 + 0.12 + 0.55 | $4.84 |

- Lookups are $3.00 of $4.84. A shared category and brand price cache at a 50% hit rate halves it to $1.50; Gemini search grounding is free to 5,000 a month, then $14 per 1,000, which covers about 16 claims a month at 300 lookups. Section 5's "in an hour" needs non-batch Haiku: photos $0.18, emails $0.32, statements $0.03 instead of $0.09, $0.16, $0.02, adding about $0.27.
- Other per claim: payments 2.9% x $249 + $0.30 = $7.52; SMS Q&A 50 x $0.0123 + 50 x $0.0113 = $1.18 ([Twilio pricing](https://www.twilio.com/en-us/sms/pricing/us), read 2026-10-31); storage 2 GB of downscaled photos x $0.023 x 12 months = $0.55 [ASSUMPTION, list price not re-checked]; support $10 [ASSUMPTION]; infrastructure $80 a month / 20 claims = $4.00 early (/ 100 claims = $0.80).
- Margin: early 4.84 + 7.52 + 1.18 + 0.55 + 10.00 + 4.00 = $28.09, so ($249 - $28.09) / $249 = 88.7%; at scale $24.89 and 90.0% (section 11: 91%). Per active month: $83.00 revenue against $9.36 cost.
- Adjuster mode ($149 a month, 2 claims): model 2 x $4.84 = $9.68; storage $1.10; payments 2.9% x $149 + $0.30 = $4.62; support $15; infrastructure $1.00: $31.40, margin 78.9%. Heavy adjuster (8 claims): 38.72 + 4.40 + 4.62 + 20 + 1.00 = $68.74, margin 54%. Heavy household (8,000 photos, 6,000 emails, 800 lookups): model $12.75 (lookups $8.00, merge 15 x $0.15 = $2.25), payments $7.52, SMS $3.54, storage $1.10, support $25, infrastructure $4.00: $53.91, margin 78%.
- Caps: the adjuster plan includes 3 claims a month and 5,000 items per claim; extra claims $39 each (cost about $6.82, 83% margin), so 8 claims earn $149 + 5 x $39 = $344 against $74.40 (78%). Households get lookups for the top 400 items; a $49 valuation pack adds 500 (cost $5.00).

### First 100 customers
Funnel [ESTIMATE]: a helpful reply brings 8 visits; visit to free first-50-items trial 12%; trial to paid 15%, so 1.8% of visits pay. Adjusters: an individually written email gets a reply 6%, a free first claim 60%, then $149 a month 40%, so 1.44% of emails yield a paying adjuster.

| Week | What you do | New customers (math) | Cumulative |
|---|---|---|---|
| 1 | Free evidence checklist and template page; state-gate page; 10 replies a week in r/Altadena and r/HomeInsurance (disclose; link only where rules allow); 40 adjuster emails a week for weeks 1 to 6 | 10 x 8 x 1.8% = 1.4 households + 40 x 1.44% = 0.6 adjusters = 2.0 | 2 |
| 2 | Repeat | 2.0 | 4 |
| 3 | Repeat; ask Eaton Fire Survivors Network leaders and United Policyholders to list the checklist [UNVERIFIED willingness] | 2.0 + (100 visits x 1.8% = 1.8) | 8 |
| 4 to 6 | Repeat; first search pages live in week 5 ("contents inventory spreadsheet for insurance claim", "proof of loss contents list template"), more in week 6 ("insurance contents claim without receipts", "recoverable depreciation holdback") | 2.0 a week | 14 |
| 7 | Community replies only; search pages draw about 20 visits a week | 1.4 + 0.4 = 1.8 | 16 |
| 8 | Review the funnel; prepare the event-page template | 1.8 | 17 |

- Result: about 17 customers by week 8 (14 households, 3.5 adjusters), 2.2 a week, so 100 takes about 9 to 12 months as search matures and adjusters tell peers [ESTIMATE]. A declared disaster changes it: an event page live within 72 hours, 400 visits x 1.8% = 7 households in week one and 30 to 60 in four weeks for a large event (1,700 to 3,300 visits); one or two events reach 100 in 4 to 5 months.
- Channels: r/Altadena, r/HomeInsurance; the Eaton Fire Survivors Network (named in a [6abc report](https://6abc.com/post/california-wildfires-altadena-eaton-fire-survivors-network-use-ai-navigate-insurance-hurdles-rebuild-lives/17021268/), search summary); United Policyholders; NAPIA and state public-adjuster associations; adjusters found by hand in state insurance-department license lookups; FEMA declarations as the trigger for event pages; SEO "how to list items lost in a fire for insurance".
- Message and offer: "You do not have to list 3,000 items from memory. Bring your photos, order emails and card statements and get an evidence-tagged list, room by room. $249 flat, never a percentage of your claim; you review and sign everything yourself." First 50 items free; pay when you export. In states not yet cleared: "not available here yet; ask a licensed public adjuster to use adjuster mode". Adjusters: free first claim, then $149 a month.
- Growth loop: neighbors from the same event; each adjuster brings 2 to 3 claims a month and tells peers; the event page is reused for every disaster.

### One-week validation test (under $50)
Three questions, none needing a household's money: where can households buy (licensing), does order history add evidence, and does anyone want it.
- Days 1 to 2, licensing map ($0): read the public-adjuster definition in 10 candidate states (suggest CA, FL, TX, LA, NC, GA, CO, OK, OR, WA [ASSUMPTION]) and tabulate citation, whether it covers "prepares, completes, or files" a claim for compensation, whether an inventory carve-out exists, and green, yellow or red. Already read: [Fla. Stat. 626.854(1)](http://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0600-0699/0626/Sections/0626.854.html), 2026 text.
- Days 2 to 5, evidence uplift: 3 consenting volunteer households in your network each give about 100 photos, their own Amazon "Request My Data" order-history export and 3 months of card statements. Run the pipeline by hand with Claude, and have each volunteer run the same photos through ProofList's free 25-photo tier. Count items with at least one evidence record, photos only versus all sources.
- Days 2 to 7, demand: a page saying "Early access list. Nothing is live. We are not a public adjuster and do not file or negotiate claims." with state, loss date and "would you pay $249 flat if it is available in your state? yes or no" (no payment taken). Answer existing questions in r/Altadena and r/HomeInsurance where rules allow and keep the page in your profile. Send 30 individually written emails to licensed public adjusters who advertise fire or flood contents work, offering a free first claim and $149 a month after.
- Budget [ESTIMATE]: domain $12; pages and forms free; Claude for 3 households 3 x $2.30 = $6.90 (photos $0.03, orders $0.02, statements $0.01, 100 lookups $1.00, merge 6 x $0.15 = $0.90, Q&A 20 x $0.011 = $0.22, export $0.12); contingency $10; total $28.90. Counsel review ($1,500 to $3,000 [ASSUMPTION]) comes after a pass.
- Pass (set in advance), all three: (A) at least 4 of the 10 states green or yellow; (B) order history and statements raise evidenced items by at least 30% over photos alone in at least 2 of 3 households [ASSUMPTION threshold]; (C) at least 25 early-access signups with a loss in the last 24 months or a pending claim and at least 10 of them saying yes to $249, or at least 3 of 30 adjusters replying, 2 calls held and 1 agreeing in writing to a free first claim and $149 a month.
- Fail: A passes in 1 or 0 states (then adjuster-only), or B under 15% in 2 households, or under 10 signups and no adjuster reply. Anything else: rerun in a different channel.

### Build brief (paste into a coding session)
**Product summary.** Contents Claim Builder rebuilds an insurer-ready contents inventory after a fire or flood from a family's photos, order emails and card statements. Each line carries its evidence level and a sourced replacement price; it exports to the carrier's spreadsheet and tracks the depreciation holdback after payout. Households pay $249 flat; licensed public adjusters pay $149 a month.

**Liability line and licensing guardrail (keep visible in the UI, copy and prompts).** Preparation and organization only: it does not negotiate with or contact the insurer, advise on coverage, limits, valuation disputes or settlement, or file the claim, and never charges a share of the recovery. Licensing: Florida defines a public adjuster to include a person who "for money, commission, or any other thing of value, directly or indirectly prepares, completes, or files an insurance claim for an insured", "regardless of how that person describes or presents his or her services", yet excludes "a person who photographs or inventories damaged personal property" who does not otherwise solicit, adjust, investigate or negotiate (Fla. Stat. 626.854(1), 2026 text, read 2026-10-31). Wisconsin chapter 629 defines an "adjusting service" as an act on behalf of an insured, in exchange for compensation, with the preparation, completion or filing of a first-party claim (search summary). So v1 gives households the inventory, the evidence appendix and a recall attestation the insured writes and signs, with no household proof-of-loss drafting and no claim narrative; the proof-of-loss draft exists only in adjuster mode, where a licensed adjuster is the user of record. A state gate (state, citation, green, yellow or red, counsel review date) blocks household checkout outside cleared states. Describe what the software does in marketing, because a label does not protect. Get counsel before any consumer sale [UNVERIFIED whether self-serve software used by the insured falls inside any state's definition].

**MVP features (each testable)**
1. Intake (state, insurer, policy type, loss date) and state gate. Test: every non-cleared state is blocked from household checkout.
2. Upload of zipped photos and video (frame extraction), PDFs, card CSVs and forwards to an inbound address; hash dedupe. Test: a 4,000-photo zip processes with no manual step.
3. Photo item detection by room with confidence. Test: at least 80% recall of items worth $50 or more and 85% precision on 30 sample homes.
4. Order and receipt extraction from emails, PDFs and Amazon's order-history export. Test: at least 90% of 200 synthetic orders correct.
5. Matching and dedupe of photo, purchase and statement records. Test: at least 90% right, at most 3% wrong.
6. Evidence level per line (documented, photographed, purchase record only, owner recall); recall never upgraded automatically. Test: 0 recalled lines marked documented across 500 lines.
7. Sourced replacement prices for the top items with link and date, a shared cache, no auto-inflation, user override with a reason. Test: 100 items, every link works, at least 90% within 25% of a human-checked price.
8. Gap questions by text or web, top 60 by value. Test: an answer updates its line within 5 seconds.
9. Export: carrier template (3 plus a generic one) as XLSX or CSV, PDF evidence appendix with thumbnails, recall attestation page. Test: files open in Excel and every line links to evidence.
10. Adjuster mode: workspace, share link, edit log, white-label export, proof-of-loss draft behind a licensed-user flag, and a holdback tracker (user enters RCV, ACV, withheld amount and deadline; replacement receipts link to lines). Test: holdback balance equals entered amounts minus linked purchases.

**Non-goals.** Filing, insurer contact or negotiation; coverage, valuation or appraisal advice; percentage pricing; household proof of loss or claim narrative; a pre-loss inventory app; a room-scan app; Gmail OAuth (restricted scopes need a security assessment [UNVERIFIED], so forwarding and exports only); a mobile app.

**Core AI loop.** Inputs: photo and video exports, forwarded order emails, order-history exports, card statements, answers. Haiku 5.5 batch ($0.05 / $0.25 per 1M; non-batch $0.10 / $0.50 when the user waits) for photos, emails and statements; Sonnet 5.5 ($2 / $10) for merge, dedupe and Q&A; web search ($10 per 1,000) or Gemini grounding for prices, with a cache; no frontier tier. Prompts detect items with room and confidence, extract merchant, item, price and date, join records and explain each match, and ask the smallest question that upgrades the most value. Human checkpoints: the family confirms each room list ("is this yours?"), answers questions and signs the attestation; the adjuster reviews in adjuster mode; the founder reviews the first 20 exports.

**Data model.** Claim, Household, Room, Item, Evidence (photo, receipt, order, statement row, recall), PriceQuote (source, date), Match, Question, Answer, Export, CarrierTemplate, StateGate, AdjusterAccount (license number, state), Holdback, ReplacementPurchase.

**Integrations and stack.** Anthropic API ([docs](https://platform.claude.com/docs)); Gemini grounding ([docs](https://ai.google.dev/gemini-api/docs/grounding)); Twilio ([docs](https://www.twilio.com/docs/messaging)); Postmark inbound email ([docs](https://postmarkapp.com/developer/webhooks/inbound-webhook)); Stripe ([docs](https://docs.stripe.com/payments/payment-links)). Next.js on Vercel (about $20), Supabase Postgres, Auth and Storage (about $25), a Fly.io worker for photo and video jobs (about $15) with a Postgres queue, Sentry and PostHog free tiers: about $80 to $100 a month before model usage [ESTIMATE, list prices not re-checked].

**Evals.** (1) Detection: 30 sample homes with hand ground truth; at least 80% recall for items $50 or more, 85% precision. (2) Matching: 200 synthetic orders and 100 photos; at least 90% correct, at most 3% wrong. (3) Evidence integrity: 500 lines, 0 recalled items marked documented. (4) Prices: 100 items; all links work, at least 90% within 25% of a human-checked price, 0 fabricated URLs. (5) Guardrail: 30 prompts asking for coverage, negotiation, valuation-dispute advice or a claim narrative; 100% refused and routed to an adjuster or attorney; checkout blocked in every non-cleared state.

**Build plan (8 weeks).** Weeks 1 to 2: upload pipeline, state gate, photo detection on 30 sample homes; start counsel. Weeks 3 to 4: order, receipt and statement extraction, matching, dedupe, review UI by room. Week 5: sourced pricing, cache, gap questions. Week 6: carrier templates, evidence appendix, attestation page. Week 7: adjuster mode and holdback tracker. Week 8: payments, final state-gate review, launch, event-page template.

**Key risks to test first.** (1) Licensing: the state map, then counsel. (2) Item detection on cluttered photos. (3) Whether adjusters and carriers accept the prices and templates. (4) Free competitors (ProofList, Bevel, Loti, a Claude skill). (5) Spiky demand: be ready with an event page within 72 hours.

**Notes for the main researcher.** Fla. Stat. 626.854 carves out inventorying but covers preparing or completing a claim for pay, so section 5's household "draft proof of loss" should move behind the adjuster license or counsel clearance. Bevel (free) and ClaimLedger AI are new competitors; whitespace 2 holds. Not in the file: Triple-I's 47% pre-loss inventory figure and the $0.27 cost of live versus batch processing.

## Red team
Skeptical-investor review on 2026-11-01 (full text: `research/RED_TEAM_A.md`). Verdict: **pass**.

**Top attacks (summarized):**
1. **The sellable household product is a commodity; the valuable one is gated.** After the licensing guardrail the household tier is an inventory, an evidence appendix and an attestation, which ProofList ($59 to $499), Bevel (free), Loti (free), ClaimLedger AI and a free Claude skill approximate.
2. **The $249 vs 12.5% to 15% anchor compares different jobs.** Adjusters sell negotiation, appraisal strategy and carrying the fight, all license-gated.
3. **The adjuster channel is thin and carriers have their own AI.** InventoryQuant (YC W26) and Adjusto serve the professional and insurer side; the adjuster count is an assumption.
What would change the red team's mind: counsel clearing household sale in four high-volume states, order history adding 30%+ evidenced items in 2 of 3 households, and an adjuster firm or carrier confirming an output was accepted on a real claim.

**Response (main researcher):**
- Attack 1 lands on willingness to pay, which drops from 3 to 2. The household tier is positioned as a reconstruction engine (camera roll, videos, order history, card exports into a priced inventory), which is exempt from adjuster licensing in Florida's statute ("photograph or inventory"), and is priced against ProofList rather than adjuster fees.
- Attack 2 lands: drop the adjuster-fee comparison from all marketing.
- Attack 3 lands partly. The professional tier (the licensed adjuster is the user of record) is the safer business but faces InventoryQuant; whitespace stays at 2. Solo feasibility stays at 3 because the inventory-only scope needs no state-by-state legal gating.
- Pain (4) and evidence (4) stay: the strongest signals in the project (GAP-01, GAP-02, GAP-04, GAP-05) show households already paying 12.5% to 15% to get this done.
