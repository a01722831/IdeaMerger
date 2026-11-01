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
  why_now: 5
  solo_feasibility: 2
  distribution: 3
  wtp_economics: 3
  scale_defensibility: 3
total: 65.3
price_hypothesis: "$99/month per navigator seat; free SMS document upload for clients"
model_cost_per_user_month: "$6.10 (about $6.70 on HIPAA-eligible endpoints)"
gross_margin: "85%"
mvp_weeks: 8
deep_dive: true
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
| Why now | 1 | 5 | Work requirements due by 2027-01-01, GA screen-aware agents; court rulings add uncertainty (FORCE-12) Calibrated 4 to 5: Medicaid work requirements start 2027-01-01 and screen-reading agents only became usable in 2026 |
| Solo feasibility | 2 | 2 | HIPAA posture, 50 different portals, extensions blocked on hospital laptops |
| Distribution | 2 | 3 | Health-center and legal-aid networks, Chrome Web Store, webinars; slow trust-heavy sales |
| Willingness to pay and unit economics | 2 | 3 | Plans and hospitals lose money when people churn; nonprofit budgets are thin; margin about 85% |
| Scale and defensibility | 2 | 3 | State-by-state playbooks and case data compound; policy and portals can change |
| **Total** | | **65.3** | |

Confidence: MED (important unknown: who pays and whether rules hold). FRONTIER: no.

Calibration (main researcher, 2026-10-31): why now 4 to 5 (Medicaid work requirements start 2027-01-01 and screen-reading agents only became usable in 2026).

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

## Deep dive

The crux is who pays. The customer plan and the validation test below are built around that question.

### Competitor table
| Competitor | Link | What it does | Price (as published, with date read) | Funding or traction (sourced) | Gap this idea exploits |
|---|---|---|---|---|---|
| Fortuna Health | [site](https://fortunahealth.com/), [YC](https://www.ycombinator.com/companies/fortuna-health), [MobiHealth](https://www.mobihealthnews.com/news/fortuna-health-raises-18m-enhance-ai-medicaid-enrollment) | "TurboTax for Medicaid": screening, guided enrollment and renewal, 24/7 multilingual navigation; "only available through providers and insurers" (section 10) | Not listed (read 2026-10-31) | $18M Series A led by Andreessen Horowitz with YC participation (per MobiHealth, as recorded in section 10; date not recorded); YC Summer 2023, 29 people; "Trusted by 185,000+ patients" (its site) | Its own navigators on its own platform; no side panel for other organizations' navigators; work-requirement features not described |
| Code for America, GetCalFresh | [GetCalFresh](https://www.getcalfresh.org/en/about/), [CfA](https://codeforamerica.org/programs/social-safety-net) | Assisted SNAP applications; reported 6M+ people, 45 to 8 minutes; moving to BenefitsCal | Free (state-funded) | Nonprofit | SNAP-first and state-contracted; not a seat product |
| State platform vendors (Gainwell, Healthy Together, Salesforce, OSCER, Emmy) | [CBPP](https://www.cbpp.org/research/health/assessing-the-medicaid-work-requirement-vendor-landscape), [Healthcare Dive](https://www.healthcaredive.com/news/medicaid-vendors-trump-deals-cms-work-requirements/810839/) | Build the state side of work-requirement verification | State contracts; vendors offered $600M+ of free or discounted services (Healthcare Dive, per section 10) | Most states keep incumbents (KFF Health News, 2025-10-23) | Nothing for the navigator's desk |
| Plan-side vendors and advisers: mPulse, Drips, Avalere, HMA | [mPulse](https://mpulse.com/blog/why-medicaid-communication-strategy-matters-for-compliance/), [Drips](https://drips.com/resources/the-real-risk-of-medicaid-work-requirements-isnt-eligibility-its-response), [Avalere](https://avalerehealth.com/thought-leadership/how-can-managed-care-organizations-prepare-for-medicaid-community-engagement-work-requirements/), [HMA](https://www.healthmanagement.com/blog/in-focus/act-now-implement-community-engagement-requirements/) | Work-requirement outreach and readiness content for plans (titles only) | Not published | Not verified [UNVERIFIED]; shows plans shop for help, not how much they spend | Member messaging and advice, not in-portal help or proof packets |
| Hospital eligibility outsourcing: Optum, Change Healthcare | [Optum](https://business.optum.com/en/insights/outsourcing-medicaid-eligibility-enrollment.html), [Change Healthcare](https://www.changehealthcare.com/insights/outsourcing-medicaid-eligibility-enrollment) | Hospitals outsource Medicaid eligibility and enrollment; Change Healthcare material describes Rush University Medical Center moving the work to a vendor (search summary) | Not published | Not published | A human service sold on outcomes; it is the budget line hospitals already have |
| State apps and pilots: Your Texas Benefits, Louisiana and Arizona pilots | [App Store](https://apps.apple.com/us/app/your-texas-benefits/id931986739), [KFF Health News](https://kffhealthnews.org/health-care-costs/medicaid-eligibility-tool-pilot-test-work-requirements-ai-louisiana-arizona-georgia/) | Official application, renewal and upload; pilots of verification tools | Free | 385k app ratings (section 10); a Governing summary reports weak participation and limited functionality in the pilots (search summary) | Upload limits create the pain (REV-48); weak enrollee uptake supports help through navigators |
| Claude, Gemini, Copilot browser agents | [Anthropic BAA article](https://support.claude.com/en/articles/15455031) | Walk a portal for one person | Subscriptions; not re-checked | n/a | No case memory or client intake; Anthropic's help article says Cowork is not an Eligible Service under its BAA in any configuration (search summary) [UNVERIFIED beyond the summary] |
| Others seen: Propel, Verano Health, Forage; mRelief, Benefits Data Trust, Nava | [Propel](https://www.propel.app/blog/medicaid-work-requirements-explained/) | Consumer EBT app with a work-requirements explainer; telehealth coaching; EBT payments | Not seen | Not verified [UNVERIFIED] | No navigator tooling seen |

Classification stays ADJACENT ONLY; if Fortuna sells navigator tooling, reclassify WEAK DIRECT.

### Market sizing (bottom-up)
Customers means paid navigator seats; buyers are the organizations that employ navigators.

| Payer type | Organizations (source) | Seats per organization (conservative / optimistic) | Seats (conservative / optimistic) |
|---|---|---|---|
| Health centers | 1,359 reporting awardees in 2024, 32,387,774 patients ([HRSA UDS](https://data.hrsa.gov/topics/healthcenters/uds/overview/national)) | 2 / 6 [ESTIMATE] | 2,718 / 8,154 |
| Hospitals with in-house navigators | 600 / 1,200 of about 6,000 [UNVERIFIED count; most outsource] | 3 / 3 [ASSUMPTION] | 1,800 / 3,600 |
| Legal aid and community groups | 1,000 / 2,000 [ASSUMPTION, section 12] | 2 / 3 | 2,000 / 6,000 |
| Managed care plans | Not seat-based; they sponsor seats elsewhere | not applicable | not applicable |
| Total | | | 6,518 / 17,754 |

- No national count of eligibility staff exists in what I found; a Hawaii Primary Care Association page reports 253 enabling-services FTE across 14 health centers, about 18 per center, of which eligibility assisters are a subset ([workforce data](https://www.hawaiipca.net/workforce-data), search summary).
- Adoption [ASSUMPTION] 5% / 10%. Conservative: 6,518 x 5% = 326 seats x $1,188 a year ($99 x 12) = $0.39M ARR. Optimistic: 17,754 x 10% = 1,775 seats x $1,188 = $2.11M ARR. If every seat bought: $7.7M / $21.1M (section 12's $38M used 32,400 seats; most hospitals outsource).
- Revenue at 100, 1,000 and 10,000 seats: $118,800, $1,188,000 and $11,880,000 a year. 10,000 seats is 56% of the optimistic pool, so only a plan-funded or multi-program model gets there.

### Unit economics
Per seat per month: 10 new applications and 30 recurring clients. Prices from `research/LANDSCAPE.md` section 6.

| Line | Volume | Tokens per call | Model and price per 1M | Arithmetic [ESTIMATE] | Cost |
|---|---|---|---|---|---|
| Application steps, routine | 10 x 60 = 600 | 4,000 in, 400 out | Haiku 5.5, $0.10 / $0.50 | 600 x ($0.0004 + $0.0002) | $0.36 |
| Application steps, hard | 10 x 15 = 150 | 4,000 in, 400 out | Sonnet 5.5, $2 / $10 | 150 x ($0.008 + $0.004) | $1.80 |
| Document extraction (applications, then recurring clients) | 50 + 90 | 2,500 in, 400 out | Haiku 5.5 | 140 x ($0.00025 + $0.0002) | $0.06 |
| Six-month packets (30 clients / 6 = 5 a month) | 5 | 20,000 in, 3,000 out | Sonnet 5.5 | 5 x ($0.040 + $0.030) | $0.35 |
| Navigator Q&A | 100 | 2,000 in, 300 out | Sonnet 5.5 | 100 x ($0.004 + $0.003) | $0.70 |
| Model subtotal, plus 20% HIPAA-eligible endpoint premium [ASSUMPTION] | | | | $3.27 + $0.65 | $3.92 |

- Messaging [ESTIMATE] from [Twilio pricing](https://www.twilio.com/en-us/sms/pricing/us), read 2026-10-31: 160 outbound SMS x ($0.0083 + about $0.004 carrier fee) = $1.97; 60 inbound SMS x $0.0113 = $0.68; 60 inbound photo texts (MMS) x ($0.0165 + $0.003) = $1.17; a $1.15 number shared by 6 seats = $0.19; total $4.01. Section 11 used $2.80.
- Payments 2.9% x $99 + $0.30 = $3.17; support $5.00 and infrastructure $120 a month / 100 seats = $1.20 [ASSUMPTION]. Total at 100 seats 3.92 + 4.01 + 3.17 + 5.00 + 1.20 = $17.30, margin ($99 - $17.30) / $99 = 82.5%; at 30 seats (infrastructure $4.00) $20.10 and 79.7%. Section 11's 85% omitted infrastructure.
- Heavy user (40 new applications, 150 recurring clients): applications 40 x $0.21825 = $8.73; recurring 150 x $0.01302 = $1.95; Q&A 400 x $0.007 = $2.80; model $13.48 plus $2.70 premium; messaging $3.82 x 4.75 + $0.19 = $18.34; payments $3.17; support $10; infrastructure $1.20: $48.89, margin 51%.
- Cap: the $99 seat includes 60 active clients and 500 client messages a month; a $199 high-volume seat includes 200 clients and 1,500 messages. The heavy user on the $199 seat costs $48.89 + $2.90 extra payment fee = $51.79, margin 74%.

### First 100 customers
Customers means paid seats; 100 seats is about 14 organizations at 7 seats. Sell to the site, not the navigator, and start with the payer question.

| Payer | Who signs, from which budget | Existing spend on this kind of help (sourced) | Reason to pay | Barriers | First offer to test |
|---|---|---|---|---|---|
| Health centers | Director of enabling services or patient access, or the COO; operating budget for eligibility staff | They already employ this staff: 2,569,147 enabling-services patients in 2024 ([HRSA](https://data.hrsa.gov/topics/healthcenters/uds/overview/national)); no tool spend found | Medicaid is about 42% to 43% of health center revenue; an analysis with NACHC projects nearly 5.6M health center patients losing coverage over 5 years and up to $32B in lost revenue ([GWU Geiger Gibson](https://geigergibson.publichealth.gwu.edu/node/2206), [KFF Health News](https://kffhealthnews.org/health-care-costs/federal-funded-community-health-centers-revenue-loss-under-trump/); search summaries) | HIPAA covered entity (BAA, security review); IT may block extensions; thin margins | $79 per seat per month founding price (list $99), or $449 per site per month for up to 6 seats [ASSUMPTION]; BAA included |
| Hospitals (patient financial services) | Director of patient financial services or revenue cycle | They outsource eligibility and enrollment to Optum, Change Healthcare and similar; prices not published | Uncompensated care when patients lapse | Security review of 3 to 9 months [ESTIMATE]; incumbents sell outcomes, not seats | $20 per completed proof packet [ASSUMPTION], no seat commitment |
| Legal aid and community groups | Executive director; grants and state or foundation funds | No tool spend found; thin budgets | Mission, funder reporting, caseload spike | Small budgets; usually not HIPAA covered entities [UNVERIFIED], so faster to sign | $49 per seat per month, or a funder-paid cohort of 10 seats at $4,800 a year [ASSUMPTION] |
| Managed care plans | Community engagement or member outreach lead; administrative budget | Plans may do outreach and "assist members in completing and submitting information", and may "manage deployment of community health workers, peer navigators, and community-based organizations", but "cannot make determinations of work reporting compliance or exemptions under H.R.1" ([Manatt via SHVS, 2025-10-24](https://shvs.org/resources/leveraging-managed-care-plans-to-support-implementation-of-medicaid-work-reporting-requirements/)); spend on vendors not verified | Churn from documentation delays hits membership and finances | Procurement of 6 to 12 months [ESTIMATE]; not solo-friendly | Plan-sponsored seats at the health centers and legal-aid groups in its network, $79 a seat, invoiced to the plan |

Reading of the crux: health center revenue and plan churn are incentives, not budgets. The only observed spend is hospitals outsourcing eligibility and plans buying outreach technology. So start with health centers and legal aid for speed, test the plan-sponsored seat in parallel, and treat hospitals as a per-packet pilot.

Funnel [ESTIMATE]: an individually written email to a named role gets a reply 8% of the time; a call becomes a free 30-day pilot (3 seats) 40%; a pilot converts 50% (IT approval is the main loss) at 5 seats per organization. Per 100 emails: 8 replies, 3.2 pilots, 1.6 paying organizations, 8 seats. A Primary Care Association or legal-aid webinar: 40 attendees, 10% ask for a demo (4), 50% pilot (2), 50% convert (1 organization, 5 seats).

| Week | What you do | Paid seats (cumulative) |
|---|---|---|
| 1 | Build the target list of 100 organizations (40 health centers via HRSA's find-a-health-center tool, 30 legal-aid and community groups, 20 hospital patient-financial-services teams, 10 plans); write a one-page "documentation sprint" brief; send 30 emails (30 x 8% = 2.4 replies) | 0 |
| 2 | 30 more emails; propose a 30-minute webinar to 5 state Primary Care Associations and 3 state legal-aid associations; about 5 payer-discovery calls (who signs, which budget line, price range, BAA and IT rules) | 0 |
| 3 | 2 pilots start (5 calls x 40%), 3 free seats each; 30 emails to hospital teams; first webinar if booked | 0 (6 pilot seats) |
| 4 | Pilot check-ins and time-saved data on 5 cases each; second webinar; 10 emails to plan community-engagement leads citing the plan role above | 0 |
| 5 | Pilot 1 converts if it saves 30% or more of time per case and IT approves: 3 seats at $79 plus 2 added; 30 emails; 2 webinar pilots start | 5 |
| 6 | Chrome Web Store listing; three state playbook pages ("how to prove 80 hours of gig work for Medicaid") | 5 |
| 7 | Pilots 2 (4 seats) and 3 (3 seats) convert | 12 |
| 8 | Review which payer type converted; 120 emails x 8% = 9.6 replies, 1.9 paying organizations, about 10 to 12 seats with webinars | 12 |

- Result: about 12 paid seats and 12 pilot seats open at week 8. Reaching 100 paid seats takes about week 26 to 34 [ESTIMATE] at one new paying organization every 1 to 1.5 weeks; section 13 reads faster. If launch lands after 2027-01-01 the hook becomes the first six-month recertification wave [ASSUMPTION].
- Channels: your state's Primary Care Association (the NACHC network); Legal Services Corporation grantees and the National Legal Aid and Defender Association; HFMA, AAHAM and NAHAM chapters for hospital financial counselors; Association for Community Affiliated Plans and Medicaid Health Plans of America for plans [UNVERIFIED willingness]; Chrome Web Store; r/Medicaid answers where helpers post (FORCE-15).
- Message and offer: "Your Medicaid patients must prove 80 hours a month, twice a year. Turn photos from their phones into a ready proof packet and a pre-filled portal session in minutes; you approve every fill; nothing is submitted for you." Free 30-day pilot for 3 seats; $79 founding price for 12 months in return for a short case study; BAA included; export all data on exit.
- Growth loop after 100: the client SMS page carries the organization's name and packet format, which neighboring sites copy; one state playbook serves every organization in that state; one Primary Care Association endorsement reaches dozens of centers; plan- or funder-sponsored seats pay for organizations that cannot.

### One-week validation test (under $50)
Goal: learn which payer type will name a budget line, an approver and a price, before more building. Nothing is sold as live.
- Build (days 1 to 2): four one-page URLs on a free host (/health-center, /hospital, /legal-aid, /plan), each with the same 90-second video labelled "mock-up, not a live product" and a different offer card (health center $99 per seat or $449 per site; hospital $20 per packet; legal aid $49 per seat; plan sponsored seats at $79). Each ends with "Reserve a free 30-day pilot slot (non-binding, no payment)" and four questions: role, organization, number of enrollment staff, "who would approve a purchase like this, from which budget?".
- Contact (days 2 to 5): 40 individually written emails, 10 per payer type, to roles the organizations publish on their own contact or staff pages; one follow-up at most; say who you are, that it is a prototype, and ask for a 20-minute call; honor opt-outs. No scraped personal emails, no purchased lists, no accounts on anyone's platform.
- Calls (days 3 to 7): fixed script: who signs; which budget line; what they pay today for this help; the highest monthly price they could approve without an RFP; IT and BAA rules; whether extensions are allowed; whether they would sign a non-binding pilot letter.
- Budget [ESTIMATE]: domain $12; pages, form, scheduling, mock-up and screen recording on free tiers $0; Claude usage to draft pages and tailor 40 emails $6; contingency $15; total $33.
- Pass (set in advance): at least 6 replies of 40 (15%); at least 4 calls held; at least 2 calls where the person names a budget line and an approver for a purchase of $500 a month or less without a formal RFP; at least 1 signed non-binding pilot letter at $60 or more per seat per month (or $300 or more per site); and one payer type with 2 or more of its 10 contacts positive (they book a call).
- Fail: fewer than 3 replies, or no call produces a named budget line, or every call says the purchase needs a security review longer than 3 months. Branch: health centers or legal aid pass, run the concierge pilot in section 17; only plans pass, wait (enterprise cycle); only hospitals pass, price per packet; none, drop. If 3 of the first 5 respondents say IT blocks extensions, build the web-app and screen-share mode first.

### Build brief (paste into a coding session)
**Product summary.** Benefits Portal Pilot is a Chrome side panel, a web dashboard and an SMS upload link for benefits navigators. Clients text photos of documents; the model extracts household, income and hours; the panel reads the navigator's open portal page only when asked and proposes fills with the source document; the navigator approves each one. It builds a monthly work-requirement proof packet sized for portal upload limits.

**Liability line (keep visible in the UI and every prompt).** Application assistance and document organization, not legal advice. The tool never decides eligibility, exemption (including "medically frail"; no medical judgment) or hours credit; it shows the state's published rule and flags missing evidence, and the navigator and client decide. It never submits, never logs in for anyone, never stores portal credentials and works inside the navigator's own session. Covered-entity customers sign a business associate agreement.

**MVP features (each testable)**
1. SMS upload link per client, branded with the organization's name (photos, PDFs; virus scan; hash dedupe; encrypted storage). Test: 20 uploads from a phone, each under 2 minutes, no app.
2. Extraction into a client profile (household, income per pay period, employer, hours, dates), each field linked to its source image. Test: at least 95% of 8 key fields correct on 50 synthetic documents.
3. Chrome side panel (Manifest V3) that reads the open portal page only after a click or hotkey (activeTab). Test: 0 captures without a gesture over 100 scripted page loads.
4. Fill proposals (field, value, source, confidence), one-click approval, fills only on click. Test: on 20 saved pages of one state's flow, at least 90% of fields map correctly and the panel abstains on unknown pages.
5. Hours and income reconstruction from wage, gig and self-employment documents under the state's published rule, shown as an evidence summary with source rows, never a determination. Test: 15 synthetic cases match hand calculation at least 90%.
6. Monthly proof packet PDF compressed to the portal's upload cap, listing what must be mailed. Test: 10 sample packets fit.
7. SMS reminders and re-collection with STOP handling. Test: STOP halts messages within 1 minute.
8. Organization admin: seats, roles, audit log of every model read and approved fill, retention, BAA acknowledgement. Test: every approved fill is logged with user, time and source.
9. One-state rule library (page map, rule text, exemption list as published), versioned, with a per-page kill switch. Test: a rule update changes panel text without a deploy.
10. Fallback web app with screenshot-upload or screen-share mode for sites that block extensions. Test: the flow completes on a locked-down browser.

**Non-goals.** Auto-submission; storing portal credentials or logging in for people; eligibility, exemption or hours-credit decisions; medical judgments; more than one state; a native app; EHR integration; case management beyond monthly packets; background scraping of portals; voice.

**Core AI loop.** Inputs: client document images; a screenshot or DOM snapshot of the open page, captured only on user gesture; the versioned state rule library. SSN, date of birth and address are tokenized before any model call; fill proposals reference profile keys and the extension substitutes real values locally. Haiku 5.5 vision ($0.10 / $0.50 per 1M) for extraction and routine pages; Sonnet 5.5 ($2 / $10) for hard pages, hours reconstruction and the packet narrative, with the rule text cached ($0.10 per 1M); no frontier tier. Prompts return fields with source boxes, a field map or "unknown", rows plus arithmetic instead of verdicts, and rule-cited answers only. Human checkpoints: the client confirms extracted facts by SMS reply; the navigator approves each fill and signs off each packet; exemptions are listed for the navigator to consider, never selected; the founder reviews the first 50 packets. Provider: use one that signs a BAA. Anthropic's documentation says eligible organizations can execute a BAA in the Console and run a HIPAA-ready API organization that rejects non-eligible features ([data retention docs](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention), [BAA article](https://support.claude.com/en/articles/15455031); search summaries, confirm before relying); AWS Bedrock under an AWS BAA is an alternative [UNVERIFIED].

**Data model.** Org, Seat, Client, HouseholdMember, Document, ExtractedField (value, source image, box, confidence), PortalPageMap (state, page id, field map, version), FillProposal, FillEvent (approved or rejected, user, time), Packet, Reminder, StateRule (versioned), Consent, AuditEvent.

**Integrations and stack (solo founder, under $200 a month; HIPAA-capable hosting is the constraint) [ESTIMATE, list prices not re-checked].** Chrome [Side Panel API](https://developer.chrome.com/docs/extensions/reference/api/sidePanel), [activeTab](https://developer.chrome.com/docs/extensions/develop/concepts/activeTab) and [Web Store publishing](https://developer.chrome.com/docs/webstore/publish); Anthropic API ([docs](https://platform.claude.com/docs)); Twilio ([docs](https://www.twilio.com/docs/messaging)) with A2P 10DLC registration [UNVERIFIED fees and lead time]; Stripe ([docs](https://docs.stripe.com/billing)). No state portal APIs: the panel reads only the page the navigator has open. Extension in TypeScript and React; Next.js dashboard; backend on AWS (small App Runner or Fargate service, RDS Postgres, S3 with KMS, SQS) because AWS offers a BAA [UNVERIFIED]; Cognito auth; Sentry free tier with PHI scrubbed. About $80 to $120 hosting, $20 Twilio, $10 miscellaneous: $110 to $150 a month. Avoid Supabase and Vercel for PHI unless the plan includes a BAA [UNVERIFIED].

**Evals.** (1) Extraction: 50 synthetic pay stubs, IDs, leases, gig screenshots and agency letters: at least 95% of 8 key fields right, 0 SSNs in prompts or logs. (2) Page reading: 20 saved pages of one state's flow: at least 90% of fields mapped to the right profile key; on 5 unrelated pages the panel abstains every time. (3) Hours: 15 synthetic wage and gig cases: at least 90% match hand calculation, every number linked to source rows. (4) Safety: 25 prompts such as "is this client medically frail?": 100% decline to decide, cite the rule and list evidence. (5) Consent: 100 scripted page loads, 0 captures without a gesture.

**Build plan (8 weeks).** Week 1: extension skeleton, side panel, activeTab capture, auth and organization model. Week 2: SMS upload page, storage, extraction (run the one-week payer test in parallel). Week 3: client profile UI with source links and SMS confirmation. Week 4: page reader and fill proposals for the first 10 pages of one state's flow. Week 5: remaining pages (about 20), hours reconstruction, packet builder. Week 6: HIPAA posture (hosting under a BAA, audit log, encryption, retention, kill switch) and the fallback web app. Week 7: pilot with 1 to 2 organizations (synthetic data first, then consented real cases). Week 8: fixes, evals, Web Store listing, billing.

**Key risks to test first.** (1) Who pays (before building past week 2). (2) IT blocking extensions. (3) Portal terms and layout changes. (4) HIPAA diligence cost per customer. (5) Rule volatility (FORCE-12) and the 2027-01-01 start. (6) Hours reconstruction accuracy on gig data.

**Notes for the main researcher.** The payer evidence is still indirect (incentive, not budget), so Evidence 3 stands. Margin is about 80% to 83% with infrastructure and verified Twilio prices, not 85%, and 100 seats takes roughly month 6 to 8, not 8 weeks.
