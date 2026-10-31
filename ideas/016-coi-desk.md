---
id: "016"
slug: coi-desk
name: COI Desk
one_liner: "An agent for small insurance agencies that drafts certificates of insurance from email requests and chases loss runs."
target_user: "Small independent commercial-lines insurance agencies (3-15 staff) on HawkSoft, EZLynx or Applied Epic"
form_factor: "web app"
lens: "Pain-first"
frontier: false
competition: "CROWDED"
confidence: "MED"
status: "killed"
signals: [PRO-021, PRO-022, PRO-023, PRO-025, PRO-024]
scores:
  pain: 3
  evidence: 3
  ai_leverage: 3
  whitespace: 1
  novelty: 2
  why_now: 3
  solo_feasibility: 3
  distribution: 2
  wtp_economics: 2
  scale_defensibility: 2
total: 48.4
price_hypothesis: "$149/month per agency, up to 300 requests; a free tier would be needed to meet a $0 rival"
model_cost_per_user_month: "$8"
gross_margin: "91% at $149, 80% at $49"
mvp_weeks: 6
deep_dive: false
red_team: false
---

# COI Desk

> **Main-thread review, 2026-10-31: KILLED.** CROWDED. Certificial prices agency certificate issuance at $0 and the agency-management systems (Vertafore, Applied, HawkSoft, EZLynx) bundle certificate tools; the open slice is a loss-run and non-pay chaser, which would need its own evidence. The file is kept as a record of the competition check.

## 1. One-liner
An agent for small insurance agencies that drafts certificates of insurance from email requests and chases loss runs.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | Certificate requests arrive daily and eat CSR hours, but this is an old, known chore that every AMS already addresses in part. |
| Evidence quality | 2 | 3 | Five signals: one strong (an insurance-industry insider on HN) and four from r/InsuranceAgent in 2026-10; none states willingness to pay. |
| AI leverage | 2 | 3 | The model reads messy request emails, contract insurance clauses and policy endorsements; the certificate itself is a deterministic form. |
| Whitespace | 2 | 1 | Funded direct rivals (Certificate Hero, Certificial with $0 agency issuance), AMS-native tools (Vertafore, Applied, HawkSoft, EZLynx) and AI service-desk startups. |
| Novelty of insight | 1 | 2 | "COI work is rule-bound and low-judgment" is the same insight the incumbents are selling. |
| Why now | 1 | 3 | Cheap long-context reading of policy PDFs is new, but AMS vendors shipped AI agents at Accelerate 2026 (April), so the window is closing. |
| Solo feasibility | 2 | 3 | An email-forward MVP with no AMS write-back is 6 weeks; AMS integrations are partner-gated, which is the hard part. |
| Distribution | 2 | 2 | One community channel (r/InsuranceAgent); agencies buy through their AMS vendor, carriers and associations. |
| Willingness to pay and unit economics | 2 | 2 | Clear payer and about 91% margin, but the market anchor for issuance is $0, so only the bundle (chasers, contract check) can be priced. |
| Scale and defensibility | 2 | 2 | Platform risk from the AMS vendors caps this at 2; the small-agency niche is only a few thousand buyers. |
| **Total** | | **48.4** | |

Confidence: MED. FRONTIER: no. Honest read: CROWDED. See section 18 for the recommendation.

## 3. The problem
- Who: CSRs and account managers at independent agencies who handle certificate requests (holder name, additional insured, waiver of subrogation, primary and non-contributory wording) arriving by email all day.
- Cost: an insurance-industry insider expects about $500K of savings in a year from an agent that handles certificate requests (PRO-021). Separately, commercial deals stall in "Waiting on Data" while the agent chases loss runs and prior policies (PRO-023), and non-pay cancellation outreach is done by hand (PRO-025).
- Workarounds: the AMS self-service certificate portal for standard cases, manual ACORD 25 editing for the rest, and a paid Claude skill that "is just not living up to the hype" (PRO-022).
- Liability: certificate wording is E&O-sensitive; staff verify everything an AI drafts (PRO-024 on AI-generated questionnaires, same logic).

## 4. Evidence
- **PRO-021** (strong, 2026-01-06, HN): an insurance insider says their certificate-handling agent "will note when a certificate of insurance is requested over email and automatically handle the necessary checks and follow up options or resolution. Will likely save us around $500k this year." https://news.ycombinator.com/item?id=46508806
- **PRO-022** (medium, 2026-10-29, r/InsuranceAgent, HawkSoft user): "I recently paid to use the Claude skill called Freebird to assist with using Claude (AI) for loads of admin tasks inside of Hawksoft. The idea of it is great, cost is reasonable, but execution is just not living up to the hype." https://www.reddit.com/r/InsuranceAgent/comments/1xinbi7/ Shows spend plus an unmet need.
- **PRO-023** (medium, 2026-10-27, r/InsuranceAgent, AgencyZoom user): "Currently a lot of my deals are getting stuck in the middle of the pipeline particularly in Waiting on Data (this could be loss runs, or needing their current insurance policies sent to me so I can send to the underwriter.)" https://www.reddit.com/r/InsuranceAgent/comments/1xh3z8e/
- **PRO-025** (medium, 2026-10-17, r/InsuranceAgent): the owner wants the CSR to "all but knock on doors" with non-pay policyholders; the outreach cadence is manual. https://www.reddit.com/r/InsuranceAgent/comments/1x8f1ha/
- **PRO-024** (medium, 2026-10-20, r/InsuranceAgent): "even if we use AI to generate a reply, our E&O and loss ratio is on the line - we have to verify every one." https://www.reddit.com/r/InsuranceAgent/comments/1xb45at/ Shows the approval-first design is mandatory.
- Gap in the evidence: none of these says "I would pay $X for certificate automation". The price signal that does exist points down (Certificial lists agency issuance at $0, see section 10).

## 5. The product
- What it does: a shared service inbox agent. It reads each certificate request, identifies the insured and policy in the agency's data, checks the contract's insurance clause against the policy's actual endorsements, drafts the ACORD 25 (and the matching endorsement copies), and puts it in a CSR approval queue. One click sends and logs it. A second queue chases loss runs, prior policies and non-pay reinstatements on a cadence.
- Core AI loop: request email plus attachments -> extraction (holder, wording asked for, deadline) -> compare with policy declarations and endorsements -> draft with a "gap" list (for example, no waiver of subrogation endorsement on the GL policy) -> CSR edits -> sent; corrections become per-client rules.
- Interaction model: forward-to-address or Gmail/Outlook add-on; a web approval queue; no AMS write-back in the MVP (CSV and PDF export for the AMS).
- Form factor: web app with an inbound email address.
- Day in the life: a general contractor's client emails "need a cert naming the City and ABC Corp as additional insured, primary and non-contributory". The desk finds the GL policy, sees the blanket additional-insured endorsement but no primary wording, drafts the certificate, flags the gap, and the CSR calls the carrier instead of issuing a certificate that overstates coverage.

## 6. Why the LLM is load-bearing
- Requests are free text with attached contracts and prior certificates; reading the insurance clause and mapping it to endorsement forms (for example CG 20 10 or CG 20 37) is language work.
- Without the model, what is left is a form filler that the AMS portals and Certificial already provide for the easy 70% of requests. The model's value is the hard residue and the gap check.

## 7. The insight
- The easy certificate is solved and free; the expensive one is the request whose wording the policy does not support. A product that says "this certificate would be wrong, here is why" protects the agency's E&O, which is worth money, while generating a form is not.
- Honest limit: this insight is shared by Certificate Hero, which parses contracts with AI.

## 8. Why now, and why this does not exist yet
- Why now: long-context models can read a 40-page policy for about $0.05 (section 11); Vertafore added an integrated COI tool to AgencyOne at Accelerate 2026 and six AI agents, so the buyers are being primed.
- Why it already exists: see section 10. It exists in several forms; the only gap is small agencies on HawkSoft or EZLynx, which a new entrant could serve through email rather than integrations.

## 9. Inspiration and derivation
- Parents: Certificate Hero (contract parsing plus AMS connectivity), Certificial (issuance plus tracking), Acolite (YC; "forward it an email").
- Changed: target user (3-15 person agencies on HawkSoft and EZLynx, not brokers like Brown & Brown), interaction model (forward an email, no integration), business model (flat monthly with approval queue), plus the chaser module for loss runs. Core job is largely the same, so the derivation is weak.

## 10. Competition check
Queries run:
1. WebSearch: "AI agent automates certificate of insurance requests insurance agency email ACORD 25 issue COI automatically"
2. WebSearch (Product Hunt): "site:producthunt.com certificate of insurance COI automation insurance agency"
3. WebSearch (YC directory): "site:ycombinator.com/companies insurance agency AI certificates of insurance service inbox"
4. WebSearch (AMS vendors as the relevant marketplace): "Applied Epic OR AMS360 OR HawkSoft OR EZLynx AI certificate of insurance automation 2026 agency management system AI assistant"
5. WebSearch: "Certificate Hero raises $4.5 million COI platform investors AI contract review agencies Brown & Brown"
6. WebSearch: "Vertafore AgencyOne integrated Certificates of Insurance COI solution Accelerate 2026 announcement"
7. WebSearch: "AI customer service rep independent insurance agency service inbox certificates endorsements startup raises 2026 HawkSoft EZLynx"
8. WebSearch: "Freebird Claude skill HawkSoft insurance agency AI admin tasks" (no page about Freebird found)
9. WebFetch of a COI automation guide (2026-10-15) for price points. Two other fetches (iireporter, coverager) failed.

| Product | What it does | Price | How it differs |
|---|---|---|---|
| [Certificate Hero](https://certificatehero.com/blog/agentic-and-generative-artificial-intelligence-transforms-agency-performance) | AI contract parsing, certificate issuance, ACORD form editor, AMS connections (Applied Epic, AMS360, Sagitta per its blog); $4.5M seed II in 2022 led by RRE, $6.5M total ([GlobeNewswire](https://www.globenewswire.com/news-release/2022/03/15/2403508/0/en/Certificate-Hero-Raises-4-5-Million-and-Prepares-to-Launch-Its-Best-in-Class-Certificate-of-Insurance-Processing-Platform-With-a-Top-10-Broker.html)); Brown & Brown selected it ([Coverager](https://coverager.com/brown-brown-selects-certificate-hero-to-modernize-coi-workflows/)) | not visible | Closest direct rival; sold to brokers with AMS integrations, likely out of reach for 3-person agencies [UNVERIFIED] |
| [Certificial](https://certificial.com/blog-post/empowering-modern-agencies-digitizing-coi-issuance-and-response-processes) | Smart COI issuance and tracking, AMS data sync; $5.8M Series A in 2021 ([BusinessWire](https://businesswire.com/news/home/20210608005689/en/Insurtech-Startup-Certificial-Secures-5.8-Million-in-Series-A-Funding)) | "Agency issuance: $0"; requestor Professional from $99/month, per a [2026-10-15 guide](https://ustechautomations.com/resources/blog/automatically-generating-certificates-of-insurance-2026) quoting its pricing page | Free issuance sets the price floor for the core job |
| [Vertafore AgencyOne COI](https://coverager.com/vertafore-unveils-integrated-certificates-solution-to-remove-service-bottlenecks-and-accelerate-distribution-velocity-for-agencies/) | Integrated certificates for AMS360 and InsurLink customers, client self-service around the clock, Sagitta later (Accelerate 2026, April; [press release](https://www.vertafore.com/resources/press-releases/vertafore-unveils-integrated-certificates-solution-remove-service)) | bundled | The incumbent shipping the feature; also six AI agents on its Velocity platform |
| Applied Epic / CSR24, HawkSoft and EZLynx self-service | Connected certificate workflows and client self-generation, per the same guide; Applied has an "Applied AI" initiative per a [mid-2026 review](https://www.layer3labs.io/comparisons/best-ai-tools-for-insurance-agencies) | bundled | Easy cases already handled; limits on endorsement requests (guide) |
| [NowCerts](https://marketplace.btisinc.com/wp-content/uploads/2024/04/NowCerts_flyer__040124.pdf), [Momentum AMS InsuranceAgency.ai](https://support.momentumamp.com/support/solutions/articles/156000382659-insuranceagency-ai-using-ai-to-automate-insurance-agency-workflows-in-momentum-ams) | An AMS built around COI and ACORD automation; AI-generated ACORD 25s from AMS data | n/a | Small AMS vendors; same job inside their own system |
| [InsuraMate AI](https://www.capterra.com/p/10045438/InsuramateAi/), [General Magic](https://www.axios.com/pro/fintech-deals/2026/02/24/general-magic-sms-insurance-agents) | Always-on receptionist handling certificates end to end for independent agencies (Capterra lists Applied Epic only); SMS agents for insurance teams, $7.2M seed per Axios (2026-02) | n/a | Startup rivals for the "AI service desk" framing |
| [Acolite](https://www.ycombinator.com/companies/acolite) (YC) | AI-native brokerage whose AI teammates handle submissions, COIs and SOV mapping across any AMS; "forward an email" | n/a | Same interaction, but it is a brokerage, not software |
| [Cassidy](https://cassidyai.com/solutions/ai-certificate-of-insurance-processing-agent), [V7 Labs](https://www.v7labs.com/agents/ai-agent-for-certificate-of-insurance-issuers), [HelloTars](https://hellotars.com/ai-agents/insurance-certificate-request-ai-agent) | Horizontal agent builders with COI templates | n/a | DIY, shows how cheap a generic version is |
| [C2COI](https://www.producthunt.com/p/c2coi), [CertShield](https://www.producthunt.com/products/certshield/reviews) (Product Hunt), TrustLayer, myCOI | Tracking and verification of vendors' certificates (the holder side) | TrustLayer: free to 50 vendors, then $10/vendor/month (per the guide) | Different side of the same certificate |

Classification: **CROWDED**. Several funded or AMS-bundled direct rivals, one of which prices agency issuance at $0.

Platform risk: very high. The AMS vendors (Vertafore now, Applied and HawkSoft next) own the policy data and are shipping agents. Claude and ChatGPT agents with insurance skills (a [guide on Claude skills for brokers](https://www.layer3labs.io/guides/claude-skills-for-insurance-brokers)) can do the draft step for an agency that has a skills-savvy owner. Per the rubric this caps Scale and defensibility at 2 and Whitespace at 3; the rival count puts Whitespace at 1.

## 11. Business model
- Payer: the agency principal. Price: $149/month per agency up to 300 requests, $349 for up to 5 CSR seats with chasers. Anchors: Certificial $0 issuance, Certificial requestor tier $99/month, Freebird "reasonable" (price not visible). Expect to need a free tier for issuance and charge for the gap check and chasers.
- Model cost per agency per month [ESTIMATE], 300 requests, 150 policies/year: triage on Haiku 5.5, 3,000 in + 500 out = $0.00055 x 300 = $0.17; policy check on Sonnet 5.5 with cached policy context, 20,000 cached x $0.10/1M + 3,000 in x $2/1M + 800 out x $10/1M = $0.002 + $0.006 + $0.008 = $0.016 x 300 = $4.80; 100 chaser messages on Haiku at $0.0004 = $0.04; policy ingestion 12.5 policies/month x (40,000 in x $1/1M + 2,000 out x $5/1M = $0.05) = $0.63 plus OCR 500 pages x $4/1,000 = $2.00 (OCR price [UNVERIFIED]); email delivery about $0.50 [ASSUMPTION]. Total about $8.
- Gross margin [ESTIMATE]: ($149 - $8 - $4.62 Stripe) / $149 = 91%. At $49: ($49 - $8 - $1.72) / $49 = 80%.

## 12. Market size
- Buyers [ESTIMATE, UNVERIFIED base]: about 36,000 independent agencies in the US (a figure recalled from industry surveys, not verified here). Assume 30% are commercial-lines shops with 3 or more staff on an AMS [ASSUMPTION] = 10,800.
- Revenue: 10,800 x $149 x 12 = $19.3M a year if everyone bought. At 3% penetration (324 agencies) = $0.58M ARR.
- Reading: a small niche; scale needs a carrier-side or MGA channel, which is enterprise sales.

## 13. Go-to-market
- First 100: (1) answer certificate and "Waiting on Data" posts in r/InsuranceAgent with a free request-to-certificate gap checker (paste a contract clause and a policy summary), about 30; (2) state independent-agent association newsletters and webinars [ASSUMPTION: they accept vendor guest content]; (3) AgencyZoom and HawkSoft user groups and marketplaces [ASSUMPTION: open to third-party listings]; (4) SEO on "certificate of insurance request additional insured wording" queries, about 30.
- Growth loop: every certificate sent carries a small "drafted with COI Desk" footer for holders (general contractors and property managers), who often work with several agencies.

## 14. Moat and scale path
- Moat: per-agency correction rules and a library of contract-clause patterns; weak against an AMS vendor with the data.
- Scale path: loss-run and submission chasers for commercial lines, then an MGA or carrier channel. Both run into the crowded submission-intake market.

## 15. Solo feasibility
- MVP (6 weeks): inbound email parsing, policy PDF ingestion, ACORD 25 PDF generation, approval queue, correction rules, loss-run chaser templates. No AMS write-back.
- Running cost before revenue: about $60 to $120 a month (hosting, email, 10 pilot agencies x $8).
- Hardest risk: certificate accuracy and E&O exposure (a wrong certificate), then AMS data access (Applied and Vertafore APIs are partner-gated [ASSUMPTION]).

## 16. Pre-mortem
1. The easy cases are free and the hard cases are rare, so no agency pays $149.
2. The AMS vendors ship good-enough agents to their own base, or the owner uses a Claude skill.
3. A wrong certificate causes an E&O claim, and trust ends the business.

## 17. Cheapest validation test
- What: collect 30 anonymised request emails and the matching policy documents from 5 small agencies; run the draft and gap check by hand with a long-context model; the CSR grades each. Then offer $149/month while showing the free alternatives.
- Cost: about $20 in model calls. Duration: 3 weeks.
- Pass: at least 80% of standard certificates accepted without edits, the gap check catches at least 5 real mismatches, and at least 3 of 5 agencies commit to $149/month despite free options. Fail: under 2 agencies would pay.

## 18. Open questions
- Recommendation: do not build the certificate generator; it is CROWDED and the price anchor is $0. The only sharper wedge in the evidence is the chaser work that is not certificates ("Waiting on Data" loss runs and non-pay outreach, PRO-023 and PRO-025), or a contract-versus-policy gap check sold to contractor-focused agencies. If neither passes the section 17 test, kill it.
- Do small HawkSoft and EZLynx agencies see Certificial and the AMS portals as good enough? Does Certificial's free issuance cover endorsement-heavy requests?
- Is there any API route into HawkSoft or EZLynx without a partnership?
- Who bears E&O when an AI-drafted certificate is approved by a CSR?
