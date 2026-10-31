---
id: "014"
slug: iep-ally
name: IEP Ally
one_liner: "Helps parents request IEP evaluations in writing, track legal deadlines, prepare for meetings and keep a dated communication log."
target_user: "Parents of children with disabilities who are seeking or enforcing special-education services"
form_factor: "web app"
lens: "Pain-first"
frontier: false
competition: "CROWDED"
confidence: "LOW"
status: "killed"
signals: [LIFE-51, LIFE-52, REV-38, PRO-202, LIFE-53]
scores:
  pain: 4
  evidence: 2
  ai_leverage: 4
  whitespace: 1
  novelty: 2
  why_now: 3
  solo_feasibility: 4
  distribution: 3
  wtp_economics: 3
  scale_defensibility: 2
total: 57.9
price_hypothesis: "$15/month or $99/year; $12 per tracked certified letter"
model_cost_per_user_month: "$0.47"
gross_margin: "85%"
mvp_weeks: 5
deep_dive: false
red_team: false
---

# IEP Ally

> **Main-thread review, 2026-10-31: KILLED.** CROWDED. Undivided ($19 a month, about $5M raised), Expert IEP and at least five iOS apps launched April to August 2026 cover rights explanations and IEP preparation; only the evaluation-request and deadline-clock slice is open, which is a feature. The file is kept as a record of the competition check.

## 1. One-liner
Helps parents request IEP evaluations in writing, track legal deadlines, prepare for meetings and keep a dated communication log.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 4 | A child's services and a $5,000 to $8,500 lawyer quote (LIFE-51); but the peak is episodic, around evaluations and annual meetings |
| Evidence quality | 2 | 2 | Only LIFE-51 is a direct parent-IEP signal; the other three are adjacent or school-side |
| AI leverage | 2 | 4 | Reading long evaluation reports, comparing them with a draft IEP and drafting letters is model work |
| Whitespace | 2 | 1 | CROWDED: Undivided ($19/month, funded), Expert IEP, and at least five parent apps launched April to August 2026 |
| Novelty of insight | 1 | 2 | "Procedural leverage, not advice" is a good framing, but rivals already track deadlines |
| Why now | 1 | 3 | Models read evaluations cheaply; the 2026 wave of entrants shows timing, and also competition |
| Solo feasibility | 2 | 4 | No school integrations, 5 weeks; state rule accuracy is the hard part |
| Distribution | 2 | 3 | Parent communities and state-specific letter pages; Undivided and free sites hold the head terms |
| Willingness to pay and unit economics | 2 | 3 | Parents pay for help (lawyers, advocates, $19 plans), margin about 85%, but price is capped by Undivided |
| Scale and defensibility | 2 | 2 | A funded incumbent can add the missing features; assistants are free |
| **Total** | | **57.9** | |

Confidence: LOW (thin direct evidence, crowded field). FRONTIER: no.

## 3. The problem
- Who: parents of children with disabilities who need the school to evaluate, write and honor an IEP; they face unfamiliar law, short meetings and paperwork spread across apps and binders.
- Cost: a lawyer quoted $5,000 to $8,500 just to get an evaluation and an IEP meeting (LIFE-51). A parent-facing article claims paid advocates cost up to $14,000 a year (unsourced, [UNVERIFIED], https://www.essence.com/news/money-career/mother-builds-ai-education-app/).
- Workaround: free guides, parent groups, binders and spreadsheets, ChatGPT, or paying an advocate.

## 4. Evidence
Five signals; honest weighting: one direct, four adjacent.
- **LIFE-51** (medium, 2025-11-03, r/SpecialNeeds): "Consult of one I liked and came highly recommended said the entire process of using them , getting school to do eval, IEP meeting would be 5,000-8500." The price a parent is weighing for a procedural job.
- **REV-38** (strong, 2026-09-25, App Store): "So when you think you are caught up, you aren’t. You need to spend a good 20 min per kid looking for posts to see if you can find anything." School information is scattered across apps.
- **LIFE-52** (medium, 2026-10-24, r/EstatePlanning): "I have never used cash, kept receipts, sole use for beneficiary. Have binders of bank statements and receipts." Special-needs families keep paper binders and fear reporting mistakes.
- **PRO-202** (strong, 2025-08-23): a SPED case manager says "I am forced to take excessive paperwork come with me and work for free on my own time, often pushing 60 hours a week." Overloaded staff are why parent follow-up and timelines matter.
- **LIFE-53** (weak, 2026-10-26, r/Mommit): "Papers from school, bills (non-kid related papers I guess?) and the digital messages from apps like parent square. How are we keeping track and where are these things going?!"
- Competitor traction is indirect demand evidence: seven parent products launched or funded (section 10).

## 5. The product
- Finished outcome: a dated, sent and tracked written request that starts the legal clock, then a file that shows what was asked, promised and delivered.
- Core AI loop: parent describes the concern and picks state and district -> model explains the parent's procedural rights from a curated library (federal IDEA text and state rules) -> drafts the written evaluation request in the parent's voice -> sends by email and tracked certified mail -> deadline calendar (federal default 60 days from consent, state variations, [UNVERIFIED]) -> parent uploads the evaluation and the draft IEP -> model summarizes in plain language, flags findings the draft IEP does not address (both quoted) and drafts a meeting agenda and questions -> every email, call and meeting goes into a dated log.
- Interaction: mobile-friendly web app; reminders by email and SMS; share a read-only case file with an advocate or lawyer.
- Day in the life: Priya picks "request an evaluation", reviews the drafted letter, sends it certified. Day 12 the consent form arrives and she logs it; the clock starts. At day 55 the app shows the report is late and drafts a polite follow-up. When the draft IEP arrives it lists three evaluator recommendations the draft omits.
- Liability line: it explains public procedural rights, drafts letters at the parent's direction, tracks dates and organizes documents. It does not predict whether a due-process or state complaint would succeed, does not tell a parent which placement to demand, and does not interpret clinical results as medical advice (plain-language summaries plus "ask the evaluator"). Disputes route to parent training centers, advocates or attorneys.

## 6. Why the LLM is load-bearing
Evaluation reports run 15 to 30 pages of clinical language, IEP drafts vary by district, and letters must fit each family's facts and state. The model reads, compares and drafts. Without it the product is a letter template plus a calendar, which free guides already provide.

## 7. The insight
Most parent leverage comes from written requests and enforced timelines, which are procedural, not legal advice. The honest update: competitors lean on IEP review and navigator conversations. Undivided's pricing page credits its "Andy" assistant with drafting letters (fetch summary), but neither Undivided page I read mentions evaluation requests, certified sending or a legal clock (read 2026-10-31); that narrow gap is the whole wedge.

## 8. Why now, and why this does not exist yet
Models read evaluations for cents and mail APIs are cheap. It partly exists already: five parent apps were released between 2026-04-29 and 2026-08-18, so timing is clear but the window for a first mover is closed.

## 9. Inspiration and derivation
Parents: Undivided (membership plus navigators), Expert IEP (IEP review), Wrightslaw-style rights guides, and tracked-letter flows like those in Paper Trail (ideas/008). Changed: core job (enforce the process, not review the document), interaction (letter, clock and log first), business model (self-serve below $19/month), channel (state-specific request-letter pages).

## 10. Competition check
Queries run (2026-10-31): (1) web "Undivided app parents special needs IEP advocate AI tool pricing"; (2) web "Undivided special needs families platform raises funding founder"; (3) Product Hunt via search, "IEP parents advocate AI evaluation request letter" restricted to producthunt.com (no IEP product); (4) YC directory mirror https://yc-oss.github.io/api/companies/all.json with `IEP|special education|special needs|disabilit|parents of` (no parent IEP company); (5) App Store `--find "IEP special education"` and `--find "IEP parent advocate"` plus iTunes lookups; (6) fetches of Undivided's pricing and features pages and of Expert IEP.

| Product | What it does | Price | Difference |
|---|---|---|---|
| [Undivided](https://www.undivided.io/pricing/) ([features](https://www.undivided.io/features/)) | Parent platform with "AI-powered IEP & 504 Assistant: flag what's missing", a digital binder with deadline tracking and templates, human Navigators; about $5M raised, formerly Special X ([CB Insights](https://www.cbinsights.com/company/special-x)) | Free tier; $19/month or $149/year; Navigator add-ons $68 to $118/month all-in | Closest and funded. Reviews IEPs and advises; drafts some letters; pages do not mention evaluation requests, certified sending or a legal clock |
| [Expert IEP](https://www.expertiep.com/) | Upload the IEP, check for missed supports, return a revised plan, evaluation quiz | No prices on page; $1.7M raised per [VCBacked](https://www.vcbacked.co/company/expert-iep) ([UNVERIFIED]) | Document review, no letters or clock |
| [IEP Copilot](https://apps.apple.com/us/app/iep-copilot/id6779595376), [IEP Compass](https://apps.apple.com/us/app/iep-compass-parent-advocate/id6761731246), [IEPilot](https://apps.apple.com/us/app/iepilot-understand-iep-504/id6792888841), [IEP Proof](https://apps.apple.com/us/app/iep-proof-parent-advocate/id6793348622), [IEP Tracker - Ally](https://apps.apple.com/us/app/iep-tracker-ally/id6794952669) | iOS apps (released 2026-04-29 to 2026-08-18, 0 to 4 ratings): advocacy guidance, plain-English IEPs, promised-versus-delivered service logs | Free | Tiny, but five in four months; the last one shares the "Ally" name |
| Lawyers and paid advocates | Human representation | $5,000 to $8,500 (LIFE-51) | The anchor; a few parents need them |
| Free guides, parent groups, ChatGPT | Rights information, sample letters | Free | The real default; no mailing, clock or file |

Classification: CROWDED. Platform risk: Undivided can add letter drafting and sending in one release; assistants already draft letters free. Scale capped at 2.

## 11. Business model
- Payer: the parent. Anchors: $19/month Undivided, $5,000+ lawyer. Hypothesis: $15/month or $99/year, tracked certified letter at cost plus a small margin ($12).
- Model cost per active parent per month [ESTIMATE], prices from `research/LANDSCAPE.md`: 1.5 evaluation-versus-IEP comparisons on Sonnet 5.5 at 35,000 in + 3,000 out = $0.07 + $0.03 = $0.10 each, $0.15; 4 letters at 4,000 in + 1,000 out = $0.018, $0.072; log parsing on Haiku 5.5, 20 events x $0.00035 = $0.007; one agenda at 8,000 in + 1,500 out = $0.031; 30 chat turns with 20,000 cached tokens at $0.10/1M, 500 new in, 400 out = $0.002 + $0.001 + $0.004 = $0.007 each, $0.21. Total about $0.47.
- Margin at $15: payment fee 2.9% + $0.30 = $0.74; support allowance $1.00 [ASSUMPTION]; ($15 - 0.47 - 0.74 - 1.00) / $15 = 85%.

## 12. Market size
[ESTIMATE] About 7.5M US students get IDEA services [UNVERIFIED, from memory], roughly 7.0M households; assume 10% are in an active evaluation or dispute year [ASSUMPTION] = 700k x $99 = $69M a year. At 2% = 14k families = about $1.4M a year.

## 13. Go-to-market
- First 100 customers: state-specific "request a special-education evaluation" letter pages (5 states first) as free tools; helpful answers in r/specialed and r/SpecialNeeds (where LIFE-51 appeared); parent advocacy groups and parent training centers [UNVERIFIED which] that share a free letter tool; 40 SEO, 40 community, 20 advocate referrals.
- Growth loop: advocates and lawyers receive the read-only case file, a clean dated log that helps their work, and recommend it to the next family.

## 14. Moat and scale path
State rule library, dated evidence logs families keep for years (the annual cycle gives retention), and advocate white-labeling. Scale: 504 plans, early intervention, college accommodations. Honest: a funded rival can copy the wedge.

## 15. Solo feasibility
- MVP, 5 weeks: state rules and letter generator for 5 states with calendar (weeks 1-2), document upload and plain-language summary (3), IEP-versus-evaluation comparison (4), tracked mail and payments (5).
- Running cost before revenue about $50 a month. Hardest risk: state-by-state rule accuracy and reliable reading of long evaluation PDFs; child data is sensitive (encrypt, minimize, no training on user data).

## 16. Pre-mortem
1. Crowded: Undivided has the brand, navigators and funding; five new apps and free assistants squeeze price and attention.
2. One-shot usage: once the evaluation request is sent, parents churn; only the annual cycle brings them back.
3. Advice line: a wrong deadline or an overreaching rights statement could harm a child's services, and legal review costs money.

## 17. Cheapest validation test
3 weeks, about $50 and 20 hours. Ship the state-specific evaluation-request letter plus deadline calendar for 5 states free, announce it in two parent communities. Pass: 150 letters generated and at least 10% of generators pay $19 for tracked certified send-and-follow within 14 days. Fail below 5%: kill, or fold the letter and clock into a broader family-paperwork product.

## 18. Open questions
- Does Undivided already draft evaluation requests or track the legal clock inside its binder or "Andy"? Check the live product before building.
- Rename: "IEP Tracker - Ally" is a live iOS app (released 2026-08-18).
- Is the parent side defensible at all, or is the school side (ideas/013) or a broader family-mail product a better home?
- Recommendation: CROWDED, so test only the 5-state letter-and-clock wedge; do not build a general parent IEP assistant.
