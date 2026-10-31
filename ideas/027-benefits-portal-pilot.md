---
id: "027"
slug: benefits-portal-pilot
name: Benefits Portal Pilot
one_liner: "Browser side panel that guides navigators through state benefits portals, pre-fills from client documents and builds work-requirement proof packets."
target_user: "Benefits navigators at health centers, hospitals, legal aid groups and Medicaid plans"
form_factor: "browser extension"
lens: "Interaction shift"
frontier: false
competition: "ADJACENT ONLY"
confidence: "MED"
status: "developed"
signals: [FORCE-11, FORCE-12, FORCE-13, FORCE-14, FORCE-15, LIFE-32, LIFE-33, REV-48, FORCE-16]
scores:
  pain: 4
  evidence: 3
  ai_leverage: 4
  whitespace: 3
  novelty: 3
  why_now: 4
  solo_feasibility: 2
  distribution: 3
  wtp_economics: 3
  scale_defensibility: 3
total: 64.2
price_hypothesis: "$99/month per navigator seat; free SMS document upload for clients"
model_cost_per_user_month: "$6.10 (about $6.70 on HIPAA-eligible endpoints)"
gross_margin: "85%"
mvp_weeks: 8
deep_dive: false
red_team: false
---

# Benefits Portal Pilot

## 1. One-liner
Browser side panel that guides navigators through state benefits portals, pre-fills from client documents and builds work-requirement proof packets.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 4 | Coverage loss for millions; CMS counts 8.8M people documenting every 6 months at about 2 hours each (FORCE-11) |
| Evidence quality | 2 | 3 | 9 recent signals, but all enrollee-side; no navigator or plan says it would pay |
| AI leverage | 2 | 4 | Screen reading, document extraction and hours reconstruction are model work; submission stays human |
| Whitespace | 2 | 3 | ADJACENT ONLY: Fortuna Health (funded) sells navigation to plans; no navigator side panel found |
| Novelty of insight | 1 | 3 | Equip the navigators instead of rebuilding the portals; HeyClicky pattern on a narrow job |
| Why now | 1 | 4 | Work requirements due by 2027-01-01, GA screen-aware agents; court rulings add uncertainty (FORCE-12) |
| Solo feasibility | 2 | 2 | HIPAA posture, 50 different portals, extensions blocked on hospital laptops |
| Distribution | 2 | 3 | Health-center and legal-aid networks, Chrome Web Store, webinars; slow trust-heavy sales |
| Willingness to pay and unit economics | 2 | 3 | Plans and hospitals lose money when people churn; nonprofit budgets are thin; margin about 85% |
| Scale and defensibility | 2 | 3 | State-by-state playbooks and case data compound; policy and portals can change |
| **Total** | | **64.2** | |

Confidence: MED (important unknown: who pays and whether rules hold). FRONTIER: no.

## 3. The problem
- Who: navigators, enrollment specialists and caseworkers who help low-income clients apply, renew and now prove 80 hours a month of work, study or service; the clients themselves; the plans and hospitals who lose members when coverage lapses.
- Frequency and cost: states must implement by 2027-01-01. CMS estimates 8.8 million beneficiaries must document and submit every 6 months at about 2 hours each, plus 3.75 million new applicants (FORCE-11), which is about 35 million hours a year [ESTIMATE: 8.8M x 2 cycles x 2 hours]. Portals loop, reject and cap uploads (LIFE-32, REV-48).
- Workaround: phone trees, paper packets, walking clients through the portal on a shared screen, mailing or hand-delivering what the portal will not take.

## 4. Evidence
Nine signals from 2026-06 to 2026-10, all enrollee-side. The buyer side is the gap.
- **FORCE-11** (fact, 2026-06-03, Federal Register): "States are required to implement the new requirement no later than January 1, 2027." Plus the CMS burden estimate above.
- **FORCE-12** (status, 2026-10-29, r/Medicaid, 1,410 pts): "Chronically ill people on Medicaid won't be bound by new work requirement rules that the latest Trump administration guidance requires in order to qualify for "medically frail" exemptions, a federal judge ruled Thursday." Rules are moving.
- **FORCE-13** (medium, 2026-10-28): "It also says you can self attest or apply for exemption but doesn’t say how to do those either I’m so frustrated, confused and scared."
- **FORCE-14** (medium, 2026-10-27): "I make the work requirements but do I really have to supply pay Stubs and the whole process twice a year now ?"
- **FORCE-15** (medium, 2026-10-30, a social worker helping her mother): "Since DD is gig work, I am not sure how you can prove you work a certain # of hours a month."
- **LIFE-32** (medium, 2026-10-25): "They have messed up our paperwork almost every time we have to reapply for the last 4 years" (partial quote). Months of attempts to fix a rejection.
- **LIFE-33** (medium, 2026-10-28): "Ended up filling out the form on the "your Texas benefits" web site. Took forever to fill form and upload proof of hopefully everything they needed."
- **REV-48** (medium, 2026-07-27, App Store): "Like being able to send more documents than what you allow because HHSC asks for so many documents! Then the client has to go and mail, fax, or take the documents in."
- **FORCE-16** (weak, 2026-10-29): "Google says yes but my local dss office says no and I am still unsure."

## 5. The product
- Finished outcome: a navigator completes a state application or renewal faster, and each client has a monthly proof packet that is ready before the six-month check.
- Core AI loop: client texts photos of ID, pay stubs, gig statements and letters -> model extracts and normalizes household, income and hours -> navigator opens the state portal; the side panel reads the current page (only when opened or a hotkey is pressed) -> shows what this page asks and the matching client data with its source document -> navigator approves each fill and submits -> model builds the work-requirement packet (hours from wages, gig statements, service letters; lists exemptions the state names for the navigator to consider) -> reminders and re-collection by SMS -> packet fits portal upload caps and lists what must be mailed.
- Interaction: browser side panel on the navigator's own logged-in session; client side is an SMS link, no app.
- Day in the life: Rosa, an enrollment specialist, opens page 4 of 22 of the state application. The panel shows two pay stubs that total $1,420 a pay period and a mismatch with the household size on the intake. She approves the fills. For Mr. Lee's delivery income it says earnings alone do not show hours and texts him for the app's hours screen.
- Liability line: application assistance and document organization, not legal advice. The tool never decides eligibility, exemption (including "medically frail", no medical judgment), or hours credit. It shows the state's published rule, flags missing evidence, and the navigator and client decide. It never submits, never logs in for anyone and works inside the navigator's session. Covered-entity customers sign a business associate agreement.

## 6. Why the LLM is load-bearing
Portals differ by state and change often, so scripts break; documents are photos of pay stubs, leases and letters; gig income must be turned into hours. A screen-aware model reads each page and the client's files and says what goes where. Without it the product is a static checklist per state.

## 7. The insight
Navigators are the leverage point: each handles dozens of clients, and plans and hospitals pay when people churn off coverage. The HeyClicky pattern (consent by gesture, point at the field, explain by voice or text) on a narrow job beats rebuilding every state portal. Honest gap: I have no signal from a navigator or plan about budget.

## 8. Why now, and why this does not exist yet
The federal rule sets a hard date (FORCE-11), screen-understanding agents became usable in 2026, and states mostly keep incumbent vendors and tools "verify only income" (KFF Health News, 2025-10-23, [WebFetch summary](https://kffhealthnews.org/health-care-costs/medicaid-eligibility-tool-pilot-test-work-requirements-ai-louisiana-arizona-georgia/)). Navigator-side tooling is new ground because state portals are brittle for old-style scripts and civic-tech sells to states, not to the navigator.

## 9. Inspiration and derivation
Parents: Code for America's GetCalFresh (assisted applications), HeyClicky (cursor-side help), Fortuna Health (Medicaid navigation for plans). Changed: user (the navigator's own seat, not a state or plan program), interaction (side panel inside the real portal), business model (per seat, not per state contract), channel (health-center and legal-aid networks).

## 10. Competition check
Queries run (2026-10-31): (1) web "Medicaid work requirements compliance tool enrollees navigators document 80 hours verification app startup nonprofit 2026"; (2) Product Hunt via search, "Medicaid SNAP benefits application help navigator" restricted to producthunt.com (nothing relevant); (3) web "benefits navigation tools Propel Code for America GetCalFresh mRelief Benefits Data Trust Nava AI application assistance navigators"; (4) web "state Medicaid eligibility system vendors Deloitte Gainwell Conduent Maximus work requirement verification contracts 2026"; (5) YC directory mirror https://yc-oss.github.io/api/companies/all.json with `medicaid|SNAP|benefits navigation|public benefits|safety net|caseworker` from 2021 (Fortuna Health, Verano Health, Forage) plus a broad pass; (6) App Store `--find "Medicaid benefits application"` and `--find "SNAP benefits help"`; (7) fetches of Fortuna Health and a KFF Health News article.

| Product | What it does | Price | Difference |
|---|---|---|---|
| [Fortuna Health](https://fortunahealth.com/) ([YC Summer 2023](https://www.ycombinator.com/companies/fortuna-health), 29 people) | "TurboTax for Medicaid": screening, guided enrollment and renewal, status alerts, 24/7 multilingual navigation, "Trusted by 185,000+ patients"; "only available through providers and insurers"; free "HR1 Readiness Roadmap" for plans | Not listed | Nearest and funded. Uses its own licensed navigators on its own platform; no side panel for others' navigators; work-requirement features not described |
| [Code for America](https://codeforamerica.org/programs/social-safety-net) and [GetCalFresh](https://www.getcalfresh.org/en/about/) | Assisted SNAP applications (reported 6M+ people, application time 45 to 8 minutes), text-message reminders in Louisiana; [moving to BenefitsCal](https://cdss.ca.gov/inforesources/cdss-programs/calfresh-outreach/getcalfresh-transition) | Free (state-funded) | Nonprofit, state-contracted, SNAP-first |
| State platform vendors | Gainwell, Healthy Together, Salesforce and open-source OSCER and Emmy ([CBPP](https://www.cbpp.org/research/health/assessing-the-medicaid-work-requirement-vendor-landscape), [summary](https://digitalgovernmenthub.org/library/assessing-the-medicaid-work-requirement-vendor-landscape/)); vendors offering $600M+ of free or discounted services to states ([Healthcare Dive](https://www.healthcaredive.com/news/medicaid-vendors-trump-deals-cms-work-requirements/810839/)) | Contracts with states | Build the state side; most states stay with incumbents |
| State apps ([Your Texas Benefits](https://apps.apple.com/us/app/your-texas-benefits/id931986739), 385k ratings) | Official application, renewal and upload | Free | The portal whose limits (REV-48) create the pain |
| Browser agents (Claude, Gemini, Copilot) | Walk a portal for one person | $0 to subscription | No case memory, client intake or HIPAA agreement |
| [Verano Health](https://www.ycombinator.com/companies/verano-health), [Forage](https://www.ycombinator.com/companies/forage-2) | Telehealth coaching for Medicaid members; EBT payments | Not found | Different jobs |

Propel, mRelief and Benefits Data Trust are benefit-access organizations I did not verify in this session [UNVERIFIED]. Classification: ADJACENT ONLY; if Fortuna sells navigator tooling, reclassify WEAK DIRECT. Platform risk: generic browser agents can do the single-person walkthrough within 12 months, and state vendors may ship enrollee document upload; they are unlikely to build navigator case management with a HIPAA posture. Whitespace held at 3.

## 11. Business model
- Payer: the employer of the navigator (health center, hospital, legal aid, plan). Anchor [ASSUMPTION]: a navigator costs about $30 an hour loaded; saving 20 hours a month is worth about $600 against a $99 seat. Hypothesis: $99 per seat per month, clients free.
- Model cost per seat per month [ESTIMATE], 10 new applications and 30 recurring clients, prices from `research/LANDSCAPE.md`. Application: 25 pages x 3 steps = 75 steps; 60 on Haiku 5.5 at 4,000 in + 400 out = $0.0004 + $0.0002 = $0.0006 each ($0.036); 15 harder steps on Sonnet 5.5 at $0.008 + $0.004 = $0.012 each ($0.18); documents $0.00125; about $0.217 each, so $2.17. Recurring clients: 3 documents a month on Haiku $0.00075 plus a packet every 6 months on Sonnet (20,000 in + 3,000 out = $0.07) = $0.013 each, so $0.39. Navigator Q&A 100 x $0.007 = $0.70. SMS 280 messages x $0.01 = $2.80 [ASSUMPTION]. Total $6.06; with a 20% premium on model cost for HIPAA-eligible endpoints [ASSUMPTION] about $6.70.
- Margin: payment fee $3.17; support allowance $5.00 [ASSUMPTION]; ($99 - 6.70 - 3.17 - 5.00) / $99 = 85%.

## 12. Market size
[ESTIMATE] Seats: about 1,400 health center organizations [UNVERIFIED] x 6 enrollment staff = 8,400; about 6,000 hospitals [UNVERIFIED] x 3 = 18,000; 2,000 legal aid and community groups x 3 = 6,000; total 32,400 seats x $1,188 = $38M a year. At 5% = 1,620 seats = about $1.9M ARR. Plans paying per retained member would be larger but enterprise-sold.

## 13. Go-to-market
- First 100 seats: webinars on documenting the 80 hours timed to the 2027-01-01 start, state primary-care and legal-aid associations [UNVERIFIED which], Chrome Web Store listing, and answers on r/Medicaid where helpers like the FORCE-15 social worker post; 1 to 2 pilot orgs of 5 seats each, then referrals between sites.
- Growth loop: the client SMS page carries the organization's name and the packet format that other sites copy; one state playbook serves every org in that state.

## 14. Moat and scale path
State-specific portal playbooks (page maps, rules), exemption and evidence libraries, de-identified case data, and HIPAA trust. Scale: SNAP, housing, unemployment, immigration portals, then plan-paid versions. Playbooks decay with portal changes, so the moat needs constant upkeep.

## 15. Solo feasibility
- MVP, 8 weeks: extension and side panel (week 1), one state flow of about 20 pages with extraction (2-3), SMS collection and client page (4), proof-packet builder (5), HIPAA posture with provider agreement, audit log and encryption (6), pilot fixes (7-8).
- Running cost before revenue about $120 a month (hosting $30, database $25, SMS $20, HIPAA-eligible hosting premium $30, model testing $15).
- Hardest risk: portal brittleness and locked-down hospital laptops that block extensions; then HIPAA diligence.

## 16. Pre-mortem
1. Policy volatility: rulings like FORCE-12 or delays could shrink the 2027 rush, leaving only a generic enrollment aid.
2. Unproven buyer: navigator orgs have thin budgets and plans and hospitals run months of security review.
3. Portal and platform risk: states change flows or restrict automation, and generic browser agents commoditize the walkthrough.

## 17. Cheapest validation test
4 weeks, under $150 plus about 40 hours. Concierge for one state: 10 navigators run 3 real, consented cases each with a prototype panel (or screenshare) and the packet builder. Pass: at least 5 of 10 report 30%+ time saved per case and at least 2 organizations sign a $99-per-seat pilot letter. Kill if IT blocks the extension at 7 of 10 sites and no web-app fallback works.

## 18. Open questions
- Which model providers sign a business associate agreement, and what does that cost?
- Do state portal terms allow a navigator-side assistant? [UNVERIFIED]
- Which state first: one with a stable flow and an early deadline?
- Does Fortuna plan a tool for other organizations' navigators?
- What happens to the 2027 start if courts or CMS change the rule (FORCE-12)?
