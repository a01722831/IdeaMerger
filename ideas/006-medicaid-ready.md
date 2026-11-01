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
deep_dive: true
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

## Deep dive

### Competitor table
| Competitor | Link | What it does | Price (as published, with date read) | Funding or traction (sourced) | Gap this idea exploits |
|---|---|---|---|---|---|
| Non-attorney application services | [elder-law blog](https://www.eldercarelawyer.com/blog/applying-for-medicaid-cost-and-services/), [RBJ, 2012](https://rbj.net/2012/01/13/non-attorneys-may-not-handle-some-complex-medicaid-applications/) | Prepare and file the LTC Medicaid application; no legal advice | About $5,000 to $6,500 (competitors' claims in that blog, read 2026-10-31); $6K in LIFE-18 (2026-10-29) | Not published; some tied to facility referrals | Self-serve $349 with a free preview; the family keeps control |
| Elder-law attorneys | [LIFE-18](https://www.reddit.com/r/EstatePlanning/comments/1xipw1b/), [Legal Clarity](https://legalclarity.org/how-much-does-a-medicaid-lawyer-cost/) | Planning plus filing, with strategy and liability cover | $15K quote (LIFE-18); roughly $1,000 to $6,000 flat for straightforward help per Legal Clarity (search summary, page not fetched) [UNVERIFIED]; $2,500 to $4,500 in one attorney blog (section 10) | Not applicable | Strategy stays with the attorney; we hand over an organized file |
| MedicaidSoft | [Utah Business, 2025-01-27](https://www.utahbusiness.com/entrepreneurship/2025/01/27/medicaidsoft-wins-utah-tech-week-pitch-competition/), [Gust](https://gust.com/companies/medicaidsoft) | Platform that "helps prepare long-term care applications by automatically integrating with financial data systems" | Not stated | $200,000 pitch prize; the article mentions a "$2 million seed round" (closing not confirmed); "57 percent fewer rejections in half the time" is the company's claim; Krause Financial recommends it to its platform of 4,000 elder-law attorneys | Sold through attorneys; data feeds miss paper or photographed statements; no family-facing preview seen |
| Bonadio ResourceFindr, Ocrolus Medicaid-Genius | [NYSAC deck](https://www.nysac.org/media/03hpipkp/bonadio_4-21-25-resourcefindr_100725.pdf), [Ocrolus](https://ocrolus.com/?p=832) | Scan LTC applicants' statements for assets and income (snippets); Senior Planning Services uses Ocrolus for "large nursing home chain clients" | Not published | Ocrolus claims 99+% accuracy (self-reported) | Professional and B2B only |
| Fortuna Health, Benefits Fast Inc. | [MobiHealth](https://www.mobihealthnews.com/news/fortuna-health-raises-18m-enhance-ai-medicaid-enrollment), [Gust](https://gust.com/companies/benefits_fast_inc) | Fortuna: AI Medicaid enrollment and renewal for providers and insurers. Benefits Fast: SaaS for nursing homes to manage Medicaid applications (snippet) | Not listed / not published | Fortuna: $18M Series A led by Andreessen Horowitz with YC participation (per MobiHealth, as recorded in section 10; article date not recorded) | Plan- and facility-side; not a family's five-year statement review |
| NavigAid (2021), Bridge Legal guide, Ezel and Etsy kits | [NavigAid](https://www.businesswire.com/news/home/20211013005113/en/NavigAid-Supports-Caregivers-Through-the-Medicaid-Application-Process), [Bridge Legal](https://bridgelegal.org/nursing-home-medicaid-application/), [Ezel](https://ezel.ai/templates/medicaid-application-checklist), [Etsy](https://www.etsy.com/listing/4543288665) | Guides and checklists (titles and snippets only) | Free to low; exact prices not recorded | Not published | No statement analysis, no deadlines |
| ChatGPT, Claude, Gemini | not applicable | A family uploads statements and asks for flagged transfers | Inside subscriptions; not re-checked here | Not applicable | No state forms, case state, RFI tracking or packet |

Classification stays WEAK DIRECT. MedicaidSoft is the new, real rival, but it reaches families through attorneys.

### Market sizing (bottom-up)
- Buyer: the family member, often an adult child with power of attorney, who files a nursing-home Medicaid application. KFF counts about 1.24M certified-facility residents with Medicaid as primary payer for 63% ([KFF](https://www.kff.org/medicaid/issue-brief/a-look-at-nursing-facility-characteristics/), section 3): 1,240,000 x 0.63 = 781,200.
- Stock to flow [ASSUMPTION]: new cases a year = residents / average Medicaid-paid stay (3.5 years conservative, 2.5 optimistic); the share needing real statement review is 40% / 60%.

| Case | New cases a year | Needing real review | Serviceable | Adoption | Customers a year | Revenue a year |
|---|---|---|---|---|---|---|
| Conservative | 781,200 / 3.5 = 223,200 | 40% | 89,280 | 1% | 893 | 893 x $349 = $0.31M |
| Optimistic | 781,200 / 2.5 = 312,480 | 60% | 187,488 | 5% | 9,374 | 9,374 x $349 = $3.27M, plus 15% x $99 add-ons = $0.14M |

- If every serviceable case bought: 89,280 x $349 = $31M and 187,488 x $349 = $65M. Revenue at 100, 1,000 and 10,000 paying cases: $34,900, $349,000 and $3,490,000; 10,000 cases is 11% of the conservative pool and 5% of the optimistic one. Not counted: home-care and assisted-living Medicaid, annual redetermination, a professional version.

### Unit economics
One-time purchase with a 90-day case, so cost per active month is the case cost / 3. Prices from `research/LANDSCAPE.md` section 6.

| Stage | Calls | Tokens per call | Model and price per 1M | Arithmetic [ESTIMATE] | Cost |
|---|---|---|---|---|---|
| OCR (photos and scans only) | 720 pages | n/a | Mistral OCR about $4 per 1,000 pages [UNVERIFIED in landscape file] | 720 x $0.004 | $2.88 |
| Statement extraction | 180 | 4,000 in, 1,000 out | Haiku 5.5, $0.10 / $0.50 | 180 x ($0.0004 + $0.0005) | $0.16 |
| Flagging and reconciliation | 10 | 20,000 in, 2,000 out | Sonnet 5.5, $2 / $10 | 10 x ($0.040 + $0.020) | $0.60 |
| Explanation letters | 8 | 4,000 in, 800 out | Sonnet 5.5 | 8 x ($0.008 + $0.008) | $0.13 |
| State form fill | 2 | 15,000 in, 2,000 out | Sonnet 5.5 | 2 x ($0.030 + $0.020) | $0.10 |
| Q&A and RFI chat | 40 | 3,000 in, 500 out | Sonnet 5.5 | 40 x ($0.006 + $0.005) | $0.44 |
| Total model and OCR | | | | 2.88 + 0.16 + 0.60 + 0.13 + 0.10 + 0.44 | $4.31 |

- Other per case: payments 2.9% x $349 + $0.30 = $10.42; paralegal spot-check 15 min x $40/h = $10 for the first 100 cases, then 10% sampled = $1.00 [ASSUMPTION]; notifications 20 x $0.012 = $0.24 (Twilio SMS $0.0083 plus about $0.004 carrier fee, [Twilio pricing](https://www.twilio.com/en-us/sms/pricing/us), read 2026-10-31); support 30 min x $30/h = $15 [ASSUMPTION]; infrastructure $100 a month / 30 cases = $3.33 early (/ 100 cases = $1.00).
- Margin: early 4.31 + 10.42 + 10.00 + 0.24 + 15.00 + 3.33 = $43.30, so ($349 - $43.30) / $349 = 87.6%; at scale 4.31 + 10.42 + 1.00 + 0.24 + 15.00 + 1.00 = $31.97, so 90.8% (section 11's 93% omitted support and infrastructure). Per active month: $116.33 revenue against $14.43 early cost. A 30% larger token count from the newer tokenizer adds 1.43 x 0.30 = $0.43.
- Heavy user (6 accounts, 360 statements, 1,440 pages): OCR 1,440 x $0.004 = $5.76; extraction 360 x $0.0009 = $0.32; flagging 25 x $0.06 = $1.50; letters 20 x $0.016 = $0.32; forms 4 x $0.05 = $0.20; chat 150 x $0.011 = $1.65; model total $9.75. Add payments $10.42, spot-check $10, notifications $0.50, support 2 h x $30 = $60, infrastructure $3.33: $93.99, margin 73%. Support, not the model, is the risk.
- Cap: $349 includes 1,000 pages, 100 chat messages, 3 RFI rounds and one 20-minute call; extra pages $0.10 (cost about $0.006); support beyond three tickets $40 an hour; spouse or re-filing add-on $99. The heavy case then pays 440 x $0.10 = $44 of overage, so margin (393 - 93.99) / 393 = 76%.

### First 100 customers
Funnel [ESTIMATE]: visit to started upload 8%, started to finished preview 60%, preview to paid 20%, so 1.0% of visits pay; referred families (deadline pressure, trusted referrer) pay 7%. Partner outreach: 60 individually written emails a week (30 hospital case-management or social-work departments, 30 small elder-law firms, from public contact pages); 10% reply = 6; 40% of repliers adopt the one-page handout = 2.4 new partners a week, active the next week, each handing it to 3 families a week.

| Week | What you do | New paid (math) | Cumulative |
|---|---|---|---|
| 1 | Preview, 6 state guides ("[State] Medicaid look-back: which statements to gather") and a checklist PDF live. 10 helpful replies a week in r/AgingParents, r/EstatePlanning, r/Medicaid, r/eldercare and the AgingCare forum (disclose you built it; link only where rules allow). First 60 partner emails. | 10 replies x 8 visits x 1.0% = 0.8 | 1 |
| 2 | Repeat; 60 more emails; first partners start. | 0.8 + (2.4 x 3 x 7% = 0.5) = 1.3 | 2 |
| 3 | Repeat; long AgingCare post ("How I would organize five years of statements"); $150 ad test on "medicaid look back bank statements [state]" (about $4 a click [ASSUMPTION], 37 clicks). | 0.8 + 1.0 + 0.2 + 0.4 = 2.4 | 4 |
| 4 | Repeat; 60 emails. | 0.8 + (7.2 x 3 x 7% = 1.5) = 2.3 | 6 |
| 5 | Repeat; 60 emails; second post; "deadline within 14 days" fast lane. | 0.8 + 2.0 + 0.2 = 3.0 | 9 |
| 6 | Repeat; last 60 emails; keep ads only if preview-to-paid beats 20%. | 0.8 + 2.5 = 3.3 | 12 |
| 7 | Third post; monthly "what caseworkers asked" digest for partners. | 0.8 + 3.0 + 0.2 = 4.0 | 16 |
| 8 | Review the funnel; double down on the best channel. | 0.8 + 3.0 = 3.8 | 20 |

- Result: about 21 paying cases by week 8 (the table rounds each week), run rate near 4 a week. With outreach continuing, the rate rises about 0.5 a week each week and cumulative cases reach 100 near week 19 (0.252 w squared + 0.548 w = 100). Section 13 expects about 70% of the first 100 from community and search; here those supply about a third of the first 21 (7.4). Optimistic case (20% reply, 12% referral conversion; 0.864 w squared = 100): near week 11.
- Channels: the subreddits and AgingCare above; hospital discharge planners and social workers (American Case Management Association and NASW chapters); elder-law attorneys (National Academy of Elder Law Attorneys directory, local bar sections); Aging Life Care Association care managers; Area Agencies on Aging and SHIP counselors; Alzheimer's Association ALZConnected [UNVERIFIED willingness]. SEO intent: "medicaid look back bank statements [state]", "nursing home medicaid application checklist [state]", "explain large withdrawal to medicaid caseworker", "medicaid denied missing bank statements".
- Message and offer: "See every withdrawal and transfer a caseworker may ask about, free, before you pay anyone. We organize and explain; we do not give legal advice." Professionals: "A prepared, indexed 60-month file for your client's family; free to you, no referral fees, not a law firm." Free preview; $349 packet with 90 days of RFI tracking; $99 spouse or re-filing add-on; 14-day refund if no packet was downloaded.
- Growth loop after 100: partners who see clean packets send more families (the only real loop); state guides compound as they rank; accepted-letter data improves flags; a white-label packet for elder-law offices turns the heaviest referrers into a second product.

### One-week validation test (under $50)
- Build (day 1): a one-page site saying "Early access. The full packet is not built yet; I prepare previews by hand with AI help. Not a law firm; no legal advice. If your facility deadline is within 30 days, call the facility business office or an elder-law attorney." Form: state, role, power of attorney yes or no, up to 25 largest withdrawals or transfers (date, amount, what it was; no account numbers). Stripe link for a $49 refundable deposit reserving a founding price of $199 for the full packet.
- Post (days 2 to 3): from your own real account, with disclosure, in r/AgingParents, r/EstatePlanning and the AgingCare forum where the rules allow offers (elsewhere answer questions and keep the page in your profile); tell your own network. No unsolicited messages, no second accounts.
- Deliver (days 3 to 6): for each submission, by hand with Claude, list the items a caseworker may ask about and the proof that usually answers each, quoting the state agency's published rule; never say whether a transfer is penalized. Reply within 24 hours and ask "was each item something you would expect to be asked about? yes or no".
- Budget [ESTIMATE]: domain $12; site, form and analytics on free tiers $0; Stripe fees on 3 deposits 3 x (2.9% x $49 + $0.30) = $5.16; Claude for 10 previews 10 x $0.04 = $0.40 and 3 full-statement runs 3 x $4.31 = $12.93; contingency $10; total $40.49.
- Metrics on day 7: unique visitors, real submissions (at least 5 genuine transactions), deposits, share of flags marked relevant, advice-leakage sentences checked against a written list ("will be penalized", "you should transfer", "put the house in").
- Pass (set in advance): at least 60 visitors AND at least 6 real submissions AND at least 2 deposits AND at least 80% of flags relevant AND 0 advice-leakage sentences. Fail: 2 or fewer submissions, or 0 deposits with 60 or more visitors; then drop it or sell only to professionals. In between: change channel or message and run one more week. Under 60 visitors is inconclusive. Refund deposits on request and delete submitted data within 30 days.

### Build brief (paste into a coding session)
**Product summary.** Medicaid Ready turns five years of a parent's statements into a nursing-home Medicaid packet. It builds one transaction table, flags what a caseworker may ask about, collects the family's answers, drafts factual explanation letters, fills the state application and tracks agency requests for information (RFIs). Free flagged-items preview, then $349.

**Liability line (keep visible in the UI, copy and prompts).** Assembly, organization and explanation only. Never advise on gifts, trusts, deeds, annuities, selling the house or spend-down; never say whether a transfer is penalized or for how long; quote the agency's published rule; route strategy questions to an elder-law attorney.

**MVP features (each testable)**
1. Intake (state, applicant, spouse, facility, who holds power of attorney) produces a state document checklist from a rules table. Test: matches the agency's published list for the launch state.
2. Upload of PDFs, photos and forwarded email, deduplicated by hash. Test: 20 mixed files, 0 duplicates stored.
3. Extraction to one transaction table with source page. Test: at least 98% of rows correct; balances tie on at least 95% of statements.
4. Coverage grid by month and account. Test: 3 removed statements are all detected.
5. Flagging (rules plus model) of large withdrawals, transfers to individuals, retitled or closed accounts, cash deposits, insurance and annuity payments, each citing source rows. Test: 11 of 12 seeded items found.
6. Free preview shows counts only. Test: no explanation text renders for an unpaid case.
7. One structured question per flag with proof attached. Test: a flag cannot close without an answer or "I do not know".
8. Letter drafts from the family's answers only, behind an advice-phrase filter. Test: 30 adversarial prompts give 0 penalty judgments.
9. Indexed packet PDF plus the filled state application for the launch state. Test: links work and every flag has proof pages.
10. RFI tracker: a photo of an agency letter becomes deadline, requested items and a response draft, with reminders. Test: at least 90% of 15 sample letters parsed correctly.

**Non-goals.** Advice of any kind; penalty-period math; e-filing; live bank connections; assisted-living or home-care waivers; more than one state at launch; a mobile app; referral fees; a human review desk.

**Core AI loop.** Inputs: statements, family answers, agency letters, a versioned state rules table. Text-layer PDFs skip OCR; photos go through OCR ([Mistral docs](https://docs.mistral.ai/)). Extraction on Haiku 5.5; balance checks in code, with Sonnet 5.5 only for rows that fail to tie; flagging by rules first, then Sonnet 5.5 on candidate rows with the state rule text cached; letters, form fill and RFI responses on Sonnet 5.5; no Opus. Prompts return structured rows with confidence and source page, a category with the exact rule sentence (never a verdict), and letters that restate the family's own answers. Human checkpoints: the family confirms balances, answers every flag and signs every letter; the founder or a paralegal spot-checks the first 100 packets; an automatic filter blocks advice phrases.

**Data model.** Case, Person, Account, Statement, Page, Transaction, Flag, Question, Answer, Evidence, Letter, Packet, StateRule (versioned), StateForm, AgencyLetter, Deadline, Payment, AuditEvent.

**Integrations and stack (under $200 a month) [ESTIMATE, vendor list prices not re-checked].** Anthropic API ([docs](https://platform.claude.com/docs)), Mistral OCR, Stripe Payment Links ([docs](https://docs.stripe.com/payment-links)), Resend email ([docs](https://resend.com/docs)), pypdf for forms ([docs](https://pypdf.readthedocs.io/)). Next.js on Vercel (about $20), a Python FastAPI worker on Fly.io or Render (about $15), Supabase Postgres, Auth and Storage with row-level security (about $25), a Postgres job queue, Sentry free tier, 90-day default retention with a delete button: about $80 to $120 a month plus model usage.

**Evals.** (1) Extraction: 30 statements (20 synthetic, 10 redacted real; digital and photographed): at least 98% of rows right, balances tie on 95%. (2) Flag recall: a synthetic 60-month, 3-account case with 12 seeded items: at least 11 found, no more than 30% noise. (3) Missing months: 3 removed, 3 reported. (4) Advice leakage: 30 questions such as "will this be penalized?": 0 verdicts, all routed to the attorney message. (5) RFI parsing: 15 letters, at least 90% correct.

**Build plan (7 weeks).** Week 1: auth, case model, rules table for the launch state (largest nursing-home Medicaid population with a 60-month look-back, after checking the agency manual), upload, encrypted storage. Week 2: extraction, OCR fallback, reconciliation, coverage grid. Week 3: flagging, report, free preview and checkout (live now, earlier than section 15's week 5). Week 4: question flow and evidence links. Week 5: letters with the filter, state form fill. Week 6: packet export, RFI tracker, reminders. Week 7: all evals, security pass, elder-law attorney review of copy and filters ($1,500 to $3,000 [ASSUMPTION]), pilot with 5 real cases.

**Key risks to test first.** (1) The unauthorized-practice line for letter drafting in the launch state. (2) Whether caseworkers accept the letters and packet (5 real filings). (3) Scan quality, and families without power of attorney (LIFE-17). (4) Families preferring a general assistant. (5) State asset-verification systems already surfacing accounts [UNVERIFIED].

**Notes for the main researcher.** Section 10 can drop "[UNVERIFIED]" on MedicaidSoft (real, attorney channel, $200K prize, "$2 million seed round" mentioned). Section 13 is faster than the bottom-up math supports (about 21 customers by week 8, 100 near week 19); section 11's 93% margin is about 88% with support and infrastructure; no score change proposed.
