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
  wtp_economics: 3
  scale_defensibility: 2
total: 63.2
price_hypothesis: "$249 flat per claim for households; $149/month per licensed public adjuster"
model_cost_per_user_month: "$4.80 per claim (about $1.60 per active month)"
gross_margin: "91%"
mvp_weeks: 8
deep_dive: false
red_team: false
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
| Willingness to pay and unit economics | 2 | 3 | Families pay adjusters 12.5% to 15%, so $249 is easy to justify; free rivals cap price |
| Scale and defensibility | 2 | 2 | Episodic, regulated, a free adjuster-owned tool exists; insurers can offer their own |
| **Total** | | **63.2** | |

Confidence: MED. FRONTIER: no.

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
