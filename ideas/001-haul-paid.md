---
id: "001"
slug: haul-paid
name: Haul Paid
one_liner: "Collects detention, layover and short-pays for small carriers by turning rate cons, BOLs and ELD logs into escalating claims."
target_user: "Owner-operators and 1-10 truck carriers hauling for freight brokers"
form_factor: "web app"
lens: "Pain-first"
frontier: false
competition: "WEAK DIRECT"
confidence: "MED"
status: "developed"
signals: [PRO-029, PRO-030, GAP-20, PRO-026, REV-35]
scores:
  pain: 4
  evidence: 3
  ai_leverage: 3
  whitespace: 2
  novelty: 3
  why_now: 2
  solo_feasibility: 3
  distribution: 3
  wtp_economics: 3
  scale_defensibility: 2
total: 57.9
price_hypothesis: "20% of money recovered, nothing if nothing is recovered"
model_cost_per_user_month: "$1.15"
gross_margin: "90%"
mvp_weeks: 6
deep_dive: false
red_team: false
---

# Haul Paid

## 1. One-liner
Collects detention, layover and short-pays for small carriers by turning rate cons, BOLs and ELD logs into escalating claims.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 4 | Short-pays of $100-375 on $1,000 loads and a $650 detention rejection (PRO-030, GAP-20) recur load after load; real money. |
| Evidence quality | 2 | 3 | Two strong and one medium carrier signal plus a strong claim-rejection story, but no signal states willingness to pay for a collection tool. |
| AI leverage | 2 | 3 | Model reads rate cons and writes clause-cited claims; dwell math, sending and scheduling are deterministic. |
| Whitespace | 2 | 2 | Hey Bubba, WaitClaim, Detention Source and ELD-marketplace apps already log detention claims; only the escalate-and-collect half looks open. |
| Novelty of insight | 1 | 3 | Selling the broker-AP and surety escalation ladder instead of another timestamp log is a useful twist. |
| Why now | 1 | 2 | Contract extraction and ELD APIs have worked for 2+ years; only the 2026 rejection stories are new. |
| Solo feasibility | 2 | 3 | About 6 weeks for upload, extraction, packets and follow-ups; ELD OAuth and contingency billing add risk. |
| Distribution | 2 | 3 | Trucker forums, SEO and ELD marketplaces are plausible but crowded or gatekept; a broker scorecard is a possible loop. |
| Willingness to pay and unit economics | 2 | 3 | No upfront price removes the barrier and margin is high, but fee per user is about $30 a month and fee leakage is real. |
| Scale and defensibility | 2 | 2 | Feature-sized next to ELD vendors and Hey Bubba; only the broker-behavior dataset compounds. |
| **Total** | | **57.9** | |

Confidence: MED. FRONTIER: no.

## 3. The problem
- Who: owner-operators and 1-10 truck carriers hauling for brokers under a rate confirmation (rate con). The rate con promises detention (usually after about 2 free hours), layover, TONU and lumper reimbursement, but only if the carrier gives notice on time, proves the times (signed BOL, ELD or GPS) and submits paperwork inside the broker's window.
- Cost: brokers short-pay $100-375 on $1,000 loads (PRO-030) and refuse detention the rate con spells out (PRO-029). A back office that checks every POD daily still lost a $650 detention claim to a missing signed BOL time and a missed 2-hour notice email (GAP-20). At 24 loads a month, 8% disputed and $200 average [ASSUMPTION], a 2-truck carrier leaves about 24 x 0.08 x $200 = $384 a month unclaimed, plus hours of emailing.
- Workaround: repeated emails over weeks, forum advice, a factor that needs the updated rate con, timestamp apps that stop at documenting, or giving up. Surety-bond claims and FMCSA complaints exist but are rarely used because carriers fear losing the broker.
- The other side is overloaded too (45 minutes a day of check calls, PRO-026), which is why brokers default to "no proof, no pay".

## 4. Evidence
- PRO-029 (strong, r/FreightBrokers, 2026-07-01): carrier chasing detention that is "perfectly outlined" in the contract. "Why does it take multiple emails, weeks to follow up for detention and layover pay that's perfectly outlined in your contracts?"
- PRO-030 (medium, TruckersReport, 2026-06): short-pays blamed on tracking and BOLs the carrier says it sent. "They charge for not tracking even tho i was tracking, they are claiming it was not for the whole trip. $250 for not sending bols even tho it was sent."
- GAP-20 (strong, r/FreightBrokers, 2026-10-27): $650 detention claim rejected for a missing signed BOL time and a missed 2-hour notice email; the firm pays an offshore team to check paperwork daily and still leaks. "we have an offshore team going through all our PODs, rate cons, and receipts every day but stupid stuff like this still slips through. lost lumper receipts, unsigned BOLs, or invoices sitting for days while someone chases down a legible scan."
- PRO-026 (strong, 2026-09-30): the broker-side workload that drives short-pays. "Check calls are most of it, 45 min a day chasing carriers for a location so I can relay it to a shipper who's already emailed me twice."
- REV-35 (strong, App Store, 2026-09-28): ELD data is not clean evidence. "It does this 7 times a day, i lose 3.5h of my time a week." (Motive logs short stops as driving, so ELD-derived dwell can be wrong or contested.)
- No extra first-person evidence turned up in the competition research; the competitors below are indirect evidence that carriers pay for detention proof.

## 5. The product
- Outcome: the carrier forwards load paperwork and a claim is built, sent, chased and escalated until paid; the carrier approves each rung with one tap.
- Core AI loop: input (rate con PDF or email, BOL and POD photos, lumper receipts, ELD or GPS export, broker remittance emails) -> model work (extract free time, rate, notice rule, TONU, layover, claim window and AP email; compute dwell against the appointment; find shortfalls against what was paid; draft a clause-cited claim; classify replies as paid, denied, "need X" or partial offer) -> output (evidence packet, timed follow-ups, escalation packet) -> feedback (each outcome updates a per-broker profile of accepted proof and AP contacts).
- Escalation ladder, human-approved: day 0 claim to AP; day 7 reminder quoting the clause; day 14 escalation to the broker's operations contact and the shipper when known; day 21 notice of intent to file a surety claim; day 30 surety-claim packet (written demand, rate con, BOL, POD, invoice) and an FMCSA complaint draft.
- Interaction: a forwarding email address plus a phone web app for photos and one-tap approvals; SMS prompts. No ELD API at launch (CSV or PDF export and phone location history).
- Day in the life: Maria runs 2 trucks. She forwards the rate con at pickup and photographs the signed BOL at delivery, which shows 3h20m on site against 2h free at $50/hour. The next morning the broker pays $0 of the $67 detention. Haul Paid sends the claim with timestamps; on day 9 the broker offers half; Maria taps "counter at full" or "accept".

## 6. Why the LLM is load-bearing
Rate cons arrive as PDFs, email text, portal screenshots or photos, and each broker words free time, notice, caps and claim windows differently; replies are free text. Without the model you have a timestamp log and a template letter (what the apps do) and a person must read every contract and answer every reply. The model turns unstructured paper into a clause-cited claim and a next step.

## 7. The insight
Evidence logging is crowded and is not what stops payment. Claims die at the broker's AP desk for paperwork reasons (late notice, missing signed time) and by attrition because the carrier will not chase for weeks. The carrier's real leverage (surety bond, regulator complaint, the shipper) goes unused because assembling it is tedious and risks the relationship. A third party that chases in AP's language and carries a credible escalation changes the broker's calculus, and the pooled outcomes (which brokers pay what, how fast) become a product of their own.

## 8. Why now, and why this does not exist yet
Honest: half of it exists. Hey Bubba launched Bubba AI on 2025-03-25 and now reads detention terms from the rate con and starts the clock from ELD geofences on 100+ ELDs; Samsara and Motive ship detention reports and marketplace apps. I did not find a carrier-side product that runs the collection ladder (AP escalation, surety packet) or the short-pay dispute (missing BOL, tracking fees); Hey Bubba links pages titled "I'm Not Getting Paid for Accessorials" and "The Broker Hasn't Paid Me" that I could not read, so that gap is unverified. Why now: models read messy contracts for cents per load, ELD data is reachable through marketplaces, and 2026 threads show the dispute pattern continuing. There is no regulatory forcing function.

## 9. Inspiration and derivation
- Parents: chargeback-evidence recovery on contingency (Chargeflow 25%, Disputifier 20% capped at $250 per won case, from SVC-45), freight-bill audit for brokers and factors (Lighthouz AI, YC S24), detention timers (Hey Bubba, Motive and Samsara reports).
- Changed: target user (small carrier, not merchant or broker), core job (collect after the fact with escalation, not log and prove), business model (contingency per recovery), distribution channel (trucker forums and ELD marketplaces).

## 10. Competition check
- Queries run: (1) "detention pay claim software for owner-operators broker short pay rate confirmation automate demand letter"; (2) "site:producthunt.com trucking carrier detention pay rate confirmation AI" (no Product Hunt pages returned); (3) "site:ycombinator.com/companies freight carriers detention accessorial payments AI"; (4) "Motive Samsara detention time geofence automatic detention report AI trucking 2026"; (5) "Hey Bubba AI dispatcher owner-operators funding raised bubba.ai trucking"; (6) "WaitClaim detention claim app GPS timestamps owner-operators broker documentation"; (7) "broker unpaid carrier BMC-84 surety bond claim process carrier filing factoring company help short pay dispute"; (8) "freight factoring company helps carriers collect detention short pay broker disputes AI Denim Triumph RTS Apex Capital 2026". App Store lookup with scripts/app_reviews.py returned HTTP 403 on 5 of 6 tries, so store listings came from the web searches. Pages read: two bubba.ai pages; the WaitClaim SaaSHub page returned 403.
- [Hey Bubba! / Bubba AI](https://bubba.ai/solutions/detention-management): carrier-side detention management; terms "read from the rate confirmation", dwell clock from ELD geofences, claim "filed with timestamps and the agreed terms attached", broker "can be notified while the truck is still sitting"; works on loads it did not book; connects to 100+ ELDs; no price shown, "Start FREE". Launch: [GlobeNewswire 2025-03-25](https://www.globenewswire.com/fr/news-release/2025/03/25/3048891/0/en/Hey-Bubba-Inc-Launches-Bubba-AI-the-First-Agentic-Voice-AI-Dispatcher-for-Owner-Operators-and-Small-Fleets.html); [Motive integration](https://helpcenter.gomotive.com/hc/en-us/articles/31856080544413-How-to-enable-Hey-Bubba-integration). Funding not found. Its [broker-won't-pay page](https://bubba.ai/problems/broker-wont-pay-detention) shows no demand letter, AP escalation, bond claim or FMCSA step. Closest competitor; it is a dispatcher first.
- [WaitClaim](https://www.saashub.com/waitclaim): progressive web app that records GPS arrival and departure times and makes broker documentation (vendor claim, via search snippet; price and traction not found).
- [Detention Source](https://apps.apple.com/ca/app/detention-source/id6444958697) and [Detention Source Lite](https://apps.apple.com/ca/app/detention-source-lite/id6480213112): App Store detention apps (listing only, features not read). [Trucker Tools](https://www.truckertools.com/detention-strategies-for-owner-operators-and-small-carriers/) publishes detention guidance and a carrier app.
- ELD vendors: [Samsara detention reports](https://www.samsara.com/ca/blog/introducing-detention-reports), [Motive facility insights](https://gomotive.com/blog/introducing-facility-insights/), Motive marketplace apps [GeoStamp by WiseTech](https://marketplace.gomotive.com/app/geostamp-by-wisetech-global) and a [VTTI/FMCSA detention study](https://marketplace.gomotive.com/app/vtti-fmcsa-detention-study.md). They measure dwell; none sends claims. Motive complaints (REV-35) show the ELD side is itself noisy.
- Recovery services: [RevRecoup](https://revrecoup.com/go/logistics-freight/) says it works freight receivables for carriers and brokers on pure contingency (vendor claim, fee not shown). [Lighthouz AI](https://www.ycombinator.com/companies/lighthouz-ai/jobs) (YC S24) automates freight bill audit for brokers, 3PLs and factors, the other side of this problem.
- Bond route: [PFA](https://pfaprotects.com/surety/bmc-84-bmc-85-claims-submittal/) administers BMC-84 and BMC-85 claims for sureties; [TIA](https://tianet.org/?p=18943) says the bond covers unpaid freight charges only, the surety generally must respond within 30 days, and the $75,000 is shared by all claimants; [OTrucking](https://otrucking.com/resources/guides/broker-bond-claims/) gives the demand-letter, FMCSA-complaint, bond-claim sequence. No factoring company with a detention-recovery product turned up.
- Classification: WEAK DIRECT. Direct tools cover the evidence half; I found none that runs the collection ladder or short-pay disputes, and the ones found are small or unpriced.
- Platform risk: Hey Bubba is the likeliest to add escalation, and Motive or Samsara could turn dwell data into claims, though suing the brokers who also use them is awkward. A generic assistant can draft a demand letter from pasted files but cannot watch the inbox, hold ELD data or file the bond packet. Within 12 months I put the risk at medium; it caps Scale at 2.

## 11. Business model
- Payer: the carrier. Price hypothesis: 20% of money recovered, nothing if nothing is recovered (anchored on 20-25% contingency fees for chargeback recovery in SVC-45; carrier willingness is untested).
- Model and variable cost per active user per month [ESTIMATE], 2-truck carrier, 24 loads (12 per truck [ASSUMPTION]): OCR of 6 pages per load = 144 pages x $4/1,000 = $0.58; Sonnet 5.5 extraction at 6,000 in + 800 out = 6,000 x $2/1M + 800 x $10/1M = $0.020 per load x 24 = $0.48; claim packets and replies for 1.9 disputed loads at (10,000 in + 1,500 out on Sonnet = $0.035) + (6 Haiku calls = $0.003) = $0.07. Model and OCR total about $1.13.
- Other variable cost: human QA 1.9 claims x 3 minutes at $9/hour (VA rate band from SVC-61) = $0.86; certified-mail packets for 5% of claims at $8 each [ASSUMPTION] = $0.76; email about $0.01. All-in about $2.80.
- Revenue: 1.9 claims x $200 average x 50% recovered [ASSUMPTION] x 20% = $38, less 15% fee leakage = $32. Gross margin (32 - 2.8) / 32 = about 90%. Revenue per user is small and uncertain, which is the real economic risk.

## 12. Market size
Bottom-up [ESTIMATE]: [FleetOwner (2019)](https://www.fleetowner.com/research/article/21703420/2019-for-hire-500-top-carriers-in-north-america) put for-hire fleets above 777,000, about 91% with six or fewer trucks (figure read from a search summary, article not opened), so roughly 707,000 small fleets; a [Datawrapper chart](https://datawrapper.dwcdn.net/7Adxc/1/) titled as showing 1-to-6-truck fleets still declining through 2025 (data not read), so I use 40% of it as active: 280,000, call it 300,000. Assume 60% haul for brokers: 180,000. At 2% penetration (3,600 carriers) x $32 a month x 12 = about $1.4M ARR. The ceiling is low; growth needs factors, insurers or ELD vendors as partners, or the broker-side audit product.

## 13. Go-to-market
- First 100: answer detention and short-pay questions where carriers ask (r/OwnerOperators, r/Truckers, TruckersReport threads such as the PRO-030 one), publish free tools (detention calculator, rate-con clause checker, BMC-84 claim letter generator), and run the concierge test below. SEO targets: "broker short paid me", "how to file a BMC-84 claim", "detention invoice template", "broker refuses detention pay".
- Marketplaces: Motive and Samsara app marketplaces after the MVP; both already list detention partners, so approval is not guaranteed.
- Loop: every claim packet carries a link to the broker's payment record; carriers check a free broker scorecard (days to pay, detention approval rate, pooled from outcomes) before accepting a load, which brings new carriers and gives brokers a reason to pay.

## 14. Moat and scale path
The pooled broker-behavior dataset, per-broker AP contacts and the proof each accepts, and ELD integrations. Scale path: all accessorials (TONU, lumper), invoice audit for small brokers (the PRO-026 side), factor partnerships on rev share. Weak against Hey Bubba and ELD vendors if they add collection.

## 15. Solo feasibility
- MVP in 6 weeks: inbound email parser and uploads, rate-con extraction, dwell calculation from CSV or GPS export, claim and surety packet PDFs, send-and-follow-up scheduler, card on file with Stripe, a QA console.
- Running cost before revenue: about $60-100 a month (models $20, hosting $20, OCR $10, email $10, domain and tools).
- Hardest risk: extracting terms reliably from varied rate cons and getting trustworthy timestamps without an ELD API; second, collecting the contingency fee after the broker pays.

## 16. Pre-mortem
1. Most claims fail on missed notice, so recovery is under 30% and fees are too small; Hey Bubba already covers the live notice step.
2. Carriers will not pay a fee after the money arrives; leakage above 30% breaks the model.
3. Sub-$500 claims are too small for bond claims, so the escalation threat is empty and brokers ignore it; Hey Bubba or an ELD vendor adds collection first.

## 17. Cheapest validation test
Concierge test: recruit 15 carriers from r/OwnerOperators and TruckersReport, collect their last 5 loads of paperwork, build and send claims by hand. Cost about $0 plus 20 hours over 30 days. Pass: 8 or more carriers share documents, average recoverable above $150 per carrier-month, 40% or more of claims paid within 30 days, 5 or more agree in writing to a 20% fee. Fail: recovery under 25% or carriers refuse to share documents.

## 18. Open questions
- Does a BMC-84 or BMC-85 claim cover detention and layover, or only linehaul? Sureties differ [UNVERIFIED].
- What share of denials come from missed notice versus missing proof (GAP-20 suggests both)?
- Do brokers answer a third party's demand as fast as the carrier's own? Could contingency fees trigger state collection-agency licensing [UNVERIFIED]?
- What do Motive and Samsara require to list a claims app, and how much does Hey Bubba do after "claim filed"?
