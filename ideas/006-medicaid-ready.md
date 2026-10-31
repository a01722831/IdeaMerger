---
id: "006"
slug: medicaid-ready
name: Medicaid Ready
one_liner: "Builds a nursing-home Medicaid application packet from five years of statements, with flagged transfers and drafted explanation letters."
target_user: "Adult children and spouses placing a parent in nursing or memory care who must file a long-term-care Medicaid application"
form_factor: "web app"
lens: "Pain-first"
frontier: false
competition: "WEAK DIRECT"
confidence: "MED"
status: "developed"
signals: [LIFE-17, LIFE-18, LIFE-13, LIFE-16]
scores:
  pain: 4
  evidence: 3
  ai_leverage: 4
  whitespace: 3
  novelty: 3
  why_now: 3
  solo_feasibility: 3
  distribution: 3
  wtp_economics: 4
  scale_defensibility: 2
total: 65.3
price_hypothesis: "$349 one-time per applicant (packet plus 90 days of request tracking); free flagged-items preview"
model_cost_per_user_month: "$4.3 per case, one-time (about $1.4/month over a 90-day case)"
gross_margin: "93%"
mvp_weeks: 7
deep_dive: false
red_team: false
---

# Medicaid Ready

## 1. One-liner
Builds a nursing-home Medicaid application packet from five years of statements, with flagged transfers and drafted explanation letters.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 4 | Facility-set deadlines, years of statements, $6K to $15K quotes; but each family goes through it once. |
| Evidence quality | 2 | 3 | Two direct Medicaid signals (LIFE-17, LIFE-18), two adult-child admin signals and two new threads; one clear price anchor ($6K service versus $15K lawyer). |
| AI leverage | 2 | 4 | Reading 60 months of statements and spotting transfers is most of the paid labor and the model does it; agencies and humans still gate the outcome. |
| Whitespace | 2 | 3 | No consumer AI product found for this job; human services (about $6K), professional tools and one unverifiable rival (MedicaidSoft); DIY with Claude is the real substitute. |
| Novelty of insight | 1 | 3 | The flagged-items report as the thing families fear is a useful framing; that most of the fee is document review is plausible but unproven. |
| Why now | 1 | 3 | Reading hundreds of pages now costs dollars, but the problem is old and long-context models are already in families' hands. |
| Solo feasibility | 2 | 3 | Statement analysis is about 4 weeks of work; state forms, state rules and legal framing push the MVP to 7 weeks for three states. |
| Distribution | 2 | 3 | High-intent search and forum Q&A (AgingCare, r/EstatePlanning); discharge planners can point to it; a one-time purchase has no loop. |
| Willingness to pay and unit economics | 2 | 4 | Payers already budget $6K to $15K; at $349 the margin is above 90% even with spot-check QA. |
| Scale and defensibility | 2 | 2 | One-time purchase, a DIY substitute and state-by-state upkeep; the rules library is a modest moat. |
| **Total** | | **65.3** | |

Confidence: MED. FRONTIER: no.

## 3. The problem
- Who: families placing a parent in a nursing home or memory care. The facility, usually after a hospital stay, needs a Medicaid long-term-care application and sets the deadline.
- What it takes: bank and financial statements for the look-back period (60 months in most states; some states differ), explanations for withdrawals and transfers, verifications, and answers to later requests for information (RFIs).
- Cost: lawyers quote $15K and application services about $6K (LIFE-18). Attorney-written sources put non-attorney services at roughly $5,000 to $6,500 (competitor claims, treat as rough).
- Workarounds: ask the facility business office, DIY from the agency checklist, a paid service, or a lawyer. Without a power of attorney banks will not release statements (LIFE-17).
- Scale: KFF counts about 1.24M residents of certified nursing facilities (July 2025) and Medicaid as primary payer for 63% of them.

## 4. Evidence
- **LIFE-18** (strong, 2026-10-29, r/EstatePlanning, 28 comments): "Plus he said he would help her apply for Medicaid for $15K which is something she can do herself or pay $6K for a service to do it." https://www.reddit.com/r/EstatePlanning/comments/1xipw1b/
- **LIFE-17** (medium, 2025-12-30, AgingCare): "Can the LTC facility throw Auntie out of the facility if we cannot meet the required paperwork bank statements etc by the deadline? They only informed us of what they needed 2 days prior to Xmas." https://www.agingcare.com/questions/so-guess-the-next-question-is-can-the-ltc-facility-evict-our-lo-if-required-paperwork-is-not-receive-497529.htm
- **LIFE-13** (strong, 2026-10-27, r/AgingParents, 108 pts / 31 comments): the family document load after a death. "I (33 F) sifted through all the utility bills, mortgage, and car loan documents. Set up the pension documents and the IRA rollover process which should be processed by January." https://www.reddit.com/r/AgingParents/comments/1xh4xpu/
- **LIFE-16** (medium, 2026-10-06, AgingCare): "My father recently moved in with me, he is 75 years old and I am having a hard time managing the follow up appointments, coordinating referrals and just doing these admin things. I don't know how to address this with a full time job and other commitments." https://www.agingcare.com/questions/stressed-about-paperwork-about-my-father-in-need-need-tips-499738.htm
- New evidence (not in SIGNALS.md): r/EstatePlanning, 2026-10-13, 1 pt / 1 comment: "She put the life estate deed in place recently which is going to obviously trigger the 5-year look-back from Medicaid. She is 72 and currently hospitalized." Strategy questions arrive bundled with the paperwork. https://www.reddit.com/r/EstatePlanning/comments/1x4x6fo/
- New evidence (not in SIGNALS.md): HN, 2026-06-13: "The worst is for situations where their income (ssi/pensions) exceed qualification for medicaid, but are less than what could cover a nursing home. this can be solved with a miller trust but it takes time to setup so you better have another way to take care of them while sorting out." Legal-structure questions sit next to the application. https://news.ycombinator.com/item?id=48517313
- Context (not a pain signal): KFF, December 2025, about 1.24M certified-nursing-facility residents; 63% Medicaid primary payer in 2025. https://www.kff.org/medicaid/issue-brief/a-look-at-nursing-facility-characteristics/

## 5. The product
- What it does: a case file for one applicant. Guided intake (state, marital status, facility, who holds the POA), a state-specific document list, upload of statements by PDF, photo or forward, then AI builds a month-by-month transaction table across all accounts and a flagged-items report: large withdrawals, transfers to individuals, retitled accounts, cash deposits, insurance and annuity payments, closed accounts. The family answers a structured question for each flag, the AI drafts factual explanation letters from those answers, fills the state application, assembles an indexed verification packet, and tracks RFIs with deadlines.
- Core AI loop: statements in -> OCR and extraction -> flagging against the state's published rules and common caseworker questions -> question list -> family answers -> letters, forms and packet -> agency RFI letter photographed in -> response draft and attachment list -> outcome logged for next time.
- Interaction model: a web case dashboard with a checklist and an inbox for agency letters. The first output, a free count and preview of flagged items, is also the sales page.
- Form factor: web app, mobile friendly.
- Day in the life: Maria's father moves into memory care on Friday and the facility wants five years of statements. With POA in hand she uploads 61 PDFs and 14 photos from three banks over a weekend. The app returns nine flagged items, including a $14,000 withdrawal she recognizes as a roof, and she attaches the invoice. A month later the caseworker asks for one more statement; she photographs the letter and gets the response and attachment list.
- Liability line: assembly, organization and explanation only. It never advises on gifts, trusts, deeds, annuities, selling the house or spend-down, and never says whether a transfer is penalized; it quotes the agency's published rule and routes strategy questions to an elder-law attorney. Attorney-written sources say non-attorneys may prepare and file but not give legal advice; the exact line varies by state [UNVERIFIED].

## 6. Why the LLM is load-bearing
- Reading roughly 700 pages of heterogeneous, often photographed statements and classifying each transaction is the labor behind the $6K fee; OCR plus keyword rules produce too many false flags.
- Writing a plain, factual explanation letter from a family's answers, in the register caseworkers expect, and turning an RFI letter into a document request list are language tasks.
- Without the model the product is a checklist, which is what Etsy kits and templates already sell.

## 7. The insight
- Most of the fee is document review and assembly, which long-context models do for dollars. The flagged-items report, delivered before the caseworker finds the same items, is what families fear and need.
- Honest limit: whether AI-drafted letters satisfy caseworkers, and whether state asset-verification systems already surface most accounts, are untested [UNVERIFIED].

## 8. Why now, and why this does not exist yet
- Why now: OCR costs about $4 per 1,000 pages [UNVERIFIED in the landscape file] and a 1M-token context holds a whole case, so 720 pages cost about $3 to read. The facility population is large and steady.
- Why it is not here: the work sits next to legal advice, rules vary by state (California 30 months and reportedly being phased out; Maryland and Connecticut bulletins reduced documentation), and existing software sells to professionals. Human services at $5K to $6.5K are entrenched, some through nursing-home referrals.
- Honest limit: a tech-savvy family can already upload statements to a general assistant and ask for flagged transfers.

## 9. Inspiration and derivation
- Parents: done-for-you Medicaid packet services, professional statement-analysis tools (Bonadio ResourceFindr, Ocrolus Medicaid-Genius), and TurboTax-style guided interviews.
- Changed: target user (the family, not a firm), business model ($349 flat versus $6K service), interaction (self-serve preview before any payment), channel (search and forums versus facility referrals).

## 10. Competition check
Queries run:
1. WebSearch: "Medicaid long-term care application software AI look-back period bank statements nursing home families"
2. WebSearch (Product Hunt): "site:producthunt.com Medicaid application nursing home" (no Product Hunt results)
3. WebSearch (YC directory): "site:ycombinator.com/companies Medicaid applications benefits AI"
4. App Store, `scripts/app_reviews.py --find`: "Medicaid application help", "nursing home Medicaid" (only state Medicaid portals and home-care software)
5. WebSearch: "nursing home Medicaid application assistance service cost flat fee non-attorney Medicaid application preparation company families"
6. WebSearch: "KFF Medicaid nursing facility residents share paid by Medicaid number of nursing home residents 2025 long-term care Medicaid"; HN "Medicaid nursing home"; Reddit archive r/AgingParents, r/EstatePlanning, r/Medicaid, r/eldercare.

| Product or service | What it does | Price | How it differs |
|---|---|---|---|
| Non-attorney application services ([elder-law blog](https://www.eldercarelawyer.com/blog/applying-for-medicaid-cost-and-services/), [RBJ, 2012](https://rbj.net/2012/01/13/non-attorneys-may-not-handle-some-complex-medicaid-applications/)) | Prepare and file the application, no legal advice | About $5,000 to $6,500 (competitors' claims); $6K in LIFE-18 | Human, slow, some tied to facility referrals |
| Elder-law attorneys | Planning plus filing | $15K quote (LIFE-18); $2,500 to $4,500 in one attorney blog | Strategy and liability cover, which we do not offer |
| [Bonadio ResourceFindr](https://www.nysac.org/media/03hpipkp/bonadio_4-21-25-resourcefindr_100725.pdf) | Cloud tool that scans LTC Medicaid applicants' statements for assets and income (snippet) | n/a | Sold to professionals |
| [Ocrolus](https://ocrolus.com/?p=832) Medicaid-Genius (snippet) | Extracts data from Medicaid-required documents | n/a | B2B API |
| [Fortuna Health](https://www.mobihealthnews.com/news/fortuna-health-raises-18m-enhance-ai-medicaid-enrollment) | AI for Medicaid enrollment and recertification; $18M Series A led by Andreessen Horowitz, with YC participation (per MobiHealth) | B2B | Sells to providers, not families |
| [MedicaidSoft](https://gust.com/companies/medicaidsoft) | Search summary of its Gust listing says it uses software tools and AI to help families qualify for long-term care Medicaid; the page returned 403 | unknown | Only possible consumer rival; [UNVERIFIED] |
| [Ezel template](https://ezel.ai/templates/medicaid-application-checklist), [Etsy kit](https://www.etsy.com/listing/4543288665) | Static checklists | Low | No analysis |
| ChatGPT, Claude, Gemini | A family can upload statements and ask for flagged transfers | In subscription | No state forms, case state or RFI tracking |

Classification: **WEAK DIRECT**. Human services are the direct competitor; software rivals either sell to professionals or could not be verified. Kill criterion 5 (high-liability advice) is avoided only by the framing above.

Platform risk: file-based agents from OpenAI and Anthropic already enable the DIY review but will not build state forms, deadlines and RFI tracking. The vertical incumbents are elder-law firms and application services, which are services. B2B vendors (Fortuna, Ocrolus) could go consumer but sell to enterprises. Risk: low to medium; no rubric cap applies.

## 11. Business model
- Payer: the family member filing (often the adult child with POA). Price: $349 per applicant, including the packet and 90 days of tracking; $99 add-on for a spouse's documents or a re-filing; free flagged-items preview. Anchors: $6K services, $15K lawyers, $2.5K to $4.5K per one attorney blog.
- Model cost per case [ESTIMATE]: 60 months x 3 accounts = 180 statements, about 720 pages. OCR 720 x $0.004 = $2.88. Haiku 5.5 extraction 180 x (4,000 in x $0.10/1M + 1,000 out x $0.50/1M) = 180 x $0.0009 = $0.16. Sonnet 5.5 flagging and reconciliation, 10 passes x (20,000 in x $2/1M + 2,000 out x $10/1M) = 10 x $0.06 = $0.60. Letters 8 x (4,000 in + 800 out) = $0.13. Form fill 2 x (15,000 in + 2,000 out) = $0.10. Q&A and RFI chat 40 x $0.011 = $0.44. Total about $4.3.
- Other variable [ASSUMPTION]: Stripe fee 2.9% + $0.30 = $10.4; paralegal spot-check of the first 100 cases at 15 minutes x $40/hour = $10.
- Gross margin [ESTIMATE]: ($349 - $4.3 - $10.4 - $10) / $349 = 93%; 95% without spot checks.

## 12. Market size
- Buyers [ESTIMATE]: 1.24M facility residents x 63% Medicaid = 781K Medicaid-paid residents (LeadingAge's summary of KFF says about 756K). Assume an average 2.5-year Medicaid stay [ASSUMPTION], so about 310K new nursing-home Medicaid cases a year. Assume half need real statement review [ASSUMPTION] = 155K. This excludes home-care waivers and assisted-living Medicaid.
- Revenue: 155K x $349 = $54M a year if all bought. Realistic penetration 3% to 5% = 4.7K to 7.8K cases = $1.6M to $2.7M a year, plus add-ons.
- Reading: a solid niche business, not a venture-scale one on its own.

## 13. Go-to-market
- First 100 customers: (1) answer statement-and-deadline questions on AgingCare, r/AgingParents and r/EstatePlanning and offer the free flagged-items preview, about 40; (2) state-specific guides ("Medicaid look-back: what statements to gather in [state]") ranking against thin competing pages, about 30; (3) hospital social workers and discharge planners given a one-page handout, plus elder-law attorneys who want a prepared file for modest-asset clients, about 30. None needs a formal partnership.
- Growth loop: weak. Satisfied families refer others rarely; social workers and attorneys who see clean packets are the repeat referrers.

## 14. Moat and scale path
- Moat: a per-state rules and forms library, a dataset of which flags and letters caseworkers accept, and referral relationships. Modest and copyable.
- Scale path: annual redetermination, spouse protections, home-care waiver applications, a professional version sold to elder-law offices at a higher price.

## 15. Solo feasibility
- MVP (7 weeks): intake, upload and extraction, transaction table, flagged-items report with answerable questions, letter drafts, packet export, RFI tracker, three states (pick the largest by volume) with PDF form fill. Launch the flagged-items preview in week 5.
- Running cost before revenue: about $100 to $150 a month (hosting plus roughly $130 of model calls for 30 trial cases). One-time cost: an elder-law attorney review of the framing and disclaimers, about $1,500 to $3,000 [ASSUMPTION].
- Hardest risks: legal framing and per-state correctness, then scan quality and statements that cannot be obtained without a POA.

## 16. Pre-mortem
1. A bar association or attorney complaint treats the product as unauthorized practice of law, or one missed transfer causes a denial and a harmed family.
2. Families prefer to pay a human for an emotionally loaded, high-stakes filing; the $349 self-serve product does not convert.
3. State fragmentation: each new state costs weeks of rules and forms work, and rules change.

## 17. Cheapest validation test
- What: offer a free flagged-items report in r/EstatePlanning, r/AgingParents and AgingCare ("upload your statements, get the list in 24 hours"), produced by hand with Claude plus review. Ask each family for a 15-minute call and a $199 pre-order of the full packet. Have an elder-law attorney review three reports in a one-hour consult.
- Cost: about $250 to $400 (attorney hour plus tools). Duration: 3 weeks.
- Pass: at least 10 families upload real statements, at least 3 pre-order, and the attorney judges at least 80% of flags relevant with no advice leakage. Fail: fewer than 5 uploads or no pre-orders; then drop it or sell only to professionals.

## 18. Open questions
- Where exactly is the unauthorized-practice line for preparing explanation letters, and does it differ by state?
- How many cases arrive without a POA, where banks will not release statements (LIFE-17)?
- Do state asset-verification systems already find most accounts, making the family's own review less decisive? [UNVERIFIED]
- Will caseworkers accept AI-drafted explanation letters, and what do they actually ask?
- Is a professional version (elder-law offices, facility business offices) a better first market, given the conflict-of-interest warnings about facility-linked services?
