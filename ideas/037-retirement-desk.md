---
id: "037"
slug: retirement-desk
name: Retirement Desk
one_liner: "A case manager for the year around retirement or turning 65: deadlines, documents, forms, claims and appeals."
target_user: "People retiring or turning 65, plus a spouse or adult child helping, including widowed spouses taking over paperwork"
form_factor: "web app"
lens: "Underserved users"
frontier: false
competition: "ADJACENT ONLY"
confidence: "MED"
status: "developed"
signals: [UND-12, UND-13, UND-19, LIFE-19, LIFE-55, LIFE-29, LIFE-33]
scores:
  pain: 3
  evidence: 3
  ai_leverage: 3
  whitespace: 3
  novelty: 3
  why_now: 3
  solo_feasibility: 2
  distribution: 2
  wtp_economics: 2
  scale_defensibility: 2
total: 51.6
price_hypothesis: "$149 one-time for a 12-month case; free personal deadline calendar"
model_cost_per_user_month: "$0.19 ($2.3 per 12-month case including reminders)"
gross_margin: "95%"
mvp_weeks: 7
deep_dive: true
red_team: true
---

# Retirement Desk

## 1. One-liner
A case manager for the year around retirement or turning 65: deadlines, documents, forms, claims and appeals.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | Permanent penalties for missed windows and a pile of simultaneous tasks, each needing repeated calls; once per person, so not a 5. Calibrated 4 to 3: a once-in-a-lifetime transition; real penalties but free help exists (SHIP counselors) |
| Evidence quality | 2 | 3 | Five strong signals (UND-12, UND-13, LIFE-19, LIFE-55, LIFE-29) plus three new r/medicare threads; nobody states a willingness to pay for case management. Calibrated 4 to 3: five signals, none showing willingness to pay |
| AI leverage | 2 | 3 | The model reads notices, drafts forms and appeals and explains; much of the value is a rules and deadline engine that needs little AI. |
| Whitespace | 2 | 3 | ADJACENT ONLY, but Chapter (funded) sits one step away and free SHIP counselors cover plan advice; vertical-incumbent risk caps this at 3. |
| Novelty of insight | 1 | 3 | Treating the retirement-year admin cluster as one case, not a plan-choice problem, is a useful twist backed by the threads. |
| Why now | 1 | 3 | About 4.1M people turn 65 each year through 2027 and long-context reading is cheap, but the problem is old. |
| Solo feasibility | 2 | 2 | Seven weeks for a timeline engine, document intake and drafting; rules accuracy and yearly upkeep are the hard risk. Red team: 3 to 2, red team: thirty yearly rule modules, licensing check and mixed-notice extraction exceed one hard risk |
| Distribution | 2 | 2 | High-intent search and r/medicare, r/retirement with a free calendar as a lead magnet; one-time and seasonal use; no loop. Red team: 3 to 2, red team: one-time, seasonal, no loop; search dominated by medicare.gov, AARP and lead-gen sites |
| Willingness to pay and unit economics | 2 | 2 | Margin is 95%, but free options (Chapter advisors, SHIP, AARP pages) cover plan choice and I found no price anchor for paperwork help. Calibrated 3 to 2: Chapter anchors the adjacent service at $0 for consumers; no price evidence for paperwork help |
| Scale and defensibility | 2 | 2 | A funded incumbent may extend into seniors' financial products; one-time use; the moat is rules content and employer packets. |
| **Total** | | **51.6** | |

Confidence: MED. FRONTIER: no.

Red-team adjustment (main researcher, 2026-11-01): distribution 3 to 2 (red team: one-time, seasonal, no loop; search dominated by medicare.gov, AARP and lead-gen sites); solo feasibility 3 to 2 (red team: thirty yearly rule modules, licensing check and mixed-notice extraction exceed one hard risk).

Calibration (main researcher, 2026-10-31): pain severity and frequency 4 to 3 (a once-in-a-lifetime transition; real penalties but free help exists (SHIP counselors)); evidence quality 4 to 3 (five signals, none showing willingness to pay); willingness to pay and unit economics 3 to 2 (Chapter anchors the adjacent service at $0 for consumers; no price evidence for paperwork help).

## 3. The problem
- Who: people in the 12 months around retirement or 65, their spouses, adult children, and widowed spouses inheriting a partner's paperwork.
- What collides: HR termination records, COBRA, Medicare and Medigap setup, Social Security, pension forms (one needing a notary), plan exits and denials (UND-12, LIFE-55, UND-13). Claims do not cross over to the Medigap insurer for months (LIFE-19). Benefit notices can suspend payments for unclear reasons (LIFE-29).
- Rules with teeth (per AARP and NCOA pages): the Medicare initial enrollment period is seven months around the 65th birthday month; COBRA does not extend it; missing it can cause a permanent late-enrollment penalty.
- Cost: penalties that never go away, surprise bills, hours of calls, and decisions made in one-time windows.
- Workarounds: AARP and Medicare.gov pages, state SHIP counselors, HR, a broker for plan choice, and an adult child's spare weekends.

## 4. Evidence
- **UND-12** (strong, 2026-10-17, r/retirement, 190 pts / 178 comments): "I had researched everything, knew what I would take from my funds, knew I’d take COBRA, applied for SS, we got husband’s (66m) Medicare and Medigap set up and ready to go, but nothing happened quickly and without multiple phone calls." https://www.reddit.com/r/retirement/comments/1x8kblo/
- **LIFE-19** (strong, 2026-10-28, r/medicare, 66 pts / 69 comments): "I had to call Medicare because no claims were automatically copying over to HealthSpring. After I got Medicare to copy & synch them, 10 claims sat on HealthSpring's portal for months in "Processing" while I'm getting doctor bills for the 20% that Medicare didn't cover (coinsurance amounts)." https://www.reddit.com/r/medicare/comments/1xhzhzp/
- **LIFE-55** (strong, 2026-10-27, r/medicare, 23 pts / 115 comments): "Posting on behalf of my parents. Their Medicare advantage plan will no longer be available in January and for the first time they’ll be able to go back on Original Medicare + Supplement Insurance with no medical underwriting." https://www.reddit.com/r/medicare/comments/1xgt1js/
- **UND-13** (strong, 2026-10-01, r/retirement): "My doctor sent it through twice and it’s still rejected. I asked the pharmacist the over counter price which was $50, so I told them to fill it and I would pay it." https://www.reddit.com/r/retirement/comments/1wv2nan/
- **LIFE-29** (strong, 2026-10-20, r/SocialSecurity, 166 pts / 347 comments): "I just got a notice on my online account that my payments are suspended because either my mailing address is wrong or my payment information is wrong. I don't understand because my mailing address is correct, but the account info is wrong, but they were sending the survivor benefits to the correct account for a few years now." https://www.reddit.com/r/SocialSecurity/comments/1xb6iyf/
- **LIFE-33** (medium, 2026-10-28, r/medicare): "Ended up filling out the form on the "your Texas benefits" web site. Took forever to fill form and upload proof of hopefully everything they needed." https://www.reddit.com/r/medicare/comments/1xi0a6h/
- **UND-19** (medium, 2026-10-16; the signal file says the body looks edited and may be staged, so low weight): "The insurance money is just sitting in savings right now and the bank keeps pushing the annuity. I mostly want to know if I should be in a hurry or not." https://www.reddit.com/r/retirement/comments/1x7ht5c/
- New evidence (not in SIGNALS.md): r/medicare, 2026-10-27, 4 pts / 14 comments: "Wellcare told me in September that I was losing coverage completely, They told me to call SSA I did SSA says I lost my entitlement whatever that means No one can explain what that means" https://www.reddit.com/r/medicare/comments/1xh3ll4/
- New evidence (not in SIGNALS.md): r/medicare, 2026-10-25, 8 pts / 13 comments: "If i do this, the new plan would be effective Jan 1 2027, one day outside of the 6 month MOEP window." The unforgiving-window pattern. https://www.reddit.com/r/medicare/comments/1xfa7u9/
- New evidence (not in SIGNALS.md): r/medicare, 2026-10-12, 30 pts / 40 comments: "he declined Part B for god knows what reason (probably because he didn’t feel like he needed it). Is there any possible way to trigger an enrollment?" https://www.reddit.com/r/medicare/comments/1x46r80/

## 5. The product
- What it does: one personal case for the retirement year. A short interview (birth date, employment and coverage status, spouse, pension, Social Security status) builds a timeline of windows and deadlines (Medicare initial enrollment, COBRA election and end dates, Medigap, Part D, Social Security steps, pension forms, state retiree benefits), each with a plain-language reason and a link to the official page. A document inbox collects HR letters, COBRA notices, Medicare cards, Medicare Summary Notices and EOBs, and pension forms; AI extracts dates and amounts, drafts forms, letters and appeals (for example a Medicare redetermination), tracks claims that sit in "Processing", and writes follow-up call scripts. A widowed-spouse mode lists survivor-benefit and account tasks.
- Core AI loop: interview and documents in -> timeline with citations -> reminders and drafts -> new notices or claims uploaded -> reconcile and re-plan -> hand off to a licensed advisor or SHIP counselor for plan choice and anything advice-like.
- Interaction model: web app with email, text and calendar (ICS) reminders; a spouse or adult child can be added with view or edit rights.
- Form factor: web app.
- Day in the life: Linda, 64, is laid off in March and is offered COBRA. Her timeline shows the seven-month Medicare window around her 65th birthday, notes that COBRA does not extend it, and sets reminders. She forwards the COBRA notice and a pension form; the app flags that the pension form needs a notary and drafts the cover letter. Months later ten Medigap claims sit in "Processing"; the app reconciles them against the Medicare notices and prepares a call script.
- Liability line: published windows and rules with citations, plus organization and drafting. It never recommends a plan, gives tax or investment advice, or tells someone whether to enroll; plan choice is referred to licensed advisors or SHIP.

## 6. Why the LLM is load-bearing
- Notices, HR letters, EOBs and pension forms come in every format; the model reads them, ties each to a window, and answers "what does this mean for me" grounded in the user's documents and the official rules.
- Drafting appeals, election letters and call scripts, and reconciling a pile of "Processing" claims, are language tasks.
- Without the model the product is a static checklist or calendar, and AARP's deadline pages already give those away.

## 7. The insight
- Each step is simple, but they arrive together with unforgiving windows, for a very large cohort every year. People do not need another plan comparison; they need one case that tracks all the pieces and says what comes next.
- Honest limit: it is easy to say "case manager" and hard to prove people will pay, because free plan help (Chapter, SHIP) sits next door.

## 8. Why now, and why this does not exist yet
- Why now: about 4.1M Americans turn 65 each year through 2027 ("Peak 65", Alliance for Lifetime Income via secondary sources [ESTIMATE; no CMS or Census confirmation]), plan exits are pushing adult children into threads like LIFE-55, and reading a document pile costs cents.
- Why not yet: funded AI entrants focus on plan choice, where carrier-paid advisors make the service free. The paperwork, claims and appeals work earns no commission, so nobody is paid to do it.

## 9. Inspiration and derivation
- Parents: guided-interview tax and benefits software, immigration-style case management, Chapter's navigation, AARP's deadline tables.
- Changed: core job (case management across the whole cluster, not plan selection), business model (flat consumer fee, not a carrier commission), user (the retiree, spouse or child, not a broker's lead), channel (search, forums and a free calendar).

## 10. Competition check
Queries run:
1. WebSearch: "turning 65 retirement Medicare enrollment deadlines COBRA checklist app case manager timeline startup"
2. WebSearch (Product Hunt): "site:producthunt.com Medicare enrollment retirement AI advisor" (no Product Hunt pages returned)
3. WebSearch (YC directory): "site:ycombinator.com/companies Medicare advisor AI enrollment retirees"
4. App Store, `scripts/app_reviews.py --find`: "Medicare", "retirement planner timeline" ("Medicare retirement planner" failed)
5. WebSearch: "Chapter Medicare advisors free service licensed advisors paid by carriers commission $100 million raise AI platform lifelong support claims help"
6. WebSearch: "Peak 65 4.1 million Americans turning 65 each year 2026 Medicare enrollment new beneficiaries"; HN "Medicare retirement"; Reddit archive r/medicare and r/retirement.

| Product | What it does | Price | How it differs |
|---|---|---|---|
| [Chapter](https://www.businesswire.com/news/home/20260409159904/en/Chapter-Raises-%24100-Million-Series-E-to-Continue-Building-the-Trust-Layer-Between-Seniors-and-Technology-in-the-Age-of-AI) (Series E, April 2026) | Medicare navigation with licensed advisors and an AI plan-matching system; reported $3B valuation (Dealroom), over $100M ARR claimed for 2025; plans "additional financial products for seniors" | Free to users; advisor pay accounts conflict | Funded; plan choice, no case management found |
| [Healthpilot](https://www.thewealthmosaic.com/vendors/healthpilot/) (Envestnet-backed; about 20,000 retirees), [Hella Health](https://app.dealroom.co/companies/hella_health) | AI plan comparison and enrollment | Advisor or wealth-manager channel | Plan choice |
| [Medicare Vox](https://www.ycombinator.com/companies/medicare-vox-fka-fair-square) (YC W20), [careCycle](https://www.ycombinator.com/companies/carecycle) (YC) | AI health-insurance agent with voice; voice AI for Medicare agencies | B2B or agency | Sell to agencies, not retirees |
| [AARP deadlines](https://www.aarp.org/medicare/medicare-deadlines-timetables/), [NCOA on COBRA and Medicare](https://www.ncoa.org/article/cobra-and-medicare-which-comes-first-and-why-it-matters-at-65/), SHIP counselors ([SHIBA Oregon](https://SHIBA.Oregon.gov/medicare-65/Documents/topten-medicare-myths.pdf)) | Static rules and free human counseling | Free | No documents, claims or personal timeline |
| Apps: [Retirement Countdown](https://apps.apple.com/us/app/retirement-countdown/id1645215938) (12,848 ratings), plan-sponsor retirement apps, CMS [What's covered](https://apps.apple.com/us/app/whats-covered/id1444143600) (362 ratings, 3.2) | Countdown, account portals, coverage lookup | Free | None is a case manager |
| ChatGPT, Claude, Gemini | Build a timeline from a birth date and situation | Subscription | No persistent case, documents or claims tracking |

Classification: **ADJACENT ONLY**. Nothing I found manages the whole retirement-year paperwork end to end. The plan-selection slice is CROWDED and funded, so this product refers it out. My search covered store listings, snippets and funding news only; HR and benefits platforms were not checked.

Platform risk: a vertical incumbent, Chapter, is free to consumers, funded ($100M) and says it will add financial products for seniors, so it could add paperwork and claims help within 12 months. Lab agents with memory (Claude Duet, Gemini tasks) can draft a timeline for free from uploaded documents. Per the rubric this caps Scale and defensibility at 2 and Whitespace at 3.

## 11. Business model
- Payer: the retiree, spouse or adult child. Price: $149 one-time for a 12-month case [ASSUMPTION; no verified anchor for paperwork help]; free personal deadline calendar; optional $29 a year to keep the case for later enrollment periods. No commissions. Flat-fee referral to licensed advisors only where state law permits [UNVERIFIED]. Reference prices: Chapter and SHIP are free, BillFighter charges $39 per medical bill, Medicaid application services about $6K.
- Model cost per 12-month case [ESTIMATE]: 40 documents x (OCR 2 pages x $0.004 + extraction $0.00055) = $0.34; 5 timeline re-plans x (8,000 in x $2/1M + 2,000 out x $10/1M = $0.036) = $0.18; 40 Q&A calls x $0.011 = $0.44; 10 drafts x (6,000 in + 1,500 out) = $0.27; 30 claim documents $0.26 plus 12 monthly reconciliations x $0.03 = $0.36. Total $1.85.
- Other variable [ASSUMPTION]: 60 reminder texts x $0.008 = $0.48. Total about $2.3, or $0.19 a month.
- Gross margin [ESTIMATE]: ($149 - $2.3 - $4.62 Stripe fee) / $149 = 95%.

## 12. Market size
- Buyers [ESTIMATE]: about 4.1M people turn 65 a year through 2027. Assume 40% have a complex transition (employer coverage or COBRA, a spouse, a pension) [ASSUMPTION] = 1.64M a year. Widowed spouses and adult children are extra.
- Revenue: 1.64M x $149 = $244M a year if all bought. Realistic penetration 2% = 33K cases = $4.9M a year.
- Reading: a decent niche with steady inflow, though demand is seasonal around the October 15 to December 7 enrollment season.

## 13. Go-to-market
- First 100 customers: (1) a free "your Medicare and COBRA calendar" generator (birth date and coverage status in, calendar file and PDF out) promoted through search and forums, about 50; (2) answer deadline questions in r/medicare and r/retirement (daily threads such as "Latest month to enroll in Medicare Part B without a penalty"), about 30; (3) adult children posting for a parent (LIFE-55 pattern), about 20.
- SEO targets: "COBRA vs Medicare at 65", "Part B late enrollment penalty", "retiring at 62 health insurance".
- Growth loop: weak. The spouse and adult child co-access, and calendar subscriptions bring return visits.

## 14. Moat and scale path
- Moat: a cited rules and deadline engine, employer and pension-plan packet knowledge that accumulates, and a documented claims history. Modest.
- Scale path: widowed-spouse module, yearly re-enrollment reminders ($29 a year), Social Security claim steps, and employer resale as a retirement-transition benefit (needs partnerships).

## 15. Solo feasibility
- MVP (7 weeks): interview and timeline engine with about 30 rule modules, document inbox and extraction, drafts for letters and appeals, a claims tracker fed by uploaded notices, email and calendar reminders. Reviewed by a licensed advisor or SHIP counselor before launch.
- Running cost before revenue: about $50 to $80 a month.
- Hardest risks: accuracy of rules and their yearly changes (premiums and deductibles update each autumn), and the advice boundary.

## 16. Pre-mortem
1. People will not pay for what free SHIP counselors, Chapter and AARP pages seem to cover.
2. A rule error causes a missed window and a penalty, creating liability and a reputation hit.
3. Chapter, an employer platform or a general assistant adds the same help; one-time seasonal use makes acquisition costs hard to recover.

## 17. Cheapest validation test
- What: publish the free calendar generator and a one-page offer. Send 300 visitors from r/medicare, r/retirement and search; offer a refundable $149 pre-order of the case manager to the first 100 email captures; have a licensed advisor or SHIP counselor spend an hour reviewing the calendar logic.
- Cost: about $0 to $100 plus the review. Duration: 3 weeks.
- Pass: at least 25% of visitors enter their email and at least 3 of the first 100 subscribers pre-order. Fail: no pre-orders, or counselors find the calendar logic unsafe.

## 18. Open questions
- Does Chapter or any advisor offer post-enrollment claims and paperwork support? Public sources did not confirm lifelong support.
- Is a flat-fee referral to licensed advisors compliant in the states that matter? [UNVERIFIED]
- Can claim tracking work from uploaded notices alone, or does it need account access?
- Is a widowed-spouse mode a separate product, given its legal and estate adjacency?
- Do 007 Parent Mail Desk, 036 Do It With Me and this product share one family-admin base, with Retirement Desk as the retiree-facing front end?

## Deep dive

Added 2026-11-01. New facts were read 2026-11-01; "idea file" means sections 10 to 12 above (read 2026-10-31). Search-summary means I saw the fact only in a search result summary, not on the page. Plan selection stays referred out to licensed brokers and SHIP counselors, with no money changing hands in v1.

### Competitor table
| Competitor | Link | What it does | Price (as published, with date read) | Funding or traction (sourced) | Gap this idea exploits |
|---|---|---|---|---|---|
| Chapter | [BusinessWire](https://www.businesswire.com/news/home/20260409159904/en/Chapter-Raises-%24100-Million-Series-E-to-Continue-Building-the-Trust-Layer-Between-Seniors-and-Technology-in-the-Age-of-AI) | Medicare navigation with licensed advisors and AI plan matching; says it will add "additional financial products for seniors" (idea file) | Free to users; carriers pay advisors (idea file) | Series E, $100M, April 2026; $3B valuation reported by Dealroom; over $100M ARR claimed for 2025 (idea file) | Plan choice. No case management, claims or appeals found. The nearest threat if it adds paperwork help |
| Healthpilot, Hella Health | [Healthpilot](https://www.thewealthmosaic.com/vendors/healthpilot/), [Hella Health](https://app.dealroom.co/companies/hella_health) | AI plan comparison and enrollment, sold through advisors or wealth managers | Not published | Healthpilot: Envestnet-backed, about 20,000 retirees (idea file) | Plan choice only |
| Medicare Vox (YC W20), careCycle (YC) | [Medicare Vox](https://www.ycombinator.com/companies/medicare-vox-fka-fair-square), [careCycle](https://www.ycombinator.com/companies/carecycle) | AI agents and voice AI sold to insurance agencies | Not published | YC-backed (idea file) | B2B, not retirees |
| AARP deadlines, NCOA, SHIP counselors | [AARP](https://www.aarp.org/medicare/medicare-deadlines-timetables/), [NCOA](https://www.ncoa.org/article/cobra-and-medicare-which-comes-first-and-why-it-matters-at-65/), [SHIBA Oregon](https://SHIBA.Oregon.gov/medicare-65/Documents/topten-medicare-myths.pdf) | Static rules and free human counseling | Free (idea file) | Not applicable | No personal timeline, documents, claims or drafts. The real price anchor is $0 |
| CMS Blue Button API (enabler) NEW | [bluebutton.cms.gov](https://bluebutton.cms.gov/) | "delivers Medicare Part A, B, and D data for over 60 million people with Medicare"; developer sandbox sign-up | No price on the page (read 2026-11-01); production access terms not shown | CMS program | A data rail, not a service. Could feed the claims tracker with the beneficiary's consent |
| Human billing and claims advocates NEW | [CoveredUSA](https://coveredusa.org/en/blog/medical-billing-advocate-when-to-hire), [Experian](https://www.experian.com/blogs/ask-experian/when-do-you-need-medical-billing-advocate/) | Review bills, draft appeals, negotiate | Hourly $75 to $350 (one page says $70 to over $500); flat $300 to $1,500 for one bill review or appeal; contingency 25% to 35% of savings (commercial pages, search-summary, 2026-11-01); BillFighter $39 a bill (idea file, no link recorded) | Not applicable | Human-priced; $149 for a year of case work undercuts a single advocate appeal |
| Retirement Countdown, CMS "What's covered" | [Countdown](https://apps.apple.com/us/app/retirement-countdown/id1645215938), [What's covered](https://apps.apple.com/us/app/whats-covered/id1444143600) | Countdown; coverage lookup | Free (idea file) | 12,848 and 362 App Store ratings (idea file) | Neither is a case manager |
| Licensed brokers and third-party marketing organizations (TPMOs) NEW | [definition](https://intuitionlabs.ai/articles/cms-tpmo-definition-regulations), [CY2026 CMS memo](https://medicareful.ritterim.com/documents/cms-memos/memo-agent-broker-compensation-and-training-and-testing-requirements-cy2026.pdf) | Plan sales, paid by carriers. CMS treats anyone "compensated to perform lead generation, marketing, sales, and enrollment-related functions" as a TPMO (search-summary) | Free to consumers | A court stayed parts of CMS's CY2025 compensation rule; a CY2027 proposal is in comment (search-summary) | The destination for plan choice. Taking referral money would make this product a TPMO, so v1 takes none |
| ChatGPT, Claude (Cowork, Duet), Gemini (tasks) | none | Build a timeline from a birth date; read uploaded notices | Subscription or free tier (idea file) | Platform scale | No persistent case, cited rule library, claims age tracking or family roles |

### Market sizing (bottom-up)
- Count: about 4.1M people turn 65 a year; secondary sources cluster at 4.1M to 4.2M for 2026 and I found no CMS or Census count (search, 2026-11-01) [ESTIMATE]. 40% have a complex transition (employer coverage or COBRA, a spouse, a pension) [ASSUMPTION] = 1.64M a year. Widowed spouses and adult children acting for parents are extra and not counted.
- Adoption at $149 once: conservative 0.5% (free SHIP, Chapter and AARP satisfy most) = 8,200 x $149 = $1.22M; optimistic 2% = 32,800 x $149 = $4.89M. Year-two $29 renewals add about $0.07M to $0.48M (30% to 50% renewing).
- Revenue at 100 / 1,000 / 10,000 customers: $14,900 / $149,000 / $1.49M. 10,000 customers is 0.6% of the 1.64M cohort in a year, between my two cases.
- Timing: the annual enrollment period closes 2026-12-07 and a 7-week build misses it. The first real season is January to March 2027 and then October 2027. Sales are seasonal.

### Unit economics
Per 12-month case, then per month. Prices from `research/LANDSCAPE.md` section 6. All [ESTIMATE].
- Documents: 40 x (OCR 2 pages x $0.004 + extraction $0.00055) = 40 x $0.00855 = $0.342 (OCR price [UNVERIFIED]). Re-plans: 5 x (8,000 x $2/1M + 2,000 x $10/1M = $0.036) = $0.18. Q&A: 40 x $0.011 = $0.44. Drafts: 10 x (6,000 x $2/1M + 1,500 x $10/1M = $0.027) = $0.27. Claim documents: 30 x $0.00855 = $0.257. Monthly reconciliations: 12 x $0.03 = $0.36. Model total $1.85.
- Other variable: 60 reminder texts x $0.008 = $0.48 [ASSUMPTION]; payment fee $149 x 2.9% + $0.30 = $4.62; infrastructure $65 a month x 12 / 100 active cases = $7.80 (or $0.78 at 1,000); advisor or SHIP review of the rule modules $500 once plus $300 each October, $800 / 500 cases = $1.60 [ASSUMPTION].
- Gross margin: $1.85 + $0.48 + $4.62 + $7.80 + $1.60 = $16.35 at 100 active cases, margin (149 - 16.35) / 149 = 89%, or $1.36 a month; at 1,000 active cases $9.33 and 94%. The file's 95% left out infrastructure and review. If a contractor handles 30 minutes of support per case at $25 an hour ($12.50), margin is 81% and 85%.
- Heavy user (a widowed spouse: 150 documents, 15 re-plans, 200 Q&A, 30 drafts, 200 claim documents, 12 double reconciliations, 150 texts): $1.28 + $0.54 + $2.20 + $0.81 + $1.71 + $0.72 + $1.20 = $8.46 of model and text cost, margin 85% after the fixed items. Pricing cap: 150 documents and 200 questions per case; a 50-document pack costs $19 [ASSUMPTION]. The real limit is support time, not model cost.

### First 100 customers
Funnel [ESTIMATE, and the file's own pass bars rather than observed rates]: visit to email 25%; email to paid 3%, so visit to paid 0.75%. Launch assumed early January 2027, so weeks 1 to 8 fall in the January to March window when new-plan claim problems appear (the LIFE-19 pattern).
| Week | Channel and action | Message and offer | Visitors | Paid (cumulative) |
|---|---|---|---|---|
| 1 | Free calendar generator live; answer open deadline threads in r/medicare (e.g. "Latest month to enroll in Medicare Part B without a penalty") where it answers the question, maker disclosed | "Your Medicare and COBRA dates in one file." Free calendar; $149 case, 30-day refund | 300 | 2 |
| 2 | r/retirement and r/SocialSecurity threads about notices (the LIFE-29 pattern); Bogleheads.org forum if rules allow | Same, plus a free notice checklist | 450 | 6 |
| 3 | Search pages that embed the calendar: "COBRA vs Medicare at 65", "Part B late enrollment penalty", "retiring at 62 health insurance" | Same | 600 | 10 |
| 4 | Adult-child threads (LIFE-55 pattern) in r/AgingParents and AgingCare forums: "my parent's plan is ending" | Free plan-exit checklist; a co-access invite for the child | 800 | 16 |
| 5 | Guide: "Medigap claims stuck in Processing" with a free call script | Claims tracker as the paid hook | 1,000 | 24 |
| 6 | Individual emails to SHIP counselors, libraries and licensed independent advisors offering the free calendar as a client handout; no payment either way | Unpaid referrals in both directions | 1,300 | 33 |
| 7 | Three-email sequence to captured addresses (days 0, 3, 10), each naming the reader's next deadline | "Your next deadline is X" | 1,600 | 45 |
| 8 | Widow(er) checklist page (the UND-19 pattern); review the funnel | Same | 2,000 | 60 |
Base case: 8,050 visitors, 2,010 emails, 60 paying by week 8, 100 around week 11 if weekly visitors keep growing about 13%. Growth loop after 100: a spouse or adult child joins the case, calendar subscriptions bring people back, and the $29 renewal prompts the next enrollment period.

### One-week validation test (under $50)
Timely: threads on the annual enrollment period are active until 2026-12-07.
- Build (days 1 to 2): a static calendar generator limited to what official pages state plainly: the 7-month initial enrollment window around the 65th birthday month, with a warning for birthdays on the 1st, and the note that COBRA does not extend it, each with a link to the official page. The page says "not yet reviewed by a licensed advisor or SHIP counselor; check medicare.gov". It recommends no plans and says plan choice is for SHIP or a licensed agent. Result page: the dates, plus a calendar (ICS) file for an email address.
- Offer (day 3): a one-screen description of the case manager, "launching in January", with a $149 pre-order (Stripe Payment Link, 100% refundable, said on the page) and an optional field "who is buying: me, my spouse, my parent, my client".
- Post (days 3 to 7): answer open deadline questions in r/medicare and r/retirement only where the calculator answers them, maker disclosed; no unsolicited messages; no accounts but my own.
- Budget: domain $12 [ASSUMPTION]; hosting, form, email list, analytics on free tiers $0; Stripe fees on 3 refunded pre-orders 3 x $4.62 = $13.86 [ASSUMPTION: fees not returned]. Total about $26, cap $50. A paid advisor hour is outside this budget; a SHIP counselor review is free but may not arrive within the week, and "reviewed by" goes on the page only after written approval.
- Valid if at least 300 unique visitors (fewer: extend one week).
- Pass: email capture at least 25% of visitors AND at least 2 pre-orders AND pre-orders at least 2.5% of captured emails. Fail: capture under 10%, or 0 pre-orders with at least 75 emails. Between: retest with a changed offer or a $79 tier. Also record the answers to "who is buying".

### Build brief (paste into a coding session)
- Product summary: A case manager for the retirement year. A short interview builds a cited timeline of Medicare, COBRA, Social Security and pension deadlines. A document inbox reads notices, a claims tracker flags claims stuck in "Processing", and the app drafts letters, appeals and call scripts. It never recommends a plan; plan choice is handed to SHIP counselors and licensed agents.
- MVP features (each testable):
  1. Interview of at most 12 questions that yields a timeline from about 30 rule modules, each citing an official URL and a "last verified" date (40 persona fixtures match expected dates).
  2. Document inbox by upload or forwarding address; classify the document type and extract dates, amounts, claim numbers, with confidence and a user confirmation step.
  3. Reminders by email, text and ICS at 30, 7 and 1 days (a time-travel test fires all).
  4. Drafts: COBRA election cover letter, Medicare redetermination request, call scripts; the user approves before download.
  5. Q&A that answers only from the user's facts and the curated rule corpus, with citations; with no source it says so and points to SHIP.
  6. Claims tracker: from uploaded notices, flag any claim older than 45 days in "Processing" and any Medicare-to-Medigap mismatch (seeded fixture).
  7. Family roles: invite a spouse or adult child as viewer or editor with an audit log.
  8. Plan-choice handoff screen: SHIP locator, Medicare.gov, and a reminder to check any agent's license with the state insurance department; no recommendation, no named brokers, no referral fee.
  9. Stripe: $149 for 12 months, $29 yearly renewal, 30-day refund.
  10. Optional Blue Button import of Medicare claims, sandbox first.
- Non-goals (v1): plan recommendations or enrollment on a user's behalf; any referral fee or commission; tax, investment or claiming-age advice; logging in to Medicare.gov or SSA for the user or storing their credentials; Medicaid eligibility; a mobile app.
- Core AI loop: interview and documents in -> rules engine in code produces windows with citations -> OCR then Haiku 5.5 ($0.10/$0.50) classifies and extracts into JSON -> the user confirms -> Sonnet 5.5 ($2/$10) answers questions and drafts only from confirmed facts and the rule corpus -> code compares claim lines and Sonnet explains mismatches -> checkpoints: a licensed advisor or SHIP counselor reviews rule modules before launch and each October; the user approves every draft; plan questions are handed off.
- Data model: Household, Person, Case, RuleModule (version, source URL, verified date, reviewer), Window (type, start, end, reason, citation), Document, ExtractedFact, Claim (source, date, amount, status, age), Draft, Reminder, Share (role), AuditLog.
- Integrations (docs): [CMS Blue Button](https://bluebutton.cms.gov/) (sandbox sign-up; production approval path not shown on the page, so [UNVERIFIED]), official rule pages at [medicare.gov](https://www.medicare.gov/) and [ssa.gov](https://www.ssa.gov/medicare), [Stripe](https://docs.stripe.com/), [Twilio SMS](https://www.twilio.com/docs/messaging), [Resend](https://resend.com/docs), [iCalendar RFC 5545](https://datatracker.ietf.org/doc/html/rfc5545), any OCR near $4 per 1,000 pages.
- Stack (about $80 to $120 a month): Next.js on Vercel, Supabase (auth, Postgres, storage with row-level security), Stripe, Resend, Twilio, Sentry; a rules module is plain TypeScript with unit tests.
- Evals: (1) 40 personas (working past 65 with employer coverage, COBRA after retirement, born on the 1st, delayed Part B, widowed): windows match hand-verified dates 40 of 40, checked by a licensed advisor or SHIP counselor. (2) 50 mixed documents (COBRA notices, Medicare Summary Notices, EOBs, pension forms, SSA letters): at least 95% of dates and amounts correct; unknown types flagged, not guessed. (3) 20 advice probes ("Which Medigap plan should I buy?", "Should I take Part B now?"): handoff and no recommendation, 20 of 20. (4) Claims fixture with 12 claims and 3 mismatches: flags exactly those 3 and the script cites their claim numbers. (5) 10 appeal drafts against the official checklist: all required elements, no fact absent from the user's documents.
- Build plan (7 weeks): W1 interview, rule schema, enrollment and COBRA modules with citations; W2 remaining modules and an admin page to re-verify rules; W3 document inbox, OCR, extraction, confirmation; W4 reminders, ICS, family roles; W5 drafts and cited Q&A; W6 claims tracker and Blue Button sandbox; W7 advisor or SHIP review, payments, soft launch.
- Key risks to test first: (1) willingness to pay next to free SHIP and Chapter (the test above); (2) a rule error that misses a window, so counselor review before launch; (3) the advice boundary and any TPMO exposure if money ever changes hands on referrals; (4) Blue Button production access; (5) the yearly rule refresh each autumn and a Chapter move into paperwork.

Notes for the main researcher: Open question 3 is partly answered: the CMS Blue Button API covers Part A, B and D data for 60M+ people with consent, so claims tracking need not depend on uploads, but production approval is unverified. Open question 2: CMS treats compensated lead generation as TPMO activity, so a paid broker referral is not a harmless extra; v1 should carry none. Human advocates charge $300 to $1,500 flat per appeal on commercial pages, which supports the $149 anchor, but SHIP is free, so I would keep WTP at 2.

## Red team
Skeptical-investor review on 2026-11-01 (full text: `research/RED_TEAM_B.md`). Verdict: **pass**.

**Top attacks (summarized):**
1. **The licensing answer is open.** Some states license fee-charging insurance consultants; a $149 product explaining COBRA, Medigap and claim notices could be read as consulting, which would trip kill criterion 3.
2. **The price anchor is $0.** SHIP counselors, AARP tools, state notebooks, Chapter's free advisors and general assistants already explain most of it.
3. **One-time, seasonal revenue and a slow first season.** The 7-week build misses the 2026-12-07 enrollment deadline, so the first season is January to March 2027, with rules to refresh every autumn.
What would change the red team's mind: the one-week test passing with adult children and widowed spouses as buyers, plus written answers from two launch-state insurance departments (or counsel) that a flat-fee, no-commission, no-recommendation product needs no consultant license.

**Response (main researcher):**
- Attacks 2 and 3 land. Distribution drops from 3 to 2 (one-time, seasonal, search dominated by medicare.gov, AARP and lead-gen sites) and solo feasibility from 3 to 2 (thirty rule modules refreshed yearly, a licensing check, mixed-notice extraction).
- Attack 1 is the gating risk; the insurance-department letter joins the validation plan before any build.
- Strongest use of this idea: as a module inside a broader family case file (with 006 and 007), not as a standalone company.
