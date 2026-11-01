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
  novelty: 2
  why_now: 3
  solo_feasibility: 3
  distribution: 3
  wtp_economics: 2
  scale_defensibility: 2
total: 55.8
price_hypothesis: "20% of money recovered, nothing if nothing is recovered"
model_cost_per_user_month: "$1.15"
gross_margin: "90%"
mvp_weeks: 6
deep_dive: true
red_team: true
---

# Haul Paid

## 1. One-liner
Collects detention, layover and short-pays for small carriers by turning rate cons, BOLs and ELD logs into escalating claims.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 4 | Short-pays of $100-375 on $1,000 loads and a $650 detention rejection (PRO-030, GAP-20) recur load after load; real money. |
| Evidence quality | 2 | 3 | Two strong and one medium carrier signal plus a strong claim-rejection story, but no signal states willingness to pay for a collection tool. Calibrated 3 to 4: GAP-20 adds a strong detention-claim rejection signal; five signals with money lost per load Red team: 4 to 3, red team: only one of five signals is clearly a small carrier; no WTP statement |
| AI leverage | 2 | 3 | Model reads rate cons and writes clause-cited claims; dwell math, sending and scheduling are deterministic. |
| Whitespace | 2 | 2 | Hey Bubba, WaitClaim, Detention Source and ELD-marketplace apps already log detention claims; only the escalate-and-collect half looks open. |
| Novelty of insight | 1 | 2 | Selling the broker-AP and surety escalation ladder instead of another timestamp log is a useful twist. Red team: 3 to 2, red team: the third-party escalation insight does not survive the compliant design |
| Why now | 1 | 3 | Contract extraction and ELD APIs have worked for 2+ years; only the 2026 rejection stories are new. Calibrated 2 to 3: cheap document models make per-load claims worth assembling |
| Solo feasibility | 2 | 3 | About 6 weeks for upload, extraction, packets and follow-ups; ELD OAuth and contingency billing add risk. |
| Distribution | 2 | 3 | Trucker forums, SEO and ELD marketplaces are plausible but crowded or gatekept; a broker scorecard is a possible loop. |
| Willingness to pay and unit economics | 2 | 2 | No upfront price removes the barrier and margin is high, but fee per user is about $30 a month and fee leakage is real. Red team: 3 to 2, red team: contingency fee is license-gated; $29 flat untested with cancel-after-win churn |
| Scale and defensibility | 2 | 2 | Feature-sized next to ELD vendors and Hey Bubba; only the broker-behavior dataset compounds. |
| **Total** | | **55.8** | |

Confidence: MED. FRONTIER: no.

Red-team adjustment (main researcher, 2026-11-01): evidence quality 4 to 3 (red team: only one of five signals is clearly a small carrier; no WTP statement); willingness to pay and unit economics 3 to 2 (red team: contingency fee is license-gated; $29 flat untested with cancel-after-win churn); novelty of insight 3 to 2 (red team: the third-party escalation insight does not survive the compliant design).

Calibration (main researcher, 2026-10-31): evidence quality 3 to 4 (GAP-20 adds a strong detention-claim rejection signal; five signals with money lost per load); why now 2 to 3 (cheap document models make per-load claims worth assembling).

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

## Deep dive

Method (reads dated 2026-10-31): FMCSA open data (Company Census File via the data.transportation.gov API), WebFetch of bubba.ai and harborcompliance.com (a third page, Boostly's B2B compliance guide, returned HTTP 503), 4 web searches (collection licensing, Hey Bubba pricing, small-carrier counts, detention apps), and the Arctic Shift Reddit archive for channel volume. Model prices: `research/LANDSCAPE.md` section 6. Research, not legal advice.

### Competitor table
| Competitor | Link | What it does | Price (as published, with date read) | Funding or traction (sourced) | Gap this idea exploits |
|---|---|---|---|---|---|
| Hey Bubba / Bubba AI | [owner-operators](https://bubba.ai/product/owner-operators), [detention](https://bubba.ai/solutions/detention-management) | AI dispatcher for 1-5 truck carriers: load search, rate negotiation, booking. Detention terms read from the rate con, dwell clock from ELD geofences (detention page, first pass). Shows "Broker credit and days-to-pay" before booking | "your first five booked loads are free, then Bubba charges 2.99% of the negotiated rate on each load it books", "no subscription, no seat fees and no minimum"; "Back-office automation is priced separately (contact us)" (read 2026-10-31). Detention page: "Start FREE" | No funding or customer counts found. Launch: [GlobeNewswire 2025-03-25](https://www.globenewswire.com/fr/news-release/2025/03/25/3048891/0/en/Hey-Bubba-Inc-Launches-Bubba-AI-the-First-Agentic-Voice-AI-Dispatcher-for-Owner-Operators-and-Small-Fleets.html) | The owner-operator page says nothing on short-pay, demand letters or escalation. Its days-to-pay display overlaps my broker-scorecard loop (section 13), so the scorecard must show detention approval rate instead |
| Timer and invoice apps: WaitClaim, Detention Pay Tracker, Detention Source (+Lite), DMRG Detention Pay, Trucker Tools | [WaitClaim](https://www.saashub.com/waitclaim), [Pay Tracker](https://pollen-pond-d92.notion.site/Detention-Pay-Tracker-Help-FAQ-39082e9d604e804ebb1efd01981f30ad), [Detention Source](https://apps.apple.com/ca/app/detention-source/id6444958697), [DMRG](https://apps.apple.com/app/id6502769929), [Trucker Tools](https://www.truckertools.com/detention-strategies-for-owner-operators-and-small-carriers/) | Geofence or one-tap timestamps, then a PDF invoice or certificate for the broker ("generate a PDF invoice before the driver leaves the yard", WaitClaim; Pay Tracker targets 1-5 trucks). Search summaries, pages mostly not opened | not published, except DMRG "free with in-app purchases" (search summary) | none found | They stop at a document. No reminders, reply reading or escalation |
| Telematics add-ons: Samsara, Motive Facility Insights, GeoStamp, FleetOptos; McLeod TMS module | [Samsara](https://www.samsara.com/ca/blog/introducing-detention-reports), [Motive](https://gomotive.com/blog/introducing-facility-insights/), [GeoStamp](https://marketplace.gomotive.com/app/geostamp-by-wisetech-global), [FleetOptos](https://marketplace.geotab.com/solutions/fleetoptos/), [McLeod](https://www.mcleodsoftware.com/detention/) | Measure dwell from ELD or Geotab data; FleetOptos "automates detention billing" (search summary) | not published on pages seen | not sourced here | Need a telematics or TMS subscription; stop at the bill |
| RevRecoup | [page](https://revrecoup.com/go/logistics-freight/) | Human recovery of freight receivables on contingency (vendor claim) | fee not shown | not found | A service, not self-serve; minimum claim size unknown [UNVERIFIED] |
| Lighthouz AI (YC S24) | [YC page](https://www.ycombinator.com/companies/lighthouz-ai/jobs) | Freight-bill audit for brokers, 3PLs, factors | not published | YC S24 | Broker side of the same dispute |
| Bond-claim guides: PFA, TIA, OTrucking | [PFA](https://pfaprotects.com/surety/bmc-84-bmc-85-claims-submittal/), [TIA](https://tianet.org/?p=18943), [OTrucking](https://otrucking.com/resources/guides/broker-bond-claims/) | How to file a BMC-84/85 claim; TIA: covers unpaid freight charges only, $75,000 shared by all claimants (first pass) | free | n/a | Free information; building the packet is the work |
| New free builders, r/OwnerOperators | [2026-10-20](https://www.reddit.com/r/OwnerOperators/comments/1xb5gz4/), [2026-09-14](https://www.reddit.com/r/OwnerOperators/comments/1wg0ha9/) | Title: "New CDL driver here. I built a free app to stop working detention for free. Need 10 owner-operators"; another poster: "I'm researching how small carriers/owner-operators actually handle detention and accessorial pay." | free | 1 point, 0 comments each | Free logging keeps arriving; charge for follow-up and escalation, not the log |

Read across: every direct tool stops at a timestamp, invoice or certificate; I found none that chases, reads replies or builds the surety packet. Hey Bubba is priced as a dispatcher (2.99% of booked loads), so collection would be a new line for it. WEAK DIRECT still fits.

### Market sizing (bottom-up)
Source: FMCSA Company Census File, `https://data.transportation.gov/resource/az4n-8mr2.json?$select=count(*)&$where=...`, queried 2026-10-31 with `status_code='A' AND carrier_operation='A' AND classdef like '%AUTHORIZED FOR HIRE%'` (active, interstate, for-hire) and an `mcs150_date` filter. Active carriers: 251,033 updated in the last 12 months, 416,154 in 24 months. 1-5 power units: 199,566 (79.5%) and 334,424 (80.4%); of the 24-month group 217,052 run one truck. 6-10 units: 17,074 and 26,498. "For hire" is self-reported and some carriers are dormant, which the two filters bracket. The share that hauls for brokers is not in the data: 40% to 60% [ASSUMPTION]. The first-pass 180,000 sits inside this range.

| Case | Buyers | Adoption | Annual price | Serviceable ARR |
|---|---|---|---|---|
| Conservative | 199,566 x 40% = 79,826 | 1% = 798 | $29 x 12 = $348 | $0.28M |
| Optimistic | 360,922 (1-10 units, 24 months) x 60% = 216,553 | 5% = 10,828 | $39 x 12 = $468 | $5.07M |

Revenue at 100 / 1,000 / 10,000 customers: $34.8K / $348K / $3.48M at $29 a month; $46.8K / $468K / $4.68M at $39. 10,000 would be 12.5% of the conservative pool, so that row is out of reach without partners or a broker-side product. Feature-sized market.

### Unit economics
2-truck carrier, 24 loads, 8% disputed = 1.92 loads [ASSUMPTION]. All lines [ESTIMATE], per customer-month.
| Line | Arithmetic | $ |
|---|---|---|
| OCR (price UNVERIFIED) | 24 x 6 pages = 144 x $4/1,000 | 0.58 |
| Rate-con extraction, Sonnet 5.5 | (6,000 x $2/1M) + (800 x $10/1M) = $0.020 x 24 loads | 0.48 |
| Claim draft + 6 reply reads | 1.92 x [($0.020 + $0.015 Sonnet) + 6 x ($0.0003 + $0.00025 Haiku 5.5)] = 1.92 x $0.0383 | 0.07 |
| Human QA | 1.92 x 3 min at $9/hour | 0.86 |
| Certified mail, 5% of disputes | 1.92 x 0.05 x $8 [ASSUMPTION] | 0.77 |
| SMS and email | 20 x $0.008 [ASSUMPTION] + $0.01 | 0.17 |
| Stripe on $29 | 2.9% x $29 + $0.30 | 1.14 |
| Infrastructure share | $80 / 100 customers | 0.80 |
| **Total** | | **4.87** |

Gross margin at $29: (29 - 4.87) / 29 = 83%. The 90% in section 11 left out Stripe and infrastructure. Contingency variant: 1.92 x $200 x 50% recovered x 20% = $38.40; after 15% leakage $32.64; Stripe $1.40; cost $5.13; margin 84%, but it rests on an unmeasured recovery rate.
**Heavy user:** 6 trucks, 100 loads, 15 disputes, 4.5 certified packets. OCR $2.40 + extraction $2.00 + disputes $0.57 + QA 90 min x $9/hour = $13.50 + mail 4.5 x $9.65 = $43.43 (per-letter cost from idea 008) + SMS and fees about $2.5 = about $65 to $69 against $29: a loss of about $35 a month. Caps fix it: $29 includes 30 loads, then $0.75 a load; $15 per certified packet. Revenue 29 + 70 x 0.75 + 4.5 x 15 = $149 against about $69: margin 54%. Mail and human QA are the cost, not models.

**Fee structure and the collection-agency question.**
- Sources: Harbor Compliance's 50-state guide (read) lists "Collecting commercial debts" among activities that "require this license type", says "Some states provide statutory exemptions" including "entities that collect 100% business-to-business debt" (no states named), and mentions a bond and fees ([page](https://www.harborcompliance.com/information/debt-collection-agency-license)). A law firm says 34 states license collection agencies and 16 do not ([mslaw.com](https://www.mslaw.com/mslaw-blog/collection-agency-licensing-and-exemptions), search summary). A collector's marketing page claims 20 states license commercial collectors ([UNVERIFIED]). A 2001 Washington bill report allowed fees up to 35% on commercial debts ([bill report](https://lawfilesext.leg.wa.gov/Biennium/2001-02/Htm/Bill%20Reports/Senate/5331.FBR.htm), historical, search summary): contingency fees on business debts are statute-regulated in at least one state.
- Not established: a reliable state list for third-party business-debt collectors, and whether software that drafts and sends a creditor's own demand counts. The federal FDCPA is generally understood to cover consumer debts only [UNVERIFIED here, 15 U.S.C. 1692a(5)]. Verdict [UNVERIFIED]: assume a percentage-of-recovery fee for chasing someone else's receivable can need a license in some states.
- Design around it: (1) **v1 is a tool, not a collector:** every message goes out in the carrier's name after the carrier taps approve; Haul Paid never holds money, negotiates, or writes as itself; fee is $29 a month after a 30-day trial plus $15 per certified escalation packet, with a 60-day money-back guarantee, charged by card in advance (this also removes the 15% fee leakage). (2) Success fees only through a licensed partner or attorney for the day-30 rung [UNVERIFIED whether referral fees are allowed]. (3) Get licensed later in the few states with volume if "nothing unless recovered" proves essential. (4) Before charging: one hour with a collections attorney (about $300 to $600 [ESTIMATE]) on sender identity and the day-21 wording. The validation test measures how many carriers still prefer the 20% model.

### First 100 customers
Channel volume (Arctic Shift, days before 2026-10-30, broad regex so upper bounds): r/OwnerOperators about 8.6 posts a day, about 5 a week on detention/short-pay/TONU/lumper; r/Truckers about 47 a day, about 10 a week; r/FreightBrokers about 9 a day, mostly broker-side. Reddit gives 10 to 15 usable threads a week: credibility, not volume. Message: "Your rate con already says what you are owed. We read it, build the claim, send it from your name when you tap approve, and chase it." Offer: first 5 claims free, then $29 a month with a 60-day money-back guarantee. Funnel [ESTIMATE]: reader to click 2%, visit to signup 15%, signup to first upload 50%, upload to paid 40%; about 3% of visits end up paying.

| Week | Action | New paid | Cum. |
|---|---|---|---|
| 1 | Convert the validation-test carriers (15 shared, 50% take the offer). Post the checklist "rate-con clauses that cost you detention" in r/OwnerOperators and the TruckersReport owner-operator forum, after reading each rule. Free clause checker and BMC-84 letter generator | 8 | 8 |
| 2 | 10 value-first replies on short-pay threads (r/OwnerOperators, r/Truckers, TruckersReport). Email 15 outsourced dispatch services, one note each (Hey Bubba's blog says dispatchers commonly charge 5% to 10% of linehaul) | 3 | 11 |
| 3 | Free access for 3 owner-operator YouTube creators for an honest review; referral credit of one free month | 3 | 14 |
| 4 | Publish first pooled numbers (claims sent, paid, median days; no broker names under 10 claims) | 3 | 17 |
| 5 | Pilot 3 dispatch services x 3 carriers; offer 20% revenue share ($5.80 per carrier-month) | 4 | 21 |
| 6 | SEO pages: "broker short paid me", "how to file a BMC-84 claim", "detention invoice template", "broker refuses detention pay", "TONU not paid by broker" | 3 | 24 |
| 7 | Apply to Motive and Samsara marketplaces (approval not guaranteed) | 3 | 27 |
| 8 | Review recovery rate, churn, fee model | 3 | 30 |

Base case about 30 paying by week 8; 100 needs the dispatcher channel (weeks 9 to 20: 10 services x 8 carriers at 25% paying = 20, plus forums and SEO). Loop after 100: dispatcher revenue share, referral credits, a consented "which brokers pay detention and how fast" page (different from Hey Bubba's days-to-pay), later a factor partner.

### One-week validation test (under $50)
**What:** a free, manual claim review, labeled as a test run by one person; no software is live and nothing is sold. Day 1: one-page site (GitHub Pages or Carrd free): "Broker shorted you or refused detention? Send the rate con and signed BOL. In 48 hours I tell you what the contract says you are owed and write the claim for you to send. Manual test, no product live, free. I never contact your broker." Google Form takes one load's paperwork plus trucks, loads a month, current process. Days 1 to 2: one post each in r/OwnerOperators and the TruckersReport owner-operator forum (read the rules, own account, no cross-posting); 5 personal emails to dispatch services. Days 2 to 6: run extraction and the claim draft by hand with Sonnet 5.5, check against the PDF, return within 48 hours with a form: were the readings right; would you send it; pricing A (20% of recovered, nothing if nothing), B ($29 a month, money back if no claim paid in 60 days), C neither; optional $10 refundable deposit (Stripe Payment Link). Day 7: tally.
**Budget:** domain $12 (optional); Stripe fees on 5 refunded deposits 5 x ($0.29 + $0.30) = $3; model credit $5 (10 submissions x about $0.06); forms, host, email $0. About $20.
**Pass:** 8 or more loads from 5 or more carriers; 90% or more of extracted terms confirmed correct; 50% or more of loads have a supportable claim; and either 3 or more deposits or 50% of respondents pick A or B. **Fail:** under 4 submissions, or term accuracy under 80%, or 70% pick C, or zero deposits. If most pick A over B, counsel's view on licensing gates launch.

### Build brief (paste into a coding session)
```text
PRODUCT: Haul Paid helps owner-operators and 1-10 truck carriers collect detention, layover, TONU, lumper and short-pays from freight brokers.
The carrier forwards the rate con and delivery paperwork; the app reads the terms, computes what is owed, drafts a clause-cited claim, and follows up on a schedule.
The carrier approves every outbound message with one tap. The app never holds money and never writes to a broker as itself.
MVP FEATURES (each testable)
1 Per-carrier inbound email plus phone upload for rate cons, BOL/POD photos, receipts, broker replies. Test: 5 sample emails, attachments typed correctly.
2 Rate-con extraction to JSON, every term with verbatim quote and page (free time, detention rate, layover, TONU, lumper, notice rule, claim window, AP email). Test: each quote found in the source.
3 Dwell calculator in plain code (appointment, arrival, departure from signed BOL, CSV/PDF GPS export or manual; time zones, overnight, rounding).
4 Shortfall detector: contract vs broker remittance email; output amount owed or "claim not supported" with reason (late notice, missing signed time).
5 Claim draft email plus PDF evidence packet; one-tap approval.
6 Scheduler: day 0 claim, day 7 reminder quoting the clause, day 14 escalation to broker operations, day 21 notice of intent to file a surety claim, day 30 surety packet and FMCSA complaint draft; each rung needs approval.
7 Reply classifier: paid / denied (reason) / needs document / partial offer / auto-reply; proposes next step.
8 Stripe: $29/month, 30-day trial, 60-day money-back, $15 per certified packet, 30-load limit.
9 Founder QA console for low-confidence items. 10 Per-broker profile (AP email, accepted proof, days to pay), internal only.
NON-GOALS: ELD API, moving money, percentage-of-recovery fees (until counsel clears), auto-send, broker-facing product, dispatch or rate negotiation, native apps.
CORE AI LOOP: (a) classify attachments, Haiku 5.5; (b) extract terms with quotes, Sonnet 5.5; (c) read BOL/POD times and signature, Haiku 5.5 vision; (d) dwell and shortfall math in code, no model; (e) draft claims and escalations, Sonnet 5.5; (f) classify replies, Haiku 5.5, Sonnet 5.5 if unsure.
Prompts: extract only what is written, return quote and page, say "not stated" rather than guess; neutral tone; no threat beyond the rate con and published escalation channels. Humans: carrier approves every send; founder reviews the QA queue; lawyer reviews rung 4-5 templates.
DATA MODEL: Carrier, User, Broker(MC, USDOT, AP email, claim window), Load, Stop, Document(type, extracted_json), Term(kind, value, quote, page), DwellEvent(source, confidence), Payment, Claim, Step(rung, due, approved_at, sent_at), Message(classification), Outcome(result, amount, days), AuditLog.
INTEGRATIONS: Stripe https://docs.stripe.com/billing; inbound email via Cloudflare Email Workers https://developers.cloudflare.com/email-routing/email-workers/ or Postmark https://postmarkapp.com/developer/user-guide/inbound; Resend https://resend.com/docs (sender identity to be settled with counsel); Twilio https://www.twilio.com/docs/messaging; Lob certified mail https://docs.lob.com/; FMCSA census https://data.transportation.gov/resource/az4n-8mr2.json (responded 2026-10-31); phase 2 ELD: https://developers.samsara.com/ and https://developer.gomotive.com/.
STACK (about $100 to $120 a month): Next.js on Vercel Pro $20; Supabase Pro $25 (auth, Postgres, storage); Inngest free tier for schedules; Resend $20; Stripe fees; Sentry and Langfuse free; Playwright or react-pdf for packets; domain $12 a year.
EVALS: 1 Extraction, 30 real rate cons from 10+ brokers: 95% field accuracy, 100% quotes verbatim. 2 Dwell math, 20 synthetic cases: 100% exact. 3 Shortfall, 20 contract+remittance pairs, 6 where the broker is right: amount correct in 90%, "not supported" in all 6. 4 Reply classes, 50 labeled replies: 92%, zero false "paid". 5 Tone: 20 drafts never contain "collect", "collection agency" or threats beyond the contract.
BUILD PLAN (6 weeks): W1 auth, Stripe, email-in, storage, extraction v0 and eval harness. W2 BOL/POD reading, dwell, remittance parsing, shortfall; evals 1-3. W3 claim drafting, PDF packet, approval page, sending, scheduler. W4 reply classifier, escalation rungs, surety packet, Lob. W5 QA console, broker profile, retention settings, observability, start concierge group on the live app. W6 billing limits, onboarding, counsel review of templates, beta with 10 carriers.
RISKS TO TEST FIRST: 1 collections law (attorney hour before any percentage fee); 2 recovery rate (40% of supportable claims paid in 30 days; run 15 by hand); 3 extraction accuracy; 4 do top brokers accept email claims or only portals; 5 timestamp quality (signed BOL times decide most disputes; ELD data is noisy, REV-35); 6 Hey Bubba or an ELD vendor adds collection.
```

**Notes for the main researcher:** Licensing is unresolved, so I would not lead with the 20% contingency price until counsel clears it; a flat $29 plus escalation fees gives about the same revenue with no fee leakage. Hey Bubba's owner-operator page already shows broker days-to-pay (overlaps the section 13 scorecard loop). Reddit supplies only about 5 matching threads a week, so Distribution 3 depends on the dispatcher-service channel. No score change proposed.

## Red team
Skeptical-investor review on 2026-11-01 (full text: `research/RED_TEAM_A.md`). Verdict: **pass**.

**Top attacks (summarized):**
1. **The insight and the compliant design contradict each other.** The thesis is third-party escalation pressure, but the licensing-safe design sends every message in the carrier's own name.
2. **The demand evidence is mostly not the buyer.** Only PRO-030 is clearly a small carrier; PRO-029 and GAP-20 come from broker forums, PRO-026 is broker workload, REV-35 an ELD review; none states willingness to pay.
3. **Competition is closer than stated.** Hey Bubba already reads detention terms, runs the dwell clock on 100+ ELDs, files claims with timestamps and shows broker days-to-pay.
What would change the red team's mind: a 15-carrier hand run where 40%+ of supportable claims are paid within 30 days from carrier-name emails alone, 5 carriers paying $29 a month after a real recovery, and one collections-attorney hour confirming the late escalation rungs need no license in the launch states.

**Response (main researcher):**
- Attack 1 lands partly. Carriers can file surety-bond (BMC-84) claims and FMCSA complaints in their own name, so escalation leverage survives without a third-party collector; what is lost is the "outside party" effect. Novelty drops from 3 to 2.
- Attack 2 lands. Evidence drops from 4 to 3 (reverting the earlier calibration bump).
- Attack 3 lands: Hey Bubba covers much of the evidence half; whitespace stays at 2. Willingness to pay drops from 3 to 2 because the contingency model is license-gated and $29 flat is untested.
- Distribution stays at 3: trucker forums, YouTube and Facebook groups are large and reachable by one person.
