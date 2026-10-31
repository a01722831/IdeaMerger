---
id: "032"
slug: authority-guard
name: Authority Guard
one_liner: "Watches a small carrier's FMCSA authority, insurance filings and deadlines daily, and walks the owner through the fix."
target_user: "Owner-operators and 1-10 truck carriers with their own MC authority"
form_factor: "web app"
lens: "Forcing function"
frontier: false
competition: "WEAK DIRECT"
confidence: "MED"
status: "developed"
signals: [FORCE-44, FORCE-42, FORCE-41, PRO-027, FORCE-45]
scores:
  pain: 3
  evidence: 3
  ai_leverage: 2
  whitespace: 2
  novelty: 2
  why_now: 3
  solo_feasibility: 4
  distribution: 3
  wtp_economics: 3
  scale_defensibility: 2
total: 54.7
price_hypothesis: "$12/month per carrier"
model_cost_per_user_month: "$0.20"
gross_margin: "98%"
mvp_weeks: 4
deep_dive: false
red_team: false
---

# Authority Guard

## 1. One-liner
Watches a small carrier's FMCSA authority, insurance filings and deadlines daily, and walks the owner through the fix.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | A suspended MC stops revenue, but events are rare per carrier (a few a year at most) and the Motus peak may be passing. |
| Evidence quality | 2 | 3 | One strong first-person case (FORCE-44), five regulatory facts or adjacent signals, plus three new October 2026 posts and press titles. |
| AI leverage | 2 | 2 | Monitoring and filing-amount checks are deterministic; the model reads policy PDFs, explains and drafts. |
| Whitespace | 2 | 2 | J.J. Keller, Dotra, TruckDocsAI, HaulComply, Trucking Comply and Fleetworthy sell authority or compliance monitoring; the filing-mismatch fix flow is the open slice. |
| Novelty of insight | 1 | 2 | "Monitor the public record and warn the owner" is obvious; the policy-versus-filing reconciliation is a modest twist. |
| Why now | 1 | 3 | Motus (Dec 2025 to 2026) produced suspensions and mismatches; FMCSA is cleaning up, so the spike is partly temporary. |
| Solo feasibility | 2 | 4 | Public data, policy-PDF extraction and alerts fit in about 4 weeks; post-Motus data freshness is the unknown. |
| Distribution | 2 | 3 | Free DOT-number check, SEO and carrier forums work; programmatic carrier pages from rivals already own many lookups. |
| Willingness to pay and unit economics | 2 | 3 | Margin is 98% at $12 a month, but small carriers are price-sensitive and rivals' prices are unknown. |
| Scale and defensibility | 2 | 2 | Public data and small tickets; the moat is trust and alert accuracy only. |
| **Total** | | **54.7** | |

Confidence: MED. FRONTIER: no.

## 3. The problem
- Who: owner-operators and 1-10 truck carriers whose own MC authority is their license to earn. Since FMCSA moved registration to Motus (Phase I opened 2025-12-08; FORCE-42), carriers report suspensions over insurance filings that did not match, inactive status after renewals, and brokers rejecting an MC that looks "ineligible" in one database and active in another.
- Other deadlines that sneak up: MCS-150 biennial update, UCR, BOC-3, IFTA and IRP, plus new driver rules (FORCE-41, FORCE-45) and MC hijacking with fake documents (PRO-027).
- Cost [ESTIMATE]: a 3-truck carrier grossing $450,000 a year (3 x $150,000 [ASSUMPTION]) earns about $1,233 a day, so a 7-day suspension puts about $8,600 of revenue at risk, plus an $80 reinstatement fee in the FORCE-44 case.
- Workaround: calls to FMCSA and the insurance agent (18 minutes on hold and still not reinstated in FORCE-44), forum threads, Motus help blogs from insurers, or a paid managed monitoring service.

## 4. Evidence
- FORCE-44 (strong, r/OwnerOperators, 2026-10-30, 8 comments): a three-truck carrier's filing showed $750,000 of cover while the policy was $1,000,000, and Motus suspended the MC; $80 reinstatement fee, 18 minutes on hold, still not reinstated. "Today they decided that was not going to work for them and they just suspended the MC number."
- PRO-027 (strong, r/FreightBrokers, 2026-10-01): a hijacked MC with fake leases and certificates. "they were putting different, legitimate trucking company decals on the side of their truck, making up fake leases agreements and fake certificates of insurance just in case they got pulled over, the hit would go directly to the company on the side of the truck."
- FORCE-42 (medium, Federal Register, 2026-04-29): "FMCSA is announcing a new, online registration system, and explaining how use of this new system will satisfy current statutory and regulatory requirements pertaining to the Unified Registration System (URS)."
- FORCE-45 (medium, r/Truckers, 2026-10-19): "Last month, during a roadside inspection, the inspector flagged him for his lack of English proficiency and required him to take the written CDL law test in English at the DMV." Driver-level, outside authority monitoring.
- FORCE-41 (medium, Federal Register, 2026-02-13): the non-domiciled CDL final rule shows rule churn that affects driver availability; tangential.
- New evidence (not in SIGNALS.md): r/OwnerOperators, 2026-10-15, https://www.reddit.com/r/OwnerOperators/comments/1x68fqh/ (6 comments): "I've had the same problem as many of you a couple of months ago, when renewing insurance they made me inactive for almost a month."
- New evidence (not in SIGNALS.md): r/OwnerOperators, 2026-10-11, https://www.reddit.com/r/OwnerOperators/comments/1x3e58g/: "So recently I missed out on two loads because for some reason my MC number doesn't appear when you search it."
- New evidence (not in SIGNALS.md): r/Truckers, 2026-10-29, https://www.reddit.com/r/Truckers/comments/1xicoql/ (the poster offers a free checklist, so it may be lead generation): "Between IFTA every quarter, UCR every year, the MCS-150 update, and the drug consortium paperwork, it feels like there's always some filing about to sneak up on you."
- Press titles (not first-person): Overdrive, 2026-08-28, ["What's wrong with this picture? Motus mess costing small fleets thousands"](https://www.overdriveonline.com/overdrive-extra/article/15833600/fmcsas-motus-mess-costing-small-fleets-thousands) (title); CCJ, ["FMCSA defends buggy Motus rollout as necessary growing pain in fraud crackdown"](https://www.ccjdigital.com/regulations/safety-compliance/article/15834781/motus-system-glitches-delays-fmcsa-addresses-carrier-frustrations) (title).
- Counter-signals: r/OwnerOperators, 2026-10-14, ["MOTUS SEEMS TO BE FIXED!"](https://www.reddit.com/r/OwnerOperators/comments/1x5yq0a/) (title, a fleet manager), and Overdrive's 2026-10-13 headline "FMCSA's Motus mess improving, little by little?". The spike may fade. A 2026-10-02 [post](https://www.reddit.com/r/OwnerOperators/comments/1ww1nvm/) warns of a Motus impersonation phishing campaign, so any alert service must be easy to verify.

## 5. The product
- Outcome: the carrier enters a DOT or MC number (no FMCSA login) and gets a daily check of the public record; it warns before a problem becomes a suspension and says what to do.
- Core AI loop: input (public FMCSA authority, insurance, BOC-3, MCS-150 and inspection data; the carrier's policy declarations page; deadline dates) -> model work (deterministic checks first: authority status, filed liability amount and effective dates versus the policy, pending cancellation notices, update due dates, new inspections or violations the owner does not recognize; the model reads the declarations PDF, explains each finding in plain language, drafts the email to the agent or insurer, and answers "what do I do now") -> output (SMS and email alerts, a fix checklist, a deadline calendar, a shareable "active as of today" page for brokers) -> feedback (owner marks fixed; outcomes refine the playbook).
- Boundaries: read-only, never asks for Login.gov or FMCSA credentials, never files for the carrier; it prepares what the owner or agent submits.
- Day in the life: 45 days before renewal the app says "Your policy renews 2026-12-01 at $1,000,000 but the filing on record shows $750,000. Brokers and Motus may treat this as a mismatch. Send this note to your agent asking for a corrected filing?" One tap sends the drafted email.
- Form factor: web app with SMS and email alerts.

## 6. Why the LLM is load-bearing
Honest answer: partly. Status checks and filing comparisons are rules. The model matters for reading declarations pages in many formats, turning agency language into steps, drafting the agent email and handling follow-up questions. Without it the product is a monitor with alerts, which several rivals already sell. This is why AI leverage is 2.

## 7. The insight
Small carriers lose revenue to paperwork faults they do not see coming, and their authority is their license to earn. The warning signals are public; what is missing is the comparison with the carrier's own policy and a concrete next step in plain language, delivered where the owner already looks (SMS).

## 8. Why now, and why this does not exist yet
Monitoring exists. J.J. Keller sells a managed authority-monitoring service; Dotra, TruckDocsAI, HaulComply and Trucking Comply sell software for small fleets. Why now is the Motus rollout (phases from 2025-12-08, widespread problems through 2026) and the surge of insurance-filing and status mismatches, which makes "the filing says $750,000, your policy says $1,000,000" a concrete, checkable alert. Caveat: FMCSA is improving, and I could not confirm that rivals lack mismatch checks because their pricing pages were blocked.

## 9. Inspiration and derivation
- Parents: J.J. Keller's DOT authority monitoring, credit-monitoring alerts, certificate-of-insurance monitoring for brokers (CarrierOK).
- Changed: target user (the carrier, not the broker or insurer), core job (reconcile the policy with the filing and give fix steps, not just flag status), business model (self-serve $12, no sales call), distribution (free DOT-number check and SEO).

## 10. Competition check
- Queries run: (1) "FMCSA authority monitoring alerts small carrier insurance filing lapse MC revoked MCS-150 UCR BOC-3 reminder software"; (2) "site:producthunt.com FMCSA compliance DOT authority monitor trucking"; (3) "site:ycombinator.com/companies trucking compliance FMCSA DOT carriers AI" (no YC compliance startup returned); (4) "Motus FMCSA registration system carriers suspended insurance filing mismatch problems 2026". Also: a Reddit archive pull (r/OwnerOperators, r/Truckers, r/FreightBrokers, Jul-Oct 2026) and a news search. Capterra pages for TruckDocsAI and Dotra and the Overdrive article returned HTTP 403. Motive and Samsara marketplace results from the idea 001 search showed no authority monitor.
- [J.J. Keller DOT Authority Monitoring Service](https://www.JJKeller.com/shop/Product/DOT-Authority-Monitoring-Service): staff monitor your authority 365 days a year and notify you of new or updating filings (search snippet); price not seen. Established vendor, managed service.
- [Dotra](https://www.capterra.com/p/10047829/Dotra/): software that "keeps an eye on your FMCSA record in the background and surfaces what changed" (snippet); price and reviews not read.
- [TruckDocsAI](https://www.capterra.com/p/10039100/Truck-Docs-AI/): AI-powered DOT compliance platform for owner-operators and small fleets with expiration alerts and FMCSA carrier-profile monitoring, per its [launch article](https://www.businessfleet.com/news/truckdocsai-launches-ai-powered-compliance-platform-for-owner-operators-and-small-fleets); price not read. Closest direct rival.
- [HaulComply](https://www.producthunt.com/products/haulcomply/launches/haulcomply-2) (Product Hunt, launched 2026-03-31): "DOT compliance made simple for small trucking fleets"; 2 followers. [Trucking Comply](https://sourceforge.net/software/product/Trucking-Comply/): web-based FMCSA and DOT compliance for owner-operators and small fleets. [Fleetworthy](https://www.truckinginfo.com/10242629/fleetworthy-acquires-haul-to-expand-ai-enabled-fleet-compliance) acquired Haul for AI-enabled fleet compliance (title only).
- Adjacent: [CarrierOK](https://www.g2.com/products/carrierok/discuss) monitors carriers for insurers, factors and brokers (the other side); insurers and service shops publish Motus help ([Bobtail](https://www.bobtail.com/blog/stuck-in-motus-heres-whats-going-wrong-and-how-to-fix-it), [Sky Transport](https://skytransportsolutions.com/motus-problems.html)), which shows demand for hand-holding but also that insurers may add monitoring as retention.
- Classification: WEAK DIRECT. Broad compliance and authority monitoring is served by an established vendor and several small tools; I found none whose public pages describe policy-versus-filing reconciliation with fix steps, but I could not read their feature lists.
- Platform risk: medium. FMCSA could fix Motus and send better notices, shrinking demand. J.J. Keller, Fleetworthy, Motive, Samsara or an insurer could add mismatch alerts. Frontier assistants cannot watch the record daily or send SMS. This caps Scale at 2.

## 11. Business model
- Payer: the carrier. Price hypothesis: $12 a month per carrier ($9 solo, $19 for 3-10 trucks). Anchors: the $80 reinstatement fee and days of lost revenue in FORCE-44; rival prices unseen, so this is untested.
- Cost per active user per month [ESTIMATE]: daily data pulls are code, not model calls. Four alert explanations on Sonnet 5.5 at 3,000 in + 500 out = $0.011 each = $0.044; one monthly report at 6,000 in + 1,200 out = $0.012 + $0.012 = $0.024; ten chat answers on Haiku 5.5 at $0.00055 = $0.0055; 10 SMS x $0.01 [ASSUMPTION] = $0.10. Total about $0.20.
- Gross margin (12 - 0.20) / 12 = 98%.

## 12. Market size
Bottom-up [ESTIMATE]: [FleetOwner (2019)](https://www.fleetowner.com/research/article/21703420/2019-for-hire-500-top-carriers-in-north-america) reported more than 777,000 for-hire fleets, about 91% with six or fewer trucks (figure read from a search summary, article not opened); a [Datawrapper chart](https://datawrapper.dwcdn.net/7Adxc/1/) says small fleets kept declining through 2025 (data not read). Use 300,000 active small carriers. At 2% penetration, 6,000 x $14 average x 12 = $1.0M ARR.

## 13. Go-to-market
- First 100: a free "authority health check" by DOT or MC number (SEO and shareable), answers in r/OwnerOperators and TruckersReport, and a partnership pitch to truck-insurance agents and factors who want fewer lapses. SEO: "MC number suspended insurance", "BMC-91X filing amount", "Motus insurance mismatch", "authority revoked reinstatement".
- Loop: the "active as of today" page carriers send to brokers who say "your MC is ineligible"; each page links back. Pairs naturally with Haul Paid (idea 001), which targets the same carrier; this could be its free top of funnel.

## 14. Moat and scale path
Weak: the data is public and prices are small. Trust, alert accuracy and per-carrier history are the only assets. Scale path: white-label for insurance agents and factors, broker-side vetting, then bundle with claims recovery. Capped at 2.

## 15. Solo feasibility
- MVP in about 4 weeks: DOT/MC lookup from FMCSA public data (QCMobile API with a free key, SAFER and licensing pages, bulk datasets on data.transportation.gov [UNVERIFIED availability and freshness after Motus]), policy-PDF extraction, rule checks, SMS and email alerts, fix-step library, a public status page.
- Running cost before revenue: about $40-70 a month.
- Hardest risk: data freshness and accuracy. Reddit posts show SAFER returning "no matching record" while Motus shows active, so alerts can be wrong in either direction. Second: trust, since owners are primed to distrust messages that mention FMCSA.

## 16. Pre-mortem
1. Motus is repaired, suspensions fade, and the renewal-year event rate is too low for a $12 habit.
2. Rivals (J.J. Keller, TruckDocsAI, Dotra, Fleetworthy) match the feature set and a free FMCSA notice improvement makes it moot.
3. A false alarm or a missed suspension destroys trust; phishing campaigns make owners ignore third-party alerts.

## 17. Cheapest validation test
Build the free health check in one weekend (about $50) and offer it in r/OwnerOperators and TruckersReport for two weeks. Pass: 100 carriers enter a DOT number, at least 10 have an actionable flag (pending cancellation, filing amount below policy, update due within 30 days), and 5 or more pay $12 for alerts. Fail: under 3% have a flag or no one pays. A second check is whether the FMCSA data refreshes daily.

## 18. Open questions
- Which public FMCSA feeds show pending insurance cancellations, and how fresh are they since Motus?
- What do J.J. Keller, TruckDocsAI and Dotra charge, and do they reconcile the policy with the filing?
- Is the Motus problem durable or a 2026 spike? Is it better folded into Haul Paid as a free entry product?
- Will carriers upload a declarations page, or only enter a DOT number?
