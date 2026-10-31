---
id: "010"
slug: closeout-copilot
name: Closeout Copilot
one_liner: "Turns a tech's photos and voice note into the exact closeout each facility-management portal demands."
target_user: "Commercial HVAC, plumbing and electrical shops serving national accounts through facility-management portals"
form_factor: "mobile app"
lens: "Pain-first"
frontier: false
competition: "ADJACENT ONLY"
confidence: "LOW"
status: "developed"
signals: [PRO-004, REV-11, PRO-014, REV-08]
scores:
  pain: 3
  evidence: 2
  ai_leverage: 4
  whitespace: 3
  novelty: 3
  why_now: 3
  solo_feasibility: 2
  distribution: 2
  wtp_economics: 3
  scale_defensibility: 2
total: 53.7
price_hypothesis: "$149/month per shop (up to 5 techs)"
model_cost_per_user_month: "$5.30"
gross_margin: "96%"
mvp_weeks: 7
deep_dive: false
red_team: false
---

# Closeout Copilot

## 1. One-liner
Turns a tech's photos and voice note into the exact closeout each facility-management portal demands.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | Closeouts gate payment and recur on every national-account job, but only a subset of shops has the problem. |
| Evidence quality | 2 | 2 | One direct thread (PRO-004); the other three signals are property-management or ServiceTitan note-taking complaints, adjacent at best. |
| AI leverage | 2 | 4 | Voice to compliant notes, photo categorization and a per-client rules layer are model work; remove it and only forms remain. |
| Whitespace | 2 | 3 | No provider-side, multi-portal closeout assistant found; ServiceChannel is adding provider AI, which caps this at 3. |
| Novelty of insight | 1 | 3 | A rules layer across client portals, run from the van, is a useful twist. |
| Why now | 1 | 3 | Cheap voice and vision plus portal APIs make it practical; the demand side is not new. |
| Solo feasibility | 2 | 2 | Portal access, per-client rules and a no-automation constraint (platform terms) make it hard for one person. |
| Distribution | 2 | 2 | Niche buyer (office manager at a commercial shop), no store or marketplace channel found, mostly outbound. |
| Willingness to pay and unit economics | 2 | 3 | Office labor saved is concrete and margin is 96%, but the buyer pool is small and WTP is untested. |
| Scale and defensibility | 2 | 2 | A shared client-rule library compounds, yet ServiceChannel and ServiceTitan sit on the workflow. |
| **Total** | | **53.7** | |

Confidence: LOW (thin evidence, portal API access unverified). FRONTIER: no.

## 3. The problem
- Who: HVAC, refrigeration, plumbing and electrical shops that take work orders from national accounts (retailers, restaurants, banks) through facility-management portals such as ServiceChannel, Corrigo and Ariba.
- What hurts: after the tech finishes, each portal wants its own check-out, work summary and resolution codes, photos, signature, PO or NTE (not-to-exceed) handling and invoice format, and "nobody owns chasing rejections" (PRO-004). Techs drop notes and photos in field apps, so the office retypes (REV-08, PRO-014, REV-11).
- Cost [ESTIMATE]: 100 closeouts a month x 10 minutes of office rework = 16.7 hours x $22 an hour [ASSUMPTION] = about $367 a month, before late payment from rejected invoices.
- Workaround: an office person re-keys everything from the tech's ticket, keeps a spreadsheet of each client's rules, and chases rejections by email.

## 4. Evidence
- PRO-004 (medium, r/ProHVACR, 2026-10-05, 8 comments): "we’ve got customers wanting stuff through servicechannel, corrigo, ariba etc and it seems like every one of them has their own bullshit with POs, NTEs, photos, signatures, invoice formats, whatever. is somebody in the office basically sitting there keeping track of all this manually?" This is the only direct signal.
- REV-08 (strong, App Store ServiceTitan Field, 2026-09-03): notes the app drops must be retyped. "I’m literally spending an additional 15-20 minutes on each call because this app is just downright bad." Adjacent: a note-taking failure, not a portal rule.
- PRO-014 (medium, App Store AppFolio, 2026-09-01): "I spend more time fixing techs messing up closing out work orders and attaching photos than anything because the app is so difficult to use." Adjacent: property-management work orders, same closeout job.
- REV-11 (medium, App Store AppFolio, 2026-05-03): photo uploads capped at 18 MB, so the user builds a Google folder and pastes a link per request. Adjacent, same photo-handling pain.
- Rules differ per client and are published as documents: ServiceChannel's [Trade Partner Guidelines](https://servicechannel.com/wp-content/uploads/2025/01/Trade-Partner-Guidelines-1.2025.pdf) and a retailer's own [check-in/check-out training for technicians](https://www.aldi-sued.de/supplieronboarding/Dienstleister_Handling_Englisch/servicechannel/check-in-check-out-training-material-for-technicians) (titles only, documents not read).
- No new first-person evidence turned up in a Reddit archive pull of r/ProHVACR, r/HVAC, r/Plumbing and r/electricians (Oct 2025 to Oct 2026) beyond PRO-004. That is itself a warning about how narrow the audience is.

## 5. The product
- Outcome: the tech leaves the site with a complete closeout packet; the office stops reworking tickets. Missing items are caught before the van leaves.
- Core AI loop: input (voice note, 6-10 photos, the work order and the client's rule sheet) -> model work (transcribe, sort photos into the client's required categories such as before, after, nameplate and parts, write the work summary in the client's format and codes, check NTE against the running total and draft an NTE-increase request, list what is missing) -> output (a checklist the tech clears, then a packet the office or tech enters into the portal; later, submission through official portal APIs) -> feedback (a rejection reason updates that client's rules).
- Rules layer: the shop uploads each client's guideline PDFs once; the model turns them into an editable checklist per client and learns from rejections.
- Interaction: phone web app at the van (voice first), office web view. No browser automation of the portal; a human clicks submit (platform-terms risk).
- Form factor: mobile web app (installable PWA) plus office dashboard.
- Day in the life: a tech fixes a restaurant walk-in cooler, says "replaced evaporator fan motor, ran twenty minutes, thirty-eight degrees" and takes seven photos. The app answers: "Missing after-photo of the nameplate. This client wants the part number in the summary. NTE is $450, you are at $520: send an increase request?" He taps twice and drives to the next call.

## 6. Why the LLM is load-bearing
The inputs are a spoken note and unsorted photos, and the outputs differ by client in wording, codes and required images. The rule sheets are free-text PDFs. A fixed template per client cannot read a voice note, sort photos or adapt when a rejection reason changes the rule. Without the model it is a form builder.

## 7. The insight
Closeouts are payment-critical documents whose rules differ per client, which makes them a natural fit for an LLM rules layer. The portal vendors build for the facility-management side; the provider side, spread over several portals, is nobody's product. The cheapest moment to fix a closeout is before the tech leaves the site.

## 8. Why now, and why this does not exist yet
Voice and vision models make the capture cheap (about $0.045 per closeout, section 11). ServiceChannel is moving: its [Spring 2026 release](https://servicechannel.com/blog/spring-2026-product-release/) adds AI help creating work orders (including photo review) and its AI invoice feature that reads a PDF and fills the client's invoice fields is listed as beta for fall 2026 (search summary). The ServiceTitan integration syncs status, hourly invoice exports, NTE values and notes but leaves manual steps. I found no tool that enforces each client's closeout rules from a voice note and photos. Caveat: absence may mean the market is small.

## 9. Inspiration and derivation
- Parents: the ServiceTitan to ServiceChannel integration, ServiceChannel AI summaries and invoice capture, FM-side AI agents for Corrigo (Facilio), chargeback-evidence builders that map evidence to reason codes.
- Changed: target user (the contractor, not the facility manager), core job (closeout compliance and payment, not work-order creation), interaction model (voice and photo at the van), and distribution (contractor communities, not the portal).

## 10. Competition check
- Queries run: (1) "ServiceChannel work order check-out closeout automation invoice NTE PO photos AI contractors"; (2) "site:producthunt.com ServiceChannel Corrigo Fexa contractor work order invoicing automation AI" (no Product Hunt pages returned); (3) "site:ycombinator.com/companies facilities maintenance contractors work orders portal invoicing automation AI"; (4) integration and API directory check: ServiceTitan's ServiceChannel integration page read, and ServiceChannel, Corrigo and Fexa API pages from the results. Also a Reddit archive pull. The App Store lookup script returned HTTP 403.
- [ServiceChannel AI](https://servicechannel.com/tools/ai-what-it-means-for-your-business/): AI summaries and anomaly flags on work orders, photo-aware work-order creation, and invoice-from-PDF capture (beta, fall 2026). Provider check-in and check-out are documented in its [help](https://servicechannel.atlassian.net/wiki/x/mIHZIQ): Completed status, work summary, resolution and root cause codes, optional e-signature. An older [product sheet](https://servicechannel.com/wp-content/uploads/2020/04/ServiceChannel_Work-Order-Manager_Product-Sheet.pdf) shows client-side exception checks on billed rates and hours. No price found; a platform, not a closeout assistant.
- [ServiceTitan integration with ServiceChannel](https://help.servicetitan.com/commercial/docs/servicetitan-integration-with-servicechannel) (page dated 2026-10-16): work orders become bookings, status goes back, invoice status syncs hourly, NTE values go to custom fields, attachments are sent once after completion; unsupported statuses, late attachments and name mismatches stay manual. No rule checking or photo sorting.
- [Corrigo](https://www.jll.com/ar-sa/products/corrigo) (JLL): rules-based automation and invoice routing for the FM side; REST APIs (third-party [doc](https://supergood.ai/docs/corrigo-api)); [Facilio](https://facilio.com/blog/ai-agents-for-corrigo/) sells AI agents on top for facility teams. [Fexa](https://help.fexa.io/hc/en-us/articles/44294426681613-Getting-Started-with-FexaAI) has FexaAI for work-order quality and troubleshooting plus a [provider API](https://fexa.io/api-providers/). ServiceChannel has a third-party-documented [API](https://supergood.ai/docs/servicechannel-api); whether it covers photos and NTE for providers is unverified.
- [CallSphere blog](https://callsphere.ai/blog/who-on-your-payroll-logs-into-servicechannel-every-morning-in-2026-the): describes an agent that posts check-out times from photo timestamps and uploads before and after photos; an illustration from a voice-agent vendor, not a documented product.
- YC: [Upkeep](https://www.ycombinator.com/companies/upkeep) (mobile work-order and asset management, the FM side) and [CentralComs](https://www.ycombinator.com/companies/centralcoms) (property management). Product Hunt: nothing relevant.
- Classification: ADJACENT ONLY. The portal vendors and FM-side agents sit nearby; none does the provider-side, multi-portal closeout job.
- Platform risk: medium to high. ServiceChannel already ships provider-facing AI and could add closeout checks for its own portal within 12 months; ServiceTitan could add rule checks. A multi-portal, per-client rules layer is harder for either to prioritize. General assistants lack portal and client-rule context. This caps Scale at 2 and Whitespace at 3.

## 11. Business model
- Payer: the shop owner or office manager. Price hypothesis: $149 a month per shop (up to 5 techs), $19 per extra tech. Anchors: office rework worth about $367 a month; a work-order AI add-on listed at $200 a month in a search snippet (vendor FlowPath, link not captured) [UNVERIFIED].
- Cost per active shop per month [ESTIMATE], 100 closeouts: transcription 100 x 1.5 minutes x $0.003 = $0.45; photos 800 x $0.003 (middle of the $0.0003-$0.01 vision range) = $2.40; Sonnet 5.5 drafting with a cached 4,000-token rule sheet at $0.10/1M ($0.0004) plus 2,000 fresh tokens at $2/1M ($0.004) plus 800 output at $10/1M ($0.008) = $0.0124 x 100 = $1.24; Haiku 5.5 completeness check $0.00045 x 100 = $0.05; rule-sheet OCR $0.20; infrastructure $1.00. Total about $5.30.
- Gross margin (149 - 5.30) / 149 = 96%.

## 12. Market size
Bottom-up [ESTIMATE]: search summaries of Census County Business Patterns list 111,207 HVAC and plumbing establishments (2023) and 81,842 electrical establishments (2022), about 193,000. Assume 5% do portal-based national-account work [ASSUMPTION]: about 9,650 shops. At 5% penetration of that group (483 shops) x $149 x 12 = $0.86M ARR. Adding refrigeration, roofing, janitorial and landscaping might triple it to about $2.6M. This is a small niche.

## 13. Go-to-market
- First 100: outbound to office managers of commercial shops (state license lists, job posts that mention ServiceChannel or Corrigo), answers in r/ProHVACR and r/HVAC threads like PRO-004, and a free "closeout checklist from your client's guideline PDF" tool. SEO: "ServiceChannel invoice rejected", "NTE increase request template", "ServiceChannel check out photos required".
- Loop: a shared, anonymized rule library per client brand improves every shop that serves the same client. It only works if the guidelines are shareable [UNVERIFIED].

## 14. Moat and scale path
The per-client rule library and rejection history, plus daily use by techs. Scale path: more trades (janitorial, landscaping, pest, roofing), property-management vendor portals, invoice follow-up. A portal vendor shipping the same checks would cap it at 2.

## 15. Solo feasibility
- MVP in about 7 weeks: voice and photo capture, transcription, photo classification, rule extraction from PDFs, closeout checklist and packet, NTE tracker. Portal APIs in phase 2; the shop must supply credentials.
- Running cost before revenue: about $60-100 a month.
- Hardest risk: portal access. Whether providers can write photos and NTE through ServiceChannel, Corrigo or Ariba APIs is unverified, and UI automation would breach platform terms (kill criterion 4), so the fallback is a copy-and-paste packet.

## 16. Pre-mortem
1. The audience is too narrow: one direct thread, a small share of shops, and a buyer who already hired an office person.
2. ServiceChannel's provider AI and the ServiceTitan integration close most of the gap before a solo founder reaches 100 customers.
3. Rejections come from human reviewers at the client, not from rules, so the checklist does not move payment time.

## 17. Cheapest validation test
Recruit 10 commercial shops. Collect three months of rejected or delayed invoices and the portal's stated reasons, then build checklists by hand for 20 closeouts each. Cost about $50 and 25 hours over 4 weeks. Pass: at least 5 shops share data, median 8 or more office minutes per closeout or 10% or more of invoices rejected on first pass, and 3 agree to pay $149 for a 60-day pilot. Fail: rework under 3 minutes or rejections under 3%.

## 18. Open questions
- Do provider APIs for ServiceChannel, Corrigo and Ariba accept photos, NTE changes and codes? What do their terms say about third-party tools?
- How often are invoices rejected on first pass, and why? Are the reasons rules or reviewer whims?
- Who buys: the owner, the office manager or the dispatcher, and do techs close out at the van or in the office?
- Will ServiceChannel's invoice AI (beta, fall 2026) make the office-side half moot?
