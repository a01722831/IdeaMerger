---
id: "019"
slug: job-walk
name: Job Walk
one_liner: "Tech talks while walking the job and snaps photos; AI returns good-better-best estimates from the shop's price book."
target_user: "Residential HVAC, plumbing and electrical shops with 1-10 techs on Jobber or Housecall Pro"
form_factor: "mobile app"
lens: "Newly possible"
frontier: false
competition: "CROWDED"
confidence: "MED"
status: "killed"
signals: [REV-07, REV-08, REV-09, PRO-005, PRO-003, REV-10]
scores:
  pain: 4
  evidence: 3
  ai_leverage: 4
  whitespace: 1
  novelty: 2
  why_now: 3
  solo_feasibility: 3
  distribution: 3
  wtp_economics: 3
  scale_defensibility: 2
total: 57.9
price_hypothesis: "$99/month per shop (up to 3 techs)"
model_cost_per_user_month: "$10.20"
gross_margin: "90%"
mvp_weeks: 7
deep_dive: false
red_team: false
---

# Job Walk

> **Main-thread review, 2026-10-31: KILLED.** CROWDED. Jobber's AI voice mode creates quotes, Housecall Pro ships voice-to-invoice, and ServiceTitan's Atlas with Max reached all residential contractors in October 2026. The vertical incumbents own the price book and the workflow. The file is kept as a record of the competition check.

## 1. One-liner
Tech talks while walking the job and snaps photos; AI returns good-better-best estimates from the shop's price book.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 4 | Estimates and notes are typed on every call; users report an hour for 3 estimates and 15-20 minutes of retyping per call (REV-07, REV-08). |
| Evidence quality | 2 | 3 | Two strong and two medium signals on the pain, one strong on build-your-own; none states willingness to pay for voice estimates specifically. |
| AI leverage | 2 | 4 | Voice plus photos to a priced, tiered estimate does not exist without the model. |
| Whitespace | 2 | 1 | A dozen voice or photo quote tools plus Jobber voice quotes, Housecall Pro voice-to-invoice and ServiceTitan Atlas; see section 10. |
| Novelty of insight | 1 | 2 | Obvious, and many have built it; the price-book mapping is the only twist. |
| Why now | 1 | 3 | Voice and vision became cheap and accurate in the last 12-18 months, but incumbents are already shipping. |
| Solo feasibility | 2 | 3 | Capture app is easy; price-book mapping accuracy and write access to Jobber or Housecall Pro are the hard parts. |
| Distribution | 2 | 3 | Trade subreddits, YouTube and possibly the Jobber and Housecall Pro app marketplaces [UNVERIFIED]. |
| Willingness to pay and unit economics | 2 | 3 | Margin is 90%, but free generators and $99-per-shop rivals cap the price. |
| Scale and defensibility | 2 | 2 | Platform risk is high; a price-book dataset helps only if you own the workflow. |
| **Total** | | **57.9** | |

Confidence: MED. FRONTIER: no. **Recommendation: CROWDED; see section 18.**

## 3. The problem
- Who: owners and techs at residential HVAC, plumbing and electrical shops with 1-10 techs. On a service call the tech diagnoses, builds an estimate with options in the field-service app, types job notes or an invoice summary, and someone must follow up.
- What hurts: a ServiceTitan Field user says the app takes an hour to build 3 estimates and type the invoice summary after AI features were added (REV-07); another loses 15-20 minutes per call retyping dropped notes (REV-08); an owner with 7 techs still does dispatch and follow-ups and missed a $3k estimate follow-up (PRO-005); a contractor misses 2-3 calls a day and quote follow-ups fall through (PRO-003).
- Cost [ESTIMATE]: 44 estimates a month per tech x 10 minutes of typing = 7.3 hours x $45 an hour loaded [ASSUMPTION] = about $330 per tech per month, before lost follow-ups.
- Workaround: typing on a phone, paper tickets the office re-keys, an owner who pays college students $10-15k for a custom app (REV-09), or a free quote generator.

## 4. Evidence
- REV-07 (strong, App Store ServiceTitan Field, 2026-09-11): the user says the app was fine before AI features were added. "Takes an hour to just build 3 estimates and type out the invoice summary."
- REV-08 (strong, App Store ServiceTitan Field, 2026-09-03): "I’m literally spending an additional 15-20 minutes on each call because this app is just downright bad."
- REV-09 (strong, r/HVAC, 2026-10-30): "Long story short, he found out how much the apps cost, ended up paying some local college kids like $10-15k or so to build us something with all the same features. Took like 6 months to work through the major bugs, but after that it was great lol."
- PRO-005 (medium, r/ProHVACR, 2026-06-23): "running 7 techs across 2 locations right now and i'm still the one handling dispatch, scheduling, and follow-ups on top of everything else. missed a $3k estimate follow-up last week because i was slammed."
- PRO-003 (medium, ContractorTalk, 2026-10; post names the app Tradestash, may be vendor-seeded): "where im still losing money is two spots it doesnt really cover: follow ups and dealing with missed calls when im on a job."
- REV-10 (medium, r/HVACAdvice, 2026-10-29): price pushback on field-service software. "idk about paying $500 just for color contrasted numbers on a spreadsheet when Excel is free"
- New evidence (not in SIGNALS.md): r/ProHVACR, 2026-10-22, https://www.reddit.com/r/ProHVACR/comments/1xc9cyd/ (6 comments): "The tech finishes, writes the ticket in the truck, and the office turns that into an invoice later." The double entry is the pain.

## 5. The product
- Outcome: the tech talks through the job and photographs the equipment; before leaving the driveway he has a tiered estimate built from the shop's own price book, job notes written, and follow-up texts scheduled. A draft lands in Jobber or Housecall Pro.
- Core AI loop: input (voice walk-through, photos of nameplates and problem areas, the shop's price book and equipment tiers) -> model work (transcribe, read model, serial and age from nameplates, pick matching items and good-better-best tiers from the book, list unknowns for the tech to answer, write the customer summary and job notes) -> output (estimate options on the phone, a draft estimate pushed to the field-service app through its API, a day 1, 3 and 7 follow-up sequence) -> feedback (edited prices and accepted tiers improve the mapping).
- Guardrail: prices come only from the shop's book; anything not in it is flagged "ask office". The model never invents a price.
- Interaction: phone web app (hold to talk, tap to photograph), no typing; the office sees drafts.
- Form factor: mobile web app (installable PWA).
- Day in the life: at a no-cool call, Luis says "Carrier three-ton, 2014, compressor locked out, line set looks reusable, recommend condenser and coil" and photographs both nameplates. The app returns three options at $6,900, $8,400 and $11,200 from the shop's equipment tiers. He taps send; the homeowner gets a text; the draft appears in Jobber.

## 6. Why the LLM is load-bearing
The input is a spoken walk-through and nameplate photos; the output is line items mapped to a shop-specific price book with tiers and plain-language wording. Matching "locked-out compressor on a 2014 three-ton" to the shop's SKUs needs language and vision understanding. Without the model it is the form the techs already hate.

## 7. The insight
The field is a voice-and-camera environment, and the shop's price book is the moat: an estimate is a mapping from messy field talk to the shop's own SKUs and tiers. Honest note: the voice half is being commoditized by the platforms themselves (Jobber voice mode, Housecall Pro voice-to-invoice). What remains is the nameplate-to-options mapping and follow-up, and that is not yet proven valuable.

## 8. Why now, and why this does not exist yet
It exists in pieces and arrives in the incumbents next. Jobber's AI voice mode (beta) can create a quote by voice and edit line items; Housecall Pro announced voice-activated invoicing (ACHR News headline, 2025-11-19) and lists "Voice AI (Voice to invoice)" as coming soon in February 2026; ServiceTitan launched Atlas for technicians (September 2025) and its help page dated 2026-10-15 still describes estimates as built manually from the pricebook, with Atlas finding replacement parts matched to the pricebook. The gap I could see is photo and voice to tiered options from the price book. It is narrow and short-lived.

## 9. Inspiration and derivation
- Parents: ServiceTitan Atlas, Jobber AI voice mode, Housecall Pro voice AI, QuoteIQ and BuildFolio photo-to-quote, and the HeyClicky voice-plus-context pattern.
- Changed: interaction model (walk the job and talk, not fill in a form), target user (1-10-tech shops on Jobber or Housecall Pro, not ServiceTitan accounts), business model (add-on per shop, not a suite), distribution (marketplaces and trade communities).

## 10. Competition check
- Queries run: (1) "Jobber Copilot Housecall Pro AI estimate from photos voice notes quote assistant 2026 field service technicians"; (2) "ServiceTitan Titan Intelligence AI estimates technician voice notes photos good better best options 2026 Atlas"; (3) "site:producthunt.com voice estimate app HVAC plumbing electrician photos AI quote on site"; (4) "site:ycombinator.com/companies HVAC plumbing technicians estimates voice AI field service"; (5) "ServiceTitan Atlas mobile app technicians voice estimates Pantheon 2026 Max residential contractors announcement"; (6) "Jobber Copilot AI quotes create quote line items from notes photos official Jobber blog". Also: Housecall Pro and ServiceTitan help pages read, a Reddit archive pull, news searches. The App Store lookup script returned HTTP 403.
- [Jobber AI voice and chat (beta)](https://help.getjobber.com/en/articles/jobber-ai-voice-and-chat-beta/): in Voice mode it can "Create a new quote, Use a quote template, Edit line items, Add/remove discounts, Adjust tax rate, Assign a salesperson"; typed chat cannot create records. An [AI button rewrites line-item text](https://help.getjobber.com/en/articles/quote-basics/). A rival's [comparison](https://intercom.help/quoteiq/en/articles/13834817-quoteiq-vs-jobber) says the receptionist is a paid add-on (unverified). I found nothing showing Jobber builds line items from photos.
- [Housecall Pro February 2026 updates](https://www.housecallpro.com/resources/february-2026-product-updates/) (read): CSR AI chat and Accountant AI available; "Voice AI (Voice to invoice)" and "Summary of Work 2.0" coming soon; no AI estimates, price-book AI or good-better-best mentioned. [ACHR News headline](https://www.achrnews.com/articles/165511-housecall-pro-brings-ai-powered-voice-activated-invoicing-to-the-trades), 2025-11-19: "Housecall Pro Brings AI-Powered, Voice-Activated Invoicing to the Trades". Its AI chat agent drew a complaint for impersonating the owner (REV-05).
- ServiceTitan: Atlas (SiliconANGLE headline, 2025-09-18) and an Atlas mobile app with Max for all residential contractors (Quiver Quantitative headline, 2026-10-06). Its [estimates help page](https://help.servicetitan.com/docs/estimates-and-proposals-in-servicetitan-max) (2026-10-15) says estimates are built from the Pricebook or templates and Atlas answers questions and finds compatible parts matched to the pricebook; see also [Atlas in mobile](https://help.servicetitan.com/docs/atlas-in-mobile-overview).
- Voice and photo quote apps (vendor claims, prices mostly unseen): [quotiai](https://www.producthunt.com/p/quotiai) ("voice memo + site photos" to a quote), QuoteDash AI and [PreventivAI](https://www.producthunt.com/products/preventivai/makers) (WhatsApp, branded PDF quote in 90 seconds) on Product Hunt (QuoteDash page [link](https://www.producthunt.com/posts/1236419), name-to-link mapping unverified), [Estimation Pro AI](https://www.capterra.com/p/10036618/Estimation-Pro-AI) (photos and voice notes to estimates), [BuildFolio](https://build-folio.com/features/ai-photo-to-quote/), [QuoteIQ](https://myquoteiq.com/ai/), [CountBricks](https://apps.apple.com/app/id6738529690). [TierMenu](https://www.reddit.com/r/ProHVACR/comments/1x0tgrx/) (r/ProHVACR, 2026-10-08): good, better, best options on a phone for 1-5-tech shops, free now, priced later at $99 a month for the whole shop. A [free generator](https://www.reddit.com/r/sweatystartup/comments/1xdz038/) was posted 2026-10-24 (title only).
- YC: [Broccoli AI](https://ycombinator.com/companies/broccoli-ai) (voice agents for plumbing and HVAC that book in ServiceTitan and follow up on open estimates), [Elyos](https://www.ycombinator.com/launches/OIa-elyos-ai-ai-customer-service-reps-built-for-trades-and-field-services), [Acrely](https://www.ycombinator.com/companies/acrely), [Oncactus](https://www.ycombinator.com/companies/oncactus) and [Robby](https://www.ycombinator.com/companies/robby). Mostly phone-answering, adjacent. Handoff (YC) covers remodelers.
- Classification: CROWDED. Many funded or popular products and several small ones do voice or photo to quote; the platforms are adding it.
- Platform risk: high. Jobber, Housecall Pro and ServiceTitan each have voice features shipping and own the price book and the customer. Likely within 12 months: photo plus voice to tiered options inside the suite. A frontier assistant can build a quote from pasted notes but has no price book or sync. This caps Scale at 2 and Whitespace at 3 even before the crowd.

## 11. Business model
- Payer: the shop owner. Price hypothesis: $99 a month per shop (up to 3 techs), $25 per extra tech. Anchors: TierMenu's announced $99 a month per shop, a $99 a month Jobber or Housecall Pro complaint (r/sweatystartup title), ServiceTitan "$500" pushback (REV-10).
- Cost per active shop per month [ESTIMATE], 3 techs x 44 estimates = 132: transcription 132 x 4 minutes x $0.003 = $1.58; photos 132 x 8 x $0.003 (middle of the $0.0003-$0.01 range) = $3.17; Sonnet 5.5 estimate call with a cached 5,000-token price book at $0.10/1M ($0.0005) plus 3,000 fresh tokens at $2/1M ($0.006) plus 1,800 output at $10/1M ($0.018) = $0.0245 x 132 = $3.23; follow-up drafts 132 x 3 Haiku 5.5 calls x $0.00055 = $0.22; sync and infrastructure $2.00. Total about $10.20.
- Gross margin (99 - 10.20) / 99 = 90%.

## 12. Market size
Bottom-up [ESTIMATE]: search summaries of Census County Business Patterns list 111,207 HVAC and plumbing establishments (2023) and 81,842 electrical establishments (2022), about 193,000. Assume 40% have 2-10 techs and use Jobber, Housecall Pro or similar: about 77,000. At 1.5% penetration, 1,155 shops x $99 x 12 = $1.4M ARR.

## 13. Go-to-market
- First 100: post demos and a free "good-better-best template" in r/HVAC and r/ProHVACR, give 20 shops a free month, and list in the Jobber and Housecall Pro app marketplaces if they exist [UNVERIFIED]. SEO: "good better best template HVAC", "how to price an HVAC replacement", "ServiceTitan alternative for small shops".
- Loop: customer-facing estimate pages carry a small "estimate by Job Walk" footer on the free tier; techs who change shops bring the tool.

## 14. Moat and scale path
The shop's price-book mapping, nameplate history and follow-up outcomes. Scale path: install quotes with permits, maintenance agreements, commercial. Platform risk makes this a 2.

## 15. Solo feasibility
- MVP in about 7 weeks: phone capture, transcription, nameplate reading, price-book CSV import, option generator, customer text page, follow-up scheduler; Jobber or Housecall Pro API push later [UNVERIFIED].
- Running cost before revenue: about $70 a month.
- Hardest risk: price accuracy. One wrong $2,000 line in front of a homeowner ends trust. Second, write access to the field-service app.

## 16. Pre-mortem
1. The platforms ship photo and voice estimates natively; a $99 add-on loses to a free feature.
2. Mapping errors on messy price books, so techs re-check every line and save no time.
3. Price pressure from free generators and small $99 tools leaves too little revenue per shop.

## 17. Cheapest validation test
Recruit 8 shops on Jobber or Housecall Pro. Three techs per shop walk 10 real jobs each; I process the voice and photos with the shop's price-book CSV and return drafts within an hour. Cost about $100 and 3 weeks. Pass: at least 90% of lines correct, time to estimate under 3 minutes, 5 of 8 shops keep using it after two weeks, 3 pay $99. Fail: line accuracy under 80% or no one reaches for it.

## 18. Open questions
- Recommendation: kill the generic voice-to-estimate product. The one wedge worth a test is HVAC replacement options from a nameplate photo matched to the shop's equipment tiers, for Jobber and Housecall Pro shops; check first whether equipment data (for example the AHRI directory) can be used legally [UNVERIFIED].
- Do Jobber and Housecall Pro expose APIs to create estimates, and do their marketplaces admit competitors of their AI?
- How fast will ServiceTitan's Atlas and Jobber's voice mode produce tiered estimates from photos?
- Is estimate time or follow-up the real lever for close rate?
