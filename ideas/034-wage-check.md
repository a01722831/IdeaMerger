---
id: "034"
slug: wage-check
name: Wage Check
one_liner: "Workers upload pay stubs, timecards and gig statements and get a pay-discrepancy report, inquiry draft and labor-agency claim packet."
target_user: "Hourly, delivery and gig workers who suspect unpaid hours, overtime or missing payouts"
form_factor: "web app"
lens: "Underserved users"
frontier: false
competition: "ADJACENT ONLY"
confidence: "LOW"
status: "developed"
signals: [UND-37, UND-38, UND-40, UND-42, UND-34]
scores:
  pain: 3
  evidence: 3
  ai_leverage: 3
  whitespace: 4
  novelty: 3
  why_now: 3
  solo_feasibility: 3
  distribution: 3
  wtp_economics: 2
  scale_defensibility: 2
total: 57.9
price_hypothesis: "Free first audit; $19 per claim packet; $199/month per worker center"
model_cost_per_user_month: "$0.12 per audit ($0.19 with a claim packet)"
gross_margin: "80%"
mvp_weeks: 7
deep_dive: false
red_team: false
---

# Wage Check

## 1. One-liner
Workers upload pay stubs, timecards and gig statements and get a pay-discrepancy report, inquiry draft and labor-agency claim packet.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | Small amounts every pay period for people with little slack; but workers ask rather than pay or hack |
| Evidence quality | 2 | 3 | 5 recent signals, all medium; none states willingness to pay |
| AI leverage | 2 | 3 | Model reads messy stubs and screenshots and drafts; the pay math must be deterministic code |
| Whitespace | 2 | 4 | ADJACENT ONLY: hours trackers, a form filler and hackathon prototypes; no real audit product found |
| Novelty of insight | 1 | 3 | Documentable small repeated amounts; the evidence file may matter more than the dollar figure |
| Why now | 1 | 3 | Cheap screenshot reading and Spanish voice; no regulatory trigger |
| Solo feasibility | 2 | 3 | 7 weeks, but rules across states and local ordinances plus trust are hard |
| Distribution | 2 | 3 | Worker subreddits, worker centers and legal aid are reachable; calculator SEO is held by big sites |
| Willingness to pay and unit economics | 2 | 2 | Workers will not pay much; lawyer-referral revenue may be restricted; worker centers have thin budgets |
| Scale and defensibility | 2 | 2 | Small market, low lock-in; assistants compute overtime from pasted stubs |
| **Total** | | **57.9** | |

Confidence: LOW (the payer is unproven). FRONTIER: no.

## 3. The problem
- Who: hourly employees, delivery drivers, home-care aides and gig workers whose paid hours, overtime, lunches or payouts do not match what they worked.
- Frequency and cost: every pay period, in small repeated amounts. Examples: a manager asking a driver to edit a timecard to show an unpaid lunch (UND-37), five completed blocks with no payment (UND-40), glitchy EVV sign-outs that lower aides' pay (UND-34).
- Workaround: ask on Reddit, call payroll, screenshot everything, or give up. Lawyers and agencies exist but need organized records [UNVERIFIED which fees apply].

## 4. Evidence
Five independent signals (four dated 2026-10, one 2025-08), all medium.
- **UND-37** (medium, 2026-10-30, r/AmazonDSPDrivers, 35 comments): "My manager just told me to edit my timecard to show I took a lunch even though I told him I didn’t take one and he said it’s unpaid. Isn’t this illegal?" The question the product answers first.
- **UND-40** (medium, 2026-10-27, r/AmazonFlexDrivers): "I’ve completed a total of five blocks since October 18, and I haven’t seen a dime of payment from any of those blocks." Payout reconciliation, a gig-specific case where wage law may not apply.
- **UND-38** (medium, 2026-10-26, App Store): "The app has changed recently and we are unable to access the actual full pay check stub. Phones do not have storage capability to download another reader that bloats the phone." Workers cannot easily get their own records.
- **UND-34** (medium, 2025-08-18, App Store, EVV app): "This app reflects on your pay. One mistake and you will have a lower pay because this dumb app is glitchy." Systems errors become pay errors.
- **UND-42** (medium, 2026-10-28, r/mexico, 32 comments): "Pregunto porque en mis 30 y tantos años de vida, no conozco a nadie que sí se las paguen o se las cuenten" [I ask because in my 30-something years of life I do not know anyone who actually gets them paid or even counted]. Overtime is invisible, and Spanish matters.
- Gap: nobody says they would pay; two signals are contractor or app issues, not employee wage claims.

## 5. The product
- Finished outcome: a worker learns in minutes whether the records show a discrepancy, and leaves with a message to payroll and an organized claim file.
- Core AI loop: upload pay stubs, schedule or timecard screenshots, gig earnings screens, bank deposits, plus voice notes in English or Spanish -> vision model extracts periods, hours, rates, deductions, tips -> model reconstructs hours worked from records and the worker's account -> a deterministic rules engine (federal overtime and minimum wage, then a few states) computes expected pay -> discrepancy report with line-by-line math and a confidence label -> model drafts a polite payroll inquiry and, if the worker chooses, fills the state labor-agency complaint form and builds a dated evidence table -> worker can export or share with legal aid or a worker center.
- Interaction: mobile-first web, text-message follow-ups, Spanish and English; uploads hashed so the file's date and content can be shown later.
- Day in the life: Marcus, a delivery driver, uploads two weeks of pay screens and his schedule. The report shows 6.5 hours worked through unpaid lunches across four shifts and the math under his state's rules, labels it "possible discrepancy", and drafts a two-sentence message to payroll. He decides whether to send it.
- Liability line: arithmetic and documentation under published rules. It does not decide exempt status, contractor misclassification, willfulness or damages, does not predict outcomes, and does not advise whether to sue. Reports say "possible discrepancy based on the records you uploaded" with the rule cited. It gives public information about filing and about retaliation protections, warns not to use employer devices, and refers to the agency, legal aid or an attorney. Lawyer-referral money needs counsel first (rules on paying for referrals vary, [UNVERIFIED]).

## 6. Why the LLM is load-bearing
Pay records are screenshots and PDFs from hundreds of payroll and gig systems, and the worker's story is unstructured, often in Spanish. The model turns that into structured hours and plain-language messages. Without it the worker types everything into a calculator, which is what the existing overtime calculators and hours trackers already ask.

## 7. The insight
Wage theft is small, repeated and documentable from records workers already hold. Honest add: the durable asset may be the clean, dated evidence file that an agency or lawyer can use, not the dollar estimate; and the hard problem is who pays for it, not whether it works.

## 8. Why now, and why this does not exist yet
Reading arbitrary screenshots and speech in two languages now costs cents. It does not exist as a product because workers do not pay, lawyers handle volume cases themselves, and the rules are messy; the only visible attempts are a hackathon project (WageGuard), an open-source calculator and form fillers.

## 9. Inspiration and derivation
Parents: the Department of Labor's timesheet app, Gridwise-style earnings trackers, Instafill-style form fillers, TurboTax-style free-to-start flows. Changed: target user (low-wage and gig workers), core job (find the discrepancy and build the file, not track hours), business model (free first audit with B2B2C), channel (worker communities, worker centers).

## 10. Competition check
Queries run (2026-10-31): (1) web "app upload pay stubs timecards check unpaid overtime wages owed AI wage theft claim labor department"; (2) Product Hunt via search, "wage theft unpaid overtime workers pay check" restricted to producthunt.com (employee-monitoring tools only); (3) web "gig driver earnings audit app unpaid pay discrepancy Amazon Flex DoorDash Uber underpaid tracker Driver's Seat Gridwise Worker Info Exchange"; (4) YC directory mirror https://yc-oss.github.io/api/companies/all.json with `wage theft|unpaid wages|overtime|wage and hour|worker rights|paystub|timecard|gig workers|hourly workers` from 2021 (no wage-claim company; Dayra and Veltha are unrelated); (5) App Store `--find "wage theft overtime pay"` and `--find "paycheck wage claim"`.

| Product | What it does | Price | Difference |
|---|---|---|---|
| [US Department of Labor timesheet app](https://www.dol.gov/newsroom/releases/whd/whd20220630) ([2011 coverage](https://www.nbcnews.com/id/wbna43128963)) | Tracks hours, breaks and overtime and calculates wages due | Free | Worker keeps their own log; no stub reading, no claim packet |
| [Instafill.ai](https://instafill.ai/forms/new-york-state-department-of-labor-division-of-labor-standards-complaint-form-ls-223) | AI fill of the New York labor complaint form (LS 223) | Not found | Form filler only; no pay math |
| [WageGuard](https://devpost.com/software/wageguard) (hackathon), [equilaw](https://github.com/mandu5/equilaw) (open source) | Pay-stub scan for violations; unpaid wage calculator and complaint draft | Free | Prototypes, not services |
| [Gridwise](https://gridwise.io/features/earnings), [Driver's Seat Cooperative](https://app.dealroom.co/companies/driver_s_seat_cooperative) | Gig earnings, mileage and pay benchmarking | Not found | Tax and transparency, not underpayment claims ([Mozilla](https://www.mozillafoundation.org/en/blog/giving-gig-workers-the-transparency-they-deserve/) notes stories of underpayment) |
| iOS hours trackers: [Work Log](https://apps.apple.com/us/app/work-log-shift-tracker/id1578126960) (4,535 ratings), [atWork](https://apps.apple.com/us/app/hours-pay-tracker-atwork/id857189697) (3,836) | Log shifts and estimate pay | Free to paid | Manual entry; no discrepancy check against stubs |
| Earned-wage-access apps ([Tapcheck](https://apps.apple.com/us/app/tapcheck-on-demand-earnings/id1482944292)) | Advance pay | Fees | Different job |
| Wage-and-hour plaintiff firms; state labor agencies | Take claims | Contingency fees; agency claims free [UNVERIFIED] | The destination for a claim, not a competitor |
| ChatGPT, Claude, Gemini | Compute overtime from pasted numbers | Free tiers exist | No document intake, evidence file or form fill |

Classification: ADJACENT ONLY. Platform risk: assistants already compute overtime from a pasted stub; payroll vendors are unlikely to build worker-side audits (conflict with employers); the Labor Department could modernize its app. Moderate; scale capped at 2.

## 11. Business model
- Payer: workers rarely pay. Hypothesis: free first audit; $19 for the claim packet; $199 a month per worker center, legal-aid group or union local for intake triage; lawyer referral only if counsel clears it. Anchor [ASSUMPTION]: workers pay tax-prep and money-transfer fees of $10 to $30 without complaint.
- Model cost per audit [ESTIMATE], prices from `research/LANDSCAPE.md`: read 12 images (2 stubs, 10 screenshots) on Haiku 5.5, 18,000 in + 2,000 out = $0.0018 + $0.001 = $0.0028; map to rules on Sonnet 5.5, 10,000 in + 2,000 out = $0.02 + $0.02 = $0.04; draft inquiry, 4,000 in + 1,000 out = $0.018; 10 chat turns with 8,000 cached tokens at $0.10/1M, 500 new in, 400 out = $0.0008 + $0.001 + $0.004 = $0.0058 each, $0.058. Total about $0.12. Claim packet adds 20,000 in + 3,000 out on Sonnet = $0.07.
- Blended margin per 1,000 free audits [ESTIMATE]: 1,000 x $0.12 = $120 of free cost; 5% buy a packet = 50 x $19 = $950; packet model cost $3.50, payment fees 50 x ($0.551 + $0.30) = $42.55, support $0.50 per packet = $25. Margin = ($950 - 120 - 3.50 - 42.55 - 25) / $950 = 80%. Free-tier abuse must be capped.

## 12. Market size
[ESTIMATE] About 80M US hourly workers [UNVERIFIED, from memory] x 8% who suspect a pay problem and look for help each year [ASSUMPTION] = 6.4M; 10% use a tool = 640k audits; 4% buy a $19 packet = 25.6k x $19 = $0.49M a year. Worker centers and legal aid: 1,000 [ASSUMPTION] x $2,388 = $2.4M; 10% = $0.24M. Lawyer leads, if permitted: 25.6k x 30% accepted x $100 [ASSUMPTION] = $0.77M. About $1.5M a year at these shares; small unless the payer problem is solved.

## 13. Go-to-market
- First 100 users: helpful posts and a free "did I get paid right?" check in worker communities such as r/AmazonDSPDrivers and r/AmazonFlexDrivers (where UND-37 and UND-40 appeared), following each sub's rules; Spanish-language communities (UND-42); worker centers and legal-aid intake pages. Target 300 audits, 100 users who finish, 5 paid.
- Growth loop: shareable, anonymized "how to read your stub" guides per payroll or gig platform; workers who win tell co-workers; worker centers reuse the same packet.

## 14. Moat and scale path
Per-platform parsers (A to Z, Flex, EVV apps, common payroll stubs), a verified rules library by state and city, an anonymized pattern dataset that shows which employers or apps repeatedly shortchange (use carefully), and agency and legal-aid relationships. Scale: employer self-audits (the opposite buyer), unemployment and benefits forms.

## 15. Solo feasibility
- MVP, 7 weeks: uploads and extraction for stubs plus five timecard formats (weeks 1-2), rules engine for federal plus three states with unit tests from published examples (3-4), inquiry and claim packet (5), Spanish and text messaging (6), lawyer review of copy and launch (7).
- Running cost before revenue about $60 a month. Hardest risk: rules correctness across states and local ordinances (tip credits, daily overtime, meal-break premiums), then workers' trust in uploading pay records.

## 16. Pre-mortem
1. No payer: workers will not pay, lawyer referral money may be barred or conflicted, and worker centers have small budgets.
2. Rules and liability: 50 states plus cities, exempt-status gray areas and wrong math both harm trust; unauthorized-practice complaints are possible.
3. Misuse and retaliation fear: fake or edited stubs (see AI2-21 on forged stubs), false claims, or workers punished for filing.

## 17. Cheapest validation test
3 weeks, about $200 for an hour with an employment lawyer on copy plus 30 hours. Ship a free overtime-and-lunch check for federal rules and three states, promoted in worker subreddits. Pass: 300 completed audits, at least 25% showing a discrepancy, and either 15 paid packets or 2 worker-center or legal-aid pilots that agree to pay or provide a letter of intent. Fail otherwise.

## 18. Open questions
- Who pays: workers, worker centers and unions, a city labor-standards office, or the opposite buyer (small employers auditing themselves)?
- Which three states first, and how to handle city rules?
- How to treat gig pay where wage law may not apply (payout reconciliation only)?
- Is a lawyer-referral revenue line allowed where we operate? Ask counsel before building around it.
- Spanish first? Voice-first for low-bandwidth users?
