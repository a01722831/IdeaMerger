---
id: "031"
slug: product-compliance-desk
name: Product Compliance Desk
one_liner: "One product record becomes per-country compliance obligations, documents and a ship-or-skip verdict for micro-sellers."
target_user: "Micro-makers and small online sellers with under 100 SKUs shipping physical goods into the EU or the US"
form_factor: "web app"
lens: "Forcing function"
frontier: false
competition: "CROWDED"
confidence: "MED"
status: "killed"
signals: [HN-13, HN-14, FORCE-07, FORCE-08, FORCE-30, FORCE-33, FORCE-35, RED-31, PRO-220]
scores:
  pain: 4
  evidence: 4
  ai_leverage: 3
  whitespace: 1
  novelty: 2
  why_now: 4
  solo_feasibility: 2
  distribution: 3
  wtp_economics: 3
  scale_defensibility: 2
total: 56.8
price_hypothesis: "$49/month for up to 25 SKUs and 8 markets; $99/month for 100 SKUs; free break-even calculator"
model_cost_per_user_month: "$0.55 steady state, $1.15 in month one"
gross_margin: "95%"
mvp_weeks: 8
deep_dive: false
red_team: false
---

# Product Compliance Desk

> **Main-thread review, 2026-10-31: KILLED.** CROWDED. Complir (reported $11M seed) and free Shopify GPSR apps cover EU product-compliance documents, and most of the seller's cost is fixed third-party fees (authorized representative, producer-responsibility organizations), not finding the rules. Open sliver: a ship-or-skip calculator and CPSC certificate data for small US importers. The file is kept as a record of the competition check.

## 1. One-liner
One product record becomes per-country compliance obligations, documents and a ship-or-skip verdict for micro-sellers.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 4 | Micro-sellers pay EUR 800 to 2,000 per country per year (HN-13), stop shipping to the EU (HN-14) or watch Amazon EU listings sit inactive (FORCE-33); rules renew yearly. |
| Evidence quality | 2 | 4 | Two strong HN signals with euro amounts, plus Amazon, CPSC and workaround signals; RED-31 and FORCE-08 are one thread and FORCE-35 is third-hand. |
| AI leverage | 2 | 3 | Reading product data and test reports, mapping them to obligations and drafting multilingual documents is model work; the rules table and fees are data, not inference. |
| Whitespace | 2 | 1 | Complir (YC Spring 2026, reported $11M seed), EAS, AVASK, five or more Shopify GPSR and EPR apps, Lizenzero-style licensors and Amazon's provider network already serve the EU side. |
| Novelty of insight | 1 | 2 | "Tell the seller when a market is not worth entering" is a fresh angle; the rest is a known compliance stack. |
| Why now | 1 | 4 | EU packaging rules (PPWR) apply from 2026-08-12, GPSR bites on marketplaces, and CPSC eFiling started 2026-07-08. |
| Solo feasibility | 2 | 2 | Rules for many states, three waste streams and the US must be accurate and current; the representative and registration steps need licensed partners. |
| Distribution | 2 | 3 | Shopify App Store, Amazon and HN threads where the pain is aired, and a shareable calculator; all contested by vendors. |
| Willingness to pay and unit economics | 2 | 3 | Clear payer, 95% margin, and rivals quote $5,000 to $8,000 a year (FORCE-35); but the biggest costs are fixed third-party fees software cannot remove. |
| Scale and defensibility | 2 | 2 | A maintained rules database is a real asset, but a funded rival and the marketplaces can build the same. |
| **Total** | | **56.8** | |

Confidence: MED. FRONTIER: no.

## 3. The problem
- Who: micro-makers and small sellers of physical goods (electronics, toys, packaged goods) who sell into the EU and US from anywhere, with a handful of SKUs.
- How often: registrations and reports renew every year, and every new SKU or market reopens the question.
- What it costs: EUR 800 to 2,000 per country per year for an authorized representative and a producer-responsibility organization (HN-13); estimated EUR 11,850 to about 24,000 a year for EU-wide WEEE and packaging by one electronics micro-seller (HN-14); $5,000 to $8,000 a year for label and QR-page software (FORCE-35, third-hand); a stalled Amazon EU listing (FORCE-33).
- Workaround today: pay a service per country, install a marketplace-approved provider, drop countries, or hack it with an assistant (PRO-220).

## 4. Evidence
Nine cited signals (full rows in `research/SIGNALS.md`); the most telling:
- HN-13 (strong, 2026-08-24): "We pay 800-2,000 EUR per country annually for the authorized representative (AR) and producer responsibility organization (PRO) fees. [...] We are debating if we should continue selling to Europe at this stage." Shows: a hardware maker pricing the fixed fees. https://news.ycombinator.com/item?id=49422546
- HN-14 (strong, 2026-08-20): "There is NO de minimis threshold with regard to obligations, neither under WEEE nor under PPWR. This means that, as a micro-enterprise, I face the same costs as Amazon if I want to ship throughout the EU." Shows: a seller that suspended EU-wide shipping. https://news.ycombinator.com/item?id=49374029
- FORCE-30 (medium, page undated): the European Commission says it proposed in December 2025 "to suspend the obligation for producers to appoint an authorised representative when they sell packaged products directly to consumers in Member States other than the one where they are located"; the proposal is still before Parliament and Council, and PPWR applies from 2026-08-12. https://environment.ec.europa.eu/topics/waste-and-recycling/packaging-waste_en
- FORCE-33 (medium, 2026-07-12): "Hey all, were live on Amazon US and hoping to be live on EU by Sep, but the GPSR filing is taking longer than expecting - listing remains inactive, and I'm hoping we pass within the next week like they say." https://www.reddit.com/r/FulfillmentByAmazon/comments/1uuse8s/
- FORCE-35 (weak, 2026-10-19, third-hand via a builder): "Every compliance software company he talked to wanted $5,000 to $8,000 a year just to generate box labels and host multi-language QR pages." https://www.reddit.com/r/FulfillmentByAmazon/comments/1x9seel/
- FORCE-08 and RED-31 (medium, 2026-10-30; one r/ecommerce thread, counted once): "Also curious whether anyone has decided to stop shipping certain items to the US for now because the cost of compliance doesn’t make sense for them." Shows: the same ship-or-skip question on the US side. https://www.reddit.com/r/ecommerce/comments/1xjrdxl/
- FORCE-07 (medium, 2025-01-08): CPSC certificate data must be eFiled with CBP for regulated imports from 2026-07-08; the rule estimates 57.5 million filings a year. https://www.federalregister.gov/documents/2025/01/08/2024-30826/certificates-of-compliance
- PRO-220 (medium, 2026-02-08): "It's got API creds for my Amazon account, so I use it for everything from figuring out when I need to reorder to filling out spreadsheets for companies that safety test my product." Shows: a seller already uses an assistant for test-lab paperwork. https://news.ycombinator.com/item?id=46939807
- New evidence (not in SIGNALS.md): none first-person. A search summary says Complir job postings name the Digital Product Passport, GPSR and REACH as rules reshaping the market (paraphrase, not a verbatim quote, not verified).

## 5. The product
- Outcome: enter or import a product (name, materials, battery, packaging, category, target countries, expected sales) and get an obligations table per country, a document pack, a registration checklist and a plain verdict: ship, ship with conditions, or skip this market.
- Core AI loop: input (product record from Shopify, Etsy, Amazon or CSV; supplier test reports; photos of the package and label) -> classify the product into regulated streams (GPSR, WEEE, batteries, packaging, CE-type directives, REACH, US CPSC children's or general products), map to country rules from a maintained table, and compute fixed fees against expected sales -> output: obligations table with citations, drafted GPSR information block and label text in the target languages, Declaration of Conformity draft, pre-filled data for registries (LUCID, Citeo) and for CPSC certificate fields, break-even verdict, reminder calendar -> feedback: seller confirms or corrects a rule; every correction is reviewed and may update the shared table.
- Interaction model: web app with a free break-even calculator on the front door; Shopify and marketplace imports later.
- Form factor: web app.
- Day in the life: a maker of a USB-powered plant light with 6 SKUs lists Germany, France, Netherlands and the US. The tool shows WEEE, battery and packaging duties per country, the GPSR block and a CPSC certificate data sheet. It says Germany and the US are worth it at her volume, France and the Netherlands are not until monthly sales pass the break-even, and it exports the German registration checklist.

## 6. Why the LLM is load-bearing
- Product data arrives messy (a title, a photo, a supplier PDF test report); deciding which regimes a USB light with a coin cell triggers needs reading and judgment.
- Documents have to be drafted in several languages in the form each registry or marketplace expects.
- Without the model it is a static rules table and form templates, which is what a Shopify GPSR block app already is.

## 7. The insight
For a micro-seller the first question is "is this market worth it?" and nobody answers it, because every vendor sells compliance, not the decision to skip. Honest weakness: the posts show the cost is mostly fixed third-party fees (representatives, producer organizations), not the effort of figuring out rules, so software shrinks only the smaller part of the bill.

## 8. Why now, and why this does not exist yet
- Why now: GPSR enforcement (Amazon lets sellers prove compliance on the account health page), PPWR from 2026-08-12 with no de minimis threshold (HN-14), CPSC eFiling from 2026-07-08 with no de minimis exemption, and cheap models to read supplier reports.
- It partly exists: see section 10. The EU document layer is crowded; a cross-border ship-or-skip verdict for the smallest sellers, and CPSC certificate data for small foreign importers, are thinner.
- Rules may shift: the Commission's pending omnibus proposal would suspend the authorised-representative duty for cross-border direct sellers (FORCE-30), which would cut demand for one paid service and reshape the verdict.

## 9. Inspiration and derivation
- Parents: Vanta-style compliance automation (Complir calls itself "Vanta for physical products"), Shopify GPSR and EPR apps, EPR licensors, authorized-representative services, CPSC eFiling brokers.
- Changed: target user (a one-person maker, not a retailer's compliance team), core job (decide whether to enter, then document), business model ($49 a month instead of service bundles).

## 10. Competition check
Queries run (2026-10-31):
1. Web: "Lizenzero EPR WEEE packaging registration small online seller cost per country authorized representative GPSR service price 2026"
2. Product Hunt: "site:producthunt.com GPSR compliance EU product compliance EPR sellers tool" (no Product Hunt pages; Shopify listings surfaced)
3. YC: "site:ycombinator.com/companies product compliance regulatory ecommerce sellers CPSC GPSR EPR" (surfaced Complir)
4. Store and CPSC: "CPSC eFiling certificate of compliance software importers service 2026 small sellers tool Amazon EPR service Europe", then "CPSC eFiling software tool small importers certificate of compliance Product Registry GTIN eFile service provider launches automated certificate generation"
5. Funded rival: "Complir "Vanta for physical products" product compliance startup retailers cross-border launch Y Combinator" (the YC page fetch returned only a title)
6. Amazon: "Amazon EPR service sellers Europe Germany packaging WEEE registration Amazon compliance partner offer price EPR registration number upload"

Findings:
- [Complir](https://www.ycombinator.com/companies/complir) (Copenhagen, YC Spring 2026): "Vanta for physical products"; AI agents handle regulations and documentation across every market; labelling, testing, risk scoring, monitoring; a [Vestbee article](https://vestbee.com/insights/articles/complir-raises-11-m) reports an $11M seed (secondary, unverified). Aimed at retailers, not micro-sellers, per the coverage I saw ([Oresund Startups](https://oresundstartups.com/ai-startup-automating-product-compliance-joins-y-combinator-as-regulation-hits-european-retailers/)). Price not visible.
- Shopify apps: [EUReady GPSR & EPR Compliance](https://apps.shopify.com/euready) (free catalog scan, GPSR info block in EN/FR/DE, EPR packaging reports for Germany and France), [GPSR Shield](https://apps.shopify.com/gpsr-app) (free plan, no reviews yet), [GPSR Compliance Manager](https://apps.shopify.com/gpsr-compliance-manager) (free plan), [GPSR Product Safety Info](https://apps.shopify.com/priceproof-gpsr), [GC GPSR Compliance](https://apps.shopify.com/gpsr-compliance-dashboard). Descriptions from search summaries.
- Services: [EAS](https://easproject.com/epr/) (authorized representative and EPR; GPSR services "start at 199€ a year", a vendor claim); [AVASK](https://avask.com/epr-self-serve/) (EPR self-serve for Amazon sellers; registration per category from EUR 80, vendor price); [WebInterpret GPSR](https://webinterpret.com/en/solutions/gpsr-compliance); Lizenzero ([Germany EPR guide for Amazon sellers](https://www.lizenzero.de/en/blog/extended-producer-responsibility-epr-in-germany-everything-you-need-to-know-now-to-continue-selling-on-amazon-co./)), whose parent Interzero publishes 2026 price lists for licensing, WEEE and an authorized-representative service (page not read).
- Marketplaces: Amazon requires EPR numbers for Germany and France through its [EPR portal](https://sellercentral-europe.amazon.com/seller-forums/discussions/t/d39fc5dbcb5095d02de209d578585c87), points sellers to an "EPR Service Provider Network" of approved providers, and lets sellers [prove GPSR compliance on the account health page](https://developer-docs.amazon.com/sp-api/changelog/sellers-can-prove-their-gpsr-compliance-on-their-account-health-page); eBay lists [third-party compliance services](https://pages.ebay.com/regulatory/regulatory-compliance-support/). Amazon's own service is a provider directory, not a product.
- US CPSC eFiling: [Eurofins eFiling services](https://www.eurofins.com/toys-hardlines/services/regulatory-and-compliance/eurofins-toys-hardlines-efiling-services/), [Zonos CPSC eFiling guide](https://zonos.com/docs/guides/cpsc-efiling), carrier guidance from FedEx and UPS, law-firm and broker guides ([GingerControl](https://gingercontrol.com/blog/cpsc-efiling-certificate-of-compliance-ace), [a small-importer guide](https://beancount.io/blog/2026/07/10/cpsc-efiling-mandate-small-importers-guide)). I found no software tool aimed at small sellers' certificate data (negative result from two searches). CPSC's [FAQ](https://www.cpsc.gov/FAQ/eFiling-Frequently-Asked-Questions-FAQ) says there is no de minimis exemption for eFiling.

Classification: CROWDED. A funded YC company, several cheap Shopify apps, two service families and Amazon's provider network cover the EU side. The CPSC certificate-data niche for small importers looks open but small, and brokers can add it.

Platform risk: high. Amazon, eBay and Shopify already force or host GPSR and EPR proof and can integrate providers or build blocks; the EU omnibus may remove a paid obligation; CPSC or carriers can ship a free certificate-data helper; Complir can add a self-serve tier. Caps Whitespace at 1 and Scale at 2.

## 11. Business model
- Payer: the seller (maker or small brand), on a card; accountants and marketplace consultants as resellers later.
- Price hypothesis: $49/month for 25 SKUs and 8 markets; $99/month for 100 SKUs; a free break-even calculator. Anchors: EUR 800 to 2,000 per country per year of fixed fees (HN-13), $5,000 to $8,000 a year for label software quotes (FORCE-35), EAS GPSR services from EUR 199 a year, free Shopify apps for the GPSR block. The tool's price must sit near the cheap apps unless the verdict saves real fees.
- Model cost per active user [ESTIMATE] (Sonnet 5.5 $2.00 in / $10.00 out; Haiku 5.5 $0.10 / $0.50; from `research/LANDSCAPE.md` section 6):
  - Month one, 25 SKUs obligation mapping on Sonnet 5.5, 6,000 in + 1,500 out: 25 x (6,000 x $2 + 1,500 x $10) / 1M = 25 x $0.027 = $0.675.
  - Multilingual document drafts on Haiku 5.5, 800 in + 1,200 out per SKU: 25 x (800 x $0.10 + 1,200 x $0.50) / 1M = $0.017.
  - Questions and edits, 20 per month on Sonnet 5.5, 4,000 in + 500 out: 20 x (4,000 x $2 + 500 x $10) / 1M = $0.26.
  - Rule-change monitoring share per user $0.20 [ASSUMPTION: one research task per rule, shared across users].
  - Month one total $1.15; steady state (no onboarding, 3 SKU changes at $0.027 = $0.08) $0.26 + $0.20 + $0.08 = $0.54, called $0.55.
- Gross margin: ($49 - $0.55 - card fee $1.72) / $49 = 95.4%. Human legal review, if offered at all, is a separate partner-priced product.

## 12. Market size
- [ASSUMPTION] 300,000 small sellers of physical goods outside the EU or US perimeter who ship into it; one third (100,000) sell regulated categories or packaged goods; 10% adopt a paid tool = 10,000 x $49 x 12 = $5.9M a year serviceable.
- Realistic solo share: 5% of that = 500 sellers x $588 = $0.29M ARR. The pool is small because many sellers leave the market rather than comply (HN-14, FORCE-08).

## 13. Go-to-market
- First 100 customers: (1) 40 from the free break-even calculator posted in the threads where this pain is aired (HN threads like HN-13 and HN-14, r/FulfillmentByAmazon, r/ecommerce, r/EtsySellers, Tindie and Crowd Supply maker forums); (2) 30 from the Shopify App Store listing; (3) 30 from SEO on "GPSR responsible person for [product]", "WEEE registration Germany small seller" and "CPSC eFiling for small importers".
- Timing: PPWR and CPSC dates are now; marketplace compliance checks recur each quarter.
- Growth loop: the calculator result is shareable; the generated compliance page for each product links back.

## 14. Moat and scale path
- Medium-weak. Candidates: a maintained, cited rules table per country and category; correction history; product-record data that makes the next market cheap.
- Scale path: more regimes (UK, Canada, Digital Product Passport), then a seller-side monitor; or become a rules API that marketplaces embed.

## 15. Solo feasibility
- MVP (8 weeks): product intake and category tree; rules table for 8 EU markets across GPSR, WEEE, batteries and packaging plus US CPSC fields; obligations view with citations; fee table and break-even verdict; document drafts (GPSR block, label text, Declaration of Conformity draft); reminders.
- Running cost before revenue: about $90/month (hosting $25, database $15, model and monitoring tests $40, domain and email $10) [ESTIMATE].
- Hardest technical risk: rule accuracy and freshness (27 states, a changing packaging regulation, a pending omnibus) and liability for wrong advice. Registration and representative steps need licensed partners and cannot be automated, so the MVP stops at documents and checklists.

## 16. Pre-mortem
1. The money is in fixed third-party fees, not in knowing the rules, so the tool saves little and the price is capped by free Shopify apps.
2. Crowded and funded: Complir, EAS, AVASK and marketplace networks have distribution; a self-serve tier from any of them ends the niche.
3. Rule volatility and liability: a stale rule or wrong "skip" verdict costs the seller money or a listing, and sellers who leave the EU shrink the market.

## 17. Cheapest validation test
- Build the calculator for 5 product categories and 8 countries from published fee lists and rules, post it in 6 relevant communities (no sign-up wall), and run 10 concierge obligation sheets with Claude for sellers who ask, charging $79 one time.
- Cost: about $25 of model spend and 25 hours; duration 3 weeks.
- Pass: at least 300 calculator uses, at least 30 email requests for the full sheet, and at least 4 of 10 concierge buyers pay with at least 3 saying it changed a ship-or-skip decision. Fail: fewer than 100 uses or buyers who say their marketplace's provider already covers it.

## 18. Open questions
- Recommendation: do not build the full desk. Test the free break-even calculator and, if it pulls, a narrow CPSC certificate-data helper for small foreign importers; fold into a larger seller tool otherwise.
- Which Shopify GPSR apps have paying users and good reviews (several have none yet)?
- What does Complir charge, and does it serve sellers with fewer than 25 SKUs?
- If the EU omnibus suspends the authorised-representative duty for cross-border direct sellers, does demand for this tool rise (more markets viable) or fall?
