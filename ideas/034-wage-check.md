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
  evidence: 2
  ai_leverage: 3
  whitespace: 3
  novelty: 3
  why_now: 3
  solo_feasibility: 3
  distribution: 3
  wtp_economics: 1
  scale_defensibility: 2
total: 51.6
price_hypothesis: "Free first audit; $19 per claim packet; $199/month per worker center"
model_cost_per_user_month: "$0.12 per audit ($0.19 with a claim packet)"
gross_margin: "80%"
mvp_weeks: 7
deep_dive: true
red_team: true
---

# Wage Check

## 1. One-liner
Workers upload pay stubs, timecards and gig statements and get a pay-discrepancy report, inquiry draft and labor-agency claim packet.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | Small amounts every pay period for people with little slack; but workers ask rather than pay or hack |
| Evidence quality | 2 | 2 | 5 recent signals, all medium; none states willingness to pay Red team: 3 to 2, red team: only one of five signals is a US employee wage-law question |
| AI leverage | 2 | 3 | Model reads messy stubs and screenshots and drafts; the pay math must be deterministic code |
| Whitespace | 2 | 3 | ADJACENT ONLY: hours trackers, a form filler and hackathon prototypes; no real audit product found Red team: 4 to 3, red team: Reclamo AI and OvertimeLaw.ai are free purpose-built wage checkers |
| Novelty of insight | 1 | 3 | Documentable small repeated amounts; the evidence file may matter more than the dollar figure |
| Why now | 1 | 3 | Cheap screenshot reading and Spanish voice; no regulatory trigger |
| Solo feasibility | 2 | 3 | 7 weeks, but rules across states and local ordinances plus trust are hard |
| Distribution | 2 | 3 | Worker subreddits, worker centers and legal aid are reachable; calculator SEO is held by big sites |
| Willingness to pay and unit economics | 2 | 1 | Workers will not pay much; lawyer-referral revenue may be restricted; worker centers have thin budgets Red team: 2 to 1, red team: payer still unidentified; break-even needs 1.4% of free users to buy |
| Scale and defensibility | 2 | 2 | Small market, low lock-in; assistants compute overtime from pasted stubs |
| **Total** | | **51.6** | |

Confidence: LOW (the payer is unproven). FRONTIER: no.

Red-team adjustment (main researcher, 2026-11-01): whitespace 4 to 3 (red team: Reclamo AI and OvertimeLaw.ai are free purpose-built wage checkers); evidence quality 3 to 2 (red team: only one of five signals is a US employee wage-law question); willingness to pay and unit economics 2 to 1 (red team: payer still unidentified; break-even needs 1.4% of free users to buy).

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

## Deep dive

Added 2026-11-01. New facts were read 2026-11-01; "idea file" means sections 10 to 12 above (read 2026-10-31). The payer is the crux, so each part below tests who pays. Search-summary means I saw the fact only in a search result summary, not on the page.

### Competitor table
| Competitor | Link | What it does | Price (as published, with date read) | Funding or traction (sourced) | Gap this idea exploits |
|---|---|---|---|---|---|
| Reclamo AI (Justicia Lab with NYLAG), NEW | [NYLAG](https://nylag.org/justicia-lab-and-new-york-legal-assistance-group-launch-new-chatbot-reclamo-ai-to-help-new-yorkers-understand-and-address-wage-theft/) (403 to my fetch), [Brooklyn Reader](https://www.bkreader.com/non-profit-community/new-workers-rights-ai-tool-combats-wage-theft-in-new-york-11775997) | Wage-theft chatbot for New York workers: check pay, report wage theft, employer violation lookup, links to pro bono lawyers and advocates; WhatsApp or browser, text or voice, 50+ languages (search-summary of press copy) | Not published [UNVERIFIED] | Launched early 2026 with a legal-aid nonprofit (NYLAG) as partner; no usage numbers found | Chat and intake. A stub analyzer was not confirmed. Open: stub and timecard reading, state pay math, dated evidence file. Also a free-price anchor and a possible partner |
| Labor agencies (California Labor Commissioner, US DOL Wage and Hour Division) | [California page](https://www.dir.ca.gov/dlse/HowToFileWageClaim.htm), [DOL release](https://www.dol.gov/newsroom/releases/whd/whd20260108) | Take claims online, by email, mail or in person; ask for paystubs and hours "if you have them available" (CA page, April 2024) | Fee not stated on the California page (read 2026-11-01); free [UNVERIFIED] | WHD FY2025: more than $259M back wages for 176,957 workers, about $1,465 each (DOL release, search-summary) | The destination, not a rival. Workers arrive without organized records |
| US DOL timesheet app | [DOL](https://www.dol.gov/newsroom/releases/whd/whd20220630) | Worker keeps own log of hours, breaks, overtime | Free (idea file) | Not published | No stub reading, no discrepancy check, no packet |
| Instafill.ai | [Instafill](https://instafill.ai/forms/new-york-state-department-of-labor-division-of-labor-standards-complaint-form-ls-223) | AI fill of the NY labor complaint form (LS 223) | Not found (idea file) | Not found | Form only; no pay math or evidence table |
| WageGuard, JornadaJusta NEW, equilaw, wage CALC NEW | [WageGuard](https://devpost.com/software/wageguard), [JornadaJusta](https://devpost.com/software/jornadajusta), [equilaw](https://github.com/mandu5/equilaw), [wage CALC](https://gust.com/companies/wage-calc) | Hackathon or open-source stub scanners and calculators; JornadaJusta lists voice intake and 50-state pay comparison, with the photo reader planned (search-summary); wage CALC targets law firms, listed "In Development" | Free / not published | No traction found | Prototypes; none is a service with state rules, Spanish and an evidence file |
| Gridwise, Driver's Seat Cooperative | [Gridwise](https://gridwise.io/features/earnings), [Driver's Seat](https://app.dealroom.co/companies/driver_s_seat_cooperative) | Gig earnings, mileage, pay benchmarks | Not found (idea file) | Not verified | Tax and transparency, not underpayment claims |
| iOS hours trackers Work Log, atWork | [Work Log](https://apps.apple.com/us/app/work-log-shift-tracker/id1578126960), [atWork](https://apps.apple.com/us/app/hours-pay-tracker-atwork/id857189697) | Manual shift logging and pay estimates | Free to paid (idea file) | 4,535 and 3,836 App Store ratings (idea file) | Manual entry; no check against stubs |
| Tapcheck (earned wage access) | [Tapcheck](https://apps.apple.com/us/app/tapcheck-on-demand-earnings/id1482944292) | Advances pay | Fees (idea file) | Not verified | Different job |
| Wage-and-hour plaintiff firms | none | Take larger or collective claims on contingency | Contingency [UNVERIFIED] | n/a | Destination for big cases; an average federal recovery of $1,465 is likely too small for them [ASSUMPTION] |
| ChatGPT, Claude, Gemini | none | Compute overtime from pasted numbers | Free tiers exist (idea file) | n/a | No intake of messy images in two languages, no state rule library, no evidence file |

### Market sizing (bottom-up)
- Counts: 80.3M US workers were paid hourly in 2024, 55.6% of wage and salary workers, 760,000 of them below the federal minimum ([BLS](https://www.bls.gov/opub/reports/minimum-wage/2024/home.htm), search-summary). This replaces the idea file's unverified 80M. Cross-check: WHD FY2025 recovered for 176,957 workers (federal only).
- Path A, workers pay $19 per packet. Conservative: 80.3M x 3% suspect a problem = 2.41M; x 0.4% buy = 9,636 x $19 = $0.18M (5% of WHD's recoveries). Optimistic: 80.3M x 8% = 6.42M; x 1% = 64,240 x $19 = $1.22M (36% of WHD's recoveries, a stretch). Rates are [ASSUMPTION].
- Path B, organizations pay $199 a month ($2,388 a year). Universe about 1,050 [ESTIMATE: 250 worker centers + 300 legal-aid employment units + 500 union locals; no source found]. Conservative 3% = 32 x $2,388 = $0.08M; optimistic 10% = 105 x $2,388 = $0.25M. Reclamo AI being free pushes this price down.
- Path C, lawyers (counsel-gated, excluded from totals): 1.37M US lawyers in 2025 ([ABA Profile via TaxProf Blog](https://taxprofblog.aals.org/2025/12/10/aba-profile-of-the-legal-profession-number-of-lawyers-increase/), search-summary) x 0.5% on the plaintiff side [ASSUMPTION] = 6,850; a flat $199 monthly listing at 1% to 3% adoption = 68 to 206 x $2,388 = $0.16M to $0.49M.
- Serviceable market (A plus B): conservative $0.26M, optimistic $1.47M a year ($1.96M with C). A mission-sized business unless one payer proves out.
- Revenue at 100 / 1,000 / 10,000 customers: packet buyers $1,900 / $19,000 / $190,000 (10,000 is 16% of the optimistic pool); organization seats $238,800 / $2.39M (the whole assumed universe) / not reachable.

### Unit economics
Per month for one free user, then one paying user. Prices from `research/LANDSCAPE.md` section 6. All [ESTIMATE].
- Free audit, model: read 12 images on Haiku 5.5, 18,000 in x $0.10/1M + 2,000 out x $0.50/1M = $0.0018 + $0.0010 = $0.0028; map to rules on Sonnet 5.5, 10,000 x $2/1M + 2,000 x $10/1M = $0.040; inquiry draft, 4,000 x $2/1M + 1,000 x $10/1M = $0.018; 10 chat turns, each 8,000 cached x $0.10/1M + 500 x $2/1M + 400 x $10/1M = $0.0058, so $0.058. Model total $0.1188.
- Free audit, other: 3 voice notes x 1.5 min x $0.003 = $0.0135; 6 texts x $0.008 = $0.048 [ASSUMPTION on SMS price]; infrastructure $60 a month / 1,000 audits = $0.06. Free user total $0.240.
- Paid packet add-on: model 20,000 x $2/1M + 3,000 x $10/1M = $0.070; payment fee $19 x 2.9% + $0.30 = $0.851; support $0.50; counsel review $400 / 1,000 packets = $0.40 [ASSUMPTION]. Add-on $1.821. A paying user costs $0.240 + $1.821 = $2.06, margin (19 - 2.06) / 19 = 89%.
- Blended per 1,000 free audits: 5% buy = 50 x $19 = $950 revenue, cost $240 + 50 x $1.821 = $331, margin 65%; 2% buy = $380 revenue, cost $277, margin 27%; 1% buy loses money. Break-even conversion = $240 / ($19 - $1.821) = 1.4%. The file's 80% margin ignored SMS, voice, infrastructure and counsel.
- Organization plan, $199 a month: 40 intake audits x $0.240 = $9.61 + 10 packets x $0.07 = $0.70 + fee $6.07 = $16.38, margin 92%. The real cost is about 3 hours of founder onboarding per organization.
- Heavy user (12 months of records, 60 images, 40 chat turns): vision $0.012 + mapping $0.18 + draft $0.018 + chat $0.232 + packet $0.14 = $0.58. Pricing cap: the $19 packet covers one case up to 60 images and 40 chat turns; a second case needs a second packet; one free audit per phone number.

### First 100 customers
Funnel [ESTIMATE]: visit to started upload 15%; started to finished audit 50%; finished to "possible discrepancy" 30% (the file's pass bar is 25%); flagged to $19 packet 15%. Visit to paid = 0.15 x 0.5 x 0.3 x 0.15 = 0.34%. Organizations: 15 individual emails a week, 20% reply, 25% of replies accept a free 30-day pilot, 30% of pilots pay.
| Week | Channel and action | Message and offer | Visitors | Paid (cumulative, incl. orgs) |
|---|---|---|---|---|
| 1 | Ask mods first, then one guide post each in r/AmazonDSPDrivers and r/AmazonFlexDrivers (where UND-37 and UND-40 appeared) | "How to check your timecard and payout against what you worked." Free audit, $19 packet, maker disclosed | 600 | 2 |
| 2 | Spanish landing page and Spanish search pages ("me descontaron el almuerzo y no lo tomé"); ask Spanish-serving worker centers to share the free check (UND-42 is a Mexico-law thread in r/mexico, so do not post there) | "Revisa si te pagaron tus horas extra." Same offer | 900 | 5 |
| 3 | 15 emails to worker centers and legal-aid employment units found through LawHelp.org state pages and their own sites | "A first-pass discrepancy sheet and evidence table for your intake staff; your staff reviews it." Free 30-day pilot, then $199 a month | 1,200 | 9 |
| 4 | Search pages on intent queries: "manager edited my timecard unpaid lunch", "Amazon Flex blocks not paid", "overtime with lunch deducted" | Same free audit | 1,500 | 14 |
| 5 | One how-to-read-your-stub guide per payroll or gig platform; second email batch | Same | 2,000 | 21 |
| 6 | First pilot results as an anonymized case note with the organization's consent | Pilot to paid | 2,500 | 30 |
| 7 | Other gig-worker communities, rules permitting | Same | 3,000 | 41 |
| 8 | Review funnel; fix the leakiest step | Same | 3,500 | 53 |
Base case: 15,200 visitors, 1,140 finished audits, 51 packets and 2 organizations = 53 paying by week 8; 100 around week 12 if weekly visitors reach 4,000. Pessimistic (one third of the traffic) reaches 100 only after week 20, which is the signal to stop B2C and go organization-only.
- Lawyer-money rules check (not legal advice; counsel confirms before any lawyer revenue). ABA Model Rule 7.2(b) bars giving "anything of value" for a recommendation, with room to pay lead generators that do not recommend the lawyer, subject to fee-division and independence rules 1.5(e) and 5.4 ([Rule 7.2 comment text](https://www.courtrules.net/new_hampshire/new-hampshire-professional-conduct/rule-7-2), search-summary). The ABA Journal (2012-08-06) says the generator "should not vouch for the lawyer's credentials or abilities" ([article](https://www.abajournal.com/news/article/online_marketing_including_lead_generation_is_addressed)). States differ: New York treats paying a website for a referral as improper ([NYSBA Opinion 1267](https://nysba.org/?p=170984), title and search-summary only). So v1 takes no lawyer money, names no firm, and never takes a share of a recovery. The one structure worth a counsel hour later is a flat, non-contingent directory fee, with the product neutral.
- Growth loop after 100: workers who recover money tell coworkers (a delivery station is a closed group); one stub guide per platform ranks in search; organizations reuse the same packet and bring their clients.

### One-week validation test (under $50)
- Build (days 1 to 2): one static page headed "Wage Check, pre-launch, not live". It shows a sample report on fictional data (labeled fictional) and three actions: free-check waitlist (Google Form: contact, state, employer type), "reserve the $19 claim packet" (Stripe Payment Link, fully refundable until it ships, said on the page), and "request a free 30-day pilot" for organizations. It collects no pay records this week.
- Post (days 3 to 6): only where a moderator agrees, one post in each of the two subreddits above ("I am building this; nothing is live; waitlist is free"). Send 12 individually written emails to publicly listed contacts (4 worker centers, 4 legal-aid employment units, 4 union-local member-service offices), in two batches. No other outreach; no accounts but my own.
- Day 7: tally and refund reservations if stopping.
- Budget: domain $12 [ASSUMPTION]; hosting, form, email list and analytics on free tiers $0; Stripe fees on up to 3 refunded reservations 3 x $0.851 = $2.55 [ASSUMPTION: fees are not returned]. Total about $15, hard cap $50. The $200 to $400 employment-lawyer hour is the gate before any real audit and sits outside this test.
- Valid only if the page gets at least 200 unique visitors (fewer: extend one week, do not decide).
- Worker arm: pass = at least 20 waitlist entries (10%) and at least 3 paid reservations (1.5%); 1 to 2 reservations = weak, retest at $9; 0 = B2C fails.
- Organization arm: pass = at least 3 replies and 2 booked calls from the 12 emails; on each call ask who holds the budget, whether they would pay $99 to $199 a month after a pilot, and whether they would sign a one-line letter of intent. 0 replies by day 7 = inconclusive (nonprofits are slow), extend to day 14.
- Overall pass = either arm passes and at least one named payer states a budget line. Fail = 0 reservations at 200+ visitors and 0 booked calls by day 14.

### Build brief (paste into a coding session)
- Product summary: Workers upload pay stubs, timecards and gig earnings screens. The app extracts hours and pay, checks them against published federal and three state rules with deterministic code, and returns a "possible discrepancy" report, a payroll inquiry draft and a dated claim packet. Spanish and English; a free first audit; $19 for the packet.
- MVP features (each testable):
  1. Upload up to 15 images or PDFs; extraction of period, hours, rate, deductions, tips with per-field confidence; the user corrects fields (accuracy on a 30-document gold set).
  2. Hours reconstruction form plus voice note in English or Spanish, stored apart from the records.
  3. Rules engine in code: federal overtime over 40 hours, minimum wage, unpaid meal-break deductions, then three states, each rule set versioned with source URL and effective date (25 worked examples to the cent).
  4. Report with line-by-line math, the rule cited, and the label "possible discrepancy based on the records you uploaded".
  5. Payroll inquiry draft in English or Spanish; the user edits and sends it; the app never sends.
  6. Claim packet PDF: evidence table, SHA-256 hash and upload time of each file, agency filing steps and retaliation warning; first page free, export $19.
  7. Share to a worker center or legal-aid account by a consent toggle; organization intake queue.
  8. Stripe Checkout for the packet and the $199 monthly organization plan.
  9. Delete-my-data button; default 30-day retention; warning not to use employer devices.
- Non-goals: legal advice; exempt or contractor decisions; damages, willfulness or outcome predictions; sending or filing for the worker; lawyer referral or any lawyer payment; employer-side tools; native apps; payroll-system integrations; stub authenticity checks beyond hashing (mark everything "user-supplied, unverified").
- Core AI loop: images and voice in -> Haiku 5.5 vision extraction into a JSON schema -> user confirms fields (checkpoint 1) -> rules engine computes expected pay in code, never the model -> Sonnet 5.5 explains the result and drafts the inquiry and packet text from the computed figures only -> low-confidence or refused cases go to a manual review queue (checkpoint 2) -> every rule module and template is reviewed by an employment lawyer before launch (checkpoint 3). Voice: gpt-4o-mini-transcribe at $0.003 a minute.
- Data model: User, Case, Document (hash, storage path), ExtractedPeriod, HoursEntry, RuleSet (jurisdiction, version, effective dates, source URL), Calculation, Finding, Draft, Packet, OrgAccount, Share, AuditLog.
- Integrations (docs): [Anthropic API](https://docs.anthropic.com/), [OpenAI speech-to-text](https://platform.openai.com/docs/guides/speech-to-text), [Stripe Checkout](https://docs.stripe.com/payments/checkout), [Twilio SMS](https://www.twilio.com/docs/messaging), [Supabase](https://supabase.com/docs); rule sources: [DOL FLSA](https://www.dol.gov/agencies/whd/flsa) and each state agency page. No payroll APIs in v1.
- Stack (about $120 a month [ASSUMPTION: vendor prices not checked]): Next.js on Vercel, Supabase (Postgres, phone-OTP auth, private storage), Stripe, Twilio, Resend, Inngest or pg_cron for jobs, react-pdf for PDFs, Sentry and PostHog free tiers, model spend about $60.
- Evals: (1) extraction on 30 documents (10 stubs in 5 formats, 10 gig screens, 10 handwritten or app timecards): at least 95% field accuracy before edits. (2) Rules: 25 of 25 worked examples exact. (3) UND-37 scenario: 5 shifts with a 30-minute lunch deducted but not taken give 2.5 unpaid hours, cite the rule, say "possible discrepancy", and never say "illegal" or "you are owed" (string test over 20 runs). (4) Boundary probes ("Am I exempt?", "Should I sue?", "How much will I win?"): decline and point to the agency or legal aid, 20 of 20. (5) Spanish: 10 voice notes, hours match in at least 9; the Spanish inquiry passes a bilingual reviewer.
- Build plan (7 weeks): W1 schema, auth, storage, extraction with confirmation UI; W2 five timecard and gig formats, gold-set harness; W3 rules engine (federal) with DOL examples; W4 three state modules and the report page; W5 inquiry, packet PDF, Stripe; W6 Spanish voice, SMS, organization view; W7 boundary tests, retention and delete, lawyer review, soft launch.
- Key risks to test first: (1) the payer (the test above); (2) one state's rules checked by an employment lawyer; (3) extraction on handwritten timecards; (4) whether workers will upload records at all; (5) edited or forged stubs and retaliation fear.

Notes for the main researcher: Reclamo AI (Justicia Lab with NYLAG, early 2026) is a direct rival with a legal-aid nonprofit partner that section 10 missed, so Whitespace 4 looks generous (I would say 3) and the free-price anchor makes the organization arm harder. Federal data now give an average recovery of $1,465 per worker, so a $19 packet is 1.3% of an average recovery, but that is still a worker-pays model with no stated willingness to pay. Keep WTP at 2 until a payer shows up in the test. UND-42 is a Mexico-law thread (r/mexico), so it supports the Spanish need but not US demand.

## Red team
Skeptical-investor review on 2026-11-01 (full text: `research/RED_TEAM_B.md`). Verdict: **pass**.

**Top attacks (summarized):**
1. **Every route to a payer is free or restricted.** Reclamo AI (Justicia Lab with NYLAG) and OvertimeLaw.ai (new) check wages free; workers would need to convert at 1.4% of free audits to a $19 packet to break even; lawyer-lead money sits behind referral-fee rules.
2. **The one on-target signal asks the question the product must not answer.** Only UND-37 is a US employee asking about wage law ("Isn't this illegal?"), and the product must never say "illegal"; the other signals are app, gig or Mexico-law issues.
3. **Liability lives in the copy.** The FTC's DoNotPay order shows "AI lawyer" claims draw action without a licensing finding, and an inquiry telling payroll the worker is owed money is legal-adjacent output for retaliation-sensitive users.
What would change the red team's mind: a worker center, legal-aid unit, union local or city labor office signing a paid pilot at $99+ a month, or 3 paid $19 packets from 200 visitors, plus counsel clearing the copy.

**Response (main researcher):**
- All three attacks land. Whitespace drops from 4 to 3 (free purpose-built wage checkers exist), evidence from 3 to 2 (one on-target US signal), and willingness to pay from 2 to 1 (no payer identified).
- What survives: the pain is real and recurring, and an institution-paid model (worker centers, unions, city labor offices funding seats) is the only plausible business; test that first or drop the idea.
